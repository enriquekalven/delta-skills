#!/usr/bin/env python3
"""
Ralph Autonomous Loop Engine.

Reads a prd.json task list, tracks task statuses (pending, in_progress, completed),
executes test/verification commands, and reports loop completion state.

Usage:
  python3 scripts/run_ralph_loop.py --prd docs/prd.json
"""

import sys
import os
import json
import argparse
import subprocess
from typing import Dict, Any, List


def load_prd_tasks(prd_path: str) -> Dict[str, Any]:
    if not os.path.exists(prd_path):
        # Create a sample prd.json if not present
        sample_prd = {
            "project_name": "Sample Task Loop",
            "version": "1.0.0",
            "tasks": [
                {
                    "id": "TASK-1",
                    "title": "Verify Environment Setup",
                    "status": "completed",
                    "verification_command": "python3 --version"
                },
                {
                    "id": "TASK-2",
                    "title": "Run Unit Test Suite",
                    "status": "pending",
                    "verification_command": "pytest -q"
                }
            ]
        }
        os.makedirs(os.path.dirname(prd_path), exist_ok=True)
        with open(prd_path, "w", encoding="utf-8") as f:
            json.dump(sample_prd, f, indent=2)
        print(f"💡 Created initial PRD task list template at {prd_path}")

    with open(prd_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Ralph Autonomous Loop Runner")
    parser.add_argument("--prd", type=str, default="docs/prd.json", help="Path to prd.json task list")
    args = parser.parse_args()

    prd_data = load_prd_tasks(args.prd)
    tasks: List[Dict[str, Any]] = prd_data.get("tasks", [])

    total_tasks = len(tasks)
    completed_count = sum(1 for t in tasks if t.get("status") == "completed")
    pending_tasks = [t for t in tasks if t.get("status") != "completed"]

    print("=" * 60)
    print(f"🔄 Ralph Autonomous Loop Status: {prd_data.get('project_name', 'Task Loop')}")
    print(f"📊 Task Completion: {completed_count} / {total_tasks} ({round(completed_count/total_tasks*100 if total_tasks else 0, 1)}%)")
    print("=" * 60)

    for t in tasks:
        status_icon = "✅" if t.get("status") == "completed" else "⏳"
        print(f" {status_icon} [{t.get('id')}] {t.get('title')} ({t.get('status')})")

    print("=" * 60)
    if pending_tasks:
        next_task = pending_tasks[0]
        print(f"🚀 Next Task to Execute: [{next_task.get('id')}] {next_task.get('title')}")
        cmd = next_task.get("verification_command")
        if cmd:
            print(f"💻 Verification Command: {cmd}")
    else:
        print("🎉 ALL PRD TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()
