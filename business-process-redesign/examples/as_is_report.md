# "As-Is" Process Analysis & Findings Report: Customer Onboarding

## 1. Executive Summary

This report evaluates the current-state customer onboarding process for our operations team, which manages a high-frequency volume of **100 new customer onboardings per month (1,200 per year)**. 

Currently, the entire onboarding lifecycle—from sales close to final system provisioning and technical config—is executed manually via fragmented emails and Google Sheets/Excel trackers. This operational model creates substantial manual bottlenecks, data handoff delays, and copy-paste error loops, consuming **1,700 hours of operational labor annually** and costing the company **$60,550 per year** in administrative overhead and rework.

---

## 2. Current-State Workflow Deconstruction

### Task Decomposition Table
The onboarding lifecycle consists of 5 core sequential tasks, all executed manually by Onboarding Customer Success Managers (CSMs) or Ops Administrators:

| Task ID | Task Name | Step Description (As-Is) | Actor (Who does it?) | Systems/Tools | Key Inputs | Key Outputs | Cycle Time | Frequency |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | Deal Hand-off | Receive sales win email, open Onboarding Tracker sheet, and manually type in client name, CSM, and tier. | Ops Manager | Gmail, Google Sheets | Sales Email | Tracker Row Created | 10 mins | 100 / month |
| **T2** | Account Provisioning | Log into admin portal, click create workspace, set up licenses, and generate temporary login details. | IT Admin / CSM | System Admin Portal | Product Tier | Temp Credentials | 15 mins | 100 / month |
| **T3** | Welcome Send | Copy email template, paste credentials & name, attach onboarding PDF, and send welcome email. | Onboarding CSM | Gmail, Local Files | Credentials, Template | Sent Welcome Email | 10 mins | 100 / month |
| **T4** | Intake Logging | Download customer replied intake sheet, copy technical answers, and paste them back into Onboarding Tracker. | Onboarding CSM | Gmail, Google Sheets | Emailed Attachment | Updated Tracker | 20 mins | 100 / month |
| **T5** | Tech Configuration | Configure custom settings in system portal, upload CSV files, and create shared customer Slack channel. | Onboarding CSM | Portal, Slack | Technical Intake Data | Active Workspace | 30 mins | 100 / month |

### Autonomy Classification Analysis
Applying the Autonomy Spectrum Framework to the current task structure reveals that the majority of tasks are ripe for automated or agent-assisted execution:
*   **T1 (Deal Hand-off):** *L3 Potential (Autonomous).* Standard rules-based data ingestion.
*   **T2 (Account Provisioning):** *L3 Potential (Autonomous).* Structured API-driven account generation.
*   **T3 (Welcome Send):** *L3 Potential (Autonomous).* Event-driven templated communication.
*   **T4 (Intake Logging):** *L2 Potential (Agent-Assisted).* Heavy synthesis of unstructured/structured customer responses.
*   **T5 (Tech Configuration):** *L2 Potential (Agent-Assisted).* API orchestration and configuration setup under human safety gates.

---

## 3. Key Operational Friction Points & Bottlenecks

*   **Handoff Inefficiencies:** Sales-to-onboarding transition relies entirely on passive email notifications. This results in delays in the onboarding kickoff if the Ops Manager misses the email.
*   **Manual Labor Blocks:** The manual copy-pasting of custom credentials and data points across Salesforce, local Excel files, and Gmail is highly repetitive and slows customer onboarding velocity.
*   **Decision & Delay Points:** System provisioning is a blocker. Because IT Admins have to provision accounts manually, customers frequently experience a 24-48 hour delay between signing their contract and receiving welcome credentials.
*   **Error & Rework Analysis:** Manual entry of complex technical parameters (API keys, database setups) from emailed intake forms results in a **5% rework rate**. A single typo in a credential setup breaks the user's login, requiring a high-priority 30-minute triage loop to resolve and resend.

---

## 4. Process Baseline Scorecard

*   **Total Time Spent:** 1.42 Hours per customer $\times$ 1,200 customers = **1,700 Hours / Year**
*   **Fully Burdened Labor Rate:** `$35.00 / hour` (incorporating salary, overhead, taxes, and benefits for Ops/CSM roles)
*   **Annual Rework Cost:** 1,200 customers $\times$ 5% error rate $\times$ 0.5 hours rework $\times$ `$35.00/hr` = **$1,050 / Year**

```
=============================================
PROCESS BASELINE SCORECARD (As-Is)
=============================================
Process Name:   Manual Customer Onboarding
Annual Volume:  1,200 transactions / year

• Total Time Spent:  1,700 hours / year
• Labor Cost Baseline: $59,500 / year
• Rework (Error) Cost: $1,050 / year  (at 5% error rate)
─────────────────────────────────────────────
TOTAL PROCESS BASELINE: $60,550 / year
=============================================
```
