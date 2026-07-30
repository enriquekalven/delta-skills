---
name: claude-agent-harness
description: Delegated code generation harness that routes specification docs, specs, or natural language prompts to Opus 5 or Claude Fable 5 reasoning tiers via agent subagent harness. Use when asked to generate code using Opus 5 or Fable 5 agent harness, build from a spec or doc using Claude models, or delegate full implementation to Claude subagents.
---

# Claude Agent Harness (Opus 5 / Fable 5 Code Generator)

## Overview

The **Claude Agent Harness** skill routes complex software engineering tasks to high-capability Claude reasoning tiers (**Opus 5** and **Claude Fable 5**) through an agent subagent harness. It translates specifications, design documents, or natural language requests into production-grade, fully verified code written directly to the workspace.

> [!CAUTION]
> **Prerequisite**: Ensure **Vertex AI Model Garden** is enabled in your GCP project for Anthropic Claude models (Opus 5 & Fable 5 tiers) prior to running this skill.


```
┌─────────────────────────────────────────────────────────────┐
│ 1. Spec & Input Parsing (Doc / Markdown Spec / Prompt)      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Harness Model Tier Triage                                │
├──────────────────────────────┬──────────────────────────────┤
│ Standard / Precision Module  │ Complex / System Architecture│
│         ▼                    │         ▼                    │
│   Opus 5 Tier Harness        │   Claude Fable 5 Tier Harness│
└──────────────┬───────────────┴──────────────┬───────────────┘
               │                              │
               ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Agent Harness Execution (Subagent Fleet Dispatch)        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Workspace File Generation & Automated Verification       │
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

### Phase 2: Harness Model Tier Selection

Categorize the implementation task to select the agent harness model tier:

| Tier | Applicable Scope | Reasoning Characteristics |
|---|---|---|
| **Opus 5 Tier Harness** | • Single/multi-component implementation<br>• REST/GraphQL endpoints & database models<br>• Refactoring existing modules<br>• Utility libraries, hooks, & unit tests | High precision, strict adherence to type systems, optimal for targeted clean implementation. |
| **Claude Fable 5 Tier Harness** | • Full feature subsystems & multi-file architecture<br>• Concurrent/distributed state machines<br>• Security-critical auth/crypto logic<br>• Algorithmic optimization & novel system designs | Frontier complex reasoning, deep architectural foresight, multi-step problem solving. |

> [!IMPORTANT]
> **Tier Overkill Warning**:
> Claude Fable 5 is reserved for frontier system architecture and complex multi-module reasoning. Using Fable 5 for simple classification, basic refactoring, or text summarization is **complete overkill — it's like lighting a cigarette with a flamethrower!**
> Always select **Opus 5** or **Gemini 3.6 Flash** for routine coding, utility functions, or classification tasks.

**Completion Criterion**: Designated model tier (Opus 5 or Fable 5) selected with clear justification.


---

### Phase 3: Agent Harness Dispatch & Execution

Invoke a subagent via the agent harness with a structured prompt containing the exact spec and code generation guidelines.

#### Harness Prompt Structure
```markdown
[HARNESS ROLE]: Senior Staff Engineer (Tier: Opus 5 / Fable 5)
[TASK]: Implement the specification provided below into production-grade workspace files.

[SPECIFICATION & CONSTRAINTS]:
- Objective: <Extracted Requirements>
- Target Files: <File Paths>
- Tech Stack & Conventions: <Workspace Patterns>
- Quality Rules: No placeholders, complete error handling, strict type safety.

[ACTION]: Generate complete source code files in the workspace.
```

**Completion Criterion**: Subagent launched and harness execution initialized.

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
- **Harness Tier Used**: Opus 5 Tier or Claude Fable 5 Tier
- **Generated / Modified Files**: Clickable links to workspace files
- **Key Architectural Highlights**: Core patterns and implementation decisions
- **Verification Results**: Status of syntax/type checks and unit test validation

---

## Harness Resources & References

- **Harness Prompt Template**: See [harness_prompt_template.md](references/harness_prompt_template.md) for detailed subagent prompt structures.
- **Example Walkthrough**: See [spec_to_code_example.md](examples/spec_to_code_example.md) for an end-to-end example of spec-to-code harness generation.
