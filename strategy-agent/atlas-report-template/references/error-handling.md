# Error Handling & Fallback Protocol

## Error Scenarios & Resolution Paths

### Error 1: Skill Output Missing or Malformed

- **Detection:** Skill JSON unparseable or missing required fields
- **Fallback:** Use last-available version of skill output; note version and age
- **Escalation:** Flag in report footer; request skill re-run; delay publication if data >2 weeks old
- **Resolution:** Trigger skill re-execution; reconcile and re-generate report

### Error 2: Conflicting Recommendations Between Skills

- **Detection:** Skill A recommends "PIVOT strategy" while Skill B recommends "PROCEED as planned"
- **Fallback:** Present BOTH recommendations in report; highlight conflict; reference CONFLICT-RESOLUTION.md
- **Escalation:** Flag as "REQUIRES EXECUTIVE DECISION"; include conflict summary in Executive Summary
- **Resolution:** Invoke CONFLICT-RESOLUTION.md protocol; coordinate skill re-analysis with shared context

### Error 3: Data Mismatch (e.g., revenue assumptions inconsistent)

- **Detection:** Financial Strategy says $50M ARR, GTM Strategy assumes $60M
- **Fallback:** Use conservative estimate ($50M); flag as "RECONCILIATION NEEDED"; note both figures
- **Escalation:** Include data reconciliation table in report; request Finance/GTM skill re-alignment
- **Resolution:** Skills re-run analysis with shared assumptions; re-generate report section

### Error 4: Missing Critical Section (e.g., Risk Assessment)

- **Detection:** Risk Assessment skill did not produce output
- **Fallback:** Generate risk assessment from other skills' "risk_flags" section
- **Escalation:** Flag as "PRELIMINARY RISK ASSESSMENT"; mark confidence as MEDIUM; request skill completion
- **Resolution:** If critical for decision, delay publication; if non-critical, proceed with caveat

### Error 5: Stage 2 Critique Reveals Major Design Flaw

- **Detection:** Design panel finds typography/hierarchy fundamentally broken; OR Strategy panel finds narrative arc missing
- **Fallback:** Fix critical issues (BLOCKER); defer non-critical fixes (NICE-TO-HAVE)
- **Escalation:** Extend Stage 3 timeline; communicate delay to stakeholders
- **Resolution:** Implement all blockers; assess nice-to-have prioritization; re-publish

### Error 6: Report HTML Generation Fails (CSS/JavaScript issue)

- **Detection:** Report renders broken in browser
- **Fallback:** Use text-only version; strip CSS; provide raw data export
- **Escalation:** Flag as "TECHNICAL ISSUE"; provide alternative format (PDF, Word)
- **Resolution:** Debug HTML; fix CSS/JS errors; re-generate report

## Input Validation Logic

### Pre-Flight Check Before Report Generation

**Validation Protocol:**

1. **Skill Output Completeness Check:**
   - [ ] All active skills have provided structured output JSON block
   - [ ] Each skill output includes: skill_name, timestamp, confidence, key_findings, recommendations, assumptions
   - [ ] If any skill missing: BLOCK report generation; request skill re-run with structured output

2. **Data Quality Validation:**
   - [ ] All financial figures present and internally consistent (revenue, CAC, LTV, gross margin)
   - [ ] All metrics have confidence levels assigned (H/M/L)
   - [ ] All recommendations have owners and timelines
   - [ ] If data quality <80%: BLOCK report; request data reconciliation from skills

3. **Cross-Skill Consistency Check:**
   - [ ] Revenue assumptions consistent across Product, GTM, Financial skills
   - [ ] Hiring timelines consistent between People and Product roadmaps
   - [ ] Market assumptions consistent between Strategy Partner and Market Intelligence
   - [ ] If major inconsistencies detected: BLOCK report; trigger CONFLICT-RESOLUTION.md

4. **Minimum Content Requirements:**
   - [ ] Executive Summary exists (from Strategy Partner)
   - [ ] Strategic Diagnosis exists (from Strategy Partner)
   - [ ] Crux Decision exists (from Rumelt Forge)
   - [ ] Risk Assessment exists (from all skills)
   - [ ] If any section missing: FLAG as error; attempt fallback generation

**Fallback Protocol (If Validation Fails):**
- Missing skill output → Use "PRELIMINARY" placeholder; mark confidence as LOW; request skill completion
- Data quality issues → Use most recent available data; flag as "ESTIMATED"; request skill re-validation
- Inconsistency detected → Present both versions in report; flag disagreement; reference CONFLICT-RESOLUTION.md
- Missing section → Recommend delaying publication until section complete OR generate placeholder with "TO BE COMPLETED BY [SKILL]" note

**Quality Gate Decision:**
- IF validation passes with 0 blockers → PROCEED to Stage 1 report generation
- IF validation passes with <3 warnings → PROCEED to Stage 1 with flags noted in footer
- IF validation fails on critical data OR >3 warnings → BLOCK; request skill fixes before proceeding
