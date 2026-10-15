#!/usr/bin/env python3
"""Compute mean, median, p90, 95% normal CI, and 95% Wilson CIs for a 50-sample baseline audit."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path


def wilson_ci95(successes: int, total: int) -> tuple[float, float]:
    """Return 95% Wilson score interval (as percentages 0..100) for a binomial proportion."""
    if total <= 0:
        raise ValueError("total must be > 0")
    z = 1.959963984540054
    phat = successes / total
    denom = 1.0 + (z * z) / total
    center = (phat + (z * z) / (2.0 * total)) / denom
    half = (
        z
        * math.sqrt((phat * (1.0 - phat) + (z * z) / (4.0 * total)) / total)
        / denom
    )
    low = max(0.0, (center - half) * 100.0)
    high = min(100.0, (center + half) * 100.0)
    return round(low, 1), round(high, 1)


def compute_baseline_metrics(
    times_minutes: list[float],
    errors_count: int,
    escalations_count: int,
    hourly_rate_usd: float,
    overhead_per_unit_usd: float,
    annual_volume_units: int,
) -> dict[str, object]:
    """Compute distribution stats and unit cost for synthetic-baseline-protocol."""
    n = len(times_minutes)
    if n < 2:
        raise ValueError("At least 2 sample handling times are required")
    if not (0 <= errors_count <= n) or not (0 <= escalations_count <= n):
        raise ValueError("errors_count and escalations_count must be between 0 and sample size")

    sorted_t = sorted(times_minutes)
    mean_t = statistics.fmean(sorted_t)
    median_t = statistics.median(sorted_t)
    sd_t = statistics.stdev(sorted_t)
    p90_idx = min(n - 1, max(0, math.ceil(0.90 * n) - 1))
    p90_t = sorted_t[p90_idx]
    half_ci = 1.959963984540054 * (sd_t / math.sqrt(n))

    err_pct = round((errors_count / n) * 100.0, 1)
    esc_pct = round((escalations_count / n) * 100.0, 1)
    err_ci = wilson_ci95(errors_count, n)
    esc_ci = wilson_ci95(escalations_count, n)

    unit_cost = (mean_t / 60.0) * hourly_rate_usd + overhead_per_unit_usd
    annual_cost = unit_cost * annual_volume_units

    return {
        "sample_size": n,
        "handling_time_minutes": {
            "mean": round(mean_t, 1),
            "median": round(median_t, 1),
            "p90": round(p90_t, 1),
            "sd": round(sd_t, 2),
            "ci95": [round(mean_t - half_ci, 1), round(mean_t + half_ci, 1)],
        },
        "error_rate_percent": {
            "value": err_pct,
            "ci95": [err_ci[0], err_ci[1]],
        },
        "escalation_rate_percent": {
            "value": esc_pct,
            "ci95": [esc_ci[0], esc_ci[1]],
        },
        "infrastructure_overhead_per_unit_usd": round(overhead_per_unit_usd, 2),
        "unit_cost_usd": round(unit_cost, 2),
        "annual_volume_units": annual_volume_units,
        "total_baseline_annual_cost_usd": round(annual_cost, 2),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--times-json",
        type=str,
        required=True,
        help="JSON array of handling times in minutes (or path to a .json file containing the array).",
    )
    parser.add_argument("--errors", type=int, required=True, help="Count of items requiring rework/correction")
    parser.add_argument("--escalations", type=int, required=True, help="Count of items escalated to senior specialist")
    parser.add_argument("--hourly-rate", type=float, required=True, help="Blended fully-loaded hourly rate (USD)")
    parser.add_argument("--overhead-per-unit", type=float, default=0.0, help="Existing licence/infra overhead per unit (USD)")
    parser.add_argument("--annual-volume", type=int, required=True, help="Annual transaction volume (units)")
    args = parser.parse_args(argv)

    try:
        raw = args.times_json.strip()
        if raw.startswith("["):
            times = [float(x) for x in json.loads(raw)]
        else:
            times = [float(x) for x in json.loads(Path(raw).read_text(encoding="utf-8"))]
        metrics = compute_baseline_metrics(
            times_minutes=times,
            errors_count=args.errors,
            escalations_count=args.escalations,
            hourly_rate_usd=args.hourly_rate,
            overhead_per_unit_usd=args.overhead_per_unit,
            annual_volume_units=args.annual_volume,
        )
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
