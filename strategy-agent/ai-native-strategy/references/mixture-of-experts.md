# Mixture of Experts: AI Strategy Expert Panel

## Overview

This reference provides 5 expert personas representing different perspectives on AI strategy. When major decisions arise, convene the panel to surface divergent views, identify blind spots, and synthesize recommendations.

**Panel Composition**:
1. **AI Venture Capitalist** — Pattern recognition, market timing, business viability
2. **Chief AI Officer** — Enterprise execution, organizational change, scaling
3. **AI Research Scientist** — Technical feasibility, model limitations, what's actually possible vs. hype
4. **AI Ethics & Policy Expert** — Regulatory compliance, responsible AI, societal impact
5. **AI-Native Founder** — Scrappy execution, rapid iteration, market fit

---

## EXPERT 1: AI VENTURE CAPITALIST

**Profile**:
- 15+ years investing in AI companies, 500+ evaluations
- Backed 20+ AI startups, 3 exits >$1B
- Pattern recognition across AI landscape, market cycles
- Deep understanding of what drives AI company value

### Expertise Areas
- Business model viability and defensibility
- Market timing and competitive windows
- Unit economics and path to profitability
- Founder quality and execution capability
- Exit potential and valuation trajectory

### What They Focus On

**Pattern 1: Data Moat vs. Execution**
- Belief: Execution matters more than data in 2026
- Why: Synthetic data commoditizing, fine-tuning on public data works
- Example: DeepSeek beat US labs on cost with similar data, better execution

**Pattern 2: First-Mover Trap**
- Belief: Fast-followers win in immature markets
- Why: First-movers learn expensive lessons, followers avoid those costs
- Example: Agentic AI (2024 movers struggling, 2026 followers positioned to win)

**Pattern 3: TAM Expansion vs. TAM Capture**
- Belief: Expanding TAM > capturing market share
- Example: Instead of fighting ChatGPT, build AI for underserved verticals
- Companies that create new categories worth more than followers in existing categories

### Red Flags

**Red Flag #1: "We'll compete on better AI"**
- Why it's bad: Model quality commoditizing, differentiation is 2-3 months at most
- What to do instead: Differentiate on distribution, vertical specialization, or integration

**Red Flag #2: "Our data moat is defensible"**
- Why it's bad: Synthetic data + public data often sufficient
- What to do instead: Build product moat (switching costs, customer lock-in)

**Red Flag #3: "We'll launch in 18 months with perfect product"**
- Why it's bad: AI moves fast, you'll be behind before launch
- What to do instead: Ship in 3 months, iterate with customers

**Red Flag #4: "We raised $100M, we'll dominate"**
- Why it's bad: Capital doesn't guarantee AI dominance (execution does)
- What to do instead: Focus on execution speed and product-market fit

### Questions They Always Ask

1. **"What's your unit economics at 10x scale?"**
   - Reveals: Cost structure, margin viability, scaling feasibility

2. **"If a giant (Google/Microsoft/OpenAI) launches the same product, how do you win?"**
   - Reveals: True defensibility, whether you're in a winnability position

3. **"How long until your advantage erodes?"**
   - Reveals: Realism about competitive window, time pressure

4. **"Who's your customer? Can you reach them cost-effectively?"**
   - Reveals: Go-to-market viability, CAC, market access

5. **"What's the narrative in 3 years if this company is a hit?"**
   - Reveals: Understanding of value creation, founder vision clarity

### How They Evaluate Recommendations

- **HIGH CONFIDENCE**: Business model is proven, unit economics work, clear competitive advantage
- **MEDIUM CONFIDENCE**: Business model reasonable, execution risk, competitive advantage unclear
- **LOW CONFIDENCE**: Unproven model, poor unit economics, easily copied, long payoff period

---

## EXPERT 2: CHIEF AI OFFICER (ENTERPRISE)

**Profile**:
- 15+ years in enterprise AI, built AI orgs at Fortune 500s
- Deployed 20+ production AI systems, scaled from pilot to enterprise
- Deep understanding of enterprise change management, governance, scaling
- Knows how to navigate organizational politics, regulatory requirements

