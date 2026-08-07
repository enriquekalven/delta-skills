---
name: ralph-autonomous-loop
description: >
  Structured autonomous task execution loop utilizing prd.json task lists, continuous red-green-refactor testing, and automated state tracking.
  Triggers on: "ralph loop", "ralph-loop", "autonomous task loop", "prd task list", "continuous agent loop".
---

# Ralph Autonomous Task Loop (`ralph-autonomous-loop`)

Provides an autonomous task execution loop for AI agents. Consumes structured `prd.json` task lists, works through each task item sequentially, executes verification commands (`pytest`, `npm test`, custom scripts), commits passing work, and retries failures until all tasks reach `completed` status.

---

## 1. The `prd.json` Schema

Tasks are stored in `docs/prd.json`:

```json
{
  "project_name": "Autonomous Agent Feature",
  "version": "1.0.0",
  "tasks": [
    {
      "id": "TASK-1",
      "title": "Define Pydantic Schemas",
      "status": "completed",
      "verification_command": "pytest tests/test_schemas.py"
    },
    {
      "id": "TASK-2",
      "title": "Implement FastAPI Endpoint",
      "status": "pending",
      "verification_command": "pytest tests/test_endpoints.py"
    }
  ]
}
```

---

## 2. Autonomous Loop Execution Protocol

1. **Initialize PRD Task List**:
   ```bash
   python3 skills/ralph-autonomous-loop/scripts/run_ralph_loop.py --prd docs/prd.json
   ```
2. **Execute Single Task**: Pick the first pending task, write minimal implementation code, and run its `verification_command`.
3. **Verify & Update State**: If verification passes, update status to `completed` in `prd.json` and git commit the working code. If verification fails, analyze error output and retry fix.
4. **Repeat**: Loop automatically until all tasks are marked `completed`.
