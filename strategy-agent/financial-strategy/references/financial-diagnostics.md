# Financial Health Diagnostic

The goal of this phase is to assess the overall financial health of the business across four dimensions: P&L structure and margin architecture, cash flow generation and conversion, balance sheet strength and capital structure, and financial performance benchmarks against industry peers.

This is where you answer: "How healthy is this business? Where are the financial weaknesses? What are the early warning signs?"

---

## 1. P&L Waterfall & Margin Structure

Start with a clear P&L, then decompose each margin layer to find where value is created and destroyed.

### Step 1: Assemble the P&L

Request or build a clean P&L for the trailing 12 months (preferably monthly) and the prior year:

```
P&L STRUCTURE (TTM)
═══════════════════════════════════════════
Revenue                          $XXM      100%
  Cost of Goods Sold            ($XXM)     (X%)
  ───────────────────────────────────────
Gross Profit                      $XXM      X%

Operating Expenses:
  Sales & Marketing              ($XXM)     (X%)
  Research & Development         ($XXM)     (X%)
  General & Administrative       ($XXM)     (X%)
  ───────────────────────────────────────
Operating Income (EBITDA)        $XXM      X%

Interest, Taxes, Depreciation    ($XXM)     (X%)
  ───────────────────────────────────────
Net Income                        $XXM      X%
```

Note: The exact P&L structure varies by industry (SaaS has different buckets than manufacturing, which differs from retail). Adjust the template to match how management reports it.

### Step 2: Margin Waterfall

Calculate margins at every level and track year-over-year changes:

```
MARGIN WATERFALL (YoY Change)
═══════════════════════════════════════════
Gross Margin
  Prior Year:                    X%
  Current Year:                  X%
  Change:                        ±X bps
  Drivers: [COGS inflation / volume / mix / pricing]

Operating Margin (Excluding D&A)
  Prior Year:                    X%
  Current Year:                  X%
  Change:                        ±X bps
  Drivers: [Sales efficiency / OpEx leverage / headcount growth]

Operating Margin (Including D&A)
  Prior Year:                    X%
  Current Year:                  X%
  Change:                        ±X bps
  Drivers: [Capex intensity / amortization schedule / D&A acceleration]

Net Margin
  Prior Year:                    X%
  Current Year:                  X%
  Change:                        ±X bps
  Drivers: [Tax rate / interest burden / other items]
```

For each margin layer, identify:
- **Is it expanding or contracting?** If contracting, why? If expanding, is it sustainable?
- **How does it compare to prior year and budget?** What's the variance?
- **What's driving the change?** Revenue mix? Cost inflation? Operating leverage? New product launch? Market share loss?

### Step 3: Segment Margin Analysis (If Multi-Segment)

If the company operates multiple business units, segments, geographies, or product lines, break margin by segment:

```
SEGMENT MARGIN BRIDGE
═══════════════════════════════════════════
                   Revenue    Gross M%   Op M%   Contribution
Segment A          $XXM       X%         X%      $XXM
Segment B          $XXM       X%         X%      $XXM
Segment C          $XXM       X%         X%      $XXM
Corporate Overhead  —          —         (X%)    ($XXM)
Total              $XXM       X%         X%      $XXM
```

Key questions:
- Which segments are most profitable? Least?
- Do lower-margin segments have other strategic value (market entry, customer breadth)?
- Is there cross-subsidy (high-margin segment subsidizing low-margin but strategic segment)?
- Are segment margins trending in same or different directions?

---

## 2. Cash Conversion Cycle & Working Capital Health

Profit on the income statement doesn't equal cash. A business can be profitable and insolvent if working capital is mismanaged.

### Step 1: Calculate Cash Conversion Cycle (CCC)

