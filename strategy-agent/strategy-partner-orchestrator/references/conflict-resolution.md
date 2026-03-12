# StrategyOS Conflict Resolution & Devil's Advocate Framework

**Purpose:** Detect conflicts between skill positions, synthesize them using the Devil's Advocate protocol, and escalate unresolvable conflicts to the user with decision frameworks.

**Version:** 1.0 | **Status:** ACTIVE | **Updated:** 2026-03-10

---

## 1. Conflict Detection Algorithm

### When Conflicts Are Detected

Conflicts are identified in TWO ways:

**Method 1: Explicit Flagging (from DATA-CONTRACT.md)**
- Each skill's structured output includes `conflicts_detected` array
- Skill explicitly flags: "I conflict with Skill X on this position"

**Method 2: Auto-Detection**
- System compares outputs from skills that should align and identifies mismatches:
  - **Contradicting recommendations:** Skill A says "do X" but Skill B says "don't do X"
  - **Conflicting assumptions:** Skill A assumes CAC=$15K but Skill B validates CAC=$18K
  - **Incompatible data:** Skill A cites market data suggesting feature X wins; Skill B cites data suggesting feature Y wins
  - **Timeline conflicts:** Skill A needs 6 months but Skill B says we have 4 months
  - **Resource conflicts:** Skill A budgets $2M but Skill B says budget is $1.5M

### Conflict Classification

Every detected conflict is classified as one of these types:

| Type | Definition | Examples | Resolution Authority |
|---|---|---|---|
| **STRATEGIC** | Affects overall direction or crux | "Consolidate or diversify?" "Acquire or grow organic?" "Enter adjacent market or stay focused?" | Rumelt Forge + User |
| **OPERATIONAL** | Affects execution approach but not direction | "Do we hire 5 people or 10?" "Do we launch in Q2 or Q3?" "Do we use partnership or build?" | Functional skill owner + User |
| **DATA** | Factual disagreement about metrics/market | "Market growth is 20% or 15%?" "Our CAC is $15K or $18K?" "Retention is 80% or 75%?" | Data with stronger source wins automatically |
| **TIMING** | Sequence disagreement | "Do Growth strategy BEFORE Financial or AFTER?" | Determined by dependency rules in INTEGRATION.md |

### Auto-Detection Algorithm

```
For each pair of skills (A, B) that both provided output:

  STEP 1: Compare Recommendations
    For each recommendation in A:
      Does B recommend the opposite?
        YES → Flag as STRATEGIC or OPERATIONAL conflict

  STEP 2: Compare Assumptions
    For each assumption in A:
      Does B's data contradict this assumption?
        YES → Flag as DATA conflict

  STEP 3: Compare Data Points
    For each metric in A:
      Does B cite a different value for same metric?
        YES → Compare confidence levels
        If A and B confidence are equal → Flag as DATA conflict
        If one has higher confidence → Auto-resolve (higher confidence wins)

  STEP 4: Compare Timelines
    Do A's requirements conflict with B's timeline?
      YES → Flag as TIMING conflict

  STEP 5: Compare Resource Allocations
    Does A's budget conflict with B's budget?
      YES → Flag as OPERATIONAL conflict

Output: List of conflicts, classified by type, with confidence levels for each position
```

---

## 2. Devil's Advocate Synthesis Protocol

When a conflict is detected, generate a synthesis using this exact structure. This protocol attempts to find a position that satisfies BOTH sides' core concerns.

### The Synthesis Template

