# Security & Data-Governance Notes: Claude Agent Harness

This document covers the security controls the **Claude Agent Harness** actually implements, and the data-governance facts to confirm before using it on a customer engagement.

> [!WARNING]
> **Confirm data-handling terms before you rely on them.** Retention, logging, and training commitments for third-party models on Vertex AI come from your organization's Google Cloud agreement, the model's Model Garden terms, and project settings (for example, caching and abuse-monitoring configuration). **Neither the harness nor the model can attest to them.** Check the current Vertex AI data-governance documentation and your contract before telling a customer that data is "zero retention".

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ Customer / engagement environment (IAM, optionally VPC-SC)                              │
│                                                                                         │
│  ┌───────────────────────┐       ┌──────────────────────────────┐                       │
│  │ Spec / PRD + Goal     │ ────▶ │ Goal-loop harness (local)    │── acceptance cmds ──┐ │
│  │ Contract (--verify)   │       │ sandboxed file tools only    │◀─ exit codes ───────┘ │
│  └───────────────────────┘       └──────────────┬───────────────┘                       │
│                                                 │ ADC / Workload Identity               │
│                                                 │ roles/aiplatform.user                 │
│                                                 ▼                                       │
│                                   ┌──────────────────────────────┐                      │
│                                   │ Vertex AI Model Garden       │                      │
│                                   │ Anthropic Claude (regional)  │                      │
│                                   └──────────────────────────────┘                      │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Controls

| Area | Requirement | How the harness implements it | How to verify |
| :--- | :--- | :--- | :--- |
| **Data handling** | Inference data governed by Google Cloud terms | Requests go only to Anthropic Claude on Vertex AI Model Garden, in your project and region. No third-party SaaS endpoints. | Confirm retention and training terms in your agreement and the Vertex AI docs (see warning above). |
| **Identity & access** | Least-privilege IAM; no hardcoded credentials | Application Default Credentials (`gcloud auth application-default login`), service accounts, or Workload Identity Federation, resolved by the Anthropic Vertex client. No API keys. | A failed auth is reported as `api_error` with a re-login hint. The identity needs `roles/aiplatform.user`. |
| **Data residency** | Control over processing region | `--region` / `CLOUD_ML_REGION` pick the regional endpoint. | `region` field in the JSON report. |
| **Perimeter** | VPC-SC compatibility | Calls only Google APIs (`*-aiplatform.googleapis.com`). | Test inside your perimeter; add Vertex AI to the service perimeter. |
| **Workspace sandbox** | Model output can't write outside the target repo | Every tool path is resolved (including symlinks) and must stay inside `--workspace`. Absolute paths, `..` escapes, and `.git/` are rejected. 1 MB write cap. | Offline unit tests in [test_call_opus_model_garden.py](../scripts/test_call_opus_model_garden.py). |
| **Command execution** | No arbitrary shell from model output | The model can only trigger the operator-defined `--verify` commands, run without a shell. Shell operators are rejected. | Code review of `run_verification` / `parse_verify_command` in [call_opus_model_garden.py](../scripts/call_opus_model_garden.py). |
| **Code completeness** | No placeholder delivery | Completion is rejected if files written in the run contain `TODO`/`FIXME`/`XXX` markers (except `TODO(security)`) or "implement later"-style phrases. | `declare_goal_complete` rejection messages; unit tests. |
| **Quality verification** | Code verified before it's accepted | Goal loop: the harness re-runs every acceptance command (syntax → lint → types → tests) before accepting completion. The host agent re-runs them again. | JSON report `acceptance` array plus an independent re-run. |

---

## 3. IAM Roles

The calling identity (user or service account) needs:

- **Role:** `roles/aiplatform.user` (Vertex AI User)
- **Also:** access to the project where the Claude model is enabled in Model Garden.

### Service Account Example (Terraform)
```hcl
resource "google_project_iam_member" "ai_coding_harness" {
  project = var.project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:ai-coding-bot@${var.project_id}.iam.gserviceaccount.com"
}
```

---

## 4. What You May and May Not Claim to a Customer

| ✅ Supported by this harness | ⚠️ Needs contractual or documentation confirmation |
|---|---|
| Requests go to Vertex AI in project `X`, region `Y` | "Zero data retention" |
| No API keys; ADC / Workload Identity only | "Never used for training" (confirm current Model Garden terms) |
| Model output was sandboxed to the repo, and only operator-defined commands ran | Specific encryption or TLS versions, CMEK coverage |
| Acceptance commands passed (with the report attached) | Any certification (SOC 2, HIPAA, etc.) for this workflow |

---

## 5. Pre-Flight Checklist

1. Project is set:
   ```bash
   gcloud config get-value project
   ```
2. Vertex AI API is enabled:
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```
3. ADC is valid:
   ```bash
   gcloud auth application-default print-access-token > /dev/null && echo ok
   ```
4. SDK is installed in the project environment (not globally):
   ```bash
   pip install "anthropic[vertex]"
   ```
5. The Claude model you pass as `--model` is enabled in Model Garden for your project and region.
