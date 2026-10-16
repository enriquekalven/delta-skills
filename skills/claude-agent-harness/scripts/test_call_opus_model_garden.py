"""Offline tests for the goal-driven harness. No network or GCP credentials needed.

Run: python3 -m unittest discover -s ai-coding/claude-agent-harness/scripts -p 'test_*.py'
"""

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from typing import Any
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import call_opus_model_garden as harness

PY = sys.executable
CHECK_ADD = f"{PY} -c \"import sys; sys.path.insert(0, '.'); import calc; assert calc.add(2, 3) == 5\""

BROKEN = "def add(a, b):\n    return a - b\n"
FIXED = "def add(a, b):\n    return a + b\n"


def tool(name: str, tool_id: str, **tool_input: Any) -> SimpleNamespace:
    return SimpleNamespace(type="tool_use", id=tool_id, name=name, input=tool_input)


def text(value: str) -> SimpleNamespace:
    return SimpleNamespace(type="text", text=value)


def reply(
    *blocks: SimpleNamespace, stop_reason: str = "tool_use", tokens: int = 10
) -> SimpleNamespace:
    return SimpleNamespace(
        content=list(blocks),
        stop_reason=stop_reason,
        usage=SimpleNamespace(input_tokens=tokens, output_tokens=tokens),
    )


class FakeClient:
    """Replays scripted model turns and records every messages.create request."""

    def __init__(self, script: list[SimpleNamespace]) -> None:
        self.script = list(script)
        self.requests: list[dict[str, Any]] = []
        self.messages = self

    def create(self, **kwargs: Any) -> SimpleNamespace:
        self.requests.append({**kwargs, "messages": list(kwargs["messages"])})
        if not self.script:
            raise AssertionError("model called more times than scripted")
        return self.script.pop(0)


class WorkspaceSandboxTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.join(self.tmp.name, "ws")
        os.makedirs(self.root)
        self.ws = harness.Workspace(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_rejects_absolute_paths(self) -> None:
        with self.assertRaises(harness.WorkspaceError):
            self.ws.write_file(os.path.join(self.tmp.name, "evil.py"), "x")

    def test_rejects_parent_traversal(self) -> None:
        with self.assertRaises(harness.WorkspaceError):
            self.ws.write_file("../evil.py", "x")
        self.assertFalse(os.path.exists(os.path.join(self.tmp.name, "evil.py")))

    def test_rejects_sibling_prefix_bypass(self) -> None:
        os.makedirs(self.root + "-malicious")
        with self.assertRaises(harness.WorkspaceError):
            self.ws.write_file("../ws-malicious/evil.py", "x")

    def test_rejects_symlink_escape(self) -> None:
        os.symlink(self.tmp.name, os.path.join(self.root, "link"))
        with self.assertRaises(harness.WorkspaceError):
            self.ws.write_file("link/evil.py", "x")

    def test_rejects_git_dir(self) -> None:
        with self.assertRaises(harness.WorkspaceError):
            self.ws.write_file(".git/config", "x")

    def test_blocks_sensitive_credential_and_env_files_while_allowing_env_example(self) -> None:
        for secret_file in (".env", ".env.production", "private.pem", "server.key", "gcp-credentials.json", "service-account-key.json"):
            full = os.path.join(self.root, secret_file)
            with open(full, "w", encoding="utf-8") as fh:
                fh.write("SECRET_TOKEN=supersecret123\n")
            with self.assertRaises(harness.WorkspaceError):
                self.ws.read_file(secret_file)
            with self.assertRaises(harness.WorkspaceError):
                self.ws.write_file(secret_file, "x")
        self.ws.write_file(".env.example", "API_KEY=your_key_here\n")
        self.assertIn("API_KEY=your_key_here", self.ws.read_file(".env.example"))
        listed = self.ws.list_files(".")
        self.assertIn(".env.example", listed)
        self.assertNotIn(".env.production", listed)
        grep_out = self.ws.grep_search("supersecret123", ".")
        self.assertEqual(grep_out, "(no matches)")

    def test_write_read_replace_round_trip(self) -> None:
        self.ws.write_file("pkg/calc.py", BROKEN)
        self.ws.replace_in_file("pkg/calc.py", "a - b", "a + b")
        self.assertEqual(self.ws.read_file("pkg/calc.py"), FIXED)
        self.assertEqual(self.ws.written, {os.path.join("pkg", "calc.py")})

    def test_replace_requires_unique_match(self) -> None:
        self.ws.write_file("a.py", "x = 1\nx = 1\n")
        with self.assertRaises(harness.WorkspaceError):
            self.ws.replace_in_file("a.py", "x = 1", "x = 2")

    def test_placeholder_scan_allows_security_todo_and_lowercase(self) -> None:
        self.ws.write_file(
            "ok.py", "# TODO(security): add rate limiting\ntodo_list = []\n"
        )
        self.ws.write_file("bad.py", "def f():\n    # TODO finish\n    pass\n")
        findings = self.ws.placeholder_findings()
        self.assertEqual(len(findings), 1)
        self.assertTrue(findings[0].startswith("bad.py:2"))

    def test_replace_in_file_on_large_file_over_200kb_does_not_corrupt(self) -> None:
        padding = "# " + ("x" * 98) + "\n"
        big_content = (padding * 2100) + "TARGET_VALUE = 1\n"
        self.assertGreater(len(big_content.encode("utf-8")), harness.MAX_READ_BYTES)
        self.ws.write_file("large.py", big_content)
        self.ws.replace_in_file("large.py", "TARGET_VALUE = 1", "TARGET_VALUE = 2")
        _, full_after = self.ws._read_full_text("large.py")
        self.assertTrue(full_after.endswith("TARGET_VALUE = 2\n"))
        self.assertNotIn("truncated", full_after)

    def test_read_file_line_slice_and_grep_search(self) -> None:
        content = "\n".join(f"line_{i} = {i}" for i in range(1, 21)) + "\n"
        self.ws.write_file("lines.py", content)
        sliced = self.ws.read_file("lines.py", start_line=5, end_line=7)
        self.assertEqual(sliced, "line_5 = 5\nline_6 = 6\nline_7 = 7\n")
        grep_out = self.ws.grep_search("line_15", rel_path=".")
        self.assertIn("lines.py:15: line_15 = 15", grep_out)

    def test_protected_files_block_writes_and_detect_tampering(self) -> None:
        test_path = os.path.join(self.root, "test_calc.py")
        with open(test_path, "w", encoding="utf-8") as handle:
            handle.write("assert True\n")
        protected_ws = harness.Workspace(self.root, protected_globs=("test_*.py",))
        with self.assertRaises(harness.WorkspaceError):
            protected_ws.write_file("test_calc.py", "assert True  # weakened\n")
        with self.assertRaises(harness.WorkspaceError):
            protected_ws.replace_in_file("test_calc.py", "True", "1 == 1")
        self.assertEqual(protected_ws.protected_violations(), [])
        with open(test_path, "w", encoding="utf-8") as handle:
            handle.write("assert False\n")
        self.assertEqual(len(protected_ws.protected_violations()), 1)


class VerifyCommandTests(unittest.TestCase):
    def test_rejects_shell_operators(self) -> None:
        with self.assertRaises(ValueError):
            harness.parse_verify_command("ruff check . && pytest")

    def test_reports_missing_binary(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            [result] = harness.run_verification(
                ["definitely-not-a-real-binary-xyz"], root, 10
            )
        self.assertEqual(result.exit_code, 127)
        self.assertFalse(result.passed)


class GoalLoopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _run(
        self, script: list[SimpleNamespace], **overrides: Any
    ) -> tuple[dict[str, Any], FakeClient]:
        client = FakeClient(script)
        config = harness.GoalConfig(
            goal="Implement calc.add",
            verify_commands=[CHECK_ADD],
            workspace=self.root,
            **overrides,
        )
        with redirect_stderr(io.StringIO()):
            report = harness.GoalHarness(client, config, log=lambda _m: None).run()
        return report, client

    def test_iterates_until_verification_passes(self) -> None:
        report, client = self._run(
            [
                reply(tool("write_file", "t1", path="calc.py", content=BROKEN)),
                reply(
                    tool("declare_goal_complete", "t2", summary="done")
                ),  # rejected: check fails
                reply(
                    tool(
                        "replace_in_file",
                        "t3",
                        path="calc.py",
                        old_text="a - b",
                        new_text="a + b",
                    )
                ),
                reply(
                    tool("declare_goal_complete", "t4", summary="fixed subtraction bug")
                ),
            ]
        )
        self.assertTrue(report["goal_met"])
        self.assertEqual(report["status"], "goal_met")
        self.assertEqual(report["turns"], 4)
        self.assertEqual(report["files_written"], ["calc.py"])
        self.assertEqual(report["summary"], "fixed subtraction bug")
        rejection = client.requests[2]["messages"][-1]["content"][0]
        self.assertEqual(rejection["tool_use_id"], "t2")
        self.assertIn("NOT accepted", rejection["content"])

    def test_first_request_carries_goal_contract_and_tools(self) -> None:
        _, client = self._run(
            [
                reply(tool("write_file", "t1", path="calc.py", content=FIXED)),
                reply(tool("declare_goal_complete", "t2", summary="ok")),
            ]
        )
        first = client.requests[0]
        self.assertEqual(first["model"], "claude-sonnet-5-5")
        self.assertEqual(harness.DEFAULT_REGION, "global")
        self.assertIn("<acceptance_criteria>", first["messages"][0]["content"])
        self.assertEqual(
            {t["name"] for t in first["tools"]}
            >= {"write_file", "declare_goal_complete"},
            True,
        )
        self.assertNotIn("temperature", first)

    def test_rejects_completion_with_placeholders(self) -> None:
        placeholder = FIXED + "# TODO handle overflow\n"
        report, _ = self._run(
            [
                reply(tool("write_file", "t1", path="calc.py", content=placeholder)),
                reply(tool("declare_goal_complete", "t2", summary="done")),
                reply(tool("write_file", "t3", path="calc.py", content=FIXED)),
                reply(tool("declare_goal_complete", "t4", summary="done")),
            ]
        )
        self.assertTrue(report["goal_met"])
        self.assertEqual(report["turns"], 4)

    def test_prose_only_turns_stall(self) -> None:
        report, client = self._run(
            [reply(text("I think it's done."), stop_reason="end_turn")] * 3
        )
        self.assertEqual(report["status"], "stalled")
        self.assertFalse(report["goal_met"])
        self.assertIn("not verified yet", client.requests[1]["messages"][-1]["content"])

    def test_truncated_tool_call_is_not_executed(self) -> None:
        report, client = self._run(
            [
                reply(
                    tool(
                        "write_file",
                        "t1",
                        path="calc.py",
                        content="def add(a, b):\n    ret",
                    ),
                    stop_reason="max_tokens",
                ),
                reply(tool("write_file", "t2", path="calc.py", content=FIXED)),
                reply(tool("declare_goal_complete", "t3", summary="ok")),
            ]
        )
        self.assertTrue(report["goal_met"])
        skipped = client.requests[1]["messages"][-1]["content"][0]
        self.assertTrue(skipped["is_error"])
        self.assertIn("Not executed", skipped["content"])

    def test_max_turns_reports_failing_acceptance(self) -> None:
        report, _ = self._run(
            [reply(tool("write_file", "t1", path="calc.py", content=BROKEN))],
            max_turns=1,
        )
        self.assertEqual(report["status"], "max_turns_reached")
        self.assertFalse(report["acceptance"][0]["passed"])

    def test_token_budget_stops_loop(self) -> None:
        report, _ = self._run(
            [reply(tool("list_files", "t1"), tokens=600)], token_budget=1000
        )
        self.assertEqual(report["status"], "token_budget_exhausted")
        self.assertEqual(report["turns"], 1)

    def test_api_error_is_reported(self) -> None:
        class Boom(FakeClient):
            def create(self, **kwargs: Any) -> SimpleNamespace:
                raise RuntimeError("503 overloaded")

        client = Boom([])
        config = harness.GoalConfig(
            goal="g", verify_commands=[CHECK_ADD], workspace=self.root
        )
        report = harness.GoalHarness(client, config, log=lambda _m: None).run()
        self.assertEqual(report["status"], "api_error")
        self.assertIn("503", report["error"])

    def test_requires_acceptance_commands(self) -> None:
        with self.assertRaises(ValueError):
            harness.GoalHarness(
                FakeClient([]),
                harness.GoalConfig(goal="g", verify_commands=[], workspace=self.root),
            )


class CliTests(unittest.TestCase):
    def test_cli_refuses_to_run_without_verify(self) -> None:
        with (
            tempfile.TemporaryDirectory() as root,
            redirect_stderr(io.StringIO()) as err,
        ):
            code = harness.main(
                ["--goal", "build it", "--workspace", root, "--project", "p"]
            )
        self.assertEqual(code, 1)
        self.assertIn("--verify", err.getvalue())

    def test_dry_run_does_not_claim_goal_met(self) -> None:
        with (
            tempfile.TemporaryDirectory() as root,
            redirect_stdout(io.StringIO()) as out,
        ):
            spec = os.path.join(root, "PRD.md")
            with open(spec, "w", encoding="utf-8") as handle:
                handle.write("# Spec\nadd(a, b) returns a + b\n")
            code = harness.main(
                [
                    "--spec",
                    spec,
                    "--workspace",
                    root,
                    "--project",
                    "p",
                    "--verify",
                    CHECK_ADD,
                    "--dry-run",
                ]
            )
        self.assertEqual(code, 0)
        report = json.loads(out.getvalue())
        self.assertEqual(report["status"], "dry_run_ok")
        self.assertFalse(report["goal_met"])
        self.assertEqual(report["verify_commands"], [CHECK_ADD])

    def test_report_creates_missing_parent_dir_in_both_modes(self) -> None:
        base = ["--goal", "build calc", "--project", "p", "--verify", CHECK_ADD]
        with tempfile.TemporaryDirectory() as root:
            dry_path = os.path.join(root, ".harness", "last_run_report.json")
            with redirect_stdout(io.StringIO()):
                code = harness.main(
                    base + ["--workspace", root, "--dry-run", "--report", dry_path]
                )
            self.assertEqual(code, 0)
            with open(dry_path, encoding="utf-8") as handle:
                self.assertEqual(json.load(handle)["status"], "dry_run_ok")

            live_path = os.path.join(root, "out", "live", "last_run_report.json")
            fake_anthropic = types.ModuleType("anthropic")
            fake_anthropic.AnthropicVertex = lambda **_kw: FakeClient(  # type: ignore[attr-defined]
                [
                    reply(tool("write_file", "t1", path="calc.py", content=FIXED)),
                    reply(tool("declare_goal_complete", "t2", summary="done")),
                ]
            )
            with (
                mock.patch.dict(sys.modules, {"anthropic": fake_anthropic}),
                redirect_stdout(io.StringIO()),
                redirect_stderr(io.StringIO()),
            ):
                code = harness.main(base + ["--workspace", root, "--report", live_path])
            self.assertEqual(code, 0)
            with open(live_path, encoding="utf-8") as handle:
                self.assertTrue(json.load(handle)["goal_met"])

    def test_review_target_must_be_inside_workspace(self) -> None:
        with (
            tempfile.TemporaryDirectory() as root,
            tempfile.NamedTemporaryFile(suffix=".py") as outside,
        ):
            args = harness.build_arg_parser().parse_args(
                ["--review", outside.name, "--workspace", root]
            )
            with self.assertRaises(ValueError):
                harness.build_goal_text(args, root)

    def test_review_target_must_exist(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            missing = os.path.join(root, "nonexistent.py")
            args = harness.build_arg_parser().parse_args(
                ["--review", missing, "--workspace", root]
            )
            with self.assertRaises(FileNotFoundError):
                harness.build_goal_text(args, root)

    def test_list_files_omits_symlinks_escaping_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as outer:
            ws_dir = os.path.join(outer, "ws")
            os.makedirs(ws_dir)
            secret = os.path.join(outer, "secret.txt")
            with open(secret, "w", encoding="utf-8") as handle:
                handle.write("secret")
            os.symlink(secret, os.path.join(ws_dir, "escape.txt"))
            ws = harness.Workspace(ws_dir)
            ws.write_file("safe.py", "x = 1\n")
            self.assertEqual(ws.list_files("."), "safe.py")

    def test_tracked_review_file_is_checked_for_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            target = os.path.join(root, "calc.py")
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(FIXED + "# TODO remove before prod\n")
            client = FakeClient(
                [
                    reply(tool("declare_goal_complete", "t1", summary="looks good")),
                    reply(tool("write_file", "t2", path="calc.py", content=FIXED)),
                    reply(tool("declare_goal_complete", "t3", summary="cleaned up")),
                ]
            )
            config = harness.GoalConfig(
                goal="Harden calc.py",
                verify_commands=[CHECK_ADD],
                workspace=root,
                tracked_files=("calc.py",),
            )
            report = harness.GoalHarness(client, config, log=lambda _m: None).run()
            self.assertTrue(report["goal_met"])
            self.assertEqual(report["turns"], 3)

    def test_rejects_non_positive_budgets(self) -> None:
        with tempfile.TemporaryDirectory() as root, self.assertRaises(ValueError):
            harness.GoalHarness(
                FakeClient([]),
                harness.GoalConfig(
                    goal="g",
                    verify_commands=[CHECK_ADD],
                    workspace=root,
                    max_turns=0,
                ),
            )


if __name__ == "__main__":
    unittest.main()
