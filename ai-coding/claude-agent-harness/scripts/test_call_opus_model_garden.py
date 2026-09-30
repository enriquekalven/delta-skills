"""Offline tests for the goal-driven harness. No network or GCP credentials needed.

Run: python3 -m unittest discover -s ai-coding/claude-agent-harness/scripts -p 'test_*.py'
"""

from __future__ import annotations

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from typing import Self

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


class _Stream:
    def __init__(self, message: SimpleNamespace) -> None:
        self._message = message

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        return None

    def get_final_message(self) -> SimpleNamespace:
        return self._message


class FakeClient:
    """Replays scripted model turns and records every request."""

    def __init__(self, script: list[SimpleNamespace]) -> None:
        self.script = list(script)
        self.requests: list[dict[str, Any]] = []
        self.messages = self

    def stream(self, **kwargs: Any) -> _Stream:
        self.requests.append({**kwargs, "messages": list(kwargs["messages"])})
        if not self.script:
            raise AssertionError("model called more times than scripted")
        return _Stream(self.script.pop(0))


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
            def stream(self, **kwargs: Any) -> _Stream:
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


if __name__ == "__main__":
    unittest.main()
