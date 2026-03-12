# Mixture of Experts: Five-Expert Product Panel

Before finalizing any major product decision (roadmap, business model, platform decision, prioritization), run it through a five-expert panel. Each expert brings a distinct lens and blindspot. Together they catch what any single person would miss. This reference defines the five experts and their critiques.

---

## The Five Experts

### Expert 1: Product Visionary (The Steve Jobs Lens)

**Identity**: Former founder / Chief Product Officer with 15+ years shipping products customers love. Jobs-to-be-done obsessed. Simplification missionary. Taste over data.

**Lens**:
- **Question**: "Does this delight the customer? Or just satisfy them?"
- **Framework**: Jobs-to-be-done, customer empathy, product elegance
- **Focus**: Does the product solve the customer's real problem? Is it simple and elegant? Will customers love it?

**Key Questions This Expert Asks**:

1. **What job are we solving?**
   - Not "what feature are we building" but "what is the customer trying to accomplish?"
   - Red flag: If you describe the product in feature terms ("search, filtering, export") not job terms ("find the right product faster"), visionary says "we don't understand the job."

2. **Is this the simplest solution?**
   - Can we remove 30% of the feature set and still solve the job?
   - Red flag: "We added 12 features in the roadmap" → Visionary says "we need 3 features and relentless simplification."

3. **Will customers love this or tolerate it?**
   - Love = NPS 60+, word-of-mouth, repeat usage
   - Tolerate = NPS 30-40, churns eventually, features but no passion
   - Red flag: Roadmap optimized for feature velocity, not delight.

4. **Are we copying or creating?**
   - Copying competitors' features is playing their game.
   - Creating is finding a job no one has solved well.
   - Red flag: "Competitor shipped X, so we need to match it." Visionary says "compete, don't match. Build what they can't."

5. **What would we cut if we had infinite engineering?**
   - If you'd still cut certain features when unconstrained, they don't belong.
   - Red flag: Feature on roadmap because "we promised it" not because "it matters."

**Scoring (0-10)**:
- 9-10: Solves clear job elegantly. Simple. Delightful.
- 7-8: Solves job. Some complexity but justified. Good.
- 5-6: Solves job but inelegant. Acceptable.
- 3-4: Solves job but confusing. Must simplify.
- 0-2: Solves wrong job, or overcomplicates right job. Reject.

