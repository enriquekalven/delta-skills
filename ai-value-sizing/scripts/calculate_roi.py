#!/usr/bin/env python3
"""Deterministic TAM/SAM/SOM and 3-Year ROI/NPV calculator for ai-value-sizing."""

from __future__ import annotations

import argparse
import json
import sys


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
) -> dict[str, object]:
    """Calculate SOM (Q), Gross/Net Annual Value, 3-Year TCO, 3-Year ROI %, and 3-Year NPV."""
    if not (0.0 < sam_share <= 1.0):
        raise ValueError("sam_share must be in (0, 1]")
    if not (0.0 < adoption_rate <= 1.0):
        raise ValueError("adoption_rate must be in (0, 1]")
    if not (0.0 < tech_compat <= 1.0):
        raise ValueError("tech_compat must be in (0, 1]")
    if tam_units <= 0 or hours_saved_per_unit <= 0 or hourly_rate_usd <= 0:
        raise ValueError("tam_units, hours_saved_per_unit, and hourly_rate_usd must be > 0")
    if capex_usd < 0 or annual_opex_usd < 0:
        raise ValueError("capex_usd and annual_opex_usd must be >= 0")

    sam_units = tam_units * sam_share
    som_units = sam_units * adoption_rate * tech_compat
    gross_annual_value = som_units * hours_saved_per_unit * hourly_rate_usd
    total_3yr_tco = capex_usd + (3.0 * annual_opex_usd)
    if total_3yr_tco <= 0:
        raise ValueError("Total 3-year TCO must be > 0")

    def scenario_metrics(scen_vcr: float, scen_scdf: float) -> dict[str, float]:
        net_annual = gross_annual_value * scen_vcr * scen_scdf
        net_3yr_value = 3.0 * net_annual
        roi_pct = ((net_3yr_value - total_3yr_tco) / total_3yr_tco) * 100.0
        npv = -capex_usd + sum(
            (net_annual - annual_opex_usd) / ((1.0 + wacc) ** yr) for yr in (1, 2, 3)
        )
        monthly_net = (net_annual - annual_opex_usd) / 12.0
        payback_months = (capex_usd / monthly_net) if monthly_net > 0 else float("inf")
        return {
            "vcr": round(scen_vcr, 4),
            "scdf": round(scen_scdf, 4),
            "net_annual_value_usd": round(net_annual, 2),
            "net_3yr_value_usd": round(net_3yr_value, 2),
            "roi_3yr_percent": round(roi_pct, 2),
            "npv_3yr_usd": round(npv, 2),
            "payback_months": round(payback_months, 1) if payback_months != float("inf") else -1.0,
        }

    return {
        "funnel": {
            "tam_units": round(tam_units, 2),
            "sam_units": round(sam_units, 2),
            "som_units": round(som_units, 2),
            "sam_share": sam_share,
            "adoption_rate": adoption_rate,
            "tech_compat": tech_compat,
        },
        "tco": {
            "year0_capex_usd": round(capex_usd, 2),
            "annual_opex_usd": round(annual_opex_usd, 2),
            "total_3yr_tco_usd": round(total_3yr_tco, 2),
        },
        "gross_annual_value_usd": round(gross_annual_value, 2),
        "wacc": wacc,
        "scenarios": {
            "base": scenario_metrics(vcr, scdf),
            "bull": scenario_metrics(min(1.0, vcr * 1.5), min(1.2, scdf * 1.2)),
            "bear": scenario_metrics(vcr, 0.40),
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tam-units", type=float, required=True, help="Total annual universe (units/transactions)")
    parser.add_argument("--sam-share", type=float, required=True, help="Serviceable share of TAM (0..1)")
    parser.add_argument("--adoption-rate", type=float, required=True, help="Year-1 adoption rate (0..1, typically <=0.30)")
    parser.add_argument("--tech-compat", type=float, default=1.0, help="Technical compatibility factor (0..1)")
    parser.add_argument("--hours-saved", type=float, required=True, help="Hours saved per unit/transaction")
    parser.add_argument("--hourly-rate", type=float, required=True, help="Fully loaded hourly labor rate (USD)")
    parser.add_argument("--capex", type=float, required=True, help="Year 0 build CapEx (USD)")
    parser.add_argument("--annual-opex", type=float, required=True, help="Ongoing annual run OpEx (USD)")
    parser.add_argument("--vcr", type=float, default=0.25, help="Value Capture Rate (0.25 task, 0.50 rev, 1.00 hard)")
    parser.add_argument("--scdf", type=float, default=0.85, help="Systemic Capability Discount Factor (0.40, 0.85, 1.20)")
    parser.add_argument("--wacc", type=float, default=0.10, help="Discount rate / WACC (default 0.10)")
    args = parser.parse_args(argv)

    try:
        result = compute_sizing_and_roi(
            tam_units=args.tam_units,
            sam_share=args.sam_share,
            adoption_rate=args.adoption_rate,
            tech_compat=args.tech_compat,
            hours_saved_per_unit=args.hours_saved,
            hourly_rate_usd=args.hourly_rate,
            capex_usd=args.capex,
            annual_opex_usd=args.annual_opex,
            vcr=args.vcr,
            scdf=args.scdf,
            wacc=args.wacc,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
