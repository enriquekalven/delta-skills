# Phase 2: Human-Agent Interaction & Role Redefinition Reference

This reference outlines the templates and frameworks to execute Output 3: Human-Agent Interaction Models & Redefined Role Descriptions.

---

## 1. Human-Agent Interaction Model (Collaboration Swimlanes)

An agentic process is a collaborative dance between human expertise and automated capacity. Use this model to map how tasks and decisions flow between the Agent, the Human Operator, and Shared/HITL checkpoints:

```
┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
│     AGENT SWIMLANE    │   │   SHARED / HITL GATE  │   │    HUMAN SWIMLANE     │
└──────────┬────────────┘   └──────────┬────────────┘   └──────────┬────────────┘
           │                           │                           │
   [Runs Triage / Setup]               │                           │
           │                           │                           │
           ▼                           │                           │
   (Generates Draft) ─────────────────>│                           │
                                       │                           │
                               [CSM Approval Card]                 │
                                       │                           │
                                       └──────────────────────────>│
                                                                   │
                                                            [Review Draft &]
                                                            [Verify Key Data]
                                                                   │
                                       ┌───────────────────────────┘
                                       │
                                       ▼
                                [Clicks Approve] 
                                       │
           ┌───────────────────────────┘
           │
           ▼
  [Executes API Build]
```

### Interaction Matrix Template

For every collaborative task, define the boundary rules:

| Task ID | Task Name | Agent Responsibility | Human Responsibility | Handoff Mechanism | Boundary / Safety Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T4** | Intake Logging | Automatically parse web form submissions & draft database payload. | Verify mapped fields match the client's custom contract terms. | Slack Webhook with Review Card. | **Rule:** Agent cannot update the Master Database without human click. |
| **T5** | Setup Config | Execute APIs to create databases & configure software settings. | Conduct final end-to-end verification of active workspace. | Auto-generated Slack workspace check-sheet. | **Rule:** Agent can provision but cannot "go live" without QA sign-off. |

---

## 2. Redefined Role Description Template

When manual tasks are automated, the human operator's role shifts from a **low-value transaction clerk** to a **high-value strategic coordinator**. You MUST explicitly redefine their operational role description using this template:

```
=====================================================================
REDEFINED OPERATIONAL ROLE DESCRIPTION
=====================================================================
Role Title (Legacy):    [E.g., Customer Onboarding Coordinator]
Role Title (Redefined):  [E.g., Customer Onboarding Operations & Quality Lead]

1. CORE MISSION SHIFT
---------------------------------------------------------------------
• Legacy Focus:     High-frequency administrative task execution (copy-
                    pasting, manual typing, basic credential setup).
• Redefined Focus:  System quality governance, complex edge-case exception 
                    handling, and high-touch customer alignment.

2. TASK REDISTRIBUTION
---------------------------------------------------------------------
• ELIMINATED TASKS (Assumed by Agent):
  - [Eliminated Task 1 (e.g., copying Salesforce details into sheet)]
  - [Eliminated Task 2 (e.g., manually clicking "create workspace" in admin portal)]
  - [Eliminated Task 3 (e.g., emailing temp passwords)]

• EXPANDED / NEW RESPONSIBILITIES:
  - [New Responsibility 1 (e.g., reviewing custom database configurations)]
  - [New Responsibility 2 (e.g., running proactive customer kickoff alignment calls)]
  - [New Responsibility 3 (e.g., monitoring agent exception queues)]

3. SKILL & CAPABILITY EVOLUTION
---------------------------------------------------------------------
• Skills No Longer Required:  Rote data-entry, repetitive admin systems.
• Critical New Skills:        SLA diagnostics, data auditing, relationship 
                              management, client consulting.

4. UPDATED PERFORMANCE METRICS (KPIs)
---------------------------------------------------------------------
• Old Metrics:  Onboarding queue volume, manual tickets closed / week.
• New Metrics:  Client Time-to-Value (TTV) speed, onboarding QA pass rate, 
                Client CSAT score, exception resolution SLA speed.
=====================================================================
```
