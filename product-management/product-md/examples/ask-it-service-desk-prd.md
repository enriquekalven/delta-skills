# PRD: [Global Semiconductor Corp] AskIT Service Desk Optimization

| [Global Semiconductor Corp] AskIT Service Desk Optimization PRD | | **Summary:** Internal IT service desk agent for triage, task-distilled troubleshooting, and autonomous command center remediation. |
| :--- | :--- | :--- |
| **Authors:** Enrique Chan (TDL), Mariem Ayadi (FDE Lead)<br>**Client POCs:** VP IT Service Operations, Global Service Desk Lead, Enterprise Command Center Lead | **Status:** Gate 1 Approved<br>**Last Revised:** 2026-06-22<br>**Read Time:** ~6 min | **Context & Upstream Artifacts:**<br>- `docs/WORKSHOP_INTAKE.md`<br>- `docs/USE_CASE_CANVAS.md`<br>- `docs/CUJ_MAP.md`<br>- `docs/baseline_kpis.json` |

**Discovery Sessions Completed:**
- `2026-06-18`: AI Factory Biweekly — Use Case Backlog & Prioritization Review
- `2026-06-23`: AskIT, Service Desk & Enterprise Command Center Requirements Deep-Dive

---

## 1. USE CASE

The AskIT transformation shifts employee IT support from fragmented, high-friction support portals to a unified "Single Door" **AskCompany** interface. The architecture integrates voice-first Genesys Cloud contact channels, ServiceNow Pro predictive intelligence, and Google Cloud's Agent Development Kit (ADK). By centralizing all employee touchpoints into an orchestrated gateway, the platform eliminates context loss across siloed queues and establishes a safe execution plane for automated remediation.

### Primary Objective

For our **130,000-employee global workforce**, the objective is to replace manual portal navigation and ticket ping-pong with an intelligent, conversational workflow agent that bridges diagnostic communication and system execution.

| Dimension | Specification |
| :--- | :--- |
| **Title** | Triage and Resolve IT System Operations |
| **Persona Identification** | "As an Enterprise Employee or IT Support Agent" |
| **Context Trigger** | When I encounter an IT system issue, submit a support ticket, or trigger an infrastructure alert. |
| **The Goal** | I need to automatically triage, contextually troubleshoot, or autonomously remediate the issue via a unified enterprise conversational interface. |
| **Strategic Outcome** | So that I can bypass manual queues, resolve downtime in minutes, and maintain peak operational availability across 130,000 employees. |

### Strategic Opportunity Analysis

The current IT service desk model suffers from systemic routing and knowledge inefficiencies that cause avoidable employee downtime. These six opportunities shift IT support from reactive "break-fix" cycles to proactive, autonomous workflows:

* **Inbound Triage, Classification, and Routing:** The service desk currently generates **44,000 misrouted interaction records annually**. Deploying a Workflow Agent to classify intent and hardware metadata at ingestion ensures tickets land in the right resolution queue on the first hop.
* **Hyper-Personalized User Profiling & Context:** By utilizing a persistent **Memory Bank**, the agent ingests historical hardware telemetry, OS patch level, and peripheral configurations before the first turn, cutting discovery time and eliminating repetitive diagnostic questions.
* **Personal Agentic AI IT Support Self-Help:** Moving beyond static KB link retrieval, the agent executes guided diagnostic steps with the employee at the edge before a formal ServiceNow ticket is ever generated.
* **Advanced Sentiment Analysis & Experience Quality:** To break the existing **80% CSAT ceiling**, real-time sentiment scoring detects user frustration or critical business impact and fast-tracks sensitive cases to senior L2/L3 engineers with a distilled summary.
* **Supplier & Level 3 Auto-Follow Up:** AskIT autonomously tracks SLA timers on external vendor and Level 3 (L3) engineering queues, executing proactive status follow-ups so vendor tickets do not stall.
* **Command Center (ICC) E2E Autonomous Workflow Automation:** Transitions AskIT from a reactive chat assistant to an event-driven workflow agent that executes pre-approved self-healing scripts for **LAN Chassis Down** and **WAN Bandwidth Critical** infrastructure alerts.

