#!/usr/bin/env python3
"""
AI Slop & Jargon Scanner for Technical Documentation.

Scans Markdown documents for:
1. High-density corporate buzzwords ("synergistic", "holistic", "seamless paradigm").
2. Non-falsifiable hand-wavy claims ("ultra-scalable", "enterprise-grade perfection").
3. Common AI hallucination patterns (invalid package names, fake product aliases).

Usage:
  python3 scripts/scan_doc_slop.py --file docs/MY_DOC.md
"""

import sys
import os
import argparse
import re
from typing import List, Dict, Any, Tuple


# Known AI Slop & Buzzword Patterns
BUZZWORD_PATTERNS = [
    (r'\bseamless(?:ly)?\b', "Vague filler; describe actual mechanism (e.g. 'via REST API' or 'via gRPC')"),
    (r'\bsynergistic(?:ally)?\b', "Corporate fluff; remove or explain specific integration"),
    (r'\bholistic(?:ally)?\b', "Overused AI adjective; specify exact components"),
    (r'\bcutting-edge\b', "Hype word; state specific technology version (e.g. 'FastAPI v0.110')"),
    (r'\bstate-of-the-art\b', "Hype word; state exact benchmark or standard"),
    (r'\bnext-generation\b', "Vague hype; state version or feature diff"),
    (r'\brevolutionary\b', "Hype word; state exact quantitative improvement"),
    (r'\bgame-changing\b', "Hype word; state specific ROI or metric"),
    (r'\bultra-scalable\b', "Hand-waving; provide specific RPS, QPS, or Cloud Run instance limits"),
    (r'\benterprise-grade\b', "Hand-waving; list specific IAM, VPC-SC, or CMEK security rules"),
    (r'\bdelve\b', "Overused LLM transition word; replace with 'explore', 'examine', or 'analyze'"),
    (r'\brobust\b', "Vague adjective; state specific error-handling or retry logic"),
    (r'\bparadigm shift\b', "Corporate fluff; describe actual design pattern change"),
]

# Common AI Hallucinations for Google Cloud AI Stack
HALLUCINATION_PATTERNS = [
    (r'@google/adk', "Invalid package name; correct PyPI package is 'google-adk' (imported as 'google.adk')"),
    (r'Vertex AI Reasoning Engine.*Public Preview', "Factual error; Reasoning Engine is GA (now known as Agent Engine)"),
]


def scan_file_for_slop(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {"error": f"File not found: {filepath}"}

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    total_words = 0
    slop_findings: List[Dict[str, Any]] = []

    for idx, line in enumerate(lines, 1):
        words = line.split()
        total_words += len(words)

        for pattern, recommendation in BUZZWORD_PATTERNS:
            matches = re.findall(pattern, line, re.IGNORECASE)
            if matches:
                for match in matches:
                    slop_findings.append({
                        "line": idx,
                        "match": match,
                        "type": "Buzzword / Corporate Fluff",
                        "recommendation": recommendation,
                        "context": line.strip()
                    })

        for pattern, recommendation in HALLUCINATION_PATTERNS:
            matches = re.findall(pattern, line, re.IGNORECASE)
            if matches:
                for match in matches:
                    slop_findings.append({
                        "line": idx,
                        "match": match,
                        "type": "Hallucination / Factual Error",
                        "recommendation": recommendation,
                        "context": line.strip()
                    })

    slop_score = max(0.0, 100.0 - (len(slop_findings) * 5.0))

    return {
        "filepath": filepath,
        "total_words": total_words,
        "total_findings": len(slop_findings),
        "slop_score": round(slop_score, 1),
        "findings": slop_findings
    }


def main():
    parser = argparse.ArgumentParser(description="AI Slop & Jargon Scanner")
    parser.add_argument("--file", type=str, required=True, help="Path to markdown document to scan")
    args = parser.parse_args()

    result = scan_file_for_slop(args.file)

    if "error" in result:
        print(f"❌ {result['error']}")
        sys.exit(1)

    print("=" * 60)
    print(f"🔍 AI Slop Audit Report: {result['filepath']}")
    print(f"📊 Document Word Count: {result['total_words']} words")
    print(f"🚩 Total Slop Findings : {result['total_findings']}")
    print(f"✨ Plain-English Score : {result['slop_score']} / 100")
    print("=" * 60)

    if result["findings"]:
        print("\nDetailed Findings & Plain-English Replacement Recommendations:")
        for f in result["findings"]:
            print(f"  Line {f['line']:3d} | [{f['type']}] '{f['match']}'")
            print(f"           └─ Context: \"{f['context'][:70]}...\"")
            print(f"           └─ Recommendation: {f['recommendation']}\n")
    else:
        print("\n🎉 No AI Slop or corporate buzzwords detected! Document is grounded and plain-English.")

    print("=" * 60)


if __name__ == "__main__":
    main()
