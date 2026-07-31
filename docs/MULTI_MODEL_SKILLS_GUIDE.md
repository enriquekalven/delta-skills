# Using Claude Models in Antigravity

This guide provides step-by-step setup instructions and usage patterns for team members to enable **Opus 5** (Zero Data Retention) multi-model peer review and code generation inside Antigravity.

---

## 🌟 Overview of the Skills

| Skill | Purpose | Key Models Used | Compliance Status |
|---|---|---|---|
| [`claude-review`](../skills/claude-review/SKILL.md) | **Two-Pass Execution & Review Loop**: Generates baseline implementation immediately with Gemini 3.6 Flash, reviews with Opus 5 via Model Garden API, and applies revisions. | Gemini 3.6 Flash (Primary)<br>Opus 5 Tier (ZDR Reviewer) | **ZDR Compliant** |
| [`claude-agent-harness`](../skills/claude-agent-harness/SKILL.md) | **Direct High-Tier Delegation**: Translates specs, PRDs, or natural language prompts directly into production code files via Model Garden API script. | Opus 5 Tier (ZDR Code Gen) | **ZDR Compliant** |

> [!CAUTION]
> **Security Policy & Data Retention Requirement**:
> Only Zero Data Retention (ZDR) models (e.g. **Opus 5**) are authorized. Fable 5 has a **30-day data retention policy** on Anthropic servers and is **STRICTLY PROHIBITED** under corporate Google accounts and customer data.

---

## 📋 Prerequisites & Technical Architecture

### 1. Enable Vertex AI Model Garden Access
Before using `claude-review` or `claude-agent-harness`, your Google Cloud Project must have **Vertex AI Model Garden** enabled with access to Anthropic Claude model endpoints:

1. Open **Google Cloud Console** → **Vertex AI** → **Model Garden**.
2. Search for **Claude** (Anthropic model cards).
3. Click **Enable / Request Access** for your target GCP project.
4. Verify your account has `roles/aiplatform.user` IAM permissions.

### 2. Local Environment & Authentication Setup

Run the following commands in your shell:

```bash
# 1. Install the Anthropic Vertex AI Python client
pip install anthropic[vertex]

# 2. Authenticate Application Default Credentials
gcloud auth application-default login

# 3. Export your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
export CLOUD_ML_REGION="us-central1"
```

### 3. How Skills Execute Model Garden API Calls
Unlike basic prompt roleplaying, these skills execute an explicit Python helper script (`scripts/call_opus_model_garden.py`) via `run_command`:

```python
from anthropic import AnthropicVertex

# Connects via Application Default Credentials to Vertex AI Model Garden
client = AnthropicVertex(region="us-central1", project_id=os.environ["GOOGLE_CLOUD_PROJECT"])
message = client.messages.create(
    model="claude-3-5-opus@20241022",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}]
)
```

---

## 🚀 Installation & Setup Options

Teammates can enable these skills in Antigravity using either **Workspace Level** setup or **Global System-Wide** setup.

### Option A: Workspace Setup (Recommended for Project Repos)

1. Clone or pull the latest `delta-skills` repository:
   ```bash
   git clone git@github.com:enriquekalven/delta-skills.git
   cd delta-skills
   ```
2. Antigravity automatically discovers skills located in `skills/` inside active workspace projects.

---

### Option B: Global Setup (Available Across All Local Projects)

To make these skills available across **all** your local projects and repositories:

1. Create your global skills directory (if not already present):
   ```bash
   mkdir -p ~/.gemini/config/skills
   ```
2. Copy the skills into your global config:
   ```bash
   cp -r skills/claude-review ~/.gemini/config/skills/
   cp -r skills/claude-agent-harness ~/.gemini/config/skills/
   ```

---

## 💡 Use Case 1: Enable Opus 5 as a Reviewer of Gemini Code

Use **`claude-review`** when you want Gemini 3.6 Flash to rapidly build the baseline, followed by automated review and polish by Opus 5 via Vertex AI API.

### Example Prompts:
- **Simple Coding Task**:
  > *"Use `claude-review` to write a Python async rate-limiting class."*

- **Complex System Task**:
  > *"Apply `claude-review` to refactor our OAuth2 token refresh architecture and state machine across multiple services."*

---

## ⚡ Use Case 2: Jump Directly to Opus 5 for Coding

Use **`claude-agent-harness`** when you have a PRD, specification document, or complex prompt and want Opus 5 to directly generate the production implementation via Model Garden API.

### Example Prompts:
- **From a Spec / PRD Document**:
  > *"Use `claude-agent-harness` to implement the specification in [PRD.md](file:///path/to/docs/PRD.md)."*

- **Precision Code Generation (Opus 5 Harness)**:
  > *"Delegate implementation of this TypeScript REST endpoint to the Opus 5 `claude-agent-harness`."*

- **Automated Default Workflow (Bypass Gemini to Default to Opus 5)**:
  To automatically route **all** code implementation and refactoring requests to the Opus 5 `claude-agent-harness` by default, append this rule to your `~/.gemini/config/AGENTS.md` (or `.agents/AGENTS.md`):
  ```markdown
  - Always use the claude-agent-harness skill (Opus 5 tier) for all code writing, feature implementation, and refactoring tasks.
  ```

---

## 🔍 Verification & Troubleshooting

- **Check Active Skills**:
  Ask Antigravity: *"List available skills"* or check your context to confirm `claude-review` and `claude-agent-harness` are recognized.
- **Verify API Calls**:
  Inspect the terminal execution log when `scripts/call_opus_model_garden.py` runs to verify live communication with `claude-3-5-opus@20241022` on Vertex AI.
