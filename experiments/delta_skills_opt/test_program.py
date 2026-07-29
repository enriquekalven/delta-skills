import pytest
from initial_program import resolve_capability_slot, verify_phase_gate, calculate_synthetic_baseline

def test_resolve_capability_slot():
    caps = resolve_capability_slot(1, "Customer-Intake")
    assert isinstance(caps, list)
    assert "workshop-intake" in caps

def test_verify_phase_gate():
    approved, msg = verify_phase_gate(1, {}, {"prd": "PRD.md", "baseline_kpis_committed": True})
    assert approved is True
    assert "Passed" in msg

    rejected, msg = verify_phase_gate(1, {}, {})
    assert rejected is False

def test_calculate_synthetic_baseline():
    samples = [
        {"handling_time_min": 45.0, "has_error": False, "is_escalated": False} for _ in range(50)
    ]
    kpis = calculate_synthetic_baseline(samples)
    assert kpis["sample_size"] == 50
    assert kpis["baseline_metrics"]["avg_handling_time_minutes"] == 45.0
    assert kpis["baseline_metrics"]["unit_cost_usd"] == 56.25
