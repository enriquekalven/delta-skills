# KPI Cascade Design

## Translate Strategy into Metric Hierarchy

```
STRATEGIC OBJECTIVE
│
├── ANNUAL TARGETS (What must be true at year-end?)
│   └── Targets: Revenue, Growth Rate, Profitability, Customer Acquisition, Retention
│
├── QUARTERLY MILESTONES (What quarterly gates must we hit?)
│   └── Gates by function: Product PMF signals, GTM customer acquisition, Org capacity milestones
│
├── MONTHLY METRICS (What trends are we monitoring?)
│   └── Metrics by function: CAC, LTV, Churn, NPS, Feature adoption, Hiring progress
│
└── WEEKLY LEADING INDICATORS (What do we measure to steer?)
    └── Metrics: Pipeline health, demo conversion, onboarding completion, hiring applications
```

## Metric Selection Criteria

| Metric Type | Definition | Cadence | Example |
|---|---|---|---|
| **Strategic** | Annual target that defines success | Monthly review | Revenue: $50M ARR by Dec 31 |
| **Leading** | Predictive of future outcome; controllable | Weekly | Pipeline conversion rate, onboarding completion % |
| **Operational** | In-flight execution metric; real-time course steering | Daily/Weekly | Marketing pipeline $ by stage, hiring offers extended |
| **Lagging** | Outcome after actions taken; validation signal | Monthly/Quarterly | Revenue achieved, customer churn rate |

## Traffic Light Thresholds (Be Specific)

For each metric, define three ranges:
- **GREEN threshold:** On-track or exceeding plan
- **AMBER threshold:** Below plan but correctable; action plan required
- **RED threshold:** Strategy-invalidating miss; course correction decision needed

Example:

```
KPI: CAC (Customer Acquisition Cost)
Plan: $5,000 per customer
  GREEN: $4,500-$5,500 (within 10%)
  AMBER: $5,500-$6,500 (11-30% over)
  RED: >$6,500 (>30% over; payback > 18mo; scaling uneconomic)

Action if RED: Evaluate new channel, improve conversion, adjust pricing, or kill initiative
```

## Key Success Factors

1. **Specificity matters** — "improve growth" is useless; "$X.XM ARR by Dec 31, $XXK MRR by end of Q1" is specific
2. **Connect to strategy** — Each metric should ladder up to a strategic objective
3. **Balance leading + lagging** — Don't rely on lagging KPIs alone; use leading indicators to steer
4. **Actionability** — Every metric should drive a decision or action
5. **Realistic but ambitious** — Targets should stretch but be achievable with execution excellence
