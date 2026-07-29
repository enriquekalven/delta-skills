"""
CLI-compatible Evaluator for Delta Skills AlphaEvolve Optimization

Evaluates candidate algorithms on 3 benchmark axes:
1. Capability Slot Resolution Accuracy & Speed
2. Phase Gate Verification Precision (handling true/false edge cases)
3. Synthetic Baseline Protocol Financial Accuracy & ROI Projection Quality
"""

import sys
import os
import argparse
import json
import math
import time
import trace
from typing import Dict, Any, List


def evaluate_program(code: str, timeout_seconds: int = 30) -> Dict[str, Any]:
    """
    Evaluates Candidate Python Code and returns a score dict with insights.
    """
    insights: List[Dict[str, str]] = []
    
    # 1. Syntax check
    try:
        compiled_code = compile(code, "<candidate>", "exec")
    except Exception as e:
        insights.append({"label": "Syntax Error", "text": str(e)})
        return {"score": None, "insights": insights}

    # 2. Exec environment setup
    exec_globals: Dict[str, Any] = {}
    try:
        start_t = time.perf_counter()
        exec(compiled_code, exec_globals)
        exec_t = (time.perf_counter() - start_t) * 1000.0  # ms
    except Exception as e:
        insights.append({"label": "Runtime Execution Error", "text": str(e)})
        return {"score": None, "insights": insights}

    # Extract required functions
    resolve_fn = exec_globals.get("resolve_capability_slot")
    verify_fn = exec_globals.get("verify_phase_gate")
    calc_fn = exec_globals.get("calculate_synthetic_baseline")

    if not (callable(resolve_fn) and callable(verify_fn) and callable(calc_fn)):
        insights.append({"label": "Missing Functions", "text": "Program must define resolve_capability_slot, verify_phase_gate, and calculate_synthetic_baseline."})
        return {"score": None, "insights": insights}

    # Benchmark 1: Capability Slot Resolution Tests
    cap_score = 0.0
    total_cap_tests = 4
    try:
        p1 = resolve_fn(1, "Customer-Intake")
        if isinstance(p1, list) and "workshop-intake" in p1:
            cap_score += 1.0

        p2 = resolve_fn(2, "InfoSec-Threat-Modeling")
        if isinstance(p2, list) and ("threat-model-analyst" in p2 or "security-and-hardening" in p2):
            cap_score += 1.0

        p3 = resolve_fn(3, "Intent-Audit")
        if isinstance(p3, list) and "intended-vs-implemented" in p3:
            cap_score += 1.0

        p4 = resolve_fn(4, "Agent-Evaluation")
        if isinstance(p4, list) and "google-agents-cli-eval" in p4:
            cap_score += 1.0
    except Exception as e:
        insights.append({"label": "Capability Resolution Test Failure", "text": str(e)})

    cap_accuracy = cap_score / total_cap_tests

    # Benchmark 2: Phase Gate Verification Tests
    gate_score = 0.0
    total_gate_tests = 5
    try:
        # Pass P1
        ok, msg = verify_fn(1, {}, {"prd": "PRD.md", "baseline_kpis_committed": True})
        if ok: gate_score += 1.0

        # Fail P1 (missing prd)
        ok, msg = verify_fn(1, {}, {"baseline_kpis_committed": True})
        if not ok: gate_score += 1.0

        # Pass P2
        ok, msg = verify_fn(2, {}, {"tdd_doc": True, "infosec_approval": True})
        if ok: gate_score += 1.0

        # Pass P3
        ok, msg = verify_fn(3, {}, {"test_pass_rate": 1.0, "intent_gap_cleared": True})
        if ok: gate_score += 1.0

        # Pass P4
        ok, msg = verify_fn(4, {}, {"roi_dashboard": True, "handoff_packet": True})
        if ok: gate_score += 1.0
    except Exception as e:
        insights.append({"label": "Phase Gate Test Failure", "text": str(e)})

    gate_accuracy = gate_score / total_gate_tests

    # Benchmark 3: Baseline Protocol Financial Calculation Tests
    financial_accuracy = 0.0
    try:
        samples = [
            {"handling_time_min": 45.0, "has_error": False, "is_escalated": False} for _ in range(35)
        ] + [
            {"handling_time_min": 60.0, "has_error": True, "is_escalated": True} for _ in range(10)
        ] + [
            {"handling_time_min": 90.0, "has_error": True, "is_escalated": False} for _ in range(5)
        ]

        res = calc_fn(samples, blended_hourly_rate=75.0)

        # Theoretical expected average handling time = (35*45 + 10*60 + 5*90) / 50 = (1575 + 600 + 450)/50 = 2625/50 = 52.5 min
        # Expected unit labor cost = (52.5 / 60) * 75 = 0.875 * 75 = $65.625 -> $65.63
        avg_h_time = res.get("baseline_metrics", {}).get("avg_handling_time_minutes", 0)
        unit_cost = res.get("baseline_metrics", {}).get("unit_cost_usd", 0)
        savings = res.get("target_post_deployment_kpis", {}).get("projected_annual_savings_usd", 0)

        if abs(avg_h_time - 52.5) < 0.1 and abs(unit_cost - 65.63) < 0.2 and savings > 0:
            financial_accuracy = 1.0
        else:
            insights.append({"label": "Financial Calculation Discrepancy", "text": f"Got avg_time={avg_h_time}, unit_cost={unit_cost}, savings={savings}"})
    except Exception as e:
        insights.append({"label": "Baseline Protocol Test Failure", "text": str(e)})

    # Composite Score (Maximized, 0.0 to 100.0 scale)
    raw_score = (0.35 * cap_accuracy + 0.35 * gate_accuracy + 0.30 * financial_accuracy) * 100.0
    
    # Execution speed penalty if excessively slow (> 100ms)
    speed_bonus = max(0.0, 5.0 - (exec_t / 20.0))
    total_score = raw_score + speed_bonus

    # Check for NaN / Inf as mandated by AlphaEvolve rules
    if math.isnan(total_score) or math.isinf(total_score):
        insights.append({"label": "Numerical Instability", "text": "Score is NaN or Inf."})
        return {"score": None, "insights": insights}

    insights.append({
        "label": "Performance Breakdown",
        "text": f"CapAccuracy: {cap_accuracy*100:.1f}%, GateAccuracy: {gate_accuracy*100:.1f}%, FinAccuracy: {financial_accuracy*100:.1f}%, ExecTime: {exec_t:.2f}ms"
    })

    return {"score": round(total_score, 4), "insights": insights}


def main():
    parser = argparse.ArgumentParser(description="AlphaEvolve CLI Evaluator")
    parser.add_argument("--program-dir", required=True, help="Directory containing initial_program.py")
    parser.add_argument("--output-file", required=True, help="JSON output filepath")
    args = parser.parse_args()

    prog_path = os.path.join(args.program_dir, "initial_program.py")
    if not os.path.exists(prog_path):
        # Fallback to any python candidate file in directory
        py_files = [f for f in os.listdir(args.program_dir) if f.endswith(".py") and f != "evaluator.py"]
        if py_files:
            prog_path = os.path.join(args.program_dir, py_files[0])

    try:
        with open(prog_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        result = {"score": None, "insights": [{"label": "File Read Error", "text": str(e)}]}
        with open(args.output_file, "w", encoding="utf-8") as out:
            json.dump(result, out, indent=2)
        sys.exit(1)

    result = evaluate_program(code)

    with open(args.output_file, "w", encoding="utf-8") as out:
        json.dump(result, out, indent=2)

    print(f"Evaluation complete. Score: {result['score']}")


if __name__ == "__main__":
    main()
