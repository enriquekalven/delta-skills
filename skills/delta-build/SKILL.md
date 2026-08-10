---
name: delta-build
description: >
  Phase 3 Production Build & TDD Verification Skill.
  Executes prd.json task loops, builds FastMCP tool servers, integrates official MCP server registries (Postgres, SQLite, Git, Memory), runs secret scanning, Playwright CLI UI tests, and AlphaEvolve evaluation cascades.
  Triggers on: "delta build", "phase 3 build", "tdd build", "mcp server", "playwright test", "secret scan", "eval cascade".
---

# Phase 3: Production Build & TDD (`delta-build`)

Governs Phase 3 (Weeks 7-10) of the delivery lifecycle. Drives test-driven development using production code templates, FastMCP tool servers, official MCP registry integrations, and automated secret scanning.

---

## 🛠️ Build Protocols

1. **`prd.json` Task Loop**: Executes red-green-refactor iteration on task items with AST traceback error parsing.
2. **FastMCP & Official MCP Registry**: Integrates custom Stdio/SSE FastMCP tool servers (`templates/mcp_fastapi_sse.py`) and official pre-built MCP servers ([`github.com/modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers)) for Postgres, SQLite, Git, Filesystem, and Memory.
3. **Playwright UI Testing**: Verifies web app availability and captures full-page screenshots via `--playwright` flag.
4. **Secret Scanner**: Scans workspace for exposed API keys (GCP, OpenAI, GitHub PATs, JWTs).
5. **AlphaEvolve Evaluation Cascade**: Executes multi-objective scoring across Accuracy, Secret Hygiene, Cost, and Latency (`--eval-cascade`).

---

## 💻 CLI Execution

```bash
# Standard Phase 3 verification with endpoint check:
python3 skills/delta-build/scripts/delta_cli.py build --phase 3 --url https://delta-tdl-user-guide.web.app

# Run AlphaEvolve Multi-Objective Evaluation Cascade:
python3 skills/delta-build/scripts/delta_cli.py build --phase 3 --eval-cascade
```

---

## ✋ Human Checkpoint (Phase Gate 3 Exit)
Programmatic verification pass confirming zero secret exposures, 100% PyTest pass rate, and an AlphaEvolve Evaluation Cascade fitness score ≥ 80.0/100 before advancing to Phase 4 (`delta-harden`).
