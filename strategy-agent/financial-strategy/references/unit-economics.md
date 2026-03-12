# Unit Economics & Profitability Analysis

The goal is to understand profitability at the atomic level: per customer, per product, per segment, per transaction. Where is value created? Where is it destroyed? This is the foundation of defensible profit growth.

---

## 1. Core Unit Economics Framework

Unit economics are the fundamental metrics that define the business model's ability to create profit. They vary dramatically by business model.

### SaaS Unit Economics

For subscription businesses, the core metrics are:

```
SAAS UNIT ECONOMICS
═══════════════════════════════════════════

ACQUISITION METRICS
Customer Acquisition Cost (CAC)
  = [Sales & Marketing Spend] / [New Customers Acquired]
  = $XXX per customer
  CAC Payback Period = [CAC] / [ARPU × Gross Margin %]
  = X months

ARPU (Annual Recurring Revenue Per User)
  = [Total ARR] / [# Customers]
  = $XXX per customer per year
  Trend: [Growing / Stable / Declining]

RETENTION METRICS
Gross Retention Rate (GRR)
  = [Revenue at End of Period – Churn] / [Revenue at Start of Period]
  = X%

Net Retention Rate (NRR)
  = [Revenue at End of Period] / [Revenue at Start of Period]
  = X% (includes upsells)

Churn Rate (Monthly)
  = [Customers Lost in Month] / [Customers at Start of Month]
  = X%
  Annual equivalent: [1 – (1 – Monthly Churn)^12] = X%

Customer Lifetime Value (LTV)
  = [ARPU × Gross Margin %] / [Monthly Churn Rate]
  = $XXX total over customer lifetime

VALUE CREATION RATIO
LTV / CAC Ratio
  = X (Industry benchmark: 3:1 or higher)
  Assessment: [Healthy / Concerns / Unsustainable]

Payback Period
  = [CAC] / [ARPU × Gross Margin % / 12]
  = X months (Target: <12 months)
```

**What matters:**
- **LTV/CAC > 3:** Sustainable unit economics (often targets 5+)
- **LTV/CAC 2-3:** May work but tight margins on sales spend
- **LTV/CAC < 2:** Economics don't justify customer acquisition at scale
- **Payback Period < 12 months:** Strong; self-funding CAC from revenue. > 24 months: may require significant capital.

### Marketplace/Platform Unit Economics

For two-sided marketplans (Uber, Airbnb, DoorDash style):

```
MARKETPLACE UNIT ECONOMICS
═══════════════════════════════════════════

SUPPLY SIDE
Total Supply (Active Listings / Merchants)
  = X [growing at Y% annually]

Supply Growth CAC
  = [Spend to onboard merchants] / [New merchants]
  = $XXX

Supply Lifetime Value
  = [GMV per merchant] × [Gross margin %] / [Merchant churn rate]
  = $XXX

DEMAND SIDE
Total Demand (Active Consumers / Buyers)
  = X [growing at Y% annually]

Consumer Acquisition Cost
  = [Marketing spend] / [New consumers]
  = $XXX

Consumer Lifetime Value
  = [Spend per consumer] × [Gross margin %] / [Consumer churn rate]
  = $XXX

MARKETPLACE METRICS
Gross Merchandise Value (GMV)
  = $XXM annually
  Growth rate: X% YoY

Take Rate (Commission)
  = [Fees / GMV] = X%
  (Benchmark: varies widely 5-30% depending on service)

Unit Economics per Transaction
  = [Gross margin per transaction] – [CAC allocation per transaction]
  = $XXX (positive or negative?)

Network Effects
  = [Is NPS improving or declining?] [Are repeat rates improving?] [Is virality coefficient > 1?]
```

### DTC / E-Commerce Unit Economics

For direct-to-consumer brands:

