# Organizational Design & Structure

Org design is often treated as a box-drawing exercise. It's not. Org structure shapes information flow, decision-making speed, accountability, and career paths. The wrong structure makes execution harder and culture worse, no matter how talented your people are. The right structure enables execution and reinforces your operating model.

---

## Part 1: Org Design Principles

Before choosing a structure, understand the principles:

**Principle 1: Structure Follows Strategy**
Your org structure must enable the strategy. If you're pursuing speed and customer intimacy, a heavily centralized structure will fail. If you need cost control and consistency, a federated structure will fail. Structure must match what you're trying to do.

**Principle 2: Span of Control Must Be Realistic**
A manager can effectively direct 4-8 direct reports (typical range). More than that, quality of coaching declines. Fewer than that, you add management layers. The right span depends on:
- Complexity of roles (homogeneous roles → larger span)
- Maturity of reports (senior ICs → larger span; juniors → smaller span)
- Uncertainty/volatility (more uncertain → smaller span)
- Manager's experience (veteran → larger span; new manager → smaller span)

**Principle 3: Decision Rights Must Be Clear**
Org charts show reporting lines, not who makes decisions. For every important decision (hiring, budget, strategy, promotion, compensation), define: Who decides? Who has input? Who has veto? Who's informed? This is RACI (Responsible, Accountable, Consulted, Informed). Without clear decision rights, org structure creates friction, not flow.

**Principle 4: Cross-Functional Flow Matters More Than Reporting Lines**
A perfect org chart with broken cross-functional collaboration is worse than an imperfect chart with clear collaboration. Product needs to work closely with engineering and design. Sales needs to work closely with customer success and product. You can't hire your way out of bad cross-functional flow.

**Principle 5: Span Creates Throughput; Layers Create Quality**
Larger spans move decisions faster (fewer layers). More layers allow deeper specialization and better quality. You must choose your tradeoff: fast + rough, or slow + refined. Your strategy determines which.

---

## Part 2: Org Structure Archetypes

There are five main org structure patterns. Most companies use a hybrid, but one usually dominates.

### 1. Functional Organization

**Structure:** Organized by function/discipline (Engineering, Sales, Product, Finance, etc.)

```
CEO
├─ VP Engineering
│  ├─ Engineering Manager (Team A)
│  ├─ Engineering Manager (Team B)
│  └─ Engineering Manager (Team C)
├─ VP Sales
│  ├─ Sales Manager (Enterprise)
│  └─ Sales Manager (Mid-Market)
├─ VP Product
│  ├─ Senior PM (Platform)
│  └─ PM (Integrations)
└─ VP Finance
   └─ Controller
```

**When to use:**
- Early stage (pre-PMF)
- Deep technical work where functional expertise matters (biotech, infrastructure, fintech)
- Cost control is priority
- Low complexity customer needs

**Strengths:**
- Deep expertise and specialization
- Clear career paths within function
- Easy to control cost (scale by adding within function)
- Good for maintaining technical standards

