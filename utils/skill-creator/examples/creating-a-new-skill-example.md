# Worked Example: Creating & Validating a New Skill (`bq-cost-auditor`)

This example walks through creating a compliant skill in `delta-skills` using [`scripts/init_skill.py`](../scripts/init_skill.py) and verifying it with `python3 scripts/validate_skills.py`.

---

## 1. Requirements & Trigger Definition
- **Skill Name:** `bq-cost-auditor`
- **Target Output Artifact:** `docs/BQ_COST_AUDIT.md`
- **Obvious Triggers:** `"audit bigquery slot usage"`, `"find expensive bigquery queries"`, `"generate BQ_COST_AUDIT.md"`
- **Negative Triggers:** Do NOT trigger for general SQL query authoring without cost/slot auditing (use `bigquery-sql`).

---

## 2. Scaffold Initialization

Run [`scripts/init_skill.py`](../scripts/init_skill.py) to create the directory structure with `SKILL.md` and `examples/worked-example.md` (no `.gitkeep` placeholder directories):

```bash
python3 utils/skill-creator/scripts/init_skill.py bq-cost-auditor --path delivery
```

Generated tree:
```text
delivery/bq-cost-auditor/
├── SKILL.md
└── examples/
    └── worked-example.md
```

---

## 3. Completed `SKILL.md` & Worked Example

### `delivery/bq-cost-auditor/SKILL.md`
```markdown
---
name: bq-cost-auditor
description: >
  Audit BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT over the last 30 days to identify top
  slot-consuming queries, unpartitioned table scans, and reservation right-sizing savings,
  writing docs/BQ_COST_AUDIT.md. Triggers on "audit bigquery costs", "find expensive bigquery
  queries". Do NOT trigger for general SQL query authoring without cost analysis.
metadata:
  version: '1.0'
---

# BigQuery Cost & Slot Auditor

This skill queries `region-<region>.INFORMATION_SCHEMA.JOBS_BY_PROJECT` over a 30-day window, isolates the top 10 queries by `total_bytes_billed` and `total_slot_ms`, and writes a remediation plan to `docs/BQ_COST_AUDIT.md`.

## Execution Steps
1. Verify active GCP project and BigQuery dataset region.
2. Execute the 30-day `INFORMATION_SCHEMA.JOBS_BY_PROJECT` diagnostic query grouping by normalized query hash.
3. Recommend partitioning/clustering keys, materialized views, or Enterprise Edition slot autoscaling caps for any query pattern exceeding 1 TB/day billed.
4. Write the findings table and annualized savings estimate to `docs/BQ_COST_AUDIT.md`.

## Validation Checklist
- [ ] Every recommended partitioning/clustering change cites the exact table, 30-day bytes billed, and query count.
- [ ] Savings math separates on-demand TB reduction from reservation slot-hour reduction.

## Examples
- [Worked Example: 30-Day BigQuery Cost Audit](examples/worked-example.md)
```

---

## 4. Repository Validation Gate

Run the repository validator from the repo root to confirm frontmatter, links, non-empty `examples/`, and zero orphan files:

```bash
python3 scripts/validate_skills.py
```

Expected output:
```text
OK: all skill frontmatter, code fences, JSON files, skill assets, worked examples, and relative links are valid.
```
