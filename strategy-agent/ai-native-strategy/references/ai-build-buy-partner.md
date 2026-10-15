# Build vs. Buy vs. Partner Decision Reference

Use this rubric to decide whether an AI capability should be **Built**, **Bought (SaaS/Managed Platform)**, or **Partnered**, and whether customization requires **Prompting + RAG** or **Fine-Tuning**.

---

## 1. Build vs. Buy vs. Partner Matrix

| Strategic Differentiation | Technical & Data Complexity | Recommended Path | Typical Time-to-Value | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Low** (Commodity workflow) | **Low** | **BUY** (Off-the-shelf SaaS / Gemini Enterprise) | 2–4 weeks | Internal IT helpdesk FAQ search |
| **Low** (Non-core domain) | **High** (Specialized compliance/data) | **PARTNER / BUY Vertical SaaS** | 4–8 weeks | Sanctions & KYC watchlist screening |
| **High** (Proprietary workflow) | **Low–Medium** | **COMPOSE** (Managed LLM API + Custom ADK Orchestration & RAG) | 6–12 weeks | Commercial insurance FNOL triage & reserve recommendation |
| **High** (Core IP & Proprietary Data Moat) | **High** | **BUILD** (Custom Agent Runtime + Fine-Tuned Domain Models) | 3–6 months | Proprietary algorithmic underwriting or clinical trial matching |

---

## 2. Adaptation Method: Prompting vs. RAG vs. Fine-Tuning

| Criterion | Prompt Engineering + Structured Output | Retrieval-Augmented Generation (RAG) | Supervised / RL Fine-Tuning |
| :--- | :--- | :--- | :--- |
| **Primary Goal** | Enforce output schema, reasoning steps, and tool rules | Ground responses in dynamic or large internal documents | Teach domain-specific syntax, classification, or style |
| **Data Requirement** | 3–10 curated few-shot examples | Indexed document corpus + chunking/citation pipeline | $\ge 500$ verified, high-quality labeled input/output pairs |
| **Update Latency** | Immediate (config deployment) | Minutes (index refresh) | Days/weeks (retrain + eval regression suite) |
| **Upfront Engineering Cost** | `$5K – $15K` | `$25K – $75K` | `$50K – $150K+` |
| **When to Select** | Always start here (Baseline Gate) | Facts change frequently or require page-level citations | Base models fail latency, cost, or accuracy targets even with optimal RAG |

---

## 3. Vendor & Model Evaluation Scorecard

Score candidate platforms from `1` (Poor) to `5` (Best-in-Class):

| Criterion | Weight | Evaluation Question |
| :--- | :--- | :--- |
| **Task Accuracy on Golden Eval Set** | `30%` | Does the model pass accuracy and citation-grounding thresholds on our 50-sample baseline? |
| **Unit Cost at Target Scale** | `20%` | Does cost per completed transaction preserve target gross margin ($\ge 70\%$ for SaaS) at 10x volume? |
| **Latency & Throughput SLA** | `15%` | Does p95 latency meet the CUJ budget with provisioned throughput available? |
| **Security, Residency & Zero-Data-Retention** | `15%` | Are VPC-SC, CMEK, regional residency, and zero training-on-customer-data contractually guaranteed? |
| **Integration & Tool/MCP Support** | `10%` | How cleanly does the runtime integrate with existing identity (IAM/OAuth) and enterprise APIs? |
| **Portability / Switching Cost** | `10%` | Are prompts, eval sets, and tool schemas portable across model providers? |
