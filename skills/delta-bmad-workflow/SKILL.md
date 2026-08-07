---
name: delta-bmad-workflow
description: Master Spec-Driven Development (SDD) workflow bridge mapping BMAD Method's 8-step daisy-chain sequence to Google Cloud Delta Squad enterprise field playbooks, GCP architecture advisory, and ZDR multi-model routing.
triggers:
  - "delta bmad workflow"
  - "marry bmad and delta"
  - "bmad gcp integration"
  - "bmad delivery with delta skills"
  - "gcp bmad workflow"
  - "sdd bmad workflow"
---

# Delta-BMAD Master Spec-Driven Development (SDD) Bridge (`delta-bmad-workflow`)

> **Bridge Purpose**: Seamlessly marries the **BMAD Method 8-Step Spec-Driven Development (SDD) Daisy-Chain** with **Google Cloud Delta Squad Enterprise Field Execution Skills**. Enforces standardized artifact output paths (`docs/spec/`) so every step feeds into the next.

---

## 1. Standardized BMAD Artifact Path Structure (`docs/spec/`)

All BMAD and Delta skills interact with standardized workspace paths configured in `.agents/_bmad/config.toml`:

```text
{project-root}/
├── docs/spec/
│   ├── project-context.md               <-- Step 1: Technology stack & architecture guardrails
│   ├── plans/
│   │   ├── brainstorming/               <-- Step 2: Analysis & brainstorming outputs
│   │   ├── prd/                         <-- Step 3: Functional/NFR PRDs & GCP Architecture Advisor
│   │   └── epics-and-stories.md         <-- Step 4: Epics & Story breakdown
│   └── implementation/
│       ├── sprint-status.yaml           <-- Step 5: Sprint backlog status
│       ├── 1-1-story.md                 <-- Step 6: Dedicated story specification
│       └── code-review-report.md        <-- Step 8: Live Opus 5 ZDR code review report
```

---

## 2. The 8-Step SDD Daisy-Chain Integration

```
flowchart TD
    S1["1. Onboarding<br>(/bmad-generate-project-context + codebase-onboarding)"] --> A1["📄 docs/spec/project-context.md"]
    A1 --> S2["2. Analysis<br>(/bmad-brainstorming + synthetic-baseline-protocol)"]
    S2 --> A2["📄 docs/spec/plans/brainstorming-output.md<br>📄 baseline_kpis.json"]
    A2 --> S3["3. Planning<br>(/bmad-prd + gcp-agent-architecture-advisor)"]
    S3 --> A3["📄 docs/spec/plans/prd/prd.md<br>📄 gcp_architecture_recommendation.md"]
    A3 --> S4["4. Solutioning<br>(/bmad-create-epics-and-stories + tdl-field-guide)"]
    S4 --> A4["📄 docs/spec/plans/epics-and-stories.md"]
    A4 --> S5["5. Backlog<br>(/bmad-sprint-planning + e2e-delivery-workflow)"]
    S5 --> A5["📄 docs/spec/implementation/sprint-status.yaml"]
    A5 --> S6["6. Create Story<br>(/bmad-create-story)"]
    S6 --> A6["📄 docs/spec/implementation/1-1-story.md"]
    A6 --> S7["7. Code Story<br>(/bmad-dev-story + claude-agent-harness)"]
    S7 --> A7["💻 Source Code Implementation"]
    A7 --> S8["8. Review Story<br>(/bmad-code-review + claude-review)"]
    S8 --> A8["📄 docs/spec/implementation/code-review-report.md"]
```

---

## 3. Mapping Milestone Matrix

| Step | SDD Milestone | BMAD Core Skill | Integrated Delta Skill | Artifact Created |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Onboarding** | `/bmad-generate-project-context` | `codebase-onboarding-and-mapping` | `docs/spec/project-context.md`<br>`docs/ONBOARDING.md` |
| **2** | **Analysis** | `/bmad-brainstorming` | `synthetic-baseline-protocol` | `docs/spec/plans/brainstorming-output.md`<br>`baseline_kpis.json` |
| **3** | **Planning** | `/bmad-prd` | `gcp-agent-architecture-advisor` | `docs/spec/plans/prd/prd.md`<br>`gcp_architecture_recommendation.md` |
| **4** | **Solutioning** | `/bmad-create-epics-and-stories` | `tdl-field-guide` | `docs/spec/plans/epics-and-stories.md` |
| **5** | **Backlog** | `/bmad-sprint-planning` | `e2e-delivery-workflow` | `docs/spec/implementation/sprint-status.yaml` |
| **6** | **Create Story** | `/bmad-create-story` | `e2e-delivery-workflow` | `docs/spec/implementation/1-1-story.md` |
| **7** | **Code Story** | `/bmad-dev-story` | `claude-agent-harness` | Source Code Files (`index.html`, `app.js`, etc.) |
| **8** | **Review Story** | `/bmad-code-review` | `claude-review` (Model Garden ZDR Opus 5) | `docs/spec/implementation/code-review-report.md` |

---

## 4. Execution Commands

```bash
# Install Delta Skills into BMAD Method environment
npx bmad-method install --custom https://github.com/enriquekalven/delta-skills

# Run unified SDD Bridge workflow in Antigravity or Gemini CLI
agy skill run delta-bmad-workflow
```
