# Mixture of Experts: Technology Council

Critical thinking framework using five expert perspectives to pressure-test technology strategy and identify blind spots.

After running technology landscape assessment, AI/data strategy, digital transformation planning, or making major architecture decisions, run your analysis through this technology council. Each expert brings a unique lens that catches what others miss.

## The Five Experts

### Expert 1: Enterprise Architect

**Identity:** 25-year veteran who's integrated 100+ acquisitions, designed systems at global scale, and managed technical debt disasters.

**Lens:** Systems thinking. How does this decision affect the entire system? What integrations are we creating? Will it scale to 100x current size? What's the debt we're taking on?

**Questions They Ask:**
- Is this architecture coherent, or are we gluing incompatible pieces together?
- Where are the integration points? Have we thought through data consistency?
- What's the technical debt we're incurring? Is it intentional and bounded?
- Can this scale to 10x, 100x our current size without fundamental redesign?
- Are we creating a monolith in disguise (coupling through shared data or synchronous calls)?
- What's the long-term cost of this decision if it succeeds? If it fails?
- How will we decommission this system in 5-10 years when requirements change?

**What They Score:**
- Architectural coherence (1-5): Do pieces fit together logically?
- Scalability thinking (1-5): Has scale been architected for, not just hoped for?
- Technical debt awareness (1-5): Are we aware of and tracking debt taken on?
- System interdependence (1-5): How tightly coupled is this to other systems?

**Red Flags They Raise:**
- "This will require changes to X systems later" → Replan to avoid future churn
- "We're not sure how this scales" → Reject until we are
- "We'll refactor this later" → If later never comes, you've built a legacy liability
- "This is the latest [trendy pattern]" → Why does buzzword matter?

**Their Hardest Critique:**
"You're optimizing for local elegance at the expense of system health. This looks clean in isolation, but it creates integration pain across the organization."

---

### Expert 2: AI/ML Product Leader

**Identity:** Led ML deployment at scale (Netflix, Google, Uber). Shipped 100+ models to production. Built MLOps infrastructure. Lost money on AI theater projects.

**Lens:** Does this AI strategy create real customer/business value? Are we being honest about what data exists? Have we thought through production complexity?

**Questions They Ask:**
- What's the actual business problem this AI solves? (Not "can we build a model" but "will this change customer behavior or outcomes?")
- What data actually exists, and what's the quality? (Be pessimistic, not optimistic)
- Have we measured baseline/control? How do we know if the model is actually working?
- What's the cost to deploy and maintain this model in production?
- How often must we retrain? What happens if we stop retraining?
- Can we explain the model's decisions to stakeholders, users, regulators?
- Do we understand failure modes? What happens when the model gets it wrong?
- Is this a multi-month science project or a 4-week product experiment?

**What They Score:**
- Business value clarity (1-5): Is there a real problem this solves?
- Data realism (1-5): Are we honest about data quality and completeness?
- Production readiness (1-5): Can we actually operate this at scale?
- Team capability (1-5): Does our team have MLOps and data engineering depth?

**Red Flags They Raise:**
- "We want to do AI" without defining the use case → Wrong starting point
- "We have a data lake, so we can do AI" → No, a lake isn't data architecture
- "We'll handle production later" → This is where 80% of the work happens
- "The model had 95% accuracy in the lab" → Test on holdout data, in production, against baselines

**Their Hardest Critique:**
"You're confusing machine learning exploration with shipped products. Until there's code in production with measured business impact, you don't have an AI strategy. You have research."

---

### Expert 3: Digital Transformation Officer

**Identity:** Run digital transformations at Fortune 500s (retail, insurance, banking). Led 10,000+ person organizations through change. Built platform engineering teams. Survived executive leadership turnover.

**Lens:** Will the organization actually adopt this? Do we understand the change burden? Is leadership aligned?

**Questions They Ask:**
- What's the change capacity of this organization? (Be brutal about this.)
- Who will resist this, and have we planned for that?
- Is executive leadership aligned on the vision? (If 5 execs, do all 5 agree?)
- Do we have the skills in-house, or will we need to hire/train/partner?
- What's the timeline for organizational change vs. technical change?
- How will we measure adoption and business impact?
- What could cause the leader to lose faith in this initiative?
- Do we have a clear executive sponsor who will unblock decisions?

**What They Score:**
- Organizational readiness (1-5): Can this org absorb this change?
- Leadership alignment (1-5): Are executives truly aligned or politely nodding?
- Change management rigor (1-5): Is there a real change plan or just tech?
- Talent/hiring plan (1-5): Can we attract and retain needed people?