```
═══════════════════════════════════════════════════════════════════════
CONFLICT SYNTHESIS
═══════════════════════════════════════════════════════════════════════

Conflict ID: [AUTO-GENERATED: conf-YYMMDD-001, conf-YYMMDD-002, etc.]
Engagement ID: [engagement_id]
Date Detected: [ISO 8601]
Type: [STRATEGIC | OPERATIONAL | DATA | TIMING]
Severity: [BLOCKING | HIGH | MEDIUM | LOW]

───────────────────────────────────────────────────────────────────────
POSITIONS
───────────────────────────────────────────────────────────────────────

Position A ([Skill Name]):
  Claim: [What they recommend/concluded]
  Evidence: [Their supporting data + sources]
  Confidence: [H/M/L]
  Key Logic: [Their core reasoning]

Position B ([Skill Name]):
  Claim: [What they recommend/concluded]
  Evidence: [Their supporting data + sources]
  Confidence: [H/M/L]
  Key Logic: [Their core reasoning]

───────────────────────────────────────────────────────────────────────
DEVIL'S ADVOCATE ANALYSIS
───────────────────────────────────────────────────────────────────────

Why Position A Might Be Right:
  [Steel-man argument: Make the strongest possible case for A, even if you
   initially disagreed. What is A seeing that B is missing?]

Why Position A Might Be Wrong:
  [Best counter-argument to A. What's the flaw in A's logic?]

Why Position B Might Be Right:
  [Steel-man argument for B]

Why Position B Might Be Wrong:
  [Best counter-argument to B]

───────────────────────────────────────────────────────────────────────
SYNTHESIS POSITION
───────────────────────────────────────────────────────────────────────

Recommended Resolution:
  [Attempt to resolve the tension. This should NOT be "split the difference"
   but rather "here's a third position that satisfies both sides' core needs"]

Rationale:
  [Why this synthesis is superior to either position alone. How does it
   address A's core concern AND B's core concern?]

Residual Risk:
  [What risk remains even with synthesis?]

Confidence in Synthesis: [H/M/L]

───────────────────────────────────────────────────────────────────────
IF SYNTHESIS FAILS (Cannot reach agreement)
───────────────────────────────────────────────────────────────────────

Escalation: PRESENT BOTH POSITIONS TO USER

Evidence for Position A:
  [Summary of A's strongest evidence]

Evidence for Position B:
  [Summary of B's strongest evidence]

Critical Question for User:
  [Specific question the user MUST answer to decide between A and B]

Decision Framework:
  IF [user chooses A] → [What happens next]
  IF [user chooses B] → [What happens next]

Impact of Delaying Decision:
  [What can we not do if we don't decide now?]

═══════════════════════════════════════════════════════════════════════
```

### Synthesis Example 1: Growth Rate Conflict

