# Operating Model Design (10/10 Complete Framework)

## What Changed
Expanded from a 5-layer design framework to a full transformation blueprint. Added: stakeholder resistance mapping and change management woven throughout, cost modeling and business case, failure patterns with examples, technology selection criteria, pre-built operating model archetypes, capability building framework, governance decision patterns, and a detailed worked example. Now covers what actually makes redesigns succeed (70% of failures are people and change management, not design).

## When to Use
Use when redesigning how the organization actually works — structure, governance, processes, people, technology, and change. Triggers: post-M&A, scaling inflection, strategy pivot, execution failures, cost transformation. **Critical:** This is the complete blueprint. A COO should use this to manage end-to-end redesign without guessing.

## Phase 0: Operating Model Archetypes (Choose Your Pattern)

**Rapid Scaling (Growth 3x in 2 years)**
- Move from functional to divisional by geography or product line
- Implement shared services center for HR, Finance, IT
- Decentralize P&L, centralize standards
- Failure risk: "Org chart shuffle" — boxes moved, behaviors unchanged

**Post-M&A Integration (Combine 2+ organizations)**
- Start with duplicate structure, then merge layer by layer (hardest first)
- Create integration management office (IMO) to coordinate, not run
- Identify 10-15 "must integrate" processes; leave rest alone initially
- Failure risk: "All structure no process" — standardized reporting lines but kept broken processes

**Digital Transformation (Win on speed/innovation)**
- Shift from functional silos to cross-functional pods with shared platforms
- Flatten hierarchy (remove approval layers)
- Create product/data-driven decision culture
- Failure risk: "Frozen middle" — frontline empowered but middle management still gatekeeping

**Cost Transformation (Cut 20%+ expense)**
- Centralize and standardize everything possible (shared services, processes, vendors)
- Eliminate redundant roles and layers
- Automate manual work
- Failure risk: "Cuts that cure disease" — layoffs cause flight of best people, remaining staff overloaded

**Regulatory/Compliance Overhaul**
- Restructure to embed compliance in core processes, not bolt-on
- Create clear audit trails and decision documentation
- Implement control testing into weekly/monthly cadence
- Failure risk: "Theater" — processes exist on paper but nobody follows them

## Phase 1: Strategy Translation & Resistance Mapping

**Strategy-to-Model Bridge:**
Translate strategy into operating model requirements. For each strategic goal, list what the org must be great at:

| Strategic Goal | Must Be Great At | Structural Implication |
|---|---|---|
| Win on customer experience | Fast front-line decisions, empowered teams, customer data flow | Decentralized authority, integrated data, customer-centric metrics |
| Win on cost | Standardized processes, shared services, lean operations | Centralized services, standardized decisions, tight cost control |
| Win on innovation | Rapid experimentation, failure tolerance, cross-functional speed | Flat hierarchy, dedicated pods, looser controls, innovation metrics |
| Win on operational excellence | Consistency, quality, compliance | Centralized process, detailed controls, audit trails |

**Stakeholder Resistance Mapping (Critical for Change Success):**
Before designing, identify who wins/loses and map resistance:

```
STAKEHOLDER: [Title/Team]
  Current state benefits: [What they gain today]
  New model impact: [What they lose/gain]
  Resistance level: [High/Medium/Low]
  Converter strategy: [Appeal to / Threat / Incentive / Coalition]
  Coalition priority: [Critical/Important/Nice-to-have]

Example:
STAKEHOLDER: Regional Sales VP
  Current benefits: P&L control, hire/fire authority, territory autonomy
  New model impact: LOSE authority (now matrix with product), GAIN efficiency/support, potential comp reduction
  Resistance: HIGH — identity threat, compensation risk
  Converter: Early win in new structure (new tools/support they requested), guaranteed transition comp, clear new career path
  Priority: CRITICAL — controls sales team, can slow adoption
```

Map at least 12-15 stakeholders. Identify which 3-4 are "critical converters" — if they support the change, 70% of resistance collapses.

## Phase 2: Design the Operating Model Stack

### Layer 1: Organization Structure
Choose the archetype that serves your "must-be-great-at" list:

**Functional** — Organized by expertise (Eng, Sales, Marketing, Ops)
- Use when: Deep expertise critical, moderate scale, similar products, cost efficiency matters
- Tradeoff: Slow cross-functional work, no end-to-end ownership, silos