---

## 2. PAIN POINTS & PROBLEMS

Addressing these systemic blockers is the prerequisite for achieving the target **55% ticket deflection rate** and reclaiming **114,000 hours** of annual employee productivity.

| Classification | Pain Point | Description & Operational Impact |
| :--- | :--- | :--- |
| **Blocker (Adoption-Preventing)** | Unstructured ServiceNow Runbooks (Low RAG Accuracy) | Existing KB articles and runbooks are written as long-form prose rather than deterministic troubleshooting trees, yielding poor RAG accuracy. A mandatory 6-week task-distillation cleanup is required prior to production cutover. |
| **Blocker (Adoption-Preventing)** | Routing Overhead Waste | 44,000 unsupported or misrouted interaction records per year create queue noise and delay MTTR by an average of 14.5 hours per misrouted ticket. |
| **Friction (Efficiency-Draining)** | Cognitive Load and Task Distillation | Support agents spend 6–9 minutes per ticket reading sprawling historical work notes across multiple systems; automated task distillation is needed to synthesize actionable summaries. |
| **Friction (Efficiency-Draining)** | Stagnant Experience Scores | The 80% CSAT ceiling stems from static escalation thresholds that fail to adapt to real-time user sentiment or executive/fab-critical urgency. |
| **Friction (Efficiency-Draining)** | Manual L3 Escalation Latency | Manual follow-ups with external hardware/network suppliers introduce multi-hour downtime during critical infrastructure incidents. |

---

## 3. CRITICAL USER JOURNEYS (CUJs)

The following journeys define the sequential flow between the **AskCompany** root orchestrator and the **AskIT** specialist sub-agents across Phase 1 (reactive) and Phase 2 (proactive event-driven).

### CUJ 1: Automated Ticket Triage and Intelligent Routing (Phase 1 — Reactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **1** | Trigger | An employee submits an IT issue via the unified "AskCompany" web/chat interface. |
| **2** | Classification | AskIT analyzes natural language intent, device telemetry, and user location against the ServiceNow Connector. |
| **3** | Validation | The agent validates assignment-group routing rules and maps the intent to the exact resolution queue. |
| **4** | Action | The ServiceNow incident is created with structured work notes; the user receives instant confirmation and live queue depth estimate. |

### CUJ 2: Personalized Troubleshooting with Task Distillation (Phase 1 — Reactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **5** | Context Ingestion | AskIT queries the user's **Memory Bank** and CMDB hardware profile (OS build, VPN client version, assigned laptop asset tag). |
| **6** | Troubleshooting | The agent identifies the root issue class (e.g., `VPN Split-Tunnel Cert Expired`) and retrieves the structured, task-distilled runbook. |
| **7** | Interaction | The user confirms each diagnostic step; the agent branches conditionally if a local check fails. |
| **8** | Resolution | The issue is resolved at the source without L1 human intervention, and a structured resolution summary is written to persistent history. |

### Transition to Proactive Remediation
While CUJ 1 and CUJ 2 are reactive user-initiated journeys, CUJ 3 transitions to event-driven autonomous remediation where the system acts on infrastructure telemetry without waiting for human prompts.

### CUJ 3: Autonomous Command Center Self-Healing (Phase 2 — Proactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **9** | Event Trigger | A ServiceNow webhook triggers a high-priority infrastructure alert (e.g., `WAN Bandwidth Critical` or `LAN Chassis Down`). |
| **10** | Diagnostic | AskIT initiates an autonomous diagnostic DAG to correlate interface error counters and recent change requests. |
| **11** | Remediation | Using the **Agent Sandbox**, the agent executes a pre-approved diagnostic/remediation script (with mandatory HITL approval gate for mutative chassis resets). |
| **12** | Verification | The system polls interface telemetry for 5 minutes to confirm the alert cleared and posts the post-incident audit log to the ICC channel. |