```
CASH CONVERSION CYCLE
═══════════════════════════════════════════
Days Inventory Outstanding (DIO)
  = [Ending Inventory / COGS] × 365
  = X days
  Industry benchmark: X days
  Trend: [Improving / Stable / Deteriorating]

Days Sales Outstanding (DSO)
  = [Ending Accounts Receivable / Revenue] × 365
  = X days
  Industry benchmark: X days
  Trend: [Improving / Stable / Deteriorating]

Days Payable Outstanding (DPO)
  = [Ending Accounts Payable / COGS] × 365
  = X days
  Industry benchmark: X days
  Trend: [Improving / Stable / Deteriorating]

Cash Conversion Cycle = DIO + DSO – DPO
  = X + X – X = X days
  Industry benchmark: X days
  Trend: [Improving / Stable / Deteriorating]
```

Interpretation:
- **CCC < 0:** Business collects cash before it pays suppliers. Ideal. (Example: Retail, SaaS)
- **CCC 0-30:** Minimal working capital drag.
- **CCC 30-90:** Moderate; typically requires some working capital financing.
- **CCC > 90:** High; indicates potential cash stress, especially in growth phase.

### Step 2: Working Capital Analysis

```
WORKING CAPITAL EFFICIENCY
═══════════════════════════════════════════
Accounts Receivable
  Trailing 12M (TTM):            $XXM
  As % of Revenue:               X%
  Days Sales Outstanding (DSO):  X days
  Aging: [% current, % 30+ days, % 60+ days, % 90+ days]
  Trend:                         [Improving / Stable / Deteriorating]

Inventory
  TTM:                           $XXM
  As % of COGS:                  X%
  Days Inventory Outstanding:    X days
  Turnover ratio:                X× per year
  Trend:                         [Improving / Stable / Deteriorating]
  Quality:                       [Is obsolescence a risk? Markdown risk?]

Accounts Payable
  TTM:                           $XXM
  As % of COGS:                  X%
  Days Payable Outstanding:      X days
  Trend:                         [Improving / Stable / Deteriorating]
  Vendor concentration:          [Are we over-dependent on extending payment terms?]
```

Key questions:
- **Is DSO increasing?** Potential collection problem or customers negotiating longer terms?
- **Is inventory growing faster than revenue?** Potential obsolescence or poor demand forecasting?
- **Is DPO decreasing?** Vendor terms tightening, indicating they perceive risk?
- **Is CCC deteriorating?** If so, how much additional working capital is this consuming?

### Step 3: Operating Cash Flow vs. Net Income

```
OPERATING CASH FLOW BRIDGE
═══════════════════════════════════════════
Net Income (Accrual)             $XXM
Adjustments for non-cash:
  Depreciation & Amortization    +$XXM
  Stock-based compensation       +$XXM
  Deferred revenue (SaaS)        +/$XXM
  Deferred taxes                 +/$XXM
Changes in working capital:
  Increase in AR (use of cash)   ($XXM)
  Increase in Inventory (use)    ($XXM)
  Increase in AP (source)        +$XXM
  Other                          +/$XXM
  ───────────────────────────────────────
Operating Cash Flow              $XXM
FCF Conversion:                  [OCF / NI] = X%
```

Key insight: If OCF < NI, working capital is a drag. If OCF >> NI (common in SaaS with deferred revenue), that's a cash generation advantage.

---

## 3. Balance Sheet Strength & Capital Structure

### Step 1: Financial Position Scorecard

```
FINANCIAL POSITION SCORECARD
═══════════════════════════════════════════

LIQUIDITY (Can we pay short-term obligations?)
  Current Ratio:                 X.X (Industry: X.X) — [✓ Healthy / ⚠ Monitor / ✗ Concerning]
  Quick Ratio:                   X.X (Industry: X.X) — [✓ Healthy / ⚠ Monitor / ✗ Concerning]
  Cash on hand:                  $XXM (Monthly OpEx: $XXM) — [✓ > 6 months / ⚠ 3-6 months / ✗ < 3 months]
  Cash burn rate:                ($XXM/month) or [Positive / Neutral]

SOLVENCY (Can we pay long-term obligations?)
  Debt-to-Equity Ratio:          X.X (Industry: X.X) — [✓ Safe / ⚠ Moderate / ✗ High]
  Net Debt / EBITDA:             X.X (Industry: X.X; Covenant: X.X) — [✓ Below covenant / ⚠ Approaching / ✗ Breached]
  Interest Coverage:             X.X× (Covenant: X.X×) — [✓ Safe / ⚠ Tight / ✗ Below covenant]
  Debt Maturity Profile:         [When does debt come due? Any refinancing risk?]

PROFITABILITY
  Return on Assets (ROA):        X% — [Improving / Stable / Declining]
  Return on Equity (ROE):        X% — [Improving / Stable / Declining]
  ROIC:                          X% — [Company creating value if > Cost of Capital]

CAPITAL STRUCTURE HEALTH
  Equity Financing Available:    [Yes / Limited / None]
  Debt Capacity (est.):          [Additional $XXM available / No capacity / Restricted]
  Dividend/Share buyback:        [$XXM annually / None planned]
```

