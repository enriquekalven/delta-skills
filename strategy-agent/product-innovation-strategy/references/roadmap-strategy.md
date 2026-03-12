# Roadmap Strategy & Horizon Planning

A roadmap is not a feature list published by product managers. A roadmap is an allocation of organizational capacity (people, time, money) across strategic priorities, sequenced in time, with clear owners and dependencies. This reference operationalizes roadmap strategy across three horizons.

---

## Three Horizons Product Planning

Coined by Baghai, Coley, and White, the three horizons framework separates product strategy into distinct time windows with different logics:

### Horizon 1: Optimize What Works (0-12 months)

**Definition**: Products and features that generate today's revenue and serve today's customers.

**Goal**: Maximize cash generation. Improve margins. Defend competitive position.

**What Goes Here**:
- Current products: new versions, releases, improvements
- Defensible features: what keeps customers renewing and reducing churn
- Competitive responses: must-have features to remain viable
- Operational improvements: reduce technical debt, improve reliability, reduce support costs

**Metrics**:
- Revenue, growth rate, retention, NPS
- Gross margin, customer satisfaction, churn rate
- Feature adoption, time-to-value

**Team Composition**:
- Seasoned engineers familiar with the codebase
- Experienced product managers who know the customer deeply
- Full go-to-market team (sales, marketing, CS)

**Anti-Pattern**: Spending >80% of engineering on H1 creates zombie company. You defend today but have no future.

**Success Bar**:
- Maintain or grow H1 revenue
- H1 retention stable or improving
- Gross margin stable or improving
- Competitive position defended (not losing share to new entrants)

### Horizon 2: Build Adjacent (12-24 months)

**Definition**: New products or features targeting adjacent customer segments or new jobs-to-be-done for existing customers.

**Goal**: Grow beyond existing market. De-risk future revenue. Find adjacent repeatable models.

**What Goes Here**:
- Expansion features for existing customers (new modules, new use cases)
- New customer segments with similar problems (e.g., mid-market vs. enterprise)
- Adjacent product lines or tiers (e.g., freemium to paid, professional to consumer)
- New go-to-market channels (e.g., self-serve vs. sales-led)
- Extensions to the core platform (e.g., APIs, integrations, ecosystem)

**Metrics**:
- Time to PMF, retention curves, viral coefficient
- Attach rate (% of H1 customers adopting H2 offering)
- Customer acquisition efficiency in new segment
- Time to break-even within segment

**Team Composition**:
- Mixed: 1-2 experienced engineers + 1-2 growth-stage engineers
- Product managers with some expertise in new area
- Go-to-market person focused on new segment
- Often: small, autonomous team with fewer dependencies on H1

**Anti-Pattern**: H2 products that require H1 product to be rebuilt. H2 needs to be somewhat independent.

**Success Bar**:
- First repeatable customer acquisition in new segment
- Retention curve showing shelf (not continuous decline)
- Clear roadmap to attachment or standalone viability
- Evidence of customer pull, not just internal build

### Horizon 3: Place Options on the Future (18-36 months)

**Definition**: Explorations into future market needs, emerging technologies, or potential disruptions. High-risk, high-upside bets.

**Goal**: Build optionality against disruption. Learn about emerging needs. Place small bets on futures that could matter.

