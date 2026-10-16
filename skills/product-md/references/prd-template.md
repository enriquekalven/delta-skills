# Delta Agentic Product Requirements Document Template (`docs/PRD.md`)

Use this Delta Agentic PRD template (paired with RICE feature prioritization; adapt section depth to the engagement and omit sections that do not apply) to produce `docs/PRD.md`.

```markdown
# PRD: [<Client>] <Product / Agent Initiative Name>

| [<Client>] <Product / Agent Initiative Name> PRD | | **Summary:** <1-sentence summary of the agent system and primary workflow automated> |
| :--- | :--- | :--- |
| **Authors:** <TDL Name, PM Name><br>**Client POCs:** <Business Sponsor, Technical POCs> | **Status:** <Draft \| Gate 1 Approved><br>**Last Revised:** <YYYY-MM-DD><br>**Read Time:** ~5 min | **Context & Upstream Artifacts:**<br>- `docs/WORKSHOP_INTAKE.md`<br>- `docs/USE_CASE_CANVAS.md`<br>- `docs/CUJ_MAP.md`<br>- `docs/as_is_report.md` |

**Discovery Sessions Completed:**
- <Date>: <Discovery / Technical Alignment Session Name & Notes Link>

---

## 1. USE CASE

<1-paragraph architectural executive summary explaining the shift from fragmented manual channels/workflows to an orchestrated enterprise agent workflow.>

### Primary Objective

<1–2 sentences stating target workforce/customer population and how the agent replaces manual navigation or triage with conversational and autonomous execution.>

| Dimension | Specification |
| :--- | :--- |
| **Title** | <Action-oriented use case title, e.g., Triage and Resolve IT System Operations> |
| **Persona Identification** | "As a <Primary End-User / Operator Persona>" |
| **Context Trigger** | When I <specific operational trigger, ticket submission, or alert event>. |
| **The Goal** | I need to <automatically triage, contextually troubleshoot, or autonomously execute via unified interface>. |
| **Strategic Outcome** | So that I can <quantified operational outcome: bypass manual queues, cut cycle time, reclaim hours>. |

### Strategic Opportunity Analysis

* **<Opportunity 1 Name>:** <Quantified baseline waste (e.g., 44,000 misrouted records/year) and how the workflow agent eliminates it.>
* **<Opportunity 2 Name>:** <How persistent memory/context hydration reduces discovery/lookup time.>
* **<Opportunity 3 Name>:** <How edge self-help or proactive vendor/SLA management eliminates operational bottlenecks.>
* **<Opportunity 4 Name>:** <How Phase 2 autonomous/event-driven workflows transition the system from reactive chat to proactive self-healing.>

---

## 2. PAIN POINTS & PROBLEMS

Addressing these systemic blockers and friction points is the prerequisite for achieving the target outcome cited in `docs/as_is_report.md`.

| Classification | Pain Point | Description & Operational Impact |
| :--- | :--- | :--- |
| **Blocker (Adoption-Preventing)** | <e.g., Unstructured Runbooks / Low RAG Accuracy> | <Exact data or process failure preventing deployment and required remediation.> |
| **Blocker (Adoption-Preventing)** | <e.g., Routing / Triage Overhead Waste> | <Quantified volume of misrouted/exception records blocking deterministic logic.> |
| **Friction (Efficiency-Draining)** | <e.g., Cognitive Load & Context Switching> | <Impact on operator handling time and need for automated task distillation.> |
| **Friction (Efficiency-Draining)** | <e.g., Manual Escalation Latency> | <Downtime caused by manual follow-ups across L2/L3 teams or external vendors.> |

---

## 3. CRITICAL USER JOURNEYS (CUJs)

Define the sequential flow across Phase 1 (reactive human-initiated journeys) and Phase 2 (proactive/event-driven autonomous journeys).

### CUJ 1: <Primary Triage / Core Workflow Name> (Phase 1 — Reactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **1** | Trigger | <How user or upstream system initiates the request.> |
| **2** | Classification / Context | <How the agent parses intent and queries enterprise connectors.> |
| **3** | Validation | <Deterministic policy/confidence check or queue mapping.> |
| **4** | Action | <Record creation, resolution confirmation, or user response.> |

### CUJ 2: <Contextual Troubleshooting / Deep-Dive Workflow> (Phase 1 — Reactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **5** | Context Ingestion | <Memory Bank + user/asset profile lookup.> |
| **6** | Execution / Reasoning | <Task-distilled runbook or multi-tool synthesis.> |
| **7** | Interaction | <Iterative diagnostic feedback or HITL review.> |
| **8** | Resolution | <Source resolution and persistent state logging.> |

### Transition to Proactive Remediation
### CUJ 3: <Event-Driven Autonomous Workflow> (Phase 2 — Proactive)

| Step | Phase | Action Details |
| :--- | :--- | :--- |
| **9** | Event Trigger | <Webhook / Pub/Sub / Alert trigger without manual human prompt.> |
| **10** | Diagnostic | <Autonomous diagnostic DAG execution.> |
| **11** | Remediation | <Sandboxed script/tool execution or pre-approved action.> |
| **12** | Verification | <Post-action monitoring and human operator notification.> |

---

## 4. INFORMATION ARCHITECTURE & DAG DESIGN

| Architecture Component | Type | Details & Functionality |
| :--- | :--- | :--- |
| **Triggers** | Manual | <Chat-based or UI-initiated manual starts.> |
| | Scheduled | <Cron/schedule-based routine audits or batch jobs.> |
| | Event-Driven | <ServiceNow/Webhook/PubSub triggers for event-driven automation.> |
| **Nodes** | Enterprise Connectors | <Bidirectional CRUD and metadata management (e.g., ServiceNow, Salesforce, iNEWS).> |
| | QA / Knowledge Agent (RAG) | <Partitioned vector/search node over structured runbooks/policies.> |
| | BYO-MCP Server Node | <Integration of internal/legacy tools via Model Context Protocol.> |
| | Multi-Agent Orchestrator | <Manages state hand-offs between diagnostic and execution sub-agents.> |
| **Logic Gates** | Conditional Branching | <Deterministic routing rules based on record attributes or confidence thresholds.> |
| | Looping | <Batch record processing or iterative refinement with max-turn guardrails.> |
| | Human-in-the-Loop (HITL) | <Mandatory approval checkpoints before mutative or high-risk actions execute.> |

---

## 5. PRIORITIZED REQUIREMENTS, RICE BACKLOG & PLATFORM LAUNCH ALIGNMENT

### 5.1 Platform Dependency & GA Alignment

| Platform Capability / Feature | Priority | Target / GA Date |
| :--- | :--- | :--- |
| <e.g., Agent Identity (SPIFFE) & Agent Registry> | P0 | <YYYY-MM-DD> |
| <e.g., Enterprise Connector / MCP Server> | P0 | <YYYY-MM-DD> |
| <e.g., Agent Runtime / Memory Bank> | P1 | <YYYY-MM-DD> |

### 5.2 RICE-Prioritized Feature Backlog

$$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort (Person-Months)}}$$

| Feature ID | Feature Name | CUJ | Reach (/qtr) | Impact | Confidence | Effort (PM) | RICE Score | Priority / Phase |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **F-01** | <Feature Name> | CUJ 1 | <N> | <0.25–3.0> | <0.5–1.0> | <PM> | <Score> | P0 (Phase 1) |
| **F-02** | <Feature Name> | CUJ 2 | <N> | <0.25–3.0> | <0.5–1.0> | <PM> | <Score> | P0 (Phase 1) |
| **F-03** | <Feature Name> | CUJ 3 | <N> | <0.25–3.0> | <0.5–1.0> | <PM> | <Score> | P1 (Phase 2) |

### 5.3 Detailed Feature Acceptance Criteria & Non-Functional SLAs
- **Latency SLA:** <e.g., p95 <= 2.5s interactive triage; p95 <= 8.0s multi-doc synthesis>
- **Data Privacy & Security:** <PII/PHI/PCI handling, VPC-SC, IAM least privilege>
- **Evaluation Gate:** <Minimum precision/grounding score on N>=50 golden evaluation set>

---

## 6. HYPOTHESES TO TEST

| Hypothesis | Core Belief | Pivot / Mitigation Plan |
| :--- | :--- | :--- |
| **Hypothesis 1** | <e.g., Task-Based RAG> | <We believe structuring runbooks will increase RAG accuracy by X%; if not, pivot to deterministic decision trees.> |
| **Hypothesis 2** | <e.g., Unified Interface Adoption> | <We believe single-door entry increases adoption; if not, embed directly in legacy ticketing overlay.> |
| **Hypothesis 3** | <e.g., Sandboxed Automation> | <We believe sandboxed scripts safely resolve X% of alerts with zero human intervention.> |

---

## 7. SCOPE EXCLUSIONS

To maintain architectural integrity of the 12-week MVP and enforce the 1-in-1-out scope rule, the following boundaries are explicitly excluded:

| Category | Excluded Scope & Boundaries |
| :--- | :--- |
| **Logistics / Operations** | <e.g., Physical technician dispatching or hardware shipping logistics.> |
| **Security / Identity** | <e.g., Direct Active Directory (AD) or Workday mutations (password resets, org-chart edits).> |
| **Finance / Approvals** | <e.g., Direct financial system approvals, budgetary spend, or procurement authorization.> |
| **Localization** | <e.g., Non-English interactions during initial Phase 1 GA.> |

---

## 8. STAKEHOLDERS & BUSINESS VALUE METRICS

| Stakeholder / Metric Area | Target Details |
| :--- | :--- |
| **Project Leadership** | **Google Owner:** <TDL / PM> \| **Client POCs:** <Names & Roles> |
| **User Impact** | Target user base of **<N> employees / operators** |
| **Core Value Metric** | <e.g., Deflect and resolve 55% of internal support tickets> (Baseline vs. Target from `docs/as_is_report.md`) |
| **Efficiency Gain** | <e.g., Reclaim 114,000 hours of wait/handling time annually ($X.XM/yr)> |
| **Phase 1 Success** | Judged by <e.g., Triage Accuracy >= 92% and elimination of misrouted records> |
| **Phase 2 Success** | Judged by <e.g., Autonomous Remediation Volume cleared without human intervention> |
```
