#!/usr/bin/env python3
"""Claude Agent Harness: goal-driven coding loop on Vertex AI Model Garden.

The harness always runs in goal mode. It never makes a single completion call.
Claude (default ``claude-sonnet-5-5`` in region ``global``) runs as a tool-using
agent inside a sandboxed workspace and keeps iterating until the Goal Contract
is met:

* every acceptance command passed with ``--verify`` exits with code 0, and
* the model calls ``declare_goal_complete``, after which the harness re-runs
  all acceptance commands and scans the files it wrote for placeholders.

The model can only list, read, and write files inside the workspace and run
the acceptance commands you configured. It cannot run arbitrary shell commands.

Exit codes: 0 = goal met, 2 = goal not met (turn/token budget or stall),
1 = setup or API error. A JSON report is always printed to stdout.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

DEFAULT_MODEL = os.environ.get("CLAUDE_MODEL_NAME", "claude-sonnet-5-5")
DEFAULT_REGION = os.environ.get("CLOUD_ML_REGION", "global")

IGNORED_DIRS = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".tox",
    }
)
MAX_READ_BYTES = 200_000
MAX_WRITE_BYTES = 1_000_000
MAX_SPEC_BYTES = 400_000
MAX_TOOL_OUTPUT_CHARS = 30_000
MAX_LIST_ENTRIES = 500
SHELL_OPERATORS = frozenset({"&&", "||", "|", ";", ">", ">>", "<", "&"})

# Uppercase markers only, so ordinary words like "todo list" don't count.
# TODO(security) is allowed because it documents a deliberately deferred control.
_PLACEHOLDER_MARKERS = re.compile(r"\b(?:TODO|FIXME|XXX)\b(?!\(security\))")
_PLACEHOLDER_PHRASES = re.compile(
    r"implement (?:this|me|later|here)|rest of (?:the )?(?:code|implementation)|\.\.\. ?existing code",
    re.IGNORECASE,
)

SYSTEM_PROMPT = """You are a principal software engineer working inside a goal-driven harness. \
You act only through the provided tools, inside a sandboxed workspace.

