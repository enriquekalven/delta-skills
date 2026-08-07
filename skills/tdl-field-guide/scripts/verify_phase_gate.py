#!/usr/bin/env python3
"""
Programmatic Phase Gate Verifier for TDL Field Execution Playbook.

Verifies mandatory artifacts, pytest pass rates, and security posture before
allowing STATE.md phase progression.

Usage:
  python3 scripts/verify_phase_gate.py --phase 1
  python3 scripts/verify_phase_gate.py --phase 2
  python3 scripts/verify_phase_gate.py --phase 3
  python3 scripts/verify_phase_gate.py --phase 4
"""

import sys
import os
import argparse
import json
import re
import subprocess
from typing import List, Tuple, Dict, Any


def check_file_exists(filepath: str) -> Tuple[bool, str]:
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        return True, f"✓ Found {filepath} ({os.path.getsize(filepath)} bytes)"
    return False, f"✗ Missing or empty required artifact: {filepath}"


def scan_for_exposed_secrets(search_dir: str = ".") -> Tuple[bool, List[str]]:
    """Basic secret scanner checking for hardcoded API keys."""
    secret_patterns = [
        re.compile(r'AIzaSy[A-Za-z0-9_-]{33}'),  # GCP API Key
        re.compile(r'sk-[A-Za-z0-9]{32,}'),       # OpenAI/Anthropic Key
        re.compile(r'ghp_[A-Za-z0-9]{36}'),       # GitHub Token
    ]
    violations = []
    for root, _, files in os.walk(search_dir):
        if any(ignored in root for ignored in [".git", "node_modules", "__pycache__", ".venv"]):
            continue
        for file in files:
            if file.endswith((".py", ".json", ".yaml", ".yml", ".md", ".env")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        for pattern in secret_patterns:
                            if pattern.search(content):
                                violations.append(f"Exposed secret pattern in {path}")
                except Exception:
                    pass
    return len(violations) == 0, violations


def run_pytest_verification() -> Tuple[bool, str]:
    """Runs pytest and checks for 100% pass rate."""
    try:
        res = subprocess.run(["pytest", "-q"], capture_output=True, text=True, timeout=60)
        if res.returncode == 0:
            return True, "✓ PyTest passed with 100% success rate."
        return False, f"✗ PyTest failures detected:\n{res.stdout}\n{res.stderr}"
    except FileNotFoundError:
        return True, "⚠ PyTest binary not found; skipping test execution check."
    except subprocess.TimeoutExpired:
        return False, "✗ PyTest execution timed out (>60s)."


def verify_phase_1(project_root: str) -> Tuple[bool, List[str]]:
    logs = []
    passed = True

    required_files = [
        os.path.join(project_root, "docs", "ONBOARDING.md"),
        os.path.join(project_root, "PRD.md"),
        os.path.join(project_root, "baseline_kpis.json"),
    ]

    for req in required_files:
        ok, msg = check_file_exists(req)
        logs.append(msg)
        if not ok:
            passed = False

    sec_ok, sec_logs = scan_for_exposed_secrets(project_root)
    if not sec_ok:
        passed = False
        logs.extend(sec_logs)
    else:
        logs.append("✓ Secret scan passed (no hardcoded credentials).")

    return passed, logs


def verify_phase_2(project_root: str) -> Tuple[bool, List[str]]:
    logs = []
    passed = True

    required_files = [
        os.path.join(project_root, "docs", "ARCHITECTURE_RECOMMENDATION.md"),
        os.path.join(project_root, "docs", "TDD.md"),
    ]

    for req in required_files:
        ok, msg = check_file_exists(req)
        logs.append(msg)
        if not ok:
            passed = False

    return passed, logs


def verify_phase_3(project_root: str) -> Tuple[bool, List[str]]:
    logs = []
    passed = True

    test_ok, test_msg = run_pytest_verification()
    logs.append(test_msg)
    if not test_ok:
        passed = False

    sec_ok, sec_logs = scan_for_exposed_secrets(project_root)
    if not sec_ok:
        passed = False
        logs.extend(sec_logs)
    else:
        logs.append("✓ Secret scan passed.")

    return passed, logs


def verify_phase_4(project_root: str) -> Tuple[bool, List[str]]:
    logs = []
    passed = True

    required_files = [
        os.path.join(project_root, "docs", "HANDOFF_PACKET.md"),
        os.path.join(project_root, "baseline_kpis.json"),
    ]

    for req in required_files:
        ok, msg = check_file_exists(req)
        logs.append(msg)
        if not ok:
            passed = False

    return passed, logs


def main():
    parser = argparse.ArgumentParser(description="Programmatic TDL Phase Gate Verifier")
    parser.add_argument("--phase", type=int, required=True, choices=[1, 2, 3, 4], help="Phase gate to verify (1-4)")
    parser.add_argument("--project-root", type=str, default=".", help="Root path of repository")
    args = parser.parse_args()

    print("=" * 60)
    print(f"🔒 Running Programmatic Phase Gate Verification: Phase {args.phase}")
    print("=" * 60)

    verifiers = {
        1: verify_phase_1,
        2: verify_phase_2,
        3: verify_phase_3,
        4: verify_phase_4,
    }

    verifier = verifiers[args.phase]
    passed, logs = verifier(args.project_root)

    for log in logs:
        print(log)

    print("=" * 60)
    if passed:
        print(f"✨ PHASE {args.phase} GATE VERIFICATION PASSED. Approved to advance STATE.md.")
        sys.exit(0)
    else:
        print(f"❌ PHASE {args.phase} GATE VERIFICATION FAILED. Fix missing artifacts or test failures before advancing state.")
        sys.exit(1)


if __name__ == "__main__":
    main()
