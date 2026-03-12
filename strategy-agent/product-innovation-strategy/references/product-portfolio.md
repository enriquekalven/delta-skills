# Product Portfolio Diagnostic

This reference provides the tools to assess product health, lifecycle stage, product-market fit, and portfolio composition. A portfolio diagnostic is the prerequisite for all downstream roadmap, innovation, and business model decisions. You cannot optimize what you do not measure.

---

## Product Health Scorecard

A product health scorecard quantifies how well a product is performing across key dimensions. This is the foundation of portfolio management. A single metric (e.g., revenue) can mask catastrophic problems (e.g., declining retention despite stable revenue from churning large customers replaced by new ones). Multi-dimensional scoring reveals portfolio composition and strategic implications.

### Scorecard Dimensions

**Growth Rate (Revenue, Users, or GMV)**
- **5/5**: YoY growth >50%. Product is accelerating or maintaining hyper-growth.
- **4/5**: YoY growth 25-50%. Product is growing above market. Strong competitive position.
- **3/5**: YoY growth 10-25%. Growth is positive but at or below market. Mature/maturing product.
- **2/5**: YoY growth 0-10%. Growth is stalling. Requires intervention or harvest.
- **1/5**: YoY decline. Product is declining. Harvest or sunset.

*Calibration: Growth rate depends on product lifecycle stage and industry. A 5/5 growth rate for a mature enterprise product might be 20%. For a consumer SaaS, it might be 60%. Always compare to cohort growth and market growth.*

**Retention (30/60/90-day or annual churn)**
- **5/5**: >95% retained at 90 days (churn <5%). Exceptional product-market fit.
- **4/5**: 85-95% retained at 90 days (churn 5-15%). Strong retention, good engagement.
- **3/5**: 75-85% retained at 90 days (churn 15-25%). Acceptable retention, but signals engagement gaps.
- **2/5**: 60-75% retained at 90 days (churn 25-40%). Significant churn. Engagement or value delivery issue.
- **1/5**: <60% retained at 90 days (churn >40%). Broken product-market fit.

*Calibration: Cohort analysis matters. Are all cohorts retaining equally or is retention decaying by age? Is churn due to natural company size graduation (good, expected) or product issues (bad)?*

**Net Expansion (NRR for SaaS, or equivalent)**
- **5/5**: NRR >130%. Customers are expanding within the product.
- **4/5**: NRR 110-130%. Strong expansion signal, product is becoming more embedded.
- **3/5**: NRR 100-110%. Healthy expansion, company grows with customers.
- **2/5**: NRR 90-100%. Flat or slight contraction. Expansion motions are not working.
- **1/5**: NRR <90%. Significant contraction. Price or positioning misaligned.

*Calibration: NRR is not available for one-time purchase or freemium products. For those, use cohort cohesion (do early cohorts grow into larger customers over time?) or usage-based expansion.*

**NPS or Customer Satisfaction**
- **5/5**: NPS >60 or CSAT >90%. Customers are promoters. Word-of-mouth is strong.
- **4/5**: NPS 40-60 or CSAT 75-90%. Customers are satisfied, not passionate.
- **3/5**: NPS 20-40 or CSAT 60-75%. Customers are mixed. Satisfaction is at market parity or slightly below.
- **2/5**: NPS 0-20 or CSAT 45-60%. Customers are detractors. At risk of churn.
- **1/5**: NPS <0 or CSAT <45%. Severe satisfaction crisis.

*Calibration: NPS varies by industry and customer segment. Enterprise customers typically have lower NPS than consumer. New customers have different NPS than long-tenured. Segment and track separately.*

**Unit Economics (Margin, CAC, LTV)**
- **5/5**: Gross margin >70%, LTV/CAC >5, payback <12 months. Economically defensible.
- **4/5**: Gross margin 50-70%, LTV/CAC 3-5, payback 12-18 months. Healthy, though margin improvement opportunity.
- **3/5**: Gross margin 30-50%, LTV/CAC 2-3, payback 18-30 months. Requires scale to be profitable.
- **2/5**: Gross margin <30%, LTV/CAC <2, payback >30 months. Economically broken without major pricing/cost restructure.
- **1/5**: Negative unit economics or margin. Unsustainable.

*Calibration: Unit economics must be assessed with realistic cost allocation. Allocating corporate overhead 50/50 across products distorts picture of product-specific economics. Use incremental margin.*

