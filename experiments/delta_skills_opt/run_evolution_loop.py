#!/usr/bin/env python3
"""
AlphaEvolve Hill-Climbing Execution Loop & Control Harness

Runs either:
1. Cloud AlphaEvolve Control Loop via `ae experiment run` CLI.
2. Local Evolutionary Hill-Climbing Loop (Offline Evaluator harness).

Usage:
  uv run python run_evolution_loop.py --mode local --generations 20
  uv run python run_evolution_loop.py --mode cloud --nickname exp-delta-opt
"""

import sys
import os
import argparse
import subprocess
import json
import time
import re
from typing import Dict, Any, List
from evaluator import evaluate_program


def run_local_hill_climbing_loop(generations: int = 20, program_file: str = "initial_program.py"):
    """
    Executes a local iterative evolutionary hill-climbing loop on initial_program.py.
    """
    print("=" * 60)
    print(f"🚀 Starting Local AlphaEvolve Hill-Climbing Loop ({generations} Generations)")
    print("=" * 60)

    if not os.path.exists(program_file):
        print(f"❌ Program file {program_file} not found.")
        sys.exit(1)

    with open(program_file, "r", encoding="utf-8") as f:
        current_best_code = f.read()

    baseline_eval = evaluate_program(current_best_code)
    current_best_score = baseline_eval.get("score") or 0.0

    print(f"📊 Baseline Score: {current_best_score:.4f}")
    for ins in baseline_eval.get("insights", []):
        print(f"   └─ [{ins['label']}] {ins['text']}")

    best_code = current_best_code
    history: List[Dict[str, Any]] = [
        {"generation": 0, "score": current_best_score, "accepted": True}
    ]

    for g in range(1, generations + 1):
        # Generate candidate mutation within EVOLVE-BLOCK
        mutated_code = current_best_code
        
        # Simulated heuristic mutation for demonstration: add micro-optimization
        if "max(1.0," in mutated_code and g % 2 == 0:
            mutated_code = mutated_code.replace("max(1.0,", "max(0.5,")
        
        eval_res = evaluate_program(mutated_code)
        cand_score = eval_res.get("score")

        if cand_score is not None and cand_score > current_best_score:
            print(f"✨ Gen {g:02d}: Improved! Score: {current_best_score:.4f} -> {cand_score:.4f}")
            current_best_score = cand_score
            current_best_code = mutated_code
            history.append({"generation": g, "score": cand_score, "accepted": True})
        else:
            cand_score_str = f"{cand_score:.4f}" if cand_score is not None else "Failed"
            print(f"  Gen {g:02d}: Rejected (Score: {cand_score_str} <= Best: {current_best_score:.4f})")
            history.append({"generation": g, "score": cand_score, "accepted": False})

        time.sleep(0.1)

    # Output final summary
    print("\n" + "=" * 60)
    print(f"🏆 Hill-Climbing Loop Complete!")
    print(f"   Initial Score : {history[0]['score']:.4f}")
    print(f"   Final Best    : {current_best_score:.4f}")
    print(f"   Improvement   : +{(current_best_score - history[0]['score']):.4f} pts")
    print("=" * 60)

    # Save best evolved program artifact
    evolved_out = "evolved_best_program.py"
    with open(evolved_out, "w", encoding="utf-8") as f:
        f.write(current_best_code)
    print(f"💾 Saved best program to {evolved_out}")


def run_cloud_alpha_evolve_loop(nickname: str, evaluator: str = "evaluator.py"):
    """
    Executes the Cloud AlphaEvolve evaluation control loop using `ae experiment run`.
    """
    print("=" * 60)
    print(f"🌩️ Connecting to Cloud AlphaEvolve Control Loop for Experiment: {nickname}")
    print("=" * 60)

    cmd = [
        "ae", "experiment", "run",
        nickname,
        "--evaluator", evaluator,
        "--dashboard"
    ]
    print(f"Executing: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("❌ `ae` CLI not found on PATH. Please ensure ae is installed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Control loop terminated with exit code {e.returncode}")


def main():
    parser = argparse.ArgumentParser(description="AlphaEvolve Hill-Climbing Loop Harness")
    parser.add_argument("--mode", choices=["local", "cloud"], default="local", help="Loop mode: local or cloud")
    parser.add_argument("--generations", type=int, default=20, help="Number of generations for local loop")
    parser.add_argument("--nickname", type=str, help="Experiment nickname for cloud ae loop")

    args = parser.parse_args()

    if args.mode == "local":
        run_local_hill_climbing_loop(generations=args.generations)
    elif args.mode == "cloud":
        if not args.nickname:
            print("❌ --nickname is required for cloud mode.")
            sys.exit(1)
        run_cloud_alpha_evolve_loop(nickname=args.nickname)


if __name__ == "__main__":
    main()
