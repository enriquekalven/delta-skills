# Strategy Brief: Enterprise NRR Recovery via Automated Tier-1/Tier-2 Support Resolution
Date: 2026-08-14 | Sponsor: Chief Operating Officer & VP Customer Success | Confidence: HIGH

## 1. Governing Question & Bottom Line
- **Question:** Why did enterprise Net Revenue Retention (NRR) drop from 122% to 109% (-13 pts, -$11.4M ARR) over the last four quarters, and what intervention recovers NRR above 118% within 12 months?
- **Recommendation:** Execute **Option B (Deploy an ADK-based Tier-1/Tier-2 Resolution Agent integrated with Jira/Salesforce + Restructure CSM Ratios)** at a 12-month investment of **$1.45M (6 FTE + $350K cloud/licensing)** to cut median enterprise ticket resolution time from 46 hours to 4.2 hours, recovering **$8.2M in retained ARR** (projected NRR: 118.4%).

---

## 2. MECE Diagnostic Issue Tree

**Total Gap:** -$11.4M ARR (-13 pts NRR across $88M starting enterprise ARR base).

- **L1 Branch A: Gross Retention Degradation (-9.5 pts / -$8.36M ARR — PRIORITY, 73% of gap)** `[HIGH]`
  - *Baseline:* Across all 310 enterprise accounts, product uptime remained 99.95% and core feature usage held steady at 74% DAU/MAU.
  - *Differentiation:* Churned accounts experienced a **46.2-hour median Tier-2 ticket resolution SLA** (vs. 11.4 hours for retained accounts) after the Q2 support-tier migration.
  - **L2.1 (Support Backlog after ERP Connector Release):** 64% of churned accounts cited unresolved ERP sync failures waiting in Tier-2 engineering queues `[HIGH — Salesforce Churn Exit Survey, N=28]`.
  - **L2.2 (CSM Reactive Triage Load):** Enterprise CSMs spend 58% of weekly hours manually pulling Cloud Logging traces and writing status updates instead of running QBRs and expansion plays `[HIGH — 50-ticket time study]`.
- **L1 Branch B: Net Expansion Slowdown (-3.5 pts / -$3.08M ARR — 27% of gap)** `[HIGH]`
  - **L2.1 (Delayed Multi-Region Upsells):** Accounts with >3 open Severity-2 tickets froze seat expansion renewals `[HIGH — CRM pipeline audit]`.
  - **L2.2 (Pricing Discounting at Renewal):** Renewal reps granted an average 9% credit to offset SLA breaches, eroding expansion net dollars `[HIGH — Deal Desk logs]`.
- **L1 Branch C: Segment Mix Shift (0.0 pts — Deprioritized)** `[HIGH]`
  - Enterprise share of total ARR remained constant at 68% YoY; mix shift does not explain the NRR decline.

---

## 3. Strategic Options & Weighted Decision Matrix

1. **Option A: Offshore BPO Support Expansion (+25 Tier-1/Tier-2 contractors)**
   - Adds manual headcount ($1.9M/yr OpEx) without fixing diagnostic log correlation across BigQuery, Cloud Logging, and Jira.
2. **Option B (Recommended): Agentic Tier-1/Tier-2 Diagnostic & Triage Engine (Google Cloud ADK) + CSM Role Split**
   - Automates log correlation, schema diffing, and draft patch generation for ERP connector tickets on Vertex AI Agent Runtime; frees CSMs to run renewal/expansion QBRs.
3. **Option C: Status Quo + SLA Fee Credits**
   - Continues absorbing $8.36M annual churn + $1.1M in SLA credit concessions.

| Criterion | Weight | Option A (BPO Expansion) | Option B (ADK Triage Agent + CSM Split) | Option C (Status Quo) |
|---|---|---|---|---|
| Strategic Fit (Fixes root-cause SLA + frees CSMs) | 25% | 5.0 | **9.0** | 2.0 |
| Time-to-Value (Impact within 2 quarters) | 20% | 7.0 | **8.0** | 3.0 |
| Implementation Feasibility | 20% | 8.0 | **7.5** | 9.0 |
| Capital Efficiency (3-yr ROI) | 15% | 4.0 | **9.0** | 2.0 |
| Risk-Adjusted Return | 20% | 5.0 | **8.5** | 1.0 |
| **Weighted Score** | **100%** | **5.85** | **8.40** | **3.30** |

*Sensitivity Check:* Even if Implementation Feasibility weight increases from 20% to 35%, Option B leads Option A (8.18 vs. 6.38).

---

## 4. 90-Day Resource-Loaded Execution Plan

| Workstream | Days 1–30 | Days 31–60 | Days 61–90 | FTE / Budget | Owner |
|---|---|---|---|---|---|
| **WS1: Baseline & Golden Eval Set** | Audit 50 historical ERP sync tickets; freeze `docs/baseline_kpis.json` and 200-case eval suite | Run shadow-mode evaluation against live Zendesk/Jira stream | Gate cutover to L2 human-in-the-loop production | 1.5 FTE / $40K | Technical Deployment Lead |
| **WS2: ADK Diagnostic Agent Build** | Build read-only tools for Cloud Logging, BigQuery schema inspector, and Jira history | Add automated root-cause classification & remediation draft generator | Deploy to Vertex AI Agent Runtime with VPC-SC perimeter | 3.0 FTE / $210K | Forward-Deployed Engineers |
| **WS3: Support & CSM Operating Model** | Redefine L2 Support Engineer queue around agent-drafted packets; remove ticket triage from CSMs | Train 18 Support Engineers on HITL review console | Reassign CSMs to 60-day pre-renewal expansion playbooks | 1.5 FTE / $100K | VP Customer Success |

---

## 5. Risks, Assumptions & Kill Conditions

| Item | Type | Threshold / Trigger | Action if Triggered |
|---|---|---|---|
| **Diagnostic accuracy on ERP tickets** | Kill Condition | Shadow-mode root-cause precision < 80% on the 200-ticket eval set at Day 45 | Halt autonomous ticket updates; restrict agent to log-bundle retrieval and escalate retrieval pipeline redesign |
| **Support Engineer adoption** | Kill Condition | Weekly HITL draft acceptance rate < 50% after 3 weeks in production (Day 75) | Freeze rollout to additional ticket categories; audit top 20 rejected drafts and retrain prompt/tool schema |
| **Ticket volume spike during Q4 ERP upgrade** | Risk | Inbound volume exceeds 1,800 tickets/week (+40% over baseline) | Pre-provision Vertex AI provisioned throughput and enforce strict L3 auto-acknowledge + log prefetch |
| **CSM time reallocation** | Assumption | Freed CSM hours (14 hrs/week/CSM) convert into >=2 additional executive QBRs per CSM per week | Track QBR completion weekly in Salesforce; tie Q3 variable comp to QBR coverage on renewals <120 days out |
