# Report Section Mapping & Skill Integration

## Which Skill Output Feeds Which Report Section

| Report Section | Primary Skill | Supporting Skills | Input Mapping |
|---|---|---|---|
| **01 Executive Summary** | Strategy Partner | All skills | Extract: top 3 findings, recommendation, investment, timeline from all skills; synthesize into 1-page verdict |
| **02 Strategic Diagnosis** | Strategy Partner, Market Intelligence | All diagnostic skills | Market landscape, competitive forces, crux question, internal capabilities assessment |
| **03 The Crux Decision** | Rumelt Forge | Strategy Partner | Strategy kernel, guiding policy, coherent actions, why this matters |
| **04 Product/Solution** | Product Innovation | Technology, People | Product portfolio health, roadmap, features, MVP design |
| **05 Technology & Build** | Technology & Digital | Product, People | Architecture, build vs. buy, integration, timeline, team, dependencies |
| **06 Financial Model** | Financial Strategy | All skills (cost/benefit) | Revenue model, unit economics, investment, payback period, P&L sensitivity |
| **07 Go-to-Market** | GTM Strategy | Product, People, Market Intel | Launch strategy, customer acquisition, pricing, partnerships, competitive positioning |
| **08 Risk Assessment** | All skills (adversarial) | Execution Monitoring, Change Mgmt | Key assumptions, kill conditions, Devil's Advocate case, Bear Case, mitigation strategies |

## Fallback if Skill Missing

- Missing Strategy Partner: Synthesize from Market Intelligence + Rumelt Forge
- Missing Product Innovation: Use user feedback + market trends
- Missing Technology: Use current stack + industry benchmarks
- Missing Financial: Use comparable company metrics + build-up estimation
- Missing GTM: Use market intelligence + competitor GTM analysis
- Missing Risk: Use assumptions from other skills + historical failure patterns

## Conflict Resolution Integration

### How ATLAS Invokes CONFLICT-RESOLUTION.md

```
IF skill_A.recommendation != skill_B.recommendation ON (core_assumption OR financial_impact OR strategic_direction)
  AND disagreement_impact = MATERIAL
  THEN invoke CONFLICT-RESOLUTION.md
```

### Conflict Types & Resolution Paths

1. **Strategic Conflict** (e.g., "Pivot" vs. "Proceed")
   - Trigger: Rumelt Forge vs. Strategy Partner disagree on crux response
   - Resolution path: CONFLICT-RESOLUTION.md Step 1
   - Output: Either unified strategy recommendation OR "Executive Decision Pending" flag in Executive Summary

2. **Financial Conflict** (e.g., CAC assumptions)
   - Trigger: GTM Strategy assumes CAC $5K; Financial Strategy models $8K
   - Resolution path: CONFLICT-RESOLUTION.md Step 2 (validate data sources)
   - Output: Reconciled financial model with acknowledged assumption delta

3. **Execution Conflict** (e.g., Timeline feasibility)
   - Trigger: Product roadmap assumes 6-month delivery; Technology says 12 months
   - Resolution path: CONFLICT-RESOLUTION.md Step 3 (resource/dependency resolution)
   - Output: Agreed timeline with resource allocation plan

4. **Risk Assessment Conflict** (e.g., "High risk" vs. "Manageable")
   - Trigger: Execution Monitoring flags high execution risk; Hypothesis Testing says low confidence risk
   - Resolution path: CONFLICT-RESOLUTION.md Step 4 (validate evidence)
   - Output: Risk assessment with acknowledged disagreement or unified position

### Escalation Rules

- MATERIAL conflict (impacts decision) → Block report publication; resolve via CONFLICT-RESOLUTION.md
- MINOR conflict (doesn't impact decision) → Present both views in report; note disagreement in footer
- UNRESOLVABLE conflict → Escalate to human decision-maker; flag for executive judgment

### Report Presentation of Resolved Conflicts

```
CONFLICT RESOLUTION BOX (if conflicts existed):
───────────────────────────────────────
Skill A vs. Skill B Disagreement:
[Original positions]

Resolution Applied:
[How conflict was resolved per CONFLICT-RESOLUTION.md]

Impact:
[How this affects recommendations]
───────────────────────────────────────
```

## Input Format Expected

```
## Strategy Engagement Output

Company: {{NAME}}
Engagement: {{TITLE}}
Skills Used: [list]
Date: {{DATE}}

### Skill Outputs
[Each skill's structured output, including all data, analysis, recommendations, risks]
```

## Output Format

A single HTML file saved to the web/ directory, named `{{company}}-{{engagement}}-strategy.html`
