# Build vs. Buy vs. Partner for AI Capabilities

## Executive Summary

One of the most critical AI strategy decisions: Should you build proprietary AI capabilities, buy from vendors, or partner? The answer depends on strategic importance, differentiation potential, and execution capability.

**2026 Reality**:
- Foundation models are commoditizing (GPT-5.2 ≈ Claude ≈ Gemini 3)
- Building from scratch is only viable for tech giants or well-funded startups
- Buying/partnering with APIs is fastest but creates lock-in
- Open-source models (Llama 4) provide middle ground

---

## PART 1: BUILD VS. BUY VS. PARTNER DECISION FRAMEWORK

### 4-Quadrant Matrix

Strategic value (X-axis): Low ← → High
Implementation complexity (Y-axis): Low ← → High

| Quadrant | Strategic Value | Complexity | Decision | Timeline |
|----------|---|---|---|---|
| **Low value, Low complexity** | Marketing chatbot | Build simple, no custom | **BUY** (use API) | 2-4 weeks |
| **High value, Low complexity** | Recommendation system | Straightforward | **BUY** + customize | 4-8 weeks |
| **Low value, High complexity** | Specialized model for niche | Hard but not core | **PARTNER** | 8-12 weeks |
| **High value, High complexity** | Core autonomous system | Critical + complex | **BUILD** | 12-24 months |

### Detailed Decision Framework

```
Question 1: Is this capability core to your competitive advantage?
├─ NO → Continue to Question 2
└─ YES → BUILD (you need control)

Question 2: Is this strategically important 3+ years from now?
├─ NO → BUY (commodity)
├─ YES → Continue to Question 3

Question 3: Can you build it better than vendors?
├─ NO (vendors are better/faster) → BUY
├─ YES → Continue to Question 4
├─ MAYBE (uncertain) → PARTNER (hedge bet)

Question 4: Do you have talent and runway?
├─ NO → PARTNER or BUY
├─ YES → BUILD

Question 5: Is it strategically defensible long-term?
├─ YES (data moat, talent, IP) → BUILD
├─ NO (easily commoditized) → BUY
```

---

## PART 2: FOUNDATION MODEL SELECTION

### To Build, Buy, or Adapt?

**Scenario 1: Do You Need a Custom Foundation Model?**

**Factors to consider**:
- Do commodity models (GPT-5.2, Claude, Gemini) work for your use case?
  - If YES → Don't build, fine-tune or prompt engineer
  - If NO → Continue below

- Do you have unique data that would improve a model?
  - If NO → Use open-source (Llama 4) and fine-tune
  - If YES → Consider building (only if data is defensible)

- Do you have $100M+ and 18+ months?
  - If NO → Not realistic to build
  - If YES → DeepSeek and Llama paths show it's possible

**Decision**:
- **Build**: Only if you're a tech giant OR well-funded AI startup with defensible data advantage
- **Buy**: Use Claude, GPT-5.2, Gemini APIs (easier, faster)
- **Open-source + fine-tune**: Use Llama 4 or Qwen, specialize for your domain

---

### Foundation Model Selection Decision Tree

```
Do you need multimodal (image, video)?
├─ YES → Gemini 3 (best multimodal) or GPT-5.2
├─ NO → Continue

Do you need context >200K tokens?
├─ YES → Llama 4 Scout (10M context, only option)
├─ NO → Continue

Do you need best reasoning quality?
├─ YES → Claude Opus 4.6 or DeepSeek-R1
├─ NO → Continue

Do you need lowest cost?
├─ YES → Qwen 3 or Llama 4 Scout (self-hosted)
├─ NO → Continue

Do you need proprietary moat?
├─ YES → Fine-tune Claude or GPT-5.2 (builds model moat if differentiated)
├─ NO → Use commodity API

Do you need open-source compliance?
├─ YES → Llama 4 or DeepSeek (open)
└─ NO → Any vendor is OK
```

---

## PART 3: FINE-TUNING VS. PROMPT ENGINEERING VS. RAG DECISION TREE

### Decision Framework

```
Start: Do you need the model to learn task-specific behavior?

├─ NO (can handle with prompting) → Prompt Engineering + RAG
│
├─ YES (needs to learn patterns)
│   ├─ Does your domain have unique style/terminology? (Legal docs, medical reports)
│   │   ├─ YES → Fine-tuning
│   │   └─ NO → RAG might be enough
│   │
│   ├─ Do you have >500 examples of desired behavior?
│   │   ├─ YES (sufficient training data) → Fine-tuning
│   │   └─ NO (limited data) → Prompt engineering + few-shot examples
│   │
│   └─ How much does output quality matter?
│       ├─ Critical (hiring, legal decisions) → Fine-tuning
│       └─ Nice-to-have → Prompt engineering + RAG
```

