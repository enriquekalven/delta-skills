# Phase-Gated Execution Model

Complex software projects and enterprise engagements require state-gated execution rather than un-gated single-turn execution.

Running a multi-phase project from initial discovery through production deployment in a single pass risks scope drift, context exhaustion, and missed human verification gates.

---

## Un-Gated vs Phase-Gated Execution

### Un-Gated Single-Turn Execution (Anti-Pattern)
```
[User Input] --> [Agent runs Scoping, PRD, Arch, Build, Security, Launch in 1 turn] --> Failure
                 • No human sign-off on PRD scope
                 • No InfoSec review prior to build phase
                 • Unverified assumptions compound across phases
                 • Context window exhaustion and quality loss
```

### Phase-Gated Execution Pattern
```
[Invoke Meta-Skill] 
       |
       v
┌──────────────┐      Gate Check       ┌─────────────────────────────────┐
│ TDL Phase 1  │ ---> (Human Review) -->│ "PRD & baseline_kpis APPROVED?" │
└──────────────┘                        └────────────────┬────────────────┘
                                                         │ YES
                                                         v
                                               ┌──────────────────┐
                                               │   TDL Phase 2    │
                                               └──────────────────┘
```

---

## State Machine Execution Flow

### 1. State Inspection
When invoked, the meta-skill reads `STATE.md` in the workspace root:
```markdown
# Current Engagement State
- Engagement: Customer Real Estate Concierge
- Current Phase: Phase 1 (Discover & Define)
- Status: PRD Drafted. Pending Synthetic Baseline Audit.
```

### 2. Single-Phase Execution
The agent executes only active tasks mapped to the current phase (e.g. running intake, capturing `baseline_kpis.json`, and writing `create-prd`).

### 3. Execution Stop & Gate Evaluation
The agent stops execution and presents a gate review:

> **PHASE 1 GATE CHECK**
> * PRD generated: `docs/PRD.md`
> * Baseline captured: `baseline_kpis.json` (50 samples audited)
> 
> **Action Required**: Please review `docs/PRD.md`.
> * Reply **"Approved"** to advance `STATE.md` to Phase 2 (Architecture & InfoSec).
> * Or reply with feedback to iterate on Phase 1 requirements.

### 4. Resumable State Transition
When the user approves, the agent updates `STATE.md` to `Phase 2: Prototype & Validate` and advances context to architecture grilling (`grill-with-docs`) and threat modeling (`threat-model-analyst`).

---

## Operational Benefits

Packaging tasks under a meta-skill provides structured governance:
1. Maintains a deterministic execution pipeline.
2. Tracks progress via persistent state (`STATE.md`).
3. Enforces human-in-the-loop verification gates prior to advancing project state.