**Divisional** — Organized by product, geography, or customer segment
- Use when: Markets distinct, P&L accountability critical, speed matters more than efficiency
- Tradeoff: Resource duplication, loss of functional excellence, inconsistent quality

**Matrix** — Dual reporting lines (Functional + Divisional)
- Use when: Need both deep expertise AND market responsiveness
- Tradeoff: Slow decisions, politics, confusion — only works with crystal-clear decision rights and strong governance discipline

**Pod/Network** — Cross-functional pods with shared platforms
- Use when: Innovation and speed critical, project-based work, tech enables coordination
- Tradeoff: Harder to maintain expertise depth, coordination overhead, culture-dependent

**Recommendation:** State structure + why + explicit trade-offs. Example: "Divisional by customer segment because speed-to-market is critical. Trade-off: We'll duplicate some functions but accept this because customer responsiveness drives revenue growth."

**Spans and Layers:**
- Layers (CEO to front-line): 3-4 = fastest decisions, 5-6 = moderate control, 7+ = tight control/bureaucratic
- Span of control: 6-8 = autonomy, 3-4 = coaching capacity
- Rule: If you can't justify a layer, delete it

### Layer 2: Decision Rights & Governance Patterns

For 10-12 critical recurring decisions, specify RACI + pattern:

```
DECISION: Feature roadmap (next quarter)
  Decides: [Product VP]
  Advises: [Engineering Lead, Sales Lead, Finance]
  Informed: [All teams]
  Escalation: [CEO if >$2M investment or strategic conflict]
  Cadence: Quarterly, 2 weeks before next quarter starts
  Decision Rights Pattern: Weighted voting (50% customer signal, 30% strategic, 20% engineering feasibility)
```

**Governance Decision Patterns (Pick 3-4 core patterns):**

1. **Weighted Scoring** — Multiple criteria (customer demand, strategic fit, cost, risk) with weights. Best for: resource allocation, feature prioritization. Risk: Gaming the weights.

2. **Delegation with Limits** — Lower levels decide up to a threshold; escalate above. Best for: hiring, expense approval, vendor selection. Risk: Threshold creep (everyone stays just under).

3. **Consensus with Tiebreaker** — Try consensus first; named person decides if no consensus. Best for: strategy, cross-functional trade-offs. Risk: Can still be slow.

4. **Authority by Role** — One role has final say (e.g., CEO decides strategy, CFO decides budget). Best for: speed, clarity. Risk: Excludes valuable input.

5. **Small Committee** — 3-5 people decide together. Best for: important decisions, reducing single-point-of-failure. Risk: Slow, can devolve into politics.

**Governance Design Rule:** If decisions are escalating constantly, either the wrong person owns them or the decision criteria are unclear. Fix criteria first, not governance.

### Layer 3: Core Processes & Ways of Working

Identify 5-7 critical processes (ones where failure breaks strategy):

```
PROCESS: Monthly forecast update
  Purpose: Maintain accurate revenue visibility, catch misses early
  Current state: 3/5 — Takes 4 days, 30% accuracy, missing category, manually built
  Gap: Missing by 30%, late visibility, too much manual work
  Target state: 5/5 — Automated pull from CRM/ERP, <24 hours, <10% error, broken down by segment
  Owner: CFO (Finance Lead executes)
  Timeline to target: 4 months (3 months system config, 1 month process tuning)
```

**Coordination Mechanisms (How teams stay aligned):**
- Planning cadence: Annual strategy → quarterly OKRs → monthly plans → weekly execution
- Review cadence: Weekly metrics review (ops), monthly business review (leadership), quarterly strategy review (board)
- Communication norms: Decisions go to Slack immediately, details in email/docs, discussion in meetings only if contested
- Cross-functional rituals: Weekly standups (15 min, async option), monthly demos, quarterly retros

### Layer 4: Capability Building Plan (Not Just "Hire Data Scientists")

For each critical capability gap, build a full plan:

```
CAPABILITY: Data-driven decision-making at all levels
  Current state: Only Finance has data skills; most decisions gut-feel or off outdated reports
  Gap: Decisions slow, poor quality, missed opportunities

  Talent plan:
    - Hire: 1 Chief Data Officer (Year 1, $250K), 2 data engineers (Year 1, $350K), 1 analyst per division (Year 1-2, $280K)
    - Train: 2-day "Data 101" for all leaders (Q2 Year 1), monthly data workshop (ongoing)
    - Acquire: Tableau license + data platform (Year 1, $150K)
    - Partner: Work with external data strategy firm for first 6 months to design metrics framework

  Timeline: Foundation by Q3 Year 1, proficiency by Q2 Year 2
  Investment: $1.3M Year 1, $600K Year 2
  Risk: Slow adoption — mitigate with mandatory metrics in every decision
```

