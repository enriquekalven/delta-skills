---
name: claude-agent-harness
description: >
  Goal-driven coding harness that turns specs, PRDs, or engineering prompts into verified code, using Anthropic Claude (default `claude-sonnet-5-5` in region `global`) on Vertex AI Model Garden.
  Always runs in goal mode: Claude works through sandboxed file tools and keeps iterating until every acceptance command passes. It never makes a single completion call.
  Trigger when asked to "build code from this spec", "implement this PRD", "use claude harness", "run the harness as a goal", or "delegate implementation to Claude on Vertex".
  Do NOT trigger for quick edits the current agent can make directly, or when the user wants a design discussion rather than code.
metadata:
  author: cloud-gtm@
  version: '3.2'
---

# Claude Agent Harness (Goal Mode — `claude-agent-harness`)

You delegate implementation work to Claude on **Vertex AI Model Garden** through a **goal loop**, never through a single API call.

Every run is bound by a **Goal Contract**: an objective plus executable acceptance commands. The harness gives Claude sandboxed tools (`list_files`, `read_file`, `write_file`, `replace_in_file`, `run_verification`, `declare_goal_complete`). Claude keeps iterating until every acceptance command exits `0`. The harness **re-runs verification itself** before it accepts completion, and rejects completions whose files contain placeholder markers.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 2 Core Build & Sprints 1–4 (Weeks 3–10):** Autonomous goal-loop build per feature ticket |
| **Reads (Inputs)** | `docs/PRD.md`, `docs/TDD.md` (passed via repeatable `--spec` flags) |
| **Writes (Outputs)** | Verified `src/`, `tests/`, and `.harness/last_run_report.json` (`status: "goal_met"`) |
| **Primary CLI Command** | `python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py --spec docs/PRD.md --spec docs/TDD.md --workspace . --verify "python3 -m pytest -q" --dry-run` |

---

## Non-Negotiable Rules

1. **Always goal mode.** Never call the model once and paste its output. The script has no single-shot mode, so don't build one around it.
2. **No Goal Contract, no run.** Every run needs at least one `--verify` command. If you can't write an executable acceptance check, clarify the requirement with the user first.
3. **Don't stop until the goal is met or the budget runs out.** You, the host agent, must not end your turn on a partial result. Re-run or fix directly until acceptance passes, or report honestly why it can't (see Phase 4).
4. **Trust but verify.** Re-run the acceptance commands yourself after the harness exits, and review the diff. The harness blocks placeholders but can't tell whether a test was weakened.
5. **Long runs:** for multi-hour work, suggest the user start the task with **`/goal`** so the session keeps going until the contract is met.

---

## Phase 1: Write the Goal Contract

Read the spec (`docs/PRD.md`, `docs/TDD.md`, or the user's prompt) and write the contract in your plan before running anything:

| Field | Content |
|---|---|
| **Objective** | One paragraph: what must exist when the goal is met |
| **Workspace** | The directory Claude may read and write (the sandbox root) |
| **Acceptance commands** | 2–5 commands mapped to the 4 verification tiers (below). Each is its own `--verify` |
| **Budget** | `--max-turns` (default 40) and `--token-budget` (default 2M tokens) |

**Map the 4 verification tiers to the project's stack:**

| Tier | Python example | TypeScript example |
|---|---|---|
| 1. Syntax | `python3 -m compileall -q src` | `npx tsc --noEmit` |
| 2. Lint | `ruff check .` | `npx eslint .` |
| 3. Types | `mypy --strict src` | *(covered by tsc)* |
| 4. Tests | `python3 -m pytest -q` | `npm test --silent` |

> [!IMPORTANT]
> Acceptance commands run **without a shell**. `&&`, pipes and redirects are rejected. Pass each check as its own `--verify` flag. Acceptance tests should exist **before** the run, written by you or the user from the spec, so Claude can't define its own finish line.

---

## Phase 2: Run the Goal Loop

```bash
python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py \
  --spec docs/PRD.md \
  --spec docs/TDD.md \
  --workspace . \
  --verify "python3 -m compileall -q src" \
  --verify "ruff check src tests" \
  --verify "mypy --strict src" \
  --verify "python3 -m pytest -q" \
  --report .harness/last_run_report.json
```

Other entry points:
- `--goal "<objective>"`: prompt-driven goal instead of or alongside `--spec`.
- `--review src/module.py --goal "Harden for input validation and timeouts"`: harden a workspace file in place until acceptance passes.
- `--dry-run`: validate the Goal Contract, spec files, and `--verify` command parsing offline before invoking Vertex AI. It reports `status: "dry_run_ok"` with `goal_met: false`, because no model call is made and no acceptance command is executed.
- `--model` (default `claude-sonnet-5-5` or `CLAUDE_MODEL_NAME`), `--region` (default `global` or `CLOUD_ML_REGION`), `--project`, `--max-turns`, `--token-budget`, `--max-tokens`, `--verify-timeout`, `--temperature`.

---

## Phase 3: Read the Report & Close the Goal

The script prints a JSON report to stdout and uses these exit codes:

| Exit | `status` | Meaning |
|---|---|---|
| `0` | `goal_met` | All acceptance commands passed and Claude declared completion |
| `2` | `max_turns_reached` / `token_budget_exhausted` / `stalled` / `model_refused` | Goal not met. `acceptance` shows which checks still fail |
| `1` | `api_error` or setup error | Auth, quota, model ID, or configuration problem. See `error` |

1. **Re-verify independently.** Run every acceptance command yourself.
2. **Review the diff** (`git diff`) for weakened or deleted tests, scope creep, and hardcoded secrets.
3. **If the goal wasn't met:** re-run the harness with a narrower objective that names the failing checks, or fix the remaining issues directly.

---

## References

- [harness-prompt-template.md](references/harness-prompt-template.md): objective templates for spec, subsystem, and hardening goals.
- [spec-to-production-code.md](examples/spec-to-production-code.md): an end-to-end goal-mode walkthrough.
- [pso-compliance-matrix.md](references/pso-compliance-matrix.md): IAM, data residency, and data-governance notes.
- [call_opus_model_garden.py](scripts/call_opus_model_garden.py): the goal-loop runner. Offline tests: `python3 -m unittest discover -s skills/claude-agent-harness/scripts -p 'test_*.py'`.
