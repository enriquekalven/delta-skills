# Financial Health Diagnostic Reference

Use this reference to diagnose P&L margin bridges, cash conversion cycles, and balance-sheet constraints when authoring `docs/FINANCIAL_STRATEGY.md`.

---

## 1. P&L & Margin Waterfall Template

| Line Item | Prior Period ($M / % Rev) | Current Period ($M / % Rev) | YoY Change (bps) | Primary Variance Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Revenue** | `$XXM (100.0%)` | `$XXM (100.0%)` | `—` | Volume, price realization, segment mix |
| **COGS (Hosting, Inference, Support)** | `($XXM) (XX.X%)` | `($XXM) (XX.X%)` | `±XX bps` | Token/compute cost per unit, support headcount |
| **Gross Profit & Gross Margin %** | `$XXM (XX.X%)` | `$XXM (XX.X%)` | `±XX bps` | Target $\ge 70\%$ for B2B SaaS |
| **Sales & Marketing (S&M)** | `($XXM) (XX.X%)` | `($XXM) (XX.X%)` | `±XX bps` | CAC efficiency, sales cycle length |
| **Research & Development (R&D)** | `($XXM) (XX.X%)` | `($XXM) (XX.X%)` | `±XX bps` | Engineering headcount, capitalized software |
| **General & Administrative (G&A)** | `($XXM) (XX.X%)` | `($XXM) (XX.X%)` | `±XX bps` | Legal, compliance, corporate overhead |
| **Operating Income (EBIT / EBITDA)** | `$XXM (XX.X%)` | `$XXM (XX.X%)` | `±XX bps` | Operating leverage |
| **Free Cash Flow (FCF)** | `$XXM (XX.X%)` | `$XXM (XX.X%)` | `±XX bps` | Working capital & CapEx intensity |

---

## 2. Cash Conversion Cycle (CCC) & Working Capital Formulas

$$\text{DIO} = \left(\frac{\text{Ending Inventory}}{\text{Annual COGS}}\right) \times 365, \quad \text{DSO} = \left(\frac{\text{Ending AR}}{\text{Annual Revenue}}\right) \times 365, \quad \text{DPO} = \left(\frac{\text{Ending AP}}{\text{Annual COGS}}\right) \times 365$$

$$\text{Cash Conversion Cycle (Days)} = \text{DIO} + \text{DSO} - \text{DPO}$$

- **Cash Released per Day of DSO Reduction:** $\frac{\text{Annual Revenue}}{365}$
- **Warning Triggers:**
  - $\text{DSO}$ expanding $> 5\text{ days}$ YoY indicates enterprise collection friction or extended payment terms.
  - $\text{OCF} < \text{Net Income}$ over 2+ consecutive quarters signals working-capital absorption or aggressive revenue recognition.

---

## 3. Liquidity & Covenant Headroom Checklist

| Metric | Formula | Healthy Benchmark | Red Flag Trigger |
| :--- | :--- | :--- | :--- |
| **Runway (Months)** | $\text{Cash \& Equivalents} / \text{Monthly Net Burn}$ | $\ge 18\text{ months}$ | $< 9\text{ months}$ |
| **Net Debt / EBITDA** | $(\text{Total Debt} - \text{Cash}) / \text{LTM EBITDA}$ | $< 2.5\times$ | Within $0.5\times$ of debt covenant ceiling |
| **Interest Coverage** | $\text{LTM EBIT} / \text{Annual Interest Expense}$ | $> 4.0\times$ | $< 2.0\times$ |
| **ROIC vs. WACC Spread** | $\text{NOPAT} / \text{Invested Capital} - \text{WACC}$ | $> +300\text{ bps}$ | Negative spread (growth destroys capital) |
