# Mixture of Experts: Financial Review Panel

Every significant financial analysis should be reviewed by a panel of five financial experts who each bring a different lens, ask different questions, and have different standards. This document defines the panel, their expertise, their review process, and synthesis rules.

---

## The Five Experts

### Expert 1: Public Company CFO

**Background:** 15+ years as CFO at public companies (F500 or growth IPO), responsible for GAAP financial reporting, board/investor relations, Sarbanes-Oxley compliance, earnings guidance, capital structure.

**Lens:** Financial rigor, reporting credibility, investor-grade quality, governance, risk management

**Primary Questions:**
- Is the financial narrative bulletproof? Would it withstand investor or analyst scrutiny?
- Are accounting treatments defensible under GAAP? Any aggressive assumptions?
- What are the audit/compliance implications?
- Is the guidance conservative enough to be credible without being pessimistic?
- What could cause restatement or audit issue?

**Scoring Criteria (out of 5):**
- **5:** Financial analysis is investor-ready; no material risks; assumptions conservative and well-documented
- **4:** Analysis is solid; minor items to tighten; ready for board with caveats noted
- **3:** Analysis is usable but has gaps; needs quality improvements before external use
- **2:** Analysis has material issues; assumptions weak or aggressive; needs significant rework
- **1:** Analysis is not credible; fundamental flaws; do not use for external communication

**Hard Stops:**
- ❌ Aggressive revenue recognition (front-loading, not conservative)
- ❌ Unrealistic margin or cash flow assumptions presented without downside scenario
- ❌ Covenant calculations that don't match actual debt documents
- ❌ Projections beyond forecast period without explicit "terminal value" assumptions

**Typical Critique:**
"Your NPV analysis assumes 15% margins by Year 5. That would put us in the top 5% of the industry. I need to see (a) what specific actions drive margin expansion, and (b) downside case where we get only 50% of planned expansion. As written, guidance is too optimistic for an SEC filing."

---

### Expert 2: FP&A Director

**Background:** 10+ years as FP&A Director / VP, responsible for monthly/quarterly forecasting, variance analysis, rolling forecasts, driver-based models, operational metrics, cross-functional planning.

**Lens:** Modeling precision, operational reality, actuals-vs-forecast reconciliation, driver architecture, execution feasibility

