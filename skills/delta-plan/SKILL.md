---
name: delta-plan
description: >
  Phase 2 Architecture & Planning Skill.
  Workshops PRD requirements with stakeholders, runs GCP Abstraction Selection Matrix, configures Google ADK DatabaseSessionService & AlloyDBpg vector memory, builds THREAT_MODEL.md, and initializes 2-role squad pair (Architect & Builder).
  Triggers on: "delta plan", "phase 2 planning", "gcp architecture advisor", "threat model", "squad matrix", "adk memory".
---

# Phase 2: Architecture & Planning (`delta-plan`)

Governs Phase 2 (Weeks 4-6) of the customer engagement lifecycle. Recommends the optimal GCP architecture tier, configures stateful Google ADK session persistence, and establishes threat boundaries before writing production code.

---

## 🏛️ Abstraction Selection Matrix

- **Deterministic Skill**: Simple CLI / prompt workflow.
- **Model Context Protocol (MCP)**: Custom Stdio/SSE tool server (`mcp_fastapi_sse.py`) or official server registry.
- **Autonomous Agent**: Custom `google-adk` Python agent hosted on Vertex AI Agent Engine / Cloud Run with `DatabaseSessionService` and `AlloyDBpg` episodic vector memory.

---

## 👥 2-Role Squad Execution Model

1. **Architect & Specifier (TDL Persona)**: Owns discovery, PRD, architecture recommendation, threat model (`THREAT_MODEL.md`), and phase gate verifications.
2. **Builder & Hardener (FDE Persona)**: Owns task breakdown, TDD implementation, FastMCP tool building, and CI/CD pipelines.

---

## 💻 CLI Execution

```bash
python3 skills/delta-build/scripts/delta_cli.py plan --prd PRD.md
```

---

## ✋ Human Checkpoint (Phase Gate 2 Exit)
Customer sign-off required on `docs/ARCHITECTURE_RECOMMENDATION.md` and `THREAT_MODEL.md` before advancing to Phase 3 (`delta-build`).
