# `delta /forward` Agentic Process Transformation & CUJ Templates (`docs/CUJ_MAP.md`)

Use these 4 official **TDL Toolbox Agentic Process Transformation Templates** (plus the Strategic Context & JSON payload) when generating `docs/CUJ_MAP.md`.

---

## Strategic Context & Persona Summary
- **Outcome (Level 1):** `<Business-level impact — The 'Why'>`
- **Stages (Level 2):** `<Collaborative milestones / break-points>`
- **Operating Level:** `[Outcome | Stage | CUJ | Task | Step/CUI]`
- **Target Actor / Persona:** `<Role, systems used, and primary pain>`
- **Reframed Goal (Level 3):** `"As a result of completing these tasks, I will have/get [X]."`
- **AI Value Proposition:**
  - **Core Feature:** *"AI [Removes / Replaces / Augments / Adds to] [items at operating level minus 1] by [what the AI solution gives the user]."*
  - **Integration:** *"AI [Integrates with] [tool/process] to [items at operating level minus 1]."*

---

## Template 1: Process Ethnography & Observation Capturing (As-Is Ground Truth)

Records the raw "ground truth" of legacy workflows at a discrete user action level, capturing system context switches, latency, and observed friction.

- **Observer Name:** `<Observer>` | **Observation Date:** `<YYYY-MM-DD>`
- **Participant Role:** `<Target Persona>` | **Business Process Unit:** `<Department / Workflow>`

| Step ID | Associated Task Shorthand | User Action / Step Description (As-Is) | System / Application Used | Context-Switching Point? (Y/N) | Friction Category | Observed Friction & Waste Description | Est. Latency (Min) | Qualitative User Quote / Grounding |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :--- |
| **Step 1.1** | `<Task Shorthand>` | `<Discrete manual action>` | `<System>` | `Y / N` | `<Data Retrieval \| System Latency \| Munging/Transform \| Quality Checks>` | `<Specific manual waste or error risk>` | `<Min>` | `"<Verbatim quote from SME observation>"` |

---

## Template 2: Critical User Journey (CUJ) Map Hierarchy (L1–L5)

Deconstructs legacy workflows into hierarchical human objectives completely decoupled from specific software tools.

| Business Outcome (Level 1) | Process Stage (Level 2) | CUJ Goal Shorthand (Level 3a) | Goal / Result Statement (Level 3) | Task (Level 4 — Verb + Noun) | Step (Level 5 — User Action) | Target Actor / Persona | Is Validated? (Y/N) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `<Outcome>` | `<Stage>` | `<Goal Shorthand>` | `As a result of completing these tasks, I will have/get <X>` | `<Verb + Noun>` | `<Discrete Step>` | `<Persona>` | `Y / N` |

---

## Template 3: Future State CUJ & AI Touchpoint Taxonomy

Maps proposed AI solutions directly to the L1–L5 CUJ Hierarchy from Template 2, classifying recommendations using standardized AI Core Effects, Standardized AI Intents, and HITL Governance roles.

| Business Outcome (L1) | Process Stage (L2) | CUJ Goal Shorthand (L3a) | Task (L4 — Verb + Noun) | Step (L5 — User Action) | Proposed AI Touchpoint Description | AI Core Effect | Standardized AI Intent | Capabilities & Dependencies | HITL Role & Governance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `<Outcome>` | `<Stage>` | `<Goal Shorthand>` | `<Task>` | `<Step>` | `<How AI transforms this step>` | `<Replace \| Augment \| Remove \| Add to \| Integrate with>` | `<Retrieve \| Execute \| Transform \| Analyze \| Answer \| Summarize \| Route \| Monitor>` | `<Required APIs, RAG corpora, ontologies, schemas>` | `<Reviewer \| Prompt Curator \| Approver>` (`<Exact human sign-off check>`) |

---

## Template 4: Collaborative AI Touchpoint Prioritization Matrix

Evaluates, scores, and prioritizes proposed AI touchpoints using the weighted `/forward` formula:
- $\text{Value Score (Avg)} = \frac{\text{User Pain} + \text{Efficiency Gain} + \text{Strategic Alignment}}{3}$
- $\text{Feasibility Score (Avg)} = \frac{\text{Data Readiness} + \text{Tech Feasibility}}{2}$
- $\text{Overall Score (Wtd)} = 0.60 \times \text{Value Score} + 0.40 \times \text{Feasibility Score}$

| TP ID | Associated Goal Shorthand | Proposed AI Touchpoint Description | User Pain (1–5) | Efficiency Gain (1–5) | Strategic Alignment (1–5) | Value Score (Avg) | Data Readiness (1–5) | Tech Feasibility (1–5) | Feasibility Score (Avg) | Overall Score (Wtd) | Priority Level | Next Steps Workstream | Product Owner | Tech Owner |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **TP-1** | `<Goal Shorthand>` | `<Touchpoint>` | `5.0` | `5.0` | `5.0` | `5.00` | `4.0` | `4.0` | `4.00` | **4.60** | `P0 (Immediate)` | `Iterative Build` | `<PO>` | `<Tech Lead>` |
