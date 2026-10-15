# Worked Example: 50-Sample Commercial Auto Claims Baseline Audit (`docs/baseline_kpis.json`)

## 1. Audit Context & Stratification
- **Engagement:** Acme P&C Insurance — Commercial Auto FNOL Intake & Triage Agent
- **Audit Window:** `2026-04-01` through `2026-06-30` (Q2 historical closed claims)
- **Stratified Random Sample ($N = 50$):**
  - **Standard (35 claims / 70%):** Single-vehicle commercial fender/glass/parking claims (`ACORD 2` + 1 repair estimate).
  - **Complex (10 claims / 20%):** Multi-vehicle highway collisions involving third-party commercial carriers, subrogation recovery, or bodily injury attachments.
  - **Outlier / Malformed (5 claims / 10%):** Low-DPI handwritten county sheriff reports, missing policy numbers, or duplicate broker attachments.

---

## 2. Reproducible Calculation via `scripts/compute_baseline_stats.py`

```bash
python3 delivery/synthetic-baseline-protocol/scripts/compute_baseline_stats.py \
  --times-json "[16,18,18,19,20,21,22,23,24,25,26,28,30,32,34,35,36,37,37,38,38,38,38,38,38,38,38,39,40,41,42,43,44,45,46,50,53,56,59,62,66,70,74,78,82,84,88,91,95,97]" \
  --errors 7 \
  --escalations 4 \
  --hourly-rate 75.00 \
  --overhead-per-unit 0.00 \
  --annual-volume 12000
```

- **Sample Size ($N$):** `50`
- **Handling Time ($T$):** Mean = `45.0 mins`, Median = `38.0 mins`, p90 = `82.0 mins`, SD = `22.01 mins`, 95% CI = `[38.9, 51.1] mins`
- **Error / Rework Rate ($E$):** `7 / 50 = 14.0%` (95% Wilson CI: `[7.0%, 26.2%]`)
- **Senior Escalation Rate ($X$):** `4 / 50 = 8.0%` (95% Wilson CI: `[3.2%, 18.8%]`)

---

## 3. Frozen Deliverable (`docs/baseline_kpis.json`)

Committed to repository root under `docs/baseline_kpis.json` and recorded in `STATE.md` (`baseline_commit_sha: 4f91a2c8e01b3d77f89210ab44c9102e88a12b03`):

```json
{
  "project_name": "Acme P&C Commercial Auto Claims FNOL Agent",
  "audit_date": "2026-08-21",
  "sample": {
    "size": 50,
    "mix": {
      "standard": 35,
      "complex": 10,
      "outlier": 5
    },
    "window": "2026-04-01..2026-06-30",
    "timing_source": {
      "system_timestamps": 42,
      "observed": 8,
      "sme_recall": 0
    }
  },
  "blended_hourly_rate_usd": 75.00,
  "baseline_metrics": {
    "handling_time_minutes": {
      "mean": 45.0,
      "median": 38.0,
      "p90": 82.0,
      "sd": 22.01,
      "ci95": [38.9, 51.1]
    },
    "error_rate_percent": {
      "value": 14.0,
      "ci95": [7.0, 26.2]
    },
    "escalation_rate_percent": {
      "value": 8.0,
      "ci95": [3.2, 18.8]
    },
    "infrastructure_overhead_per_unit_usd": 0.00,
    "unit_cost_usd": 56.25,
    "annual_volume_units": 12000,
    "total_baseline_annual_cost_usd": 675000.00
  },
  "target_post_deployment_kpis": {
    "_note": "Hypotheses. The final read-out (weeks 11-12) must replace these with measured values on an N=50 post-launch sample.",
    "handling_time_minutes": 3.0,
    "error_rate_percent": 2.0,
    "infrastructure_overhead_per_unit_usd": 0.75,
    "unit_cost_usd": 4.50,
    "projected_annual_savings_usd": 621000.00
  }
}
```
