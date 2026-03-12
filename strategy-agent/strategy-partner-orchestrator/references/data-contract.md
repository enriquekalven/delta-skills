# StrategyOS Data Contract Specification

**Purpose:** Define the universal, machine-readable output format that every skill MUST produce. This enables conflict detection, dependency validation, context flow, and the ATLAS reporting pipeline.

**Version:** 1.0 | **Status:** ACTIVE | **Updated:** 2026-03-10

---

## 1. Universal Skill Output Schema

Every strategy skill produces two sequential outputs:

1. **Part 1:** Full narrative analysis (unchanged from current format)
2. **Part 2:** `STRUCTURED OUTPUT` block containing machine-readable JSON

### Output Assembly Pattern

```
[NARRATIVE ANALYSIS - Full skill output as currently generated]

---

## Structured Output (ATLAS Pipeline)

```json
{
  [SCHEMA BELOW]
}
```
```

### Complete JSON Schema Definition

```json
{
  "skill_metadata": {
    "skill_name": "string",
    "skill_version": "string",
    "execution_timestamp": "ISO 8601",
    "engagement_id": "string",
    "engagement_name": "string",
    "execution_speed_mode": "STANDARD | QUICK_STRIKE"
  },

  "analysis_quality": {
    "confidence": {
      "overall": "H | M | L",
      "basis": "string (1-2 sentences explaining confidence level)"
    },
    "speed_mode": "STANDARD | QUICK_STRIKE",
    "estimated_quality": "FULL | ESTIMATED | LOW_CONFIDENCE",
    "iteration_count": "integer"
  },

  "key_findings": [
    {
      "finding": "string (core insight)",
      "evidence": "string (data/sources supporting this)",
      "confidence": "H | M | L",
      "quantified_metric": "string (if applicable, e.g., '$45M ARR shortfall')",
      "implication": "string (what this means for strategy)"
    }
  ],

  "recommendations": [
    {
      "action": "string (specific, actionable recommendation)",
      "rationale": "string (why this action)",
      "expected_outcome": "string (what improves if we do this)",
      "timeline": "string (when should this happen)",
      "owner": "string (who executes)",
      "confidence": "H | M | L",
      "confidence_basis": "string (why we believe this will work)",
      "success_metric": "string (how we measure success)"
    }
  ],

  "risk_flags": [
    {
      "risk": "string (what could go wrong)",
      "probability": "H | M | L",
      "impact": "H | M | L",
      "mitigation": "string (how to reduce/prevent)",
      "trigger": "string (what warning sign indicates this risk is materializing)"
    }
  ],

  "kill_conditions": [
    {
      "condition": "string (what would invalidate this entire analysis)",
      "threshold": "string (specific measurement or event)",
      "action_if_triggered": "string (what we should do if this happens)",
      "monitoring_frequency": "string (how often to check)"
    }
  ],

  "assumptions": [
    {
      "assumption": "string (what we're assuming to be true)",
      "impact_if_wrong": "MATERIAL | MODERATE | LOW",
      "validation_method": "string (how to test this assumption)",
      "validation_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
      "validation_timeline": "string (when should we validate)"
    }
  ],

  "data_points": [
    {
      "metric": "string (name of metric)",
      "value": "string or number",
      "unit": "string ($, %, years, etc.)",
      "source": "string (where this data came from)",
      "confidence": "H | M | L",
      "date_of_measurement": "ISO 8601 (when was this measured)",
      "basis": "string (assumptions embedded in this data point)"
    }
  ],

  "dependencies": {
    "dependencies_consumed": [
      "string (which upstream skills' outputs did we use?)",
      "EXAMPLES: rumelt-forge, product-innovation, financial-strategy"
    ],
    "dependencies_produced": [
      "string (which downstream skills should consume our output?)",
      "EXAMPLES: gtm-strategy, operating-model, people-talent"
    ],
    "missing_dependencies": [
      {
        "skill": "string",
        "reason": "string (why we needed this but didn't get it)",
        "impact_on_analysis": "string (what's less confident because of this)"
      }
    ]
  },

  "conflicts_detected": [
    {
      "conflicting_skill": "string",
      "this_position": "string (our recommendation/finding)",
      "their_position": "string (what the other skill recommends/found)",
      "resolution_needed": "boolean",
      "conflict_type": "STRATEGIC | OPERATIONAL | DATA | TIMING",
      "my_confidence_in_my_position": "H | M | L",
      "their_confidence_in_theirs": "H | M | L (if available)",
      "attempted_resolution": "string (have we tried to resolve this?)"
    }
  ],

  "context_written": {
    "context_keys_updated": [
      "string (what keys in master context object did we update?)",
      "EXAMPLES: diagnosis_state.key_findings, strategy_state.kernel, financial_state.margins"
    ],
    "context_version": "integer (what version of master context did we read?)"
  }
}
```

