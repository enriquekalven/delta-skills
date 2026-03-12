# Resource Allocation Governance Framework

Governance is the system that makes capital allocation decisions predictable, accountable, and disciplined. Without governance, capital allocation becomes political. With governance, it becomes science.

This framework designs the people, processes, and decision rights that prevent capital waste and enforce ROIC discipline.

---

## Core Principle: Transparency & Consistency

**Governance only works if:**
1. **Rules are public.** Everyone knows what the decision-making criteria are, before a request is made.
2. **Rules are applied consistently.** The same investment that gets approved under one rule can't be rejected because of politics.
3. **Decisions are reversible.** Bad investments can be killed; good investments can be scaled. Nothing is locked in forever.
4. **Accountability is clear.** One person owns each decision. If it goes wrong, it's clear who's responsible.

---

## Step 1: Establish Investment Authority Levels

Define who can approve capital investment at each size. This prevents small decisions from clogging up the CEO's inbox and big decisions from being made by junior staff.

### Authority Matrix by Investment Size

| Investment Size | Business Unit Capex | Strategic Capex | M&A | Software/Tech | Approval Authority |
|---|---|---|---|---|---|
| **< $0.5M** | Approve | Approve | N/A | Approve | Business Unit Head |
| **$0.5M - $2M** | Approve | Requires Review | N/A | Requires Review | Business Unit Head + CFO |
| **$2M - $10M** | Requires Review | Requires Review | Requires Review | Requires Review | CEO + CFO + COO |
| **$10M - $25M** | Requires Review | Requires Board Committee | Requires Board Committee | Requires Board Committee | Board Finance Committee + CEO |
| **> $25M** | Requires Board Approval | Board Approval | Board Approval | Board Approval | Full Board |

**Key principles:**
- **Routine maintenance capex** (keep the lights on): Lower bar, faster approval
- **Strategic capex** (new markets, new capabilities): Higher bar, requires thesis
- **M&A** (inorganic growth): Highest bar, requires independent valuation
- **Exceptions** (fast-track opportunities): Pre-defined exception process

### Define Thresholds for Your Company

Absolute dollar amounts vary by company size. Use these templates:

**$100M+ revenue company:**
- < $1M: BU Head
- $1-5M: CFO
- $5-15M: CEO
- $15M+: Board

**$500M+ revenue company:**
- < $5M: BU Head
- $5-20M: CFO
- $20-50M: CEO
- $50M+: Board

**Startup (<$50M revenue):**
- < $0.5M: CEO
- $0.5-2M: CEO + Board
- > $2M: Board + VC investors

---

## Step 2: Design the Capital Committee

**Purpose:** Monthly or quarterly review of pending capital investments, performance of past investments, and reallocation of underperforming capital.

### Committee Composition

**Permanent Members:**
- **CEO** (Chair) — Owns overall capital strategy, breaks ties
- **CFO** — Runs capital planning, models financials, enforces discipline
- **COO** — Owns execution, operability of investments
- **Chief Strategy Officer** or equivalent — Connects capital strategy to competitive strategy
- **Board Finance Committee Chair** or equivalent — Governance/fiduciary lens

**Rotating Members (1 per meeting):**
- **Business Unit Head** — For units with pending investments or underperformance
- **Head of M&A** or equivalent — If acquisitions are on agenda
- **Head of Technology/Innovation** — For tech/software investments

**Frequency:**
- Monthly: In companies with active capex pipeline
- Quarterly: Mature companies with stable capex
- As-needed: Between meetings for >$25M investments

### Capital Committee Charter

