# Worked Example: Supplier Spend & Rate Variance CUJ Transformation (`docs/CUJ_MAP.md`)

This worked example demonstrates the complete 4-tab **`delta /forward` Agentic Process Transformation & CUJ Mapping** workbook from the TDL Toolbox applied to Enterprise Procurement Supplier Spend & Rate Analysis.

---

## Strategic Context & Persona Summary

- **Business Outcome (Level 1):** Enterprise spends less money on external service suppliers by eliminating rate-card leakage.
- **Process Stage (Level 2):** Identify rate opportunities across active supplier Statements of Work (SOWs).
- **Operating Level:** `Task` & `Step (Level 4–5)`
- **Target Actor / Persona:** Procurement Category Analyst (manages 120+ active IT/engineering staffing SOWs across SQL scripts, BuyingHub, and Google Sheets).
- **Reframed Goal (Level 3):** *"As a result of completing these tasks, I have found a verified gap/opportunity where supplier billing rates exceed Preferred Supplier Pricing (PSP) thresholds."*
- **AI Value Proposition:**
  - **Core Feature:** *"AI **Replaces** manual SQL contract queries and SOW rate-card comparisons by autonomously retrieving supplier contracts, normalizing inconsistent job titles to the standard role ontology, and flagging PSP rate variances."*
  - **Integration:** *"AI **Integrates with** Google Sheets and BuyingHub to populate retrieved contract rate cards into a standardized audit workbook."*

---

## 1. Process Ethnography & Observation Capturing (As-Is Ground Truth)

- **Observer Name:** Ricky Hennessy | **Observation Date:** 2026-06-10
- **Participant Role:** Procurement Agent | **Business Process Unit:** Supplier Spend & Rate Analysis
- **Total Observed Manual Cycle Time:** `100.0 minutes` per supplier audit (`2` context-switching points across 3 disconnected tools)

| Step ID | Associated Task Shorthand | User Action / Step Description (As-Is) | System / Application Used | Context-Switching Point? (Y/N) | Friction Category | Observed Friction & Waste Description | Est. Latency (Min) | Qualitative User Quote / Grounding |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :--- |
| **Step 1.1** | Get all contracts for a supplier | Write custom SQL query in Plx Scripts to join tables, search for active supplier contracts, and fetch contract IDs. | Plx Scripts | **Y** | `Data Retrieval` | Highly manual process requiring SQL knowledge; syntax errors and complex table joins cause repeated attempts and waste. | **15.0** | *"I'll constantly have to join tables to get the data that we need. I can't wait for natural language in SQL."* — P4, Internal |
| **Step 1.2** | Get all contracts for a supplier | Log in to BuyingHub, search contracts by supplier name, export active rates, and download raw CSV data. | BuyingHub | **Y** | `System Latency` | High system latency and scattered contract repositories. Requires manual login, file downloads, and copy-pasting data into Sheets. | **10.0** | *"Getting those documents is a pain... Having to log in to separate systems."* — P5, External |
| **Step 1.3** | Normalize role descriptions | Manually scan columns to find and reconcile inconsistent role titles across different supplier spreadsheets to align job categories. | Google Sheets | **N** | `Munging/Transform` | Inconsistent naming standards across supplier roles (e.g., `"L3 Software Eng"`, `"SWE - Level 3"`, `"Developer III"`). Formatting waste requiring manual alignment. | **30.0** | *"But sometimes the formatting just doesn't match up. Often times it's just stupid things."* — P2, External |
| **Step 1.4** | Identify rate variances | Stare-and-compare SOW rate columns against Preferred Supplier Pricing (PSP) threshold to manually identify and highlight overpricing. | Google Sheets | **N** | `Quality Checks` | Extremely error-prone and tedious; manual recalculation required. High visual fatigue makes it easy to miss rate leakage. | **45.0** | *"Data quality and retrieval is extremely error prone and requires manual, painful recalculation and comparison..."* — CME Partner |

---

## 2. Critical User Journey (CUJ) Map Hierarchy (L1–L5)

| Business Outcome (Level 1) | Process Stage (Level 2) | CUJ Goal Shorthand (Level 3a) | Goal / Result Statement (Level 3) | Task (Level 4 — Verb + Noun) | Step (Level 5 — User Action) | Target Actor / Persona | Is Validated? (Y/N) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | As a result of completing these tasks, I have found a gap/opportunity where rates could be lower | Get all contracts for a supplier | Write query in Plx to search for supplier contract IDs | Procurement Agent | **Y** |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | As a result of completing these tasks, I have found a gap/opportunity where rates could be lower | Get all contracts for a supplier | Download contract data and active rate cards into a formatted Sheet | Procurement Agent | **Y** |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | As a result of completing these tasks, I have found a gap/opportunity where rates could be lower | Rationalize roles and rates across all supplier contracts | Normalize and group similar role descriptions | Procurement Agent | **Y** |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | As a result of completing these tasks, I have found a gap/opportunity where rates could be lower | Identify rate variances for similar deliverables | Highlight rates above the PSP rate for supplier | Procurement Agent | **Y** |

