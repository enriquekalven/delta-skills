---
name: execute-review-revise
description: Execute-Review-Revise workflow. Executes the task using the primary model (Gemini 3.6 Flash), classifies complexity to route review to Opus tier (simple) or Claude Fable 5 tier (complex), and revises the solution based on peer review critique. Use when asked to execute with automated review and revision, run two-pass coding, or execute first then review with Opus/Fable and revise.
---

# Execute-Review-Revise Workflow

## Overview

The **Execute-Review-Revise** skill enforces a high-assurance, multi-model engineering pipeline. It guarantees that every implementation is executed immediately, subjected to automated multi-model peer review, and refined prior to final delivery.

> [!CAUTION]
> **Prerequisite**: Ensure **Vertex AI Model Garden** is enabled in your GCP project for Anthropic Claude models (Opus 5 & Fable 5 tiers) prior to running this skill.


```
                   ┌────────────────────────────────────────┐
                   │  Phase 1: Baseline Execution          │
                   │  (Primary Model: Gemini 3.6 Flash)     │
                   └───────────────────┬────────────────────┘
                                       │
                                       ▼
                   ┌────────────────────────────────────────┐
                   │  Phase 2: Complexity Triage            │
                   └───────────┬────────────────┬───────────┘
                               │                │
                    Simple     │                │ Complex
                   ┌───────────▼───┐        ┌───▼───────────┐
                   │ Opus Tier     │        │ Fable 5 Tier  │
                   │ Reviewer      │        │ Reviewer      │
                   └───────────┬───┘        └───┬───────────┘
                               │                │
                               └────────┬───────┘
                                        │
                                        ▼
                   ┌────────────────────────────────────────┐
                   │  Phase 3: Peer Review Critique         │
                   └───────────────────┬────────────────────┘
                                       │
                                       ▼
                   ┌────────────────────────────────────────┐
                   │  Phase 4: Revision & Polish           │
                   │  (Primary Model Refinement)            │
                   └────────────────────────────────────────┘
```

---

## Workflow Phases & Protocol

### Phase 1: Baseline Execution (Primary Model)

1. **Immediate Execution**: Using the active default model (Gemini 3.6 Flash / default Google model), implement the user's requested feature, bug fix, or refactor completely in the workspace.
2. **Functional Verification**: Run local tests or syntax checks to ensure the initial baseline builds, runs, and satisfies basic requirements.
3. **Completion Criterion**: Baseline code written to workspace with no initial runtime or syntax errors.

---

### Phase 2: Complexity Triage & Model Assignment

Evaluate the baseline solution against the complexity criteria to select the reviewer model tier:

| Complexity Level | Characteristics | Designated Reviewer |
|---|---|---|
| **Simple Coding** | • Single file or isolated utility function<br>• Localized bug fix or refactor<br>• Straightforward script or component | **Opus Tier Reviewer**<br>*(Anthropic Claude Opus / High-Precision Code Reviewer)* |
| **Complex Use Case** | • Multi-file architectural changes<br>• State management or concurrency<br>• Security-sensitive boundaries, API design, or complex algorithms | **Claude Fable 5 Tier Reviewer**<br>*(Claude Fable 5 / Top-Tier Complex Reasoning Reviewer)* |

**Completion Criterion**: Task explicitly categorized as `Simple` or `Complex`, with reviewer persona/model identified.

---

### Phase 3: Multi-Model Peer Review

Spawn a review subagent (or execute a dedicated review loop) using the designated reviewer tier.

#### Reviewer Subagent Prompt Directive
The reviewer subagent must inspect the baseline implementation against five core axes:

1. **Logic & Bug Detection**: Are there edge cases, race conditions, type misalignments, or off-by-one errors?
2. **Code Quality & Simplicity**: Is there unnecessary complexity, redundant abstraction, or violation of codebase conventions?
3. **Performance & Scalability**: Are there unnecessary allocations, inefficient loops, or missing caching opportunities?
4. **Security & Hardening**: Are input validation, authorization, data sanitization, and error handling properly implemented?
5. **Test Completeness**: Does the code handle unexpected inputs or external failures gracefully?

#### Expected Review Report Format
The reviewer must output:
```markdown
### Peer Review Report
- **Reviewer Tier**: [Opus Tier | Fable 5 Tier]
- **Complexity Assessment**: [Simple | Complex]
- **Overall Verdict**: [APPROVED | NEEDS_REVISION]

#### Key Findings & Critique:
1. [Critical / Major / Minor] Description of issue or improvement opportunity
2. ...

#### Recommended Diffs / Revisions:
- Specific code blocks or architectural changes recommended.
```

**Completion Criterion**: Review report produced with actionable findings or explicit approval.

---

### Phase 4: Revision & Polish (Primary Model)

1. **Critique Synthesis**: Read the reviewer report generated in Phase 3.
2. **Targeted Refinement**: Apply all valid corrections, performance improvements, and simplifications to the code in the workspace.
3. **Re-Verification**: Re-test or verify the revised implementation to ensure no regressions were introduced.
4. **Final Summary Delivery**: Present the final revised solution to the user, highlighting:
   - Initial implementation key points
   - Reviewer tier used & findings
   - Revisions applied

**Completion Criterion**: Revised code applied in workspace, passed verification, and reported to user.

---

## Detailed Review Rubric

For detailed criteria used by the Opus and Fable reviewer tiers, refer to [review_rubric.md](references/review_rubric.md).
