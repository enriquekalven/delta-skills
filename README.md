# Delta Skills (`delta-skills`)

> Enterprise Google Cloud AI Agent architecture advisory, multi-model ZDR cost routing, SME baseline KPI auditing, and 12-week Technical Deployment Lead (TDL) field execution playbooks. Fully integrated with **BMAD Method**, **Antigravity CLI**, **Google Agents CLI**, and **Open Skills**.

🌐 **Live User Guide & Interactive Sandbox**: [https://delta-tdl-user-guide.web.app](https://delta-tdl-user-guide.web.app)

`delta-skills` packages meta-skills for customer engagement orchestration, technical discovery, baseline KPI auditing, GCP AI Agent architecture evaluation, repository governance, multi-model Vertex AI ZDR integration, and phase-gated software engineering lifecycles.

---

## 🤝 BMAD Method Integration

`delta-skills` acts as an official BMAD Method enterprise module (`bmad-module-gcp-delta`), marrying BMAD's 4-Phase Delivery Loop with GCP-specific architecture and enterprise field playbooks.

| BMAD Delivery Phase | Delta Skills Integrated Workflows |
| :--- | :--- |
| **Phase 1: Analysis (Clarify)** | `delta-discover` (50 SME sample audit ➔ `baseline_kpis.json`), `codebase-onboarding-and-mapping` |
| **Phase 2: Planning (Solution)** | `delta-plan` (3-Tier GCP Advisor: No-Code vs Low-Code vs High-Code ADK), `tdl-field-guide` (12-Week Squad & Scope) |
| **Phase 3: Build & Verify** | `delta-build` (FastMCP tools, Secret Scanning, Playwright UI testing, 100% PyTest), `ecc-repo-conventions` |
| **Phase 4: Learn & Adjust** | `delta-harden` (Model Garden Opus 5 ZDR Peer Review, Plain-English Anti-Slop Audit, Realized ROI Report) |

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
* **skills.sh / Open Skills** (`npx skills.sh`)
* **Claude Code / Cursor / Codex**

---

## Skills Catalog (v3.2.0)

### 1. 4-Phase Phased Lifecycle Suite
1. **`delta-orchestrator`**: Master phase router enforcing phase gate criteria before advancing `STATE.md`.
2. **`delta-discover`** (Phase 1, Weeks 1–3): Customer intake interviews, repository mapping (`docs/ONBOARDING.md`), and 50 SME ticket baseline audit (`baseline_kpis.json`).
3. **`delta-plan`** (Phase 2, Weeks 4–6): Abstraction matrix evaluation (Skill vs MCP vs Agent), GCP 3-Tier Architecture recommendation (`docs/ARCHITECTURE_RECOMMENDATION.md`), and `THREAT_MODEL.md`.
4. **`delta-build`** (Phase 3, Weeks 7–10): FastMCP tool server implementation, automated secret scanning, Playwright CLI browser UI tests, and 100% PyTest validation.
5. **`delta-harden`** (Phase 4, Weeks 11–12): Plain-English anti-slop documentation audit, Vertex AI Model Garden Opus 5 ZDR peer review, and customer ROI savings report.

### 2. Multi-Model Vertex AI ZDR Skills
6. **`claude-review`**: Two-pass execution loop. Generates baseline code rapidly with Gemini 3.6 Flash, executes ZDR peer review with Opus 5 via Vertex AI Model Garden API, and applies revisions.
7. **`claude-agent-harness`**: Delegated high-tier code generation routing PRDs and specs directly to Vertex AI Model Garden Opus 5 (`claude-opus-5` in region `us-central1`).
   ```bash
   # Spec ingestion
   python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py --spec docs/PRD.md

   # File review
   python3 skills/claude-review/scripts/call_opus_model_garden.py --review src/agent_server.py
   ```

### 3. Discovery & Benchmarking
8. **`skill-discovery-and-benchmarking`**: Audits local skill gaps and searches external registries (`skills.sh`, `SkillsMP`, `MCPMarket`) for high-performing upgrades.

---

## Installation

### BMAD Method Installer
```bash
npx bmad-method install --custom https://github.com/enriquekalven/delta-skills
```

### Antigravity CLI
```bash
agy plugin install delta-skills
```

### skills.sh Universal Registry
```bash
npx skills.sh add delta-skills
```

### Gemini CLI / Google Agents CLI
```bash
agents-cli plugin install delta-skills
```

---

## Documentation & Playbooks

* 🌐 [Live User Guide Website](https://delta-tdl-user-guide.web.app)
* 📘 [Technical Deployment Lead (TDL) Field Execution User Guide](docs/tdl-user-guide.md)
* 🛡️ [Using Claude Models in Antigravity (Vertex AI ZDR Guide)](docs/MULTI_MODEL_SKILLS_GUIDE.md)
* 🚀 [Delta Vision: TDL + FDE Field Strategy](docs/BLOG_POST_DELTA_VISION_TDL_FDE.md)
* 📊 [Squash & Unification Master Report](docs/SQUASH_AND_UNIFICATION_MASTER_REPORT.md)

---

## License
Licensed under the [Apache-2.0 License](LICENSE).

