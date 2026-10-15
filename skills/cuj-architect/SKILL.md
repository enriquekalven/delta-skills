---
name: cuj-architect
description: >
  Decompose legacy and AI-native product journeys using the official 4-tab delta /forward Agentic
  Process Transformation & CUJ Templates (1. Process Ethnography & Observation Capturing, 2. L1-L5
  CUJ Map Hierarchy, 3. Future State CUJ & AI Touchpoint Taxonomy with HITL Governance, and 4.
  Collaborative AI Touchpoint Prioritization Matrix) and write docs/CUJ_MAP.md plus a
  schema-validated JSON payload. Trigger when asked to generate an AI CUJ, run process ethnography,
  map an L1-L5 user journey, or prioritize AI touchpoints.
metadata:
  version: '4.2'
---

# `delta /forward` Agentic Process Transformation & CUJ Architect (`cuj-architect`)

This skill maps legacy and future-state workflows across the five-level hierarchy (`Outcome [L1] → Stage [L2] → CUJ Goal [L3] → Task [L4] → Step/CUI [L5]`) using the official **4-Tab TDL Toolbox CUJ Definition Templates**, preventing bolt-on AI features by binding every proposed AI touchpoint to observed process ethnography friction, a standardized AI core effect, a user intent, an explicit HITL governance role, and a weighted prioritization score in `docs/CUJ_MAP.md`.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 Foundations (Weeks 1–2):** 3.5-hour 4-tab CUJ mapping & touchpoint prioritization workshop |
| **Time-to-Market (TTM) Compression** | **24.0h manual $\rightarrow$ 3.5h skill-guided (`85.4%` faster L1–L5 journey & touchpoint prioritization)** |
| **Reads (Inputs)** | `docs/as_is_report.md`, `docs/to_be_designs.md` |
| **Writes (Outputs)** | `docs/CUJ_MAP.md` (following [`references/output-template.md`](references/output-template.md) and [`references/schema.json`](references/schema.json)) |
| **Value Realization Linkage** | Ranks AI touchpoints by $\text{Overall Score} = 0.60 \times \text{Value Score} + 0.40 \times \text{Feasibility Score}$ so Sprint 1 builds highest-ROI `P0` touchpoints first |

---

## The 4 Official `delta /forward` CUJ Templates

Every complete `docs/CUJ_MAP.md` deliverable follows the 4-stage methodology in [output-template.md](references/output-template.md):

| Template Tab | Purpose | Required Columns & Formulas |
| :--- | :--- | :--- |
| **1. Process Ethnography** | Capture As-Is ground truth & swivel-chair waste | `Step ID` · `Actor` · `System/App` · `Context-Switch (Y/N)` · `Friction Category` (`Data Retrieval`, `System Latency`, `Munging/Transform`, `Quality Checks`) · `Latency (min)` · `Verbatim Quote` |
| **2. L1–L5 CUJ Hierarchy** | Deconstruct workflow into tool-agnostic goals | `L1 Business Outcome` $\rightarrow$ `L2 Stage` $\rightarrow$ `L3 Goal ("As a result of completing these tasks, I will have/get [X]")` $\rightarrow$ `L4 Task (Verb + Noun)` $\rightarrow$ `L5 Step` |
| **3. Future State & AI Taxonomy** | Bind AI capabilities & HITL governance to L4/L5 steps | `AI Core Effect` (`Replace`, `Augment`, `Remove`, `Add to`, `Integrate with`) · `AI Intent` (`Retrieve`, `Execute`, `Transform`, `Analyze`, `Answer`, `Summarize`, `Route`, `Monitor`) · `HITL Role` (`Reviewer`, `Prompt Curator`, `Approver`) |
| **4. Prioritization Matrix** | Rank touchpoints (`TP-1..TP-n`) for sprint backlog | $\text{Value Score} = \frac{\text{Pain} + \text{Efficiency} + \text{Alignment}}{3}$ · $\text{Feasibility Score} = \frac{\text{Data} + \text{Tech}}{2}$ · $\text{Overall} = 0.60 \times \text{Value} + 0.40 \times \text{Feasibility}$ (`P0`, `P1`, `P2`) |

---

## Execution Steps

1. **Capture Process Ethnography (Template 1):** Document how the workflow is performed today without AI, logging every system hop, friction category, latency in minutes, and SME quote.
2. **Build L1–L5 CUJ Hierarchy (Template 2):** Reframe all Level 3 goals using *"As a result of completing these tasks, I will have/get [X]."*
3. **Design Future-State AI Touchpoints & HITL Governance (Template 3):** Assign each step its `AI Core Effect`, `Standardized AI Intent`, `Capabilities & Dependencies`, and `HITL Role` (`Reviewer`, `Prompt Curator`, `Approver`).
4. **Score & Prioritize Touchpoints (Template 4) & Validate JSON:** Compute the $0.60 \times \text{Value Score} + 0.40 \times \text{Feasibility Score}$ weighted scores and write `docs/CUJ_MAP.md` following [output-template.md](references/output-template.md) and [schema.json](references/schema.json).

---

## Customer Sign-Off & Quality Gate

| Gate Criterion | Approve When | Reject If |
| :--- | :--- | :--- |
| **Ethnography Grounding** | Every AI touchpoint traces back to an observed Template 1 friction point with measured latency in minutes and system hops. | Proposes "bolt-on" chatbot features untethered from observed workflow bottlenecks. |
| **L3 Result Framing & HITL Role** | Every L3 goal uses *"As a result of completing these tasks, I will have/get [X]"* and every touchpoint assigns `Reviewer`, `Prompt Curator`, or `Approver`. | Writes L3 goals as software feature descriptions or omits human governance roles. |
| **Deterministic `0.60V + 0.40F` Math** | Template 4 computes exact `Value Score`, `Feasibility Score`, and `0.60 * Value + 0.40 * Feasibility` priority bands (`P0`, `P1`, `P2`). | Uses subjective "High/Medium/Low" labels without computing the weighted 1–5 scores. |

---

## References & Examples

- [4-Tab `delta /forward` CUJ Output Template](references/output-template.md): Complete Markdown tables for Process Ethnography, L1–L5 Hierarchy, Future State AI Touchpoint Taxonomy, and Weighted Prioritization Matrix.
- [Intent & Quality Measurement Variants](references/quality-variants.md): Exhaustive table of user intents and evaluation dimensions.
- [CUJ JSON Schema](references/schema.json): JSON Schema (`draft-07`) for structured CUJ hierarchy validation.
- [Worked Example 1: Supplier Spend & Rate Variance CUJ Transformation](examples/supplier-rate-audit-cuj.md): Complete 4-tab TDL Toolbox workbook example (`Process Ethnography`, `L1–L5 Hierarchy`, `Future State CUJ`, and `AI Prioritization Matrix`).
- [Worked Example 2: Cloud Support Incident Triage & Remediation CUJ](examples/cloud-support-triage-cuj.md): Narrative context and schema-validated JSON payload for cloud support triage.
