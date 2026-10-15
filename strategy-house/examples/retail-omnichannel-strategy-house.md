# Strategy House & Opportunity Matrix: OmniRetail Corp (FY25–FY26)
Date: 2026-08-20 | Evidence Base: FY24–FY25 Form 10-K, Q1'25–Q4'26 Form 10-Q & Earnings Transcripts

## 1. Vision (The Roof)
OmniRetail Corp will transform from a store-centric specialty retailer pressured by inventory markdowns and rising fulfillment split-shipments into an AI-orchestrated omnichannel commerce platform that delivers sub-24-hour localized fulfillment while expanding operating margin by 280 bps to 14.5% by FY28.

---

## 2. Strategy & Business Focus Areas (The Pillars)

| Focus Area (Pillar) | Cited Financial Problem (8-Quarter Filing Evidence) | Target Outcome | From → To Shift |
|---|---|---|---|
| **1. Predictive Inventory & Markdown Optimization** | Gross margin contracted 190 bps over 8 quarters (Q1'25–Q4'26 10-K Item 7) due to $142M in seasonal clearance markdowns and regional stockouts. | Cut clearance markdown rate by 30% (+110 bps gross margin lift, +$42.6M/yr). | **From:** Static 16-week spreadsheet allocation by merchant buyers.<br>**To:** Daily SKU-store demand sensing on BigQuery + Vertex AI Forecast. |
| **2. Intelligent Order Routing & Split-Shipment Reduction** | Split-shipment rate reached 24.8% of e-commerce orders in FY25 (Q4'26 Earnings Call), adding $6.40 incremental parcel cost per split order ($38.4M annual drag). | Reduce split-shipment rate from 24.8% to <12.0% ($19.8M annual freight savings). | **From:** Rules-based OMS routing to nearest node with partial stock.<br>**To:** Real-time margin-aware fulfillment optimization balancing shipping cost vs. store markdown risk. |
| **3. Autonomous Customer Care & Returns Triage** | Post-purchase contact rate is 18.2% of digital orders ($8.90 cost/contact across 6.2M annual contacts = $55.2M SG&A, FY25 10-K). | Deflect 55% of Tier-1 WISMO/returns inquiries and reduce average cost/contact to $3.60 ($29.4M annual SG&A savings). | **From:** Manual BPO ticket handling across 4 disconnected carrier portals.<br>**To:** ADK Customer Resolution Agent with direct OMS/carrier API write actions. |
| **4. Associate Merchandising & Catalog Velocity** | Onboarding new vendor SKUs requires 14 days of manual attribute tagging and copywriting, delaying seasonal digital drops (Q2'26 10-Q). | Compress SKU onboarding lead time from 14 days to <24 hours; lift organic search conversion +45 bps. | **From:** Manual vendor spreadsheet cleanup and copy drafting.<br>**To:** Multimodal Gemini attribute extraction and automated taxonomy validation. |

---

## 3. Prioritization & Opportunity Matrix (The Phases)

| Phase | Use Case ID & Name | Pillar | Business Value (1-5) | Tech Feasibility (1-5) | Est. Annual Impact ($M) | Primary GCP Stack |
|---|---|---|---|---|---|---|
| **Phase 1: Stabilization (Mos 1–4)** | **UC-1.1:** Unified Inventory & Order Telemetry Lakehouse | Pillars 1, 2 | 4.5 | 4.5 | Enables Phase 2–3 | BigQuery, Datastream, Pub/Sub |
| **Phase 1: Stabilization (Mos 1–4)** | **UC-1.2:** Multimodal Vendor Catalog Enrichment Pipeline | Pillar 4 | 3.5 | 5.0 | $6.8M | Vertex AI (`gemini-3`), Cloud Run |
| **Phase 1: Stabilization (Mos 1–4)** | **UC-1.3:** Tier-1 WISMO & Return-Label Self-Service Agent | Pillar 3 | 4.5 | 4.5 | $16.2M | Google ADK, Vertex AI Agent Runtime |
| **Phase 2: Optimization (Mos 5–8)** | **UC-2.1:** Store-SKU Demand Sensing & Rebalancing Copilot | Pillar 1 | 5.0 | 4.0 | $24.0M | BigQuery ML, Vertex AI Forecast |
| **Phase 2: Optimization (Mos 5–8)** | **UC-2.2:** Margin-Aware OMS Split-Shipment Optimizer | Pillar 2 | 4.5 | 3.5 | $19.8M | Cloud Run, OR-Tools, BigQuery |
| **Phase 2: Optimization (Mos 5–8)** | **UC-2.3:** Fraudulent Return & Wardrobing Detection Engine | Pillar 3 | 4.0 | 4.0 | $13.2M | Vertex AI Feature Store, BigQuery |
| **Phase 3: Transformation (Mos 9–12)** | **UC-3.1:** Autonomous Dynamic Markdown & Promotional Pricing Agent | Pillar 1 | 5.0 | 3.5 | $18.6M | Google ADK, BigQuery, Price Engine API |
| **Phase 3: Transformation (Mos 9–12)** | **UC-3.2:** Proactive Carrier Delay Intervention & Re-shipment Agent | Pillars 2, 3 | 4.0 | 4.0 | $8.4M | Pub/Sub, Google ADK, OMS API |
| **Phase 3: Transformation (Mos 9–12)** | **UC-3.3:** Conversational Stylist & Cross-Category Bundle Agent | Pillar 4 | 4.0 | 3.5 | $14.5M | Vertex AI Search for Commerce, ADK |

---

## 4. Measure Success (OKRs & KPIs)

- **Objective 1 (Phase 1 — Customer Care & Catalog Foundation):** Eliminate manual toil in post-purchase support and vendor catalog onboarding.
  - **KR 1.1:** Reduce post-purchase cost per contact from **$8.90 → $4.80** within 120 days of UC-1.3 launch.
  - **KR 1.2:** Compress new vendor SKU time-to-site from **14.0 days → 1.0 day** with >=98% attribute completeness.
- **Objective 2 (Phase 2 — Fulfillment & Inventory Margin Recovery):** Stop margin leakage from split shipments and regional inventory imbalances.
  - **KR 2.1:** Reduce e-commerce split-shipment rate from **24.8% → 11.8%** across top 150 fulfillment stores by end of Month 8.
  - **KR 2.2:** Improve in-season sell-through at full price from **64.2% → 71.5%** across top 5 apparel categories.
- **Objective 3 (Phase 3 — Autonomous Margin Expansion):** Achieve sustainable SG&A leverage and gross margin expansion across the omnichannel fleet.
  - **KR 3.1:** Reduce annual clearance markdown expense from **$142M → $99M** (-30.3%) by end of Month 12.
  - **KR 3.2:** Expand consolidated GAAP Operating Margin from **11.7% → 14.5%** (+280 bps).

---

## 5. Impacted Teams

- **Merchandising & Inventory Planning — Operational Change & Resource Requirement:** Transition 45 allocation analysts from manual weekly Excel transfers to exception-based review of daily AI rebalancing recommendations; requires 2-week training program and updated open-to-buy approval thresholds.
- **Supply Chain & Store Fulfillment Operations — Operational Change & Resource Requirement:** Embed margin-aware routing scores into Manhattan OMS pick-wave logic across 420 retail stores and 4 distribution centers; requires 2 Supply Chain Engineers and updated store labor KPIs.
- **Customer Experience & Digital Operations — Operational Change & Resource Requirement:** Restructure 180-seat BPO support queue around L3 autonomous WISMO/returns resolution and L2 complex exception handling; requires 1 CX Automation Product Owner and Golden Evaluation Set governance.
- **Enterprise Data & Platform Engineering — Operational Change & Resource Requirement:** Establish streaming CDC from OMS/ERP into BigQuery and govern Vertex AI Agent Runtime deployment within VPC Service Controls; requires 3 Platform Engineers and 2 Forward-Deployed AI Engineers.
