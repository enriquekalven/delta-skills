---
name: strategy-partner-orchestrator
description: >
  Diagnose strategic business problems with a MECE issue tree, score options with a weighted
  decision matrix, and produce a resource-loaded 90-day execution plan in docs/STRATEGY_BRIEF.md.
  Trigger when asked to frame an executive decision, diagnose stalled growth or margin compression,
  or coordinate ai-native-strategy and financial-strategy. Do NOT trigger for single-feature PRDs
  (use product-md) or process swimlanes (use business-process-redesign).
metadata:
  author: rcfaris@
  version: '3.0'
---

# Strategy Partner Orchestrator

This skill turns an ambiguous strategic problem into a single concrete decision document (`docs/STRATEGY_BRIEF.md`) across three phases: **Diagnosis → Decision Framing → 90-Day Execution Plan**.

---

## Operating Rules

1. **Evidence & Confidence Tags:** Tag every material claim `[HIGH]` (verified internal/public data), `[MEDIUM]` (triangulated benchmark), or `[LOW]` (unverified assumption). Never base a final recommendation on `[LOW]` claims without an explicit validation gate.
2. **Baseline-Then-Differentiate:** When comparing options or competitors, state:
   - **Baseline:** What is true across all options?
   - **Differentiation:** What separates each option quantitatively?
   - **Implication:** What decision follows from that gap?
3. **Recommend One Path:** Present 2–3 distinct options (including status quo), score them in a weighted matrix, and commit to one recommendation with explicit trade-offs and kill conditions.

---

## Procedure

### Phase 1: MECE Diagnosis
1. Define the governing question in one sentence (e.g., *"Why did enterprise Net Revenue Retention drop 14 percentage points in FY25, and how do we recover to 118% within 12 months?"*).
2. Decompose the problem into 2–4 mutually exclusive, collectively exhaustive (MECE) Level-1 branches and testable Level-2 hypotheses using [mece-issue-tree.md](references/mece-issue-tree.md).
3. Quantify the magnitude of each branch (`$` or `%` contribution to the gap) so analysis focuses on the largest driver first.

### Phase 2: Decision Framing & Option Scoring
1. Formulate 3 genuinely distinct strategic options (Option A, Option B, Option C / Status Quo).
2. Score each option (1–10) against explicit weighted criteria (Strategic Fit, Time-to-Value, Implementation Feasibility, Capital Efficiency, Risk-Adjusted Return) following [strategy-synthesis.md](references/strategy-synthesis.md).
3. Delegate deeper domain work when needed:
   - AI build/buy/partner, model unit economics, or agent architecture → [ai-native-strategy](../ai-native-strategy/SKILL.md)
   - P&L diagnostics, LTV/CAC unit economics, or NPV/IRR modeling → [financial-strategy](../financial-strategy/SKILL.md)

### Phase 3: 90-Day Execution Plan & Pre-Mortem
1. Write a resource-loaded 90-day implementation plan (workstreams, FTEs, budget, owners, Day-30 gate).
2. Define 2–3 measurable **Kill Conditions** (exact metric threshold + date that triggers a pivot or halt).
3. Write the final deliverable to `docs/STRATEGY_BRIEF.md`.

---

## Deliverable Template (`docs/STRATEGY_BRIEF.md`)

```markdown
# Strategy Brief: <Title>
Date: <YYYY-MM-DD> | Sponsor: <Role> | Confidence: <HIGH | MEDIUM | LOW>

## 1. Governing Question & Bottom Line
- **Question:** <1 sentence>
- **Recommendation:** <1-2 sentences stating chosen option, investment, and expected outcome>

## 2. MECE Diagnostic Issue Tree
- **L1 Branch A (Priority — <X%> of gap):** <Hypothesis + evidence + [H/M/L]>
  - L2.1: <Sub-hypothesis + metric>
  - L2.2: <Sub-hypothesis + metric>
- **L1 Branch B (<Y%> of gap):** <Hypothesis + evidence + [H/M/L]>

## 3. Strategic Options & Weighted Decision Matrix
| Criterion | Weight | Option A | Option B | Option C (Status Quo) |
|---|---|---|---|---|
| Strategic Fit | 25% | | | |
| Time-to-Value | 20% | | | |
| Implementation Feasibility | 20% | | | |
| Capital Efficiency | 15% | | | |
| Risk-Adjusted Return | 20% | | | |
| **Weighted Score** | **100%** | | | |

## 4. 90-Day Resource-Loaded Execution Plan
| Workstream | Days 1-30 | Days 31-60 | Days 61-90 | FTE / Budget | Owner |
|---|---|---|---|---|---|

## 5. Risks, Assumptions & Kill Conditions
| Item | Type (Risk / Assumption / Kill Condition) | Threshold / Trigger | Action if Triggered |
|---|---|---|---|
```

---

## References & Examples

- [MECE Issue Tree Builder](references/mece-issue-tree.md): Diagnostic, solution, and evaluation tree patterns.
- [Strategy Synthesis & Weighted Decision Matrix](references/strategy-synthesis.md): Option scoring, stakeholder impact, and pre-mortem checklist.
- [Worked Example: B2B SaaS Support & Retention Turnaround](examples/cloud-migration-strategy-brief.md): Complete `docs/STRATEGY_BRIEF.md` artifact showing MECE diagnosis, weighted option scoring, 90-day execution plan, and kill conditions.
