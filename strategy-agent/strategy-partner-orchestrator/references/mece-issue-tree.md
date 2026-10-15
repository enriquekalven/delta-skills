# MECE Issue Tree Reference

Use a **Mutually Exclusive, Collectively Exhaustive (MECE)** issue tree to decompose an ambiguous business or technical problem into falsifiable hypotheses before running analysis.

---

## 1. Three Tree Types

| Tree Type | Core Question | Level-1 (L1) Decomposition Pattern |
| :--- | :--- | :--- |
| **Diagnostic Tree** | *"Why is metric $X$ underperforming by $\Delta$?"* | Mathematical driver breakdown (e.g., $\text{Profit} = \text{Volume} \times \text{Price} - \text{Variable Cost} - \text{Fixed Cost}$) |
| **Solution Tree** | *"How can we achieve target $\Delta Y$ within constraints $C$?"* | Mutually exclusive levers (e.g., Demand reduction vs. Automation deflection vs. Cycle-time compression) |
| **Evaluation Tree** | *"Should we commit capital to Option $A$?"* | Decision gates (Strategic Fit $\land$ Financial NPV/Payback $\land$ Technical Feasibility $\land$ Operational Risk) |

---

## 2. Construction Rules

1. **Quantify Branch Magnitude First:** Attach a dollar, percentage, or latency share to every L1 branch before drilling into L2 so you don't spend 80% of effort on a branch responsible for 5% of the variance.
2. **Keep L1 to 2–4 Branches:** If an L1 has 6+ branches, group them into higher-level drivers.
3. **Write L2 Leaves as Falsifiable Hypotheses:**
   - *Bad (Topic label):* `"Onboarding issues"`
   - *Good (Falsifiable claim):* `"Post-Q2 mid-market cohorts experience >15% 90-day churn due to >14-day data-integration onboarding time."`
4. **Never Mix Diagnosis and Solutions in the Same Tree:** Diagnose root causes first, then build a Solution Tree for the confirmed root cause.

---

## 3. Standard Markdown Template

```markdown
### Issue Tree: [Governing Question]
- **Tree Type:** [Diagnostic | Solution | Evaluation]
- **Baseline Gap:** [e.g., +$18.4M annual cloud run-rate overrun]

1. **L1 Branch A: [Name] (Est. Share: XX% / $XXM) — [PRIORITY]**
   - **Hypothesis A1:** [Falsifiable statement]
     - *Required Evidence / Query:* [Exact table, log, or financial report]
     - *Pass/Fail Threshold:* [Numeric threshold]
   - **Hypothesis A2:** [Falsifiable statement]
     - *Required Evidence / Query:* [Exact source]
     - *Pass/Fail Threshold:* [Numeric threshold]
2. **L1 Branch B: [Name] (Est. Share: XX% / $XXM)**
   - **Hypothesis B1:** [Falsifiable statement]
3. **L1 Branch C: [Name] (Est. Share: XX% / $XXM) — [DEPRIORITIZED]**
   - *Rationale for Deprioritization:* [Why impact is immaterial or out of scope]
```