---

### Option A: Prompt Engineering + RAG

**What**: Use the base model + retrieval-augmented generation

**Cost**:
- Development: 2-4 weeks
- LLM cost: $X per inference (base model cost)
- Infrastructure: Vector DB (~$200/month for 10M embeddings)
- Total: ~$500-1K/month

**Timeline**: 2-4 weeks to launch

**Pros**:
- ✓ Fastest to market
- ✓ Cheapest
- ✓ No custom training data needed
- ✓ Easy to iterate (just change prompts/retrieval)

**Cons**:
- ✗ Limited to what model already knows
- ✗ Can't teach unique patterns
- ✗ Hallucination risk remains
- ✗ Context window limits (how much data can you feed?)

**When to use**: 70% of AI products fall here

**Example**: Customer support chatbot
- Prompt: "You are a customer support agent. Use the following context to answer questions."
- RAG: Retrieve relevant docs from knowledge base
- Result: Model answers questions using retrieved docs
- Cost: $2-5K/month for 10K questions

---

### Option B: Fine-Tuning

**What**: Train model on your specific data to learn domain patterns

**Cost**:
- Training data preparation: $5-20K (labeling, curation)
- Fine-tuning compute: $5-30K (depends on model and data size)
- LLM cost: Slightly cheaper than base model (but additional cost initially)
- Total: $10-50K upfront, then lower per-inference cost

**Timeline**: 6-12 weeks (data prep, training, evaluation, iteration)

**Pros**:
- ✓ Model learns domain patterns
- ✓ Better accuracy on domain-specific tasks
- ✓ Potentially lower per-inference cost (smaller model or better efficiency)
- ✓ More control (model behavior)

**Cons**:
- ✗ Slower to market (6-12 weeks)
- ✗ Requires labeled training data
- ✗ Evaluation is complex (need domain expertise)
- ✗ Risks: Overfitting, catastrophic forgetting, bias

**When to use**: 20% of AI products (domain-specific)

**Examples**:
- **Legal document generation**: Model learns legal style, clause patterns
- **Medical notes**: Model learns medical terminology, document structure
- **Code generation**: Model learns your codebase patterns (autocomplete++)

**Fine-tuning Decision Checklist**:
- [ ] Do you have >500 examples of desired behavior? YES
- [ ] Is your domain specialized (legal, medical, technical)? YES
- [ ] Do generic models perform poorly for you (<80% accuracy)? YES
- [ ] Are you willing to wait 6-12 weeks? YES
- [ ] Can you commit to maintaining the fine-tuned model? YES

If all YES → Fine-tuning makes sense

---

### Option C: Full Model Training (Rare)

**What**: Train a model from scratch on your data

**Cost**:
- Infrastructure: $1-5M (GPUs, compute)
- Data: $1-10M (collection, labeling, curation)
- Team: $2-5M (researchers, engineers)
- Timeline: 18-36 months
- Total: $5-20M+

**When to use**: <1% of companies (tech giants, well-funded AI startups)

**Examples**:
- **DeepSeek**: Trained own models (cost advantage from China)
- **Anthropic**: Trained own models (safety focus)
- **OpenAI**: Trained GPT models (research + product)

**Reality check**: Unless you're a tech giant with defensible data advantage, don't do this.

---

## PART 4: VENDOR EVALUATION SCORECARD FOR AI

### Scoring Framework

Rate each vendor 1-5 on each criterion, then weight

| Criterion | Weight | Evaluation | Vendor A | Vendor B | Vendor C |
|-----------|--------|---|---|---|---|
| **Model Quality** | 25% | Test on your tasks (accuracy, latency, cost) | 5 | 4 | 3 |
| **Pricing & Economics** | 20% | TCO at 10x scale, margin sustainability | 5 | 3 | 4 |
| **API Stability & SLA** | 15% | Uptime, latency SLA, deprecation policy | 4 | 5 | 3 |
| **Safety & Compliance** | 15% | EU AI Act compliance, bias testing, transparency | 4 | 3 | 5 |
| **Integration Ease** | 10% | Time to integrate with your systems, MCP support | 5 | 3 | 4 |
| **Vendor Viability** | 10% | Funding, runway, team retention, market position | 5 | 4 | 2 |
| **Lock-in Risk** | 5% | How hard to migrate to alternative? (Invert: 5=low lock-in) | 3 | 5 | 2 |

**Weighted Total**: (5×0.25) + (5×0.20) + (4×0.15) + ... = **Final score out of 5**

**Threshold**: 3.5+/5 = proceed, 3-3.5 = caution, <3 = reject

---

### Vendor Comparison (2026)

