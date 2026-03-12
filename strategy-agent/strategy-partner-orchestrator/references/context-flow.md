# StrategyOS Context Flow Specification

**Purpose:** Define the master context object that accumulates across all skills in an engagement, specify what each skill reads and writes, and resolve the contradiction in INTEGRATION.md where context flow templates are referenced but don't exist.

**Version:** 1.0 | **Status:** ACTIVE | **Updated:** 2026-03-10

---

## 1. Master Context Object (Shared State)

Every engagement maintains a single master context object that all 12 skills read from and write to. This object starts empty at engagement start and accumulates knowledge as each skill executes.

### Complete Master Context Schema

```json
{
  "engagement_metadata": {
    "engagement_id": "string (e.g., 'eng-2026-03-acme-growth')",
    "engagement_name": "string (e.g., 'Acme Growth Strategy')",
    "engagement_start_date": "ISO 8601",
    "engagement_status": "ACTIVE | PAUSED | COMPLETED",
    "client_name": "string",
    "primary_decision_maker": "string",
    "engagement_type": "ANNUAL_STRATEGY | FUNCTIONAL_STRATEGY | CRISIS | SPECIAL_PROJECT"
  },

  "client_context": {
    "company_name": "string",
    "industry": "string",
    "industry_segment": "string (if applicable)",
    "company_stage": "SEED | SERIES_A | SERIES_B+ | LATE_STAGE | PUBLIC | PRIVATE_EQUITY",
    "revenue_scale": "string (e.g., '$45M ARR')",
    "employee_count": "integer",
    "geographic_scope": "string (e.g., 'North America, EMEA')",
    "current_business_model": "string (e.g., 'SaaS, subscription')",
    "key_products": [
      "string (product/service name)"
    ],
    "urgency_level": "CRITICAL | HIGH | MEDIUM | LOW",
    "urgency_reason": "string (why is this decision urgent?)",
    "budget_available": "string (e.g., '$500K for engagement')",
    "executive_commitment_level": "HIGH | MEDIUM | LOW",
    "prior_strategy_work": "string (what strategy exists already?)"
  },

  "diagnosis_state": {
    "current_understanding": "string (what do we understand about the situation so far?)",
    "situation_summary": "string (2-3 sentence executive summary of the situation)",
    "key_findings": [
      {
        "finding": "string",
        "evidence": "string",
        "confidence": "H | M | L",
        "source_skill": "string (which skill found this?)"
      }
    ],
    "confidence": {
      "overall": "H | M | L",
      "confidence_basis": "string (what's making us confident or uncertain?)"
    },
    "key_uncertainties": [
      "string (what could change our diagnosis?)"
    ],
    "problem_classification": "COMPETITIVE | GROWTH | OPERATIONAL | FINANCIAL | ORG | TECH | GTM | M&A | OTHER",
    "root_cause_hypothesis": "string (our best hypothesis about what's really causing the problem)",
    "analysis_completeness": "COMPLETE | IN_PROGRESS | BLOCKED (if blocked, why?)"
  },

  "strategy_state": {
    "crux": {
      "statement": "string (singular challenge that must be solved)",
      "rationale": "string (why this is the crux)",
      "source_skill": "rumelt-forge"
    },
    "kernel": {
      "diagnosis": "string (explanatory framework for why we have the crux)",
      "guiding_policy": "string (the approach that creates competitive advantage)",
      "coherent_actions": [
        {
          "action": "string (specific, coordinated move)",
          "owner": "string (who executes)",
          "timeline": "string (when)",
          "resources_required": "string",
          "dependencies": "string (what must happen first)",
          "success_metric": "string (how we measure success)"
        }
      ],
      "source_skill": "rumelt-forge"
    },
    "validation_scores": {
      "bad_strategy_detector": "X/16 (lower is worse)",
      "coherence": {
        "overall": "X/100",
        "internal": "X/100 (are the actions internally consistent?)",
        "external": "X/100 (does it address the market reality?)",
        "execution": "X/100 (can we actually execute?)"
      },
      "confidence": "HIGH | MEDIUM | LOW"
    },
    "kill_conditions": [
      {
        "condition": "string (if this happens, abandon strategy)",
        "threshold": "string (specific measurement)",
        "monitoring_frequency": "string"
      }
    ],
    "strategy_revision_count": "integer (how many times has this been revised?)"
  },

  "financial_state": {
    "unit_economics": {
      "cac": {
        "value": "number",
        "currency": "string",
        "basis": "string (assumptions included)",
        "confidence": "H | M | L"
      },
      "ltv": {
        "value": "number",
        "currency": "string",
        "basis": "string (assumptions included)",
        "confidence": "H | M | L"
      },
      "payback_period_months": "number",
      "ltv_cac_ratio": "number (should be 3:1 or better)",
      "ltv_cac_ratio_healthy": "boolean"
    },
    "margins": {
      "gross_margin_percent": "number",
      "operating_margin_percent": "number",
      "net_margin_percent": "number (year and basis)",
      "margin_forecast": [
        {
          "year": "string (e.g., 'Year 2')",
          "gross_margin": "number",
          "operating_margin": "number",
          "net_margin": "number"
        }
      ]
    },
    "growth_constraint": "string (what's the maximum growth rate sustainable given unit economics?)",
    "capital_requirements": {
      "year_1": "string (e.g., '$5M')",
      "year_2": "string (e.g., '$8M')",
      "year_3": "string (e.g., '$12M')",
      "total_3_year": "string (e.g., '$25M')",
      "basis": "string"
    },
    "funding_strategy": "string (how are we financing growth?)",
    "source_skill": "financial-strategy"
  },

  "product_state": {
    "pmf_assessment": {
      "has_pmf": "boolean",
      "pmf_confidence": "H | M | L",
      "evidence": "string",
      "retention_rate": "string (e.g., '80% year-1 retention')",
      "expansion_rate": "string (e.g., '20% annual expansion')"
    },
    "feature_portfolio": [
      {
        "feature": "string",
        "pmf_signal": "HIGH | MEDIUM | LOW (does this drive retention?)",
        "market_signal": "HIGH | MEDIUM | LOW (does this win deals?)",
        "investment_priority": "string"
      }
    ],
    "product_roadmap": "string (link to external doc or summary)",
    "product_differentiation": "string (what makes our product distinctive?)",
    "source_skill": "product-innovation"
  },

  "execution_state": {
    "ninety_day_plan": {
      "phase": "string (e.g., 'Phase 1: Diagnosis and Foundation')",
      "objectives": [
        "string (specific 90-day objective)"
      ],
      "milestones": [
        {
          "milestone": "string",
          "date": "ISO 8601",
          "owner": "string"
        }
      ],
      "success_metrics": [
        "string (how we measure 90-day success)"
      ]
    },
    "key_initiatives": [
      {
        "initiative": "string (name)",
        "owner": "string",
        "timeline": "string",
        "budget": "string (if applicable)",
        "dependencies": [
          "string (what must happen first?)"
        ]
      }
    ],
    "gtm_model": {
      "customer_acquisition_motion": "string (PLG, field sales, partner-led, etc.)",
      "customer_segments": [
        {
          "segment": "string",
          "size_estimate": "string",
          "go_to_market_approach": "string"
        }
      ],
      "messaging_pillars": [
        "string"
      ],
      "pricing_strategy": "string"
    },
    "org_model": {
      "structure_summary": "string (current structure vs. proposed structure)",
      "key_changes": [
        "string"
      ],
      "reporting_structure": "string (link to org chart or summary)"
    },
    "source_skills": [
      "gtm-strategy",
      "operating-model",
      "people-talent"
    ]
  },

  "assumption_register": {
    "strategic_assumptions": [
      {
        "assumption": "string",
        "impact_if_wrong": "MATERIAL | MODERATE | LOW",
        "validation_method": "string",
        "validation_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
        "validation_timeline": "string (when should we know?)",
        "source_skill": "string"
      }
    ],
    "financial_assumptions": [
      {
        "assumption": "string",
        "impact_if_wrong": "MATERIAL | MODERATE | LOW",
        "validation_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
        "source_skill": "string"
      }
    ],
    "market_assumptions": [
      {
        "assumption": "string",
        "impact_if_wrong": "MATERIAL | MODERATE | LOW",
        "validation_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
        "source_skill": "string"
      }
    ],
    "execution_assumptions": [
      {
        "assumption": "string",
        "impact_if_wrong": "MATERIAL | MODERATE | LOW",
        "validation_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
        "source_skill": "string"
      }
    ]
  },

  "conflict_register": [
    {
      "conflict_id": "string (auto-generated)",
      "conflicting_skills": [
        "string",
        "string"
      ],
      "conflict_summary": "string (what's the disagreement?)",
      "resolution_status": "DETECTED | IN_SYNTHESIS | ESCALATED | RESOLVED",
      "resolution_approach": "string (how are we resolving it?)",
      "date_detected": "ISO 8601"
    }
  ],

  "hypothesis_register": [
    {
      "hypothesis": "string (what are we testing?)",
      "supporting_evidence": "string",
      "contradicting_evidence": "string (if any)",
      "test_status": "UNTESTED | IN_PROGRESS | VALIDATED | INVALIDATED",
      "test_timeline": "string (when will we know?)",
      "source_skill": "string"
    }
  ],

  "context_versioning": {
    "version": "integer (increments every time context is written)",
    "last_updated": "ISO 8601",
    "last_updated_by_skill": "string",
    "version_history": [
      {
        "version": "integer",
        "updated_at": "ISO 8601",
        "updated_by": "string",
        "keys_changed": [
          "string (list of keys modified in this version)"
        ]
      }
    ]
  }
}
```

