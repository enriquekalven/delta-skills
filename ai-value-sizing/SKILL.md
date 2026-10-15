---
name: ai-value-sizing
description: >
  Size AI opportunities (TAM -> SAM -> SOM) and compute risk-adjusted 3-year TCO, ROI %,
  NPV, and payback across Base/Bull/Bear scenarios using scripts/calculate_roi.py, writing
  docs/VALUE_SIZING.md. Trigger when sizing the business value of an AI use case or building
  a Phase 1 projection and a final read-out (weeks 11-12) measured ROI case.
metadata:
  author: leejasony@
  version: '3.0'
---

# AI Value Realization: Sizing & Financials

This skill maps a proposed AI use case to measurable value pillars, narrows the addressable volume (`TAM → SAM → SOM`), applies mandatory Value Capture Rate (`VCR`) and Systemic Capability Discount Factor (`SCDF`) haircuts, and computes a verified 3-year ROI and NPV schedule in `docs/VALUE_SIZING.md`.

---

## Operating Principles

1. **Size Before Math:** Establish the obtainable annual unit volume (`SOM / Q`) before computing dollar savings. If [synthetic-baseline-protocol](../delivery/synthetic-baseline-protocol/SKILL.md) has been run, read `unit_cost_usd`, `handling_time_minutes`, and `annual_volume_units` directly from `docs/baseline_kpis.json`.
2. **The 1-to-1 Time Trap:** 1 hour of saved employee time does NOT equal 1 hour of P&L cash flow. Always apply a **Value Capture Rate (VCR)**:
   - `0.25` (25%) — Task automation where headcount is unchanged and time is reallocated.
   - `0.50` (50%) — Revenue-generating or overflow-avoidance workflows (sales pipeline, avoided TPA/overtime).
   - `1.00` (100%) — Hard vendor contract elimination or hard headcount reduction.
3. **Engineering Maturity Haircut (SCDF):** Multiply by the **Systemic Capability Discount Factor**:
   - `0.40` — Low maturity (data silos, manual deployments).
   - `0.85` — Average enterprise maturity (standard integration friction).
   - `1.20` — High maturity (automated CI/CD, reusable platform primitives).
4. **Deterministic Math via Script:** Do not estimate ROI/NPV in prose. Run [`scripts/calculate_roi.py`](scripts/calculate_roi.py) and embed the exact numbers and CLI command in `docs/VALUE_SIZING.md`.

---

## Procedure

### Phase 1: Opportunity Sizing Funnel (TAM → SAM → SOM)
1. Map the use case to 1–2 Value Pillars:
   - **Productivity & Efficiency** (cycle time, handling hours)
   - **Revenue Generation** (conversion lift, retention)
   - **Risk & Compliance** (error/rework reduction, fine avoidance)
   - **Business Agility** (throughput scaling without headcount)
   - **Stakeholder Experience** (CSAT, onboarding velocity)
2. Quantify the funnel:
   - **TAM:** Total annual universe of transactions/items/tickets (cite internal report or web source).
   - **SAM:** Serviceable slice after filtering out unsupported channels, geographies, or legacy systems (`SAM = TAM × sam_share`).
   - **SOM (Q):** Realistic Year-1 volume (`SOM = SAM × adoption_rate × tech_compat`, with `adoption_rate <= 0.30` unless contracted).

### Phase 2: 3-Year TCO & Risk-Adjusted ROI
1. Itemize **Year 0 CapEx** (engineering build, integrations, security/eval setup) and **Annual OpEx** (model tokens/compute, storage, maintenance at >=15% of CapEx).
2. Run [`scripts/calculate_roi.py`](scripts/calculate_roi.py):
   ```bash
   python3 ai-value-sizing/scripts/calculate_roi.py \
     --tam-units <TAM> \
     --sam-share <0..1> \
     --adoption-rate <0..0.30> \
     --tech-compat <0..1> \
     --hours-saved <hours_per_unit> \
     --hourly-rate <usd_per_hour> \
     --capex <year0_usd> \
     --annual-opex <annual_usd> \
     --vcr <0.25|0.50|1.00> \
     --scdf <0.40|0.85|1.20> \
     --wacc 0.10
   ```
3. Write `docs/VALUE_SIZING.md` containing the Sizing Funnel, TCO Breakdown, Haircut Justifications, and Base/Bull/Bear Scenario Table.

---

## Quality Checklist

- [ ] Every TAM/SAM figure cites a concrete internal document, `docs/baseline_kpis.json`, or web source.
- [ ] Year-1 `adoption_rate` is `<= 0.30` (or justified by an executive mandate).
- [ ] `VCR` and `SCDF` haircuts are explicitly justified.
- [ ] All table totals match the JSON output of [`scripts/calculate_roi.py`](scripts/calculate_roi.py).

---

## Scripts & Examples

- [Deterministic ROI & Sizing Calculator](scripts/calculate_roi.py): Zero-dependency Python CLI computing SOM, 3-Year TCO, Net Value, ROI %, NPV, and payback across Base/Bull/Bear scenarios.
- [Worked Example: Commercial Auto Claims Triage Value Sizing](examples/claims-triage-value-sizing.md): Complete `docs/VALUE_SIZING.md` deliverable tied to `docs/baseline_kpis.json` and verified by `calculate_roi.py`.
