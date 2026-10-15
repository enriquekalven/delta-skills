#!/usr/bin/env python3
"""Statistical auditor for LLM-as-a-Judge (Assessment Use Argument report).

Implements the three auditing pipelines from the TDL Toolbox deck
"Statistical Auditing for LLM-as-a-Judge" (H. Gonzalez):

  Pipeline 1  Development calibration, human vs. LLM judge:
              PRMSE, disattenuated correlation d.R, Pearson r, exact / adjacent
              agreement, quadratic weighted kappa (QWK), Wilcoxon signed-rank W,
              scale compression (SD ratio).
  Pipeline 2  Live production option A, intra-rater (one judge, K passes at T>0):
              Cronbach's alpha, SEM, 95% CI (= +/- 2 SEM, as in the deck).
  Pipeline 3  Live production option B, inter-model double marking (two judges,
              T=0): ICC(3,k), Pearson r, Spearman rho, exact / adjacent agreement,
              QWK, Wilcoxon W, per-item confidence score for HITL routing.

Deployment gates (from the deck): d.R >= 0.80, QWK >= 0.60, SD ratio >= 0.80,
Cronbach's alpha >= 0.80, per-criterion d.rho >= 0.70 and QWK >= 0.60.
Repo conventions (not in the deck, stated as such): PRMSE > 0, Wilcoxon p > 0.05
as the "no systematic bias" test, ICC(3,k) >= 0.80 as the Pipeline 3 gate,
confidence C = 1 - |a - b| / (scale range) for HITL routing.

Stdlib only. No hidden constants: LLM-judge reliability for d.R defaults to 1.0
(conservative) and can be supplied from Pipeline 2 via --llm-reliability.

Input JSON (holistic block, each array length N):
  {"scale_min": 1, "scale_max": 5,
   "human_r1": [...], "human_r2": [...], "llm_scores": [...],
   "judge_b": [...],                      # optional -> Pipeline 3
   "passes": [[p1..pK], ...],             # optional -> Pipeline 2 (N x K)
   "criteria": {"Vocabulary": {same keys}, ...}}   # optional per-criterion blocks
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

FIXTURES_DIR = Path(__file__).resolve().parent.parent / "examples" / "fixtures"


# ----------------------------------------------------------------------------
# basic statistics
# ----------------------------------------------------------------------------
def _mean(xs: Sequence[float]) -> float:
    return sum(xs) / len(xs)


def _variance(xs: Sequence[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    m = _mean(xs)
    return sum((x - m) ** 2 for x in xs) / (n - 1)


def _std(xs: Sequence[float]) -> float:
    return math.sqrt(_variance(xs))


def round_half_up(x: float) -> int:
    """Deterministic rounding for consensus scores (avoids banker's rounding)."""
    return int(math.floor(x + 0.5))


def pearson_r(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y must have equal length >= 2")
    mx, my = _mean(x), _mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    if dx == 0.0 or dy == 0.0:
        return 0.0
    return max(-1.0, min(1.0, num / (dx * dy)))


def _ranks(xs: Sequence[float]) -> List[float]:
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j + 2) / 2.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman_rho(x: Sequence[float], y: Sequence[float]) -> float:
    return pearson_r(_ranks(x), _ranks(y))


def quadratic_weighted_kappa(a: Sequence[int], b: Sequence[int], lo: int, hi: int) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("ratings must be non-empty and equal length")
    k = hi - lo + 1
    n = float(len(a))
    ha, hb = [0.0] * k, [0.0] * k
    obs = [[0.0] * k for _ in range(k)]
    for ra, rb in zip(a, b):
        ia = min(k - 1, max(0, int(ra) - lo))
        ib = min(k - 1, max(0, int(rb) - lo))
        ha[ia] += 1
        hb[ib] += 1
        obs[ia][ib] += 1
    denom = float((k - 1) ** 2) or 1.0
    num_o = num_e = 0.0
    for i in range(k):
        for j in range(k):
            w = ((i - j) ** 2) / denom
            num_o += w * obs[i][j] / n
            num_e += w * (ha[i] * hb[j]) / (n * n)
    if num_e == 0.0:
        return 1.0 if num_o == 0.0 else 0.0
    return 1.0 - num_o / num_e


def wilcoxon_signed_rank(x: Sequence[float], y: Sequence[float]) -> Tuple[float, float, float]:
    """Return (W = min(W+, W-), z, two-tailed p) with the normal approximation.

    Zero differences are dropped (Wilcoxon's original treatment). For n < ~10 the
    normal approximation is rough; the deck's reports use N = 30.
    """
    d = [b - a for a, b in zip(x, y) if abs(b - a) > 1e-12]
    n = len(d)
    if n == 0:
        return 0.0, 0.0, 1.0
    r = _ranks([abs(v) for v in d])
    w_pos = sum(rk for v, rk in zip(d, r) if v > 0)
    w_neg = sum(rk for v, rk in zip(d, r) if v < 0)
    w = min(w_pos, w_neg)
    mu = n * (n + 1) / 4.0
    sigma = math.sqrt(n * (n + 1) * (2 * n + 1) / 24.0)
    z = (w - mu) / sigma if sigma else 0.0
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return round(w, 3), round(z, 3), round(p, 4)


def disattenuated_correlation(r_xy: float, r_xx: float, r_yy: float) -> Optional[float]:
    """Spearman's correction: r_xy / sqrt(r_xx * r_yy). None if undefined."""
    if r_xx <= 0.0 or r_yy <= 0.0:
        return None
    return max(-1.0, min(1.0, r_xy / math.sqrt(r_xx * r_yy)))


def prmse(human_r1: Sequence[float], human_r2: Sequence[float], machine: Sequence[float]) -> Optional[float]:
    """Proportional reduction in mean squared error (Haberman, 2008) with 2 human raters.

    PRMSE = 1 - MSE_true(machine) / Var_true(human), where the human error variance
    estimated from the two raters is removed from both the MSE and the variance of
    the averaged human score. None if the true-score variance is not positive.
    """
    n = len(machine)
    if len(human_r1) != n or len(human_r2) != n or n < 2:
        raise ValueError("human_r1, human_r2 and machine must have equal length >= 2")
    h_avg = [(a + b) / 2.0 for a, b in zip(human_r1, human_r2)]
    err_var = sum(((a - b) ** 2) / 2.0 for a, b in zip(human_r1, human_r2)) / n  # single-rater error variance
    var_true = _variance(h_avg) - err_var / 2.0
    if var_true <= 0.0:
        return None
    mse = sum((m - h) ** 2 for m, h in zip(machine, h_avg)) / n
    mse_true = max(0.0, mse - err_var / 2.0)
    return round(1.0 - mse_true / var_true, 4)


def cronbach_alpha(matrix: Sequence[Sequence[float]]) -> float:
    """Cronbach's alpha over an N x K matrix (N items rated, K passes)."""
    n, k = len(matrix), len(matrix[0])
    if n < 2 or k < 2:
        raise ValueError("need >= 2 items and >= 2 passes")
    cols = [[matrix[i][j] for i in range(n)] for j in range(k)]
    totals = [sum(row) for row in matrix]
    vt = _variance(totals)
    if vt == 0.0:
        return 0.0
    return (k / (k - 1.0)) * (1.0 - sum(_variance(c) for c in cols) / vt)


def icc_3k(matrix: Sequence[Sequence[float]]) -> float:
    """Two-way mixed, consistency, average-measures ICC(3,k) (Shrout & Fleiss)."""
    n, k = len(matrix), len(matrix[0])
    grand = sum(sum(r) for r in matrix) / (n * k)
    row_means = [_mean(r) for r in matrix]
    col_means = [_mean([matrix[i][j] for i in range(n)]) for j in range(k)]
    ss_total = sum((matrix[i][j] - grand) ** 2 for i in range(n) for j in range(k))
    ss_rows = k * sum((m - grand) ** 2 for m in row_means)
    ss_cols = n * sum((m - grand) ** 2 for m in col_means)
    ss_err = max(0.0, ss_total - ss_rows - ss_cols)
    ms_rows = ss_rows / (n - 1)
    ms_err = ss_err / ((n - 1) * (k - 1))
    return 0.0 if ms_rows == 0.0 else (ms_rows - ms_err) / ms_rows


# ----------------------------------------------------------------------------
# pipelines
# ----------------------------------------------------------------------------
def pipeline_1_calibration(
    human_r1: Sequence[int],
    human_r2: Sequence[int],
    llm: Sequence[int],
    lo: int = 1,
    hi: int = 5,
    llm_reliability: float = 1.0,
) -> Dict[str, Any]:
    n = len(llm)
    h_mean = [(a + b) / 2.0 for a, b in zip(human_r1, human_r2)]
    h_int = [round_half_up(v) for v in h_mean]

    exact = sum(1 for h, l in zip(h_int, llm) if h == l) / n
    adjacent = sum(1 for h, l in zip(h_int, llm) if abs(h - l) <= 1) / n
    r = pearson_r(h_mean, llm)
    r_hh = pearson_r(human_r1, human_r2)  # human inter-rater reliability
    d_r = disattenuated_correlation(r, r_hh, llm_reliability)
    qwk = quadratic_weighted_kappa(h_int, llm, lo, hi)
    pr = prmse(human_r1, human_r2, llm)
    w, z, p = wilcoxon_signed_rank(h_mean, llm)
    sd_h, sd_l = _std(h_mean), _std(llm)
    sd_ratio = (sd_l / sd_h) if sd_h > 0 else None

    gates = {
        "d_r_ge_0.80": d_r is not None and d_r >= 0.80 and r >= 0.50 and r_hh >= 0.50,
        "qwk_ge_0.60": qwk >= 0.60,
        "sd_ratio_ge_0.80": sd_ratio is not None and sd_ratio >= 0.80,
        "prmse_gt_0 (repo convention)": pr is not None and pr > 0.0,
        "wilcoxon_p_gt_0.05 (repo convention)": p > 0.05,
    }
    return {
        "n_items": n,
        "exact_agreement_pct": round(exact * 100, 1),
        "adjacent_agreement_pct": round(adjacent * 100, 1),
        "pearson_r": round(r, 4),
        "human_inter_rater_r": round(r_hh, 4),
        "llm_reliability_assumed": llm_reliability,
        "disattenuated_d_r": None if d_r is None else round(d_r, 4),
        "qwk": round(qwk, 4),
        "prmse": pr,
        "wilcoxon_w": w,
        "wilcoxon_z": z,
        "wilcoxon_p": p,
        "sd_human": round(sd_h, 4),
        "sd_llm": round(sd_l, 4),
        "sd_ratio": None if sd_ratio is None else round(sd_ratio, 4),
        "gates": gates,
        "passed": all(gates.values()),
    }


def pipeline_2_intra_rater(passes: Sequence[Sequence[float]]) -> Dict[str, Any]:
    alpha = cronbach_alpha(passes)
    item_means = [_mean(row) for row in passes]
    sd = _std(item_means)
    sem = sd * math.sqrt(max(0.0, 1.0 - alpha))
    per_item_sd = [round(_std(row), 3) for row in passes]
    return {
        "n_items": len(passes),
        "k_passes": len(passes[0]),
        "cronbach_alpha": round(alpha, 4),
        "sd_observed": round(sd, 4),
        "sem": round(sem, 4),
        "ci95_half_width_2sem": round(2.0 * sem, 4),
        "per_item_sd": per_item_sd,
        "gates": {"alpha_ge_0.80": alpha >= 0.80},
        "passed": alpha >= 0.80,
    }


def pipeline_3_double_marking(a: Sequence[int], b: Sequence[int], lo: int = 1, hi: int = 5) -> Dict[str, Any]:
    n = len(a)
    matrix = [[float(x), float(y)] for x, y in zip(a, b)]
    icc = icc_3k(matrix)
    r = pearson_r(a, b)
    rho = spearman_rho(a, b)
    qwk = quadratic_weighted_kappa(a, b, lo, hi)
    exact = sum(1 for x, y in zip(a, b) if x == y) / n
    adjacent = sum(1 for x, y in zip(a, b) if abs(x - y) <= 1) / n
    w, z, p = wilcoxon_signed_rank(a, b)
    span = float(hi - lo) or 1.0
    confidence = [round(1.0 - abs(x - y) / span, 3) for x, y in zip(a, b)]
    return {
        "n_items": n,
        "icc_3k": round(icc, 4),
        "pearson_r": round(r, 4),
        "spearman_rho": round(rho, 4),
        "qwk": round(qwk, 4),
        "exact_agreement_pct": round(exact * 100, 1),
        "adjacent_agreement_pct": round(adjacent * 100, 1),
        "wilcoxon_w": w,
        "wilcoxon_z": z,
        "wilcoxon_p": p,
        "final_scores": [round((x + y) / 2.0, 2) for x, y in zip(a, b)],
        "confidence": confidence,
        "confidence_definition": "C = 1 - |score_a - score_b| / (scale_max - scale_min); repo convention",
        "gates": {
            "icc_3k_ge_0.80 (repo convention)": icc >= 0.80,
            "wilcoxon_p_gt_0.05 (repo convention)": p > 0.05,
        },
        "passed": icc >= 0.80 and p > 0.05,
    }


def criterion_flags(block: Dict[str, Any]) -> Dict[str, Any]:
    """Per-criterion diagnostic flag using the deck's glossary: d.rho >= 0.70 and QWK >= 0.60."""
    p1 = block.get("pipeline_1")
    p3 = block.get("pipeline_3")
    if p1:
        d = p1["disattenuated_d_r"]
        qwk = p1["qwk"]
    elif p3:
        d = p3["spearman_rho"]
        qwk = p3["qwk"]
    else:
        return {"flag": "n/a"}
    ok_d = d is not None and d >= 0.70
    ok_k = qwk >= 0.60
    return {"d_rho_or_rho": d, "qwk": qwk, "flag": "PASS" if (ok_d and ok_k) else ("MIXED" if (ok_d or ok_k) else "FAIL")}


# ----------------------------------------------------------------------------
# driver
# ----------------------------------------------------------------------------
def audit(data: Dict[str, Any], llm_reliability: Optional[float] = None) -> Dict[str, Any]:
    lo = int(data.get("scale_min", 1))
    hi = int(data.get("scale_max", 5))
    out: Dict[str, Any] = {"scale": [lo, hi]}

    def run_block(block: Dict[str, Any]) -> Dict[str, Any]:
        res: Dict[str, Any] = {}
        rel = llm_reliability
        if "passes" in block:
            res["pipeline_2"] = pipeline_2_intra_rater(block["passes"])
            if rel is None:
                rel = res["pipeline_2"]["cronbach_alpha"]  # use measured judge reliability when available
        if all(k in block for k in ("human_r1", "human_r2", "llm_scores")):
            res["pipeline_1"] = pipeline_1_calibration(
                block["human_r1"], block["human_r2"], block["llm_scores"], lo, hi, rel if rel is not None else 1.0
            )
        if "judge_b" in block and "llm_scores" in block:
            res["pipeline_3"] = pipeline_3_double_marking(block["llm_scores"], block["judge_b"], lo, hi)
        return res

    out["holistic"] = run_block(data)
    if "criteria" in data:
        out["criteria"] = {}
        for name, block in data["criteria"].items():
            res = run_block(block)
            res["diagnostic"] = criterion_flags(res)
            out["criteria"][name] = res
    return out


def _fmt(v: Any) -> str:
    return "n/a" if v is None else (f"{v:.4f}" if isinstance(v, float) else str(v))


def _fmt_p(p: float) -> str:
    return "<0.0001" if p < 0.0001 else f"{p:.4f}"


def format_report(res: Dict[str, Any], title: str) -> str:
    h = res["holistic"]
    L = [f"=== Assessment Use Argument (AUA) Report: {title} ===", f"Scale: {res['scale'][0]}-{res['scale'][1]}"]
    if "pipeline_1" in h:
        p = h["pipeline_1"]
        L += [
            "",
            f"[Pipeline 1] Development calibration, human vs. LLM judge (N={p['n_items']})",
            f"  Exact / adjacent agreement : {p['exact_agreement_pct']}% / {p['adjacent_agreement_pct']}%",
            f"  Pearson r                  : {_fmt(p['pearson_r'])}   (human inter-rater r {_fmt(p['human_inter_rater_r'])}, LLM reliability {p['llm_reliability_assumed']})",
            f"  Disattenuated d.R          : {_fmt(p['disattenuated_d_r'])}   gate >= 0.80",
            f"  QWK                        : {_fmt(p['qwk'])}   gate >= 0.60",
            f"  PRMSE                      : {_fmt(p['prmse'])}   gate > 0 (repo convention)",
            f"  Wilcoxon W / p             : {p['wilcoxon_w']} / {_fmt_p(p['wilcoxon_p'])}   bias flag if p <= 0.05",
            f"  Scale compression SD ratio : {_fmt(p['sd_ratio'])}   gate >= 0.80  (SD LLM {p['sd_llm']} / SD human {p['sd_human']})",
            f"  Verdict                    : {'PASS' if p['passed'] else 'FAIL -> recalibrate rubric / few-shot anchors'}",
        ]
    if "pipeline_2" in h:
        p = h["pipeline_2"]
        L += [
            "",
            f"[Pipeline 2] Intra-rater stability, {p['k_passes']} passes (N={p['n_items']})",
            f"  Cronbach's alpha           : {_fmt(p['cronbach_alpha'])}   gate >= 0.80",
            f"  SEM                        : {_fmt(p['sem'])}   95% CI = observed +/- {p['ci95_half_width_2sem']} (2 SEM)",
            f"  Verdict                    : {'PASS' if p['passed'] else 'FAIL'}",
        ]
    if "pipeline_3" in h:
        p = h["pipeline_3"]
        low = sum(1 for c in p["confidence"] if c < 0.75)
        L += [
            "",
            f"[Pipeline 3] Inter-model double marking (N={p['n_items']})",
            f"  ICC(3,k)                   : {_fmt(p['icc_3k'])}   gate >= 0.80 (repo convention)",
            f"  Pearson r / Spearman rho   : {_fmt(p['pearson_r'])} / {_fmt(p['spearman_rho'])}",
            f"  QWK                        : {_fmt(p['qwk'])}",
            f"  Exact / adjacent agreement : {p['exact_agreement_pct']}% / {p['adjacent_agreement_pct']}%",
            f"  Wilcoxon W / p             : {p['wilcoxon_w']} / {_fmt_p(p['wilcoxon_p'])}",
            f"  Items with confidence <0.75: {low} of {p['n_items']} -> HITL queue",
            f"  Verdict                    : {'PASS' if p['passed'] else 'FAIL'}",
        ]
    if "criteria" in res:
        L += ["", "[Per-criterion diagnostics] d.rho >= 0.70 and QWK >= 0.60"]
        for name, block in res["criteria"].items():
            d = block["diagnostic"]
            L.append(f"  {name:<22}: {d['flag']:<5} (d.rho/rho {_fmt(d.get('d_rho_or_rho'))}, QWK {_fmt(d.get('qwk'))})")
    return "\n".join(L)


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Statistical auditing for LLM-as-a-Judge (AUA report).")
    ap.add_argument("--input", type=Path, help="JSON file with ratings (see module docstring)")
    ap.add_argument("--demo", action="store_true", help="Run both bundled fixtures in examples/fixtures/")
    ap.add_argument("--llm-reliability", type=float, default=None,
                    help="LLM-judge reliability for d.R (default: Pipeline 2 alpha if passes given, else 1.0)")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of the text report")
    args = ap.parse_args(argv)

    if not args.input and not args.demo:
        ap.error("provide --input FILE or --demo")

    inputs = [args.input] if args.input else sorted(FIXTURES_DIR.glob("*.json"))
    reports = {}
    for path in inputs:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        reports[Path(path).stem] = audit(data, args.llm_reliability)

    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        print("\n\n".join(format_report(r, name) for name, r in reports.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
