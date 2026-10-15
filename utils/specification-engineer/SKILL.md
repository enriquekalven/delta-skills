---
name: specification-engineer
description: >
  Write an Enterprise Agent Technical Specification / Technical Design Document (docs/TDD.md) from a
  PRD and architecture recommendation using the official 4-Part / 4-Pillar TDL Toolbox template
  (go/delta-squad-agent-specs: Part I Project Context, Part II Use Case Specification, Part III
  Platform Infrastructure & Developer Clearance Checklist, and Part IV Deep-Dive Agent Technical
  Specifications across Pillar 1 BUILD, Pillar 2 SCALE, Pillar 3 GOVERN, and Pillar 4 OPTIMIZE).
  Triggers on "write a TDD", "create technical design doc", "agent technical specifications",
  "go/delta-squad-agent-specs", "specification engineer", "turn PRD into TDD.md". Do NOT use for
  product requirements (use product-md) or initial GCP platform tier selection (use
  gcp-agent-architecture-advisor).
---

# Specification Engineer (`docs/TDD.md` — Enterprise Agent Technical Specifications)

This skill translates a Product Requirements Document (`docs/PRD.md`) and Architecture Recommendation (`docs/ARCHITECTURE_RECOMMENDATION.md`) into an implementation-ready **Enterprise Agent Technical Specification (`docs/TDD.md`)** aligned with the official **TDL Toolbox Agent Technical Specifications (`go/delta-squad-agent-specs`)** standard.

## File Contract

- **Inputs:**
  - `docs/PRD.md` (8-section Delta Agentic PRD with CUJs, DAG design, and RICE requirements)
  - `docs/ARCHITECTURE_RECOMMENDATION.md` (Selected runtime tier, data stores, and IAM design)
- **Outputs:**
  - `docs/TDD.md` (Complete 4-Part / 4-Pillar Enterprise Agent Technical Specification with Developer Access Clearance Checklist, API enablement matrix, Pydantic/TypeScript schemas, `session.state` keys, Memory Bank config, SPIFFE/IAP governance, and executable test/eval commands)
- **Reference Template:** [`references/tdd-spec-template.md`](references/tdd-spec-template.md)
- **Worked Examples:**
  - [`examples/broadcast-asset-buddy-agent-specs.md`](examples/broadcast-asset-buddy-agent-specs.md) (Full 4-Part / 4-Pillar TDL Toolbox specification for the **Broadcast News "Asset Buddy" Multi-Agent System**)
  - [`examples/claims-extraction-service-tdd.md`](examples/claims-extraction-service-tdd.md) (Service-level TDD with Pydantic v2 models, BigQuery DDL, and deterministic routing rules for **Commercial Auto FNOL Triage**)

---

## Core Rules

