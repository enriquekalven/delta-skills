#!/usr/bin/env python3
"""Initialize a new skill directory with standard Agent Skills boilerplate."""

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
    """Initialize a new skill directory confined within base_path."""
    valid_name = validate_skill_name(skill_name)
    real_base = os.path.realpath(base_path)
    skill_dir = os.path.realpath(os.path.join(real_base, valid_name))
    if not skill_dir.startswith(real_base + os.sep):
        raise ValueError(f"skill directory escapes base_path: {skill_name!r}")

    directories = [
        skill_dir,
        os.path.join(skill_dir, "scripts"),
        os.path.join(skill_dir, "references"),
        os.path.join(skill_dir, "assets"),
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        if directory != skill_dir:
            gitkeep = Path(directory) / ".gitkeep"
            if not gitkeep.exists():
                gitkeep.write_text("", encoding="utf-8")

    skill_md_path = Path(skill_dir) / "SKILL.md"
    if not skill_md_path.exists():
        title = valid_name.replace("-", " ").title()
        skill_md_path.write_text(
            f"""---
name: {valid_name}
description: >
  Describe what this skill does and when to use it.
  Triggers on: "<obvious trigger phrases>".
  Do NOT trigger when: "<negative trigger conditions>".
---

# {title}

Provide concise step-by-step instructions (under 5,000 words) using progressive disclosure.
Move executable helpers to `scripts/` and detailed domain references to `references/`.

## Execution Steps
1. Inspect inputs and verify preconditions.
2. Execute core workflow steps and reference files in `references/` on demand.
3. Verify outputs against acceptance criteria before returning.

## Mandatory Guidelines
- **MUST**: Enforce deterministic verification and explicit user checkpoints where required.
- **MUST NOT**: Fabricate outputs, skip validation steps, or hardcode credentials.
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
