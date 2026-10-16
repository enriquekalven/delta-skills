---
name: tdl-user-guide
description: Master registry and navigation index for the 13 TDL-exclusive skills in the TDL User Guide repository (10 codify all 18 official TDL Toolbox assets behind go/delta-delivery-guide; 3 are Google Cloud TDL engineering and ROI accelerators). Maps each skill to its source, input files, output artifacts, scripts, and worked examples across the 12-week Delta engagement. Triggers on "tdl user guide", "list available skills", "find a skill", "which skill should I use", "tdl toolbox mapping", or "understand the capabilities of this workspace".
---

# TDL User Guide (13 TDL-Exclusive Skills)

13 focused skills for executing an end-to-end 12-week Google Cloud AI / Agent Delta engagement (`go/delta-delivery-guide`): qualification, process ethnography and baseline evaluation metrics on the Golden Dataset → CUJ, Agentic PRD, GCP architecture and 4-pillar technical spec → Stitch/Delta-brand prototyping and goal-driven build → recursive fan-out load testing and LLM-judge statistical auditing (CLA + AUA) → value realization and closeout.

- **10 skills codify all 18 official TDL Toolbox assets** (`go/delta-delivery-guide` and linked docs, sheets, and decks).
- **3 skills are Google Cloud TDL delivery & engineering accelerators** (`gcp-agent-architecture-advisor`, `ai-value-sizing`, `claude-agent-harness`).
- Generic commodity skills (React/UI styling, TDD, ticket breakdown, browser testing, generic strategy) are intentionally delegated to upstream `skills.sh` packs — see [README.md](README.md).

Rules enforced by `scripts/validate_skills.py`:
1. **Explicit file contracts** — every skill names the artifacts it reads and writes (`docs/*.md`, `docs/*.json`, `STATE.md`).
2. **Deterministic, unit-tested scripts** where numbers are produced (ROI/NPV, agent fan-out & Vertex 5x quota sizing, LLM-judge AUA statistics, Model Garden goal loop); no hidden constants.
3. **A worked example per skill.** Four are adapted from toolbox material and one quotes a deck's real output; the rest follow one consistent *fictional* scenario (Acme P&C commercial-auto claims) and say so. Numbers attributed to a script are that script's actual output.

---

## End-to-End 12-Week Engagement Artifact Graph (phases per `go/delta-delivery-guide`)

```text
Prelude & Phase 1: Qualification, Discovery & Foundations (Weeks 0-2)
  [DISCOVERY WORKSHEET] workshop-intake                  -> docs/WORKSHOP_INTAKE.md (Starter Qs + Available/Usable/Quality Data Yardstick)
  [DISCOVERY WORKSHEET] create-delta-ucc                 -> docs/USE_CASE_CANVAS.md (Use Case Canvas + MVP Alignment Summary)
  [DISCOVERY WORKSHEET] business-process-redesign        -> docs/as_is_report.md, docs/to_be_designs.md, docs/human_agent_roles.md
  [DISCOVERY WORKSHEET] cuj-architect                    -> docs/CUJ_MAP.md (Ethnography, L1-L5 CUJ & 0.6V+0.4F Matrix)
  [GATE 1 ARTIFACT]     product-md                       -> docs/PRD.md (go/delta-prd-template Agentic PRD; worksheets can collapse here)
  [GATE 1 & 3 ARTIFACT] ai-value-sizing                  -> docs/VALUE_SIZING.md (Phase 1 ROI projection & Phase 3 measured closeout)
  [GATE 1 ARTIFACT]     gcp-agent-architecture-advisor   -> docs/ARCHITECTURE_RECOMMENDATION.md (Tier 1 No-Code vs. Tier 2/3 Code-First)
  [GATE 1 ARTIFACT]     specification-engineer           -> docs/TDD.md (go/delta-squad-agent-specs + Golden Dataset Eval Baseline)
  [UI WORKSHEET · Opt]  stitch-design                    -> docs/STITCH_PROTOTYPE.md (Custom UI only; skip for headless / Tier 1)

Phase 2: Core Build & Bi-Weekly Demo Sprints (Weeks 3-10, four 2-week sprints, Demos 1-3)
  [BUILD · Tier 2/3]    claude-agent-harness             -> verified src/ & tests/ + .harness/last_run_report.json (skip for Tier 1 No-Code)
  [GATE 2 · Tier 2/3]   agent-load-testing               -> docs/LOAD_TEST_REPORT.md (sprints 3-4: fan-out math, 5x quota, Locust SSE)
  [GATE 2 ARTIFACT]     agent-eval-statistical-auditing  -> docs/EVAL_AUDIT_REPORT.md (sprints 3-4: CLA criteria + AUA judge pipelines)

Phase 3: Final Read-Out & Close (Weeks 11-12)
  [GATE 3 ARTIFACT]     ai-value-sizing                  -> docs/VALUE_SIZING.md (measured post-launch KPIs vs. Phase 1 baseline)
  [GATE 0-3 ARTIFACT]   tdl-field-guide                  -> STATE.md, docs/DEMO_FRAME_UP.md, dual RAID logs, closeout deck, retro
```

---

## Complete Skill Catalog (13 TDL-Exclusive Skills)