---

## 4. INFORMATION ARCHITECTURE & DAG DESIGN

AskIT uses a Directed Acyclic Graph (DAG) multi-agent architecture for deterministic control flow and operational safety.

| Architecture Component | Type | Details & Functionality |
| :--- | :--- | :--- |
| **Triggers** | Manual | **Chat-based** manual starts inside the AskCompany employee portal. |
| | Scheduled | **Schedule-based** SLA timer audits for L3 supplier follow-ups and nightly KB standardization jobs. |
| | Event-Driven | **ServiceNow Webhooks** for real-time ICC infrastructure alert ingestion. |
| **Nodes** | ServiceNow Connector | Bidirectional incident CRUD, CMDB asset lookup, and assignment-group routing. |
| | QA Agent (RAG) | Partitioned Vertex AI Search corpus over task-distilled troubleshooting runbooks. |
| | BYO-MCP Server Node | Integration of internal network diagnostic CLI tools via Model Context Protocol (MCP). |
| | Multi-Agent Orchestrator | Coordinates hand-offs between Triage, Self-Help Troubleshooting, and ICC Remediation sub-agents. |
| **Logic Gates** | Conditional Branching | Routes the DAG based on taxonomy domain (Network vs. Endpoint Hardware vs. SaaS Access) and confidence score (`>= 0.85`). |
| | Looping | Batch record processing of interaction logs and multi-step diagnostic verification (capped at 5 turns). |
| | Human-in-the-Loop (HITL) | Mandatory HITL checkpoint before any mutative network modification (e.g., chassis reset or BGP traffic rerouting), requiring an authorized ICC technician approval token before execution. |

---

## 5. PRIORITIZED REQUIREMENTS, RICE BACKLOG & PLATFORM LAUNCH ALIGNMENT

### 5.1 Platform Dependency & GA Alignment

| Feature / Platform Capability | Priority | Target / GA Alignment |
| :--- | :--- | :--- |
| **Agent Identity (SPIFFE) & Agent Registry** | P0 | Phase 1 Foundation (Weeks 1–2) |
| **ServiceNow Bidirectional Connector** | P0 | Phase 1 Sprint 1 (Week 4) |
| **Agent Runtime (Managed Reasoning Engine)** | P0 | Phase 1 Sprint 1 (Week 4) |
| **Single-Agent Triage & Task-Distilled RAG** | P0 | Phase 1 Sprint 2 (Week 6 — Demo 1) |
| **Memory Bank (Hardware & User Profiles)** | P1 | Phase 1 Sprint 3 (Week 8 — Demo 2) |
| **Multi-Agent Orchestration & Interactive UI** | P1 | Phase 1 Sprint 4 (Week 10 — Demo 3) |
| **Agent Sandbox (ICC Script Execution + HITL)** | P1 | Phase 2 Fast-Follow |

### 5.2 RICE-Prioritized Feature Backlog

$$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort (Person-Months)}}$$

| Feature ID | Feature Name | CUJ | Reach (/qtr) | Impact | Confidence | Effort (PM) | RICE Score | Priority / Phase |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **F-01** | ServiceNow Intent Triage & Queue Router | CUJ 1 | 65,000 | 2.0 | 0.90 | 1.5 | **78,000** | P0 (Phase 1) |
| **F-02** | Task-Distilled Runbook RAG Self-Help | CUJ 2 | 50,000 | 2.0 | 0.85 | 2.0 | **42,500** | P0 (Phase 1) |
| **F-03** | CMDB & Memory Bank Profile Pre-Hydration | CUJ 2 | 50,000 | 1.0 | 0.90 | 1.2 | **37,500** | P0 (Phase 1) |
| **F-04** | Real-Time Sentiment Escalation & History Distiller | CUJ 1/2 | 32,000 | 1.0 | 0.80 | 1.0 | **25,600** | P1 (Phase 1) |
| **F-05** | Automated L3 Supplier SLA Tracker & Follow-Up | CUJ 1 | 8,500 | 1.5 | 0.85 | 1.0 | **10,838** | P1 (Phase 2) |
| **F-06** | ICC Webhook Diagnostic DAG & HITL Self-Healing | CUJ 3 | 3,000 | 3.0 | 0.70 | 2.5 | **2,520** | P1 (Phase 2) |

