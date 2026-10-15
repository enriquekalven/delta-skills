#!/usr/bin/env python3
"""Agentic fan-out and Vertex AI quota calculator.

Implements the fan-out formula and quota-sizing rule from the TDL Toolbox
"Executive Consulting Guide: Load Testing Design, Multi-Tier Parallelism,
Infrastructure Quotas, Reports & Metrics, and Performance Optimizations"
(Nova Scotia Health Clinician Search Agent, Sept 2026):

    Total LLM calls per turn = 1 (Safety) + 1 (Decomposition)
                               + (Qt x Cq chunked synthesis) + 1 (Final synthesis)
    Peak RPM  = concurrent complex turns per minute x LLM calls per turn
    Peak TPM  = Peak RPM x tokens per call
    Quota     = 5 x peak ("Proactive Quota Sizing ... 5x Peak Multiplier")

Defaults reproduce the guide's inputs: Qt ~ 6 sub-questions, Cq ~ 2-4 chunks,
20,000 tokens per call, 10 simultaneous doctors. Everything else is an explicit
input; there are no hidden constants.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Any, Dict, Optional


def calculate_agent_quotas(
    peak_turns_per_min: int = 10,
    sub_questions: int = 6,
    chunks_per_subquestion: int = 4,
    safety_calls: int = 1,
    decomp_calls: int = 1,
    final_calls: int = 1,
    tokens_per_call: int = 20_000,
    semantic_queries_per_turn: int = 30,
    prefetch_modes: int = 2,
    grpc_pool_size: int = 8,
    peak_multiplier: float = 5.0,
    cache_hit_ratio: float = 0.0,
    admission_cap: Optional[int] = None,
) -> Dict[str, Any]:
    """Return per-turn fan-out, peak load, and recommended Vertex AI quotas.

    peak_turns_per_min:        simultaneous complex user turns in the peak minute
                               (the guide's example: 10 doctors).
    sub_questions (Qt):        sub-questions per decomposed query (guide: ~6).
    chunks_per_subquestion:    synthesis chunks per sub-question (guide: ~2-4).
    tokens_per_call:           average input tokens per LLM call (guide: 20,000).
    semantic_queries_per_turn: vector queries emitted per turn (guide: 18-60).
    prefetch_modes:            lookups per semantic query (guide: dense + sparse = 2).
    grpc_pool_size:            client gRPC channel pool (guide: 8 default, 128 after fix).
    peak_multiplier:           quota headroom over peak (guide: 5x).
    cache_hit_ratio:           fraction of input tokens served from Vertex AI
                               context cache (guide reports 50-70%). 0 = no cache.
    admission_cap:             optional max concurrently admitted turns
                               (Traffic Queue Admission Controller).
    """
    if peak_turns_per_min <= 0:
        raise ValueError("peak_turns_per_min must be > 0")
    if min(sub_questions, chunks_per_subquestion, safety_calls, decomp_calls, final_calls) < 0:
        raise ValueError("call counts must be >= 0")
    if tokens_per_call <= 0:
        raise ValueError("tokens_per_call must be > 0")
    if semantic_queries_per_turn < 0 or prefetch_modes < 1 or grpc_pool_size < 1:
        raise ValueError("semantic_queries_per_turn >= 0, prefetch_modes >= 1, grpc_pool_size >= 1")
    if not 0.0 <= cache_hit_ratio < 1.0:
        raise ValueError("cache_hit_ratio must be in [0, 1)")
    if peak_multiplier < 1.0:
        raise ValueError("peak_multiplier must be >= 1.0")
    if admission_cap is not None and admission_cap <= 0:
        raise ValueError("admission_cap must be > 0 when provided")

    chunked_synthesis_calls = sub_questions * chunks_per_subquestion
    llm_calls_per_turn = safety_calls + decomp_calls + chunked_synthesis_calls + final_calls

    peak_rpm = peak_turns_per_min * llm_calls_per_turn
    peak_tpm = peak_rpm * tokens_per_call
    effective_tokens_per_call = tokens_per_call * (1.0 - cache_hit_ratio)
    peak_tpm_after_cache = peak_rpm * effective_tokens_per_call

    grpc_requests_per_turn = semantic_queries_per_turn * prefetch_modes
    concurrent_grpc_requests = peak_turns_per_min * grpc_requests_per_turn
    grpc_pool_waves = math.ceil(concurrent_grpc_requests / grpc_pool_size) if concurrent_grpc_requests else 0

    result: Dict[str, Any] = {
        "inputs": {
            "peak_turns_per_min": peak_turns_per_min,
            "sub_questions_Qt": sub_questions,
            "chunks_per_subquestion_Cq": chunks_per_subquestion,
            "safety_calls": safety_calls,
            "decomp_calls": decomp_calls,
            "final_calls": final_calls,
            "tokens_per_call": tokens_per_call,
            "semantic_queries_per_turn": semantic_queries_per_turn,
            "prefetch_modes": prefetch_modes,
            "grpc_pool_size": grpc_pool_size,
            "peak_multiplier": peak_multiplier,
            "cache_hit_ratio": cache_hit_ratio,
            "admission_cap": admission_cap,
        },
        "per_turn_fanout": {
            "chunked_synthesis_calls": chunked_synthesis_calls,
            "llm_calls_per_turn": llm_calls_per_turn,
            "vector_grpc_requests_per_turn": grpc_requests_per_turn,
        },
        "peak_load": {
            "peak_llm_rpm": peak_rpm,
            "peak_input_tpm": peak_tpm,
            "peak_input_tpm_after_cache": round(peak_tpm_after_cache),
            "concurrent_vector_grpc_requests": concurrent_grpc_requests,
            "grpc_pool_waves": grpc_pool_waves,
        },
        "recommended_quotas": {
            "gemini_generate_content_rpm": math.ceil(peak_rpm * peak_multiplier),
            "gemini_input_tpm": math.ceil(peak_tpm * peak_multiplier),
            "gemini_input_tpm_after_cache": math.ceil(peak_tpm_after_cache * peak_multiplier),
        },
    }
    if admission_cap is not None:
        result["admission_control"] = {
            "admitted_turns": min(peak_turns_per_min, admission_cap),
            "queued_turns": max(0, peak_turns_per_min - admission_cap),
            "admitted_llm_rpm": min(peak_turns_per_min, admission_cap) * llm_calls_per_turn,
        }
    return result


def _format_report(result: Dict[str, Any]) -> str:
    f = result["per_turn_fanout"]
    p = result["peak_load"]
    q = result["recommended_quotas"]
    i = result["inputs"]
    lines = [
        "=== Agentic Fan-Out & Vertex AI Quota Sizing ===",
        f"LLM calls / turn            : {f['llm_calls_per_turn']}  "
        f"(= {i['safety_calls']} safety + {i['decomp_calls']} decomp + "
        f"{i['sub_questions_Qt']} x {i['chunks_per_subquestion_Cq']} chunked + {i['final_calls']} final)",
        f"Vector gRPC requests / turn : {f['vector_grpc_requests_per_turn']}  "
        f"(= {i['semantic_queries_per_turn']} semantic x {i['prefetch_modes']} prefetch modes)",
        "-----------------------------------------------",
        f"Peak LLM RPM                : {p['peak_llm_rpm']:,}  (= {i['peak_turns_per_min']} turns/min x {f['llm_calls_per_turn']})",
        f"Peak input TPM              : {p['peak_input_tpm']:,}  (= RPM x {i['tokens_per_call']:,} tokens/call)",
    ]
    if i["cache_hit_ratio"] > 0:
        lines.append(f"Peak input TPM after cache  : {p['peak_input_tpm_after_cache']:,}  (cache hit ratio {i['cache_hit_ratio']:.0%})")
    lines += [
        f"Concurrent vector gRPC reqs : {p['concurrent_vector_grpc_requests']:,}  -> {p['grpc_pool_waves']} queue waves at pool size {i['grpc_pool_size']}",
        "-----------------------------------------------",
        f"Quota: generate_content RPM : {q['gemini_generate_content_rpm']:,}  ({i['peak_multiplier']:g}x peak)",
        f"Quota: input TPM            : {q['gemini_input_tpm']:,}  ({i['peak_multiplier']:g}x peak)",
    ]
    if i["cache_hit_ratio"] > 0:
        lines.append(f"Quota: input TPM after cache: {q['gemini_input_tpm_after_cache']:,}")
    if "admission_control" in result:
        a = result["admission_control"]
        lines.append(
            f"Admission cap {i['admission_cap']}        : {a['admitted_turns']} admitted / {a['queued_turns']} queued "
            f"-> admitted LLM RPM {a['admitted_llm_rpm']:,}"
        )
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Agentic fan-out and Vertex AI quota calculator (TDL load-testing guide).")
    parser.add_argument("--peak-turns-per-min", type=int, default=10, help="Simultaneous complex turns in the peak minute (guide: 10 doctors)")
    parser.add_argument("--sub-questions", type=int, default=6, help="Qt: sub-questions per query (guide: ~6)")
    parser.add_argument("--chunks-per-subquestion", type=int, default=4, help="Cq: synthesis chunks per sub-question (guide: ~2-4)")
    parser.add_argument("--safety-calls", type=int, default=1)
    parser.add_argument("--decomp-calls", type=int, default=1)
    parser.add_argument("--final-calls", type=int, default=1)
    parser.add_argument("--tokens-per-call", type=int, default=20_000, help="Average input tokens per LLM call (guide: 20,000)")
    parser.add_argument("--semantic-queries-per-turn", type=int, default=30, help="Vector queries per turn (guide: 18-60)")
    parser.add_argument("--prefetch-modes", type=int, default=2, help="Lookups per semantic query (guide: dense + sparse)")
    parser.add_argument("--grpc-pool-size", type=int, default=8, help="Client gRPC pool (guide: 8 default, 128 after fix)")
    parser.add_argument("--peak-multiplier", type=float, default=5.0, help="Quota headroom over peak (guide: 5x)")
    parser.add_argument("--cache-hit-ratio", type=float, default=0.0, help="Context-cache hit ratio 0..1 (guide: 0.5-0.7)")
    parser.add_argument("--admission-cap", type=int, default=None, help="Max concurrently admitted turns (Traffic Queue)")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of the text report")
    args = parser.parse_args(argv)

    result = calculate_agent_quotas(
        peak_turns_per_min=args.peak_turns_per_min,
        sub_questions=args.sub_questions,
        chunks_per_subquestion=args.chunks_per_subquestion,
        safety_calls=args.safety_calls,
        decomp_calls=args.decomp_calls,
        final_calls=args.final_calls,
        tokens_per_call=args.tokens_per_call,
        semantic_queries_per_turn=args.semantic_queries_per_turn,
        prefetch_modes=args.prefetch_modes,
        grpc_pool_size=args.grpc_pool_size,
        peak_multiplier=args.peak_multiplier,
        cache_hit_ratio=args.cache_hit_ratio,
        admission_cap=args.admission_cap,
    )
    print(json.dumps(result, indent=2) if args.json else _format_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
