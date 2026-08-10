# Anthropic Loop Engineering & Agentic Workflow Best Practices

- **Primary Source**: Anthropic Engineering Research (*"Building Effective Agents"*, Dec 2024)
- **Authors**: Erik S. & Barry Zhang (Anthropic Agent Engineering Team)
- **Target Repository**: `delta-skills` Suite (v3.0.0)

---

## 1. Executive Summary

Anthropic's research across dozens of enterprise LLM deployments highlights a core finding: **The most successful agent implementations avoid bloated, opaque frameworks.** Instead, they build with simple, composable patterns directly on top of model APIs, prioritizing transparency, ground-truth environmental feedback, and clean Agent-Computer Interface (ACI) design.

---

## 2. The 5 Foundational Agentic Workflow Patterns

```
┌────────────────────────────────────────────────────────────────────────┐
│               ANTHROPIC 5 CORE AGENTIC WORKFLOW PATTERNS               │
├────────────────────────────────────────────────────────────────────────┤
│ 1. PROMPT CHAINING      : Sequenced LLM calls with programmatic gates  │
│                           validating intermediate outputs.             │
│                                                                        │
│ 2. ROUTING              : Classifying inputs and routing to specialized│
│                           subtasks or cost-optimized models (Haiku vs │
│                           Sonnet vs Opus).                             │
│                                                                        │
│ 3. PARALLELIZATION      : Executing parallel tasks via Sectioning     │
│                           (independent subtasks) or Voting (consensus).│
│                                                                        │
│ 4. ORCHESTRATOR-WORKERS : Central LLM dynamically plans & delegates    │
│                           unpredictable subtasks to worker agents.     │
│                                                                        │
│ 5. EVALUATOR-OPTIMIZER  : Generator LLM + Evaluator LLM feedback loop  │
│                           iterating until explicit criteria pass.      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Anthropic Loop Engineering Core Principles

### 1. Simplicity Over Heavy Abstractions
Avoid overly complex multi-agent frameworks that hide low-level prompts and introduce debugging opacity. Start with direct API calls and add multi-step complexity *only* when it demonstrably improves benchmark performance.

### 2. Ground-Truth Environmental Feedback
An agent loop MUST ingest ground-truth feedback from its environment at every turn (e.g. `pytest` test results, exit codes, HTTP status, compiler errors) rather than relying solely on self-reflection.

### 3. Agent-Computer Interface (ACI) Design
Treat tool definitions with the same care as Human-Computer Interfaces (HCI):
- Avoid format overhead (e.g. requiring models to manually compute chunk header line counts or string-escape complex JSON).
- Give the model room to "think" before tool calls.
- Include usage examples, edge cases, and clear boundaries between tools.

### 4. Human-in-the-Loop & Circuit Breakers
- Always set maximum iteration limits (`max_iterations=10`) to prevent infinite loop runaways.
- Include explicit human checkpoints before destructive operations (e.g. database schema migrations, code pushes).

---

## 4. How `delta-skills` Implements Anthropic Loop Engineering

| Anthropic Pattern | Implementation in `delta-skills` v3.0.0 |
| :--- | :--- |
| **Orchestrator-Workers** | `delta-orchestrator` routes tasks to specialized phase workers (`delta-discover`, `delta-plan`, `delta-build`, `delta-harden`). |
| **Evaluator-Optimizer** | `delta-harden` pairs Gemini Flash generation with Vertex AI Model Garden Opus 5 ZDR evaluation. |
| **Prompt Chaining** | Phase gate verifications (`delta_cli.py build --phase X`) enforce programmatic gates between steps. |
| **ACI Tool Design** | FastMCP template (`mcp_fastapi_sse.py`) provides clean Pydantic v2 schemas and explicit docstrings for tool interfaces. |
| **Ground-Truth Feedback** | `delta_cli.py` returns real pytest results, HTTP status, and secret scanning findings to the agent loop. |