### 5.3 Non-Functional Requirements & Acceptance Gates
- **Latency SLA:** p95 <= 2.5 seconds for CUJ 1 intent classification; p95 <= 4.5 seconds for CUJ 2 RAG troubleshooting turn.
- **Accuracy & Evaluation Gate:** `>= 92%` queue routing accuracy and `>= 95%` factual grounding precision on the 100-item ServiceNow golden dataset (`agents-cli eval run`).

---

## 6. HYPOTHESES TO TEST

| Hypothesis | Core Belief | Pivot / Mitigation Plan |
| :--- | :--- | :--- |
| **Hypothesis 1: Task-Based RAG** | Converting unstructured prose KB articles into structured task-based runbooks will increase RAG troubleshooting accuracy by **>= 40%**. | Restrict Phase 1 self-help to the top 50 highest-volume ticket types where runbooks are manually verified by SMEs. |
| **Hypothesis 2: Unified Interface Engagement** | Employees prefer the "AskCompany" single-entry point over legacy siloed portals, driving higher self-service completion. | Embed the AskIT widget directly inside the existing ServiceNow Employee Center header as an overlay. |
| **Hypothesis 3: Sandboxed Network Scripts** | Executing read-only diagnostics and HITL-gated remediation in the Agent Sandbox safely resolves **20% of common ICC alerts** without L3 escalation. | Keep Phase 1 strictly read-only (diagnostic packet attachment to ticket) until ARB approves mutative script execution. |
| **Hypothesis 4: ServiceNow Data Hygiene** | A 6-week cleanup of historical ServiceNow category/subcategory labels is the single highest-leverage driver of triage accuracy. | Use LLM zero-shot semantic routing against assignment-group descriptions rather than noisy historical category tags. |

---

## 7. SCOPE EXCLUSIONS

To protect the 12-week delivery timeline and enforce the 1-in-1-out governance rule, the following capabilities are explicitly excluded from MVP scope:

| Category | Excluded Scope & Boundaries |
| :--- | :--- |
| **Logistics** | **Physical Technician Dispatching:** The agent will not schedule field-tech deskside visits or manage physical laptop/hardware shipping logistics. |
| **Security** | **Direct Active Directory (AD) or Workday Mutations:** To prevent privilege-escalation risks, the agent is strictly prohibited from modifying identity or HR records (e.g., privileged password resets, RBAC group grants, or org-chart updates). |
| **Finance** | **Direct Financial System Approvals:** The agent cannot authorize budgetary spend, software license purchases, or hardware procurement orders. |
| **Localization** | **Non-English Interactions:** Phase 1 GA is scoped strictly to English-language internal support interactions. |

---

## 8. STAKEHOLDERS & BUSINESS VALUE METRICS

| Stakeholder / Metric Area | Target Details |
| :--- | :--- |
| **Project Leadership** | **Google TDL:** Enrique Chan \| **FDE Lead:** Mariem Ayadi \| **Client Sponsor:** VP Enterprise IT Operations |
| **User Impact** | Global workforce of **130,000 employees** and **420 IT Service Desk / ICC analysts** |
| **Core Value Metric** | Deflect and resolve **55%** of Tier-1 internal support tickets at the edge |
| **Efficiency Gain** | Reclaim **114,000 hours** of annual employee wait time and eliminate **44,000** misrouted ticket hops |
| **Phase 1 Success** | Judged by **Triage Routing Accuracy (>= 92%)** and reduction of the 44,000 misrouted interaction records |
| **Phase 2 Success** | Judged by **Autonomous Remediation Volume** (percentage of WAN/LAN ICC alerts diagnosed and cleared via sandboxed workflows) |
