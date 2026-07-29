---
name: skill-stocktake
description: >
  Audit tool and skill availability across workspace environments to verify all required phase capability slots are installed and operational.
  Triggers on: "skill stocktake", "audit skills", "verify capabilities", "check installed tools", "skill audit".
---

# Skill Stocktake & Capability Slot Audit

Audits the local workspace, environment configuration, and active plugins to verify that all required capability slots (`#CAPABILITY: Slot-Name`) are available prior to executing project phases.

---

## 4-Step Stocktake Audit Pipeline

```
1. Scan Plugin Registry --> 2. Check Capability Slots --> 3. Identify Gaps --> 4. Generate Stocktake Report
```

### Step 1: Plugin Registry Scan
Inspect global config (`~/.gemini/config/plugins/` or equivalent) and workspace `.agents/` directories to index active skills.

### Step 2: Capability Slot Verification
Map installed skills against required phase capabilities:

| Capability Slot | Expected Primary Tool | Status |
|---|---|---|
| `#CAPABILITY: Customer-Intake` | `workshop-intake` | Checked |
| `#CAPABILITY: PRD-Creation` | `create-prd` | Checked |
| `#CAPABILITY: GCP-Architecture-Advisor` | `gcp-agent-architecture-advisor` | Checked |
| `#CAPABILITY: TDD-Build` | `test-driven-development` | Checked |
| `#CAPABILITY: Agent-Evaluation` | `google-agents-cli-eval` | Checked |

### Step 3: Gap Remediation
If a required capability slot is missing, generate the exact CLI command to install the missing skill package:
```bash
npx skills add <repository>/<skill-name>
```

### Step 4: Output `docs/SKILL_STOCKTAKE.md`
Write the audit log and capability mapping status to `docs/SKILL_STOCKTAKE.md`.