---

## 2. Context Flow Maps: What Each Skill Reads and Writes

This section specifies for each of the 12 skills what context it READS, what it WRITES, and what it VALIDATES.

### SKILL 1: Strategy Partner

**Reads:**
- `client_context` (company, industry, stage, urgency)

**Writes:**
- `diagnosis_state.current_understanding`
- `diagnosis_state.situation_summary`
- `diagnosis_state.key_findings`
- `diagnosis_state.confidence`
- `diagnosis_state.key_uncertainties`
- `diagnosis_state.problem_classification`
- `diagnosis_state.root_cause_hypothesis`
- `assumption_register.strategic_assumptions`
- `assumption_register.market_assumptions`
- `hypothesis_register` (initial hypotheses to test)

**Validates Before Proceeding:**
- Does `client_context` contain enough information to diagnose? If not, request additional client background
- Is `engagement_id` populated and consistent?

**Escalation Rules:**
- If diagnosis confidence < 70%, request additional analysis from user before handing off to Rumelt Forge
- If problem classification is ambiguous, present to user for clarification

---

### SKILL 2: Rumelt Strategy Forge

**Reads:**
- `diagnosis_state.current_understanding`
- `diagnosis_state.key_findings`
- `diagnosis_state.confidence`
- `diagnosis_state.problem_classification`
- `diagnosis_state.root_cause_hypothesis`
- `assumption_register.strategic_assumptions`

