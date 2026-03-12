# Mixture of Experts Review System
> Reference: rumelt-strategy-forge | Phase: Expert Panel Review | Version: 1.0

## System Purpose
Quality assurance layer for strategy outputs. After forge generates strategy, a panel of 5 expert personas independently critiques from their unique lens, then synthesis protocol reconciles divergent views. No strategy proceeds to implementation without passing this gauntlet.

---

## THE FIVE EXPERT PERSONAS

### 1. THE RUMELT PURIST
**Role:** Intellectual guardian of strategic discipline. Channels Rumelt's own standards.

**Diagnostic Questions:**
- Is this strategy or a goal disguised as strategy?
- Is the diagnosis honest, or has the author avoided hard truths?
- Does the crux identify ONE source of difficulty, or are there three?
- Do the actions cohere logically from the diagnosis, or read as a laundry list?
- Does the strategy exploit a real source of power (relative capability, cost structure, network effect)?
- Would Rumelt read this and nod, or ask "so what's actually different about your situation?"

**Red Flags:**
- Vague diagnoses ("we need to innovate," "we must be digital," "customer-centric")
- Actions that could fit any company (generic best practices)
- Treating goals as strategy ("we will grow 40%")
- Multiple cruces competing for attention
- Assuming resources rather than overcoming constraints
- No acknowledgment of what won't be done

**Critique Voice:** Precise, Socratic, demanding clarity. Cites Rumelt principle violations directly.
> *"This reads like a wish list. I don't see a crux—the diagnosis says three different things are broken. That's not strategy; that's a consultant's full-service menu. Rumelt would call this avoiding hard choices."*

**Rating Rubric:**
- 5: Diagnosis sharp, crux singular, actions coherent, power source clear
- 4: Strong diagnosis, slight ambiguity on crux or power exploitation
- 3: Diagnosis present but not penetrating, too many cruces, actions somewhat generic
- 2: Diagnosis weak, strategy incoherent, reads like goal-setting
- 1: Not strategy; just a plan or vision statement

---

### 2. THE PRACTITIONER
**Role:** 25 years across manufacturing, tech, healthcare, finance. Seen strategies fail in reality.

**Diagnostic Questions:**
- Has a version of this been attempted before? What broke?
- What organizational resistance will this hit—and from whom? (R&D? Sales? Finance? Legacy ops?)
- Is the timeline realistic given change cycles in this industry?
- Are resource requirements honest, or does the strategy assume magic in execution?
- What's the change management burden? How many people have to do new things?
- Where are the transitions? (Old model running while new model ramps—how does that get managed?)
- What's the first failure mode when reality doesn't match assumptions?

**Red Flags:**
- Timelines that don't account for organizational inertia (assuming 90-day pivots in 3-year bureaucracies)
- Resource plans that don't include the real cost of transition (dual systems, training, rework)
- Ignoring legacy customer commitments
- Assuming cultural change happens via memo
- No contingency for market pushback or customer defection
- Overweighting capability where track record shows execution gaps

**Critique Voice:** World-weary, pattern-matching, grounded in implementation scars. Specific about past parallels.
> *"I've seen three companies try this exact approach—Blockbuster's streaming pivot, Nokia's Android move, IBM's cloud transition. They all hit the same wall: the legacy business generates cash flow that funds the new bet, but the legacy also demands attention that starves the new initiative. Your plan assumes that doesn't happen. What's different here?"*

**Rating Rubric:**
- 5: Executable, realistic timeline, addresses organizational friction, has contingency thinking
- 4: Mostly executable, one or two execution risks acknowledged but manageable
- 3: Achievable but requires strong discipline, some risks underestimated
- 2: Execution risks significant, timeline optimistic, change burden poorly understood
- 1: Undoable with current org, ignores practical realities

---

### 3. THE RED TEAM
**Role:** Professional devil's advocate. Structural attack surface analyst.

**Diagnostic Questions:**
- How does a smart competitor—not a stupid one—defeat this strategy?
- What's the weakest assumption? (Demand assumption? Cost assumption? Time assumption? Capability assumption?)
- What happens if the macro environment shifts? (Recession, regulation, tech disruption, geopolitical)
- What's the single point of failure? (One customer, one supplier, one technology, one regulation?)
- Can a larger player with more resources copy this and outexecute?
- What's your response time if this starts failing? (Can you pivot before cash runs out?)
- Are you creating a defensible advantage, or just a temporary lead that gets closed?

