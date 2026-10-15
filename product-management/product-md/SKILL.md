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
  version: '3.0'
---

# Delta Agentic Product Requirements Document Generator (`product-md`)

This skill produces, prioritizes, or critiques a structured Product Requirements Document at `docs/PRD.md` aligned with the official **TDL Toolbox Agentic PRD standard** (the canonical Gate 1 artifact required by [tdl-field-guide](../../delivery/tdl-field-guide/SKILL.md), [gcp-agent-architecture-advisor](../../delivery/gcp-agent-architecture-advisor/SKILL.md), [specification-engineer](../../utils/specification-engineer/SKILL.md), and [claude-agent-harness](../../ai-coding/claude-agent-harness/SKILL.md)).

---

## Core Rules

1. **Canonical Output Path:** Always write the PRD to `docs/PRD.md` unless the user explicitly specifies another filename.
2. **Official 8-Section Delta Agentic PRD Structure:** Every generated `docs/PRD.md` must follow the 8-section TDL Toolbox template in [prd-template.md](references/prd-template.md):
   - **Header Metadata Block & Discovery Session Links**
   - **1. USE CASE:** Executive narrative, `Primary Objective` table (`Title | Persona Identification | Context Trigger | The Goal | Strategic Outcome`), and `Strategic Opportunity Analysis`.
   - **2. PAIN POINTS & PROBLEMS:** Classified explicitly into **`Blocker (Adoption-Preventing)`** (e.g., unstructured RAG data, routing noise) vs. **`Friction (Efficiency-Draining)`** (e.g., operator cognitive load, manual L3 escalation latency).
   - **3. CRITICAL USER JOURNEYS (CUJs):** Step-by-step tables (`Step | Phase | Action Details`) separating **Phase 1 Reactive Journeys** (user-initiated triage & troubleshooting) from **Phase 2 Proactive/Autonomous Journeys** (webhook/event-driven self-healing).
   - **4. INFORMATION ARCHITECTURE & DAG DESIGN:** Table mapping **Triggers** (`Manual`, `Scheduled`, `Event-Driven`), **Nodes** (`Enterprise Connectors`, `QA Agent RAG`, `BYO-MCP Server Node`, `Multi-Agent Orchestrator`), and **Logic Gates** (`Conditional Branching`, `Looping`, `Mandatory Human-in-the-Loop [HITL]`).
   - **5. PRIORITIZED REQUIREMENTS, RICE BACKLOG & PLATFORM LAUNCH ALIGNMENT:** Cloud AI platform dependency GA dates (`P0`/`P1`) plus a RICE-scored feature table and non-functional SLAs.
   - **6. HYPOTHESES TO TEST:** Table of load-bearing assumptions (`Hypothesis | Core Belief | Pivot / Mitigation Plan`).
   - **7. SCOPE EXCLUSIONS:** Categorized boundaries (`Logistics`, `Security`, `Finance`, `Localization`) enforcing the 1-in-1-out governance rule.
   - **8. STAKEHOLDERS & BUSINESS VALUE METRICS:** Quantified target metrics (`Project Leadership`, `User Impact`, `Core Value Metric`, `Efficiency Gain`, `Phase 1 Success`, `Phase 2 Success`).
3. **RICE Prioritization Mandatory:** Every feature in Section 5 must be scored using:
   $$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort (Person-Months)}}$$
   - **Reach:** Users or transactions impacted per quarter.
   - **Impact:** `3.0` = massive, `2.0` = high, `1.0` = medium, `0.5` = low, `0.25` = minimal.
   - **Confidence:** `1.0` (100% — measured data), `0.8` (80% — benchmarked), `0.5` (50% — hypothesis).
   - **Effort:** Person-months required.

---

## Operational Modes

### Mode 1: Generate (`docs/PRD.md`)
Read discovery inputs (`docs/WORKSHOP_INTAKE.md`, `docs/USE_CASE_CANVAS.md`, `docs/CUJ_MAP.md`, and `docs/as_is_report.md` if present) and generate a complete 8-section PRD following [prd-template.md](references/prd-template.md).

### Mode 2: Prioritize Backlog (RICE)
Take a raw list of candidate features and platform dependencies, compute Reach, Impact, Confidence, and Effort with explicit justifications, and sort the backlog into **Phase 1 MVP (P0 — Weeks 3–10)** vs. **Phase 2 Proactive Fast-Follow (P1)**.

### Mode 3: Critique Existing PRD
Audit a draft PRD against the Validation Checklist below and flag any missing `Blocker vs. Friction` classifications, missing DAG logic gates/HITL checkpoints, untestable hypotheses, or unquantified value metrics.

---

## Validation Checklist

- [ ] Saved to `docs/PRD.md` with Header Metadata Block, Status, Owners, and Discovery Session links.
- [ ] Section 1 defines the `Primary Objective` 5-row table (`Title`, `Persona Identification`, `Context Trigger`, `The Goal`, `Strategic Outcome`) and quantified `Strategic Opportunity Analysis`.
- [ ] Section 2 classifies every pain point as **`Blocker (Adoption-Preventing)`** or **`Friction (Efficiency-Draining)`**.
- [ ] Section 3 separates **Phase 1 Reactive CUJs** from **Phase 2 Proactive/Event-Driven CUJs**.
- [ ] Section 4 specifies DAG **Triggers**, **Nodes** (Connectors, RAG, MCP, Orchestrator), and **Logic Gates** (Branching, Looping, Mandatory HITL).
- [ ] Section 5 includes both **Platform Launch/GA Alignment (`P0`/`P1`)** and **RICE-scored features (`F-01`, `F-02`...)**.
- [ ] Section 6 documents testable **Hypotheses to Test** with explicit **Pivot / Mitigation Plans**.
- [ ] Section 7 defines explicit **Scope Exclusions** across Logistics, Security, Finance, and Localization.
- [ ] Section 8 quantifies **User Impact**, **Core Value Metric**, **Efficiency Gain (hours/$ saved)**, and **Phase 1 vs. Phase 2 Success**.

---

## References & Examples

- [Delta Agentic PRD Template](references/prd-template.md): Official 8-section template for `docs/PRD.md`.
- [Worked Example 1: AskIT Service Desk Optimization PRD](examples/ask-it-service-desk-prd.md): Complete 8-section TDL Toolbox PRD for a 130,000-employee IT service desk & autonomous command center agent.
- [Worked Example 2: Commercial Auto Claims FNOL Triage Agent PRD](examples/enterprise-claims-agent-prd.md): Complete `docs/PRD.md` artifact for insurance claims triage with RICE feature scoring and acceptance criteria.