**Writes:**
- `strategy_state.crux.statement`
- `strategy_state.crux.rationale`
- `strategy_state.kernel.diagnosis`
- `strategy_state.kernel.guiding_policy`
- `strategy_state.kernel.coherent_actions`
- `strategy_state.validation_scores`
- `strategy_state.kill_conditions`

**Validates Before Proceeding:**
- Is `diagnosis_state.confidence.overall` >= 70%? If not, request Strategy Partner to increase confidence before proceeding
- Are the key findings in `diagnosis_state.key_findings` specific enough to build a strategy on?

**Escalation Rules:**
- If coherence score < 70/100, iterate on kernel (max 3 iterations). If still <70, escalate to user with options: (a) provide additional diagnostic input, or (b) accept lower-confidence strategy
- If multiple crux candidates are equally valid (within 5 points), present top 3 to user for decision

---

### SKILL 3: Growth Strategy

**Reads:**
- `strategy_state.kernel` (guiding policy, coherent actions)
- `strategy_state.crux`
- `financial_state.unit_economics` (CAC, LTV constraints)
- `financial_state.growth_constraint` (what growth rate is sustainable?)
- `product_state.pmf_assessment` (do we have product-market fit?)

**Writes:**
- `diagnosis_state.key_findings` (adds findings about growth drivers and blockers)
- `execution_state.ninety_day_plan.objectives` (growth-specific objectives)
- `assumption_register.financial_assumptions` (growth rate assumptions)
- `hypothesis_register` (growth hypotheses to test)

**Validates Before Proceeding:**
- Is `strategy_state.kernel` populated and validated (coherence >= 70)?
- Is `financial_state.unit_economics` populated? If LTV/CAC not yet calculated, growth strategy runs at reduced confidence

**Bidirectional Flow with Financial:**
- Iterates with Financial Strategy: Growth proposes growth rate → Financial validates unit economics support that rate
- Max 2 iterations; convergence when growth rate proposal doesn't change >5%
- If no convergence after 2 iterations, escalate to user with both positions

---

### SKILL 4: GTM Strategy

**Reads:**
- `strategy_state.kernel` (guiding policy, coherent actions)
- `strategy_state.crux`
- `product_state.pmf_assessment` (does product have PMF?)
- `product_state.feature_portfolio` (which features win deals?)
- `financial_state.unit_economics` (CAC assumptions)
- `execution_state.execution_state.gtm_model` (prior GTM context, if any)

**Writes:**
- `execution_state.gtm_model.customer_acquisition_motion`
- `execution_state.gtm_model.customer_segments`
- `execution_state.gtm_model.messaging_pillars`
- `execution_state.gtm_model.pricing_strategy`
- `assumption_register.execution_assumptions` (GTM execution assumptions)
- `hypothesis_register` (GTM hypotheses: which customer segment responds to which message?)

