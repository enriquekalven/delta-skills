# Financial Modeling & Forecasting

The goal is to build driver-based financial models that forecast P&L, balance sheet, and cash flow under different scenarios, and to test sensitivity to key assumptions. A model is only useful if it clarifies which assumptions matter most.

---

## 1. 3-Statement Model Architecture

A complete financial model links Income Statement, Balance Sheet, and Cash Flow Statement so that changes in operations flow through all three.

### Step 1: Revenue Driver Architecture

Build revenue forecast from unit drivers, not just a top-line growth rate.

```
REVENUE DRIVER ARCHITECTURE
═══════════════════════════════════════════

Option A: Unit × Price Model (Product-Based)
  Units Sold (Year 1)           X
  Growth Rate (%)               Y%
  Units Sold (Year 5)           [Year 1 × (1+growth)^4]

  Price per Unit (Year 1)       $XXX
  Price inflation (%)           Z%
  Price per Unit (Year 5)       [Year 1 × (1+inflation)^4]

  Revenue (Year 1)              [Units × Price]
  Revenue (Year 5)              [Units × Price at Year 5]

Option B: Customer × ARPU Model (Subscription)
  Customers (Year 1)            X
  Annual CAC payback logic      [Cost to acquire / ARPU payback]
  Customer growth rate          Y%
  Customers (Year 5)            [Year 1 × (1+growth)^4]

  ARPU (Year 1)                 $XXX
  ARPU growth (expansion)       Z% annually
  ARPU (Year 5)                 [Year 1 × (1+growth)^4]

  Revenue (Year 1)              [Customers × ARPU]
  Revenue (Year 5)              [Customers × ARPU at Year 5]

Option C: Segment-Based Model
  Segment A units               X at price $XXX
  Segment B units               Y at price $YYY
  Segment C units               Z at price $ZZZ
  Total Revenue                 [Sum of all segments]
  Growth assumption per segment [Different for each]

CRITICAL: Revenue should NEVER be a single growth rate assumption.
Build from units, customers, or segments, so each assumption is testable.
```

**Why this matters:** If you say "revenue grows 25%," you have no idea what you're assuming. If you say "we acquire 100 new enterprise customers at $50K ACV," that's testable.

### Step 2: Cost of Goods Sold (COGS) & Gross Margin

```
COGS FORECAST
═══════════════════════════════════════════

Option A: % of Revenue (Simple)
  Revenue                       $XXM
  COGS % (assumption)           X%
  COGS Dollars                  $XXM
  Gross Margin %                (100% – X%)

  COGS % Sensitivity:
    Base case: X%
    If volume discounts achieved: X-1%
    If inflation hits COGS: X+2%
    Outcome: Gross margin ranges from X% to Y%

Option B: Component-Based (More Precise)
  Revenue (Units)               X units

  Direct Material Cost per Unit    $XX
  Direct Labor Cost per Unit       $XX
  Outsourced Service per Unit      $XX
  Logistics / Fulfillment per Unit $XX
  ─────────────────────────────
  Total COGS per Unit              $XXX
  COGS Dollars = Units × COGS/unit

  Gross Margin % = [Revenue – COGS] / Revenue

CRITICAL: COGS % often improves (margin expansion) as volume scales due to:
  – Volume discounts from suppliers
  – Labor absorption (fixed labor costs spread over more units)
  – Supply chain efficiencies
BUT can also deteriorate due to:
  – Input cost inflation
  – Loss of pricing power
  – Shift to lower-margin products
```

### Step 3: Operating Expense Forecast

```
OPERATING EXPENSE FORECAST
═══════════════════════════════════════════

Sales & Marketing (S&M)
  Customer Acquisition model:
    Target annual CAC: $XXX per customer
    Planned customer acquisitions: X
    S&M spend needed: [CAC × # customers]

  Alternative: S&M % of Revenue
    Current: X%
    Assumption (improving scale): Y%
    Spend: [Revenue × Y%]

  Red flag: If S&M % is increasing while retention is worsening, model is not sustainable

Research & Development (R&D)
  Model as:
    – Fixed headcount: X engineers at $XXX loaded cost = $XXM annually
    – % of revenue: Y% (common in growth stage: 20-30%)
    – Specific project budgets: [List projects and costs]

  Sensitivity: Does product velocity change if R&D spend increases / decreases?

General & Administrative (G&A)
  Fixed costs: Finance, Legal, HR, Executive
    – Headcount: X staff at $XXX loaded = $XXM
    – As % of revenue: Y% (should decline as company scales)
    – Does G&A include corporate office, insurance, etc.?

  Assumption check: G&A as % of revenue should decline over time

TOTAL OPEX FORECAST (EXAMPLE)
Year 1:
  S&M spend: $XXM (@ X% of revenue)
  R&D spend: $XXM (@ Y% of revenue)
  G&A spend: $XXM (@ Z% of revenue)
  Total OpEx: $XXM (Total % of revenue: X%)

Year 5:
  S&M spend: $XXM (@ X-1% of revenue – improving CAC efficiency)
  R&D spend: $XXM (@ Y-2% of revenue – operating leverage)
  G&A spend: $XXM (@ Z-3% of revenue – fixed cost absorption)
  Total OpEx: $XXM (Total % of revenue: X-2%)

Operating leverage emerges when OpEx % declines as revenue scales.
```