### Expertise Areas
- Enterprise AI deployment and scaling
- Team building and organizational structure
- Governance frameworks, risk management
- Executive alignment and board communication
- ROI measurement and business case development

### What They Focus On

**Pattern 1: Pilot → Production Gap**
- Reality: 40% of enterprise AI projects fail transitioning from pilot to production
- Why: Pilots hide organizational complexity, governance gaps, data integration hell
- Lesson: Start with production-ready architecture, not just POC

**Pattern 2: Team Structure Determines Success**
- Reality: How you organize AI team predicts success better than model choice
- Why: Centralized = slow, federated = fragmented, hybrid = complex but works
- Lesson: Get the org structure right before hiring team

**Pattern 3: Legacy System Integration**
- Reality: 70% of enterprise AI failure is legacy system integration, not model issues
- Why: AI must connect to 20-year-old systems, data quality is terrible, governance is strict
- Lesson: Budget 40% of project time for integration

### Red Flags

**Red Flag #1: "We'll use the latest cutting-edge AI model"**
- Why it's bad: Enterprise wants stability, not the latest. GPT-5.2 from 2024 is fine.
- What to do instead: Choose proven, stable models. Innovation is in applications, not models.

**Red Flag #2: "We'll build a central AI team and have business units consume"**
- Why it's bad: Creates bottleneck, business units get impatient, start building competing AI
- What to do instead: Embed engineers in business units, architect for scale

**Red Flag #3: "This AI system will be autonomous"**
- Why it's bad: Enterprise never trusts full autonomy. Human oversight always required.
- What to do instead: Design with bounded autonomy, human checkpoints

**Red Flag #4: "We'll worry about governance later"**
- Why it's bad: By then, you have 20 unmonitored AI systems with no risk assessment
- What to do instead: Build governance from day 1, it's not optional

### Questions They Always Ask

1. **"How will this integrate with legacy systems?"**
   - Reveals: Architectural realism, integration complexity awareness

2. **"Who owns this AI system? What's their accountability?"**
   - Reveals: Organizational clarity, ownership structure, risk awareness

3. **"How will you measure success and ROI?"**
   - Reveals: Business case clarity, metric definition, executive expectations

4. **"What's your governance and escalation process?"**
   - Reveals: Risk awareness, compliance mindset

5. **"How will you retain the people who build this?"**
   - Reveals: Talent strategy, retention thinking, organizational sustainability

### How They Evaluate Recommendations

- **HIGH CONFIDENCE**: Production-ready architecture, clear ownership, governance defined, legacy integration planned
- **MEDIUM CONFIDENCE**: Some organizational gaps, governance clarification needed, integration questions
- **LOW CONFIDENCE**: Unproven in enterprise, weak governance, unclear ownership, integration nightmare

---

## EXPERT 3: AI RESEARCH SCIENTIST

**Profile**:
- 10+ years in AI research, published 50+ papers
- Deep understanding of model capabilities, limitations, what's hype vs. real
- Follows research frontier, knows what's possible vs. vendor claims
- Skeptical of marketing, grounded in empirical evidence

### Expertise Areas
- Model capabilities and limitations
- Architecture design and optimization
- Training, fine-tuning, evaluation methodology
- Research feasibility and technical risk assessment
- Separating real advances from marketing hype

### What They Focus On

**Pattern 1: Model Capability Overstated**
- Reality: Models are much worse at edge cases than benchmarks suggest
- Why: Benchmarks test "typical" cases, production sees rare/weird cases
- Example: GPT-5.2 is 90% accurate on common Q&A, but 30% on domain-specific edge cases

**Pattern 2: Fine-Tuning ROI is Overstated**
- Reality: Fine-tuning improves performance 5-15%, usually not worth the complexity
- Why: Foundation models generalize so well, targeted fine-tuning doesn't help much
- Exception: Domain-specific tasks (legal, medical) where specialized language helps

**Pattern 3: Prompt Engineering is the Real Leverage**
- Reality: 80% of AI performance comes from prompt engineering, not model choice
- Why: Better prompts = better reasoning = better outputs
- Lesson: Invest in prompt engineering, not in model fine-tuning

### Red Flags

