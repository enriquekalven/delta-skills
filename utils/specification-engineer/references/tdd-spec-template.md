# Enterprise Agent Technical Specifications Template (`docs/TDD.md`)

Use this official **Delta Squad Enterprise Agent Technical Specifications (`go/delta-squad-agent-specs`)** template when generating `docs/TDD.md`.

**Legend:**
- **✳️ Mandatory:** Must be completed for approvals and squad provisioning.
- **👥 Joint Effort:** Collaboration required between TDL and FDE Tech Lead.

````markdown
# Enterprise Agent Technical Specifications: [Use Case / System Name]

- **Source PRD:** `docs/PRD.md`
- **Source Architecture:** `docs/ARCHITECTURE_RECOMMENDATION.md`
- **Status:** <Draft | Discovery Sign-off | Gate 2 Approved>
- **Last Revised:** <YYYY-MM-DD>

---

# Part I: Project Context

## A. Project Administration

| Attribute | Details / Values |
| :--- | :--- |
| **✳️ Use Case Name** | <Enter Official Use Case Name> |
| **✳️ Customer / Client** | <Name of the Organization> |
| **✳️ Primary Client Contacts** | **Business Sponsor:** <Name><br>**Lead Engineer / POC:** <Name><br>**Security Officer:** <Name> |
| **✳️ Google TDL** | <Name> |
| **✳️ Google FDE Tech Lead** | <Name> |
| **✳️ Target Milestones** | **Project Start Date:** <YYYY-MM-DD><br>**Discovery Sign-off:** <YYYY-MM-DD><br>**Squad Target Start Date:** <YYYY-MM-DD> |
| **✳️ Primary Goal** | <High-level summary of the agent's goal> |
| **Salesforce Opportunity ID / Expert Request** | <ER-XXXXXX> |
| **Buganizer / Jira / Epic Tracker Link(s)** | <Link> |
| **Shared Collaboration** | **Shared Drive:** <Link><br>**Slack/Chat Channel:** <Channel><br>**Git Repository:** <Repo URL> |

---

# Part II: Use Case Specification

## A. Business Goal & Problem Statement
* **✳️ Core Problem Statement:** <What explicit manual bottleneck, business inefficiency, or cost driver does this agent solve?>
* **✳️ Target Business Outcome:** <Describe the measurable quantitative value delivered by this agent, citing `docs/baseline_kpis.json`.>

## B. ✳️ Measurable Success Metrics (KPIs)
- [ ] **Time Savings / Productivity:** <e.g., Reduces manual compilation time by 80%, saves 25 hours/week>
- [ ] **Task Accuracy & Grounding:** <e.g., >95% factual grounding precision on internal documentation>
- [ ] **Latency Threshold:** <e.g., Interactive response time p95 < 2.5 seconds per turn>
- [ ] **Operational Volume:** <e.g., Automatically processes 500 intake documents per day>
- [ ] **User Engagement:** <e.g., Active daily users, session completion rate>

## C. ✳️ Users & Critical User Journeys (CUJs)
* **Primary Target Persona(s):** <e.g., Enterprise Customer Support Agents, Broadcast Producers, Claims Adjusters>
* **End-to-End User Journey Description:**
  1. **Trigger / Entry Point:** <How does the user or upstream system initiate the agent interaction?>
  2. **Agent Execution Steps:** <Stage-by-stage reasoning steps, tool lookups, brand/context hydration, or model executions.>
  3. **Final Resolution & Output:** <Standardized JSON/UI deliverable the user receives at the end.>

## D. High-Level Solution Concept & UX Modality

### 1. Proposed Agentic Architecture
<Mermaid architecture diagram or module layout>

### 2. ✳️ UX Modality & User Interface 👥
- [ ] **Gemini Enterprise (App) Integration:**
  - [ ] **Workspace Extensions / Plugins / Connectors:** Agent registered in Gemini Enterprise App catalog for end-users.
  - [ ] **Gemini for Google Workspace:** Embedded inside Google Docs, Sheets, Gmail, or Drive.
- [ ] **Standalone Web & Mobile Applications:**
  - [ ] **Desktop Web Portal:** Dedicated browser-based chat interface or dashboard.
  - [ ] **Native Mobile App:** Dedicated iOS / Android chat application.
  - [ ] **Responsive Mobile Web:** Mobile-optimized web portal or Progressive Web App (PWA).
