# Workshop Discovery & Intake Brief: Acme Property & Casualty Insurance
Date: 2026-08-12 | Status: Confirmed | Engagement Track: 12-Week Delta Engagement (Phase 1 Kickoff)

---

## 1. Customer, Sponsorship & Pod Breakout Structure
- **Customer Name & Segment:** Acme P&C Insurance ($4.2B Gross Written Premium, North America Commercial Lines)
- **Executive Sponsor:** Dana Morales, SVP & Head of Commercial Claims Operations (Gate 1–4 budget & scope authority)
- **Primary Customer POC:** Victor Chen, Director of Claims Technology & Guidewire Platform
- **Customer Participants (11 total):**
  - Business / Operations SMEs: 2 Regional Claims Managers, 2 Senior Commercial Auto Adjusters
  - Engineering / Data Platform: Director of Claims Tech, Lead Guidewire Integration Architect, Senior BigQuery Data Engineer
  - Security / Risk / Legal: Principal Cloud Security Architect (CISO Office), VP Claims Compliance
- **Google Cloud Squad & Pod Structure:**
  - Technical Deployment Lead (TDL): Lead Architect
  - Forward-Deployed Engineers (FDEs) / Pod Leads: 2 Senior AI Engineers (Pod 1: FNOL Document Intake & Extraction; Pod 2: Coverage Verification & Subrogation Routing)
  - Account / AI Consulting Lead: Strategic Account Executive & Value Advisor

---

## 2. Pillar 1: Business Objectives (Product Strategy)

### 2.1 Strategic Business Objectives (Revenue vs. Efficiency Levers)
- **Trigger Event (Why Now):** Commercial Auto loss-adjustment expense (LAE) rose 19% YoY due to manual First Notice of Loss (FNOL) packet triage and third-party administrator (TPA) overflow fees during Q2 weather events. Board approved Q3 funding to automate intake and severity routing before the Q1 policy renewal cycle.
- **Revenue / Recovery Impact Levers:** Eliminates the **14% subrogation misrouting rate** (which currently delays third-party recovery by 22 days), increasing net subrogation salvage recovery across 50,000 annual claims.
- **Efficiency Impact Levers:** Reduces adjuster manual packet reading and Guidewire data entry from **45 minutes to 9 minutes per claim**, removing TPA overflow bottlenecks and creating a reusable Document AI + ADK triage pattern for Commercial Property and Workers' Comp LOBs.

### 2.2 User Personas (Internal & External)

| Persona / Segment | Type (`Internal` / `External`) | Day-to-Day Tasks | Primary Friction Points & UI Preferences |
| :--- | :--- | :--- | :--- |
| **Commercial Auto FNOL Adjuster (85 FTEs)** | `Internal` | Reads 30–80 page PDF demand/FNOL packets (police reports, ACORD forms, repair estimates, medical bills) and keys 42 fields into Guidewire ClaimCenter. | Visual fatigue across multi-document PDFs; context switching between GCS viewer and Guidewire. Wants an embedded side-by-side citation review card inside ClaimCenter. |
| **Subrogation & Complex Claims Specialist (24 FTEs)** | `Internal` | Investigates high-severity bodily injury (`>$25K`) and third-party liability recovery claims. | Receives misrouted claims 22 days late after evidence has gone stale; needs immediate day-1 escalation alerts with cited police report narratives. |
| **Commercial Fleet Policyholder** | `External` | Submits initial loss packet via broker email or portal after a commercial vehicle accident. | Waits 3.4 business days for initial claim assignment and reserve confirmation. |

