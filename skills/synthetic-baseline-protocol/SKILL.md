---
name: synthetic-baseline-protocol
description: >
  Execute a 50-sample retrospective audit of historical customer tickets, documents, or logs with client SMEs
  to establish manual unit costs, handling time, and error rates, outputting a frozen baseline_kpis.json benchmark artifact for Phase 4 eval ROI comparison.
  Triggers on: "synthetic baseline protocol", "baseline kpi audit", "audit baseline kpis", "run baseline audit", "create baseline_kpis.json".
---

# Synthetic Baseline Protocol

Quantitative pre-deployment baseline protocol for capturing manual operational metrics before system deployment.

---

## 4-Step Baseline Protocol

```
1. Sample Selection --> 2. Retrospective Audit --> 3. Financial Unit Cost --> 4. Freeze baseline_kpis.json
   (50 Rep. Records)     (SME Workstation Time)      (Labor + OpEx Rate)       (Benchmark Artifact)
```

### Step 1: Sample Selection (N = 50)
Select 50 representative historical records (support tickets, underwriting files, claims, or manual ETL logs):
* 35 Standard Cases (70%)
* 10 Complex / Edge Cases (20%)
* 5 Outlier / Malformed Cases (10%)

### Step 2: SME Retrospective Workstation Time Audit
Audit client Subject Matter Experts (SMEs) to measure manual baseline parameters across the 50 samples:
* **Handling Time ($T_{\text{manual}}$)**: Average minutes spent per item.
* **Error Rate ($E_{\text{manual}}$)**: Percentage of items requiring manual re-work.
* **Escalation Frequency ($X_{\text{manual}}$)**: Percentage of items escalated to senior specialists.

### Step 3: Financial Unit Cost Calculation
Calculate baseline unit cost per transaction ($C_{\text{unit}}$):

$$C_{\text{unit}} = \left( \frac{T_{\text{manual}}}{60} \times \text{Blended Hourly Rate} \right) + \text{Infrastructure Overhead}$$

### Step 4: Output `baseline_kpis.json`
Write the benchmark artifact to `docs/baseline_kpis.json`.

---

## Benchmark Schema (`baseline_kpis.json`)

```json
{
  "project_name": "Real Estate Concierge Agent",
  "audit_date": "2026-07-21",
  "sample_size": 50,
  "blended_hourly_rate_usd": 75.00,
  "baseline_metrics": {
    "avg_handling_time_minutes": 45.0,
    "error_rate_percent": 14.0,
    "escalation_rate_percent": 8.0,
    "unit_cost_usd": 56.25,
    "annual_volume_units": 12000,
    "total_baseline_annual_cost_usd": 675000.00
  },
  "target_post_deployment_kpis": {
    "target_handling_time_minutes": 3.0,
    "target_error_rate_percent": 2.0,
    "target_unit_cost_usd": 4.50,
    "projected_annual_savings_usd": 621000.00
  }
}
```

---

## Phase 1 Gate Verification Checklist
- [ ] 50 representative historical records audited with client SME.
- [ ] Handling time, error rate, and unit cost computed.
- [ ] `baseline_kpis.json` committed to `docs/baseline_kpis.json`.
- [ ] Client sponsor sign-off obtained for Phase 4 evaluation comparison.