**Red Flag #1: "This AI achieves 99% accuracy"**
- Why it's bad: Accuracy doesn't measure what matters (false positives, edge cases, drift)
- What to do instead: Measure accuracy on diverse test sets, audit for bias, test edge cases

**Red Flag #2: "We'll fine-tune the model to be smarter"**
- Why it's bad: Fine-tuning helps 10%, but foundation model is already 90% of the value
- What to do instead: Try prompt engineering first, only fine-tune if you have domain-specific patterns

**Red Flag #3: "This AI solves reasoning, we're using Tree of Thoughts"**
- Why it's bad: ToT is 3-5x more expensive, only worth it for very high-stakes decisions
- What to do instead: Use ReAct for most tasks, ToT only when justified

**Red Flag #4: "We'll use this model for high-stakes decisions with no human oversight"**
- Why it's bad: Model errors happen (hallucinations, bias, edge cases), humans are required
- What to do instead: Human-in-the-loop, bounded autonomy, continuous monitoring

### Questions They Always Ask

1. **"What's your actual accuracy on diverse test sets, including edge cases?"**
   - Reveals: Understanding of model limitations, evaluation rigor

2. **"Have you tested for hallucinations? What's your rate?"**
   - Reveals: Safety awareness, thorough testing, production readiness

3. **"What happens at edge cases? Have you characterized failure modes?"**
   - Reveals: Robustness testing, realism about limitations

4. **"How much of performance comes from the model vs. the prompt/architecture?"**
   - Reveals: Technical literacy, understanding of where value actually comes from

5. **"What does the research literature say about this approach?"**
   - Reveals: Grounding in research, awareness of what's actually validated

### How They Evaluate Recommendations

- **HIGH CONFIDENCE**: Grounded in research, edge cases tested, evaluation rigorous, limitations acknowledged
- **MEDIUM CONFIDENCE**: Reasonable approach, evaluation adequate, some limitations unexplored
- **LOW CONFIDENCE**: Overstated capabilities, insufficient evaluation, ignores research

---

## EXPERT 4: AI ETHICS & POLICY EXPERT

**Profile**:
- 10+ years in AI ethics, policy, responsible AI
- Advised regulators on AI policy, worked on EU AI Act
- Deep understanding of regulatory landscape, bias, fairness, compliance
- Focused on ethical deployment and societal impact

### Expertise Areas
- Regulatory compliance (EU AI Act, GDPR, sectoral regulations)
- Bias assessment and fairness evaluation
- Responsible AI deployment and safety
- Risk assessment and incident response
- Board governance and ethical decision-making

### What They Focus On

**Pattern 1: Compliance is Not Optional**
- Reality: EU AI Act deadline August 2026, non-compliance = €30M+ fines
- Why: Regulation is real, enforcement will be real, early movers will get fined
- Lesson: Build compliance into architecture from day 1, not as afterthought

**Pattern 2: Bias is Systemic, Not Just Data**
- Reality: Bias comes from data selection, labeling, model design, evaluation
- Why: Can't audit bias away, must build fairness into every step
- Example: Even if training data is balanced, model can learn biased patterns

**Pattern 3: Transparency Creates Liability**
- Reality: Being transparent about AI failures can create legal exposure
- Why: Documentation can be used against you in litigation
- Nuance: Still need documentation for compliance, but need legal review

### Red Flags

**Red Flag #1: "We don't need to worry about bias, it's data science issue"**
- Why it's bad: Bias is organizational issue, requires governance, cannot be ignored
- What to do instead: Governance framework, bias audit, fairness monitoring

**Red Flag #2: "We'll handle compliance after launch"**
- Why it's bad: By then, you're non-compliant, at risk, need to retrofit
- What to do instead: Build compliance into architecture from day 1

**Red Flag #3: "Our AI is fair because we removed protected attributes"**
- Why it's bad: Proxy discrimination still happens (zip code predicts race)
- What to do instead: Fairness metrics, intersectionality testing, external audit

**Red Flag #4: "This is high-risk AI, we don't need to tell customers"**
- Why it's bad: Transparency is legal requirement, hiding creates liability
- What to do instead: Disclose, document, monitor, audit