- [ ] **Embedded Client Overlay:** Integrated into existing internal CRM, ERP, or portal.
- [ ] **Automated / Batch Trigger:** Non-interactive background pipeline (triggered by Pub/Sub, Cloud Scheduler, or webhook).

### 3. ✳️ Expected Inputs & Outputs 👥
* **Expected Inputs:** <Exact payloads, uploaded PDFs/images, GCS URIs, session metadata>
* **Expected Outputs:** <Markdown chat responses, structured JSON schemas, Base64/signed GCS media URLs, API updates, SSE events>

### 4. ✳️ Data Requirements
- [ ] **Mock Data Needed for MVP Development?:** [ ] Yes [ ] No — Location: <Path / Drive Link>
- [ ] **Real Data Needed for MVP Development?:** [ ] Yes [ ] No — Location: <Path / Drive Link>

### 5. Architectural Review Board (ARB) Alignment
<Outline whether client ARB approval is required prior to production readiness, timeline, required deliverables, and key approvers.>

## E. ✳️ Out-of-Scope Boundaries
* <Explicit capability, legacy integration, or mutative API agreed as OUT OF SCOPE for initial delivery>

---

# Part III: Platform Infrastructure & Developer Clearance

*To be filled out by TDLs prior to developer onboarding (Prelude / Week 0 Gate).*

## A. Onboarding & Developer Access Clearance Checklist 👥
- [ ] **✳️ Client Workstation / VDI Access:**
  - [ ] Virtual Desktop / VDI Required (Status / Delivery Timeline): <Details>
  - [ ] Corporate Client Laptop Required
  - [ ] Direct Bring-Your-Own-Device (BYOD) with Workload Identity Federation (WIF) Access
- [ ] **✳️ GCP Project Access Mapping:**
  - **Development Environment Project ID:** `<dev-project-id>`
  - **Staging / UAT Environment Project ID:** `<staging-project-id>`
  - **Production Environment Project ID:** `<prod-project-id>`
  - **Code Handoff Target (Git / Gerrit / Cloud Source Repo):** `<repo-url>`
- [ ] **✳️ Development Tooling & Licenses:**
  - [ ] **Antigravity Developer Licenses Provisioned:** [ ] Yes [ ] No
  - [ ] **Gemini Enterprise Licenses Provisioned:** [ ] Yes [ ] No [ ] N/A
- [ ] **✳️ IAM Roles Checklist (Grant to Google Delivery Team):** 👥
  - [ ] `roles/aiplatform.user` *(Vertex AI Agent Engine deployment)*
  - [ ] `roles/iam.serviceAccountUser` *(Act-As SA execution)*
  - [ ] `roles/secretmanager.secretAccessor` *(Secret & API key hydration)*
  - [ ] `roles/logging.viewer` *(Diagnostics & error auditing)*
  - [ ] `roles/monitoring.viewer` *(Telemetry & performance dashboards)*
  - [ ] **Custom Client Roles:** `<custom-roles>`

## B. Google Cloud Service Enablement Matrix 👥

| Service Category | Google Cloud API Name | API Service Identifier | Enabled (Y/N) | Technical Role & Dependency Justification |
| :--- | :--- | :--- | :---: | :--- |
| **Core AI & ML** | Vertex AI API | `aiplatform.googleapis.com` | [ ] | <Models & Reasoning Engine orchestration> |
| | Cloud Telemetry API | `cloudtelemetry.googleapis.com` | [ ] | <Real-time observability & ADK tracing> |
| **Compute & Runtime** | Cloud Run API | `run.googleapis.com` | [ ] | <Serverless container runtime> |
| | Cloud Build API | `cloudbuild.googleapis.com` | [ ] | <Container build & CI/CD pipeline> |
| | Artifact Registry API | `artifactregistry.googleapis.com` | [ ] | <Versioned Docker container registry> |
| **Databases & Storage** | Cloud Storage JSON API | `storage.googleapis.com` | [ ] | <Staging artifacts & signed URLs> |
| | Cloud Firestore API | `firestore.googleapis.com` | [ ] | <Low-latency session & state persistence> |
| | Secret Manager API | `secretmanager.googleapis.com` | [ ] | <Credentials & API key storage> |
| | BigQuery API | `bigquery.googleapis.com` | [ ] | <Agent analytics & audit logs> |

