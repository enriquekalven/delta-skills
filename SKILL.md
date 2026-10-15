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
  workshop-intake                  -> docs/WORKSHOP_INTAKE.md (33 Starter Qs + 6-Dim Data Yardstick)
  create-delta-ucc                 -> docs/USE_CASE_CANVAS.md (4-Tab UCC + MVP Alignment Summary)
  business-process-redesign        -> docs/as_is_report.md, docs/to_be_designs.md, docs/human_agent_roles.md
  cuj-architect                    -> docs/CUJ_MAP.md (4-Tab Ethnography, L1-L5 CUJ & 0.6V+0.4F Matrix)
  product-md                       -> docs/PRD.md (go/delta-prd-template 8-Section Agentic PRD)
  gcp-agent-architecture-advisor   -> docs/ARCHITECTURE_RECOMMENDATION.md (Tier 1/2/3 + Model Economics)
  specification-engineer           -> docs/TDD.md (go/delta-squad-agent-specs Parts I-IV + Golden Dataset Eval Baseline)

Phase 2: Core Build & Bi-Weekly Demo Sprints (Weeks 3-10, four 2-week sprints, Demos 1-3)
  stitch-design                    -> docs/STITCH_PROTOTYPE.md (3-stage prototyping, Delta Brand #13, Stitch MCP)
  claude-agent-harness             -> verified src/ & tests/ + .harness/last_run_report.json
  agent-load-testing               -> docs/LOAD_TEST_REPORT.md (sprints 3-4: fan-out math, 5x quota, Locust SSE)
  agent-eval-statistical-auditing  -> docs/EVAL_AUDIT_REPORT.md (sprints 3-4: 27 CLA criteria + 3 AUA pipelines)

Phase 3: Final Read-Out & Close (Weeks 11-12)
  ai-value-sizing                  -> docs/VALUE_SIZING.md (measured post-launch KPIs vs. Phase 1 baseline)
  tdl-field-guide                  -> STATE.md, dual RAID logs, demo frame-up, closeout deck, retro
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

---

## When Is This Worth It? 3-Tier Engagement Sizing Matrix (`scripts/evaluate_1000x_personas.py`)

Validated across **50 Enterprise Use Cases × 20 Customer Stakeholder Personas = 1,000 simulated engagements (`13,000` individual skill evaluations)** (`python3 scripts/evaluate_1000x_personas.py --strict`), `calculate_roi.py` automatically classifies every engagement into one of three execution modes in Week 0 so teams never over-engineer small bots or under-govern core builds:

| Engagement Mode | Qualifying Criteria (`project_worth_verdict`) | Skills to Run | Effort (`Manual` $\rightarrow$ `Skill`) | 50-Use-Case Portfolio Economics |
| :--- | :--- | :--- | :--- | :--- |
| **1. Full 13-Skill 12-Week Delta Mode (`WORTH_IT_FULL_13_SKILL`)** | Core Tier 2 / Tier 3 multi-agent build; **Base & Bear 3-Year NPV > `$0`** and **Payback $\le 18$ mos** (`SOM >= 10,000` units/yr or high-value regulated workflows). | **All 13 Skills** (Prelude $\rightarrow$ Phase 1 $\rightarrow$ Phase 2 $\rightarrow$ Phase 3) | `470.0h` $\rightarrow$ **`73.5h`** (`396.5h` saved / `84.4%` TTM compression) | **40 / 50 Use Cases (80%)**: Mean Base 3-Yr NPV **`+$869,390`**, Mean Bear 3-Yr NPV **`+$205,498`**, Mean Payback **`5.7 mos`**, Token OpEx **`$4,855/yr`** (at 60% context cache). |
| **2. Fast-Track 5-Skill Lite Mode (`WORTH_IT_FAST_TRACK_5_SKILL`)** | Departmental / Tier 1 Gemini Enterprise connector scope (`SOM ~2,500–5,000` units/yr) where a full 12-week `$160k+` CapEx would make Bear NPV negative (`-$228k`), but a **2-week lean sprint (15% CapEx/OpEx)** yields **Lite Base & Bear NPV > `$0`**. | **5 Skills Only:** `workshop-intake` $\rightarrow$ `create-delta-ucc` $\rightarrow$ `gcp-agent-architecture-advisor` (Tier 1) $\rightarrow$ `stitch-design` $\rightarrow$ `ai-value-sizing` | `110.0h` $\rightarrow$ **`18.5h`** (2-week TDL+FDE pair sprint) | **6 / 50 Use Cases (12%)**: Flips Bear-case 3-Yr NPV from **`-$228,092` (CFO Reject)** to **`+$9,985` (CFO Approve)**. |
| **3. Prelude Gate-0 Stop / Kill (`KILL_OR_RE_SCOPE_AT_GATE_0`)** | Low volume (`SOM < 1,000`/yr) or unindexed/air-gapped data (`SCDF <= 0.20` — e.g., handwritten faxes, unscanned microfiche) where even Lite Mode has negative NPV. | **Stop after 2 Prelude Skills:** `workshop-intake` + `ai-value-sizing` | **`4.5h`** (Fail-fast in Week 0 before writing code) | **4 / 50 Use Cases (8%)**: Catches & kills unviable traps in Week 0, saving **`$230k–$260k` in wasted build CapEx per trap**. |

