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
    "vcr": 0.5912,
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
    llm_calls_per_unit: float = 0.0,
    tokens_per_call: float = 0.0,
    cost_per_1m_tokens_usd: float = 1.25,
    cache_hit_ratio: float = 0.60,
) -> dict[str, object]:
    """Calculate SOM (Q), Gross/Net Annual Value, 3-Year TCO, 3-Year ROI %, 3-Year NPV, and Project Worth Verdict."""
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

    # Optional dynamic LLM token inference cost modeling (with context caching)
    effective_token_mult = max(0.0, 1.0 - (cache_hit_ratio * 0.75))
    annual_tokens = som_units * llm_calls_per_unit * tokens_per_call
    annual_token_opex_usd = (annual_tokens / 1_000_000.0) * cost_per_1m_tokens_usd * effective_token_mult
    effective_annual_opex = annual_opex_usd + annual_token_opex_usd

    total_3yr_tco = capex_usd + (3.0 * effective_annual_opex)
    if total_3yr_tco <= 0:
        raise ValueError("Total 3-year TCO must be > 0")

    def scenario_metrics(scen_vcr: float, scen_scdf: float, custom_capex: float | None = None, custom_opex: float | None = None) -> dict[str, float]:
        c_capex = capex_usd if custom_capex is None else custom_capex
        c_opex = effective_annual_opex if custom_opex is None else custom_opex
        c_tco = c_capex + (3.0 * c_opex)
        net_annual = gross_annual_value * scen_vcr * scen_scdf
        net_3yr_value = 3.0 * net_annual
        roi_pct = ((net_3yr_value - c_tco) / c_tco) * 100.0 if c_tco > 0 else 0.0
        npv = -c_capex + sum(
            (net_annual - c_opex) / ((1.0 + wacc) ** yr) for yr in (1, 2, 3)
        )
        monthly_net = (net_annual - c_opex) / 12.0
        payback_months = (c_capex / monthly_net) if monthly_net > 0 else float("inf")
        return {
            "vcr": round(scen_vcr, 4),
            "scdf": round(scen_scdf, 4),
            "net_annual_value_usd": round(net_annual, 2),
            "net_3yr_value_usd": round(net_3yr_value, 2),
            "roi_3yr_percent": round(roi_pct, 2),
            "npv_3yr_usd": round(npv, 2),
            "payback_months": round(payback_months, 1) if payback_months != float("inf") else -1.0,
        }

    base_sc = scenario_metrics(vcr, scdf)
    bull_sc = scenario_metrics(min(1.0, vcr * 1.5), min(1.2, scdf * 1.2))
    bear_sc = scenario_metrics(vcr, 0.40)

    # Evaluate Fast-Track 5-Skill Lite Mode (15% CapEx, 15% OpEx matching 18.5h Tier-1/2 lean sprint vs 12-week squad)
    lite_base_sc = scenario_metrics(vcr, scdf, custom_capex=capex_usd * 0.15, custom_opex=effective_annual_opex * 0.15)
    lite_bear_sc = scenario_metrics(vcr, 0.40, custom_capex=capex_usd * 0.15, custom_opex=effective_annual_opex * 0.15)

    if base_sc["npv_3yr_usd"] > 0 and bear_sc["npv_3yr_usd"] > 0 and base_sc["payback_months"] <= 18.0:
        verdict = "WORTH_IT_FULL_13_SKILL"
        recommended_mode = "Full 13-Skill 12-Week Delta Mode (73.5h skill-guided effort)"
    elif lite_base_sc["npv_3yr_usd"] > 0 and lite_bear_sc["npv_3yr_usd"] > 0:
        verdict = "WORTH_IT_FAST_TRACK_5_SKILL"
        recommended_mode = "Fast-Track 5-Skill Lite Mode (18.5h effort; 2-week Tier 1/2 lean build to protect Bear NPV)"
    else:
        verdict = "KILL_OR_RE_SCOPE_AT_GATE_0"
        recommended_mode = "STOP at Prelude Gate 0: Re-scope volume/CapEx or fix Data Readiness (SCDF) before coding"

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
            "annual_opex_usd": round(effective_annual_opex, 2),
            "annual_token_opex_usd": round(annual_token_opex_usd, 2),
            "total_3yr_tco_usd": round(total_3yr_tco, 2),
        },
        "gross_annual_value_usd": round(gross_annual_value, 2),
        "wacc": wacc,
        "scenarios": {
            "base": base_sc,
            "bull": bull_sc,
            "bear": bear_sc,
        },
        "project_worth_verdict": {
            "verdict": verdict,
            "recommended_mode": recommended_mode,
            "base_npv_lite_mode_usd": lite_base_sc["npv_3yr_usd"],
            "bear_npv_full_mode_usd": bear_sc["npv_3yr_usd"],
            "bear_npv_lite_mode_usd": lite_bear_sc["npv_3yr_usd"],
        },
    }


def format_markdown_table(result: dict[str, object]) -> str:
    """Format the 3-scenario ROI/NPV output as a ready-to-paste Markdown table."""
    scenarios = result["scenarios"]  # type: ignore[index]
    lines = [
        "| Scenario | VCR | SCDF | Net Annual Value | 3-Year Net Value | 3-Year ROI % | 3-Year NPV | Payback |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for key, label in (("base", "**Base**"), ("bull", "**Bull**"), ("bear", "**Bear**")):
        sc = scenarios[key]  # type: ignore[index]
        payback = f"{sc['payback_months']:.1f} mos" if sc["payback_months"] > 0 else "Never"
        lines.append(
            f"| {label} | `{sc['vcr']:.4f}` | `{sc['scdf']:.2f}` | "
            f"`${round(sc['net_annual_value_usd']):,}` | `${round(sc['net_3yr_value_usd']):,}` | "
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
    parser.add_argument("--capex", type=float, default=None, help="Year 0 build CapEx (USD)")
    parser.add_argument("--annual-opex", type=float, default=None, help="Ongoing annual run OpEx (USD)")
    parser.add_argument("--vcr", type=float, default=None, help="Value Capture Rate (0.25 task, 0.50 rev, 1.00 hard)")
    parser.add_argument("--scdf", type=float, default=None, help="Systemic Capability Discount Factor (0.40, 0.85, 1.20)")
    parser.add_argument("--wacc", type=float, default=None, help="Discount rate / WACC (default 0.10)")
    args = parser.parse_args(argv)

    required_flags = (
        ("tam_units", "--tam-units"),
        ("sam_share", "--sam-share"),
        ("adoption_rate", "--adoption-rate"),
        ("hours_saved", "--hours-saved"),
        ("hourly_rate", "--hourly-rate"),
        ("capex", "--capex"),
        ("annual_opex", "--annual-opex"),
    )
    if not args.demo:
        missing = [flag for attr, flag in required_flags if getattr(args, attr) is None]
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
            hours_saved_per_unit=resolve("hours_saved", DEMO_DEFAULTS["hours_saved"]),
            hourly_rate_usd=resolve("hourly_rate", DEMO_DEFAULTS["hourly_rate"]),
            capex_usd=resolve("capex", DEMO_DEFAULTS["capex"]),
            annual_opex_usd=resolve("annual_opex", DEMO_DEFAULTS["annual_opex"]),
            vcr=resolve("vcr", 0.25),
            scdf=resolve("scdf", 0.85),
            wacc=resolve("wacc", 0.10),
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
