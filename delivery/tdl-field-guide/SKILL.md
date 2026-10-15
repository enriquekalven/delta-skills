---
name: tdl-field-guide
description: >
  Field playbook for Technical Deployment Leads running a 12-week Google Cloud Delta engagement
  per go/delta-delivery-guide: Prelude (qualification + access clearance), Phase 1 Foundations
  (weeks 1-2), Phase 2 Core Build & bi-weekly Demo Sprints (weeks 3-10, four sprints, three
  milestone demos, next-phase scoping ~week 10), Phase 3 Final Read-Out & Close (weeks 11-12).
  Adds this repo's STATE.md gate tracking, dual RAID logs from the Program Tracker, and a
  rollback loop. Triggers on "tdl field guide", "run a delta engagement", "what phase are we in",
  "program tracker", "demo frame-up", "closeout deck", "12-week plan".
metadata:
  version: '3.1'
---

# TDL Field Guide: the 12-Week Delta Engagement

This skill sequences the engagement and enforces gates; specialist work is delegated to the linked skills. Two kinds of content are kept apart on purpose:

- **Official** — taken from the TDL Toolbox: `go/delta-delivery-guide` (12-Week AI Delivery Guide), the example Kickoff Deck, the Demo Frame-Up deck, the Program Tracker, the Closeout Deck template and the FDE Retro deck.
- **Repo convention** — governance this repository adds (`STATE.md`, gate sign-offs, 1-in-1-out scope swaps, rollback loop). Useful, but do not present it to a customer as Google's standard.

---

## 1. Who is on the squad (official)

| Role | Appears in | Owns |
|---|---|---|
| **Technical Deployment Lead (TDL)** | Kickoff deck, delivery guide | Architecture, `go/delta-squad-agent-specs`, demos, phase gates, this guide |
| **Technical Deployment Manager (TDM)** | Kickoff deck | Program tracker, cadences, RAID, stakeholder comms |
| **Forward Deployed Engineers (FDE ×2–3)** | Kickoff deck, delivery guide | Build, evaluation harness, load testing, production hardening |
| **Account team — AE, Field Solutions Architect (FSA), Customer Engineer** | Kickoff deck ("stateful account team") | Commercial relationship, environment/quota access, continuity after week 12 |
| **Agentic Transformation Lead (ATL)** | `delta /forward` | Process ethnography, CUJ mapping, change management |
| **10x Lead** | `delta /forward` deck | Origination and executive sponsorship |

Customer side (kickoff deck): executive sponsor, product owner, engineering/platform leads, business/end-user representatives, security/compliance.

**Repo convention — small engagements:** collapse to a **TDL + FDE pair**; the TDL absorbs TDM/ATL duties. Record the collapse in `STATE.md` so gate owners are unambiguous.

---

## 2. Non-negotiables

**Official (`go/delta-delivery-guide`)**
1. **One use case per 12-week squad.** "Commit strictly to one high-priority use case per 12-week timeline. Multi-scoping dilutes focus." Additional asks go into the next-phase plan.
2. **Crucial access before the clock starts.** Device/system access, datasets and benchmark data (Part III of `go/delta-squad-agent-specs`) are secured in the Prelude, not in week 1.
3. **PRD by end of week 2**, built on a Golden Dataset with baseline evaluation metrics.
4. **Bi-weekly demos** of *working* functionality to client leadership, structured as **four 2-week sprints**.
5. **Next-phase plan drafted around week 10**; final read-out, TDD hand-over and knowledge transfer in weeks 11–12; **blameless internal retro** after close.

**Repo convention (this skill adds)**
6. **12-week cap:** scope moves, the date does not.
7. **1-in / 1-out:** a mid-flight request enters only if an item of equal or higher RICE score leaves; log both in `STATE.md`.
8. **Baseline before build:** establish baseline evaluation metrics on the curated Golden Dataset in `docs/TDD.md` (Part IV) and record operational baseline metrics in `docs/as_is_report.md` in Phase 1; no ROI or quality lift claim in week 12 without them.
9. **Environment segregation:** synthetic data in shared sandboxes (`gcc-delta-tdl`); customer data only inside the customer's project/VPC.
10. **No phase advance without a named human sign-off recorded in `STATE.md`.**

---

## 3. State tracking: `STATE.md` + the Program Tracker

