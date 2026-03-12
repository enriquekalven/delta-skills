# Feature Prioritization & Trade-Offs

Feature prioritization is where strategy meets execution. You have unlimited ideas and limited capacity. Prioritization is the discipline of saying no strategically. This reference operationalizes multiple prioritization frameworks and anti-patterns.

---

## RICE Scoring Operationalized

RICE (Reach × Impact × Confidence / Effort) is the most widely used quantitative prioritization framework. It scores features against strategic impact, forcing explicit tradeoff thinking.

### The Formula

**RICE Score = (Reach × Impact × Confidence) / Effort**

Each component is defined below. Output is a single score per feature. Higher score = higher priority.

### Reach: How Many People Will Use This?

**Definition**: Number of people (customers, users, or transactions) affected by this feature in a time window (typically quarterly).

**Scoring Scale**:

| Score | Count | Example |
|-------|-------|---------|
| 100 | Affects 100% of users | "Improve core search" — used by everyone |
| 50 | Affects ~50% of users | "Add analytics dashboard" — used by half of users |
| 25 | Affects ~25% of users | "Build SMS notifications" — used by 1/4 of users |
| 10 | Affects ~10% of users | "Add French language support" — used by 10% |
| 1 | Affects <5% of users | "Custom field for one customer" |

**Calibration**:
- Measure actively-engaged users, not registered accounts (many registered ≠ active)
- Measure potential reach if feature ships (not current demand signal)
- **Example**: "Build Zapier integration" might reach only 20% of users today (SMBs who use Zapier). But if you have 5,000 SMB customers and even 20% = 1,000 users. Score: 25-50 depending on TAM.

