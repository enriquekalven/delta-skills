# MECE Issue Tree Builder (10/10 Version)

## What Changed
The original framework was theoretically sound but tactically incomplete. This version adds: quantification guidance to size branches and focus effort; industry-specific decomposition patterns (B2B SaaS, Consumer, Industrial, M&A, Operations); a complete worked example showing diagnostic → hypothesis → priority branching; iterative refinement protocol when initial trees miss the mark; explicit handoff signals to the Hypothesis Engine; decision rules for competing L1 structures; 7 concrete decomposition traps with fixes; and stakeholder frame mapping so you know when different leaders see different trees.

## When to Use This Framework
Use MECE issue trees **first** in any strategic analysis where:
- The problem is ambiguous or the team disagrees on root cause
- Multiple hypotheses could explain the performance issue
- You need to prove you've examined all possibilities (rigor requirement)
- The decision tree doesn't exist yet — you're building the architecture of analysis

Do NOT use if: The question is already narrow and specific ("Should we buy Company X?" → Jump to M&A evaluation framework). The issue tree is a problem-decomposition tool, not a solution-evaluation tool in the final stage.

## Problem Classification (Choose One)

**Diagnostic Tree** — "Why is X happening?" (explaining underperformance)
- Structure: Break outcome into all possible causes, prioritize investigation
- Example: "Why did we lose 15% of enterprise customers in Q3?"
- Level 1 typically mirrors business model (Customer factors / Product factors / Sales/delivery factors)

**Solution Tree** — "What should we do about X?" (solving an identified problem)
- Structure: Break solution space into mutually exclusive, collectively exhaustive approaches
- Example: "How do we grow revenue 30% without M&A?"
- Level 1 often uses Ansoff (existing vs. new products/markets) or mechanism (organic, partnerships, geographic)

**Evaluation Tree** — "Should we do X?" (assessing a specific option)
- Structure: Break decision into criteria that matter, assess option against each
- Example: "Should we enter the Indian market?"
- Level 1 typically: Strategic fit → Financial case → Execution feasibility → Risk profile

**State your tree type upfront.** The type determines decomposition logic and what counts as "complete."

## Step 1: Quantify Branch Size (Where Effort Goes)

Before decomposing, estimate the magnitude of each major factor to know where to focus:

**Diagnostic context:** If investigating "Why is revenue down 20%?", decompose by known contribution first:
- "Market overall contracted 8%" (affects all players)
- "We lost 6% share to Competition A" (specific to us)
- "We had 4% pricing erosion in segment X" (specific to us)
- "Remaining 2% attribution unclear"

Now you know to deep-dive into the 6% share loss branch (high magnitude, addressable).

**Solution context:** For "How to grow 30%?", size the opportunity in each branch:
- "Existing market for existing products: addressable TAM = $50M, we have 10% = $5M, could grow to 20% = +$5M" (10pt growth)
- "Adjacent markets for existing products: TAM = $120M, current penetration = 0%, realistic target = 2% = +$2.4M" (8pt growth)
- "New product lines: market = immature, realistic contribution year 1-2 = $1-2M" (4pt growth)

This tells you: Go deep on share-gain in existing market first, then adjacent expansion. New products are secondary unless you have unique IP.

**Evaluation context:** Size the swing factor:
- "If we enter India and win 2% market share, that's $150M revenue uplift (strategic fit = high, but financial is lower than it looks at first)"
- "If execution takes 3x longer than plan, we face $100M sunk cost and late entry"

## Step 2: Level 1 Decomposition (The Governing Frame)

Level 1 is your **problem architecture**. A bad Level 1 ruins everything downstream.

### Industry-Specific L1 Patterns

**B2B SaaS (Diagnostic — why is NRR slowing?):**
- Cohort retention rates / Net expansion rate / CAC efficiency / Pricing/mix change
- OR: New customer acquisition → Existing customer expansion → Churn → Mix shift (by motion)

**Consumer/Retail (Diagnostic — why did sales drop?):**
- Market growth/contraction / Market share (traffic) / Conversion rate / Basket size (economics)
- OR: By customer segment (geographic, demographic, behavioral) to isolate impact

**Industrial/B2B (Diagnostic — why are margins compressing?):**
- Volume (utilization) / Price (list, discounts, mix) / COGS (input costs, efficiency) / OpEx (fixed vs. variable)

**M&A Evaluation:**
- Strategic fit (portfolio gap, tech, market access) / Financial case (growth, ROIC, synergies) / GTM & Commercial capability / Product differentiation / Execution (integration, people) / Risk (competitive response, regulatory)
  - **GTM & Commercial Capability (L2):** Sales force strength and productivity, KOL/advocacy networks and relationships, existing partnerships and alliances (exclusivity, transferability), marketing capabilities and medical affairs depth, channel access and distribution reach. *Why this branch:* Many M&A theses fail because the acquirer lacks the commercial capabilities to realize value — this branch forces explicit validation before proceeding.
  - **Product Differentiation (L2):** Dosing/formulation convenience vs. competitors, side effect profile and safety record, patient compliance and adherence factors, regulatory approval breadth (geographies, indications), product-level competitive advantages that drive physician/customer switching. *Why this branch:* Category-level analysis ("we'll be #3 in oncology") misses the product-level dynamics that determine actual adoption and market share.