**Primary Questions:**
- Are the revenue drivers sound? Based on actual sales pipeline, customer flow, capacity?
- Does the cost model match how the company actually operates?
- Are headcount plans aligned with revenue ramp?
- Do the monthly assumptions (how you get to annual) make sense?
- Are you missing any fixed cost step-functions (you can't hire 0.5 people)?

**Scoring Criteria (out of 5):**
- **5:** Model is operationally sound; driver architecture matches how business actually runs; could guide monthly execution
- **4:** Model is solid with one or two refinements; ready for planning use
- **3:** Model is usable but has operational disconnects; needs adjustment before using for monthly planning
- **2:** Model has material operational flaws; assumes capabilities that don't exist; not aligned to how company actually runs
- **1:** Model is detached from reality; unusable for operational planning; do not reference for execution

**Hard Stops:**
- ❌ Sales forecast assumes X% conversion rate with no pipeline data to support it
- ❌ Headcount plan doesn't step-function cost (assumes continuous fractional hiring)
- ❌ Working capital assumptions don't match historical DSO/DIO/DPO by 20%+
- ❌ Revenue assumes "catch-up" in Q4 without explaining how that happens operationally

**Typical Critique:**
"Your Q4 revenue assumes we close $XXM in deals, but your sales team has closed $XXM total in last 4 quarters. Where does the $XXM come from? New team? New market? Better win rate? You need to build this from actual pipeline, not from 'we need this number to hit guidance.'"

---

### Expert 3: PE/VC Investor

**Background:** 12+ years as investor (buyout fund, growth equity, early-stage VC), responsible for valuation, unit economics obsession, exits, return analysis, path to profitability, capital efficiency.

**Lens:** Unit economics obsession, capital efficiency, path to EBITDA/cash generation, exit scenarios, ROI, value drivers

**Primary Questions:**
- What is the unit economics story? Does every dollar of revenue produce positive contribution?
- What's the path to profitability or positive FCF? Is it realistic?
- If we invested in this strategy, what's our exit scenario in 5 years?
- Are we being capital-efficient? Could we achieve the same outcomes with less capital?
- Is the cash-to-outcome ratio attractive relative to alternatives?

**Scoring Criteria (out of 5):**
- **5:** Unit economics are healthy and improving; path to profitability is clear and capital-efficient; exit scenario is credible
- **4:** Unit economics support the plan; capital efficiency is reasonable; minor optimizations possible
- **3:** Unit economics are breakeven or marginal; capital plan is acceptable but not efficient; path to profitability needs clarification
- **2:** Unit economics are concerning; capital being deployed with low return; path to profitability unclear
- **1:** Unit economics are broken; capital is burning with no path to return; do not fund

**Hard Stops:**
- ❌ LTV/CAC < 2 (customers don't justify acquisition cost)
- ❌ Path to profitability is > 7 years out (too long, too uncertain)
- ❌ Cash needed exceeds likely capital available
- ❌ Unit economics projected to improve but no specific actions to drive improvement

**Typical Critique:**
"Your LTV/CAC is 2.5x, which is acceptable, but the assumption is that CAC stays at $XXX while we scale. Historically in your space, CAC increases 15-20% annually as you scale because you've already captured easy customers. If CAC increases 15%, your LTV/CAC drops to 1.8x in Year 3, which breaks the model. You need a specific plan to reduce CAC (improve product virality, optimize sales model) or the unit economics don't work at scale."

---

### Expert 4: Cost Transformation Consultant

**Background:** 12+ years optimizing cost structures (Big 4 consulting, internal transformation roles), zero-based budgeting, shared services, procurement, outsourcing, process automation.

**Lens:** Cost structure benchmarking, operating leverage, cost categorization, transformation feasibility, execution risk

**Primary Questions:**
- What is the cost structure versus industry benchmarks? Why is it different?
- Which costs are truly strategic vs. fixed vs. waste?
- Is the cost reduction roadmap realistic? What's the execution risk?
- Are there shared services or outsourcing opportunities being missed?
- Is the operating leverage assumption valid?

**Scoring Criteria (out of 5):**
- **5:** Cost structure is benchmarked and optimized; opportunities are clearly identified; transformation plan is realistic and achievable
- **4:** Cost structure is reasonable; identified savings are achievable; minor execution risks
- **3:** Cost structure is acceptable; transformation plan has execution challenges; confidence is moderate
- **2:** Cost structure appears unoptimized; transformation plan has material execution risk; savings may not be realized
- **1:** Cost structure is inefficient; transformation plan is unrealistic; do not rely on projected savings

**Hard Stops:**
- ❌ Assumes X% cost reduction without explaining how (headcount cuts are always mentioned last / after other levers)
- ❌ Predicts operating leverage without separating fixed from variable costs
- ❌ Plans outsourcing that would lose critical IP or capability
- ❌ Assumes cost reductions don't impact revenue (if you cut QA, what happens to defect rate and churn?)

**Typical Critique:**
"You assume OpEx declines from 50% to 40% of revenue through operating leverage, but your fixed cost is only 30% of total OpEx. That means you're expecting variable costs to decline X%, but your unit is already fairly efficient. The only way to get to 40% is headcount reduction, which you haven't planned for explicitly. Which teams are right-sizing? What's the execution risk if you don't hit the reduction?"

---

### Expert 5: Treasury / Investor Relations Specialist

**Background:** 10+ years managing treasury, debt relationships, capital markets, investor communication, cash management, covenant monitoring.

**Lens:** Cash management, capital structure, debt covenants, liquidity, communication with external stakeholders

**Primary Questions:**
- Is the cash projection realistic? Do we have enough liquidity headroom?
- Do we understand the covenant implications? What's our headroom?
- Is the capital structure optimal for the strategy?
- Could we have better debt terms if we communicated this differently to lenders?
- What does this financial strategy mean for credit rating (if public)?

**Scoring Criteria (out of 5):**
- **5:** Cash projection is sound; covenant headroom is comfortable; capital structure is appropriate; no liquidity risk
- **4:** Projection is solid; headroom is adequate; capital structure is reasonable with minor optimization possible
- **3:** Projection is acceptable; covenant headroom is tight; capital structure is acceptable but suboptimal
- **2:** Projection has liquidity risk; covenant headroom is concerning; capital structure may not support strategy
- **1:** Projection shows liquidity crisis; covenant breach risk is high; capital structure inadequate; do not fund without capital raise

**Hard Stops:**
- ❌ Covenant headroom < 10% (too tight, any variance causes breach)
- ❌ Assumes capital raise but no capital source identified
- ❌ Runway < 6 months and no financing plan in place
- ❌ Debt schedule doesn't match actual loan documents

**Typical Critique:**
"Your Year 2 cash projection shows $XXM ending balance, but your leverage covenant has maximum 3.5x Debt/EBITDA. Your Year 2 EBITDA is $XXM, which means you can have max $XXM debt. Your current debt is $XXM plus $XXM of debt raised in Year 1 = $XXM total. That puts you at 3.2x leverage, which is fine, but leaves no room for additional debt or EBITDA shortfall. If EBITDA misses by 10%, you hit covenant threshold. I'd recommend either (a) lower debt in Year 1 raise, or (b) negotiate covenant to 3.7x."

---

## Review Process

### Step 1: Panel Assembly & Framing (15 min)

Gather the five experts and frame the question:

```
PANEL BRIEFING
═══════════════════════════════════════════
Financial analysis under review: [Initiative name or question]
Decision being made: [What is this analysis informing?]
Key constraints: [Budget, timeline, governance]
Highest risk area: [What is the panel most concerned about?]

Time allocation: [Each expert gets X minutes to review analysis before panel discussion]
```

### Step 2: Individual Expert Review (45 min)

Each expert independently reviews the analysis and completes a scorecard:

```
EXPERT REVIEW SCORECARD
═══════════════════════════════════════════
Expert: [CFO / FP&A / Investor / Cost Consultant / Treasury]
Analysis: [Name]
Date: [Date]

SCORE: [1-5 scale as per expert criteria above]

TOP 3 STRENGTHS
  1. [What's well done?]
  2. [What's well done?]
  3. [What's well done?]

TOP 3 CONCERNS
  1. [What's problematic? How material is it?]
  2. [What's problematic?]
  3. [What's problematic?]

HARD STOP ISSUES (if any)
  ☐ [Does this hit a hard stop? If yes, explain why]
  ☐ [Any others?]

CRITICAL QUESTIONS FOR DISCUSSION
  1. [Question to be asked in panel discussion]
  2. [Question]
  3. [Question]

RECOMMENDATION
  ☐ APPROVE as-is
  ☐ APPROVE with revisions (specify)
  ☐ CONDITIONAL APPROVE (if conditions are met)
  ☐ REJECT (explain why)
```

### Step 3: Panel Synthesis Discussion (30 min)

Experts present findings and debate. The moderator (typically the Chief Financial Officer or Executive) facilitates:

```
PANEL DISCUSSION AGENDA
═══════════════════════════════════════════

Round 1: Individual Scores & Rationale (5 min each)
  CFO:        [Score and 1-minute summary of concerns]
  FP&A:       [Score and 1-minute summary of concerns]
  Investor:   [Score and 1-minute summary of concerns]
  Cost Cons:  [Score and 1-minute summary of concerns]
  Treasury:   [Score and 1-minute summary of concerns]

Round 2: Hard Stops & Dealbreakers (5 min)
  Any expert with a hard stop issue explains and defends

Round 3: Point of Disagreement (10 min)
  If experts disagree significantly on score, debate the issue
  Example: "CFO is concerned about aggressive margins, but Investor sees margins as achievable. Let's hear both sides."

Round 4: Synthesis & Recommendation (10 min)
  Moderator synthesizes: "The panel agrees on X, disagrees on Y. Here's how we're resolving it."
```

### Step 4: Final Verdict & Actions

The panel produces a consensus verdict:

```
PANEL VERDICT
═══════════════════════════════════════════

OVERALL RECOMMENDATION: [PASS / CONDITIONAL / REVISE / REJECT]

EXPERT BREAKDOWN
  CFO:                   [Pass / Conditional / Revise / Reject]
  FP&A:                  [Pass / Conditional / Revise / Reject]
  Investor:              [Pass / Conditional / Revise / Reject]
  Cost Consultant:       [Pass / Conditional / Revise / Reject]
  Treasury:              [Pass / Conditional / Revise / Reject]

KEY POINTS OF AGREEMENT
  • All experts agree on: [Key assumption or finding]
  • All experts agree on: [Key assumption or finding]

POINTS OF DISAGREEMENT & RESOLUTION
  • CFO concerned about [X], Investor believes [Y]. Resolution: [How we're breaking the tie]
  • Investor concerned about [X], Cost Consultant believes [Y]. Resolution: [How we're breaking the tie]

CRITICAL REVISIONS NEEDED BEFORE APPROVAL
  1. [What must be fixed? Non-negotiable]
  2. [What must be fixed?]
  3. [What must be fixed?]

CONDITIONAL APPROVALS (if not hard stops)
  1. [Condition]: [If [condition is met], we approve. If not, we revisit]
  2. [Condition]: [If this holds, analysis is good. If it doesn't, we need to reconsider]

APPROVED, BUT MONITOR
  • [Assumption or metric to track closely]
  • [Assumption or metric that has execution risk]
  • [Review trigger if [condition deteriorates]]

OWNER FOR REVISIONS
  [Who is accountable for incorporating feedback and re-presenting?]
  Timeline: [By when should revised analysis be ready?]
```

---

## Hard Stops vs. Issues vs. Nice-to-Haves

The panel must distinguish between:

```
ISSUE CLASSIFICATION
═══════════════════════════════════════════

HARD STOPS (Analysis fails — do not use)
  ❌ LTV/CAC < 1.5 (unit economics don't work)
  ❌ Covenant headroom < 5% (covenant breach risk is high)
  ❌ Margin assumptions are unjustified (no path specified)
  ❌ Revenue driver is disconnected from reality (not based on actual pipeline)
  ❌ Assumes capital availability with no source identified
  ❌ Analysis has mathematical errors (formula mistakes, reconciliation fails)

CRITICAL ISSUES (Must be fixed before approval)
  🔴 Operating leverage assumption needs to be stress-tested
  🔴 Headcount plan doesn't match revenue ramp
  🔴 Margin assumption is at industry extreme; needs sensitivity analysis
  🔴 Downside scenario shows cash negative; need mitigation plan
  🔴 Covenant calculation needs to be verified against actual debt docs

CONDITIONAL ISSUES (Can approve if condition is met)
  🟡 NPV is sensitive to churn assumption. Approve if [team commits to weekly churn monitoring]
  🟡 Assumes supplier pricing. Approve if [procurement completes negotiations by Month X]
  🟡 Assumes new capability hiring. Approve if [recruiting plan shows realistic timeline]

NICE-TO-HAVES (Could be better, but not blocking)
  🟢 Would benefit from sensitivity table (but NPV is clearly positive even in downside)
  🟢 Gross margin assumption is conservative; could be stated more boldly (but being conservative is fine)
  🟢 Should include competitor benchmarking (would strengthen narrative but not required)
```

---

## Synthesis Protocol

When experts disagree, here's the resolution process:

```
DISAGREEMENT RESOLUTION FRAMEWORK
═══════════════════════════════════════════

Scenario 1: One Expert Says "Reject," Others Say "Pass"
  → Moderator hears the single expert's concern in detail
  → If concern is a hard stop, the single expert wins (hard stops are veto)
  → If concern is not a hard stop, vote: majority wins
  → Document the dissent for the record

Scenario 2: Expert Scores Differ by 2+ Points (e.g., CFO says 3, Investor says 5)
  → Moderator asks: "What would it take for you to move to [middle ground]?"
  → If gap is about missing data, can it be sourced quickly? If yes, defer decision.
  → If gap is about different standards (CFO more conservative, Investor more optimistic):
     Moderator notes the disagreement, both scores stand, overall recommendation reflects range
     → "FP&A gives this 4/5 (operationally sound), CFO gives 3/5 (margins need more justification).
            Panel recommendation: CONDITIONAL on margin assumptions being tightened."

Scenario 3: Multiple Experts Cite Same Hard Stop
  → Analysis is rejected
  → If ≥ 3 experts cite the same hard stop, it's a veto
  → Recommend: revise and resubmit

GENERAL RULE: If ≥ 3 experts flag the same issue, it's a hard stop regardless of how it's classified.
```

---

## Output Template

```
MIXTURE OF EXPERTS REVIEW
═══════════════════════════════════════════

ANALYSIS UNDER REVIEW
[Name, owner, decision being informed]

EXPERT SCORECARD SUMMARY
CFO:                          [Score 1-5 and brief rationale]
FP&A Director:                [Score 1-5 and brief rationale]
PE/VC Investor:               [Score 1-5 and brief rationale]
Cost Transformation Consul:   [Score 1-5 and brief rationale]
Treasury/IR Specialist:       [Score 1-5 and brief rationale]

AVERAGE SCORE: [X/5]

PANEL CONSENSUS VERDICT
Recommendation: [PASS / CONDITIONAL / REVISE / REJECT]

KEY AREAS OF AGREEMENT
[What all experts agree is strong]

KEY AREAS OF DISAGREEMENT
[Where experts differ, how resolved]

HARD STOP ISSUES (if any)
[Which hard stops, if any, were triggered]

CRITICAL REVISIONS REQUIRED
[What must be fixed before use]

CONDITIONAL APPROVALS
[What conditions must be met for approval]

ISSUES TO MONITOR
[Post-approval, what metrics or assumptions need close watching]

NEXT STEPS
[Who owns revisions? By when? Resubmission process?]
═══════════════════════════════════════════
```

---

## Using This Panel in Practice

**When to convene the full panel:**
- Major capital allocation decisions ($XXM+)
- Strategy shifts (new market, new product, restructuring)
- Significant financial forecasts (IPO readiness, board guidance)
- Quarterly/annual budget reviews

**When lighter review is adequate:**
- Routine operational decisions ($XXM <)
- Tactical changes (smaller reforecasts, minor projects)
- Implementation planning (after strategy is decided)

**Typical time commitment:**
- Panel review: 2 hours total (individual 45 min + group 75 min)
- Async review (if experts are remote): Individual + async discussion over 2-3 days

**Expected frequency:**
- Monthly for major companies (quarterly deep-dive)
- Quarterly for growth/scale companies
- As-needed for smaller or earlier-stage companies
