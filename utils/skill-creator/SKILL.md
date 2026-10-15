---
name: skill-creator
description: >
  Initialize, structure, and validate new agent skills following the Agent Skills specification
  (YAML frontmatter, concrete input/output file contracts, deterministic scripts, and mandatory
  worked examples in examples/). Trigger when the user types /skill-creator or asks to create or
  refactor a skill.
metadata:
  version: '2.0'
---

# Skill Creator (`skill-creator`)

This skill initializes and validates agent skills in this repository so every skill has clean YAML frontmatter, concrete file inputs/outputs, zero roleplay fluff, and at least one complete worked example in `examples/`.

---

## Mandatory Architectural Standards

Every skill in this repository must adhere to [agentskills-specification.md](references/agentskills-specification.md) and pass `python3 scripts/validate_skills.py`:

1. **Concrete File Contracts Over Roleplay:** State what files the skill reads, what commands/steps it runs, and what exact file it writes (e.g., `docs/PRD.md`, `docs/baseline_kpis.json`). Never include fake persona bios or nonexistent runtime state machines.
2. **3-Part Trigger `description`:** The YAML `description` (1..1024 chars) must state:
   - What artifact the skill produces
   - Explicit trigger phrases (`Triggers on: ...`)
   - Explicit negative triggers (`Do NOT trigger for ...`)
3. **Mandatory Worked Example (`examples/`):** Every skill must include at least one complete, realistic worked example in `examples/*.md` ($\ge 30$ lines) linked directly from `SKILL.md`.
4. **Zero Empty Scaffolds:** Never create `.gitkeep` files or empty `assets/`, `references/`, or `scripts/` directories. Only create a subdirectory when placing a real file inside it and linking it from `SKILL.md`.

---

## Execution Steps

### Step 1: Define the Skill Contract
Confirm with the user:
1. **Skill Name:** Lowercase kebab-case (`^[a-z0-9]+(?:-[a-z0-9]+)*$`, matching the directory name).
2. **Input → Output Contract:** What upstream files/data does it consume, and what deliverable file does it write?
3. **Triggers & Negative Triggers:** When should it activate, and which adjacent skill should handle out-of-scope requests?

### Step 2: Initialize the Skill Directory
Run [`scripts/init_skill.py`](scripts/init_skill.py) to create `<parent-dir>/<skill-name>/SKILL.md` and `<parent-dir>/<skill-name>/examples/worked-example.md`:
```bash
python3 utils/skill-creator/scripts/init_skill.py <skill-name> --path <parent-dir>
```

### Step 3: Author `SKILL.md`, `examples/`, and Optional `references/` or `scripts/`
1. Draft `SKILL.md` using [skill-template.md](references/skill-template.md).
2. Replace `examples/worked-example.md` with a complete, realistic worked deliverable (minimum 30 lines).
3. If the skill performs mathematical or statistical calculations, add a zero-dependency Python CLI under `scripts/` and link it from `SKILL.md`.

### Step 4: Run the Repository Validator
Execute `python3 scripts/validate_skills.py` from the repository root and fix any frontmatter, link, duplicate, or example errors before finishing.

---

## References, Scripts & Examples

- [Agent Skills Specification](references/agentskills-specification.md): Frontmatter, naming, and progressive disclosure rules.
- [Skill Markdown Template](references/skill-template.md): Blank `SKILL.md` template.
- [Skill Initializer CLI](scripts/init_skill.py): Creates a compliant skill folder with `SKILL.md` and `examples/worked-example.md`.
- [Worked Example: Creating & Validating `bq-cost-auditor`](examples/creating-a-new-skill-example.md): End-to-end walkthrough of scaffolding, writing, and validating a new skill.
