# Workshop Discovery Intake & Onsite Pod Alignment Template (`docs/WORKSHOP_INTAKE.md`)

Use this official **TDL Toolbox Onsite Discovery & Use Case Qualification Template** when generating `docs/WORKSHOP_INTAKE.md`.

```markdown
# Workshop Discovery & Intake Brief: <Customer Name>
Date: <YYYY-MM-DD> | Status: <Draft | Confirmed | Onsite Complete> | Engagement Track: <12-Week Delta / Rapid Discovery>

---

## 1. Customer, Sponsorship & Pod Breakout Structure
- **Customer Name & Segment:** <Name, Industry, Revenue/Headcount>
- **Executive Sponsor:** <Name, Title> (Gate 1–4 budget & scope authority)
- **Primary Customer POC:** <Name, Title>
- **Customer Participants:**
  - Business / Operations SMEs: <Roles>
  - Engineering / Data Platform: <Roles>
  - Security / Risk / Legal: <Roles>
- **Google Cloud Squad & Pod Structure:**
  - Technical Deployment Lead (TDL): <Name>
  - Forward-Deployed Engineers (FDEs) / Pod Leads: <Names & Assigned Use Case Pods>
  - Account / AI Consulting Lead: <Name>

---

## 2. Pillar 1: Business Objectives (Product Strategy)

### 2.1 Strategic Business Objectives (Revenue vs. Efficiency Levers)
- **Trigger Event (Why Now):** <Catalyst business milestone, earnings target, or operational bottleneck>
- **Revenue Impact Levers:** <New product/service, enhanced feature, faster time-to-market, CSAT lift, or market eminence>
- **Efficiency Impact Levers:** <Workforce hours saved, bottleneck/handoff removed, output accuracy improvement, or reusable cross-LOB pattern>

### 2.2 User Personas (Internal & External)
| Persona / Segment | Type (`Internal` / `External`) | Day-to-Day Tasks | Primary Friction Points & UI Preferences |
| :--- | :--- | :--- | :--- |
| `<Role / Segment>` | `Internal` | `<Tasks>` | `<Bottlenecks & UI modality>` |

### 2.3 OKRs and Quantifiable Success Metrics
- **Current Baseline Performance:** <Quantified status-quo handling time, volume, error rate, and cost>
- **1-Year Executive "Wildly Successful" Headline Metric:** <Top metric for executive readout>
- **PoC / MVP Go-to-Production Gate Metrics:**
  - <Metric 1: e.g., Deflect 30% of Tier-1 tickets / >= 92% triage routing accuracy>
  - <Metric 2: e.g., Reduce human handling time by 25% / p95 latency <= 2.5s>

---

## 3. Pillar 2: Technical Planning (Platform Architecture)

### 3.1 Data Strategy, Sourcing & Readiness (`Available / Usable / Quality` Yardstick)

| Data Dimension | Criterion | Assessment (`Pass` / `Gap` / `Action Needed`) | Evidence & Source Details |
| :--- | :--- | :--- | :--- |
| **Available** | Exists in sufficient volume & historical depth | `<Status>` | `<Table / Bucket / Volume>` |
| **Available** | Permitted under privacy policies, rights & consents | `<Status>` | `<Consent / BAA / Legal status>` |
| **Usable** | Centralized vs. siloed across local drives/sheets | `<Status>` | `<Location>` |
| **Usable** | Clear data owner & fast approval process | `<Status>` | `<Owner Name / SLA>` |
| **Usable** | Cataloged metadata & AI-accessible (not trapped in bad scans) | `<Status>` | `<Format: SQL, JSON, Native PDF, Scanned PDF>` |
| **Quality** | Accurate, reliable, free of major anomalies/missing values | `<Status>` | `<Known data quality caveats>` |
| **Quality** | Consistently formatted & matches required frequency (real-time vs. batch) | `<Status>` | `<Refresh cadence>` |
| **Quality** | Minimal manual cleansing/labeling required before use | `<Status>` | `<Prep pipeline needed>` |

### 3.2 Core Capabilities, Architecture & Environment
- **Working Environment:** <Identified GCP Project / VPC / IAM readiness>
- **System-of-Record Integrations & Complexity:** <OOTB Connectors vs. Custom APIs/MCP servers>
- **Top 2–3 Capabilities PoC Must Demonstrate Live:** <Capabilities>
- **Existing Technical Debt:** <Runbook cleanup, legacy schema migrations, etc.>

### 3.3 CI/CD, Security & FinOps Considerations
- **Sensitive Data Handling (PII / PHI / PCI):** <Masking, DLP redaction, HIPAA/SOC2/CMEK/VPC-SC>
- **Frontend Auth & IAM Structure:** <Okta / Entra SSO / IAP / Service Account RBAC>
- **CI/CD & FinOps Boundaries:** <Deployment pipeline, token tracking, monthly API budget caps>

---

## 4. `/forward` Delivery Considerations Checklist (6 Mandatory Gates)

- [ ] **1. Security & PII Clarity:** Security requirements, environment limitations, and PII/PHI policies are known at a high level.
- [ ] **2. Isolated Non-Prod GCP Environment:** A separate GCP project or VPC (isolated from live production connections) is ready or deployable within Week 1.
- [ ] **3. Active Weekly Customer Tech Collaboration:** Customer engineering team commits to active weekly co-development, experimentation, and problem-solving.
- [ ] **4. Assigned Business SMEs:** Customer business SMEs are named and allocated to share process knowledge and run UAT/baseline audits.
- [ ] **5. Clear Co-Development Boundaries:** Explicit delineation of development responsibilities between Customer tech teams, third-party partners, and Google FDEs.
- [ ] **6. Baseline Analytics or Survey Commitment:** Historical operational baseline data and curated Golden Dataset test cases are available (or customer commits to running a baseline user survey).

---

## 5. Pillar 3: Estimated Dates, Agenda & 30-60-90 Day Execution Plan

### 5.1 Onsite Workshop Agenda & Breakout Structure
- **Day 1 (Discovery & Breakout 1):** Business Objectives Overview → **Breakout Session 1: Technical Planning** (Data Strategy, Core Capabilities, CI/CD & Security) → Pod Present-Backs (15 min/pod).
- **Day 2 (Tangible Assumption Testing & Breakout 2–4):** **Breakout Sessions 2 & 3: Test Day 1 Assumptions With Something Tangible** (live ADK spike, wireframe, or architecture prototype) → **Breakout Session 4: 30-60-90 Day Plan** → Tangible Artifact Present-Back.

### 5.2 30-60-90 Day Execution Plan

| Horizon | Key Milestones | Tangible Leadership Review Assets | Pending Access / Blockers |
| :--- | :--- | :--- | :--- |
| **Next 30 Days (Days 1–30)** | <Finalize architecture, ingest/vectorize initial dataset, build PoC pipeline, establish Golden Dataset baseline metrics> | `docs/PRD.md`, `docs/TDD.md`, `docs/as_is_report.md`, Working Demo 1 PoC | `<Pending IAM/data access>` |
| **Days 31–60** | <Alpha testing with veteran SMEs, prompt/retrieval tuning, CI/CD & widget integration> | Demo 2 Readout, Alpha Eval Scorecard, Integrated Staging Build | `<Pending UAT signoff>` |
| **Days 61–90** | <Executive Go/No-Go review against OKRs, FinOps token monitoring, production rollout & training> | Demo 3 Full Delivery, Final Closeout Deck, Production Cutover & Handoff Guide | `<Production ARB>` |
```