**Red Flags They Raise:**
- "We'll do this in 12 months" for anything except pure technology → Organizational change takes 18-36 months
- "IT will handle the technical change, business will handle adoption" → Separation kills projects
- "We'll retrain everyone in workshops" → Upskilling requires mentoring, practice, failure
- "Executives want this but we haven't told teams yet" → If teams don't feel it's real, they'll wait it out

**Their Hardest Critique:**
"You've built a beautiful technology strategy that an organization isn't ready to execute. This will stall in month 6 when the executive sponsor has a bad quarter and redirects attention. Diagnose the organization first, then design for what they can absorb."

---

### Expert 4: Venture CTO

**Identity:** Built startups at speed (Figma, Plaid, Stripe in the early days). Chose pragmatic over perfect every day. Hired technical talent. Decided on-the-fly whether to build or buy. Made tech decisions with limited information.

**Lens:** Is this pragmatic for our constraints? Are we over-engineering? Can we get to value faster?

**Questions They Ask:**
- What's the minimum viable architecture to prove this works?
- Can we get to customer value in 4 weeks with 80% fidelity?
- Are we building platform for a product that doesn't exist yet?
- What's the simplest technology choice that unblocks us?
- Should we buy/partner instead of building?
- What tech debt is worth taking on for speed?
- How small can we keep the team in month 1-6?
- What don't we need to do to launch?

**What They Score:**
- Pragmatism (1-5): Are we over-engineering or under-engineering?
- Speed to value (1-5): Can we prove this works in <12 weeks?
- Simplicity (1-5): Have we removed unnecessary complexity?
- Build vs. buy realism (1-5): Are we solving problem or building tools?

**Red Flags They Raise:**
- "We need to build a platform before we build the product" → Build product, extract platform later if needed
- "We'll have full microservices from day one" → Kill five services? Only deploy monolith with clear service boundaries
- "We need a dedicated ops team before launch" → Operator-engineers, shared load. Ops specialist once you're at scale
- "We'll invest in best practices and standards" → Do minimum viable governance; standards emerge from practice

**Their Hardest Critique:**
"You've optimized for a Fortune 500 company when you're an early-stage business that needs to move fast. Boring is good when boring gets you to customer feedback. You're choosing elegance over learning velocity."

---

### Expert 5: CISO / Risk Advisor

**Identity:** Managed security and compliance for global enterprises and fintech. Prevented breaches. Built incident response. Navigated regulators. Understands cryptography, threat modeling, and liability.

**Lens:** What are the security and compliance risks? Are we building systems that can be compromised? Are we managing third-party risk?

**Questions They Ask:**
- Have we threat-modeled this system? What are the attack surfaces?
- If this system is breached, what's the blast radius? What customer data is at risk?
- Are we handling sensitive data (PII, payment, healthcare) correctly? (Encryption, access controls, audit trails)
- Do we understand third-party risk? (Vendor, cloud provider, SaaS tools - what could they do to us?)
- Are we compliant with relevant regulations? (GDPR, CCPA, HIPAA, PCI-DSS, industry-specific)
- What's our disaster recovery and business continuity plan?
- Are we logging and monitoring for security events?
- Have we planned for security incident response?
- Is data minimization in our design? (Don't collect/store data you don't need)

**What They Score:**
- Security architecture (1-5): Is this designed for security or bolted on?
- Risk awareness (1-5): Do we understand what could go wrong?
- Compliance readiness (1-5): Are we meeting regulatory requirements?
- Incident response planning (1-5): Are we prepared to respond to breaches?

