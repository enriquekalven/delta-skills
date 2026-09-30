# Goal Objective Templates

These templates are **objectives** for the goal-mode harness. Pass one as `--goal` (or in a `--file`), together with `--verify` acceptance commands. The harness adds the acceptance criteria, a workspace snapshot, and the tool instructions automatically, so **don't** ask for a special output format. Claude writes files through its sandboxed tools.

> [!IMPORTANT]
> A template is never a single-shot prompt. Every run needs at least one `--verify` command, and the loop continues until all of them pass. Always fill in `ACCEPTANCE` with the same commands you pass as `--verify`, so the objective and the contract agree.

---

## 1. Spec-to-Production-Code (Full Implementation)

Use this when turning a PRD, API specification, or architecture blueprint into working code. Usually paired with `--spec <file>`, which inlines the spec.

```markdown
Implement the attached specification completely inside the workspace.

### TARGET SCOPE
- Stack: <e.g., Python 3.11+, TypeScript, Go 1.22+>
- Files: <e.g., src/queue/distributed_retry_queue.py, tests/queue/test_retry_queue.py>
- Architecture: deep modules, explicit seams, decoupled interfaces. Follow the existing project layout.

### IMPLEMENTATION RULES
1. Complete implementations only: no TODO, stub, or elided sections.
2. Validate input at boundaries. Handle timeouts, partial failures, races, and corrupt data.
3. Strict typing (Python type hints with dataclasses/Pydantic, or TypeScript strict mode).
4. Structured logging that's safe for Cloud Logging. Never log secrets or PII.
5. No hardcoded secrets. Use parameterized queries. Never pass untrusted input to shell/exec sinks.
6. Tests for the happy path, boundary conditions, and failure modes.

### ACCEPTANCE
The goal is met when these commands pass from the workspace root (mirror your --verify flags):
- <e.g., python3 -m pytest -q tests/queue>
- <e.g., mypy --strict src/queue>

Do not modify these existing acceptance tests: <e.g., tests/queue/test_contract.py>
```

---

## 2. Architectural Subsystem (Multi-Module Systems)

Use this for multi-component subsystems (event streaming, distributed caching, agent tool protocols).

```markdown
Design and implement a decoupled subsystem that satisfies the requirements below.

### SYSTEM REQUIREMENTS
<INSERT_ARCHITECTURE_REQUIREMENTS>

### ARCHITECTURAL PRIORITIES
1. Clear seams and deep modules: minimal, cohesive interfaces that hide internal complexity.
2. Concurrency safety: atomic state updates, thread-safe queues, backpressure.
3. Resilience: retries with exponential backoff and jitter, circuit breakers, and dead-letter handling where the requirements call for them.
4. Google Cloud conventions: Application Default Credentials, Cloud Storage, Pub/Sub, Cloud Run patterns.

### DELIVERABLES
1. Interface / data contract definitions.
2. Core engine / service implementation.
3. Configuration / factory loaders.
4. Test suite that exercises the contracts.

### ACCEPTANCE
- <one command per --verify flag>
```

---

## 3. Code Review & Hardening

Use this with `--review <file>` to harden a workspace file in place.

```markdown
Review and harden the target file against enterprise security and reliability standards, fixing issues in place.

### AUDIT VECTORS
1. Security and data privacy: secret leaks, unvalidated input, insecure deserialization, missing authentication.
2. Concurrency: locks, shared-state mutation, async cancellation.
3. Reliability: explicit timeouts, deadlines, and retry policies on every network call.
4. Resource management: file descriptor, memory, and connection leaks; unbounded buffers.

### REQUIREMENTS
- Fix every Critical and High finding in place with replace_in_file.
- Add or extend tests that fail before each fix and pass after it.
- In the declare_goal_complete summary, list each finding with its risk rating (Critical, High, Medium, Low) and the fix.

### ACCEPTANCE
- <one command per --verify flag>
```

Run it with: `--review <file> --goal "$(cat hardening_objective.md)" --verify ...`
