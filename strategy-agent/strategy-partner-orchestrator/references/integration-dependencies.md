# Skill Dependency Map - Echo Skills Integration

**Purpose:** Complete reference for all 16 skills' dependencies, inputs, outputs, and quality gates. These are blocking constraints, not suggestions.

**Version:** 5.0 | **Updated:** 2026-03-10

---

## 1.1 Market Intelligence

**Purpose:** Real-time data collection and analysis. Feeds all diagnostic and strategy skills with external competitive, customer, and market data.

**Classification:** Cross-layer / Cross-skill dependency

**Hard Dependencies:** None (can start immediately)

**Inputs Required:**
- Search domain (competitor names, markets, industry segments)
- Analysis focus (product launches, funding, market trends, customer sentiment)
- Time horizon (last 30 days, last 90 days, year-to-date)

**Outputs Produced:**
- Competitor playbook (positioning, product roadmap, go-to-market approach)
- Market trend analysis (growth rates, consolidation, disruption signals)
- Customer sentiment synthesis (satisfaction, switching intent, pain points)
- Valuation benchmarks and comparable data
- Confidence level per finding (H/M/L with evidence source)

**Consumed By:** Strategy Partner, Rumelt Forge, Growth Strategy, GTM Strategy, AI-Native Strategy, Product Innovation, Technology Strategy, M&A & Corp Dev

**Timing:** 1-2 days (can run in parallel with initial diagnosis)

**Quality Gates:**
- All sources dated and ranked by recency
- At least 3 independent sources per major claim
- Confidence tagged H/M/L based on source quality
- Assumptions flagged (e.g., "assuming pricing stable" or "based on 2-month-old data")

---

## 1.2 Strategy Partner

**Purpose:** Diagnostic analysis. Frames the decision, synthesizes problem understanding, creates decision framework.

**Classification:** Layer 1 (Corporate & Portfolio)

**Hard Dependencies:** Market Intelligence (optional but recommended for strength of analysis)

**Inputs Required:**
- Client situation (revenue, growth, stage, market position, urgency)
- Core decision or problem statement
- Available time/budget constraints
- Prior analyses or strategy (if any)