**Competitive Position (Market Share, Win Rate, Switching Cost)**
- **5/5**: Market leader or #2 with defensible moat (brand, integration, ecosystem, switching cost). Hard for competitors to displace.
- **4/5**: Clear differentiation in one dimension. Customers choose us over specific alternatives. Solid competitive position.
- **3/5**: At parity with major competitors on key dimensions. Compete on execution or price. Vulnerable to better competitor.
- **2/5**: Losing share to one or more named competitors. Losing deals to better-positioned alternative.
- **1/5**: Irrelevant to competitive landscape. Fragmented market position. Losing deals to new entrants.

*Calibration: Competitive position is more than technology. Include channel position, customer segments owned, switching costs, and brand.*

### Scorecard Output Template

```
PRODUCT: [Name]
═══════════════════════════════════════════
Growth Rate:            [X/5] [Actual %] [Trend: ↑ ↓ →]
Retention:              [X/5] [90-day retention %] [Trend: ↑ ↓ →]
Net Expansion:          [X/5] [NRR % or equivalent] [Trend: ↑ ↓ →]
Customer Satisfaction:  [X/5] [NPS or CSAT] [Trend: ↑ ↓ →]
Unit Economics:         [X/5] [Gross margin %, LTV/CAC, Payback months]
Competitive Position:   [X/5] [Market position description]

OVERALL HEALTH SCORE:   [X/30]

HEALTH TRAJECTORY
Last quarter:  [Score]
This quarter:  [Score]
Direction:     [↑ Improving / → Stable / ↓ Declining]

KEY SIGNALS
Strengths:     [What is working]
Weaknesses:    [What is not working]
Inflection Points:
  - [Signal that matters: what it suggests]

PORTFOLIO ROLE
Current:       [Cash cow, Growth engine, Investment, Option, or Zombie]
Target:        [What role this product should play]
Strategic Fit: [HIGH/MEDIUM/LOW — does this product serve a clear portfolio role?]
═══════════════════════════════════════════
```

---

## Product Lifecycle Stage Assessment

Every product moves through stages, and strategy differs dramatically by stage. A mature product in growth-product strategy (hiring fast, feature-adding) destroys value. An emerging product treated as a cash cow stagnates.

### The Four Stages

**Introduction (0-30% of peak revenue)**
- **Characteristics**: New product, limited customer base, high churn, feature set incomplete, pricing unstable, significant losses
- **Key Metrics**: Time to first revenue, customer acquisition rate, activation rate, early NPS
- **Strategy**: Validate product-market fit. Obsess over retention and engagement. Build proof points.
- **Organization**: Small, experimental, fast-cycle learning. Test multiple customer segments in parallel.
- **Success Definition**: Evidence of repeatable customer acquisition, >30% 90-day retention, customers willing to pay

**Growth (30%-70% of peak revenue)**
- **Characteristics**: Repeatable customer acquisition, improving retention, revenue accelerating, feature set stabilizing, approaching breakeven or already profitable
- **Key Metrics**: Growth rate, retention curves, NRR, CAC payback, gross margin
- **Strategy**: Accelerate growth. Build repeatable go-to-market. Expand customer segments. Improve margins.
- **Organization**: Scaling go-to-market (sales, marketing, CS). Building operational discipline (processes, metrics, hiring).
- **Success Definition**: Consistent 25%+ YoY growth, retention >80%, NRR >110%

**Maturity (70%+ of peak revenue, growth stabilizing)**
- **Characteristics**: Market saturation in core segment, growth slowing, retention stable, margin optimization focus, competitive intensification
- **Key Metrics**: Market share in served market, customer concentration, pricing elasticity, margin structure, competitive churn rate
- **Strategy**: Defend market position. Optimize unit economics. Explore adjacent segments/products to reignite growth.
- **Organization**: Operational excellence focus. Efficiency organization. Product evolves toward ecosystem/partner leverage.
- **Success Definition**: Stable market share, gross margin >60%, stable revenue, clear path to adjacency

**Decline (Revenue declining YoY)**
- **Characteristics**: New competitors or platforms dominating, customer migration, churn exceeding new customer acquisition
- **Key Metrics**: Churn rate, win rate vs. new entrants, customer concentration of remaining base
- **Strategy**: Harvest for cash or double down on defensible segment. Prepare for sunset.
- **Organization**: Minimal investment. Focus on profitability. Plan transition for customers.
- **Success Definition**: Harvesting cash at declining burn rate OR successfully repositioned to defend smaller but profitable niche

