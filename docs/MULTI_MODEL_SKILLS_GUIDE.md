# Using Claude Models in Antigravity / Jetski

This guide provides step-by-step setup instructions and usage patterns for team members to enable **Opus 5** and **Claude Fable 5** multi-model peer review and code generation inside Antigravity / Jetski.

---

## 🌟 Overview of the New Skills

| Skill | Purpose | Key Models Used |
|---|---|---|
| [`execute-review-revise`](../skills/execute-review-revise/SKILL.md) | **Two-Pass Execution & Review Loop**: Generates baseline implementation immediately with Gemini 3.6 Flash, triages complexity, reviews with Opus 5 (simple) or Fable 5 (complex), and applies revisions. | Gemini 3.6 Flash (Primary)<br>Opus 5 Tier (Simple Reviewer)<br>Claude Fable 5 Tier (Complex Reviewer) |
| [`claude-agent-harness`](../skills/claude-agent-harness/SKILL.md) | **Direct High-Tier Delegation**: Translates specs, PRDs, or natural language prompts directly into production code files via Opus 5 or Fable 5 agent harnesses. | Opus 5 Tier (Precision Code Gen)<br>Claude Fable 5 Tier (System Architecture) |

> [!IMPORTANT]
> **Model Routing & Efficiency Note**:
> Claude Fable 5 is designed for frontier reasoning, complex multi-module architecture, distributed concurrency, and security-critical systems. Using Fable 5 for simple classification, basic bug fixes, or text summarization is **complete overkill — it's like lighting a cigarette with a flamethrower!**
> 
> For standard coding, utility functions, or classification/summarization tasks, always stick with **Gemini 3.6 Flash** or the **Opus 5 Tier** to optimize speed and compute efficiency.


---

## 📋 Prerequisites

> [!CAUTION]
> **Mandatory Setup Requirement**:
> Before using `execute-review-revise` or `claude-agent-harness`, your Google Cloud Project must have **Vertex AI Model Garden** enabled with access to Anthropic Claude model endpoints (Opus 5 & Fable 5 tiers).
> 
> **Setup Steps**:
> 1. Open **Google Cloud Console** → **Vertex AI** → **Model Garden**.
> 2. Search for **Claude** (Anthropic model cards).
> 3. Click **Enable / Request Access** for your target GCP project.
> 4. Verify your identity/service account has `roles/aiplatform.user` IAM permissions.

---

## 🚀 Installation & Setup Options

Teammates can enable these skills in Jetski using either **Workspace Level** setup or **Global System-Wide** setup.

### Option A: Workspace Setup (Recommended for Project Repos)

1. Clone or pull the latest `delta-skills` repository:
   ```bash
   git clone git@github.com:enriquekalven/delta-skills.git
   cd delta-skills
   ```
2. Jetski automatically discovers skills located in `skills/` inside active workspace projects.

---

### Option B: Global Setup (Available Across All Local Projects)

To make these skills available across **all** your local projects and repositories:

1. Create your global skills directory (if not already present):
   ```bash
   mkdir -p ~/.gemini/config/skills
   ```
2. Copy the skills into your global config:
   ```bash
   cp -r skills/execute-review-revise ~/.gemini/config/skills/
   cp -r skills/claude-agent-harness ~/.gemini/config/skills/
   ```

---

## 💡 Use Case 1: Enable Opus 5 / Fable 5 as a Reviewer of Gemini Code

Use **`execute-review-revise`** when you want Gemini 3.6 Flash to rapidly build the baseline, followed by automated review and polish by an Opus 5 or Fable 5 reviewer.

```
                    ┌────────────────────────┐
                    │  1. Primary Build      │
                    │  (Gemini 3.6 Flash)    │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │  2. Complexity Triage  │
                    └─────┬────────────┬─────┘
            Simple        │            │       Complex
            ┌─────────────▼──┐      ┌──▼─────────────┐
            │ Opus 5 Reviewer│      │Fable 5 Reviewer│
            └─────────────┬──┘      └──┬─────────────┘
                          └──────┬─────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  3. Refine & Polish    │
                    │  (Gemini 3.6 Flash)    │
                    └────────────────────────┘
```

### Example Prompts:

- **Simple Coding Task (Triggers Opus 5 Reviewer)**:
  > *"Use `execute-review-revise` to write a Python async rate-limiting class."*

- **Complex System Task (Triggers Fable 5 Reviewer)**:
  > *"Apply `execute-review-revise` to refactor our OAuth2 token refresh architecture and state machine across multiple services."*

- **Automated Default Workflow (Optional)**:
  To enforce this two-pass workflow on **all** coding prompts automatically, append the following line to your `~/.gemini/config/AGENTS.md` (or `.agents/AGENTS.md`):
  ```markdown
  - Always use the execute-review-revise skill when asked to write or modify code.
  ```

---

## ⚡ Use Case 2: Jump Directly to Opus 5 or Fable 5 for Coding

Use **`claude-agent-harness`** when you have a PRD, specification document, or complex prompt and want Opus 5 or Fable 5 to directly generate the production implementation.

### Example Prompts:

- **From a Spec / PRD Document**:
  > *"Use `claude-agent-harness` to implement the specification in [PRD.md](file:///path/to/docs/PRD.md)."*

- **Precision Code Generation (Opus 5 Harness)**:
  > *"Delegate implementation of this TypeScript REST endpoint to the Opus 5 `claude-agent-harness`."*

- **Complex Subsystem Architecture (Fable 5 Harness)**:
  > *"Use `claude-agent-harness` with Claude Fable 5 tier to architect and generate our real-time WebSocket event broker."*

---

## 🔍 Verification & Troubleshooting

- **Check Active Skills**:
  Ask Jetski: *"List available skills"* or check your context to confirm `execute-review-revise` and `claude-agent-harness` are recognized.
- **Inspect Review Output**:
  During Phase 3 of `execute-review-revise`, Jetski will render a **Peer Review Report** showing the verdict (`APPROVED` or `NEEDS_REVISION`) and specific findings before applying changes.
