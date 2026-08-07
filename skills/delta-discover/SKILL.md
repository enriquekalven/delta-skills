---
name: delta-discover
description: >
  Phase 1 Discovery & Customer Intake Skill.
  Conducts customer intake interviews, maps repository component dependencies (ONBOARDING.md), and audits 50 historical SME tickets to freeze baseline_kpis.json.
  Triggers on: "delta discover", "phase 1 discovery", "customer intake", "sme ticket audit", "baseline kpi".
---

# Phase 1: Discovery & Customer Intake (`delta-discover`)

Governs Phase 1 (Weeks 1-3) of the engagement lifecycle. Establishes the baseline ROI benchmarks, maps repository architecture, and conducts customer interviews to align stakeholders on project scope.

---

## 📋 Phase 1 Protocol & Deliverables

1. **Customer Intake Interview**: Interview client SMEs to identify pain points, handling time, and error rates.
2. **Repository Dependency Mapping**: Generate `docs/ONBOARDING.md` detailing system components, entry points, and data boundaries.
3. **50 SME Ticket Baseline Audit**: Audit 50 historical tickets to calculate blended hourly rate, unit cost, and target annual savings in `baseline_kpis.json`.

---

## 💻 CLI Execution

```bash
python3 skills/delta-build/scripts/delta_cli.py analyze --path .
```

---

## ✋ Human Checkpoint (Phase Gate 1 Exit)
Customer SME sign-off required on `PRD.md` and `baseline_kpis.json` before advancing to Phase 2 (`delta-plan`).
