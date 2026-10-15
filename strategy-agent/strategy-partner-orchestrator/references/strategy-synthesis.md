# Strategic Option Scoring & Synthesis Reference

Use this reference when synthesizing diagnostic findings into a decision-ready `docs/STRATEGY_BRIEF.md`.

---

## 1. Option Design Rules

Every strategic synthesis must evaluate **3 genuinely distinct options** (never strawmen):
1. **Option 1 (Status Quo / Incremental Baseline):** Quantifies the trajectory and cost of continuing current operations.
2. **Option 2 (Targeted / Phased Intervention):** Focuses resources on the highest-ROI bottleneck with bounded capital risk.
3. **Option 3 (Full Structural Transformation):** High-capex, longer-horizon overhaul.

---

## 2. Weighted Decision Matrix

Score each option from `1` (Poor) to `10` (Excellent) across explicit weighted criteria:

| Criterion | Typical Weight | Definition |
| :--- | :--- | :--- |
| **Financial Impact (3-Yr NPV / Margin Lift)** | `30%` | Risk-adjusted net economic value created over 36 months |
| **Time-to-Value / Payback Speed** | `20%` | Months to reach cash-flow break-even and measurable KPI lift |
| **Execution & Technical Feasibility** | `20%` | Readiness of data, APIs, and internal engineering talent |
| **Capital Efficiency (Inverted CapEx)** | `15%` | Upfront investment required relative to budget ceiling |
| **Operational & Compliance Risk** | `15%` | Resilience against regulatory, SLA, or customer-churn downside |

**Sensitivity Check:** Verify whether shifting any single criterion weight by $\pm 10\%$ changes the winning option. State the result explicitly.

---

## 3. Pre-Mortem & Kill Criteria

Every recommended strategy must include a **Pre-Mortem Risk Table** and **Hard Kill/Pivot Triggers**:

| Failure Mode | Likelihood (H/M/L) | Impact ($ / SLA) | Preventive Control | Kill / Pivot Trigger |
| :--- | :--- | :--- | :--- | :--- |
| Pilot adoption stalls below target | Medium | Delays payback by 9 months | Embed workflow directly in existing adjuster UI | Active weekly usage $< 40\%$ after 60 days in production |
| Upstream API/data quality below threshold | Medium | Forces manual fallback | Run 50-sample baseline audit in Week 1 before build | Field extraction confidence $< 85\%$ on $> 30\%$ of volume |
