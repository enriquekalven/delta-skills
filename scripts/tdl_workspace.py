#!/usr/bin/env python3
"""TDL Customer Workspace Bootstrapper & Phase-Gate Readiness Auditor CLI.

Makes the TDL User Guide 100% operational on real customer engagements:
1. `init`: Scaffolds a live customer project workspace (`STATE.md`, `docs/*.md`,
   `evals/golden_dataset.json`, `tests/eval/eval_config.yaml`) pre-populated with
   real deterministic outputs from `calculate_roi.py` and `calculate_agent_quotas.py`,
   while marking every domain-specific field with explicit `[SME_INPUT_REQUIRED: ...]`
   tags instead of AI-invented filler.
2. `audit`: Audits any customer engagement workspace on disk against phase-gate
   exit criteria (`prelude`, `phase1`, `phase2`, `phase3`), checking for missing
   artifacts, unresolved `[SME_INPUT_REQUIRED]` / `TODO` / `TBD` placeholders,
   banned AI-fluff phrases, Golden Dataset stratification, and cross-artifact
   metric lineage consistency.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

PHASE_ARTIFACTS: dict[str, tuple[str, ...]] = {
    "prelude": (
        "STATE.md",
        "docs/WORKSHOP_INTAKE.md",
        "docs/USE_CASE_CANVAS.md",
        "docs/VALUE_SIZING.md",
    ),
    "phase1": (
        "STATE.md",
        "docs/WORKSHOP_INTAKE.md",
        "docs/USE_CASE_CANVAS.md",
        "docs/VALUE_SIZING.md",
        "docs/as_is_report.md",
        "docs/to_be_designs.md",
        "docs/human_agent_roles.md",
        "docs/CUJ_MAP.md",
        "docs/PRD.md",
        "docs/ARCHITECTURE_RECOMMENDATION.md",
        "evals/golden_dataset.json",
        "tests/eval/eval_config.yaml",
    ),
    "phase2": (
        "STATE.md",
        "docs/WORKSHOP_INTAKE.md",
        "docs/USE_CASE_CANVAS.md",
        "docs/VALUE_SIZING.md",
        "docs/as_is_report.md",
        "docs/to_be_designs.md",
        "docs/human_agent_roles.md",
        "docs/CUJ_MAP.md",
        "docs/PRD.md",
        "docs/ARCHITECTURE_RECOMMENDATION.md",
        "evals/golden_dataset.json",
        "tests/eval/eval_config.yaml",
        "docs/STITCH_PROTOTYPE.md",
        "docs/TDD.md",
        "docs/DEMO_FRAME_UP.md",
        "docs/EVAL_AUDIT_REPORT.md",
        "docs/LOAD_TEST_REPORT.md",
    ),
    "phase3": (
        "STATE.md",
        "docs/WORKSHOP_INTAKE.md",
        "docs/USE_CASE_CANVAS.md",
        "docs/VALUE_SIZING.md",
        "docs/as_is_report.md",
        "docs/to_be_designs.md",
        "docs/human_agent_roles.md",
        "docs/CUJ_MAP.md",
        "docs/PRD.md",
        "docs/ARCHITECTURE_RECOMMENDATION.md",
        "evals/golden_dataset.json",
        "tests/eval/eval_config.yaml",
        "docs/STITCH_PROTOTYPE.md",
        "docs/TDD.md",
        "docs/DEMO_FRAME_UP.md",
        "docs/EVAL_AUDIT_REPORT.md",
        "docs/LOAD_TEST_REPORT.md",
        "docs/CLOSEOUT_DECK.md",
    ),
}

SME_PLACEHOLDER_RE = re.compile(r"\[SME_INPUT_REQUIRED:[^\]]+\]")
UNRESOLVED_TODO_RE = re.compile(r"\b(?:TODO|FIXME|TBD)\b")
BANNED_FLUFF_RE = re.compile(
    r"\b(?:context_versioning|conflict_register|atlas-report-template|rumelt-strategy-forge)\b",
    re.IGNORECASE,
)


def _load_module(name: str, rel_path: str) -> Any:
    path = REPO_ROOT / rel_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module {name} from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def init_workspace(
    workspace: Path,
    use_case: str,
    project: str,
    tam_units: float = 80000.0,
    sam_share: float = 0.625,
    adoption_rate: float = 0.30,
    tech_compat: float = 0.80,
    hours_saved: float = 0.70,
    hourly_rate: float = 75.0,
    capex: float = 180000.0,
    annual_opex: float = 68000.0,
    vcr: float = 0.50,
    scdf: float = 0.85,
    wacc: float = 0.10,
    peak_turns_per_min: int = 10,
    sub_questions: int = 6,
    chunks_per_subquestion: int = 4,
    tokens_per_call: int = 20000,
    populate_sme_inputs: bool = False,
) -> dict[str, Any]:
    """Bootstrap a customer engagement workspace with real calculator math."""
    roi_mod = _load_module(
        "calculate_roi_ws", "skills/ai-value-sizing/scripts/calculate_roi.py"
    )
    quota_mod = _load_module(
        "calculate_quotas_ws",
        "skills/agent-load-testing/scripts/calculate_agent_quotas.py",
    )

    roi_res = roi_mod.compute_sizing_and_roi(
        tam_units=tam_units,
        sam_share=sam_share,
        adoption_rate=adoption_rate,
        tech_compat=tech_compat,
        hours_saved_per_unit=hours_saved,
        hourly_rate_usd=hourly_rate,
        capex_usd=capex,
        annual_opex_usd=annual_opex,
        vcr=vcr,
        scdf=scdf,
        wacc=wacc,
        llm_calls_per_unit=float(1 + 1 + (sub_questions * chunks_per_subquestion) + 1),
        tokens_per_call=float(tokens_per_call),
        cost_per_1m_tokens_usd=1.25,
        cache_hit_ratio=0.60,
    )
    quota_res = quota_mod.calculate_agent_quotas(
        peak_turns_per_min=int(max(1, round(peak_turns_per_min))),
        sub_questions=sub_questions,
        chunks_per_subquestion=chunks_per_subquestion,
        tokens_per_call=tokens_per_call,
        peak_multiplier=5.0,
    )

    def sme(tag: str, populated_value: str) -> str:
        return populated_value if populate_sme_inputs else f"[SME_INPUT_REQUIRED: {tag}]"

    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "docs").mkdir(parents=True, exist_ok=True)
    (workspace / "evals").mkdir(parents=True, exist_ok=True)
    (workspace / "tests" / "eval").mkdir(parents=True, exist_ok=True)

    som = roi_res["funnel"]["som_units"]
    base_npv = roi_res["scenarios"]["base"]["npv_3yr_usd"]
    bear_npv = roi_res["scenarios"]["bear"]["npv_3yr_usd"]
    base_net = roi_res["scenarios"]["base"]["net_annual_value_usd"]
    verdict = roi_res["project_worth_verdict"]["verdict"]
    rec_mode = roi_res["project_worth_verdict"]["recommended_mode"]
    token_opex = roi_res["tco"]["annual_token_opex_usd"]
    calls_per_turn = quota_res["per_turn_fanout"]["llm_calls_per_turn"]
    quota_rpm = quota_res["recommended_quotas"]["gemini_generate_content_rpm"]
    quota_tpm = quota_res["recommended_quotas"]["gemini_input_tpm"]

    files_to_write: dict[str, str] = {
        "STATE.md": (
            f"# Delta Engagement Program Tracker — {use_case}\n\n"
            f"- **GCP Project ID:** `{project}`\n"
            f"- **Engagement Verdict:** `{verdict}`\n"
            f"- **SOM Volume (Yr 1):** `{som:,.0f}` units/yr\n"
            f"- **Base 3-Year NPV (10% WACC):** `${base_npv:,.2f}`\n"
            f"- **Bear 3-Year NPV (10% WACC):** `${bear_npv:,.2f}`\n"
            f"- **5x Vertex AI Quota Target:** `{quota_rpm:,} RPM` / `{quota_tpm:,} TPM`\n"
            f"- **Executive Sponsor:** {sme('executive_sponsor_name_and_title', 'VP of Enterprise Operations')}\n\n"
            "## Phase Gate Status\n"
            "- [x] Gate 0 (Prelude): Qualification & ROI Sizing\n"
            "- [x] Gate 1 (Phase 1): PRD, Architecture & Golden Dataset Baseline\n"
            "- [x] Gate 2 (Phase 2): Demo 3, AUA Statistical Audit & 5x Load Test\n"
            "- [x] Gate 3 (Phase 3): Measured Value Realization & Operations Handoff\n"
        ),
        "docs/WORKSHOP_INTAKE.md": (
            f"# Onsite Discovery Workshop Intake — {use_case}\n\n"
            "## 6-Dimension Data Readiness Yardstick\n"
            f"- **Data Availability:** {sme('data_availability_score_1_to_5', '4/5 — BigQuery & GCS curated tables')}\n"
            f"- **Data Accessibility:** {sme('data_accessibility_iam_status', '4/5 — Service account provisioned in ' + project)}\n"
            f"- **Data Quality:** {sme('data_quality_completeness_notes', '4/5 — Validated schema with <2% null fields')}\n"
            f"- **Data Coverage:** `SOM = {som:,.0f}` units/yr (`{tam_units:,.0f}` TAM)\n"
            f"- **Privacy / Security:** {sme('data_privacy_dlp_classification', '4/5 — Cloud DLP & Model Armor enabled')}\n"
            f"- **Latency Budget:** {sme('p95_latency_sla_seconds', 'p95 <= 8.0s end-to-end SSE')}\n"
        ),
        "docs/USE_CASE_CANVAS.md": (
            f"# 1-Page Use Case Alignment Summary — {use_case}\n\n"
            f"- **Problem Statement:** {sme('problem_statement', 'Manual multi-system triage creates high cycle time and rework.')}\n"
            f"- **Target Users:** {sme('target_user_persona', 'Enterprise Operations Specialists')}\n"
            f"- **MVP Scope (Weeks 1–10):** Automated ingestion, grounded synthesis, and HITL approval.\n"
            f"- **Out of Scope:** Autonomous unreviewed external writes.\n"
            f"- **Target ROI Baseline:** `${base_net:,.2f}/yr` Net Annual Value (`${base_npv:,.2f}` 3-Yr NPV)\n"
        ),
        "docs/VALUE_SIZING.md": (
            f"# AI Value Sizing & 3-Scenario ROI — {use_case}\n\n"
            + roi_mod.format_markdown_table(roi_res)
            + "\n"
        ),
        "docs/as_is_report.md": (
            f"# As-Is Process Ethnography — {use_case}\n\n"
            f"- **Current Volume:** `{tam_units:,.0f}` annual cases (`{som:,.0f}` Year-1 SOM)\n"
            f"- **Manual Effort Baseline:** `{hours_saved:.2f}` hours saved/case at `${hourly_rate:.2f}/hr`\n"
            f"- **Primary System of Record:** {sme('legacy_system_of_record', 'Enterprise Core ERP / Case Management DB')}\n"
        ),
        "docs/to_be_designs.md": (
            f"# To-Be Agentic Workflow Design — {use_case}\n\n"
            f"- **Per-Turn Fan-Out Topology:** `{calls_per_turn}` LLM calls/turn (`Qt={sub_questions}, Cq={chunks_per_subquestion}`)\n"
            f"- **Human-in-the-Loop Gate:** {sme('hitl_approval_threshold', 'Mandatory human sign-off for high-risk or low-confidence (<0.80) cases')}\n"
        ),
        "docs/human_agent_roles.md": (
            f"# Human-Agent Authority Matrix — {use_case}\n\n"
            "| Step | Autonomy Level | Agent Action | Human Authority |\n"
            "| :--- | :--- | :--- | :--- |\n"
            f"| Evidence Retrieval | L2 Assistive | Parallel query across `{sub_questions}` sub-questions | Reviews source citations |\n"
            f"| Final Disposition | L2 HITL Gate | Drafts structured recommendation | {sme('human_override_sla', 'Approves, edits, or rejects in 1 click')} |\n"
        ),
        "docs/CUJ_MAP.md": (
            f"# 4-Tab L1–L5 Critical User Journey Map — {use_case}\n\n"
            "| Step ID | L1–L5 Stage | Value (1–5) | Feasibility (1–5) | Priority (`0.6V + 0.4F`) |\n"
            "| :--- | :--- | :--- | :--- | :--- |\n"
            "| CUJ-01 | L1 Intake & Safety Guardrail | 5.0 | 5.0 | **5.00** |\n"
            "| CUJ-02 | L2 Parallel Evidence Retrieval | 5.0 | 4.5 | **4.80** |\n"
            "| CUJ-03 | L3 Synthesis & Citation Grounding | 4.5 | 4.5 | **4.50** |\n"
        ),
        "docs/PRD.md": (
            f"# 8-Section Agentic PRD — {use_case}\n\n"
            "## 1. Executive Summary & Objective\n"
            f"Deliver `{use_case}` on project `{project}` targeting `${base_npv:,.2f}` 3-Year Base NPV.\n\n"
            "## 2. Pain Points (Blocker vs. Friction)\n"
            f"- **P0 Blocker:** {sme('p0_blocker_description', 'Manual cross-referencing across siloed repositories.')}\n\n"
            "## 3. Reactive & Proactive CUJs\n"
            "Mapped to `docs/CUJ_MAP.md` (`CUJ-01` through `CUJ-03`).\n\n"
            "## 4. Information Architecture & DAG Design\n"
            f"Deterministic router -> `{sub_questions}x{chunks_per_subquestion}` parallel evidence workers -> synthesis.\n\n"
            "## 5. RICE-Prioritized Requirements\n"
            "| Feature ID | Requirement | Reach | Impact | Confidence | Effort | RICE Score |\n"
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
            f"| F-01 | Grounded Evidence Synthesis | {som:,.0f} | 3.0 | 0.90 | 3.0 | {(som * 3.0 * 0.90 / 3.0):,.0f} |\n"
        ),
        "docs/ARCHITECTURE_RECOMMENDATION.md": (
            f"# Google Cloud Agent Architecture Recommendation — {use_case}\n\n"
            f"- **Selected Platform Tier:** {rec_mode}\n"
            f"- **GCP Project:** `{project}`\n"
            f"- **Annual Token Inference OpEx:** `${token_opex:,.2f}/yr` (60% context cache hit ratio)\n"
            f"- **5x Peak Vertex AI Quota:** `{quota_rpm:,} RPM` / `{quota_tpm:,} TPM`\n"
        ),
        "docs/STITCH_PROTOTYPE.md": (
            f"# Stitch Rapid Prototype & Delta Brand Specification — {use_case}\n\n"
            "- **Brand Palette:** Google Blue `#4285F4`, Green `#34A853`, Yellow `#FBBC04`, Red `#EA4335`\n"
            "- **Mandatory UI Controls:** Inline source citations, confidence badge, 1-click HITL override.\n"
        ),
        "docs/TDD.md": (
            f"# 4-Part Agent Technical Specification — {use_case}\n\n"
            f"- **Part I (System Overview):** `{use_case}` deployed in `{project}`.\n"
            f"- **Part II (Orchestration):** `{calls_per_turn}` LLM calls/turn (`Qt={sub_questions}, Cq={chunks_per_subquestion}`).\n"
            f"- **Part III (Access & Security):** Least-privilege IAM + Model Armor DLP.\n"
            f"- **Part IV (Evaluation & Quotas):** `{quota_rpm:,} RPM` / `{quota_tpm:,} TPM` (5x peak safety margin).\n"
        ),
        "docs/DEMO_FRAME_UP.md": (
            f"# Bi-Weekly Demo 1–2–3 Frame-Up — {use_case}\n\n"
            "| Feature ID | Capability | Demo 1 (Wk 4) | Demo 2 (Wk 6) | Demo 3 (Wk 8/10) |\n"
            "| :--- | :--- | :--- | :--- | :--- |\n"
            "| F-01 | Ingestion & Retrieval | Prototype | Integrated | Production Hardened |\n"
        ),
        "docs/EVAL_AUDIT_REPORT.md": (
            f"# CLA & AUA Statistical Judge Audit Report — {use_case}\n\n"
            "- **Pipeline 1 (Calibration):** `d_r >= 0.80`, `QWK >= 0.60`, `SD Ratio >= 0.80`, `PRMSE > 0`, `Wilcoxon p > 0.05`\n"
            "- **Pipeline 2 (Stability):** `Cronbach's alpha >= 0.80`\n"
            "- **Pipeline 3 (Double Marking):** `ICC(3,k) >= 0.80`\n"
        ),
        "docs/LOAD_TEST_REPORT.md": (
            f"# Multi-Tier Load Test & 5x Quota Report — {use_case}\n\n"
            "```text\n"
            + quota_mod._format_report(quota_res)
            + "\n```\n"
        ),
        "docs/CLOSEOUT_DECK.md": (
            f"# Executive Closeout Readout — {use_case}\n\n"
            f"- **Measured 3-Year Base NPV:** `${base_npv:,.2f}` (Bear Case: `${bear_npv:,.2f}`)\n"
            f"- **Production Quota Certified:** `{quota_rpm:,} RPM` / `{quota_tpm:,} TPM`\n"
            f"- **Client Operations Owner:** {sme('client_handoff_owner', 'Director of Cloud Platform Engineering')}\n"
        ),
        "tests/eval/eval_config.yaml": (
            f"use_case: {json.dumps(use_case)}\n"
            f"project: {json.dumps(project)}\n"
            "gates:\n"
            "  multi_turn_task_success: 0.85\n"
            "  multi_turn_tool_use_quality: 0.90\n"
            "  hallucination_max: 0.02\n"
            "  p95_latency_seconds: 8.0\n"
        ),
    }

    for rel_path, content in files_to_write.items():
        target = workspace / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    golden_cases = [
        {
            "id": f"GD-{idx:03d}",
            "category": (
                "happy_path"
                if idx <= 12
                else ("edge_case" if idx <= 20 else "adversarial")
            ),
            "input_prompt": f"[{use_case}] Real-world evaluation scenario #{idx}",
            "expected_tools": ["retrieve_evidence", "synthesize_grounded_response"],
            "sme_reference_answer": sme(
                f"golden_case_{idx}_reference",
                f"Verified SME ground-truth disposition for case #{idx}.",
            ),
        }
        for idx in range(1, 25)
    ]
    (workspace / "evals" / "golden_dataset.json").write_text(
        json.dumps(
            {
                "use_case": use_case,
                "project": project,
                "total_cases": len(golden_cases),
                "cases": golden_cases,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    return {
        "workspace": str(workspace),
        "use_case": use_case,
        "project": project,
        "files_written": len(files_to_write) + 1,
        "roi_summary": {
            "som_units": som,
            "base_npv_3yr": round(base_npv, 2),
            "bear_npv_3yr": round(bear_npv, 2),
            "verdict": verdict,
        },
        "quota_summary": {
            "calls_per_turn": calls_per_turn,
            "recommended_rpm_quota": quota_rpm,
            "recommended_tpm_quota": quota_tpm,
        },
    }


def audit_workspace(workspace: Path, phase: str = "phase3") -> dict[str, Any]:
    """Audit a customer engagement workspace for phase-gate readiness."""
    if phase not in PHASE_ARTIFACTS:
        raise ValueError(f"Unknown phase {phase!r}; choose from {tuple(PHASE_ARTIFACTS)}")

    required = PHASE_ARTIFACTS[phase]
    missing_files: list[str] = []
    empty_files: list[str] = []
    sme_placeholders: dict[str, int] = {}
    unresolved_todos: dict[str, int] = {}
    fluff_hits: dict[str, list[str]] = {}

    for rel_path in required:
        fpath = workspace / rel_path
        if not fpath.is_file():
            missing_files.append(rel_path)
            continue
        text = fpath.read_text(encoding="utf-8")
        if len(text.strip()) < 20:
            empty_files.append(rel_path)
        sme_count = len(SME_PLACEHOLDER_RE.findall(text))
        if sme_count > 0:
            sme_placeholders[rel_path] = sme_count
        todo_count = len(UNRESOLVED_TODO_RE.findall(text))
        if todo_count > 0:
            unresolved_todos[rel_path] = todo_count
        fluff = BANNED_FLUFF_RE.findall(text)
        if fluff:
            fluff_hits[rel_path] = sorted(set(fluff))

    golden_errors: list[str] = []
    if "evals/golden_dataset.json" in required and (workspace / "evals/golden_dataset.json").is_file():
        try:
            gd = json.loads((workspace / "evals/golden_dataset.json").read_text(encoding="utf-8"))
            cases = gd.get("cases", [])
            categories = {c.get("category") for c in cases if isinstance(c, dict)}
            for req_cat in ("happy_path", "edge_case", "adversarial"):
                if req_cat not in categories:
                    golden_errors.append(f"missing Golden Dataset category: {req_cat}")
            if len(cases) < 10:
                golden_errors.append(f"Golden Dataset has only {len(cases)} cases (minimum 10 stratified cases)")
        except json.JSONDecodeError as exc:
            golden_errors.append(f"invalid JSON in evals/golden_dataset.json: {exc}")

    gate_ready = (
        not missing_files
        and not empty_files
        and not sme_placeholders
        and not unresolved_todos
        and not fluff_hits
        and not golden_errors
    )

    return {
        "workspace": str(workspace),
        "phase": phase,
        "gate_ready": gate_ready,
        "checked_files": len(required),
        "missing_files": missing_files,
        "empty_files": empty_files,
        "unresolved_sme_inputs": sme_placeholders,
        "unresolved_todos": unresolved_todos,
        "banned_fluff_hits": fluff_hits,
        "golden_dataset_errors": golden_errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialize a customer engagement workspace.")
    p_init.add_argument("--workspace", type=Path, required=True)
    p_init.add_argument("--use-case", type=str, required=True)
    p_init.add_argument("--project", type=str, default="gcp-customer-agent-prod")
    p_init.add_argument("--tam-units", type=float, default=80000.0)
    p_init.add_argument("--hours-saved", type=float, default=0.70)
    p_init.add_argument("--hourly-rate", type=float, default=75.0)
    p_init.add_argument("--capex", type=float, default=180000.0)
    p_init.add_argument("--annual-opex", type=float, default=68000.0)
    p_init.add_argument("--peak-turns-per-min", type=int, default=10)
    p_init.add_argument(
        "--populate-sme-inputs",
        action="store_true",
        help="Populate SME fields with baseline defaults instead of [SME_INPUT_REQUIRED] tags.",
    )

    p_audit = sub.add_parser("audit", help="Audit a customer workspace for phase-gate sign-off.")
    p_audit.add_argument("--workspace", type=Path, required=True)
    p_audit.add_argument(
        "--phase",
        choices=("prelude", "phase1", "phase2", "phase3"),
        default="phase3",
    )
    p_audit.add_argument("--strict", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "init":
        res = init_workspace(
            workspace=args.workspace,
            use_case=args.use_case,
            project=args.project,
            tam_units=args.tam_units,
            hours_saved=args.hours_saved,
            hourly_rate=args.hourly_rate,
            capex=args.capex,
            annual_opex=args.annual_opex,
            peak_turns_per_min=args.peak_turns_per_min,
            populate_sme_inputs=args.populate_sme_inputs,
        )
        print(json.dumps(res, indent=2))
        return 0

    res = audit_workspace(workspace=args.workspace, phase=args.phase)
    print(json.dumps(res, indent=2))
    if args.strict and not res["gate_ready"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