---

## 2. Dual Output Mode Specification

### Part 1: Narrative Analysis (Unchanged)

Continue producing the full narrative output as currently designed. No changes to how skills write their analysis, recommendations, risk assessment, or executive summary.

### Part 2: Structured Output Block (New)

Immediately after the narrative closes, add:

```
---

## Structured Output (ATLAS Pipeline)

```json
[Full schema above, populated with data from the analysis]
```

### Why Dual Mode?

- **Humans read Part 1:** Narrative, explanation, reasoning, nuance
- **Machines read Part 2:** Structured data for conflict detection, dependency validation, context flow, report generation
- **Zero redundancy required:** Part 2 extracts from Part 1, doesn't duplicate full content

---

## 3. Data Point Standards & Formatting Rules

Every metric in your analysis must conform to these standards for the data pipeline to work:

### Financial Figures

**Format requirement:**
```
{value} {currency} {period}, {basis}
```

**Examples:**
- ✅ "$828M ARR Year 3, Base Case"
- ✅ "$45.2M annual CAC, current customer mix, no volume discounts"
- ✅ "€15M upfront capex, amortized over 5 years"
- ✅ "$2.3M net margin at 40% revenue scale"

**Why this matters:** Report templates need to know whether we're talking about Year 1 or Year 5, Base Case or Bear Case, and what assumptions are baked in.

### Percentages

**Format requirement:**
```
{value}% ({numerator}/{denominator}), {context}
```

**Examples:**
- ✅ "42% gross margin (revenue minus COGS / revenue), mature product line"
- ✅ "8.5% market share (our revenue / TAM), growing segment"
- ✅ "73% customer satisfaction NPS, surveyed Q4 2025, N=150"
- ✅ "15% YoY growth (2026 vs 2025 revenue), organic only"

**Why this matters:** Without numerator/denominator context, percentages are meaningless. "15% improvement" could mean 15 out of 100 or 1,500 out of 10,000.

### Confidence Tags

**Format requirement:**
```
{confidence_level} confidence: {1-sentence basis}
```

**Examples:**
- ✅ "H confidence: Validated through 15 customer interviews and 3 years of market data"
- ✅ "M confidence: Based on company's stated strategy, but execution track record is mixed"
- ✅ "L confidence: Market is moving fast; our assumptions about competitor positioning may be outdated"

**Why this matters:** Confidence without basis is useless. The basis shows why we believe it or why we're uncertain.

### Time-Based Metrics

**Format requirement:**
```
{value} {unit} ({baseline → target | current state}), {timeline}
```

**Examples:**
- ✅ "12 months ($0M → $15M ARR), Year 1 plan"
- ✅ "8 months (200 employees → 350 employees), Q3-Q4 2026 hiring"
- ✅ "Q2 2026 (launch first product), based on engineering roadmap"

**Why this matters:** Strategy happens over time. "12 months" is useless without knowing what we're measuring and when.

### Market/Competitive Metrics

**Format requirement:**
```
{metric} = {value}, {source}, {dated}
```

**Examples:**
- ✅ "TAM for SaaS observability = $45B, IDC 2025 report, published Jan 2025"
- ✅ "Competitor's NPS = 52, Trustpilot, as of Feb 2026"
- ✅ "Market growth rate = 28% CAGR, Gartner Magic Quadrant 2024"

**Why this matters:** Market claims are only as good as their source and date.

---

## 4. Version Control & Backward Compatibility

### Schema Versioning

**Current Version:** 1.0

**Versioning Rules:**

| Change Type | Version Bump | Migration Path |
|---|---|---|
| New required field | Major (2.0) | Skills must update; cannot read 1.x |
| New optional field | Minor (1.1) | Skills can ignore; backward compatible |
| Field removal | Major (2.0) | Deprecated for 1 version, then removed |
| Field rename | Major (2.0) | Must provide translation table |
| Type change (string → number) | Major (2.0) | Must provide conversion logic |

### Declaring Compatibility

Every skill must declare:

```
"schema_version": "1.0"
```

In its structured output. If a skill reads from master context, it must also declare:

```
"context_version_read": 15
```

### Migration Strategy (When Upgrading to 2.0)

1. **Deprecation period:** 1 full engagement cycle
2. **Dual support:** System accepts both 1.x and 2.0 outputs
3. **Mapping layer:** Automatic translation from old → new schema
4. **Cutover:** Full migration to 2.0 after deprecation period
5. **Rollback plan:** If 2.0 breaks conflict detection, revert to 1.0

---

## 5. Skill-Specific Implementation Checklist

Use this checklist when implementing structured output in your skill:

### Before You Output

- [ ] Did you declare `skill_name` and `engagement_id`? They must match across all skills in one engagement.
- [ ] Did you populate all REQUIRED fields (skill_metadata, analysis_quality, key_findings, recommendations, risk_flags, kill_conditions, assumptions, data_points, dependencies)?
- [ ] Did you check that every percentage has numerator/denominator context?
- [ ] Did you check that every financial figure includes currency, period, and basis?
- [ ] Did you check that every confidence tag includes a 1-sentence basis?
- [ ] Did you list which upstream skills you consumed (dependencies_consumed)?
- [ ] Did you list which downstream skills should use your output (dependencies_produced)?
- [ ] Did you detect any conflicts with other skills' positions and flag them?
- [ ] Did you validate your schema against the JSON schema above (lint before output)?

### During Output

- [ ] Is your narrative still readable and complete (Part 1)?
- [ ] Is your structured output valid JSON (Part 2)?
- [ ] Does your `engagement_id` match the engagement context?

### After Output (Report Generation)

- [ ] Did the ATLAS template successfully parse your JSON?
- [ ] Did all your data points appear in the report?
- [ ] Did your conflict flags trigger conflict resolution?
- [ ] Did downstream skills successfully read your dependencies_produced?

---

## 6. Integration with ATLAS Report Template

The ATLAS report template automatically:

1. **Consumes** all structured outputs from participating skills
2. **Validates** schema version compatibility
3. **Extracts** key_findings and recommendations into report sections
4. **Builds** conflict resolution pipeline from conflicts_detected
5. **Populates** data visualizations from data_points
6. **Verifies** dependency chains (if skill X claims it consumed skill Y, does Y exist in this engagement?)

### Report Generation Flow

```
Skill 1 Output (Narrative + Structured)
Skill 2 Output (Narrative + Structured)
...
Skill N Output (Narrative + Structured)
        ↓