1. **Official 4-Part / 4-Pillar Structure (`go/delta-squad-agent-specs`):** Every generated `docs/TDD.md` must cover all four parts from [`references/tdd-spec-template.md`](references/tdd-spec-template.md), marking **`✳️ Mandatory`** items (required for squad provisioning) and **`👥 Joint Effort`** items (TDL + FDE Tech Lead):
   - **Part I: Project Context:** `A. Project Administration` table (Use Case, Client POCs, TDL, FDE Tech Lead, Target Milestones, Tracker & Git links).
   - **Part II: Use Case Specification:** `A. Business Goal & Problem Statement`, `B. Measurable Success Metrics (KPIs)`, `C. Users & Multi-Stage CUJs`, `D. High-Level Solution Concept & UX Modality` (`Gemini Enterprise App` / `Standalone Web-Mobile` / `Embedded Client Overlay` / `Automated Batch Trigger`, Expected Inputs/Outputs, Mock vs. Real Data Requirements, ARB Alignment), and `E. Out-of-Scope Boundaries`.
   - **Part III: Platform Infrastructure & Developer Clearance (Prelude Gate):** `A. Onboarding & Developer Access Clearance Checklist` (`VDI / Laptop / BYOD with WIF`, `Dev / Staging / Prod GCP Project IDs`, `Antigravity & Gemini Enterprise Licenses`, `IAM Roles Checklist`), `B. Google Cloud Service Enablement Matrix` (`*.googleapis.com` with technical justifications), and `C. Client Architecture & Shared Components Baseline`.
   - **Part IV: Deep-Dive Agent Technical Specifications (4 Pillars of Gemini Enterprise Agent Platform):**
     - **Pillar 1 — BUILD:** Agent Identity & Topology (`ReAct` / `RAG` / `Graph-Coordinator` / `A2A`), System Instructions & Anti-Hallucination Directives, Data Modalities & Grounding, Tooling/MCP/Pydantic Schemas & Timeout Matrix, and Gemini Enterprise App / A2A routes (`/a2a/app/.well-known/agent-card.json`, `/a2a/app/run_rpc`).
     - **Pillar 2 — SCALE:** Load & Concurrency Expectations (`MVP Users`, `Prod Users`, `Peak Concurrent Sessions`, `Expected QPS`), Typed `session.state` Keys & Persistence Engine (`In-Memory` vs. `Firestore`), Memory Bank (`PreloadMemory`, `LoadMemory`, Retention TTL), and Cost Controls (`ADK Context Caching TTL`, daily token caps, turn caps).
     - **Pillar 3 — GOVERN:** Agent Identity & Delegated Auth (`SPIFFE Principal` / Service Account + IAP JWT headers), Agent Gateway & Network Security (`Zero-Trust Egress`, `IAP`, `VPC-SC`), Governance Policies & Model Armor (`Prompt Injection`, `PII/PHI Redaction`, `Semantic Governance Policies [SGP]`, Data Residency), Agent Registry (`agents-cli publish gemini-enterprise`), Sensitive Data Masking, and Canned Fallback Envelopes.
     - **Pillar 4 — OPTIMIZE:** Offline Evaluation (`agents-cli eval run`, 50+ Golden Dataset, ADK User Simulation, Executable Pytest Matrix), Online Continuous Evaluation (`OpenTelemetry GenAI signals`, `OnlineEvaluator`, Cloud Monitoring Alerts), Troubleshooting & Automatic Optimization (`Unified Trace Viewer`, `Failure Clustering`, `GEPA adk optimize`), and `BigQueryAgentAnalyticsPlugin` telemetry streaming.
2. **Concrete Types Only:** Every tool boundary and `session.state` key must be defined with explicit types (Pydantic `BaseModel`, TypeScript `interface`, or SQL DDL) and an explicit timeout/retry/fallback table.

---

## Workflow

### Step 1: Populate Project Context, Use Case Spec & Developer Clearance (Parts I–III)
Read `docs/PRD.md` and `docs/ARCHITECTURE_RECOMMENDATION.md`. Complete the administrative metadata, UX modality checkboxes, Dev/Staging/Prod GCP project mapping, IAM role checklist, and Google Cloud API Enablement Matrix.

### Step 2: Specify Pillar 1 (BUILD) & Pillar 2 (SCALE)
Define the exact agent topology (`LlmAgent` coordinator vs. sub-agents), verbatim system instructions, typed Pydantic v2 input/output schemas, MCP/tool timeout thresholds, typed `session.state` dictionary keys, Firestore persistence, Memory Bank topics/TTL, and ADK Context Caching TTL.

### Step 3: Specify Pillar 3 (GOVERN) & Pillar 4 (OPTIMIZE)
Document SPIFFE/Service Account principals, IAP/VPC-SC network perimeters, Model Armor & Semantic Governance Policies (SGP), PII/PHI log sanitization rules, OpenTelemetry tracing, `BigQueryAgentAnalyticsPlugin` schema, and the executable acceptance test matrix (`pytest -q`, `agents-cli eval run`), then write the complete specification to `docs/TDD.md`.
