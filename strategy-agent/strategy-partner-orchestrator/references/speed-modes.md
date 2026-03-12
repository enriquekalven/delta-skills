# Speed Mode Decision Tree & Skill Specifications

**Purpose:** Define how the strategy ecosystem adapts analysis depth, timeline, and confidence based on decision urgency and complexity. Every skill must explicitly specify what analyses run, compress, or skip in each mode.

**Version:** 1.0 | **Created:** 2026-03-10 | **Audit Reference:** P1-1

---

## 1. Speed Mode Overview

The StrategyOS ecosystem operates in three speed modes, each with distinct time budgets, quality expectations, and use cases:

### Mode 1: Quick Strike (60 minutes end-to-end)

**Time Budget:** 60 minutes total (all skills combined)
**Quality Expectation:** Directional guidance, suitable for immediate decisions
**Confidence Cap:** Medium (70% maximum)
**Use Case:** Board meeting in 24 hours, investor call this week, urgent competitive move, kill/proceed checkpoint
**Output:** 1-2 key recommendations with clear rationale; reduced supporting analysis
**Risk Profile:** Acceptable for reversible decisions; unacceptable for capital allocation >$5M

**Characteristics:**
- Heavy use of frameworks (MECE, Porter Five Forces, SCP, 2x2 matrices)
- Limited primary data gathering; rely on existing knowledge + public data
- One scenario analyzed (usually base case or most likely)
- Hypothesis-driven (minimize analysis breadth, maximize hypothesis confirmation speed)
- No extensive benchmarking; use broad industry standards only
- Decision tree pruning: test only 2-3 primary branches
- External intelligence: public sources only (no paid databases, no primary interviews)

---

### Mode 2: Standard (half-day / 4 hours)

**Time Budget:** 4 hours total per skill (skills run sequentially or parallel, total engagement 6-12 hours)
**Quality Expectation:** High confidence, defensible recommendations
**Confidence Cap:** High (80-85%)
**Use Case:** Strategic planning cycle, quarterly business reviews, GTM for new product, org restructuring, competitive positioning
**Output:** Detailed recommendations with supporting analysis, multiple scenarios, validation evidence
**Risk Profile:** Appropriate for most strategic decisions (capital <$50M, medium-term commitments)

**Characteristics:**
- Balanced analysis depth and speed
- Data gathering from internal sources + public benchmarks
- 3-4 scenarios modeled (Upside, Base, Downside, Disruptive where applicable)
- Multiple analytical lenses applied (e.g., Strategy Partner runs MECE + Competitive Landscape + Scenario Planning)
- Some benchmarking against peer set
- All core dependencies validated
- External intelligence: public sources + limited paid databases
- Iteration loops: up to 2 cycles for hypothesis refinement

---

### Mode 3: Deep Dive (multi-day / 20+ hours)

**Time Budget:** 20+ hours total (full engagement across multiple days)
**Quality Expectation:** Exhaustive analysis, highest defensibility
**Confidence Cap:** Very High (90%+)
**Use Case:** M&A due diligence, major capital allocation (>$50M), org-wide transformation, irreversible strategic shifts, high-stakes multi-stakeholder decisions
**Output:** Comprehensive analysis with detailed alternatives, sensitivity testing, scenario stress-testing, full validation
**Risk Profile:** Required for high-stakes, irreversible decisions

**Characteristics:**
- Exhaustive primary data gathering (interviews, surveys, detailed operational analysis)
- Deep benchmarking across full competitive set + historical case studies
- All 4 scenarios fully modeled with sensitivity analysis
- Multiple analytical frameworks applied in sequence (validation through triangulation)
- Devil's Advocate and Bear Case explicitly surface
- Assumption validation through primary research
- Iteration loops: 3+ cycles allowed for thorough exploration
- External intelligence: all sources (paid databases, primary research, expert interviews, confidential competitor intelligence where available)
- Stress testing: what assumptions must hold for recommendation to be valid?

---

## 2. Speed Mode Decision Tree

Use this flowchart to select the appropriate speed mode for your engagement:

```
START: NEW PROBLEM ARRIVES
        ↓
1. TIME CONSTRAINT?
  ├─ IMMEDIATE (decision must be made in <24 hours)
  │   └─ → QUICK STRIKE (60 min)
  │
  ├─ THIS WEEK (decision by Friday)
  │   └─ → Proceed to question 2
  │
  └─ THIS MONTH or longer
      └─ → Proceed to question 2

2. DECISION COMPLEXITY?
  ├─ SINGLE DOMAIN (e.g., pricing only, headcount reduction only)
  │   └─ → QUICK STRIKE or STANDARD depending on stakes
  │
  ├─ MULTI-DOMAIN (3+ functional areas affected; e.g., strategy + GTM + org + financial)
  │   └─ → STANDARD minimum
  │
  └─ PORTFOLIO/TRANSFORMATION (org-wide implications, multiple business units)
      └─ → DEEP DIVE

3. DATA AVAILABILITY?
  ├─ RICH DATA (we have market data, customer data, financial baseline, operational metrics)
  │   └─ → Can compress time, proceed to question 4
  │
  ├─ SPARSE DATA (limited internal analytics, missing customer insights)
  │   └─ → Extend time, shift toward DEEP DIVE
  │
  └─ NO DATA (new market, new business model, first entry)
      └─ → DEEP DIVE mandatory

4. DECISION STAKES & REVERSIBILITY?
  ├─ LOW STAKES & REVERSIBLE (can undo in 3-6 months; <$1M impact)
  │   └─ → QUICK STRIKE acceptable
  │
  ├─ MEDIUM STAKES & PARTIALLY REVERSIBLE (6-12 month impact; $1-50M)
  │   └─ → STANDARD
  │
  ├─ HIGH STAKES & HARD-TO-REVERSE (>12 months; >$50M; org-wide change)
  │   └─ → DEEP DIVE mandatory
  │
  └─ EXISTENTIAL STAKES (survival decision; acquisition target; complete pivot)
      └─ → DEEP DIVE mandatory

5. CONFIDENCE REQUIRED?
  ├─ DIRECTIONAL OK (60%+ confidence in direction is acceptable)
  │   └─ → QUICK STRIKE
  │
  ├─ HIGH CONFIDENCE NEEDED (80%+ for implementation confidence)
  │   └─ → STANDARD
  │
  └─ CERTAINTY REQUIRED (90%+ for board/investor confidence)
      └─ → DEEP DIVE

FINAL DECISION:
  ├─ QUICK STRIKE: 60 min, directional, <70% confidence, reversible decisions only
  ├─ STANDARD: 4-6 hours, defensible, 80%+ confidence, most strategic decisions
  └─ DEEP DIVE: 20+ hours, exhaustive, 90%+ confidence, high-stakes/irreversible decisions
```

---

## 3. Skill-by-Skill Speed Mode Specifications

### Skill: STRATEGY PARTNER

**Role in Engagement:** Diagnostic and analytical foundation for all strategic work.

#### Quick Strike (60 min total)
**Analyses to RUN:**
- MECE Issue Tree (rapid decomposition, 2-3 levels max)
- Competitive Landscape (4-5 competitor snapshot, current state only)
- Hypothesis Engine (test 2-3 critical hypotheses only)

**Analyses to SKIP:**
- Strategic Position deep dive
- Scenario Planning (except cursory 1 scenario)
- Value Chain detailed flow
- Detailed industry analysis
- Porter Five Forces full scoring

**Analyses to COMPRESS:**
- Executive Communication (1-page executive summary only, no detailed narratives)
- Decision Frame (simple decision tree, not exhaustive)