```
DTC UNIT ECONOMICS
═══════════════════════════════════════════

UNIT ECONOMICS PER TRANSACTION
Average Order Value (AOV)
  = [Total Revenue] / [Total Orders]
  = $XXX
  Trend: [Growing / Stable / Declining]

Customer Acquisition Cost (CAC)
  = [Marketing spend] / [New customers]
  = $XXX

Gross Margin %
  = [AOV – COGS] / [AOV]
  = X%

Contribution to CAC
  = [AOV × Gross Margin %]
  = $XXX
  Can we afford CAC? [Yes / Marginal / No]

REPEAT PURCHASE METRICS
Customer Repeat Rate
  = [# Repeat customers] / [# Total customers who have purchased]
  = X% (after 60 days, 180 days)

Repeat Purchase Value
  = [Total revenue from repeats] / [Repeat customers]
  = $XXX

Cohort Analysis
  Cohort acquired in Month X:
    – Month 1 retention: X%
    – Month 3 retention: X%
    – Month 6 retention: X%
    – Projected LTV: $XXX

CUSTOMER LIFETIME VALUE
LTV = [AOV × Gross Margin %] × [Average # Purchases]
    = $XXX

LTV / CAC Ratio
  = X (Target: >3)

Payback Period
  = [CAC] / [AOV × Gross Margin %]
  = X months

COHORT PAYBACK
How many repeat purchases to break even on CAC?
  = [CAC] / [AOV × Gross Margin %]
  = X purchases

When does this happen (in days / months)?
  = X (Is it realistic for customer to make this many purchases?)
```

### Enterprise / B2B SaaS Unit Economics

For enterprise sales:

```
ENTERPRISE B2B UNIT ECONOMICS
═══════════════════════════════════════════

CONTRACT VALUE
Annual Contract Value (ACV)
  = [Total contract value] / [# Contracts]
  = $XXX
  Range: [$X to $XXX depending on segment]

Total Contract Value (TCV) – includes multi-year deals
  = [TCV] / [# Contracts]
  = $XXX

Ramp Curve
  Year 1 ACV realization: X%
  Year 2 ACV realization: Y%
  Year 3+ ACV realization: Z%

SALES PRODUCTIVITY
CAC = [Fully Loaded Sales & Marketing] / [New ACV closed]
    = [Quota Load] / [% to quota]
    = $XXX

Sales Cycle
  = X months (has it been lengthening?)

Win Rate
  = [# Deals won] / [# Deals pursued]
  = X%

RETENTION & EXPANSION
Net Retention Rate (NRR)
  = [Ending ARR] / [Starting ARR]
  = X%

Expansion Revenue per Customer (Upsell/Cross-sell)
  = [Expansion revenue] / [# existing customers]
  = $XXX annually (growing or declining?)

Logo Churn
  = [# Customers lost] / [# Customers at start]
  = X% annually

Revenue Churn
  = [Revenue lost] / [Starting revenue]
  = X% (different from logo churn due to expansion)

PAYBACK & LTV
CAC Payback (months)
  = [CAC] / [ACV × Gross Margin % / 12]
  = X months

Customer Lifetime Value
  = [ACV × Gross Margin %] / [Annual churn rate]
  = $XXX

LTV / CAC
  = X (Target: >3-5 depending on payback comfort)
```

---

## 2. Contribution Margin Analysis

Contribution margin is the revenue remaining after deducting variable costs. It's the pool available to cover fixed costs and generate profit.

### Step 1: Contribution Margin Calculation

```
CONTRIBUTION MARGIN ANALYSIS
═══════════════════════════════════════════

PRODUCT / SEGMENT LEVEL
Revenue                                    $XXM      100%
Variable Costs:
  COGS / Cost of Service Delivery         ($XXM)     (X%)
  Payment processing / Platform fees      ($XXM)     (X%)
  Fulfillment / Logistics (if variable)   ($XXM)     (X%)
  Sales commissions                       ($XXM)     (X%)
  ───────────────────────────────────────────
Contribution Margin                        $XXM       X%
  Also called: Gross Profit (if no variable OpEx)

Contribution per Unit Sold
  = [Contribution Margin] / [# Units]
  = $XXX

Contribution Margin Ratio
  = [Contribution Margin] / [Revenue]
  = X%
```

Key insight: Contribution margin shows how much of each dollar of revenue is available to cover fixed costs (R&D, corporate overhead, etc.) and profit.

### Step 2: Segment Profitability Tiers

Break down contribution margin by segment, customer type, or product line:

```
SEGMENT PROFITABILITY RANKING
═══════════════════════════════════════════
                    Revenue    COGS %    CM %    Contribution   Rank
Segment A           $XXM       X%        X%      $XXM            ★★★★★
Segment B           $XXM       X%        X%      $XXM            ★★★★
Segment C           $XXM       X%        X%      $XXM            ★★★
Segment D           $XXM       X%        X%      $XXM            ★★
Corporate Overhead   —          —        —       ($XXM)          —
                    ───────────────────────────────────────
Total               $XXM       X%        X%      $XXM
```

