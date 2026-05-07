# Human-Agent Interaction Models & Redefined Role Descriptions: Customer Onboarding

## 1. Human-Agent Interaction Model

This section defines the collaborative boundaries and swimlane flows showing how the **Onboarding Agent** and the **Onboarding Customer Success Manager (CSM)** work in tandem.

### Collaboration Swimlanes

```
 CUSTOMER                ONBOARDING AGENT               ONBOARDING CSM
 ────────               ────────────────               ──────────────
    │                           │                             │
[Deal Closes]                   │                             │
    │                           │                             │
    │                   [Receives Webhook]                    │
    │                   [Updates Master Tracker]              │
    │                   [Provision Account via API]           │
    │                   [Email Temp Credentials]              │
    │                           │                             │
[Receives Welcome]              │                             │
[Submits Intake Form] ─────────>│                             │
    │                   [Parses Form Data]                    │
    │                   [Drafts Configuration]                │
    │                   [Posts Approval Card] ───────────────>│
    │                           │                             │
    │                           │                      [Reviews Technical]
    │                           │                      [SSO & Setting Plans]
    │                           │                      [Verifies against UXR]
    │                           │                             │
    │                   [Receives Approval] <───────── [Clicks APPROVE]
    │                   [Executes Setup Config]               │
    │                   [Provisions Slack Channel]            │
    │                           │                             │
[Onboarding Complete] <─────────┘                             │
    │                                                         │
    │ <──────────────────────────────────────────────── [Runs 1:1 Kickoff Call]
    │                                                   [Runs Enablement Training]
```

### Interaction Matrix

| Task ID | Task Name | Agent Responsibility | Human Responsibility | Handoff Mechanism | Boundary / Safety Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | Deal Hand-off | Intercept CRM webhook, parse customer metadata, and insert a row into Google Tracker. | None. Monitor system logs. | Automated API payload trigger. | **Rule:** Fully autonomous. No human approval required. |
| **T2** | Account Provisioning | Make API call to create customer workspace and generate temp credentials. | None. Handle system timeouts. | Automated API call. | **Rule:** Fully autonomous. Escalate to IT Ops if API returns >3 timeouts. |
| **T3** | Welcome Send | Draft and send credential email with a secure link to Web Intake Form. | None. | SMTP mail webhook. | **Rule:** Fully autonomous. Email must use encrypted TLS. |
| **T4** | Intake Logging | Parse Web Intake data, update Google Tracker, and compile a draft config payload. | Audit intake responses and verify mapped technical settings. | Slack review card with **[APPROVE]** / **[REVISE]** buttons. | **Rule:** Human-in-the-Loop. Agent cannot configure customer workspace without human approval. |
| **T5** | Tech Configuration | Execute APIs to configure settings, upload CSVs, and create customer Slack channel. | Perform final QA check of live customer workspace. | Automated configuration completion and Slack channel setup. | **Rule:** Human must run the kickoff call and verify that data is active. |

---

## 2. Redefined Role Description

By automating 94% of manual administrative labor, the Onboarding team has unlocked **1,600 hours of annual capacity**. The role of the Onboarding Coordinator is formally redefined to maximize strategic, high-touch value.

```
=====================================================================
REDEFINED OPERATIONAL ROLE DESCRIPTION
=====================================================================
Role Title (Legacy):    Customer Onboarding Coordinator
Role Title (Redefined):  Customer Onboarding Operations & Quality Lead

1. CORE MISSION SHIFT
---------------------------------------------------------------------
• Legacy Focus:     High-frequency, low-value administrative task 
                    execution (manual data transfer, credentials copy-
                    pasting, clicking "create workspace" in admin portal).
• Redefined Focus:  System configuration quality governance, onboarding 
                    exception triage, and high-touch strategic client 
                    alignment to decrease customer Time-to-Value (TTV).

2. TASK REDISTRIBUTION
---------------------------------------------------------------------
• ELIMINATED TASKS (Assumed by Onboarding Agent):
  - Manually copying contract details from Sales emails into Sheets tracker.
  - Logging into system portals to manually click "create new account."
  - Copying temporary passwords and pasting them into Outlook templates.
  - Downloading emailed spreadsheets and typing customer tech responses.

• EXPANDED / NEW RESPONSIBILITIES:
  - Operating as the HITL Quality Gatekeeper (approving agent configs).
  - Hosting high-value 1:1 strategic alignment and kickoff calls.
  - Actively monitoring onboarding system logs and exception queues.
  - Running custom consulting and onboarding enablement workshops.

3. SKILL & CAPABILITY EVOLUTION
---------------------------------------------------------------------
• Skills No Longer Required:  High-speed administrative data-entry, 
                              repetitive clerical ticketing management.
• Critical New Skills:        Technical data auditing, process exception 
                              diagnostics, strategic business consulting, 
                              executive communication.

4. UPDATED PERFORMANCE METRICS (KPIs)
---------------------------------------------------------------------
• Legacy Metrics:  Tickets closed / week, rows updated, emails sent.
• Redefined KPIs:  Customer Time-to-Value speed (contract sign to go-live),
                   Workspace QA audit pass rate (0% post-onboarding bugs),
                   Customer CSAT Score, Exception queue SLA resolution speed.
=====================================================================
```
