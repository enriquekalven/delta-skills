# Process Design Review (PDR) Reference

This reference outlines the guidelines and checklists to prepare for and execute a formal **Process Design Review (PDR)**.

---

## 1. Objective of a Process Design Review (PDR)

A Process Design Review is a structured meeting or alignment gate with key stakeholders—Business Process Owners, Subject Matter Experts (SMEs), Technical Leads, and Security/Compliance Officers—to review the proposed "To-Be" agentic process, evaluate risks, and secure formal authorization/sign-off to build.

### Core Stakeholder Roles
*   **Business Process Owner:** Approves the business logic, autonomy levels, and financial business case (ROI).
*   **Subject Matter Expert (SME):** Validates that the agentic workflow accounts for real-world edge cases, nuances, and customer experiences.
*   **Technical/Engineering Lead:** Confirms that the APIs, databases, and tools are technically accessible and that the agent's performance expectations are realistic.
*   **Security & Compliance Officer:** Validates that data handling satisfies privacy regulations (e.g., GDPR, HIPAA) and security protocols.

---

## 2. Pre-PDR Checklist (Preparation)

Before presenting the redesigned workflow to stakeholders, you MUST ensure the following deliverables are ready:

*   [ ] **Locked Baseline:** Current-state baseline (Volume, Time, Labor Cost, Error Rates) is documented and cited.
*   [ ] **Redesigned Spec:** The "To-Be" agentic process specification is fully drafted.
*   [ ] **Escalation Matrix:** Escalation conditions and human-in-the-loop (HITL) paths are explicit and clearly mapped.
*   [ ] **ROI Calculations:** The business case, payback period, and implementation costs are completed.
*   [ ] **API Inventory:** A list of required systems/tools and their API availability is assembled.

---

## 3. PDR Alignment Questionnaire

During the review session, use these targeted questions to probe stakeholders and identify hidden risks or requirements:

### Probing Questions for the Business Process Owner
*   *"Do the estimated time and cost savings align with your operational goals?"*
*   *"Are you comfortable with the proposed level of agent autonomy (e.g., auto-responding to disputes under $500)?"*
*   *"What is your primary success metric for this implementation? (e.g., cycle time reduction vs. customer satisfaction)?"*

### Probing Questions for the Subject Matter Expert (SME)
*   *"What is the most complex edge-case you handle in this process today, and how would the proposed escalation rules handle it?"*
*   *"Are there specific informal 'rules of thumb' that you use to spot fraudulent or problematic requests that we need to write into the agent's instructions?"*
*   *"When the agent hands off an escalated ticket to you, what context is absolutely critical for you to see immediately?"*

### Probing Questions for the Technical & Security Leads
*   *"Are the required data sources and tools accessible via standard APIs with the necessary read/write permissions?"*
*   *"Do we store or process any Personally Identifiable Information (PII) in this workflow, and what encryption or redaction is required?"*
*   *"Does the agent's response speed (latency) affect the downstream process or customer experience?"*

---

## 4. PDR Sign-off & Action Item Template

At the conclusion of the Process Design Review, compile the PDR outcome scorecard to document alignment:

```
=====================================================================
PROCESS DESIGN REVIEW (PDR) OUTCOME
=====================================================================
Process Name:       [Process Title]
Review Date:        [YYYY-MM-DD]
Facilitator:        [Agent Name]

STAKEHOLDER ATTENDANCE & SIGN-OFF
---------------------------------------------------------------------
• Process Owner:     [Name] | Status: [APPROVED / REJECTED / CONDITIONAL]
• SME:               [Name] | Status: [APPROVED / REJECTED / CONDITIONAL]
• Tech Lead:         [Name] | Status: [APPROVED / REJECTED / CONDITIONAL]
• Security/Comp:     [Name] | Status: [APPROVED / REJECTED / CONDITIONAL]

OPEN ACTION ITEMS
---------------------------------------------------------------------
1. [Action Item Description] | Owner: [Name] | Due: [YYYY-MM-DD]
2. [Action Item Description] | Owner: [Name] | Due: [YYYY-MM-DD]

REVISION TRIGGERS (When must we re-review?)
---------------------------------------------------------------------
• If implementation cost exceeds estimate by >[X]%.
• If testing reveals agent confidence is consistently <[Y]% on standard cases.

FINAL ALIGNMENT STATEMENT
---------------------------------------------------------------------
"By signing off on this design, the team agrees that the 'To-Be'
workflow delivers a mathematically defensible value improvement while
maintaining strict compliance, security, and human oversight."
=====================================================================
```
