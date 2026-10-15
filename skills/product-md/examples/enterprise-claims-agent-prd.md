# PRD: Commercial Auto Claims FNOL Intake & Triage Agent
- **Status:** Gate 1 Approved
- **Last Updated:** 2026-08-15
- **Owners:** Victor Chen (Director of Claims Tech), Dana Morales (SVP Commercial Claims), Lead TDL
- **Linked Artifacts:** `docs/WORKSHOP_INTAKE.md`, `docs/as_is_report.md`, `docs/CUJ_MAP.md`

---

## 1. Executive Vision
The Commercial Auto Claims FNOL Intake & Triage Agent extracts structured claim entities from multi-document broker packets, validates policy coverage against Guidewire ClaimCenter, and generates a cite-linked severity & subrogation routing recommendation so commercial adjusters cut per-claim intake time from 45.0 minutes to 3.0 minutes.

---

## 2. Background, Problem & Target Users

### 2.1 Problem & Baseline Context
Per the Phase 1 As-Is workflow report (`docs/as_is_report.md`), Acme P&C receives 50,000 serviceable commercial auto claims annually (12,000 in the Phase 1 regional rollout). Adjusters currently spend **45.0 minutes (mean)** and **82.0 minutes (p90)** manually reading 30–80 page PDF packets (ACORD 2, police crash reports, repair estimates, medical bills), keying 42 fields into Guidewire ClaimCenter, and assigning routing queues. Manual entry causes a **14.0% error/rework rate** and **8.0% senior-specialist escalation rate**, costing **$56.25 per claim ($675,000/yr across the 12,000-claim Phase 1 cohort)**.

### 2.2 Target Users
| User Role | Headcount / Volume | Primary Need |
|---|---|---|
| **Commercial Auto Intake Adjuster** | 38 adjusters / 12,000 claims/yr (Phase 1) | Pre-populated Guidewire FNOL fields with clickable page/bounding-box citations and one-click severity routing approval. |
| **Senior Subrogation & Complex Claims Specialist** | 12 specialists / ~2,400 complex claims/yr | Immediate flagging of third-party fault indicators, commercial fleet endorsements, and bodily injury triggers within 5 minutes of packet arrival. |
| **Claims Operations Manager** | 4 regional managers | Real-time queue telemetry, extraction confidence histograms, and audit logs of adjuster overrides. |

### 2.3 Glossary & Definitions
| Term | Definition |
|---|---|
| **FNOL** | First Notice of Loss packet submitted via broker portal or intake email (`application/pdf`, `image/tiff`, `xlsx`). |
| **Subrogation Recovery** | Legal right for Acme P&C to recover claim payouts from an at-fault third party's insurer. |
| **HITL Gate** | Human-in-the-Loop review step required before committing complex or low-confidence claims to Guidewire ClaimCenter. |

---

## 3. Product Strategy, Scope & Success Metrics

### 3.1 Goals
- **G1:** Reduce mean adjuster FNOL handling time from **45.0 minutes to <= 3.0 minutes** on the 12,000-claim Phase 1 cohort.
- **G2:** Reduce intake data-entry and queue-misrouting error rate from **14.0% to <= 2.0%**.
- **G3:** Achieve **>= 94.0% field extraction F1** and **>= 92.0% routing classification agreement** against the 200-claim golden evaluation set prior to production cutover.

### 3.2 Out of Scope (Non-Goals for 12-Week Engagement)
- **NG1:** Autonomous claim payout disbursement or reserve check issuance (all reserve assignments remain L1/L2 adjuster actions in Guidewire).
- **NG2:** Live inbound voice call transcription for retail personal-auto policyholders (commercial claims arrive asynchronously via broker portal/email).
- **NG3:** Non-North American paper-mail claims outside Guidewire ClaimCenter v2.

