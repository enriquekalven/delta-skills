"""Unit tests for scripts/validate_skills.py, init_skill.py, calculate_roi.py, compute_baseline_stats.py, calculate_agent_quotas.py, and audit_llm_judge.py."""

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "utils" / "skill-creator" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "ai-value-sizing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "delivery" / "synthetic-baseline-protocol" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "delivery" / "agent-load-testing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "delivery" / "agent-eval-statistical-auditing" / "scripts"))

import audit_llm_judge
import calculate_agent_quotas
import calculate_roi
import compute_baseline_stats
import init_skill
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


class InitSkillTests(unittest.TestCase):
    def test_creates_valid_skill_that_passes_validator(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with redirect_stdout(io.StringIO()):
                skill_dir = init_skill.create_skill("sample-skill", tmp)
            self.assertTrue((skill_dir / "SKILL.md").is_file())
            self.assertTrue((skill_dir / "examples" / "worked-example.md").is_file())
            with redirect_stdout(io.StringIO()):
                code = validate_skills.main(["--root", tmp])
            self.assertEqual(code, 0)

    def test_rejects_invalid_or_escaping_skill_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for bad in ("../escape", "Bad_Name", "-leading", "trailing-", ""):
                with self.assertRaises(ValueError):
                    init_skill.create_skill(bad, tmp)


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


class ComputeBaselineStatsTests(unittest.TestCase):
    EXAMPLE = REPO_ROOT / "delivery" / "synthetic-baseline-protocol" / "examples" / "claims-baseline-audit.md"

    def test_worked_example_matches_script_output(self) -> None:
        times = "[16,18,18,19,20,21,22,23,24,25,26,28,30,32,34,35,36,37,37,38,38,38,38,38,38,38,38,39,40,41,42,43,44,45,46,50,53,56,59,62,66,70,74,78,82,84,88,91,95,97]"
        out = io.StringIO()
        with redirect_stdout(out):
            code = compute_baseline_stats.main([
                "--times-json", times, "--errors", "7", "--escalations", "4",
                "--hourly-rate", "75.00", "--overhead-per-unit", "0.00", "--annual-volume", "12000",
            ])
        self.assertEqual(code, 0)
        data = json.loads(out.getvalue())
        example = self.EXAMPLE.read_text(encoding="utf-8")
        ht = data["handling_time_minutes"]
        for token in (f"Mean = `{ht['mean']}", f"Median = `{ht['median']}", f"p90 = `{ht['p90']}", f"SD = `{ht['sd']}",
                      f"[{ht['ci95'][0]}, {ht['ci95'][1]}]",
                      f"{data['error_rate_percent']['value']}%", f"[{data['error_rate_percent']['ci95'][0]}%, {data['error_rate_percent']['ci95'][1]}%]",
                      f"{data['escalation_rate_percent']['value']}%", f"\"unit_cost_usd\": {data['unit_cost_usd']}",
                      f"{int(data['total_baseline_annual_cost_usd'])}"):
            self.assertIn(token, example, f"baseline example drifted: {token!r}")

    def test_computes_baseline_kpis_from_times_array(self) -> None:
        times = [30.0 + (i % 15) for i in range(50)]
        out = io.StringIO()
        with redirect_stdout(out):
            code = compute_baseline_stats.main(
                [
                    "--times-json",
                    json.dumps(times),
                    "--errors",
                    "5",
                    "--escalations",
                    "10",
                    "--hourly-rate",
                    "65",
                    "--overhead-per-unit",
                    "1.25",
                    "--annual-volume",
                    "120000",
                ]
            )
        self.assertEqual(code, 0)
        data = json.loads(out.getvalue())
        self.assertEqual(data["sample_size"], 50)
        self.assertAlmostEqual(data["error_rate_percent"]["value"], 10.0)
        self.assertAlmostEqual(data["escalation_rate_percent"]["value"], 20.0)
        self.assertGreater(data["unit_cost_usd"], 0)


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


if __name__ == "__main__":
    unittest.main()
