---
name: agentic-engineering
description: >
  Govern subagent task decomposition, multi-model cost routing, and subagent fleet management for enterprise AI projects.
  Triggers on: "agentic engineering", "subagent fleet routing", "optimize subagent costs", "task decomposition strategy".
---

# Agentic Engineering & Subagent Fleet Operations

Provides operational strategies for task decomposition, multi-agent fleet routing, context compression, and token cost optimization across enterprise projects.

---

## Subagent Fleet Model Routing Matrix

```
┌────────────────────────────────────────────────────────┐
│ Task Classification & Model Routing Matrix             │
├──────────────────────────┬─────────────────────────────┤
│ Fast & Lightweight Tasks │ Flash Tier (e.g. 1.5 Flash) │
│ (Search, grep, linting)  │                             │
├──────────────────────────┼─────────────────────────────┤
│ Deep Reasoning & Design  │ Pro / Opus Tier             │
│ (Arch, PRD, Refactoring) │                             │
└──────────────────────────┴─────────────────────────────┘
```

### Model Tier Routing Rules

| Workload Type | Subagent Role | Model Tier | Target Latency / Cost Goal |
|---|---|---|---|
| Codebase Research & Search | `researcher` | Flash | High speed, minimal token cost |
| Architecture & Spec Design | `architect` | Pro / Opus | Maximum reasoning quality |
| Unit Test & TDD Iteration | `test-runner` | Flash / Pro | Rapid Red-Green-Refactor loop |
| Intent & Security Audit | `auditor` | Pro / Opus | Strict policy & boundary enforcement |

---

## Subagent Fleet Governance Rules

1. **Context Boundary Isolation**: Subagents must receive concise, targeted task descriptions rather than full conversation dumps.
2. **Non-Blocking Execution**: Launch subagents backgrounded or in parallel when tasks are independent.
3. **Completion Verification**: Always verify subagent deliverables against acceptance criteria before closing subagent tasks.
4. **Token Budget Cap**: Limit recursive subagent delegation depth to max 2 levels to prevent token exhaustion.