## C. Client Architecture & Shared Components Baseline 👥
* **Data Stores & Analytical Warehouses:**
  - Relational DB (`PostgreSQL / Cloud SQL / AlloyDB`): <Details>
  - Analytical Warehouse (`BigQuery`): <Details>
  - NoSQL / Document Store (`Firestore / MongoDB`): <Details>
  - Object Storage (`Google Cloud Storage GCS`): <Details>
* **Asynchronous Task & Event Queues:**
  - Job Queue (`Cloud Tasks / Celery / Redis`): <Details>
  - Event Streaming (`Google Cloud Pub/Sub / Kafka`): <Details>
* **Services (Internal & Third-Party):** <Details>
* **Serverless & Managed Compute:** <Cloud Run / Cloud Run Jobs / Cloud Run Functions / App Engine>
* **Identity & Authentication Infrastructure:** <Okta / SAML 2.0 / PingIdentity / OAuth 2.0 / OIDC / IAP / RBAC>

---

# Part IV: Deep-Dive Agent Technical Specifications

*Structured around the four pillars of the Gemini Enterprise Agent Platform (`BUILD`, `SCALE`, `GOVERN`, `OPTIMIZE`).*

## Pillar 1: BUILD (Agent Architecture, Models & Tools)

### A. Agent Identity & Topology
- **✳️ Agent System Name (snake_case):** `<agent_system_name>`
- **✳️ Agent Display Name:** `"<Human-Readable Display Name>"`
- **✳️ Agent Archetype & Topology:** 👥
  - [ ] **ReAct Conversational Agent:** Standard ADK reasoning-action loop.
  - [ ] **RAG (Retrieval-Augmented Generation) Agent:** Integrates with RAG Engine / Vector Search.
  - [ ] **Graph-Based / Coordinator Multi-Agent Workflow:** Deterministic state machine or `transfer_to_agent` coordinator with specialist sub-agents.
  - [ ] **Agent-to-Agent (A2A) Peer Agent:** Independent microservice sub-agent exposing JSON-RPC endpoints.
- **✳️ Primary LLM Orchestrator & Model Suite:** <e.g., Gemini 2.5 Flash, Gemini 2.5 Pro, Imagen 4.0, Veo 3.0>

### B. System Instructions & Behavioral Rules 👥
```text
[Exact system prompt, routing rules, state keys, and anti-hallucination constraints]
```

### C. Data Modalities & Grounding
- **Data Sources & Search Engines:** <RAG Engine / Vector Search / Direct SQL or NoSQL connectors / Google Search Grounding>
- **Multimodal Content Ingestion:** <Images, Audio/Speech, Video/Vision Warehouse, Documents/PDFs>

### D. Tooling, MCP & Code Execution 👥
- **Standard API Tools & Typed Schemas (Pydantic / TypeScript):**
```python
# Exact Pydantic v2 input/output models and tool signatures
```
- **Model Context Protocol (MCP) Servers:** Authentication model (`Bearer Token` / `OAuth 2.0` / `Service Account`), timeout thresholds, and retry/fallback matrix.
- **Python Code Execution Sandbox:** <Sandboxed Python execution or rendering engines>
- **1st-Party, 3rd-Party OOTB & Custom Connectors:** <Federated vs. Ingested, sync schedule>

### E. Gemini Enterprise App Integration
- **Registered in Gemini Enterprise App?:** [ ] Yes [ ] No
- **A2A Routes Configured:** `GET /a2a/app/.well-known/agent-card.json` and `POST /a2a/app/run_rpc`

---

## Pillar 2: SCALE (Runtime, State & Memory Bank)

### A. Load & Concurrency Expectations
- **✳️ MVP Active Users:** `<N>` | **Production Target Users:** `<N>`
- **✳️ Peak Concurrent Sessions:** `<N>` | **Expected QPS:** `<QPS>`

### B. Agent Platform Sessions & State Management 👥
- **Session State Keys (`session.state`):**
```python
# Exact typed keys held during active conversation thread
```
- **Session Persistence Engine:** `In-Memory (Dev only, TTL)` vs. `Firestore Database / Cloud SQL (Production state persistence)`

### C. Agent Platform Memory Bank (Cross-Session Recall) 👥
- **Enable Google Memory Bank:** [ ] Yes [ ] No
- **Fact Extraction & Consolidation:** <Rules for auto-extracting user preferences across sessions>
- **Custom Memory Topics:** <e.g., Role/Department, Preferred Style Presets, Entity Glossary>
- **Memory Retention TTL:** `<N> days`
- **Built-in Memory Tools:** [ ] `PreloadMemory` (Auto-inject on turn start) [ ] `LoadMemory` (On-demand search)

