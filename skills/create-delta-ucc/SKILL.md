---
name: create-delta-ucc
description: >
  Facilitate a 4-worksheet discovery interview (User Focus, Value Proposition, Business Viability,
  Technical Feasibility & Data Readiness [Available / Usable / Quality]) and generate a combined
  Strategic Use Case Canvas & Official TDL Toolbox MVP Alignment Summary Document in
  docs/USE_CASE_CANVAS.md (including Must-Haves vs. Okay for Slippage, Before/After CUJ Flowchart,
  Eval Round 1 vs. Round 2 Scope, Solution Inputs/Outputs tables, and Evaluation Approach). Trigger
  when asked to brainstorm a use case, create a Delta Use Case Canvas (UCC), or write an MVP
  Alignment Summary Document. Do NOT trigger for full PRDs (use product-md) or code generation.
metadata:
  version: '3.2'
---

# Strategic Use Case Canvas & MVP Alignment Summary Generator (`create-delta-ucc`)

This skill guides the user through a 4-part discovery worksheet and compiles a formal **Strategic Use Case Canvas & MVP Alignment Summary Document** (`docs/USE_CASE_CANVAS.md`) aligned with the official **TDL Toolbox Use Case Alignment Summary Document (`MVP Alignment Doc`)** and **Use Case Selection Guidelines**.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Prelude (Week 0):** MVP scope lock session immediately following `workshop-intake` |
| **Reads (Inputs)** | `docs/WORKSHOP_INTAKE.md` (32 Starter Questions & Data Readiness Yardstick) |
| **Writes (Outputs)** | `docs/USE_CASE_CANVAS.md` (using [`references/ucc-template.md`](references/ucc-template.md)) |

---

## Execution Procedure

### Phase 1: The 4-Worksheet Discovery & `/forward` Yardstick Loop
Guide the user through the four worksheets one at a time (or extract answers from `docs/WORKSHOP_INTAKE.md` if provided). Do not invent features without user confirmation; when proposing refinements, offer 3 concrete options grounded in Google Cloud patterns so the user can choose.

Commit strictly to one high-priority use case per 12-week timeline ([`go/delta-delivery-guide`](https://goto.google.com/delta-delivery-guide)); park other ideas under `(Future) Phase 2+ Scope`.

| Worksheet | Core Discovery Questions | Required Output in `docs/USE_CASE_CANVAS.md` |
| :--- | :--- | :--- |
| **1. User Focus** | Primary internal persona / external segment, annual transaction volume, top 3 workflow bottlenecks, and adoption triggers | Persona profile, annual volume baseline, and quantified pain/gain table |
| **2. Value Proposition** | Core Job-To-Be-Done (JTBD), **Revenue Impact Levers** (new offering, faster TTM, CSAT) vs. **Efficiency Impact Levers** (hours saved, handoff removal, accuracy, cross-LOB reuse) | JTBD statement + Revenue & Efficiency lever mapping |
| **3. Business Viability & MVP Scope** | Which KPIs move (`Baseline -> Target`)? Which goals are **Non-Negotiable Must-Haves** vs. **Okay for Slippage**? How do features split across **Eval Round 1**, **Eval Round 2**, and **Not In Focus**? | Must-Haves vs. Slippage table + Eval Round 1 / Round 2 scope matrix |
| **4. Technical Feasibility & Data Readiness** | `Available / Usable / Quality` yardstick, upstream/downstream data sources & MCPs, status quo quality, and whether formal **UAT is required (`Yes/No`)** | Solution Inputs/Outputs tables + Evaluation & UAT plan |

### Phase 2: Canvas & MVP Alignment Doc Generation
Once the four worksheets are complete, write `docs/USE_CASE_CANVAS.md` using the combined template in [ucc-template.md](references/ucc-template.md).

---

## References & Examples

- [Delta Use Case Canvas & MVP Alignment Doc Template](references/ucc-template.md): Complete Markdown template for `docs/USE_CASE_CANVAS.md`.
- [Worked Example: Commercial Loan Covenant Monitoring UCC & MVP Alignment Doc](examples/customer-onboarding-ucc.md): Complete `docs/USE_CASE_CANVAS.md` deliverable showing both the 4-worksheet canvas and the full MVP Alignment Summary Document.