ATLAS Template Stage 1: GENERATE
  • Parses all JSON
  • Validates schema versions match
  • Checks for missing critical fields
  • Detects conflicts
        ↓
If validation passes:
  • Builds report sections from narratives
  • Inserts data points from structured outputs
  • Flags conflicts for Stage 2
        ↓
If validation fails:
  • Returns error report specifying which skill(s) failed
  • Specifies field(s) missing or malformed
  • Does not proceed to Stage 2
```

---

## 7. Examples: How to Structure Different Skill Outputs

### Example 1: Strategy Partner Skill Output

```
[NARRATIVE ANALYSIS - full diagnostic output]

---

## Structured Output (ATLAS Pipeline)

```json
{
  "skill_metadata": {
    "skill_name": "strategy-partner",
    "skill_version": "3.2",
    "execution_timestamp": "2026-03-10T14:23:45Z",
    "engagement_id": "eng-2026-03-acme-growth",
    "engagement_name": "Acme Growth Strategy",
    "execution_speed_mode": "STANDARD"
  },
  "analysis_quality": {
    "confidence": {
      "overall": "H",
      "basis": "Analyzed 6 years of company financials, conducted 12 customer interviews, mapped competitive positioning against 5 main competitors. Initial diagnosis validated through executive team discussion."
    },
    "speed_mode": "STANDARD",
    "estimated_quality": "FULL",
    "iteration_count": 2
  },
  "key_findings": [
    {
      "finding": "Revenue growth has stalled because the company is pursuing too many customer segments simultaneously, diluting GTM effectiveness and product focus",
      "evidence": "Marketing spend up 35% YoY but CAC has increased 28% while LTV stayed flat; product roadmap addresses 7 different customer needs; sales team lacks clear targeting criteria",
      "confidence": "H",
      "quantified_metric": "CAC increased from $12K to $15.4K while LTV remained at $180K (Year 3 basis)",
      "implication": "Company must consolidate go-to-market strategy and focus engineering resources on the highest-value customer segment"
    },
    {
      "finding": "Management team lacks alignment on the core business model; three different strategic visions are competing for resources",
      "evidence": "CEO prioritizes enterprise transformation (large deals, slow sales). COO prioritizes mid-market efficiency (predictable revenue). VP Product prioritizes product-led growth (viral motion). No single strategy document exists; each division operates independently.",
      "confidence": "H",
      "quantified_metric": "Resource allocation across 3 distinct strategies; no consolidated plan",
      "implication": "Before execution strategy can be designed, Rumelt Forge must create a single coherent strategy that the leadership team aligns to"
    },
    {
      "finding": "Competitive positioning is unclear; the company doesn't articulate a distinctive competitive advantage vs. main competitors",
      "evidence": "Compared our messaging vs. Competitor A, B, C—all claim similar value props (speed, ease of use, low cost). Customer interviews show no strong preference driver other than price.",
      "confidence": "M",
      "quantified_metric": null,
      "implication": "GTM strategy must be built on a stronger competitive differentiation; pricing alone won't sustain growth"
    }
  ],
  "recommendations": [
    {
      "action": "Immediately consolidate to 2 primary customer segments (Enterprise and Mid-Market); kill all other segmentation efforts",
      "rationale": "Fragmented GTM is causing inefficient marketing spend. Concentrating on 2 segments will improve CAC trajectory and allow Product team to focus deeply on PMF validation",
      "expected_outcome": "CAC trajectory improves from +28% to flat/negative within 2 quarters; Product team ships feature differentiation for primary segments",
      "timeline": "Weeks 1-4 of Year 2 plan",
      "owner": "CEO (strategic decision); CMO (execution of go-to-market)",
      "confidence": "H",
      "confidence_basis": "This approach is validated by 6 companies in our reference set (Intercom, Drift, Zendesk) that all went through similar consolidation",
      "success_metric": "CAC improves and LTV expands; sales cycle predictability increases"
    },
    {
      "action": "Commission Rumelt Forge to build a single strategy kernel that all divisions align to by end of Q1",
      "rationale": "Misaligned leadership is the primary blocker to execution. A clear, coherent strategy will unblock resource decisions and prioritization",
      "expected_outcome": "Leadership alignment on strategy; clear prioritization of investments; elimination of conflicting initiatives",
      "timeline": "Q1 2026 (8-week engagement)",
      "owner": "CEO",
      "confidence": "H",
      "confidence_basis": "Strategy clarity has resolved similar conflicts in 4 prior Rumelt engagements in this portfolio",
      "success_metric": "Leadership team signs off on single strategy document; resource allocation aligns to that strategy"
    }
  ],
  "risk_flags": [
    {
      "risk": "If we consolidate to 2 segments, the other segments won't grow—but those segments represent 25% of current revenue",
      "probability": "H",
      "impact": "H",
      "mitigation": "Model the long-term revenue impact of consolidated focus vs. fragmented growth. If consolidated approach drives higher LTV and lower CAC, it should win on lifetime value even with lower near-term revenue.",
      "trigger": "Monthly revenue reporting shows decline in 'other' segments >15% MoM; escalate to CEO for decision to continue vs. stop consolidation"
    },
    {
      "risk": "Leadership misalignment is deep; Rumelt Forge builds a strategy that 1-2 executives still resist",
      "probability": "M",
      "impact": "H",
      "mitigation": "Conduct pre-work with each executive to understand their vision; use that to inform Rumelt's strategy building. Include executives in Rumelt's process so they feel ownership of the output.",
      "trigger": "During Rumelt's work, any executive is hesitant to engage or dismissive of direction; surface immediately"
    }
  ],
  "kill_conditions": [
    {
      "condition": "If analysis shows our TAM is <$100M and we're already at 15% share, growth strategy won't work—we'd need to enter adjacent markets",
      "threshold": "TAM < $100M, our share > 10%",
      "action_if_triggered": "Restart analysis to understand adjacent market expansion as primary growth lever instead of consolidation within current market",
      "monitoring_frequency": "Market research update Q2 2026"
    }
  ],
  "assumptions": [
    {
      "assumption": "The 2 primary customer segments we've identified (Enterprise and Mid-Market) will still have PMF after we consolidate and stop serving other segments",
      "impact_if_wrong": "MATERIAL",
      "validation_method": "Conduct win/loss analysis with customers in those 2 segments; verify retention and expansion rates remain >80% and >20% respectively",
      "validation_status": "IN_PROGRESS",
      "validation_timeline": "End of Q1 2026"
    },
    {
      "assumption": "Management team will accept a single coherent strategy even if it means deprioritizing some executives' preferred initiatives",
      "impact_if_wrong": "MATERIAL",
      "validation_method": "Pre-work conversations with each executive; explicit commitment to adopt single strategy",
      "validation_status": "UNTESTED",
      "validation_timeline": "Before commissioning Rumelt Forge (Week 2 of engagement)"
    },
    {
      "assumption": "Competitive differentiation can be built within our product and messaging; it's not a core limitation",
      "impact_if_wrong": "MODERATE",
      "validation_method": "Product Innovation skill assesses whether differentiation is achievable in 6-12 months",
      "validation_status": "UNTESTED",
      "validation_timeline": "After Product Innovation executes"
    }
  ],
  "data_points": [
    {
      "metric": "Revenue",
      "value": "45.2",
      "unit": "$M",
      "source": "Company financials 2025",
      "confidence": "H",
      "date_of_measurement": "2025-12-31",
      "basis": "GAAP reported revenue, full year"
    },
    {
      "metric": "YoY Revenue Growth",
      "value": "12",
      "unit": "%",
      "source": "Company financials 2024-2025",
      "confidence": "H",
      "date_of_measurement": "2025-12-31",
      "basis": "$40.3M in 2024 → $45.2M in 2025"
    },
    {
      "metric": "CAC",
      "value": "15400",
      "unit": "$",
      "source": "Company finance system, quarterly analysis",
      "confidence": "M",
      "date_of_measurement": "2026-Q1",
      "basis": "Marketing spend divided by new customers acquired; does not include sales headcount allocation"
    },
    {
      "metric": "LTV",
      "value": "180000",
      "unit": "$",
      "source": "Company finance system, cohort analysis",
      "confidence": "M",
      "date_of_measurement": "2025-Q4",
      "basis": "Average customer lifetime value for 2022 cohorts; assumes 3-year retention, 20% expansion"
    },
    {
      "metric": "LTV:CAC Ratio",
      "value": "11.7",
      "unit": "ratio",
      "source": "Calculated from CAC and LTV above",
      "confidence": "M",
      "date_of_measurement": "2026-Q1",
      "basis": "$180K LTV / $15.4K CAC; above benchmark of 3:1, so unit economics are healthy"
    },
    {
      "metric": "Marketing Spend Growth",
      "value": "35",
      "unit": "%",
      "source": "Company budget tracking",
      "confidence": "H",
      "date_of_measurement": "2025-12-31",
      "basis": "2024 marketing spend vs. 2025; $8.2M → $11.1M"
    }
  ],
  "dependencies": {
    "dependencies_consumed": [
      "None (Strategy Partner is first skill in this engagement)"
    ],
    "dependencies_produced": [
      "rumelt-forge (Strategy Partner diagnosis will inform strategy kernel building)",
      "gtm-strategy (Recommended segment consolidation will shape GTM design)",
      "product-innovation (Need Product to validate PMF in consolidated segments)"
    ],
    "missing_dependencies": []
  },
  "conflicts_detected": [
    {
      "conflicting_skill": "None yet (Strategy Partner is first skill)",
      "this_position": null,
      "their_position": null,
      "resolution_needed": false,
      "conflict_type": null,
      "my_confidence_in_my_position": null,
      "their_confidence_in_theirs": null,
      "attempted_resolution": null
    }
  ],
  "context_written": {
    "context_keys_updated": [
      "diagnosis_state.current_understanding",
      "diagnosis_state.key_findings",
      "diagnosis_state.confidence",
      "assumption_register.strategic_assumptions",
      "hypothesis_register.pmf_hypothesis",
      "hypothesis_register.competitive_differentiation_hypothesis"
    ],
    "context_version": 1
  }
}
```
```

### Example 2: Financial Strategy Skill Output (Partial)

```
[NARRATIVE FINANCIAL ANALYSIS]

