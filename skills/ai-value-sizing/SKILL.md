---
name: ai-value-sizing
description: >
  Size AI opportunities (TAM -> SAM -> SOM) and compute risk-adjusted 3-year TCO, ROI %,
  NPV, and payback across Base/Bull/Bear scenarios using scripts/calculate_roi.py, writing
  docs/VALUE_SIZING.md. Trigger when sizing the business value of an AI use case or building
  a Phase 1 projection and a final read-out (weeks 11-12) measured ROI case.
metadata:
  author: leejasony@
  version: '3.2'
---

# AI Value Realization: Sizing & Financials (`ai-value-sizing`)

This skill maps a proposed AI use case to measurable value pillars, narrows the addressable volume (`TAM → SAM → SOM`), applies mandatory Value Capture Rate (`VCR`) and Systemic Capability Discount Factor (`SCDF`) haircuts, and computes a 3-year ROI and NPV schedule in `docs/VALUE_SIZING.md`.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 Projection (Weeks 1–2) & Phase 3 Measured Closeout (Weeks 11–12)** |
| **Reads (Inputs)** | `docs/as_is_report.md`, `docs/USE_CASE_CANVAS.md` (fold token OpEx from `docs/ARCHITECTURE_RECOMMENDATION.md` into `--annual-opex`) |
| **Writes (Outputs)** | `docs/VALUE_SIZING.md` |
| **Value Realization Linkage** | Computes `SOM (Q)`, `3-Year TCO`, `Net Annual Value`, `3-Year ROI %`, `3-Year NPV`, and `Payback Months` across **Base / Bull / Bear** scenarios with explicit `VCR` and `SCDF` haircuts |
| **Primary CLI Command** | `python3 skills/ai-value-sizing/scripts/calculate_roi.py --demo` (or `--markdown` for a ready-to-paste Markdown table) |

---

## Operating Principles & Haircut Matrix

1. **Size Before Math:** Establish the obtainable annual unit volume (`SOM / Q`) before computing dollar savings. Read baseline handling time, unit cost, and annual volume from `docs/as_is_report.md` and `docs/USE_CASE_CANVAS.md`.
2. **Mandatory Haircuts (`VCR` & `SCDF`):** Never equate 1 hour of saved employee time to 1 hour of P&L cash flow (`The 1-to-1 Time Trap`). Always apply both haircuts:

| Haircut Parameter | Tier / Value | When to Apply | Scenario Behavior in `calculate_roi.py` |
| :--- | :---: | :--- | :--- |
| **Value Capture Rate (`VCR`)** | `0.25` (25%) | Task automation where headcount is unchanged and freed time is reallocated | **Base:** user `--vcr` · **Bull:** $\min(1.0, 1.5 \times \text{VCR})$ · **Bear:** user `--vcr` |
| **Value Capture Rate (`VCR`)** | `0.50` (50%) | Revenue-generating or overflow/TPA/overtime-avoidance workflows | Same as above (or weighted blend, e.g., `0.5912`) |
| **Value Capture Rate (`VCR`)** | `1.00` (100%) | Hard vendor contract elimination or hard headcount reduction | Capped at `1.00` in Bull scenario |
| **Systemic Capability Discount (`SCDF`)** | `0.40` / `0.85` / `1.20` | `0.40` low maturity (silos) · `0.85` average enterprise · `1.20` high maturity (CI/CD + MCP primitives) | **Base:** user `--scdf` · **Bull:** $\min(1.2, 1.2 \times \text{SCDF})$ · **Bear:** `0.40` |

3. **Deterministic Math via Script:** Do not estimate ROI/NPV in prose. Run [`scripts/calculate_roi.py`](scripts/calculate_roi.py) and embed the exact numbers and CLI command in `docs/VALUE_SIZING.md`.

---

## Procedure

### Phase 1: Opportunity Sizing Funnel (TAM → SAM → SOM)
1. Map the use case to 1–2 Value Pillars (`Productivity & Efficiency`, `Revenue Generation`, `Risk & Compliance`, `Business Agility`, `Stakeholder Experience`).
2. Quantify the funnel:
   - **TAM:** Total annual universe of transactions/items/tickets (cite internal report or `docs/as_is_report.md`).
   - **SAM:** Serviceable slice after filtering out unsupported channels, geographies, or legacy systems (`SAM = TAM × sam_share`).
   - **SOM (Q):** Realistic Year-1 volume (`SOM = SAM × adoption_rate × tech_compat`, with `adoption_rate <= 0.30` unless contracted).

### Phase 2: 3-Year TCO & Risk-Adjusted ROI
1. Itemize **Year 0 CapEx** (engineering build, integrations, security/eval setup) and **Annual OpEx** (model tokens/compute, storage, maintenance at >=15% of CapEx).
2. Run [`scripts/calculate_roi.py`](scripts/calculate_roi.py):
   ```bash
   # Run with custom engagement parameters (add --markdown for a Markdown table):
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
3. Write `docs/VALUE_SIZING.md` containing the Sizing Funnel, TCO Breakdown, Haircut Justifications, and Base/Bull/Bear Scenario Table.

---

## Scripts & Examples

- [Deterministic ROI & Sizing Calculator](scripts/calculate_roi.py): Zero-dependency Python CLI computing SOM, 3-Year TCO, Net Value, ROI %, NPV, and payback across Base/Bull/Bear scenarios (`--demo` and `--markdown` supported).
- [Worked Example: Commercial Auto Claims Triage Value Sizing](examples/claims-triage-value-sizing.md): Complete `docs/VALUE_SIZING.md` deliverable tied to `docs/as_is_report.md` and verified by `calculate_roi.py`.
