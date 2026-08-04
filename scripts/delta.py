#!/usr/bin/env python3
"""
Delta Skills CLI Helper Utility (scripts/delta.py)
Provides zero-dependency engagement management for TDLs and FDEs.
"""

import sys
import os
import argparse
from pathlib import Path

STATE_TEMPLATE = """# Engagement State Machine (STATE.md)

- **Client**: {client_name}
- **Engagement Duration**: {weeks}-Week Capped Window
- **Current Phase**: Phase 1: Discover & Define
- **Status**: IN_PROGRESS
- **Last Updated**: 2026-07-29

## Active Capability Slots
- [x] #CAPABILITY: Skill-Stocktake
- [ ] #CAPABILITY: Codebase-Onboarding
- [ ] #CAPABILITY: Repo-Conventions
- [ ] #CAPABILITY: PRD-Creation
- [ ] #CAPABILITY: Baseline-Audit

## Phase Gate Checklist (Phase 1)
- [ ] docs/ONBOARDING.md created and reviewed
- [ ] docs/PRD.md finalized with Goals & Non-Goals
- [ ] docs/baseline_kpis.json SME audit complete ($N=50$)
- [ ] Sponsor sign-off received
"""

REQUIRED_SLOTS = [
    "#CAPABILITY: Skill-Stocktake",
    "#CAPABILITY: Codebase-Onboarding",
    "#CAPABILITY: Repo-Conventions",
    "#CAPABILITY: PRD-Creation",
    "#CAPABILITY: Baseline-Audit",
    "#CAPABILITY: GCP-Architecture-Advisor",
    "#CAPABILITY: Executive-Persona-Review",
    "#CAPABILITY: Tech-Design-Document",
    "#CAPABILITY: API-Design",
    "#CAPABILITY: InfoSec-Threat-Modeling",
    "#CAPABILITY: Fleet-Management",
    "#CAPABILITY: Task-Breakdown",
    "#CAPABILITY: TDD-Build",
    "#CAPABILITY: Code-Simplification",
    "#CAPABILITY: Intent-Audit",
    "#CAPABILITY: Code-Review",
    "#CAPABILITY: Agent-Evaluation",
    "#CAPABILITY: ROI-Sizing",
    "#CAPABILITY: Release-Deployment",
    "#CAPABILITY: Handoff-Artifacts"
]

def init_engagement(client: str, weeks: int):
    root = Path.cwd()
    state_file = root / "STATE.md"
    docs_dir = root / "docs"
    
    docs_dir.mkdir(exist_ok=True)
    
    if not state_file.exists():
        state_file.write_text(STATE_TEMPLATE.format(client_name=client, weeks=weeks))
        print(f"✅ Initialized engagement for '{client}' in STATE.md")
        print(f"📁 Created docs/ directory at {docs_dir}")
    else:
        print("⚠️ STATE.md already exists in current working directory.")

def show_status():
    state_file = Path.cwd() / "STATE.md"
    if not state_file.exists():
        print("❌ No STATE.md found. Run 'python3 scripts/delta.py init' first.")
        return
    
    content = state_file.read_text()
    print("--- Current Engagement Status ---")
    for line in content.splitlines():
        if line.startswith("- **") or line.startswith("## ") or line.startswith("- ["):
            print(line)

def run_stocktake():
    print("--- Dynamic Capability Slot Stocktake ---")
    skills_dir = Path.home() / ".gemini" / "config" / "plugins"
    local_skills = Path.cwd() / "skills"
    
    resolved_count = 0
    for slot in REQUIRED_SLOTS:
        skill_name = slot.split(": ")[-1].lower().replace(" ", "-")
        local_exists = (local_skills / skill_name).exists()
        global_exists = any(skills_dir.glob(f"**/{skill_name}")) if skills_dir.exists() else False
        
        if local_exists or global_exists:
            location = "local workspace" if local_exists else "global config"
            print(f"  [OK] {slot} resolved ({location})")
            resolved_count += 1
        else:
            print(f"  [PENDING] {slot} missing or unmapped")
            
    print(f"\n📊 Capability Slot Summary: {resolved_count}/{len(REQUIRED_SLOTS)} resolved.")

