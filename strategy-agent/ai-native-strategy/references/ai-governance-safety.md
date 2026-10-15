# AI Governance, Safety & Operational Controls Reference

Use this reference to define risk tiers, human-in-the-loop (HITL) autonomy boundaries, production monitoring thresholds, and incident containment runbooks.

---

## 1. Use-Case Risk Classification

| Risk Tier | Definition | Examples | Mandatory Controls |
| :--- | :--- | :--- | :--- |
| **Tier 1: Prohibited** | Unacceptable legal or safety risk | Unconsented biometric surveillance, deceptive manipulation | Do not build or deploy |
| **Tier 2: High Risk** | Material financial, legal, medical, or employment impact | Underwriting/lending decisions, claims denial, hiring screening | Mandatory human sign-off on adverse actions, immutable audit log, bias/fairness eval, explainable citations |
| **Tier 3: Bounded Operational Risk** | External customer communication or internal system writes with bounded financial exposure | Automated support resolution, low-dollar claims fast-track ($\le \$5\text{K}$) | Confidence floor ($\ge 0.85$), dollar cap, automatic escalation to human queue on low confidence |
| **Tier 4: Low / Internal Productivity** | Read-only summarization, internal drafting, code assistance | Meeting notes, internal knowledge search, draft generation | Source citations, standard access controls (IAM) |

---

## 2. Autonomy Levels & Human-in-the-Loop (HITL) Gates

| Level | Name | Agent Authority | Human Role |
| :--- | :--- | :--- | :--- |
| **L0** | Manual Baseline | None | Executes 100% of workflow |
| **L1** | Read-Only Copilot | Retrieves context and summarizes evidence | Makes decision and executes all system writes |
| **L2** | Recommend & Approve (HITL) | Extracts data, runs rules, prepares payload | Reviews side-by-side citations and clicks Approve/Override |
| **L3** | Bounded Conditional Autonomy (HOTL) | Auto-executes within strict guardrails (e.g., confidence $\ge 0.85$ and value $\le \$5\text{K}$); routes exceptions to L2 | Audits 5% random sample; handles all escalated exceptions |
| **L4** | Full Autonomy | Executes end-to-end with automated circuit breakers | Monitors aggregate SLA/drift dashboards and kill switches |

---

## 3. Production Monitoring & Circuit-Breaker Thresholds

| Metric | Target | Warning Alert | Circuit-Breaker / Rollback Trigger |
| :--- | :--- | :--- | :--- |
| **Citation / Grounding Accuracy** | $\ge 97\%$ | $< 95\%$ on daily eval sample | $< 92\%$ $\rightarrow$ Downgrade L3 auto-execution to L2 HITL review |
| **Human Override Rate** | $\le 10\%$ | $> 15\%$ over 24h rolling window | $> 25\%$ $\rightarrow$ Freeze auto-routing for affected category |
| **Upstream Tool Error Rate** | $< 0.5\%$ | $> 1.0\%$ | $> 3.0\%$ $\rightarrow$ Trip circuit breaker; route directly to manual queue |
| **Cost per Transaction** | Within budget | $+20\%$ spike vs. 7-day baseline | $+50\%$ spike $\rightarrow$ Enforce hard per-request token cap |
| **Prompt Injection / Policy Violation** | `0` successful | Elevated block rate at input filter | Any successful unauthorized tool call $\rightarrow$ Immediate credential revoke |
