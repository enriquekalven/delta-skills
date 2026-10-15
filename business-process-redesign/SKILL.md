---
name: business-process-redesign
description: >
  Reimagine legacy business processes using the official delta /forward Business Process
  Reimagination Method Guide: navigate the 3 Levels of Altitude (Level 1 Transformational
  Priorities -> Level 2 Strategic Initiatives -> Level 3 AI Building Blocks), apply the 4
  Forward-Deployed Principles (Embed don't consult, Co-creation not handoff, Process over Product,
  Harvest Everything), quantify manual labor/rework costs, classify steps along the L1-L3 autonomy
  spectrum, and produce docs/as_is_report.md, docs/to_be_designs.md, and docs/human_agent_roles.md.
  Trigger when asked to reimagine a business process, map a workflow for AI agents, or quantify
  process bottlenecks. Do NOT trigger for product requirements documents (use product-md).
metadata:
  author: antigravity@
  version: '3.0'
---

# `delta /forward` Business Process Redesign & Reimagination (`business-process-redesign`)

This skill maps and reimagines legacy operational workflows using the official **TDL Toolbox `delta /forward` Reimagine Business Processes Method Guide**, navigating the **3 Levels of Altitude**, calculating annualized baseline cost (labor + rework), classifying each task by autonomy level (`L1 Human-Only`, `L2 Agent-Assisted / HITL`, `L3 Fully Autonomous`), and producing three concrete deliverables in `docs/`.

---

## 1. The 4 `delta /forward` Principles

1. **Embed, Don't Consult:** Daily engagement in the customer's operational reality—observe real practitioners executing work (process ethnography) rather than relying on slide-deck descriptions.
2. **Co-Creation, Not Handoff:** Build with the customer's process owners, IT/data leads, and practitioners, not in isolation for them.
3. **Process Over Product:** Prioritize redesigning legacy workflows around modern AI agents rather than engineering net-new administrative software around broken manual steps.
4. **Harvest Everything:** Generalize bespoke engineering code, schemas, and skills into reusable "Golden Paths" to accelerate future squads.

---

## 2. The 3 Levels of Altitude

Always anchor where the engagement is operating across the three altitudes before decomposing tasks:

| Altitude Level | Name | Definition & Scope | Stakeholders | Value & Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **Highest Level (Altitude 1)** | **Transformational Priorities** | Enterprise AI transformation opportunities that set the mid-to-long-term vision and overarching financial/P&L goals (e.g., *Transform Insurance Customer Experience & Expedite Internal Risk Processes*). | C-Level / ELT Steering Committee (`3–5` leaders) | Top-down P&L and strategic efficiency KPIs. |
| **Mid Level (Altitude 2)** | **Strategic Initiatives** | Cross-functional business processes or end-to-end user experiences attached to a Transformational Priority and specific financial metrics (e.g., *Claims Processing*, *Dynamic Risk Management*, *Agentic Sales Hub*). | Business Unit Leaders (`N-1`, `4–6` leaders) & Process Owners (`N-2`, `2–3`/BU) | End-to-end As-Is & To-Be CUJ Maps and prioritized AI touchpoints. |
| **Lowest Level (Altitude 3)** | **AI Building Blocks** | Individual workflows combining agentic, ML, or analytical components tied to a specific journey stage (e.g., *FNOL Doc Ingestion & Extraction*, *Policy Coverage Assessment*, *Fraud Detection*). | IT & Data Leads (`2–4` experts) + Practitioners (`10–20` daily users) | Functional specs (`docs/PRD.md`, `docs/TDD.md`), quality metrics, TCO reduction, and deployed agent. |

---

## 3. Autonomy Spectrum & Defensible Math Rules

1. **Autonomy Spectrum (`L1` / `L2` / `L3`):**
   - **L1 (Human-Only):** High-empathy, subjective, or irreversible legal/strategic sign-offs.
   - **L2 (Agent-Assisted / HITL):** Unstructured synthesis, draft generation, or high-value configuration requiring human review (`Reviewer`, `Prompt Curator`, or `Approver`) before commit.
   - **L3 (Fully Autonomous):** Deterministic, rules-based, or low-risk API/data operations with automated logging and rollback.
