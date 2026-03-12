# Financial Strategy Skill — Complete Overview

## Purpose

A complete financial strategy system for CFOs, FP&A leaders, and financial strategists. This skill orchestrates end-to-end financial analysis, from diagnostic assessment through investor communication.

---

## Files & Structure

### Main Skill File

**`SKILL.md`** — The orchestrator and role definition
- Identity: CFO with 20+ years at Big 4, investment banks, PE/VC, Fortune 500, tech, turnarounds
- Core operating principles (6 core principles)
- Engagement flow: Phase 1 (Diagnosis) → Phase 2 (Decision Framing) → Phase 3 (Execution Plan)
- Quality gates, output format, integration with other skills
- Interaction style and decision discipline

### Reference Files (7 analytical frameworks + 1 expert system)

#### **`financial-diagnostics.md`** (420 lines)
Assess overall financial health across four dimensions.

**Contents:**
1. P&L waterfall and margin structure analysis
2. Cash conversion cycle and working capital health
3. Balance sheet strength and capital structure assessment
4. Financial benchmarking vs. industry peers
5. Early warning indicators (red flags and green flags)
6. Output template

**Use When:** "How healthy is this business? Where are the financial weaknesses?"

---

#### **`unit-economics.md`** (556 lines)
Understand profitability at the atomic level.

**Contents:**
1. Core unit economics framework (SaaS, Marketplace, DTC, Enterprise)
2. Contribution margin analysis and profitability tiers
3. Customer profitability distribution and cohort analysis
4. Marginal economics and scaling sensitivity
5. Unit economics by business model with specific checklists
6. Output template

**Use When:** "What are our unit economics? Which segments are profitable?"

---

#### **`financial-modeling.md`** (509 lines)
Build driver-based financial models with scenario analysis.

**Contents:**
1. 3-statement model architecture (Revenue drivers, COGS, OpEx, P&L, Balance Sheet, Cash Flow)
2. Scenario analysis (Base, Bull, Bear cases with scenario triggers)
3. Sensitivity analysis (which assumptions matter most?)
4. Monte Carlo simulation (probabilistic modeling)
5. Model quality checklist (11-point audit)
6. Output template

**Use When:** "What's our financial forecast? How sensitive are we to assumptions?"

---

#### **`cost-transformation.md`** (484 lines)
Systematically optimize cost structure for profit growth.

**Contents:**
1. Zero-based budgeting methodology (baseline, classification, optimal budget)
2. Operating leverage analysis (fixed vs. variable costs, leverage ratio, sensitivity)
3. Cost reduction roadmap (quick wins, medium-term optimization, long-term rebalancing)
4. Cost structure benchmarking vs. peers
5. Output template

**Use When:** "How do we improve profitability? What's our cost optimization path?"

---

#### **`business-case-builder.md`** (537 lines)
Build rigorous financial business cases for capital allocation.

**Contents:**
1. Business case framework (Initiative definition, investment, benefits, returns)
2. NPV and IRR calculation
3. Payback period and cash payback analysis
4. Risk-adjusted returns with scenario analysis
5. Sensitivity and break-even analysis
6. Stage-gate investment framework (Stage 1-4)
7. Common business case failures (red flags)
8. Business case template

**Use When:** "Should we invest in this? What's the ROI and payback period?"

---

#### **`investor-communication.md`** (407 lines)
Translate financial strategy into compelling narratives.

**Contents:**
1. Financial narrative architecture (3-act story: Situation, Inflection, Response)
2. Earnings story structure (for quarterly/interim reporting)
3. Financial KPI dashboard for boards and investors
4. Investor materials (presentation outline, fact book)
5. Objection scripts and response frameworks
6. Output template

**Use When:** "How do we communicate this strategy to board/investors?"

---

#### **`mixture-of-experts.md`** (426 lines)
Expert review panel for financial rigor.

**Contents:**
1. Five expert panel (CFO, FP&A Director, PE/VC Investor, Cost Consultant, Treasury/IR)
2. Each expert: background, lens, questions, scoring, hard stops
3. Review process (individual review, panel discussion, synthesis)
4. Hard stops vs. critical issues vs. conditional vs. nice-to-haves
5. Disagreement resolution framework
6. Output template

**Use When:** "Is this financial analysis rigorous? What are we missing?"

---

## How to Use This Skill

### Engagement Flow

1. **User brings a financial problem** (or you recognize one)
   - Example: "We need to understand our unit economics"
   - Example: "Should we invest $5M in this expansion?"
   - Example: "How do we improve margins?"

