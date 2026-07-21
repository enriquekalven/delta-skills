# Phase-Gated Meta-Skill Execution Model

You have made a fundamental architectural insight: **A complex software project or 12-week client engagement CANNOT (and SHOULD NOT) execute in a single un-gated agent turn.** 

Trying to run a project from initial discovery through production launch in one pass violates security governance, blows context limits, and bypasses essential human/SME verification sign-offs.

---

## 🛑 Why One-Shot Execution Fails

```
❌ UN-GATED "ONE-SHOT" EXECUTION (Anti-Pattern)
[User Input] ──→ [Agent runs Scoping, PRD, Architecture, TDD, Security, Launch in 1 turn] ──→ 💥 Disaster
                 • No human sign-off on PRD scope
                 • No InfoSec board review before coding
                 • Hallucinated assumptions compound across phases
                 • Context window exhaustion & loss of precision
```

---

## 🟢 The Solution: State-Machine Meta-Skills with Phase Gates

Instead of a "one-shot batch script," a Meta-Skill (`e2e-delivery-workflow` or `tdl-field-guide`) operates as an **Iterative State Machine**. 

It uses a lightweight tracking file (`STATE.md` or `.agents/state.json` in the workspace root) to checkpoint progress, enforce explicit human gates, and allow step-by-step iterations:

```
✅ PHASE-GATED ITERATIVE EXECUTION (State Machine Pattern)

[Invoke Meta-Skill] 
       │
       ▼
┌──────────────┐      Gate 1 Check      ┌─────────────────────────────────┐
│ TDL Phase 1  │ ─── (Human Sign-off) ──▶│ "PRD & baseline_kpis APPROVED?" │
└──────────────┘                         └────────────────┬────────────────┘
                                                          │ YES
                                                          ▼
                                                ┌──────────────────┐
                                                │   TDL Phase 2    │
                                                └──────────────────┘
```

---

## 🔄 How a Phase-Gated Meta-Skill Operates in Practice

### Step 1: State Inspection
When you type `tdl-field-guide`, the meta-skill inspects the repository's `STATE.md` file:
```markdown
# Current Engagement State
- Engagement: Customer X Multimodal Concierge
- Current Phase: Phase 1 (Discover & Define)
- Status: PRD Drafted. Pending Synthetic Baseline Audit.
```

### Step 2: Single-Phase Execution
The agent executes **only** the active tasks for Phase 1 (running `workshop-intake`, capturing `baseline_kpis.json`, and writing `create-prd`).

### Step 3: Hard Stop & Gate Evaluation
The agent **stops execution** and presents a clear Gate Review to the TDL / User:

> ✋ **PHASE 1 GATE CHECK**
> * PRD generated: `docs/PRD.md`
> * Baseline captured: `baseline_kpis.json` (50 samples audited)
> 
> **Action Required**: Please review `docs/PRD.md` with the client SME. 
> * Reply **"Approved"** to advance `STATE.md` to Phase 2 (Architecture & InfoSec).
> * Or reply with feedback to iterate on Phase 1 requirements.

### Step 4: Resumable Transition
When you reply *"Approved"*, the agent updates `STATE.md` to `Phase 2: Prototype & Validate` and transitions its context to architecture grilling (`grill-with-docs`) and threat modeling (`threat-model-analyst`).

---

## 🎯 Summary Conclusion

Packaging everything under a Meta-Skill does **NOT** mean running it in one shot. 

A Meta-Skill acts as the **Governor & Memory**:
1. It knows the **Master Blueprint** (the 4 TDL phases or 7 E2E phases).
2. It knows **Where You Are** (`STATE.md`).
3. It enforces **Human-in-the-Loop Gates** before allowing the project to advance.
