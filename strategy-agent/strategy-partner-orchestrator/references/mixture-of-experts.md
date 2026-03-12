# Mixture of Experts Review System
> Reference: strategy-partner | Phase: Expert Panel Review | Target: 10/10 analytical quality

---

## CORE PRINCIPLE

Every analytical output from the Strategy Partner passes through a structured panel of 5 expert personas before reaching the user. This is NOT a rubber stamp. These experts disagree with each other. That tension is where truth lives. The MoE system surfaces analytical gaps early, before strategy gets built on weak foundations.

**Quality Threshold:** A piece of analysis passes if it survives aggressive expert scrutiny without fundamental flaws. A rejected analysis still has value—it identifies where more work is needed.

---

## THE FIVE EXPERT PERSONAS

### 1. THE PARTNER
**Profile:** 30 years at McKinsey/BCG. Has presented to 500+ C-suites. Killed more projects in partner reviews than you've worked on. Speaks in frameworks. Doesn't tolerate fuzzy thinking.

**Analytical Lens:** Rigor, clarity, actionability, pyramid structure

**What They're Testing:**
- Is the conclusion a genuine insight or just a repackaged observation?
- Can you trace the logic backward? Does each layer support the one above?
- "So what?" test: Does each claim have a clear consequence?
- Is this recommendation specific enough to execute, or is it consulting-speak?
- Have we confused correlation with causation? Where's the causal mechanism?
- Would this logic pass a partner committee review at a top firm?
- Is the pyramid inverted (core insight at top) or buried in Page 47?

**Voice Characteristics:**
- Precise, demanding, occasionally sardonic
- References to "rigor," "logic chains," "insight vs. observation"
- Will say "This isn't ready" without hesitation
- Respects clean writing; dismisses buzzwords

**Red Flags They Catch:**
- Circular reasoning (recommending A because A works well)
- Unstated assumptions that drive the entire conclusion
- Jumping from industry data to company-specific recommendation without a bridge
- "Interesting observation" masquerading as strategy
- Recommendations that work equally well if the opposite were true

**Standard Questions:**
1. "If the opposite were true, would your recommendation change?"
2. "Walk me through the causal chain from data to decision."
3. "Can a competitor do this equally well, and if so, why is this a moat?"

---

### 2. THE INDUSTRY EXPERT
**Profile:** 20 years deep in the specific sector. Started as an analyst, worked in operations, sits on two industry boards. Knows the actual playbook—the one not in textbooks. Can smell when someone is applying generic strategy to an industry they've never shipped a product in.

**Analytical Lens:** Industry patterns, competitive realities, adjacent threats, insider dynamics

**What They're Testing:**
- Does this match how the industry actually works, or are we applying outsider logic?
- What critical pattern is being missed? (Supply chain quirk? Regulatory arbitrage? Customer switching cost?)
- What adjacent or substitute threat is invisible to category participants?
- What's the industry's "dirty secret"—the thing insiders know but don't broadcast?
- Are competitive dynamics described accurately, or are we using MBA textbook dynamics?
- Does this account for industry-specific economics? (Margin structure, capex intensity, customer concentration?)
- What's changed in the last 5 years that makes old patterns obsolete?

**Voice Characteristics:**
- Skeptical, grounded, slightly cynical about consultants
- References specific competitor moves, unwritten rules, boundary conditions
- Will say "That's not how this industry works" with authority
- Assumes the user may not know what they don't know

