# AI Value Realization Case: Commercial Auto Claims Intake & Triage Agent
Date: 2026-08-21 | Baseline Source: `docs/as_is_report.md` (Phase 1 Operational Baseline) | WACC: 10.0%

## 1. Executive Bottom Line
Automating commercial auto First Notice of Loss (FNOL) document extraction and adjuster triage across **12,000 obtainable annual claims (SOM)** requires **$180,000 in Year 0 CapEx** and **$68,000 in annual OpEx ($384,000 3-Year TCO)**, generating **$321,300 in risk-adjusted annual benefit** (**Base Case 3-Year ROI: +151.0%**, **3-Year NPV @ 10%: $449,920**, **Payback: 8.5 months**).

---

## 2. Phase 1: Opportunity Sizing Funnel (TAM → SAM → SOM)

- **Primary Value Pillar:** Productivity & Efficiency (adjuster handling time reduction from 45.0 mins to 3.0 mins per claim).
- **Secondary Value Pillar:** Risk & Compliance (reduces misrouted severity/subrogation leakage from 14.0% error rate to 2.0%).

| Funnel Stage | Annual Volume (Claims) | Constraint & Calculation Logic | Source / Verification |
|---|---|---|---|
| **TAM (Total Enterprise Claims)** | **80,000 claims / yr** | Total commercial property & casualty claims filed annually across North America & EMEA operations. | FY25 Claims Administration Annual Report |
| **SAM (Serviceable Slice)** | **50,000 claims / yr** (`62.5% of TAM`) | Filters to North American Commercial Auto claims ingested via digital broker portal or PDF email attachments (excludes legacy paper-only international claims). | Guidewire ClaimCenter FY25 channel breakdown |
| **SOM (Year-1 Obtainable Q)** | **12,000 claims / yr** (`24.0% of SAM`) | `SAM (50,000) × Year-1 Pilot Adoption (30.0%) × API/Form Compatibility (80.0%) = 12,000 claims/yr`. | Agreed Phase 1 rollout scope with VP of Claims |

---

## 3. Phase 2: 3-Year TCO & Value Capture Math

### 3.1 Total Cost of Ownership (TCO)
- **Year 0 CapEx ($180,000):**
  - Forward-Deployed Engineering & Document AI / ADK pipeline build: $125,000
  - Guidewire ClaimCenter REST integration & VPC-SC security review: $35,000
  - Golden Dataset curation & 200-claim automated evaluation harness: $20,000
- **Annual Run OpEx ($68,000 / yr):**
  - Vertex AI (`gemini-3` + Document AI OCR) + Agent Runtime compute ($0.75/claim × 12,000 claims): $9,000/yr
  - Cloud Logging, BigQuery audit storage, and monitoring: $12,000/yr
  - Ongoing MLOps maintenance & prompt drift evaluation (15% of CapEx + 0.2 FTE): $47,000/yr
- **Total 3-Year TCO:** `$180,000 + (3 × $68,000) = $384,000`

### 3.2 Gross-to-Net Value Haircuts
- **Baseline Time Saved per Claim:** `45.0 mins (baseline) - 3.0 mins (HITL review) = 42.0 mins (0.70 hours) saved/claim` (from `docs/as_is_report.md`).
- **Blended Adjuster Hourly Rate:** `$75.00 / hr` (fully loaded).
- **Gross Annual Labor Value:** `12,000 claims × 0.70 hrs × $75.00/hr = $630,000 / yr`.
- **Productivity Capture Rate (`--capture-rate = 0.60` / 60%):**
  - Saved adjuster capacity during storm surges converts into avoided external TPA (Third-Party Administrator) overflow fees + reduced subrogation leakage; remaining time is task productivity.
- **Delivery Readiness Factor (`--delivery-factor = 0.85`):**
  - Standard enterprise maturity (CI/CD and Guidewire APIs exist, 15% friction discount for exception queues).
- **Risk-Adjusted Annual Benefit (Base Case, Pre-OpEx):** `$630,000 × 0.60 × 0.85 = $321,300 / yr` (`$963,900` over 3 years).
- **Annual Net Cash Flow (Base Case, Post-OpEx):** `$321,300 - $68,000 = $253,300 / yr` (`$579,900` net 3-year benefit after subtracting `$384,000` 3-Year TCO).

---

## 4. Reproducible Calculator Command & Scenario Table

Verified with [`scripts/calculate_roi.py`](../scripts/calculate_roi.py):

```bash
python3 skills/ai-value-sizing/scripts/calculate_roi.py \
  --tam-units 80000 \
  --sam-share 0.625 \
  --adoption-rate 0.30 \
  --tech-compat 0.80 \
  --hours-saved 0.70 \
  --hourly-rate 75.0 \
  --capex 180000 \
  --annual-opex 68000 \
  --capture-rate 0.60 \
  --delivery-factor 0.85 \
  --wacc 0.10
```

| Scenario | Capture Rate | Delivery Factor | Risk-Adj Annual Benefit (Pre-OpEx) | Annual Net Cash Flow (Post-OpEx) | 3-Year Risk-Adj Benefit | 3-Year TCO | 3-Year ROI % | 3-Year NPV @ 10% | Payback |
|---|---|---|---|---|---|---|---|---|---|
| **Base Case (Target)** | 60.0% | 0.85 | **$321,300** | $253,300 | **$963,900** | $384,000 | **+151.0%** | **$449,920** | **8.5 mos** |
| **Bull Case (Full TPA Offload)** | 90.0% | 1.02 | **$578,340** | $510,340 | **$1,735,020** | $384,000 | **+351.8%** | **$1,089,140** | **4.2 mos** |
| **Bear Case (Low Maturity / High Friction)** | 60.0% | 0.40 | **$151,200** | $83,200 | **$453,600** | $384,000 | **+18.1%** | **$26,906** | **26.0 mos** |