```
═══════════════════════════════════════════════════════════════════════
CONFLICT SYNTHESIS: Growth Rate & Unit Economics
═══════════════════════════════════════════════════════════════════════

Conflict ID: conf-20260310-001
Type: OPERATIONAL
Severity: HIGH

───────────────────────────────────────────────────────────────────────
POSITIONS
───────────────────────────────────────────────────────────────────────

Position A (Growth Strategy):
  Claim: We should pursue 40% YoY growth; it's required to reach $200M ARR
           within 5 years
  Evidence: Market analysis shows 45% CAGr opportunity; competitors are
            growing at 35-40%; our retention is 80%, expansion is 20%
  Confidence: H (based on market size validation + competitive benchmarking)
  Key Logic: Market opportunity is huge; if we don't grow fast, competitors
             will take share; 40% is necessary to capture TAM

Position B (Financial Strategy):
  Claim: 40% growth will break unit economics; we can only sustainably
          support 30% growth at current CAC and LTV
  Evidence: Historical data shows CAC increases 8% per cohort (scaling friction).
            At 40% growth, payback extends to 14.2 months (vs. 10.3 now).
            Comparable companies (Zendesk, HubSpot, Drift) show CAC increases
            accelerate above 35% growth.
  Confidence: H (based on 4-year cohort analysis + external benchmarking)
  Key Logic: Unit economics will degrade as we scale; 40% growth is feasible
             SHORT-TERM but unsustainable without improving LTV first

───────────────────────────────────────────────────────────────────────
DEVIL'S ADVOCATE ANALYSIS
───────────────────────────────────────────────────────────────────────

Why Growth Might Be Right:
  Growth is correct that the market opportunity is massive. If we grow at
  30%, a competitor growing at 40% will capture more TAM and eventually
  outposition us. Financial is assuming static unit economics, but aggressive
  growth can unlock operational leverage (marketing efficiency, higher ACV
  deals, product-led expansion). Growth's concern about competitive positioning
  is VALID and material to long-term strategy.

Why Growth Might Be Wrong:
  Growth is assuming we can maintain CAC trajectory while others are
  accelerating spend against same customer pool. As competition increases,
  CAC WILL increase (Financial's historical data supports this). Growth is
  also underestimating the risk of cash burn: at 40% growth with declining
  unit economics, we could exhaust capital before profitability.

Why Financial Might Be Right:
  Financial's unit economics analysis is rigorous and validated by comparable
  companies. The data showing CAC increases with scale is real. Payback
  periods >12 months are concerning and historically correlate with increased
  churn and reduced retention. Financial is being prudent about capital.

Why Financial Might Be Wrong:
  Financial is treating unit economics as static and ignoring that aggressive
  growth can IMPROVE unit economics through product-led motion, higher ACV,
  and viral expansion. Growth strategy can change the CAC/LTV equation
  (e.g., if we enter upmarket, ACV increases 3x, which improves LTV without
  changing payback). Financial may be anchored to historical unit economics
  and not accounting for strategic transformation.

───────────────────────────────────────────────────────────────────────
SYNTHESIS POSITION
───────────────────────────────────────────────────────────────────────

Recommended Resolution:
  TARGET 35% YoY growth WITH PARALLEL LTV IMPROVEMENT initiative

  Specifically:
  1. Pursue 35% growth rate (sweet spot: above 30% to stay competitive,
     below 40% where unit economics break)
  2. Invest parallel initiative to improve LTV by 15% within 12 months
     through: (a) product-led expansion features, (b) upmarket repositioning,
     (c) customer success model improvements
  3. If LTV improves as projected (to $207K), unit economics support 40%
     growth in Year 2
  4. If LTV doesn't improve, growth rate caps at 35% and we re-examine
     strategy

Rationale:
  This position satisfies Growth's concern (competitive positioning + TAM
  capture via 35% growth) AND Financial's concern (unit economics remain
  healthy). By decoupling growth rate from LTV improvement, we create a
  two-lever strategy that's more resilient than either position alone.

  Growth's core fear (losing competitive position) is addressed by 35%
  growth rate, which is still above market average.

  Financial's core fear (cash burn + unit economics degradation) is addressed
  by: (a) conservative growth target initially, (b) explicit LTV improvement
  initiative with measurable milestones, (c) fallback to 30% if LTV
  improvement fails.

Residual Risk:
  - If LTV improvement initiative fails (e.g., upmarket repositioning doesn't
    land), we're stuck at 35% growth vs. 40%, potentially losing competitive
    positioning anyway
  - Parallel LTV initiative requires product and customer success resources,
    which could slow other initiatives
  - 35% growth is still 17% above what Financial thinks is "safe"

Confidence in Synthesis: H (80%)
  Reasoning: We have a clear path (LTV improvement) to validate which side
  is ultimately right. We're not betting the company on either position.

───────────────────────────────────────────────────────────────────────
IF SYNTHESIS ACCEPTED: Next Steps
───────────────────────────────────────────────────────────────────────
- Growth targets 35% YoY growth for Year 2
- Financial models three scenarios: (a) LTV improves 15% → growth can
  accelerate to 40% in Year 2, (b) LTV improves 7% → growth caps at 35%,
  (c) LTV flat → growth caps at 30%
- People & Talent plan headcount for 35% growth initially, with capacity
  to scale to 40% if LTV improves
- Monthly monitoring: Track LTV trajectory weekly, growth rate daily;
  if either deviates >10% from plan, escalate immediately

═══════════════════════════════════════════════════════════════════════
```

### Synthesis Example 2: Feature Priority Conflict (No Synthesis Possible)

