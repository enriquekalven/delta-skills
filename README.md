# Delta Skills (`delta-skills`)

> Field execution playbooks and orchestrator skills for Google Cloud Technical Deployment Leads (TDLs), Forward Deployed Engineers (FDEs), and Agentic Transformation Leads (ATLs).

`delta-skills` packages meta-skills for customer engagement orchestration, technical discovery, baseline KPI auditing, GCP AI Agent architecture evaluation, repository governance, multi-model Claude integration, and phase-gated software engineering lifecycles.

---

## Prerequisites

### 1. Runtimes & Package Managers
* **Node.js 18+ & `npx`**:
  ```bash
  node -v
  ```
* **Python 3.10+ & `uv`**:
  ```bash
  python3 --version
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Supported AI Agent Framework (At Least One)
* **Antigravity CLI** (`agy`)
* **Google Agents CLI / Gemini CLI** (`agents-cli` / `gemini`)
* **Claude Code / Cursor / Codex**

### 3. Upstream Skill Dependencies
Install upstream dependencies if using skill-based orchestration:

```bash
# 1. Production Agent Skills (Addy Osmani)
npx skills add addyosmani/agent-skills

# 2. PM Skills
# Installed into ~/.gemini/config/plugins/ or ~/.agents/skills

# 3. Engineering Skills (Matt Pocock)
# Installed into ~/.gemini/config/plugins/ or ~/.agents/skills

# 4. Google Cloud Agents CLI Skills
agents-cli update
```

---

## Skills Included

### Meta-Orchestrators & Field Playbooks
1. **`tdl-field-guide`**: Operational execution playbook for 12-week enterprise engagements across 4 phases (Discover/Define ➔ Prototype/Validate ➔ Production Build ➔ Harden/Launch).
2. **`e2e-delivery-workflow`**: Phase-gated software delivery workflow guiding projects step-by-step through a 7-phase SDLC.

### Architecture & Discovery Skills
3. **`gcp-agent-architecture-advisor`**: Ingests PRD & intake notes to recommend a Google Cloud AI Agent architecture across 3 tiers (No-Code, Low-Code, High-Code ADK) with product release maturity flags (GA vs Preview).
4. **`synthetic-baseline-protocol`**: Pre-deployment quantitative baseline protocol for auditing historical SME records and outputting `baseline_kpis.json`.
5. **`codebase-onboarding-and-mapping`**: Analyzes client repositories to map components, entry points, and dependencies into `docs/ONBOARDING.md`.

### Multi-Model & Claude Integration Skills (ZDR Compliant)
6. **`claude-review`**: Two-pass coding and review workflow. Baseline execution via Gemini 3.6 Flash followed by peer review via Vertex AI Model Garden Opus 5 ZDR endpoint.
7. **`claude-agent-harness`**: Delegated spec-to-code generation routing PRDs and specs directly to Model Garden Opus 5 ZDR endpoint.

### Operations, Governance, & Auditing Skills
8. **`ecc-repo-conventions`**: Enforces standardized repository structure, file naming conventions, `STATE.md`, and environment hygiene.
9. **`agentic-engineering`**: Governs subagent task decomposition, multi-model cost routing, and subagent fleet management.
10. **`skill-stocktake`**: Audits workspace capability slots (`#CAPABILITY: Slot-Name`) to verify tool readiness prior to executing project phases.

---

## Installation

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

* [Using Claude Models in Antigravity Guide](docs/MULTI_MODEL_SKILLS_GUIDE.md)
* [Technical Deployment Lead (TDL) Field Execution User Guide](docs/tdl-user-guide.md)
* [End-to-End Delivery Workflow Guide](docs/e2e-delivery-workflow.md)
* [AlphaEvolve Skill Evaluation Matrix](docs/alphaevolve-masterclass-matrix.md)

---

## License
Licensed under the [Apache-2.0 License](LICENSE).