### Layer 5: Technology Selection Criteria

When evaluating technology for the operating model:

| Criterion | Why It Matters | Evaluation |
|---|---|---|
| **Integration** | Does it connect with existing systems? | Map data flows; test API; talk to customers with similar stack |
| **Adoption Cost** | How long to full proficiency? | User testing with lowest-tech users; measure time-to-value |
| **Flexibility** | Can we customize or does it force our process? | Ask: "Can we change this in 6 months?" If vendor says no, reject it |
| **Vendor Lock-in** | Can we get data out if we change vendors? | Require data export, API access, no proprietary data formats |
| **TCO (5-year)** | License + implementation + support + training | Build bottom-up model; pad by 30% for overruns |
| **Org Impact** | Will adoption require org changes? | Map required org changes; estimate change cost (people, training) as 2-3x software cost |

**Technology Rule:** Software enables, doesn't fix. If the process is broken, software makes it broken faster.

## Phase 3: Cost Modeling & Business Case

**Build a full cost model:**

| Cost Category | Current State | New Model | Year 1 Transition | Ongoing |
|---|---|---|---|---|
| Structure (salaries, benefits) | [Current headcount × avg cost] | [New headcount × avg cost] | +Transition costs | Ongoing savings |
| Processes (hours, tools) | [Current hours × labor] | [Automated/improved hours × labor] | +Implementation | Ongoing savings |
| Technology | [Current stack cost] | [New stack cost] | +Migration, training | [Annual support] |
| Capability building | [Training spend] | [Training + hire/external] | +Investment | +Ongoing |
| Change management | [Current ad-hoc] | [Structured program] | +Full program | Minimal |
| **TOTAL COST** | | | | |

Example: "New cost-optimized structure costs $300K less annually in salaries but requires $800K investment to transition (severance, hiring, training, new systems). Payback in 3.2 years. ROIC: 28%."

## Phase 4: Change Management & Momentum Maintenance

**Communication Cascade (Who says what when):**

```
Week 1: CEO town hall — "Here's why we're changing. Here's what's in it for you. Here's the timeline."
Week 2: Direct reports — "Here's your new role/team. Here's what success looks like."
Week 3: All-hands — Q&A, answer concerns, show transition plan
Week 4: Pulse survey — "How are you feeling? What's confusing?"
Ongoing: Weekly leadership updates, monthly all-hands, real-time FAQ, narrative in every communication

Success metric: 70%+ confidence in the change by month 2; 80%+ by month 4
```

**Resistance Handling Tactics:**

1. **Early Wins (Month 1-2):** Deliver something the organization clearly wanted (faster hiring process, reduced approvals, better tools). Show "the new model works." Builds momentum.

2. **Coalition Building:** Identify the 3-4 "critical converter" stakeholders. Give them high-visibility roles in transition. Let them see it working early, then use them to influence peers.

