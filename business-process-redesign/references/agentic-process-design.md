# Phase 2: Designing 'To-be' Agentic Processes Reference

This reference outlines the principles and templates to execute Phase 2: Designing 'To-be' Agentic Processes.

---

## 1. Principles of Human-Agent Collaboration

Designing an "Agentic" process is NOT about replacing humans. It is about creating a symbiotic workflow where agents execute structured, heavy-lift, or repetitive tasks, and humans operate as strategic supervisors, estimators, and governors.

### The Collaborative Blueprint

```
┌──────────────────────────────────────────────────────────────────┐
│                       INPUT TRIGGER                              │
│   (e.g., Email Arrives, Webhook Fired, Scheduled Cron Job)        │
└─────────────────┬────────────────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────────────────┐
│                   AGENT EXECUTION LAYER                          │
│   • Retrieve Context (Salesforce, PDF Contracts, Knowledge Base) │
│   • Synthesize & Draft Response                                  │
│   • Run Calculations / Rules-Check                               │
└─────────────────┬────────────────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────────────────┐
│              HUMAN-IN-THE-LOOP (HITL) GATE                       │
│   • Does confidence meet threshold? (e.g., >90% / Value < $10k)   │
├─────────────────┴──────────────────────────────┬─────────────────┤
│                      YES                       │       NO        │
│                       │                        │        │
│                       ▼                        │        ▼
┌────────────────────────────────────────────────┐  ┌──────────────┐
│               AUTONOMOUS ACTION                │  │  HUMAN REVIEW│
│   (Update database, Send formatted email)      │  │  & CORRECTION│
└────────────────────────────────────────────────┘  └──────┬───────┘
                                                           │
                                                           ▼
                                                    ┌──────────────┐
                                                    │ LEARNING LOOP│
                                                    │  (Log feedback│
                                                    │   for tuning)│
                                                    └──────────────┘
```

---

## 2. Collaborative Workflow Design Template

For every process redesigned for AI agents, you MUST define the following six core dimensions:

### 1. Agent Mandate
Clearly define the agent's responsibilities, boundaries, and expectations.
*   *Example:* *"The agent is responsible for reviewing incoming billing disputes, retrieving invoice details, verifying against the refund policy, and drafting a response."*

### 2. Action Triggers
What initiates the agent's execution?
*   *Examples:*
    *   **Event-Driven:** Incoming webhook, new Zendesk ticket, SQL database insert.
    *   **Scheduled:** Daily at 8:00 AM, hourly syncs.
    *   **User-Initiated:** Chat slash command (`/billing-triage`).

### 3. Data & Knowledge Sources
What information repositories does the agent have access to for context?
*   *Examples:* Salesforce CRM API, Snowflake Billing DB, Refund Policy PDF, customer transaction logs.

### 4. Action Tools
What tools/APIs can the agent execute?
*   *Examples:* Zendesk API (to post drafts), Slack webhook (to notify), Gmail SMTP (to draft emails).

### 5. HITL Quality Gates & Escalation Rules
Define the specific boundary lines where the agent MUST stop and escalate to a human.
*   **Value Thresholds:** *"If the dispute amount is greater than $500, the agent MUST NOT auto-respond and must escalate to a Billing Manager."*
*   **Confidence Score:** *"If the agent's categorization confidence is below 85%, it must route to a Human Triage queue."*
*   **Complex Scenarios:** *"If the customer email mentions legal action, route immediately to Executive Escalations."*

### 6. Learning & Feedback Loop
How does the agent learn from human adjustments?
*   *Mechanism:* Human corrections to the agent's draft are captured, logged to a CSV/database file, and analyzed weekly to tune prompts or improve the agent's grounding data.

---

## 3. "To-Be" Process Design Template

Detail the redesigned process using the structured template below:

```
=====================================================================
REDESIGNED AGENTIC PROCESS SPECIFICATION
=====================================================================
Process Title: [Process Name]
Primary Goal: [What business outcome is delivered?]

1. WORKFLOW SPECIFICATION
---------------------------------------------------------------------
• Action Trigger:      [Event / Schedule / Command]
• Target Agent:        [Agent Name / Role]
• Grounding Data:      [Salesforce, Policy PDFs, Databases, etc.]
• Action Tools:        [APIs, Webhooks, System write-actions]

2. STEP-BY-STEP FLOW
---------------------------------------------------------------------
[Step 1]: Agent receives trigger.
[Step 2]: Agent retrieves context from [Data Source].
[Step 3]: Agent processes [Task] (e.g., drafts email response).
[Step 4]: [HITL Gate] If [Escalation Condition] is met, route to Human.
          Else, execute [Autonomous Action].

3. ESCALATION RULES
---------------------------------------------------------------------
• Escalation Gate 1:  [Condition] --> Routes to [Human Role]
• Escalation Gate 2:  [Condition] --> Routes to [Human Role]

4. FEEDBACK & LEARNING LOOP
---------------------------------------------------------------------
• Feedback Storage:   [File path / Database table]
• Tuning Frequency:   [Weekly / Monthly review of human corrections]
=====================================================================
```

---

## 4. Business Case & ROI Estimation

To present a compelling case to Business Process Owners, calculate the estimated return on investment (ROI).

### ROI Calculations

$$\text{Annual Time Saved (Hours)} = \text{As-Is Annual Time Spend (Hours)} - \text{To-Be Annual Time Spend (Hours)}$$

$$\text{Annual Labor Savings} = \text{Annual Time Saved (Hours)} \times \text{Labor Rate} (\$/\text{Hour})$$

$$\text{Annual Error Savings} = \text{As-Is Rework Cost} - \text{To-Be Rework Cost}$$

$$\text{Implementation Cost (One-time)} = \text{Agent Design & Build Time (Hours)} \times \$75.00/\text{Hour}$$

$$\text{Estimated Payback Period (Months)} = \left( \frac{\text{Implementation Cost}}{\text{Annual Labor Savings} + \text{Annual Error Savings}} \right) \times 12$$

### ROI Summary Template

```
=============================================
REDUX BUSINESS CASE CARD
=============================================
Process Name: [Process Title]

• Est. Annual Time Saved:   [Hours] hours / year
• Est. Annual Labor Saved:  $[Cost] / year
• Est. Rework/Error Saved:  $[Cost] / year
─────────────────────────────────────────────
TOTAL ANNUAL VALUE:         $[Total Cost] / year
─────────────────────────────────────────────
• One-Time Build Cost:      $[Build Cost]
• Est. Payback Period:      [X] months
=============================================
```

---

## 5. "To-Be" Agent-Enhanced Process Designs Template

This is the formal layout for **Output 2**. Use this template to compile the target state designs:

```markdown
# "To-Be" Agent-Enhanced Process Design: [Process Title]

## 1. Design Goals & Scope
- **Automation Objectives:** [Core objectives of the redesign (e.g., reduce cycle time by X%, eliminate human transcription errors).]
- **Process Boundaries:** [Clearly state what is in-scope for agentic automation vs. what remains explicitly manual.]

## 2. Collaborative Architecture & Workflow Spec
- [Insert the completed REDESIGNED AGENTIC PROCESS SPECIFICATION detailing trigger, agent, data, and tools.]

## 3. Step-by-Step Agentic Execution Path
- [Detail the step-by-step workflow. Use formatting like `[Agent]` for autonomous steps, and `[HITL Gate]` for steps requiring human interaction.]
- **Escalation Matrix:** [Document the precise escalation gates: thresholds, low-confidence overrides, and error triggers.]

## 4. Business Case & ROI Model
- [Insert the completed REDUX BUSINESS CASE CARD showing time, labor, and error savings.]
- [Detail the build cost calculations: developer hours, software licensing changes, and payback period.]
```