2. **Run Problem Intake & Scoping**
   - Assess what you've been given
   - Calibrate scope (Quick Diagnostic / Focused / Full Strategy)
   - Propose approach and wait for confirmation

3. **Select Frameworks & Execute Analysis**
   - Identify which 1-4 reference files you need
   - Run analyses in sequence (frameworks feed into each other)
   - Maintain shared context across analyses

4. **Run Quality Gates**
   - Apply critical gates to every output
   - Check confidence levels, sensitivity, reasonableness
   - Don't ship LOW-confidence analysis with HIGH-confidence language

5. **Expert Review**
   - Run mixture of experts panel for significant analyses
   - Resolve expert disagreements
   - Incorporate feedback

6. **Synthesize & Recommend**
   - If multiple frameworks have been run, synthesize into coherent strategy
   - Answer: What should we do? Why this? What has to go right? Sequence? KPIs? Risks?

7. **Communicate**
   - Package findings into narratives for different audiences
   - Prepare objection responses

---

## Framework Selection Guide

| Problem | Framework | Reference File |
|---------|-----------|-----------------|
| "How healthy is the business?" | Financial Health Diagnostic | financial-diagnostics.md |
| "What are our unit economics?" | Unit Economics & Profitability | unit-economics.md |
| "What's our forecast?" | Financial Modeling & Scenarios | financial-modeling.md |
| "How do we improve profitability?" | Cost Transformation | cost-transformation.md |
| "Should we invest in X?" | Business Case Builder | business-case-builder.md |
| "How do we communicate this?" | Investor Communication | investor-communication.md |
| "Is this analysis rigorous?" | Mixture of Experts | mixture-of-experts.md |

---

## Integration with Broader Strategy System

**With Strategy Partner:**
- Strategy Partner provides competitive/market context → Financial Strategy applies that to financial decisions
- Financial Strategy output (unit economics, margins, scenarios) → Strategy Partner uses to validate market opportunity and positioning
- Handoff: When financial analysis needs broader strategy context, request Strategy Partner analysis

**With Rumelt Strategy Forge:**
- Financial Strategy provides analytical intelligence (margins, costs, unit economics, scenarios)
- Rumelt Forge uses financial findings to forge strategy (Crux → Diagnosis → Guiding Policy → Actions)
- Handoff: When financial analysis is complete but strategy still needs to be decided, hand off to Rumelt Forge

---

## Key Principles

### 1. Numbers Over Narratives
Every claim gets specific numbers attached. "Improved margins" is unacceptable. "Expanded gross margin from 42% to 50% through supplier consolidation" is specific.

### 2. Assumption Transparency
Call out every assumption. Where do they differ from history? Which are most sensitive? What's the risk if wrong?

### 3. Cash Is King
- Operating profit = vanity
- Operating cash flow = survival metric
- Balance sheet strength = solvency

### 4. Scenario Discipline
Single forecast = fantasy. Always build Base/Bull/Bear cases and show what separates them.

### 5. Confidence Calibration
Every finding tagged [HIGH/MEDIUM/LOW]. Never present LOW-confidence claims with HIGH-confidence language.

### 6. "So What?" Cascade
Every finding → implication → action. If it doesn't change what the company does, cut it.

---

## Quality Standards

All outputs must meet these gates before presentation:

- **Gate 1: Numbers Are Complete** — Specific numbers, not vague claims
- **Gate 2: Assumptions Are Clear** — Explicit, documented, validated
- **Gate 3: Cash Flow Reality Check** — Not just P&L, also cash
- **Gate 4: Sensitivity & Scenarios** — Three cases shown, sensitivities tested
- **Gate 5: Confidence Audit** — Calibrated confidence levels
- **Gate 6: Red Team** — What would disprove this? Why hasn't it been done?

---

## For Practitioners

### If you're a CFO:
This system codifies your thinking. Use it to ensure rigor and consistency across your financial strategy work. The quality gates catch issues before they reach the board.

### If you're FP&A:
This system is your operational playbook. The financial modeling and business case builder sections are immediately applicable to your monthly/quarterly work.

### If you're an investor:
This system shows you what good financial strategy looks like. Use the mixture of experts panel to pressure-test any financial analysis presented to you.

### If you're a strategic advisor:
This system deepens your financial rigor. The business case builder, cost transformation, and investor communication sections will strengthen your strategy recommendations.

---

## Version & Maintenance

**Version:** 1.0 (Complete)
**Last Updated:** March 2026
**Status:** Production-ready, no placeholders

All files are complete, detailed, and immediately usable. This is not a template system requiring customization — it's a fully developed methodology ready for application.