3. **Neutralize Blockers:** For high-resistance people/roles:
   - If critical to organization: Make them ambassador (gives them control, solves for loss-of-control resistance)
   - If critical to transition: Accelerate their success (training, resources, support)
   - If neither: Move them to stable role with clear future or exit (don't drag out death march)

4. **Momentum Maintenance (Months 3-6):** This is where 70% of redesigns die. Sustain by:
   - Weekly progress metrics (adoption, cycle time, decision speed)
   - Monthly wins (celebrate hitting milestones)
   - Quarterly feedback loops (show improvements working)
   - Ruthless removal of blockers (if a process is slowing adoption, kill it immediately)

## Phase 5: Failure Pattern Recognition

**1. "Org Chart Shuffle"** — Boxes moved, behaviors unchanged
- Example: "We're now divisional!" (boxes moved) but CFO still controls every spending decision (behavior same as before)
- Prevention: Measure behavior change, not structure change. Track how fast decisions are made, who's deciding, how often decisions escalate

**2. "Frozen Middle"** — Frontline empowered, middle management still gatekeeping
- Example: Squad leaders told to move fast but regional VP still approves everything. Squad leaders stop trying.
- Prevention: Map decision rights 2-3 layers deep. Make explicit which decisions middle mgmt no longer owns. Hold them accountable for enabling speed, not controlling work.

**3. "All Structure No Process"** — Reporting lines changed but broken processes unchanged
- Example: "New structure!" but still using same 6-week approval process, same manual data entry, same 20-person meeting to decide anything
- Prevention: For every structure change, map which processes must change to support it. Implement process changes within 4 weeks, not 6 months.

**4. "Technology Theater"** — New system, old ways of working
- Example: Implement Salesforce so everyone can see the pipeline, but sales team still only reports up to regional VP through email
- Prevention: Design process first, then select technology. Measure adoption (% using system for decisions, not just data entry). Kill old workarounds.

**5. "Capability Mismatch"** — Designed for people you don't have
- Example: Divisional structure requires strong GMs but you have 0 GMs and 12-month hiring lead time for good ones
- Prevention: For every role/decision right in the design, map "do we have this capability today?" If not, build a 6-12 month capability plan before you flip the structure.

**6. "Comp Misalignment"** — Org redesigned, comp plan unchanged
- Example: Told to collaborate cross-functionally but bonus based on individual function metrics
- Prevention: Change comp plan 30 days before structure change. New comp = new behaviors.

## Phase 6: Measurement Framework

**Leading Indicators (What's working in the design, measured weekly/monthly):**
- Decision cycle time (Days from decision needed to decision made)
- Escalation rate (% of decisions escalating up)
- Process automation (% of manual steps eliminated)
- Capability coverage (% of critical roles at "great" performance level)
- Adoption metrics (% using new systems/processes to decide, not just report)
- Engagement (pulse survey on clarity, empowerment, pace)

**Lagging Indicators (Whether strategy is actually working, measured quarterly/annually):**
- Financial impact (Revenue growth, cost savings vs. model)
- Capability scores (Internal assessment of "must-be-great-at" capabilities: 1-5 scale)
- Customer impact (NPS, retention, win rate, close time)
- Talent impact (Retention of critical talent, hiring quality, internal promotion rate)
- Organizational health (Retention overall, engagement, voluntary turnover)

**Example Dashboard:**
```
OPERATING MODEL HEALTH: [Business Unit] — Monthly Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEADING (Process):
  Decision cycle time: 8 days (target: 7) — ON TRACK
  Escalation rate: 12% (target: 10%) — WATCH
  New system adoption: 67% (target: 80%) — AT RISK
  Skill gaps filled: 4/6 roles (target: 6/6) — IN PROGRESS

LAGGING (Impact):
  Revenue growth: 18% YoY (target: 20%) — ACCEPTABLE
  Cost savings: $450K realized vs. $600K target — TRACKING
  NPS: 62 (was 58 baseline) — POSITIVE TREND
  Voluntary turnover: 8% (was 6%, acceptable given change)
```

## Worked Example: Post-Acquisition Integration (TechCo + DataCo)

**Context:** TechCo (SaaS platform, $100M ARR, 600 people) acquired DataCo (data analytics platform, $20M ARR, 150 people). Goal: Integrated product, 15% cost synergies, single go-to-market.

**Phase 1 Resistance Mapping:**
- DataCo CEO (HIGH RISK): Sees loss of autonomy, brand, and team. Risk: Active resistance. Converter: COO role with real authority over product integration, 2x earnout for hitting synergy targets, dedicated team.
- TechCo VP Sales (HIGH RISK): Sees new sales process, different margins, different commission structure. Risk: Top reps quit. Converter: Blended commission structure (favorable interim), early access to integrated product, customer success wins.
- DataCo Engineering Lead (MEDIUM): Sees code rewrite, process changes. Converter: Tech lead role on integration, hiring authority for best-in-class team, clear technical roadmap.

**Phase 2 Design Decisions:**
- Structure: Start with parallel functional structure (keep DataCo mostly intact). After 6 months, merge engineering/product into TechCo, consolidate back-office immediately. "Parallel → Merged" approach reduces resistance, allows quick financial wins.
- Decision rights: Create Integration Management Office (IMO). CEO + DataCo COO + TechCo CTO + Finance + Sales. Decides on customer migration, product prioritization, cost synergies. Escalates to Board if conflict.
- Critical processes to merge first (quick wins): Finance (1 GL, 1 FP&A team), HR (1 recruiting, benefits), Contracts (1 legal team). Take 8 weeks.
- Defer merger: Engineering (needs care, talent flight risk), Sales operations (different models, keep parallel for 1 year), Product team (only merge after technical integration plan is solid).

**Phase 3 Cost Model:**
| | Current | Year 1 | Year 2+ |
|---|---|---|---|
| TechCo salaries | $75M | $75M | $75M |
| DataCo salaries | $12M | $12M | $8.4M (30% savings from dedup) |
| Systems (pre-merge) | $800K | $1.2M (transition) | $900K |
| Severance (dedup) | 0 | $1.8M | 0 |
| Integration PMO | 0 | $400K | $0 |
| **Total Cost to Org** | | **+$1.6M** | **-$3.6M** |

Payback: 5 months. Year 2+ ROI: 400%.

**Phase 4 Communication Cascade:**
- Week 1: Combined town hall with both CEOs. "Here's why we combined. Here's what's non-negotiable (product, go-to-market). Here's what we're keeping (culture, people, leadership)."
- Week 2: Separate department heads meetings. Clear role changes, who reports to whom, what decisions are theirs vs. IMO.
- Week 3: All-hands Q&A. Focus on "What happens to my team?" and "Will I be laid off?"
- Monthly: Integration progress (process mergers, system consolidations, synergy tracking).

**Phase 5 Measurement (Monthly):**
Leading:
- Process mergers on track (Finance merged by week 8, HR by week 10, etc.) — YES/NO
- Escalation rate in IMO (target: no more than 1-2 decisions to CEO per month) — Track
- System migration progress (% of DataCo data migrated to TechCo systems) — 80%+ by week 12

Lagging:
- Revenue retention (TechCo + DataCo existing customers) — Target: >95% (common acquisition risk: customer churn during integration)
- Cost synergies realized ($3.6M by year-end) — Track monthly
- Voluntary turnover (watch for flight of DataCo talent) — Target: <5% in Year 1

---

```
OPERATING MODEL REDESIGN: [Company/Division]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESIGN CRITERIA (from strategy):
  Archetype: [Rapid Scaling / Post-M&A / Digital Transformation / Cost / Compliance]
  Must be great at: 1. [...] 2. [...] 3. [...]
  Explicit trade-offs: [What we're sacrificing]

STAKEHOLDER RESISTANCE MAP:
  Critical converters: [3-4 people/roles with lever points]
  High resistance: [Who + why + converter strategy]
  Coalition plan: [Which roles to give authority/visibility]

STRUCTURE:
  Type: [Functional/Divisional/Matrix/Pod] — Why: [Link to criteria]
  Layers: [...] — Spans: [...]
  Key trade-off: [What this gives up and why worth it]

DECISION RIGHTS: [8-10 critical decisions with RACI + pattern]

CORE PROCESSES: [5-7 with current/gap/target and owner]

CRITICAL CAPABILITIES:
  Gaps: [Top 3 capability gaps]
  Plan: [Hire/train/acquire/partner for each, timeline, cost]
  Timeline: [When proficiency reached]

TECHNOLOGY:
  Systems to change: [What and why]
  Adoption cost: [Time, training, change]
  Integration: [What connects to what]

COST MODEL:
  Current state: [Structure + cost baseline]
  New model: [Structure + cost]
  Year 1 investment: [Transition costs]
  Ongoing impact: [Annual savings/cost]
  Payback: [Months to positive ROI]

FAILURE RISKS & MITIGATION:
  Risk 1: [Org chart shuffle / Frozen middle / Process mismatch / etc.]
  Mitigation: [How to prevent or catch early]
  Measurement: [Leading indicator to track]

CHANGE PLAN:
  Communication: [Cascade by week, key messages]
  Early wins: [Specific 30-day wins to build momentum]
  Resistance handling: [For each high-resistance group]
  Momentum maintenance: [How to keep energy through month 6]

MEASUREMENT:
  Leading (weekly/monthly): [Cycle time, adoption, escalations, skills]
  Lagging (quarterly/annual): [Financial, capability, customer, talent]
  Review cadence: [Weekly ops, monthly leadership, quarterly strategy]

TIMELINE:
  Phase 1 (Foundation): [Months X-Y] — [Key moves]
  Phase 2 (Hardwire): [Months X-Y] — [Process + system changes]
  Phase 3 (Optimize): [Months X-Y] — [Measurement + adjustment]
```
