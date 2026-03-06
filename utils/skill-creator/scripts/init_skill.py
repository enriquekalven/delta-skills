#!/usr/bin/env python3
import os
import argparse

def create_skill(skill_name, base_path="."):
    """Initializes a new skill directory with standard boilerplate."""
    skill_dir = os.path.join(base_path, skill_name)
    
    # Create directories
    directories = [
        skill_dir,
        os.path.join(skill_dir, "scripts"),
        os.path.join(skill_dir, "references"),
        os.path.join(skill_dir, "assets")
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Add a .gitkeep to empty dirs so they track in version control
        if directory != skill_dir:
            with open(os.path.join(directory, ".gitkeep"), "w") as f:
                f.write("")

    # Create boilerplate SKILL.md
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        with open(skill_md_path, "w") as f:
            f.write(f"""---
name: {skill_name}
description: [OBVIOUS TRIGGER: When to fire] | [NEGATIVE TRIGGER: When NOT to fire] | [EDGE CASE: Boundaries]
---

# {skill_name.replace('-', ' ').title()}

TODO - Add main instructions explicitly formatted for Gemini 3.1 Pro constraints. Keep this file under 5,000 words (Progressive Disclosure) and move logic to scripts/ and domain knowledge to references/.

## Examples
- Example 1: Use concrete Multi-MCP tool handoffs here.

## Mandatory Guidelines
- **MUST**: [Non-negotiable rule to prevent Model Laziness]
- **MUST NOT**: [Strict Anti-Pattern]
""")
    
    print(f"Successfully initialized skill '{skill_name}' at {skill_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new agent skill.")
    parser.add_argument("name", help="The name of the skill (use-kebab-case)")
    parser.add_argument("--path", default=".", help="Base path to create the skill in")
    
    args = parser.parse_args()
    create_skill(args.name, args.path)
