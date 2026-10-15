---
name: delta-skills-directory
description: Master registry and navigation index for the 22 skills in the delta-skills repository (9 codify the 18 TDL Toolbox assets behind go/delta-delivery-guide; 13 are repo-native). Maps each skill to its source, input files, output artifacts, scripts, and worked examples across the 12-week Delta engagement. Triggers on "list available skills", "find a skill", "which skill should I use", "tdl toolbox mapping", or "understand the capabilities of this workspace".
---

# Delta Skills Directory (22 skills)

22 skills for an end-to-end Google Cloud AI / agent engagement: discovery, process ethnography and baseline measurement → CUJ, PRD, architecture and technical spec → prototyping and goal-driven build → load testing and LLM-judge auditing → value realization and closeout. **9 skills codify the 18 TDL Toolbox assets** (`go/delta-delivery-guide` and linked docs); **13 are repo-native** — see the `Source` column and [README.md](README.md).

Rules enforced by `scripts/validate_skills.py`:
1. **Explicit file contracts** — every skill names the artifacts it reads and writes (`docs/*.md`, `docs/*.json`, `STATE.md`).
2. **Deterministic, unit-tested scripts** where numbers are produced (ROI/NPV, 50-sample baseline statistics, agent fan-out & Vertex quota sizing, LLM-judge AUA statistics, Model Garden goal loop, skill scaffolding); no hidden constants.
3. **A worked example per skill.** Four are adapted from toolbox material and one quotes a deck's real output; the rest are one consistent *fictional* scenario (Acme P&C commercial-auto claims) and say so. Numbers attributed to a script are that script's actual output.

---

## End-to-End 12-Week Engagement Artifact Graph (phases per `go/delta-delivery-guide`)

```text
Prelude & Phase 1: Qualification, Discovery & Foundations (Weeks 0-2)
  workshop-intake                  -> docs/WORKSHOP_INTAKE.md (33 Starter Qs + Data Yardstick)
  create-delta-ucc                 -> docs/USE_CASE_CANVAS.md (4-Tab UCC + MVP Alignment Summary)
  strategy-house                   -> docs/STRATEGY_HOUSE.md
  strategy-partner-orchestrator    -> docs/STRATEGY_BRIEF.md
  ai-native-strategy               -> docs/AI_STRATEGY.md
  financial-strategy               -> docs/FINANCIAL_CASE.md
  business-process-redesign        -> docs/as_is_report.md, docs/to_be_designs.md, docs/human_agent_roles.md
  cuj-architect                    -> docs/CUJ_MAP.md (4-Tab Ethnography, L1-L5 CUJ & AI Touchpoint Matrix)
  product-md                       -> docs/PRD.md (go/delta-prd-template 8-Section Agentic PRD)
  product-feature-md               -> docs/features/<feature_slug>.md
  synthetic-baseline-protocol      -> docs/baseline_kpis.json (50-Sample Historical Audit)
  gcp-agent-architecture-advisor   -> docs/ARCHITECTURE_RECOMMENDATION.md
  specification-engineer           -> docs/TDD.md (go/delta-squad-agent-specs Parts I-IV + 4 Pillars)

Phase 2: Core Build & Bi-Weekly Demo Sprints (Weeks 3-10, four 2-week sprints, Demos 1-3)
  stitch-design                    -> docs/STITCH_PROTOTYPE.md (spikes; 3-stage prototyping + Stitch MCP)
  frontend-design                  -> prototype UI & Material 3 design tokens
  prompt-engineer                  -> audited system prompts & eval cases
  claude-agent-harness             -> verified src/ & tests/ + .harness/last_run_report.json
  agent-load-testing               -> docs/LOAD_TEST_REPORT.md (sprints 3-4: fan-out math, 5x quota, Locust SSE)
  agent-eval-statistical-auditing  -> docs/EVAL_AUDIT_REPORT.md (sprints 3-4: CLA criteria + AUA judge audit)

Phase 3: Final Read-Out & Close (Weeks 11-12)
  ai-value-sizing                  -> docs/VALUE_SIZING.md (measured post-launch KPIs vs. frozen baseline)
  tdl-field-guide                  -> STATE.md, dual RAID logs, demo frame-up, closeout deck, retro
```

---

## Complete Skill Catalog (22 Skills)