**Common Mistake**: Assuming enterprise features reach 100 (they don't). "Executive reporting" might reach only 20-30% (only some customers are large enough to have execs).

### Impact: How Much Does This Improve Key Metric?

**Definition**: Impact on the core business metric (retention, NRR, growth, margin). Not vanity metrics (feature adoption rate), but business metrics.

**Scoring Scale**:

| Score | Impact | Example |
|-------|--------|---------|
| 3 | Massive | "Improves retention 20%+" or "Grows NRR 15%+" |
| 2 | High | "Improves retention 10-15%" or "Grows NRR 5-10%" |
| 1 | Medium | "Improves retention 5-10%" or "Grows NRR 2-5%" |
| 0.5 | Low | "Improves retention <5%" or "Nice to have" |
| 0.25 | Minimal | "Maintenance" or "Compliance requirement" |

**Calibration**:
- Base impact on customer research and historical data, not opinion
- Link impact to a metric. "Improves retention" is too vague. "Improves 90-day retention from 72% to 77%" (5 percentage point improvement) is clear
- Use A/B test data if available. "We tested this feature with 500 users. Retention improved 3%. Projected to 100% of user base = 3% retention improvement."

**Common Mistake**: Conflating feature adoption with impact. "80% of users who see this feature use it" (adoption) ≠ "Improves retention 5%" (impact). Users might use a feature and still churn.

### Confidence: How Sure Are We About Reach and Impact Estimates?

**Definition**: Your confidence that the reach and impact estimates are accurate.

**Scoring Scale**:

| Score | Confidence | Example |
|-------|------------|---------|
| 100% | Very high | Feature similar to existing feature where we know impact. Strong data. |
| 75% | High | Feature similar to past work. Good data on reach. Impact is educated guess. |
| 50% | Medium | Feature is somewhat novel. Limited data. Impact is assumption. |
| 25% | Low | Feature is new category. Minimal data. High uncertainty. |
| 10% | Very low | Complete unknown. We're guessing. |

**Calibration**:
- Differentiate reach confidence from impact confidence. You might be 90% confident on reach (we know how many SMBs use Zapier) but 25% confident on impact (whether they churn less if we integrate).
- Use the lower of the two. If reach is 90% confident and impact is 25% confident, use 25%.
- Check your confidence against data. If you scored 75% but have no evidence, you're lying. Adjust down.

**Common Mistake**: Assuming everything is 75% confident. Be honest. Novel features should be <50%.

### Effort: How Much Work?

**Definition**: Engineering effort in person-weeks or person-months.

**Scoring Scale**:

| Score | Effort | Example |
|-------|--------|---------|
| 1 | <1 week | Configuration, small bug fix, copy change |
| 2 | 1-2 weeks | Small feature, single engineer, no dependencies |
| 4 | 1 month (4 weeks) | Medium feature, some testing, one engineer with help |
| 8 | 2 months | Large feature, multiple engineers, testing, QA |
| 16 | 4 months | Very large, platform work, multiple teams, dependencies |
| 32+ | 8+ months | Rewrite, platform shift, multi-quarter project |

**Calibration**:
- Include testing, QA, design, and deployment. Not just dev time.
- Include dependencies. If feature requires 2 weeks of dev + 1 week waiting on infra + 1 week for QA = 4 weeks effort, not 2.
- Ask engineers, don't guess.

**Common Mistake**: Underestimating effort. Always add 50% buffer. If engineers say 2 weeks, assume 3.

### RICE Scoring Process

**Step 1: List Candidate Features**

Gather all candidate features across product backlog. Aim for 10-20 features to score at a time (too many is noise).

**Step 2: Score Each Dimension**

For each feature, agree on Reach, Impact, Confidence, Effort. This requires discussion.

```
FEATURE: Add real-time collaboration
───────────────────────────────────
Reach:       25 (affects users doing group work, ~20-30%)
Impact:      2 (improves retention 10-15%, based on [customer research])
Confidence:  50% (novel feature, limited data on how much users will use)
Effort:      8 (requires WebSocket infrastructure, testing, QA)

RICE = (25 × 2 × 0.5) / 8 = 25 / 8 = 3.1
```

**Step 3: Calculate RICE Score**

RICE = (Reach × Impact × Confidence) / Effort

Feature with RICE 10 scores higher than feature with RICE 1.

**Step 4: Rank and Prioritize**

Sort by RICE score highest to lowest. This is your priority order.

**Step 5: Sense-Check**

Does the ranking pass the smell test? If not, audit:
- Are assumptions on reach/impact defensible?
- Did we underestimate effort on high-scoring items?
- Are strategic priorities reflected?

If RICE order contradicts strategy, choose consciously (perhaps sacrificing one feature to fund a strategic priority). But do it explicitly.

### Example RICE Scorecard

```
FEATURE PRIORITIZATION (Q3)
═══════════════════════════════════════════════════

Rank  Feature                Reach Impact Conf  Effort  RICE
─────────────────────────────────────────────────────────────
 1    Dark Mode              75    1      75%    4      14.1
 2    Real-Time Collab       25    2      50%    8      3.1
 3    Mobile App             50    2      50%    32     1.6
 4    Salesforce Integ       10    1      75%    2      3.8
 5    API Rate Limiting      100   0.5    100%   2      25.0
 6    Spanish Language       20    1      80%    6      2.7
 7    Custom Alerts          15    1.5    75%    4      4.2

PRIORITY ORDER (by RICE):
1. API Rate Limiting (25.0) → Core infrastructure, must-have
2. Dark Mode (14.1) → Quick win, high reach
3. Custom Alerts (4.2) → Moderate effort, expansion feature
4. Salesforce Integration (3.8) → Expansion feature
5. Real-Time Collab (3.1) → Strategic but risky
6. Spanish Language (2.7) → Geographic expansion
7. Mobile App (1.6) → Large effort, uncertain impact
```

### When RICE Fails

**RICE works best for**: Mature products with strong data, similar feature types, clear metrics.

**RICE works poorly for**: Novel features, features with hard-to-quantify impact (brand, moat), strategic pivots.

**What to do**: Combine RICE with judgment. RICE is input to decision, not the decision itself.

---

## ICE Scoring Comparison

ICE (Impact × Confidence / Effort) is simpler than RICE. Use when:
- You don't have reliable reach data
- Features serve highly variable user bases
- You're moving fast and need quick decisions

**Formula**: ICE = (Impact × Confidence) / Effort

Same definitions as RICE, just omit Reach. Reach is implicit in Impact (if something has high impact, it's hitting important users).

**Example**: Dark Mode might have Impact 2 (not huge impact on retention), Confidence 75%, Effort 4. ICE = (2 × 0.75) / 4 = 0.375

Use ICE when RICE feels like overkill.

---

## Opportunity Scoring (Teresa Torres Approach)

RICE is quantitative. Opportunity Scoring (from Teresa Torres' "Continuous Discovery") is more qualitative and research-driven. Use when you want to ground prioritization in actual customer insight.

### The Opportunity Scoring Framework

1. **Conduct Customer Interviews** (weekly, 5-7 interviews)
   - Ask about jobs they're trying to do
   - Listen for problems and unmet needs
   - Probe on frequency (does this matter every day or once a year?)
   - Probe on urgency (how important is solving this?)

2. **Synthesize into Opportunities**
   - Group similar problems into opportunity areas
   - Example opportunities: "Faster project setup", "Better visibility into team capacity", "Reduce time spent in status updates"

3. **Score Each Opportunity**
   ```
   OPPORTUNITY: Reduce time spent in status updates

   Frequency:  How often do users face this problem?
               └─ Daily (4) / Weekly (3) / Monthly (2) / Rarely (1)
               └─ Score: 4 (daily problem)

   Importance: How much does solving this matter to them?
               └─ Critical (4) / Important (3) / Nice-to-have (2) / Trivial (1)
               └─ Score: 4 (critical for their workflow)

   Satisfaction Gap: How dissatisfied are they with current solution?
                    └─ Very dissatisfied (4) / Dissatisfied (3) / Neutral (2) / Satisfied (1)
                    └─ Score: 4 (hate current solution)

   OPPORTUNITY SCORE = Frequency × Importance × Satisfaction Gap
                     = 4 × 4 × 4 = 64
   ```

4. **Rank and Prioritize**
   Highest-scoring opportunities are most likely to delight customers.

### Why Opportunity Scoring Over RICE

**Advantages**:
- Grounded in customer voice (not assumptions)
- Captures urgency and pain (RICE can miss this)
- Forces continuous customer discovery

**Disadvantages**:
- More effort (requires weekly interviews)
- Less quantifiable (some subjectivity in scoring)
- Slower (interviews take time)

**When to use**: Retention-focused phase (mature product, fighting churn). Customer discovery is your strongest input.

---

## Buy-a-Feature Exercise Design

Buy-a-Feature is a participatory exercise where customers "vote with money" on features. It reveals true prioritization and builds customer buy-in.

### How to Run

**Step 1: Feature List**

Create a list of 8-12 potential features. Include:
- Features customers have requested
- Features you're considering
- Features you don't plan to build (as decoys)

Example list:
- Advanced analytics ($5,000)
- Mobile app ($10,000)
- Custom alerts ($2,000)
- Integrations with Salesforce, Slack, Zapier ($3,000 each)
- Dark mode ($1,000)
- API access ($4,000)

**Step 2: Allocate Budget**

Give each customer a budget to spend. Total allocated budget > cost of all features (so they choose, not buy everything).

Example: 5 customers × $50,000 budget = $250,000 total. Total feature cost = $350,000. They have to choose.

**Step 3: Facilitated Shopping**

Customers pick features. They can negotiate ("give us dark mode and Slack integration for $8,000 instead of $9,000"). This is the learning.

**Step 4: Synthesize Results**

Track what sells and what doesn't. Pattern match.

Example results:
- Mobile app: All 5 customers buy ($50,000 total) → Unanimous demand
- Dark mode: 3 customers buy ($3,000 total) → Nice-to-have
- Advanced analytics: 4 customers buy ($20,000 total) → Important but not essential
- API access: 0 customers buy → Nobody wants it

**Step 5: Learn**

This is not a vote on what to build. It's learning what customers truly value. Use it as input to RICE or strategy.

### Exercise Variations

**Charity Format**: "We'll donate $1 to [charity] for each $1 of features you buy. You decide what to fund."

**Iteration Format**: Run exercise, tell customers "we're building X." Run again next quarter. See if priorities changed.

---

## MoSCoW Prioritization for Releases

MoSCoW is simple and works well for release planning. Use for quarterly or bi-weekly release planning.

**M = Must Have** (non-negotiable for this release)
- Examples: Bug fixes, must-have features for committed customers, compliance requirements
- If must-haves don't ship, release is a failure

**S = Should Have** (strongly desired, ship if possible)
- Examples: Nice-to-have features, optimizations, documentation improvements
- Typically: 50% of should-haves ship

**C = Could Have** (nice-to-have, ship if time permits)
- Examples: Experimental features, polish, edge cases
- Typically: 10% of could-haves ship

**W = Won't Have** (explicitly not in this release, push to next)
- Examples: Features in backlog but not committed to this release
- Prevents scope creep

### Release Planning with MoSCoW

```
RELEASE: Q3 Major Update
═══════════════════════════════════════════════════

MUST HAVE (Committed, non-negotiable)
├─ Fix OAuth bug (customer-blocking, 20% of logins fail)
├─ Add SAML support (contractual requirement)
└─ Upgrade database infrastructure (stability, 6 months overdue)

SHOULD HAVE (Strongly desired, schedule-permitting)
├─ Real-time collaboration (roadmap commitment)
├─ Advanced analytics (top customer request)
├─ Mobile app phase 1 (strategic initiative)
└─ Integrations (Salesforce, Slack, Zapier)

COULD HAVE (Nice-to-have, effort-permitting)
├─ Dark mode
├─ Spanish language support
├─ Performance optimization
└─ UI Polish

WON'T HAVE (Deferred to Q4+)
├─ PDF export (in Q4)
├─ Custom fields API (in Q4)
├─ Developer marketplace (in H2)

EFFORT ALLOCATION
Must Have:     40% of engineering
Should Have:   50% of engineering
Could Have:    10% of engineering (stretch)
```

When a release slips, cut from Should/Could first, never Must. This forces hard prioritization.

---

## Kano Model: Feature Classification

The Kano model classifies features into three categories based on how they impact satisfaction:

### The Three Feature Types

**Must-Haves (Threshold/Hygiene Factors)**
- Absent = customer is very dissatisfied
- Present = customer is not satisfied, just not dissatisfied
- Example: A SaaS product MUST not go down. If it's down, customer is furious. If it's up 99.99%, customer doesn't praise you, they expect it.

**Performance Features (Satisfiers)**
- More = more satisfaction
- Less = less satisfaction
- Example: Faster performance = more satisfied. Slower performance = less satisfied. Linear relationship.

**Delighters (Exciters)**
- Absence = customer doesn't expect it, so not dissatisfied
- Presence = customer is delighted
- Example: Dark mode. You don't expect it, but if it's there, you love it.

### Strategic Implications

**Must-Haves**:
- Required to stay in the game
- Don't create competitive advantage (everyone has them)
- But failing on them is catastrophic
- Example: SaaS uptime, data privacy

**Performance Features**:
- These create competitive advantage
- Improve retention and NPS proportionally
- Invest here to win against competitors

**Delighters**:
- Create emotional attachment
- Become table-stakes (delighters become must-haves)
- Short-term competitive advantage

### Prioritization with Kano

```
KANO ANALYSIS: Feature Categorization
═══════════════════════════════════════════════════

MUST-HAVES (Prevent dissatisfaction)
├─ Uptime/Reliability
├─ Data Security
├─ Basic functionality
├─ Support responsiveness

PERFORMANCE FEATURES (Create advantage)
├─ Speed of features shipping
├─ Intuitiveness of UX
├─ Integration breadth
├─ Feature depth in key areas

DELIGHTERS (Create delight, temporary advantage)
├─ Dark mode
├─ Exceptional onboarding
├─ Surprising performance
├─ Thoughtful UX touches

STRATEGIC FOCUS
└─ Must-Haves: Maintain at category parity
└─ Performance: Differentiate here against key competitors
└─ Delighters: Use to create emotional advantage, but don't rely on them
```

**Watch for**: Delighters becoming must-haves. Dark mode started as delighter (2016), becoming expected (2024). Adjust prioritization as features evolve categories.

---

## Trade-Off Frameworks: Scope vs. Time vs. Quality

Every project requires tradeoffs: Scope × Time × Quality. You can optimize two, but one will suffer.

### The Three Dimensions

**Scope**: What are you building? (Features, functionality, polish)

**Time**: When does it ship? (Deadline)

**Quality**: How well does it work? (Reliability, performance, UX polish)

### Trade-Off Patterns

**High Scope + Tight Timeline = Quality Suffers**
- Ship feature-complete but buggy or poorly designed
- Example: Ship real-time collaboration in 2 months, but it's hard to use
- Risk: Users hate it, churn increases

**High Quality + Tight Timeline = Scope Suffers**
- Ship high-quality but limited feature
- Example: Ship dark mode beautifully in 6 weeks (just dark mode, no other features)
- Risk: Feature is incomplete, customers want more

**High Scope + High Quality = Timeline Slips**
- Ship feature-complete and polished, but take longer
- Example: Real-time collaboration, polished, ships in 6 months
- Risk: Timeline slip damages credibility, opportunity window closes

### Decision Framework

When you have constraints, decide explicitly:

```
TRADE-OFF DECISION
═══════════════════════════════════════════════════

CONSTRAINT: Real-time collaboration must ship in Q3 (July)

OPTION A: Full Scope + Deadline (Quality suffers)
├─ Ship: Real-time cursors, comments, version history, offline support
├─ Timeline: July (as committed)
├─ Quality: Basic (buggy, UX not polished)
├─ Risk: Users frustrated by bugs, slower adoption

OPTION B: Reduced Scope + Deadline (Quality OK)
├─ Ship: Real-time cursors + comments (not offline, not version history)
├─ Timeline: July (as committed)
├─ Quality: Good (tested, polished)
├─ Risk: Incomplete feature, customers want more (backlog for later)

OPTION C: Full Scope + Quality (Timeline slips)
├─ Ship: All features, polished
├─ Timeline: October (3 months slip)
├─ Quality: Excellent
├─ Risk: Window of opportunity closes, competitors ship first

DECISION: Option B (Reduced Scope)
Rationale: Market window is July-September. If we slip to October, competitor ships. Better to ship partial feature in July, expand in Q4.
```

---

## Anti-Patterns: Bad Prioritization

### HiPPO-Driven ("Highest Paid Person's Opinion")

**Signal**: CEO likes an idea, it gets top priority despite low customer demand and high effort.

**Why it fails**: Optimization for executive opinion, not customer value. Low ROI work crowds out high-ROI work.

**Fix**: RICE scoring, customer research, transparent prioritization logic.

### Squeaky Wheel

**Signal**: Loudest customer or most senior sales rep gets features prioritized regardless of impact.

**Why it fails**: Vocal minorities are not representative. You optimize for vocal, not impactful.

**Fix**: Weigh all customer feedback equally. Use RICE or Opportunity Scoring to remove bias.

### Roadmap by Committee

**Signal**: Every department votes on features. Roadmap is compromise list where nothing has sufficient resources.

**Why it fails**: You ship 15 features at 6% capacity each, shipping slowly, not moving needle on any.

**Fix**: CPO (or single owner) makes final prioritization. Stakeholders provide input, but one person decides.

### Feature Parity Treadmill

**Signal**: Competitor ships feature, so you prioritize matching it, all quarter.

**Why it fails**: You're always 6 months behind. You never build your own moat.

**Fix**: Only match on must-haves. On performance features, leap-frog, don't match.

### Scope Creep

**Signal**: Feature starts as "add dark mode" (1 week), ends as "redesign entire theme system" (4 months).

**Why it fails**: You miss deadline. Scope expands and consumes time.

**Fix**: Define scope explicitly at planning. When new ideas emerge mid-project, add to backlog, don't expand scope.

