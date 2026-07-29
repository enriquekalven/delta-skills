---
name: e2e-delivery-workflow
description: >
  End-to-end master software engineering workflow orchestrator across the complete 7-phase delivery lifecycle.
  Enforces dynamic capability slots, state regression loops, and phase-gated execution.
  Triggers on: "e2e workflow", "deliver project end to end", "e2e delivery", "run full delivery workflow", "end to end software lifecycle".
---

# End-to-End Software Delivery Workflow

Orchestrate customer software projects across a 7-phase software engineering lifecycle.

---

## Orchestration Rules

1. **State Machine Enforcement**: Read and update `STATE.md` in the workspace root. Execute one phase per step and wait for explicit gate approval before advancing.
2. **Capability Slot Resolution**: Resolve runtime capability slots (e.g. `#CAPABILITY: PRD-Creation`) via plugin registry lookups rather than hardcoding static paths.
3. **Rollback Loops**: Execute explicit state rollbacks (e.g. `ACTION: ROLLBACK_TO_PHASE_3`) when verification or audits identify architectural or intent gaps.

---

## 7-Phase Delivery Pipeline

```
[Read STATE.md] --> [Resolve Capability Slots] --> [Execute Phase Tasks] --> [Gate Approval Check] --> [Advance State]
```

### Phase 1: Idea Refinement & Solution Scoping
* **Capabilities**: `#CAPABILITY: Idea-Refinement` (`idea-refine`), `#CAPABILITY: Opportunity-Mapping` (`opportunity-solution-tree`), `#CAPABILITY: Pretotyping` (`brainstorm-experiments-new`).
* **Gate Check**: Present solution options and pretotype hypothesis. Require explicit approval before advancing.

### Phase 2: Requirements, SOW, and PRD Creation
* **Capabilities**: `#CAPABILITY: PRD-Creation` (`create-prd`), `#CAPABILITY: Red-Teaming` (`strategy-red-team`), `#CAPABILITY: Metrics-Design` (`metrics-dashboard`).
* **Gate Check**: Present PRD detailing explicit Goals and Non-Goals. Require SOW sign-off before advancing.

### Phase 3: Technical Architecture & System Design
* **Capabilities**: `#CAPABILITY: GCP-Architecture-Advisor` (`gcp-agent-architecture-advisor`), `#CAPABILITY: Architecture-Grilling` (`grill-with-docs`), `#CAPABILITY: API-Design` (`api-and-interface-design`), `#CAPABILITY: InfoSec-Threat-Modeling` (`threat-model-analyst`).
* **Gate Check**: Present Architecture Recommendation (`docs/ARCHITECTURE_RECOMMENDATION.md`), ADRs, `CONTEXT.md`, and STRIDE threat matrix. Require InfoSec sign-off before advancing.

### Phase 4: Task Breakdown & Iteration Planning
* **Capabilities**: `#CAPABILITY: Task-Breakdown` (`planning-and-task-breakdown`), `#CAPABILITY: Ticket-Splitting` (`to-tickets`), `#CAPABILITY: Pre-Mortem` (`pre-mortem`).
* **Gate Check**: Present prioritized backlog and dependency graph. Require sprint commitment before advancing.

### Phase 5: Incremental Implementation & TDD
* **Capabilities**: `#CAPABILITY: Vertical-Slicing` (`incremental-implementation`), `#CAPABILITY: TDD` (`test-driven-development`), `#CAPABILITY: Source-Grounding` (`source-driven-development`).
* **Gate Check**: Present passing unit test suite and committed vertical slices. Require code review before advancing.

### Phase 6: QA, Chaos Simulation, & Verification Gate
* **Capabilities**: `#CAPABILITY: Intent-Audit` (`intended-vs-implemented`), `#CAPABILITY: Security-Hardening` (`security-and-hardening`), `#CAPABILITY: Code-Review` (`code-review-and-quality`), `#CAPABILITY: Agent-Evaluation` (`google-agents-cli-eval`).
* **Regression Loop**: If intent audits identify architectural drift, write `ACTION: ROLLBACK_TO_PHASE_3` to `STATE.md`.
* **Gate Check**: Present intent gap audit report and regression test scores. Require release approval before advancing.

### Phase 7: Production Deployment & Artifact Handoff
* **Capabilities**: `#CAPABILITY: Release-Launch` (`shipping-and-launch`), `#CAPABILITY: Handoff-Artifacts` (`shipping-artifacts`), `#CAPABILITY: Cloud-Deploy` (`google-agents-cli-deploy`), `#CAPABILITY: Release-Notes` (`release-notes`).
* **Gate Check**: Present production release status, telemetry dashboards, and handoff documentation packet.