### Questions They Always Ask

1. **"Have you done a fairness audit? By whom?"**
   - Reveals: Governance maturity, external validation

2. **"What's your compliance status with EU AI Act?"**
   - Reveals: Regulatory awareness, governance implementation

3. **"How will you monitor for bias in production?"**
   - Reveals: Commitment to responsible AI, governance structure

4. **"What's your incident response plan for AI failures?"**
   - Reveals: Risk awareness, preparation, accountability

5. **"Have you assessed impact on different demographic groups?"**
   - Reveals: Fairness thinking, stakeholder consideration

### How They Evaluate Recommendations

- **HIGH CONFIDENCE**: Governance framework in place, compliance planned, fairness metrics defined, audit scheduled
- **MEDIUM CONFIDENCE**: Governance starting, compliance plan emerging, fairness considered
- **LOW CONFIDENCE**: Governance absent, compliance unclear, fairness ignored

---

## EXPERT 5: AI-NATIVE FOUNDER

**Profile**:
- Founded 2+ AI startups, 1 venture-backed
- Deep experience in rapid execution, learning from failures
- Understands market validation, product-market fit, growth
- Pragmatic about what actually works vs. what theory says

### Expertise Areas
- Rapid MVP development and iteration
- Market validation and product-market fit
- Go-to-market strategy and customer acquisition
- Team building and startup execution
- Fundraising and investor communication

### What They Focus On

**Pattern 1: Speed > Perfection**
- Reality: Ship in 3 months with 70% solution, iterate with customers
- Why: AI market moves fast, waiting for perfect product means you're behind
- Example: Launch with simple chatbot, add agents later, customers teach you what's needed

**Pattern 2: Customers Teach You What's Real**
- Reality: Your assumptions are usually wrong, customers correct you
- Why: Product ideas in your head ≠ what customers actually need
- Lesson: Get to customers in weeks, not months

**Pattern 3: Unit Economics Must Work Early**
- Reality: If your unit economics don't work at 100 customers, won't work at 1000
- Why: Scaling doesn't fix bad economics, just compounds the problem
- Example: If CAC is $50K and customer only pays $20K, more customers = bigger losses

### Red Flags

**Red Flag #1: "We're still in stealth, perfecting the product"**
- Why it's bad: Stealth phase usually means learning about customer need incorrectly
- What to do instead: Get customer feedback, even if it breaks your original vision

**Red Flag #2: "We'll launch with all features, perfect product"**
- Why it's bad: You'll be 6 months late, market will have moved, customer needs changed
- What to do instead: Launch MVP, iterate weekly with customer feedback

**Red Flag #3: "We'll raise more money to get us through unit economics"**
- Why it's bad: More money doesn't fix bad unit economics, just delays reckoning
- What to do instead: Fix unit economics before raising, prove model works

**Red Flag #4: "The market doesn't understand our product yet"**
- Why it's bad: If customers don't understand, it's not ready
- What to do instead: Rethink positioning, simplify message, validate demand

### Questions They Always Ask

1. **"Have you talked to 10+ customers? What did they say?"**
   - Reveals: Customer validation, assumptions vs. reality

2. **"What's your core loop from customer to feedback?"**
   - Reveals: Learning speed, iteration capability

3. **"Do your unit economics work? Can you show me the math?"**
   - Reveals: Business model viability, realism

4. **"What's the simplest version you could launch in 4 weeks?"**
   - Reveals: Feature prioritization, execution reality

5. **"Why will customers choose you over the alternative?"**
   - Reveals: Differentiation clarity, competitive positioning

### How They Evaluate Recommendations

- **HIGH CONFIDENCE**: MVP clear, customer validation started, unit economics reasonable, launch planned for weeks (not months)
- **MEDIUM CONFIDENCE**: Customer validation partial, unit economics emerging, launch in months
- **LOW CONFIDENCE**: No customer validation, unit economics uncertain, launch timeline vague

---

## EXPERT PANEL CONVERGENCE & DIVERGENCE PROTOCOL

### When Experts Agree (High Confidence)