Operating rules:
1. This is a goal, not a single answer. Keep iterating until every acceptance command passes. \
Never end a turn with prose alone while the goal is unmet.
2. Read before you write. Inspect the relevant files and follow the project's existing conventions, \
dependencies, and layout.
3. Write complete, working code. No placeholders, stubs, TODO/FIXME markers, or elided sections. \
A TODO(security) note that explains a deliberately deferred control is allowed.
4. Use replace_in_file for targeted edits to existing files. Use write_file for new files or full \
rewrites. Keep each write under 1 MB.
5. Never hardcode secrets or credentials. Validate input at trust boundaries. Use parameterized \
queries. Never bind test servers to 0.0.0.0.
6. When verification fails, read the output, find the root cause, and fix it. Never weaken, skip, \
or delete tests or acceptance checks to make them pass.
7. Once run_verification passes, call declare_goal_complete with a short summary of what changed and why."""

TOOLS: list[dict[str, Any]] = [
    {
        "name": "list_files",
        "description": "List files under a workspace directory as relative paths. Skips VCS, virtualenv, and cache directories.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory relative to the workspace root. Defaults to '.'.",
                }
            },
            "required": [],
        },
    },
    {
        "name": "read_file",
        "description": "Read a UTF-8 text file from the workspace.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "File path relative to the workspace root.",
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Create or overwrite a UTF-8 text file in the workspace, creating parent directories as needed.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "File path relative to the workspace root.",
                },
                "content": {"type": "string", "description": "Complete file content."},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "replace_in_file",
        "description": "Replace exactly one occurrence of old_text with new_text in a workspace file. Fails unless old_text occurs exactly once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_text": {"type": "string"},
                "new_text": {"type": "string"},
            },
            "required": ["path", "old_text", "new_text"],
        },
    },
    {
        "name": "run_verification",
        "description": "Run every acceptance command in the Goal Contract from the workspace root. Returns each command's exit code and the tail of its output.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "declare_goal_complete",
        "description": "Claim the goal is met. The harness re-runs every acceptance command and scans the files you wrote for placeholders. Completion is accepted only if all checks pass.",
        "input_schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string", "description": "What changed and why."}
            },
            "required": ["summary"],
        },
    },
]


class WorkspaceError(Exception):
    """Raised when a tool request violates the workspace sandbox or limits."""


def _truncate(
    text: str, limit: int = MAX_TOOL_OUTPUT_CHARS, keep_tail: bool = False
) -> str:
    if len(text) <= limit:
        return text
    omitted = len(text) - limit
    if keep_tail:
        return f"[... {omitted} chars omitted ...]\n" + text[-limit:]
    return text[:limit] + f"\n[... {omitted} chars omitted ...]"


class Workspace:
    """Tool-facing file access confined to a single root directory."""

    def __init__(self, root: str) -> None:
        self.root = os.path.realpath(root)
        self.written: set[str] = set()

    def resolve(self, rel_path: Any) -> str:
        if not isinstance(rel_path, str) or not rel_path.strip() or "\x00" in rel_path:
            raise WorkspaceError("path must be a non-empty string")
        if os.path.isabs(rel_path):
            raise WorkspaceError(f"absolute paths are not allowed: {rel_path}")
        candidate = os.path.realpath(os.path.join(self.root, rel_path))
        if candidate != self.root and not candidate.startswith(self.root + os.sep):
            raise WorkspaceError(f"path escapes the workspace: {rel_path}")
        if ".git" in os.path.relpath(candidate, self.root).split(os.sep):
            raise WorkspaceError("access inside .git is not allowed")
        return candidate

    def relative(self, abs_path: str) -> str:
        return os.path.relpath(abs_path, self.root)

    def _is_contained(self, path: str) -> bool:
        real = os.path.realpath(path)
        return real == self.root or real.startswith(self.root + os.sep)

    def list_files(self, rel_dir: str = ".") -> str:
        base = self.resolve(rel_dir or ".")
        if not os.path.isdir(base):
            raise WorkspaceError(f"not a directory: {rel_dir}")
        entries: list[str] = []
        for current, dirs, files in os.walk(base):
            dirs[:] = sorted(
                d
                for d in dirs
                if d not in IGNORED_DIRS
                and self._is_contained(os.path.join(current, d))
            )
            for name in sorted(files):
                full = os.path.join(current, name)
                if not self._is_contained(full):
                    continue
                entries.append(self.relative(full))
                if len(entries) >= MAX_LIST_ENTRIES:
                    return (
                        "\n".join(entries)
                        + f"\n[... listing capped at {MAX_LIST_ENTRIES} entries ...]"
                    )
        return "\n".join(entries) if entries else "(empty)"

    def read_file(self, rel_path: Any) -> str:
        path = self.resolve(rel_path)
        if not os.path.isfile(path):
            raise WorkspaceError(f"file not found: {rel_path}")
        size = os.path.getsize(path)
        with open(path, "rb") as handle:
            data = handle.read(MAX_READ_BYTES)
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise WorkspaceError(f"{rel_path} is binary or not UTF-8") from exc
        if size > MAX_READ_BYTES:
            text += f"\n[... truncated: file is {size} bytes, showing first {MAX_READ_BYTES} ...]"
        return text

    def write_file(self, rel_path: Any, content: Any) -> str:
        if not isinstance(content, str):
            raise WorkspaceError("content must be a string")
        encoded = content.encode("utf-8")
        if len(encoded) > MAX_WRITE_BYTES:
            raise WorkspaceError(
                f"content exceeds {MAX_WRITE_BYTES} bytes; split the file"
            )
        path = self.resolve(rel_path)
        if os.path.isdir(path):
            raise WorkspaceError(f"{rel_path} is a directory")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as handle:
            handle.write(encoded)
        self.written.add(self.relative(path))
        return f"wrote {self.relative(path)} ({len(encoded)} bytes)"

    def replace_in_file(self, rel_path: Any, old_text: Any, new_text: Any) -> str:
        if (
            not isinstance(old_text, str)
            or not old_text
            or not isinstance(new_text, str)
        ):
            raise WorkspaceError(
                "old_text must be a non-empty string and new_text a string"
            )
        current = self.read_file(rel_path)
        count = current.count(old_text)
        if count != 1:
            raise WorkspaceError(
                f"old_text must occur exactly once in {rel_path}; found {count}"
            )
        return self.write_file(rel_path, current.replace(old_text, new_text, 1))

    def placeholder_findings(self) -> list[str]:
        findings: list[str] = []
        for rel in sorted(self.written):
            try:
                text = self.read_file(rel)
            except WorkspaceError:
                continue
            for lineno, line in enumerate(text.splitlines(), 1):
                if _PLACEHOLDER_MARKERS.search(line) or _PLACEHOLDER_PHRASES.search(
                    line
                ):
                    findings.append(f"{rel}:{lineno}: {line.strip()[:160]}")
        return findings


@dataclass
class VerifyResult:
    command: str
    exit_code: int
    passed: bool
    output_tail: str


def parse_verify_command(command: str) -> list[str]:
    """Split an acceptance command into argv. Shell operators are rejected."""
    argv = shlex.split(command)
    if not argv:
        raise ValueError("empty --verify command")
    operators = SHELL_OPERATORS.intersection(argv)
    if operators:
        raise ValueError(
            f"--verify {command!r} uses shell operators {sorted(operators)}; "
            "pass each command as its own --verify flag"
        )
    return argv


def run_verification(commands: list[str], cwd: str, timeout: int) -> list[VerifyResult]:
    results: list[VerifyResult] = []
    # Python checks cached bytecode by source mtime and size, so a same-size edit made
    # within the same second could run stale code. Don't write .pyc files during verification.
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    for command in commands:
        argv = parse_verify_command(command)
        try:
            proc = subprocess.run(
                argv,
                cwd=cwd,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
            )
            code, output = proc.returncode, (proc.stdout or "") + (proc.stderr or "")
        except FileNotFoundError:
            code, output = 127, f"command not found: {argv[0]}"
        except subprocess.TimeoutExpired:
            code, output = 124, f"timed out after {timeout}s"
        results.append(
            VerifyResult(
                command, code, code == 0, _truncate(output, 6_000, keep_tail=True)
            )
        )
    return results


def format_verification(results: list[VerifyResult]) -> str:
    lines = []
    for index, result in enumerate(results, 1):
        status = "PASS" if result.passed else f"FAIL (exit {result.exit_code})"
        lines.append(
            f"[{index}] {status}: {result.command}\n{result.output_tail}".rstrip()
        )
    return "\n\n".join(lines)


@dataclass
class GoalConfig:
    goal: str
    verify_commands: list[str]
    workspace: str
    model: str = DEFAULT_MODEL
    max_turns: int = 40
    max_tokens: int = 16_000
    token_budget: int = 2_000_000
    verify_timeout: int = 600
    temperature: float | None = None
    max_idle_turns: int = 3
    tracked_files: tuple[str, ...] = ()


@dataclass
class GoalState:
    status: str = "running"
    turns: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    verification_runs: int = 0
    idle_turns: int = 0
    summary: str = ""
    error: str = ""
    last_verification: list[VerifyResult] = field(default_factory=list)


def build_initial_message(goal: str, verify_commands: list[str], snapshot: str) -> str:
    criteria = "\n".join(
        f"{i}. `{cmd}` exits with code 0" for i, cmd in enumerate(verify_commands, 1)
    )
    return (
        f"<goal>\n{goal}\n</goal>\n\n"
        "<acceptance_criteria>\nThe goal is met only when every command below passes, run from the workspace root:\n"
        f"{criteria}\n</acceptance_criteria>\n\n"
        f"<workspace_snapshot>\n{snapshot}\n</workspace_snapshot>\n\n"
        "Work iteratively: inspect the relevant files, make changes with the file tools, run verification, "
        "fix any failures, and repeat. Call declare_goal_complete only after run_verification passes."
    )


class GoalHarness:
    """Runs the tool-use loop until the Goal Contract is met or a budget runs out."""

    def __init__(
        self, client: Any, config: GoalConfig, log: Callable[[str], None] | None = None
    ) -> None:
        if not config.verify_commands:
            raise ValueError(
                "goal mode requires at least one acceptance command (--verify)"
            )
        if (
            config.max_turns < 1
            or config.max_tokens < 1
            or config.token_budget < 1
            or config.verify_timeout < 1
        ):
            raise ValueError(
                "max_turns, max_tokens, token_budget, and verify_timeout must be >= 1"
            )
        for command in config.verify_commands:
            parse_verify_command(command)
        self.client = client
        self.config = config
        self.workspace = Workspace(config.workspace)
        for rel in config.tracked_files:
            resolved = self.workspace.resolve(rel)
            self.workspace.written.add(self.workspace.relative(resolved))
        self.state = GoalState()
        self.log = log or (lambda message: print(message, file=sys.stderr))

    def _call_model(self, messages: list[dict[str, Any]]) -> Any:
        kwargs: dict[str, Any] = {
            "max_tokens": self.config.max_tokens,
            "messages": messages,
            "model": self.config.model,
            "system": SYSTEM_PROMPT,
            "tools": TOOLS,
        }
        if self.config.temperature is not None:
            kwargs["temperature"] = self.config.temperature
        return self.client.messages.create(**kwargs)

    def _verify(self) -> list[VerifyResult]:
        self.state.verification_runs += 1
        results = run_verification(
            self.config.verify_commands, self.workspace.root, self.config.verify_timeout
        )
        self.state.last_verification = results
        passed = sum(r.passed for r in results)
        self.log(
            f"[goal] verification {self.state.verification_runs}: {passed}/{len(results)} passing"
        )
        return results

    def _dispatch(self, name: str, args: dict[str, Any]) -> tuple[str, bool]:
        ws = self.workspace
        try:
            if name == "list_files":
                return ws.list_files(args.get("path") or "."), False
            if name == "read_file":
                return _truncate(ws.read_file(args.get("path"))), False
            if name == "write_file":
                result = ws.write_file(args.get("path"), args.get("content"))
                self.log(f"[goal] {result}")
                return result, False
            if name == "replace_in_file":
                result = ws.replace_in_file(
                    args.get("path"), args.get("old_text"), args.get("new_text")
                )
                self.log(f"[goal] {result}")
                return result, False
            if name == "run_verification":
                return format_verification(self._verify()), False
            if name == "declare_goal_complete":
                return self._judge_completion(str(args.get("summary", ""))), False
            return f"unknown tool: {name}", True
        except (WorkspaceError, OSError, ValueError) as exc:
            return f"error: {exc}", True

    def _judge_completion(self, summary: str) -> str:
        results = self._verify()
        placeholders = self.workspace.placeholder_findings()
        if all(r.passed for r in results) and not placeholders:
            self.state.status = "goal_met"
            self.state.summary = summary
            return "Goal accepted: all acceptance commands pass and no placeholders were found."
        problems = ["Goal NOT accepted. Keep working."]
        if not all(r.passed for r in results):
            problems.append(
                "Failing acceptance commands:\n"
                + format_verification([r for r in results if not r.passed])
            )
        if placeholders:
            problems.append(
                "Placeholder markers in files you wrote:\n"
                + "\n".join(placeholders[:50])
            )
        return "\n\n".join(problems)

    def run(self) -> dict[str, Any]:
        cfg, state = self.config, self.state
        snapshot = self.workspace.list_files(".")
        messages: list[dict[str, Any]] = [
            {
                "role": "user",
                "content": build_initial_message(
                    cfg.goal, cfg.verify_commands, snapshot
                ),
            }
        ]
        while state.status == "running":
            if state.turns >= cfg.max_turns:
                state.status = "max_turns_reached"
                break
            if state.input_tokens + state.output_tokens >= cfg.token_budget:
                state.status = "token_budget_exhausted"
                break
            state.turns += 1
            self.log(f"[goal] turn {state.turns}/{cfg.max_turns} -> {cfg.model}")
            try:
                message = self._call_model(messages)
            except Exception as exc:  # noqa: BLE001 - any SDK/transport error is reported, not raised
                state.status = "api_error"
                state.error = f"{type(exc).__name__}: {exc}"
                break
            usage = getattr(message, "usage", None)
            state.input_tokens += int(getattr(usage, "input_tokens", 0) or 0)
            state.output_tokens += int(getattr(usage, "output_tokens", 0) or 0)
            stop_reason = getattr(message, "stop_reason", None)
            content = list(getattr(message, "content", []) or [])
            messages.append({"role": "assistant", "content": content})

            if stop_reason == "refusal":
                state.status = "model_refused"
                break

            tool_uses = [
                block for block in content if getattr(block, "type", "") == "tool_use"
            ]
            if not tool_uses:
                state.idle_turns += 1
                if state.idle_turns >= cfg.max_idle_turns:
                    state.status = "stalled"
                    break
                nudge = (
                    "Your response was cut off at the token limit. Continue with smaller tool calls."
                    if stop_reason == "max_tokens"
                    else "The goal is not verified yet. Keep working with the tools and call "
                    "declare_goal_complete once run_verification passes."
                )
                messages.append({"role": "user", "content": nudge})
                continue
            state.idle_turns = 0

            results: list[dict[str, Any]] = []
            for block in tool_uses:
                if stop_reason == "max_tokens":
                    # The tool input may be truncated (for example, half a file). Never execute it.
                    output, is_error = (
                        "Not executed: this call was cut off at the token limit. Resend it in smaller pieces.",
                        True,
                    )
                else:
                    raw_input = getattr(block, "input", {})
                    output, is_error = self._dispatch(
                        block.name, raw_input if isinstance(raw_input, dict) else {}
                    )
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": output,
                        "is_error": is_error,
                    }
                )
            messages.append({"role": "user", "content": results})

        if state.status != "goal_met" and state.status != "api_error":
            self._verify()
        return self.report()

    def report(self) -> dict[str, Any]:
        state = self.state
        return {
            "status": state.status,
            "goal_met": state.status == "goal_met",
            "model": self.config.model,
            "workspace": self.workspace.root,
            "turns": state.turns,
            "verification_runs": state.verification_runs,
            "usage": {
                "input_tokens": state.input_tokens,
                "output_tokens": state.output_tokens,
            },
            "files_written": sorted(self.workspace.written),
            "acceptance": [
                {"command": r.command, "passed": r.passed, "exit_code": r.exit_code}
                for r in state.last_verification
            ],
            "summary": state.summary,
            "error": state.error,
        }


def discover_project_id() -> str | None:
    """Resolve the GCP project from the environment or gcloud config."""
    project_id = (
        os.environ.get("ANTHROPIC_VERTEX_PROJECT_ID")
        or os.environ.get("GOOGLE_CLOUD_PROJECT")
        or os.environ.get("CLOUD_ML_PROJECT_ID")
        or os.environ.get("GCP_PROJECT")
    )
    if project_id:
        return project_id.strip()
    try:
        res = subprocess.run(
            ["gcloud", "config", "get-value", "project"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    value = res.stdout.strip()
    return value if res.returncode == 0 and value and "(unset)" not in value else None


def _read_text(path: str, limit: int = MAX_SPEC_BYTES) -> str:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"file not found: {path}")
    if os.path.getsize(path) > limit:
        raise ValueError(
            f"{path} exceeds {limit} bytes; reference it from the workspace instead"
        )
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def build_goal_text(args: argparse.Namespace, workspace: str) -> str:
    objective = (
        args.goal
        or args.prompt
        or (" ".join(args.prompt_pos) if args.prompt_pos else "")
    )
    if args.file:
        objective = (objective + "\n\n" if objective else "") + _read_text(args.file)
    if not objective and not args.spec and not args.review and not sys.stdin.isatty():
        objective = sys.stdin.read()
    parts = [objective.strip()] if objective.strip() else []
    if args.spec:
        if not parts:
            parts.append(
                "Implement the specification below completely inside the workspace."
            )
        parts.append(
            f'<specification path="{args.spec}">\n{_read_text(args.spec)}\n</specification>'
        )
    if args.review:
        review_abs = os.path.realpath(args.review)
        root = os.path.realpath(workspace)
        if not review_abs.startswith(root + os.sep):
            raise ValueError(
                f"--review file must be inside the workspace: {args.review}"
            )
        if not os.path.isfile(review_abs):
            raise FileNotFoundError(f"--review file not found: {args.review}")
        if not parts:
            parts.append(
                "Review and harden the file below in place for security, reliability, and correctness."
            )
        parts.append(
            f"Target file (read it with read_file): {os.path.relpath(review_abs, root)}"
        )
    if not parts:
        raise ValueError(
            "no goal provided: use --goal, --spec, --review, --prompt, --file, or stdin"
        )
    return "\n\n".join(parts)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Goal-driven Claude coding harness on Vertex AI Model Garden (never a single call)."
    )
    parser.add_argument("prompt_pos", nargs="*", help="Optional goal text")
    parser.add_argument("-g", "--goal", help="Objective of the Goal Contract")
    parser.add_argument("-p", "--prompt", help="Alias for --goal")
    parser.add_argument(
        "-s",
        "--spec",
        help="Specification or PRD file to implement (inlined into the goal)",
    )
    parser.add_argument(
        "-r", "--review", help="Workspace file to review and harden in place"
    )
    parser.add_argument("-f", "--file", help="Read additional goal text from a file")
    parser.add_argument(
        "-w",
        "--workspace",
        "-o",
        "--output-dir",
        dest="workspace",
        default=".",
        help="Sandbox root the agent may read and write (default: current directory)",
    )
    parser.add_argument(
        "-v",
        "--verify",
        action="append",
        default=[],
        metavar="CMD",
        help="Acceptance command that must exit 0. Repeatable. Required.",
    )
    parser.add_argument(
        "--max-turns", type=int, default=40, help="Max model turns (default: 40)"
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16_000,
        help="Max output tokens per turn (default: 16000)",
    )
    parser.add_argument(
        "--token-budget",
        type=int,
        default=2_000_000,
        help="Stop after this many input+output tokens in total (default: 2,000,000)",
    )
    parser.add_argument(
        "--verify-timeout",
        type=int,
        default=600,
        help="Seconds per acceptance command (default: 600)",
    )
    parser.add_argument(
        "--temperature", type=float, default=None, help="Optional sampling temperature"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=4,
        help="SDK retries for transient API errors (default: 4)",
    )
    parser.add_argument("--project", help="GCP project ID (default: auto-detected)")
    parser.add_argument(
        "--region",
        default=DEFAULT_REGION,
        help="Vertex AI region (default: global or CLOUD_ML_REGION)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model Garden model ID (default: claude-sonnet-5-5 or CLAUDE_MODEL_NAME)",
    )
    parser.add_argument("--report", help="Also write the JSON report to this path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    try:
        os.makedirs(args.workspace, exist_ok=True)
        goal = build_goal_text(args, args.workspace)
        if not args.verify:
            raise ValueError(
                "goal mode needs at least one --verify acceptance command, "
                "e.g. --verify 'python3 -m pytest -q' --verify 'ruff check .'"
            )
        for command in args.verify:
            parse_verify_command(command)
        tracked: tuple[str, ...] = ()
        if args.review:
            root = os.path.realpath(args.workspace)
            tracked = (os.path.relpath(os.path.realpath(args.review), root),)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    project_id = args.project or discover_project_id()
    if not project_id:
        print(
            "Error: set GOOGLE_CLOUD_PROJECT or pass --project <id>.", file=sys.stderr
        )
        return 1
    try:
        from anthropic import AnthropicVertex  # type: ignore[import-not-found]
    except ImportError:
        print(
            "Error: install the Vertex extra: pip install 'anthropic[vertex]'",
            file=sys.stderr,
        )
        return 1

    client = AnthropicVertex(
        region=args.region, project_id=project_id, max_retries=args.max_retries
    )
    config = GoalConfig(
        goal=goal,
        verify_commands=list(args.verify),
        workspace=args.workspace,
        model=args.model,
        max_turns=args.max_turns,
        max_tokens=args.max_tokens,
        token_budget=args.token_budget,
        verify_timeout=args.verify_timeout,
        temperature=args.temperature,
        tracked_files=tracked,
    )
    report = GoalHarness(client, config).run()
    report.update({"project": project_id, "region": args.region})
    error = report["error"]
    if (
        "DefaultCredentialsError" in error or "RefreshError" in error
    ) and "application-default login" not in error:
        report["error"] += " | Run: gcloud auth application-default login"

    rendered = json.dumps(report, indent=2)
    print(rendered)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as handle:
            handle.write(rendered + "\n")
    if report["goal_met"]:
        return 0
    return 1 if report["status"] == "api_error" else 2


if __name__ == "__main__":
    sys.exit(main())