**Questions:**
- Are high-margin and low-margin segments both strategic, or should low-margin segments be exited?
- Is there a customer type analysis? (Some customer segments may be more or less profitable even within same product)
- Is there pricing power? (Can margin be expanded by adjusting price or reducing COGS?)

### Step 3: Fixed Cost Coverage

Once you know contribution margin, determine how much fixed cost it covers:

```
FIXED COST COVERAGE
═══════════════════════════════════════════
Total Contribution Margin                  $XXM

Fixed Operating Expenses:
  R&D (product development, not variable)  ($XXM)
  Corporate G&A                            ($XXM)
  Corporate overhead allocation            ($XXM)
  ───────────────────────────────────────────
Operating Income (before D&A)              $XXM       X% margin

Questions:
  – What is the breakeven point (contribution margin = fixed costs)?
  – How much revenue shortfall can we absorb? (safety margin)
  – How much of fixed cost is truly fixed vs. can be flexed?
```

---

## 3. Customer Profitability Distribution

Customers are not equally profitable. Some are highly profitable, others are loss-making. Understand the distribution.

### Step 1: Customer Profitability Ranking

```
CUSTOMER PROFITABILITY ANALYSIS
═══════════════════════════════════════════

Revenue per Customer (Annual)
  Customer A (largest):          $XXX
  Customer B:                    $XXX
  ...
  Customer Z (smallest):         $X

Gross Profit per Customer (Annual)
  = [Revenue] – [COGS specific to that customer] – [Support cost for that customer]
  = Customer A: $XXX
  = Customer B: $XXX
  ...
  = Customer Z: $(XXX) [Loss-making!]

Customer Profitability Ranking
  Top 20% of customers: X% of profit
  Middle 30%:           Y% of profit
  Bottom 50%:           Z% of profit (or negative profit?)

Pareto Distribution
  [Is 80/20 rule holding? 70/30? Is distribution more extreme?]
```

### Step 2: Customer Cohort Analysis

Group customers by acquisition cohort or characteristics:

```
COHORT PROFITABILITY ANALYSIS (Example: SaaS)
═══════════════════════════════════════════

Cohort (Customers acquired in January 2023)
  Customers acquired:         X
  Month 1 ARPU:               $XXX
  Month 3 ARPU (after churn): $XXX
  Month 6 ARPU:               $XXX
  Month 12 ARPU:              $XXX
  Projected total revenue:    $XXM
  Projected total profit:     $XXM
  Cohort health:              [Healthy / Concerning]

Cohort Comparison
  Cohort acquired Q4 2022:  $X profit; YoY growth: +Y%
  Cohort acquired Q4 2023:  $X profit; YoY growth: +Y%
  Trend:                     [Improving cohort quality or deteriorating?]
```

**What this tells you:**
- Are newer cohorts more or less profitable than older ones?
- Is customer quality (retention, expansion) improving or declining?
- Are you acquiring more loss-making customers in pursuit of growth?

### Step 3: Segment-Level Economics

Analyze profitability by customer segment (company size, industry, geography, use case):

```
PROFITABILITY BY SEGMENT
═══════════════════════════════════════════
                        Revenue    CAC    LTV    LTV/CAC    Health
Large Enterprise        $XXM       $XXX   $XXX   X          [✓/⚠/✗]
Mid-Market              $XXM       $XXX   $XXX   X          [✓/⚠/✗]
SMB                     $XXM       $XXX   $XXX   X          [✓/⚠/✗]
Channel / Reseller      $XXM       $XXX   $XXX   X          [✓/⚠/✗]
```

---

## 4. Marginal Economics & Sensitivity

Understanding how unit economics change as the business scales is critical for forecasting profitability.

### Step 1: Variable Cost Sensitivity

How do costs behave as volume scales?

```
VARIABLE COST SCALING
═══════════════════════════════════════════
Current Volume:        X units

Cost per Unit @ 100% volume:    $XXX
Cost per Unit @ 150% volume:    $XXX (Do we achieve volume discounts?)
Cost per Unit @ 200% volume:    $XXX

Conclusion:
  – Are COGS declining as we scale? (Volume discounts from suppliers?)
  – Are COGS stable? (Commodity cost structure?)
  – Are COGS increasing? (Supplier negotiations breaking down / inflation?)
```

### Step 2: Fixed Cost Absorption

As revenue grows, fixed costs absorb across a larger base, improving margins.