```
CAPITAL ALLOCATION COMMITTEE CHARTER
═══════════════════════════════════════

PURPOSE
- Allocate capital across competing uses to maximize ROIC
- Review performance of past investments vs. thesis
- Rebalance capital away from underperforming uses
- Ensure consistent application of investment criteria
- Advise CEO on funding strategy (debt, equity, retained earnings)

AUTHORITY
- Approve investments up to $[X]M
- Recommend to Board for investments > $[X]M
- Override or kill investments mid-stream if performance deteriorates
- Adjust hurdle rates if market conditions shift
- Approve exceptions to standard investment process

DECISION-MAKING RULES
- Decisions require [X] members present
- Decisions are made by consensus where possible; [Chair] breaks ties
- Disagreements are noted in minutes; Board Finance Committee reviews contested decisions
- All investments ≥ $[X]M require written investment thesis before approval
- All investments are reviewed against established hurdle rate criteria before approval

RESPONSIBILITIES
- CEO: Sets overall capital strategy, breaks ties, represents to Board
- CFO: Prepares analysis, models returns, tracks vs. thesis
- COO: Assesses execution risk, realism of timeline and budget
- CSO: Assesses strategic fit, competitive context, option value
- BU Heads: Present investments, defend thesis, commit to ownership

INFORMATION REQUIRED FOR APPROVAL
- Investment thesis (if >$[X]M)
- ROIC model with sensitivity analysis
- Risk assessment and kill triggers
- Owner and accountability
- Milestones and leading indicators
- Competitive / strategic context

CADENCE
- Monthly: New investment approvals, performance reviews
- Quarterly: ROIC realization vs. thesis, reallocation decisions
- Annually: Strategy refresh, hurdle rate review, capital structure target review

ESCALATION
- Investments requiring Board approval are escalated with [X] weeks notice
- Contested decisions go to Board Finance Committee
- Exceptions to standard process require CEO approval + disclosure to Board
═══════════════════════════════════════
```

---

## Step 3: Stage-Gate Investment Process

Not every investment gets approved at once. Large investments progress through gates, with decision points at each stage.

### Generic Stage-Gate Process

```
STAGE 1: CONCEPT & BUSINESS CASE (Week 0-4)
│
├─ Write investment thesis (one-page initial hypothesis)
├─ Estimate capital, timeline, expected ROIC
├─ Identify key risks and kill criteria
├─ Present to Capital Committee for go/no-go on further development
│
└─ Gate 1 Decision: Proceed to Stage 2? YES / NO / REWORK

STAGE 2: DETAILED ANALYSIS (Month 1-3)
│
├─ Build detailed financial model (5-year)
├─ Run sensitivity analysis
├─ Deep-dive on competitive landscape
├─ Detailed implementation plan with milestones
├─ Risk assessment and mitigation plans
├─ Present to Capital Committee for approval in principle
│
└─ Gate 2 Decision: Approve $[M] for Stage 3? YES / NO / REWORK

STAGE 3: EXECUTION (Month 3-12)
│
├─ Commit capital for implementation
├─ Monthly tracking vs. milestones and budget
├─ Monitor leading indicators (CAC, LTV, adoption rate, etc.)
├─ Quarterly review with Capital Committee
├─ Kill decision if performance is below kill threshold
│
└─ Gate 3 Decision (Month 12): Scale? Pivot? Kill? SCALE / PIVOT / KILL

STAGE 4: SCALING (Year 1-3)
│
├─ Increase capital investment based on early success
├─ Monitor ROIC trajectory vs. thesis
├─ Quarterly reviews by Capital Committee
├─ Annual strategic assessment
│
└─ Gate 4 Decision (Year 3): Mature? Harvest? Exit? Continue / Harvest / Exit

STAGE 5: STEADY-STATE / HARVEST (Year 3+)
│
├─ Business is mature, cash-generating
├─ Annual capital allocation decisions
├─ Monitor ROIC vs. alternative uses
│
└─ Gate 5 Decision (Annual): Maintain? Reallocate? Divest? MAINTAIN / REALLOCATE / DIVEST
```

### Gate Criteria

Each gate uses the same criteria:

| Gate | Key Questions | Approval Criteria | Kill Criteria |
|---|---|---|---|
| **Gate 1** | Is this worth exploring? Do we have conviction on the hypothesis? | CEO + CFO approve thesis | Kill if core hypothesis is implausible or contradicts strategy |
| **Gate 2** | Will this generate returns ≥ hurdle rate? Are risks mitigated? | Capital Committee approves spend | Kill if model shows ROIC < hurdle - 2% or risks are unmitigable |
| **Gate 3** | Is early performance tracking thesis? Can we scale? | Capital Committee approves Stage 3+ spend OR kill | Kill if leading indicators miss plan by >20% OR kill triggers are hit |
| **Gate 4** | Is ROIC tracking thesis? Should we continue or harvest? | Capital Committee recommends continue/harvest | Kill if ROIC < hurdle for 2+ consecutive quarters |
| **Gate 5** | Should we maintain or reallocate capital elsewhere? | Annual Capital Committee review | Reallocate if ROIC < hurdle or opportunity cost is high |

---

## Step 4: Decision Rights Matrix (RACI)

For each type of capital decision, define who is:
- **R** — Responsible (does the work)
- **A** — Accountable (owns the outcome)
- **C** — Consulted (provides input)
- **I** — Informed (gets updated)

### Capital Decision RACI Template

