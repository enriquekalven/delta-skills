---
name: claude-agent-harness
description: Delegated code generation harness that routes specification docs, specs, or natural language prompts to Zero Data Retention (ZDR) Opus 5 via Vertex AI Model Garden. Use when asked to generate code using Opus 5 agent harness, build from a spec or doc using Claude models, or delegate full implementation to Opus 5 subagent harness.
---

# Claude Agent Harness (Opus 5 Code Generator)

## Overview

The **Claude Agent Harness** skill routes complex software engineering specifications directly to the high-capability, Zero Data Retention (ZDR) compliant **Opus 5** model on Vertex AI Model Garden. It converts PRDs, architecture documents, or prompts into verified, production-ready code.

> [!CAUTION]
> **Compliance & Data Retention Requirement**:
> Only Zero Data Retention (ZDR) models (e.g. **Opus 5**) are authorized. Non-ZDR models (like Fable 5) have a **30-day data retention policy** and are **STRICTLY PROHIBITED** under corporate Google accounts and customer data. Ensure **Vertex AI Model Garden** is enabled in your GCP project prior to execution.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Spec Ingestion (PRD / Markdown Spec / Natural Prompt)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Model Garden API Execution (--spec <file> or --prompt)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Direct File Writing & Local Test Verification            │
└─────────────────────────────────────────────────────────────┘
```

---

## Quickstart & Execution Protocol

### Step 1: Ingest & Mine Requirements
1. Read target specification file (e.g. `docs/PRD.md`, `specs/api_spec.md`) or parse user request.
2. Identify target workspace files, data schemas, dependencies, and boundary conditions.

### Step 2: Invoke Model Garden Opus 5
Execute the live Model Garden ZDR script via `run_command`:

**From a Specification File:**
```bash
python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py --spec <path_to_spec.md>
```

**From a Direct Prompt:**
```bash
python3 skills/claude-agent-harness/scripts/call_opus_model_garden.py --prompt "Implement async rate limiter in TypeScript"
```

> [!IMPORTANT]
> **Live API Requirement**:
> You **MUST** execute the live Model Garden script. In-context simulation is prohibited. If unauthenticated, run `gcloud auth application-default login` and export `GOOGLE_CLOUD_PROJECT`.

### Step 3: Write Code & Verify
1. **Workspace Assembly**: Write complete generated files into the workspace (zero placeholders or TODO stubs).
2. **Verification Check**:
   - Run type checks / linter checks if configured.
   - Execute project test suite (`pytest`, `npm test`, etc.) to guarantee passing code.

### Step 4: Present Delivery Report
Provide a clear summary to the user:
- **Model Endpoint**: `claude-opus-5` (Vertex AI Model Garden ZDR)
- **Files Created / Modified**: Clickable links to workspace files
- **Verification Status**: Test and lint results

---

## Resources & References

- **Prompt Templates**: See [harness_prompt_template.md](references/harness_prompt_template.md)
- **Walkthrough Example**: See [spec_to_code_example.md](examples/spec_to_code_example.md)