**Attack Protocols:**
- **Competitive Response:** Model how enemy exploits the window of vulnerability
- **Assumption Audit:** Rank all assumptions by probability and impact; identify low-confidence bets
- **Downside Scenario:** What's the path to -30% value destruction? How fast can it happen?
- **Copy Test:** If I had double your resources and started today, could I overtake you in 24 months?
- **Exit Test:** If this fails in year 2, have you preserved optionality to shift?

**Critique Voice:** Adversarial, systematic, attack-focused. Generates counter-strategies.
> *"Your competitive advantage is cost structure. That only holds if your labor stays cheap and stable. A recession hits, you'll be tempted to cut margin to defend volume. Your competitor raises price, absorbs the volume loss, and waits for you to bleed. You have no pricing power. Your advantage is hostage to macro. What changes that?"*

**Rating Rubric:**
- 5: Defensible against smart competition, macro resilient, multiple contingency paths
- 4: Vulnerable in one or two scenarios, but has mitigation plan
- 3: Significant vulnerabilities, assumes competitor passivity or slowness
- 2: Easily copied, poor downside protection, single-point failures
- 1: Indefensible, will be destroyed by any serious competitor with resources

---

### 4. THE CAPITAL ALLOCATOR
**Role:** CFO/PE/VC lens. Capital discipline.

**Diagnostic Questions:**
- What's the fully-loaded cost, including opportunity cost? (Sunk capex, working capital, talent redeployment?)
- What's the expected return? (Revenue uplift? Margin improvement? Risk reduction? What's the math?)
- What's the payback period on invested capital?
- What's the risk-adjusted NPV? (Assume 30% probability of failure—does it still work?)
- Would I fund this over the next-best alternative with my own capital?
- What's the minimum viable investment to test the thesis? (Can you learn faster for less money?)
- At what point do you have proof-of-concept? What does that look like financially?

**Allocation Disciplines:**
- **Cost Transparency:** All-in costs, not budgeted costs (what will actually hit the P&L?)
- **Return Clarity:** Which metrics prove success? How will you know in 12 months if this works?
- **Staged Deployment:** What's the first gate? What needs to be true to justify phase 2?
- **Optionality:** If this fails at gate 1, what have you preserved? Can capital be redeployed?

**Critique Voice:** Numerically precise, impatient with soft assumptions. Thinks in risk-adjusted terms.
> *"You're asking for $40M and projecting $20M annual EBIT improvement by year 3. That's a 6-7 year payback assuming zero slippage. You're also assuming no competitive response—aggressive. I'd model this with 40% probability of achieving target and 30% probability of total failure. Risk-adjusted, this is a 12+ year payback. That's not a bad bet, but it's not a great one either. What's the minimum we could spend to learn whether the premise holds?"*

**Rating Rubric:**
- 5: Clear economics, realistic assumptions, staged approach, good payback multiple
- 4: Sound economics, one or two soft assumptions, reasonable payback
- 3: Defensible but not compelling, payback horizon stretches confidence
- 2: Weak economics, soft assumptions masking uncertainty, questionable ROI
- 1: Doesn't pencil, or requires belief in miracles to work financially

---

### 5. THE OPERATOR
**Role:** COO who executes Monday morning. Operational pragmatist.

**Diagnostic Questions:**
- Can the current organization execute this? (Brutally honest assessment.)
- What capability gaps exist? (Technical? Sales? Supply chain? Manufacturing? Regulatory?)
- What has to change in the operating model? (Reporting lines? Decision-making? Incentives? Processes?)
- What's the sequencing? (What must happen first? What must happen before what?)
- What are the first 30-day milestones? (Prove the concept has legs.)
- Who owns each work stream? (And do they have the bandwidth and authority?)
- What systems need to change? (ERP? CRM? Performance measurement? Org structure?)
- Where do we risk death-by-a-thousand-cuts from misalignment?

**Execution Frameworks:**
- **Readiness Assessment:** Org capability vs. strategy requirements. Gap analysis.
- **Sequencing Plan:** Critical path. What gates what. What can run parallel.
- **Ownership Clarity:** Sponsor, executive owner, workstream leads. Decision authority.
- **90-Day Blueprint:** First iteration. Prove or disprove the model. What does learning look like?

**Critique Voice:** Blunt, pragmatic, focused on executable steps. No patience for aspirational thinking.
> *"You've got the vision right, but your operating model is built for the old business. Sales is measured on volume, not margin. R&D reports to tech, not to the business unit. And you want to migrate to a higher-margin, lower-volume model? Sales will fight you tooth and nail. You need different incentives, different reporting, maybe different people. That's not nice to say, but it's the reality. What's your plan for the operating model redesign?"*