**Operational Turnaround:**
- Revenue (pricing, volume, mix) / Gross margin (COGS, mix) / OpEx (fixed, variable, discretionary)

### Selection Rules When Multiple L1s Exist

You often have competing valid L1 structures. Use these criteria to choose:

1. **Hypothesis pre-test:** Which L1 structure puts your top 1-2 hypotheses into a single, drillable branch?
2. **Data availability:** Which L1 can you actually investigate quickly?
3. **Stakeholder alignment:** Which decomposition will convince the decision-maker?
4. **Isolation:** Does the L1 separate controllable from uncontrollable, or isolate the variable in question?

**Example:** Investigating "Why did gross margin fall 200 bps?" — you could decompose by:
- (A) Product category (if margin varies by product)
- (B) COGS driver vs. price driver (if you suspect specific causes)
- (C) Mix vs. unit economics (if portfolio changed)

If you strongly suspect "we're selling more low-margin product," choose (A) or (C). If you suspect "suppliers raised prices," choose (B). Pick the one that **isolates your top hypothesis most sharply.**

### Building L1: Rules

- 2-4 branches (rarely more; if you have 5+ something is wrong with abstraction)
- Each branch must represent a **fundamentally different explanation** or **mechanism**
- Branches must be **mutually exclusive** (evidence for one doesn't support another)
- Branches must be **collectively exhaustive** (all possible root causes fit into at least one)
- Each L1 branch gets a clear owner/analyst and specific hypotheses

## Step 3: Level 2 Decomposition (Testable Working Hypotheses)

Under each L1, build 2-4 Level 2 branches. Each must be:
- **Testable** — You can gather data to confirm/deny it in <1 week
- **Specific** — Not too broad (doesn't hide the real issue)
- **Written as a question** — "Is adoption of Feature X still below 30%?" not "Feature adoption"

Level 2 is where most investigation happens. Don't auto-go to Level 3; go deep only on high-impact branches.

## Step 4: Iterative Refinement (Trees Evolve)

Your first tree is a hypothesis, not truth. Refine using:

**After analyzing L1 branches:**
- If priority branch doesn't explain the gap, reassign effort to secondary branches
- If you find evidence that violates your MECE structure, redraw the tree
- If data reveals a sub-hypothesis is wrong, update the supporting branch

**Refinement triggers:**
- Data contradicts a key assumption → Rebuild affected L1/L2
- A branch proves 10x larger/smaller than estimated → Rebalance analysis effort
- Team disagreement emerges → Decompose further to expose the real disagreement point
- New stakeholder joins → Map their perspective onto the existing tree (see Step 7)

**Don't present multiple trees to clients.** Present one refined tree that incorporates learning.

## Step 5: Common Decomposition Traps

Avoid these—they destroy analysis quality:

**Trap 1: "Internal vs. External"**
- Bad: Breaks almost everything (internal people, external market, internal process, external regulation)
- Fix: Use "controllable vs. uncontrollable" OR "company-specific vs. market-wide" (narrower, cleaner)

**Trap 2: Overlapping categories**
- Bad: "Revenue vs. Profitability" (revenue is IN profitability)
- Fix: "Revenue drivers vs. Cost drivers" or "Pricing/volume vs. COGS"

**Trap 3: Timeline boundaries without definition**
- Bad: "Short-term vs. Long-term" (when does short end?)
- Fix: "Next 90 days vs. next 12 months vs. 2+ years" OR "Immediate actions vs. Structural changes"

**Trap 4: Unbalanced depth**
- Bad: L1 has 4 branches, one has L3 decomposition, others stop at L2
- Fix: Go deep on priority branches only, note why others are deprioritized

**Trap 5: Mixing problem types**
- Bad: A diagnostic tree that includes solution branches ("Loss of share" + "Pricing actions we could take")
- Fix: Diagnostic and solution trees are separate. Diagnostic identifies root causes; solution trees address them.

**Trap 6: Missing the "other" category**
- Bad: Decomposing "Why is churn up?" into "Product issues" + "Sales issues" + missing "Customer segment migration" or "Macro condition"
- Fix: Include catch-all or "Other" if there's a real gap

**Trap 7: False specificity**
- Bad: Too many L2 branches (8+ total), suggesting you haven't abstracted properly
- Fix: Roll similar issues up; if you have 8 L2 branches, you likely have a hidden L1 category

## Step 6: Handoff to Hypothesis Engine

When your tree is complete, signal to the Hypothesis Engine:

```
PRIORITY BRANCH for analysis: [L1 branch name]
PRIMARY HYPOTHESIS: [Specific, falsifiable claim]
SUCCESS METRIC: [What data confirms/denies this?]
ANALYSIS APPROACH: [Quick quantitative, interview-based, data-pull, etc.]
CONTINGENCY: [If this hypothesis fails, next branch to investigate is...]
```

The Hypothesis Engine will take your tree structure and turn priorities into executable analysis workstreams.

## Step 7: Stakeholder Frame Mapping

Different leaders see different trees. Map the alignment:

**CEO view:** Typically wants financial decomposition (revenue / gross margin / OpEx / ROIC impact)
**Product lead:** Wants feature/user behavior decomposition
**Sales lead:** Wants customer segment/motion decomposition
**CFO:** Wants waterfall decomposition (P&L line drivers)

When stakeholder trees differ, it's not a problem — it's **evidence that multiple lenses are needed.** Present the financial tree to the CEO, the product tree to the product leader, but ensure they all ladder up to the same root cause conclusion. If they don't, you have a disagreement to resolve upfront.

## Step 8: Output Format

```
ISSUE TREE: [Problem statement — one sentence]
Type: [Diagnostic / Solution / Evaluation]
Owner: [Lead analyst]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

L1: [Branch A] ← PRIORITY BRANCH
  Quantified impact: [$ or % contribution to overall gap]
  Hypothesis: [Specific, testable claim]
  Confidence: [High/Medium/Low — why?]
  L2: [Sub-issue A1] — Question: [...]
    Data needed: [...]
    Owner: [...]
  L2: [Sub-issue A2] — Question: [...]
    Data needed: [...]

L1: [Branch B]
  Quantified impact: [...]
  Hypothesis: [...]
  L2: [Sub-issue B1]
  L2: [Sub-issue B2]

L1: [Branch C] — DEPRIORITIZED
  Reason: [Why not investigating first; will revisit if A/B don't pan out]

MECE VERIFICATION: ✓ Mutually exclusive | ✓ Collectively exhaustive | [Issues found and fixes applied]
STAKEHOLDER FRAMES: [Who sees this tree differently and why — CEO / Product / Sales alignment]
NEXT STEP: [Specific first analysis to run on priority branch this week]
HANDOFF TO HYPOTHESIS ENGINE: [Primary hypothesis, success metric, analysis approach, contingency]
```

## Worked Mini-Example

**Problem:** "Why did our enterprise SaaS NRR drop from 125% to 110%?" (15pt decline)

**Tree type:** Diagnostic

**Quantification:** 15 points of NRR loss could come from:
- Retention (impact ~10 points if we went from 92% to 87%)
- Net expansion (impact ~5 points if we went from 35% to 30%)

**L1 Structure** (by motion):
- L1: Customer retention degradation (high likelihood, high magnitude)
- L1: Net expansion rate decline (high likelihood, high magnitude)
- L1: Mix shift to lower-NRR segments (medium likelihood, medium magnitude)

**Decomposed tree:**

```
L1: RETENTION DECLINE
  Hypothesis: Longer sales cycles + poor onboarding led to higher early churn in cohorts added post-Q2
  L2: Churn in cohorts added before vs. after June cutoff
    Data: Cohort retention curves; if post-June cohorts have 15% y1 churn vs. 8% pre-June, hypothesis confirmed
  L2: Churn by customer segment (enterprise vs. mid-market vs. SMB)
    Data: Segment-level retention curves; if only SMB churn spiked, different root cause
  L2: Churn by product adoption (high adopters vs. low adopters)
    Data: Feature adoption vs. churn; if low-adoption customers churn 2x more, onboarding is the issue

L1: NET EXPANSION DECLINE
  Hypothesis: Economic slowdown reduced expansion, or our upsell motion weakened
  L2: Contraction (downgrades, cancelations) vs. expansion (upsells) motion
    Data: Dollar-based net expansion by motion; if expansion revenue is flat but contraction spiked, economic
  L2: Expansion rate by cohort age
    Data: Year 2+ customer expansion curves; if older cohorts still expand normally, issue is sales motion not product

L1: MIX SHIFT
  Hypothesis: We added lower-NRR customer types without realizing it
  Hypothesis: Null hypothesis — mix stable
  L2: Customer segment composition (did % enterprise vs. mid-market shift?)
    Data: Segment mix by period; if enterprise dropped from 60% to 50%, that alone explains 2-3pt NRR drop
```

**Priority:** Retention decline (larger magnitude, more controllable). Analyze cohort retention curves by onboard date first this week.

---

This is a professional, complete framework. Hand it to a junior analyst and they'll produce a defensible issue tree on their first try.
