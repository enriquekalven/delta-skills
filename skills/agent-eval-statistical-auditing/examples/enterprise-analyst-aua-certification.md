# Worked Example: `docs/EVAL_AUDIT_REPORT.md` — AUA Certification of a Layer-3 Judge

Two sources are shown side by side and **never mixed**:

- **Part A** — the AUA reports printed in the TDL Toolbox deck, which the author states are *"a real example output from my implementation in ADK"* (N = 30 essays; criteria Vocabulary, Syntax, Textual Knowledge, Functional Knowledge).
- **Part B** — the verbatim output of `scripts/audit_llm_judge.py --demo` on the two **synthetic, seeded fixtures** bundled with this skill. A unit test asserts that the numbers quoted here are the numbers the script prints.

---

## Part A — The deck's reference reports (real ADK output)

### A.1 Pipeline 1 — Development calibration, human vs. Gemini judge (N = 30)

```text
Assessment Use Argument (AUA) Final Report — Batch Processing (N=30 essays)
Predictive Accuracy (PRMSE):          0.400
Disattenuated Correlation (d.R):      0.809  (Raw Pearson r: 0.746)
Systematic Bias Detected:             False  (Wilcoxon W: 15.0, p-value: 0.727)
Scale Compression Flag:               COMPRESSION DETECTED (Ratio < 0.80)
Warning: Alignment is high, but severe Scale Compression is detected. The judge
clusters scores in the middle. Few-shot calibration required.

Per-criterion (thresholds d.rho >= 0.70, QWK >= 0.60)
  PASS Vocabulary:           d.rho 0.926 | QWK 0.700 | Exact 62.5%
  FAIL Syntax:               d.rho 0.663 | QWK 0.348 | Exact 50.0%
  PASS Textual Knowledge:    d.rho 0.966 | QWK 0.737 | Exact 37.5%
  FAIL Functional Knowledge: d.rho 0.663 | QWK 0.429 | Exact 37.5%
```

Reading: holistic alignment passes (d.R 0.809 ≥ 0.80, no severity bias) but the judge compresses the scale and two criteria fail → **do not deploy; add few-shot anchors for Syntax and Functional Knowledge, re-run Pipeline 1.**

### A.2 Pipeline 2 — Intra-rater stability, 5 passes (N = 30 × 5)

```text
Cronbach's Alpha (α):                 0.982
Standard Error of Measurement (SEM):  0.077
95% Confidence Interval:              Observed Score ± 0.15
Deployment Decision: PASS — overall reliability ≥ .80
Per-criterion α: Vocabulary 0.920 | Syntax 0.894 | Textual 0.973 | Functional 0.916
Item view: Text 1 3.10/5 (Vocab 2.80, Syntax 2.00, Textual 4.00, Functional 3.60) …
```

### A.3 Pipeline 3 — Inter-model double marking (Gemini + Sonnet, T = 0)

```text
Absolute Agreement (ICC3k):           0.857
Linear Consistency (Pearson r):       0.926
Systematic Bias Detected:             False  (Wilcoxon W: 3.5, p-value: 0.062)
Per-criterion flags driven by Spearman ρ and QWK, e.g.
  FAIL Functional Knowledge: ρ 0.630 | QWK 0.400 | Exact 25.0% | Adjacent 100.0%
Item view: Text 1 Final 2.88/5 | Confidence 99.6% Auto-Approved
           Text 2 Final 3.50/5 | Confidence 93.8% Auto-Approved …
```

---

## Part B — Script output on the bundled fixtures (synthetic, reproducible)

Fixtures: [fixtures/calibrated_judge.json](fixtures/calibrated_judge.json) (isolated per-criterion judge, no bias) and [fixtures/compressed_lenient_judge.json](fixtures/compressed_lenient_judge.json) (one monolithic prompt: compresses toward 3, lenient by +0.6). Both: N = 30, two human raters, a second model family, 5 stochastic passes, 4 criteria. Generator and seed are in each file's `_note`.

```bash
python3 delivery/agent-eval-statistical-auditing/scripts/audit_llm_judge.py --demo
```

### B.1 Calibrated judge → PASS on all three pipelines

