"""
Delta Skills Meta-Orchestrator Initial Program

This program defines the core execution algorithms for:
1. E2E Delivery Workflow Orchestration & Phase Gate verification.
2. Synthetic Baseline Protocol calculation and KPI benchmarking.

AlphaEvolve will hill-climb the functions inside the EVOLVE-BLOCKs to improve execution speed,
accuracy, phase-gate verification accuracy, and KPI optimization precision.
"""

import json
from typing import Dict, Any, List, Tuple


# EVOLVE-BLOCK-START
def resolve_capability_slot(phase: int, capability_name: str) -> List[str]:
    """
    Resolves runtime capability slots for E2E Delivery & TDL Meta-Orchestrator phases.
    Returns prioritized list of primary and secondary tools.
    """
    matrix = {
        1: {
            "Customer-Intake": ["workshop-intake", "interview-me"],
            "Scope-Mapping": ["opportunity-solution-tree", "user-stories", "job-stories"],
            "PRD-Creation": ["create-prd", "spec-driven-development"],
        },
        2: {
            "Architecture-Grilling": ["grill-with-docs", "google-agents-cli-adk-code"],
            "Tech-Design-Document": ["documentation-and-adrs", "spec-driven-development"],
            "API-Design": ["api-and-interface-design", "domain-modeling"],
            "InfoSec-Threat-Modeling": ["threat-model-analyst", "security-and-hardening"],
        },
        3: {
            "Task-Breakdown": ["planning-and-task-breakdown", "to-tickets"],
            "TDD-Build": ["test-driven-development", "source-driven-development"],
            "Intent-Audit": ["intended-vs-implemented", "sql-queries"],
            "Code-Review": ["code-review-and-quality", "code-simplification"],
        },
        4: {
            "Agent-Evaluation": ["google-agents-cli-eval", "eval-quality-gate"],
            "ROI-Sizing": ["ai-value-sizing", "cohort-analysis", "ab-test-analysis"],
            "Release-Deployment": ["shipping-and-launch", "google-agents-cli-deploy"],
            "Handoff-Artifacts": ["shipping-artifacts", "release-notes", "retro"],
        }
    }
    phase_caps = matrix.get(phase, {})
    return phase_caps.get(capability_name, ["generic-skill"])


def verify_phase_gate(phase: int, state_data: Dict[str, Any], artifacts: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Verifies if a Phase Gate is satisfied before advancing state in STATE.md.
    Returns (is_approved, reason).
    """
    if phase == 1:
        if "prd" in artifacts and artifacts.get("baseline_kpis_committed", False):
            return True, "Phase 1 Gate Passed: PRD and baseline_kpis.json verified."
        return False, "Missing PRD or uncommitted baseline_kpis.json."
    elif phase == 2:
        if artifacts.get("tdd_doc", False) and artifacts.get("infosec_approval", False):
            return True, "Phase 2 Gate Passed: TDD.md and InfoSec Matrix approved."
        return False, "Missing TDD documentation or InfoSec sign-off."
    elif phase == 3:
        if artifacts.get("test_pass_rate", 0.0) >= 1.0 and artifacts.get("intent_gap_cleared", False):
            return True, "Phase 3 Gate Passed: 100% test pass rate and zero intent gaps."
        return False, "Tests not passing at 100% or intent gaps remain."
    elif phase == 4:
        if artifacts.get("roi_dashboard", False) and artifacts.get("handoff_packet", False):
            return True, "Phase 4 Gate Passed: ROI dashboard and handoff packet complete."
        return False, "Incomplete ROI dashboard or handoff packet."
    return False, f"Unknown phase: {phase}"


def calculate_synthetic_baseline(
    samples: List[Dict[str, Any]],
    blended_hourly_rate: float = 75.0,
    legacy_overhead_per_unit: float = 0.0
) -> Dict[str, Any]:
    """
    Computes quantitative baseline operational KPIs from N historical SME samples.
    """
    if not samples:
        return {}

    total_time = sum(s.get("handling_time_min", 0.0) for s in samples)
    error_count = sum(1 for s in samples if s.get("has_error", False))
    escalation_count = sum(1 for s in samples if s.get("is_escalated", False))

    n = len(samples)
    avg_handling_time = total_time / n
    error_rate = (error_count / n) * 100.0
    escalation_rate = (escalation_count / n) * 100.0

    unit_labor_cost = (avg_handling_time / 60.0) * blended_hourly_rate
    unit_cost = unit_labor_cost + legacy_overhead_per_unit

    annual_volume = 12000
    total_annual_cost = unit_cost * annual_volume

    target_handling_time = max(1.0, avg_handling_time * 0.067)  # 93.3% reduction target
    target_error_rate = max(0.5, error_rate * 0.14)            # ~86% reduction target
    target_unit_cost = (target_handling_time / 60.0) * blended_hourly_rate
    projected_savings = total_annual_cost - (target_unit_cost * annual_volume)

    return {
        "sample_size": n,
        "blended_hourly_rate_usd": blended_hourly_rate,
        "baseline_metrics": {
            "avg_handling_time_minutes": round(avg_handling_time, 2),
            "error_rate_percent": round(error_rate, 2),
            "escalation_rate_percent": round(escalation_rate, 2),
            "unit_cost_usd": round(unit_cost, 2),
            "annual_volume_units": annual_volume,
            "total_baseline_annual_cost_usd": round(total_annual_cost, 2)
        },
        "target_post_deployment_kpis": {
            "target_handling_time_minutes": round(target_handling_time, 2),
            "target_error_rate_percent": round(target_error_rate, 2),
            "target_unit_cost_usd": round(target_unit_cost, 2),
            "projected_annual_savings_usd": round(projected_savings, 2)
        }
    }
# EVOLVE-BLOCK-END


if __name__ == "__main__":
    # Smoke test execution
    caps = resolve_capability_slot(1, "Customer-Intake")
    print(f"Resolved capability slot: {caps}")

    gate_ok, msg = verify_phase_gate(1, {}, {"prd": "PRD.md", "baseline_kpis_committed": True})
    print(f"Gate test: {gate_ok} - {msg}")

    sample_data = [
        {"handling_time_min": 45.0, "has_error": False, "is_escalated": False} for _ in range(35)
    ] + [
        {"handling_time_min": 60.0, "has_error": True, "is_escalated": True} for _ in range(10)
    ] + [
        {"handling_time_min": 90.0, "has_error": True, "is_escalated": False} for _ in range(5)
    ]

    res = calculate_synthetic_baseline(sample_data)
    print(f"Baseline KPI test unit cost: ${res['baseline_metrics']['unit_cost_usd']}")
