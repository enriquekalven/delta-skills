#!/usr/bin/env python3
"""Initialize a new skill directory with standard Agent Skills structure and a worked example."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_NAME_LEN = 64


def validate_skill_name(skill_name: str) -> str:
    """Validate skill_name against the Agent Skills naming specification."""
    cleaned = skill_name.strip()
    if not cleaned:
        raise ValueError("skill name must be non-empty")
    if len(cleaned) > MAX_NAME_LEN:
        raise ValueError(f"skill name exceeds {MAX_NAME_LEN} characters: {cleaned!r}")
    if not SKILL_NAME_RE.match(cleaned):
        raise ValueError(
            f"skill name {cleaned!r} must be lowercase alphanumeric with single hyphens"
        )
    return cleaned


def create_skill(skill_name: str, base_path: str = ".") -> Path:
    """Initialize a new skill directory confined within base_path with SKILL.md and examples/."""
    valid_name = validate_skill_name(skill_name)
    real_base = os.path.realpath(base_path)
    skill_dir = os.path.realpath(os.path.join(real_base, valid_name))
    if not skill_dir.startswith(real_base + os.sep):
        raise ValueError(f"skill directory escapes base_path: {skill_name!r}")

    examples_dir = Path(skill_dir) / "examples"
    os.makedirs(examples_dir, exist_ok=True)

    title = valid_name.replace("-", " ").title()
    example_path = examples_dir / "worked-example.md"
    if not example_path.exists():
        example_path.write_text(
            f"""# Worked Example: {title}

## 1. Input Context
Describe the exact input files, parameters, or prompt that triggers `{valid_name}`.
- Input artifact: `docs/WORKSHOP_INTAKE.md`
- Target output: `docs/{valid_name.upper().replace('-', '_')}.md`

## 2. Step-by-Step Execution
1. Parse and validate all required fields from the input artifact.
2. Execute the domain logic or helper script and verify numerical outputs.
3. Write the formatted markdown or JSON output to the target artifact path.

## 3. Verified Output Artifact
Provide a complete, realistic deliverable produced by `{valid_name}` that passes all validation checks.
""",
            encoding="utf-8",
        )

    skill_md_path = Path(skill_dir) / "SKILL.md"
    if not skill_md_path.exists():
        skill_md_path.write_text(
            f"""---
name: {valid_name}
description: >
  Describe what {valid_name} produces, its required inputs, and its output file path.
  Triggers on: "<obvious trigger phrases>".
  Do NOT trigger when: "<negative trigger conditions>".
metadata:
  version: '1.0'
---

# {title}

State the concrete input files, execution steps, and output file path for `{valid_name}`.

## Execution Steps
1. Read required inputs and verify preconditions.
2. Execute the workflow steps and write the target output artifact.
3. Verify the deliverable against the Validation Checklist.

## Validation Checklist
- [ ] All required sections and metrics are populated with verified data.
- [ ] Output passes `python3 scripts/validate_skills.py`.

## Examples
- [Worked Example: {title}](examples/worked-example.md)
""",
            encoding="utf-8",
        )

    print(f"Successfully initialized skill '{valid_name}' at {skill_dir}")
    return Path(skill_dir)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Initialize a new agent skill.")
    parser.add_argument("name", help="Skill directory name (lowercase kebab-case)")
    parser.add_argument("--path", default=".", help="Base directory to create the skill in")
    args = parser.parse_args(argv)
    try:
        create_skill(args.name, args.path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