### 3.3 Success Metrics (Baseline vs. Target)
| Metric | Baseline (`docs/as_is_report.md`) | Target (final read-out, weeks 11-12) | Measurement Method |
|---|---|---|---|
| **Mean Handling Time ($T$)** | 45.0 mins (95% CI: 39.1–50.9) | <= 3.0 mins | Guidewire ClaimCenter active session timestamps across post-launch stratified sample |
| **Intake Error / Rework Rate ($E$)** | 14.0% (95% CI: 7.0%–26.2%) | <= 2.0% | Weekly QA audit of routed claims |
| **Unit Cost per Claim ($C_{\text{unit}}$)** | $56.25 | <= $4.50 (incl. $0.75 GCP/token overhead) | `(T / 60) * $75.00 + GCP unit cost` |

---

## 4. User Journeys & RICE-Prioritized Feature Requirements

### 4.1 Critical User Journeys (CUJ Inventory)
| CUJ ID | User Role | Reframed Goal | Priority |
|---|---|---|---|
| **CUJ-01** | Intake Adjuster | As a result of completing these tasks, I will have a validated 42-field Guidewire FNOL record with source PDF bounding-box citations and a recommended routing tier ready for 1-click commit. | P0 |
| **CUJ-02** | Subrogation Specialist | As a result of completing these tasks, I will have an extracted fault-and-recovery evidence summary highlighting police report narratives, third-party insurer policy numbers, and VINs. | P0 |
| **CUJ-03** | Claims Ops Manager | As a result of completing these tasks, I will have an immutable BigQuery audit trail of every agent extraction, confidence score, and human adjuster override. | P1 |

### 4.2 Feature Backlog & RICE Scoring
*(Reach = claims impacted per quarter across the 12,000/yr Phase 1 cohort = 3,000 claims/qtr)*

| Feature ID | Feature Name | CUJ | Reach (/qtr) | Impact | Confidence | Effort (PM) | RICE Score | Phase |
|---|---|---|---|---|---|---|---|---|
| **F-01** | Multi-Document FNOL Entity Extractor & Bounding-Box Anchor | CUJ-01 | 3,000 | 3.0 | 1.0 | 1.5 | **6,000** | Phase 1 MVP |
| **F-02** | Guidewire Policy Lookup & Coverage Verification Tool | CUJ-01 | 3,000 | 2.0 | 1.0 | 1.0 | **6,000** | Phase 1 MVP |
| **F-03** | Severity & Subrogation Triage Classifier + HITL Gate | CUJ-01, CUJ-02 | 3,000 | 3.0 | 0.9 | 1.5 | **5,400** | Phase 1 MVP |
| **F-04** | Side-by-Side Adjuster Review Panel & Override Audit Logger | CUJ-01, CUJ-03 | 3,000 | 2.0 | 0.9 | 1.2 | **4,500** | Phase 1 MVP |
| **F-05** | Automated Broker Missing-Document Follow-Up Email Draft | CUJ-01 | 600 | 1.0 | 0.8 | 1.0 | **480** | Phase 2 Fast-Follow |

### 4.3 Detailed Feature Specifications & Acceptance Criteria

#### F-01: Multi-Document FNOL Entity Extractor & Bounding-Box Anchor
- **Inputs:** GCS URI (`gs://acme-claims-vault-prod/<claim_id>/*.pdf`) containing 1–10 attachments (up to 100 pages total).
- **Behavior & Business Rules:**
  1. Classify each page range by document type (`ACORD_2`, `POLICE_REPORT`, `REPAIR_ESTIMATE`, `MEDICAL_BILL`, `OTHER`).
  2. Extract the 42 canonical FNOL schema fields (Policy Number, Loss Timestamp, Loss Geocode, Insured VINs, Third-Party VINs, Police Report Number, Bodily Injury Flag, Estimated Damage USD).
  3. Attach `{document_id, page_number, bounding_box, confidence}` to every extracted field.
- **Outputs:** Validated `FnolExtractionPacket` JSON payload written to BigQuery staging and Guidewire draft endpoint.
- **Acceptance Criteria:**
  - [ ] Field-level F1 >= 0.94 across the 200-claim golden evaluation set.
  - [ ] 100% of non-null extracted fields include a valid `page_number` and `bounding_box` coordinate array.
  - [ ] Malformed or 0-byte PDFs return a structured `NEEDS_MANUAL_INTAKE` status code within 10 seconds without crashing the worker.

