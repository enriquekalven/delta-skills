---
name: claude-review
description: Two-pass coding and review workflow. Executes the task using the primary model (Gemini 3.6 Flash), classifies complexity to route review to the ZDR-compliant Opus 5 tier, and revises the solution based on peer review critique. Use when asked to execute with automated Claude review and revision, run two-pass coding, use claude-review, or execute first then review with Opus 5 and revise.
---

# Claude Review Workflow (`claude-review`)

## Overview

The **Claude Review** (`claude-review`) skill enforces a high-assurance, multi-model engineering pipeline. It guarantees that every implementation is executed immediately, subjected to automated peer review using Zero Data Retention (ZDR) compliant Claude models (Opus 5), and refined prior to final delivery.

> [!CAUTION]
> **Compliance & Data Retention Requirement**:
> Only Zero Data Retention (ZDR) models (e.g. **Opus 5**) are authorized. Fable 5 has a **30-day data retention policy** and is **STRICTLY PROHIBITED** under corporate Google accounts and customer data. Ensure **Vertex AI Model Garden** is enabled in your GCP project for Opus 5 prior to running this skill.

```
                   ┌────────────────────────────────────────┐
                   │  Phase 1: Baseline Execution          │
                   │  (Primary Model: Gemini 3.6 Flash)     │
                   └───────────────────┬────────────────────┘
                                       │
                                       ▼
                   ┌────────────────────────────────────────┐
                   │  Phase 2: Review Routing (Opus 5 ZDR)  │
                   └───────────────────┬────────────────────┘
                                       │
                                       ▼
                   ┌────────────────────────────────────────┐
                   │  Phase 3: Peer Review Critique         │
                   │  (Opus 5 Tier Reviewer)                │
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

### Phase 2: Reviewer Routing (Opus 5 ZDR)

Route the baseline solution to the Zero Data Retention (ZDR) compliant Opus 5 reviewer:

| Complexity Level | Designated Reviewer | Compliance Status |
|---|---|---|
| **All Coding & System Tasks** | **Opus 5 Tier Reviewer**<br>*(Anthropic Claude Opus / ZDR High-Precision Reviewer)* | **AUTHORIZED** (Zero Data Retention) |
| **Non-ZDR Models (Fable 5)** | N/A | **PROHIBITED** (30-day data retention violation) |

**Completion Criterion**: Task routed to ZDR-compliant Opus 5 reviewer persona.

---

### Phase 3: Multi-Model Peer Review (Model Garden API Execution)

To obtain the live peer review critique from Opus 5 on Vertex AI Model Garden, execute the helper script via `run_command`:

```bash
python3 skills/claude-review/scripts/call_opus_model_garden.py "Please review the baseline implementation in <target_file> against logic bugs, edge cases, thread safety, and code simplicity."
```

#### Reviewer Prompt Directive
The Opus 5 Model Garden API response will inspect the baseline implementation against five core axes:

1. **Logic & Bug Detection**: Are there edge cases, race conditions, type misalignments, or off-by-one errors?
2. **Code Quality & Simplicity**: Is there unnecessary complexity, redundant abstraction, or violation of codebase conventions?
3. **Performance & Scalability**: Are there unnecessary allocations, inefficient loops, or missing caching opportunities?
4. **Security & Hardening**: Are input validation, authorization, data sanitization, and error handling properly implemented?
5. **Test Completeness**: Does the code handle unexpected inputs or external failures gracefully?

#### Expected Review Report Format
The reviewer must output:
```markdown
### Peer Review Report
- **Reviewer Tier**: Opus 5 Tier (ZDR Compliant)
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

For detailed criteria used by the Opus 5 reviewer tier, refer to [review_rubric.md](references/review_rubric.md).
