# Bayesian Updating & Confidence Tracking

Track confidence as evidence accumulates. This is not statistical hypothesis testing—it's belief updating.

## Core Concept

```
Posterior Confidence = Prior Confidence + Evidence
```

You start with an initial belief (prior), gather evidence, update your belief (posterior), and repeat.

## Example: Does Enterprise Market Pay $50K/Year?

```
HYPOTHESIS: Enterprise customers will pay $50K/year for platform

Prior confidence: 40% (based on TAM analysis + expert opinion)

Evidence gathered:
  1. Customer interviews (10 CIOs):
     → 8/10 say they'd consider platform
     → Confidence shift: 40% → 55%
     → Why: Qualitative validation but small sample

  2. Pricing survey (50 prospects):
     → 6/20 would actually pay $50K
     → (others prefer lower price or don't value enough)
     → Confidence shift: 55% → 60%
     → Why: Stated willingness ≠ actual behavior; only 30% conversion

  3. Pilot with 3 customers:
     → 2/3 committed to $50K contracts
     → 1/3 negotiated down to $35K
     → Confidence shift: 60% → 72%
     → Why: Real purchase behavior stronger than stated; 67% at full price

Current confidence: 72% (enough to proceed to sales pilot, but not to full go-to-market)

Remaining doubt:
  → Large-deal sales cycle may be 6+ months (affects payback)
  → Competitors may undercut on price
  → Implementation complexity may slow customer adoption

Next evidence needed:
  → 5-customer sales cycle (moves confidence to 85%)
  → Win-loss analysis with lost deals
  → Competitive response tracking
```

## Decision Points by Confidence

| Confidence | Status | Action |
|---|---|---|
| **≥ 80%** | VALIDATED | Proceed with confidence. Scale the strategy. Document assumptions as validated. Plan next phase. |
| **60-80%** | PARTIALLY VALIDATED | Proceed but build contingencies. Continue targeted tests on remaining doubts. Monitor early indicators closely. |
| **40-60%** | UNCERTAIN | Core value prop or customer segment needs rework. Redesign based on learnings. Retest. |
| **< 40%** | NOT VALIDATED | This hypothesis is unlikely to be true. Kill it or pivot fundamentally. Reallocate resources. |

## Kill / Continue / Pivot Decision Framework

When hypothesis testing is complete:

```
Confidence ≥ 80%
  ├─ CONTINUE: This assumption is validated. Proceed with strategy.
  └─ Action: Schedule follow-on validation at scale. Document as validated.

Confidence 60-80%
  ├─ CONTINUE WITH CONDITIONS: Assume is likely true but not certain.
  └─ Action: Proceed but build contingencies. Run targeted tests on remaining doubts.
  └─ Example: "We believe market will adopt at $50K, but we'll offer $40K option as fallback"

Confidence 40-60%
  ├─ PIVOT: Core element needs rework before proceeding.
  └─ Action: Redesign based on learnings (value prop, segment, channel). Retest.
  └─ Example: "Market doesn't perceive $50K value. Pivot to $30K price point with limited features."

Confidence < 40%
  ├─ KILL: This hypothesis is unlikely to be true. Stop pursuing this strategy.
  └─ Action: Reallocate resources. Document learning. Find new opportunity.
  └─ Example: "Enterprise market doesn't have urgent need for this. Pivot to SMB market."
```

## Tracking Confidence Over Time

Create a confidence matrix to track all strategic hypotheses:

```
HYPOTHESIS CONFIDENCE TRACKER
═════════════════════════════════════════════════════════════════
Hypothesis                                Prior  Q1    Q2    Q3    Q4   Status
─────────────────────────────────────────────────────────────────────────────
Market: Enterprise will pay $50K/year      40%   55%   72%   80%   85%   ✓ VALIDATED
Product: Customers adopt for daily use     45%   50%   65%   70%   75%   ⚠ PROCEEDING
Pricing: Elasticity favorable at $50K      35%   45%   58%   65%   72%   ⚠ PROCEEDING
Channel: Sales can acquire at $200 CAC     50%   60%   70%   78%   82%   ✓ VALIDATED
Retention: 85% annual retention            40%   50%   60%   68%   72%   ⚠ PROCEEDING
```

## Common Pitfalls to Avoid

### 1. Anchoring to Prior Confidence

**Problem:** You start at 40% confident; after one positive signal, you say "we're 80% confident."

**Better approach:** Evidence moves confidence incrementally. First evidence moves 40% → 55%. Second evidence moves 55% → 65%. Build gradually.

### 2. Confirmation Bias

**Problem:** You find evidence supporting your hypothesis and ignore contradicting evidence.

**Better approach:** Weight contradicting evidence heavily. If 80% say "yes" but 20% say "no" with strong reasoning, that 20% might be more important.

### 3. Overweighting Recent Evidence

**Problem:** Latest test shows negative result; you drop confidence from 70% → 30% (ignoring prior evidence).

**Better approach:** Integrate new evidence with prior. If 3 prior tests supported hypothesis but 1 recent test didn't, confidence might drop 70% → 55% (not to 30%).

### 4. Premature Scaling

**Problem:** Confidence is 60% but you launch full go-to-market.

**Better approach:** Confidence 60-80% = proceed with conditions, build contingencies, test on smaller scale first.

## Bayesian Updating in Practice

Each test result updates your confidence. Track these formally:

```
Test 1: Customer interviews
  Finding: 8/10 mention core problem; 7/10 willing to try
  Interpretation: Problem resonates; needs solution
  Confidence update: 40% → 55%

Test 2: Pricing survey
  Finding: Only 30% would pay target price
  Interpretation: Price might be too high; segment might not value enough
  Confidence update: 55% → 58% (slight downward revision)

Test 3: MVP with 50 users
  Finding: 65% Day-7 retention (target was 60%); strong NPS feedback
  Interpretation: Product resonates; core value prop validated
  Confidence update: 58% → 75% (significant upward revision)
```

At the end, you have clear confidence levels for each hypothesis, which feed directly into your next strategic phase.