| Decision | Business Unit Head | CFO | CEO | Board | COO | Strategy |
|---|---|---|---|---|---|---|
| Maintenance capex (<$1M) | **A** | C | I | - | C | I |
| Growth capex ($1-5M) | **R** | **A** | C | I | C | C |
| Growth capex ($5-20M) | R | **A** | **A** | C | C | C |
| M&A (<$50M) | C | **A** | **A** | C | C | C |
| M&A ($50-250M) | C | **A** | **A** | **A** | C | C |
| M&A (>$250M) | C | C | **A** | **A** | C | C |
| Debt issuance | C | **A** | **A** | C | I | I |
| Equity raise | C | **A** | **A** | **A** | I | C |
| Dividend / Buyback | C | **A** | **A** | **A** | I | I |
| Divestiture | C | **A** | **A** | **A** | **R** | C |

**Key rules:**
- Every decision has one **A** (accountable); they own the outcome
- **R** does the analytical work; **A** makes the final call
- **C** provides critical input but doesn't decide
- **I** gets notified of decision but isn't involved
- Disagreement between **A**-level people goes to next-level **A** (e.g., CEO/Board) for tie-break

---

## Step 5: Annual Planning & Budgeting Cadence

Capital allocation happens continuously, but it's anchored by an annual planning cycle.

### Annual Capital Planning Calendar

**Q1 (Jan - Mar):**
- Month 1: Board and CEO set strategic priorities for year
- Month 2: BU heads forecast capital needs for year based on strategy
- Month 3: CFO consolidates forecasts, identifies mismatch between needs and sources

**Q2 (Apr - Jun):**
- Month 4: Capital Committee prioritizes investments by ROIC and strategic value
- Month 5: CFO models different funding scenarios (debt, equity, retention mix)
- Month 6: CEO and Board approve annual capital budget and funding plan

**Q3 (Jul - Sep):**
- Month 7-9: Execution and monthly tracking vs. budget
- Month 7, 8, 9: Monthly Capital Committee reviews actual vs. plan