### D. Cost Controls 👥
- **ADK Context Caching:** Target Cache TTL (`<N> minutes`) for large system prompts / brand guidelines / schemas.
- **Usage Limits:** Daily token cap per user/session (`<N> tokens/day`) and maximum multi-turn session length (`<N> turns`).

---

## Pillar 3: GOVERN (Security, Gateway, Identity & Registry)

### A. ✳️ Agent Identity & Delegated Auth 👥
- [ ] **Attested SPIFFE Principal:** `principal://agents.global.../reasoningEngines/[ENGINE_ID]` or dedicated least-privilege IAM Service Account.
- [ ] **Delegated Auth Broker:** Access downstream user-gated APIs using user-delegated OAuth tokens / IAP JWT assertion headers.

### B. ✳️ Agent Gateway & Network Security 👥
- [ ] **Zero-Trust Default-Deny Egress / IAP Ingress:** Outbound calls restricted; ingress protected by Identity-Aware Proxy (`roles/iap.httpsResourceAccessor`).
- [ ] **VPC Service Controls (VPC-SC):** Deployed inside restricted GCP service perimeter.

### C. ✳️ Governance Policies & Model Armor 👥
- [ ] **Model Armor Integration:** Prompt Injection & Jailbreak mitigation, Sensitive Data Leak Prevention (PII/PHI redaction), and **Semantic Governance Policies (SGP)** on tool calls.
- [ ] **Safety Filters & Deny Lists:** Gemini safety filter thresholds, regex deny lists, and data residency (`us-central1`, etc.).

### D. Agent Registry & Discoverability 👥
- [ ] **Registry Enrollment:** Published via `agents-cli publish gemini-enterprise`.
- [ ] **Agent Card (`agent-card.json`):** Configured with `name`, `version`, `description`, and tagged skills.

### E. ✳️ Sensitive Data / PII / PHI Handling
- **PII/PHI Expected in Inputs?:** [ ] Yes [ ] No
- **Fields to Mask / Sanitize in Logs:** <Specific fields & Cloud DLP / logging redaction rules>

### F. ✳️ Security Guardrails & Fallback Responses
- **Canned Fallback Responses:** Structured error envelopes for blocked or out-of-scope triggers.

---

## Pillar 4: OPTIMIZE (Evaluation, Observability & Analytics)

### A. Offline Evaluation & Executable Acceptance Matrix 👥
- **Local Rapid Testing:** `agents-cli eval run --set-id <id>` and unit/integration test commands (`pytest -q`, `ruff check .`, `mypy src`).
- **Golden Dataset:** 50+ curated real-world CUJ test cases in GCS / Cloud Console.
- **ADK User Simulation:** `agents-cli eval dataset synthesize` multi-turn conversation simulation.
- **Platform Predefined & Custom Metrics:** Single-turn (`Final Response Quality`, `Hallucination`, `Tool Use Quality`, `Safety`), Multi-turn (`Task Success`, `Trajectory Quality`), plus custom CLA / deterministic validators.

| PRD Requirement | Test File / Eval Set | Verification Case | Executable Command |
| :--- | :--- | :--- | :--- |
| `FR-1` | `tests/test_...py` | `test_...` | `pytest tests/test_...py -q` |

### B. Deployment & Online Continuous Evaluation 👥
- **OpenTelemetry Instrumentation:** `AdkAppExtension(enable_tracing=True)` capturing `gen_ai.agent.name`, `gen_ai.conversation.id`, and turn spans.
- **Online Monitors & Quality Alerts:** `OnlineEvaluator` over sampled production traffic + Cloud Monitoring alerting policies.

### C. Troubleshooting & Automatic Optimization 👥
- **Unified Trace Viewer & Failure Clustering:** Cloud Trace turn-by-turn inspection and semantic failure clustering.
- **Automated Prompt Optimization (GEPA):** `adk optimize --dataset-path=<path>`.

### D. Out-of-the-Box BigQuery Agent Analytics 👥
- **Enable `BigQueryAgentAnalyticsPlugin`:** Asynchronous streaming to BigQuery `agent_events` table (`prompt_tokens`, `completion_tokens`, `latency_ms`, payload) + Looker Studio stakeholder dashboard.
````
