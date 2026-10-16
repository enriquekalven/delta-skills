---
name: specification-engineer
description: >
  Write an Enterprise Agent Technical Specification / Technical Design Document (docs/TDD.md) from a
  PRD and architecture recommendation using the official TDL Toolbox template
  (go/delta-squad-agent-specs: Project Context, Use Case Specification,
  Platform Infrastructure & Developer Clearance Checklist, and Deep-Dive Agent Technical
  Specifications across BUILD, SCALE, GOVERN, and OPTIMIZE).
  Triggers on "write a TDD", "create technical design doc", "agent technical specifications",
  "go/delta-squad-agent-specs", "specification engineer", "turn PRD into TDD.md". Do NOT use for
  product requirements (use product-md) or initial GCP platform tier selection (use
  gcp-agent-architecture-advisor).
metadata:
  version: '3.2'
---

# Specification Engineer (`docs/TDD.md` — Enterprise Agent Technical Specifications)

This skill translates a Product Requirements Document (`docs/PRD.md`) and Architecture Recommendation (`docs/ARCHITECTURE_RECOMMENDATION.md`) into an implementation-ready **Enterprise Agent Technical Specification (`docs/TDD.md`)** aligned with the official **TDL Toolbox Agent Technical Specifications (`go/delta-squad-agent-specs`)** standard.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 Foundations (Weeks 1–2):** Enterprise Agent Technical Specification (`BUILD / SCALE / GOVERN / OPTIMIZE`) |
| **Reads (Inputs)** | `docs/PRD.md`, `docs/ARCHITECTURE_RECOMMENDATION.md` |
| **Writes (Outputs)** | `docs/TDD.md` (following [`references/tdd-spec-template.md`](references/tdd-spec-template.md)) |

---

## Official Specification Structure (`go/delta-squad-agent-specs`)

Every generated `docs/TDD.md` covers the relevant sections from [`references/tdd-spec-template.md`](references/tdd-spec-template.md) (scaling depth to the selected architecture tier), marking **`✳️ Mandatory`** items (required for squad provisioning) and **`👥 Joint Effort`** items (TDL + FDE Tech Lead):

| Part / Pillar | Scope | Mandatory Deliverables in `docs/TDD.md` |
| :--- | :--- | :--- |
| **Part I: Project Context** | Administration & Governance | Client POCs, TDL, FDE Tech Lead, target milestone dates, Program Tracker & Git links |
| **Part II: Use Case Spec** | Modality & Boundaries | Business goal, measurable KPIs, UX modality (`Gemini Enterprise App`, `Standalone Web`, `Embedded Overlay`, `Batch`), mock vs. real data plan, out-of-scope boundaries |
| **Part III: Infrastructure & Clearance** | Prelude Access Gate | Developer onboarding (`VDI/BYOD + WIF`), `Dev / Staging / Prod` GCP Project IDs, IAM role checklist, and `*.googleapis.com` API Enablement Matrix |
| **Part IV — Pillar 1: BUILD** | Topology, Prompts & Tools | Agent topology (`ReAct`, `RAG`, `Graph-Coordinator`, `A2A`), system instructions, Pydantic v2 / TypeScript tool schemas, timeout/retry matrix, `/a2a/app/run_rpc` routes |
| **Part IV — Pillar 2: SCALE** | Concurrency, State & Cost | Peak QPS/concurrency, typed `session.state` keys, `Firestore` vs. `In-Memory` persistence, Memory Bank TTL, and `ADK Context Caching TTL` + daily token caps |
| **Part IV — Pillar 3: GOVERN** | Identity, Security & SGP | `SPIFFE Principal` / Service Account + IAP JWT, `VPC-SC` perimeter, `Model Armor` + Semantic Governance Policies (`SGP`), PII/PHI redaction, canned fallback envelopes |
| **Part IV — Pillar 4: OPTIMIZE** | Golden Dataset & Evals | **Curated Golden Dataset (50+ real-world CUJ test cases) & Baseline Evaluation Metrics**, `agents-cli eval run` config, executable `pytest -q` matrix, OpenTelemetry + `BigQueryAgentAnalyticsPlugin` |

---

## Workflow

### Step 1: Populate Project Context, Use Case Spec & Developer Clearance (Parts I–III)
Read `docs/PRD.md` and `docs/ARCHITECTURE_RECOMMENDATION.md`. Complete the administrative metadata, UX modality checkboxes, Dev/Staging/Prod GCP project mapping, IAM role checklist, and Google Cloud API Enablement Matrix.

### Step 2: Specify Pillar 1 (BUILD) & Pillar 2 (SCALE)
Define the exact agent topology (`LlmAgent` coordinator vs. sub-agents), verbatim system instructions, typed Pydantic v2 input/output schemas, MCP/tool timeout thresholds, typed `session.state` dictionary keys, Firestore persistence, Memory Bank topics/TTL, and ADK Context Caching TTL.

### Step 3: Specify Pillar 3 (GOVERN) & Pillar 4 (OPTIMIZE)
Document SPIFFE/Service Account principals, IAP/VPC-SC network perimeters, Model Armor & Semantic Governance Policies (SGP), PII/PHI log sanitization rules, OpenTelemetry tracing, `BigQueryAgentAnalyticsPlugin` schema, and the **Golden Dataset Baseline Evaluation Metrics** + executable acceptance test matrix (`pytest -q`, `agents-cli eval run`), then write the complete specification to `docs/TDD.md`.

---

## References & Worked Examples

- [`references/tdd-spec-template.md`](references/tdd-spec-template.md): Official template for `docs/TDD.md`.
- [`examples/broadcast-asset-buddy-agent-specs.md`](examples/broadcast-asset-buddy-agent-specs.md): Full TDL Toolbox specification for the **Broadcast News "Asset Buddy" Multi-Agent System**.
- [`examples/claims-extraction-service-tdd.md`](examples/claims-extraction-service-tdd.md): Service-level TDD with Pydantic v2 models, BigQuery DDL, and deterministic routing rules for **Commercial Auto FNOL Triage**.
