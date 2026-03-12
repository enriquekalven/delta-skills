# Hypothesis-Driven Analysis Engine (10/10 Version)

## What Changed from the Original
Added: Bayesian confidence shifting mechanics with evidence-weight calibration. Cognitive bias checklist with concrete debiasing protocols. Multi-hypothesis management framework. Worked mini-example showing hypothesis evolution. Team alignment protocols for divergent priors. Contradictory evidence decision tree. Speed-vs-rigor calibration grid. Integration hooks with MECE Issue Trees.

## When to Use
Use at the start of any engagement where the answer isn't obvious. Hypothesis-driven analysis is the core operating method of top consulting teams because it prevents boiling-the-ocean analysis and forces intellectual courage early. This is especially critical when:
- Time is limited (force focus on high-impact questions)
- Data is messy or conflicting (structure how to weight contradictions)
- Teams have different views (alignment before execution)
- You're managing multiple competing theories (can't test everything)

This framework also structures ANY other framework — instead of running a complete Five Forces, hypothesize which forces matter most and test that.

## Step 1: Assess Available Evidence First

Before forming a hypothesis, inventory what you already know:

**Evidence Inventory:**
- What data has the user provided? (Summarize key facts)
- What does general industry knowledge suggest? (Pattern matching)
- What analogies from similar situations apply? (Relevant precedents)
- What doesn't add up or seems surprising? (Anomalies are clues)
- What's the conventional wisdom, and is there reason to think it's wrong?

This step matters because the best hypotheses don't come from frameworks — they come from noticing something in the evidence that others miss.

## Step 2: Form the Starting Hypothesis

Write one clear, specific, falsifiable statement about what the answer probably is.

**Bad hypotheses:**
- "The company should consider strategic options" (not falsifiable)
- "Growth is being affected by market dynamics" (not specific)
- "There may be opportunities in new markets" (not committal)

**Good hypotheses:**
- "Revenue growth stalled because mid-market customers are churning to Competitor X's lower-priced product, and the 40% price premium is no longer justified by feature differentiation"
- "The company should enter the EU market through acquisition of a local player because organic entry would take 3+ years and first-mover advantage is closing"
- "Profitability will improve 300bps by consolidating from 4 regional supply chains to 2 centralized hubs"

**Why this hypothesis and not another:** Explain in 2-3 sentences. What evidence or pattern pointed you here? This makes the hypothesis transparent and challengeable.

**Initial Confidence:** State as a percentage (e.g., "70% confident"). This is your prior — use it to track updates.

## Step 3: Identify Kill Criteria & Competing Hypotheses

**Hard Kill:** What single data point definitively disproves the hypothesis? (e.g., "If mid-market churn is actually flat, this is dead")

**Soft Kill:** What pattern would make the hypothesis unlikely enough to abandon? (e.g., "If 3 of 4 customers say price isn't the issue, we pivot")

**Pivot Triggers:** If the starting hypothesis dies, what are the 2-3 most likely alternatives?
- Alt A: [Statement] — Switch if [condition]
- Alt B: [Statement] — Switch if [condition]

**Note:** You may run 2-3 hypotheses in parallel early. Once evidence narrows the field, kill the weakest ones. Don't let competing hypotheses muddy your analysis — they should clarify which question matters most.

## Step 4: Design the Analytical Plan

For each key question, specify exactly what you need to know and how:

```
KEY QUESTION 1: Does price sensitivity actually explain the churn?
  Analysis: Customer churn cohort analysis (when customers churned, what they cite as reason)
  Data source: [CRM + exit surveys]
  Effort: 4 hours
  Confidence impact: HIGH (moves needle ±15%)

KEY QUESTION 2: Are we losing to competitor X specifically or bleeding broadly?
  Analysis: Win/loss analysis last 12 months
  Data source: [Sales team interviews + Salesforce pipeline]
  Effort: 6 hours
  Confidence impact: MEDIUM (±10%)
```

**Prioritization rule:** Sequence questions by confidence impact ÷ effort. Answer the questions that most efficiently increase or decrease confidence first.

**Adaptive timeline:** Instead of a fixed 3-week plan, define milestones:
- **Checkpoint 1 (early):** Have we found any kill criteria? Is the hypothesis still alive?
- **Checkpoint 2 (mid):** What's our confidence level now? Do we need to pivot to a different hypothesis?
- **Checkpoint 3 (pre-synthesis):** Is the evidence strong enough to recommend?