**Outputs Produced:**
- Situation summary (2-3 sentence executive summary)
- Key findings (3-5 major discoveries with evidence and confidence)
- Problem classification (Competitive / Growth / Operational / Financial / Org / Tech / GTM / M&A / Other)
- Root cause hypothesis (our best theory about what's really driving the problem)
- Decision frame (if-then logic on key levers)
- Confidence score (% on analytical base)
- Critical assumptions flagged for validation
- Recommended next skill(s) (always Rumelt Forge for strategy, or domain skills for functional decisions)

**Consumed By:** Rumelt Forge (primary), Hypothesis Testing (validates assumptions), Execution Monitoring (tracks whether diagnosis was correct)

**Timing:** 0.5-1.5 days depending on situation complexity and available data

**Quality Gates:**
- Confidence ≥70% before handing to Rumelt Forge (or explicitly flag <70% and request more analysis)
- MECE problem tree (mutually exclusive, collectively exhaustive)
- At least 3 independent evidence sources for major findings
- Kill conditions explicit (what would invalidate this diagnosis)

---

## 1.3 Hypothesis Testing

**Purpose:** Assumption validation. Systematically tests strategic assumptions via designed experiments.

**Classification:** Layer 6 (Learning & Adaptation)

**Hard Dependencies:** Strategy Partner output (assumptions to test) OR Rumelt Forge output (assumptions embedded in kernel)

**Inputs Required:**
- List of critical assumptions (from Strategy Partner or Rumelt)
- Confidence level of each assumption (starting confidence)
- Business impact of each assumption (what happens if wrong?)
- Available data/research budget

**Outputs Produced:**
- Hypothesis test plan (experiments designed to validate/invalidate each assumption)
- Test results (validated / invalidated / inconclusive)
- Updated confidence levels (post-test)
- Pivot recommendations (if assumptions invalidated, what changes?)
- Confidence matrix (which assumptions are highest risk, most uncertain)

**Consumed By:** Strategy Partner (updates diagnosis), Rumelt Forge (updates strategy if assumptions invalidated), All functional skills (use validated assumptions)

**Timing:** 2-5 days (depends on complexity of validation, data availability)

**Quality Gates:**
- Experiments are designed before execution (not ad-hoc)
- Sample size sufficient for statistical validity
- Control variables identified
- Success criteria pre-defined (what would "validate" this assumption?)

---

## 1.4 Rumelt Strategy Forge

**Purpose:** Strategy creation. Builds the coherent strategy kernel from diagnostic intelligence.

**Classification:** Layer 2 (Competitive & Business Model)

**Hard Dependencies:** Strategy Partner output (REQUIRED - cannot forge strategy without diagnosis)

**Inputs Required:**
- Strategic diagnosis (from Strategy Partner)
- Competitive position analysis (what can we do that competitors can't?)
- Market dynamics (what's changing in market that creates opportunity?)
- Capability map (what can we actually execute?)
- Validated assumptions (from Hypothesis Testing, if available)

**Outputs Produced:**
- The Crux (singular challenge that must be solved)
- Strategy Kernel:
  - Diagnosis (explanatory framework)
  - Guiding Policy (approach that creates competitive advantage)
  - Coherent Actions (3-5 specific, coordinated moves with owner/timeline/resources)
- Validation Scores:
  - Bad Strategy Detector (X/16)
  - Coherence (overall X/100, breakdown: internal/external/execution)
  - Confidence (HIGH/MEDIUM/LOW)
- Kill conditions (when we abandon this strategy)
- Assumptions flagged for post-implementation validation
- Recommended next skill(s) (Operating Model, GTM, Financial, People, Product, Technology based on strategy)

**Consumed By:** Operating Model, GTM Strategy, Financial Strategy, People & Talent, Product Innovation, Technology Strategy, Change Management, Execution Monitoring, Atlas Report Template

**Timing:** 0.5-1.5 days (depends on diagnostic complexity)

**Quality Gates:**
- Coherence score ≥70/100 (must be tested across all 3 dimensions: internal/external/execution)
- Bad Strategy Detector ≥8/16 (if <8, major revision needed)
- All Coherent Actions are SPECIFIC (not vague), with owner and timeline
- Strategy can be explained in 2 paragraphs or less (sign of clarity)

---

## 1.5 Growth Strategy

**Purpose:** Growth modeling. Forecasts revenue potential, unit economics, and growth curve by market/segment/lever.

**Classification:** Layer 1 (Corporate & Portfolio)

**Hard Dependencies:** Strategy Partner (required), Market Intelligence (required for benchmarking)

**Inputs Required:**
- Market opportunity (total addressable market, serviceable addressable market)
- Competitive position (our market share vs. competitors)
- Growth levers (pricing, feature set, go-to-market, market segment, geography)
- Historical growth data (if company has history)
- Scenario assumptions (Upside/Base/Downside scenarios)

**Outputs Produced:**
- Market sizing (TAM/SAM/SOM for each growth opportunity)
- Growth curve modeling (acquisition/retention/expansion dynamics)
- Unit economics by growth lever (CAC, LTV, payback period, margin)
- Scenario financial modeling (Upside/Base/Downside growth trajectories)
- Growth opportunity ranking (which lever has highest impact?)
- Key assumptions documented (growth rate, churn rate, pricing assumptions)

**Consumed By:** Financial Strategy (uses unit economics), GTM Strategy (designs motion around growth levers), Rumelt Forge (informs strategy kernel), Execution Monitoring (tracks growth performance vs. model)

**Timing:** 1-2 days

**Quality Gates:**
- Market sizing supported by external benchmarks (not just bottoms-up estimates)
- Unit economics modeled across 3+ years (not just Year 1)
- Key assumptions called out (growth rate, churn, pricing, CAC)
- Confidence levels assigned to each growth lever

---

## 1.6 GTM Strategy

**Purpose:** Go-to-market design. Creates customer acquisition motion, pricing, channels, sales process.

**Classification:** Layer 3 (Execution Design)

**Hard Dependencies:** Product Innovation (REQUIRED - PMF validation), Rumelt Forge (required for strategy context), Growth Strategy (optional but recommended for unit economics)

**Inputs Required:**
- Product positioning (what does product solve?)
- Target customer (customer segmentation, personas)
- Value proposition (why should customers choose us?)
- Competitive positioning (how are we different/better?)
- Revenue targets (from Financial Strategy or Rumelt Forge)
- Budget constraints (what can we spend on GTM?)
- Market context (from Market Intelligence)

**Outputs Produced:**
- Customer segmentation and targeting (which customer segments first?)
- Value proposition and messaging (how do we communicate value?)
- Pricing strategy (list price, discounting, packaging)
- Sales motion (direct, channel, inside, field sales?)
- Marketing motion (awareness, demand generation, brand)
- Channel strategy (which channels to market, which to partners?)
- CAC assumption (cost per customer acquired)
- Sales process (discovery, demo, negotiation, close)
- GTM timeline and phasing (what launches when?)

**Consumed By:** Financial Strategy (uses CAC), Operating Model (informs sales org design), Execution Monitoring (tracks CAC/LTV vs. targets)

**Timing:** 0.5-1.5 days

**Quality Gates:**
- CAC assumption validated against benchmarks (in collaboration with Financial Strategy)
- Sales process end-to-end defined (not vague)
- Customer segmentation MECE (no overlap, collectively covers target market)
- Pricing strategy justified (not arbitrary)

---

## 1.7 Financial Strategy

**Purpose:** Financial modeling. Creates revenue projections, unit economics, path to profitability.

**Classification:** Layer 3 (Execution Design)

**Hard Dependencies:** Rumelt Forge (required for strategy context), Growth Strategy (required for unit economics), GTM Strategy (required for CAC validation)

**Inputs Required:**
- Strategy kernel (from Rumelt Forge)
- Growth model (from Growth Strategy)
- GTM assumptions (CAC from GTM Strategy)
- Operating cost model (from Operating Model or People & Talent)
- Capital constraints (how much can we raise/invest?)
- Time horizon (3, 5, or 10 year model?)

**Outputs Produced:**
- Unit economics by customer segment (LTV, CAC, payback, margin)
- Revenue projections (3-5 year, scenario-based)
- Operating cost structure (fixed + variable costs)
- Cash flow projections (when do we break even?)
- Profitability timeline (path to positive EBITDA)
- Capital requirement (total investment needed)
- Sensitivity analysis (what assumptions are most sensitive?)
- Price elasticity modeling (if applicable)
- Scenario financial models (Upside/Base/Downside)

**Consumed By:** Rumelt Forge (validates kernel feasibility), Capital & Resource Strategy (informs capital allocation), Execution Monitoring (tracks actuals vs. model), Board/investors (primary audience for financials)

**Timing:** 1-2 days

**Quality Gates:**
- LTV:CAC ratio documented (typically 3:1 or better)
- Profitability timeline explicit (when do we achieve positive EBITDA?)
- Key assumptions called out (growth rate, churn, pricing, unit costs)
- Sensitivity analysis shows which assumptions drive outcomes most
- Confidence tagged on all projections (Base case more certain than Upside/Downside)

---

## 1.8 Capital & Resource Strategy

**Purpose:** Capital allocation. Decides how to deploy capital across strategy initiatives.

**Classification:** Layer 1 (Corporate & Portfolio)

**Hard Dependencies:** Financial Strategy (required for capital requirements), Rumelt Forge (required for strategic prioritization)

**Inputs Required:**
- Strategic priorities (from Rumelt Forge and playbook sequencing)
- Capital requirements by initiative (from Financial Strategy and functional skills)
- Available capital (from balance sheet or financing capacity)
- Cost of capital (discount rate for ROI calculations)
- Time horizon for payback

**Outputs Produced:**
- Capital allocation plan ($ by initiative, by timing)
- ROI analysis (return on capital deployed)
- Prioritization of initiatives (which get funded first?)
- Financing strategy (internal cash, debt, equity, partnerships)
- Contingency capital (reserve for surprises)
- Resource prioritization (which teams get expanded, which contract?)

**Consumed By:** Execution Monitoring (tracks capital deployment vs. plan), Operating Model (informs headcount planning), People & Talent (informs hiring plan)

**Timing:** 0.5-1 day (typically done after strategy is locked)

**Quality Gates:**
- All strategic initiatives have capital attached (nothing left unfunded)
- ROI analysis defensible (not overly optimistic)
- Financing plan realistic (can we actually raise this capital?)
- Contingency reserve included (typically 10-20% of total capital)

---

## 1.9 Product Innovation Strategy

**Purpose:** Product roadmap. Defines feature priorities, product positioning, and PMF validation.

**Classification:** Layer 4 (Functional Strategies)

**Hard Dependencies:** Strategy Partner (required for competitive context), Market Intelligence (required for customer insights)

**Inputs Required:**
- Competitive product analysis (from Market Intelligence)
- Customer needs and preferences (from primary research)
- Product-market fit thesis (which features drive retention/expansion?)
- Technical capability (what can we build?)
- Strategic direction (from Rumelt Forge, if available)

**Outputs Produced:**
- Product-market fit assessment (do we have PMF? Confidence level H/M/L)
- Feature priority ranking (which features drive most value?)
- Product roadmap (12-month, phased by priority)
- Positioning statement (what problem does product solve?)
- Customer success metrics (retention, NPS, expansion)
- Technical debt assessment (what's holding us back?)
- Go/no-go decision on current positioning (do we pivot or double down?)

**Consumed By:** GTM Strategy (designs go-to-market around feature priorities), Technology Strategy (informs tech roadmap), Execution Monitoring (tracks PMF signals)

**Timing:** 1-2 days

**Quality Gates:**
- PMF scoring explicit (not vague; use quantified retention/NPS metrics)
- Feature priority justified by customer data (not executive preference)
- Product roadmap realistic (can be executed with available team)
- Customer success metrics trackable (not aspirational)

---

## 1.10 Technology & Digital Strategy

**Purpose:** Technology roadmap. Defines tech capabilities needed to execute strategy, platform evolution, data/AI strategy.

**Classification:** Layer 4 (Functional Strategies)

**Hard Dependencies:** Rumelt Forge (required for strategic context), Product Innovation (required for product tech stack)

**Inputs Required:**
- Strategy kernel (what capabilities does strategy require?)
- Product roadmap (what tech must product team build?)
- Current tech stack (what's our baseline?)
- Cloud/infrastructure constraints (cost, compliance, geography)
- Data and AI opportunities (what data do we have? What ML can we do?)
- Technical risk assessment (what's our single point of failure?)

**Outputs Produced:**
- Technology roadmap (24-36 months, prioritized by strategic importance)
- Build/buy/partner decisions (for each major capability)
- Platform modernization plan (legacy system retirement, cloud migration, etc.)
- Data and AI strategy (what data can we leverage? Where is ML valuable?)
- Infrastructure and security roadmap
- Technical debt paydown plan
- Talent/hiring plan for tech team

**Consumed By:** Operating Model (informs tech org design), People & Talent (informs tech hiring), Capital & Resource Strategy (informs tech investment), Execution Monitoring (tracks tech roadmap progress)

**Timing:** 1-2 days

**Quality Gates:**
- Tech roadmap aligned with business strategy (not tech for tech's sake)
- Build/buy decisions have explicit trade-offs (cost, time, control)
- Data strategy defensible (data actually available and valuable)
- Talent plan realistic (can hire needed skills?)

---

## 1.11 Operating Model

**Purpose:** Organization design. Defines structure, governance, processes, accountability.

**Classification:** Layer 3 (Execution Design)

**Hard Dependencies:** Rumelt Forge (required for execution requirements), People & Talent (paired dependency - must align on structure)

**Inputs Required:**
- Coherent Actions (from Rumelt Forge)
- Execution requirements per action (timelines, resource needs, capabilities)
- Current org structure and capability gaps
- Governance philosophy (centralized vs. distributed?)
- Span of control and management philosophy
- Decision-making authority (who decides what?)

**Outputs Produced:**
- Org structure (boxes and lines, reporting relationships)
- Role definitions (what does each role own?)
- Governance model (decision-making authority, approval levels)
- Process maps (how decisions get made, how work gets done)
- Accountability framework (who's responsible for what KPI?)
- Org redesign timeline (what changes when?)
- Headcount model (how many people per function?)

**Consumed By:** People & Talent (hires and develops talent for structure), Change Management (designs change program for org transition), Execution Monitoring (tracks org effectiveness, governance issues)

**Timing:** 1-2 days

**Quality Gates:**
- Structure EXPLICITLY supports Coherent Actions from Rumelt (not generic structure)
- Roles and responsibilities clear (not overlapping, not gaps)
- Decision authorities explicit (avoid ambiguity)
- Span of control reasonable (not excessive breadth or depth)
- Headcount plan realistic and resourced

---

## 1.12 People & Talent Strategy

**Purpose:** Talent model and org capability. Designs hiring, development, culture.

**Classification:** Layer 3 (Execution Design)

**Hard Dependencies:** Operating Model (required for structure that talent must fill)

**Inputs Required:**
- Org structure (from Operating Model)
- Role requirements per position (from Operating Model)
- Current talent capability gaps
- Hiring timeline and budget
- Compensation philosophy and benchmarks
- Cultural values and behaviors
- Development and retention strategy

**Outputs Produced:**
- Talent model (headcount by function and level)
- Hiring plan (timeline, role descriptions, sourcing strategy)
- Compensation and benefits structure
- Development and training plan
- Retention and incentive strategy
- Cultural values and behaviors aligned with strategy
- Talent assessment (retention risk, key person risks)

**Consumed By:** Operating Model (validation of structure feasibility), Change Management (informs change communications and training), Execution Monitoring (tracks hiring vs. plan, retention metrics)

**Timing:** 0.5-1 day

**Quality Gates:**
- Hiring plan realistic (can we actually hire this fast/at this cost?)
- Compensation competitive (benchmarked against market)
- Retention strategy specific (not generic)
- Cultural alignment explicit (values tied to strategy)

---

## 1.13 Change Management

**Purpose:** Transformation execution. Designs change readiness, adoption, communication, resistance management.

**Classification:** Layer 5 (Implementation & Change)

**Hard Dependencies:** Rumelt Forge (required for change scope), Operating Model (required for org changes), People & Talent (required for talent implications)

**Inputs Required:**
- Strategy kernel (what's changing and why?)
- Org redesign (from Operating Model)
- Talent changes (from People & Talent)
- Timeline for transformation (how fast?)
- Stakeholder map (who's affected?)
- Change readiness assessment (how ready is organization?)
- Historical change experience (what worked/failed before?)

**Outputs Produced:**
- Change readiness assessment (how ready is organization? H/M/L score)
- Stakeholder alignment map (who supports/opposes/neutral?)
- Communication plan (what, when, how we communicate change)
- Training and enablement plan (what skills must people develop?)
- Adoption forecast (how fast will people adopt new ways?)
- Resistance management strategy (how do we address objections?)
- Change metrics and monitoring (how do we know change is working?)
- Post-implementation review process (how do we learn and adjust?)

**Consumed By:** Execution Monitoring (tracks adoption and change effectiveness)

**Timing:** 1-2 days

**Quality Gates:**
- Change readiness assessment evidence-based (not assumption-based)
- Stakeholder analysis complete (all major groups identified)
- Communication plan specific (not vague; who says what, when, how)
- Training plan realistic (people have time to learn?)
- Adoption forecast reasonable (not too optimistic or pessimistic)

---

## 1.14 Execution Monitoring

**Purpose:** KPI tracking and course correction. Monitors assumption validation, tracks execution drift, triggers course correction.

**Classification:** Layer 5 (Implementation & Change)

**Hard Dependencies:** All other skills (consumes their outputs to set up tracking)

**Inputs Required:**
- Strategy kernel and Coherent Actions (from Rumelt Forge)
- Key assumptions from all skills (assumption register)
- Financial targets and KPIs (from Financial Strategy)
- Product targets (from Product Innovation)
- Org structure and accountability (from Operating Model)
- Change adoption targets (from Change Management)

**Outputs Produced:**
- KPI dashboard (what are we tracking? Target vs. actual?)
- Assumption validation status (validated/invalidated/uncertain?)
- Execution drift alerts (are we on track? Or drifting?)
- Course correction recommendations (if drifting, what changes?)
- Post-mortem analysis (after engagements, what did we learn?)
- Traffic light reports (green/yellow/red status by KPI)
- Confidence updates (based on early assumption validation)

**Consumed By:** All skills (feedback loop to adjust strategy/plans if needed)

**Timing:** Continuous (daily/weekly tracking, monthly reporting)

**Quality Gates:**
- KPIs directly tied to strategy (not vanity metrics)
- Targets realistic (achievable, but stretch)
- Assumption register complete (all critical assumptions tracked)
- Course correction process clear (who decides, when, how?)

---

## 1.15 AI-Native Strategy

**Purpose:** Real-time agentic intelligence and acceleration. Identifies AI opportunities/threats, runs scenario simulations, detects contradictions.

**Classification:** Cross-layer

**Hard Dependencies:** None (can start immediately, but most valuable when other skills are running)

**Inputs Required:**
- Strategy context and assumptions (from other skills)
- Market and competitive data (from Market Intelligence)
- Real-time signals and changes (news, product launches, funding)
- Scenario assumptions (from Scenario Framework)
- Contradiction detection scope (which skill outputs to scan?)

**Outputs Produced:**
- AI/ML opportunities and threats assessment
- Real-time market intelligence (what's changed since last check?)
- Scenario simulation results (what if X changes? What's outcome?)
- Contradiction detection (which skill outputs conflict?)
- Assumption drift alerts (are our assumptions still valid?)
- Agentic recommendations for speed compression (which analyses can we parallelize?)

**Consumed By:** All skills (provides continuous intelligence and contradiction alerts)

**Timing:** Continuous (can run in parallel with other skills)

**Quality Gates:**
- AI opportunities grounded in strategy (not cool AI for its own sake)
- Market signals current (last 24-48 hours)
- Scenario simulations realistic (not science fiction)
- Contradiction flagging helpful (not just noise)

---

## 1.16 M&A & Corporate Development

**Purpose:** Portfolio strategy and M&A evaluation. Assesses acquisition targets, partnership opportunities, portfolio fit.

**Classification:** Layer 1 (Corporate & Portfolio)

**Hard Dependencies:** Strategy Partner (required for strategic context), Rumelt Forge (required if M&A is part of strategy)

**Inputs Required:**
- Strategic direction (from Rumelt Forge or Strategy Partner)
- Strategic priorities (what are we trying to accomplish?)
- Target company/partnership analysis (candidates, sizes, capabilities)
- Financial targets for acquisition (price, EPS accretion, ROI)
- Market dynamics (consolidation, competition, threat)
- Integration capability (can we actually integrate?)

**Outputs Produced:**
- M&A opportunity assessment (strategic fit, valuation, risk)
- Target company analysis (positioning, capabilities, customer base, synergies)
- Valuation analysis (price recommendation, deal structure)
- Synergy analysis (what value can we create from acquisition?)
- Integration plan (how do we combine companies?)
- Partnership opportunity assessment (if relevant)
- Go/no-go recommendation (acquire, pass, make offer)

**Consumed By:** Capital & Resource Strategy (informs capital allocation), Financial Strategy (informs financial targets and returns), Operating Model (informs integration planning)

**Timing:** 2-5 days (depends on complexity of target evaluation)

**Quality Gates:**
- Strategic fit explicit (how does this serve strategy?)
- Valuation defensible (peer benchmarks, DCF, precedent transactions)
- Synergy analysis realistic (not overly optimistic)
- Integration risks identified (cultural, systems, customer)
- Deal structure addresses key risks (earn-outs, reps & warranties)

---

## 1.17 ATLAS Report Template

**Purpose:** Final deliverable. Synthesizes all skill outputs into premium strategy document.

**Classification:** Output Pipeline

**Hard Dependencies:** All skills (consumes their structured outputs)

**Inputs Required:**
- Structured outputs from all participating skills (JSON blocks with key findings, recommendations, confidence, risks, kill conditions)
- Narrative summaries from each skill
- Executive context and decision needs
- Design preferences (color, tone, length)

**Outputs Produced:**
- Premium strategy report (HTML, 8 sections, ~25-40 pages)
- Executive summary (1 page)
- Strategic diagnosis (with key findings)
- The Crux and strategy kernel (with visual)
- Implementation plans (org, GTM, financial, tech, talent)
- Risk assessment and contingencies
- Appendices (assumptions, detailed analyses, supporting data)
- Interactive elements (clickable navigation, collapsible sections)

**Consumed By:** Client leadership, board, executive team (primary audience)

**Timing:** 1-2 days (after all skills complete their work)

**Quality Gates:**
- All skill outputs represented in report (no missing skill data)
- Narrative coherence across 8 sections (smooth story flow)
- Executive readability (can C-suite understand without deep dives?)
- Data accuracy (all numbers from source skill outputs)
- Visual design meets premium standard (McKinsey/Google quality)
- Decision clarity (reader knows what to do)

---

## Skill Classification Layers

Skills are organized into layers based on their role in the engagement:

- **Layer 1 (Corporate & Portfolio):** Strategy Partner, Growth Strategy, Capital & Resource Strategy, M&A & Corp Dev
- **Layer 2 (Competitive & Business Model):** Rumelt Strategy Forge
- **Layer 3 (Execution Design):** GTM Strategy, Financial Strategy, Operating Model, People & Talent
- **Layer 4 (Functional Strategies):** Product Innovation, Technology & Digital Strategy
- **Layer 5 (Implementation & Change):** Change Management, Execution Monitoring
- **Layer 6 (Learning & Adaptation):** Hypothesis Testing
- **Cross-Layer:** Market Intelligence, AI-Native Strategy
- **Output Pipeline:** ATLAS Report Template