### 1. Engagement Governance, Architecture, Load Testing & Judge Auditing (`delivery/`)
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[tdl-field-guide](delivery/tdl-field-guide/SKILL.md)** | Toolbox 06·07·08·09·11·12 | `STATE.md`, `docs/DEMO_FRAME_UP.md` | — | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **[gcp-agent-architecture-advisor](delivery/gcp-agent-architecture-advisor/SKILL.md)** | TDL repo-native | `docs/ARCHITECTURE_RECOMMENDATION.md` | [`model-economics-config.json`](delivery/gcp-agent-architecture-advisor/references/model-economics-config.json) | [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md) |
| **[agent-load-testing](delivery/agent-load-testing/SKILL.md)** | Toolbox 16 | `docs/LOAD_TEST_REPORT.md` | [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py), [`load-testing-and-quota-playbook.md`](delivery/agent-load-testing/references/load-testing-and-quota-playbook.md) | [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) |
| **[agent-eval-statistical-auditing](delivery/agent-eval-statistical-auditing/SKILL.md)** | Toolbox 17·18 | `docs/EVAL_AUDIT_REPORT.md` | [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py), [`cla-rubric-and-aua-methodology.md`](delivery/agent-eval-statistical-auditing/references/cla-rubric-and-aua-methodology.md) | [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) |

### 2. Discovery, Qualification & Value Realization
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[workshop-intake](workshop-intake/SKILL.md)** | Toolbox 01·10 | `docs/WORKSHOP_INTAKE.md` | [`intake-template.md`](workshop-intake/references/intake-template.md) | [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md) |
| **[create-delta-ucc](usecase-canvas/create-delta-ucc/SKILL.md)** | Toolbox 04·10 | `docs/USE_CASE_CANVAS.md` | [`ucc-template.md`](usecase-canvas/create-delta-ucc/references/ucc-template.md) | [`customer-onboarding-ucc.md`](usecase-canvas/create-delta-ucc/examples/customer-onboarding-ucc.md) |
| **[ai-value-sizing](ai-value-sizing/SKILL.md)** | TDL repo-native | `docs/VALUE_SIZING.md` | [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) | [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md) |

### 3. Workflow Redesign, CUJ Mapping, Agentic PRD & Technical Specs
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[business-process-redesign](business-process-redesign/SKILL.md)** | Toolbox 02 | `docs/as_is_report.md`, `docs/to_be_designs.md`, `docs/human_agent_roles.md` | [`agentic-process-design.md`](business-process-redesign/references/agentic-process-design.md), [`discovery-deconstruction.md`](business-process-redesign/references/discovery-deconstruction.md), [`human-agent-interaction.md`](business-process-redesign/references/human-agent-interaction.md), [`process-design-review.md`](business-process-redesign/references/process-design-review.md) | [`as_is_report.md`](business-process-redesign/examples/as_is_report.md), [`to_be_designs.md`](business-process-redesign/examples/to_be_designs.md), [`human_agent_roles.md`](business-process-redesign/examples/human_agent_roles.md) |
| **[cuj-architect](cuj-architect/SKILL.md)** | Toolbox 03 | `docs/CUJ_MAP.md` | [`output-template.md`](cuj-architect/references/output-template.md), [`quality-variants.md`](cuj-architect/references/quality-variants.md), [`schema.json`](cuj-architect/references/schema.json) | [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md), [`cloud-support-triage-cuj.md`](cuj-architect/examples/cloud-support-triage-cuj.md) |
| **[product-md](product-management/product-md/SKILL.md)** | Toolbox 05 | `docs/PRD.md` | [`prd-template.md`](product-management/product-md/references/prd-template.md) | [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md), [`enterprise-claims-agent-prd.md`](product-management/product-md/examples/enterprise-claims-agent-prd.md) |
| **[specification-engineer](utils/specification-engineer/SKILL.md)** | Toolbox 14 | `docs/TDD.md` | [`tdd-spec-template.md`](utils/specification-engineer/references/tdd-spec-template.md) | [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md), [`claims-extraction-service-tdd.md`](utils/specification-engineer/examples/claims-extraction-service-tdd.md) |

### 4. Prototyping, Brand Guidelines & Goal-Driven Build
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[stitch-design](prototyping/stitch-design/SKILL.md)** | Toolbox 13·15 | `docs/STITCH_PROTOTYPE.md` | [`stitch-mcp-workflow.md`](prototyping/stitch-design/references/stitch-mcp-workflow.md), [`ui-review-checklist.md`](prototyping/stitch-design/references/ui-review-checklist.md) | [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md), [`agent-ops-console-prototype.md`](prototyping/stitch-design/examples/agent-ops-console-prototype.md) |
| **[claude-agent-harness](ai-coding/claude-agent-harness/SKILL.md)** | TDL repo-native | Verified `src/`, `tests/`, `.harness/last_run_report.json` | [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py), [`harness-prompt-template.md`](ai-coding/claude-agent-harness/references/harness-prompt-template.md), [`pso-compliance-matrix.md`](ai-coding/claude-agent-harness/references/pso-compliance-matrix.md) | [`spec-to-production-code.md`](ai-coding/claude-agent-harness/examples/spec-to-production-code.md) |