```text
[Pipeline 1] Development calibration, human vs. LLM judge (N=30)
  Exact / adjacent agreement : 56.7% / 100.0%
  Pearson r                  : 0.8855   (human inter-rater r 0.9001, LLM reliability 0.9786)
  Disattenuated d.R          : 0.9435   gate >= 0.80
  QWK                        : 0.8592   gate >= 0.60
  PRMSE                      : 0.8234   gate > 0
  Wilcoxon W / p             : 55.0 / 0.5014   bias flag if p <= 0.05
  Scale compression SD ratio : 0.9777   gate >= 0.80  (SD LLM 1.2341 / SD human 1.2622)
  Verdict                    : PASS

[Pipeline 2] Intra-rater stability, 5 passes (N=30)
  Cronbach's alpha           : 0.9786   gate >= 0.80
  SEM                        : 0.1750   95% CI = observed +/- 0.35 (2 SEM)
  Verdict                    : PASS

[Pipeline 3] Inter-model double marking (N=30)
  ICC(3,k)                   : 0.9138   gate >= 0.80
  Pearson r / Spearman rho   : 0.8459 / 0.8433
  QWK                        : 0.8382
  Exact / adjacent agreement : 56.7% / 100.0%
  Wilcoxon W / p             : 35.0 / 0.4631
  Items with confidence <0.75: 0 of 30 -> HITL queue
  Verdict                    : PASS

[Per-criterion diagnostics] d.rho >= 0.70 and QWK >= 0.60
  Vocabulary            : PASS  (d.rho/rho 0.9190, QWK 0.8219)
  Syntax                : PASS  (d.rho/rho 1.0000, QWK 0.8571)
  Textual Knowledge     : PASS  (d.rho/rho 0.9654, QWK 0.8184)
  Functional Knowledge  : PASS  (d.rho/rho 1.0000, QWK 0.7729)
```

### B.2 Compressed + lenient judge → FAIL (and why each gate matters)

```text
[Pipeline 1] Development calibration, human vs. LLM judge (N=30)
  Exact / adjacent agreement : 40.0% / 86.7%
  Pearson r                  : 0.7277   (human inter-rater r 0.6182, LLM reliability 0.8853)
  Disattenuated d.R          : 0.9837   gate >= 0.80
  QWK                        : 0.4275   gate >= 0.60
  PRMSE                      : -0.3201   gate > 0
  Wilcoxon W / p             : 4.0 / <0.0001   bias flag if p <= 0.05
  Scale compression SD ratio : 0.4943   gate >= 0.80  (SD LLM 0.4983 / SD human 1.008)
  Verdict                    : FAIL -> recalibrate rubric / few-shot anchors

[Pipeline 2] Intra-rater stability, 5 passes (N=30)
  Cronbach's alpha           : 0.8853   gate >= 0.80
  SEM                        : 0.1805   95% CI = observed +/- 0.361 (2 SEM)
  Verdict                    : PASS

[Pipeline 3] Inter-model double marking (N=30)
  ICC(3,k)                   : 0.6064   gate >= 0.80
  Pearson r / Spearman rho   : 0.4742 / 0.4793
  QWK                        : 0.3312
  Exact / adjacent agreement : 50.0% / 93.3%
  Wilcoxon W / p             : 7.0 / 0.0026
  Items with confidence <0.75: 2 of 30 -> HITL queue
  Verdict                    : FAIL

[Per-criterion diagnostics] d.rho >= 0.70 and QWK >= 0.60
  Vocabulary            : MIXED (d.rho/rho 0.9224, QWK 0.4528)
  Syntax                : MIXED (d.rho/rho 1.0000, QWK 0.5506)
  Textual Knowledge     : MIXED (d.rho/rho 0.8573, QWK 0.4627)
  Functional Knowledge  : MIXED (d.rho/rho 0.7829, QWK 0.4595)
```

What the failing run teaches (and matches the deck's warnings):

| Signal | Value | Lesson |
|---|---|---|
| d.R **passes** (0.9837) while QWK fails (0.4275) | rank-order is fine, absolute scale is not | d.R alone is not a deployment gate — the deck pairs it with QWK and compression |
| SD ratio 0.4943 | judge clusters at 3–4 | the deck's own report raised the same flag → few-shot anchors at 1 and 5 |
| Wilcoxon p < 0.0001, PRMSE −0.32 | systematic leniency; predicts worse than the sample mean | fix the rubric's severity, not the threshold |
| Pipeline 2 **passes** (α 0.8853) on the same bad judge | consistent ≠ accurate | the deck's "illusion of accuracy" con for option A — Pipeline 1 is mandatory |
| Pipeline 3 fails (ICC 0.6064), 2 items routed to HITL | the second model does not share the compression | the deck's asymmetric-drift benefit of option B |

---

## Deployment decision recorded in `docs/EVAL_AUDIT_REPORT.md`

- Criteria: Vocabulary, Syntax, Textual Knowledge, Functional Knowledge (one anchored 1–5 judge each).
- Pipeline 1 verdict on the current rubric version: **PASS** (calibrated fixture) / **FAIL → re-anchor** (compressed fixture).
- Production monitoring: option B (Gemini + Sonnet at T = 0); auto-approve when confidence ≥ 0.75 (repo convention, `--hitl-threshold`), otherwise HITL queue; re-run Pipeline 1 on every rubric or model change.
