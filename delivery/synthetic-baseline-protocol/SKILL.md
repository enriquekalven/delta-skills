---
name: synthetic-baseline-protocol
description: >
  Establish a pre-deployment baseline by auditing 50 representative historical work items
  (tickets, claims, files, logs) with client SMEs to measure manual handling time, error
  rate, escalation rate and unit cost, then freeze docs/baseline_kpis.json for the Phase 4
  ROI comparison. Triggers on "baseline audit", "baseline kpis", "create baseline_kpis.json",
  "measure the manual process before we build". Do NOT use for forward-looking market sizing
  (use ai-value-sizing).
metadata:
  version: '1.0'
---

# Synthetic Baseline Protocol

You cannot prove an AI system saved money without a measured "before". This protocol
produces that number in Phase 1, and freezes it so it cannot drift to flatter the result.

```
1. Select 50 samples -> 2. Audit with SMEs -> 3. Compute unit cost -> 4. Freeze baseline_kpis.json
```

## Step 1: Select the sample (N = 50)

Draw from a recent, representative window (e.g. the last 1-3 months) and stratify:

| Stratum | Count | Share | Examples |
|---|---|---|---|
| Standard | 35 | 70% | Routine, well-formed items |
| Complex / edge | 10 | 20% | Multi-step, ambiguous, policy exceptions |
| Outlier / malformed | 5 | 10% | Missing data, wrong channel, garbage input |

- Adjust the split if the real volume mix differs, and **record the actual mix**.
- Pick randomly within each stratum. Do not let the client hand-pick "good examples".
- Use sanitized copies. Real client data stays in the client environment.

## Step 2: Audit with SMEs

For each item, capture:

| Metric | Symbol | Definition |
|---|---|---|
| Handling time | T | Active minutes of work per item (not wall-clock queue time) |
| Error / rework | E | Item needed correction or rework (yes/no) |
| Escalation | X | Item was escalated to a senior specialist (yes/no) |

**Evidence quality, best to worst:** system timestamps (ticket open/close, audit logs) >
observed timing of SMEs redoing the item > SME recall. Record which source each value came
from. SME recall routinely underestimates time; flag it when it is the only source.

## Step 3: Compute unit cost

```
C_unit = (T / 60) x blended_hourly_rate + infrastructure_overhead_per_unit
```

- `blended_hourly_rate`: fully loaded (salary + benefits + overhead), agreed with finance.
- `infrastructure_overhead_per_unit`: tooling or licence cost per item. Use `0` only if
  none exists, and write it as an explicit `0`.

**Report the distribution, not only the mean:**
- mean, median and p90 of T
- a 95% confidence interval for mean T: `mean +/- 1.96 x (sd / sqrt(50))` (use a bootstrap if T
  is heavily skewed)
- E and X as proportions, with 95% CIs (e.g. Wilson interval)

With N = 50, a 14% error rate has a CI of roughly +/-10 points. Say so, rather than implying
false precision.

## Step 4: Freeze `docs/baseline_kpis.json`

Commit the file, record the commit SHA in `STATE.md`, and do not edit it afterwards. If
the baseline must change, add a new versioned file and explain why.

```json
{
  "project_name": "Real Estate Concierge Agent",
  "audit_date": "2026-07-21",
  "sample": {
    "size": 50,
    "mix": {"standard": 35, "complex": 10, "outlier": 5},
    "window": "2026-04-01..2026-06-30",
    "timing_source": {"system_timestamps": 38, "observed": 8, "sme_recall": 4}
  },
  "blended_hourly_rate_usd": 75.00,
  "baseline_metrics": {
    "handling_time_minutes": {"mean": 45.0, "median": 38.0, "p90": 82.0, "ci95": [39.1, 50.9]},
    "error_rate_percent": {"value": 14.0, "ci95": [7.0, 26.2]},
    "escalation_rate_percent": {"value": 8.0, "ci95": [3.2, 18.8]},
    "infrastructure_overhead_per_unit_usd": 0.00,
    "unit_cost_usd": 56.25,
    "annual_volume_units": 12000,
    "total_baseline_annual_cost_usd": 675000.00
  },
  "target_post_deployment_kpis": {
    "_note": "Hypotheses. Phase 4 must replace these with measured values.",
    "handling_time_minutes": 3.0,
    "error_rate_percent": 2.0,
    "infrastructure_overhead_per_unit_usd": 0.75,
    "unit_cost_usd": 4.50,
    "projected_annual_savings_usd": 621000.00
  }
}
```

Check the example: baseline `45/60 x 75 + 0 = 56.25`, and `56.25 x 12000 = 675000`.
Target `3/60 x 75 + 0.75 = 4.50`, `4.50 x 12000 = 54000`, and savings
`675000 - 54000 = 621000`.

## Hand-off

- [ai-value-sizing](../../ai-value-sizing/SKILL.md) uses `unit_cost_usd` and
  `annual_volume_units` as the cost-of-status-quo input for ROI/TCO.
- In Phase 4, run the same metrics on a comparable post-deployment sample (same stratum
  mix) and report measured vs. baseline, with CIs.

## Gate checklist

- [ ] 50 items audited, with the actual stratum mix recorded
- [ ] Timing source recorded per item; recall-only values flagged
- [ ] Mean, median, p90 and 95% CI reported for handling time
- [ ] Overhead field explicit (even if 0); arithmetic checks out
- [ ] `docs/baseline_kpis.json` committed and its SHA recorded in `STATE.md`
- [ ] Sponsor sign-off that this baseline is the Phase 4 comparison point
