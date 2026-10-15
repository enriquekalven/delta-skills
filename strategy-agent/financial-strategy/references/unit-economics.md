# Unit Economics & Contribution Margin Reference

Use this reference to calculate atomic unit profitability (per customer, per seat, or per AI transaction) in `docs/FINANCIAL_STRATEGY.md`.

---

## 1. B2B SaaS & AI-Native Unit Economics Formulas

| Metric | Formula | Healthy B2B SaaS Benchmark | Danger Zone |
| :--- | :--- | :--- | :--- |
| **Gross Margin (%)** | $\frac{\text{Revenue} - (\text{Hosting} + \text{LLM Inference} + \text{CS Delivery})}{\text{Revenue}}$ | $\ge 70\%$ | $< 55\%$ (Uncapped token/inference burn) |
| **CAC ($)** | $\frac{\text{Fully Loaded S\&M Spend}}{\text{New Customers Acquired}}$ | Segment-dependent | Growing faster than ACV |
| **CAC Payback (Months)** | $\frac{\text{CAC}}{\text{Monthly ARPU} \times \text{Gross Margin \%}}$ | $\le 15\text{ months}$ | $> 24\text{ months}$ |
| **LTV ($)** | $\frac{\text{Annual ACV} \times \text{Gross Margin \%}}{\text{Annual Logo Churn Rate}}$ | $\ge 3\times \text{CAC}$ | $< 2\times \text{CAC}$ |
| **Net Dollar Retention (NDR %)** | $\frac{\text{Starting ARR} + \text{Expansion} - \text{Downsell} - \text{Churn}}{\text{Starting ARR}}$ | $\ge 110\%$ (Enterprise) | $< 95\%$ |
| **Burn Multiple** | $\frac{\text{Net Burn}}{\text{Net New ARR Added}}$ | $< 1.5\times$ | $> 2.5\times$ |

---

## 2. AI Feature Contribution Margin Decomposition

When pricing an AI agent workflow (per-seat vs. usage-based vs. outcome-based), compute the **Per-Tenant Monthly Contribution Margin**:

$$\text{Contribution Margin (\$)} = \text{Monthly Price} - \left(N_{\text{tasks}} \times \text{Tokens}_{\text{task}} \times \text{Blended Rate}_{\text{1M}}\right) - \text{Vector/DB Storage} - \text{HITL Escalation Labor}$$

### Stress-Testing Heavy-Usage ("Whale") Tenants
Always model unit margin at both **p50 (median)** and **p95 (heavy-usage)** tenant volume:
- If **p95 tenant usage** pushes gross margin negative under flat-rate per-seat pricing, introduce:
  1. **Model Cascade Routing** (route 70%+ of routine classifications to a sub-`$1/1M` model tier),
  2. **Prompt Prefix Caching** (cut repeated system/context input cost by 50%–75%), and
  3. **Tiered Included-Task Allowances** with overage blocks (`$/1,000` resolved tasks).