**Validates Before Proceeding:**
- Is `strategy_state.kernel` populated and coherence >= 70%?
- Is `product_state.pmf_assessment.has_pmf` true? If unclear (<70% confidence), request Product Innovation to clarify before proceeding

**Bidirectional Flow with Product:**
- GTM claims "Feature X wins deals" → Product claims "Feature Y drives retention"
- Max 2 iterations; convergence when feature priority doesn't change
- If conflict persists after 2 iterations: Product's PMF signal wins if confidence >= 70%; else escalate to user

---

### SKILL 5: Financial Strategy

**Reads:**
- `strategy_state.kernel` (guiding policy, coherent actions to assess feasibility)
- `strategy_state.crux`
- `diagnosis_state.key_findings` (to understand business context)
- `execution_state.ninety_day_plan` (to model costs)
- `assumption_register.financial_assumptions` (prior financial assumptions)

**Writes:**
- `financial_state.unit_economics` (CAC, LTV, payback)
- `financial_state.margins` (gross, operating, net margins)
- `financial_state.growth_constraint` (maximum sustainable growth rate)
- `financial_state.capital_requirements` (how much capital needed?)
- `financial_state.funding_strategy` (how will we fund this?)
- `assumption_register.financial_assumptions` (updates with confidence levels)

**Validates Before Proceeding:**
- Is `strategy_state.kernel` populated? If not, wait for Rumelt Forge

**Bidirectional Flow with Growth & GTM:**
- Financial validates Growth's growth rate assumptions
- Financial validates GTM's CAC assumptions
- Growth/GTM iterates back if margins don't work at proposed rate/CAC
- Max 2 iterations per pair; if no convergence, escalate to user

---

### SKILL 6: Capital & Resource Strategy

**Reads:**
- `financial_state` (all capital requirements, margins, growth constraints)
- `strategy_state.kernel` (to assess strategy feasibility given capital constraints)
- `execution_state.ninety_day_plan` (capital needs for 90-day plan)