### Step 2: Covenant Analysis (If Debt Exists)

If the company has bank debt or bonds, extract the covenant package:

```
DEBT COVENANTS (if applicable)
═══════════════════════════════════════════
Financial Covenants:
  Leverage Ratio (Net Debt / EBITDA)
    Maximum Allowed:             X.X×
    Current:                     X.X×
    Headroom:                    X.X×
    Status:                      [✓ Safe / ⚠ Tight / ✗ Breach risk]

  Interest Coverage (EBITDA / Interest)
    Minimum Required:            X.X×
    Current:                     X.X×
    Headroom:                    X.X×
    Status:                      [✓ Safe / ⚠ Tight / ✗ Breach risk]

  Minimum Liquidity
    Required:                    $XXM
    Current:                     $XXM
    Status:                      [✓ Safe / ⚠ Tight / ✗ Breach risk]

Operational Covenants:
  - Can we incur additional debt without lender approval? [Yes / No / Limited]
  - Can we make acquisitions? [Yes / No / Limited]
  - Can we pay dividends? [Yes / No / Limited]
  - Are there asset sale restrictions? [Yes / No]

Covenant Sensitivity:
  - If EBITDA declines X%, do we breach leverage? [Yes / No / Maybe]
  - If revenue declines Y%, do we breach coverage? [Yes / No / Maybe]
```

---

## 4. Financial Benchmarking & Industry Context

### Step 1: Industry Benchmarking

Compare key metrics to industry peers and historical norms:

```
FINANCIAL BENCHMARKING
═══════════════════════════════════════════

Gross Margin
  Company:                       X%
  Industry Median:               X%
  Top Quartile:                  X%
  Assessment:                    [✓ Competitive / ⚠ Below peer avg / ✗ Significant gap]

Operating Margin
  Company:                       X%
  Industry Median:               X%
  Top Quartile:                  X%
  Assessment:                    [✓ Competitive / ⚠ Below peer avg / ✗ Significant gap]

Net Margin
  Company:                       X%
  Industry Median:               X%
  Top Quartile:                  X%
  Assessment:                    [✓ Competitive / ⚠ Below peer avg / ✗ Significant gap]

Return on Invested Capital
  Company:                       X%
  Industry Median:               X%
  Top Quartile:                  X%
  Assessment:                    [✓ Value creation / ⚠ Meeting cost of capital / ✗ Value destruction]

Debt-to-Equity
  Company:                       X.X
  Industry Median:               X.X
  Safe Range for Industry:       X.X – X.X
  Assessment:                    [✓ Moderate leverage / ⚠ Above average / ✗ High risk]

Cash Conversion Cycle
  Company:                       X days
  Industry Median:               X days
  Best in class:                 X days
  Assessment:                    [✓ Better than average / ⚠ In-line / ✗ Worse than peers]
```

Questions to answer:
- Where is the company outperforming peers? Can this advantage be sustained?
- Where is the company underperforming? Is this a competitive weakness or a strategic choice?
- Are industry benchmarks stable or changing? (Margin compression across the industry vs. company-specific issue?)

### Step 2: Trend Analysis (Last 3-5 Years)

Track key metrics over time to identify inflection points:

```
5-YEAR TREND ANALYSIS
═══════════════════════════════════════════
                    Y-5    Y-4    Y-3    Y-2    Y-1    YTD
Revenue ($M)        XXX    XXX    XXX    XXX    XXX    XXX
Growth %            X%     X%     X%     X%     X%     X%
Gross Margin %      X%     X%     X%     X%     X%     X%
OpEx as % Rev       X%     X%     X%     X%     X%     X%
Operating Margin    X%     X%     X%     X%     X%     X%
FCF ($M)            XXX    XXX    XXX    XXX    XXX    XXX
Headcount           XXX    XXX    XXX    XXX    XXX    XXX
```

Interpretation:
- **Is growth accelerating or decelerating?** If decelerating, why?
- **Are margins expanding or contracting?** Consistent with industry trends or company-specific?
- **Is FCF improving or deteriorating?** Is growth consuming or generating cash?
- **Is headcount growth aligned with revenue growth?** (Revenue per employee metric)

---

## 5. Early Warning Indicators

These are red flags that typically precede financial distress or strategic inflection points:

### Red Flags

**P&L Red Flags:**
- Gross margin declining while competitors maintain or expand theirs (pricing power loss or COGS inflation unaddressed)
- Opex as % of revenue increasing despite scale (lack of operational leverage)
- Working capital metrics deteriorating (AR aging, inventory buildup, tighter payment terms)
- Revenue deceleration without apparent external cause (product/market fit issues?)

**Cash Flow Red Flags:**
- Operating cash flow declining while net income looks stable (earnings quality issue)
- Days inventory outstanding increasing (potential obsolescence or demand forecast error)
- Days sales outstanding increasing (customer credit quality issue or collection problem)
- Increasing reliance on debt to fund operations (not sustainable)

**Balance Sheet Red Flags:**
- Cash balance declining despite positive net income (misalignment of accrual and cash)
- Debt covenants tightening or approaching breach (lender confidence declining)
- Short-term debt increasing relative to long-term (refinancing risk growing)
- Asset write-downs or restructuring charges (quality of earnings issue)

**Valuation Red Flags:**
- ROIC declining below cost of capital (value destruction despite top-line growth)
- Capital expenditures increasing without corresponding revenue lift (investment not generating returns)
- Customer concentration increasing (single customer becoming >25% of revenue = risk)
- Acquisition multiples on company declining (external view of value deteriorating)

### Green Flags

- Operating leverage emerging (margins expanding as revenue grows and fixed costs absorb)
- Cash conversion improving (CCC decreasing or FCF as % of net income increasing)
- Debt paydown ahead of schedule (confidence in cash generation)
- ROIC expanding above cost of capital (value creation accelerating)
- Customer cohort metrics improving (CAC declining, LTV expanding, retention rate improving)

---

## Output Template

```
FINANCIAL HEALTH DIAGNOSTIC
═══════════════════════════════════════════

BOTTOM LINE UP FRONT
[One-sentence assessment of financial health and primary concern]

P&L STRUCTURE & MARGIN ANALYSIS
[P&L waterfall, margin trends, segment analysis if relevant]

CASH FLOW ASSESSMENT
[CCC analysis, working capital health, operating cash flow quality]

BALANCE SHEET STRENGTH
[Liquidity, solvency, capital structure, covenant headroom]

FINANCIAL BENCHMARKING
[Industry comparison, historical trends, competitive positioning]

EARLY WARNING INDICATORS
[Red flags present / Green flags present / Overall trajectory]

KEY FINDINGS
1. [Finding] — Confidence: [H/M/L] — Impact: [What this means]
2. [Finding] — Confidence: [H/M/L] — Impact: [What this means]
3. [Finding] — Confidence: [H/M/L] — Impact: [What this means]

FINANCIAL HEALTH SCORE
Overall health rating: [Excellent / Good / Adequate / At-risk / In crisis]
Primary concern: [What needs attention most urgently?]
Secondary concerns: [What to monitor?]

NEXT STEPS
[What analysis should follow from here?]
═══════════════════════════════════════════
```
