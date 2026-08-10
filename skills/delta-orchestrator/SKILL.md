---
name: delta-orchestrator
description: >
  Master Router & Anthropic Loop Engineering Orchestrator.
  Coordinates transitions across the 4 natural customer engagement phases (delta-discover, delta-plan, delta-build, delta-harden) using Anthropic's 5 Core Agentic Workflow Patterns (Orchestrator-Workers, Evaluator-Optimizer, Prompt Chaining, Routing, Parallelization).
  Enforces zero-hardcoding: reads real workspace files, scans live code, and reports missing gaps with actionable recommendations.
  Triggers on: "delta orchestrator", "run delta suite", "delta workflow", "master orchestrator", "loop engineering", "anthropic patterns".
---

# Delta Master Lifecycle Orchestrator (`delta-orchestrator`)

Governs the 4-phase enterprise customer engagement lifecycle grounded strictly in **Anthropic's Loop Engineering Best Practices** (*Building Effective Agents*, Dec 2024).

---

## 🚫 ZERO-HARDCODING & GROUND-TRUTH PRINCIPLE

> [!IMPORTANT]
> **Core Engineering Rule**: Never hallucinate, mock, or hardcode metrics, baseline data, or test results. Always read real workspace files on disk. If artifacts, files, or test suites are missing, explicitly report the gap (`❌ MISSING`) and provide actionable recommendations (`💡 Recommendation`) to resolve it.

---

## 🌀 Anthropic's 5 Loop Engineering Patterns Integrated

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ANTHROPIC AGENTIC LOOP PATTERNS                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. ORCHESTRATOR-WORKERS : delta-orchestrator delegates tasks to        │
│                           delta-discover, delta-plan, delta-build,     │
│                           and delta-harden.                            │
│                                                                        │
│ 2. EVALUATOR-OPTIMIZER  : delta-harden pairs Gemini Flash generator    │
│                           with Vertex AI Model Garden Opus 5 ZDR       │
│                           peer reviewer.                               │
│                                                                        │
│ 3. PROMPT CHAINING      : Programmatic phase gates (delta_cli.py)      │
│                           verify outputs before advancing.             │
│                                                                        │
│ 4. ROUTING              : Directs tasks based on cost/complexity       │
│                           (Haiku vs Sonnet vs Opus 5).                 │
│                                                                        │
│ 5. PARALLELIZATION      : Sectioning (independent component audits)    │
│                           + Voting (multi-prompt security reviews).    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🏛️ 4-Phase Engagement Lifecycle

1. **🔍 PHASE 1: `delta-discover`**
   - Customer intake interviews, repository dependency mapping (`ONBOARDING.md`), and 50 SME ticket baseline audit (`baseline_kpis.json`).
   - *Human Checkpoint*: Problem statement & baseline ROI sign-off.

2. **🏛️ PHASE 2: `delta-plan`**
   - GCP 3-tier architecture recommendation, Abstraction Selection Matrix, `THREAT_MODEL.md`, and 2-role squad pair initialization.
   - *Human Checkpoint*: GCP Architecture recommendation sign-off.

3. **🛠️ PHASE 3: `delta-build`**
   - `prd.json` TDD task loop with red-green-refactor iteration, FastMCP tool servers, secret scanning, and Playwright CLI UI tests.
   - *Human Checkpoint*: Programmatic secret scan & 100% pytest pass rate.

4. **🔒 PHASE 4: `delta-harden`**
   - Plain-English anti-slop audit (`rm-slop`), Vertex AI Model Garden Opus 5 ZDR review, and ROI savings report.
   - *Human Checkpoint*: Operational handoff packet & launch sign-off.

---

## 💻 CLI Orchestration Commands

```bash
# Verify phase gate status before advancing STATE.md:
python3 skills/delta-build/scripts/delta_cli.py build --phase 1

# Run AlphaEvolve dynamic evaluation cascade:
python3 skills/delta-build/scripts/delta_cli.py build --phase 1 --eval-cascade
```
