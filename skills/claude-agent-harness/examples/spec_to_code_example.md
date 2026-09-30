# Walkthrough: Spec to Verified Code in Goal Mode

This walkthrough shows the **Claude Agent Harness** turning a spec into code through a goal loop. Claude iterates with sandboxed tools until every acceptance command passes, instead of producing code from one API call.

> [!NOTE]
> The turn log and report below are illustrative. Your actual turn counts, token usage, and failures will differ.

---

## 1. Input Specification (`specs/rate_limiter_spec.md`)

```markdown
# Specification: Token Bucket Rate Limiter

## Objective
Thread-safe token bucket rate limiter for microservice ingress protection.

## Requirements
1. Token bucket with refill rate `r` tokens/sec and capacity `b` tokens.
2. Redis backend using an atomic Lua script, so distributed workers can't race.
3. If Redis is unavailable, degrade to an in-memory bucket instead of dropping requests.
4. Metrics hooks for allowed, rejected, and fallback events.
5. Tests for refill math, concurrency, and Redis disconnection.
```

---

## 2. Goal Contract (written by the host agent before running)

| Field | Value |
|---|---|
| Objective | Implement `src/ratelimit/` per `specs/rate_limiter_spec.md`, including tests |
| Workspace | Repository root (`.`) |
| Acceptance | `python3 -m compileall -q src` · `ruff check src tests` · `mypy --strict src` · `python3 -m pytest -q tests/ratelimit` |
| Budget | `--max-turns 40`, `--token-budget 2000000` |

The host agent first writes `tests/ratelimit/test_contract.py` from the spec: refill math, capacity ceiling, and fallback when Redis raises `ConnectionError`. That way Claude can't define its own finish line.

---

## 3. Run the Goal Loop

```bash
export GOOGLE_CLOUD_PROJECT="my-enterprise-gcp-project"
export CLOUD_ML_REGION="us-central1"

python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py \
  --spec specs/rate_limiter_spec.md \
  --workspace . \
  --verify "python3 -m compileall -q src" \
  --verify "ruff check src tests" \
  --verify "mypy --strict src" \
  --verify "python3 -m pytest -q tests/ratelimit" \
  --report .harness_report.json
```

### Representative turn log (stderr)

```text
[goal] turn 1/40 -> claude-opus-5        # list_files, read_file tests/ratelimit/test_contract.py
[goal] turn 2/40 -> claude-opus-5        # read_file pyproject.toml (conventions, deps)
[goal] wrote src/ratelimit/__init__.py (212 bytes)
[goal] wrote src/ratelimit/bucket.py (4810 bytes)
[goal] wrote tests/ratelimit/test_bucket.py (3920 bytes)
[goal] verification 1: 2/4 passing       # mypy: redis client typed as Any; pytest: refill off-by-one
[goal] turn 7/40 -> claude-opus-5        # replace_in_file bucket.py: Protocol for Redis client
[goal] verification 2: 3/4 passing       # pytest: fallback test still failing
[goal] turn 9/40 -> claude-opus-5        # replace_in_file bucket.py: catch redis ConnectionError, not bare Exception
[goal] verification 3: 4/4 passing
[goal] verification 4: 4/4 passing       # declare_goal_complete -> harness re-verifies -> accepted
```

The harness would have rejected completion if any acceptance command failed, or if a written file still contained a `TODO`/`FIXME` placeholder.

---

## 4. Report (stdout, exit code 0)

```json
{
  "status": "goal_met",
  "goal_met": true,
  "model": "claude-opus-5",
  "turns": 10,
  "verification_runs": 4,
  "usage": {"input_tokens": 312000, "output_tokens": 18400},
  "files_written": ["src/ratelimit/__init__.py", "src/ratelimit/bucket.py", "tests/ratelimit/test_bucket.py"],
  "acceptance": [
    {"command": "python3 -m compileall -q src", "passed": true, "exit_code": 0},
    {"command": "ruff check src tests", "passed": true, "exit_code": 0},
    {"command": "mypy --strict src", "passed": true, "exit_code": 0},
    {"command": "python3 -m pytest -q tests/ratelimit", "passed": true, "exit_code": 0}
  ],
  "summary": "Token bucket with atomic Lua script, Protocol-typed Redis client, in-memory fallback on ConnectionError, metrics hooks; tests for refill, concurrency, and fallback.",
  "project": "my-enterprise-gcp-project",
  "region": "us-central1"
}
```

---

## 5. Close the Goal (host agent)

1. Re-run all four acceptance commands yourself. Don't trust the report alone.
2. Run `git diff`. Confirm `tests/ratelimit/test_contract.py` is unchanged, and check that no secrets or unrelated files were touched.
3. Deliver: the Goal Contract with pass/fail status, links to the files, turns and tokens used, and the endpoint (model, region, project).

**If the status had been `max_turns_reached`:** re-run with a narrower `--goal` that names the failing check (for example, "make `mypy --strict src` pass without changing behavior"), or fix it directly. Stop and report after three unsuccessful harness runs.
