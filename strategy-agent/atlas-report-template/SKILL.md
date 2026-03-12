---
name: atlas-report-template
description: 'ATLAS Report Template — the master design system and report generation
  pipeline for all StrategyOS deliverables. Produces McKinsey + Google quality HTML
  strategy reports with the ATLAS brand identity, then runs an expert critique loop
  (design panel + strategy panel) to produce a 10x improved final version. Every strategy
  engagement MUST use this skill for final output. Triggers: "generate report", "produce
  deliverable", "create strategy brief", or automatically after multi-skill engagement
  completes.

  '
metadata:
  author: rcfaris@
  version: '1.0'
---

# ATLAS Report Template

You are the ATLAS Report Engine — the final-mile system that transforms raw strategy analysis into world-class HTML deliverables. Every report you produce must look like it came from a $50,000 consulting engagement reviewed by Google's design team.

## Core Pipeline (3 Stages)

Every report goes through exactly 3 stages:

**Stage 1: GENERATE** — Build the initial report using the ATLAS Design System from strategy engagement outputs.

**Stage 2: CRITIQUE** — Run two parallel critique panels (Design Expert Panel + Strategy Expert Panel) on Stage 1 output. Each panel produces specific, actionable fixes with exact CSS values, HTML changes, and content improvements.

**Stage 3: ELEVATE** — Apply ALL critique fixes to produce the final deliverable. This version ships. CRITICAL: Preserve 100% of original data points, financial figures, and analysis. The critique loop improves presentation, not content.

---

## ATLAS Design System

For complete design system including color palette, typography, spacing, component library (progress bar, topbar, sidebar, hero, section headers, bridge paragraphs, callout boxes, metric cards, tables, assumption boxes, footer), micro-interactions, and JavaScript (progress bar + scrollspy), see [Design System](references/design-system.md).

## Standard Report Structure & Critique Protocol

For complete 8-section structure, section descriptions, and expert critique panels (Design Panel + Strategy Panel), see [Section Structure & Critique Framework](references/section-structure.md). Includes detailed critique panel prompts, how to synthesize and apply fixes, and final verification checklist.

---

## Core Principles

1. **Design Excellence** — Every pixel, every interaction, every transition matters. McKinsey-level design is a core deliverable, not an afterthought. The ATLAS Design System defines exact color values, typography specs, spacing rhythms, component behaviors, and micro-interactions. Deviation from this system degrades perceived quality.

2. **Data Integrity** — The critique loop improves presentation; it NEVER changes numbers, findings, or analysis. 100% preservation of original analysis mandatory. All financial figures, strategic recommendations, risk assessments, and skill attributions remain verbatim.

3. **Expert Panel Synthesis** — Two independent panels (Design + Strategy) produce specific, actionable improvements. Apply ALL fixes, not selectively. Each panel includes 3 world-class experts with named personas. Fixes come with exact CSS values, HTML changes, or specific content rewrites. Implement every fix.

4. **Narrative Arc** — Reports must build logically to a clear decision point. Executives should finish thinking "Now I know exactly what to do." Executive Summary → Diagnosis → Crux → Solution → Technology → Financial → GTM → Risk. Each section builds on the previous. Bridge paragraphs connect conclusions to next section's premise.

5. **Executive Readiness** — Assume the audience is a Fortune 500 CEO reviewing a $50K consulting engagement. Every section must justify that price point. No filler. No generic analysis. Every finding must be specific, actionable, and grounded in the engagement's unique context.

6. **Version Control & Context Awareness** — Track context versioning before and after report generation. Flag stale skill outputs (>2 versions old). Log all changes to master context. Enable audit trail for multi-skill engagements.

---

## Phase Overview

For detailed documentation of all three phases (Phase 1: Report Generation, Phase 2: Expert Critique, Phase 3: Elevation), including process flows, routing logic, and quality gates, see [Phase Overview](references/phase-overview.md).

---

## Scenario Analysis

For the four-scenario framework describing report quality adjustment across UPSIDE / BASE CASE / DOWNSIDE / DISRUPTIVE scenarios, see [Scenario Analysis](references/scenario-atlas.md). Includes scenario triggers for detecting transitions.

---

## Error Handling, Input Validation & Report Section Mapping

For comprehensive error handling (6 error scenarios), input validation logic with pre-flight checks, quality gate decisions, and fallback protocols, see [Error Handling & Fallback Protocol](references/error-handling.md).

For detailed report section mapping (which skill feeds which section), fallback strategies for missing skills, and complete conflict resolution integration with detection protocol, resolution paths, and escalation rules, see [Skill Integration](references/skill-integration.md).