### Step 4: Complete P&L Forecast

```
3-YEAR P&L FORECAST (EXAMPLE)
═══════════════════════════════════════════
                        Year 1      Year 2      Year 3
Revenue                 $XXM        $XXM        $XXM
  YoY growth            +X%         +Y%         +Z%

COGS                    ($XXM)      ($XXM)      ($XXM)
  COGS % of Rev         (X%)        (X-1%)      (X-1%)
────────────────────────────────────────────
Gross Profit            $XXM        $XXM        $XXM
  Gross Margin %        X%          X+1%        X+1%

Operating Expenses:
  S&M                   ($XXM)      ($XXM)      ($XXM)
    % of revenue        (X%)        (X-1%)      (X-1%)
  R&D                   ($XXM)      ($XXM)      ($XXM)
    % of revenue        (Y%)        (Y-1%)      (Y-1%)
  G&A                   ($XXM)      ($XXM)      ($XXM)
    % of revenue        (Z%)        (Z-1%)      (Z-1%)
────────────────────────────────────────────
Operating Income        $XXM        $XXM        $XXM
  Operating Margin %    X%          X+Y%        X+Y+Z%

Interest expense        ($XXM)      ($XXM)      ($XXM)
Taxes                   ($XXM)      ($XXM)      ($XXM)
────────────────────────────────────────────
Net Income              $XXM        $XXM        $XXM
  Net Margin %          X%          X%          X%
```

### Step 5: Balance Sheet Forecast

```
BALANCE SHEET FORECAST
═══════════════════════════════════════════

ASSETS
Cash                    $XXM (Driven by: FCF + financing – capex)
Accounts Receivable     $XXM (= Revenue × Days Sales Outstanding / 365)
Inventory               $XXM (= COGS × Days Inventory Outstanding / 365)
Fixed Assets (net)      $XXM (= Prior year + CapEx – Depreciation)
Other Assets            $XXM
────────────────────────────────────────────
Total Assets            $XXM

LIABILITIES
Accounts Payable        $XXM (= COGS × Days Payable Outstanding / 365)
Short-term Debt        $XXM (Loan repayments due within 12 months)
Accrued Expenses        $XXM (Bonuses, taxes, other payables)
────────────────────────────────────────────
Current Liabilities     $XXM

Long-term Debt         $XXM (Loan principal due > 12 months)
────────────────────────────────────────────
Total Liabilities       $XXM

EQUITY
Common Stock            $XXM (Unchanged unless new equity raise)
Retained Earnings       $XXM (Prior year + Net Income – Dividends)
────────────────────────────────────────────
Total Equity            $XXM

Check: Total Assets = Total Liabilities + Total Equity
```

### Step 6: Cash Flow Statement Forecast

```
CASH FLOW FORECAST
═══════════════════════════════════════════

OPERATING ACTIVITIES
Net Income              $XXM
Add back non-cash:
  Depreciation          +$XXM
  Amortization          +$XXM
  Stock compensation    +$XXM
Changes in working capital:
  Increase in AR        ($XXM) [uses cash]
  Increase in inventory ($XXM) [uses cash]
  Increase in AP        +$XXM [sources cash]
────────────────────────────────────────────
Operating Cash Flow     $XXM

INVESTING ACTIVITIES
Capital expenditures    ($XXM)
Acquisitions            ($XXM)
────────────────────────────────────────────
Investing Cash Flow     ($XXM)

FINANCING ACTIVITIES
Debt raised             +$XXM
Debt repaid             ($XXM)
Equity raised           +$XXM
Dividends paid          ($XXM)
────────────────────────────────────────────
Financing Cash Flow     $XXM (or negative)

Net Change in Cash      = Operating + Investing + Financing
Ending Cash             = Beginning Cash + Net Change

CRITICAL: If Operating Cash Flow < Net Income, the business is burning working capital.
          If Operating Cash Flow > Net Income, the business is generating cash from operations.
```

---

## 2. Scenario Analysis (Base / Bull / Bear)

Never forecast a single P&L. Build three scenarios that test key assumptions.

### Step 1: Define Scenario Assumptions