### 1. Engagement delivery, load testing & judge auditing (`delivery/`)
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[tdl-field-guide](delivery/tdl-field-guide/SKILL.md)** | Toolbox 06·07·08·09·11·12 | `STATE.md`, `docs/DEMO_FRAME_UP.md` | — | [`engagement-state-and-gate-review.md`](delivery/tdl-field-guide/examples/engagement-state-and-gate-review.md) |
| **[synthetic-baseline-protocol](delivery/synthetic-baseline-protocol/SKILL.md)** | repo-native | `docs/baseline_kpis.json` | [`compute_baseline_stats.py`](delivery/synthetic-baseline-protocol/scripts/compute_baseline_stats.py) | [`claims-baseline-audit.md`](delivery/synthetic-baseline-protocol/examples/claims-baseline-audit.md) |
| **[gcp-agent-architecture-advisor](delivery/gcp-agent-architecture-advisor/SKILL.md)** | repo-native | `docs/ARCHITECTURE_RECOMMENDATION.md` | — | [`architecture-recommendation-example.md`](delivery/gcp-agent-architecture-advisor/examples/architecture-recommendation-example.md) |
| **[agent-load-testing](delivery/agent-load-testing/SKILL.md)** | Toolbox 16 | `docs/LOAD_TEST_REPORT.md` | [`calculate_agent_quotas.py`](delivery/agent-load-testing/scripts/calculate_agent_quotas.py), [`load-testing-and-quota-playbook.md`](delivery/agent-load-testing/references/load-testing-and-quota-playbook.md) | [`clinical-search-load-test-report.md`](delivery/agent-load-testing/examples/clinical-search-load-test-report.md) |
| **[agent-eval-statistical-auditing](delivery/agent-eval-statistical-auditing/SKILL.md)** | Toolbox 17·18 | `docs/EVAL_AUDIT_REPORT.md` | [`audit_llm_judge.py`](delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py), [`cla-rubric-and-aua-methodology.md`](delivery/agent-eval-statistical-auditing/references/cla-rubric-and-aua-methodology.md) | [`enterprise-analyst-aua-certification.md`](delivery/agent-eval-statistical-auditing/examples/enterprise-analyst-aua-certification.md) |

### 2. Discovery, Strategy & Value Sizing
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[workshop-intake](workshop-intake/SKILL.md)** | Toolbox 01·10 | `docs/WORKSHOP_INTAKE.md` | [`intake-template.md`](workshop-intake/references/intake-template.md) | [`acme-financial-workshop-intake.md`](workshop-intake/examples/acme-financial-workshop-intake.md) |
| **[create-delta-ucc](usecase-canvas/create-delta-ucc/SKILL.md)** | Toolbox 04·10 | `docs/USE_CASE_CANVAS.md` | [`ucc-template.md`](usecase-canvas/create-delta-ucc/references/ucc-template.md) | [`customer-onboarding-ucc.md`](usecase-canvas/create-delta-ucc/examples/customer-onboarding-ucc.md) |
| **[strategy-house](strategy-house/SKILL.md)** | repo-native | `docs/STRATEGY_HOUSE.md` | [`strategy-house-template.md`](strategy-house/references/strategy-house-template.md), [`strategy-schema.ts`](strategy-house/references/strategy-schema.ts) | [`retail-omnichannel-strategy-house.md`](strategy-house/examples/retail-omnichannel-strategy-house.md) |
| **[strategy-partner-orchestrator](strategy-agent/strategy-partner-orchestrator/SKILL.md)** *(Index: [SKILLS_INDEX.md](strategy-agent/SKILLS_INDEX.md))* | repo-native | `docs/STRATEGY_BRIEF.md` | [`mece-issue-tree.md`](strategy-agent/strategy-partner-orchestrator/references/mece-issue-tree.md), [`strategy-synthesis.md`](strategy-agent/strategy-partner-orchestrator/references/strategy-synthesis.md) | [`cloud-migration-strategy-brief.md`](strategy-agent/strategy-partner-orchestrator/examples/cloud-migration-strategy-brief.md) |
| **[ai-native-strategy](strategy-agent/ai-native-strategy/SKILL.md)** | repo-native | `docs/AI_STRATEGY.md` | [`agentic-architecture-strategy.md`](strategy-agent/ai-native-strategy/references/agentic-architecture-strategy.md), [`ai-build-buy-partner.md`](strategy-agent/ai-native-strategy/references/ai-build-buy-partner.md), [`ai-governance-safety.md`](strategy-agent/ai-native-strategy/references/ai-governance-safety.md), [`model-economics-config.json`](strategy-agent/ai-native-strategy/references/model-economics-config.json) | [`enterprise-agent-platform-strategy.md`](strategy-agent/ai-native-strategy/examples/enterprise-agent-platform-strategy.md) |
| **[financial-strategy](strategy-agent/financial-strategy/SKILL.md)** | repo-native | `docs/FINANCIAL_CASE.md` | [`business-case-builder.md`](strategy-agent/financial-strategy/references/business-case-builder.md), [`financial-diagnostics.md`](strategy-agent/financial-strategy/references/financial-diagnostics.md), [`unit-economics.md`](strategy-agent/financial-strategy/references/unit-economics.md) | [`saas-margin-and-ai-capex-plan.md`](strategy-agent/financial-strategy/examples/saas-margin-and-ai-capex-plan.md) |
| **[ai-value-sizing](ai-value-sizing/SKILL.md)** | repo-native | `docs/VALUE_SIZING.md` | [`calculate_roi.py`](ai-value-sizing/scripts/calculate_roi.py) | [`claims-triage-value-sizing.md`](ai-value-sizing/examples/claims-triage-value-sizing.md) |