**Time Budget:** 45 minutes for analysis + 15 minutes for output formatting
**Minimum Output Requirements:**
- MECE tree identifying 2-3 primary hypotheses/levers
- 2-3 key findings with HIGH/MEDIUM confidence tags only (no LOW)
- One clear decision point and recommended path
- 1-2 critical assumptions flagged for validation

**Confidence Cap:** 65% (explicitly cap any higher confidence claims)
**Success Criteria:** User can make directional decision without additional analysis

---

#### Standard (4 hours)
**Analyses to RUN:**
- Full MECE Issue Tree (3-4 levels, complete decomposition)
- Comprehensive Competitive Landscape (6-8 competitors, current + recent trajectory)
- Hypothesis Engine (test 4-6 hypotheses, prioritize by impact)
- Strategic Position assessment (our strengths vs. competitive landscape)
- Scenario Planning (model Base Case and Downside scenarios)
- Value Chain analysis (identify value creation and cost drivers)

**Analyses to COMPRESS:**
- None—run full depth for all core analyses

**Time Budget:** 180 minutes for analysis + 30 minutes for output formatting + 30 minutes for synthesis
**Minimum Output Requirements:**
- Complete MECE tree with all major categories and hypotheses
- 4-5 key findings with evidence and confidence tags (H/M/L)
- 2-3 scenarios explicitly modeled
- Clear decision frame with 2-3 paths and relative recommendation
- 3-4 critical assumptions flagged with validation plan

**Confidence Cap:** 80%
**Success Criteria:** Downstream skills (Rumelt, GTM, Financial) have sufficient context to proceed without requesting additional Strategy Partner analysis

---

#### Deep Dive (20+ hours)
**Analyses to RUN:**
- Full MECE Issue Tree (5+ levels, exhaustive)
- Comprehensive Competitive Landscape (10+ competitors, historical analysis, weak signals)
- Hypothesis Engine (test 8+ hypotheses, including contrarian views)
- Strategic Position (deep capability assessment, barriers to entry/exit analysis)
- Scenario Planning (all 4 scenarios fully modeled: Upside, Base, Downside, Disruptive)
- Value Chain deep analysis (detailed economics, cost structure, value capture)
- Industry Analysis (market structure, profit pools, growth drivers, disruption risk)
- Stakeholder Analysis (who wins/loses under each scenario)
- First-principles competitive analysis (from customer perspective)

**Time Budget:** 1,000+ minutes (16+ hours) for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- MECE tree with exhaustive categorization
- 8+ key findings with detailed evidence, confidence tags, and supporting data
- All 4 scenarios fully modeled with probability weightings
- Strategic Position assessed against all competitive dimensions
- Devil's Advocate case: "Here's how we could be wrong" section
- 6+ critical assumptions with detailed validation plans and trigger thresholds
- Alternative paths explicitly evaluated and rejected (with reasoning)

**Confidence Cap:** 90%+
**Success Criteria:** Board-ready analysis; downstream skills proceed with high confidence; key assumptions tested through primary research

---

### Skill: RUMELT STRATEGY FORGE

**Role in Engagement:** Create coherent strategy kernel from diagnostic intelligence.

#### Quick Strike (15 min)
**Analyses to RUN:**
- Auto-identify crux from Strategy Partner hypothesis prioritization
- Quick kernel assembly (3-5 coherent actions only, not exhaustive set)
- Coherence scoring (simplified, 3 dimensions only: internal, external, execution)

**Analyses to SKIP:**
- Bad Strategy Detector (full 16-point assessment)
- Resilience testing across all scenarios
- Deep capability mapping
- Kill conditions definition
- Assumption validation planning

**Analyses to COMPRESS:**
- Coherent Actions definition (one-liner + owner + timeline only, no detailed execution requirements)
- Guiding Policy statement (simple, one sentence)

**Time Budget:** 15 minutes
**Minimum Output Requirements:**
- One clear crux statement
- 3-5 Coherent Actions with owner and timeline only
- Coherence score (simplified: X/30, using Internal/External/Execution breakdown)
- One kill condition (the most critical "if this changes, strategy fails" condition)

**Confidence Cap:** 60% on coherence (flag explicitly: "Preliminary coherence; requires validation")
**Success Criteria:** Downstream skills understand the strategic direction and can proceed with detailed design

---

#### Standard (1-2 hours)
**Analyses to RUN:**
- Full crux identification from Strategy Partner analysis
- Complete kernel assembly (5-7 coherent actions, prioritized)
- Coherence assessment (full scoring: Internal/External/Execution, 0-100)
- Bad Strategy Detector (full 16-point assessment)
- Resilience testing (test kernel across Base + Downside scenarios)
- Assumption validation planning

**Analyses to COMPRESS:**
- None—run full depth

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Clear, singular crux statement
- 5-7 Coherent Actions with detailed specifications (owner, timeline, resource needs, success metric)
- Guiding Policy statement (one paragraph explanation of the strategic approach)
- Coherence score: Internal X/33, External X/33, Execution X/33 (total X/100)
- Bad Strategy score: X/16 (note: aim for 10+; anything below 8 requires kernel revision)
- Kill conditions: 2-3 critical assumptions with invalidation thresholds
- Resilience assessment: How does kernel hold up if Base Case assumptions fail?

**Confidence Cap:** 80%
**Success Criteria:** All downstream skills (GTM, Financial, Operating Model, People) have clear kernel to execute against without requesting clarification

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Multiple crux candidates identified and evaluated (5+ candidates, select top 1-3 for kernel building)
- Complete kernel assembly with extensive validation
- Full coherence assessment (all three dimensions deeply explored)
- Bad Strategy Detector (16-point assessment with detailed reasoning for each point)
- Resilience testing (kernel tested across all 4 scenarios: Upside, Base, Downside, Disruptive)
- Scenario stress-testing: Which assumptions must hold for success? What's the break-even case?
- Stakeholder impact analysis: Who wins/loses under this strategy? Are key stakeholders aligned?
- Historical case study comparison: Have similar strategies succeeded/failed? Why?
- Detailed assumption mapping: Every assumption linked to validation method and timeline

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- Singular, well-reasoned crux statement with 2-3 alternative crux candidates evaluated and rejected
- 7-10 Coherent Actions with extensive execution specifications
- Detailed Guiding Policy (one-page statement with rationale and competitive logic)
- Coherence score with detailed justification: Internal X/33 (why scored here), External X/33, Execution X/33
- Bad Strategy score: X/16 with detailed explanation for each dimension
- Resilience matrix: Strategy kernel tested across all 4 scenarios with pass/fail scoring
- Kill conditions: 5+ critical assumptions with detailed invalidation thresholds and monitoring plan
- Stakeholder alignment assessment: Which stakeholders must be convinced? What are their incentives?
- Alternative strategies explicitly considered and rejected (with detailed reasoning)
- Make-or-break assumptions clearly surfaced

**Confidence Cap:** 90%+
**Success Criteria:** Strategy is defensible against adversarial challenge; board-ready; all downstream skills proceed with minimal iteration

---

### Skill: GROWTH STRATEGY

**Role in Engagement:** Define and validate growth models and market expansion approaches.

#### Quick Strike (15 min)
**Analyses to RUN:**
- Market size estimation (TAM, rule-of-thumb approach)
- Growth lever identification (organic penetration vs. adjacent markets vs. acquisition)
- Quick unit economics (CAC/LTV estimate from industry benchmarks)

**Analyses to SKIP:**
- Detailed market segmentation
- Customer journey mapping
- Pricing strategy design
- Competitive growth positioning analysis
- Multi-year growth forecasting

**Analyses to COMPRESS:**
- Growth curve (linear projection only, 1-3 year horizon)
- Expansion roadmap (2-3 markets/segments only)

