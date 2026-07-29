# End-to-End Customer Project Delivery Workflow

This document details the 7-phase software delivery workflow mapping skill capability slots to open-source repository packages.

---

## Skill Source Repositories
* **[Delta Meta-Skills]** = [enriquekalven/delta-skills](https://github.com/enriquekalven/delta-skills)
* **[PM]** = [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
* **[MP]** = [mattpocock/skills](https://github.com/mattpocock/skills)
* **[AO]** = [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
* **[G]** = [google/agents-cli](https://github.com/google/agents-cli)

---

## Orchestration Model
To execute the 7-phase workflow using state-gated tracking (`STATE.md`) with dynamic capability slots and rollback loops:
```bash
"Let's run e2e-delivery-workflow for this project."
```

---

## E2E Project Lifecycle Pipeline

```mermaid
graph TD
    A["Phase 1: Idea Refinement & Solution Scoping"] --> B["Phase 2: Requirements, SOW, and PRD Creation"]
    B --> C["Phase 3: Technical Architecture & System Design"]
    C --> D["Phase 4: Task Breakdown & Iteration Planning"]
    D --> E["Phase 5: Incremental Implementation & TDD"]
    E --> F["Phase 6: QA, Chaos Simulation, & Verification Gate"]
    F --> G["Phase 7: Production Deployment & Artifact Handoff"]

    F -. "State Regression Rollback" .-> C
```

---

## Phase Capability Resolution

### Phase 1: Idea Refinement & Solution Scoping
* **Capability Slots**: `#CAPABILITY: Idea-Refinement`, `#CAPABILITY: Opportunity-Mapping`, `#CAPABILITY: Pretotyping`
* **Resolved Skills**:
  * **[`idea-refine`](https://github.com/addyosmani/agent-skills/tree/main/skills/idea-refine)** [AO] — Structured problem exploration.
  * **[`opportunity-solution-tree`](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/opportunity-solution-tree)** [PM] — Outcome-to-feature mapping.
  * **[`brainstorm-experiments-new`](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/brainstorm-experiments-new)** [PM] — Pretotyping and hypothesis validation.

### Phase 2: Requirements, SOW, and PRD Creation
* **Capability Slots**: `#CAPABILITY: PRD-Creation`, `#CAPABILITY: Red-Teaming`, `#CAPABILITY: Metrics-Design`
* **Resolved Skills**:
  * **[`create-prd`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/create-prd)** [PM] — PRD specification with explicit Goals and Non-Goals.
  * **[`spec-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/spec-driven-development)** [AO] — Interface & spec constraints.
  * **[`strategy-red-team`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/strategy-red-team)** [PM] — Risk assessment on key assumptions.

### Phase 3: Technical Architecture & System Design
* **Capability Slots**: `#CAPABILITY: Architecture-Grilling`, `#CAPABILITY: API-Design`, `#CAPABILITY: InfoSec-Threat-Modeling`
* **Resolved Skills**:
  * **[`grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)** [MP] — Architecture review producing ADRs & `CONTEXT.md`.
  * **[`api-and-interface-design`](https://github.com/addyosmani/agent-skills/tree/main/skills/api-and-interface-design)** [AO] — Module boundaries & API contracts.
  * **[`google-agents-cli-adk-code`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-adk-code)** [G] — ADK Python architecture patterns.

### Phase 4: Task Breakdown & Iteration Planning
* **Capability Slots**: `#CAPABILITY: Task-Breakdown`, `#CAPABILITY: Ticket-Splitting`, `#CAPABILITY: Pre-Mortem`
* **Resolved Skills**:
  * **[`planning-and-task-breakdown`](https://github.com/addyosmani/agent-skills/tree/main/skills/planning-and-task-breakdown)** [AO] — Task decomposition.
  * **[`to-tickets`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets)** [MP] — Task dependency graphing.
  * **[`pre-mortem`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/pre-mortem)** [PM] — Failure mode risk classification.

### Phase 5: Incremental Implementation & TDD
* **Capability Slots**: `#CAPABILITY: Vertical-Slicing`, `#CAPABILITY: TDD`, `#CAPABILITY: Source-Grounding`
* **Resolved Skills**:
  * **[`incremental-implementation`](https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation)** [AO] — Vertical slicing.
  * **[`test-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/test-driven-development)** [AO/MP] — Red-Green-Refactor logic.
  * **[`source-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/source-driven-development)** [AO] — Documentation-grounded code generation.

### Phase 6: QA, Chaos Simulation, & Verification Gate
* **Capability Slots**: `#CAPABILITY: Intent-Audit`, `#CAPABILITY: Security-Hardening`, `#CAPABILITY: Code-Review`, `#CAPABILITY: Agent-Evaluation`
* **Resolved Skills**:
  * **[`intended-vs-implemented`](https://github.com/phuryn/pm-skills/tree/main/pm-ai-shipping/skills/intended-vs-implemented)** [PM] — Audit intent vs code implementation.
  * **[`security-and-hardening`](https://github.com/addyosmani/agent-skills/tree/main/skills/security-and-hardening)** [AO] — Security boundary controls.
  * **[`code-review-and-quality`](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality)** [AO/MP] — Multi-axis code review.
  * **[`google-agents-cli-eval`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-eval)** [G] — Evaluation regression suites.
* **Regression Loop**: If intent audits identify architectural drift, write `ACTION: ROLLBACK_TO_PHASE_3` to `STATE.md`.

### Phase 7: Production Deployment & Artifact Handoff
* **Capability Slots**: `#CAPABILITY: Release-Launch`, `#CAPABILITY: Handoff-Artifacts`, `#CAPABILITY: Cloud-Deploy`
* **Resolved Skills**:
  * **[`shipping-and-launch`](https://github.com/addyosmani/agent-skills/tree/main/skills/shipping-and-launch)** [AO] — Deployment & rollback manifests.
  * **[`shipping-artifacts`](https://github.com/phuryn/pm-skills/tree/main/pm-ai-shipping/skills/shipping-artifacts)** [PM] — Handoff documentation (`architecture.md`, `flows.md`, `variables.md`).
  * **[`google-agents-cli-deploy`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-deploy)** & **[`publish`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-publish)** [G] — Deployment to Cloud Run/GKE and registry indexing.