---

## Structured Output (ATLAS Pipeline)

```json
{
  "skill_metadata": {
    "skill_name": "financial-strategy",
    "skill_version": "2.1",
    "execution_timestamp": "2026-03-10T16:45:22Z",
    "engagement_id": "eng-2026-03-acme-growth",
    "engagement_name": "Acme Growth Strategy",
    "execution_speed_mode": "STANDARD"
  },
  "analysis_quality": {
    "confidence": {
      "overall": "H",
      "basis": "Built unit economics model using 3 years historical data, validated CAC assumptions with 5 customers, benchmarked unit economics against 12 comparable public SaaS companies"
    },
    "speed_mode": "STANDARD",
    "estimated_quality": "FULL",
    "iteration_count": 1
  },
  "key_findings": [
    {
      "finding": "Current unit economics can support 30% YoY growth; higher growth rates require either improving LTV or reducing CAC",
      "evidence": "At current CAC of $15.4K and LTV of $180K with 3-year payback, Rule of 40 (growth + margin) is 42%, which is healthy. But at 40% growth target, we burn more cash than current model generates.",
      "confidence": "H",
      "quantified_metric": "Payback period = 10.3 months (CAC $15.4K ÷ monthly margin of $1.5K); at 40% growth, payback extends to 14 months",
      "implication": "Growth strategy must be calibrated to 30% YoY unless we improve unit economics in parallel"
    }
  ],
  "recommendations": [
    {
      "action": "If strategy demands 40% growth, invest in expanding LTV by 15% (retention improvement + expansion revenue) in parallel",
      "rationale": "LTV expansion to $207K would restore 10.3-month payback even at 40% growth targets",
      "expected_outcome": "Rule of 40 remains healthy at higher growth rate; cash generation supports growth investments",
      "timeline": "Implement retention improvements within 6 months of Year 2 start",
      "owner": "VP Product + VP Customer Success",
      "confidence": "H",
      "confidence_basis": "Comparable SaaS companies (Zendesk, Intercom) have achieved 15% LTV expansion through similar initiatives",
      "success_metric": "LTV increases to $207K; monthly churn rate decreases from 5% to 3.5%"
    }
  ],
  "risk_flags": [
    {
      "risk": "If CAC grows faster than LTV (current trajectory), payback period will exceed 12 months and cash will be constrained",
      "probability": "M",
      "impact": "H",
      "mitigation": "Monitor CAC and LTV monthly; if CAC > LTV trend worsens, reduce growth investments until ratio stabilizes",
      "trigger": "Payback period exceeds 12 months for 2 consecutive months; escalate to CFO"
    }
  ],
  "kill_conditions": [
    {
      "condition": "If LTV drops below $140K or CAC exceeds $20K, unit economics are broken and growth strategy is not viable without capital injection",
      "threshold": "LTV < $140K or CAC > $20K",
      "action_if_triggered": "Halt growth investments; focus on efficiency improvements until unit economics restore to LTV >= $160K",
      "monitoring_frequency": "Monthly cohort analysis"
    }
  ],
  "assumptions": [
    {
      "assumption": "Retention rates will remain stable as we grow from 45 to 68 employees and scale GTM",
      "impact_if_wrong": "MATERIAL",
      "validation_method": "Monthly cohort retention analysis; track retention by onboarding cohort and hiring period",
      "validation_status": "IN_PROGRESS",
      "validation_timeline": "Monitor throughout Year 2"
    },
    {
      "assumption": "Customer mix (Enterprise 60%, Mid-Market 40%) will remain stable; no single large deal will distort unit economics",
      "impact_if_wrong": "MODERATE",
      "validation_method": "Monthly revenue mix analysis; flag if single customer > 5% of MRR",
      "validation_status": "VALIDATED",
      "validation_timeline": "Validated through 2025 data analysis"
    }
  ],
  "data_points": [
    {
      "metric": "CAC (Current)",
      "value": "15400",
      "unit": "$",
      "source": "Company finance system Q1 2026",
      "confidence": "M",
      "date_of_measurement": "2026-03-09",
      "basis": "Marketing spend + allocated sales headcount ÷ new customers; does not include product and onboarding"
    },
    {
      "metric": "LTV (Current)",
      "value": "180000",
      "unit": "$",
      "source": "Cohort analysis 2022-2025 customers",
      "confidence": "H",
      "date_of_measurement": "2026-03-01",
      "basis": "Average lifetime value assuming 3-year retention, 20% annual expansion, $5K average annual value per customer"
    },
    {
      "metric": "Payback Period (Months)",
      "value": "10.3",
      "unit": "months",
      "source": "Calculated from CAC and monthly contribution margin",
      "confidence": "H",
      "date_of_measurement": "2026-03-09",
      "basis": "CAC $15.4K ÷ average monthly contribution margin $1.5K"
    },
    {
      "metric": "Gross Margin",
      "value": "72",
      "unit": "%",
      "source": "Company P&L 2025",
      "confidence": "H",
      "date_of_measurement": "2025-12-31",
      "basis": "Revenue $45.2M minus COGS $12.6M = $32.6M ÷ $45.2M"
    },
    {
      "metric": "Operating Margin (Current)",
      "value": "-8",
      "unit": "%",
      "source": "Company P&L 2025",
      "confidence": "H",
      "date_of_measurement": "2025-12-31",
      "basis": "Operating expenses (headcount + G&A) exceed contribution margin by $3.6M"
    },
    {
      "metric": "Monthly Churn Rate",
      "value": "5",
      "unit": "%",
      "source": "Company analytics 2025",
      "confidence": "M",
      "date_of_measurement": "2025-12-31",
      "basis": "Average monthly churn across all customer cohorts; Enterprise cohorts churn at 2%, Mid-Market at 7%"
    }
  ],
  "dependencies": {
    "dependencies_consumed": [
      "rumelt-forge (consumed strategy kernel to assess feasibility of growth targets)",
      "gtm-strategy (consumed GTM assumptions about CAC trajectory to validate financial model)"
    ],
    "dependencies_produced": [
      "capital-resource-strategy (Financial model informs capital requirements for growth investment)",
      "operating-model (Unit economics will inform operating cost structure for Year 2)",
      "growth-strategy (Financial model will constrain growth rate assumptions)"
    ],
    "missing_dependencies": []
  },
  "conflicts_detected": [
    {
      "conflicting_skill": "gtm-strategy",
      "this_position": "CAC at current $15.4K is optimal; any increase degrades unit economics. GTM should optimize for efficient customer acquisition.",
      "their_position": "GTM model assumes CAC of $18K in Year 2 due to increased competition for customer attention.",
      "resolution_needed": true,
      "conflict_type": "OPERATIONAL",
      "my_confidence_in_my_position": "H",
      "their_confidence_in_theirs": "M",
      "attempted_resolution": "Flagged for Devil's Advocate synthesis; Financial position is benchmarked, GTM position is directional. Recommend GTM stress-test their model to hit $15.4K CAC target; if not possible, Financial will adjust growth rate expectations down."
    }
  ],
  "context_written": {
    "context_keys_updated": [
      "financial_state.unit_economics",
      "financial_state.payback_period",
      "financial_state.growth_constraint",
      "financial_state.margin_forecast"
    ],
    "context_version": 2
  }
}
```
```

---

## 8. Troubleshooting: Common Schema Errors

| Error | Cause | Fix |
|---|---|---|
| `engagement_id` mismatch | Skill used different engagement ID than other skills | Use the `engagement_id` from master context object; verify all skills read same context |
| Empty `dependencies_produced` | Skill doesn't know which downstream skills will consume its output | Check INTEGRATION.md Routing Decision Tree and Playbooks; list all skills that need your output |
| Missing `confidence_basis` | Confidence tag without explanation | For every confidence level (H/M/L), add a 1-sentence explanation |
| Percentage without numerator/denominator | Ambiguous metric | Add (X/Y) context; e.g., "42% (gross margin = revenue minus COGS ÷ revenue)" |
| Data point with no `source` | Unclear where data came from | Cite specific document, interview, analysis, or external database |
| Conflict marked but no `attempted_resolution` | Conflict detected but not addressed | Either resolve it here or flag for Devil's Advocate synthesis in CONFLICT-RESOLUTION.md |
| Schema doesn't validate as JSON | Syntax error in structured output | Run through JSON linter before outputting |

---

## 9. Validation Checklist Before ATLAS Generation

The ATLAS template runs this validation BEFORE consuming skill outputs:

- [ ] All required fields are present and non-empty
- [ ] `engagement_id` matches across all skills in engagement
- [ ] `schema_version` is 1.0 or declared compatible
- [ ] No duplicate findings/recommendations/risks
- [ ] All percentages include numerator/denominator context
- [ ] All financial figures include currency and basis
- [ ] All confidence tags include 1-sentence basis
- [ ] All data points have source and date
- [ ] JSON is valid (no syntax errors)
- [ ] If conflicts detected, they follow the structure in CONFLICT-RESOLUTION.md
- [ ] Dependencies listed in `dependencies_consumed` and `dependencies_produced` match actual skills in engagement
- [ ] No circular dependencies (skill A consumes B consumes A)

If ANY validation fails, ATLAS returns error report and does not proceed to report generation.

---

## End of Data Contract Specification

This document defines the universal output format that enables the StrategyOS skill ecosystem to operate as an integrated system. Every skill MUST conform to this contract. The ATLAS report template and conflict resolution engine depend on it.

**Questions?** Refer to CONTEXT-FLOW.md for context object structure or CONFLICT-RESOLUTION.md for conflict handling.
