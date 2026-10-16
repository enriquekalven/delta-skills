"""Unit tests for scripts/validate_skills.py, calculate_roi.py, calculate_agent_quotas.py, and audit_llm_judge.py."""

from __future__ import annotations

import io
import json
import os
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "ai-value-sizing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "delivery" / "agent-load-testing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "delivery" / "agent-eval-statistical-auditing" / "scripts"))

import audit_llm_judge
import calculate_agent_quotas
import calculate_roi
import validate_skills

VALID_EXAMPLE_MD = """# Worked Example: My Skill

## 1. Input Context
Input file `docs/WORKSHOP_INTAKE.md` with baseline scope.

## 2. Step-by-Step Execution
1. Parse the input requirements.
2. Run deterministic validation checks.
3. Generate the target deliverable.

## 3. Verified Output Artifact
Output written to `docs/OUTPUT.md` and verified against schema.
"""


class ValidateSkillsTests(unittest.TestCase):
    def test_valid_skill_and_links_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            ref = sdir / "references"
            ex = sdir / "examples"
            ref.mkdir(parents=True)
            ex.mkdir(parents=True)
            (ref / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (ex / "worked-example.md").write_text(VALID_EXAMPLE_MD, encoding="utf-8")
            (sdir / "SKILL.md").write_text(
                "---\nname: my-skill\ndescription: A valid test skill.\n---\n\nSee [guide](references/guide.md) and [example](examples/worked-example.md).\n",
                encoding="utf-8",
            )
            with redirect_stdout(io.StringIO()):
                code = validate_skills.main(["--root", str(root)])
            self.assertEqual(code, 0)

    def test_detects_missing_worked_example(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            sdir.mkdir()
            (sdir / "SKILL.md").write_text(
                "---\nname: my-skill\ndescription: Valid desc.\n---\n",
                encoding="utf-8",
            )
            errs = validate_skills.validate_skill_file(sdir / "SKILL.md", root)
            self.assertTrue(any("missing required worked example" in e for e in errs))

    def test_detects_mismatched_skill_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            ex = sdir / "examples"
            ex.mkdir(parents=True)
            (ex / "worked-example.md").write_text(VALID_EXAMPLE_MD, encoding="utf-8")
            (sdir / "SKILL.md").write_text(
                "---\nname: wrong-name\ndescription: Valid desc.\n---\n\n[ex](examples/worked-example.md)\n",
                encoding="utf-8",
            )
            errs = validate_skills.validate_skill_file(sdir / "SKILL.md", root)
            self.assertEqual(len(errs), 1)
            self.assertIn("does not match directory name", errs[0])

    def test_detects_unclosed_and_nested_fences(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            md = root / "doc.md"
            md.write_text(
                "# Doc\n\n```\nouter\n```json\n{}\n```\n```\n",
                encoding="utf-8",
            )
            errs = validate_skills.validate_markdown_file(
                md, root, os.path.realpath(root)
            )
            self.assertTrue(any("nested code fence" in e for e in errs))
            self.assertTrue(any("unclosed code fence" in e for e in errs))

    def test_detects_broken_link_orphan_and_gitkeep(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            ref = sdir / "references"
            ex = sdir / "examples"
            ref.mkdir(parents=True)
            ex.mkdir(parents=True)
            (ref / "orphan.md").write_text("# Orphan\n", encoding="utf-8")
            (ref / ".gitkeep").write_text("", encoding="utf-8")
            (ex / "worked-example.md").write_text(VALID_EXAMPLE_MD, encoding="utf-8")
            (sdir / "SKILL.md").write_text(
                "---\nname: my-skill\ndescription: Valid.\n---\n\nSee [missing](references/missing.md) and [ex](examples/worked-example.md).\n",
                encoding="utf-8",
            )
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
                code = validate_skills.main(["--root", str(root)])
            self.assertEqual(code, 1)
            output = err.getvalue()
            self.assertIn("broken relative link", output)
            self.assertIn("orphan skill file", output)
            self.assertIn(".gitkeep", output)

    def test_detects_banned_fluff_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            md1 = root / "a.md"
            md2 = root / "b.md"
            md1.write_text("# Duplicate with context_versioning\n", encoding="utf-8")
            md2.write_text("# Duplicate with context_versioning\n", encoding="utf-8")
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
                code = validate_skills.main(["--root", str(root)])
            self.assertEqual(code, 1)
            output = err.getvalue()
            self.assertIn("banned AI-fluff", output)
            self.assertIn("duplicate markdown files", output)

    def test_detects_invalid_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "bad.json").write_text("{not valid json", encoding="utf-8")
            errs = validate_skills.validate_json_files(root)
            self.assertEqual(len(errs), 1)
            self.assertIn("invalid JSON", errs[0])


class CalculateRoiTests(unittest.TestCase):
    EXAMPLE = REPO_ROOT / "ai-value-sizing" / "examples" / "claims-triage-value-sizing.md"

    def test_worked_example_matches_script_output(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            code = calculate_roi.main([
                "--tam-units", "80000", "--sam-share", "0.625", "--adoption-rate", "0.30",
                "--tech-compat", "0.80", "--hours-saved", "0.70", "--hourly-rate", "75.0",
                "--capex", "180000", "--annual-opex", "68000", "--vcr", "0.5912",
                "--scdf", "0.85", "--wacc", "0.10",
            ])
        self.assertEqual(code, 0)
        data = json.loads(out.getvalue())
        example = self.EXAMPLE.read_text(encoding="utf-8")
        for scen in ("base", "bull", "bear"):
            sc = data["scenarios"][scen]
            for key in ("net_annual_value_usd", "net_3yr_value_usd", "npv_3yr_usd"):
                token = f"${round(sc[key]):,}"
                self.assertIn(token, example, f"{scen}.{key} {token} missing from example")
            self.assertIn(f"{sc['roi_3yr_percent']:.1f}%", example)
            self.assertIn(f"{sc['payback_months']:.1f} mos", example)

    def test_computes_three_scenarios_and_npv(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            code = calculate_roi.main(
                [
                    "--tam-units",
                    "120000",
                    "--sam-share",
                    "0.8",
                    "--adoption-rate",
                    "0.3",
                    "--hours-saved",
                    "0.5",
                    "--hourly-rate",
                    "65",
                    "--capex",
                    "180000",
                    "--annual-opex",
                    "45000",
                    "--vcr",
                    "0.5",
                ]
            )
        self.assertEqual(code, 0)
        payload = json.loads(out.getvalue())
        self.assertIn("scenarios", payload)
        self.assertEqual(
            set(payload["scenarios"].keys()),
            {"base", "bull", "bear"},
        )
        self.assertGreater(payload["scenarios"]["base"]["npv_3yr_usd"], 0)
        self.assertLess(
            payload["scenarios"]["bear"]["npv_3yr_usd"],
            payload["scenarios"]["bull"]["npv_3yr_usd"],
        )

    def test_bear_scdf_floor_and_non_labor_benefit_and_ramp(self) -> None:
        # When Base SCDF is < 0.40 (e.g. 0.25), Bear must not exceed Base
        low_scdf = calculate_roi.compute_sizing_and_roi(
            tam_units=10000,
            sam_share=0.5,
            adoption_rate=0.3,
            tech_compat=1.0,
            hours_saved_per_unit=1.0,
            hourly_rate_usd=100.0,
            capex_usd=50000,
            annual_opex_usd=10000,
            vcr=0.5,
            scdf=0.25,
            annual_non_labor_benefit_usd=50000.0,
            year1_ramp=0.5,
        )
        base_sc = low_scdf["scenarios"]["base"]  # type: ignore[index]
        bear_sc = low_scdf["scenarios"]["bear"]  # type: ignore[index]
        self.assertEqual(bear_sc["scdf"], 0.25)
        self.assertLessEqual(bear_sc["npv_3yr_usd"], base_sc["npv_3yr_usd"])
        self.assertAlmostEqual(
            base_sc["annual_net_cashflow_usd"],
            base_sc["net_annual_value_usd"] - 10000.0,
            places=2,
        )
        # With year1_ramp=0.5, 3-year benefit is 2.5x steady-state annual benefit
        self.assertAlmostEqual(
            base_sc["net_3yr_value_usd"],
            2.5 * base_sc["net_annual_value_usd"],
            places=2,
        )


class CalculateAgentQuotasTests(unittest.TestCase):
    EXAMPLE = REPO_ROOT / "delivery" / "agent-load-testing" / "examples" / "clinical-search-load-test-report.md"

    def test_reproduces_guide_fanout_and_5x_quota(self) -> None:
        res = calculate_agent_quotas.calculate_agent_quotas()  # guide defaults: 10 doctors, Qt=6, Cq=4, 20k tokens/call
        self.assertEqual(res["per_turn_fanout"]["llm_calls_per_turn"], 27)
        self.assertEqual(res["per_turn_fanout"]["vector_grpc_requests_per_turn"], 60)
        self.assertEqual(res["peak_load"]["peak_llm_rpm"], 270)
        self.assertEqual(res["peak_load"]["peak_input_tpm"], 5_400_000)
        self.assertEqual(res["peak_load"]["grpc_pool_waves"], 75)
        self.assertEqual(res["recommended_quotas"]["gemini_generate_content_rpm"], 1_350)
        self.assertEqual(res["recommended_quotas"]["gemini_input_tpm"], 27_000_000)

        low = calculate_agent_quotas.calculate_agent_quotas(chunks_per_subquestion=3)
        self.assertEqual(low["per_turn_fanout"]["llm_calls_per_turn"], 21)
        self.assertEqual(low["peak_load"]["peak_llm_rpm"], 210)

        fixed = calculate_agent_quotas.calculate_agent_quotas(grpc_pool_size=128, cache_hit_ratio=0.6, admission_cap=8)
        self.assertEqual(fixed["peak_load"]["grpc_pool_waves"], 5)
        self.assertEqual(fixed["peak_load"]["peak_input_tpm_after_cache"], 2_160_000)
        self.assertEqual(fixed["admission_control"], {"admitted_turns": 8, "queued_turns": 2, "admitted_llm_rpm": 216})

    def test_rejects_invalid_inputs(self) -> None:
        for kwargs in ({"peak_turns_per_min": 0}, {"cache_hit_ratio": 1.0}, {"peak_multiplier": 0.5}, {"admission_cap": 0}):
            with self.assertRaises(ValueError):
                calculate_agent_quotas.calculate_agent_quotas(**kwargs)

    def test_worked_example_quotes_actual_script_output(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            calculate_agent_quotas.main([])
        example = self.EXAMPLE.read_text(encoding="utf-8")
        for line in out.getvalue().splitlines():
            if line.strip() and not line.startswith("==="):
                self.assertIn(line, example, f"example drifted from script output: {line!r}")


class AuditLlmJudgeTests(unittest.TestCase):
    FIXTURES = audit_llm_judge.FIXTURES_DIR
    EXAMPLE = REPO_ROOT / "delivery" / "agent-eval-statistical-auditing" / "examples" / "enterprise-analyst-aua-certification.md"

    def _load(self, name: str) -> dict:
        return json.loads((self.FIXTURES / f"{name}.json").read_text(encoding="utf-8"))

    def test_calibrated_fixture_passes_all_three_pipelines(self) -> None:
        res = audit_llm_judge.audit(self._load("calibrated_judge"))
        h = res["holistic"]
        self.assertTrue(h["pipeline_1"]["passed"])
        self.assertGreaterEqual(h["pipeline_1"]["disattenuated_d_r"], 0.80)
        self.assertGreaterEqual(h["pipeline_1"]["qwk"], 0.60)
        self.assertGreaterEqual(h["pipeline_1"]["sd_ratio"], 0.80)
        self.assertTrue(h["pipeline_2"]["passed"])
        self.assertTrue(h["pipeline_3"]["passed"])
        self.assertEqual({c["diagnostic"]["flag"] for c in res["criteria"].values()}, {"PASS"})

    def test_compressed_lenient_fixture_fails_calibration_but_looks_consistent(self) -> None:
        res = audit_llm_judge.audit(self._load("compressed_lenient_judge"))
        h = res["holistic"]
        self.assertFalse(h["pipeline_1"]["passed"])
        self.assertLess(h["pipeline_1"]["sd_ratio"], 0.80)      # scale compression caught
        self.assertLess(h["pipeline_1"]["qwk"], 0.60)
        self.assertLessEqual(h["pipeline_1"]["wilcoxon_p"], 0.05)  # leniency bias caught
        self.assertTrue(h["pipeline_2"]["passed"])             # the deck's "illusion of accuracy"
        self.assertFalse(h["pipeline_3"]["passed"])

    def test_statistics_against_known_values(self) -> None:
        self.assertAlmostEqual(audit_llm_judge.pearson_r([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]), 1.0)
        self.assertAlmostEqual(audit_llm_judge.spearman_rho([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), -1.0)
        self.assertAlmostEqual(audit_llm_judge.quadratic_weighted_kappa([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1, 5), 1.0)
        self.assertAlmostEqual(audit_llm_judge.cronbach_alpha([[1, 1], [2, 2], [3, 3], [4, 4]]), 1.0)
        self.assertAlmostEqual(audit_llm_judge.icc_3k([[1, 2], [2, 3], [3, 4], [4, 5]]), 1.0)
        self.assertEqual([audit_llm_judge.round_half_up(v) for v in (1.5, 2.5, 3.5, 4.5)], [2, 3, 4, 5])
        self.assertIsNone(audit_llm_judge.disattenuated_correlation(0.8, 0.0, 1.0))

    def test_llm_reliability_has_no_hidden_default(self) -> None:
        data = {k: v for k, v in self._load("calibrated_judge").items() if k not in ("passes", "criteria")}
        res = audit_llm_judge.audit(data)
        self.assertEqual(res["holistic"]["pipeline_1"]["llm_reliability_assumed"], 1.0)
        res2 = audit_llm_judge.audit(data, llm_reliability=0.9)
        self.assertEqual(res2["holistic"]["pipeline_1"]["llm_reliability_assumed"], 0.9)

    def test_worked_example_quotes_actual_script_output(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            audit_llm_judge.main(["--demo"])
        example = self.EXAMPLE.read_text(encoding="utf-8")
        for line in out.getvalue().splitlines():
            if line.strip() and not line.startswith("===") and not line.startswith("Scale:"):
                self.assertIn(line, example, f"example drifted from script output: {line!r}")


class IndexHtmlContractTests(unittest.TestCase):
    INDEX_HTML = REPO_ROOT / "index.html"

    def test_index_html_has_13_skills_15_steps_and_valid_cli_contracts(self) -> None:
        html = self.INDEX_HTML.read_text(encoding="utf-8")
        self.assertNotIn("14 Skills", html)
        self.assertNotIn("synthetic-baseline-protocol", html)
        self.assertIn("tool-tdl-user-guide plugin (all 13 skills)", html)
        self.assertIn("Example scenario (fictional)", html)
        self.assertIn("CUSTOMER_PRESETS", html)
        self.assertNotIn("customerApprove", html)
        self.assertNotIn("rejectIf", html)
        self.assertNotIn("axesBoost", html)
        for step_num in range(1, 16):
            self.assertIn(f'"step-{step_num}"', html)

    def test_xp_rank_ladder_top_rank_reachable_only_at_full_completion(self) -> None:
        html = self.INDEX_HTML.read_text(encoding="utf-8")

        # Steps per stage: count step ids declared between consecutive stage ids in STAGES.
        stages_block = html[html.index("var STAGES = ["):html.index("var STORAGE_KEY")]
        stage_marks = [(m.group(1), m.start()) for m in re.finditer(r'\bid: "(?!step-)([a-z0-9]+)"', stages_block)]
        step_counts = {}
        for i, (stage_id, start) in enumerate(stage_marks):
            end = stage_marks[i + 1][1] if i + 1 < len(stage_marks) else len(stages_block)
            step_counts[stage_id] = len(re.findall(r'\bid: "step-\d+"', stages_block[start:end]))
        self.assertEqual(sum(step_counts.values()), 15)

        xp_block = html[html.index("var XP_TABLE = {"):html.index("var RANKS = [")]
        xp_table = {
            m.group(1): (int(m.group(2)), int(m.group(3)))
            for m in re.finditer(r"(\w+):\s*\{\s*perStep:\s*(\d+),\s*gateBonus:\s*(\d+)", xp_block)
        }
        self.assertEqual(set(xp_table), set(step_counts), "every stage needs an XP_TABLE entry")

        ranks_start = html.index("var RANKS = [")
        ranks_block = html[ranks_start:html.index("];", ranks_start)]
        thresholds = [int(x) for x in re.findall(r"minXp:\s*(\d+)", ranks_block)]
        titles = re.findall(r'title:\s*"([^"]+)"', ranks_block)
        self.assertEqual(thresholds[0], 0)
        self.assertEqual(thresholds, sorted(set(thresholds)), "rank thresholds must strictly increase")

        max_xp = sum(count * xp_table[sid][0] + xp_table[sid][1] for sid, count in step_counts.items())
        self.assertEqual(thresholds[-1], max_xp, "top rank must equal the max attainable XP")
        self.assertEqual(titles[-1], "Mars Mission Commander")

    def test_quota_cli_supports_both_canonical_and_short_flags(self) -> None:
        out1 = io.StringIO()
        with redirect_stdout(out1):
            rc1 = calculate_agent_quotas.main([
                "--sub-questions", "6",
                "--chunks-per-subquestion", "4",
                "--tokens-per-call", "20000",
                "--peak-turns-per-min", "12",
                "--peak-multiplier", "5.0",
                "--json",
            ])
        out2 = io.StringIO()
        with redirect_stdout(out2):
            rc2 = calculate_agent_quotas.main([
                "--qt", "6",
                "--cq", "4",
                "--tokens-per-call", "20000",
                "--peak-turns-per-min", "12",
                "--safety-multiplier", "5.0",
                "--json",
            ])
        self.assertEqual(rc1, 0)
        self.assertEqual(rc2, 0)
        self.assertEqual(json.loads(out1.getvalue()), json.loads(out2.getvalue()))

    def test_antigravity_plugin_layout(self) -> None:
        plugin_json = REPO_ROOT / "plugin.json"
        self.assertTrue(plugin_json.is_file(), "Missing root plugin.json for Antigravity")
        plugin_meta = json.loads(plugin_json.read_text(encoding="utf-8"))
        self.assertEqual(plugin_meta.get("name"), "tool-tdl-user-guide")

        skills_dir = REPO_ROOT / "skills"
        self.assertTrue(skills_dir.is_dir(), "Missing root skills/ directory for Antigravity")
        real_skill_dirs = [
            p for p in skills_dir.iterdir()
            if p.is_dir() and not p.is_symlink() and (p / "SKILL.md").is_file()
        ]
        self.assertEqual(len(real_skill_dirs), 13, "Expected 13 real skill directories in skills/")

    def test_calculate_roi_supports_demo_and_markdown_flags(self) -> None:
        out_json = io.StringIO()
        with redirect_stdout(out_json):
            rc_json = calculate_roi.main(["--demo"])
        self.assertEqual(rc_json, 0)
        parsed = json.loads(out_json.getvalue())
        self.assertIn("scenarios", parsed)

        out_md = io.StringIO()
        with redirect_stdout(out_md):
            rc_md = calculate_roi.main(["--demo", "--markdown"])
        self.assertEqual(rc_md, 0)
        self.assertIn("| Scenario |", out_md.getvalue())
        self.assertIn("3-Year NPV", out_md.getvalue())


if __name__ == "__main__":
    unittest.main()