```
═══════════════════════════════════════════════════════════════════════
CONFLICT SYNTHESIS: Feature Priority (Enterprise vs. Mid-Market)
═══════════════════════════════════════════════════════════════════════

Conflict ID: conf-20260310-002
Type: OPERATIONAL
Severity: MEDIUM

───────────────────────────────────────────────────────────────────────
POSITIONS
───────────────────────────────────────────────────────────────────────

Position A (GTM Strategy):
  Claim: Enterprise segment needs Compliance feature (SOC 2, HIPAA, etc.)
          to win large deals. This is the primary deal-blocker in enterprise
  Evidence: Win/loss analysis of 12 Enterprise deals: 8 lost due to missing
            compliance features. Competitor A has compliance, we don't.
  Confidence: H (based on direct customer feedback from lost deals)
  Key Logic: Enterprise buyers have compliance mandates; without this,
             we can't compete for their business

Position B (Product Innovation):
  Claim: Mid-Market segment needs Analytics feature (data visibility,
          reporting) to drive expansion and retention. This drives more
          lifetime value than Compliance
  Evidence: Retention cohort analysis: customers using analytics feature
            have 92% year-1 retention vs. 78% for others. Expansion:
            analytics users expand 28% vs. 18% for others.
  Confidence: H (based on 24-month cohort data, n=1,200 customers)
  Key Logic: Analytics drives more revenue per customer than Compliance
             (which is table-stakes, not a growth driver)

───────────────────────────────────────────────────────────────────────
DEVIL'S ADVOCATE ANALYSIS
───────────────────────────────────────────────────────────────────────

Why GTM Might Be Right:
  GTM is right that Compliance is a deal-blocker for Enterprise. You can't
  win an Enterprise deal without it. This is a hard constraint, not a nice-to-have.
  Without Enterprise deals, we won't hit $100M ARR targets.

Why GTM Might Be Wrong:
  GTM is assuming we MUST win Enterprise. But our current revenue (60%
  Mid-Market) shows we've built a viable business in Mid-Market. Forcing
  Compliance for Enterprise might cannibalize resources from Analytics, which
  is proven to drive expansion in our core Mid-Market segment.

Why Product Might Be Right:
  Product is right that Analytics drives MORE lifetime value. A $10K MRR
  enterprise customer with no expansion is worth less long-term than a
  $50K MRR mid-market customer that expands 28% annually.

Why Product Might Be Wrong:
  Product is treating feature ROI in isolation, without considering that
  Compliance is a gating factor for entire Enterprise segment. Product's
  analytics data is strong, but it's from Mid-Market customers, not Enterprise.
  The marginal return of analytics to Enterprise customers might be different.

───────────────────────────────────────────────────────────────────────
SYNTHESIS POSITION
───────────────────────────────────────────────────────────────────────

Recommended Resolution:
  CANNOT SYNTHESIZE — These positions are not naturally compatible.

  This is a strategic choice about which segment to win in, not a tactical
  execution question. We have capacity for ONE major feature in next quarter.
  We must choose: Dominate Enterprise (via Compliance) or Maximize Mid-Market
  penetration (via Analytics).

Resolution Approach:
  Escalate to user with decision framework (see below).

Residual Risk:
  - If we choose Compliance: Mid-Market analytics demand goes unmet,
    possibly driving churn
  - If we choose Analytics: Enterprise segment remains uncompetitive,
    limiting revenue scale

───────────────────────────────────────────────────────────────────────
ESCALATION TO USER
───────────────────────────────────────────────────────────────────────

Critical Question:
  Which segment do we prioritize: Enterprise (Compliance to win deals)
  or Mid-Market (Analytics to retain + expand)?

Decision Framework:

  IF User chooses ENTERPRISE:
    → GTM wins: We build Compliance feature
    → Financial must adjust: Enterprise deals have longer sales cycles
      (expect 6-month sales cycle, not 3), which affects cash flow timing
    → People: We hire sales engineers specialized in Enterprise compliance
    → Product: Analytics goes to Roadmap Q2, Compliance is Q1 (3-month delay
      for Analytics)
    → Risk: Mid-Market churn may increase if analytics demand unmet
    → Upside: Enterprise deals are 5-10x larger, drive valuation multiple

  IF User chooses MID-MARKET:
    → Product wins: We build Analytics feature
    → GTM must adjust: We explicitly position against Enterprise segment,
      focus sales on Mid-Market only
    → Financial: Revenue CAGR may be lower (mid-market deal size smaller)
      but LTV higher due to expansion
    → Compliance: Go to Roadmap Q2 (3-month delay)
    → Risk: We abandon Enterprise opportunity; competitors with Compliance
      may dominate Enterprise
    → Upside: Predictable Mid-Market revenue, high retention + expansion,
      potentially profitable faster

Impact of Delay:
  If we don't decide TODAY, both features get delayed (scheduling conflict).
  This delays either Enterprise sales or Mid-Market retention, both of which
  affect revenue in 6 weeks.

═══════════════════════════════════════════════════════════════════════
```

---

## 3. Conflict Resolution Hierarchy

When a conflict is detected, follow this hierarchy to attempt resolution BEFORE escalating to user:

### Level 1: Auto-Resolve via Data (No Human Involvement)

**Trigger:** Conflict is DATA type and one side has significantly stronger evidence