### 2.3 OKRs and Quantifiable Success Metrics
- **Current Baseline Performance:** `45.0 minutes` mean handling time, `14.0%` queue misrouting rate, `$56.25` labor cost per claim across `50,000` annual claims (`docs/baseline_kpis.json`).
- **1-Year Executive "Wildly Successful" Headline Metric:** Cut FNOL triage handling time by **80%** (`45 min -> 9 min`), reclaim **30,000 adjuster hours/year** (`$2.25M` gross capacity), and reduce subrogation leakage by **75%**.
- **PoC / MVP Go-to-Production Gate Metrics:**
  - `>= 92.0%` field extraction F1 and queue routing accuracy on the 200-claim golden evaluation dataset.
  - `< 60 seconds` p95 end-to-end packet processing latency in `acme-claims-nonprod`.
  - `100%` deterministic escalation to human review whenever OCR citation confidence `< 0.85`.

---

## 3. Pillar 2: Technical Planning (Platform Architecture)

### 3.1 Data Strategy, Sourcing & Readiness (`Available / Usable / Quality` Yardstick)

| Data Dimension | Criterion | Assessment (`Pass` / `Gap` / `Action Needed`) | Evidence & Source Details |
| :--- | :--- | :--- | :--- |
| **Available** | Exists in sufficient volume & historical depth | **Pass** | 3 years of historical FNOL PDF packets (`150,000+` claims) stored in `gs://acme-claims-vault-prod` and historical routing outcomes in BigQuery (`acme_claims_edw.fnol_history`). |
| **Available** | Permitted under privacy policies, rights & consents | **Pass** | Covered under existing HIPAA BAA and commercial policyholder claims processing consent. |
| **Usable** | Centralized vs. siloed across local drives/sheets | **Pass** | Centralized in GCS and BigQuery; policy endorsements accessible via Guidewire ClaimCenter REST API v2. |
| **Usable** | Clear data owner & fast approval process | **Pass** | Owned by Director of Claims Technology (`Victor Chen`); sandbox IAM roles provisioned in 48 hours. |
| **Usable** | Cataloged metadata & AI-accessible (not trapped in bad scans) | **Action Needed** | ACORD forms and repair estimates are clean PDFs, but 15% of local municipal police reports are low-DPI handwritten scans requiring Document AI OCR + confidence gating. |
| **Quality** | Accurate, reliable, free of major anomalies/missing values | **Action Needed** | Historical human queue labels in BigQuery have a 14% misrouting noise rate; Golden Dataset (`N=200`) must be re-verified by 2 Senior Adjusters. |
| **Quality** | Consistently formatted & matches required frequency (real-time vs. batch) | **Pass** | Event-driven GCS object upload webhook triggers processing within seconds of email/portal intake. |
| **Quality** | Minimal manual cleansing/labeling required before use | **Pass** | Cloud DLP de-identification template ready for non-prod sanitization. |

### 3.2 Core Capabilities, Architecture & Environment
- **Working Environment:** Isolated non-prod project `acme-claims-sandbox-01` (`us-central1`) configured with VPC-SC and CMEK.
- **System-of-Record Integrations & Complexity:** Guidewire ClaimCenter REST Claims API v2 (`claimcenter-fnol-v2.yaml` — medium complexity, OAuth 2.0 mTLS) + BigQuery OOTB connector.
- **Top 2–3 Capabilities PoC Must Demonstrate Live:**
  1. Multi-document PDF parsing (ACORD form + Police Report + Repair Estimate) with bounding-box page citations.
  2. Live policy coverage & deductible lookup against Guidewire REST mock/staging endpoint.
  3. Deterministic routing classification (`FAST_TRACK`, `STANDARD_ADJUSTER`, `SENIOR_COMPLEX`, `HUMAN_ESCALATION`) when confidence `< 0.85`.
- **Existing Technical Debt:** Legacy regex email parser drops multi-attachment ZIP files; FDEs will replace with an Eventarc + Cloud Run unpacking step.

### 3.3 CI/CD, Security & FinOps Considerations
- **Sensitive Data Handling (PII / PHI / PCI):** Restricted PII + PHI (medical bodily-injury attachments); Cloud DLP redaction on logs; zero data egress outside `us-central1`; CMEK via Cloud KMS.
- **Frontend Auth & IAM Structure:** Okta Workforce Identity Federation + Identity-Aware Proxy (IAP); dedicated least-privilege service account `fnol-triage-agent-sa`.
- **CI/CD & FinOps Boundaries:** Terraform + Cloud Build pipeline; `BigQueryAgentAnalyticsPlugin` token tracking with a `$0.18/claim` inference ceiling and Cloud Monitoring budget alerts.

