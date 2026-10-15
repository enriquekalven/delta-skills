# Delta Skills (`delta-skills`)

An operational collection of **22 agentic skills** and **6 deterministic Python CLI tools** for executing a **12-week Google Cloud AI / Agent Delta engagement** (`go/delta-delivery-guide`)—from **Week 0 qualification and onsite discovery** through **As-Is ethnography, 50-sample baseline auditing, CUJ & Agentic PRD authoring, 4-pillar technical specification, Stitch/M3 prototyping, goal-driven code generation, recursive fan-out load testing, LLM-as-a-Judge statistical auditing (CLA + AUA), and Phase 3 ROI closeout**.

Full skill registry and artifact dependency graph: **[`SKILL.md`](SKILL.md)**.

---

## Table of Contents

1. [What Is in This Repository (and What Was Cleaned Up)](#1-what-is-in-this-repository-and-what-was-cleaned-up)
2. [Quick Start: Installing & Using the Skills](#2-quick-start-installing--using-the-skills)
3. [How to Run a 12-Week Delta Engagement Step-by-Step](#3-how-to-run-a-12-week-delta-engagement-step-by-step)
4. [Deterministic CLI Calculators & Harness Reference](#4-deterministic-cli-calculators--harness-reference)
5. [Complete 22-Skill Catalog & TDL Toolbox Mapping](#5-complete-22-skill-catalog--tdl-toolbox-mapping)
6. [Worked Examples & Provenance Policy](#6-worked-examples--provenance-policy)
7. [Validation, CI Drift Guards & External Prerequisites](#7-validation-ci-drift-guards--external-prerequisites)

---

## 1. What Is in This Repository (and What Was Cleaned Up)

### Provenance Split: TDL Toolbox vs. Repo-Native
- **9 skills codify all 18 official assets from the TDL Toolbox** (`go/delta-delivery-guide` and its linked Google Docs, Sheets, and Slides decks).
- **13 skills are repo-native accelerators**: deterministic calculators, executive strategy frameworks, goal-driven coding harnesses, and prompt/skill utilities that complement the official toolbox.
- Every skill's `SKILL.md` states its exact provenance and explicitly labels any repository extension as *(repo convention)*.

### Legacy Cleanup Summary
All legacy scaffolds, duplicate persona files, and unreferenced templates have been removed:
- **Purged empty `.gitkeep` scaffolds** across `usecase-canvas/create-delta-ucc/{assets,references,scripts}`.
- **Removed 16 duplicate roleplay files** (`prototyping/frontend-design/references/design-council/*` and `prototyping/stitch-design/references/design-council/*`) in favor of single-pass engineering checklists ([`ui-review-checklist.md`](prototyping/frontend-design/references/ui-review-checklist.md) and [`stitch-mcp-workflow.md`](prototyping/stitch-design/references/stitch-mcp-workflow.md)).
- **Removed 11 unused strategy templates** (legacy report template stubs and orphaned `strategy-agent/ai-native-strategy/references/*` files) and consolidated `business-process-redesign/docs/*` into [`business-process-redesign/examples/`](business-process-redesign/examples/as_is_report.md).
- **Replaced prose-only math with zero-dependency Python 3 CLI calculators** verified by unit tests so worked examples never drift from script stdout.

---

## 2. Quick Start: Installing & Using the Skills

### Option A: Use Directly in Antigravity / Gemini CLI / Claude Code
Clone this repository and register it as a skill directory or open it alongside your customer engagement workspace:

```bash
git clone <repo-url> delta-skills
cd delta-skills
python3 scripts/validate_skills.py
```

- **In Antigravity / Gemini CLI:** Symlink or copy individual skill folders (or the repo as a plugin) into `~/.gemini/config/skills/` or `~/.gemini/config/plugins/delta-skills/`.
- **In a Customer Engagement Repo:** Point your coding agent at `delta-skills/SKILL.md` or invoke a specific skill by path (for example: *"Read `delta-skills/workshop-intake/SKILL.md` and generate `docs/WORKSHOP_INTAKE.md` from our discovery notes"*).

### Option B: How Skills Chain Together via Shared File Contracts
Skills communicate through explicit markdown and JSON artifacts in the customer repository (`docs/` and `STATE.md`). You do not need to copy-paste context between prompts—each downstream skill reads the files produced by upstream skills:

```text
customer-engagement-repo/
├── STATE.md                              # Written & updated by tdl-field-guide (gates, sprints, dual RAID logs)
├── docs/
│   ├── WORKSHOP_INTAKE.md                # Written by workshop-intake (33 Starter Qs + 6-Dim Data Yardstick)
│   ├── USE_CASE_CANVAS.md                # Written by create-delta-ucc (4-Tab UCC + MVP Alignment Summary)
│   ├── as_is_report.md                   # Written by business-process-redesign (Task decomposition + baseline)
│   ├── to_be_designs.md                  # Written by business-process-redesign (L1/L2/L3 agent workflow)
│   ├── human_agent_roles.md              # Written by business-process-redesign (HITL & escalation matrix)
│   ├── CUJ_MAP.md                        # Written by cuj-architect (4-Tab Ethnography, L1-L5 CUJs, 0.6V+0.4F)
│   ├── baseline_kpis.json                # Written by synthetic-baseline-protocol (frozen 50-sample baseline)
│   ├── PRD.md                            # Written by product-md (8-section Agentic PRD + prompt/eval specs)
│   ├── features/<feature_slug>.md        # Written by product-feature-md (sprint-scoped feature spec)
│   ├── ARCHITECTURE_RECOMMENDATION.md    # Written by gcp-agent-architecture-advisor (Tier 1 vs Tier 2 vs Tier 3)
│   ├── TDD.md                            # Written by specification-engineer (Parts I-IV + 4 Architectural Pillars)
│   ├── STITCH_PROTOTYPE.md               # Written by stitch-design (3-stage prototyping + Stitch MCP screens)
│   ├── DEMO_FRAME_UP.md                  # Written by tdl-field-guide (Why / What / How bi-weekly demo script)
│   ├── LOAD_TEST_REPORT.md               # Written by agent-load-testing (fan-out math, 5x quota, Locust SSE)
│   ├── EVAL_AUDIT_REPORT.md              # Written by agent-eval-statistical-auditing (27 CLA + 3 AUA pipelines)
│   ├── VALUE_SIZING.md                   # Written by ai-value-sizing (post-launch ROI vs. baseline_kpis.json)
│   ├── STRATEGY_HOUSE.md                 # Optional executive track: strategy-house
│   ├── STRATEGY_BRIEF.md                 # Optional executive track: strategy-partner-orchestrator
│   ├── AI_STRATEGY.md                    # Optional executive track: ai-native-strategy
│   └── FINANCIAL_CASE.md                 # Optional executive track: financial-strategy
└── .harness/
    └── last_run_report.json              # Written by claude-agent-harness goal loop
```

---

## 3. How to Run a 12-Week Delta Engagement Step-by-Step

The workflow below follows the official **`go/delta-delivery-guide`** lifecycle (**Prelude $\rightarrow$ Phase 1 $\rightarrow$ Phase 2 $\rightarrow$ Phase 3**).

### Prelude: Pre-Engagement Qualification & Intake (Week 0)
Before committing a squad or starting the 12-week clock, qualify the candidate use cases and verify data readiness.

1. **Capture Discovery Notes & Score the Data Yardstick (`workshop-intake`):**
   - **Read:** [`workshop-intake/SKILL.md`](workshop-intake/SKILL.md)
   - **Action:** Run the **33 Starter Questions** across Business Context, Users/Workflows, Technical Systems, and Risk, and score the **6-Dimension Data Yardstick** (`Data Availability`, `Accessibility`, `Quality`, `Coverage`, `Privacy/Security`, `Latency`).
   - **Output:** `docs/WORKSHOP_INTAKE.md` (see example: [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md)).
2. **Prioritize Use Cases & Lock the 1-Page MVP Alignment Summary (`create-delta-ucc`):**
   - **Read:** [`usecase-canvas/create-delta-ucc/SKILL.md`](usecase-canvas/create-delta-ucc/SKILL.md)
   - **Action:** Score candidate initiatives across the 4-Tab Use Case Canvas and produce the **1-Page Use Case Alignment Summary** (`Problem Statement`, `Target Users`, `MVP Scope`, `Out of Scope`, `Success Metrics`, `Key Dependencies`).
   - **Output:** `docs/USE_CASE_CANVAS.md` (see example: [`customer-onboarding-ucc.md`](usecase-canvas/create-delta-ucc/examples/customer-onboarding-ucc.md)).
3. **Initialize Engagement Governance (`tdl-field-guide`):**
   - **Read:** [`delivery/tdl-field-guide/SKILL.md`](delivery/tdl-field-guide/SKILL.md)
   - **Action:** Initialize `STATE.md` with the 7-tab Program Tracker structure (`Timeline`, `Use Cases`, `Staffing`, `Use Case RAID`, `Program RAID`, `Meetings`, `OOO`) and confirm Prelude exit criteria (signed SOW, named client product owner, sandbox environment request).

---

### Phase 1: Foundations — Ethnography, Baseline, PRD & Architecture (Weeks 1–2)
Deconstruct the current manual workflow, freeze the pre-AI statistical baseline, lock the Agentic PRD, and complete the 4-part Technical Specification before writing production code.

1. **Deconstruct the "As-Is" Workflow & Design the "To-Be" Agent Process (`business-process-redesign`):**
   - **Read:** [`business-process-redesign/SKILL.md`](business-process-redesign/SKILL.md)
   - **Output:** `docs/as_is_report.md`, `docs/to_be_designs.md`, and `docs/human_agent_roles.md` (see examples: [`as_is_report.md`](business-process-redesign/examples/as_is_report.md), [`to_be_designs.md`](business-process-redesign/examples/to_be_designs.md), [`human_agent_roles.md`](business-process-redesign/examples/human_agent_roles.md)).
2. **Map L1–L5 Critical User Journeys & AI Touchpoints (`cuj-architect`):**
   - **Read:** [`cuj-architect/SKILL.md`](cuj-architect/SKILL.md)
   - **Action:** Complete the 4-tab CUJ workbook structure (Ethnography $\rightarrow$ Pain Points $\rightarrow$ L1–L5 Journey Steps $\rightarrow$ AI Touchpoint Matrix scored by `Priority = 0.6 × Value + 0.4 × Feasibility`).
   - **Output:** `docs/CUJ_MAP.md` (see examples: [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md), [`cloud-support-triage-cuj.md`](cuj-architect/examples/cloud-support-triage-cuj.md)).
3. **Freeze the 50-Sample Historical Baseline (`synthetic-baseline-protocol`):**
   - **Read:** [`delivery/synthetic-baseline-protocol/SKILL.md`](delivery/synthetic-baseline-protocol/SKILL.md)
   - **Action:** Audit $N \ge 50$ historical tickets/claims/transactions with SMEs and run [`compute_baseline_stats.py`](delivery/synthetic-baseline-protocol/scripts/compute_baseline_stats.py) to compute mean/median/P90 handling time, error rate, escalation rate, and unit cost.
   - **Output:** `docs/baseline_kpis.json` (see example: [`claims-baseline-audit.md`](delivery/synthetic-baseline-protocol/examples/claims-baseline-audit.md)).
4. **Author the 8-Section Agentic PRD (`product-md` & `product-feature-md`):**
   - **Read:** [`product-management/product-md/SKILL.md`](product-management/product-md/SKILL.md) (and [`product-feature-md/SKILL.md`](product-management/product-feature-md/SKILL.md) for sprint-scoped features).
   - **Output:** `docs/PRD.md` following `go/delta-prd-template` including System Prompt Architecture and Evaluation Rubrics (see examples: [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md), [`enterprise-claims-agent-prd.md`](product-management/product-md/examples/enterprise-claims-agent-prd.md)).
5. **Select the GCP Agent Architecture Tier (`gcp-agent-architecture-advisor`):**
   - **Read:** [`delivery/gcp-agent-architecture-advisor/SKILL.md`](delivery/gcp-agent-architecture-advisor/SKILL.md)
   - **Action:** Compare Tier 1 (Gemini Enterprise no-code), Tier 2 (ADK on Vertex AI Agent Engine), and Tier 3 (ADK self-hosted on Cloud Run / GKE), verifying current GCP launch stages (`GA` vs. `Preview`).
   - **Output:** `docs/ARCHITECTURE_RECOMMENDATION.md` (see example: [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md)).
6. **Write the 4-Part Agent Technical Specification (`specification-engineer`):**
   - **Read:** [`utils/specification-engineer/SKILL.md`](utils/specification-engineer/SKILL.md)
   - **Action:** Document Parts I–IV (`System Overview`, `Agent Architecture & Orchestration`, `Tools & Data Contracts`, `Evaluation, Security & Operations`) and the 4 Pillars (`Prompting`, `RAG/Context`, `Tools/MCP`, `Eval/Observability`) per `go/delta-squad-agent-specs`.
   - **Output:** `docs/TDD.md` (see examples: [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md), [`claims-extraction-service-tdd.md`](utils/specification-engineer/examples/claims-extraction-service-tdd.md)).
7. **Pass Phase Gate 1 (`tdl-field-guide`):** Verify all Phase 1 exit artifacts are signed off in `STATE.md` before starting Sprint 1.

---

### Phase 2: Core Build & Bi-Weekly Demo Sprints (Weeks 3–10 — Four 2-Week Sprints)
Execute four 2-week sprints (**Sprint 1 [W3–4]**, **Sprint 2 [W5–6]**, **Sprint 3 [W7–8]**, **Sprint 4 [W9–10]**) with three customer-facing milestone demos (**Demo 1 [W4]**, **Demo 2 [W6]**, **Demo 3 [W8/W10]**).

1. **Rapid UI Prototyping & Brand Alignment (`stitch-design` & `frontend-design`):**
   - **Read:** [`prototyping/stitch-design/SKILL.md`](prototyping/stitch-design/SKILL.md) and [`prototyping/frontend-design/SKILL.md`](prototyping/frontend-design/SKILL.md)
   - **Action:** Execute the 3-stage prototyping workflow (Low-Fi Flow $\rightarrow$ Stitch MCP Screen Generation $\rightarrow$ Interactive HTML/React Validation) using Google Brand & Material 3 tokens (`#4285F4`, `#34A853`, `#FBBC04`, `#EA4335`, Google Sans / Roboto / Roboto Mono).
   - **Output:** `docs/STITCH_PROTOTYPE.md` and UI components (see examples: [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md), [`agent-ops-console-prototype.md`](prototyping/frontend-design/examples/agent-ops-console-prototype.md)).
2. **Harden System Prompts & Guardrails (`prompt-engineer`):**
   - **Read:** [`utils/prompt-engineer/SKILL.md`](utils/prompt-engineer/SKILL.md)
   - **Action:** Refactor agent system instructions with explicit XML/Markdown delimiters, tool-use preconditions, output JSON schemas, and prompt-injection refusal rules, verified against [`prompt-audit-checklist.md`](utils/prompt-engineer/references/prompt-audit-checklist.md).
3. **Run Goal-Driven Implementation Loops (`claude-agent-harness`):**
   - **Read:** [`ai-coding/claude-agent-harness/SKILL.md`](ai-coding/claude-agent-harness/SKILL.md)
   - **Action:** Run [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py) against `docs/PRD.md` and `docs/TDD.md` with deterministic `--verify-cmd` acceptance gates (unit tests, linter, typecheck) until all commands exit `0`.
   - **Output:** Verified `src/`, `tests/`, and `.harness/last_run_report.json`.
4. **Sprints 3–4 Production Load Testing & Quota Sizing (`agent-load-testing`):**
   - **Read:** [`delivery/agent-load-testing/SKILL.md`](delivery/agent-load-testing/SKILL.md)
   - **Action:** Run [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py) to calculate recursive fan-out calls per turn (`1 + Qt + Qt·Cq + 1`), peak RPM/TPM, and **5x safety-margin Vertex AI quota requests**, then execute Locust SSE streaming load tests and apply context/payload optimizations.
   - **Output:** `docs/LOAD_TEST_REPORT.md` (see example: [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md)).
5. **Sprints 3–4 Linguistic Quality (CLA) & Statistical Judge Auditing (`agent-eval-statistical-auditing`):**
   - **Read:** [`delivery/agent-eval-statistical-auditing/SKILL.md`](delivery/agent-eval-statistical-auditing/SKILL.md)
   - **Action:** Evaluate agent outputs against the **27 Communication & Linguistic Assessment (CLA) criteria** and audit your LLM-as-a-Judge against human SME consensus across all 3 pipelines using [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py) (`Pearson r ≥ 0.80`, `ICC(2,1) ≥ 0.75`, `Krippendorff's α ≥ 0.67`, `Quadratic Weighted Kappa ≥ 0.70`, `|Bias| ≤ 0.15`, `Compression Ratio ≥ 0.80`).
   - **Output:** `docs/EVAL_AUDIT_REPORT.md` (see example: [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md)).
6. **Pass Phase Gate 2 (`tdl-field-guide`):** Frame up each bi-weekly demo in `docs/DEMO_FRAME_UP.md` (`Why / What / How`) and enforce the **1-in-1-out scope swap rule** in `STATE.md`.

---

### Phase 3: Final Read-Out & Close (Weeks 11–12)
Quantify post-launch value against the frozen Week 1 baseline, deliver the executive closeout readout, and transition ownership to the client team.

1. **Calculate Measured ROI vs. Frozen Baseline (`ai-value-sizing`):**
   - **Read:** [`ai-value-sizing/SKILL.md`](ai-value-sizing/SKILL.md)
   - **Action:** Run [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) comparing `docs/baseline_kpis.json` against post-deployment telemetry across Conservative, Base, and Aggressive adoption scenarios.
   - **Output:** `docs/VALUE_SIZING.md` (see example: [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md)).
2. **Executive Closeout Deck, Handoff & Blameless Retro (`tdl-field-guide`):**
   - **Read:** [`delivery/tdl-field-guide/SKILL.md`](delivery/tdl-field-guide/SKILL.md)
   - **Action:** Compile the Closeout Slide Deck, close or transfer all items in the Use Case RAID and Program RAID logs, and facilitate the FDE Blameless Retrospective (`STATE.md`).

---

### Optional Track: Executive Strategy & CFO Business Cases
When an engagement includes an executive advisory workstream or C-suite strategy readout, use the four strategy skills (indexed in [`strategy-agent/SKILLS_INDEX.md`](strategy-agent/SKILLS_INDEX.md)):
- **[`strategy-house`](strategy-house/SKILL.md)** $\rightarrow$ `docs/STRATEGY_HOUSE.md` (Vision, Strategic Pillars, From-To Shifts, Capabilities).
- **[`strategy-partner-orchestrator`](strategy-agent/strategy-partner-orchestrator/SKILL.md)** $\rightarrow$ `docs/STRATEGY_BRIEF.md` (MECE issue tree, weighted decision matrix, 90-day roadmap).
- **[`ai-native-strategy`](strategy-agent/ai-native-strategy/SKILL.md)** $\rightarrow$ `docs/AI_STRATEGY.md` (AI-Enhanced vs. AI-Native moat scoring, Build/Buy/Partner, model routing unit economics).
- **[`financial-strategy`](strategy-agent/financial-strategy/SKILL.md)** $\rightarrow$ `docs/FINANCIAL_CASE.md` (P&L diagnostics, LTV/CAC & contribution margin, 3-scenario NPV/IRR schedule).

---

## 4. Deterministic CLI Calculators & Harness Reference

All calculators use **only the Python 3 standard library** (except `call_opus_model_garden.py`, which calls Vertex AI Model Garden when executed live) and expose all assumptions via CLI flags.

### 1. 50-Sample Historical Baseline Calculator (`compute_baseline_stats.py`)
Computes mean, median, P90 cycle time, error rate, escalation rate, unit labor cost, and annualized baseline cost from a CSV of historical work items (`sample_id,duration_minutes,had_error,escalated`).

```bash
python3 delivery/synthetic-baseline-protocol/scripts/compute_baseline_stats.py \
  --demo \
  --process-name "Commercial Auto FNOL Triage" \
  --hourly-rate 54.0 \
  --annual-volume 45000 \
  --output docs/baseline_kpis.json
```

### 2. Multi-Agent Fan-Out & Vertex AI 5x Quota Calculator (`calculate_agent_quotas.py`)
Implements the recursive tool fan-out formula (`Total Calls = 1 + Qt + (Qt × Cq) + 1`) and 5x safety-margin quota sizing from the TDL Load Testing Guide.

```bash
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py \
  --peak-turns-per-min 10 \
  --sub-queries 6 \
  --Follow-up-depth 4 \
  --avg-tokens-per-call 20000 \
  --safety-factor 5.0
```

### 3. LLM-as-a-Judge Statistical Auditor (`audit_llm_judge.py`)
Runs the 3-pipeline Agreement & Uncertainty Analysis (AUA) certification (`Pearson r`, `Spearman ρ`, `ICC(2,1)`, `Krippendorff's α`, `Quadratic Weighted Kappa`, `Mean Bias`, `Compression Ratio`, `Flip Rate`, and `Mean Entropy`) on paired human SME and LLM judge ratings.

```bash
# Audit the bundled calibrated judge fixture (PASS)
python3 delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py \
  --input delivery/agent-eval-statistical-auditing/examples/fixtures/calibrated_judge.json

# Audit the bundled compressed/lenient judge fixture (FAIL)
python3 delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py \
  --input delivery/agent-eval-statistical-auditing/examples/fixtures/compressed_lenient_judge.json
```

### 4. 3-Scenario AI Value Sizing & NPV Calculator (`calculate_roi.py`)
Computes gross labor savings, rework savings, cloud/token OpEx, net annual benefit, 3-year NPV, ROI %, and payback period across Conservative (`0.60x`), Base (`0.85x`), and Aggressive (`1.00x`) adoption multipliers.

```bash
python3 ai-value-sizing/scripts/calculate_roi.py \
  --annual-volume 45000 \
  --baseline-minutes 42.0 \
  --target-minutes 11.5 \
  --hourly-rate 54.0 \
  --baseline-error-rate 0.14 \
  --target-error-rate 0.03 \
  --rework-cost 185.0 \
  --implementation-cost 240000 \
  --annual-cloud-cost 48000 \
  --discount-rate 0.10
```

### 5. Vertex AI Model Garden Goal-Loop Harness (`call_opus_model_garden.py`)
Runs an iterative code-generation and verification loop on Vertex AI Model Garden (Claude Opus 4.6) until every `--verify-cmd` passes.

```bash
python3 ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py \
  --project-id "$GOOGLE_CLOUD_PROJECT" \
  --region us-east5 \
  --workspace . \
  --goal "Implement the FNOL extraction service per docs/TDD.md" \
  --spec-file docs/PRD.md \
  --spec-file docs/TDD.md \
  --verify-cmd "python3 -m unittest discover -s tests -p 'test_*.py'" \
  --dry-run
```

### 6. New Skill Scaffolder (`init_skill.py`)
Scaffolds a new skill directory that conforms to repository validation rules.

```bash
python3 utils/skill-creator/scripts/init_skill.py my-new-skill --path delivery
```

---

## 5. Complete 22-Skill Catalog & TDL Toolbox Mapping

### Part A: The 18 Official TDL Toolbox Assets $\rightarrow$ 9 Skills

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
| **13** | Delta Brand & UI Guidelines (Google colors, typography, co-branding) | Delta Design | [`frontend-design`](prototyping/frontend-design/SKILL.md) | [`ui-review-checklist.md`](prototyping/frontend-design/references/ui-review-checklist.md) · [`agent-ops-console-prototype.md`](prototyping/frontend-design/examples/agent-ops-console-prototype.md) |
| **14** | Agent Technical Specifications (`go/delta-squad-agent-specs`) | C. Clark | [`specification-engineer`](utils/specification-engineer/SKILL.md) | [`tdd-spec-template.md`](utils/specification-engineer/references/tdd-spec-template.md) · [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md) *(adapted from toolbox spec)* |
| **15** | TDL Prototyping Guide (3 stages + Stitch MCP workflow) | S. Srinivasan | [`stitch-design`](prototyping/stitch-design/SKILL.md) | [`stitch-mcp-workflow.md`](prototyping/stitch-design/references/stitch-mcp-workflow.md) · [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md) |
| **16** | Load Testing, Parallelism, Quotas & Optimizations Guide (NSH Clinician Search) | S. Kuwel | [`agent-load-testing`](delivery/agent-load-testing/SKILL.md) | [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py) · [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) *(exact guide math)* |
| **17** | Linguistic Output Quality Evaluation Framework (CLA, 27 criteria) | H. González | [`agent-eval-statistical-auditing`](delivery/agent-eval-statistical-auditing/SKILL.md) | [`cla-rubric-and-aua-methodology.md`](delivery/agent-eval-statistical-auditing/references/cla-rubric-and-aua-methodology.md) |
| **18** | Statistical Auditing for LLM-as-a-Judge (3 pipelines, AUA report) | H. González | [`agent-eval-statistical-auditing`](delivery/agent-eval-statistical-auditing/SKILL.md) | [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py) · [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) *(deck report + fixture output)* |

### Part B: The 13 Repo-Native Skills

| Skill | Category | Output Artifact(s) | Script / Reference & Worked Example |
| :--- | :--- | :--- | :--- |
| **[`synthetic-baseline-protocol`](delivery/synthetic-baseline-protocol/SKILL.md)** | Delivery & Baseline | `docs/baseline_kpis.json` | [`compute_baseline_stats.py`](delivery/synthetic-baseline-protocol/scripts/compute_baseline_stats.py) · [`claims-baseline-audit.md`](delivery/synthetic-baseline-protocol/examples/claims-baseline-audit.md) |
| **[`gcp-agent-architecture-advisor`](delivery/gcp-agent-architecture-advisor/SKILL.md)** | Architecture | `docs/ARCHITECTURE_RECOMMENDATION.md` | [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md) |
| **[`ai-value-sizing`](ai-value-sizing/SKILL.md)** | Value Realization | `docs/VALUE_SIZING.md` | [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) · [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md) |
| **[`product-feature-md`](product-management/product-feature-md/SKILL.md)** | Product Specs | `docs/features/<feature_slug>.md` | [`feature-spec-template.md`](product-management/product-feature-md/references/feature-spec-template.md) · [`voice-capture-feature-spec.md`](product-management/product-feature-md/examples/voice-capture-feature-spec.md) |
| **[`frontend-design`](prototyping/frontend-design/SKILL.md)** *(beyond Toolbox 13)* | Prototyping | Production HTML/CSS/TS UI | [`ui-review-checklist.md`](prototyping/frontend-design/references/ui-review-checklist.md) · [`agent-ops-console-prototype.md`](prototyping/frontend-design/examples/agent-ops-console-prototype.md) |
| **[`claude-agent-harness`](ai-coding/claude-agent-harness/SKILL.md)** | AI Coding | Verified `src/`, `tests/`, `.harness/last_run_report.json` | [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py) · [`spec-to-production-code.md`](ai-coding/claude-agent-harness/examples/spec-to-production-code.md) |
| **[`prompt-engineer`](utils/prompt-engineer/SKILL.md)** | Engineering Utils | Audited system prompts & eval cases | [`prompt-audit-checklist.md`](utils/prompt-engineer/references/prompt-audit-checklist.md) · [`agent-system-prompt-refactor.md`](utils/prompt-engineer/examples/agent-system-prompt-refactor.md) |
| **[`skill-creator`](utils/skill-creator/SKILL.md)** | Engineering Utils | New validated skill directory | [`init_skill.py`](utils/skill-creator/scripts/init_skill.py) · [`creating-a-new-skill-example.md`](utils/skill-creator/examples/creating-a-new-skill-example.md) |
| **[`strategy-house`](strategy-house/SKILL.md)** | Executive Strategy | `docs/STRATEGY_HOUSE.md` | [`strategy-house-template.md`](strategy-house/references/strategy-house-template.md) · [`retail-omnichannel-strategy-house.md`](strategy-house/examples/retail-omnichannel-strategy-house.md) |
| **[`strategy-partner-orchestrator`](strategy-agent/strategy-partner-orchestrator/SKILL.md)** | Executive Strategy | `docs/STRATEGY_BRIEF.md` | [`mece-issue-tree.md`](strategy-agent/strategy-partner-orchestrator/references/mece-issue-tree.md) · [`cloud-migration-strategy-brief.md`](strategy-agent/strategy-partner-orchestrator/examples/cloud-migration-strategy-brief.md) |
| **[`ai-native-strategy`](strategy-agent/ai-native-strategy/SKILL.md)** | Executive Strategy | `docs/AI_STRATEGY.md` | [`model-economics-config.json`](strategy-agent/ai-native-strategy/references/model-economics-config.json) · [`enterprise-agent-platform-strategy.md`](strategy-agent/ai-native-strategy/examples/enterprise-agent-platform-strategy.md) |
| **[`financial-strategy`](strategy-agent/financial-strategy/SKILL.md)** | Executive Strategy | `docs/FINANCIAL_CASE.md` | [`business-case-builder.md`](strategy-agent/financial-strategy/references/business-case-builder.md) · [`saas-margin-and-ai-capex-plan.md`](strategy-agent/financial-strategy/examples/saas-margin-and-ai-capex-plan.md) |
| **[`delta-skills-directory`](SKILL.md)** *(root index)* | Workspace Registry | Navigation & artifact routing | [`SKILL.md`](SKILL.md) |

---

## 6. Worked Examples & Provenance Policy

Every skill in this repository includes at least one complete worked example in its `examples/` folder:

1. **Adapted from Real TDL Toolbox Artifacts (4 examples):**
   - [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md) — adapted from Emily Chan's Intel AskIT Agentic PRD (`Toolbox #05`).
   - [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md) — adapted from Craig Clark's NBCU Asset Buddy Technical Specification (`Toolbox #14`).
   - [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md) — adapted from Ronan Hennessy's Procurement Supplier Rate Audit CUJ Workbook (`Toolbox #03`).
   - [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) — uses only the published Nova Scotia Health (NSH) Clinician Search Agent parameters and results from Said Kuwel's Load Testing Guide (`Toolbox #16`).
2. **Real Deck Report + Deterministic Bundled Fixtures (1 example):**
   - [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) — reproduces Héctor González's published AUA certification reports (`Toolbox #18`) alongside the exact stdout of `audit_llm_judge.py` run against [`calibrated_judge.json`](delivery/agent-eval-statistical-auditing/examples/fixtures/calibrated_judge.json) and [`compressed_lenient_judge.json`](delivery/agent-eval-statistical-auditing/examples/fixtures/compressed_lenient_judge.json).
3. **Unified Illustrative End-to-End Thread (Remaining Examples):**
   - To show how artifacts reference each other across all 12 weeks without exposing confidential client data, the remaining examples use one consistent *fictional* scenario (**Acme P&C — Commercial Auto Claims FNOL**): [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md) $\rightarrow$ [`claims-baseline-audit.md`](delivery/synthetic-baseline-protocol/examples/claims-baseline-audit.md) $\rightarrow$ [`enterprise-claims-agent-prd.md`](product-management/product-md/examples/enterprise-claims-agent-prd.md) $\rightarrow$ [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md) $\rightarrow$ [`claims-extraction-service-tdd.md`](utils/specification-engineer/examples/claims-extraction-service-tdd.md) $\rightarrow$ [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md) $\rightarrow$ [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) $\rightarrow$ [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md). Every illustrative file is explicitly labeled as a fictional template in its header.

---

## 7. Validation, CI Drift Guards & External Prerequisites

### Run the Repository Validator & Unit Test Suites
Run these three commands before committing any change to a skill, template, example, or calculator:

```bash
# 1. Validate all SKILL.md frontmatter, links, JSON files, code fences, and orphan/duplicate rules
python3 scripts/validate_skills.py

# 2. Run repository validator unit tests + example-to-script stdout drift guards (21 tests)
python3 -m unittest discover -s scripts -p 'test_*.py'

# 3. Run Claude Agent Harness unit tests (25 tests)
python3 -m unittest discover -s ai-coding/claude-agent-harness/scripts -p 'test_*.py'
```

### What `scripts/validate_skills.py` and `scripts/test_validate_skills.py` Enforce
- Valid YAML frontmatter (`name` and `description`) on every `SKILL.md`.
- Every skill directory with subdirectories links to at least one substantive worked example (`examples/*.md`, $\ge 8$ non-empty lines).
- Every file under `references/`, `examples/`, `scripts/`, and `assets/` is referenced by a markdown link (zero orphaned files).
- Zero `.gitkeep` files, zero duplicate markdown files across skills, balanced fenced code blocks, valid JSON syntax, and zero broken relative links.
- **Automated Drift Guards:** Unit tests execute `calculate_roi.py`, `compute_baseline_stats.py`, `calculate_agent_quotas.py`, and `audit_llm_judge.py` and assert that the numbers embedded in their respective worked examples match the scripts' exact stdout.

### External Prerequisites (Not Vendored)
- **`stitch-design` (Steps 4–5):** Requires a Stitch MCP server configured as `StitchMCP` in your agent host; otherwise follow the manual UI specification fallback documented in [`stitch-design/SKILL.md`](prototyping/stitch-design/SKILL.md).
- **`claude-agent-harness` (Live Vertex AI Mode):** Requires `pip install 'anthropic[vertex]'`, `gcloud auth application-default login`, and Vertex AI Model Garden access to Claude 4.6 models (`--dry-run` works offline with standard library only).