### 3. Workflow Redesign, Journey Mapping & Product Specs
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[business-process-redesign](business-process-redesign/SKILL.md)** | Toolbox 02 | `docs/as_is_report.md`, `docs/to_be_designs.md`, `docs/human_agent_roles.md` | [`agentic-process-design.md`](business-process-redesign/references/agentic-process-design.md), [`discovery-deconstruction.md`](business-process-redesign/references/discovery-deconstruction.md), [`human-agent-interaction.md`](business-process-redesign/references/human-agent-interaction.md), [`process-design-review.md`](business-process-redesign/references/process-design-review.md) | [`as_is_report.md`](business-process-redesign/examples/as_is_report.md), [`to_be_designs.md`](business-process-redesign/examples/to_be_designs.md), [`human_agent_roles.md`](business-process-redesign/examples/human_agent_roles.md) |
| **[cuj-architect](cuj-architect/SKILL.md)** | Toolbox 03 | `docs/CUJ_MAP.md` | [`output-template.md`](cuj-architect/references/output-template.md), [`quality-variants.md`](cuj-architect/references/quality-variants.md), [`schema.json`](cuj-architect/references/schema.json) | [`supplier-rate-audit-cuj.md`](cuj-architect/examples/supplier-rate-audit-cuj.md), [`cloud-support-triage-cuj.md`](cuj-architect/examples/cloud-support-triage-cuj.md) |
| **[product-md](product-management/product-md/SKILL.md)** | Toolbox 05 | `docs/PRD.md` | [`prd-template.md`](product-management/product-md/references/prd-template.md) | [`ask-it-service-desk-prd.md`](product-management/product-md/examples/ask-it-service-desk-prd.md), [`enterprise-claims-agent-prd.md`](product-management/product-md/examples/enterprise-claims-agent-prd.md) |
| **[product-feature-md](product-management/product-feature-md/SKILL.md)** | repo-native | `docs/features/<feature_slug>.md` | [`feature-spec-template.md`](product-management/product-feature-md/references/feature-spec-template.md) | [`voice-capture-feature-spec.md`](product-management/product-feature-md/examples/voice-capture-feature-spec.md) |

### 4. Prototyping, Engineering & Utilities
| Skill | Source | Output Artifact(s) | Scripts & References | Worked Example(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[frontend-design](prototyping/frontend-design/SKILL.md)** | Toolbox 13 (brand) + repo-native | Production HTML/CSS/TS UI components | [`ui-review-checklist.md`](prototyping/frontend-design/references/ui-review-checklist.md) | [`agent-ops-console-prototype.md`](prototyping/frontend-design/examples/agent-ops-console-prototype.md) |
| **[stitch-design](prototyping/stitch-design/SKILL.md)** | Toolbox 15 | `docs/STITCH_PROTOTYPE.md` | [`stitch-mcp-workflow.md`](prototyping/stitch-design/references/stitch-mcp-workflow.md) | [`stitch-claims-portal-walkthrough.md`](prototyping/stitch-design/examples/stitch-claims-portal-walkthrough.md) |
| **[claude-agent-harness](ai-coding/claude-agent-harness/SKILL.md)** | repo-native | Verified `src/`, `tests/`, `.harness/last_run_report.json` | [`call_opus_model_garden.py`](ai-coding/claude-agent-harness/scripts/call_opus_model_garden.py), [`harness-prompt-template.md`](ai-coding/claude-agent-harness/references/harness-prompt-template.md), [`pso-compliance-matrix.md`](ai-coding/claude-agent-harness/references/pso-compliance-matrix.md) | [`spec-to-production-code.md`](ai-coding/claude-agent-harness/examples/spec-to-production-code.md) |
| **[specification-engineer](utils/specification-engineer/SKILL.md)** | Toolbox 14 | `docs/TDD.md` | [`tdd-spec-template.md`](utils/specification-engineer/references/tdd-spec-template.md) | [`broadcast-asset-buddy-agent-specs.md`](utils/specification-engineer/examples/broadcast-asset-buddy-agent-specs.md), [`claims-extraction-service-tdd.md`](utils/specification-engineer/examples/claims-extraction-service-tdd.md) |
| **[prompt-engineer](utils/prompt-engineer/SKILL.md)** | repo-native | Audited system prompts & eval test cases | [`prompt-audit-checklist.md`](utils/prompt-engineer/references/prompt-audit-checklist.md) | [`agent-system-prompt-refactor.md`](utils/prompt-engineer/examples/agent-system-prompt-refactor.md) |
| **[skill-creator](utils/skill-creator/SKILL.md)** | repo-native | New validated skill directory | [`init_skill.py`](utils/skill-creator/scripts/init_skill.py), [`skill-template.md`](utils/skill-creator/references/skill-template.md) | [`creating-a-new-skill-example.md`](utils/skill-creator/examples/creating-a-new-skill-example.md) |
