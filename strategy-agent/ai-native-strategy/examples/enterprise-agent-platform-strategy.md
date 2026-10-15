# AI Strategy & Architecture Brief: Commercial Property Underwriting Co-Pilot & Triage Engine
Date: 2026-08-18 | Classification: Hybrid (AI-Enhanced Underwriter Workbench → AI-Native Straight-Through Renewals)

## 1. Strategic Positioning & Defensibility Scorecard

**Executive Summary:** Deploying a generic PDF-chat wrapper over broker submissions provides zero competitive moat. Defensibility comes from combining proprietary 12-year loss-run history in BigQuery with automated ACORD/SOV (Statement of Values) reconciliation and direct write-back into Guidewire PolicyCenter.

| Moat Dimension | Score (1-5) | Evidence / Mechanism |
|---|---|---|
| **Proprietary Data Loop** | **4.5 / 5** | 12 years of closed-claim loss ratios linked to property geocodes and underwriter override notes stored in BigQuery (`underwriting_gold.loss_history`). |
| **Workflow Integration Depth** | **4.0 / 5** | Direct read/write integration with Guidewire PolicyCenter, spatial hazard APIs, and broker intake inbox; replaces 4 manual spreadsheet reconciliations. |
| **Switching Costs** | **4.0 / 5** | Every underwriter override logs structured rationale back into the evaluation dataset, compounding calibration accuracy quarter over quarter. |
| **Unit Cost Advantage** | **3.5 / 5** | 75/25 model routing split reduces per-submission inference cost from $1.84 (all-frontier) to $0.38 per submission. |

---

## 2. Build vs. Buy vs. Partner Matrix

| Capability | Decision | Rationale | Target Stack / Vendor |
|---|---|---|---|
| **Enterprise Employee Search (HR/IT Policy Q&A)** | **Buy** | Commodity capability with zero underwriting differentiation; deploy in <2 weeks. | Gemini Enterprise (No-Code Connectors for Drive/Confluence) |
| **Geospatial Catastrophe & Flood Hazard Scoring** | **Partner** | Regulatory-certified catastrophe models require decades of actuarial filings that cannot be replicated in-house. | CoreLogic / Verisk API via Apigee |
| **SOV Normalization & Loss-Run Extraction Pipeline** | **Build** | Broker schedules arrive in 40+ non-standard Excel/PDF layouts; custom Document AI + Gemini validation rules tie directly to internal coverage codes. | Google Cloud Document AI + Vertex AI (`gemini-3`) |
| **Underwriting Risk Synthesis & Appetite Matching Agent** | **Build** | Core IP: evaluates extracted exposures against proprietary underwriting guidelines and historical loss ratios. | Google ADK on Vertex AI Agent Runtime + `claude-opus-4.6` |

---

## 3. Model Routing & Unit Economics

**Workload Basis:** 25,000 commercial broker submissions/month. Average submission packet = 45 pages (~60K input tokens, 4K output tokens across pipeline stages).Rates sourced from [`model-economics-config.json`](../references/model-economics-config.json).

| Task Tier | Share of Token Volume | Model | Avg Input / Output Tokens per Submission | Cost per Submission | Monthly Cost @ 25,000 Submissions |
|---|---|---|---|---|---|
| **Tier 1: Document Classification & Table Extraction** | 75% | `gemini-3` ($2.50 / $10.00 per 1M) | 45,000 in / 3,000 out | $0.1425 | $3,562.50 |
| **Tier 2: Complex Endorsement & Actuarial Risk Synthesis** | 25% | `claude-opus-4.6` ($5.00 / $25.00 per 1M) | 15,000 in / 1,000 out | $0.1000 | $2,500.00 |
| **Document AI OCR & BigQuery Vector Search** | — | Managed GCP Services | 45 pages / 8 queries | $0.1350 | $3,375.00 |
| **Total Blended Unit Economics** | **100%** | **Routed Multi-Model** | **60,000 in / 4,000 out** | **$0.3775** | **$9,437.50 / mo ($113.25K / yr)** |

*Margin Impact:* At $0.38 inference cost per submission vs. $56.25 manual triage baseline cost (45 mins @ $75/hr), gross unit cost per triaged submission drops by **99.3%** on automated steps.

---

## 4. Agentic Orchestration & Governance Gates

- **Orchestration Pattern:** **Sequential Pipeline with Supervisor Gate** (3 ADK sub-agents):
  1. `IngestionAgent`: Extracts ACORD forms, SOV tables, and 5-year loss runs; validates column totals (`sum(building_tiv) == declared_total_tiv`).
  2. `HazardEnrichmentAgent`: Calls Verisk/CoreLogic APIs and queries BigQuery historical loss ratios for matching occupancy codes.
  3. `AppetiteSynthesisAgent`: Generates the structured Underwriting Deal Memo with cite-linked page anchors.
- **Human-in-the-Loop (HITL) Escalation Rules:**
  - **L3 Straight-Through Quote Draft:** Only allowed for renewals with Total Insured Value (TIV) < $5M, zero claims in 36 months, and extraction confidence = 100% arithmetic match.
  - **L2 Mandatory Senior Underwriter Sign-Off:** All new business submissions, any submission with TIV >= $5M, or any discrepancy between declared TIV and summed SOV rows.
- **Compliance & Security Controls:**
  - All broker documents and model invocations remain inside the `prod-uw-vpc-sc` VPC Service Controls perimeter using CMEK encryption.
  - Cloud DLP strips applicant SSNs and bank routing numbers prior to model context assembly.
  - Every generated Underwriting Memo logs prompt hash, model version, source PDF byte offsets, and underwriter approve/edit diff to BigQuery (`uw_audit.agent_decisions`) for state insurance department market-conduct audits.
