---
name: delta-orchestrator
description: >
  Master Router & Phase-Gate Lifecycle Orchestrator.
  Coordinates transitions across the 4 natural customer engagement phases: delta-discover (Phase 1), delta-plan (Phase 2), delta-build (Phase 3), and delta-harden (Phase 4).
  Triggers on: "delta orchestrator", "run delta suite", "delta workflow", "master orchestrator", "phase transition".
---

# Delta Master Lifecycle Orchestrator (`delta-orchestrator`)

Governs the 4-phase enterprise customer engagement lifecycle. Ensures that each phase completes its natural human feedback loops, customer interviews, and gate verifications before advancing `STATE.md`.

---

## 🏛️ 4-Phase Engagement Lifecycle

```
┌────────────────────────────────────────────────────────────────────────┐
│                    DELTA 4-PHASE LIFECYCLE ROUTER                      │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│ 🔍 PHASE 1: delta-discover (Weeks 1-3)                                 │
│    • Conduct customer intake interviews & repo mapping (ONBOARDING.md).│
│    • Audit 50 SME tickets to establish baseline_kpis.json.             │
│    • Customer Sign-off: Problem statement & baseline ROI frozen.       │
│                                                                        │
│ 🏛️ PHASE 2: delta-plan (Weeks 4-6)                                     │
│    • Workshop PRD requirements & run GCP Abstraction Selection Matrix. │
│    • Build THREAT_MODEL.md & initialize 2-role squad pair.             │
│    • Customer Sign-off: GCP 3-tier architecture recommendation.        │
│                                                                        │
│ 🛠️ PHASE 3: delta-build (Weeks 7-10)                                   │
│    • Execute prd.json task loops with TDD red-green-refactor iteration.│
│    • Build FastMCP tool servers & run Playwright CLI UI tests.         │
│    • Verification Gate: Programmatic secret scan & 100% pytest pass.  │
│                                                                        │
│ 🔒 PHASE 4: delta-harden (Weeks 11-12)                                 │
│    • Run rm-slop plain-English audit & Model Garden Opus 5 ZDR review. │
│    • Validate final ROI metric savings & deliver HANDOFF_PACKET.md.    │
│    • Customer Sign-off: Operational handoff & launch.                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 CLI Orchestration Commands

```bash
# Verify phase gate status before advancing STATE.md:
python3 skills/delta-build/scripts/delta_cli.py build --phase 1
```