**Rule:**
```
IF Skill A claims metric = X and Skill B claims metric = Y:
  IF confidence(A) >= 90% AND confidence(B) <= 60%:
    Position A wins automatically
    Document: "A's data stronger; B should revise assumption"
  IF confidence(A) >= 80% AND confidence(B) <= 70%:
    Position A wins automatically
    Document: "A's evidence more rigorous; B should accept A's data"
  IF confidence(A) and confidence(B) both >=75%:
    Escalate to Level 2 (cannot auto-resolve)
```

**Examples:**
- A's CAC data (from internal analytics, n=500) vs. B's CAC data (from industry report): A's data wins
- A's market size estimate (from multiple sources) vs. B's estimate (from one source): A's data wins

---

### Level 2: Devil's Advocate Synthesis

**Trigger:** Conflict not resolvable via data; requires strategic/operational judgment

**Process:**
1. Generate synthesis using the template above
2. Check if synthesis satisfies BOTH positions' core concerns
3. If YES: Synthesis becomes recommended resolution; document and proceed
4. If NO: Escalate to Level 3

**Success Rate Target:** Synthesis should resolve 60-70% of conflicts

---

### Level 3: Hierarchy Resolution (Tiebreaker Rules)

**Trigger:** Synthesis not possible; must apply strategic hierarchy

**Hierarchy (highest authority wins):**

| Rank | Authority | Rationale |
|---|---|---|
| 1 | **Strategic Rationale** | Strategy kernels and crux decisions override everything else |
| 2 | **Market Reality** | Market data trumps internal assumptions |
| 3 | **Operational Feasibility** | What we can actually execute beats what we theoretically could |
| 4 | **Functional Best Practice** | Within a functional area, best practice wins |
| 5 | **Cost** | When all else is equal, lower cost wins |

**Application Examples:**