**Weaknesses:**
- Slow cross-functional decision-making (everything escalates)
- Risk of siloed thinking (engineering doesn't understand customer)
- Product becomes a bottleneck
- Not customer-centric

**Span of Control:** 5-8 direct reports per manager typical

### 2. Divisional Organization (By Customer/Product)

**Structure:** Organized around customer segments or products (Enterprise Division, SMB Division, etc., or Product A Division, Product B Division)

```
CEO
├─ VP Enterprise Division
│  ├─ Sales lead
│  ├─ Customer Success lead
│  ├─ Product lead
│  └─ Operations lead
├─ VP SMB Division
│  ├─ Sales lead
│  ├─ Customer Success lead
│  ├─ Product lead
│  └─ Operations lead
└─ Shared Services
   ├─ Engineering (shared)
   ├─ Finance
   └─ HR
```

**When to use:**
- Multi-product or multi-segment strategy
- Different customer needs require different go-to-market
- Each division has P&L accountability
- Growth is priority

**Strengths:**
- Customer-centric (division owns entire customer journey)
- Clear P&L accountability
- Faster decision-making within division
- Easy to scale divisions independently
- Can pursue different strategies per division

**Weaknesses:**
- Duplication of functions (sales in each division)
- Shared engineering becomes bottleneck if not staffed right
- Conflicts over shared resources
- More expensive than functional

**Span of Control:** 3-5 divisions per CEO typical; 4-6 per divisional VP

### 3. Matrix Organization (By Function + Dimension)

**Structure:** People report to two managers — one functional (for discipline/expertise) and one product/customer (for execution)

```
CEO
├─ VP Engineering (reports to)
│  ├─ Senior Eng A (reports to)
│  └─ Senior Eng B (reports to)
│
├─ VP Product (dotted line reports to)
│  ├─ Product Manager (Platform) (dotted)
│  └─ Product Manager (Integrations) (dotted)
│
Engineering resources report functionally to VP Engineering,
but work on projects led by Product managers.
```

**When to use:**
- Complex product portfolio (multiple products, shared platform)
- Shared resources (engineering, design) across multiple product initiatives
- Need deep functional expertise AND product focus
- Scale beyond 100 people

**Strengths:**
- Optimal resource utilization (engineering shared across products)
- Deep functional expertise maintained
- Product focus + functional depth
- Balanced power (prevents silos)

**Weaknesses:**
- Confusion about who decides and who's accountable
- "Two bosses" creates stress and political maneuvering
- Slow decision-making if matrix not managed well
- Requires more sophisticated management culture

**Span of Control:** 4-6 per functional VP; 3-4 per product leader

**Critical:** In matrix, define decision rights explicitly. Who has final say on hiring? Product priorities? Budget allocation? Without clear RACI, matrix becomes chaos.

### 4. Network/Platform Organization

**Structure:** Loosely coupled autonomous teams connected through platforms/shared services

```
CEO
├─ Team A (autonomous product team)
│  └─ Has mini P&L, own hiring decisions
├─ Team B (autonomous product team)
│  └─ Has mini P&L, own hiring decisions
├─ Platform Engineering (shared)
│  └─ Maintains shared infrastructure, APIs
└─ Shared Services
   ├─ Finance, HR, Legal
   └─ Sales & Marketing (often)
```

**When to use:**
- Large-scale (500+ people), multiple products
- Need entrepreneurial teams with autonomy
- Shared platforms/infrastructure
- High-growth companies that need speed

**Strengths:**
- Speed (teams don't wait for central approval)
- Ownership & accountability (teams are entrepreneurs)
- Scales well (add teams without re-org)
- Attracts entrepreneurial talent

**Weaknesses:**
- Requires sophisticated planning (if teams are truly autonomous, how do they not collide?)
- Easy to lose strategic coherence
- Requires strong culture (what holds it together?)
- Hard to move people between teams
- Can amplify inequality (successful teams grow fast, struggling ones starve)

**Span of Control:** CEO has 6-10 team leads; each team is 8-15 people

### 5. Flat Organization

**Structure:** Minimal hierarchy. Most people report to CEO or there's one layer of management.

```
CEO
├─ Product Manager
├─ Senior Engineer
├─ Sales Person
├─ Customer Success Manager
├─ Finance/Operations
└─ Junior Hires (report to senior people, not managers)
```

**When to use:**
- Very early stage (pre-50 people)
- Simple product/market
- High trust culture
- Everyone hiring and doing many roles

**Strengths:**
- Speed
- Clarity (fewer layers)
- Low overhead
- Everyone touches everything

**Weaknesses:**
- Doesn't scale (beyond 30-40 people becomes chaos)
- No room to grow for individual contributors
- CEO becomes bottleneck
- Hard to develop depth

**Span of Control:** CEO may have 8-12 reports in flat org (high, but typical at early stage)

---

## Part 3: Org Design Decision Framework

### Step 1: Map Strategic Priorities to Required Structure

```
STRUCTURE DECISION FRAMEWORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRATEGIC QUESTION: "How do we organize around our strategy?"

STRATEGIC IMPERATIVE                | STRUCTURE IMPLICATIONS
────────────────────────────────────┼──────────────────────────────────────
We must move fast & be              | Divisional or Network.
customer-centric                    | Minimize layers. Autonomous teams.
                                    | Cross-function must be tight.

We must be cost-efficient           | Functional or Matrix.
                                    | Centralize shared services. Eliminate duplication.
                                    | Larger spans of control.

We must maintain technical          | Functional or Matrix.
excellence (engineering-heavy)      | Strong functional leadership. Career paths for ICs.
                                    | Don't dilute engineering with non-technical mgmt.

We must scale without               | Divisional or Network.
re-organizing constantly            | Build repeatable team model.
                                    | Enable autonomy.

We must coordinate                  | Matrix or Network with strong platforms.
across multiple products            | Shared engineering/product platforms.
                                    | Clear handoffs and APIs.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 2: Define Span of Control by Role

```
SPAN OF CONTROL BY ROLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CEO

Early stage (20-30 people):     CEO has 6-8 direct reports
                                (flat: product, sales, eng, ops, finance, maybe more)

Growth stage (50-100 people):   CEO has 4-5 direct reports
                                (VP Sales, VP Eng, VP Product, CFO, maybe COO)

Scale (200+ people):            CEO has 3-4 direct reports
                                (Chief Revenue Officer, VP Engineering, VP Product, CFO)

Engineering Manager

Early stage (high junior %):    4-5 reports
Growth stage (mixed):           5-6 reports
Scale (experienced team):       6-8 reports

Sales Manager

Typical:                        5-8 reps (sales is higher span)
Good performers:                Up to 10 (but starts declining quality)

Product Manager

Manages people:                 1 person reporting
(Most PMs have no directs; Product Manager ≠ Engineering Manager)

Cross-functional collaboration should NOT be through reporting line.
Use working groups, guilds, or councils instead.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 3: Design Decision Rights (RACI)

For every important decision, populate RACI:

```
SAMPLE RACI: WHO DECIDES ON HIRING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DECISION: Should we hire this candidate?

HIRING DECISION RACI MATRIX
────────────────────────────────────────────────────────────────
                               | R | A | C | I |
────────────────────────────────────────────────────────────────
Hiring Manager (direct report)  | R | — | — | — |  ← Does the work
Functional Lead (VP Eng)        | — | A | — | — |  ← Signs off, holds quality bar
HR / People Partner             | R | — | C | — |  ← Screens, may object
Finance (for budget allocation) | — | — | C | I |  ← Consulted on cost
CEO (for senior roles)          | — | A | C | — |  ← Signs off on director+ roles
────────────────────────────────────────────────────────────────

R = Responsible (does the work; can be multiple)
A = Accountable (final decision/sign-off; single person)
C = Consulted (has opinion, must be asked)
I = Informed (kept in loop, but no decision power)

COMMON DECISIONS TO MAP:
  • Hiring (by level & function)
  • Firing / Performance management
  • Promotion / leveling
  • Compensation & raises
  • Budget allocation
  • Strategy & direction
  • Cross-functional prioritization
  • Performance metrics / OKRs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Part 4: Reorg Playbook

When it's time to reorganize, follow this sequence. Reorgs are high-risk and high-impact. Mess them up and you lose people, trust, and momentum.

### Pre-Reorg Planning (Weeks -2 to 0)

**1. Define the Why** — Why are we reorganizing? (Growth, capability gaps, underperformance, new strategy) Be specific. The why determines what you're optimizing for.

**2. Model 3-5 Options** — Don't propose one org chart. Model 3-5 options, score them against decision criteria (speed, cost, scalability, talent retention, cross-functional flow).

**3. Stress-Test for Retention Risk** — Which people might leave under each option? Where are the sensitivities?
- People being moved to new managers (risk: rebuilding trust)
- People losing span of control (risk: feels like demotion)
- People losing direct access to leadership (risk: feels sidelined)
- People whose function is being restructured (risk: unclear future)

**4. Prepare Talking Points** — For each role affected, be ready to explain:
- Why their role/team is structured this way
- What's different from before
- What's the same (reporting line, scope, compensation)
- Why this is better for them + company

### Communication (Day 1-2)

**1. All-Hands First** — Announce the new structure to everyone in a town hall, simultaneously. No surprises in 1:1s first. All-hands simultaneously, then 1:1s.

**2. One-on-One With Everyone Directly Impacted** (same day, after all-hands) — Meet with everyone whose role or manager changes. Be specific:
- What's their new role/reporting line?
- What doesn't change (compensation, title, authority)?
- What are new expectations?
- What are they worried about? (Answer honestly)

**3. Manager Communication** — Equip all managers (not just new ones) with the talking points. They'll get asked by their teams. They should have consistent answers.

### Implementation (Weeks 1-4)

**1. Establish New Routines Immediately** — First meeting under new structure should happen within 3 days. Show the new reporting lines are real.

**2. Reset 1:1s** — Especially for people with new managers. First 1:1 should cover:
- How they work best (learning style, feedback style, decision-making preferences)
- What they want to achieve in next 90 days
- Expectations (hours, availability, communication)
- Questions they have about the role

**3. Cross-Functional Sync** — If the reorg affected collaboration (e.g., moved product under engineering), establish clear working relationships between product and engineering immediately. Don't wait.

**4. Monitor Early Signals** — Track:
- Who goes quiet in meetings (disengaged)
- Who starts looking for other jobs (early warning: resume updates on LinkedIn)
- Who reaches out to HR about exit conversations
- Engagement survey / pulse survey drops

Act fast on early warning signals. A conversation in week 2 might prevent a departure in month 3.

### Post-Reorg (Weeks 4-12)

**1. Check-In Cycle** — Every high-risk person (retention risk, new manager, big role change) gets a skip-level check-in from their skip (skip-level = their manager's manager) at week 4 and week 8.

**2. Pulse Surveys** — Light engagement pulse survey at week 2 and week 4. Are people confused about roles? Do new reporting lines feel weird? Address fast.

**3. Early Re-adjustment** — Be willing to adjust in the first 4 weeks if the structure isn't working. If a reporting line creates confusion or handoff delays, fix it.

**4. Celebrate Wins** — As soon as the new structure enables a win (faster decision, better collaboration, successful project launch), highlight it. Link the win to the reorg.

---

## Part 5: Org Design Output & Recommendations

### Template

```
ORGANIZATIONAL DESIGN RECOMMENDATION
═════════════════════════════════════════════════════════════

CURRENT STATE
  • Structure type: [e.g., Functional]
  • Headcount: [Total by function]
  • Key pain points: [What's broken in current org?]
  • Span of control analysis: [Are spans right-sized?]
  • Cross-functional flow: [Where is collaboration failing?]

STRATEGIC IMPERATIVES
  • Growth rate: [e.g., 100% YoY]
  • Customer complexity: [Simple vs. high-touch vs. enterprise]
  • Product complexity: [Single vs. multi-product]
  • Key talent constraints: [What do we struggle to hire/retain?]

DESIGN ALTERNATIVES EVALUATED
  Option A: [Structure type] — Pros: [X, Y] Cons: [A, B] — Fit: [70%]
  Option B: [Structure type] — Pros: [X, Y] Cons: [A, B] — Fit: [85%]
  Option C: [Structure type] — Pros: [X, Y] Cons: [A, B] — Fit: [60%]

RECOMMENDED STRUCTURE
  Type: [e.g., Matrix with clear product dimensions]
  Rationale: [Why this option?]

PROPOSED ORG CHART
  [ASCII org chart or structured description]

KEY ROLE CHANGES
  • [Person] moving from [Old reporting line] to [New reporting line]
  • [New role being created]
  • [Role being consolidated]

SPAN OF CONTROL CHANGES
  • [Manager's span going from X to Y]
  • Impact: [Better? Worse?]

DECISION RIGHTS (RACI)
  [Key RACI matrices for critical decisions]

RETENTION RISK ASSESSMENT
  • High risk: [Who? Why? Mitigation?]
  • Medium risk: [Who? Why? Mitigation?]

IMPLEMENTATION PLAN
  • Week 1: [All-hands announcement + 1:1s]
  • Week 2: [New routines established]
  • Month 1: [Monitor and adjust]
  • Month 3: [Full stabilization expected]

EXPECTED OUTCOMES
  • Decision-making speed: [Faster/Same/Slower and why]
  • Cross-functional collaboration: [Better/Same/Worse and how]
  • Cost structure: [Higher/Same/Lower and why]
  • Scalability: [Can add teams/people without re-org]

KILL CONDITIONS
  If [specific signal] by [date], we revert or re-adjust structure.
═════════════════════════════════════════════════════════════
```

---

## Quality Gates for Org Design

**Gate 1: Strategy Alignment** — Does the proposed org structure directly support the strategic priorities? If you changed the strategy, would the structure change? If the answer is "no," the design isn't driven by strategy, it's politics.

**Gate 2: Span Reality** — Are spans of control realistic? Have you accounted for manager experience, team maturity, complexity? If you're proposing a first-time manager with 10 reports, you've already lost.

**Gate 3: Decision Rights Clarity** — For every important decision, is it clear who decides? If RACI is unclear, the org will create conflict, not execution.

**Gate 4: Retention Sensitivity** — Have you identified who might leave? Is there a mitigation plan? If retention hasn't been thought through, the reorg will fail.

**Gate 5: Execution Readiness** — Can you implement this? Do you have the communication plan, the timing, the manager readiness? If you're winging the implementation, you're wasting the design work.

