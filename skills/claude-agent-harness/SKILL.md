---
name: claude-agent-harness
description: Delegated code generation harness that routes specification docs, specs, or natural language prompts to Zero Data Retention (ZDR) Opus 5 via Vertex AI Model Garden. Use when asked to generate code using Opus 5 agent harness, build from a spec or doc using Claude models, or delegate full implementation to Opus 5 subagent harness.
---

# Claude Agent Harness (Opus 5 Code Generator)

## Overview

The **Claude Agent Harness** skill routes complex software engineering tasks to the high-capability, Zero Data Retention (ZDR) compliant **Opus 5** model on Vertex AI Model Garden via a dedicated execution script. It translates specifications, design documents, or natural language requests into production-grade, fully verified code written directly to the workspace.

> [!CAUTION]
> **Compliance & Data Retention Requirement**:
> Only Zero Data Retention (ZDR) models (e.g. **Opus 5**) are authorized. Fable 5 has a **30-day data retention policy** and is **STRICTLY PROHIBITED** under corporate Google accounts and customer data. Ensure **Vertex AI Model Garden** is enabled in your GCP project for Opus 5 prior to running this skill.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Spec & Input Parsing (Doc / Markdown Spec / Prompt)      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Model Garden API Execution (scripts/call_opus_model_garden.py)│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Workspace File Generation & Automated Verification       │
└──────────────────────────────┘
```

---

## Workflow Protocol

### Phase 1: Input Ingestion & Requirement Mining

1. **Source Analysis**: Read and parse the provided input source:
   - **Document / Spec File**: Read via `view_file` (e.g. `docs/PRD.md`, `specs/api_spec.md`).
   - **Natural Language Request**: Extract implicit requirements, scope boundaries, and deliverables.
2. **Contract Extraction**: Extract core architectural elements:
   - Target files & directory structure
   - External dependencies & imports
   - Type definitions & interface contracts
   - Error handling & edge-case requirements

**Completion Criterion**: Explicit list of functional requirements, data contracts, and target files created.

---

### Phase 2: Model Selection & Compliance Gate

| Tier | Applicable Scope | Compliance Status |
|---|---|---|
| **Opus 5 Tier Harness** | • Full feature implementation & multi-component code<br>• REST/GraphQL endpoints & database models<br>• Refactoring existing modules<br>• Utility libraries & unit tests | **AUTHORIZED** (Zero Data Retention) |
| **Non-ZDR Models (Fable 5)** | N/A | **PROHIBITED** (30-day data retention violation) |

**Completion Criterion**: Selected ZDR-compliant Opus 5 model tier.

---

### Phase 3: Model Garden API Execution

Execute the real Model Garden Anthropic Vertex AI script via `run_command` to query Opus 5:

```bash
python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py "Implement the specification: <spec_summary>"
```

The script connects via `AnthropicVertex` SDK using your Application Default Credentials (`GOOGLE_CLOUD_PROJECT`) and returns the generated code.

---

### Phase 4: Workspace File Assembly & Verification

1. **Direct Workspace Editing**: Write complete, production-ready code files into the workspace using appropriate file writing tools.
2. **Verification Check**:
   - Run type checks / linter checks if available in the project.
   - Run test suite or create targeted unit tests to verify correctness.
   - Ensure zero placeholder comments or incomplete function stubs.

**Completion Criterion**: All code written to disk, passing verification checks with zero compilation or runtime errors.

---

### Phase 5: Implementation Delivery Report

Present a concise delivery report to the user including:
- **Harness Model Used**: Opus 5 Tier (Model Garden ZDR Endpoint `claude-3-5-opus@20241022`)
- **Generated / Modified Files**: Clickable links to workspace files
- **Key Architectural Highlights**: Core patterns and implementation decisions
- **Verification Results**: Status of syntax/type checks and unit test validation

---

## Harness Resources & References

- **Harness Prompt Template**: See [harness_prompt_template.md](references/harness_prompt_template.md) for detailed subagent prompt structures.
- **Example Walkthrough**: See [spec_to_code_example.md](examples/spec_to_code_example.md) for an end-to-end example of spec-to-code harness generation.