```
SCENARIO ASSUMPTIONS
═══════════════════════════════════════════

BASE CASE (Most Likely)
  Revenue growth:         X% annually
  Gross margin:           Y% (stable or improving slightly)
  OpEx as % of revenue:   Z% (declining with scale)
  Customer churn:         A% annually (stable)
  ARPU growth:            B% annually (modest expansion)
  Key risks:              [1-2 realistic risks]

BULL CASE (Optimistic – Things Go Right)
  Revenue growth:         X% annually (higher than base due to:)
    – Faster customer acquisition (better product-market fit)
    – Larger deal sizes (enterprise expansion)
    – International expansion (new market)
  Gross margin:           Y% + 2-3 bps (achieve volume discounts, reduce COGS)
  OpEx as % of revenue:   Z-1% (better operating leverage)
  Customer churn:         A% -1% (improvement in retention)
  ARPU growth:            B%+2% (stronger expansion revenue)
  Key upside scenarios:   [What would trigger this? Major deal? Product launch?]

BEAR CASE (Pessimistic – Things Go Wrong)
  Revenue growth:         X% – 10% annually (slower due to:)
    – Slower customer acquisition (market saturation, competition)
    – Lower deal sizes (pivot downmarket, new pricing)
    – Churn acceleration (product issues, competitive loss)
  Gross margin:           Y% – 3-5 bps (inflation hits COGS, pricing power lost)
  OpEx as % of revenue:   Z+2% (struggle to cut costs to match lower revenue)
  Customer churn:         A% +3% (retention deteriorates)
  ARPU growth:            B-2% or negative (downselling, compression)
  Key downside scenarios: [What would trigger this? Regulatory change? Recession? Key customer loss?]

CRITICAL: Make sure Bull and Bear cases are not fairy tales or disasters.
They should be realistic scenarios that management should be prepared for.
```

### Step 2: Financial Outcomes Under Each Scenario

```
SCENARIO COMPARISON TABLE
═══════════════════════════════════════════
                    BASE CASE      BULL CASE      BEAR CASE
Year 1 Revenue      $XXM           $XXM (+Y%)     $XXM (-Y%)
Year 5 Revenue      $XXM           $XXM           $XXM
5-year CAGR         X%             X%+Z%          X%-Z%

Year 5 Gross Margin X%             X%+Y%          X%-Y%
Year 5 OpEx %       Z%             Z-1%           Z+2%
Year 5 Op. Income   $XXM           $XXM           $XXM or loss

Cumulative FCF
(Years 1-5)         $XXM           $XXM           $XXM

Year 5 Cash Balance $XXM           $XXM           $XXM (or negative?)

Key Implications
  Base:   Breakeven / Modestly profitable by Year 3, self-funding by Year 4
  Bull:   High growth, profitable by Year 2, strong cash generation
  Bear:   Prolonged path to profitability, may need additional capital in Year 3-4
```

### Step 3: Scenario Triggers

Define what events would move you from base to bull or bear:

```
SCENARIO TRIGGER FRAMEWORK
═══════════════════════════════════════════

BASE CASE HOLDS IF:
  – Product adoption continues at historical rate
  – No major competitive disruption
  – No significant input cost inflation
  – Team remains stable

MOVE TO BULL IF:
  – [Specific event #1]: e.g., "Major enterprise customer signed for $X revenue"
  – [Specific event #2]: e.g., "Gross margin improves to X% due to [reason]"
  – [Specific event #3]: e.g., "Geographic expansion enters new market with Y% attach rate"

MOVE TO BEAR IF:
  – [Specific event #1]: e.g., "Churn accelerates above X% in two consecutive quarters"
  – [Specific event #2]: e.g., "Major customer (>10% revenue) churns"
  – [Specific event #3]: e.g., "COGS inflation >X% due to supplier consolidation"

CRITICAL: Use these triggers to set monitoring KPIs and alert thresholds.
```

---

## 3. Sensitivity Analysis

Which assumptions matter most? Test sensitivity to key drivers.

```
SENSITIVITY TABLE: IMPACT ON YEAR 5 OPERATING MARGIN
═══════════════════════════════════════════
                        -10%        BASE        +10%
Revenue Growth Rate
  (X% annually)         X%         X%          X%
  Year 5 Op. Margin:    X%         Y%          Z%

COGS % (Impact on Gross Margin)
  (Base: X%)            X+2%       X%          X-2%
  Year 5 Op. Margin:    X%         Y%          Z%

S&M Efficiency (CAC as % of revenue)
  (Base: X%)            X+2%       X%          X-2%
  Year 5 Op. Margin:    X%         Y%          Z%

OpEx as % of Revenue
  (Base: X%)            X+2%       X%          X-2%
  Year 5 Op. Margin:    X%         Y%          Z%

Key Insight: [Which assumption has the biggest impact?] [What does this tell us?]
```

