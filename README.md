# Delta Skills Hub (`delta-skills`)

> **Google Cloud Delta Squad Meta-Skills & Field Execution Hub**

`delta-skills` packages the official Meta-Skills for Google Cloud Delta Squads, empowering Technical Deployment Leads (TDLs), Forward Deployed Engineers (FDEs), and Agentic Transformation Leads (ATLs) to architect, deploy, and prove the business value of mission-critical AI solutions.

---

## 📋 Prerequisites (What to Install First)

Before installing or running `delta-skills`, ensure the following dependencies are installed on your machine:

### 1. Core Runtime Runtimes & Package Managers
* **Node.js 18+ & npx**: Required for skill installation CLI and Node-based tool agents.
  ```bash
  node -v  # Should be v18.0.0 or higher
  ```
* **Python 3.10+ & `uv`**: Required for executing Python installer scripts and agent evaluation loops.
  ```bash
  python3 --version
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Supported AI Agent Framework (At Least One)
* **Antigravity CLI** (`agy`) OR
* **Google Agents CLI / Gemini CLI** (`agents-cli` / `gemini`) OR
* **Claude Code / Cursor / OpenAI Codex**

### 3. Base Upstream Skill Packs
`delta-skills` orchestrates base skills across PM, engineering, and agent security. Install the upstream skill packs beforehand:

```bash
# 1. Addy Osmani's Production Agent Skills
npx skills add addyosmani/agent-skills

# 2. Paweł Huryn's PM Skills Marketplace
# Installed into your global config (~/.gemini/config/plugins/) or ~/.agents/skills

# 3. Matt Pocock's Engineering & Productivity Skills
# Installed into your global config (~/.gemini/config/plugins/) or ~/.agents/skills

# 4. Google Cloud Agents CLI Skills
agents-cli update
```

---

## 📦 Installed Meta-Skills

### 1. `tdl-field-guide` (12-Week TDL Operational Playbook)
* **Trigger Phrases**: `"tdl field guide"`, `"tdl playbook"`, `"run tdl engagement"`, `"delta squad execution"`
* **Description**: Orchestrates 12-week enterprise engagements across the 4 field phases (Discover/Define ➔ Prototype/Validate ➔ Production Build ➔ Harden/Launch), enforcing the 6-role squad matrix, 1-in-1-out scope control, synthetic baseline capture, and the 14-skill streamlined stack.

### 2. `e2e-delivery-workflow` (7-Phase SDLC Methodology)
* **Trigger Phrases**: `"e2e workflow"`, `"deliver project end to end"`, `"e2e delivery"`, `"run full delivery workflow"`
* **Description**: Master software engineering methodology orchestrator guiding projects step-by-step through the 7-phase delivery lifecycle.

---

## ⚡ Quick Start & Installation

### Antigravity CLI (Native Plugin)
```bash
agy plugin install https://github.com/enriquekalven/delta-skills.git
```

### Gemini CLI / Google Agents CLI
```bash
gemini skills install https://github.com/enriquekalven/delta-skills.git --path skills
```

### Open Skills Standard (Claude Code, Cursor, Codex)
```bash
npx skills add enriquekalven/delta-skills
```

---

## 📄 Documentation & Guides

* [End-to-End Delivery Workflow Methodology](docs/e2e-delivery-workflow.md)
* [AlphaEvolve Multi-Domain Evaluation Matrix](docs/alphaevolve-masterclass-matrix.md)
* [Phase-Gated Meta-Skill Execution Model](docs/phase-gated-execution-model.md)

---

## 📜 License
Licensed under the [Apache-2.0 License](LICENSE).