def advance_phase():
    import re
    state_file = Path.cwd() / "STATE.md"
    if not state_file.exists():
        print("❌ No STATE.md found. Run 'python3 scripts/delta.py init' first.")
        return
        
    content = state_file.read_text()
    phases = [
        "Phase 1: Discover & Define",
        "Phase 2: Requirements & PRD",
        "Phase 3: Architecture & System Design",
        "Phase 4: Task Breakdown & Backlog",
        "Phase 5: Incremental Implementation & TDD",
        "Phase 6: QA & Verification Gate",
        "Phase 7: Production Deployment & Handoff"
    ]
    
    match = re.search(r"-\s*\*\*Current Phase\*\*:\s*(Phase \d:[^\n]+)", content)
    if not match:
        print("❌ Unable to parse Current Phase line in STATE.md.")
        return
        
    current_phase_str = match.group(1).strip()
    current_phase_idx = next((i for i, p in enumerate(phases) if p in current_phase_str), -1)
    
    if current_phase_idx == -1:
        print(f"❌ Unknown Current Phase string: '{current_phase_str}'")
        return
        
    if current_phase_idx >= len(phases) - 1:
        print("🎉 Engagement is already at Phase 7 (Completed)!")
        return
        
    next_phase = phases[current_phase_idx + 1]
    new_content = re.sub(r"(?m)^(-\s*\*\*Current Phase\*\*:\s*).*", r"\g<1>" + next_phase, content)
    state_file.write_text(new_content)
    print(f"🔄 Advanced Engagement State Loop: Moved from '{current_phase_str}' -> '{next_phase}'")

def rollback_phase(target_phase: int, reason: str = "Architectural drift detected"):
    import re
    state_file = Path.cwd() / "STATE.md"
    if not state_file.exists():
        print("❌ No STATE.md found.")
        return
        
    content = state_file.read_text()
    phases = [
        "Phase 1: Discover & Define",
        "Phase 2: Requirements & PRD",
        "Phase 3: Architecture & System Design",
        "Phase 4: Task Breakdown & Backlog",
        "Phase 5: Incremental Implementation & TDD",
        "Phase 6: QA & Verification Gate",
        "Phase 7: Production Deployment & Handoff"
    ]
    
    target_str = f"Phase {target_phase}:"
    matched_target = next((p for p in phases if p.startswith(target_str)), None)
    if not matched_target:
        print(f"❌ Invalid target phase: {target_phase}")
        return
        
    match = re.search(r"-\s*\*\*Current Phase\*\*:\s*(Phase \d:[^\n]+)", content)
    current_phase_str = match.group(1).strip() if match else "Unknown Phase"
    
    new_content = re.sub(r"(?m)^(-\s*\*\*Current Phase\*\*:\s*).*", r"\g<1>" + matched_target, content)
    state_file.write_text(new_content)
    print(f"⏪ State Regression Loop Executed: Rolled back from '{current_phase_str}' -> '{matched_target}'")
    print(f"📌 Reason: {reason}")

def main():
    parser = argparse.ArgumentParser(description="Delta Skills TDL CLI Tool")
    subparsers = parser.add_subparsers(dest="command")
    
    init_parser = subparsers.add_parser("init", help="Initialize a new customer engagement")
    init_parser.add_argument("--client", default="Enterprise Customer", help="Customer name")
    init_parser.add_argument("--weeks", type=int, default=12, help="Engagement duration window in weeks")
    
    subparsers.add_parser("status", help="Show current engagement status")
    subparsers.add_parser("stocktake", help="Audit capability slots")
    subparsers.add_parser("advance", help="Advance state machine loop to next phase")
    
    rollback_parser = subparsers.add_parser("rollback", help="Execute regression loop to target phase")
    rollback_parser.add_argument("--phase", type=int, required=True, help="Target phase number (1-7)")
    rollback_parser.add_argument("--reason", default="Verification audit regression", help="Rollback justification")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_engagement(args.client, args.weeks)
    elif args.command == "status":
        show_status()
    elif args.command == "stocktake":
        run_stocktake()
    elif args.command == "advance":
        advance_phase()
    elif args.command == "rollback":
        rollback_phase(args.phase, args.reason)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
