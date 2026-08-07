---
name: delta-build
description: >
  Phase 3 Production Build & TDD Verification Skill.
  Executes prd.json task loops, builds FastMCP tool servers, runs secret scanning, Playwright CLI UI tests, and builds against production code templates.
  Triggers on: "delta build", "phase 3 build", "tdd build", "mcp server", "playwright test", "secret scan".
---

# Phase 3: Production Build & TDD (`delta-build`)

Governs Phase 3 (Weeks 7-10) of the delivery lifecycle. Drives test-driven development using production code templates, FastMCP tool servers, and automated secret scanning.

---

## 🛠️ Build Protocols

1. **`prd.json` Task Loop**: Executes red-green-refactor iteration on task items.
2. **FastMCP Server**: Implements Stdio/SSE tool servers for external database and vector search integration.
3. **Playwright UI Testing**: Verifies web app availability and captures full-page screenshots via `--playwright` flag.
4. **Secret Scanner**: Scans workspace for exposed API keys (GCP, OpenAI, GitHub PATs, JWTs).

---

## 💻 CLI Execution

```bash
python3 skills/delta-build/scripts/delta_cli.py build --phase 3 --url https://delta-tdl-user-guide.web.app
```

---

## ✋ Human Checkpoint (Phase Gate 3 Exit)
Programmatic verification pass (`verify_phase_gate.py`) confirming zero secret exposures and 100% PyTest pass rate before advancing to Phase 4 (`delta-harden`).
