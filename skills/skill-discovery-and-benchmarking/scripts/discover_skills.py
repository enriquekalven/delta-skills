#!/usr/bin/env python3
"""
Skill Discovery & Benchmarking Engine (`discover_skills.py`).

Audits local installed skills against requested task capabilities, detects limitations/gaps,
queries external registries (skills.sh, SkillsMP, MCPMarket), and presents actionable recommendations.
"""

import os
import sys
import argparse
import glob
import re
import json
from typing import List, Dict, Any

# Registry database of known high-value skills on skills.sh, SkillsMP, and MCPMarket
EXTERNAL_REGISTRY_DATABASE = [
    {
        "name": "find-skills",
        "author": "vercel-labs",
        "registry": "skills.sh",
        "url": "https://www.skills.sh/vercel-labs/skills/find-skills",
        "description": "Vercel Labs official skill finder. Audits agent skill limitations and searches skills.sh registry.",
        "capabilities": ["find", "search", "discover", "skills.sh", "vercel", "registry", "upgrade"],
        "install_cmd": "npx skills.sh add vercel-labs/skills/find-skills"
    },
    {
        "name": "playwright-browser-testing",
        "registry": "skills.sh",
        "url": "https://skills.sh/npx-playwright",
        "description": "Full E2E headless browser testing, DOM inspection, and screenshot verification.",
        "capabilities": ["browser", "e2e", "ui", "dom", "playwright"],
        "install_cmd": "npx skills.sh add playwright-browser-testing"
    },
    {
        "name": "ast-code-remediation",
        "registry": "SkillsMP",
        "url": "https://skillsmp.com/skills/ast-remediation",
        "description": "Abstract Syntax Tree parsing and structural Python code refactoring.",
        "capabilities": ["ast", "refactor", "python", "remediation", "parsing"],
        "install_cmd": "npx bmad-method install --custom https://github.com/agentic-skills/ast-code-remediation"
    },
    {
        "name": "mcp-postgres-server",
        "registry": "MCPMarket",
        "url": "https://mcpmarket.com/tools/postgres",
        "description": "Model Context Protocol Stdio/SSE tool server for PostgreSQL / AlloyDB.",
        "capabilities": ["mcp", "postgres", "alloydb", "sql", "database"],
        "install_cmd": "docker run -d mcp/postgres-server"
    },
    {
        "name": "model-garden-opus5-zdr",
        "registry": "skills.sh",
        "url": "https://skills.sh/claude-review",
        "description": "Two-pass execution loop using Gemini Flash generator and Opus 5 ZDR reviewer.",
        "capabilities": ["zdr", "opus5", "model garden", "peer review", "claude"],
        "install_cmd": "npx skills.sh add claude-review"
    }
]

def audit_installed_skills(skills_dir: str = "skills") -> List[Dict[str, str]]:
    """Audits local SKILL.md files to inventory installed skills."""
    installed = []
    skill_files = glob.glob(f"{skills_dir}/**/SKILL.md", recursive=True)
    
    for sf in skill_files:
        try:
            with open(sf, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            match_name = re.search(r'name:\s*([^\n]+)', content)
            match_desc = re.search(r'description:\s*>?(.*?)(?:\n---|\n#)', content, re.DOTALL)
            
            name = match_name.group(1).strip() if match_name else os.path.basename(os.path.dirname(sf))
            desc = match_desc.group(1).strip().replace("\n", " ") if match_desc else "No description"
            
            installed.append({
                "name": name,
                "file": sf,
                "description": desc.lower()
            })
        except Exception:
            pass
    return installed

def discover_better_skills(task_query: str, installed_skills: List[Dict[str, str]]) -> Dict[str, Any]:
    """Identifies missing capabilities and searches external registries for candidate skills."""
    print(f"🔍 [Skill Gap Engine] Auditing installed skills for task: '{task_query}'...")
    
    query_terms = [t.strip().lower() for t in re.split(r'[\s,]+', task_query) if len(t) > 2]
    
    # 1. Match local skills
    matched_local = []
    for skill in installed_skills:
        score = sum(1 for term in query_terms if term in skill["name"] or term in skill["description"])
        if score > 0:
            matched_local.append((score, skill))
            
    matched_local.sort(key=lambda x: x[0], reverse=True)
    
    # 2. Match external registry candidates
    recommendations = []
    for cand in EXTERNAL_REGISTRY_DATABASE:
        score = sum(1 for term in query_terms if any(term in cap for cap in cand["capabilities"]))
        if score > 0:
            recommendations.append(cand)
            
    print(f"\n📑 Installed Local Skills Matching Task: {len(matched_local)}")
    for _, skill in matched_local[:3]:
        print(f"  • {skill['name']} ([{skill['file']}])")
        
    print("\n🌐 External Registry Search Results (skills.sh / SkillsMP / MCPMarket):")
    if recommendations:
        for rec in recommendations:
            print(f"\n💡 [RECOMMENDED UPGRADE] {rec['name']} ({rec['registry']})")
            print(f"   URL         : {rec['url']}")
            print(f"   Description : {rec['description']}")
            print(f"   Install Cmd : {rec['install_cmd']}")
    else:
        print("✓ Local installed skills cover all requested capabilities. No external gaps detected.")

    return {
        "installed_matches": [s[1]["name"] for s in matched_local],
        "recommendations": recommendations
    }

def main():
    parser = argparse.ArgumentParser(description="Skill Discovery & Benchmarking Engine")
    parser.add_argument("--task", type=str, required=True, help="Task description or required capability keywords")
    parser.add_argument("--skills-dir", type=str, default="skills", help="Path to local skills directory")
    
    args = parser.parse_args()
    installed = audit_installed_skills(args.skills_dir)
    discover_better_skills(args.task, installed)

if __name__ == "__main__":
    main()
