# Worked Example: `STATE.md`, Demo Frame-Up and Dual RAID Logs across a 12-Week Engagement

> [!NOTE]
> **Illustrative scenario, not a case study.** Acme P&C, its people and numbers are fictional; they are the same fictional thread used by the PRD, TDD, baseline, prototype and value-sizing examples in this repository so the artifacts chain together. The structures (phases, RAID columns, demo frame-up, closeout sections) follow the TDL Toolbox; the governance fields (`STATE.md`, gates, 1-in/1-out, rollback) are this repo's conventions.

Engagement: **Acme P&C — Commercial Auto Claims FNOL Intake & Triage Agent** (see [enterprise-claims-agent-prd.md](../../../product-management/product-md/examples/enterprise-claims-agent-prd.md)). Squad: TDL + FDE pair (TDM/ATL duties absorbed by the TDL, recorded below).

---

## 1. Demo frame-up (`docs/DEMO_FRAME_UP.md`), set at kickoff and re-planned each sprint

Modeled on the toolbox deck (Intel AskHR: 39 committed features, 4 pillars per demo, feature IDs from the backlog). Acme committed **14** features.

| Pillar | Feature (PRD backlog ID) | Demo 1 — core experience | Demo 2 — advanced & enterprise readiness | Demo 3 — complete |
|---|---|---|---|---|
| Multimodal intake & extraction | `CL-FNOL-0001` ACORD 25/125 + police report → 42-field canonical JSON with bounding-box citations | ✔ | | |
| Multimodal intake & extraction | `CL-FNOL-0006` Multi-VIN fleet schedule batch matcher (BigQuery) | | ✔ *(swapped in, sprint 2)* | |
| Policy & coverage verification | `CL-FNOL-0002` Deductible / endorsement / excluded-driver check via BigQuery SQL tool | ✔ | | |
| Policy & coverage verification | `CL-FNOL-0009` Subrogation recovery potential scorer | | | ✔ |
| Enterprise guardrails & HITL | `CL-FNOL-0003` `Approver` gate in Guidewire ClaimCenter for reserves > $25k or bodily injury | | ✔ | |
| Enterprise guardrails & HITL | `CL-FNOL-0011` Cloud DLP redaction + Model Armor + load test at 5× peak quota | | | ✔ |
| Continuous optimization | `CL-FNOL-0013` LLM-judge AUA audit on 200-claim golden set; eval dashboard | | | ✔ |

Demo dates (sprint read-outs): sprint 1 → Demo 1; sprint 3 → Demo 2; sprint 4 → Demo 3; next-phase plan drafted in the week-10 read-out.

---

## 2. Snapshot A — week 7 (sprint 3), rollback triggered

Integration testing in `acme-claims-nonprod` showed that calls from Agent Engine to the public NHTSA vPIC VIN API were blocked by the `acme-claims-vpc-sc` perimeter. That is a design/perimeter defect, not a code bug, so the TDL logged it in the Use Case RAID and rolled back to the spec.

```markdown
# STATE
project: "Acme P&C — Commercial Auto Claims FNOL Intake & Triage Agent"
phase: 2
week: 7
sprint: 3
squad: pair (TDL+FDE)      # TDL absorbs TDM + ATL duties (recorded 2026-08-05)
last_gate_passed: 1
gate_signoff: "Dana Morales (SVP Claims), 2026-08-22"
baseline_commit_sha: "4f91a2c8e01b3d77f89210ab44c9102e88a12b03"
action: ROLLBACK_TO_PHASE_1
rollback_reason: >
  Outbound HTTPS from Agent Engine to the public NHTSA vPIC API is blocked by
  acme-claims-vpc-sc egress rules. Update docs/ARCHITECTURE_RECOMMENDATION.md and
  docs/TDD.md to mirror the vPIC snapshot into BigQuery
  (acme_claims_edw.nhtsa_vpic_mirror via scheduled Data Transfer) before resuming sprint 3.
scope_log:
  - in: "CL-FNOL-0006 Multi-VIN fleet schedule batch matcher" (RICE 4800)
    out: "CL-FNOL-0004 PDF annotation export to broker portal" (RICE 4500)
    date: 2026-09-18
    approved_by: "Dana Morales (SVP Claims)"
use_case_raid:
  - workstream: "Agent Engine egress / VPC-SC"
    google_owner: "Alex Rivera (TDL)"
    lead_lgtmd: "Yes"
    category: "Issue"
    description: "Public NHTSA vPIC endpoint blocked by acme-claims-vpc-sc perimeter."
    date_added: "2026-09-28"
    status: "In Progress"
    latest_update: "2026-09-28: BigQuery Data Transfer mirror of vPIC requested; CISO review booked 2026-09-30."
    owner: "Victor Chen (Dir. Claims Tech)"
  - workstream: "Multimodal OCR quality"
    google_owner: "Samira Patel (FDE)"
    lead_lgtmd: "Yes"
    category: "Risk"
    description: "Faxed police reports under 150 DPI fall back to Gemini 2.5 Pro; adds latency on the extraction stage."
    date_added: "2026-09-12"
    status: "Mitigated"
    latest_update: "2026-09-20: context caching (1-h TTL) enabled on system instructions + schema; re-measure in sprint 4 load test."
    owner: "Samira Patel (FDE)"
program_raid:
  - id: "A-001"
    workstream: "Program governance & steering committee"
    google_owner: "Alex Rivera (TDL)"
    category: "Decision"
    description: "HITL role for senior adjusters in the Guidewire UI."
    date_added: "2026-08-19"
    status: "Completed"
    latest_update: "2026-08-26: 'Approver' for all bodily-injury and > $25k reserve recommendations."
    owner: "Dana Morales (SVP Claims)"
```