## Step 5: Bayesian Confidence Updating

As evidence arrives, update your confidence using this grid:

| Evidence Type | Confirms Hypothesis | Disconfirms Hypothesis |
|---|---|---|
| **Strong** (direct measurement, multiple sources, no ambiguity) | +20-25% | -20-25% |
| **Moderate** (one solid source, some interpretation needed) | +10-15% | -10-15% |
| **Weak** (anecdotal, single datapoint, high noise) | +3-5% | -3-5% |
| **Contradictory** (equally supports multiple hypotheses) | 0% | 0% |

**Example:** Start at 70% confident in Hypothesis A. Find strong confirming evidence → jump to 85-90%. Find moderate contradicting evidence → drop to 75-80%.

**When evidence splits 50/50:** Don't try to force a tiebreaker. Instead:
1. Acknowledge the split explicitly ("We found X supporting the hypothesis and Y against")
2. Decide: Do you need MORE evidence to break the tie, or is the split itself the answer? (Sometimes the answer is "this is truly uncertain")
3. If more evidence is needed, identify what would actually move the needle (strong evidence only)
4. If the split is the answer, recommend a hedging strategy (see Step 7)

## Step 6: Cognitive Bias Checklist & Debiasing Protocols

Before finalizing your recommendation, check for these traps:

| Bias | Red Flag | Debiasing Protocol |
|---|---|---|
| **Confirmation Bias** | You're only collecting evidence that supports your hypothesis | Assign someone to argue AGAINST your hypothesis. Find the strongest evidence against and force yourself to counter it. |
| **Anchoring** | Your initial confidence hasn't moved despite new evidence | Recalculate confidence from scratch using the Bayesian grid. Don't reference your starting percentage. |
| **Availability Bias** | You're relying heavily on the most recent or most vivid data point | Require evidence from multiple time periods and sources. Check: Does the recent example represent the broader pattern? |
| **Sunk Cost Fallacy** | You're defending a hypothesis because you've already spent time on it | Kill criteria exist for a reason. If they're triggered, pivot immediately. Past effort is irrelevant. |
| **Anchoring to Conventional Wisdom** | Your hypothesis is just "what everyone believes about this industry" | Explicitly test the opposite. What would have to be true for conventional wisdom to be wrong? |
| **Groupthink** | Your team all agreed immediately; nobody challenged the hypothesis | Require a "murder the hypothesis" session before finalizing. Bring in someone unfamiliar with the problem. |

## Step 7: Team Alignment with Divergent Priors

If team members start with different confidence levels, don't suppress it — surface it:

**Discovery:**
- "What's your prior confidence in this hypothesis?" (Ask before sharing evidence)
- "What evidence would move you?" (Make their decision tree explicit)
- "Where do you disagree with the direction?" (Identify the core disagreement)

**Resolution:**
1. **Separate belief from evidence.** The CFO might be skeptical of a reorg hypothesis because they've seen it fail before (prior = 20%). The COO is optimistic (prior = 75%). Start by acknowledging both priors are defensible.
2. **Run the evidence against both priors.** If you find strong confirming evidence, the CFO's confidence should rise to ~60%, the COO's to ~90%. If you find disconfirming evidence, both should drop.
3. **Make the evidence do the work.** Don't argue about who's right — keep testing until the evidence narrows the range.
4. **Document the alignment.** Record: "Starting gap was CFO 20% vs COO 75%. After evidence analysis, both now at 65%." This makes progress visible.

## Step 8: Multi-Hypothesis Management

When running 2-3 hypotheses in parallel:

**Early phase (before evidence arrives):**
- List all competing hypotheses clearly
- Assign each a starting confidence
- For each, identify the ONE piece of evidence that would most move the needle (highest impact/effort ratio)
- Test those high-leverage questions in parallel