#### F-02: Guidewire Policy Lookup & Coverage Verification Tool
- **Inputs:** Extracted `policy_number`, `loss_timestamp`, and `insured_vin_list`.
- **Behavior & Business Rules:**
  1. Query Guidewire ClaimCenter REST API (`GET /v2/policies/{policy_number}/coverage?asOf={loss_timestamp}`).
  2. Verify active policy status, deductible amount, fleet vehicle schedule match, and rental/subrogation endorsements.
- **Outputs:** `CoverageVerificationResult` block appended to the claim packet.
- **Acceptance Criteria:**
  - [ ] Handles HTTP 404 (policy not found) and 429/503 (Guidewire retry with exponential backoff up to 3 attempts) deterministically.
  - [ ] Flags any unscheduled VIN or lapsed policy date as `COVERAGE_EXCEPTION_L2_REVIEW`.

#### F-03: Severity & Subrogation Triage Classifier + HITL Gate
- **Inputs:** `FnolExtractionPacket` + `CoverageVerificationResult`.
- **Behavior & Business Rules:**
  1. Assign routing queue: `EXPRESS` (property damage < $10K, single vehicle, clear coverage, all field confidences >= 0.92), `STANDARD` ($10K–$50K, multi-vehicle), or `COMPLEX_SUBROGATION` (bodily injury = true, commercial hazmat, disputed fault, or damage > $50K).
  2. Enforce HITL Gate: Any claim classified `COMPLEX_SUBROGATION` or having any required field confidence `< 0.92` blocks auto-routing and routes to the L2 Adjuster Review UI.
- **Outputs:** `TriageDecision` with queue assignment, subrogation recovery score (`0.0..1.0`), and cite-linked rationale bullets.
- **Acceptance Criteria:**
  - [ ] Zero false-negative `EXPRESS` assignments on claims containing bodily injury or fatality indicators across the 200-claim eval set (100% recall on bodily injury escalation).

#### F-04: Side-by-Side Adjuster Review Panel & Override Audit Logger
- **Inputs:** Draft claim packet and adjuster review actions (`APPROVE`, `EDIT_AND_APPROVE`, `REJECT_TO_MANUAL`).
- **Behavior & Business Rules:** Renders extracted fields alongside the highlighted source PDF page; logs every field edit (`field_name`, `agent_value`, `human_value`, `reason_code`, `adjuster_id`, `duration_ms`) to BigQuery (`acme_claims_edw.fnol_audit_log`).
- **Acceptance Criteria:**
  - [ ] Every adjuster commit writes an immutable audit row to BigQuery within 2 seconds and updates Guidewire ClaimCenter via idempotent `PUT /v2/claims/{claim_id}/fnol`.

---

## 5. Non-Functional Requirements, Compliance & Risks
- **Scale & Latency:** Support 500 claims/day baseline and 60 claims/hour storm surge; end-to-end async pipeline latency `<= 60 seconds p50` and `<= 90 seconds p95` for packets up to 80 pages.
- **Data Privacy, Security & Compliance:**
  - All workloads run inside `acme-claims-vpc-sc` in `us-central1` with CMEK encryption (`projects/acme-sec/locations/us-central1/keyRings/claims-kr`).
  - HIPAA BAA required; zero prompt/completion caching outside the customer GCP project; Cloud DLP redacts driver SSNs from application logs.
- **AI Quality & Evaluation Gates:**
  - Automated CI evaluation runs on every prompt or tool change against the 200-claim stratified dataset (`140 standard / 40 complex / 20 outlier`). Build fails if field F1 < 0.94 or bodily-injury escalation recall < 1.00.
- **Open Risks & Mitigations:**
| Risk | Severity | Mitigation | Owner |
|---|---|---|---|
| Low-DPI handwritten police reports degrade VIN/party extraction | High | Route pages with Document AI OCR confidence < 0.85 to multimodal Gemini high-res inspection + mandatory L2 adjuster verification badge | Lead FDE |
| Guidewire ClaimCenter API rate-limiting during storm surge | Medium | Buffer incomingGCS events via Cloud Pub/Sub with max-concurrency=10 Cloud Run/Agent worker throttling | Platform Engineer |