2. **Defensible Math:** Every process baseline and To-Be business case must compute:
   - $\text{Annual Hours} = \text{Annual Volume} \times \text{Cycle Time (Hours)}$
   - $\text{Annual Labor Cost} = \text{Annual Hours} \times \text{Fully Burdened Hourly Rate}$
   - $\text{Annual Rework Cost} = \text{Annual Volume} \times \text{Error Rate} \times \text{Rework Time (Hours)} \times \text{Hourly Rate}$
3. **Explicit Safety Gates:** Every L2 and L3 task must define its trigger, tool/API permissions, confidence/monetary escalation threshold, and fallback path.

---

## 4. Execution Timeline & Procedure (Week -4 Mobilization → Week 0 Gate)

### Phase 1: Mobilization, Ethnography & "As-Is" Deconstruction (Weeks -4 to -2)
1. **Week 0 Readiness & Stakeholder Roster:** Confirm Steering Committee (`C-Level`), Business Unit Leaders (`N-1`), Process Owners (`N-2`), IT/Data Leads, and Practitioners (`10–20` users), and collect legacy SOPs, schemas, and data samples.
2. **Stakeholder Interviews & Ethnographic Observation:** Conduct 20-min GM strategic sessions, 45-min Process Owner deep dives, and live screen-recorded ethnographic observations using [discovery-deconstruction.md](references/discovery-deconstruction.md) to capture "swivel-chair" context switches and hidden manual waste.
3. **Decompose Tasks & Score Baseline:** Break the workflow into sequential tasks (`T1..Tn`) with actor, systems, inputs, outputs, cycle time, frequency, error rate, and L1–L3 classification, and write `docs/as_is_report.md`.

### Phase 2: "To-Be" Agentic Process & Role Design (Weeks -2 to -1)
1. **Map AI Building Blocks & 5 AI Core Effects (`Remove`, `Replace`, `Augment`, `Add to`, `Integrate with`):** For each L2/L3 task, specify the 6 agentic workflow dimensions (Mandate, Trigger, Data Sources, Action Tools, HITL Escalation Gate, Feedback Loop) using [agentic-process-design.md](references/agentic-process-design.md).
2. **Calculate Post-Automation ROI:** Compute annual hours saved, labor savings, error reduction savings, build cost, and payback months, and write `docs/to_be_designs.md`.
3. **Redefine Human-Agent Swimlanes:** Define the human-agent collaboration matrix, escalation thresholds, and updated human role KPIs using [human-agent-interaction.md](references/human-agent-interaction.md), and write `docs/human_agent_roles.md`.

### Phase 3: 2-Day Process Reimagination Workshop & PDR Gate (Week 0)
1. **Day 1:** Validate goals, review As-Is ethnographic friction points (with dot-voting), and iterate on the To-Be CUJ & AI Intent Taxonomy.
2. **Day 2:** Prioritize AI Building Blocks for the 12-week FDE build, verify all deliverables against [process-design-review.md](references/process-design-review.md), and feed directly into `docs/PRD.md`.

---

## Standard Outputs

Write these three files to the workspace `docs/` directory:
1. `docs/as_is_report.md` — Altitude framing, current-state task decomposition, ethnographic bottlenecks, and annualized cost baseline.
2. `docs/to_be_designs.md` — Redesigned agentic workflow, prioritized AI Building Blocks, HITL gates, and ROI/payback scorecard.
3. `docs/human_agent_roles.md` — Human-agent interaction matrix and redefined operator job description.

---

## References & Worked Examples

- **Reference Templates:**
  - [Discovery & Deconstruction Guide](references/discovery-deconstruction.md)
  - [Agentic Process Design Guide](references/agentic-process-design.md)
  - [Human-Agent Interaction & Role Guide](references/human-agent-interaction.md)
  - [Process Design Review (PDR) Checklist](references/process-design-review.md)
- **Complete Worked Case Study (Customer Onboarding Workflow — 1,200 transactions/yr):**
  - [Worked Example 1: As-Is Process Analysis Report](examples/as_is_report.md)
  - [Worked Example 2: To-Be Agent-Enhanced Process Designs](examples/to_be_designs.md)
  - [Worked Example 3: Human-Agent Interaction Models & Redefined Roles](examples/human_agent_roles.md)
