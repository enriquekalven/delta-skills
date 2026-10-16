# AI Value Realization Case: Commercial Auto Claims Intake & Triage Agent
Date: 2026-08-21 | Baseline Source: `docs/as_is_report.md` (Phase 1 Operational Baseline) | WACC: 10.0%

## 1. Executive Bottom Line
Automating commercial auto First Notice of Loss (FNOL) document extraction and adjuster triage across **12,000 obtainable annual claims (SOM)** requires **$180,000 in Year 0 CapEx** and **$68,000 in annual OpEx ($384,000 3-Year TCO)**, generating **$316,588 in risk-adjusted net annual value** (**Base Case 3-Year ROI: +147.3%**, **3-Year NPV @ 10%: $438,201**, **Payback: 8.7 months**).

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
- **Value Capture Rate (VCR = 59.1% blended):**
  - 50% of saved adjuster capacity converts directly into avoided external TPA (Third-Party Administrator) overflow fees during storm surges + reduced subrogation leakage; remaining time is task productivity.
- **Systemic Capability Discount Factor (SCDF = 0.85):**
  - Standard enterprise maturity (CI/CD and Guidewire APIs exist, 15% friction discount for exception queues).
- **Risk-Adjusted Annual Benefit (Base Case, Pre-OpEx):** `$630,000 × 0.5912 × 0.85 = $316,588 / yr` (`$949,763` over 3 years).
- **Annual Net Cash Flow (Base Case, Post-OpEx):** `$316,588 - $68,000 = $248,588 / yr` (`$565,763` net 3-year benefit after subtracting `$384,000` 3-Year TCO).

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
  --vcr 0.5912 \
  --scdf 0.85 \
  --wacc 0.10
```

| Scenario | VCR | SCDF | Risk-Adj Annual Benefit (Pre-OpEx) | Annual Net Cash Flow (Post-OpEx) | 3-Year Risk-Adj Benefit | 3-Year TCO | 3-Year ROI % | 3-Year NPV @ 10% | Payback |
|---|---|---|---|---|---|---|---|---|---|
| **Base Case (Target)** | 59.1% | 0.85 | **$316,588** | $248,588 | **$949,763** | $384,000 | **+147.3%** | **$438,201** | **8.7 mos** |
| **Bull Case (Full TPA Offload)** | 88.7% | 1.02 | **$569,858** | $501,858 | **$1,709,573** | $384,000 | **+345.2%** | **$1,068,046** | **4.3 mos** |
| **Bear Case (Low Maturity / High Friction)** | 59.1% | 0.40 | **$148,982** | $80,982 | **$446,947** | $384,000 | **+16.4%** | **$21,391** | **26.7 mos** |