```
OPERATING LEVERAGE ANALYSIS
═══════════════════════════════════════════

Current State
  Revenue:                        $XXM
  Fixed OpEx:                     $XXM (includes R&D, G&A)
  Fixed OpEx as % of Revenue:     X%
  Variable costs as % of Rev:     X%
  Operating Margin:               X%

At 1.5× Revenue (no change in fixed costs)
  Revenue:                        $XXM
  Fixed OpEx:                     $XXM (same)
  Fixed OpEx as % of Revenue:     X% (lower)
  Variable costs:                 $XXM (scales with revenue)
  Operating Margin:               X% (higher)

Operating Leverage Factor
  = [% change in operating income] / [% change in revenue]
  = X (for every 1% revenue growth, operating income grows X%)
```

**Interpretation:**
- If operating leverage > 1, business gets more profitable as it scales (up to capacity limits)
- If operating leverage < 1, business becomes less profitable as it scales (sign of inefficiency)

---

## 5. Unit Economics by Business Model

### Subscription Model Checklist

```
SAAS/SUBSCRIPTION CHECKLIST
═══════════════════════════════════════════
□ Monthly Churn < 5% (Annual < 45%)
□ Net Retention Rate > 100% (expansion offsetting churn)
□ CAC Payback < 12 months
□ LTV / CAC > 3
□ Gross Margin > 70%
□ Operating Margin > 10% (mature companies)
□ CAC increasing or stable (not deteriorating)
□ Retention improving or stable (not deteriorating)
□ Expansion revenue growing faster than base revenue
```

### Marketplace Model Checklist

```
MARKETPLACE CHECKLIST
═══════════════════════════════════════════
□ Supply-side two-sided network effects evident
□ Demand-side two-sided network effects evident
□ Take rate sustainable (competitors cannot undercut)
□ Repeat rate > 60% on demand side
□ Supply growth rate > Demand growth rate (excess supply better than excess demand)
□ Unit economics per transaction positive (not necessarily profitable at company level yet)
□ GMV growth > 50% annually (growth offsetting take rate pressure)
□ Cohort retention improving over time
```

### DTC Model Checklist

```
DTC CHECKLIST
═══════════════════════════════════════════
□ CAC < 30% of first purchase value
□ Repeat purchase rate > 20% within 6 months
□ LTV (repeat purchases) > 3× CAC
□ Gross margin > 50%
□ Payback period < 6 months
□ Unit economics work at scale (not just with paid traffic / influencer partnerships)
□ Customer acquisition channels diversifying (not over-reliant on paid ads)
□ Organic / referral growth increasing as % of new customers
```

### Enterprise B2B Checklist

```
ENTERPRISE B2B CHECKLIST
═══════════════════════════════════════════
□ ACV growing or stable (not declining)
□ Sales cycle < 6 months (ideally)
□ Win rate > 20%
□ Net retention > 100% (expansion offsetting churn)
□ CAC payback < 18 months
□ LTV / CAC > 3-5 (depending on sales intensity)
□ Gross margin > 70%
□ Sales productivity (ACV attained vs. quota) consistent
□ Sales ramp curve predictable (not erratic)
```

---

## Output Template

```
UNIT ECONOMICS & PROFITABILITY ANALYSIS
═══════════════════════════════════════════

BOTTOM LINE UP FRONT
[One-sentence assessment of unit economics health and primary profit driver/lever]

UNIT ECONOMICS BY BUSINESS MODEL
[SaaS / Marketplace / DTC / Enterprise metrics as appropriate]

CONTRIBUTION MARGIN & PROFITABILITY TIERS
[Segment-level profitability ranking, margin architecture]

CUSTOMER PROFITABILITY DISTRIBUTION
[Top customers vs. average vs. bottom tier, cohort analysis if relevant]

OPERATING LEVERAGE & SCALING DYNAMICS
[How do margins change as business scales? Where is the friction?]

CRITICAL UNIT ECONOMICS METRICS SCORECARD
[Health assessment: which metrics are healthy, which need attention]

KEY FINDINGS
1. [Finding] — Confidence: [H/M/L] — Action: [What to do]
2. [Finding] — Confidence: [H/M/L] — Action: [What to do]
3. [Finding] — Confidence: [H/M/L] — Action: [What to do]

PROFITABILITY IMPROVEMENT LEVERS
[Where should the company focus? Price? COGS? Churn reduction? CAC?]

NEXT STEPS
[What analysis should follow? Business case for specific initiatives? Cost transformation? Pricing analysis?]
═══════════════════════════════════════════
```
