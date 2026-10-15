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
  version: '4.0'
---

# `delta /forward` Agentic Process Transformation & CUJ Architect

This skill maps legacy and future-state workflows across the five-level hierarchy (`Outcome [L1] → Stage [L2] → CUJ Goal [L3] → Task [L4] → Step/CUI [L5]`) using the official **4-Tab TDL Toolbox CUJ Definition Templates**, preventing bolt-on AI features by binding every proposed AI touchpoint to observed process ethnography friction, a standardized AI core effect, a user intent, an explicit HITL governance role, and a weighted prioritization score in `docs/CUJ_MAP.md`.

---

## The 4 Official `delta /forward` CUJ Templates

Every complete `docs/CUJ_MAP.md` deliverable follows the 4-stage methodology in [output-template.md](references/output-template.md):

1. **Template 1 — Process Ethnography & Observation Capturing (As-Is Ground Truth):**
   - Captures discrete manual actions (`Step 1.1`, `Step 1.2`...), system/application used, **Context-Switching Point (`Y/N`)**, **Friction Category** (`Data Retrieval`, `System Latency`, `Munging/Transform`, `Quality Checks`), estimated manual latency in minutes, and verbatim user quotes.
2. **Template 2 — CUJ Map Hierarchy (Levels 1–5):**
   - Deconstructs the workflow purely through human objectives decoupled from software tools:
     - **Level 1 (`Business Outcome`):** Measurable P&L or operational result.
     - **Level 2 (`Process Stage`):** Milestone grouping of interconnected CUJs.
     - **Level 3a (`CUJ Goal Shorthand`) & Level 3 (`Goal / Result Statement`):** Reframed from *"I want to..."* into **"As a result of completing these tasks, I will have/get [X]."**
     - **Level 4 (`Task — Verb + Noun`):** Implementation-independent task.
     - **Level 5 (`Step — User Action`):** Concrete interaction step, target persona, and validation status (`Y/N`).
3. **Template 3 — Future State CUJ & AI Touchpoint Taxonomy:**
   - Aligns proposed AI solutions directly to L1–L5 and classifies each touchpoint by:
     - **AI Core Effect:** `Replace`, `Augment`, `Remove`, `Add to`, or `Integrate with`.
     - **Standardized AI Intent:** `Retrieve`, `Execute`, `Transform`, `Analyze`, `Answer`, `Summarize`, `Route`, `Monitor` (with quality metrics from [quality-variants.md](references/quality-variants.md)).
     - **Capabilities & Dependencies:** Required APIs, ontologies, vector corpora, and schemas.
     - **HITL Role & Governance:** `Reviewer` (verifies retrieved records), `Prompt Curator` (manages mapping rules for anomalies), or `Approver` (signs off on exceptions/mutations).
4. **Template 4 — Collaborative AI Touchpoint Prioritization Matrix:**
   - Scores every touchpoint (`TP-1`, `TP-2`...) on a 1–5 scale and computes:
     - $\text{Value Score (Avg)} = \frac{\text{User Pain} + \text{Efficiency Gain} + \text{Strategic Alignment}}{3}$
     - $\text{Feasibility Score (Avg)} = \frac{\text{Data Readiness} + \text{Tech Feasibility}}{2}$
     - $\text{Overall Score (Wtd)} = 0.60 \times \text{Value Score} + 0.40 \times \text{Feasibility Score}$
   - Classifies each touchpoint into `P0 (Immediate — Iterative Build)`, `P1 (High — Design Sprint / Technical Discovery)`, or `P2 (Backlog)`.

---

## Execution Steps

1. **Capture Process Ethnography (Template 1):** Document how the workflow is performed today without AI, logging every system hop, friction category, latency in minutes, and SME quote.
2. **Build L1–L5 CUJ Hierarchy (Template 2):** Reframe all Level 3 goals using *"As a result of completing these tasks, I will have/get [X]."*
3. **Design Future-State AI Touchpoints & HITL Governance (Template 3):** Assign each step its `AI Core Effect`, `Standardized AI Intent`, `Capabilities & Dependencies`, and `HITL Role` (`Reviewer`, `Prompt Curator`, `Approver`).
4. **Score & Prioritize Touchpoints (Template 4) & Validate JSON:** Compute the $0.60 \times \text{Value} + 0.40 \times \text{Feasibility}$ weighted scores and write `docs/CUJ_MAP.md` following [output-template.md](references/output-template.md) and [schema.json](references/schema.json).

---

## References & Examples

- [4-Tab `delta /forward` CUJ Output Template](references/output-template.md): Complete Markdown tables for Process Ethnography, L1–L5 Hierarchy, Future State AI Touchpoint Taxonomy, and Weighted Prioritization Matrix.
- [Intent & Quality Measurement Variants](references/quality-variants.md): Exhaustive table of user intents and evaluation dimensions.
- [CUJ JSON Schema](references/schema.json): JSON Schema (`draft-07`) for structured CUJ hierarchy validation.
- [Worked Example 1: Supplier Spend & Rate Variance CUJ Transformation](examples/supplier-rate-audit-cuj.md): Complete 4-tab TDL Toolbox workbook example (`Process Ethnography`, `L1–L5 Hierarchy`, `Future State CUJ`, and `AI Prioritization Matrix`).
- [Worked Example 2: Cloud Support Incident Triage & Remediation CUJ](examples/cloud-support-triage-cuj.md): Narrative context and schema-validated JSON payload for cloud support triage.
