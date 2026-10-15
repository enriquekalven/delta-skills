---
name: product-md
description: >
  Generate, prioritize (via RICE), or critique a full Delta Agentic Product Requirements Document
  (PRD) saved to docs/PRD.md using the official 8-section TDL Toolbox PRD structure (Use Case &
  Primary Objective, Pain Points [Blocker vs. Friction], Reactive & Proactive CUJs, Information
  Architecture & DAG Design, RICE-Prioritized Requirements & Platform GA Alignment, Hypotheses to
  Test, Scope Exclusions, and Stakeholders & Business Value Metrics). Trigger when asked to write a
  PRD, structure product requirements, or prioritize a feature backlog.
metadata:
  version: '3.2'
---

# Delta Agentic Product Requirements Document Generator (`product-md`)

This skill produces, prioritizes, or critiques a structured Product Requirements Document at `docs/PRD.md` aligned with the official **TDL Toolbox Agentic PRD standard** (the canonical Gate 1 artifact required by [tdl-field-guide](../tdl-field-guide/SKILL.md), [gcp-agent-architecture-advisor](../gcp-agent-architecture-advisor/SKILL.md), [specification-engineer](../specification-engineer/SKILL.md), and [claude-agent-harness](../claude-agent-harness/SKILL.md)).

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 Foundations (Due End of Week 2):** 6.0-hour structured PRD authoring & RICE backlog lock |
| **Time-to-Market (TTM) Compression** | **40.0h manual $\rightarrow$ 6.0h skill-guided (`85.0%` faster Gate 1 PRD completion)** |
| **Reads (Inputs)** | `docs/WORKSHOP_INTAKE.md`, `docs/USE_CASE_CANVAS.md`, `docs/CUJ_MAP.md`, `docs/as_is_report.md` |
| **Writes (Outputs)** | `docs/PRD.md` (following [`references/prd-template.md`](references/prd-template.md)) |
| **Value Realization Linkage** | Binds every `P0` feature (`F-01..F-n`) to a deterministic **RICE Score** ($\frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$) and quantified Section 8 Business Value Metrics |

---

## Core Rules & 8-Section Structure

1. **Canonical Output Path:** Always write the PRD to `docs/PRD.md` unless the user explicitly specifies another filename.
2. **Official 8-Section Delta Agentic PRD Structure (`go/delta-prd-template`):**

| Section | Title | Mandatory Contents |
| :--- | :--- | :--- |
| **1** | **Use Case & Primary Objective** | Executive narrative, 5-row `Primary Objective` table (`Title`, `Persona Identification`, `Context Trigger`, `The Goal`, `Strategic Outcome`), and `Strategic Opportunity Analysis` |
| **2** | **Pain Points & Problems** | Every problem explicitly classified as **`Blocker (Adoption-Preventing)`** or **`Friction (Efficiency-Draining)`** |
| **3** | **Critical User Journeys (CUJs)** | Step-by-step tables separating **Phase 1 Reactive Journeys** (user-initiated) from **Phase 2 Proactive/Autonomous Journeys** (event/webhook-driven) |
| **4** | **Information Architecture & DAG Design** | Table mapping **Triggers** (`Manual`, `Scheduled`, `Event-Driven`), **Nodes** (`Connectors`, `RAG`, `BYO-MCP`, `Orchestrator`), and **Logic Gates** (`Branching`, `Looping`, `Mandatory HITL`) |
| **5** | **Prioritized Requirements & RICE Backlog** | Cloud AI platform GA alignment (`P0`/`P1`) + **RICE-scored feature table** (`Reach`, `Impact`, `Confidence`, `Effort`, `RICE Score`) + latency/availability SLAs |
| **6** | **Hypotheses to Test** | Load-bearing assumptions table (`Hypothesis | Core Belief | Pivot / Mitigation Plan`) |
| **7** | **Scope Exclusions** | Explicit out-of-scope boundaries across `Logistics`, `Security`, `Finance`, and `Localization` (enforces 1-in-1-out rule) |
| **8** | **Stakeholders & Business Value Metrics** | Quantified targets (`Project Leadership`, `User Impact`, `Core Value Metric`, `Efficiency Gain`, `Phase 1 Success`, `Phase 2 Success`) |

3. **RICE Prioritization Formula:** Every feature in Section 5 must be scored using:
   $$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort (Person-Months)}}$$
   - **Reach:** Users or transactions impacted per quarter.
   - **Impact:** `3.0` = massive, `2.0` = high, `1.0` = medium, `0.5` = low, `0.25` = minimal.
   - **Confidence:** `1.0` (100% — measured data), `0.8` (80% — benchmarked), `0.5` (50% — hypothesis).
   - **Effort:** Person-months required.

---

## Operational Modes

1. **Mode 1 — Generate (`docs/PRD.md`):** Read discovery inputs (`docs/WORKSHOP_INTAKE.md`, `docs/USE_CASE_CANVAS.md`, `docs/CUJ_MAP.md`, `docs/as_is_report.md`) and generate a complete 8-section PRD following [prd-template.md](references/prd-template.md).
2. **Mode 2 — Prioritize Backlog (RICE):** Compute Reach, Impact, Confidence, and Effort for candidate features and sort into **Phase 1 MVP (P0 — Weeks 3–10)** vs. **Phase 2 Proactive Fast-Follow (P1)**.
3. **Mode 3 — Critique Existing PRD:** Audit a draft PRD against the Customer Sign-Off Gate below and flag missing `Blocker vs. Friction` tags, missing DAG logic gates/HITL checkpoints, or unquantified value metrics.

---

## Customer Sign-Off & Quality Gate

| Gate Criterion | Approve When | Reject If |
| :--- | :--- | :--- |
| **Complete 8-Section Structure** | All 8 sections of `go/delta-prd-template` are populated, including `Blocker vs. Friction` tags and `Phase 1 Reactive` vs. `Phase 2 Proactive` CUJs. | Uses a generic traditional software PRD that omits agent DAG nodes, triggers, or HITL logic gates. |
| **RICE-Scored Backlog (`F-01..F-n`)** | Every feature in Section 5 has explicit numerical `Reach`, `Impact`, `Confidence`, `Effort`, and computed `RICE Score` (`(R*I*C)/E`). | Features are listed without RICE scores, preventing 1-in-1-out scope swap governance in Phase 2. |
| **Testable Hypotheses & Exclusions** | Section 6 defines concrete pivot plans for each hypothesis and Section 7 locks explicit out-of-scope boundaries. | Leaves scope exclusions blank or omits quantified Section 8 business value metrics. |

---

## References & Examples

- [Delta Agentic PRD Template](references/prd-template.md): Official 8-section template for `docs/PRD.md`.
- [Worked Example 1: AskIT Service Desk Optimization PRD](examples/ask-it-service-desk-prd.md): Complete 8-section TDL Toolbox PRD for a 130,000-employee IT service desk & autonomous command center agent.
- [Worked Example 2: Commercial Auto Claims FNOL Triage Agent PRD](examples/enterprise-claims-agent-prd.md): Complete `docs/PRD.md` artifact for insurance claims triage with RICE feature scoring and acceptance criteria.
