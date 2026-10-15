# CLA Criteria Library (27) and LLM-Judge Bias Catalogue (11)

Source: TDL Toolbox deck *Linguistic Output Quality Evaluation Framework* (H. González), which grounds Layer 3 of agent evaluation in Bachman & Palmer's **Communicative Language Ability (CLA)** model. The deck's wording: *"The 3 high-level pillars map into 8 sub-categories, which map into 27 specific scorable criteria. You are never measuring all 27 of these at once. This is a menu, not a mandatory checklist… filter this down to 3 to 5 criteria or composite criteria that actually drive business value and mitigate their specific risks."*

---

## 1. The 27 criteria (3 pillars → 8 sub-categories → 27 criteria)

### Pillar A — Organizational Knowledge *(structure within and beyond the sentence; e.g. can it stay coherent over a 10-page brief or a 20-minute chat?)*

| Sub-category | Criteria |
|---|---|
| **Grammatical Knowledge** | 1. Vocabulary · 2. Syntax · 3. Phonology / Graphology |
| **Textual Knowledge** | 4. Cohesion · 5. Rhetorical Organization · 6. Conversational Organization |

### Pillar B — Pragmatic Knowledge *("read the room": meaning behind the words — consultative tone for a B2B client, exploratory questioning before prescribing)*

| Sub-category | Criteria |
|---|---|
| **Functional Knowledge** | 7. Ideational · 8. Manipulative · 9. Heuristic · 10. Imaginative |
| **Sociolinguistic Knowledge** | 11. Dialects / Varieties · 12. Registers · 13. Naturalness · 14. Cultural References |

### Pillar C — Strategic Competence *(the agent's metacognition: does it say "I don't know" instead of hallucinating; does it repair a misunderstanding or double down?)*

| Sub-category | Criteria |
|---|---|
| **Goal Setting** | 15. Identify the Task · 16. Choose Tasks · 17. Decide on Participation |
| **Assessment** | 18. Assessing the Task · 19. Assessing Resources & Transparency · 20. Building on Previous Knowledge · 21. Monitoring & Evaluating |
| **Planning** | 22. Select Elements · 23. Formulate a Plan · 24. Select a Plan |
| **Execution & Repair** | 25. Repair / Self-Correction · 26. Message Adjustment · 27. Compensating |

Definitions the deck spells out (the full library with definitions, LLM proficiency/limitations per criterion and example rubrics is linked from the deck):
- **Rhetorical Organization** — structuring written text according to genre, logical progression of ideas and overall structure.
- **Heuristic Function** — using language to extend knowledge, learn or solve problems; includes *exploratory questioning* to diagnose before prescribing.
- **Registers** — varying formality to match the communicative context.
- **Compensating** — circumlocution or paraphrase to overcome gaps in vocabulary or data (e.g. explaining a concept when the exact definition is missing).

### How practitioners subset the menu (deck examples)

| Use case | Criteria chosen | Weighting |
|---|---|---|
| Academic certification (GRE / TOEFL) | Vocabulary, Syntax, Organization (= Cohesion + Rhetorical Organization composite), Content (Pragmatic composite) | 25% each |
| Enterprise analyst agent (McKinsey-style) | Heavier on Pragmatics: **Registers** (junior vs. senior analyst — "can the agent sound like a senior analyst?") | Register weighted **20%** |
| B2B sales agent | Textual Knowledge (Cohesion + Rhetorical Organization), **Manipulative** function (persuasion) | per engagement |

---

## 2. The 11 LLM-as-a-Judge biases the framework must guard against

| # | Bias | Failure mode | Citation (as given in the deck) |
|---|---|---|---|
| 1 | **Position bias** | Favors candidates by their order/location in the prompt | Zheng et al., 2023 |
| 2 | **Verbosity bias** | Prefers longer, wordier responses even when less accurate or relevant | Zheng et al., 2023 |
| 3 | **Egocentric bias** | Scores responses from itself or its own model family higher | Koo et al., 2024; Krumdick et al., 2025 |
| 4 | **Compassion-fade bias** | Favors responses labeled with prestigious model names (e.g. "gpt-4") | Koo et al., 2023 |
| 5 | **Diversity bias** | Favors responses aligned with prevailing cultural/demographic stereotypes | Johnson & Zhang, 2024; Zhang et al., 2024 |
| 6 | **Cultural bias** | Scores unfamiliar cultures' expressions poorly; misses regional variants (Western-dominant training data) | Godwin-Jones, 2024; Gu et al., 2025 |
| 7 | **Style bias** | Prefers visually appealing formatting (emojis, emotional tone) | Gu et al., 2025 |
| 8 | **Authority / citation bias** | Favors responses with specific numbers or citations regardless of factual correctness | Gu et al., 2025 |
| 9 | **Familiar-knowledge bias** | Favors facts/topics prevalent in the judge's pre-training data | Gu et al., 2025 |
| 10 | **Leniency bias** | Over-rates quality vs. professional human teachers, especially on content-heavy rubrics | Seßler et al., 2025 |
| 11 | **Pragmatic bias** | Near-chance at unstated implicature; misses sarcasm, humor, indirect requests | Godwin-Jones, 2024; Robrecht et al., 2024 |

### Architectural rules the deck derives from these biases

1. **One LLM judge per criterion.** Bundling constructs (factual accuracy, linguistic depth, style) into one score causes cognitive overload and halo effects; the deck's reference architecture instantiates a separate judge per criterion in every pipeline.
2. **Pointwise, anchored rubrics — not pairwise.** Pairwise judges hide absolute failure (one incoherent answer still "wins") and amplify verbosity/position bias. A 1–5 scale needs **explicit behavioral anchors for every score level**; generic "worst-to-best" descriptors yield unstable, poorly calibrated ratings.
3. **Audit the judge statistically** (Pipelines 1–3 in [SKILL.md](../SKILL.md)); never trust it on vibes.
4. **Few-shot calibration when compression is flagged.** The deck's own Pipeline 1 report shows alignment passing while scale compression fails ("judge clusters scores in the middle. Few-shot calibration required").