If 4-5 experts agree → Proceed with high confidence
- Example: All agree this model choice makes sense, unit economics work, no regulatory issues, execution is feasible

**Action**: Approve and move forward

### When Experts Diverge (Decision Required)

If experts disagree, identify the root cause:

**Type A: Different Risk Tolerance**
- VC wants speed, CAO wants governance, Founder wants to move fast
- Resolution: Define risk tolerance explicitly, find middle ground
- Example: All agree on approach, just differ on governance rigor

**Type B: Different Information**
- One expert has info others don't
- Resolution: Share information, re-evaluate
- Example: Researcher knows about recent paper that changes feasibility

**Type C: Genuine Disagreement**
- Experts disagree on facts, not just risk tolerance
- Resolution: Design experiment to test, collect more data
- Example: Disagree on whether model fine-tuning will help → Run POC

**Type D: False Dichotomy**
- Experts framed as either/or, but third option exists
- Resolution: Question framing, find synthesis
- Example: Disagree on Build vs. Buy → Hybrid strategy works

---

## WHEN TO CONVENE THE PANEL

### Automatic Escalation (Convene Panel)

- [ ] Regulatory/compliance uncertainty (EU AI Act, sectoral regs)
- [ ] Mission-critical AI system (hiring, lending, autonomous)
- [ ] High investment decision (>$5M)
- [ ] Significant organizational change (new AI team, restructure)
- [ ] Competitive response (competitor launched, need counter)
- [ ] Ethical/fairness concerns raised
- [ ] Unit economics unclear (margin viability uncertain)
- [ ] Market entry decision (new product, vertical)

### Panel Meeting Protocol

**Duration**: 1-2 hours

**Structure**:
1. **Frame the decision** (10 min): What are we deciding?
2. **Each expert perspective** (8 min each, 5 experts = 40 min):
   - What's their analysis?
   - What are they optimizing for?
   - What red flags do they see?
   - What questions do they have?
3. **Identify convergence** (10 min):
   - Where do experts agree?
   - What's the confidence level?
4. **Identify divergence** (10 min):
   - Where do experts disagree?
   - What's the root cause?
   - What information would resolve disagreement?
5. **Synthesis and recommendation** (10 min):
   - Given expert input, what's the recommendation?
   - What are the risks?
   - What's the contingency plan?

**Output**: Documented synthesis with:
- Decision made
- Confidence level (HIGH/MEDIUM/LOW)
- Reasoning (what experts agreed on, where they diverged)
- Risks and mitigations
- Go/No-Go decision or need for more information

---

## TEMPLATE: MIXTURE OF EXPERTS EVALUATION

**Decision Being Evaluated**: [Decision name]

**VC Perspective**:
- Business model viability: [Assessment]
- Market timing: [Assessment]
- Unit economics: [Assessment]
- Confidence: [HIGH/MEDIUM/LOW]
- Red flags: [List]

**CAO Perspective**:
- Organizational readiness: [Assessment]
- Governance fit: [Assessment]
- Scaling potential: [Assessment]
- Confidence: [HIGH/MEDIUM/LOW]
- Red flags: [List]

**Research Scientist Perspective**:
- Technical feasibility: [Assessment]
- Evaluation rigor: [Assessment]
- Risk assessment: [Assessment]
- Confidence: [HIGH/MEDIUM/LOW]
- Red flags: [List]

**Ethics Expert Perspective**:
- Regulatory compliance: [Assessment]
- Fairness and bias: [Assessment]
- Governance readiness: [Assessment]
- Confidence: [HIGH/MEDIUM/LOW]
- Red flags: [List]

**Founder Perspective**:
- Execution feasibility: [Assessment]
- Customer validation: [Assessment]
- Unit economics viability: [Assessment]
- Confidence: [HIGH/MEDIUM/LOW]
- Red flags: [List]

**Synthesis**:
- **Convergence**: Experts agree on [X]
- **Divergence**: Experts disagree on [Y], root cause is [Z]
- **Recommendation**: [Decision]
- **Confidence**: [HIGH/MEDIUM/LOW]
- **Next steps**: [Actions needed]

---

**Last Updated**: March 2026
**Reference**: SKILL.md Expert Panel Integration
