# Governance Framework: RACI & Escalation

Design decision rights and escalation paths using RACI matrix.

## RACI Definition

- **Responsible:** Does analysis; implements decision
- **Accountable:** Approves decision; owns outcome; can override
- **Consulted:** Provides input; their perspective matters
- **Informed:** Kept in the loop; no input required

## Example RACI Matrix

### Product Roadmap Priority Decision
```
Decision: Product roadmap priority (e.g., New Feature A vs. Enhancement B)
   Responsible: VP Product (decision owner; does analysis)
   Accountable: CEO (approves; owns outcome)
   Consulted: VP Eng (feasibility), VP GTM (market need), CFO (resource cost)
   Informed: All-hands (communication post-decision)
```

### Customer Expansion Deal ($100K+)
```
Decision: Customer > $100K expansion deal
   Responsible: VP Sales (owns negotiation)
   Accountable: Chief Revenue Officer (approves; owns quota)
   Consulted: VP Delivery (can we deliver?), Finance (contract terms)
   Informed: Customer Success team
```

### Critical Role Hiring (VP Eng, Director Finance)
```
Decision: New hire for critical role
   Responsible: Hiring manager (leads search, interviews)
   Accountable: CEO (approves; owns cultural fit)
   Consulted: Team (panel interviews), People Ops (process), Finance (budget)
   Informed: Leadership team
```

## Escalation Rules (When does something escalate?)

### Product Decision
```
├─ Impacts revenue forecast by > 10%? → Escalate to CEO
├─ Requires resource reallocation across teams? → Escalate to CTO + VP Product
├─ Breaks user promise or brand promise? → Escalate to CEO
└─ Otherwise → VP Product decides
```

### Sales/Customer Decision
```
├─ Contract value > $500K? → Escalate to CRO + CEO
├─ Legal/compliance issue? → Escalate to General Counsel + CEO
├─ Customer churn risk > $50K? → Escalate to CRO
└─ Otherwise → VP Sales decides
```

### Operational/Budget Decision
```
├─ Expense > quarterly budget by > 20%? → Escalate to CFO + CEO
├─ Impacts hiring plan? → Escalate to CHRO + CFO
├─ New capability required? → Escalate to relevant CXO
└─ Otherwise → Functional owner decides
```

## Building Your RACI Matrix

1. **Identify 8-10 critical decisions** that happen repeatedly
2. **For each decision, assign:** Responsible, Accountable, Consulted, Informed
3. **Make sure no role is Accountable for two conflicting decisions** (creates ambiguity)
4. **Keep Responsible count low** (too many = decision paralysis)
5. **Make Accountable crystal clear** (no "co-accountability")
6. **Define Consulted scope narrowly** (too many consultants slow decisions)
7. **Test the matrix:** Walk through a recent decision. Does the RACI match how it actually happened? If not, refine.

## Governance Output Template

- **Decision Charter:** RACI matrix for 8-10 critical decisions
- **Escalation Rules:** Explicit triggers for escalation by decision category
- **Review Cadence:** Daily/Weekly/Monthly/Quarterly/Annual meeting structure
- **Approval Authority:** Spending limits, hiring, strategic decisions by role level
