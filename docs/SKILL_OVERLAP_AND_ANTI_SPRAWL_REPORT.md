# Skill Overlap & Anti-Sprawl Governance Audit Report

- **Target Repository**: `delta-skills` (v1.3.0)
- **Total Skills Audited**: 14 Meta-Skills
- **Reviewer Protocol**: `claude-review` ZDR Multi-Model Peer Review

---

## 1. Inventory & Category Taxonomy (14 Skills)

| Category | Skill Name | Primary Function | Primary Phase Slot |
| :--- | :--- | :--- | :--- |
| **Analysis** | `codebase-onboarding-and-mapping` | Dependency mapping & `ONBOARDING.md` | Phase 1 (Analysis) |
| **Analysis** | `synthetic-baseline-protocol` | 50-sample SME ticket ROI audit | Phase 1 (Analysis) |
| **Planning** | `gcp-agent-architecture-advisor` | Abstraction Matrix (Skill vs MCP vs Agent) | Phase 2 (Planning) |
| **Planning** | `tdl-field-guide` | 12-week customer engagement & 2-role matrix | Phase 2 (Planning) |
| **Build** | `e2e-delivery-workflow` | 7-phase software engineering SDLC | Phase 3 (Build) |
| **Build** | `mcp-server-builder` | Custom Model Context Protocol (MCP) server builder | Phase 3 (Build) |
| **Build** | `agent-browser-testing` | Playwright CLI & DevTools UI health tester | Phase 3 (Build) |
| **Build** | `ralph-autonomous-loop` | `prd.json` task execution loop | Phase 3 (Build) |
| **Build** | `claude-agent-harness` | Spec-to-code delegation to Opus 5 ZDR | Phase 3 (Build) |
| **Build** | `ecc-repo-conventions` | Repo structure, `STATE.md`, & env hygiene | Phase 3 (Build) |
| **Build** | `agentic-engineering` | Multi-model cost routing & subagent fleets | Phase 3 (Build) |
| **Learn / Review** | `claude-review` | 2-pass Gemini Flash + Opus 5 ZDR peer review | Phase 4 (Learn) |
| **Learn / Review** | `rm-slop` | Plain-English AI slop & buzzword auditor | Phase 4 (Learn) |
| **Learn / Review** | `skill-stocktake` | Audits capability slots before phase gates | Phase 4 (Learn) |

---

## 2. Identified Overlaps & Sprawl Vulnerabilities

### 🚩 Cluster 1: Workflow Lifecycle Overlap
* **Overlapping Skills**: `delta-bmad-workflow` vs `tdl-field-guide` vs `e2e-delivery-workflow`
* **Finding**: Both `tdl-field-guide` and `e2e-delivery-workflow` track phase transitions, creating potential confusion on entry point.
* **Correction**: Designate `delta-bmad-workflow` as the **Exclusive Entry Router**, delegating to `tdl-field-guide` for squad governance and `e2e-delivery-workflow` for code execution.

### 🚩 Cluster 2: Model Garden API Invocation
* **Overlapping Skills**: `claude-review` vs `claude-agent-harness`
* **Finding**: Both scripts manage Vertex AI Model Garden endpoints (`call_opus_model_garden.py`).
* **Correction**: Centralize Model Garden API invocation logic into a single shared module to avoid code duplication.

### 🚩 Cluster 3: Verification & Execution Loops
* **Overlapping Skills**: `ralph-autonomous-loop` vs `verify_phase_gate.py`
* **Finding**: Clear functional distinction exists: `ralph-autonomous-loop` manages task-level red-green iteration within `prd.json`, while `verify_phase_gate.py` enforces phase-level exit gates.

---

## 3. 3-Point Anti-Sprawl Governance Plan

1. **Phase Slot Lock-In**: Every skill must explicitly specify its single primary phase slot in `module.yaml`.
2. ** DRY Helper Library**: Consolidate repetitive utility scripts under a shared directory (`scripts/common/`).
3. **Automated Stocktake Audit**: Use `skill-stocktake` CLI to detect unmapped or orphan skills prior to release.
