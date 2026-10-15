# AI-Enhanced CUJ Map: Cloud Database Incident Triage & Remediation

## 1. STRATEGIC CONTEXT
- **Outcome**: Enterprise Cloud Support reduces Severity-1/Severity-2 database incident Mean Time to Resolution (MTTR) from 46 minutes to under 8 minutes while maintaining >=98% remediation safety.
- **Stages**: `1. Triage & Correlation` → `2. Root-Cause Diagnosis & Patch Approval`
- **Operating Level**: `Task` (The ADK Diagnostic Agent replaces manual log-gathering and correlation tasks, and augments the human SRE's remediation approval task).

## 2. PERSONA (The 'Who')
- **Bio**: Priya Nair, L2 Cloud Database Site Reliability Engineer (SRE). Manages 40+ escalated Cloud SQL and AlloyDB production incidents per week across multi-region customer environments.
- **Expectations**: Zero manual copy-pasting of project IDs across Cloud Logging, Monitoring, and Jira; immediate pinpointing of lock contention or replication lag with cite-linked log lines and a dry-run verified SQL/Terraform mitigation command.

## 3. JOURNEY DETAILS (The 'How')
- **CUJ Header**: Triage and Diagnose Production Database Latency Spike
- **Reframed Goal**: As a result of completing these tasks, I will have a verified root-cause diagnosis with linked Cloud Logging evidence and a sandbox-tested mitigation command ready for one-click approval.
- **Motivations**: Prevent customer SLA breaches during peak traffic without running risky manual DDL/configuration changes under pressure.
- **Challenges**: Today, correlating PagerDuty alerts with Cloud Logging slow-query logs, recent Terraform deployment diffs, and BigQuery historical incident tickets takes 35+ minutes of manual tab-switching.

## 4. AI VALUE PROPOSITION (Linguistic Formulation)
- **Core Feature**: AI **Replaces** manual log retrieval and deployment-diff correlation tasks by automatically assembling a cite-linked root-cause diagnostic packet within 45 seconds of alert firing.
- **Core Feature**: AI **Augments** the SRE mitigation verification task by generating a dry-run validated configuration patch with explicit blast-radius metrics before human sign-off.
- **Integration**: AI **Integrates with** PagerDuty, Google Cloud Logging, GitHub Actions, and Jira Service Management to correlate telemetry and execute approved runbooks.

---

## 5. SCHEMA-VALIDATED CUJ PAYLOAD (`references/schema.json`)

```json
{
  "outcome": "Reduce enterprise Cloud SQL/AlloyDB Severity-1/2 incident MTTR from 46 minutes to under 8 minutes with zero unapproved production writes.",
  "stages": [
    {
      "name": "Triage & Telemetry Correlation",
      "goal": "Incoming incident alert is enriched with correlated logs, metric anomalies, and recent deployment diffs within 60 seconds.",
      "cujs": [
        {
          "name": "Triage Production Database Latency Alert",
          "goal": "As a result of completing these tasks, I will have a unified incident packet isolating the exact query signature or deployment commit causing the latency spike.",
          "tasks": [
            {
              "action": "Collect incident telemetry across monitoring and logging systems",
              "steps": [
                {
                  "interaction": "Ingest PagerDuty webhook payload and extract GCP project_id, instance_id, and alert window",
                  "intent": "Retrieve",
                  "ai_effect": "Replace",
                  "quality_metrics": [
                    "Completeness",
                    "Contextual relevance"
                  ]
                },
                {
                  "interaction": "Query Cloud Logging and Cloud Monitoring for top 5 blocking SQL fingerprints and CPU/IO saturation curves",
                  "intent": "Retrieve",
                  "ai_effect": "Replace",
                  "quality_metrics": [
                    "Factuality",
                    "Contextual relevance"
                  ]
                }
              ]
            },
            {
              "action": "Correlate anomaly window against recent infrastructure and schema changes",
              "steps": [
                {
                  "interaction": "Diff GitHub Terraform and Liquibase commits merged within 4 hours of anomaly onset",
                  "intent": "Summarize",
                  "ai_effect": "Replace",
                  "quality_metrics": [
                    "Factuality",
                    "Completeness"
                  ]
                },
                {
                  "interaction": "Match failure signature against BigQuery vector index of 10,000 resolved postmortems",
                  "intent": "Answer",
                  "ai_effect": "Augment",
                  "quality_metrics": [
                    "Factuality",
                    "Contextual relevance"
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "Remediation Proposal & HITL Execution",
      "goal": "Safe mitigation is validated in dry-run and applied with human SRE sign-off.",
      "cujs": [
        {
          "name": "Approve and Execute Database Mitigation Runbook",
          "goal": "As a result of completing these tasks, I will have restored database p99 latency below SLA threshold and logged the audit trail to Jira.",
          "tasks": [
            {
              "action": "Draft and validate mitigation command",
              "steps": [
                {
                  "interaction": "Generate parameterized gcloud sql flags patch or pg_terminate_backend script and execute read-only dry-run validation",
                  "intent": "Execute",
                  "ai_effect": "Augment",
                  "quality_metrics": [
                    "Factuality",
                    "Completeness"
                  ]
                },
                {
                  "interaction": "SRE reviews blast-radius summary and clicks Approve in Slack/Console HITL gate",
                  "intent": "Route",
                  "ai_effect": "Integrate with",
                  "quality_metrics": [
                    "Contextual relevance"
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