**Vendor A: OpenAI (GPT-5.2)**

| Factor | Score | Notes |
|--------|-------|-------|
| Model quality | 5/5 | Best reasoning, fastest inference |
| Pricing | 3/5 | High cost ($1.75 input, $14 output) |
| API stability | 5/5 | Proven track record, high uptime |
| Safety/compliance | 4/5 | Good safety, but less transparent than Anthropic |
| Integration | 5/5 | Mature ecosystem, great docs |
| Vendor viability | 5/5 | Well-funded, Microsoft backing |
| Lock-in risk | 2/5 | High lock-in (GPT-optimized workflows hard to port) |
| **Total** | **4/5** | Great option but expensive |

**Vendor B: Anthropic (Claude Opus 4.6)**

| Factor | Score | Notes |
|--------|-------|-------|
| Model quality | 5/5 | Excellent reasoning, best instruction-following |
| Pricing | 2/5 | Highest cost ($5 input, $25 output) |
| API stability | 5/5 | Reliable, good uptime |
| Safety/compliance | 5/5 | Transparency, constitution AI, safety focus |
| Integration | 5/5 | Great Agent SDK, MCP native |
| Vendor viability | 4/5 | Well-funded, strong team |
| Lock-in risk | 3/5 | Medium lock-in (Claude SDK is proprietary but good) |
| **Total** | **4/5** | Best for reasoning, safest, but expensive |

**Vendor C: Google (Gemini 3)**

| Factor | Score | Notes |
|--------|-------|-------|
| Model quality | 4/5 | Good all-around, best multimodal |
| Pricing | 4/5 | Mid-range cost ($2.50 input, $10 output) |
| API stability | 4/5 | Stable, though outages have occurred |
| Safety/compliance | 4/5 | Good safety, less transparent than Anthropic |
| Integration | 4/5 | Good ecosystem, search integration |
| Vendor viability | 5/5 | Massive company, strong funding |
| Lock-in risk | 3/5 | Medium (ecosystem integration) |
| **Total** | **4/5** | Solid all-around option |

**Vendor D: Meta (Llama 4 Scout)**

| Factor | Score | Notes |
|--------|-------|-------|
| Model quality | 4/5 | Good quality, improving rapidly |
| Pricing | 5/5 | Cheapest ($0.40/1M) + open-source |
| API stability | 3/5 | Self-hosted = depends on you |
| Safety/compliance | 3/5 | Open-source = your responsibility |
| Integration | 4/5 | Open ecosystem, MCP-friendly |
| Vendor viability | 5/5 | Meta backing, well-funded |
| Lock-in risk | 5/5 | Lowest (open-source, no lock-in) |
| **Total** | **4/5** | Best value if you can self-host |

---

## PART 5: TOTAL COST OF OWNERSHIP (TCO) MODELING

### Cost Components

**Year 1: Build Phase**

| Component | Cost | Notes |
|-----------|------|-------|
| **Team** | $1-2M | 2-3 engineers + PM |
| **Training/Education** | $100K | Learning new tools |
| **Infrastructure** | $200K | Compute, storage, cloud |
| **LLM Vendor Costs** | $50-300K | Usage-based during build |
| **Tools/Services** | $50K | Monitoring, testing, ops |
| **Total Year 1** | **$1.4-2.7M** | Investment phase, little revenue |

**Year 2: Growth Phase**

| Component | Cost | Notes |
|-----------|------|-------|
| **Team** | $1.5-2M | Same team + specialized hires |
| **Infrastructure** | $500K | Scale to 10x usage |
| **LLM Vendor Costs** | $500K-2M | 10-100x volume from Y1 |
| **Tools/Services** | $100K | Monitoring, governance |
| **Total Year 2** | **$2.6-4.6M** | Still mostly investment, but revenue starting |

**Year 3: Scale Phase**

| Component | Cost | Notes |
|-----------|------|-------|
| **Team** | $2-3M | Full team, less hiring |
| **Infrastructure** | $1M | 100x scale from Y1 |
| **LLM Vendor Costs** | $2-5M | Heavy usage, but cost-optimized |
| **Tools/Services** | $200K | Mature ops |
| **Total Year 3** | **$5.2-8.2M** | Significant costs, but revenue likely >10M |

---

### TCO Example: Customer Service Agent Platform

**Assumptions**:
- Processing 10K customer interactions/month by end of Year 1
- Growing to 1M by end of Year 3
- Using Claude Opus + retrieval

**Year 1 Costs**:
- Team (2 engineers, 1 PM): $600K
- Infrastructure: $100K
- LLM costs (10K interactions × 2K tokens × $5/1M): $0.1K/month = $1.2K for year
- Tools: $50K
- Total: $751K (mostly team + infrastructure)