**What Goes Here**:
- New technologies (AI, blockchain, AR, quantum, biotech, etc.)
- Adjacent industries or verticals (expand TAM 10x)
- Emerging customer needs (new job-to-be-done you haven't heard yet)
- Defensive positions against potential disruptors
- Partnerships with complementary companies for future integrations

**Metrics**:
- Learning per dollar spent (did we reduce uncertainty?)
- Concepts tested, hypotheses invalidated, insights generated
- Partnerships formed, ecosystems explored
- Time-to-thesis (how long did it take to learn enough to decide go/no-go)

**Team Composition**:
- Exploration: researchers, designers, strategists
- Learning: customer research, technical experiments
- Often: partnerships, ecosystem building, external investment

**Anti-Pattern**: Calling everything "innovation" and funding 20 H3 bets. Should be small and bounded.

**Success Bar**:
- Clarity on whether the space is real (customer need exists)
- Clarity on whether we can win (defensible advantage possible)
- Clarity on scale (if real, how big could it be)
- Decision to either graduate to H2, continue exploring, or shut down

### Resource Allocation Across Horizons

A healthy product organization distributes engineering capacity and management attention across all three:

**Typical Allocation**:
- **H1**: 70% of engineering, 80% of product, 90% of sales/marketing
- **H2**: 20% of engineering, 15% of product, 10% of sales/marketing
- **H3**: 10% of engineering, 5% of product, <1% of sales/marketing

*Calibration*: This assumes a mature product with strong competitive moat. Early-stage products skew toward H3 (most is learning). Dying companies overweight H1 (harvest mode).

**Reallocation Triggers**:
- If H1 revenue growth stalls and H2 shows PMF signals, rebalance: move 15% of H1 engineers to H2.
- If H2 is approaching H1 scale, graduate product to H1 allocation and create new H2.
- If H3 bet shows promise, graduate to H2 and explore new H3.

---

## Now/Next/Later Framework Operationalized

Now/Next/Later is a simplified three-bucket roadmap framework designed for transparency without commitment.

**Now** (0-90 days): Specific features, releases, with clear completion dates. Team is committed. This is a promise.

**Next** (90-180 days): Thematic direction, customer problems to solve, prioritized but not detailed. Ordering may shift based on learnings.

**Later** (180+ days): Strategic directions and longer-term bets. Not scheduled. High uncertainty.

### Operationalization

**Building the Now Bucket**:
1. Start with strategic priorities (from portfolio diagnostic, competitive position, revenue goals)
2. Translate into specific customer outcomes ("reduce time to onboard customers from 2 weeks to 3 days")
3. Decompose into features or technical work ("build configuration wizard", "create API for provisioning")
4. Estimate effort and assign owners
5. Build release milestone: target ship date, dependencies, success criteria
6. **Commit**: Do not move things in/out of Now without material change. Now is a promise to customers and team.

**Building the Next Bucket**:
1. Pool of customer problems that are real but not yet scoped
2. Organize by theme: "Improve analytics capabilities", "Expand to SMB segment", "Build integration ecosystem"
3. For each theme, list the problems and prioritization logic
4. Do not estimate in detail. Do not commit to timeline.
5. Review quarterly and graduate top items to Now for next cycle

**Building the Later Bucket**:
1. Strategic directions (e.g., "Build AI-powered workflows")
2. Market opportunities (e.g., "Enter Asia market")
3. Longer-term bets (e.g., "Develop adjacent product line")
4. Listed without timeline. Used to guide horizon planning and capital allocation, not execution.

### Now/Next/Later Release Rhythm

**Monthly Cadence Example**:
- **Month 1**: Plan Now. Define 4-6 specific outcomes, feature work, estimates. Month 1 becomes committed Now.
- **Month 2**: Execute Now. Graduation from Next to Now happens as Now completes. New Next items emerge from customer feedback.
- **Month 3**: Quarter planning. Full review of Portfolio Diagnostic. Adjust strategic priorities. Rebalance H1/H2/H3. New Now/Next/Later for next quarter.

This keeps the roadmap fresh without constantly shifting commitments.

---

## Roadmap Types and When to Use Each

### 1. Timeline-Based Roadmap (Gantt Chart)

**Format**: Features/releases on Y-axis, time on X-axis. Bars show when each ships.

**Best For**: Communicating specific release schedules to sales, customers, investors. High commitment and clarity on timing.

**Strengths**:
- Clear, easy to understand
- Sales can tell customers "it ships in Q3"
- Investors see specific delivery milestones
- Team accountability is clear

**Weaknesses**:
- Assumes predictable delivery (often wrong)
- Encourages deadline-driven behavior over outcome-driven
- Creates blame when timeline slips
- Doesn't show dependencies or risk

**Anti-Pattern**: Showing timeline roadmap as certain when large uncertainty exists. Customers then feel betrayed when timeline shifts.

**Example Format**:
```
Feature                  Q2      Q3      Q4
Advanced Analytics       ├─────┤
Custom Workflows               ├─────────┤
API v2.0                ├─────────────┤
Mobile App                         ├─────┤
```

### 2. Kanban-Style Roadmap

**Format**: Columns for "Backlog", "In Progress", "In Testing", "Shipped" or "Ready", "In Development", "Shipped". Cards show features.

**Best For**: Engineering teams. Shows work in motion and current priorities without committing to timeline.

**Strengths**:
- Transparent on current work
- No false commitment to dates
- Easy to see blockers and dependencies
- Flexible as priorities change

**Weaknesses**:
- Does not communicate roadmap vision or strategy
- Hard to show multi-quarter planning
- Customers/investors may not understand what's coming

**Anti-Pattern**: Using kanban as the roadmap shared with customers/board. Too low-level. Use as internal tracker, share summarized version externally.

### 3. Outcome-Based Roadmap

**Format**: Themes or customer jobs, with success metrics and priority. Does not specify features.

**Best For**: Product-led organizations. Emphasizes customer outcomes over delivery commitments.

**Strengths**:
- Focuses team on impact, not features
- Flexible how to achieve outcome (teams can choose approach)
- Less gaming (team focused on outcome, not shipping feature)
- Easier to pivot if approach isn't working

**Weaknesses**:
- Requires mature product org and clear metrics
- Longer feedback cycles (you don't know if you succeeded until later)
- Harder for sales to communicate (no specific feature to sell)

**Example Format**:
```
THEME: Accelerate Customer Onboarding
Success Metric: Reduce time-to-first-value from 14 days to 7 days
Current Approach: [Hypothesis on what will work]
Owner: [Name]
Timeline: Q3 (endpoint, not start/end date of specific features)
Resources: [Team size]

THEME: Build Expansion Revenue
Success Metric: Increase NRR from 110% to 125%
Current Approach: [Hypothesis]
Owner: [Name]
Timeline: Q2-Q4
Resources: [Team size]
```

### 4. Customer Journey Roadmap

**Format**: Organized by stage of customer journey (awareness, onboarding, activation, expansion, retention). Features/initiatives mapped to where they impact the journey.

**Best For**: Product teams focused on customer experience and lifecycle. Good for retention-focused strategies.

**Strengths**:
- Aligns team around customer experience, not internal features
- Identifies gaps in journey
- Easy to see where work is concentrated (e.g., onboarding vs. retention)
- Helps prioritize based on customer impact

**Weaknesses**:
- Requires clear definition of customer journey
- Can be cumbersome if journey has many stages

**Example Format**:
```
AWARENESS         ONBOARDING        ACTIVATION        EXPANSION         RETENTION
├─ Improved       ├─ Email guides    ├─ Workflow       ├─ Add-ons        ├─ Health tracking
│  messaging      │                  │  templates      │  module          │
│                 ├─ Setup           ├─ Success        ├─ Integration     ├─ Support hub
│                 │  wizard           │  metrics        │  marketplace     │
```

### 5. Theme-Based Roadmap

**Format**: Strategic themes (e.g., "Become the #1 AI-powered platform", "Expand to SMB", "Build ecosystem"), with key initiatives under each theme, ordered by priority.

**Best For**: Executive audiences, board presentations. Shows strategic direction without feature-level detail.

**Strengths**:
- Communicates strategy clearly
- Flexible on implementation
- Easy to discuss trade-offs ("do we invest in SMB or enterprise?")
- Good for explaining why work matters

**Weaknesses**:
- Lacks specificity on what ships and when
- Requires supporting detail (output-based or Gantt roadmap) for execution teams

**Example Format**:
```
THEME 1: Become #1 AI-Powered Platform (40% of engineering)
├─ Initiative: Build AI-driven workflow automation
├─ Initiative: Launch prompt engineering tools
├─ Initiative: Build competitive AI copilot

THEME 2: Expand into SMB (30% of engineering)
├─ Initiative: Build self-serve onboarding
├─ Initiative: Create SMB-friendly pricing tier
├─ Initiative: Develop SMB integrations

THEME 3: Build Ecosystem & Platform (20% of engineering)
├─ Initiative: Public API
├─ Initiative: Partner marketplace
├─ Initiative: Developer tools and docs

THEME 4: Defend Market Position (10% of engineering)
├─ Initiative: Competitive feature parity
├─ Initiative: Customer retention programs
```

---

## Theme-Based Roadmapping Methodology

Theme-based roadmapping is best for complex portfolios and aligns teams around strategic outcomes. This is the methodology to use when you've done the portfolio diagnostic and need to communicate roadmap strategy.

### Step 1: Identify Strategic Themes (Portfolio Level)

From your portfolio diagnostic and strategic priorities, identify 3-5 themes. Each theme should answer: "What capability, customer segment, or competitive position are we building?"

**Examples**:
- "Own the SMB market" (segment)
- "Become the AI copilot" (capability)
- "Defend against [competitor]" (competitive)
- "Expand adjacent into [vertical]" (market)
- "Build ecosystem defensibility" (moat)

**Test**: If you removed one theme, would the strategy still be coherent? If not, it's not a core theme.

### Step 2: Map Initiatives to Themes

For each theme, list 3-5 key initiatives. These are multi-quarter efforts that roll up into the theme.

**Example Theme: "Own the SMB Market"**
- Initiative 1: Build self-serve onboarding (improves SMB ability to get value without sales support)
- Initiative 2: Create SMB-friendly pricing tier (reduces friction to entry)
- Initiative 3: Develop SMB-focused integrations (SMB buyers care about integration to their existing stack)
- Initiative 4: Build SMB marketing motion (case studies, webinars, verticalized content)

**Test**: For each initiative, can you articulate why it moves the needle on the theme? If not, it doesn't belong.

### Step 3: Allocate Resources by Theme

Assign percentage of engineering and product capacity to each theme:

```
Theme                          Engineering %    Product %
────────────────────────────────────────────────────────
Own SMB Market                      35%           40%
Become AI Copilot                   30%           35%
Defend Competitive Position         20%           20%
Build Ecosystem                     15%            5%
────────────────────────────────────────────────────────
TOTAL                              100%          100%
```

### Step 4: Sequence Initiatives (Now/Next/Later)

For each theme, identify which initiatives go into Now, Next, Later:

**Now (Next 90 days)**: Initiatives that unblock other work or show early proof of concept. Should complete at least one initiative per theme in Now.

**Next (90-180 days)**: Follow-on initiatives from Now. Refinements based on learning.

**Later (180+ days)**: Longer-term capability building or stretch bets.

### Step 5: Create Communication Roadmaps

From the theme roadmap, generate simplified roadmaps for different audiences:

**Board Roadmap**: Themes only. Resources allocated. Timeline at theme level (when does "Own SMB" go from exploration to revenue contributor).

**Engineering Roadmap**: Initiatives + key features. Sequence and dependencies. Timeline for Now bucket.

**Sales Roadmap**: Specific features with dates (timeline roadmap) only for items they can sell. Themes for context.

**Customer Roadmap**: Themes in customer language ("We're building AI workflows", "Expanding to support your SMB growth"). Outcomes-focused, not feature-focused.

---

## Stakeholder Alignment Protocol

A roadmap only works if stakeholders believe in it and feel heard. This protocol ensures alignment.

### Phase 1: Input Gathering (Week 1)

**Who to Ask**:
- Sales leadership: what features would help you win more deals?
- Customer success: what would improve retention and expansion?
- Engineering leadership: what technical debt must we address?
- Finance: what revenue targets are we committing to?
- CEO/Board: what strategic priorities are we committing to?

**How to Ask**:
- One-on-one conversations, not survey. Surveys produce noise.
- Ask "what's the problem we need to solve" not "what features do you want"
- Listen for themes: are multiple people saying the same problem?

### Phase 2: Theme Development (Week 2)

Product + CPO synthesize inputs into 3-5 themes. Each theme has:
- Problem statement: what are we trying to solve?
- Success metric: how will we know we succeeded?
- Rough resource estimate: how much engineering do we expect to invest?

Present to leadership team and gather feedback. Not for final approval — for input and context.

### Phase 3: Resource Negotiation (Week 3)

With CPO, CTO, and CFO:
- "We want to allocate 35% to SMB. That means we move 35% away from something. What do we move away from?"
- "We want to build this feature. It requires this team. That team today is doing X. How do we handle that transition?"

This is the hard part. Forces real trade-offs. Once you've done this, the roadmap is credible.

### Phase 4: Finalization (Week 4)

Present the roadmap. For each stakeholder, connect their ask to the roadmap:
- Sales: "You wanted X. It's in the Next bucket. Timeline TBD but we're planning Q3 entry."
- Customer Success: "You need Y. It's in the Now bucket. Ships in 45 days."
- Finance: "Revenue target Z. Here's how the roadmap supports it..."

Make trade-offs explicit: "We deprioritized A in favor of B because [reason]."

### Phase 5: Quarterly Check-ins

Once a quarter (at most):
- Are themes still relevant?
- Has market shifted and changed priorities?
- Are we learning things that invalidate our approach?

If Yes to any, propose updated roadmap. Don't over-rotate — roadmap should be sticky enough to execute against.

---

## Roadmap Communication Templates

### Board Roadmap Template

```
PRODUCT ROADMAP OVERVIEW
═══════════════════════════════════════════════════

STRATEGIC CONTEXT
Market Opportunity: [Size, growth, competitive context]
Current Position: [Where we stand, why]
3-Year Vision: [Where we're going]

PORTFOLIO HEALTH
[Product Health Scorecard summary across key products]

ROADMAP THEMES (Resource Allocation)
└─ Theme 1: [Description] — [% of resources]
   Status: [On track / At risk / Need decision]
   Key Milestones: [When does this contribute to revenue?]

└─ Theme 2: ...

└─ Theme 3: ...

KEY DEPENDENCIES & RISKS
[What has to go right? What could derail us?]

COMPETITIVE MOAT PROGRESS
[How does this roadmap strengthen competitive position?]
```

### Engineering Roadmap Template

```
ROADMAP BREAKDOWN (Now/Next/Later)
═══════════════════════════════════════════════════

NOW (Next 90 Days) — [Total Engineering %]
└─ Initiative: [Name]
   Features:
   ├─ Feature A — Owner: [Name] — Complete by: [Date]
   ├─ Feature B — Owner: [Name] — Complete by: [Date]
   Dependencies: [What must complete first?]
   Risk: [What could block this?]

└─ Initiative: [Name]
   ...

NEXT (90-180 Days) — [Total Engineering %]
└─ Initiative: [Name]
   Status: [Design phase / Ready to start / Blocked]
   ...

LATER (180+ Days) — [Total Engineering %]
└─ Strategic Direction: [Description]
   Current Learning: [What do we need to learn first?]
```

### Sales/Customer Roadmap Template

```
WHAT'S COMING FOR YOUR BUSINESS
═══════════════════════════════════════════════════

SHIPPING SOON (Next 90 Days)
├─ Feature A — Solves: [Customer problem] — Available: [Month]
├─ Feature B — Solves: [Customer problem] — Available: [Month]

COMING NEXT (90-180 Days)
├─ Capability X — Why: [Why we're building this]
├─ Capability Y — Why: [Why we're building this]

HOW YOU CAN INFLUENCE PRIORITIES
[Link to feature request process. How to vote on priorities.]

QUESTIONS?
[Contact info for product team]
```

---

## Anti-Patterns to Avoid

### Feature Factory

Team is shipping features at high velocity but none of them move the needle on strategic metrics (growth, retention, expansion). Roadmap is a backlog of feature requests. No theme. No strategic coherence.

**Signal**: "We shipped 47 features this quarter!" Retention unchanged. Growth rate unchanged. NPS flat.

**Fix**: Pause. Audit shipped features. Which ones did customers ask for? Which ones changed behavior? Rebase roadmap around strategic themes with measurable outcomes.

### Death by Roadmap

Roadmap is sacred commitment. Sales promised X. Board approved X. Now it's Q3 and market dynamics have changed, but we ship X anyway because it's on the roadmap.

**Signal**: Shipping features nobody wants because "we committed to them."

**Fix**: Quarterly roadmap review with explicit decision gates: "Does this theme still make sense? Should we pivot?" Roadmap is a guide, not a law.

### Shiny Object Syndrome

Roadmap changes weekly based on latest customer conversation, competitor move, or executive idea. Team is whipsawed. Nothing ships.

**Signal**: "Wait, I thought we were doing X, now we're doing Y?"

**Fix**: Stabilize the Now bucket. It's locked. Next bucket can shift. Later bucket definitely shifts. Quarterly review is the natural re-planning moment.

### Roadmap by Committee

Every stakeholder gets to add their priority. Roadmap becomes a compromise wish list. Nothing important gets 40% of engineering; everything gets 10%.

**Signal**: 15 themes, each allocated 5-7% of engineering. No theme gets sufficient resources to move the needle.

**Fix**: Force hard prioritization. "We can do 3-4 themes well or 15 themes poorly. Which 3-4?" Once chosen, resources flow to those themes.

