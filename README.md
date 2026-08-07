# Delta Skills (`delta-skills`)

> Enterprise Google Cloud AI Agent architecture advisory, multi-model ZDR cost routing, SME baseline KPI auditing, and 12-week Technical Deployment Lead (TDL) field execution playbooks. Fully integrated with **BMAD Method**, **Antigravity CLI**, **Google Agents CLI**, and **Open Skills**.

`delta-skills` packages meta-skills for customer engagement orchestration, technical discovery, baseline KPI auditing, GCP AI Agent architecture evaluation, repository governance, multi-model Vertex AI ZDR integration, and phase-gated software engineering lifecycles.

---

## 🤝 BMAD Method Integration

`delta-skills` acts as an official BMAD Method enterprise module (`bmad-module-gcp-delta`), marrying BMAD's 4-Phase Delivery Loop with GCP-specific architecture and enterprise field playbooks.

| BMAD Delivery Phase | Delta Skills Integrated Workflows |
| :--- | :--- |
| **Phase 1: Analysis (Clarify)** | `synthetic-baseline-protocol` (50 SME sample audit ➔ `baseline_kpis.json`), `codebase-onboarding-and-mapping` |
| **Phase 2: Planning (Solution)** | `gcp-agent-architecture-advisor` (No-Code vs Low-Code vs High-Code ADK), `tdl-field-guide` (12-Week Squad & Scope) |
| **Phase 3: Build & Verify** | `e2e-delivery-workflow` (7-Phase SDLC), `claude-review` (Gemini Flash + Vertex ZDR Opus 5 peer review), `ecc-repo-conventions` |
| **Phase 4: Learn & Adjust** | Post-eval ROI benchmark verification against `baseline_kpis.json`, `skill-stocktake` |

* **Bridge Skill**: `delta-bmad-workflow` — Runs BMAD delivery loops with GCP enterprise skills.

---

## Prerequisites

### 1. Runtimes & Package Managers
* **Node.js 20.12+ & `npx`**:
  ```bash
  node -v
  ```
* **Python 3.10+ & `uv`**:
  ```bash
  python3 --version
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Supported AI Agent Framework (At Least One)
* **BMAD Method CLI** (`npx bmad-method`)
* **Antigravity CLI** (`agy`)
* **Google Agents CLI / Gemini CLI** (`agents-cli` / `gemini`)
* **Claude Code / Cursor / Codex**

---

## Skills Included

### Meta-Orchestrators & Workflow Bridges
1. **`delta-bmad-workflow`**: **[NEW]** Master workflow bridge mapping BMAD Method 4-phase delivery to GCP TDL enterprise field playbooks.
2. **`tdl-field-guide`**: Operational execution playbook for 12-week enterprise engagements across 4 phases (Discover/Define ➔ Prototype/Validate ➔ Production Build ➔ Harden/Launch).
3. **`e2e-delivery-workflow`**: Phase-gated software delivery workflow guiding projects step-by-step through a 7-phase SDLC.

### Architecture & Discovery Skills
4. **`gcp-agent-architecture-advisor`**: Ingests PRD & intake notes to recommend a Google Cloud AI Agent architecture across 3 tiers (No-Code, Low-Code, High-Code ADK) with product release maturity flags (GA vs Preview).
5. **`synthetic-baseline-protocol`**: Pre-deployment quantitative baseline protocol for auditing historical SME records and outputting `baseline_kpis.json`.
6. **`codebase-onboarding-and-mapping`**: Analyzes client repositories to map components, entry points, and dependencies into `docs/ONBOARDING.md`.

### Multi-Model & Claude Integration Skills (ZDR Compliant)
7. **`claude-review`**: Two-pass coding and review workflow. Baseline execution via Gemini 3.6 Flash followed by peer review via Vertex AI Model Garden Opus 5 ZDR endpoint.
8. **`claude-agent-harness`**: Delegated spec-to-code generation routing PRDs and specs directly to Model Garden Opus 5 ZDR endpoint.

### Operations, Governance, & Auditing Skills
9. **`ecc-repo-conventions`**: Enforces standardized repository structure, file naming conventions, `STATE.md`, and environment hygiene.
10. **`agentic-engineering`**: Governs subagent task decomposition, multi-model cost routing, and subagent fleet management.
11. **`skill-stocktake`**: Audits workspace capability slots (`#CAPABILITY: Slot-Name`) to verify tool readiness prior to executing project phases.

---

## Installation

### BMAD Method Installer
```bash
npx bmad-method install --custom https://github.com/enriquekalven/delta-skills
```

### Antigravity CLI
```bash
agy plugin install https://github.com/enriquekalven/delta-skills.git
```

### Gemini CLI / Google Agents CLI
```bash
gemini skills install https://github.com/enriquekalven/delta-skills.git --path skills
```

### Open Skills Standard
```bash
npx skills add enriquekalven/delta-skills
```

---

## Documentation

* [Delta-BMAD Master Workflow Bridge](skills/delta-bmad-workflow/SKILL.md)
* [Using Claude Models in Antigravity Guide](docs/MULTI_MODEL_SKILLS_GUIDE.md)
* [Technical Deployment Lead (TDL) Field Execution User Guide](docs/tdl-user-guide.md)
* [End-to-End Delivery Workflow Guide](docs/e2e-delivery-workflow.md)
* [AlphaEvolve Skill Evaluation Matrix](docs/alphaevolve-masterclass-matrix.md)

---

## License
Licensed under the [Apache-2.0 License](LICENSE).