**Year 1 Revenue**:
- 5 customers, avg $50K ACV = $250K (if Q3 launch)
- Gross margin: 70% = $175K gross profit
- Net: -$576K (expected in growth phase)

**Year 2 Costs**:
- Team: $1M
- Infrastructure: $300K
- LLM costs (100K interactions/month avg): $0.6M/year
- Tools: $100K
- Total: $2M

**Year 2 Revenue**:
- 30 customers × $50K = $1.5M
- Gross margin 70%: $1.05M
- Net: -$950K (still investing)

**Year 3 Costs**:
- Team: $1.5M
- Infrastructure: $600K
- LLM costs (1M interactions/month = 12M/year × $5/1M): $60K/month = $720K/year
- Tools: $200K
- Total: $3.02M

**Year 3 Revenue**:
- 75 customers × $50K = $3.75M
- Gross margin 70%: $2.625M
- Net: -$395K (approaching breakeven)

**Year 4** (not shown):
- Costs flatten ~$3.5M (team growth slows)
- Revenue hits $7.5M (150 customers)
- Gross profit: $5.25M
- Net: +$1.75M (PROFITABLE)

**Key insight**: AI platforms need 3-4 years to profitability. Investors need patience.

---

## PART 6: INTEGRATION COMPLEXITY ASSESSMENT

### Build → Buy → Partner Complexity

| Scenario | Complexity | Timeline | Cost | Risk |
|----------|-----------|----------|------|------|
| **Buy LLM API, add to product** | Low | 2-4 weeks | $100K-500K | Low |
| **Fine-tune open-source model** | Medium | 6-10 weeks | $500K-2M | Medium |
| **Custom vector DB + RAG system** | Medium | 4-8 weeks | $300K-1M | Medium |
| **Multi-agent orchestration** | High | 8-16 weeks | $1-3M | High |
| **Custom model training** | Very High | 12-24 months | $5-20M | Very High |

---

## PART 7: OPEN-SOURCE VS. PROPRIETARY TRADEOFFS

### Detailed Comparison

| Factor | Open-Source (Llama 4) | Proprietary (Claude, GPT-5.2) |
|--------|---|---|
| **Initial Cost** | $0 (model is free) | $0 (API access, pay per use) |
| **Operational Cost** | Infrastructure (self-host): $1-5K/month | API costs: $0.50-5 per 1M tokens |
| **Model Quality** | Good (4/5), rapidly improving | Excellent (5/5) |
| **Customization** | High (fine-tune, modify) | Limited (prompt engineering) |
| **Speed to Market** | Medium (need ops expertise) | Fast (API, no ops needed) |
| **Lock-in Risk** | None (yours to run) | High (proprietary APIs) |
| **Compliance/Data** | Your responsibility | Shared responsibility |
| **Latency Predictability** | Depends on your infrastructure | Vendor-managed, predictable |
| **Community/Support** | Large community (Reddit, Discord) | Vendor support, professional |
| **Ability to Customize Safety** | High (you control everything) | Limited (vendor-controlled) |

### Decision: When to Use Each

**Use Open-Source (Llama 4) if**:
- [ ] You have infrastructure/ops expertise
- [ ] Model quality 4/5 is sufficient
- [ ] Cost is critical (you're processing massive volume)
- [ ] You want no lock-in
- [ ] You need model customization
- [ ] You want to avoid proprietary data residency issues

**Use Proprietary (Claude, GPT) if**:
- [ ] Speed to market is critical
- [ ] You need best-in-class quality (5/5)
- [ ] You lack ops expertise
- [ ] You have predictable budgets (usage-based ok)
- [ ] You want vendor support/SLA

**Hybrid (Recommended for 2026)**:
- Use Claude Opus for complex reasoning tasks (where quality matters)
- Use Llama 4 for high-volume, lower-complexity tasks (where cost matters)
- Blended cost: much cheaper than all Claude, better quality than all Llama

---

## DECISION CHECKLIST

- [ ] **Build vs. Buy**: Decision made and documented
- [ ] **Foundation model selected**: With unit economics validated
- [ ] **Fine-tuning decision**: If applicable, plan created
- [ ] **Vendor evaluation**: Scorecard completed
- [ ] **TCO modeled**: 3-year forecast complete
- [ ] **Integration complexity**: Assessed and mitigated
- [ ] **Lock-in risk**: Identified and mitigation plan
- [ ] **Switching cost**: Understood (if changing direction later)
- [ ] **Open-source vs. proprietary**: Strategic decision made
- [ ] **Budget approved**: By CFO and board

---

**Last Updated**: March 2026
**Reference**: SKILL.md Phase 6 (Build vs. Buy vs. Partner)
