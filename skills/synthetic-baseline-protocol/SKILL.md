---
name: synthetic-baseline-protocol
description: >
  Execute a 50-sample retrospective audit of historical customer tickets, documents, or logs with client SMEs
  to establish manual unit costs, handling time, and error rates, outputting a frozen baseline_kpis.json benchmark artifact for Phase 4 eval ROI comparison.
  Triggers on: "synthetic baseline protocol", "baseline kpi audit", "audit baseline kpis", "run baseline audit", "create baseline_kpis.json".
---

# Synthetic Baseline Protocol (Pre-Deployment KPI Benchmark)

This skill guides Technical Deployment Leads (TDLs) and AI Activation Leads (AIALs) through a 50-sample retrospective audit of historical client workflows to capture quantitative baseline operational metrics in Phase 1 (Weeks 0-2) before any code is built.

---

## 📋 The 4-Step Baseline Protocol

```
1. SAMPLE SELECTION ──→ 2. RETROSPECTIVE AUDIT ──→ 3. UNIT COST METRICS ──→ 4. FREEZE BASELINE_KPIS.JSON
   (50 Rep. Tickets)     (SME Workstation Time)      (Labor + OpEx Rate)       (Frozen Benchmark)
```

### Step 1: Representative Sample Selection (N = 50)
Select 50 historical customer interactions (support tickets, underwriting PDFs, claims files, or manual ETL records) covering:
* 35 Standard Cases (70%)
* 10 Complex / Edge Cases (20%)
* 5 Outlier / Malformed Cases (10%)

### Step 2: SME Retrospective Workstation Time Audit
Interview client Subject Matter Experts (SMEs) to measure manual handling parameters across the 50 samples:
* **Handling Time ($T_{\text{manual}}$)**: Average minutes spent per item.
* **Error / Rework Rate ($E_{\text{manual}}$)**: Percentage of items requiring secondary manual correction.
* **Escalation Frequency ($X_{\text{manual}}$)**: Percentage of items escalated to Tier 3 specialists.

### Step 3: Financial Unit Cost Calculation
Compute the baseline financial unit cost per transaction ($C_{\text{unit}}$):

$$C_{\text{unit}} = \left( \frac{T_{\text{manual}}}{60} \times \text{Blended Hourly Labor Rate} \right) + \text{Legacy Infrastructure Overhead}$$

### Step 4: Generate Frozen `baseline_kpis.json`
Output the benchmark artifact to the project root directory (`docs/baseline_kpis.json`).

---

## 📄 JSON Benchmark Schema (`baseline_kpis.json`)

```json
{
  "project_name": "Multimodal Real Estate Concierge Agent",
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

## ✋ Phase 1 Gate Verification Checklist
- [ ] 50 representative historical samples audited with client SME
- [ ] Handling time, error rate, and unit cost calculated
- [ ] `baseline_kpis.json` generated and committed to project root
- [ ] Client sponsor signed off on baseline numbers for Phase 4 ROI comparison
