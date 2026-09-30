---
name: tdl-field-guide
description: >
  Field playbook for Technical Deployment Leads (TDLs) running a 12-week Google Cloud
  Delta engagement: squad roles, governance rules (12-week cap, 1-in-1-out scope swaps,
  50-sample baseline, environment segregation), four phase gates with required artifacts,
  and a STATE.md rollback loop. Triggers on "tdl field guide", "tdl playbook", "run a delta
  engagement", "plan the 12-week engagement", "what phase are we in". Do NOT trigger for a
  single isolated task (e.g. only writing a PRD) - use that skill directly.
metadata:
  version: '1.0'
---

# TDL Field Guide: 12-Week Delta Engagement

This skill sequences an engagement. It does not do the specialist work itself; each phase
hands off to a skill in this repo (or an optional external skill) and then enforces a gate.

## 1. Squad roles

| # | Role | Owns | Most active |
|---|---|---|---|
| 01 | 10X Lead | Origination, executive sponsor relationship | Pre-engagement, Phase 1 |
| 02 | AI Activation Lead | Governance, value case, stakeholder alignment | Phases 1, 4 |
| 03 | Technical Deployment Lead (TDL) | Architecture, specs, phase gates, `STATE.md` | All phases |
| 04 | Forward-Deployed Engineer (FDE) | Build, hardening, tests | Phases 2-4 |
| 05 | Platform Engineer | Productization, CI/CD, deployment | Phases 3-4 |
| 06 | Agentic Transformation Lead (ATL) | Change management, scaling, adoption | Phases 3-4 |

**Small engagements:** collapse to a **TDL + FDE pair**. The TDL absorbs roles 01, 02 and
06; the FDE absorbs 05. Record the collapse in `STATE.md` so gate owners are unambiguous.

## 2. Governance rules (non-negotiable)

1. **12-week cap.** The window is fixed. Scope moves; the date does not.
2. **1-in, 1-out scope control.** A mid-flight request enters only if an item of equal or
   greater RICE score leaves. Log both items and both scores in `STATE.md`.
3. **Baseline before build.** Run [synthetic-baseline-protocol](../synthetic-baseline-protocol/SKILL.md)
   in Phase 1 and freeze `docs/baseline_kpis.json`. No ROI claim in Phase 4 without it.
4. **Environment segregation.** PoC and staging use sanitized or synthetic data only.
   Real client data is used only inside the client's own project/VPC.

## 3. State tracking

Keep a `STATE.md` at the engagement repo root. Minimum fields:

```markdown
# STATE
phase: 2            # 1 | 2 | 3 | 4
week: 4
squad: full         # full | pair (TDL+FDE)
last_gate_passed: 1
gate_signoff: "<sponsor name>, <date>"
action: NONE        # NONE | ROLLBACK_TO_PHASE_2
scope_log:
  - in: "<item>" (RICE 42)  out: "<item>" (RICE 45)  date: <date>
open_risks:
  - <risk>
```

Before any work in a session: read `STATE.md`. If `action: ROLLBACK_TO_PHASE_2`, stop
build work and re-run the Phase 2 steps affected by the defect before anything else.

## 4. Phases and gates

Week ranges: **1-2 / 3-5 / 6-10 / 11-12**.

### Phase 1 - Discover & Define (weeks 1-2, TDL-led)

| Step | Skill | Artifact |
|---|---|---|
| Intake / discovery call | [workshop-intake](../../workshop-intake/SKILL.md) | Intake notes |
| Strategic framing (if exec-level) | [strategy-house](../../strategy-house/SKILL.md) | Strategy house, opportunity matrix |
| Process mapping (if process-heavy) | [business-process-redesign](../../business-process-redesign/SKILL.md) | As-Is / To-Be |
| User journeys | [cuj-architect](../../cuj-architect/SKILL.md) | CUJ map |
| Requirements | [product-md](../../product-management/product-md/SKILL.md) | `docs/PRD.md` |
| Baseline audit | [synthetic-baseline-protocol](../synthetic-baseline-protocol/SKILL.md) | `docs/baseline_kpis.json` |
| Existing codebase (if any) | optional: `codebase-onboarding-and-mapping` | `docs/ONBOARDING.md` |

**Gate 1:** `docs/PRD.md` (goals, non-goals, success metrics) and `docs/baseline_kpis.json`
exist, plus `docs/ONBOARDING.md` if there is an existing codebase. Sponsor signs off. Set
`phase: 2`.

### Phase 2 - Prototype & Validate (weeks 3-5, TDL + FDE)

| Step | Skill | Artifact |
|---|---|---|
| Architecture choice | [gcp-agent-architecture-advisor](../gcp-agent-architecture-advisor/SKILL.md) | `docs/ARCHITECTURE_RECOMMENDATION.md` |
| Technical spec | [specification-engineer](../../utils/specification-engineer/SKILL.md) | `docs/TDD.md` |
| Threat model | optional: `determine-threat-model`, `security-and-hardening` | `docs/THREAT_MODEL.md` |
| Prototype UI (if needed) | [frontend-design](../../prototyping/frontend-design/SKILL.md) or [stitch-design](../../prototyping/stitch-design/SKILL.md) | Clickable prototype |
| Agent scaffold (if ADK) | optional: `google-agents-cli-scaffold` | Scaffolded project |

**Gate 2:** architecture recommendation (with launch stages verified and dated) and threat
model are approved by the sponsor and, where required, the client security team. Set
`phase: 3`.

### Phase 3 - Production Build (weeks 6-10, FDE-led)

| Step | Skill | Artifact |
|---|---|---|
| Task breakdown | optional: `planning-and-task-breakdown` | RICE-ordered backlog |
| Implementation | [claude-agent-harness](../../ai-coding/claude-agent-harness/SKILL.md) or your normal coding agent | Code + passing tests |
| Intent audit | optional: `intended-vs-implemented` | Gap report |
| Code review | optional: `code-review-and-quality` | Review sign-off |

**Rollback loop:** if a defect traces to the architecture or threat model (not the code),
set `action: ROLLBACK_TO_PHASE_2` in `STATE.md`, record the defect, and fix the design
first.

**Gate 3:** all tests pass in CI, the intent-audit gaps are closed or explicitly accepted,
and no open Critical/High security findings remain. Set `phase: 4`.

### Phase 4 - Harden & Launch (weeks 11-12, full squad)

| Step | Skill | Artifact |
|---|---|---|
| Agent evaluation | optional: `google-agents-cli-eval` | Eval results vs. thresholds |
| ROI vs. baseline | [ai-value-sizing](../../ai-value-sizing/SKILL.md) | ROI report citing `baseline_kpis.json` |
| Deployment | optional: `shipping-and-launch`, `google-agents-cli-deploy` | Running service, rollback plan |
| Handoff | optional: `shipping-artifacts` | Architecture, flows, variables, runbook |

**Gate 4:** the service is live in the client environment with monitoring, the ROI report
compares measured post-deployment KPIs against the frozen baseline (not targets), and the
handoff packet is accepted.

## 5. Rules for the agent

- Never advance `phase` without an explicit human sign-off recorded in `STATE.md`.
- Skills marked *optional* live outside this repo. If one is not installed, do the step
  manually and say so; do not invent its output.
- Report measured numbers only. Targets from `baseline_kpis.json` are hypotheses until
  Phase 4 measures them.
