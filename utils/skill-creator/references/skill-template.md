# Skill Authoring Template (`SKILL.md`)

Copy this template when authoring a new `SKILL.md` file:

````markdown
---
name: template-skill
description: >
  State what artifact this skill produces, what inputs it reads, and when to trigger it.
  Triggers on: "<explicit trigger phrases>".
  Do NOT trigger when: "<explicit negative trigger>".
metadata:
  version: '1.0'
---

# Template Skill Name

State in 1–2 sentences what concrete file or action this skill produces (e.g., `docs/OUTPUT.md`) and which upstream files it reads.

## Step-by-Step Procedure
1. **Read Inputs:** Inspect `<input_file>` and validate required fields.
2. **Execute / Calculate:** Run `<script_or_analysis>` and apply domain rules from `references/` if needed.
3. **Write Deliverable:** Write the output to `<output_file>` and verify against the checklist below.

## Validation Checklist
- [ ] Output file exists at `<output_file>` with all required sections populated.
- [ ] All numeric calculations and citations are verified.

## References & Examples
- [Worked Example](examples/worked-example.md): Complete end-to-end input → execution → output artifact.
````
