---
name: workshop-intake
description: >
  Conduct a structured customer discovery and onsite workshop intake interview using the official
  TDL Toolbox 32 Starter Questions, the Data Readiness Yardstick (Available / Usable / Quality),
  the 6 /forward Delivery Considerations, and the 3-Pillar Onsite Pod Breakout & 30-60-90 Day
  Execution Plan, writing docs/WORKSHOP_INTAKE.md. Trigger when asked to start a workshop intake,
  plan an onsite discovery workshop, qualify a use case, or gather customer engagement requirements.
  Do NOT trigger when the word "workshop" is mentioned in passing.
metadata:
  author: heyderek@
  version: '3.2'
---

# Workshop Discovery, Use Case Qualification & Onsite Intake (`workshop-intake`)

This skill guides a customer discovery or onsite workshop intake session using the official **TDL Toolbox Use Case Selection Guidelines (32 Starter Questions + Data Readiness Yardstick)** and **Onsite Discovery Workshop Pod Playbook**, producing a complete intake brief at `docs/WORKSHOP_INTAKE.md` (used directly by [tdl-field-guide](../tdl-field-guide/SKILL.md), [create-delta-ucc](../create-delta-ucc/SKILL.md), and [gcp-agent-architecture-advisor](../gcp-agent-architecture-advisor/SKILL.md)).

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Prelude (Week 0):** customer qualification or 2-day onsite discovery pod |
| **Reads (Inputs)** | Raw stakeholder interview notes, legacy SOPs, or live interactive discovery answers |
| **Writes (Outputs)** | `docs/WORKSHOP_INTAKE.md` (using [`references/intake-template.md`](references/intake-template.md)) |

---

## Execution Rules

1. **Sequential Discovery Across the 3 Workshop Pillars:** Ask questions in logical groups (**Pillar 1: Business Objectives [Product Strategy]** $\rightarrow$ **Pillar 2: Technical Planning & Data Readiness [Platform Architecture]** $\rightarrow$ **Pillar 3: `/forward` Delivery Considerations & 30-60-90 Day Execution Plan**). Wait for the user's responses rather than dumping every question at once.
2. **Never Invent Client Facts:** If a field is unknown during intake, record `TBD — Owner: <Role>, Due: <Date>` so gaps are visible before the workshop starts.
3. **Evaluate the Data Readiness Yardstick (`Available / Usable / Quality`):**

| Yardstick Dimension | Qualification Question | Pass Criteria (Ready for Week 1) | Blocker / Escalation Trigger |
| :--- | :--- | :--- | :--- |
| **1. Available** | Does data exist in sufficient volume/depth and fall within permitted privacy/consent rights? | Historical corpus accessible; legal/privacy use approved | Missing legal consent or zero historical records |
| **2. Usable** | Is data centralized, owned by a responsive steward, cataloged, and AI-accessible? | Named data owner; API/Warehouse export or clean PDFs | Trapped in illegible paper scans or unowned local spreadsheets |
| **3. Quality** | Is data accurate, consistently formatted, and aligned with batch/real-time latency needs? | Schema documented; minimal manual cleansing needed | High missing-value rate requiring months of ETL before Week 1 |

4. **Enforce the 6 `/forward` Delivery Considerations:** Verify security/PII clarity, isolated non-prod GCP project/VPC, active weekly customer tech collaboration, assigned business SMEs, clear co-development boundaries, and baseline analytics or time/motion data (or a baseline end-user survey) so value can be measured.
5. **Standard Output Path:** Save the finalized brief to `docs/WORKSHOP_INTAKE.md` using [intake-template.md](references/intake-template.md).

---

## The 32 Official TDL Toolbox Starter Questions (By Category)

### 1. Business Impact (5 Questions)
- **Revenue Impact:** Will this use case create a new product/service, enhance existing features, or reduce time-to-market?
- **Customer Experience:** In what specific, measurable ways will this improve CSAT or increase industry mindshare and market eminence?
- **Efficiency Impact:** How will this solution save workforce time, remove bottlenecks/handoffs, or improve output accuracy?
- **Reusability:** Does this create a reusable solution pattern that can be replicated across other lines of business, products, or services?
- **Quantifiable Goals:** What are the exact numerical targets for this impact (e.g., *"save agents 15 minutes per interaction and reduce 100k annual requests by 10%"* rather than *"save time"*)?