---

## 3. Snapshot B — week 12, close

After the BigQuery mirror and CISO re-approval (2026-09-30), the squad delivered Demo 3 in sprint 4, ran the load test and judge audit, and closed with the executive read-out.

```markdown
# STATE
project: "Acme P&C — Commercial Auto Claims FNOL Intake & Triage Agent"
phase: 3
week: 12
squad: pair (TDL+FDE)
last_gate_passed: 3
gate_signoff: "Dana Morales (SVP Claims) & Victor Chen (Dir. Claims Tech), 2026-11-06"
baseline_commit_sha: "4f91a2c8e01b3d77f89210ab44c9102e88a12b03"
action: NONE
scope_log:
  - in: "CL-FNOL-0006 Multi-VIN fleet schedule batch matcher" (RICE 4800)
    out: "CL-FNOL-0004 PDF annotation export to broker portal" (RICE 4500)
    date: 2026-09-18
    approved_by: "Dana Morales (SVP Claims)"
gate_history:
  - gate: 0
    date: 2026-08-08
    artifacts: ["Part III developer clearance checklist", "golden dataset (200 historical claims)"]
    signoff: "Victor Chen (Dir. Claims Tech)"
  - gate: 1
    date: 2026-08-22
    artifacts: ["docs/WORKSHOP_INTAKE.md", "docs/CUJ_MAP.md", "docs/PRD.md", "docs/TDD.md", "docs/as_is_report.md"]
    signoff: "Dana Morales (SVP Claims)"
  - gate: 2
    date: 2026-10-23
    artifacts: ["Demo 3 acceptance", "docs/LOAD_TEST_REPORT.md", "docs/EVAL_AUDIT_REPORT.md", "next-phase scope draft"]
    signoff: "Victor Chen (Dir. Claims Tech) — 200-claim eval F1 0.954, bodily-injury recall 1.00; judge QWK 0.84"
  - gate: 3
    date: 2026-11-06
    artifacts: ["docs/VALUE_SIZING.md", "closeout deck", "final docs/TDD.md + runbook", "retro notes"]
    signoff: "Dana Morales (SVP Claims) — measured handle time 2.8 min vs 45.0 min baseline"
use_case_raid: []
program_raid: []
```

### Closeout deck (toolbox structure)

- **The Challenge | The Vision | The Experience** — manual FNOL intake averaged 45.0 min (p90 82.0) across four systems with a 14.0% field-error rate (from `docs/as_is_report.md`); the vision was zero-touch multimodal intake with cited evidence inside ClaimCenter; before/after walk-through of one claim.
- **The Architecture | The Tech** — user workflow in ClaimCenter; Vertex AI Agent Engine, Gemini 2.5 Flash/Pro router, Document AI, BigQuery policy + VIN mirror inside `acme-claims-vpc-sc`, Cloud DLP + Model Armor.
- **The Value | The Future** — measured 2.8 min handle time, F1 0.954, bodily-injury recall 1.00 (`docs/VALUE_SIZING.md` computes the dollar case against the Phase 1 baseline); next phase: subrogation demand package generation.
