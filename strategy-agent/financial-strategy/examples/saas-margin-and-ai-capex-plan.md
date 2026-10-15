# Financial Case & Unit Economics Analysis: Support COGS Transformation & Gross Margin Expansion
Date: 2026-08-19 | WACC: 10.0% | Currency: USD

## 1. Executive Bottom Line
Deploying the automated Tier-1/Tier-2 diagnostic agent and migrating legacy log search onto BigQuery + Vertex AI requires **$650K in Year 0 CapEx** and generates **$3.82M in risk-adjusted 3-year net cash flow** (**3-Year NPV @ 10%: $2.47M**, **IRR: 148%**, **Payback: 6.8 months**), expanding company-wide Gross Margin by **+340 bps** (from 68.2% to 71.6%).

---

## 2. P&L & Unit Economics Diagnostic (Current vs. Target)

**Company Baseline:** $85.0M ARR across 500 enterprise customers ($170K average ACV). Gross margin has compressed from 72.0% to 68.2% (-380 bps) over 6 quarters due to support headcount growth and third-party log indexing overages.

| Metric | Current Baseline | Post-Initiative Target (Yr 2) | Delta | Key Assumption |
|---|---|---|---|---|
| **ARR** | $85,000K | $85,000K (held constant for cost case) | $0 | Excludes upside NRR expansion to isolate hard COGS impact |
| **Hosting & Observability COGS** | $14,450K (17.0% ARR) | $13,090K (15.4% ARR) | -160 bps (-$1,360K/yr) | Consolidating 42 TB/mo diagnostic logs from legacy APM to BigQuery partitioned tables |
| **Customer Support COGS** | $12,580K (14.8% ARR) | $10,540K (12.4% ARR) | -240 bps (-$2,040K/yr) | Automating 55% of Tier-1/2 log triage avoids 12 backfills/contractors @ $170K/yr fully loaded |
| **AI Inference & Agent Runtime COGS** | $0K (0.0% ARR) | $510K (0.6% ARR) | +60 bps (+$510K/yr) | 180,000 tickets/yr × $2.83 blended Vertex AI + Agent Runtime cost per ticket |
| **Total Gross Margin %** | **68.2%** | **71.6%** | **+340 bps (+$2,890K/yr)** | Net COGS reduction after accounting for new AI token & runtime spend |
| **Contribution Margin / Customer** | $115.9K / yr | $121.7K / yr | +$5.8K / customer / yr | Improves enterprise LTV from $966K to $1,014K at 12% gross churn |
| **CAC Payback Period** | 21.4 months | 20.4 months | -1.0 month | Fully loaded enterprise CAC held constant at $206K |

---

## 3. 3-Year Cash Flow & TCO Schedule ($K)

**Value Capture Rules Applied:**
- **Hard Vendor Savings (100% capture):** Legacy log indexing contract down-tiering takes effect at Month 7 renewal ($680K saved in Yr 1, $1,360K/yr in Yrs 2–3).
- **Support Labor Savings (75% capture in Yr 1, 100% in Yrs 2–3):** Freeze 6 open contractor requisitions immediately ($510K Yr 1); natural attrition + BPO contract reduction of 12 seats by Q4 ($2,040K/yr in Yrs 2–3).

| Line Item ($K) | Year 0 (Build) | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|---|
| **CapEx: FDE Build & BigQuery Log Migration** | ($520) | $0 | $0 | $0 | ($520) |
| **CapEx: Security Audit & Golden Eval Harness** | ($130) | $0 | $0 | $0 | ($130) |
| **OpEx: Vertex AI Inference & Agent Runtime** | $0 | ($380) | ($510) | ($560) | ($1,450) |
| **OpEx: MLOps Maintenance & Prompt Eval (0.5 FTE)** | $0 | ($95) | ($95) | ($100) | ($290) |
| **Total Cost (TCO)** | **($650)** | **($475)** | **($605)** | **($660)** | **($2,390)** |
| **Hard Inflow: Observability Vendor Reduction** | $0 | $680 | $1,360 | $1,360 | $3,400 |
| **Hard Inflow: Avoided BPO & Contractor Spend** | $0 | $510 | $1,530 | $1,770 | $3,810 |
| **Gross Cash Inflows** | **$0** | **$1,190** | **$2,890** | **$3,130** | **$7,210** |
| **Risk-Adjusted Haircut (0.85 SCDF on Labor)** | $0 | ($77) | ($230) | ($266) | ($573) |
| **Net Cash Flow** | **($650)** | **$638** | **$2,055** | **$2,204** | **$3,817** |
| **Discount Factor (WACC = 10%)** | 1.000 | 0.909 | 0.826 | 0.751 | — |
| **Discounted Cash Flow (PV)** | **($650)** | **$580** | **$1,697** | **$1,655** | **NPV: $2,469K** |

---

## 4. Scenario & Sensitivity Matrix (Base / Bull / Bear)

| Scenario | Ticket Deflection Rate | Inference Cost / Ticket | 3-Yr Net Cash Flow | 3-Yr NPV @ 10% | IRR | Payback |
|---|---|---|---|---|---|---|
| **Base Case (Target)** | 55% Tier-1/2 automated | $2.83 | **$3,817K** | **$2,469K** | **148%** | **6.8 mos** |
| **Bull Case (High Deflection + Caching)** | 70% Tier-1/2 automated | $1.90 (context caching) | **$5,140K** | **$3,912K** | **212%** | **5.1 mos** |
| **Bear Case (Delayed BPO Exit + 2x Tokens)** | 35% Tier-1/2 automated | $5.60 | **$1,490K** | **$892K** | **54%** | **13.5 mos** |

**Kill Condition:** If shadow-mode pilot in Month 2 shows Ticket Deflection < 30% OR inference cost exceeds $6.50/ticket after prompt caching, halt BPO contract reduction and restrict deployment to BigQuery log tiering only (standalone NPV of log migration = $1.12M).
