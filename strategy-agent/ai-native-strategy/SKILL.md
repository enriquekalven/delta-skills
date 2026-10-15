---
name: ai-native-strategy
description: >
  Evaluate AI-Enhanced vs. AI-Native product positioning, Build vs. Buy vs. Partner decisions,
  model routing unit economics, and AI governance gates to produce docs/AI_STRATEGY.md.
  Trigger when asked to assess AI defensibility, compare Build vs. Buy for AI capabilities,
  model token unit economics, or define enterprise AI governance controls.
metadata:
  author: rcfaris@
  version: '2.0'
---

# AI-Native Strategy

This skill evaluates an organization's AI initiative across four concrete dimensions—**Defensibility & Positioning**, **Build vs. Buy vs. Partner**, **Model Routing Economics**, and **Governance Gates**—and writes `docs/AI_STRATEGY.md`.

---

## Operating Rules

1. **AI-Enhanced vs. AI-Native:**
   - *AI-Enhanced:* Adds an LLM copilot or automation layer to an existing workflow without changing the pricing or core value loop.
   - *AI-Native:* The agent executes the core job-to-be-done, enabling outcome-based or usage-based pricing and a closed-loop data moat.
2. **Defensibility Must Survive Model Upgrades:** Never claim a prompt wrapper or generic RAG pipeline is a moat. Defensibility comes from proprietary feedback data, deep system-of-record write integrations, regulatory compliance boundaries, or distribution lock-in.
3. **Model Routing Economics:** Ground token cost projections in [`references/model-economics-config.json`](references/model-economics-config.json). Route high-volume classification/extraction to fast/low-cost models and reserve frontier reasoning models for complex synthesis or code/tool verification.
4. **Explicit Risk & Compliance Gates:** Every autonomous write action must specify its human-in-the-loop (HITL) threshold, audit log destination, and regulatory classification (see [ai-governance-safety.md](references/ai-governance-safety.md)).

---

## Procedure

### Step 1: Classify the AI Play & Moat
1. Classify each proposed initiative as **AI-Enhanced**, **AI-Native**, or **Hybrid**.
2. Score defensibility (1–5) across Proprietary Data, Workflow Integration Depth, Switching Costs, and Unit Cost Advantage.

### Step 2: Build vs. Buy vs. Partner Decision
Apply the decision framework in [ai-build-buy-partner.md](references/ai-build-buy-partner.md):
- **Buy (SaaS / Gemini Enterprise prebuilt):** Horizontal productivity, standard enterprise search, non-differentiating workflows.
- **Partner / Co-Develop:** Regulated domain models or specialized connectors where vendor IP accelerates time-to-market by >6 months.
- **Build (Custom ADK / Vertex AI):** Core proprietary workflows where domain telemetry and custom tool orchestration create competitive separation.

### Step 3: Model Economics & Multi-Agent Architecture
1. Estimate monthly token volume (`requests/month × avg input/output tokens`) and calculate blended monthly inference cost using [`references/model-economics-config.json`](references/model-economics-config.json).
2. Select the orchestration pattern (Single Agent with Tools, Sequential Pipeline, or Router + Specialist Subagents) using [agentic-architecture-strategy.md](references/agentic-architecture-strategy.md).

### Step 4: Governance & Safety Controls
Define risk tier, PII/PHI handling, evaluation thresholds, and kill switches using [ai-governance-safety.md](references/ai-governance-safety.md), then write `docs/AI_STRATEGY.md`.

---

## Deliverable Template (`docs/AI_STRATEGY.md`)

```markdown
# AI Strategy & Architecture Brief: <Initiative Name>
Date: <YYYY-MM-DD> | Classification: <AI-Enhanced | AI-Native | Hybrid>

## 1. Strategic Positioning & Defensibility Scorecard
| Moat Dimension | Score (1-5) | Evidence / Mechanism |
|---|---|---|

## 2. Build vs. Buy vs. Partner Matrix
| Capability | Decision (Build / Buy / Partner) | Rationale | Target Stack / Vendor |
|---|---|---|---|

## 3. Model Routing & Unit Economics
| Task Tier | Share of Calls | Model | Avg Input / Output Tokens | Monthly Cost @ <Volume> |
|---|---|---|---|---|

## 4. Agentic Orchestration & Governance Gates
- **Pattern:** <Single Agent | Sequential Pipeline | Supervisor-Specialist>
- **HITL Escalation Rule:** <Exact threshold>
- **Compliance & Audit:** <VPC-SC, DLP redaction, evaluation gate>
```

---

## References & Examples

- [AI Build-Buy-Partner Framework](references/ai-build-buy-partner.md): Decision trees and trade-off matrices.
- [Agentic Architecture Strategy](references/agentic-architecture-strategy.md): Orchestration patterns and state handoffs.
- [AI Governance & Safety](references/ai-governance-safety.md): Risk tiers, EU AI Act / HIPAA / SOC2 checklists, and HITL gates.
- [Model Economics Config](references/model-economics-config.json): Reference token pricing and routing splits.
- [Worked Example: Commercial Underwriting AI Strategy](examples/enterprise-agent-platform-strategy.md): Complete `docs/AI_STRATEGY.md` deliverable showing moat scoring, Build/Buy matrix, routed token economics, and governance controls.