---

## 3. Future State CUJ & AI Touchpoint Taxonomy

| Business Outcome (L1) | Process Stage (L2) | CUJ Goal Shorthand (L3a) | Task (L4 — Verb + Noun) | Step (L5 — User Action) | Proposed AI Touchpoint Description | AI Core Effect | Standardized AI Intent | Capabilities & Dependencies | HITL Role & Governance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | Get all contracts for a supplier | Write query in Plx to search for supplier contract IDs | AI replaces manual queries by autonomously searching and retrieving all contracts for a given supplier across Plx and BuyingHub. | `Replace` | `Retrieve` | Natural Language Query, Agentic Search, API Orchestration; Plx catalog schemas, BuyingHub contract registry metadata | **Reviewer** (Verify supplier and contract IDs returned) |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | Get all contracts for a supplier | Download contract data and active rate cards into a formatted Sheet | AI integrates with Google Sheets to push retrieved contract and rate data automatically into a standardized worksheet template. | `Integrate with` | `Execute` | Google Workspace API integration, structured data pipeline; Sheets API authorization, target spreadsheet template | **Reviewer** (Confirm successful import of rates) |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | Rationalize roles and rates across all supplier contracts | Normalize and group similar role descriptions | AI semantic parser automatically clusters similar role titles and maps them to the standard job code ontology. | `Augment` | `Transform` | Unstructured-to-structured clustering, semantic embedding, text mapping; Standard role & job code ontology dictionary | **Prompt Curator** (Manage standard mapping rules for anomalies) |
| Enterprise spends less money on suppliers | Identify rate opportunities | Find lower rate opportunities | Identify rate variances for similar deliverables | Highlight rates above the PSP rate for supplier | AI automatically compares SOW rates against preferred pricing (PSP) and flags deviations above the threshold. | `Replace` | `Analyze` | Deterministic math & rule execution engine, anomaly detection, automated highlighting; Actual SOW rates DB, Preferred Supplier Pricing (PSP) DB | **Approver** (Sign off on justified rate exceptions) |

---

## 4. Collaborative AI Touchpoint Prioritization Matrix

- **Summary Metrics:** `4` Total Opportunities | `2` P0 Immediate Initiatives | `2` P1 High-Priority Sprints | `4.25` Average Strategic Alignment
- **Scoring Formula:**
  - $\text{Value Score} = \text{Avg}(\text{User Pain}, \text{Efficiency Gain}, \text{Strategic Alignment})$
  - $\text{Feasibility Score} = \text{Avg}(\text{Data Readiness}, \text{Tech Feasibility})$
  - $\text{Overall Score (Wtd)} = 0.60 \times \text{Value Score} + 0.40 \times \text{Feasibility Score}$

| TP ID | Associated Goal Shorthand | Proposed AI Touchpoint Description | User Pain (1–5) | Efficiency Gain (1–5) | Strategic Alignment (1–5) | Value Score (Avg) | Data Readiness (1–5) | Tech Feasibility (1–5) | Feasibility Score (Avg) | Overall Score (Wtd) | Priority Level | Next Steps Workstream | Product Owner | Tech Owner |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **TP-1** | Find lower rate opportunities | Autonomous contract data extraction and Plx-to-SQL data synthesis | `5.0` | `5.0` | `5.0` | `5.00` | `4.0` | `4.0` | `4.00` | **4.60** | `P0 (Immediate)` | Iterative Build | `brisa@` | `rickyh@` |
| **TP-2** | Find lower rate opportunities | Automated role and service categorization and normalization in Sheets | `4.0` | `4.0` | `4.0` | `4.00` | `3.0` | `3.0` | `3.00` | **3.60** | `P1 (High)` | Design Sprint | `brisa@` | `rickyh@` |
| **TP-3** | Find lower rate opportunities | Automated risk clause identification and PDF-to-dashboard linking | `5.0` | `4.0` | `5.0` | `4.67` | `4.0` | `3.0` | `3.50` | **4.20** | `P0 (Immediate)` | Iterative Build | `christiannac@` | `ashwinm@` |
| **TP-4** | Find lower rate opportunities | Collaborative spreadsheet dashboard and "Check My Data" validation tool | `3.0` | `4.0` | `3.0` | `3.33` | `4.0` | `4.0` | `4.00` | **3.60** | `P1 (High)` | Technical Discovery | `sandhyap@` | `ashwinm@` |
