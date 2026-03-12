# Execution Monitoring Output Templates

## Traffic Light Dashboard

```
EXECUTION DASHBOARD — [ENGAGEMENT NAME]
═════════════════════════════════════════
Report period: Week [#] of [#] | Status date: [Date]
Overall health: [🟢 On track / 🟡 Adjustments needed / 🔴 Course correction required]

STRATEGIC METRICS
  Revenue / ARR: [Current] vs. [Target] = [%] | Status: [🟢 / 🟡 / 🔴] | Trend: [↗️ / → / ↘️]
  Growth rate: [Current] vs. [Target] = [%] | Status: [🟢 / 🟡 / 🔴]
  Customer acquisition: [Current] vs. [Target] = [%] | Status: [🟢 / 🟡 / 🔴]
  Retention: [Current] vs. [Target] = [%] | Status: [🟢 / 🟡 / 🔴]

OPERATIONAL KPIs (By Function)
  [Function 1] — Key metric: [Value] | Target: [Value] | Status: [🟢 / 🟡 / 🔴]
  [Function 2] — Key metric: [Value] | Target: [Value] | Status: [🟢 / 🟡 / 🔴]

RED FLAGS (This Week)
  1. [Metric] breached RED threshold [value] on [date] — Root cause: [hypothesis] — Action: [Escalated]
  2. [Assumption trigger] fired on [date] — Confidence drop: [H→M] — Action: [Pending]

AMBER FLAGS (Approaching Threshold)
  1. [Metric] trending toward AMBER — Current: [value] | AMBER: [value] | Weeks to breach: [#]
  2. [Risk indicator] approaching red zone — Current probability: [L→M] — Mitigation: [Action]

ADJUSTMENT ACTIONS (This Week)
  1. [Action] — Owner: [Role] — Expected impact: [Metric improvement] — Start date: [Week #]
  2. [Action] — Owner: [Role] — Expected impact: [Metric improvement] — Start date: [Week #]

FORECAST TO ANNUAL TARGETS
  Revenue: [X]% probable of hitting $[Y]M target (confidence: [H/M/L])
  Growth: [X]% probable of hitting [Y]% growth (confidence: [H/M/L])
  Timeline: [Weeks ahead / on pace / weeks behind] vs. initial forecast

NEXT DECISION GATES
  - Gate 1: [Specific assumption/metric checkpoint] | Date: [Week #] | Decision trigger: [If [condition], then [pivot]]
  - Gate 2: [Specific assumption/metric checkpoint] | Date: [Week #] | Decision trigger: [If [condition], then [kill]]
═════════════════════════════════════════
```

---

## Assumption Register Status

```
ASSUMPTION REGISTER (Current Status)
═════════════════════════════════════════

MATERIAL ASSUMPTIONS (Impact if wrong: MATERIAL)
  1. [Assumption] — Confidence: [H] — Evidence: [Current support] — Next validation: [Week #]
  2. [Assumption] — Confidence: [M] — Evidence: [Current support] — Next validation: [Week #] — Risk: [Trigger approaching]
  3. [Assumption] — Confidence: [L] — Evidence: [Weak] — Action: [Course correction pending] — Next validation: [URGENT]

MODERATE ASSUMPTIONS (Impact if wrong: MODERATE)
  1. [Assumption] — Confidence: [H] — Validation complete: [Date]
  2. [Assumption] — Confidence: [M] — Next validation: [Week #]

CONFIDENCE SHIFTS (This Week)
  - [Assumption]: [H → M] because [evidence shift]
  - [Assumption]: [M → H] because [evidence strengthened]

ASSUMPTION RED FLAGS
  Trigger "CAC > $6K" status: [Has not fired / Probability raised to H] — Action: [Monitor weekly / Prepare pivot]
═════════════════════════════════════════
```

---

## Execution Risk Report

```
EXECUTION RISK TRACKER (Current)
═════════════════════════════════════════

HIGH RISKS (Probability: H OR Impact: H)
  Risk: [Risk name] — Probability: [H] — Impact: [H] — Overall: [🔴 Critical]
    Status: [Early warning active / Trigger fired / Mitigating]
    Owner: [Executive]
    Course correction if triggered: [Action]

  Risk: [Risk name] — Probability: [M] — Impact: [H] — Overall: [🟡 High]
    Status: [Monitoring]
    Early warning: [Indicator 1 status] [Indicator 2 status]
    Course correction if triggered: [Action]

MEDIUM RISKS (Probability: M AND Impact: M)
  Risk: [Risk name] — Status: [Monitoring / Early warning active]
  Risk: [Risk name] — Status: [Monitoring]

RISK TREND
  Risks increasing in probability: [#] — Focus area: [What]
  Risks decreasing in probability: [#] — Confidence gain: [What]

MITIGATION INVESTMENT
  Current spend on risk mitigation: $[X] | % of budget: [Y]%
  Risk-mitigated outcomes: [List 2-3 risks being actively mitigated]
═════════════════════════════════════════
```