---

## 4. `/forward` Delivery Considerations Checklist (6 Mandatory Gates)

- [x] **1. Security & PII Clarity:** HIPAA BAA, `us-central1` residency, and Cloud DLP log masking rules documented with CISO architect.
- [x] **2. Isolated Non-Prod GCP Environment:** `acme-claims-sandbox-01` and `acme-claims-nonprod` isolated from production Guidewire writes.
- [x] **3. Active Weekly Customer Tech Collaboration:** 3 Acme engineers (Guidewire Lead, BigQuery Engineer, Python Platform Dev) allocated 50% time for weekly co-development.
- [x] **4. Assigned Business SMEs:** 2 Senior Commercial Auto Adjusters assigned 4 hours/week for golden dataset labeling and bi-weekly demo UAT.
- [x] **5. Clear Co-Development Boundaries:** Google FDEs build the ADK multi-agent extraction & routing service; Acme Guidewire team owns the ClaimCenter UI webhook consumer.
- [x] **6. Baseline Analytics or Survey Commitment:** 50 stratified historical claims audited and frozen in `docs/baseline_kpis.json`.

---

## 5. Pillar 3: Estimated Dates, Agenda & 30-60-90 Day Execution Plan

### 5.1 Onsite Workshop Agenda & Breakout Structure (September 9–10, 2026)
- **Day 1 AM:** Kickoff, Voice of Customer, Business Objectives Overview, and 50-Sample Baseline Audit review.
- **Day 1 PM (Breakout Session 1 — Technical Planning):** Pods complete Data Strategy (`Available/Usable/Quality`), Core Capabilities, and Security/FinOps mapping → 15-min Pod Present-Backs.
- **Day 2 AM (Breakout Sessions 2 & 3 — Test Assumptions With Something Tangible):** Pod 1 builds live Document AI + Gemini 2.5 Flash extraction spike on 10 sanitized police reports; Pod 2 builds Guidewire coverage lookup + deterministic routing evaluator.
- **Day 2 PM (Breakout Session 4 — 30-60-90 Plan & Present-Back):** Lock 30-60-90 day milestones, live demo of tangible Day 2 prototypes to SVP Sponsor, and Gate 1 sign-off.

### 5.2 30-60-90 Day Execution Plan

| Horizon | Key Milestones | Tangible Leadership Review Assets | Pending Access / Blockers |
| :--- | :--- | :--- | :--- |
| **Next 30 Days (Weeks 1–4)** | Finalize `docs/PRD.md` & `docs/TDD.md`; curate 200-claim Golden Dataset; build end-to-end ADK extraction + Guidewire lookup pipeline in `acme-claims-nonprod`. | Signed-off `docs/PRD.md`, `docs/TDD.md`, `docs/baseline_kpis.json`, and **Demo 1 (Core Experience)** live walkthrough. | Guidewire non-prod mTLS certificate provisioning (Due Sept 15). |
| **Days 31–60 (Weeks 5–8)** | Alpha evaluation with Senior Adjusters; add OCR confidence fallback & subrogation detection; establish Cloud Build CI/CD and Locust load test at 60 claims/hr. | **Demo 2 (Advanced Features & Enterprise Readiness)**, Hill-Climb Eval Readout (`>=90%` F1), Load Test Report. | CISO sign-off on Cloud DLP log sanitization rules. |
| **Days 61–90 (Weeks 9–12)** | Blind parallel UAT on 50 live claims; executive Go/No-Go review against OKRs; FinOps token dashboard in Looker Studio; production cutover & handoff training. | **Demo 3 (Full Delivery)**, Final Closeout Slide Deck, Production Runbook & Transition Guide. | Final Production ARB sign-off (Week 11). |