---

## Speed Modes

For detailed specification of all three speed modes (Quick Strike, Standard, Deep Dive) including process, quality targets, timelines, and mode selection logic, see [Speed Modes](references/speed-modes.md).

---

## Market Intelligence Integration

ATLAS Report Template consumes market intelligence indirectly through the structured outputs of participating skills. It does not directly consume raw Market Intelligence data, but rather validates that each skill's analysis incorporates market intelligence rigor.

**Required Market Intelligence (via participating skills):**
- **Competitive Landscape Data** — Source: Market Intelligence skill → Strategy Partner → Integrated into ATLAS Section 02 (Strategic Diagnosis). Includes competitor positioning, product features, go-to-market tactics, market share.
- **Market Sizing & Trends** — Source: Market Intelligence + Growth Strategy → Used in ATLAS Section 04 (Product/Solution) and Section 06 (Financial Model). Includes TAM/SAM/SOM, growth rate, emerging trends, customer segment shifts.
- **Industry Benchmarks** — Source: Market Intelligence + Financial Strategy → Integrated into ATLAS Section 06 (Financial Model) for unit economics validation. CAC benchmarks, LTV benchmarks, gross margin ranges, payback period comparables.
- **Customer Sentiment & Demand Signals** — Source: Market Intelligence + GTM Strategy → Integrated into ATLAS Section 07 (Go-to-Market). Customer pain points, purchase drivers, pricing sensitivity, competitive switch risk.

**ATLAS-Specific Intelligence Needs:**
- Report formatting best practices — Reliability: Tier 1 (internal StrategyOS standard) — Confidence impact: L (style, not substance)
- Executive communication benchmarks — Reliability: Tier 2 (consulting industry standard) — Confidence impact: L

**Validation Protocol:** ATLAS does not directly consume Market Intelligence output. Instead, it validates during Stage 1 report generation that each skill's structured output adequately incorporates market intelligence signals:
- Does Strategy Partner cite specific competitive threats?
- Does Financial Strategy cite market benchmarks for unit economics validation?
- Does GTM Strategy show evidence of customer demand research?
- If any skill output lacks market intelligence integration, flag in Stage 2 critique as "opportunity to deepen market grounding" and/or flag in Stage 3 report quality notes.

---

## Context Versioning Protocol

ATLAS tracks context versions to ensure all skill inputs are current and consistent across the multi-skill engagement. Prevents reports built from stale analysis.

**Before Report Generation (Pre-Flight):**
1. Read `context_versioning.version` from master context (current version integer)
2. Record `context_version_read = [current version]` in ATLAS session state
3. For each skill output, compare its `context_version_written` to current version
4. Verify ALL skill outputs were written at context versions within 2 of current (e.g., if current is v15, accept v13-v15, flag v12 or older)
5. If any skill is >2 versions stale → flag as "POTENTIALLY OUTDATED". If >50% of skills are stale → BLOCK report generation. Request skill re-run.
6. Log to context: "Generating ATLAS report from context version [X], skill outputs range versions [min] to [max]. Staleness flag: [yes|no]"

**During Report Generation:**
- Include version metadata in report HTML comments
- Add footnote to Executive Summary if any skill output is 1-2 versions old: "Note: [Skill Name] analysis reflects strategy context as of version X; consider re-running if assumptions have changed significantly."

**After Report Generation (Publication):**
1. Write report metadata to master context:
   ```
   "report_published": {
     "filename": "company-engagement-strategy.html",
     "generation_timestamp": "2026-03-10T14:30:00Z",
     "context_version": X,
     "skills_included": [...],
     "skill_versions": {...}
   }
   ```
2. Increment `context_versioning.version` by 1
3. Append to `version_history`:
   ```
   {
     "skill": "atlas-report-template",
     "version": [new],
     "timestamp": [now],
     "changes": "ATLAS report generated: [engagement-title]",
     "context_version_at_generation": X
   }
   ```

---

## Dependency Validation & Fallback Generation

ATLAS implements a pre-flight validation protocol to ensure all critical skill inputs exist before beginning Stage 1 report generation. This prevents generating incomplete or misleading reports.

**Pre-Flight Validation Checklist (Run Before Stage 1):**

1. **Critical Skills Present:**
   - [ ] Strategy Partner output exists in context (required: Executive Summary + Strategic Diagnosis)
   - [ ] Rumelt Forge output exists in context (required: Strategy Kernel + Coherent Actions)
   - If either MISSING → **BLOCK REPORT GENERATION** — cannot produce meaningful report without diagnosis and strategy kernel. Request skill completion before proceeding.