### 2. Users (4 Questions)
- **Internal Users:** Who is the primary internal user role that will leverage this solution?
- **Internal Personas:** What are this primary role's day-to-day tasks, workflow bottlenecks, and UI preferences?
- **External Users:** What is the primary external customer segment this solution targets?
- **External Personas:** What are the high-level needs and expectations of this specific customer segment?

### 3. Technical Feasibility: Data Readiness (8 Questions — `Available / Usable / Quality`)
- **Availability:** Does the required data currently exist within the organization with sufficient volume and historical depth?
- **Permissions:** Does our proposed usage fall within permitted rights, privacy policies, and user consents?
- **Centralization (`Usable`):** Is the data centralized, or is it siloed across local drives and spreadsheets?
- **Access (`Usable`):** Does the data have clear ownership, and is there a fast approval process to gain access to it?
- **AI Accessibility (`Usable`):** Is the data easily accessible to AI (not trapped in physical formats or degraded scans), and is it searchable via cataloging or metadata?
- **Accuracy (`Quality`):** Is the data accurate, reliable, consistently formatted, and free of significant biases, anomalies, or missing values?
- **Frequency (`Quality`):** Does the data match the frequency requirements of the use case (daily batch uploads vs. real-time streaming)?
- **Preparation (`Quality`):** Will this data require significant manual cleansing, labeling, or transformation before it can be used?

### 4. Technical Feasibility: Architecture & Environment (5 Questions)
- **Environment:** Has the working environment for `/forward` been identified and configured with the appropriate VPC, IAM, and non-prod isolation?
- **Integrations:** What high-level integrations with existing systems of record will be necessary?
- **Integration Complexity:** Do these integrations require custom builds/MCP servers, or can we use out-of-the-box data connectors?
- **Data Handling:** Are there documented strict security requirements or specialized data handling needs (PII, PHI, PCI, CMEK, VPC-SC)?
- **Technical Debt:** Is there existing technical debt that must be addressed before or during development?

### 5. Business Viability & 30-60-90 Day Planning (10 Questions + 1 from the Onsite Discovery Workshop deck)
- **Stakeholder Alignment:** Are key decision-makers (`CxO` or `CxO-1`) supportive and ready to provide resources?
- **Timelines:** What is the preferred timeline for solution development (`Next 30 Days`, `Days 31–60`, `Days 61–90`)?
- **Urgency:** Is there a specific business milestone (product launch, offsite, earnings, renewal cycle) acting as a catalyst?
- **Technical Team Readiness:** Is the customer's technical team familiar with GCP, or do they have limited capacity requiring specialized Google FDE assistance?
- **SME Availability:** Are internal Subject Matter Experts (SMEs) aware and allocated to guide development, golden dataset creation, and UAT?
- **Cross-Functional Support:** Are internal design, product, and engineering teams able to commit weekly collaboration time?
- **Third-Party Involvement:** Will consultancies or delivery partners work alongside Google, and what are their exact responsibilities?
- **Infrastructure Investment:** Is there clarity on expenditures required for licenses, infrastructure, or hardware?
- **Operational Investment (FinOps):** Have ongoing operational costs for token compute, monitoring, and support been budgeted?
- **Enablement:** Has time/investment for workforce enablement and training been accounted for?
- **Tangible Breakout Goal** *(Onsite Discovery Workshop deck, not one of the 32 Starter Questions)*: What tangible artifact (live ADK spike, wireframe, architecture diagram, or synthetic eval) will the pod build during Onsite Breakout Sessions 2 & 3 to test Day 1 assumptions?

---

## References & Examples

- [Workshop Intake & Onsite Pod Alignment Template](references/intake-template.md): Structured template for `docs/WORKSHOP_INTAKE.md` covering the 3 Pillars, Data Readiness Yardstick, 6 `/forward` Delivery Considerations, and 30-60-90 Day Plan.
- [Worked Example: Acme P&C Insurance Commercial Claims Workshop Intake](examples/acme-financial-workshop-intake.md): Complete `docs/WORKSHOP_INTAKE.md` artifact for a 2-day enterprise claims automation onsite workshop.
