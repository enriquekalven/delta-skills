#!/usr/bin/env python3
"""Deterministic TAM/SAM/SOM and 3-Year ROI/NPV calculator for ai-value-sizing."""

from __future__ import annotations

import argparse
import json
import sys


DEMO_DEFAULTS: dict[str, float] = {
    "tam_units": 80000.0,
    "sam_share": 0.625,
    "adoption_rate": 0.30,
    "tech_compat": 0.80,
    "hours_saved": 0.70,
    "hourly_rate": 75.0,
    "capex": 180000.0,
    "annual_opex": 68000.0,
    "vcr": 0.60,
    "scdf": 0.85,
    "wacc": 0.10,
}


def compute_sizing_and_roi(
    tam_units: float,
    sam_share: float,
    adoption_rate: float,
    tech_compat: float,
    hours_saved_per_unit: float,
    hourly_rate_usd: float,
    capex_usd: float,
    annual_opex_usd: float,
    vcr: float,
    scdf: float,
    wacc: float = 0.10,
    annual_non_labor_benefit_usd: float = 0.0,
    year1_ramp: float = 1.0,
) -> dict[str, object]:
    """Calculate SOM (Q), Gross/Risk-Adjusted Annual Value, Post-OpEx Cash Flow, 3-Year TCO, ROI %, and NPV."""
    if not (0.0 < sam_share <= 1.0):
        raise ValueError("sam_share must be in (0, 1]")
    if not (0.0 < adoption_rate <= 1.0):
        raise ValueError("adoption_rate must be in (0, 1]")
    if not (0.0 < tech_compat <= 1.0):
        raise ValueError("tech_compat must be in (0, 1]")
    if not (0.0 < year1_ramp <= 1.0):
        raise ValueError("year1_ramp must be in (0, 1]")
    if tam_units <= 0:
        raise ValueError("tam_units must be > 0")
    if hours_saved_per_unit < 0 or hourly_rate_usd < 0 or annual_non_labor_benefit_usd < 0:
        raise ValueError("hours_saved_per_unit, hourly_rate_usd, and annual_non_labor_benefit_usd must be >= 0")
    if (hours_saved_per_unit * hourly_rate_usd) <= 0 and annual_non_labor_benefit_usd <= 0:
        raise ValueError("Either labor savings (hours_saved * hourly_rate) or annual_non_labor_benefit_usd must be > 0")
    if capex_usd < 0 or annual_opex_usd < 0:
        raise ValueError("capex_usd and annual_opex_usd must be >= 0")

    sam_units = tam_units * sam_share
    som_units = sam_units * adoption_rate * tech_compat
    gross_labor_value = som_units * hours_saved_per_unit * hourly_rate_usd
    gross_annual_value = gross_labor_value + annual_non_labor_benefit_usd
    total_3yr_tco = capex_usd + (3.0 * annual_opex_usd)
    if total_3yr_tco <= 0:
        raise ValueError("Total 3-year TCO must be > 0")

    year_multipliers = (year1_ramp, 1.0, 1.0)

    def scenario_metrics(scen_vcr: float, scen_scdf: float) -> dict[str, float]:
        # Steady-state risk-adjusted annual benefit (post capture & delivery-readiness haircuts, pre-OpEx)
        net_annual = gross_annual_value * scen_vcr * scen_scdf
        net_3yr_value = sum(net_annual * m for m in year_multipliers)
        annual_net_cashflow = net_annual - annual_opex_usd
        net_3yr_after_tco = net_3yr_value - total_3yr_tco
        roi_pct = (net_3yr_after_tco / total_3yr_tco) * 100.0
        npv = -capex_usd + sum(
            ((net_annual * m) - annual_opex_usd) / ((1.0 + wacc) ** yr)
            for yr, m in zip((1, 2, 3), year_multipliers)
        )
        yr1_net = (net_annual * year1_ramp) - annual_opex_usd
        steady_monthly_net = annual_net_cashflow / 12.0
        if capex_usd == 0:
            payback_months = 0.0
        elif yr1_net >= capex_usd and yr1_net > 0:
            payback_months = capex_usd / (yr1_net / 12.0)
        elif steady_monthly_net > 0:
            remaining_after_yr1 = capex_usd - yr1_net
            payback_months = 12.0 + (remaining_after_yr1 / steady_monthly_net)
        else:
            payback_months = float("inf")
        return {
            "vcr": round(scen_vcr, 4),
            "scdf": round(scen_scdf, 4),
            "capture_rate": round(scen_vcr, 4),
            "delivery_factor": round(scen_scdf, 4),
            "net_annual_value_usd": round(net_annual, 2),
            "annual_net_cashflow_usd": round(annual_net_cashflow, 2),
            "net_3yr_value_usd": round(net_3yr_value, 2),
            "net_3yr_benefit_after_tco_usd": round(net_3yr_after_tco, 2),
            "roi_3yr_percent": round(roi_pct, 2),
            "npv_3yr_usd": round(npv, 2),
            "payback_months": round(payback_months, 1) if payback_months != float("inf") else -1.0,
        }

    bear_scdf = min(scdf, 0.40)
    return {
        "funnel": {
            "tam_units": round(tam_units, 2),
            "sam_units": round(sam_units, 2),
            "som_units": round(som_units, 2),
            "sam_share": sam_share,
            "adoption_rate": adoption_rate,
            "tech_compat": tech_compat,
            "year1_ramp": year1_ramp,
        },
        "tco": {
            "year0_capex_usd": round(capex_usd, 2),
            "annual_opex_usd": round(annual_opex_usd, 2),
            "total_3yr_tco_usd": round(total_3yr_tco, 2),
        },
        "gross_labor_value_usd": round(gross_labor_value, 2),
        "annual_non_labor_benefit_usd": round(annual_non_labor_benefit_usd, 2),
        "gross_annual_value_usd": round(gross_annual_value, 2),
        "wacc": wacc,
        "scenarios": {
            "base": scenario_metrics(vcr, scdf),
            "bull": scenario_metrics(min(1.0, vcr * 1.5), min(1.2, scdf * 1.2)),
            "bear": scenario_metrics(vcr, bear_scdf),
        },
    }