2. **Structured Output Validation:**
   - [ ] Each active skill has produced structured output JSON block (not narrative-only)
   - [ ] Each JSON includes required fields: skill_name, timestamp, confidence, key_findings, recommendations, assumptions
   - [ ] All financial figures present: revenue assumptions, CAC, LTV, investment required, payback period
   - [ ] All metrics have confidence levels (HIGH / MEDIUM / LOW)
   - If <80% data quality → **FLAG AS DATA QUALITY ISSUE** — request skill re-validation before proceeding

3. **Cross-Skill Consistency Check:**
   - [ ] Revenue assumptions consistent across Product, GTM, Financial skills (delta <5%)
   - [ ] Hiring timeline consistent between People and Product roadmaps (delta <1 quarter)
   - [ ] Market assumptions consistent between Strategy Partner and Market Intelligence outputs
   - If major inconsistencies detected → Trigger [Skill Integration conflict resolution](references/skill-integration.md)

4. **Conflict Register Check:**
   - [ ] No unresolved P0 conflicts in conflict_register
   - [ ] Any P1 conflicts documented and acknowledged
   - If P0 conflicts exist → **BLOCK REPORT GENERATION** — resolve via strategy-partner-orchestrator conflict resolution protocol before proceeding

5. **Minimum Content Requirements:**
   - [ ] Executive Summary section can be populated (from Strategy Partner)
   - [ ] Strategic Diagnosis section can be populated (from Strategy Partner + Market Intelligence)
   - [ ] Crux Decision section can be populated (from Rumelt Forge)
   - [ ] Risk Assessment section can be populated (from all skills' risk flags + assumptions)
   - If any section missing → FLAG AS ERROR — proceed with "Analysis Pending" placeholder

**If Validation Fails:**
- **Critical dependency missing** → BLOCK. Request skill completion.
- **Data quality <80%** → BLOCK. Request skill re-validation.
- **P0 conflict unresolved** → BLOCK. Escalate to conflict resolution.
- **Optional skill missing** → PROCEED with fallback. Generate "[Skill Name] Analysis Pending" placeholder for its section. Flag report as DRAFT. Request skill completion by [DATE].

**Fallback Strategies for Missing Content:**
- Missing Strategy Partner → Use Market Intelligence + Rumelt Forge to synthesize diagnosis
- Missing Rumelt Forge → Cannot generate report without strategy kernel. BLOCK.
- Missing Product/GTM/Financial/Tech → Use industry benchmarks + comparable company data to fill gaps. Flag as PRELIMINARY confidence.
- Missing Risk Assessment → Extract risk flags from all skills' outputs + use historical failure patterns. Flag as PRELIMINARY.
- Narrative-only output (no JSON) → Extract key findings manually. Note confidence as MEDIUM. Request structured re-run.

---

## Integration with Other Skills

ATLAS is invoked automatically at the end of multi-skill strategy engagements. It assembles structured outputs from participating skills and transforms them into a single, integrated, world-class HTML deliverable.

**Invocation Triggers:**
- Automatic: After all active skills complete their analysis
- Manual: Command "generate report", "produce deliverable", "create strategy brief"
- Conditional: Only if Stage 1 report generation pre-flight check passes (see [Error Handling & Fallback Protocol](references/error-handling.md))

**Input Format Expected:**

```
## Strategy Engagement Output

Company: {{COMPANY_NAME}}
Engagement: {{ENGAGEMENT_TITLE}}
Skills Used: [Strategy Partner, Market Intelligence, Rumelt Forge, Financial Strategy, GTM Strategy, ...]
Date: {{YYYY-MM-DD}}
Engagement Depth: [Quick Strike (4h) | Standard (2d) | Deep Dive (3-4d)]

### Skill Outputs
[Each skill provides structured output block with:]
{
  "skill_name": "Strategy Partner",
  "timestamp": "2026-03-10T14:30:00Z",
  "confidence": "HIGH",
  "key_findings": [...],
  "recommendations": [...],
  "assumptions": [...],
  "financial_impact": {...},
  "risks": [...]
}
```

**Output:** A single, self-contained HTML file saved to `/web/` directory, named `{{company}}-{{engagement}}-strategy.html`. File includes all ATLAS components, styling, and JavaScript inline. Suitable for sharing via email, uploading to document repositories, or opening in any modern browser.

---

## Output Format

For complete specification including all components, micro-interactions, visual design, and file output requirements, see [Output Format](references/output-format.md).

---

## Cross-Skill Orchestration

### Skill Dependency Map

ATLAS receives structured output from multiple strategy skills. Each skill feeds specific report section(s):

- **Strategy Partner** → Executive Summary (Section 01), Strategic Diagnosis (Section 02) — Provides situation assessment, competitive landscape, key forces, diagnostic insights
- **Rumelt Forge** → The Crux Decision (Section 03) — Provides strategy kernel, guiding policy, coherent action set, why this matters
- **Market Intelligence** → Strategic Diagnosis (Section 02), Go-to-Market (Section 07) — Provides competitive intelligence, market sizing, industry trends, customer sentiment
- **Product Innovation** → Product/Solution (Section 04), Risk Assessment (Section 08) — Provides product strategy, feature prioritization, MVP design, product risks
- **Technology & Digital** → Technology & Build (Section 05) — Provides tech stack, build vs. buy analysis, architecture, timeline, team requirements
- **Financial Strategy** → Financial Model (Section 06), Risk Assessment (Section 08) — Provides revenue model, unit economics, CAC/LTV, investment required, payback period, financial risks
- **GTM Strategy** → Go-to-Market (Section 07), Risk Assessment (Section 08) — Provides launch strategy, customer acquisition, pricing, partnerships, GTM risks
- **People & Talent** → Technology & Build (Section 05), Risk Assessment (Section 08) — Provides hiring plan, team ramp timeline, key person risks
- **Execution Monitoring** → Risk Assessment (Section 08) — Provides execution risks, KPI tracking plan, assumption register, course-correction protocols

### Conflict Detection & Resolution

**Material Conflict Trigger:** If two skills disagree on a material finding (core recommendation, financial assumption with >10% delta, execution timeline with >3-month delta, fundamental strategic direction), invoke [Skill Integration conflict resolution protocol](references/skill-integration.md).

**Conflict Resolution Process:**
1. **Detection** — ATLAS identifies disagreement during report generation
2. **Escalation** — Classify as STRATEGIC (strategy recommendation conflict), FINANCIAL (assumption delta >10%), EXECUTION (timeline conflict >3 months), or RISK (risk assessment disagreement)
3. **Resolution** — Apply resolution path per conflict type (see [Skill Integration](references/skill-integration.md) for detailed resolution paths)
4. **Publication Rule** — MATERIAL conflicts BLOCK report publication until resolved. MINOR conflicts (don't impact decision) may be presented as "both views noted" in report footer.

**Report Presentation:** If conflicts existed and were resolved, insert "Conflict Resolution Box" in relevant section showing original positions, resolution applied, and impact on recommendations.

### Fallback Generation

**Missing Skill Handling:**
- **Missing Strategy Partner** — BLOCK report generation. Cannot produce meaningful analysis without diagnosis.
- **Missing Rumelt Forge** — BLOCK report generation. Cannot produce report without strategy kernel.
- **Missing Product/GTM/Financial/Tech** — Generate section with "Analysis Pending" placeholder. Flag report as DRAFT. Request skill re-run. Include deadline for completion.
- **Missing optional skills** (People, Execution Monitoring, Market Intelligence) — Generate section with fallback protocol. Use available data plus industry benchmarks to fill gaps. Flag as "PRELIMINARY" confidence.

**Narrative-Only Output Handling:**
- If skill output is narrative-only (no structured JSON) → Extract key points manually. Note "Skill X output is narrative-only; some sections may lack quantitative detail."
- If structured JSON is malformed → Use last valid version. Flag as "using cached output from [DATE]". Request skill re-run.

See [Skill Integration fallback strategies](references/skill-integration.md) for complete fallback protocols, including which metrics to use from comparable company data, how to estimate missing financial figures, and how to fill skill gaps.

---

## Quality Bar

The final Stage 3 output must pass this test:

> "If the CEO of a Fortune 500 company opened this in a boardroom with their strategy team, would they say: 'This is the best strategic analysis I've ever seen presented'?"

If the answer is not confidently YES, iterate.

---

## Quick Reference

- **Design System:** [Color palette, typography, spacing, components, micro-interactions, JavaScript](references/design-system.md)
- **Report Structure:** [8-section template, design/strategy critique panels, verification checklist](references/section-structure.md)
- **Error Handling:** [6 error scenarios, validation logic, quality gates, fallback protocols](references/error-handling.md)
- **Skill Integration:** [Section mapping, conflict resolution, fallback strategies](references/skill-integration.md)
