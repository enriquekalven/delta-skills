---
name: financial-strategy
description: >
  Audit P&L structure, customer and workload unit economics (CAC, LTV, contribution margin,
  payback), and 3-scenario investment cases (NPV, IRR, cash flow) to produce docs/FINANCIAL_CASE.md.
  Trigger when asked to analyze P&L margins, validate SaaS/AI unit economics, or build a CFO-ready
  capital allocation case.
metadata:
  author: rcfaris@
  version: '2.0'
---

# Financial Strategy

This skill translates operational and strategic proposals into a CFO-grade financial analysis (`docs/FINANCIAL_CASE.md`) covering **P&L & Margin Diagnostics**, **Unit Economics (LTV/CAC & Contribution Margin)**, and **3-Scenario Investment Modeling (Base / Bull / Bear)**.

---

## Operating Rules

1. **Numbers & Explicit Assumptions:** Never state "margins will improve." State exact basis points (bps), dollar impacts, and the underlying volume × rate assumptions.
2. **Operating Cash Flow Over Paper Savings:** Separate hard cash savings (vendor contract elimination, infrastructure consolidation, avoided net-new hires) from soft productivity gains (reallocated employee hours).
3. **Unit Economics Before Scale:** Validate gross margin, contribution margin after variable cloud/inference costs, CAC payback period (months), and LTV:CAC ratio before recommending expansion spend.
4. **Three Scenarios Mandatory:** Model Base, Bull, and Bear cases by varying the 2–3 highest-sensitivity drivers (adoption curve, token/compute cost per unit, churn/retention delta).

---

## Procedure

### Phase 1: P&L & Cost Structure Diagnostic
Use [financial-diagnostics.md](references/financial-diagnostics.md) to benchmark current revenue growth, COGS (hosting, support, inference, third-party APIs), gross margin %, and OpEx (R&D, S&M, G&A) against target thresholds.

### Phase 2: Unit Economics Audit
Use [unit-economics.md](references/unit-economics.md) to calculate:
- `Gross Margin % = (Revenue - COGS) / Revenue`
- `Contribution Margin per Customer/Unit = Gross Margin - Variable Support & Inference Cost`
- `CAC Payback (Months) = Fully Loaded CAC / (ARPU_monthly × Gross Margin %)`
- `LTV = (ARPU_annual × Gross Margin %) / Annual Churn Rate`

### Phase 3: 3-Year Investment Case (NPV, IRR, Payback)
Use [business-case-builder.md](references/business-case-builder.md) to model Year 0 CapEx, Years 1–3 OpEx, gross vs. risk-adjusted cash inflows, Net Present Value (NPV at explicit WACC, default 10%), and payback month. Write the final report to `docs/FINANCIAL_CASE.md`.

---

## Deliverable Template (`docs/FINANCIAL_CASE.md`)

```markdown
# Financial Case & Unit Economics Analysis: <Initiative Name>
Date: <YYYY-MM-DD> | WACC: <10.0%> | Currency: USD

## 1. Executive Bottom Line
<1-2 sentences stating 3-year NPV, IRR, Payback Period, and gross margin impact in bps>

## 2. P&L & Unit Economics Diagnostic (Current vs. Target)
| Metric | Current Baseline | Post-Initiative Target | Delta | Key Assumption |
|---|---|---|---|---|

## 3. 3-Year Cash Flow & TCO Schedule ($K)
| Line Item | Year 0 | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|---|

## 4. Scenario & Sensitivity Matrix (Base / Bull / Bear)
| Scenario | Adoption / Volume | Net 3-Yr Cash Flow | 3-Yr NPV @ 10% | Payback (Months) |
|---|---|---|---|---|
```

---

## References & Examples

- [Financial Diagnostics](references/financial-diagnostics.md): P&L, working capital, and margin decomposition checklists.
- [Unit Economics](references/unit-economics.md): LTV, CAC payback, cohort contribution margin, and AI inference COGS formulas.
- [Business Case Builder](references/business-case-builder.md): CapEx/OpEx schedules, NPV/IRR calculation rules, and sensitivity tables.
- [Worked Example: Enterprise SaaS Gross Margin Expansion & AI Support Automation](examples/saas-margin-and-ai-capex-plan.md): Complete `docs/FINANCIAL_CASE.md` showing P&L diagnostics, unit economics before/after AI deployment, and 3-year NPV/IRR schedules.