def format_markdown_table(result: dict[str, object]) -> str:
    """Format the 3-scenario ROI/NPV output as a ready-to-paste Markdown table."""
    scenarios = result["scenarios"]  # type: ignore[index]
    lines = [
        "| Scenario | Capture Rate | Delivery Factor | Risk-Adj Annual Benefit (Pre-OpEx) | Annual Net Cash Flow (Post-OpEx) | 3-Year Risk-Adj Benefit | 3-Year ROI % | 3-Year NPV | Payback |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for key, label in (("base", "**Base**"), ("bull", "**Bull**"), ("bear", "**Bear**")):
        sc = scenarios[key]  # type: ignore[index]
        payback = f"{sc['payback_months']:.1f} mos" if sc["payback_months"] > 0 else "Never"
        lines.append(
            f"| {label} | `{sc['vcr']:.2f}` | `{sc['scdf']:.2f}` | "
            f"`${round(sc['net_annual_value_usd']):,}` | `${round(sc['annual_net_cashflow_usd']):,}` | "
            f"`${round(sc['net_3yr_value_usd']):,}` | "
            f"`{sc['roi_3yr_percent']:.1f}%` | `${round(sc['npv_3yr_usd']):,}` | `{payback}` |"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="Run worked example defaults (Commercial Auto Claims FNOL)")
    parser.add_argument("--markdown", action="store_true", help="Emit a ready-to-paste Markdown scenario table")
    parser.add_argument("--tam-units", type=float, default=None, help="Total annual universe (units/transactions)")
    parser.add_argument("--sam-share", type=float, default=None, help="Serviceable share of TAM (0..1)")
    parser.add_argument("--adoption-rate", type=float, default=None, help="Year-1 adoption rate (0..1, typically <=0.30)")
    parser.add_argument("--tech-compat", type=float, default=None, help="Technical compatibility factor (0..1)")
    parser.add_argument("--hours-saved", type=float, default=None, help="Hours saved per unit/transaction")
    parser.add_argument("--hourly-rate", type=float, default=None, help="Fully loaded hourly labor rate (USD)")
    parser.add_argument(
        "--annual-non-labor-benefit",
        type=float,
        default=0.0,
        help="Additional annual gross benefit from rework/error reduction or revenue lift (USD, default 0)",
    )
    parser.add_argument(
        "--year1-ramp",
        type=float,
        default=1.0,
        help="Year-1 realization factor in (0..1] for rollout ramp (default 1.0)",
    )
    parser.add_argument("--capex", type=float, default=None, help="Year 0 build CapEx (USD)")
    parser.add_argument("--annual-opex", type=float, default=None, help="Ongoing annual run OpEx (USD)")
    parser.add_argument(
        "--capture-rate",
        "--vcr",
        dest="vcr",
        type=float,
        default=None,
        help="Productivity capture rate (0.25 task, 0.50-0.60 overflow/revenue, 1.00 hard cost elimination)",
    )
    parser.add_argument(
        "--delivery-factor",
        "--scdf",
        dest="scdf",
        type=float,
        default=None,
        help="Delivery readiness factor (0.40 low maturity, 0.85 standard enterprise, 1.20 high maturity)",
    )
    parser.add_argument("--wacc", type=float, default=None, help="Discount rate / WACC (default 0.10)")
    args = parser.parse_args(argv)

    base_required = [
        ("tam_units", "--tam-units"),
        ("sam_share", "--sam-share"),
        ("adoption_rate", "--adoption-rate"),
        ("capex", "--capex"),
        ("annual_opex", "--annual-opex"),
    ]
    if not (args.annual_non_labor_benefit and args.annual_non_labor_benefit > 0):
        base_required.extend([("hours_saved", "--hours-saved"), ("hourly_rate", "--hourly-rate")])
    if not args.demo:
        missing = [flag for attr, flag in base_required if getattr(args, attr) is None]
        if missing:
            parser.error(f"the following arguments are required (or pass --demo): {', '.join(missing)}")

    def resolve(attr: str, fallback: float) -> float:
        val = getattr(args, attr)
        if val is not None:
            return float(val)
        if args.demo and attr in DEMO_DEFAULTS:
            return DEMO_DEFAULTS[attr]
        return fallback

    try:
        result = compute_sizing_and_roi(
            tam_units=resolve("tam_units", DEMO_DEFAULTS["tam_units"]),
            sam_share=resolve("sam_share", DEMO_DEFAULTS["sam_share"]),
            adoption_rate=resolve("adoption_rate", DEMO_DEFAULTS["adoption_rate"]),
            tech_compat=resolve("tech_compat", 1.0),
            hours_saved_per_unit=resolve("hours_saved", 0.0),
            hourly_rate_usd=resolve("hourly_rate", 0.0),
            capex_usd=resolve("capex", DEMO_DEFAULTS["capex"]),
            annual_opex_usd=resolve("annual_opex", DEMO_DEFAULTS["annual_opex"]),
            vcr=resolve("vcr", 0.25),
            scdf=resolve("scdf", 0.85),
            wacc=resolve("wacc", 0.10),
            annual_non_labor_benefit_usd=float(args.annual_non_labor_benefit or 0.0),
            year1_ramp=float(args.year1_ramp if args.year1_ramp is not None else 1.0),
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.markdown:
        print(format_markdown_table(result))
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