**Critiques To Watch For**:
- "This is bloatware" (often right, sometimes wrong if you're serving power users)
- "We should cut all the features" (useful push on simplicity, but impractical if customers demand them)
- "This isn't elegant" (subjective, but usually worth listening to)

---

### Expert 2: Data-Driven PM (The Metrics Obsessive)

**Identity**: Metric-driven product manager with deep analytics background. A/B testing guru. Funnel optimizer. Data before opinions.

**Lens**:
- **Question**: "What does the data say? Show me the experiment."
- **Framework**: Funnel analysis, cohort retention, A/B testing, leading indicators
- **Focus**: Is the decision grounded in data? What will actually move the needle?

**Key Questions This Expert Asks**:

1. **What's the hypothesis?**
   - Not "we should build this" but "users churn because X, and this feature will improve retention by Y%."
   - Red flag: No hypothesis. Gut feeling. "Customers have been asking for it."

2. **How do we measure success?**
   - Not feature-level (did we ship it?) but impact-level (did it move the needle?)
   - What's the metric? (retention, NRR, engagement, churn)
   - What's the target? (from 72% to 80% retention = 8pp improvement)
   - Red flag: Success metrics are vague ("increase user engagement") not specific ("improve 30-day retention from 72% to 80%").

3. **What's the current state of the metric?**
   - Baseline matters. Are we improving from 50% to 60% or from 90% to 95%?
   - Red flag: No baseline data. "We think users don't like X" but no metric proving it.

4. **Can we test this cheaply before building?**
   - Run a small experiment (survey, wizard, smoke test) before full build.
   - Example: "Survey users: would you pay $5/month for advanced analytics?" before building.
   - Red flag: Building full feature without proving demand first.

5. **What's the leading indicator we can track weekly?**
   - Don't wait 3 months for retention to move. What can we measure this week?
   - Example: "Feature adoption rate" is leading indicator for "will this improve retention?"
   - Red flag: No leading indicators. Waiting 3 months to know if decision was right.

6. **What are we not measuring that we should?**
   - Example: Roadmap prioritizes "new integrations" but you're not tracking integration usage.
   - Red flag: Shipping integrations everyone needs but nobody uses.

**Scoring (0-10)**:
- 9-10: Clear hypothesis, measurable target, leading indicators defined, can test cheaply first
- 7-8: Hypothesis grounded in data, good metrics, but missing some testing
- 5-6: Some data, but hypothesis is weak or metrics are vague
- 3-4: Minimal data, hypothesis is assumption, no testing plan
- 0-2: No hypothesis, no data, building blind. Reject.

**Critiques To Watch For**:
- "We need to A/B test everything" (wise generally, sometimes paralysis)
- "This won't move the needle" (often right, sometimes a feature matters for strategic reasons not metrics)
- "We're optimizing the wrong metric" (insightful, usually worth considering)

---

### Expert 3: Innovation Strategist (The Christensen Disciple)

**Identity**: Innovation and disruption expert. Jobs-to-be-done theorist. Understands disruptive vs. sustaining innovation. Thinks long-term.

**Lens**:
- **Question**: "Is this building our future defensibility? Or just improving today?"
- **Framework**: Disruption theory, three-horizon planning, adjacent possible, business model innovation
- **Focus**: Does this roadmap hedge against disruption? Are we playing on our terms or competitors'?

**Key Questions This Expert Asks**:

1. **How much are we investing in horizon 1, 2, 3?**
   - H1 (defend today), H2 (grow tomorrow), H3 (hedge future)
   - Healthy: 70% H1, 20% H2, 10% H3
   - Red flag: 95% H1, 5% H2, 0% H3 = you're vulnerable to disruption.

2. **What are we not building that we should?**
   - Example: You're a SaaS company. Are you exploring AI-native features? Or waiting for competitor to ship first?
   - Red flag: Roadmap is all H1 (feature parity with competitors).

3. **Is our business model at risk?**
   - Example: You sell perpetual licenses. SaaS is eating your market. Are you building a subscription model? Or defending licenses?
   - Red flag: Defending old business model while market shifts.

4. **Who are we vulnerable to?**
   - Low-end disruptor (cheaper, simpler)? Or new-market disruptor (different job)?
   - What's our response? Match them? Co-opt? Leapfrog?
   - Red flag: Ignoring disruptors. "They're not real competitors" (usually wrong).

5. **Are we creating the future or copying the past?**
   - Sustaining innovation = better at what competitors do
   - Disruptive innovation = different approach that competitors can't match
   - Red flag: Feature roadmap is all sustaining (match competitors).

6. **What would disrupt us?**
   - Pre-mortem: It's 3 years from now and we're gone. Why?
   - What disruption should we fear? (New entrants? New category? Commoditization?)
   - Red flag: "We're not at risk of disruption. Our moat is strong." (Probably wrong.)

**Scoring (0-10)**:
- 9-10: Roadmap balances H1/H2/H3. Hedges against disruption. Creates future options.
- 7-8: Roadmap is mostly H1/H2, some H3 hedge. Generally sound.
- 5-6: Roadmap is mostly H1, minimal H2/H3. Vulnerable to disruption.
- 3-4: Roadmap is 100% H1, defending against disruption reactively. Risky.
- 0-2: No H3 at all. Playing defense only. Vulnerable.

**Critiques To Watch For**:
- "This is mature market, we should harvest" (often right, sometimes wrong if TAM is growing)
- "We need to disrupt ourselves" (true but organizationally hard)
- "This business model is doomed" (apocalyptic, sometimes prescient)

---

### Expert 4: Engineering Leader (The Technical Realist)

**Identity**: VP Engineering / CTO with 10+ years building at scale. Knows technical debt. Understands scaling constraints. Realistic about execution.

**Lens**:
- **Question**: "Can we actually build this? What's the technical risk?"
- **Framework**: Feasibility, technical debt, architecture implications, team velocity
- **Focus**: Is the roadmap realistic? What technical work is missing?

**Key Questions This Expert Asks**:

1. **What's the technical cost of this decision?**
   - Not just calendar time (2 weeks) but technical cost (does it create debt? preclude other work?).
   - Example: "Real-time collaboration is 4 weeks of dev. But requires WebSocket infrastructure (2 weeks) and will preclude shipping mobile app (conflicts with framework)."
   - Red flag: Estimating feature in isolation, not considering system-wide implications.

2. **What technical work is hiding behind the feature?**
   - Database schema changes? Infrastructure upgrades? Refactoring?
   - Example: "Advanced analytics is 2 weeks of dev but requires data warehouse migration (1 month) and nobody talks about the migration."
   - Red flag: Underestimating hidden work.

3. **Are we paying down technical debt or accumulating it?**
   - Can we ship the feature cleanly or will it create technical debt?
   - Example: "We can ship dark mode in 1 week hacky, or 3 weeks clean. The hacky approach will make future theme work 2x harder."
   - Red flag: Always choosing hacky approaches to save time. Debt accumulates.

4. **Does our team have the skills to build this?**
   - Or do we need hiring/training?
   - Example: "Real-time collaboration requires expertise in WebSockets and concurrent data synchronization. We don't have that on the team."
   - Red flag: Assigning work to team without requisite skills.

5. **What's the architectural implication?**
   - Does this feature require changes to how we structure the system?
   - Example: "Platform APIs require moving from monolith to microservices. That's a 6-month architectural shift, not a feature."
   - Red flag: Not recognizing when roadmap is actually asking for architectural change.

6. **Can we scale this? What's the failure mode?**
   - Example: "Real-time collaboration at scale means millions of concurrent WebSocket connections. Our current infrastructure can handle 10k. Scaling to 1M is non-trivial."
   - Red flag: Shipping feature that works at small scale but breaks at 10x scale.

7. **How does this affect hiring/team composition?**
   - Feature might require specialized skills (ML, WebSockets, distributed systems).
   - Hiring takes 3-6 months. Plan accordingly.
   - Red flag: Not accounting for hiring lead time.

**Scoring (0-10)**:
- 9-10: Feasible. Effort estimated well. No hidden technical work. Team can ship.
- 7-8: Feasible. Some technical work but manageable. Team can ship with help.
- 5-6: Feasible but risky. Hidden technical work. Team struggles.
- 3-4: Feasible but very difficult. Requires hiring/training or debt accumulation.
- 0-2: Not feasible with current team. Requires major architectural change or hiring. Not ready.

**Critiques To Watch For**:
- "We need to rewrite everything" (usually overcorrection, but sometimes right)
- "This is technically impossible" (rarely true, but execution risk is real)
- "We can ship this in 1 week" (always underestimated if engineer says this)

---

### Expert 5: Business Model Architect (The Unit Economics Obsessive)

**Identity**: CFO / VP Business Model / Operator who understands unit economics, defensibility, competitive moats. Thinks in financial models.

**Lens**:
- **Question**: "Does this improve unit economics? Does this create defensibility?"
- **Framework**: LTV/CAC, gross margin, competitive moats, revenue model, pricing
- **Focus**: Is the roadmap making us more or less defensible? More or less profitable?

**Key Questions This Expert Asks**:

1. **How does this impact unit economics?**
   - Does it improve or hurt LTV, CAC, gross margin, payback period?
   - Example: "Real-time collaboration improves retention 5pp (retention goes from 75% to 80%). That's 20% improvement in LTV, worth $500k/year. Effort is 4 weeks. ROI is massive."
   - Red flag: No connection between feature and unit economics. Building because "customers asked for it."

2. **Is this defensible?**
   - Will competitors match this? If yes, you're in feature arms race (terrible).
   - Example: Dark mode is easy to match (competitors ship in 2 weeks). Not defensible. But real-time collaboration + your data infrastructure = harder to match.
   - Red flag: Building features that competitors can easily copy.

3. **Are we creating a moat?**
   - Network effects (more valuable with more users)? Switching costs (hard to leave)? Data advantage (hard to replicate)?
   - Example: Platform APIs create switching costs (developers have built on top of you). Moat is real.
   - Red flag: No moat created. Just features that are commoditized.

4. **What's the revenue implication?**
   - Does this enable new revenue stream? Or just sustain current?
   - Example: APIs enable ecosystem partners (potential revenue via take rate or premium tiers).
   - Red flag: Feature has no revenue implication. Just cost.

5. **What does our financial model say?**
   - If we invest $1 in this, what's the expected return?
   - Example: "Invest $500k in real-time collaboration (4 weeks). Expected LTV improvement = $1M/year. Payback in 6 months. Good invest."
   - Red flag: No financial model. Just "it's strategic."

6. **Are we chasing high-margin or low-margin revenue?**
   - Enterprise SaaS = high margin. Marketplace = low margin. Understand the tradeoff.
   - Example: "Platform/integrations enable SMB segment (20 customers at $5k). But SMB has high churn (50%) and low margin (40%). Enterprise segment has low churn (10%) and high margin (75%). Which should we chase?"
   - Red flag: Chasing revenue volume without considering margin.

7. **What's the customer concentration risk?**
   - If top 5 customers leave, how much revenue do we lose?
   - Healthy: <30% from top 5. Risky: >50% from top 5.
   - Red flag: Roadmap doesn't address customer concentration risk.

**Scoring (0-10)**:
- 9-10: Improves unit economics and defensibility. Clear ROI. Creates moat.
- 7-8: Improves unit economics. Some defensibility. Good financial case.
- 5-6: Neutral on unit economics. Maybe improves defensibility.
- 3-4: Hurts unit economics. No defensibility improvement.
- 0-2: Destroys unit economics. No moat. Reject.

**Critiques To Watch For**:
- "This destroys our gross margins" (always worth listening to)
- "We should raise prices instead of building features" (often right, sometimes wrong if market demands features)
- "We're in a race to zero on pricing" (apocalyptic, but sometimes prescient)

---

## Five-Expert Synthesis Protocol

### Step 1: Present the Decision

Clearly state what you're deciding:
- **Decision**: "Should we prioritize real-time collaboration in Q3?"
- **Context**: Why are we considering this? (Customer request? Competitive threat? Strategic initiative?)
- **Proposal**: What exactly are we proposing? (Feature, timeline, resource commitment)

### Step 2: Run Each Expert's Assessment

Ask each expert independently:

```
EXPERT ASSESSMENT FORMAT
═══════════════════════════════════════════════════

Expert Role: [e.g., Product Visionary]

Your Lens: [What matters to you in this decision?]

Key Question: [The single most important question for your expertise]

Assessment:
  Pros (from your perspective):
  - [Advantage 1]
  - [Advantage 2]

  Cons (from your perspective):
  - [Risk 1]
  - [Risk 2]

  Score: [0-10]

  Recommendation: [Proceed / Proceed with conditions / Reject]

Critical Assumption You're Making:
  - [What are you taking as given? What could change this assessment?]
```

### Step 3: Look for Disagreement

**High consensus (4-5 experts agree)**: Confidence is high. Few edge cases to consider.

**Medium consensus (3 experts agree)**: Confidence is medium. The dissenting experts have real concerns. Investigate.

**Low consensus (2-2-1 split)**: Confidence is low. Major tradeoff. Need to make explicit choice.

### Step 4: Identify Hard Stops

**Hard Stop**: An expert's concern that, if true, makes the decision a no-go.

Example:
- **Engineering**: "This requires architectural change we can't do in Q3. Hard stop unless we defer other work."
- **Business Model**: "This improves LTV but decreases retention (churn increases). If retention decreases, this is a hard stop."
- **Visionary**: "This solves the wrong job. Hard stop."

**Consensus Hard Stops** (3+ experts flag): Should not proceed without addressing.

**Minority Hard Stops** (1-2 experts): Consider carefully but you can override if aligned with strategy.

### Step 5: Surface Tradeoffs

What are you choosing between?

```
TRADEOFF IDENTIFICATION
═══════════════════════════════════════════════════

Option A: Prioritize Real-Time Collaboration
├─ Pro: Improves retention (Data-Driven says +5pp)
├─ Pro: Delights users (Visionary says it's elegant solution to real job)
├─ Con: No defensibility (Engineer says competitors can match in 4 weeks)
├─ Con: Hurts Q3 mobile roadmap (Engineer says conflicts with framework)
└─ Net: Good near-term, but doesn't create moat

Option B: Prioritize Mobile App
├─ Pro: Creates defensibility (Engineer: mobile experience is hard to replicate)
├─ Pro: Enables SMB market (Business Model: SMB market won't adopt without mobile)
├─ Con: Takes longer to ship (Engineer: 12 weeks vs. 4 weeks for collab)
├─ Con: Doesn't delight existing users (Visionary: only helps new segment)
└─ Net: Good long-term, but sacrifices Q3 retention improvement

DECISION: Which tradeoff aligns with strategy?
If strategy is: Retain existing users → Option A (real-time collab)
If strategy is: Expand into SMB → Option B (mobile)
```

### Step 6: Document the Decision

```
EXPERT PANEL DECISION
═══════════════════════════════════════════════════

Decision: Prioritize Real-Time Collaboration in Q3

Panel Verdict: PASS (with conditions)

Expert Scores:
├─ Visionary: 8/10 (elegant solution, but complex)
├─ Data-Driven: 8/10 (improves retention 5pp, clear metrics)
├─ Innovator: 5/10 (sustaining not disruptive, no moat)
├─ Engineer: 7/10 (feasible, but resource tradeoff)
└─ Business Model: 6/10 (improves LTV, no defensibility)

AVERAGE: 6.8/10

Consensus: Proceed with conditions

Key Conditions:
1. [Engineer] Must not block mobile roadmap. Delay other work instead.
2. [Innovator] Must plan H3 hedge against disruption (different job being solved elsewhere).
3. [Business Model] Must build defensible complementary features (e.g., templates that leverage collab).

Dissent:
└─ None (all experts agreed it's worth doing, just with different concerns).

Hard Stops:
└─ None triggered.

Decision Owner: [CPO Name]
Review Date: [End of Q3]
Kill Condition: [Retention doesn't improve 3pp by end of Q3 → reevaluate]
```

---

## Quick Expert Review (When You Don't Have Time for Full Panel)

When you need a faster decision, use Quick Expert Review:

**Step 1**: Ask each expert one question (5 minutes each).

**Step 2**: If any expert says "hard stop," investigate before proceeding.

**Step 3**: If consensus is high (4-5 agree), proceed. If low (<3 agree), do full panel.

---

## Common Expert Disagreements and How To Resolve Them

### Visionary vs. Data-Driven: Feature Simplicity vs. Customer Demand

**Visionary**: "Dark mode is bloat. Cut it."
**Data-Driven**: "50% of users request dark mode. Top feature in survey."

**Resolution**: Run the request through the Jobs-to-Be-Done lens. Is the job "reduce eye strain at night" or "use dark mode because everyone else has it"? The job matters.

### Engineer vs. Business Model: Technical Debt vs. Speed

**Engineer**: "We can ship real-time collab in 1 week hacky, or 3 weeks clean. The hacky version creates 2x future cost."
**Business Model**: "We need this in Q3 to address churn. 3 weeks is too long."

**Resolution**: Finance it. "If we pay technical debt cost now, is it cheaper than churn cost?" If paying debt saves $500k in churn, invest in clean approach.

### Innovator vs. Engineer: Strategic Vision vs. Feasibility

**Innovator**: "We should build AI-native workflows. That's our future."
**Engineer**: "That requires hiring 2 ML engineers. 6-month lead time."

**Resolution**: Plan horizon 2/3. "Can we start hiring and learning now (H3) so we can ship in H2?" Don't force H1 timeline on H3 work.

### Business Model vs. Visionary: Unit Economics vs. Elegance

**Business Model**: "We should build integrations. Higher LTV, better margins."
**Visionary**: "Integrations are commoditized. Build the core experience better."

**Resolution**: Both right. Integrate both. "Core experience excellence + strategic integrations." But sequence: first make core elegant, then expand integrations.

---

## When Expert Panel Reaches Different Conclusion Than You

You believe feature X is the right priority. Panel mostly disagrees. Now what?

**Option 1: Reconsider**

Panel might be right. Ego is not strategy. Reconsider.

**Option 2: Override and Document**

You can override. But document:
- "We decided [Decision] despite [Panel Concern] because [Reason]."
- Example: "We prioritize mobile despite Business Model concern on defensibility because market timing requires it (competitors are already in SMB)."
- This makes your assumption explicit. If it's wrong, you can learn and adjust.

**Option 3: Hybrid Approach**

Blend panel feedback. "Panel said don't do real-time collab. But we're doing it anyway because of [reason]. However, we'll mitigate the [Engineer's] concern about mobile blocking by [action]."

**No Option**: Don't ignore panel unanimously without documentation. You're probably missing something.