**Writes:**
- `financial_state.funding_strategy` (validates or revises Financial's funding approach)
- `execution_state.key_initiatives` (capital allocation across initiatives)
- `assumption_register.financial_assumptions` (funding assumptions)
- `conflict_register` (if strategy is not fundable given capital constraints)

**Validates Before Proceeding:**
- Is `financial_state.capital_requirements` fully populated?

**Bidirectional Flow with Financial:**
- Max 1 iteration: Capital validates Financial's funding strategy
- If Capital says "not fundable," escalate to user with options: (a) reduce scope, (b) extend timeline, (c) raise capital

---

### SKILL 7: AI-Native Strategy

**Reads:**
- `strategy_state.kernel` (to assess how AI can enable guiding policy)
- `product_state` (current product capabilities)
- `execution_state.gtm_model` (how AI can differentiate GTM)
- All prior analysis (to identify AI opportunities)

**Writes:**
- `diagnosis_state.key_findings` (adds AI-specific findings)
- `strategy_state.kernel.coherent_actions` (adds AI-enabling actions if not already present)
- `product_state.feature_portfolio` (flags AI features and their PMF signal)
- `assumption_register.execution_assumptions` (AI capability assumptions)
- `hypothesis_register` (AI hypotheses)

**Validates Before Proceeding:**
- Is `strategy_state.kernel` populated?
- Does the strategy require AI capabilities? If not, this skill may be optional

**Special Role:**
- Runs in PARALLEL with other skills (not sequential)
- Continuous monitoring: Re-validates AI assumptions monthly
- Real-time market intelligence: Flags if new competitive AI moves require strategy revision

---

### SKILL 8: M&A & Corp Dev

**Reads:**
- `strategy_state.kernel` (does acquisition help execute guiding policy?)
- `financial_state` (acquisition economics)
- `diagnosis_state.key_findings` (M&A as growth/positioning lever?)

**Writes:**
- `diagnosis_state.key_findings` (M&A thesis and strategic fit)
- `execution_state.key_initiatives` (acquisition project plan if approved)
- `assumption_register.financial_assumptions` (M&A synergy assumptions)
- `assumption_register.execution_assumptions` (integration assumptions)

**Validates Before Proceeding:**
- Is M&A on the table for this engagement? (Check problem classification and strategy decision)
- If yes: Is `strategy_state.kernel` populated to assess strategic fit?

**Escalation Rules:**
- If acquisition economics don't work, flag for Financial to validate
- If strategic fit is unclear, escalate to user for decision on whether to pursue

---

### SKILL 9: People & Talent Strategy

**Reads:**
- `execution_state.org_model` (operating model defines required org structure)
- `strategy_state.kernel.coherent_actions` (what actions require what talent?)
- `execution_state.ninety_day_plan` (talent needs for 90-day plan)
- `financial_state` (salary/benefit budget available)

**Writes:**
- `execution_state.org_model.structure_summary`
- `execution_state.org_model.key_changes`
- `execution_state.org_model.reporting_structure`
- `assumption_register.execution_assumptions` (talent availability, retention)
- `execution_state.ninety_day_plan.key_initiatives` (talent-related initiatives)

**Validates Before Proceeding:**
- Is `execution_state.org_model` context provided by Operating Model? If vague, escalate back to Operating Model

**Bidirectional Flow:**
- If People says "we can't hire that talent in that timeline," escalate to strategy for decision: extend timeline or reduce scope

---

### SKILL 10: Product Innovation Strategy

**Reads:**
- `diagnosis_state.key_findings` (what problems must product solve?)
- `strategy_state.kernel` (what does guiding policy require from product?)
- `execution_state.gtm_model` (what features must product have to win in market?)

**Writes:**
- `product_state.pmf_assessment` (does product have PMF?)
- `product_state.feature_portfolio` (features and their PMF/market signals)
- `product_state.product_roadmap` (roadmap to achieve PMF)
- `product_state.product_differentiation`
- `assumption_register.execution_assumptions` (feature PMF assumptions)

**Validates Before Proceeding:**
- Is problem classification clear? If not, Product waits for Strategy Partner to clarify

**Bidirectional Flow with GTM:**
- Product says "Feature X drives retention" → GTM says "Feature Y wins deals"
- Max 2 iterations; if conflict persists, Product's PMF signal wins if confidence >= 70%

---

### SKILL 11: Technology & Digital Strategy

**Reads:**
- `strategy_state.kernel` (what technology must enable guiding policy?)
- `product_state.product_roadmap` (what tech is required?)
- `execution_state.key_initiatives` (tech requirements for initiatives)
- `execution_state.org_model` (tech requirements to support org structure)

**Writes:**
- `execution_state.key_initiatives` (technology initiatives and roadmap)
- `assumption_register.execution_assumptions` (tech feasibility assumptions)
- `financial_state.capital_requirements` (capex for tech initiatives)
- `hypothesis_register` (tech hypotheses)

**Validates Before Proceeding:**
- Is `strategy_state.kernel` populated?

---

### SKILL 12: ATLAS Report Template

**Reads:**
- ALL context states (diagnosis, strategy, financial, product, execution, assumptions, conflicts)
- ALL skill structured outputs (from DATA-CONTRACT.md)

**Writes:**
- Final HTML report
- Cross-references and synthesis narratives
- Conflict resolutions (from CONFLICT-RESOLUTION.md)

**Validates Before Proceeding:**
- Are all required skills' structured outputs present?
- Are there unresolved conflicts? (If yes, escalates from CONFLICT-RESOLUTION.md)
- Is strategy_state.kernel populated and validated?

---

## 3. Bidirectional Flow Rules & Convergence

This section specifies when skills iterate with each other and when they escalate.

### Growth ↔ Financial

**Flow:**
```
Growth Strategy proposes 40% YoY growth target
        ↓
Financial Strategy validates unit economics support 40% growth
        ↓
If Financial says "marginal at 40%, healthy at 30%":
  Growth revises proposal to 30%
        ↓
If unit economics align within 5%, CONVERGE
If not, iterate max 2x, then escalate to user
```

**Convergence Criteria:** Growth rate doesn't change >5% between iterations

**Timeout:** If no convergence after 2 iterations, escalate to user with both positions and ask: "Do we prioritize growth speed or unit economics margin?"

---

### GTM ↔ Product

**Flow:**
```
GTM Strategy says "Enterprise customers prioritize Feature X"
        ↓
Product Innovation says "Our retention data shows Feature Y drives churn"
        ↓
If PMF confidence for Y >= 70%: Product wins, GTM accepts prioritization
If PMF confidence < 70%: Escalate to Strategy Partner for hypothesis testing
        ↓
Iterate max 2x, then if still conflict, escalate
```

**Convergence Criteria:** Feature priority doesn't change, or one side concedes

**Timeout:** If no convergence after 2 iterations, escalate to Strategy Partner + user

---

### Financial ↔ Capital Resource

**Flow:**
```
Financial proposes $25M capital requirement for 3-year plan
        ↓
Capital & Resource validates funding sources available
        ↓
If capital available: CONVERGE
If not: Capital flags conflict, escalate to user
```

**Convergence Criteria:** Max 1 iteration; this is mostly validation, not negotiation

**Timeout:** If not fundable, escalate to user with options: (a) reduce plan, (b) extend timeline, (c) different funding source

---

### GTM ↔ Financial

**Flow:**
```
GTM proposes CAC of $12K based on customer acquisition model
        ↓
Financial validates CAC assumption against market benchmarks
        ↓
If Financial finds CAC should be $15K based on competitive pay rates:
  GTM revises model to accommodate $15K CAC
  If unit economics still work: CONVERGE
  If not: Escalate to user (strategy may not be fundable)
```

**Convergence Criteria:** CAC assumption doesn't change >10%, or one side concedes

**Timeout:** Max 2 iterations, then escalate

---

## 4. Context Versioning & Conflict Detection

### Versioning Rules

Every write to master context increments `context_versioning.version`:

```
Initial state: version = 0
Strategy Partner writes diagnosis_state: version = 1
Rumelt writes strategy_state: version = 2
Growth writes to execution_state: version = 3
... etc
```

### Version Reading

When a skill reads from master context, it must note which version it read:

```json
{
  "context_version_read": 3,
  "fields_read": [
    "strategy_state.kernel",
    "financial_state.unit_economics"
  ]
}
```

### Conflict Detection via Versioning

If Skill A reads version 3, makes decisions based on that version, but by the time Skill A outputs, Skill B has written version 6, a potential conflict may exist:

**Auto-detect rule:** If a skill's output references data from version X but current version is now X+2, flag for review

**Example:**
- Version 3: Rumelt writes coherence score = 75/100
- Version 5: Growth identifies that growth target requires higher CAC than Financial thinks is achievable
- Version 6: Financial revises margins downward
- When ATLAS reports that Rumelt's coherence score is based on outdated financial assumptions, flag this for Devil's Advocate synthesis

---

## 5. Context Flow Playbook: Revenue Growth Engagement

Here's how context flows through an actual engagement:

### Timeline: Revenue Growth Strategy (8-week engagement)

**Week 1: Diagnosis**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 1 | Strategy Partner | client_context | diagnosis_state.{situation, key_findings, confidence} | 0→1 |
| Day 3 | Strategy Partner | diagnosis_state | hypothesis_register | 1→2 |

**Week 2: Strategy Forging**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 8 | Rumelt Forge | diagnosis_state v2 | strategy_state.{crux, kernel, validation_scores} | 2→3 |

**Week 3: Parallel Analysis**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 15 | Growth | strategy_state v3 | hypothesis_register (growth hypotheses) | 3→4 |
| Day 15 | Financial | strategy_state v3 | financial_state.{unit_economics, margins, growth_constraint} | 4→5 |
| Day 15 | Product Innovation | diagnosis_state v2 | product_state.pmf_assessment | 5→6 |

**Week 4: First Bidirectional Loop (Growth ↔ Financial)**

| Time | Skill | Read | Write | Iteration |
|---|---|---|---|---|
| Day 20 | Growth | financial_state v5 | Revises growth_hypothesis from 45% to 35% | Iteration 1 |
| Day 20 | Financial | growth_hypothesis revised | Validates 35% growth, margins converge | Iteration 1 |
| Day 21 | - | - | CONVERGE (unit economics + growth align) | - |

**Week 4-5: Second Bidirectional Loop (GTM ↔ Product)**

| Time | Skill | Read | Write | Iteration |
|---|---|---|---|---|
| Day 22 | GTM | product_state v6, strategy_state v3 | Proposes "Enterprise feature prioritization" | Iteration 1 |
| Day 22 | Product | gtm_proposal, product_state | Flags "But mid-market feature Y drives churn" (PMF conf 72%) | Conflict |
| Day 23 | GTM | product_pmf_analysis | Accepts Product's prioritization | Iteration 2 |
| Day 24 | Product | gtm_revised | CONVERGE | - |

**Week 5: Execution Design**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 27 | Operating Model | strategy_state v3 | execution_state.{ninety_day_plan, org_model} | 6→7 |
| Day 27 | People & Talent | org_model v7 | execution_state.{org_structure_detail, talent_initiatives} | 7→8 |

**Week 6: Capital & Integration**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 33 | Capital & Resource | financial_state v5, execution_state v8 | Validates capital req, funding_strategy | 8→9 |

**Week 7: Risk & Conflict Resolution**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 38 | All Skills | Final context v9 | conflict_register (if any conflicts remain) | 9→10 |

**Week 8: Report Generation**

| Time | Skill | Read | Write | Version |
|---|---|---|---|---|
| Day 45 | ATLAS Template | All context states v10 | Final HTML report | 10 (read-only) |

---

## 6. Context Flow Template Examples

These are the ACTUAL templates that INTEGRATION.md referenced but didn't provide.

### Template A: Strategy Partner → Rumelt Forge Handoff

**Strategy Partner outputs this context package to Rumelt:**

```
## Strategy Partner → Rumelt Forge Context Handoff

Engagement ID: {engagement_id}
Handoff Date: {ISO 8601}

### Diagnosis Summary
- Situation: {2-3 sentences}
- Key Finding 1: {evidence + confidence}
- Key Finding 2: {evidence + confidence}
- Key Finding 3: {evidence + confidence}
- Root Cause Hypothesis: {our best guess at what's causing the problem}

### Decision Frame
- Core Decision: {what must be decided}
- Decision Tree: {IF/THEN logic}
- Key Uncertainties: {what could swing the recommendation}

### Confidence Assessment
- Overall Diagnosis Confidence: {H/M/L} (% backing the confidence assessment)
- Confidence Basis: {1-2 sentences}

### Assumptions Requiring Validation
- Assumption 1: {what we're assuming + impact if wrong}
- Assumption 2: {...}

### Hypotheses for Testing
- Hypothesis 1: {what are we testing?}
- Hypothesis 2: {...}

### Readiness for Strategy Forge
- Analysis Complete: {YES/NO}
- Confidence Sufficient: {YES (>=70%) / NO (<70%)}
- If NO, Additional Analysis Needed: {list specific analyses}

**Context Version: {version number}**
```

**Rumelt reads this and:**
1. Validates diagnosis confidence >= 70%
2. If insufficient, requests additional analysis from Strategy Partner
3. If sufficient, builds strategy kernel using diagnosis as foundation

---

### Template B: Rumelt Forge → All Execution Skills Handoff

**Rumelt outputs this to Operating Model, GTM, Financial, People:**

```
## Rumelt Forge Output → Execution Skills

Engagement ID: {engagement_id}
Strategy Finalized: {ISO 8601}
Coherence Score: {X/100}

### The Crux
{Single sentence challenge statement}

### Strategy Kernel

**Diagnosis:** {Explanatory framework for why we have the crux}

**Guiding Policy:** {Approach that creates competitive advantage}

**Coherent Actions:**
1. Action: {Specific move}
   Owner: {Name + title}
   Timeline: {Q when}
   Resources: {What's required}
   Success Metric: {How we measure it}

2. Action: {...}

3. Action: {...}

### Validation Scores
- Bad Strategy Detector: {X/16}
- Coherence: {X/100} (Internal {X}, External {X}, Execution {X})
- Confidence: {HIGH/MEDIUM/LOW}

### Kill Conditions
- If {condition} happens, we abandon this strategy
- If {...}

### Assumptions to Validate
- Assumption 1: {what + impact if wrong}
- Assumption 2: {...}

### Routing Instructions
- **Operating Model:** Design org structure to deliver Actions 1-3. What governance, reporting, spans?
- **GTM Architect:** How do we take this guiding policy to market? What's the customer engagement model?
- **Financial Strategy:** Can we resource this? What are the unit economics? LTV/CAC?
- **People & Talent:** What talent model do we need to execute these actions?

**Context Version: {version}**
```

---

### Template C: Financial → Growth Convergence Template

**Financial outputs this to Growth:**

```
## Financial → Growth Unit Economics Validation

Engagement ID: {engagement_id}

### Your Growth Proposal
- Growth Target: {X% YoY}
- Customer Acquisition Rate: {per month}
- Assumed CAC: {$XXK}

### Financial Model Response
- Sustainable Growth Rate (at current CAC): {X% YoY}
- At Your Proposed {X% growth}:
  - Required CAC: {$XXK} (vs. your assumption of ${XXK})
  - Payback Period: {X months} (benchmark: 12 months max)
  - Unit Economics Status: {HEALTHY / TIGHT / BROKEN}

### Convergence Recommendation
- **Option A:** Reduce growth target to {X%} → unit economics healthy
- **Option B:** Improve LTV by {X%} → can support your growth target
- **Option C:** Accept tighter margins and tighter payback → escalate to user

**What's Your Decision?**

**Context Version: {version}**
```

---

## 7. Escalation Matrix: When to Stop and Ask

| Situation | Stop Point | Escalation | Decision Required |
|---|---|---|---|
| Diagnosis confidence <70% | Before Rumelt | Strategy Partner requests additional analysis | Do we have enough info? |
| Coherence score <70 after 3 iterations | At Rumelt | Multiple crux candidates at equal weight | Which strategic direction? |
| Growth rate causes unit economics to break | Growth ↔ Financial | Can't converge after 2 iterations | Do we prioritize growth or margins? |
| CAC/LTV assumptions don't align | GTM ↔ Financial | Conflicting customer acquisition models | What's the realistic CAC? |
| Feature priority conflicting | GTM ↔ Product | Can't resolve after 2 iterations | Which feature wins deals vs. drives retention? |
| Strategy not fundable | Financial ↔ Capital | Capital says "not enough funding" | Reduce scope / extend timeline / raise capital? |
| Org change required is >30% | Operating Model | Must confirm user intent | Is org restructuring intended? |
| Assumption invalidated mid-engagement | Any Skill | Critical assumption now false | Do we pivot strategy or accept risk? |

---

## 8. Practical Example: Context State at Week 4 of Revenue Growth Engagement

Here's what the actual master context object looks like mid-engagement:

```json
{
  "engagement_metadata": {
    "engagement_id": "eng-2026-03-acme-growth",
    "engagement_status": "ACTIVE",
    "context_versioning": {
      "version": 9,
      "last_updated": "2026-03-20T16:30:00Z",
      "last_updated_by_skill": "gtm-strategy"
    }
  },
  "client_context": {
    "company_name": "Acme SaaS",
    "revenue_scale": "$45M ARR",
    "urgency_level": "HIGH"
  },
  "diagnosis_state": {
    "current_understanding": "Revenue growth has stalled due to unfocused GTM and misaligned leadership. Primary issue is CAC not declining despite 35% marketing spend growth.",
    "situation_summary": "Mid-market SaaS company with healthy unit economics but stalled growth.",
    "confidence": {
      "overall": "H",
      "confidence_basis": "Validated through 12 customer interviews and 3-year financial analysis"
    }
  },
  "strategy_state": {
    "crux": {
      "statement": "Consolidate go-to-market focus to 2 primary customer segments to improve CAC and product differentiation",
      "source_skill": "rumelt-forge"
    },
    "kernel": {
      "diagnosis": "Company is spreading resources across 7 customer segments, none of which have breakthrough positioning",
      "guiding_policy": "Concentrate on Enterprise and Mid-Market; build deep PMF in each",
      "coherent_actions": [
        {
          "action": "Consolidate go-to-market to Enterprise segment (60% of revenue)",
          "owner": "CMO",
          "timeline": "Q2 2026"
        },
        {
          "action": "Build feature differentiation for Enterprise (compliance, integration, analytics)",
          "owner": "VP Product",
          "timeline": "Q2-Q3 2026"
        }
      ],
      "validation_scores": {
        "bad_strategy_detector": "12/16",
        "coherence": {
          "overall": "82/100",
          "internal": "85/100",
          "external": "78/100",
          "execution": "83/100"
        }
      }
    }
  },
  "financial_state": {
    "unit_economics": {
      "cac": {
        "value": 15400,
        "currency": "$",
        "confidence": "M"
      },
      "ltv": {
        "value": 180000,
        "currency": "$",
        "confidence": "H"
      },
      "payback_period_months": 10.3,
      "ltv_cac_ratio": 11.7,
      "ltv_cac_ratio_healthy": true
    },
    "growth_constraint": "35% YoY growth is sustainable at current CAC; 40% would require improved LTV or reduced CAC"
  },
  "product_state": {
    "pmf_assessment": {
      "has_pmf": true,
      "pmf_confidence": "H",
      "retention_rate": "80% year-1"
    }
  },
  "execution_state": {
    "ninety_day_plan": {
      "phase": "Foundation: Consolidate GTM + Build Feature Differentiation",
      "objectives": [
        "Consolidate marketing to Enterprise segment",
        "Build 3 new Enterprise features",
        "Realign sales and marketing messaging"
      ]
    }
  },
  "assumption_register": {
    "strategic_assumptions": [
      {
        "assumption": "Enterprise segment will absorb consolidation and continue growth",
        "validation_status": "IN_PROGRESS",
        "source_skill": "strategy-partner"
      },
      {
        "assumption": "New Enterprise features can be built in 12 weeks",
        "validation_status": "UNTESTED",
        "source_skill": "product-innovation"
      }
    ]
  },
  "conflict_register": [
    {
      "conflict_id": "conf-001",
      "conflicting_skills": [
        "gtm-strategy",
        "product-innovation"
      ],
      "conflict_summary": "GTM says Enterprise buyers prioritize compliance feature; Product says retention data shows analytics feature drives expansion",
      "resolution_status": "RESOLVED",
      "resolution_approach": "Product's PMF confidence (92%) > GTM's market signal confidence (65%); feature priority resolved to Product's recommendation",
      "date_detected": "2026-03-18"
    }
  ]
}
```

---

## End of Context Flow Specification

This document defines the shared state that all 12 skills reference and update during an engagement. Use the context flow maps to understand what your skill should read and write. Use the bidirectional flow rules to know when to escalate. Use the templates to hand off context to the next skill.

**Key Principle:** The master context object is the source of truth. If context is not documented here, it doesn't exist for the engagement.

