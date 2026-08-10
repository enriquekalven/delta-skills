---
name: skill-discovery-and-benchmarking
description: >
  Skill Gap Audit & External Marketplace Discovery.
  Audits installed workspace skills against task requirements, detects capability limitations, searches external registries (skills.sh, SkillsMP, MCPMarket, GitHub), and recommends higher-performing skills with one-line installation commands.
  Triggers on: "discover skills", "find better skills", "skill gap audit", "skill marketplace search", "upgrade skills", "skills.sh search", "skillsmp search".
---

# Skill Discovery & Benchmarking (`skill-discovery-and-benchmarking`)

Evaluates whether currently installed local skills are sufficient for a given engineering task. When local skills are limited, missing capabilities, or outdated, it audits external registries (**`skills.sh`**, **`SkillsMP`**, **`MCPMarket`**, **`GitHub`**) to find and recommend higher-performing alternative skills.

---

## 🔍 Discovery Protocol

```
┌────────────────────────────────────────────────────────────────────────┐
│               SKILL GAP AUDIT & DISCOVERY WORKFLOW                     │
├────────────────────────────────────────────────────────────────────────┤
│ 1. LOCAL SKILL AUDIT     : Scans installed skills across plugins and   │
│                            compares them against task requirements.    │
│                                                                        │
│ 2. GAP DETECTION         : Flags missing capabilities (e.g. AST trace  │
│                            parsing, Playwright UI, ZDR Model Garden).  │
│                                                                        │
│ 3. REGISTRY SEARCH       : Queries skills.sh, SkillsMP (skillsmp.com), │
│                            and MCPMarket for matching external skills. │
│                                                                        │
│ 4. BENCHMARK COMPARISON  : Compares installed vs candidate skill       │
│                            features, fitness scores, and dependencies. │
│                                                                        │
│ 5. INSTALLATION RECOMMEND: Outputs exact one-line installation         │
│                            commands for approved candidate skills.     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 CLI Execution

```bash
# Run local skill gap audit and search external registries:
python3 skills/skill-discovery-and-benchmarking/scripts/discover_skills.py --task "AST code remediation and browser UI testing"
```

---

## ✋ Ground-Truth Rules
1. **Never guess skill capabilities**: Always inspect actual local `SKILL.md` files on disk.
2. **Actionable Recommendations**: Always output verified installation commands for recommended candidate skills.
