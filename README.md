# TDL User Guide

An operational toolkit of **13 TDL-exclusive agentic skills** and **4 deterministic Python CLI tools** for executing a **12-week Google Cloud AI / Agent Delta engagement** (`go/delta-delivery-guide`)—from **Week 0 qualification and onsite discovery** through **As-Is ethnography, Golden Dataset baseline evaluation metrics, CUJ & Agentic PRD authoring, 4-pillar technical specification, Stitch/Delta-brand prototyping, goal-driven code generation, recursive fan-out load testing, LLM-as-a-Judge statistical auditing (CLA + AUA), and Phase 3 ROI closeout**.

Full skill registry and artifact dependency graph: **[`SKILL.md`](SKILL.md)**.

---

## Table of Contents

1. [Architecture of This Repository: 13 TDL-Exclusive Skills](#1-architecture-of-this-repository-13-tdl-exclusive-skills)
2. [Recommended Companion Skills (`npx skills add`)](#2-recommended-companion-skills-npx-skills-add)
3. [Quick Start & Shared Workspace File Contracts](#3-quick-start--shared-workspace-file-contracts)
4. [How to Run a 12-Week Delta Engagement Step-by-Step](#4-how-to-run-a-12-week-delta-engagement-step-by-step)
5. [Deterministic CLI Calculators & Harness Reference](#5-deterministic-cli-calculators--harness-reference)
6. [Complete 13-Skill Catalog & 18-Asset TDL Toolbox Mapping](#6-complete-13-skill-catalog--18-asset-tdl-toolbox-mapping)
7. [Worked Examples, Validation & CI Drift Guards](#7-worked-examples-validation--ci-drift-guards)

---

## 1. Architecture of This Repository: 13 TDL-Exclusive Skills

This repository contains **only Google Cloud Delta / TDL methodology and deterministic calculators** that do not exist in public skill registries:
- **10 skills codify 100% of the 18 official assets from the TDL Toolbox** (`go/delta-delivery-guide` and its linked Google Docs, Sheets, and Slides decks).
- **3 skills are Google Cloud TDL engineering & ROI accelerators** (`gcp-agent-architecture-advisor`, `ai-value-sizing`, and `claude-agent-harness`).
- **Zero Commodity Duplicates:** Outdated local clones of generic skills (`frontend-design`, `skill-creator`, `prompt-engineer`, `product-feature-md`, `strategy-house`, and the 17-skill `strategy-agent` consulting folder) have been removed. The 1-page Delta Brand palette (`Toolbox #13`) is folded into [`stitch-design`](prototyping/stitch-design/SKILL.md), and the LLM token pricing/routing table (`model-economics-config.json`) is folded into [`gcp-agent-architecture-advisor`](delivery/gcp-agent-architecture-advisor/SKILL.md).

---

## 2. Recommended Companion Skills (`npx skills add`)

For general software engineering, React/UI implementation, browser verification, and Google ADK code patterns, install the top trending upstream skills from **[`skills.sh`](https://skills.sh)** alongside this repository:

```bash
# 1. Google ADK Official Skills (496K+ installs — ADK Python patterns, scaffolding, eval, deploy, Cloud Trace observability, Gemini Enterprise publish)
npx skills add google/agents-cli

# 2. Matt Pocock Engineering Workflow Skills (1.4M+ installs — grill-me, grill-with-docs, tdd, to-spec, to-tickets, code-review, diagnosing-bugs, handoff)
npx skills add mattpocock/skills

# 3. Vercel React, Web UI & Composition Best Practices (802K+ installs — vercel-react-best-practices, web-design-guidelines, vercel-composition-patterns)
npx skills add vercel-labs/agent-skills

# 4. Vercel Headless Agent Browser Verification (1.1M+ installs — live DOM inspection, console error capture, E2E flow verification)
npx skills add vercel-labs/agent-browser

# 5. Anthropic Official Skills (988K+ installs — frontend-design, webapp-testing, mcp-builder, pptx, xlsx, docx, pdf, skill-creator)
npx skills add anthropics/skills

# 6. High-Taste UI & Google Stitch Prompting (612K+ installs — design-taste-frontend, stitch-design-taste, high-end-visual-design)
npx skills add leonxlnx/taste-skill
```

| Engagement Need | Use This Repo (`tool-tdl-user-guide`) For | Pair With Companion Skill (`skills.sh`) |
| :--- | :--- | :--- |
| **Discovery & Scope Lock** | `workshop-intake`, `create-delta-ucc`, `cuj-architect`, `business-process-redesign` | `mattpocock/skills/grill-me` & `grill-with-docs` |
| **PRD, Specs & Tickets** | `product-md` (`go/delta-prd-template`), `specification-engineer` (`go/delta-squad-agent-specs`) | `mattpocock/skills/to-tickets` & `domain-modeling` |
| **Prototyping & Frontend UI** | `stitch-design` (3-stage TDL Prototyping Guide `#15` + Delta Brand `#13`) | `leonxlnx/taste-skill/stitch-design-taste`, `anthropics/skills/frontend-design`, `vercel-labs/agent-skills/web-design-guidelines` |
| **ADK Build & Testing** | `gcp-agent-architecture-advisor`, `claude-agent-harness` | `google/agents-cli` (`adk-code`, `scaffold`, `deploy`), `mattpocock/skills/tdd`, `vercel-labs/agent-browser` |
| **Load Testing & Judge Eval** | `agent-load-testing` (`calculate_agent_quotas.py`), `agent-eval-statistical-auditing` (`audit_llm_judge.py`) | `google/agents-cli/google-agents-cli-eval` & `google-agents-cli-observability` |
| **Decks & Workbooks** | `tdl-field-guide` (`STATE.md`, Kickoff/Demo/Closeout/Retro structure, 7-tab Program Tracker) | `anthropics/skills/pptx` & `anthropics/skills/xlsx` |

---

## 3. Quick Start & Shared Workspace File Contracts

### Install the TDL User Guide Skills
```bash
git clone https://github.com/delta-fde/tool-tdl-user-guide.git tdl-user-guide
cd tdl-user-guide
python3 scripts/validate_skills.py
```

- **With `skills` CLI:** `npx skills add delta-fde/tool-tdl-user-guide`
- **In Antigravity / Gemini CLI / Claude Code:** Symlink or copy into `~/.gemini/config/plugins/tdl-user-guide/` (or point your agent directly at `tdl-user-guide/SKILL.md`).

### Shared Workspace File Contracts
Skills communicate through explicit markdown and JSON artifacts in the customer repository (`docs/` and `STATE.md`). Downstream skills automatically consume the outputs of upstream skills:

```text
customer-engagement-repo/
├── STATE.md                              # Written & updated by tdl-field-guide (gates, sprints, dual RAID logs)
├── docs/
│   ├── WORKSHOP_INTAKE.md                # Written by workshop-intake (33 Starter Qs + 6-Dim Data Yardstick)
│   ├── USE_CASE_CANVAS.md                # Written by create-delta-ucc (4-Tab UCC + MVP Alignment Summary)
│   ├── as_is_report.md                   # Written by business-process-redesign (Task decomposition + operational baseline)
│   ├── to_be_designs.md                  # Written by business-process-redesign (L1/L2/L3 agent workflow)
│   ├── human_agent_roles.md              # Written by business-process-redesign (HITL & escalation matrix)
│   ├── CUJ_MAP.md                        # Written by cuj-architect (4-Tab Ethnography, L1-L5 CUJs, 0.6V+0.4F)
│   ├── PRD.md                            # Written by product-md (8-section Agentic PRD + prompt/eval specs)
│   ├── ARCHITECTURE_RECOMMENDATION.md    # Written by gcp-agent-architecture-advisor (Tier 1/2/3 + model economics)
│   ├── TDD.md                            # Written by specification-engineer (Parts I-IV + Golden Dataset baseline evals)
│   ├── STITCH_PROTOTYPE.md               # Written by stitch-design (3-stage prototyping + Delta Brand #13 + Stitch MCP)
│   ├── DEMO_FRAME_UP.md                  # Written by tdl-field-guide (Pillar / Feature ID / Demo 1-2-3 matrix)
│   ├── LOAD_TEST_REPORT.md               # Written by agent-load-testing (fan-out math, 5x quota, Locust SSE)
│   ├── EVAL_AUDIT_REPORT.md              # Written by agent-eval-statistical-auditing (27 CLA + 3 AUA pipelines)
│   └── VALUE_SIZING.md                   # Written by ai-value-sizing (post-launch ROI vs. Phase 1 baseline)
└── .harness/
    └── last_run_report.json              # Written by claude-agent-harness goal loop
```

---

## 4. How to Run a 12-Week Delta Engagement Step-by-Step

The workflow below follows the official **`go/delta-delivery-guide`** lifecycle (**Prelude $\rightarrow$ Phase 1 $\rightarrow$ Phase 2 $\rightarrow$ Phase 3**).

### Prelude: Pre-Engagement Qualification & Intake (Week 0)
Before committing a squad or starting the 12-week clock, qualify the candidate use cases and verify data readiness.

1. **Capture Discovery Notes & Score the Data Yardstick (`workshop-intake`):**
   - **Read:** [`workshop-intake/SKILL.md`](workshop-intake/SKILL.md)
   - **Action:** Run the **33 Starter Questions** and score the **6-Dimension Data Yardstick** (`Data Availability`, `Accessibility`, `Quality`, `Coverage`, `Privacy/Security`, `Latency`).
   - **Output:** `docs/WORKSHOP_INTAKE.md` (see example: [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md)).
2. **Prioritize Use Cases & Lock the 1-Page MVP Alignment Summary (`create-delta-ucc`):**
   - **Read:** [`usecase-canvas/create-delta-ucc/SKILL.md`](usecase-canvas/create-delta-ucc/SKILL.md)
   - **Action:** Score candidate initiatives across the 4-Tab Use Case Canvas and produce the **1-Page Use Case Alignment Summary** (`Problem Statement`, `Target Users`, `MVP Scope`, `Out of Scope`, `Success Metrics`, `Key Dependencies`).
   - **Output:** `docs/USE_CASE_CANVAS.md` (see example: [`customer-onboarding-ucc.md`](usecase-canvas/create-delta-ucc/examples/customer-onboarding-ucc.md)).
3. **Initialize Engagement Governance (`tdl-field-guide`):**
   - **Read:** [`delivery/tdl-field-guide/SKILL.md`](delivery/tdl-field-guide/SKILL.md)
   - **Action:** Initialize `STATE.md` with the 7-tab Program Tracker structure (`Timeline`, `Use Cases`, `Staffing`, `Use Case RAID`, `Program RAID`, `Meetings`, `OOO`) and confirm Prelude exit criteria (Part III Developer Clearance signed, Golden Dataset reachable).

---

### Phase 1: Foundations — Ethnography, Golden Dataset Eval Baseline, PRD & Architecture (Weeks 1–2)
Deconstruct the current manual workflow, establish baseline evaluation metrics on the curated Golden Dataset, lock the Agentic PRD, and complete the 4-part Technical Specification before writing production code.

1. **Deconstruct the "As-Is" Workflow & Design the "To-Be" Agent Process (`business-process-redesign`):**
   - **Read:** [`business-process-redesign/SKILL.md`](business-process-redesign/SKILL.md)
   - **Output:** `docs/as_is_report.md`, `docs/to_be_designs.md`, and `docs/human_agent_roles.md` (see examples: [`as_is_report.md`](business-process-redesign/examples/as_is_report.md), [`to_be_designs.md`](business-process-redesign/examples/to_be_designs.md), [`human_agent_roles.md`](business-process-redesign/examples/human_agent_roles.md)).
2. **Map L1–L5 Critical User Journeys & AI Touchpoints (`cuj-architect`):**
   - **Read:** [`cuj-architect/SKILL.md`](cuj-architect/SKILL.md)
   - **Action:** Complete the 4-tab CUJ workbook structure (Ethnography $\rightarrow$ Pain Points $\rightarrow$ L1–L5 Journey Steps $\rightarrow$ AI Touchpoint Matrix scored by `Priority = 0.6 × Value + 0.4 × Feasibility`).
   - **Output:** `docs/CUJ_MAP.md` (see examples: [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md), [`cloud-support-triage-cuj.md`](cuj-architect/examples/cloud-support-triage-cuj.md)).
3. **Author the 8-Section Agentic PRD (`product-md`):**
   - **Read:** [`product-management/product-md/SKILL.md`](product-management/product-md/SKILL.md)
   - **Output:** `docs/PRD.md` following `go/delta-prd-template` including System Prompt Architecture and Evaluation Rubrics (see examples: [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md), [`enterprise-claims-agent-prd.md`](product-management/product-md/examples/enterprise-claims-agent-prd.md)).
4. **Select the GCP Agent Architecture Tier (`gcp-agent-architecture-advisor`):**
   - **Read:** [`delivery/gcp-agent-architecture-advisor/SKILL.md`](delivery/gcp-agent-architecture-advisor/SKILL.md)
   - **Action:** Compare Tier 1 (Gemini Enterprise no-code), Tier 2 (ADK on Agent Runtime), and Tier 3 (ADK self-hosted on Cloud Run / GKE), verifying current GCP launch stages (`GA` vs. `Preview`) and grounding token economics in [`model-economics-config.json`](delivery/gcp-agent-architecture-advisor/references/model-economics-config.json).
   - **Output:** `docs/ARCHITECTURE_RECOMMENDATION.md` (see example: [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md)).
5. **Write the 4-Part Agent Technical Specification & Establish Golden Dataset Baseline Metrics (`specification-engineer`):**
   - **Read:** [`utils/specification-engineer/SKILL.md`](utils/specification-engineer/SKILL.md)
   - **Action:** Document Parts I–IV (`System Overview`, `Agent Architecture & Orchestration`, `Developer Access & Tools`, `Evaluation & Operations`) and the 4 Pillars per `go/delta-squad-agent-specs`, establishing the baseline evaluation metrics on the curated Golden Dataset (`Part IV`) as the north star for all implementation sprints.
   - **Output:** `docs/TDD.md` (see examples: [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md), [`claims-extraction-service-tdd.md`](utils/specification-engineer/examples/claims-extraction-service-tdd.md)).
6. **Pass Phase Gate 1 (`tdl-field-guide`):** Verify all Phase 1 exit artifacts (`docs/PRD.md`, `docs/TDD.md`, Golden Dataset baseline metrics) are signed off in `STATE.md` before starting Sprint 1.

---

### Phase 2: Core Build & Bi-Weekly Demo Sprints (Weeks 3–10 — Four 2-Week Sprints)
Execute four 2-week sprints (**Sprint 1 [W3–4]**, **Sprint 2 [W5–6]**, **Sprint 3 [W7–8]**, **Sprint 4 [W9–10]**) with three customer-facing milestone demos (**Demo 1 [W4]**, **Demo 2 [W6]**, **Demo 3 [W8/W10]**).

1. **Rapid UI Prototyping & Brand Alignment (`stitch-design`):**
   - **Read:** [`prototyping/stitch-design/SKILL.md`](prototyping/stitch-design/SKILL.md)
   - **Action:** Execute the 3-stage prototyping workflow (7-step hypothesis-to-mini-eval loop + Stitch MCP screen generation) using Delta Brand & Material 3 tokens (`Toolbox #13`: `#4285F4`, `#34A853`, `#FBBC04`, `#EA4335`, Google Sans / Roboto / Roboto Mono) and audit against [`ui-review-checklist.md`](prototyping/stitch-design/references/ui-review-checklist.md).
   - **Output:** `docs/STITCH_PROTOTYPE.md` (see examples: [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md), [`agent-ops-console-prototype.md`](prototyping/stitch-design/examples/agent-ops-console-prototype.md)).
2. **Run Goal-Driven Implementation Loops (`claude-agent-harness`):**
   - **Read:** [`ai-coding/claude-agent-harness/SKILL.md`](ai-coding/claude-agent-harness/SKILL.md)
   - **Action:** Run [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py) against `docs/PRD.md` and `docs/TDD.md` with deterministic `--verify-cmd` acceptance gates (unit tests, linter, typecheck) until all commands exit `0`.
   - **Output:** Verified `src/`, `tests/`, and `.harness/last_run_report.json`.
3. **Sprints 3–4 Production Load Testing & Quota Sizing (`agent-load-testing`):**
   - **Read:** [`delivery/agent-load-testing/SKILL.md`](delivery/agent-load-testing/SKILL.md)
   - **Action:** Run [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py) to calculate recursive fan-out calls per turn (`1 + Qt + Qt·Cq + 1`), peak RPM/TPM, and **5x safety-margin Vertex AI quota requests**, then execute Locust SSE streaming load tests and apply context/payload optimizations.
   - **Output:** `docs/LOAD_TEST_REPORT.md` (see example: [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md)).
4. **Sprints 3–4 Linguistic Quality (CLA) & Statistical Judge Auditing (`agent-eval-statistical-auditing`):**
   - **Read:** [`delivery/agent-eval-statistical-auditing/SKILL.md`](delivery/agent-eval-statistical-auditing/SKILL.md)
   - **Action:** Evaluate agent outputs against the **27 Communication & Linguistic Assessment (CLA) criteria** and audit your LLM-as-a-Judge against human SME consensus across all 3 pipelines using [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py) (`Pearson r ≥ 0.80`, `ICC(2,1) ≥ 0.75`, `Krippendorff's α ≥ 0.67`, `Quadratic Weighted Kappa ≥ 0.70`, `|Bias| ≤ 0.15`, `Compression Ratio ≥ 0.80`).
   - **Output:** `docs/EVAL_AUDIT_REPORT.md` (see example: [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md)).
5. **Pass Phase Gate 2 (`tdl-field-guide`):** Frame up each bi-weekly demo in `docs/DEMO_FRAME_UP.md` (`Pillar | Feature ID | Demo 1/2/3 | Status`) and enforce the **1-in-1-out scope swap rule** in `STATE.md`.

---

### Phase 3: Final Read-Out & Close (Weeks 11–12)
Quantify post-launch value against the Phase 1 operational baseline, deliver the executive closeout readout, and transition ownership to the client team.

1. **Calculate Measured ROI vs. Phase 1 Baseline (`ai-value-sizing`):**
   - **Read:** [`ai-value-sizing/SKILL.md`](ai-value-sizing/SKILL.md)
   - **Action:** Run [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) comparing the Phase 1 operational baseline (`docs/as_is_report.md` / `docs/USE_CASE_CANVAS.md`) against post-deployment telemetry across Base, Bull, and Bear scenarios.
   - **Output:** `docs/VALUE_SIZING.md` (see example: [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md)).
2. **Executive Closeout Deck, Handoff & Blameless Retro (`tdl-field-guide`):**
   - **Read:** [`delivery/tdl-field-guide/SKILL.md`](delivery/tdl-field-guide/SKILL.md)
   - **Action:** Compile the Closeout Slide Deck, close or transfer all items in the Use Case RAID and Program RAID logs, and facilitate the FDE Blameless Retrospective (`STATE.md`).

---

## 5. Deterministic CLI Calculators & Harness Reference

All calculators use **only the Python 3 standard library** (except `call_opus_model_garden.py`, which calls Vertex AI Model Garden when executed live) and expose all assumptions via CLI flags.

### 1. Multi-Agent Fan-Out & Vertex AI 5x Quota Calculator (`calculate_agent_quotas.py`)
Implements Said Kuwel's recursive tool fan-out formula (`Total Calls = 1 + Qt + (Qt × Cq) + 1`) and 5x safety-margin quota sizing from the TDL Load Testing Guide (`Toolbox #16`).

```bash
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py \
  --qt 6 \
  --cq 4 \
  --tokens-per-call 20000 \
  --peak-turns-per-min 10 \
  --safety-multiplier 5.0
```

### 2. LLM-as-a-Judge Statistical Auditor (`audit_llm_judge.py`)
Runs Héctor González's 3-pipeline Agreement & Uncertainty Analysis (AUA) certification (`Pearson r`, `Spearman ρ`, `ICC(2,1)`, `Krippendorff's α`, `Quadratic Weighted Kappa`, `Mean Bias`, `Compression Ratio`, `Flip Rate`, and `Mean Entropy`) on paired human SME and LLM judge ratings (`Toolbox #18`).

```bash
# Audit the bundled calibrated judge fixture (PASS)
python3 delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py \
  --input delivery/agent-eval-statistical-auditing/examples/fixtures/calibrated_judge.json

# Audit the bundled compressed/lenient judge fixture (FAIL)
python3 delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py \
  --input delivery/agent-eval-statistical-auditing/examples/fixtures/compressed_lenient_judge.json
```

### 3. 3-Scenario AI Value Sizing & NPV Calculator (`calculate_roi.py`)
Computes gross labor savings, CapEx/OpEx, net annual benefit, 3-year NPV, ROI %, and payback period across Base, Bull, and Bear scenarios.

```bash
python3 ai-value-sizing/scripts/calculate_roi.py \
  --tam-units 80000 \
  --sam-share 0.625 \
  --adoption-rate 0.30 \
  --tech-compat 0.80 \
  --hours-saved 0.70 \
  --hourly-rate 75.0 \
  --capex 180000 \
  --annual-opex 68000 \
  --vcr 0.5912 \
  --scdf 0.85 \
  --wacc 0.10
```

### 4. Vertex AI Model Garden Goal-Loop Harness (`call_opus_model_garden.py`)
Runs an iterative code-generation and verification loop on Vertex AI Model Garden until every `--verify` command passes.

```bash
python3 ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py \
  --project "$GOOGLE_CLOUD_PROJECT" \
  --workspace . \
  --goal "Implement the FNOL extraction service per docs/TDD.md" \
  --spec docs/PRD.md \
  --spec docs/TDD.md \
  --verify "python3 -m unittest discover -s tests -p 'test_*.py'" \
  --dry-run
```

---

## 6. Complete 13-Skill Catalog & 18-Asset TDL Toolbox Mapping

### Part A: The 18 Official TDL Toolbox Assets $\rightarrow$ 10 Skills

| # | Official TDL Toolbox Asset | Author | Mapped Skill | Template / Script & Worked Example |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Onsite Discovery Workshop Deck | E. Markman | [`workshop-intake`](workshop-intake/SKILL.md) | [`intake-template.md`](workshop-intake/references/intake-template.md) · [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md) |
| **02** | Re-imagine Business Processes (`delta /forward`) | B. Araujo | [`business-process-redesign`](business-process-redesign/SKILL.md) | [`discovery-deconstruction.md`](business-process-redesign/references/discovery-deconstruction.md) · [`as_is_report.md`](business-process-redesign/examples/as_is_report.md) · [`to_be_designs.md`](business-process-redesign/examples/to_be_designs.md) · [`human_agent_roles.md`](business-process-redesign/examples/human_agent_roles.md) |
| **03** | CUJ Definition Templates (4-tab workbook; `0.6·Value + 0.4·Feasibility`) | R. Hennessy | [`cuj-architect`](cuj-architect/SKILL.md) | [`output-template.md`](cuj-architect/references/output-template.md) · [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md) *(adapted from toolbox workbook)* |
| **04** | Use Case Alignment Summary | E. Markman | [`create-delta-ucc`](usecase-canvas/create-delta-ucc/SKILL.md) | [`ucc-template.md`](usecase-canvas/create-delta-ucc/references/ucc-template.md) · [`customer-onboarding-ucc.md`](usecase-canvas/create-delta-ucc/examples/customer-onboarding-ucc.md) |
| **05** | Agentic PRD Template (`go/delta-prd-template`) + Intel AskIT Example | E. Chan | [`product-md`](product-management/product-md/SKILL.md) | [`prd-template.md`](product-management/product-md/references/prd-template.md) · [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md) *(adapted from toolbox PRD)* |
| **06** | Example Kickoff Deck | E. Markman | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **07** | Demo Frame-Up Deck (Intel AskHR, 3 demos, 39 features) | M. Ammar | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **08** | Closeout Slide Deck Template | E. Markman | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **09** | FDE Blameless Retro Slides | E. Markman | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **10** | Use Case Selection Guidelines (33 Starter Qs + 6-Dim Data Yardstick) | J. Pashutinski | [`workshop-intake`](workshop-intake/SKILL.md), [`create-delta-ucc`](usecase-canvas/create-delta-ucc/SKILL.md) | [`intake-template.md`](workshop-intake/references/intake-template.md) · [`ucc-template.md`](usecase-canvas/create-delta-ucc/references/ucc-template.md) |
| **11** | 12-Week Delivery Guide (`go/delta-delivery-guide`) | J. Pashutinski | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **12** | Program Tracker (7 tabs: Timeline, Use Cases, Staffing, Use Case RAID, Program RAID, Meetings, OOO) | E. Markman | [`tdl-field-guide`](delivery/tdl-field-guide/SKILL.md) | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **13** | Delta Brand & UI Guidelines (Google colors, typography, co-branding) | Delta Design | [`stitch-design`](prototyping/stitch-design/SKILL.md) | [`ui-review-checklist.md`](prototyping/stitch-design/references/ui-review-checklist.md) · [`agent-ops-console-prototype.md`](prototyping/stitch-design/examples/agent-ops-console-prototype.md) |
| **14** | Agent Technical Specifications (`go/delta-squad-agent-specs`) | C. Clark | [`specification-engineer`](utils/specification-engineer/SKILL.md) | [`tdd-spec-template.md`](utils/specification-engineer/references/tdd-spec-template.md) · [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md) *(adapted from toolbox spec)* |
| **15** | TDL Prototyping Guide (3 stages + 7-step loop + Stitch MCP workflow) | S. Srinivasan | [`stitch-design`](prototyping/stitch-design/SKILL.md) | [`stitch-mcp-workflow.md`](prototyping/stitch-design/references/stitch-mcp-workflow.md) · [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md) |
| **16** | Load Testing, Parallelism, Quotas & Optimizations Guide (NSH Clinician Search) | S. Kuwel | [`agent-load-testing`](delivery/agent-load-testing/SKILL.md) | [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py) · [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) *(exact guide math)* |
| **17** | Linguistic Output Quality Evaluation Framework (CLA, 27 criteria) | H. González | [`agent-eval-statistical-auditing`](delivery/agent-eval-statistical-auditing/SKILL.md) | [`cla-rubric-and-aua-methodology.md`](delivery/agent-eval-statistical-auditing/references/cla-rubric-and-aua-methodology.md) |
| **18** | Statistical Auditing for LLM-as-a-Judge (3 pipelines, AUA report) | H. González | [`agent-eval-statistical-auditing`](delivery/agent-eval-statistical-auditing/SKILL.md) | [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py) · [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) *(deck report + fixture output)* |

### Part B: The 3 Google Cloud TDL Engineering & ROI Skills

| Skill | Category | Output Artifact(s) | Script / Reference & Worked Example |
| :--- | :--- | :--- | :--- |
| **[`gcp-agent-architecture-advisor`](delivery/gcp-agent-architecture-advisor/SKILL.md)** | GCP Architecture | `docs/ARCHITECTURE_RECOMMENDATION.md` | [`model-economics-config.json`](delivery/gcp-agent-architecture-advisor/references/model-economics-config.json) · [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md) |
| **[`ai-value-sizing`](ai-value-sizing/SKILL.md)** | Value Realization | `docs/VALUE_SIZING.md` | [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) · [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md) |
| **[`claude-agent-harness`](ai-coding/claude-agent-harness/SKILL.md)** | Goal-Loop Coding | Verified `src/`, `tests/`, `.harness/last_run_report.json` | [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py) · [`spec-to-production-code.md`](ai-coding/claude-agent-harness/examples/spec-to-production-code.md) |

---

## 7. Worked Examples, Validation & CI Drift Guards

### Provenance of Worked Examples
- **Adapted from Real TDL Toolbox Artifacts (4 examples):** [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md) (`Toolbox #05`), [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md) (`Toolbox #14`), [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md) (`Toolbox #03`), and [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) (`Toolbox #16`).
- **Real Deck Report + Deterministic Bundled Fixtures (1 example):** [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) (`Toolbox #18` + [`calibrated_judge.json`](delivery/agent-eval-statistical-auditing/examples/fixtures/calibrated_judge.json) & [`compressed_lenient_judge.json`](delivery/agent-eval-statistical-auditing/examples/fixtures/compressed_lenient_judge.json)).
- **Unified Illustrative Scenario (Remaining Examples):** Uses one consistent *fictional* thread (**Acme P&C — Commercial Auto Claims FNOL**) so every artifact references upstream and downstream files across all 12 weeks.

### Run the Repository Validator & Unit Test Suites
```bash
# 1. Validate all SKILL.md frontmatter, links, JSON files, code fences, and orphan/duplicate rules
python3 scripts/validate_skills.py

# 2. Run repository validator unit tests + example-to-script stdout drift guards (17 tests)
python3 -m unittest discover -s scripts -p 'test_*.py'

# 3. Run Claude Agent Harness unit tests (25 tests)
python3 -m unittest discover -s ai-coding/claude-agent-harness/scripts -p 'test_*.py'
```