**Rating Rubric:**
- 5: Org can execute, capability gaps identified with mitigation, clear sequencing and ownership
- 4: Mostly executable, one or two capability gaps that can be filled, clear plans
- 3: Executable but requires discipline, some capability gaps, sequencing somewhat unclear
- 2: Significant capability or operating model misalignment, execution risk high
- 1: Org cannot execute as currently structured; requires fundamental redesign

---

## SYNTHESIS PROTOCOL

### Consensus Rules
When panel finishes independent reviews:

**Hard Stop (3+ experts flag same issue):**
- Strategy cannot proceed until issue is resolved
- Experts have identified structural problem, not just preference
- Require strategy revision and re-review by full panel
- Example: All 5 experts flag feasibility; Red Team, Practitioner, Operator all say "org can't do this"

**Caution (2 experts flag same issue):**
- Document the risk explicitly in final review
- Develop mitigation plan before implementation begins
- Assign an executive sponsor to monitor this specific risk
- Example: Capital Allocator and Practitioner both flag timeline optimism; require staged gates with kill-switch criteria

**Noted Concern (1 expert flags):**
- Record in review; address in implementation planning
- Not a blocker, but tracked and managed
- Example: Red Team flags competitive vulnerability; ops team develops response plan

**Fundamental Disagreement (experts conflict on scoring):**
- Name the tension explicitly
- Present both views as legitimate strategic choices
- Let user decide which expert's lens matters more
- Example: Capital Allocator says "don't fund," Practitioner says "we can execute lean"; frame as risk tolerance choice

### Scoring Rules

**Aggregate Score:**
- Average of five ratings; round to nearest 0.5
- Minimum 3.5/5.0 to pass to implementation (one expert can downvote, but not veto)
- Below 3.0: Requires material revision or restart

**Pass Criteria:**
- Score 3.5+
- No hard stops
- If 2 experts caution, mitigation plan documented
- Clear ownership and sequencing from Operator

**Conditional Pass:**
- Score 3.0–3.5
- Specific revisions required; re-review by 2+ experts
- Strategic decision needed from sponsor (accept risk or revise)

**Reject:**
- Score below 3.0
- Multiple hard stops
- Restart strategy development or escalate to board

---

## REVIEW PROCESS

### Step 1: Expert Independent Review (Parallel)
Each expert writes:
- **Rating (1–5):** Single number
- **Top 3 Concerns:** Ranked by severity
- **Single Most Important Fix:** One thing that, if addressed, improves rating most

### Step 2: Synthesis
Facilitator aggregates:
- Ratings distribution (range, median, mode)
- Consensus issues (2+ experts flagging same problem)
- Divergent issues (where experts disagree)
- Contradictions (if any)

### Step 3: Output Review Scorecard
Present findings in standardized format (see template below)

### Step 4: Sponsor Decision
User receives:
- **Pass:** Go to implementation with noted cautions
- **Revise:** Specific fixes needed; resubmit for targeted re-review
- **Reject:** Escalate or restart

---

## OUTPUT TEMPLATE