**Mid phase (as evidence arrives):**
- Update confidence in each hypothesis using the Bayesian grid
- The hypothesis with the highest confidence after 2-3 rounds of evidence becomes the "lead" hypothesis
- Kill hypotheses with confidence below 20% (they're too weak to defend anymore)
- Keep 1-2 alternatives alive as backups

**Pre-synthesis (final phase):**
- Confidence should be concentrated in one hypothesis (typically 70%+)
- If still split, you haven't collected enough evidence — add one more round before recommending

## Step 9: Speed vs. Rigor Calibration

Not all hypotheses require the same level of evidence. Match your rigor to the stakes:

| Scenario | Speed Approach | Rigor Approach |
|---|---|---|
| **Low-stakes decision** (one-time issue, limited budget) | 2-3 quick interviews + existing data. Confidence threshold 60%. Decide in days. | 10+ interviews + statistical analysis. Confidence threshold 80%. Decide in weeks. |
| **Medium-stakes** (will affect next quarter's plan) | 5-7 interviews + light analysis. Threshold 70%. Decide in 1-2 weeks. | 20+ interviews + detailed modeling. Threshold 85%. Decide in 3+ weeks. |
| **High-stakes** (will commit significant capital) | Insufficient. Move to rigor approach. | Multiple data sources + controlled tests + sensitivity analysis. Threshold 85-90%. |

Choose your tier upfront. Don't start with speed and accidentally move to rigor halfway through.

## Step 10: Integration with MECE Issue Trees

Hypothesis-driven analysis and Issue Trees work together:

1. **Issue Tree identifies:** "What are ALL the possible levers that could affect revenue?" (Exhaustive decomposition)
2. **Hypothesis-driven analysis narrows:** "Of those 7 levers, we think Lever 3 (pricing) is the bottleneck" (Specific bet)
3. **Evidence testing proves:** "The data confirms Lever 3 is the issue AND reveals Lever 5 is also material" (Precision focus + surprise handling)

When using both:
- Build the Issue Tree first (this prevents missing a key lever)
- Form hypotheses about which branches matter most
- Test only those branches deeply
- Let surprising evidence lead you to unexpected branches (don't ignore it)

## Step 11: Worked Example — Hypothesis Evolution

**Starting state:**
- Company: SaaS product, $50M ARR, recently 8% YoY growth (used to be 30%)
- Hypothesis: "Growth slowed because we're losing mid-market customers to lower-priced competitor"
- Starting confidence: 70%

**Evidence Round 1 — Kill Criteria Check (1 week):**
- Finding: Churn rate actually flat at 3% (not spiking)
- Impact: Hard kill criterion triggered
- Confidence: Drops to 20%
- Decision: Pivot to Alternative Hypothesis

**Alternative Hypothesis:**
- "Growth slowed because of sales efficiency collapse — we're acquiring more customers but CAC has doubled"
- Starting confidence: 60%

**Evidence Round 2 (1.5 weeks):**
- Finding: CAC actually flat, but payback period increased from 18mo to 28mo (moderate confirming evidence)
- Finding: Product adoption metrics show new customers take 60% longer to hit critical mass (strong confirming)
- Finding: Sales team headcount up 40% YoY; productivity per rep down 30% (moderate confirming)
- Confidence: Rises to 75%

**Evidence Round 3 — Decision Point (final week):**
- Finding: Root cause analysis shows onboarding delays (internal team capacity issue), not product issue
- Recommendation: Invest in onboarding ops, not product changes
- Final confidence: 80%

This example shows: hypothesis dies, team pivots smoothly, evidence accumulates, confidence grows with clarity, recommendation emerges from the data.

## Step 12: Output Structure

```
HYPOTHESIS-DRIVEN ANALYSIS: [Topic]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATION
[What to do, stated directly and confidently if evidence supports it,
or stated with caveats if evidence is mixed. Include any hedging strategy.]

THE HYPOTHESIS TESTED
Starting hypothesis: [Statement]
Verdict: [Confirmed / Partially Supported / Rejected / Pivoted]
Final confidence: [%] — [Explanation of what moved it most]

EVIDENCE SUMMARY
For (by weight):
+ [Key point] — [Source] — [Weight: Strong/Moderate/Weak]
Against:
- [Key point] — [Source] — [Weight]

WHAT WE STILL DON'T KNOW
[Important unknowns and how they could change the recommendation]

CONFIDENCE LEVEL: [H/M/L with exact %]

IF WE'RE WRONG
[What happens if the hypothesis is wrong. Hedging strategy.
What's the early warning signal that we should pivot?]

TEAM ALIGNMENT
Starting confidence range: CFO 20% / COO 75%
Final confidence range: All stakeholders 70%+
Remaining disagreements: [None / or specify]
```