**Program Tracker (official, 9 tabs in the toolbox copy):** `Timeline`, `Use Cases`, `Staffing`, `Use Case RAID`, `Program RAID`, `Meetings`, `OOO`, plus two engagement-specific tabs (onsite agenda, pod roster). RAID columns verbatim:

- *Use Case RAID:* `Use Case / Workstream | Google RAID Owner | Lead LGTM'd? | Category (Risk / Issue / Decision / Action Item) | Description | Date Added | Status | Latest Update | Owner`
- *Program RAID:* `ID (Auto) | Use Case / Workstream | Google RAID Owner | Category | Description | Date Added | Status | Latest Update | Owner | Last Update (Timestamp)`

**`STATE.md` (repo convention)** at the engagement repo root:

```markdown
# STATE
project: "<Customer — use case>"
phase: 2            # 0 Prelude | 1 Foundations | 2 Build & Demo Sprints | 3 Read-Out & Close
week: 5
sprint: 2           # 1-4 (phase 2 only)
squad: full         # full | pair (TDL+FDE)
last_gate_passed: 1
gate_signoff: "<name, title>, <YYYY-MM-DD>"
action: NONE        # NONE | ROLLBACK_TO_PHASE_1 | ROLLBACK_TO_SPRINT_PLAN
scope_log:
  - in: "<feature id> <name>" (RICE <n>)   out: "<feature id> <name>" (RICE <n>)   date: <YYYY-MM-DD>   approved_by: "<sponsor>"
use_case_raid:   # mirror of the tracker tab, same columns
  - {workstream: "", google_owner: "", lead_lgtmd: "Yes", category: "Issue", description: "", date_added: "", status: "Open", latest_update: "", owner: ""}
program_raid:
  - {id: "A-001", workstream: "", google_owner: "", category: "Action Item", description: "", date_added: "", status: "Open", latest_update: "", owner: ""}
```

Read `STATE.md` before any session. If `action` is a rollback, stop feature work and fix the design/spec defect first.

---

## 4. Phases and gates (weeks per `go/delta-delivery-guide`)

### Prelude — qualification & crucial access (before week 1)

| Step | Skill / asset | Output |
|---|---|---|
| Qualify the use case (idea → good → ready; `Available / Usable / Quality` data yardstick) | [workshop-intake](../../workshop-intake/SKILL.md) | `docs/WORKSHOP_INTAKE.md` |
| MVP alignment summary | [create-delta-ucc](../../usecase-canvas/create-delta-ucc/SKILL.md) | `docs/USE_CASE_CANVAS.md` |
| Developer access clearance + Golden Dataset | [specification-engineer](../../utils/specification-engineer/SKILL.md) Part III | signed clearance checklist, dataset reachable from the sandbox |

**Gate 0 (repo convention):** clearance signed by the customer cloud admin; Golden Dataset accessible. Set `phase: 1`.

### Phase 1 — Foundations (weeks 1–2)

| Step (official activity list) | Skill / asset | Output |
|---|---|---|
| Kickoff: team intros, charter, cadences, assumptions (sandbox, user scope) | Kickoff deck (toolbox asset 06) | kickoff deck, in-squad RACI (`go/delta-12-week-delivery-raci`) |
| Process ethnography & CUJ map | [business-process-redesign](../../business-process-redesign/SKILL.md), [cuj-architect](../../cuj-architect/SKILL.md) | `docs/as_is_report.md`, `docs/CUJ_MAP.md` |
| Baseline evaluation metrics on the Golden Dataset | [specification-engineer](../../utils/specification-engineer/SKILL.md) Part IV, [agent-eval-statistical-auditing](../agent-eval-statistical-auditing/SKILL.md) | `docs/TDD.md` (Part IV Golden Dataset & Eval Rubrics) |
| Agentic PRD (due end of week 2) | [product-md](../../product-management/product-md/SKILL.md) | `docs/PRD.md` |
| Architecture + agent technical specs | [gcp-agent-architecture-advisor](../gcp-agent-architecture-advisor/SKILL.md), [specification-engineer](../../utils/specification-engineer/SKILL.md) | `docs/ARCHITECTURE_RECOMMENDATION.md`, `docs/TDD.md` |
| Discovery prototype / feasibility spike (2–4 h synthetic; ≤ 2 weeks on real data) | [stitch-design](../../prototyping/stitch-design/SKILL.md) | `docs/STITCH_PROTOTYPE.md` |