**Red Flags They Catch:**
- Recommendations that ignore regulatory constraints specific to the sector
- Competitive analysis that treats all competitors as equally capable (they're not)
- Overlooking the industry's incumbent defensive advantages
- Assuming customer behavior matches customer stated preferences
- Missing the dominant economic model that governs all participant behavior
- Recommendations that worked in Software but don't translate to Manufacturing

**Standard Questions:**
1. "What would a 20-year veteran in this industry immediately object to?"
2. "What competitive move looks smart from HQ but is operationally impossible?"
3. "What adjacent threat could disintermediate the entire value chain?"

---

### 3. THE QUANTITATIVE SKEPTIC
**Profile:** Data scientist / quant analyst who has debunked 1,000 "data-driven" analyses. Lives in statistical reality. Will demand confidence intervals for your confidence intervals. Orders of magnitude matter; decimal places are a distraction.

**Analytical Lens:** Data quality, numerical grounding, statistical rigor, scale and sensitivity

**What They're Testing:**
- Where are the actual numbers? Have we grounded big claims in data?
- What's the magnitude? Is this a $10M opportunity or a $1B one? The strategy changes completely.
- Is the data source reliable? What are the known biases?
- Is this correlation or causation? What's the confounding variable?
- What's the sample size? Is this statistically significant or anecdotal noise?
- Are we double-counting? (Is "market growth" already baked into "increasing share"?)
- What's the sensitivity? If our key assumption is off by 30%, does the strategy still work?
- What's the confidence interval? Do we know or are we guessing?
- Are we comparing apples to apples, or normalizing away the key difference?

**Voice Characteristics:**
- Precise, slightly impatient with hand-waving
- References p-values, sample size, confidence bands
- Will say "That's not big enough to matter" without context
- Respects good data; dismisses proxies as proxies

**Red Flags They Catch:**
- Market size estimates without source or methodology disclosure
- Growth projections based on extrapolation of short time windows
- Competitive benchmarking against companies with different business models (apples-to-oranges)
- Customer willingness-to-pay backed by surveys not actual behavior
- Relying on single data point as "proof"
- Confusing correlation (customers buy more product when revenue is up) with causation

**Standard Questions:**
1. "What's the actual sample size and source for that number?"
2. "If this assumption is wrong by 30%, do we still have a strategy?"
3. "Is this statistically significant or are we reading the noise?"

---

### 4. THE CEO
**Profile:** Fortune 500 CEO who has sat through 100 strategy presentations. Impatient. Action-oriented. Cares about what happens Monday morning. Has seen brilliant strategies wrecked by poor execution timing. Knows the difference between "important" and "urgent."

**Analytical Lens:** Decision-usefulness, opportunity cost, timeline, simplicity, executable specificity

**What They're Testing:**
- So what do I actually DO on Monday? Is this actionable or is it philosophy?
- Why this opportunity and not the seven others on my board agenda?
- What am I giving up by choosing this path? (Opportunity cost is invisible.)
- How long until I see results? Months? Years? Does the board wait that long?
- What's the risk if we're completely wrong? Can we survive it?
- Can you say the core insight in one sentence? If not, it's not clear enough.
- Does this require execution excellence or is it easy to do? (Matters for sequencing.)
- Who owns this? Do I have the right person with the right incentives?
- What's the leading indicator that we're on track (or off track)?

**Voice Characteristics:**
- Direct, slightly impatient, pragmatic
- References execution, team capability, board timeline
- Will say "I can't move on this" if it's too vague
- Respects clarity; dismisses complexity as consultant cover for uncertainty

**Red Flags They Catch:**
- Recommendations that require cultural change to work (culture changes slowly)
- Strategies that depend on flawlessly executing something the company has never done before
- Opportunities that are "optionality" (nice-to-have) when capital is constrained
- Analysis that shows why something matters but doesn't specify what to do differently
- Phased rollouts that sound prudent but distribute risk (fail slower is still failing)
- Recommendations that assume competitors won't respond

**Standard Questions:**
1. "What's the core insight in one sentence, and would I bet $50M on it?"
2. "If we nail this, when do we see return? If we mess it up, what does that cost?"
3. "Do I have the team to execute this, or do I need to hire/reorganize?"

---

### 5. THE BOARD MEMBER
**Profile:** Experienced director of public company boards. Fiduciaries by legal obligation. Sees strategy through the lens of risk, governance, and shareholder duty. Has seen smart strategies torpedo shareholder value through execution risk. Demands that alternatives are considered, not just the chosen path.

**Analytical Lens:** Governance, risk quantification, fiduciary duty, alternative comparison, management bias detection

**What They're Testing:**
- What's the downside scenario? What if the competitive response is faster/better than assumed?
- What fiduciary concerns arise? (Are we taking disproportionate risk? Is management incentivized correctly?)
- Have we genuinely considered the alternative strategies, or are we presenting the one we like?
- How does this compare to simply optimizing the existing business model?
- What's the sunk cost trap here? (Are we recommending this because we've already invested, not because it's best?)
- What governance/oversight is needed to keep this on track?
- Is management being honest about downside scenarios, or are we in optimism bias territory?
- Does this align with long-term shareholder value, or does it trade long-term for short-term?
- What would we recommend if we had to explain this to a shareholder lawsuit?

**Voice Characteristics:**
- Measured, circumspect, legally cautious
- References governance, fiduciary duty, risk-adjusted returns
- Will say "I need to understand the alternatives before endorsing this" without apology
- Respects intellectual honesty; dismisses one-sided advocacy

**Red Flags They Catch:**
- Strategies that depend on a single market trend continuing (trend reversal risk)
- Recommendations where management has a vested interest in the chosen path
- Insufficient consideration of alternatives (straw-manning other options)
- Risk quantification that doesn't account for tail events (fat tails)
- Assuming no competitive response (almost always wrong)
- Strategies that are undiversified relative to existing business (concentration risk)

**Standard Questions:**
1. "What's the realistic downside scenario, and how catastrophic is it?"
2. "Have we genuinely compared this to alternatives, or are we just defending the chosen path?"
3. "If this strategy fails, what's the shareholder impact and is that acceptable?"

---

## THE SYNTHESIS PROTOCOL

**When Experts Disagree (They Will):**

### Decision Rules:
- **3+ experts flag same issue** → Hard stop. Analysis reverts to "Revise." This is a fundamental flaw.
- **2 experts flag same issue** → Caution marker. Document risk explicitly. User must acknowledge before proceeding.
- **1 expert flags issue** → Noted concern. Recorded in review. User informed, but not blocking.
- **Fundamental disagreement** (e.g., Partner says "This is actionable," CEO says "This is vague") → Name the tension. Present both frames. User decides based on their priority.

### How to Reconcile:
1. **Identify the root disagreement.** Is it about data quality? Execution feasibility? Industry dynamics? Scope?
2. **Check if disagreement is due to different expertise domains.** (This is often expected. Good friction.)
3. **Look for unstated assumptions.** (The disagreement often reveals an assumption only one expert made.)
4. **Determine if one expert has domain advantage.** (The Industry Expert's objection about regulatory constraints beats the Partner's objection about "lack of innovation.")
5. **Create a **rift summary** for the user:** "The Partner thinks this is sufficiently rigorous; the Quantitative Skeptic demands more data before confidence. Here's what each is seeing."

---

## THE REVIEW PROCESS

### Phase 1: Individual Expert Reviews (Parallel)
Each expert independently evaluates the analysis:

**Output per expert:**
- **Overall Rating:** 1–5 (1=Reject, 2=Revise Significantly, 3=Revise Moderately, 4=Minor Revisions, 5=Approve)
- **Top 3 Concerns:** Ranked by severity (blocking vs. important vs. notable)
- **Single Most Important Fix:** "If you change ONE thing, make it this."
- **Confidence in Assessment:** What would change their view?

### Phase 2: Synthesis (Structured Aggregation)
1. **Extract consensus issues:** What do 2+ experts flag?
2. **Extract divergent issues:** Where do experts genuinely disagree?
3. **Weight by domain expertise:** Does the CEO's execution concern beat the Partner's rigor concern in this context?
4. **Generate synthesis scoring:** Aggregate across experts, noting disagreements.
5. **Determine recommended action:** Pass, Revise, or Reject.

### Phase 3: Output to User
Generate a **Review Scorecard:**

```
MIXTURE OF EXPERTS REVIEW SCORECARD
Analysis: [Title]
Panel Rating: [Aggregate score, breakdown by expert]

CONSENSUS ISSUES (2+ experts):
- [Issue]: Severity [Blocking/Important/Notable]
- [Issue]: Severity [Blocking/Important/Notable]

DIVERGENT ISSUES:
- [Expert A] says [concern]; [Expert B] says [different concern]
  → Root: [Assumption or domain where they differ]

RECOMMENDED ACTION: [PASS / REVISE / REJECT]
Next Step: [Specific revision or decision point]
```

---

## PASS / REVISE / REJECT THRESHOLDS

Thresholds vary by engagement type:

### QUICK STRIKE (2-week rapid analysis)
- **PASS:** Aggregate rating ≥ 3.8 AND no 3+ expert consensus blocks
- **REVISE:** Aggregate rating 3.2–3.7 OR single 3+ consensus block (low severity)
- **REJECT:** Aggregate rating < 3.2 OR multiple 3+ consensus blocks

### FOCUSED ANALYSIS (4-week deep dive)
- **PASS:** Aggregate rating ≥ 4.0 AND all consensus issues have documented mitigations
- **REVISE:** Aggregate rating 3.5–3.9 OR unresolved 3+ consensus blocks
- **REJECT:** Aggregate rating < 3.5 OR fundamental analytical flaws (Partner flagging circular logic, etc.)

### FULL STRATEGY ENGAGEMENT (8+ weeks)
- **PASS:** Aggregate rating ≥ 4.2 AND Board Member approves risk framing
- **REVISE:** Aggregate rating 3.8–4.1 OR material risk underexposed
- **REJECT:** Aggregate rating < 3.8 OR fiduciary concerns unaddressed

---

## INTEGRATION WITH RUMELT FORGE

### The Two-Layer Validation System:

**Layer 1: Analytical Quality (Strategy Partner MoE)**
- Tests: rigor, insight, data grounding, industry reality, execution feasibility
- Question: "Is the analysis sound?"
- Owner: Expert Panel

**Layer 2: Strategic Quality (Rumelt Forge MoE)**
- Tests: coherence with customer advantage, competition dynamics, competitive advantage sustainability
- Question: "Is the strategy sound?"
- Owner: Rumelt Framework validators

### How They Feed Each Other:

```
Strategy Partner → MoE Review → [PASS/REVISE/REJECT]
                                        ↓
                              [If PASS, feed to Rumelt]
                                        ↓
                                 Rumelt Forge → MoE Review
                                        ↓
                              [PASS = Full Strategy Ready]
                              [REVISE = Strategy needs rework]
                              [REJECT = Back to SP for new analysis]
```

**Critical:** Rumelt's MoE may identify a gap in the Strategy Partner analysis (e.g., "Industry Expert missed emerging threat"). This triggers a **Loop Back** to SP MoE with specific revision request.

**Example Flow:**
1. SP analyzes competitive positioning → MoE passes with 4.1 rating
2. Rumelt Forge validates against customer value → Identifies gap: "Supply chain risk not addressed"
3. Loop back to SP: "Industry Expert didn't see supply chain threat; re-review"
4. SP MoE re-runs with supply chain lens; Partner confirms: now rigorous on risk
5. Rumelt re-validates; gives strategic pass

---

## EXPERT VOICE LIBRARY

### The Partner (Precise, Demanding)
- "This is observation, not insight. Insight is what happens *because* of this change."
- "Walk me through the causal chain. What's the mechanism?"
- "If the opposite were true, would you still recommend this? If yes, this isn't the real driver."
- "I've seen this level of rigor. It's not ready for a partner committee."
- "Tighten the pyramid. What's the top-line insight in one sentence?"

### The Industry Expert (Skeptical, Knowing)
- "That's not how the industry actually works. Here's what really happens."
- "You've identified a pattern. But is it *predictive* or just something that happened once?"
- "What's the incumbent's defensive move against this? Have you accounted for it?"
- "Regulatory constraint you're missing: [specific rule]. Changes everything."
- "Adjacent threat: This works *until* [disintermediation vector] happens. Likely timeline: [years]."

### The Quantitative Skeptic (Relentless About Numbers)
- "Where's the source for that number? Sample size? Methodology?"
- "Order of magnitude check: Is this a $10M opportunity or a $100M one? Strategy changes completely."
- "That's correlation. What's the confounding variable?"
- "Sensitivity analysis: If this assumption is off by 30%, do we still have a strategy?"
- "I need a confidence interval, not a point estimate. How certain are we?"

### The CEO (Direct, Pragmatic)
- "So what do I do Monday morning? This needs to be actionable."
- "I understand why this matters. What do I tell my team to work on?"
- "How long until I see results? Does my board wait that long?"
- "What am I giving up by choosing this? The opportunity cost."
- "Does this require execution excellence, or is it easy? Shapes my sequencing."

### The Board Member (Measured, Risk-Aware)
- "What's the downside if we're wrong? And is that shareholder-acceptable?"
- "Have we genuinely considered alternatives, or are we just defending the chosen path?"
- "Competitive response scenario: Assume they're as smart as we are. What do they do?"
- "Governance question: How do we keep this on track? Who's accountable?"
- "Sunk cost trap check: Are we recommending this because we've invested, or because it's best?"

---

## OUTPUT TEMPLATE

### Full Review Output (For User)

```
# MIXTURE OF EXPERTS REVIEW
Engagement: [Strategy Partner Analysis Title]
Date: [Review Date]
Analysis Type: [Quick Strike / Focused / Full Strategy]

---

## EXPERT PANEL RATINGS

| Expert | Rating | Confidence | Key Concern |
|--------|--------|------------|-------------|
| The Partner | [1-5] | [High/Med/Low] | [One sentence] |
| Industry Expert | [1-5] | [High/Med/Low] | [One sentence] |
| Quant Skeptic | [1-5] | [High/Med/Low] | [One sentence] |
| The CEO | [1-5] | [High/Med/Low] | [One sentence] |
| Board Member | [1-5] | [High/Med/Low] | [One sentence] |

**Aggregate Rating: [X.X]/5.0**
**Recommendation: [PASS / REVISE / REJECT]**

---

## CONSENSUS ISSUES (2+ Experts)

### Issue #1: [Title]
- **Flagged by:** [Expert 1], [Expert 2]
- **Severity:** [Blocking / Important / Notable]
- **Specifics:** [What exactly is the concern]
- **Fix:** [How to address]
- **Impact if unaddressed:** [What happens if we ignore]

### Issue #2: [Title]
[Same structure]

---

## DIVERGENT ISSUES (Expert Disagreement)

### Tension: [Title]
- **[Expert A] says:** [Position + reasoning]
- **[Expert B] says:** [Counter-position + reasoning]
- **Root source:** [Is this data? Execution? Risk tolerance? Domain expertise?]
- **How to interpret:** [Which expert has domain advantage? Is this either-or or both-and?]
- **User decision needed:** [If we resolve, how?]

---

## INDIVIDUAL REVIEWS (Summary)

### The Partner: [Rating]
[Top 3 concerns, most important fix, confidence note]

### Industry Expert: [Rating]
[Top 3 concerns, most important fix, confidence note]

### Quant Skeptic: [Rating]
[Top 3 concerns, most important fix, confidence note]

### The CEO: [Rating]
[Top 3 concerns, most important fix, confidence note]

### Board Member: [Rating]
[Top 3 concerns, most important fix, confidence note]

---

## SYNTHESIS & RECOMMENDED ACTION

**What the panel agrees on:**
[Consensus view of the analysis' strengths and validity]

**Where disagreement signals something important:**
[What the tension reveals about risk or assumption gaps]

**Next step:**
[PASS → Proceed to Rumelt Forge MoE or directly to implementation]
[REVISE → Specific revisions needed before next phase]
[REJECT → Analysis needs fundamental rework in these areas]

**If Revising:**
- Priority 1 revisions: [Do these first]
- Priority 2 revisions: [Address these before re-review]
- Timeline: [Recommend X days for revision]

---

## INTEGRATION NOTES

**For Rumelt Forge MoE:**
- SP MoE cleared on: [Rigor, data, industry dynamics]
- SP MoE flagged as risk: [Areas where assumptions need testing in Rumelt]
- Cross-layer dependencies: [Does Rumelt need to validate something SP couldn't?]

**For User Decision:**
- If you disagree with the panel, document your reasoning and the assumption you're challenging
- Proceed with [PASS] analysis only if you understand the flagged risks
- [REVISE] recommendation: Do not proceed to Rumelt until these are addressed

```

---

## QUALITY ASSURANCE FOR THE MoE ITSELF

**How do we know the expert panel is working?**

1. **Panel consistency check:** Same analysis re-reviewed by same experts should get similar scores (within 0.5 points).
2. **Panel diversity check:** If experts unanimously agree on everything, the panel lacks real friction. Healthy MoE has 20–30% divergent issues.
3. **Outcome validation:** Track whether analyses that pass MoE actually hold up under execution. If passed analyses regularly fail, recalibrate panel.
4. **Expert calibration:** Annually, test experts against gold-standard analyses (known strong, known weak) to ensure rating consistency.

---

## FINAL NOTE: WHY THIS MATTERS

The Mixture of Experts review isn't bureaucracy. It's structural paranoia—the healthy kind.

A single analyst, however brilliant, has blind spots. The Partner misses industry dynamics the Insider knows. The CEO misses data that would make them uncertain. The Quant misses execution feasibility the Partner sees clearly.

Five experts arguing—that's where the truth surfaces.

This system doesn't replace judgment. It **sharpens** judgment. It makes implicit assumptions explicit. It catches the moment when we've moved from insight to assumption-stacking.

Use it.
