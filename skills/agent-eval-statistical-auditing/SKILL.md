---
name: agent-eval-statistical-auditing
description: >
  Evaluate agent output quality at Layer 3 (Communicative Language Ability, 27-criterion menu,
  pick 3-5) with one isolated LLM judge per criterion, then statistically audit the judge
  itself: Pipeline 1 human-vs-judge calibration (PRMSE, disattenuated d.R, QWK, Wilcoxon W,
  scale compression), Pipeline 2 intra-rater stability (Cronbach's alpha, SEM), Pipeline 3
  inter-model double marking (ICC(3,k), r, rho, QWK, confidence routing). Produces an Assessment
  Use Argument (AUA) report with pass/fail gates. Triggers on "audit the llm judge", "aua report",
  "cla rubric", "quadratic weighted kappa", "prmse", "double marking", "linguistic quality eval".
metadata:
  version: '1.2'
---

# Linguistic Output Quality & Statistical Auditing for LLM-as-a-Judge (`agent-eval-statistical-auditing`)

Sources: TDL Toolbox decks *Linguistic Output Quality Evaluation Framework* and *Statistical Auditing for LLM-as-a-Judge* (H. González). Thresholds marked **(deck)** are the deck's; the few this repo adds are marked **(repo convention)**.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 (Golden Dataset Rubric Setup) & Phase 2 Sprints 3–4 (Weeks 7–10), repo convention:** CLA rubric & AUA judge certification |
| **Reads (Inputs)** | `docs/PRD.md` (persona, register, business risk), `docs/TDD.md` (Part IV Golden Dataset), paired human SME + LLM judge scores |
| **Writes (Outputs)** | `docs/EVAL_AUDIT_REPORT.md` (AUA certification report + chosen CLA criteria + isolated judge prompts) |
| **Primary CLI Command** | `python3 skills/agent-eval-statistical-auditing/scripts/audit_llm_judge.py --demo` |

---

## 1. Where this sits: the 3-layer pyramid

| Layer | Question | Typical metrics |
|---|---|---|
| 1 — Technical | Did the API fire? Tool trajectory, latency, schema validity | deterministic |
| 2 — Functional / IR | Did it retrieve the right fact? Precision/recall@k, faithfulness | deterministic or NLI |
| **3 — Linguistic output quality (CLA)** | Is the long-form text/conversation *communicatively* good for this user and context? | **isolated LLM judges, statistically audited** |

Layers 1–2 are "machine-centered". Not measuring Layer 3 "leaves us blind to the linguistic failures that customers are starting to consider".

---

## 2. Define the construct (pick 3–5 criteria, one judge each)

1. Open the 27-criterion menu in [references/cla-rubric-and-aua-methodology.md](references/cla-rubric-and-aua-methodology.md) (Organizational → Grammatical/Textual; Pragmatic → Functional/Sociolinguistic; Strategic → Goal Setting/Assessment/Planning/Execution & Repair).
2. Choose **3–5 criteria or composites** that drive adoption or mitigate the engagement's risk (deck examples: GRE/TOEFL = Vocabulary, Syntax, Organization, Content at 25% each; analyst agent = Registers weighted 20%; B2B sales = Textual + Manipulative).
3. Write a **pointwise 1–5 rubric with behavioral anchors for every level** per criterion. No pairwise judging, no "score 1–5 on these 10 dimensions" prompts.
4. Instantiate **one LLM judge per criterion** (halo-effect control). Record model, temperature and prompt hash in `docs/EVAL_AUDIT_REPORT.md`.

---

## 3. Audit the judge: three pipelines, one deterministic auditor

Humans design the rubric (Role 1); the LLM judge scales it (Role 2); a **deterministic statistical auditor with zero AI in the math** certifies whether the judge can be trusted. Run `scripts/audit_llm_judge.py`.

| Pipeline | When | Metrics | Gates |
|---|---|---|---|
| **1. Development calibration — human vs. LLM judge** | Before trusting a judge; Golden Dataset double-scored by 2 human SMEs (deck report: N = 30) | PRMSE, disattenuated correlation d.R (strips human noise), Pearson r, exact & adjacent agreement, QWK, Wilcoxon signed-rank W (severity bias), scale compression SD ratio | d.R ≥ 0.80 **(deck)** · QWK ≥ 0.60 **(deck)** · SD ratio ≥ 0.80 **(deck)** · PRMSE > 0 **(deck)** · Wilcoxon p > 0.05 **(repo)** |
| **2. Live production, option A — intra-rater** | No human ground truth; one judge, same text **5 passes at T > 0** | Cronbach's α, SEM, 95% CI (= ± 2 SEM) | α ≥ 0.80 **(deck)** |
| **3. Live production, option B — inter-model double marking** | Two model families (e.g. Gemini + Sonnet), **1 pass each at T = 0.0**, scores averaged | ICC(3,k), Pearson r, Spearman ρ, exact & adjacent agreement, QWK, Wilcoxon W, per-item confidence → HITL queue | ICC(3,k) ≥ 0.80 **(deck's AUA report pass rule; its reference report passes at 0.857)** · per-criterion ρ ≥ 0.70 & QWK ≥ 0.60 flags **(deck)** |

Known blind spots (deck): Pipeline 2 cannot see severity bias or compression (a consistently biased judge gets a perfect α); Pipeline 3 cannot see two models being wrong together (agreement–accuracy paradox). Pipeline 1 is therefore mandatory once per rubric version.

```bash
# both bundled synthetic fixtures (one calibrated judge, one compressed + lenient judge)
python3 skills/agent-eval-statistical-auditing/scripts/audit_llm_judge.py --demo

# your data (JSON schema in the script docstring; per-criterion blocks optional)
python3 skills/agent-eval-statistical-auditing/scripts/audit_llm_judge.py --input ratings.json --json
```

`d.R` divides r by √(human inter-rater r × judge reliability). The script uses Pipeline 2's α as judge reliability when `passes` are supplied, otherwise **1.0 (conservative)**; override with `--llm-reliability`. The HITL routing count (confidence < 0.75) is a repo convention exposed as `--hitl-threshold`. There are no hidden constants.

---

## 4. Procedure

1. Choose criteria and write anchored rubrics (§2). Save prompts under `evals/judges/<criterion>.md`.
2. Have **two** human SMEs score the Golden Dataset on each criterion (N ≥ 30).
3. Run each judge over the same items; build `ratings.json` with `human_r1`, `human_r2`, `llm_scores` per criterion.
4. Run Pipeline 1. If **compression** fails → add few-shot anchors at scores 1 and 5 and re-run. If **Wilcoxon** flags bias → fix the rubric's severity, not the threshold. If **QWK** fails but d.R passes → the judge rank-orders well but mis-scales; re-anchor.
5. In production, pick option A (5 passes; higher token cost, N = 1 routing via per-item SD) or option B (2 models; lower cost, asymmetric drift detection, vendor dependency). Route low-confidence items to humans.
6. Write `docs/EVAL_AUDIT_REPORT.md`: criteria + weights, judge configs, the AUA report text verbatim, deployment decision.

---

## 5. References & worked example

- [scripts/audit_llm_judge.py](scripts/audit_llm_judge.py) — stdlib auditor; unit-tested; `--demo` runs the bundled fixtures.
- [examples/fixtures/calibrated_judge.json](examples/fixtures/calibrated_judge.json), [examples/fixtures/compressed_lenient_judge.json](examples/fixtures/compressed_lenient_judge.json) — synthetic, seeded inputs (generator documented in the `_note` field).
- [references/cla-rubric-and-aua-methodology.md](references/cla-rubric-and-aua-methodology.md) — the 27 criteria, the 11 cited biases, the architectural rules.
- [examples/enterprise-analyst-aua-certification.md](examples/enterprise-analyst-aua-certification.md) — the deck's own AUA reports (real numbers from its ADK implementation) side by side with the script's verbatim output on the fixtures.
