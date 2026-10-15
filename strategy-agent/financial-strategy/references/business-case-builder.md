# Business Case & Capital Allocation Reference

Use this reference when modeling 3-to-5-year NPV, IRR, Payback Period, and Stage-Gate investments in `docs/FINANCIAL_STRATEGY.md`.

---

## 1. Core Capital Budgeting Formulas

### Net Present Value (NPV)
$$\text{NPV} = -C_0 + \sum_{t=1}^{T} \frac{\text{FCF}_t}{(1 + r)^t}$$
where $C_0$ is Year-0 upfront CapEx/implementation spend, $\text{FCF}_t = \text{Gross Benefit}_t - \text{Ongoing OpEx}_t - \Delta \text{WC}_t$, and $r$ is the hurdle rate / WACC.

### Expected Value Across 3 Scenarios
$$\mathbb{E}[\text{NPV}] = p_{\text{base}} \cdot \text{NPV}_{\text{base}} + p_{\text{bull}} \cdot \text{NPV}_{\text{bull}} + p_{\text{bear}} \cdot \text{NPV}_{\text{bear}}$$
Standard default weights when empirical distribution is unknown: **Base = 50%**, **Bull = 25%**, **Bear = 25%**.

### Payback Period (Months)
$$\text{Payback (Months)} = \frac{C_0}{(\text{Annual Net Cash Inflow}) / 12}$$

---

## 2. Full Probability Chain Rule (Staged Investments)

When an initiative must pass through multiple sequential stage gates (e.g., `Phase 1 Pilot -> Phase 2 Security Sign-Off -> Phase 3 Production Scale`), never evaluate a single stage's probability in isolation:

$$P(\text{Commercial Realization}) = \prod_{k=1}^{K} P(\text{Gate } k \text{ Pass})$$

| Stage | Investment at Risk | Gate Pass Criterion | Conditional Pass Prob $P(k)$ | Cumulative Prob $\prod P$ |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Baseline & Prototype** | `$75K` | Golden-set accuracy $\ge 90\%$ on 50 historical items | `85%` | `85.0%` |
| **Stage 2: Shadow Production Pilot** | `$175K` | Override rate $\le 12\%$, p95 latency $\le 5.0\text{s}$ | `80%` | `68.0%` |
| **Stage 3: Full Rollout** | `$250K` | $\ge 60\%$ active adjuster adoption by Day 60 | `85%` | `57.8%` |

---

## 3. Standard Business Case Table

| Metric | Bear Case (25%) | Base Case (50%) | Bull Case (25%) | Probability-Weighted Expected Value |
| :--- | :--- | :--- | :--- | :--- |
| **Year-0 CapEx ($)** | `$X` | `$X` | `$X` | `$X` |
| **Annual Ongoing OpEx ($)** | `$Y` | `$Y` | `$Y` | `$Y` |
| **Year-1 Net Cash Flow ($)** | `$CF_1` | `$CF_1` | `$CF_1` | `$CF_1` |
| **Year-2 Net Cash Flow ($)** | `$CF_2` | `$CF_2` | `$CF_2` | `$CF_2` |
| **Year-3 Net Cash Flow ($)** | `$CF_3` | `$CF_3` | `$CF_3` | `$CF_3` |
| **3-Year NPV (@ WACC)** | `$NPV` | `$NPV` | `$NPV` | `$\mathbb{E}[NPV]` |
| **IRR (%)** | `X%` | `X%` | `X%` | `X%` |
| **Payback Period (Months)** | `X.X mo` | `X.X mo` | `X.X mo` | `X.X mo` |