**Time Budget:** 15 minutes
**Minimum Output Requirements:**
- TAM estimate (order of magnitude: $X billion TAM, with confidence range ±50%)
- Primary growth lever (organic / adjacent / acquisition) with one-sentence rationale
- Rough CAC/LTV ratio from industry benchmarks
- One critical growth assumption (e.g., "assumes 20% customer acquisition growth")

**Confidence Cap:** 65%
**Success Criteria:** GTM Architect can choose go-to-market motion; Financial can estimate rough revenue impact

---

#### Standard (1.5 hours)
**Analyses to RUN:**
- TAM/SAM/SOM estimation (multiple methods, reconciled)
- Growth lever analysis (all three examined: organic penetration, adjacent expansion, M&A)
- Market segmentation (identify 4-6 primary customer segments and their growth profiles)
- Customer journey mapping (high-level: how do customers discover, evaluate, buy, expand)
- Unit economics modeling (CAC, LTV, payback period for base case)
- Pricing strategy (positioning vs. competitors; customer value perception)
- Growth roadmap (2-4 markets/segments with 12-24 month sequencing)
- Competitive growth positioning (what growth strategies are competitors pursuing?)

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- TAM estimate with 2-3 estimation methods (confidence range ±30%)
- SAM (Serviceable Addressable Market) estimate for year 1-2
- Primary growth lever with 2-3 supporting data points
- Market segmentation (4-6 segments, size and growth rate for each)
- Unit economics for base case (CAC, LTV, payback, monthly cohort retention curve)
- Pricing strategy (price point vs. competitors; elasticity estimate)
- Growth roadmap (timeline and priority order for market entry)
- 2-3 growth assumptions flagged for validation (e.g., "assumes x% CAC reduction through optimization")