**Interpretation:**
- If operating margin is most sensitive to revenue growth, focus on sales/GTM strategy
- If operating margin is most sensitive to COGS %, focus on supply chain and manufacturing
- If operating margin is most sensitive to OpEx %, focus on operating leverage and cost structure

---

## 4. Monte Carlo Simulation (Probabilistic Modeling)

For more sophisticated analysis, run a Monte Carlo simulation where each assumption has a probability distribution, not a point estimate.

```
MONTE CARLO SETUP
═══════════════════════════════════════════

Instead of: Revenue grows 25% ± 5%
Say:        Revenue growth has a normal distribution:
            Mean: 25%, Std Dev: 5%
            10% chance it's <17%, 10% chance it's >33%

Instead of: Churn rate is 5%
Say:        Churn rate has a beta distribution:
            Mean: 5%, Range: 2%-10%
            Most likely: 4%, 90% confidence interval: 3%-7%

Run 10,000 simulations where each variable randomly draws from its distribution.
Output: Distribution of possible Year 5 outcomes (not just a single number).

Example output:
  Year 5 Operating Income
    10th percentile (worst 10% of outcomes): ($XXM) – loss
    Median (middle):                         $XXM
    90th percentile (best 10% of outcomes):  $XXM
    Upside/downside range: $XXM

This shows the range of realistic outcomes given uncertainty in assumptions.
```

---

## 5. Model Quality Checklist

Before shipping a model, verify it passes quality gates:

```
FINANCIAL MODEL AUDIT CHECKLIST
═══════════════════════════════════════════

STRUCTURE
□ Revenue builds from unit drivers (not arbitrary growth rate)
□ COGS scales logically with revenue (either % or component-based)
□ OpEx broken into S&M, R&D, G&A (not lumped)
□ All P&L line items reconcile to balance sheet and cash flow
□ Cash flow articulates to ending cash balance (doesn't plug)
□ Balance sheet balances (Assets = Liabilities + Equity)

ASSUMPTIONS
□ All assumptions explicitly listed and dated
□ Each assumption has a data source (history / industry benchmark / expert estimate)
□ Assumptions differ between scenarios (Bull and Bear are not just ±X%)
□ Assumptions are internally consistent (e.g., revenue growth doesn't assume market size larger than known)
□ Working capital assumptions (DSO, DIO, DPO) are supported by historical analysis

SENSITIVITY & SCENARIOS
□ Three scenarios (Base / Bull / Bear) built and compared
□ Sensitivity table shows impact of key assumptions (±10-20% change)
□ Top 3 assumptions that drive the outcome are identified
□ Scenario triggers are explicitly defined (when would we move to Bull / Bear?)

REASONABLENESS CHECKS
□ Operating margins trend toward healthy levels (not perpetually negative)
□ Cash doesn't grow without generating EBITDA (except at fundraise)
□ Headcount growth aligns with revenue growth (revenue per employee metric)
□ Customer counts and CAC are internally consistent
□ Implied market share (if entering new market) is realistic

DOCUMENTATION
□ All formulas visible and simple (no black boxes)
□ Unit assumptions clearly labeled (prices, customers, units, etc.)
□ Gross margin drivers called out
□ Operating leverage assumptions explicit

IF A MODEL FAILS ANY OF THESE GATES, IT'S NOT READY.
```

---

## Output Template

```
FINANCIAL MODELING & FORECASTING
═══════════════════════════════════════════

BOTTOM LINE UP FRONT
[One sentence: what the model shows about profitability trajectory and key risks]

REVENUE DRIVER ARCHITECTURE
[How revenue is built: units/customers/segments, with growth assumptions]

COST STRUCTURE & MARGINS
[COGS forecast, gross margin drivers, OpEx scaling logic]

BASE CASE 3-YEAR FORECAST
[P&L, balance sheet, cash flow under most likely scenario]

SCENARIO ANALYSIS: BASE VS. BULL VS. BEAR
[Comparison table with key financial outcomes under each scenario]

SENSITIVITY ANALYSIS
[Which assumptions matter most? Impact table]

KEY ASSUMPTIONS & SENSITIVITIES
1. [Assumption] — Data source: [Where does this come from?] — Impact: [If wrong by 10%, does outcome change by X%?]
2. [Assumption] — Data source: [Where does this come from?] — Impact: [If wrong by 10%, does outcome change by X%?]
3. [Assumption] — Data source: [Where does this come from?] — Impact: [If wrong by 10%, does outcome change by X%?]

CASH FLOW IMPLICATIONS
[Operating cash flow, working capital needs, capex requirements, funding needs]

MODEL QUALITY & CONFIDENCE
[Data gaps: What would improve model confidence? Sensitivity ranges to model uncertainty]

NEXT STEPS
[What analysis should follow? Business case evaluation? Cost transformation focus?]
═══════════════════════════════════════════
```
