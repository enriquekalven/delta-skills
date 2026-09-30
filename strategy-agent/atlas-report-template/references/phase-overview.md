# ATLAS Report Generation Phases

## Phase 1: Report Generation

**Objective:** Build initial HTML report from skill outputs using ATLAS Design System. Map each skill output to its designated report section. Create all HTML structure, styles, and JavaScript interactivity.

**Process:**
1. **Input Validation** — Verify all skill outputs exist. Check for structured JSON blocks. If missing or malformed, use narrative output. Log all warnings and errors.
2. **Section Population** — Map each skill to its primary report section (see [Skill Integration](skill-integration.md) for mapping table). Extract findings, recommendations, assumptions, risks, financial data from skill outputs.
3. **HTML Build** — Create semantic HTML structure with all 8 sections. Apply ATLAS Design System styling (colors, typography, spacing) inline. Embed all JavaScript for progress bar and scrollspy.
4. **Component Rendering** — Render hero section, section headers, bridge paragraphs, callout boxes, metric cards, data tables, assumption boxes. Preserve 100% of original data. Add skill attribution labels.
5. **Quality Check** — Verify all financial figures intact. Check for missing sections. Verify no data loss. Run basic HTML validation.

**Routing Logic:**
- If skill output is structured JSON → Extract key_findings, recommendations, assumptions
- If skill output is narrative-only → Flag confidence as MEDIUM. Extract key points manually.
- If skill output is missing → Flag section as "PRELIMINARY" placeholder. Note in report footer. Request skill re-run.
- If data conflicts detected between skills → Flag in report. Reference conflict resolution (see [Skill Integration](skill-integration.md)).

**Output:** Single HTML file with complete 8-section structure, all ATLAS components, full data preservation, interactive elements functional.

---

## Phase 2: Expert Critique

**Objective:** Run two parallel expert panels scoring the Stage 1 report and producing specific, actionable improvements. Each panel generates 10-20 high-impact fixes with exact implementation guidance.

**Process:**
1. **Design Panel** — 3 world-class designers (Julie Zhuo, Mike Monteiro, Jony Ive) critique typography hierarchy, color sophistication, whitespace rhythm, sidebar quality, data visualization, hero/topbar premium feel, micro-interactions, overall boardroom impact. Rate 1-10. For each issue: identify the problem, state design principle violated, provide exact CSS fix (with values), propose HTML changes if needed. (See [Section Structure & Critique Framework](section-structure.md) for complete panel prompt and critique methodology.)

2. **Strategy Panel** — 3 elite consultants (McKinsey Senior Partner, BCG Managing Director, Bain Partner) critique narrative arc (does it build to a clear decision?), executive summary strength, insight depth, competitive differentiation, assumption visibility, decision governance, actionability of recommendations, financial model credibility, risk assessment rigor. Rate 1-10. For each weakness: identify what's missing, describe what a $50K engagement would include, provide specific content/structure fix. (See [Section Structure & Critique Framework](section-structure.md) for complete panel prompt.)

3. **Fix Synthesis** — Collect all fixes from both panels. Synthesize into unified improvement list. Remove duplicates. Categorize as BLOCKER (fixes critical design/strategy flaw), PRIORITY (significant impact), NICE-TO-HAVE (polish).

4. **Prioritization** — Rank by impact. Apply all BLOCKERS. Apply all PRIORITY fixes. Apply NICE-TO-HAVE if timeline permits.

**Routing Logic:**
- Design panel rating <6: Flag as BLOCKER. Extend Stage 3 timeline.
- Strategy panel rating <6: Flag as BLOCKER. Likely delay publication.
- Combined fixes >25: Consider 2-round critique (meta-critique on Stage 3 output). Adds 1 day to timeline.
- Fixes <10: Proceed to Stage 3 quickly.

**Output:** Unified fix list with implementation guidance, prioritization labels, CSS values, HTML changes, content rewrites, timeline impact assessment.

---

## Phase 3: Elevation

**Objective:** Apply ALL critique fixes while preserving 100% of original data points. Produce final, boardroom-ready HTML report. This version ships.

**Process:**
1. **Fix Application** — For each fix: implement exact CSS value provided. Implement exact HTML change. Preserve all data points verbatim.
2. **Data Verification** — Re-verify all financial figures match original skill outputs. Check revenue, CAC, LTV, gross margin, NPV, payback period against original analysis. Reconcile any discrepancies. Update skill attributions. Preserve risk assessments and assumptions.
3. **Component Testing** — Verify progress bar updates on scroll. Test scrollspy highlights correct section. Check all micro-interactions (hover states, table rows, buttons). Verify responsive design across viewport sizes.
4. **Quality Gate** — Run final quality gate checklist (see [Section Structure & Critique Framework](section-structure.md) verification checklist). All 10 items must pass. If any item fails, fix before shipping.
5. **Final Review** — Read through as if you're the Fortune 500 CEO. Would you say "This is the best strategic analysis I've ever seen presented"? If not confidently YES, iterate.

**Routing Logic:**
- Quality gate passes → SHIP. Mark report as final. Log to context versioning.
- Quality gate has 1-2 failures → Fix and re-gate. Usually completes same day.
- Quality gate has 3+ failures → Flag for human review. May require significant rework.

**Output:** Final, polished HTML report. Single file. All sections complete. All data preserved. All critiques applied. All components functional. Boardroom-ready quality.