**Red Flags They Raise:**
- "Security is a later phase" → Security must be part of architecture, not bolted on
- "We'll encrypt data at rest and in transit" (missing encryption where it's used) → Encryption is necessary but not sufficient
- "We're buying from vendor X, they must be secure" → Vendor security doesn't absolve you of responsibility; audit them
- "We don't expect to be attacked" → You will be; planning for when not if
- "We collect all customer data for future use" → Minimize what you store; liability grows with data

**Their Hardest Critique:**
"You've built a system that works for the happy path. But you haven't designed for the inevitable breach, regulatory audit, or data exposure. This will fail its first real test."

---

## Synthesis Protocol: How the Council Works Together

### Step 1: Present the Work (15 min)

Present your technology strategy decision or analysis. Be clear about:
- What problem you're trying to solve
- What you've decided (or are trying to decide)
- What constraints you're working within
- What you're confident about vs. uncertain about

### Step 2: Each Expert Critiques (20 min total, 4 min per expert)

Each expert reads the decision through their lens and flags:
- What they see that's missing
- What they're concerned about
- One hard question they want answered

**Enterprise Architect** speaks first: "Here's what I see for system coherence and scale..."
**AI/ML Product Leader** next: "Here's what I see for AI viability and data reality..."
**Digital Transformation Officer** next: "Here's what I see for organizational readiness..."
**Venture CTO** next: "Here's what I see for pragmatism and speed..."
**CISO** last: "Here's what I see for security and compliance risk..."

### Step 3: Identify Consensus & Disagreement (10 min)

Where do the experts agree?
- These areas are solid, move forward with confidence

Where do they disagree?
- These are the real strategic tensions
- Present both sides to decision-maker

What would make each expert more confident?
- Data to gather, validation needed

### Step 4: Synthesis Scorecard (5 min)

```
TECHNOLOGY COUNCIL SYNTHESIS
═══════════════════════════════════════════════

EXPERT PANEL VERDICTS
Enterprise Architect:        [Approve / Conditional / Reject] — Confidence: [H/M/L]
AI/ML Product Leader:        [Approve / Conditional / Reject] — Confidence: [H/M/L]
Digital Transform Officer:   [Approve / Conditional / Reject] — Confidence: [H/M/L]
Venture CTO:                 [Approve / Conditional / Reject] — Confidence: [H/M/L]
CISO / Risk Advisor:         [Approve / Conditional / Reject] — Confidence: [H/M/L]

DECISION RULE:
- 5 Approves = PASS (green light)
- 4 Approves, 1 Conditional = PASS WITH CONDITIONS (address the conditional before proceeding)
- 3 Approves, 2 Conditional = CONDITIONAL (must address both conditionals)
- 3 Approves, 2 Rejects = REJECT (rework and resubmit)
- <3 Approves = HARD STOP (major rework required)

KEY AREAS OF AGREEMENT
[What the panel agrees on]

KEY AREAS OF TENSION
[Where experts disagree]
  - Tension 1: Expert A says [X], Expert B says [Y]
    → Reframe as: [Decision choice]
    → Decision-maker must explicitly choose

CONSENSUS CONCERNS
[Issues 2+ experts flagged]
  Concern: [Description] — Owner to address: [Who]
  Concern: [Description] — Owner to address: [Who]

RECOMMENDATIONS BEFORE PROCEEDING
Action 1: [What to validate or change]
Action 2: [What to validate or change]
Action 3: [What to validate or change]

CONFIDENCE SUMMARY
Overall panel confidence in this decision: [L/M/H]
Reasons for confidence: [What makes us believe this will work]
Reasons for doubt: [What worries us]
═══════════════════════════════════════════════
```

---

## Hard Stops: When the Council Rejects

If the panel consensus is REJECT or 3+ experts raise the same issue, stop and rework. Don't proceed.

**Hard Stop Triggers:**

1. **Enterprise Architect + CISO Reject** → Architecture has fundamental integration or security flaw. Rework.

2. **3+ Experts Flag Same Issue** → Example: Enterprise Architect, AI/ML Leader, and Transform Officer all say "this requires expertise we don't have" → Hiring/partnership is non-negotiable before proceeding.

3. **Venture CTO says impossible to do in timeline, Enterprise Architect agrees** → Timeline is unrealistic. Reset expectations or re-scope work.

4. **CISO raises compliance risk that's non-negotiable** → No exception. Must be addressed in architecture, not mitigated away.

5. **Digital Transform Officer says organization can't absorb this change** → No amount of technical excellence fixes organizational readiness issues. Must address change readiness first.

---

## Red Team Checklist

Use when the council consensus is "PASS WITH CONDITIONS" — validate these before proceeding:

**Architecture Red Team**
- [ ] Scalability: Can we actually scale to 100x without redesign?
- [ ] Failure modes: What breaks if [critical dependency] fails?
- [ ] Integration: Will this integrate cleanly with existing systems?
- [ ] Reversibility: Can we unwind this decision if we're wrong?

**AI/ML Red Team**
- [ ] Data reality: Have we ground-truthed data availability and quality?
- [ ] Baseline: Do we have a clear baseline metric to measure against?
- [ ] Production: Have we planned for model retraining and monitoring?
- [ ] Failure: What happens if the model is wrong? Is that acceptable?

**Transformation Red Team**
- [ ] Adoption: Have we confirmed stakeholders actually want this?
- [ ] Skills: Do we have skills in-house or viable hiring/partnership?
- [ ] Timeline: Is 18-24 months realistic given org size and complexity?
- [ ] Leadership: Will exec sponsor stay committed if results are slower?

**Operations Red Team**
- [ ] Cost: Is TCO realistic or are we missing major costs?
- [ ] Vendor: If buying, have we evaluated vendor stability?
- [ ] Team: Do we have ops expertise to run this?
- [ ] Maintenance: What's the annual cost to keep this running?

**Security Red Team**
- [ ] Data: Are we collecting/storing only what's necessary?
- [ ] Access: Who can access what? Are controls tight?
- [ ] Monitoring: Can we detect breaches/misuse?
- [ ] Compliance: Are we meeting all regulatory requirements?

---

## Worked Examples

### Example 1: Microservices Migration Decision

**Decision:** Migrate from monolith to microservices

**Council Verdicts:**
- Enterprise Architect: CONDITIONAL (depends on whether domains are truly independent)
- AI/ML Leader: APPROVE (doesn't directly impact ML strategy)
- Transform Officer: CONDITIONAL (organization needs platform engineering capability first)
- Venture CTO: REJECT (too slow, monolith is fast enough at your scale)
- CISO: APPROVE (microservices can improve security isolation if done right)

**Synthesis:**
- **HARD TENSION:** Venture CTO vs. Enterprise Architect on necessity
  - Venture CTO: "You have 40 engineers, monolith is fine, this adds 12 months delay"
  - Enterprise Architect: "In 18 months you'll have 80 engineers, monolith will be bottleneck, microservices save you pain later"
  - Decision choice: Are you optimizing for now or for 18 months from now?

- **HARD STOP:** Transform Officer's condition
  - Can't migrate to microservices without platform engineering team (Kubernetes, CI/CD, observability)
  - Current org doesn't have this capability
  - Action: Hire/train platform engineers for 6 months, then migrate

**Recommendation:** PROCEED, but with phasing
- Phase 1 (Months 1-6): Build platform engineering capability
- Phase 2 (Months 7-18): Migrate independent domains
- Abort trigger: If platform isn't ready by month 6, cancel migration

---

### Example 2: AI Use Case Prioritization

**Decision:** Which AI use cases to fund in year 1?

**Council Verdicts:**
- Enterprise Architect: APPROVE (doesn't require architecture changes)
- AI/ML Leader: CONDITIONAL (depends on data being real)
- Transform Officer: APPROVE (user adoption looks feasible)
- Venture CTO: APPROVE (can be done in 12 weeks)
- CISO: CONDITIONAL (PII handling and bias assessment needed)

**Synthesis:**
- **CONSENSUS CONDITION:** AI/ML Leader + CISO both flag: Data quality and bias assessment critical
  - Action: Before funding any use case, validate data exists and quality is acceptable, run bias audit

- **DISAGREEMENT:** AI/ML Leader wants to start with 1 use case, Venture CTO wants 3 in parallel
  - AI/ML says: "Do 1, learn, then scale"
  - Venture says: "If you have the team, do 3 in parallel, learn faster"
  - Decision: Start with 1, hire second team mid-year to take on use case 2

**Recommendation:** PROCEED with data validation first
- Validate data for top 3 use cases (4 weeks)
- Begin AI model development on top use case (Months 1-12)
- Hire second ML team (Month 6), start use case 2 (Months 7-12)

---

## Usage in the Technology & Digital Strategy Skill

**Where to Invoke the Council:**

1. **Major Architecture Decisions** — Before committing to monolith → microservices, build → buy decisions, major platform changes

2. **Technology Portfolio Analysis** — Before deciding to INVEST heavily in a system or SUNSET a system

3. **AI Strategy** — Before committing budget to AI roadmap, validating use case prioritization

4. **Digital Transformation Roadmap** — Before finalizing Wave 1-3 roadmap; validate organizational readiness

5. **Tech Debt Decisions** — Before deciding to defer tech debt; validate risk

**Scoring Integration:**

In the main SKILL.md, after running through Phase 1-6 assessments, invoke this Mixture of Experts as Step 7:

```
PHASE 7: TECHNOLOGY COUNCIL EXPERT REVIEW

Load this reference file: mixture-of-experts.md

Run your completed technology strategy through the council:
  - Present findings from Phases 1-6
  - Each of 5 experts critiques from their lens
  - Identify hard stops and conditions
  - Score decision: PASS / CONDITIONAL / REJECT
  - Document council verdicts and reasoning

If PASS: Proceed with confidence, implement roadmap
If CONDITIONAL: Address specific conditions before proceeding
If REJECT: Rework the strategy and resubmit to council
```

This ensures every major technology strategy decision has been stress-tested by multiple expert perspectives before proceeding.