| Conflict | Hierarchy Application | Winner |
|---|---|---|
| Strategy says "grow" vs. Finance says "not fundable" | Strategic Rationale > Financial | Strategy wins; Finance must find funding or Strategy must revise |
| GTM says "CAC=$15K" vs. Market data says "CAC should be $18K" | Market Reality > Operational | Market data wins; GTM must accept $18K CAC |
| Product says "feature A" vs. GTM says "feature B" | PMF data (Product's domain) > Deal-win data | Product wins if PMF confidence >=70% |
| Operating Model says "hire" vs. Finance says "can't afford" | Operational Feasibility | Finance wins if budget truly constrains; can hire differently (contractors, contractors, etc.) |

---

### Level 4: User Escalation

**Trigger:** Levels 1-3 cannot resolve; human judgment required

**Escalation Package to User:**
- Conflict ID and summary
- Position A (evidence + confidence)
- Position B (evidence + confidence)
- Devil's Advocate analysis (why each might be right/wrong)
- Synthesis attempt (if any)
- Critical question for user decision
- Decision framework (IF user chooses A → ... / IF user chooses B → ...)
- Impact of delay (what can't we do if undecided)

**User Decision SLA:** 24 hours for HIGH/BLOCKING conflicts; 1 week for MEDIUM

---

## 4. Pre-Defined Conflict Patterns & Default Resolutions

These are the 10 most common conflicts in multi-skill strategy engagements. Each has a default synthesis approach and escalation triggers.

### Conflict Pattern 1: Growth Says "Acquire" / Financial Says "Can't Afford"

**Positions:**
- Growth: "We should acquire Company X to accelerate growth 2 years"
- Financial: "Acquisition costs $50M; we can only raise $30M without dilution"

**Default Synthesis:**
- Explore asset purchase instead of full acquisition (lower cost, same strategic outcome)
- Phase acquisition: acquire core product now ($30M), acquire team later
- Explore strategic partnership instead of full acquisition

**Escalation Trigger:**
- If no viable phased approach exists, escalate with question: "Do we raise additional capital (dilution) or grow organically?"

---

### Conflict Pattern 2: GTM Says "Feature X Wins Deals" / Product Says "Feature Y Drives Retention"

**Positions:**
- GTM: "Enterprise customers won't buy without Feature X (compliance, integration, etc.)"
- Product: "Feature Y is what drives retention; we built it because Y has 92% retention signal"

**Default Synthesis:**
- If both features needed: sequence them (X first if TAM is Enterprise-heavy; Y first if TAM is Mid-Market-heavy)
- If only one fits in roadmap: compare LTV generated by each feature (see example in section 2)

**Escalation Trigger:**
- If feature choice determines market segment (see Conflict Pattern 2 example above), escalate to user for segment choice

---

### Conflict Pattern 3: Financial Says "Cut Costs" / People Says "Need to Hire"

**Positions:**
- Financial: "Operating margin is negative; we must reduce headcount 20% to reach profitability"
- People: "Key functional areas (engineering, sales) are understaffed; cutting will cause churn"

**Default Synthesis:**
- Identify which departments are overstaffed vs. understaffed (not uniform 20% cut)
- Shift resources from low-impact (e.g., corporate, finance admin) to high-impact (engineering, sales)
- Reduce external spend (agencies, contractors) instead of full-time headcount
- Reduce overhead (office, travel, etc.) instead of headcount

**Escalation Trigger:**
- If achieving profitability requires >15% headcount cut, escalate: "Do we accept slower growth to reach profitability, or do we raise capital to fund growth?"

---

### Conflict Pattern 4: Technology Says "Rebuild Platform" / Financial Says "ROI Too Long"

**Positions:**
- Technology: "Current platform is legacy; we need to rebuild to support scale and new products"
- Financial: "Rebuild costs $5M and takes 18 months; ROI is not clear"

**Default Synthesis:**
- Phased modernization instead of full rebuild (Phase 1: highest-value components, Phase 2: rest)
- Cost-share approach: use rebuild as learning/leverage for new product development (dual benefit)
- Capability-based rebuilding: only rebuild if new capability directly enables new revenue (not just technical purity)

**Escalation Trigger:**
- If rebuild is critical to strategy kernel but ROI is unclear, escalate: "Is this rebuild blocking growth, or is it technical debt?"

---

### Conflict Pattern 5: Growth Says "Enter Adjacent Market" / Rumelt Says "Concentrate on Core"

**Positions:**
- Growth: "TAM is $50B; our core market is $5B. We should expand to adjacent markets to reach $200M ARR faster"
- Rumelt: "Strategy kernel focuses on dominating core market. Expanding now dilutes focus and prevents breakthrough"

**Default Synthesis:**
- Define "core market dominance": what % share/revenue = dominance? Once achieved, then expand
- Time-gate expansion: core focus for Years 1-2, adjacent expansion in Years 3+
- Test adjacent market with dedicated team (doesn't dilute core team)

**Escalation Trigger:**
- If opportunity window for adjacent market closes (e.g., competitor entering), escalate: "Do we revise strategy kernel to include adjacent market, or accept risk of losing that market?"

---

### Conflict Pattern 6: AI-Native Says "Build AI Capability" / Capital Says "ROI Uncertain"

**Positions:**
- AI-Native: "AI will be table-stakes in our industry within 18 months; we need AI capability now to stay competitive"
- Capital: "AI ROI is unproven; we should wait for market signal before investing $3M"

**Default Synthesis:**
- Phased AI investment: Phase 1 ($500K, 3 months) to validate AI ROI with prototype; Phase 2 (decision point with data)
- Partner approach: use AI SaaS platforms (OpenAI, Claude API) instead of building; lower upfront cost, faster to market
- Bet-hedging: invest in AI capability in high-ROI area first (e.g., customer support automation), learn, then expand

**Escalation Trigger:**
- If competitive threat is imminent and prototype shows negative ROI, escalate: "Do we invest despite uncertain ROI to stay competitive, or focus on other growth drivers?"

---

### Conflict Pattern 7: M&A Says "Acquire Competitor" / Rumelt Says "Organic Growth Is Crux"

**Positions:**
- M&A: "Company X is a competitor; acquiring them eliminates competitive threat and adds revenue"
- Rumelt: "Our strategy kernel is to dominate through product differentiation, not consolidation; acquisition dilutes focus"

**Default Synthesis:**
- Acquire talent/team, not company: hire Company X's product/engineering team; let company decline (lower cost, same outcome)
- Acquire selective assets: acquire their customer list or technology, not the whole company
- Partner instead: if acquisition would dilute focus, explore partnership/reseller arrangement

**Escalation Trigger:**
- If acquisition target has unique technology required for strategy kernel, escalate: "Do we revise kernel to include acquisition, or build capability ourselves?"

---

### Conflict Pattern 8: GTM Says "PLG Motion" / Financial Says "CAC Doesn't Work at Scale"

**Positions:**
- GTM: "Product-led growth (free trial → upsell) is winning motion; competitors using PLG are scaling faster"
- Financial: "Our LTV:CAC is currently 11.7:1, but PLG requires higher CAC to acquire free users; at scale, unit economics break"

**Default Synthesis:**
- Hybrid motion: free trial for SMB (PLG works), sales team for Enterprise (relationship works)
- Time-gate PLG: start with sales-led motion to build LTV; transition to PLG once LTV is strong enough
- Leverage existing base: upsell PLG to existing customers (no CAC required), acquire new via sales

**Escalation Trigger:**
- If PLG is required for competitive positioning but unit economics don't work, escalate: "Do we reduce pricing to support PLG CAC, or stay sales-led at premium pricing?"

---

### Conflict Pattern 9: People Says "Restructure Org" / Strategy Partner Says "Execution Risk Too High"

**Positions:**
- People: "Org is misaligned; we need to restructure to reduce silos and improve accountability. This restructure will improve execution"
- Strategy Partner: "Restructuring mid-engagement creates execution risk; focus should be on executing current strategy, not changing org"

**Default Synthesis:**
- Staged restructure: implement Phase 1 (critical changes) now; Phase 2 (nice-to-have changes) after 90-day plan launches
- Minimize disruption: use attrition to restructure (don't cut people, redeploy into new structure over 6 months)
- Parallel execution: do restructure AND execute strategy in parallel (with assigned change manager to reduce risk)

**Escalation Trigger:**
- If restructure requires >30% org change mid-engagement, escalate: "Do we pause execution to restructure, or stage the restructure?"

---

### Conflict Pattern 10: Product Says "Platform Play" / Technology Says "Tech Debt Blocks It"

**Positions:**
- Product: "Our product roadmap includes platform capabilities (APIs, integrations, marketplace); this is required for strategic differentiation"
- Technology: "Our current tech debt is too high to build a platform; we should fix tech debt first (6-month effort)"

**Default Synthesis:**
- Build platform incrementally: first API release can work with current tech debt; tech debt refactoring happens in parallel
- Sequencing: ship platform beta on current tech (speed to market), then refactor tech debt as platform scales
- Dedicated team: assign tech team to debt reduction while product team ships platform features

**Escalation Trigger:**
- If platform is critical to strategy kernel but tech debt is blocking, escalate: "Do we delay platform to fix debt, or ship platform with debt and refactor later?"

---

## 5. Conflict Metrics & Tracking

### Track These Metrics Across All Engagements

| Metric | Calculation | Target | Why It Matters |
|---|---|---|---|
| **Conflicts Detected per Engagement** | (Total conflicts in engagement) | 2-5 | Baseline: low # = skills are well-aligned; high # = poor engagement scoping |
| **Auto-Resolution Rate** | (Conflicts resolved via Data) / (Total conflicts) | 30-40% | Low = skills not providing strong evidence; High = good data quality |
| **Synthesis Success Rate** | (Conflicts resolved via synthesis) / (Attempted syntheses) | 50-60% | Indicates quality of Devil's Advocate reasoning |
| **Escalation Rate** | (Conflicts escalated to user) / (Total conflicts) | 10-20% | High = critical decisions needed; Low = engagement is aligned |
| **User Decision Time** | Days from escalation to user decision | <2 days for BLOCKING | If >2 days, engagement stalls |
| **Synthesis Acceptance Rate** | (User accepts synthesis) / (Syntheses proposed) | 70%+ | If <70%, synthesize approach needs refinement |
| **Conflicts by Type** | Count of STRATEGIC / OPERATIONAL / DATA / TIMING | STRATEGIC: 30%; OPERATIONAL: 50%; DATA: 15%; TIMING: 5% | STRATEGIC should be <30% (indicates good strategic clarity) |

### Reporting

Monthly conflict report shows:
- Total conflicts detected
- Resolution breakdown (auto/synthesis/hierarchy/escalation)
- Synthesis acceptance rate
- Average time to resolution
- Unresolved conflicts (if any)

---

## 6. Escalation Document Template

When a conflict cannot be resolved at Levels 1-3, use this template to escalate to the user:

```
═══════════════════════════════════════════════════════════════════════
CONFLICT ESCALATION: DECISION REQUIRED
═══════════════════════════════════════════════════════════════════════

Conflict ID: [conf-YYMMDD-XXX]
Engagement ID: [engagement_id]
Date Escalated: [ISO 8601]
Severity: [BLOCKING | HIGH | MEDIUM]

───────────────────────────────────────────────────────────────────────
THE DECISION
───────────────────────────────────────────────────────────────────────

Critical Question:
[One sentence asking the user to choose between Position A and Position B]

Example: "Do we pursue 40% growth (with unit economics risk) or 30% growth
(with competitive positioning risk)?"

───────────────────────────────────────────────────────────────────────
POSITIONS
───────────────────────────────────────────────────────────────────────

Position A ([Skill]):
  Recommendation: [What A recommends]
  Strongest Evidence: [A's best supporting data]
  Risk If Wrong: [What happens if we choose A and A is wrong]

Position B ([Skill]):
  Recommendation: [What B recommends]
  Strongest Evidence: [B's best supporting data]
  Risk If Wrong: [What happens if we choose B and B is wrong]

───────────────────────────────────────────────────────────────────────
DECISION FRAMEWORK
───────────────────────────────────────────────────────────────────────

IF User chooses Position A:
  • Strategy implications: [What this means for overall strategy]
  • Execution implications: [How does this change the 90-day plan?]
  • Financial implications: [Budget/capital implications]
  • Risk implications: [What are we betting on?]
  • Next steps: [What happens immediately after you decide A]

IF User chooses Position B:
  • [Same format as A]

───────────────────────────────────────────────────────────────────────
IMPACT OF DELAY
───────────────────────────────────────────────────────────────────────

If we don't decide by [DATE]:
  • [What gets delayed]
  • [What revenue/timeline impact]
  • [What competitive disadvantage]

RECOMMENDATION: Decide by [48 HOURS / 1 WEEK / DATE]

───────────────────────────────────────────────────────────────────────
YOUR DECISION
───────────────────────────────────────────────────────────────────────

I choose: ☐ Position A  /  ☐ Position B

Reasoning (optional): [Why you're choosing this]

═══════════════════════════════════════════════════════════════════════
```

---

## 7. Conflict Prevention: Design Patterns

These design patterns reduce conflicts BEFORE they occur:

### Pattern 1: Dependency Validation
Before a skill executes, verify its upstream dependencies are present in context:
```
GTM reads: product_state.pmf_assessment
IF product_state not yet populated:
  GTM WAITS for Product Innovation to execute first
  (don't start GTM analysis with missing input)
```

### Pattern 2: Explicit Assumption Alignment
Before Rumelt forges strategy, get agreement from all execution skills on key assumptions:
```
Rumelt proposes: "CAC = $15K, LTV = $180K, growth = 35%"
Financial confirms: "Yes, these are our input assumptions"
GTM confirms: "Yes, we can achieve these CAC/LTV targets"
Growth confirms: "Yes, 35% growth is our target"
(if any skill disagrees, resolve BEFORE Rumelt ships strategy)
```

### Pattern 3: Early Conflict Surfacing
Encourage skills to flag conflicts early, when they're small:
```
GTM finds preliminary evidence that contradicts Financial's assumptions
GTM doesn't wait until final output; flags immediately:
"Financial assumes $15K CAC, but my preliminary research suggests $18K.
Should I investigate further, or should Financial validate?"
(resolve at Devil's Advocate Level 2, not at escalation)
```

### Pattern 4: Reversibility
Design decisions with reversibility in mind to reduce escalation need:
```
Instead of: "Do we hire or contract?" (irreversible)
Ask: "Do we hire now or contract now, with option to convert later?" (reversible)
(reduces pressure for perfect decision)
```

---

## End of Conflict Resolution & Devil's Advocate Framework

This document provides the operational framework for detecting conflicts, synthesizing them, and escalating to users when necessary. Use the pre-defined conflict patterns to handle common disagreements quickly. Use the Devil's Advocate protocol to ensure both sides are genuinely heard before escalating.

**Key Principle:** Most conflicts can be resolved through good data or creative synthesis. Only escalate when a true strategic choice is required.

**Questions?** Refer to DATA-CONTRACT.md for what data each conflict should include, or CONTEXT-FLOW.md for how conflicts are stored in the master context object.
