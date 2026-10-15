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
  version: '3.0'
---

# Strategic Use Case Canvas & MVP Alignment Summary Generator (`create-delta-ucc`)

This skill guides the user through a 4-part discovery worksheet and compiles a formal **Strategic Use Case Canvas & MVP Alignment Summary Document** (`docs/USE_CASE_CANVAS.md`) aligned with the official **TDL Toolbox Use Case Alignment Summary Document (`MVP Alignment Doc`)** and **Use Case Selection Guidelines**.

---

## Execution Procedure

### Phase 1: The 4-Worksheet Discovery & `/forward` Yardstick Loop
Guide the user through the four worksheets one at a time (or extract answers from existing intake notes if provided). Do not invent features without user confirmation; when proposing refinements, offer 3 concrete options grounded in Google Cloud patterns so the user can choose.

1. **Worksheet 1 — User Focus:**
   - Who is the primary target user role (internal persona) or external customer segment, and what volume of work do they handle?
   - What are the top 3 measurable pain points in their current workflow?
   - What specific gains (time saved, error reduction, decision quality) unlock adoption?
2. **Worksheet 2 — Value Proposition (Revenue vs. Efficiency Levers):**
   - What is the core Job-To-Be-Done (JTBD)?
   - Which **Revenue Impact Levers** (new offering, enhanced feature, faster time-to-market, CSAT lift, market eminence) and **Efficiency Impact Levers** (workforce time saved, bottleneck/handoff removal, output accuracy, reusable cross-LOB pattern) apply?
3. **Worksheet 3 — Business Viability & MVP Prioritization:**
   - Which operational KPIs move (`Baseline → Target`), and which objectives are **Non-Negotiable Must-Haves** vs. **Okay for Slippage**?
   - How are features split between **MVP Evaluation Round 1**, **MVP Evaluation Round 2**, and **Not In Focus for MVP**?
4. **Worksheet 4 — Technical Feasibility & Data Readiness (`Available / Usable / Quality`):**
   - **Data Readiness Audit:**
     - **Available:** Exists in sufficient volume/depth and permitted under privacy/consent rights.
     - **Usable:** Centralized vs. siloed; clear owner & fast access approval; cataloged & AI-accessible.
     - **Quality:** Accurate, consistently formatted, matches frequency requirements (real-time vs. batch).
   - **Solution Inputs & Outputs Mapping:** Exact upstream data sources/APIs/MCPs and downstream target systems.
   - **Evaluation & Testing Approach:** Current status quo quality, whether formal **UAT is required (`Yes/No`)**, and tentative evaluation metrics.

### Phase 2: Canvas & MVP Alignment Doc Generation
Once the four worksheets are complete, write `docs/USE_CASE_CANVAS.md` using the combined template in [ucc-template.md](references/ucc-template.md).

---

## Quality Checklist

- [ ] Contains **Part I: 4-Worksheet Strategic Use Case Canvas** (`User Focus`, `Value Proposition`, `Business Viability`, `Technical Feasibility & Data Readiness [Available / Usable / Quality]`).
- [ ] Contains **Part II: Official MVP Alignment Summary Document**:
  - [ ] `Business Objectives & Metrics` explicitly distinguishing **Non-Negotiable Must-Haves** vs. **Okay for Slippage**.
  - [ ] `Process CUJ Flow Chart (Before vs. After MVP Scope)`.
  - [ ] `Phase 1 (MVP) Scope` broken into **Eval Round 1**, **Eval Round 2**, **Not In Focus**, **Datasets Needed**, and **Assumptions & Risks**.
  - [ ] `Data Source & Agent Input/Outputs Mapping` tables (`Data Source | Access Method | Features Enabled`).
  - [ ] `Evaluation and Testing Approach` (`Status Quo Quality`, `UAT Required: Yes/No`, `Tentative Evaluation Metrics`).
  - [ ] `(Future) Phase 2+ Scope` (`Long-Term Vision` and `Potential Future Features/Needs`).

---

## References & Examples

- [Delta Use Case Canvas & MVP Alignment Doc Template](references/ucc-template.md): Complete Markdown template for `docs/USE_CASE_CANVAS.md`.
- [Worked Example: Commercial Loan Covenant Monitoring UCC & MVP Alignment Doc](examples/customer-onboarding-ucc.md): Complete `docs/USE_CASE_CANVAS.md` deliverable showing both the 4-worksheet canvas and the full MVP Alignment Summary Document.
