# Google Cloud PSO Compliance & Security Matrix: Claude Agent Harness

This document outlines the enterprise security, governance, and architectural compliance standards enforced by the **Claude Agent Harness** AI coding solution. It aligns with Google Cloud Professional Services Organization (PSO) delivery standards for enterprise customer engagements.

---

## 1. Compliance Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ Enterprise Customer Security Perimeter (VPC-SC / Cloud IAM)                             │
│                                                                                         │
│  ┌───────────────────────┐         ┌────────────────────────┐                           │
│  │ Spec / PRD Document   │ ──────▶ │ Claude Agent Harness   │                           │
│  │ (Architecture / Code) │         │ (Context & Gatekeeper) │                           │
│  └───────────────────────┘         └───────────┬────────────┘                           │
│                                                │                                        │
│                 Google Cloud Application Default Credentials (ADC) / IAM                │
│                 `roles/aiplatform.user` / Workload Identity Federation                  │
│                                                │                                        │
│                                                ▼                                        │
│                                    ┌────────────────────────┐                           │
│                                    │ Vertex AI Model Garden │                           │
│                                    │ API Endpoint           │                           │
│                                    └───────────┬────────────┘                           │
│                                                │                                        │
│                                                ▼                                        │
│                             ┌──────────────────────────────────────┐                    │
│                             │ Anthropic Claude Opus 5 on Vertex AI │                    │
│                             │  - Zero Data Retention (ZDR)         │                    │
│                             │  - Enterprise SLA & Encryption       │                    │
│                             │  - Customer Data Isolation           │                    │
│                             └──────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Compliance Pillars

| Pillar | Requirement | PSO Standard Implementation | Verification Mechanism |
| :--- | :--- | :--- | :--- |
| **Data Retention (ZDR)** | Zero Data Retention on inference prompts and outputs | Exclusively routes requests to Anthropic Claude Opus 5 on Vertex AI Model Garden under Google Cloud commercial ZDR terms. Prompts and completions are never retained, logged by model providers, or used for model training. | Commercial Enterprise Agreement & Vertex AI Data Governance SLAs. |
| **Identity & Access** | Least-privilege IAM; zero hardcoded credentials | Uses Application Default Credentials (ADC) via `gcloud auth application-default login`, Google Service Accounts, or Workload Identity Federation. Requires `roles/aiplatform.user`. | Pre-flight credential check via `google.auth.default()`. |
| **Data Residency** | Control over physical geographic data processing | Dynamic region selection (`CLOUD_ML_REGION` or `--region`), allowing routing to `us-central1`, `europe-west1`, or other authorized Vertex AI regional endpoints. | Regional endpoint validation in script flags. |
| **Perimeter Security** | VPC Service Controls (VPC-SC) readiness | Operates within Google Cloud VPC perimeters without traversing public third-party SaaS endpoints. | Google API endpoint resolution within private Google Access / PSC. |
| **Code Completeness** | Zero placeholder / zero hallucination delivery | Strict prompt engineering and post-generation gatekeeping prohibit `TODO`, `pass`, or truncated code stubs. | Automated lint and AST parsing passes before delivery. |
| **Quality Verification** | Multi-tier validation before disk modification | 4-tier verification gate: Syntax -> Linting -> Type Check -> Test Suite execution. | Automated CLI test execution (`pytest`, `npm test`). |

---

## 3. Identity and Access Management (IAM) Roles

To execute the Claude Agent Harness in an enterprise environment, the calling identity (user account or service account) must hold the following minimum permissions:

- **Required Role**: `roles/aiplatform.user` (Vertex AI User)
- **Minimum Permissions**:
  - `aiplatform.endpoints.predict`
  - `aiplatform.models.list`
  - `resourcemanager.projects.get`

### Service Account Example (Terraform)
```hcl
resource "google_project_iam_member" "ai_coding_harness" {
  project = var.project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:ai-coding-bot@${var.project_id}.iam.gserviceaccount.com"
}
```

---

## 4. Zero Data Retention (ZDR) Guarantees

Under the Google Cloud Vertex AI terms for third-party models in Model Garden:
1. **No Foundation Model Training**: Customer prompts, inputs, specifications, and generated code are **never** used to train, retrain, or improve foundational models by Google or Anthropic.
2. **Ephemeral Inference**: Inference data is processed in-memory and discarded upon completion of the response stream.
3. **Encryption**: All data in transit is encrypted using TLS 1.3; data at rest in Vertex AI is encrypted with Google-managed or Customer-Managed Encryption Keys (CMEK).

---

## 5. Pre-Flight Checklist for PSO Engagements

Before running the harness in customer environments:
1. Verify Google Cloud Project ID is active:
   ```bash
   gcloud config get-value project
   ```
2. Ensure Vertex AI API is enabled:
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```
3. Verify Application Default Credentials:
   ```bash
   gcloud auth application-default print-access-token
   ```
4. Verify required Python packages:
   ```bash
   pip install --upgrade "anthropic[vertex]" google-auth
   ```
