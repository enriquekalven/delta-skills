---
name: delta-engine
description: >
  The Ultimate Google Cloud AI Agent & Field Engineering Master Engine.
  Consolidates Discovery, GCP 3-Tier Architecture Advisory, 2-Role Squad Execution, Autonomous TDD Task Loops, FastMCP Server Building, Secret Scanning, Playwright UI Testing, Plain-English Anti-Slop Auditing, and Vertex AI Model Garden Opus 5 ZDR Peer Review into one unified master skill.
  Triggers on: "delta engine", "delta squad", "gcp agent", "ultimate skill", "delta-engine", "run delta workflow", "full delivery loop".
---

# Delta Engine Master Suite (`delta-engine`)

The ultimate, consolidated Google Cloud AI Agent & Field Engineering suite. Replaces fragmented sub-skills with a single, production-grade master engine governing the entire 4-phase delivery lifecycle.

---

## 🏛️ Architecture Overview: 4 Consolidated Pillars

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      DELTA ENGINE MASTER PIPELINE                      │
 ├────────────────────────────────────────────────────────────────────────┤
 │  1. DISCOVER & ANALYZE  : Repo dependency mapping + 50 SME baseline   │
 │                          KPI audit (baseline_kpis.json).               │
 │                                                                        │
 │  2. PLAN & ARCHITECT    : GCP 3-tier architecture choice (No-Code,      │
 │                          Low-Code, High-Code ADK) + 2-role squad.      │
 │                                                                        │
 │  3. BUILD & TEST        : prd.json task loop + FastMCP server +        │
 │                          Playwright UI test + secret scanner.          │
 │                                                                        │
 │  4. HARDEN & LAUNCH     : Model Garden Opus 5 ZDR peer review +         │
 │                          Plain-English rm-slop auditor + ROI math.     │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 👥 2-Role Lean Squad Execution Model

Rather than bloated 6-role corporate matrices, `delta-engine` enforces a **Lean 2-Role Execution Pair**:

1. **Architect & Specifier (TDL Persona)**:
   - Owns Discovery (`docs/ONBOARDING.md`), `PRD.md`, GCP 3-tier architecture selection, threat modeling (`THREAT_MODEL.md`), and programmatic phase gate enforcement.
2. **Builder & Hardener (FDE Persona)**:
   - Owns task breakdown (`prd.json`), TDD red-green-refactor loops using production templates (`fastapi_main.py`, `pydantic_v2_schemas.py`, `pytest_fixtures.py`), FastMCP server integration (`mcp_fastapi_sse.py`), secret scanning, and CI/CD deployment.

---

## 💻 Master CLI Runner (`scripts/delta_cli.py`)

Execute all phases through the unified master CLI runner:

### 1. Phase 1: Discover & Analyze
```bash
python3 skills/delta-engine/scripts/delta_cli.py analyze --path .
```
Scans repository file structure, verifies `docs/ONBOARDING.md`, and generates `baseline_kpis.json`.

### 2. Phase 2: Plan & Architect
```bash
python3 skills/delta-engine/scripts/delta_cli.py plan --prd PRD.md
```
Evaluates the **Abstraction Selection Matrix**:
- **Deterministic Skill**: Simple prompt/CLI workflow.
- **Model Context Protocol (MCP)**: Custom Stdio/SSE tool server (`mcp-server-builder`).
- **Autonomous Agent**: Custom `google-adk` Python agent hosted on Vertex AI Agent Engine / Cloud Run.

### 3. Phase 3: Build & Verify
```bash
python3 skills/delta-engine/scripts/delta_cli.py build --phase 1 --url https://delta-tdl-user-guide.web.app
```
Executes automated secret scanning, phase gate verification, and Playwright UI health checks.

### 4. Phase 4: Harden & De-Slop
```bash
python3 skills/delta-engine/scripts/delta_cli.py harden --doc README.md
```
Runs plain-English anti-slop audit (`rm-slop`) and routes peer review to Vertex AI Model Garden Opus 5 ZDR (`claude-review`).

---

## 📁 Included Production Code Templates (`templates/`)

* [`fastapi_main.py`](file:///Users/enriq/Documents/git/delta-skills/skills/tdl-field-guide/templates/fastapi_main.py): Production FastAPI app with lifespan context & CORS.
* [`pydantic_v2_schemas.py`](file:///Users/enriq/Documents/git/delta-skills/skills/tdl-field-guide/templates/pydantic_v2_schemas.py): Pydantic v2 schemas with `extra="forbid"`.
* [`pytest_fixtures.py`](file:///Users/enriq/Documents/git/delta-skills/skills/tdl-field-guide/templates/pytest_fixtures.py): PyTest fixtures with `httpx.AsyncClient` ASGI transport.
* [`mcp_fastapi_sse.py`](file:///Users/enriq/Documents/git/delta-skills/skills/mcp-server-builder/templates/mcp_fastapi_sse.py): FastMCP Python server with Stdio/SSE transports.