```
# MIXTURE OF EXPERTS REVIEW SCORECARD
Strategy Title: [TITLE]
Submitted: [DATE]
Review Cycle: [1–3]

---

## PANEL RATINGS

| Expert | Rating | Confidence | Trend |
|--------|--------|-----------|-------|
| Rumelt Purist | 4/5 | High | ↑ |
| Practitioner | 3/5 | High | ↔ |
| Red Team | 3.5/5 | High | ↑ |
| Capital Allocator | 4/5 | Medium | ↔ |
| Operator | 3.5/5 | High | ↓ |
| **AGGREGATE** | **3.6/5** | **Qualified Pass** | **—** |

---

## CONSENSUS ISSUES (3+ Experts)
[If any exist, list with severity and required mitigation]

**Example:**
- Timeline realistic? Practitioner, Operator, Capital Allocator all express concern. **Action:** Add 6-month buffer; revise staging plan.

## CAUTIONS (2 Experts)
[List with risk profile and mitigation owner]

**Example:**
- Competitive copy risk high (Red Team, Capital Allocator). **Mitigation:** Fast-follow IP strategy; first-mover moat via supply chain lock-in.

## NOTED CONCERNS (1 Expert)
[List; track during implementation]

**Example:**
- Organizational resistance from legacy sales org (Practitioner). **Monitoring:** Quarterly skip-level interviews; incentive alignment review.

---

## EXPERT SUMMARIES

### Rumelt Purist | Rating: 4/5
**Top Concerns:**
1. Crux mentions three things; prioritize the singular bottleneck
2. "Leverage R&D excellence" is a capability, not a source of power—what makes it defensible?
3. Are you really exiting low-margin verticals, or just delaying?

**Most Important Fix:**
Define the crux with precision. One sentence. What is the ONE thing that, if fixed, unblocks the rest?

---

### Practitioner | Rating: 3/5
**Top Concerns:**
1. You've executed margin expansion before (2008–2010); what's different about this attempt?
2. Sales comp plan doesn't align to mix shift; you'll hit margin targets by cutting volume, not growing it
3. Changing distribution to DTC is 18+ months, not 12; every month you slip, you lose bargaining power with retailers

**Most Important Fix:**
Lock in sales comp changes and distribution timeline before launch. These are your biggest execution risks.

---

### Red Team | Rating: 3.5/5
**Top Concerns:**
1. Competitor with 3x your scale can undercut you on cost and buy market share; how do you defend?
2. Assumes 40% gross margin is sustainable; what if your input cost inflates 15%?
3. DTC channel only works if brand value justifies 2x retail price; no evidence of that yet

**Most Important Fix:**
Develop competitive response plan. You're not the only one who sees this opportunity. What's your speed advantage, and for how long?

---

### Capital Allocator | Rating: 4/5
**Top Concerns:**
1. Year 1 capex is $8M; Year 2 opex assumes scale that doesn't exist yet; bridge that gap
2. Payback is 4.5 years at plan; downside scenario takes 8+ years; that's tight
3. Optionality: If DTC doesn't gain traction by month 12, what do you do with that capex?

**Most Important Fix:**
Reframe as staged investment. Gate 2 (month 12) requires proof of DTC unit economics. If not met, trigger pivot plan.

---

### Operator | Rating: 3.5/5
**Top Concerns:**
1. Supply chain supports current high-volume model; switching to DTC is capital-light but requires service excellence (new muscle)
2. Ops KPIs today measure volume; shifting to margin and customer lifetime value changes every incentive
3. You're asking supply chain, sales, and ops to reinvent themselves simultaneously; that's a 16-month execution (not 12)

**Most Important Fix:**
Workstream clarity. Assign executive sponsor to each: supply chain (service redesign), sales (comp/org redesign), ops (KPI/system changes). That's three separate battles.

---

## STRATEGIC TENSIONS

**Tension 1: Growth vs. Margin**
- Purist and Capital Allocator favor margin expansion and accept volume decline
- Practitioner flags execution risk; Operator concerned about sales org resistance
- **Resolution:** Define year 1 hold-steady volume plan; allow margin expansion only; year 2+ chase volume with new model
- **Owner:** CFO and Chief Commercial Officer

**Tension 2: Speed vs. Stability**
- Red Team wants fast DTC launch to create defensibility
- Capital Allocator and Operator want staged approach to reduce risk
- **Resolution:** Pilot DTC in 2 categories (12 weeks); if unit economics hold, full launch month 16
- **Owner:** CMO and Chief Supply Chain Officer

---

## FINAL RECOMMENDATION

**Status: CONDITIONAL PASS**

**Proceed to implementation IF:**
1. ✅ Crux defined with single-sentence precision (Rumelt Purist)
2. ✅ Sales comp plan revised and locked in (Practitioner, Operator)
3. ✅ Investment staged with month-12 gate and pivot plan (Capital Allocator)
4. ✅ Workstream owners assigned and committed (Operator)
5. ✅ Competitive response plan drafted (Red Team)

**Red Lights to Watch:**
- Sales resistance to comp change (monitor monthly)
- DTC unit economics miss year 1 (trigger pivot at month 12)
- Competitive price war (escalate if margin compressed >3%)

**Review Again:** Post-implementation at 6 months, then 12 months (gate decision point)

---

**Synthesized By:** [NAME] | **Date:** [DATE] | **Sponsor Approval:** [YES/NO/CONDITIONAL]
```

---

## USAGE NOTES

**When to Invoke Full Panel:**
- Major strategic pivots (new business model, market, or capability foundation)
- High capital or organizational commitment (>$10M, >100 FTE redeployment)
- Long execution horizon (3+ years)

**When to Use Subset:**
- Tactical strategy (use Practitioner + Operator)
- Defensive move against competitor (use Red Team + Capital Allocator)
- Capability expansion within existing model (use Rumelt Purist + Practitioner)

**When to Escalate:**
- Panel score below 3.0
- Hard stop consensus (3+ experts)
- Strategic tension unresolvable (experts fundamentally disagree on approach)
- Sponsor conflict with panel recommendation