**Q4 (Oct - Dec):**
- Month 10: Mid-year review of progress; adjust plan if needed
- Month 11: Forecast Year 2 capital needs (input for next year's planning)
- Month 12: Annual review of ROIC vs. thesis; reallocation decisions; Board planning for next year

### Planning Deliverables

**Strategic Plan (Annual):**
- What are our strategic priorities?
- What capital do they require?
- What's the expected ROIC?
- What are the key milestones?

**Capital Budget:**
- Business unit capex by category (maintenance, growth, strategic)
- Corporate capex
- M&A budget (target amount available for acquisitions)
- Working capital plan
- Total capital needs by quarter

**Funding Plan:**
- Operating cash flow forecast
- Equity raises planned (if any)
- Debt issuances planned (if any)
- Dividend / buyback plan
- Ending cash position forecast

**ROIC Targets:**
- By business unit (expected ROIC for year based on capital deployed)
- Company-wide target (weighted average)
- Targets for next 3 years (line of sight to mature state)

---

## Step 6: Exception & Fast-Track Processes

Not every investment follows the normal stage-gate. Some require speed (competitor moving fast) or flexibility (founder with track record proposing a small bet).

### Exception Approval Process

**When used:** Investment that doesn't fit standard categories or timeline

**Approval authority:**
- CEO can approve exceptions up to $[X]M
- Board Finance Committee approval needed for exceptions >$[X]M

**Documentation required:**
- Why exception is needed (competitive reason, time sensitivity, founder track record, etc.)
- Investment thesis (same quality as standard process)
- Mitigations for risks (e.g., if we're moving fast, how are we validating key assumptions?)

**Governance:**
- Exception is noted in Capital Committee minutes
- Exception investments are tracked for actual vs. thesis performance (to ensure we're not just rubber-stamping bad ideas)

### Fast-Track Process for Small, Founder-Led Investments

**Criteria:**
- < $[X]M total capital
- Led by experienced executive with track record
- Kills after [X] months if not hitting milestones

**Approval:**
- CEO approval (no Capital Committee meeting required)
- Updated to Capital Committee at next monthly meeting

**Governance:**
- Monthly check-in with CEO on progress
- Automatic kill if [milestones] aren't hit by [date]

---

## Step 7: Accountability & Performance Review

Governance only works if people are held accountable for investment results.

### Investment Owner Accountability

**Every investment has an owner.** Typically the executive whose budget/P&L benefits from the investment.

**Owner responsibilities:**
- Deliver investment on time and on budget
- Hit planned ROIC or explain variance
- Provide monthly updates on progress and leading indicators
- Recommend kill/scale decisions when conditions change
- Face consequences for misses (bonus impact, career impact)

**Owner metrics:**
- Actual ROIC vs. thesis (quarterly review)
- Variance between forecast and actual (tracking accuracy)
- Adherence to timeline and budget
- Leading indicators (CAC, LTV, adoption rate, etc.)

### ROIC Realization Tracking

**Quarterly:**
- Calculate actual ROIC for every material investment
- Compare vs. thesis
- Explain variances (favorable and unfavorable)
- Update investment scorecard

**Scorecard Template:**

| Investment | Forecast ROIC | Actual ROIC | Variance | Notes | Owner |
|---|---|---|---|---|---|
| [Name] | 15% | 12% | -3pp | Customer adoption slower than plan; customer lifetime value on track | [Name] |
| [Name] | 8% | -2% | -10pp | <KILL TRIGGER HIT> Recommend exit | [Name] |

**Annual:**
- Identify investments outperforming thesis (scale them)
- Identify investments underperforming thesis (fix or exit)
- Review owner's track record (make decisions about future allocation to this owner)

### Compensation Linkage

Tie executive bonuses to capital allocation outcomes, not just top-line growth:

**Example bonus structure:**
- 40% — Revenue / EBITDA target
- 30% — ROIC improvement (vs. prior year)
- 20% — Investment accuracy (actual vs. forecast ROIC)
- 10% — Capital efficiency (revenue per dollar of capital deployed)

This aligns incentives to capital discipline, not empire building.

---

## Step 8: Governance Escalation for Contested Decisions

What if the CEO and Board Finance Committee disagree on an investment?

### Escalation Protocol

```
DECISION DISPUTE
      │
      ├─ Discuss at Capital Committee
      │  └─ Can consensus be reached?
      │     ├─ Yes → Decide and move on
      │     └─ No → Continue...
      │
      ├─ Present to Board Finance Committee
      │  ├─ Finance Committee makes recommendation to full Board
      │  └─ Full Board makes final decision (if >$[X]M)
      │
      └─ If still contested: CEO has tiebreaker authority (or Board votes)
```

**Rule:** Every contested decision is documented with both sides of the argument. This creates learning for next time and prevents revisiting the same argument.

---

## Template: Capital Governance Charter for Your Company

```
CAPITAL ALLOCATION GOVERNANCE CHARTER
═══════════════════════════════════════

DECISION AUTHORITIES BY SIZE
- < $[X]M: [Authority]
- $[X]M - $[Y]M: [Authority]
- > $[Y]M: [Authority]

CAPITAL COMMITTEE
- Members: [Names/roles]
- Frequency: [Monthly / Quarterly]
- Authority: Approve investments up to $[X]M

STAGE-GATE PROCESS
- Gate 1 (Concept): [Authority] decides proceed
- Gate 2 (Full Analysis): [Authority] approves spend
- Gate 3 (Scale): [Authority] decides scale/pivot/kill
- Gate 4 (Mature): [Authority] decides harvest/maintain

INVESTMENT CRITERIA
- Hurdle rate: [X]% (or WACC + [X]%)
- Strategic investment hurdle: [Y]%
- Investment thesis required for: $[X]M+
- Kill trigger examples: ROIC < [X]% for 2 consecutive quarters

ACCOUNTABILITY
- Investment owner: [Designated person]
- ROIC tracking: Quarterly
- Bonus linkage: [Describe compensation tie]
- Underperformance consequences: [Describe]

ANNUAL PLANNING
- Capital budget approval: By [date]
- Funding plan approval: By [date]
- ROIC realization review: [Quarterly / Annual]
═══════════════════════════════════════
```

---

## Governance Best Practices Checklist

- [ ] Investment authority matrix is defined and published
- [ ] Capital Committee is formed with clear charter
- [ ] Stage-gate process is documented and followed
- [ ] Decision Rights (RACI) matrix is created
- [ ] Annual capital planning cycle is on calendar
- [ ] Investment thesis template is standardized
- [ ] ROIC tracking system is in place (quarterly reporting)
- [ ] Kill triggers are pre-defined before investment approval
- [ ] Exception approval process is documented
- [ ] Fast-track process exists for founder-led investments
- [ ] Owner accountability is tied to compensation
- [ ] Escalation path is defined for contested decisions
- [ ] Governance charter is approved by Board
- [ ] All governance documents are shared with leadership team