**Confidence Cap:** 80%
**Success Criteria:** GTM Architect has market sizing and growth assumptions; Financial can model detailed unit economics

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Exhaustive TAM/SAM/SOM (5+ estimation methods, triangulated; includes TAM expansion opportunities)
- Deep market segmentation (8+ segments analyzed, with profit pool allocation)
- Customer journey (detailed: all decision stages, evaluation criteria, switching cost, expansion dynamics)
- Unit economics (full P&L per customer cohort, LTV scenarios, CAC by channel)
- Pricing optimization (price elasticity analysis, value-based pricing modeling, discount strategy)
- Growth roadmap (12-24 month sequencing across 4-6 markets, with resource allocation model)
- Competitive growth mapping (all major competitors' growth strategies analyzed, benchmarked)
- Growth constraints (what limits growth? Sales capacity? Product capability? Capital? Market size?)
- Detailed acquisition funnel modeling (awareness → consideration → purchase → retention → expansion)
- Customer economics deep dive (CAC by channel, LTV by segment, cohort analysis across multiple dimensions)

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- TAM estimate with 5+ methods, reconciliation narrative, and expansion opportunities identified
- SAM/SOM for each market segment (current and 3-year projection)
- Market segmentation matrix (8+ segments with size, growth, profitability, competitive intensity)
- Detailed customer journey (all stages, decision criteria, customer research supporting each stage)
- Unit economics across all customer segments (CAC, LTV, payback, retention curves, 3-year cohort analysis)
- Pricing analysis (elasticity estimates, value-based pricing model, competitor pricing, discount strategy)
- Growth roadmap with resource allocation (which markets first, why, what resources, what risks?)
- Competitive benchmarking (growth rates, CAC efficiency, LTV multiples for peer set)
- Growth constraint analysis (what actually limits our growth?)
- 5+ growth assumptions with validation methods and thresholds

**Confidence Cap:** 90%+
**Success Criteria:** Financial can model detailed financial projections; GTM can design acquisition motion; scalability validated

---

### Skill: GTM STRATEGY

**Role in Engagement:** Design customer acquisition, positioning, and market motion strategy.

#### Quick Strike (15 min)
**Analyses to RUN:**
- Customer segmentation (2-3 primary segments only)
- Value proposition snapshot (why customers should buy, vs. competitors)
- Sales/marketing motion (one-liner: direct sales / inside sales / self-serve / marketplace)
- Messaging framework (one-page: who we are, why we matter, what we do)

**Analyses to SKIP:**
- Detailed competitive positioning
- Sales process design
- Marketing campaign strategy
- Channel optimization
- Sales compensation design

**Analyses to COMPRESS:**
- Value proposition (one page only, no detailed testing)
- Pricing strategy (not owned by GTM in QS, defer to Financial)

**Time Budget:** 15 minutes
**Minimum Output Requirements:**
- Target customer segment (one primary segment, one-sentence description)
- Value proposition (one paragraph: what we do, why it matters, why us vs. competitors)
- Sales/marketing motion (one sentence: e.g., "land through content marketing, expand through direct sales")
- Key messaging pillar (one message that resonates in market)

**Confidence Cap:** 65%
**Success Criteria:** Financial can estimate rough CAC; Strategy Partner can validate market positioning

---

#### Standard (1.5 hours)
**Analyses to RUN:**
- Customer segmentation (4-6 primary segments, ranked by attractiveness)
- Buyer persona development (2-3 key personas per segment, decision criteria, pain points)
- Value proposition positioning (vs. competitors, across customer segments)
- Competitive positioning (how are we different; what's our defensible position?)
- Sales process design (stages, sales cycle length, win/loss criteria, deal size by segment)
- Marketing motion (content, channels, lead generation, customer acquisition funnel)
- Messaging framework (core message, supporting pillars, segment-specific variations)
- Pricing & packaging (positioning vs. competitors, packaging strategy, discount strategy)
- Channel strategy (direct vs. indirect vs. partner channels, partner economics)

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Customer segmentation (4-6 segments, size, growth, profitability, competitive intensity for each)
- Buyer personas (2-3 personas per target segment, role, decision criteria, pain points, champion profile)
- Positioning statement (one paragraph: target market, problem we solve, why we're different)
- Competitive positioning (4-6 key competitors assessed, our positioning vs. each, white space identified)
- Sales process (stages, cycle length, win/loss criteria, typical deal size and contract length)
- Marketing motion (lead generation strategy, marketing funnel, estimated conversion rates by stage)
- Messaging framework (one core message + 3-4 supporting pillars, segment-specific messaging)
- Pricing & packaging (price point, packaging options, discount strategy aligned with GTM motion)
- 2-3 GTM assumptions flagged (e.g., "assumes x% sales productivity; assumes y% win rate")

**Confidence Cap:** 80%
**Success Criteria:** Financial can model detailed unit economics; Operating Model can staff sales/marketing appropriately; Product can prioritize features

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Exhaustive customer segmentation (8+ segments with deep profiling)
- Detailed buyer persona research (primary interviews with 10+ prospects/customers per segment)
- Value proposition testing (quantitative validation of message resonance)
- Competitive positioning deep analysis (all major competitors, positioning matrices, white space exploration)
- Sales process optimization (win/loss analysis, sales efficiency benchmarking, deal sizing)
- Marketing motion detailed design (campaign strategy, content roadmap, channel economics)
- Pricing optimization (elasticity analysis, willingness-to-pay research, competitor benchmarking)
- Partner channel strategy (identification of partner channels, partner economics, partnership agreement framework)
- Customer acquisition economics (CAC by channel, by segment, by sales process stage, trend analysis)
- Sales enablement needs (training, tools, content, compensation design)

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- Customer segmentation with deep profiling (8+ segments, size, growth, profitability, competitive dynamics)
- Buyer persona research (3-4 personas per target segment, based on primary research; decision journey mapped)
- Value proposition tested and validated (messaging resonates with 70%+ of target customers in research)
- Competitive positioning matrix (all major competitors mapped, white space identified and validated)
- Sales process designed in detail (stages, average cycle length, win/loss criteria, sales activities, deal economics)
- Marketing motion (lead generation channels and campaigns mapped, conversion funnel modeled, CAC estimated)
- Pricing strategy optimized (elasticity tested, willingness-to-pay research conducted, pricing model validated)
- Channel strategy (direct sales, inside sales, self-serve, partner channels all evaluated, recommendation prioritized)
- Sales enablement plan (training content, sales tools, sales compensation, hiring plan)
- 5+ GTM assumptions with validation through customer research

**Confidence Cap:** 90%+
**Success Criteria:** Go-to-market is fully designed and ready for execution; Financial projections validated by GTM data; market opportunity confirmed

---

### Skill: FINANCIAL STRATEGY

**Role in Engagement:** Model business unit economics, capital requirements, and financial sustainability.

#### Quick Strike (15 min)
**Analyses to RUN:**
- Unit economics estimation (CAC, LTV, payback from GTM assumptions; gross margin estimate)
- Quick 3-year revenue projection (based on growth strategy growth assumptions)
- Capital requirement estimate (rough, order-of-magnitude)

**Analyses to SKIP:**
- Detailed P&L modeling
- Cash flow modeling
- Sensitivity analysis
- Scenario modeling
- Detailed cost structure analysis
- Working capital analysis

**Analyses to COMPRESS:**
- Financial assumptions (use industry benchmarks, no detailed build-up)
- Break-even analysis (simple: when are we cash flow positive?)

**Time Budget:** 15 minutes
**Minimum Output Requirements:**
- Unit economics (CAC, LTV, payback period, estimated at order of magnitude)
- 3-year revenue projection (using growth strategy assumptions; confidence ±40%)
- Estimated capital requirement (rough, with ±30% range)
- One financial kill condition (e.g., "if CAC > $X, unit economics break")

**Confidence Cap:** 60%
**Success Criteria:** Strategy Partner can understand financial viability; decision can proceed if other factors favorable

---

#### Standard (1.5 hours)
**Analyses to RUN:**
- Unit economics modeling (CAC by channel, LTV by segment, payback period, retention curve assumptions)
- Detailed P&L projection (3-5 years, revenue growth tied to growth strategy, cost build-up by function)
- Cash flow projection (3-5 years, including working capital)
- Capital requirement (detailed build-up: product dev, GTM spend, operations, runway)
- Profitability timeline (when break-even, when cash flow positive, when target margin achieved)
- Scenario modeling (base case + downside scenario, financials for each)
- Key financial assumptions (documented and benchmarked)
- Break-even analysis (what volumes are required?)
- Cost structure analysis (variable vs. fixed, key cost drivers)

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Unit economics (CAC, LTV, payback, monthly retention cohort curves, for base case)
- 5-year financial projection (P&L: revenue, COGS, operating expenses by function, EBITDA margin)
- Cash flow projection (5-year, including working capital needs, burn rate, cash runway)
- Capital requirement (product development, GTM spend, working capital, contingency)
- Profitability timeline (when break-even, when cash flow positive, target margin achievement)
- Base case + downside scenario financials (what if growth 30% slower or unit economics 20% worse?)
- Key financial assumptions documented (growth rate, retention, CAC, COGS %, OpEx %)
- Break-even analysis (unit volume or revenue volume required)
- 2-3 financial assumptions flagged for validation

**Confidence Cap:** 80%
**Success Criteria:** Board and investors have financial clarity; capital requirements validated; profitability path clear

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Exhaustive unit economics (CAC by channel + segment, LTV by segment + cohort, detailed retention curves)
- Detailed P&L (5-10 years, revenue build-up by customer segment, detailed cost structure, sensitivity to key drivers)
- Comprehensive cash flow projection (working capital modeling, capital expenditure timing, debt/equity implications)
- Capital requirement (detailed: product dev roadmap costed, GTM spend modeled by phase, working capital build)
- Profitability & return analysis (payback period, return on invested capital, IRR, paths to profitability)
- All 4 scenario modeling (Upside, Base, Downside, Disruptive scenarios, financials for each)
- Sensitivity analysis (which assumptions have biggest financial impact? What's the break-even point?)
- Benchmarking (unit economics, margins, growth rates vs. peer set)
- Path-to-profitability analysis (what must happen for profitability target?)
- Cost structure optimization (where can we flex costs? What are fixed vs. variable?)
- Historical scenario comparison (what happened in similar companies, in similar scenarios?)

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- Exhaustive unit economics (CAC, LTV, payback by all relevant dimensions; retention curves backed by data)
- 10-year financial projection (revenue by segment, detailed cost build-up, profitability path)
- Cash flow projection with working capital dynamics (when is cash flow positive, what's the cash requirement?)
- Detailed capital requirement (phased: what's needed in year 1, year 2, etc.)
- Profitability analysis (break-even, IRR, return on invested capital, payback period)
- All 4 scenarios fully modeled (financials for Upside, Base, Downside, Disruptive)
- Sensitivity analysis (one-way sensitivity on key assumptions: growth rate, CAC, retention, COGS %)
- Benchmarking (unit economics vs. public peer set; growth rates vs. category benchmarks)
- Historical comparison (what happened in analogous companies?)
- Make-or-break financial assumptions clearly surfaced

**Confidence Cap:** 90%+
**Success Criteria:** Finance team can defend model; board/investor ready; capital allocation decisions made with high confidence

---

### Skill: CAPITAL & RESOURCE STRATEGY

**Role in Engagement:** Plan capital allocation, resource optimization, and portfolio prioritization.

#### Quick Strike (10 min)
**Analyses to RUN:**
- Capital requirement snapshot (from Financial Strategy)
- Resource prioritization (which initiatives get funded, which get deferred)

**Analyses to SKIP:**
- Detailed resource modeling
- Portfolio optimization
- Capital allocation alternative scenarios
- Detailed asset management

**Time Budget:** 10 minutes
**Minimum Output Requirements:**
- Capital required (pull from Financial Strategy estimates)
- Top 3 resource priorities for funding
- One deferral or stop decision (what do we NOT fund?)

**Confidence Cap:** 60%
**Success Criteria:** Rumelt Forge understands capital and resource constraints; strategy remains within resource envelope

---

#### Standard (1 hour)
**Analyses to RUN:**
- Capital requirement planning (from Financial Strategy, detailing across years)
- Resource allocation across strategic initiatives (which get funded, when, how much)
- Portfolio prioritization (if capital constraints exist, which initiatives matter most?)
- Resource runway analysis (do we have enough capital, or do we need external funding?)

**Time Budget:** 50 minutes for analysis + 10 minutes for output formatting
**Minimum Output Requirements:**
- Capital required (5-year plan, phase by phase)
- Resource allocation across initiatives (funding prioritization, timeline)
- Portfolio scoring (if capital constrained, scoring of initiatives by strategic importance)
- Resource constraint implications (what can we do, what must we defer?)
- External capital needs (do we need fundraising? When? How much?)

**Confidence Cap:** 80%
**Success Criteria:** Rumelt Forge and all downstream skills understand capital/resource constraints; strategy is executable within envelope

---

#### Deep Dive (2+ hours)
**Analyses to RUN:**
- Comprehensive capital planning (all sources and uses, 5-10 year horizon)
- Resource allocation optimization (maximize strategic value given constraints)
- Portfolio optimization (if constrained, optimal prioritization of initiatives)
- Working capital management (inventory, receivables, payables optimization)
- Asset management (existing assets, optimization, divestiture opportunities)
- Capital structure analysis (debt vs. equity, optimal capital structure)
- Contingency planning (what if fundraising is slower? What if capital is more expensive?)

**Time Budget:** 120 minutes for analysis + 60 minutes for synthesis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Comprehensive capital plan (sources, uses, timing, 5-10 years)
- Resource allocation optimized (all initiatives scored; funding prioritized; trade-offs explicit)
- Portfolio optimization (if capital constrained, what's the optimal portfolio?)
- Working capital management plan (optimization opportunities identified)
- Capital structure analysis (optimal debt/equity mix, capital costs, implications)
- Contingency scenarios (what if capital is unavailable? What if more capital is available?)
- Make-or-break capital assumptions identified

**Confidence Cap:** 90%+
**Success Criteria:** CFO/investor ready; capital allocation decisions defensible; resource constraints managed

---

### Skill: AI-NATIVE STRATEGY

**Role in Engagement:** Accelerate strategy work through agentic analysis and real-time intelligence.

#### Quick Strike (runs parallel to other skills, 20 min)
**Analyses to RUN:**
- Real-time competitive intelligence (news, funding, market movements)
- Rapid market data gathering (public sources on target market)
- Hypothesis validation through public data

**Analyses to SKIP:**
- Deep primary research
- Custom modeling
- Sensitivity analysis

**Time Budget:** 20 minutes (parallel with other skills)
**Minimum Output Requirements:**
- 2-3 recent competitive moves or market developments relevant to decision
- Market data points supporting growth strategy market sizing
- One hypothesis validation or contradiction from public data

**Confidence Cap:** 65%
**Success Criteria:** Intelligence is actionable; accelerates other skill work

---

#### Standard (runs parallel, 1 hour)
**Analyses to RUN:**
- Comprehensive competitive intelligence (recent moves, funding, product changes, personnel)
- Market intelligence (growth trends, customer sentiment, emerging players)
- Real-time scenario monitoring (which scenario is actually unfolding?)
- Contradiction detection (if two skills disagree, flag and suggest synthesis)

**Time Budget:** 60 minutes (parallel with other skills)
**Minimum Output Requirements:**
- Competitive intelligence summary (last 6 months of moves, implications for strategy)
- Market intelligence (growth trends, customer sentiment, emerging competitors)
- Scenario assessment (which scenario is evidence supporting? Which contradicting?)
- Contradiction flags (if Strategy Partner and Rumelt disagree on crux, AI-Native flags and suggests synthesis)

**Confidence Cap:** 80%
**Success Criteria:** Other skills are informed by real-time intelligence; contradictions surface early

---

#### Deep Dive (runs parallel, 4+ hours)
**Analyses to RUN:**
- Deep competitive intelligence (primary research interviews, detailed competitive analysis)
- Comprehensive market research (TAM validation, customer research, emerging trends)
- Scenario monitoring (all 4 scenarios, which evidence supports each)
- Continuous contradiction detection and synthesis
- Real-time assumption validation (every key assumption checked against market data)
- Emerging signal detection (what's changing that could shift the strategy?)

**Time Budget:** 240+ minutes (parallel with other skills, providing intelligence to all)
**Minimum Output Requirements:**
- Detailed competitive intelligence (comprehensive competitor analysis, recent moves, strategic positioning)
- Market research findings (TAM validation, customer research, emerging trends, disruption signals)
- Scenario assessment (probability weighting of all 4 scenarios based on current evidence)
- Assumption validation (every critical assumption cross-checked against external data)
- Emerging signals (what's changing that could invalidate the strategy?)
- Contradiction tracking (all disagreements surfaced, synthesis proposed)

**Confidence Cap:** 90%+
**Success Criteria:** Strategy is grounded in real-time market reality; assumptions continuously validated; contradictions resolved early

---

### Skill: RUMELT STRATEGY FORGE (continued from above)

### Skill: OPERATING MODEL

**Role in Engagement:** Design org structure, governance, and operating model to execute strategy.

#### Quick Strike (10 min)
**Analyses to RUN:**
- Org structure snapshot (if strategy requires org change, define at high level)
- Governance decisions (decision rights, escalation)

**Analyses to SKIP:**
- Detailed span of control analysis
- Process design
- Governance framework design

**Time Budget:** 10 minutes
**Minimum Output Requirements:**
- Org structure (simplified: major functions and reporting lines)
- Key decision owner for each Coherent Action
- One governance rule (e.g., "GTM decisions owned by VP Marketing")

**Confidence Cap:** 60%
**Success Criteria:** People & Talent understands basic org structure; Rumelt understands who owns each action

---

#### Standard (1 hour)
**Analyses to RUN:**
- Org design (functions, reporting structure, span of control, headcount plan)
- Governance framework (decision rights, escalation, regular forums)
- Operating rhythm (cadence of strategy reviews, performance reviews)
- Process design (key processes that enable strategy execution)
- Change management (what changes, how are people impacted?)
- Support functions (finance, HR, IT, communications roles)

**Time Budget:** 50 minutes for analysis + 10 minutes for output formatting
**Minimum Output Requirements:**
- Org structure (functions, reporting lines, 3-year headcount plan)
- Governance framework (decision rights, escalation authority, forums/cadence)
- Operating rhythm (monthly/quarterly reviews, decision cycles)
- Key processes (sales, product development, financial planning, customer success)
- Org change plan (what changes, timeline, change management approach)
- Support function roles (what do finance, HR, IT, comms do to enable strategy?)
- 1-2 org design assumptions flagged

**Confidence Cap:** 80%
**Success Criteria:** People & Talent can design talent model; all downstream execution understood

---

#### Deep Dive (2+ hours)
**Analyses to RUN:**
- Comprehensive org design (all functions, detailed role design, span/salary band mapping)
- Detailed governance framework (decision rights, escalation rules, role clarity)
- Operating rhythm (detailed cadence, forums, decision protocols)
- Detailed process design (all key processes, end-to-end flow, decision points)
- Org change management (detailed change plan, stakeholder impact analysis, communication plan)
- Capability gaps (what new capabilities do we need? Who do we hire vs. develop?)
- Organizational network analysis (how does information flow? Where are bottlenecks?)
- Culture & values alignment (what org culture does strategy require?)

**Time Budget:** 120 minutes for analysis + 60 minutes for synthesis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Comprehensive org structure (all roles, reporting lines, 5-year plan, span of control analysis)
- Detailed governance framework (all decisions mapped, owner, escalation rule, forum)
- Operating rhythm (all forums, cadence, decision authorities)
- Process design (all critical processes, detailed flow, decision points)
- Change management plan (what changes, stakeholder impact, communication, timeline)
- Capability assessment (current vs. required, hiring plan, development plan)
- Organizational network analysis (how does info flow? Bottlenecks identified)
- Culture implications (what culture does strategy require? How do we get there?)

**Confidence Cap:** 90%+
**Success Criteria:** Board-ready org design; People & Talent can execute with high fidelity; all downstream skills have clear org context

---

### Skill: GTM STRATEGY (MARKET ENTRY)

When GTM Architect focuses on market entry (vs. GTM for existing product), specifications are same as above (GTM STRATEGY section), except:

**Quick Strike:** Focus on entry approach (partner vs. acquisition vs. greenfield) only
**Standard:** Include entry approach, local go-to-market motion, pricing by geography
**Deep Dive:** Include regulatory analysis, local competitive landscape, detailed market entry roadmap

---

### Skill: PEOPLE & TALENT STRATEGY

**Role in Engagement:** Design talent model, org culture, and people operating model to execute strategy.

#### Quick Strike (10 min)
**Analyses to RUN:**
- Headcount requirement snapshot (from Operating Model)
- Key hiring decisions (who do we need to hire for the Coherent Actions?)

**Analyses to SKIP:**
- Detailed compensation design
- Culture architecture
- Talent development planning
- Succession planning

**Time Budget:** 10 minutes
**Minimum Output Requirements:**
- Headcount estimate (approximate total FTE from Operating Model)
- Top 5 critical hires (roles and timing)
- One staffing assumption (e.g., "assumes we can hire senior engineering 20% faster than market")

**Confidence Cap:** 60%
**Success Criteria:** Rumelt understands staffing implications; Financial can model payroll

---

#### Standard (1.5 hours)
**Analyses to RUN:**
- Talent model design (what roles, what skills, what levels)
- Headcount planning (3-year plan by function, phased)
- Compensation design (salary bands, variable comp, equity)
- Recruiting strategy (where do we source, how long to fill, costs)
- Culture & values architecture (what culture enables strategy?)
- Retention strategy (how do we keep key talent?)
- Development planning (what skills must we build internally vs. hire?)
- Leadership transition plan (any key transitions needed?)

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Talent model (key roles, required skills, experience level, compensation level)
- Headcount plan (3-year, by function, phased with strategy rollout)
- Compensation framework (salary bands, variable comp structure, equity plan)
- Recruiting strategy (source, time-to-fill estimates, cost per hire)
- Culture architecture (what values, what behaviors, how do we build?)
- Retention strategy (engagement levers, development opportunities)
- 2-3 talent assumptions flagged (time-to-fill, retention rates, comp costs)

**Confidence Cap:** 80%
**Success Criteria:** Finance can model talent costs; org understands talent requirements; hiring strategy is executable

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Comprehensive talent model (all roles, detailed job descriptions, skills matrices, competency levels)
- Detailed headcount planning (5-year plan, phased with strategy execution)
- Total compensation design (base, variable, equity, benefits optimization)
- Recruiting strategy deep dive (sourcing strategy by role, time-to-fill by role, recruiting budget)
- Compensation benchmarking (market benchmarking, equity value analysis)
- Culture & values design (detailed culture architecture, alignment with strategy, building plan)
- Talent development (skill development paths, mentoring, training, career progression)
- Succession planning (for key roles, who's ready now, who needs development?)
- Diversity & inclusion (representation goals, inclusive hiring, inclusion culture)
- Employee experience (engagement, retention, development, career growth)
- Organizational change management (managing transitions, supporting people through change)

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- Comprehensive talent model (all roles, skills, competencies, career paths)
- 5-year headcount plan (phased, by function, with hiring timeline)
- Total compensation framework (base salary, variable comp, equity, benefits)
- Recruiting strategy (sourcing, time-to-fill, recruiting budget, hiring timeline)
- Compensation benchmarking (vs. market, cost implications)
- Culture design (values, behaviors, building plan, alignment with strategy)
- Talent development program (skill development, mentoring, training, career paths)
- Succession plan (key roles, readiness assessment, development plans)
- D&I strategy (representation goals, inclusive hiring, inclusion culture)
- Make-or-break talent assumptions identified

**Confidence Cap:** 90%+
**Success Criteria:** Talent strategy is fully designed and executable; board-ready; all org change impacts understood

---

### Skill: PRODUCT INNOVATION STRATEGY

**Role in Engagement:** Define product roadmap, feature priorities, and product-market fit validation.

#### Quick Strike (15 min)
**Analyses to RUN:**
- PMF assessment (does the product drive retention/expansion?)
- Feature priority snapshot (which 2-3 features are must-have for PMF?)

**Analyses to SKIP:**
- Detailed product roadmap
- Customer research
- Product metrics design
- Pricing by feature

**Time Budget:** 15 minutes
**Minimum Output Requirements:**
- PMF confidence (high/medium/low) with one-sentence rationale
- Top 3 must-have features (for PMF or market win)
- One PMF assumption to validate (e.g., "feature X drives 80% of retained usage")

**Confidence Cap:** 65%
**Success Criteria:** GTM Architect can design GTM; Strategy Partner can assess market fit

---

#### Standard (1.5 hours)
**Analyses to RUN:**
- PMF validation (customer data: retention, expansion, churn, NPS)
- Feature prioritization (MoSCoW: must/should/could/won't have)
- Product roadmap (12-24 months, phased with GTM and growth strategy)
- Customer research (what do customers want? What are they willing to pay for?)
- Product metrics (retention, expansion, churn, unit economics by feature)
- Competitive product positioning (how are we differentiated?)
- Technical requirements (what backend/infrastructure is required?)

**Time Budget:** 90 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- PMF assessment (confidence level, supporting customer metrics: retention, NPS, expansion)
- Feature prioritization (must-haves for PMF, nice-to-haves for competitive positioning)
- Product roadmap (12-24 month plan, phased with GTM motion)
- Customer insights (what drives retention/expansion, churn analysis, customer feedback themes)
- Product metrics defined (what we measure, how we measure PMF, how we measure success)
- Product positioning (vs. competitors, differentiation, customer value proposition)
- Technical requirements (backend, infrastructure, data requirements)
- 2-3 product assumptions flagged (e.g., "assumes feature X drives 70% retention")

**Confidence Cap:** 80%
**Success Criteria:** GTM Architect can design positioning; Growth Strategy can model unit economics

---

#### Deep Dive (3+ hours)
**Analyses to RUN:**
- Deep PMF validation (cohort analysis, retention curves, NPS trend, qualitative customer research)
- Detailed feature prioritization (customer research, market research, technical feasibility)
- Comprehensive product roadmap (12-36 months, all features, all phases, all resources)
- Customer research (in-depth interviews, surveys, usage analytics)
- Product metrics framework (all metrics, definitions, targets)
- Competitive product analysis (detailed feature comparison, positioning, roadmap comparison)
- Technical architecture (systems, data, infrastructure, scalability requirements)
- Pricing optimization (willingness-to-pay, price-feature optimization)
- Product strategy (where do we concentrate product excellence? Where do we match competition?)

**Time Budget:** 200+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- Deep PMF assessment (cohort data, retention curves, expansion metrics, churn analysis)
- Detailed feature prioritization (customer research validated, market research validated)
- Comprehensive product roadmap (36 months, all features, resource requirements, timeline)
- Customer research findings (in-depth themes, validation of assumptions)
- Product metrics framework (all metrics, targets, tracking plan)
- Competitive analysis (detailed positioning, differentiation, white space)
- Technical architecture (systems, data, infrastructure, scalability, security)
- Pricing strategy (elasticity, willingness-to-pay, price-feature mapping)
- Product strategy (where do we win? Where do we hold?)
- Make-or-break product assumptions identified

**Confidence Cap:** 90%+
**Success Criteria:** Product roadmap is fully designed, validated, and resourced; GTM can execute with confidence

---

### Skill: TECHNOLOGY & DIGITAL STRATEGY

**Role in Engagement:** Define technology roadmap, digital transformation, and technology-enabled capability.

#### Quick Strike (10 min)
**Analyses to RUN:**
- Tech capability gap snapshot (what tech capabilities does strategy require that we don't have?)
- Key tech priority (one tech initiative that enables/unlocks strategy)

**Analyses to SKIP:**
- Detailed systems architecture
- Technology roadmap
- Digital transformation roadmap

**Time Budget:** 10 minutes
**Minimum Output Requirements:**
- Tech capability gap (one-sentence description of what we need)
- Top 1-2 tech initiatives (highest priority for strategy success)
- One tech assumption (e.g., "assumes we can build this in 6 months with current team")

**Confidence Cap:** 60%
**Success Criteria:** Rumelt Forge understands tech constraints; Technology Strategy can expand

---

#### Standard (1 hour)
**Analyses to RUN:**
- Technology capability assessment (current state, future state needed)
- Tech roadmap (12-24 months, phased with strategy)
- Build vs. buy vs. partner decisions (where do we build internally? Where do we buy/partner?)
- Data & analytics strategy (what data do we need? How do we get it? How do we use it?)
- Security & compliance (what's required? What's optional?)
- Infrastructure & scalability (can we scale to our growth targets?)
- Technology talent requirements (what skills do we need?)

**Time Budget:** 50 minutes for analysis + 10 minutes for output formatting
**Minimum Output Requirements:**
- Tech capability assessment (current state rated, future state defined, gap analysis)
- Tech roadmap (12-24 months, key systems/capabilities, phased with strategy)
- Build vs. buy decisions (for each major capability, build/buy/partner rationale)
- Data & analytics strategy (what data, where from, how used, governance)
- Security & compliance (requirements, implementation plan)
- Infrastructure plan (scalability to growth targets, cost implications)
- Tech talent plan (required skills, hiring/development plan)
- 1-2 tech assumptions flagged

**Confidence Cap:** 80%
**Success Criteria:** Financial can model tech capex; Operating Model understands tech constraints; growth scalable

---

#### Deep Dive (2+ hours)
**Analyses to RUN:**
- Comprehensive technology assessment (current state, future state, detailed gap analysis)
- Detailed technology roadmap (24-36 months, all systems, all phases, all resources)
- Build vs. buy vs. partner analysis (detailed for each major capability)
- Data strategy (comprehensive: what data, where from, data quality, governance, data infrastructure)
- Digital transformation roadmap (if transforming, detailed transformation program)
- Architecture design (system architecture, integration points, scalability, security)
- Technology security & compliance (comprehensive: requirements, controls, governance)
- Technology talent strategy (required skills, hiring/development plan, retention)
- Technology cost analysis (capex, opex, TCO by option)
- Innovation strategy (emerging tech, strategic importance, investment priority)

**Time Budget:** 120 minutes for analysis + 60 minutes for synthesis + 30 minutes for output formatting
**Minimum Output Requirements:**
- Comprehensive tech assessment (current state rated, future state defined, detailed gap)
- Detailed tech roadmap (36 months, all systems, resources, phased with strategy)
- Build vs. buy decisions (detailed analysis for each major capability)
- Data strategy (comprehensive: collection, quality, governance, infrastructure)
- Digital transformation (if applicable, detailed transformation program)
- Architecture design (system design, integration, scalability, security)
- Security & compliance (comprehensive framework, controls, governance)
- Tech talent plan (skills, hiring, development, retention)
- Tech cost analysis (capex, opex, ROI by initiative)
- Make-or-break tech assumptions identified

**Confidence Cap:** 90%+
**Success Criteria:** Technology roadmap is fully designed and executable; digital transformation (if needed) is planned; scalability confirmed

---

### Skill: M&A & CORPORATE DEVELOPMENT

**Role in Engagement:** Evaluate M&A opportunities, develop acquisition thesis, design integration.

#### Quick Strike (20 min)
**Analyses to RUN:**
- M&A thesis snapshot (why would we acquire? What value?)
- Strategic fit assessment (how does this fit our strategy?)
- Deal structure snapshot (rough economics, structure)

**Analyses to SKIP:**
- Detailed due diligence
- Integration planning
- Detailed financial modeling

**Time Budget:** 20 minutes
**Minimum Output Requirements:**
- M&A thesis (why acquire, what value, in one sentence)
- Strategic fit (how does this fit our competitive position, scale strategy, or capability building?)
- Deal economics (rough: acquisition price, integration costs, value capture, IRR estimate ±50%)
- One key risk (e.g., "retention risk for key acquired talent")

**Confidence Cap:** 60%
**Success Criteria:** Board can assess basic M&A logic; deeper analysis requested if thesis is compelling

---

#### Standard (2 hours)
**Analyses to RUN:**
- M&A thesis development (why acquire, what value, what alternative approaches)
- Strategic fit analysis (how does this fit our strategy, competitive positioning, capabilities?)
- Target assessment (competitive position, market position, growth rate, profitability)
- Financial analysis (historical financials, valuation, integration costs, synergy case)
- Integration planning (high-level: how would we integrate? What's the plan?)
- Risk assessment (key risks, retention risk, integration complexity, market risks)
- Deal structure (offer structure, timeline, governance during integration)

**Time Budget:** 120 minutes for analysis + 30 minutes for output formatting
**Minimum Output Requirements:**
- M&A thesis (why acquire, what value, vs. organic alternative)
- Strategic fit (positioning logic, capability logic, scale logic)
- Target company assessment (business model, financials, growth, market position)
- Financial analysis (valuation, acquisition price recommendation, integration cost estimate, synergy case)
- Integration plan (high-level: org integration, system integration, talent integration)
- Risk assessment (key risks, probabilities, mitigation)
- Deal structure (offer price, earnout, term sheet outline, timeline)
- 2-3 acquisition assumptions flagged

**Confidence Cap:** 80%
**Success Criteria:** Board can make proceed/no-proceed decision; detailed due diligence can proceed if approved

---

#### Deep Dive (4+ hours)
**Analyses to RUN:**
- Comprehensive M&A thesis (multiple acquisition targets evaluated, rationale for each)
- Deep strategic fit analysis (how does target help us win in market?)
- Target deep dive (financial analysis, customer analysis, product analysis, team analysis)
- Detailed financial analysis (historical financials, adjusted EBITDA, valuation multiples, sensitivity)
- Detailed synergy analysis (revenue synergies, cost synergies, integration costs, timeline to realization)
- Detailed integration planning (org design, system integration, cultural integration, 100-day plan)
- Risk assessment deep dive (retention risk, integration complexity, cultural risk, market risk)
- Deal negotiation strategy (valuation strategy, negotiation framework, walk-away price)
- Post-acquisition management (performance tracking, integration management, value realization)

**Time Budget:** 240+ minutes for analysis + 60 minutes for synthesis + 60 minutes for output formatting
**Minimum Output Requirements:**
- M&A thesis (multiple targets evaluated, recommended target with detailed rationale)
- Strategic fit (detailed logic: positioning, capabilities, scale, competitive advantage)
- Target assessment (financial analysis, customer analysis, competitive position, team)
- Valuation analysis (historical multiples, comparable transactions, valuation range, recommended price)
- Synergy case (revenue synergies detailed, cost synergies detailed, integration cost, timeline to realization, confidence)
- Integration plan (100-day plan, org design, system integration, talent integration, cultural integration)
- Risk assessment (retention, integration, market, financial risks with probabilities and mitigations)
- Deal negotiation strategy (valuation strategy, negotiation approach, walk-away price, earnout structure)
- Make-or-break assumptions identified

**Confidence Cap:** 90%+
**Success Criteria:** M&A opportunity is fully evaluated and ready for board decision; integration is planned and ready for execution

---

## 4. Speed Mode Coordination Rules

When skills operate at different speeds within a single engagement, apply these rules to prevent mismatches:

### Rule 1: Speed Inheritance (Default)
- When a downstream skill needs output from an upstream skill, the downstream skill operates at the upstream speed
- Example: If Rumelt Forge is Standard mode but depends on Strategy Partner diagnosis, Strategy Partner must be Standard too
- **Implication:** All skills in an engagement must be same speed (no mixing Quick Strike diagnostic with Standard execution)

### Rule 2: Speed Mismatch Detection
When a speed mismatch is detected (e.g., GTM needs full analysis but Rumelt output is QS):
- Flag explicitly: "Speed mismatch detected: Rumelt Quick Strike (kernel score only) but GTM Standard (needs detailed actions)"
- Offer three options:
  1. Rumelt shifts to Standard mode to provide detailed Coherent Actions
  2. GTM shifts to Quick Strike mode (less detailed unit economics)
  3. Pause and request more time for properly-matched execution
- Do NOT proceed with mismatched speeds without explicit user decision

### Rule 3: Auto-Degradation
If a skill begins in Standard mode but finds it doesn't have required data, degrade gracefully:
- Communicate explicitly: "Downgrading GTM to Quick Strike because customer research data unavailable"
- Confidence cap at Quick Strike level (65% max)
- Flag for follow-up validation once data is available
- Do NOT try to execute Standard-mode output with Quick Strike data

### Rule 4: Speed Acceleration
If a skill finishes early (QS analysis confident in 30 min) and has time budget remaining:
- Can optionally shift to Standard mode mid-engagement (e.g., "completing QS in 30 min, using remaining 30 min for additional Standard-mode analysis")
- Flag explicitly: "Strategy Partner complete QS in 30 min; shifting to Standard for Scenario Planning"
- New confidence cap is Standard cap (80%)

---

## 5. Quality Expectations by Speed Mode

| Dimension | Quick Strike (60 min) | Standard (4 hours) | Deep Dive (20+ hours) |
|---|---|---|---|
| **Minimum Confidence** | 60-70% | 80%+ | 90%+ |
| **Analyses Run** | Core framework only | All core + supporting | All + exploratory + stress testing |
| **Data Sources** | Existing knowledge + public | Internal + benchmarks | All sources + primary research |
| **Scenarios Modeled** | 1 (usually Base) | 2-3 (Base, Downside, Upside) | All 4 (+ stress testing) |
| **Iterations Allowed** | 0 (first-pass only) | 1-2 cycles | 3+ cycles |
| **Benchmarking** | Industry norms only | Vs. peer set | Comprehensive + historical |
| **Validation** | Hypothesis confirmation | Assumption cross-check | Primary research validation |
| **Decision Readiness** | Directional | Defensible | Board-ready |
| **External Intelligence** | Public sources only | Public + paid databases | All sources + interviews |
| **Assumption Testing** | None | Documented, cross-checked | Detailed validation plan |

---

## 6. Risk Assessment by Speed Mode

Different decision types are appropriate at different speed modes. Use this matrix to ensure decision risk is matched to analysis depth:

### Quick Strike (60 min) Risk Profile

**APPROPRIATE DECISIONS (Low Risk / Reversible):**
- Directional market moves ("Should we enter market X?")
- Feature priority tweaks
- Messaging/positioning variants
- Quarterly plan adjustments
- Headcount hiring freeze (temporary)
- Pricing optimization within existing model
- Decision point delays (pausing a decision until more data)

**INAPPROPRIATE DECISIONS (Too Risky):**
- M&A valuation or deal structure
- Capital allocation > $5M
- Org restructuring (layoffs)
- Major pricing changes
- Technology platform changes
- Go-to-market complete redesign
- Strategic pivots
- Entering new markets (without Standard+ analysis)

### Standard Mode (4 hours) Risk Profile

**APPROPRIATE DECISIONS (Medium Risk / Partially Reversible):**
- Quarterly strategy adjustments
- New market entry (with Standard analysis)
- New product line launch
- GTM redesign
- Org restructuring (org redesign, not layoffs)
- Technology roadmap
- Pricing strategy changes
- Capital allocation $5M-$50M
- Talent acquisition strategy
- Competitive positioning shifts

**INAPPROPRIATE DECISIONS (Too Risky):**
- M&A due diligence (requires Deep Dive)
- Capital allocation > $50M
- Org-wide transformation
- Business model pivot
- Irreversible market commitments
- Major asset divestiture
- Complete digital transformation

### Deep Dive (20+ hours) Risk Profile

**APPROPRIATE DECISIONS (High Risk / Mostly Irreversible):**
- M&A acquisition (any size)
- Capital allocation > $50M
- Org-wide transformation
- Business model pivot / strategic repositioning
- Complete digital transformation
- Major market exit / withdrawal
- Complete product pivot
- Major org restructuring with layoffs
- Entering new business lines
- Entering new geographies (new regions/countries)

---

## 7. Speed Mode Selection Flowchart (ASCII)

```
┌─────────────────────────────────────────────────────────────────┐
│                    START: NEW ENGAGEMENT                         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
         ┌──────────────────────────────────────┐
         │   What is the TIME PRESSURE?          │
         └──────────────────────────────────────┘
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
   < 24 hrs          1-7 days           > 7 days
   (Board                (This           (Planned
    meeting              week)            review)
   tonight)
        │                   │                   │
        ↓                   ↓                   ↓
   QUICK            Continue to Q2         Continue to Q2
   STRIKE
   (60 min)
                ┌───────────────────────────────────────┐
                │   What is the COMPLEXITY?              │
                └───────────────────────────────────────┘
                                ↓
                ┌───────────────┬───────────────┐
                ↓               ↓               ↓
            Single         Multi-domain    Portfolio/
            domain         (3+ areas)       Transform
            │              │                │
            ↓              ↓                ↓
        Check Q3       Continue to Q3   DEEP DIVE
        │              │                (20+ hrs)
        └──────┐  ┌────┘
               ↓  ↓
        ┌──────────────────────────────────────┐
        │   What is DATA AVAILABILITY?          │
        └──────────────────────────────────────┘
                        ↓
        ┌──────────────┬───────────────┐
        ↓              ↓               ↓
      RICH          SPARSE            NO
      DATA           DATA            DATA
      │              │               │
      ↓              ↓               ↓
   Can be      Extend time/      DEEP DIVE
   QUICK or    shift to           (20+ hrs)
   STANDARD   STANDARD
        │
        └──────────┐
                   ↓
         ┌─────────────────────────────────────┐
         │   What is DECISION STAKES?          │
         └─────────────────────────────────────┘
                        ↓
         ┌──────────────┬───────────────────┐
         ↓              ↓                   ↓
      LOW            MEDIUM              HIGH
    (<$1M,         ($1-50M,          (>$50M,
    reversible)    partial)        irreversible)
         │              │                   │
         ↓              ↓                   ↓
    QUICK STRIKE   STANDARD            DEEP DIVE
    (60 min)      (4 hours)           (20+ hours)


┌─────────────────────────────────────────────────────┐
│              FINAL DECISION                          │
├─────────────────────────────────────────────────────┤
│ QUICK STRIKE:                                       │
│   • 60 min total duration                          │
│   • Directional guidance                           │
│   • 60-70% confidence max                          │
│   • Reversible decisions only                      │
│                                                    │
│ STANDARD:                                          │
│   • 4-6 hours total duration                       │
│   • Defensible recommendations                     │
│   • 80%+ confidence                                │
│   • Most strategic decisions                       │
│                                                    │
│ DEEP DIVE:                                         │
│   • 20+ hours total duration                       │
│   • Exhaustive analysis                            │
│   • 90%+ confidence                                │
│   • High-stakes/irreversible decisions             │
└─────────────────────────────────────────────────────┘
```

---

## 8. Implementation Guidance

Every skill MUST include a "Speed Mode Configuration" section in its SKILL.md file that maps back to this document, specifying:

1. What analyses run/skip/compress at each speed
2. Time budget at each speed
3. Confidence cap at each speed
4. Minimum output requirements at each speed
5. Success criteria for each speed

All skills must be capable of executing at all three speeds independently. If a skill cannot execute at Quick Strike speed, that limitation must be documented with reasoning.

---

**End of Speed Mode Document**

This document is the definitive guide for speed mode execution. Every engagement MUST explicitly select a speed mode at the start and maintain it throughout (unless a formal speed mismatch is detected and resolved by user decision).

**Version:** 1.0 | **Last Updated:** 2026-03-10