### Stage Misalignment Signals

**Growth Product in Maturity Strategy** — Slowing revenue growth despite strong retention and engagement. Symptom: Leadership is focused on cost control and operational metrics, not market expansion. Fix: Shift focus to adjacencies, new segments, or business model innovation.

**Mature Product in Growth Strategy** — Churn accelerating due to overinvestment in features customers don't want. Symptom: Engineering velocity high, but NPS and engagement not improving. Fix: Shift focus from feature velocity to competitive defense and margin optimization.

**Introduction Product Treated as Cash Cow** — Insufficient investment in customer development and retention. Symptom: PMF signals are weak but product is expected to be profitable. Fix: Increase customer research and development cycles. Delay profitability timeline.

**Decline Product Denied Harvest** — Continued investment despite structural decline. Symptom: Management hopes turnaround will happen if investment increases. Fix: Name the decline explicitly. Plan for harvest or sunset. Reallocate engineering to higher-leverage opportunities.

---

## Product-Market Fit Measurement

Product-market fit (PMF) is not a binary state — it exists on a spectrum. More importantly, PMF claims are often false. This section operationalizes three methods to assess and validate PMF.

### Method 1: Sean Ellis Test

Sean Ellis' direct question test: "How would you feel if you could no longer use this product?"

- **40%+ respond "Very disappointed"** → Strong PMF signal
- **25-40% respond "Very disappointed"** → Approaching PMF. Investable.
- **<25% respond "Very disappointed"** → PMF has not been achieved. Continue exploring.

**Important**: Test only engaged users (those who have used the product meaningfully). Testing all users including one-time downloaders produces false negatives.

### Method 2: Retention Curves

A retention curve is a cohort's engagement or usage over time. PMF shows as a "shelf" — early churn (users who adopted but didn't find value) followed by a stable base (users finding continuous value).

**PMF Indicators:**
- Day 1 retention: 40-60% (some drop-off expected, not catastrophic)
- Day 30 retention: >30% (meaningful weekly engagement)
- Curve shape: Hockey stick (early drop, then flattens) not continued decline

**False PMF Indicators:**
- Continuous decline (users are not finding value and eventually all churn)
- Cohort decay (newer cohorts retain worse than older cohorts — signals positioning problem or product degradation)
- Spiky retention (viral moments or marketing pushes mask fundamental engagement weakness)

### Method 3: Engagement Scoring