**Gate 1:** sponsor and engineering lead sign `docs/PRD.md`, `docs/TDD.md` (including Golden Dataset baseline metrics), and `docs/as_is_report.md`. Set `phase: 2`.

### Phase 2 — Core Build & Demo Sprints (weeks 3–10, four 2-week sprints)

Every sprint: plan with clear owners → build → **demo working functionality** + evaluation read-out against the agreed test set → re-plan. The Demo Frame-Up deck (official example: Intel AskHR, **39 committed features**) frames three milestone demos:

| Milestone demo | Theme (from the deck) | Content |
|---|---|---|
| **Demo 1** | Fundamental user experience, core intelligence, self-service value | happy-path CUJ end to end; grouped by pillar (e.g. Conversational Intelligence · Grounded Responses · Self-Service · Continuous Optimization) |
| **Demo 2** | Advanced features & enterprise readiness | deep transactions, full-lifecycle ticketing/integrations, compliance & governance, scale/security |
| **Demo 3** | Final refinements, development complete | **all committed features**, eval scorecard, go-live readiness |

Frame-up table columns: `Pillar | Feature (ID from the PRD backlog, e.g. AI-HR-0039) | Demo 1/2/3 | Status`. The deck dates demos ~2 weeks apart ending at go-live; map them to sprint read-outs, not fixed week numbers.

| Sprint focus (repo recommendation) | Skill | Output |
|---|---|---|
| Sprints 1–2: core build, Demo 1 | [claude-agent-harness](../../ai-coding/claude-agent-harness/SKILL.md) (or your coding agent + `google-agents-cli-adk-code`), [product-md](../../product-management/product-md/SKILL.md) §5 | code + passing tests, eval round 1 |
| Sprints 3–4: enterprise readiness, Demo 2–3 | [agent-load-testing](../agent-load-testing/SKILL.md), [agent-eval-statistical-auditing](../agent-eval-statistical-auditing/SKILL.md) | `docs/LOAD_TEST_REPORT.md`, `docs/EVAL_AUDIT_REPORT.md` |
| ~Week 10: next-phase scoping & backlog | [create-delta-ucc](../../usecase-canvas/create-delta-ucc/SKILL.md), [ai-value-sizing](../../ai-value-sizing/SKILL.md) | next-phase plan (another Delta cycle or PSO scaling) |

**Gate 2 (repo convention):** Demo 3 accepted; quotas sized at 5× peak; judge audit passed; next-phase scope drafted. Set `phase: 3`.

**Rollback (repo convention):** a defect rooted in architecture, perimeter or spec (not code) sets `action: ROLLBACK_TO_PHASE_1`; fix `docs/TDD.md` / `docs/ARCHITECTURE_RECOMMENDATION.md` before resuming the sprint.

### Phase 3 — Final Read-Out & Close (weeks 11–12)

| Step (official) | Skill / asset | Output |
|---|---|---|
| Finalize & sign off next-phase scope | — | signed scope |
| Executive read-out: baseline → measured outcome | Closeout deck (toolbox asset 08): `The Challenge | The Vision | The Experience` → `The Architecture | The Tech` (user workflow) → `The Value | The Future` | closeout deck |
| Measured value vs. frozen baseline | [ai-value-sizing](../../ai-value-sizing/SKILL.md) | `docs/VALUE_SIZING.md` |
| TDD hand-over, knowledge transfer, runbooks | [specification-engineer](../../utils/specification-engineer/SKILL.md) | final `docs/TDD.md`, runbook |
| Google-internal blameless retrospective | FDE retro deck (toolbox asset 09) | retro notes; reusable patterns harvested (`/forward`: "Harvest Everything") |

**Gate 3:** service live in the customer environment with monitoring; read-out delivered with measured (not projected) KPIs; hand-over accepted.

---

## 5. Worked example

- [examples/engagement-state-and-gate-review.md](examples/engagement-state-and-gate-review.md) — an **illustrative** (fictional) Acme P&C commercial-auto FNOL engagement: `STATE.md` at a week-7 rollback and at week-12 close, a demo frame-up table, and both RAID logs in the tracker's columns.
