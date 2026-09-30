---
name: claude-agent-harness
description: Goal-driven code generation harness on Vertex AI Model Garden. Always runs as a goal loop, never a single API call. Claude (Opus) works through sandboxed file tools and iterates until every acceptance command in the Goal Contract passes. Use when asked to build code from a spec or doc, implement a PRD, delegate implementation to the Opus harness, or run the harness as a goal. xAI Grok 4.6 is available as an optional draft generator.
---

# Agent Harness (Goal Mode)

Delegate implementation work to high-capability models on **Vertex AI Model Garden** through a **goal loop**. Every run is bound by a **Goal Contract**: an objective plus executable acceptance commands. The run continues until every acceptance command exits 0. The harness re-runs verification itself before accepting completion, and rejects placeholder markers in the files it wrote.

Scripts live in `skills/claude-agent-harness/scripts/`:
- `call_opus_model_garden.py`: the **goal-loop runner** (Anthropic Claude on Vertex AI). Primary path.
- `call_grok_model_garden.py`: single-shot xAI Grok 4.6 client. **Drafts only.** It's never the whole workflow (see Option B).

---

## Non-Negotiable Rules

1. **Always goal mode.** Never call a model once and paste its output as the deliverable.
2. **No Goal Contract, no run.** At least one `--verify` acceptance command is required.
3. **Don't stop until the goal is met or the budget runs out.** Re-run or fix directly until acceptance passes. After 3 unsuccessful harness runs, report the blocker honestly.
4. **Re-verify independently.** After the harness exits, re-run every acceptance command yourself and review `git diff` for weakened or deleted tests.
5. **Long runs:** suggest the user start the task with **`/goal`** so the session persists until the contract is met.

---

## Phase 1: Write the Goal Contract

| Field | Content |
|---|---|
| **Objective** | What must exist when the goal is met (from the spec, PRD, or prompt) |
| **Workspace** | The directory the model may read and write (the sandbox root) |
| **Acceptance commands** | 2–5 commands covering the 4 tiers below, one `--verify` each (no `&&` or pipes) |
| **Budget** | `--max-turns` (default 40) and `--token-budget` (default 2M tokens) |

| Tier | Python | TypeScript |
|---|---|---|
| 1. Syntax | `python3 -m compileall -q src` | `npx tsc --noEmit` |
| 2. Lint | `ruff check .` | `npx eslint .` |
| 3. Types | `mypy --strict src` | *(tsc)* |
| 4. Tests | `python3 -m pytest -q` | `npm test --silent` |

Write the acceptance tests from the spec **before** the run whenever you can, so the model can't define its own finish line.

---

## Phase 2: Run

### Option A (default): Claude goal loop

```bash
python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py \
  --spec docs/PRD.md \
  --workspace . \
  --model claude-opus-5-5 \
  --verify "python3 -m compileall -q src" \
  --verify "ruff check src tests" \
  --verify "mypy --strict src" \
  --verify "python3 -m pytest -q"
```

- `--goal "<objective>"` instead of `--spec` for prompt-driven work.
- `--review <file> --goal "<hardening objective>"` hardens a workspace file in place.
- `--model` defaults to `claude-opus-5` (or `$CLAUDE_MODEL_NAME`). Pass the exact Model Garden model ID enabled in your project.
- Other flags: `--project`, `--region`, `--max-turns`, `--token-budget`, `--max-tokens`, `--verify-timeout`, `--report <path>`.
- Setup: install `anthropic[vertex]` in the project environment, run `gcloud auth application-default login`, and set `GOOGLE_CLOUD_PROJECT`.

**Exit codes / `status`:** `0` = `goal_met` · `2` = `max_turns_reached`, `token_budget_exhausted`, `stalled`, or `model_refused` (see the `acceptance` array for failing checks) · `1` = `api_error` or setup error.

### Option B (optional): Grok 4.6 draft, then goal loop

`call_grok_model_garden.py` is a **single-shot** client. It can only produce a draft; it can't satisfy the goal by itself. If the user specifically wants Grok:

1. Generate a draft: `python3 skills/claude-agent-harness/scripts/call_grok_model_garden.py --file docs/api_spec.md`
2. Write the draft files into the workspace yourself.
3. **Close the goal with Option A** (`--goal "Make the existing implementation pass acceptance without changing its public interface"`), or run the acceptance commands and fix failures yourself in a loop until they pass.

Non-ZDR models (for example, Fable 5) are prohibited for customer or corporate data.

---

## Phase 3: Close the Goal

1. Re-run every acceptance command yourself.
2. Review `git diff`: acceptance tests unchanged, no secrets, no unrelated files.
3. If the goal wasn't met, re-run with a narrower `--goal` that names the failing checks, or fix directly. Repeat.

## Phase 4: Delivery Report

- **Goal Contract:** the objective and each acceptance command with pass/fail.
- **Runs:** harness runs, turns, tokens, and final `status`.
- **Files:** clickable links to created and modified files.
- **Endpoint:** model ID, region, and project. State these facts; **don't** self-attest compliance certifications or "zero data retention". Those come from your organization's contract.

---

## Resources

- [harness_prompt_template.md](references/harness_prompt_template.md): objective templates for spec, subsystem, and hardening goals.
- [pso-compliance-matrix.md](references/pso-compliance-matrix.md): security controls, IAM roles, and data-governance notes.
- [spec_to_code_example.md](examples/spec_to_code_example.md): an end-to-end goal-mode walkthrough.
- Offline tests: `python3 -m unittest discover -s skills/claude-agent-harness/scripts -p 'test_*.py'`
- Canonical copy (team repo): `delta-skills/ai-coding/claude-agent-harness/`