Frequency of valuable usage. The LOOP test (Lawrence Levy's framework):

- **L = Loops**: How many users complete the job-to-be-done cycles per week? (For a messaging app: messages sent/received. For a fitness app: workouts completed.)
- **O = Outcomes**: Are loop completions producing measurable user outcomes? (For messaging: users report it solves their communication need. For fitness: users report progress toward fitness goals.)
- **O = Obligation**: Is the product becoming habitual? Do users miss it when they don't use it? (NPS or "very disappointed" correlates here.)
- **P = Payback**: Can the product sustain customer acquisition cost? (Do users refer others? Does retention curve stay flat?)

**Strong PMF Indicators:**
- LOOP frequency: >5 meaningful actions per user per week (varies by product type)
- Loop outcomes are visible to user (progress, completion, result)
- Users become obligated (habitual, miss the product)
- Payback is organic or sustainable CAC-based

---

## Portfolio Gaps Analysis

Once you've assessed individual product health, map the portfolio. Where is the portfolio strong? Where is it vulnerable?

### Portfolio Mapping Framework

Create a 2x2 matrix:

```
HIGH GROWTH
     │
   4 │  Growth Engines (invest)    Star/Question Marks (decide)
     │
     │
   3 │─────────────────────────────────────────────────
     │
     │  Cash Cows (harvest)        ? (evaluate)
   2 │
     │
     │
LOW  │
GROWTH
     └───────────────────────────────────────────────
       LOW ← PROFITABILITY → HIGH
```

**Growth Engines**: High growth, profitable or path to profitability. These are your future. Strategy: invest, expand, improve margins.

**Cash Cows**: Low growth, high profitability. Fund everything else. Strategy: optimize margins, fend off competition, harvest.

**Stars/Question Marks**: High growth, not yet profitable. Will they become cash cows or cash drains? Requires decision. Strategy: validate PMF, scale go-to-market, or kill.

**Zombies**: Low growth, low profitability. Strategy: sunset, franchise, or reposit.

### Portfolio Vulnerability Assessment

Ask:

1. **Where is new customer growth coming from?** — If one product drives 70%+ of new growth and that product shows PMF warning signs, portfolio is fragile.

2. **What if one product fails?** — Would the company still be viable? If not, you lack portfolio diversity.

3. **Are we defending our market?** — For each product, who is the competitor to watch? What's the competitive churn rate? Are we losing share?

4. **Where is adjacent market opportunity untapped?** — For each product, is there an adjacent segment or use case we're not serving? (If yes, portfolio has gaps. If no, we may be over-dependent on existing segment.)

5. **What's our dependency on one customer type?** — If 30%+ of revenue from one customer segment, that's a concentration risk.

---

## Sunset Decision Framework

Killing products is hard emotionally and organizationally. But not killing zombies is worse — they consume resources, distract organization, and dent morale (teams on zombies feel like they're failing). A clear sunset framework removes emotion.

### Sunset Criteria

A product should be sunset if **two or more** of the following hold:

- **PMF is not achievable in reasonable time**: Growth rate <10%, retention <50%, Sean Ellis <20%, despite 12+ months of work
- **Competitive position is permanently eroded**: Losing share to known competitors, win rate <30%, and defensible differentiation is unclear
- **Unit economics are broken**: Negative gross margin OR LTV/CAC <1.5 OR CAC payback >24 months, and path to improvement is unclear
- **Market is too small to justify investment**: TAM is <$50M or customer concentration is >50% (revenue is dependent on few customers)
- **Opportunity cost is high**: Engineering required to defend this product could build something with 10x better return
- **Team morale is at risk**: Team has lost confidence in product direction, best talent is leaving

### Sunset Implementation

**90 Days Before Sunset**: Communicate explicitly. "We're sunsetting Product X because [reason]. Here's the date. Here's what happens next."

**60 Days Before**: Start customer migration. Offer discounts on migration path. Provide detailed migration guides.

**30 Days Before**: Pause feature development. Move to maintenance-only mode. Reduce team size gradually.

**At Sunset**: Shut down service. Archive documentation. Offer final customer support window.

---

## Anti-Patterns to Watch

### Zombie Products

Products that are neither growing nor dying. Revenue is flat, churn is matched by new customer acquisition, so company keeps funding them. But they consume engineering, product, and leadership attention despite being strategically irrelevant.

**Signal**: Product appears in portfolio review. Everyone agrees it's not strategic. Then next quarter, it's still there.

**Fix**: Apply the sunset framework explicitly. If not sunset-worthy, assign a clear role and owner. If neither, sunset.

### Over-Diversification

Portfolio with 10+ products, most of them <$1M revenue and <10 customers. Sounds diversified, is actually fragmented. Engineering is spread thin. Go-to-market is incoherent.

**Signal**: "How many products do we have?" produces a confusing answer involving different definitions of product vs. feature vs. offering.

**Fix**: Consolidate. Merge adjacent products. Sunset niche offerings. Target <5 core products.

### PMF Hallucination

Strong growth or high revenue mistaken for PMF. Growth is often driven by sales muscle or marketing spend, not product satisfaction. PMF actually looks like: strong retention + word-of-mouth growth + high NPS + low CAC + high LTV/CAC.

**Signal**: Revenue is growing but retention is declining. NPS is dropping. CAC is increasing. Team is celebrating growth while product health metrics are deteriorating.

**Fix**: Run the Sean Ellis test and retention analysis. Separate acquisition from engagement. If retention is weak, you don't have PMF, you have a sales problem.

### The Sacred Cow Product

Launched by a founder or CEO, now it's defended regardless of performance. Data suggesting sunset is met with defensiveness. Features are built for this product even when better uses of engineering exist.

**Signal**: Portfolio analysis recommends sunset. Leadership says "no, this product is important to me," despite weak metrics.

**Fix**: Name the sacred cow explicitly. Ask: "If this product were proposed today, would we fund it?" If no, ask why we're funding it now. If yes, ask what we're not seeing in the data.

### Feature Creep Masking PMF Deterioration

Product has strong usage but all engagement is in old features. New features have low usage. Product team is shipping faster but customers are not adopting faster. Core engagement is declining.

**Signal**: Feature velocity is high. Roadmap is full. But retention curve is flat or declining.

**Fix**: Audit which features drive engagement and retention. Which have weak adoption? Why? Pause new feature work. Simplify. Reduce surface area.

