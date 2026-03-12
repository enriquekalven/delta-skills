# AI Business Models & Value Creation

> **Pricing & Model Data**: All model costs, context windows, and capability ratings in this document are derived from [`model-economics-config.json`](model-economics-config.json). When prices change, update the config — not this document. The agent should read the config to generate current tables and calculations rather than relying on the static examples below.

## Executive Summary

AI business models fall into two broad categories: **AI-native** (AI is the core value mechanism) and **AI-enhanced** (traditional business + AI layer). This distinction determines strategy, competitive dynamics, unit economics, and long-term defensibility.

Most enterprises get this wrong. They either:
1. **Overestimate AI-native opportunity** ("We'll build an autonomous agent platform") when they should be AI-enhanced
2. **Underestimate AI-native potential** ("AI is just a feature") when they could build defensible moats

This reference guide provides archetypes, revenue patterns, unit economics frameworks, and a business model canvas to clarify which you're actually building.

---

## PART 1: AI-NATIVE BUSINESS MODEL ARCHETYPES

### Archetype 1: Data Flywheel

**Core Mechanism**: Better data → Better model → Better product → More usage → More data (exponential)

**Value Drivers**:
- Proprietary dataset that competitors can't access
- Network effects amplified by AI (users create data that improves AI)
- Defensible moat that strengthens over time

**Examples** (archetypal, not actual companies):
- Autonomous vehicle platform: Millions of miles of driving data → better perception model → better product → more deployments → more data
- Autonomous agent workplace platform: Thousands of users executing workflows → better workflow understanding → better automation suggestions → higher adoption → more data
- Map/navigation service: Billions of trips → better routing models → better directions → more usage → better data

**Unit Economics**:
- **COGS**: Low (mostly LLM inference + infrastructure)
- **CAC**: High initially, but decreases as product gets better (network effect)
- **Gross margin**: 60-80% (low COGS as data leverage increases)
- **Payback period**: 12-36 months (data takes time to accumulate)

**Defensibility**: **HIGH** (3-5 years if data is unique) but erodes as competitors collect similar data

**Challenges**:
- Takes years to build defensible data advantage
- Requires scale to generate meaningful data
- Privacy/regulatory risk (data ownership, privacy laws)
- Requires strong product execution (data alone isn't valuable)

**Confidence**: HIGH (proven pattern: Tesla, Waymo, DeepMind)

---

### Archetype 2: AI-as-a-Service (AIaaS)

**Core Mechanism**: Sell AI models/services to customers who lack AI expertise

**Value Drivers**:
- Proprietary model or training approach
- Ease of use + integration
- Cost savings vs. building internally
- Speed to value

**Examples**:
- LLM API platform (GPT-5.2, Claude, Gemini APIs)
- Specialized vertical models (legal document AI, medical imaging AI, financial analysis AI)
- Workflow automation platform (agents orchestrated to automate customer processes)

**Unit Economics**:
- **COGS**: Depends on sourcing
  * If you own the model: 10-20% (infrastructure costs)
  * If you license from others: 30-50% (model licensing costs)
- **CAC**: Medium ($5K-50K for enterprise, $0 for self-serve)
- **Gross margin**: 50-70%
- **Payback period**: 3-12 months (no build delay if using licensed model)

**Revenue Models**:
- **Token-based**: $X per 1M tokens (aligns incentives, but customer cost unpredictable)
- **Subscription**: $X/month per seat or organization (predictable, but customers optimize usage down)
- **Usage-based**: $X per API call or task (scales with customer value)
- **Freemium**: Free tier (limited usage), paid tier (unlimited)

**Defensibility**: **MEDIUM-LOW** (easy to commoditize, LLM providers are competition)

**Challenges**:
- LLM prices dropping 80% in 2025-2026 → margin compression
- Switching costs low (customer can use different model easily)
- Hard to build proprietary model advantage if using commodity LLMs
- Talent competition (everyone hiring ML engineers)

**Confidence**: HIGH (proven pattern: OpenAI, Anthropic, Cohere, dozens of startups)

---

### Archetype 3: AI-Enhanced Marketplace

**Core Mechanism**: Marketplace + AI matching/ranking/curation improves unit economics dramatically

**Value Drivers**:
- AI matches supply/demand better → higher utilization
- AI reduces friction → faster transactions → more volume
- AI personalizes experience → higher conversion + retention
- Network effects (more users → better matching)

**Examples**:
- E-commerce marketplace with AI recommendation + dynamic pricing
- Hiring marketplace with AI candidate matching + skill assessment
- Freelance marketplace with AI project-to-skill matching
- Real estate marketplace with AI property valuation + buyer matching

**Unit Economics**:
- **Marketplace take rate**: 2-10% (depends on category)
- **COGS**: 2-5% (mostly LLM + infrastructure for matching)
- **Gross margin**: 85-95% (platform business, high margin)
- **CAC**: $10-100 per supplier/buyer (depending on channel)

**Critical metric**: Network effects
- 2-sided network (supply + demand)
- Chicken-egg problem: Need critical mass on both sides
- AI helps by matching less-than-perfect supply to demand (reduces supply shortage)

**Defensibility**: **MEDIUM** (AI improves unit economics, but competitors can buy same LLMs; defensibility comes from network size, data, integration depth)

**Challenges**:
- Marketplace problems are hard (supply-demand imbalance, fraud, quality)
- AI is enabler, not differentiator (everyone uses similar LLMs)
- Requires existing marketplace or massive scale-up capital
- 2-sided network effects take years

**Confidence**: HIGH (proven pattern: Amazon, Uber, Airbnb using AI; but AI isn't the primary moat)

---

### Archetype 4: Autonomous Agent Platform

**Core Mechanism**: Sell infrastructure for customers to build + deploy autonomous agents for their workflows

**Value Drivers**:
- Reduce manual work (agents automate 50-70% of repetitive tasks)
- Improve consistency + compliance (agents follow rules perfectly)
- Scale without hiring (agents work 24/7, low marginal cost)
- Unlock new workflows (agents enable tasks impossible for humans at scale)

**Examples**:
- Enterprise workflow automation platform (agents for HR, finance, operations)
- Customer service agent platform (agents handle 80% of tickets automatically)
- Research agent platform (agents synthesize documents, generate insights)
- Software development agent platform (agents write code, test, deploy)

**Unit Economics**:
- **COGS**: $500-1000/month per customer (LLM tokens + infrastructure)
- **Pricing**: $5K-100K/month (depending on customer size, task complexity)
- **Gross margin**: 80-95% (infrastructure scales)
- **CAC**: $50K-200K (enterprise sales cycles long)
- **Payback**: 6-12 months

**Revenue model usually**: Subscription + per-task execution pricing
- Base: $10K/month (platform, support, infrastructure)
- Per-task: $0.10-1.00 per process execution
- Example: 100K process executions/month + base = $20K revenue/month

**Defensibility**: **MEDIUM-HIGH**
- Switching cost high once integrated (workflows, data, integrations)
- But proprietary value comes from domain knowledge (vertical specialization), not AI itself
- Need to build deep domain expertise (HR, finance, legal, etc.)

**Challenges**:
- Enterprise sales are slow (6-12 month cycles)
- Integration complexity high (need to connect to legacy systems, ERPs, APIs)
- Agent reliability isn't perfect (hallucinations, edge cases) → requires human oversight
- Talent-intensive (need AI engineers, domain experts, customer success)
- 40% of agentic AI projects expected to fail by 2027 → customer risk perception high

**Confidence**: MEDIUM (pattern emerging but still early-stage; 11% of enterprises have production agents)

---

### Archetype 5: AI Infrastructure & Tools

**Core Mechanism**: Sell developer tools, infrastructure, frameworks for building AI systems

**Value Drivers**:
- Reduce time to build AI system (abstraction, pre-built components)
- Reduce operational burden (deploy, monitor, scale)
- Reduce cost (efficient inference, caching, optimization)
- De-risk development (battle-tested patterns, best practices)

**Examples**:
- LLM ops platform (caching, routing, cost optimization)
- Agent framework (LangGraph, CrewAI abstractions)
- Vector database (Weaviate, Pinecone, Qdrant)
- Model monitoring platform (detect drift, performance degradation)
- Fine-tuning platform (infrastructure for model customization)

**Unit Economics**:
- **COGS**: 20-40% (infrastructure, bandwidth)
- **Pricing**: Freemium (free tier, paid tiers for usage)
  * Example: Free tier up to 1M tokens/month, then $0.05 per 1M additional
- **Gross margin**: 60-80% (platform business, high scale)
- **CAC**: Near-zero for developer tools (word-of-mouth, open-source)

**Developer tools typically**: Low touch, high volume, low CAC, higher churn
- Conversion: 0.1-1% of free users → paid
- ARPU (average revenue per user): $100-1000/year
- Retention: 60-80% annually (developers churn when they build competing capability)

**Defensibility**: **MEDIUM-LOW**
- Easy to commoditize (if successful, giants build similar tool)
- Lock-in low (developers use multiple tools)
- Competitive advantage: simplicity, community, integration ecosystem
- Winners: Have massive developer community (LangChain, CrewAI)

**Challenges**:
- Network effects are weaker than platforms
- Giants have infrastructure advantage (Google, Amazon, Microsoft can build similar tools)
- Revenue predictability low (free tier converts unpredictably)
- Requires large developer ecosystem to justify sales team

**Confidence**: HIGH (proven pattern: LangChain, CrewAI, Hugging Face; but hard to monetize against giants)

---

### Archetype 6: Vertical-Specific AI (Vertical SaaS + AI)

**Core Mechanism**: Industry-specific software enhanced with proprietary AI models trained on vertical data

**Value Drivers**:
- Deep domain expertise (model understands legal/medical/financial nuances)
- Pre-integrated workflows (AI baked into existing processes)
- Higher switching cost (industry-specific features harder to replicate)
- Better unit economics (domain-specific optimization reduces LLM costs)

**Examples**:
- Legal tech platform with AI contract analysis, risk assessment
- Medical imaging platform with AI diagnostics
- Financial analysis platform with AI market modeling
- Real estate platform with AI valuation
- HR platform with AI candidate matching, assessment

**Unit Economics**:
- **COGS**: 5-15% (specialized models more efficient)
- **Pricing**: $500-10K/month per customer (vertical SaaS standard)
- **Gross margin**: 70-85%
- **CAC**: $5K-50K (sales team for industry)
- **Payback**: 3-9 months

**Defensibility**: **HIGH**
- Domain expertise is moat (hard to replicate)
- Data advantage (domain-specific training data)
- Switching cost high (industry workflows, integrations, compliance)
- Customer lock-in strong (critical to business process)

**Challenges**:
- TAM is smaller (only one industry)
- Regulatory complexity (especially healthcare, finance, legal)
- Product requirements complex (industry experts on team)
- Talent intensive (need domain experts + AI engineers)

**Confidence**: HIGH (proven pattern: many successful vertical SaaS companies; AI just amplifies existing advantages)

---

## PART 2: AI-NATIVE VS. AI-ENHANCED DECISION MATRIX

### AI-Native Business Models
Models where **AI is the core value mechanism**. If you remove AI, the business collapses.

| Archetype | Primary Value | When to Choose | Investment | Timeline | Risk |
|-----------|---------------|---|---|---|---|
| **Data Flywheel** | Proprietary data edge | Have unique data asset or can build it at scale | $5-50M | 24-36 months | HIGH (long payoff) |
| **Autonomous Agent** | Labor automation | Enterprise willing to adopt agents (2026: low) | $2-10M | 12-18 months | MEDIUM-HIGH |
| **Vertical AI** | Domain expertise | Deep industry knowledge, regulatory tailwind | $1-5M | 9-15 months | MEDIUM |

### AI-Enhanced Business Models
Models where **AI is a significant enhancement** but the business would still work without it (slower, lower quality, higher cost).

| Archetype | Primary Value | When to Choose | Investment | Timeline | Risk |
|-----------|---------------|---|---|---|---|
| **AIaaS** | Model commoditization | Have proprietary model or significant cost advantage | $0-5M | 3-6 months | MEDIUM |
| **Marketplace + AI** | Matching efficiency | Already have 2-sided network | $0-2M | 6-12 months | LOW-MEDIUM |
| **Vertical SaaS + AI** | Feature enhancement | Existing vertical SaaS with customer base | $0-1M | 3-6 months | LOW |

### Decision Rule
- **If AI is required for product to exist**: AI-native (architectures 1-3)
- **If business works without AI but AI dramatically improves it**: AI-enhanced (add AI to existing business)
- **When in doubt**: Start AI-enhanced (lower risk, faster time to value, easier to iterate)

---

## PART 3: REVENUE MODEL PATTERNS FOR AI COMPANIES

### Revenue Model Decision Tree

```
What are you selling?
├─ Models / API access?
│  ├─ Token-based pricing (GPT-5.2 model: $1.75/$14 per 1M input/output tokens)
│  ├─ Subscription + usage (base fee + per-task)
│  └─ Pure subscription (flat monthly)
│
├─ Agent services / automation?
│  ├─ Subscription + per-execution ($10K/month + $0.50 per process)
│  ├─ Outcome-based (% of cost savings)
│  └─ SaaS subscription ($100-1K per user/month)
│
├─ Infrastructure / developer tools?
│  ├─ Freemium (free tier + paid tier)
│  ├─ Usage-based (per API call, per token)
│  └─ Subscription (per seat, per org)
│
└─ Vertical SaaS?
   └─ Subscription (industry standard $500-10K/month)
```

### 1. Token-Based Pricing

**How it works**: Charge per LLM token consumed (input + output)

**Pricing examples** (see model-economics-config.json for current rates as of 2026-03-10):
- GPT-5.2: $1.75/1M input, $14/1M output
- Claude Opus: $5/1M input, $25/1M output
- Llama 4 Scout: $0.40/1M both directions
- Average mixed workload: 80% input, 20% output tokens

**When to use**:
- Selling direct access to models (LLM API, research APIs)
- Offering to developers who care about efficiency
- Business model where customer consumption varies wildly

**Pros**:
- ✓ Simple (customers understand "you pay for what you use")
- ✓ Scales with customer value (more usage = more value = more revenue)
- ✓ Good for LLM providers (incentivizes efficiency)

**Cons**:
- ✗ Customer cost unpredictable (customer doesn't know monthly bill until month-end)
- ✗ Customer incentivizes compression (use cheaper models, fewer tokens)
- ✗ Margin compression if token prices drop (and they are dropping 80% in 2-3 years)
- ✗ Customers game the system ("batch processing to reduce API calls")

**Unit economics example**:
- Customer: 100M tokens/month
- Your cost (Llama 4): 100M × $0.40 = $40/month
- Your price: $1.75/1M input average = $175/month
- Gross margin: $135/$175 = 77%
- But: If you used Claude Opus ($5/1M = $500/month), margin flips negative

**Recommendation**: Use token pricing only if:
1. You own the model (so cost is stable), OR
2. You can pass through cost adjustments to customers, OR
3. You've built usage-compression tech that's defensible

---

### 2. Subscription + Per-Execution (Hybrid)

**How it works**: Base monthly fee for platform + per-task execution cost

**Example**:
- Base: $10K/month (platform, infrastructure, support)
- Per-execution: $0.50 per process run
- Customer: 5K processes/month
- Total: $10K + $2.5K = $12.5K/month

**When to use**:
- Selling agent platforms or automation services
- Customer consumption varies (some months 1K processes, some 10K)
- Want predictable revenue (base) + upside (variable)

**Pros**:
- ✓ Predictable base revenue (budget planning)
- ✓ Upside on execution (high-volume customers pay more)
- ✓ Customers feel incentivized (if they use more, they're getting value)
- ✓ Scales with customer success

**Cons**:
- ✗ Customers perceive as "double charging" (base + variable)
- ✗ Complexity (customers hate hybrid pricing)
- ✗ Customer needs to forecast execution volume (hard)
- ✗ Conversion takes longer (complex pricing = longer sales)

**Margin implications**:
- High-usage customer: Base $10K + 100K executions × $0.50 = $60K/month (80%+ margin if cost <$2/exec)
- Low-usage customer: Base $10K + 1K executions × $0.50 = $10.5K/month (unprofitable if cost >$8/exec)

**Recommendation**: Use if execution volume varies >10x across customers (heterogeneous usage) and you want to capture upside

---

### 3. Pure Subscription

**How it works**: Flat monthly or annual fee, unlimited usage (or generous limits)

**Examples**:
- AI copilot: $20/month per user (unlimited use)
- Enterprise automation platform: $50K/month (unlimited agents, processes)
- Vertical SaaS: $5K/month (unlimited documents, transactions)

**When to use**:
- Usage patterns are similar across customers (predictable)
- You want to reduce sales friction (simple pricing)
- You're willing to absorb variable costs in margin

**Pros**:
- ✓ Simple (customers like flat fees)
- ✓ Predictable revenue (annual contracts)
- ✓ High retention (switching cost psychological)
- ✓ Supports expansion revenue (upsell to higher tiers)

**Cons**:
- ✗ Margin risk if usage spikes (your cost goes up, revenue flat)
- ✗ Need to forecast usage accurately (if wrong, you lose margin)
- ✗ Heavy users subsidize light users

**Margin implications**:
- Assumption: Average customer uses 50K processes/month
- Your cost: 50K × $0.10 = $5K/month (includes LLM, infrastructure, support)
- Your price: $20K/month
- Gross margin: 75%
- But: If customer actually uses 200K processes/month (4x), margin drops to 25%

**Recommendation**: Use only if:
1. You've validated usage patterns are consistent (90%+ customers within 2x of mean), AND
2. Your cost structure scales linearly (LLM costs), AND
3. You can lock in LLM prices (don't want commodity price drops to crush margin)

---

### 4. Outcome-Based / Revenue Sharing

**How it works**: Customer pays based on value delivered (% of cost savings, ROI)

**Examples**:
- Agent handles customer service: "We take 20% of the cost savings"
- Financial AI suggests better investments: "We take 1% of outperformance"
- Hiring AI finds better candidates: "We take $10K per hire that lasts >1 year"

**When to use**:
- ROI is clear and measurable
- Customer is risk-averse ("prove value before we pay")
- You're highly confident in your AI's performance

**Pros**:
- ✓ Perfectly aligns incentives (you win when customer wins)
- ✓ High trust (you're betting on your product)
- ✓ Can capture massive upside (if AI delivers $1M value, you get % of that)

**Cons**:
- ✗ Revenue unpredictable (depends on customer implementation, not your AI)
- ✗ Hard to measure (how do we count "cost savings"?)
- ✗ Customer disputes common ("We don't think your AI caused that value")
- ✗ Long sales cycles (need to model ROI together)
- ✗ Cash flow bad (you deliver value, get paid months/years later)

**Unit economics risk**:
- If your AI doesn't deliver, you get nothing
- If customer implements poorly, you get penalized
- Salespeople struggle (hard to forecast)

**Recommendation**: Use outcome-based only if:
1. ROI is objectively measurable (hard to dispute), AND
2. Your AI is proven to drive that ROI (you've validated with 3+ similar customers), AND
3. You can afford cash flow risk (venture-backed or profitable elsewhere)

---

## PART 4: UNIT ECONOMICS FRAMEWORK FOR AI BUSINESSES

### Core Metrics

**1. Cost of Goods Sold (COGS)**

> **[GENERATED FROM CONFIG]** The agent should read `model-economics-config.json` and render current COGS calculations. The following static snapshot was accurate as of 2026-03-10:

Breaking down COGS for AI businesses (different than traditional SaaS):

| Component | AI-Native Estimate | Notes |
|-----------|---|---|
| **LLM costs** | 5-20% of revenue | Varies: Llama 4 ($0.40/M) vs Claude ($5/M) vs GPT-5.2 ($1.75/M input) |
| **Infrastructure** | 5-10% | Compute, storage, bandwidth for hosting, retrieval (RAG), vector DB |
| **Data acquisition** | 2-5% | Training data curation, labeling if building proprietary data |
| **Support/ops** | 5-15% | Human-in-the-loop, incident response, customer support |
| **R&D** | 10-20% | Prompt optimization, model fine-tuning, safety/governance |
| **Total COGS** | **27-70%** | **Depends on architecture** |

**Typical breakdown by archetype**:
- AIaaS (token-based): 30-40% COGS (cheap LLM, scale infrastructure)
- Autonomous agent: 40-60% COGS (human oversight, infrastructure, support)
- Vertical SaaS + AI: 25-35% COGS (leverages SaaS infrastructure)
- Data flywheel: 10-20% COGS (scale improves margin)

---

### Gross Margin Target by Archetype

| Archetype | Target Margin | Achievable? | Notes |
|-----------|---|---|---|
| **AIaaS (commodity models)** | 60-70% | YES | If you can optimize LLM costs + infrastructure |
| **Autonomous agents** | 70-80% | MEDIUM | Achievable at scale, but support costs high initially |
| **Vertical SaaS + AI** | 75-85% | YES | Leverage existing SaaS margins, AI is incremental |
| **Data flywheel** | 85-95% | MEDIUM-TERM | High margin at scale, but requires years to reach scale |
| **Infrastructure/tools** | 60-75% | YES | Platform margins if you can get scale |

**Red flags** (margin concerns):
- [ ] LLM costs >20% of revenue (architecture not optimized, or model choice wrong)
- [ ] Support costs >15% of revenue (customer expectations mismanaged, AI unreliable)
- [ ] Infrastructure costs >10% (inefficient design or lacking optimization)
- [ ] Target margin <50% for SaaS (not enough leverage)

---

### Customer Acquisition Cost (CAC) & Payback Period

**CAC by go-to-market channel**:

| Channel | CAC | Payback Period | Notes |
|---------|-----|---|---|
| **Self-serve / freemium** | $0-100 | Month 1-3 | Works for low-ACV products ($100-1K/year) |
| **Inside sales** | $500-5K | 3-6 months | SMB targeting, ACV $10-50K/year |
| **Field sales** | $5K-50K | 6-12 months | Enterprise, ACV $50K-500K/year |
| **Partnerships** | $500-2K | 2-4 months | Via marketplace, reseller; lower control |
| **Community/viral** | $0-500 | Month 1 | IF product has viral coefficient >1 |

**Payback calculation**:
- Example: Customer pays $1K/month, gross margin 70% = $700/month contribution
- CAC = $5K (inside sales)
- Payback = $5K / $700 = 7.1 months
- ✓ Acceptable if annual retention >85% (breaks even year 1)

**CAC targets for different business models**:
- Freemium: Payback <1 month (need massive conversion)
- SMB SaaS: Payback 3-9 months
- Enterprise SaaS: Payback 12-24 months (acceptable, longer sales cycles)
- Marketplace: Payback 6-12 months (2-sided acquisition cost)

**Red flag**: Payback >24 months (not enough runway for 3 years growth)

---

### Retention & Expansion Revenue

**Critical for profitability**:

| Metric | Target | Implication |
|--------|--------|---|
| **Annual Churn Rate** | <10% | Retain 90%+ of revenue year-over-year |
| **Net Dollar Retention** | >110% | Expansion revenue (upsell + cross-sell) offsets churn |
| **Payback Period** | <12 months | Break even on CAC in year 1, profit in year 2+ |

**Example**: Cohort economics

- **Month 1**: 10 customers × $1K = $10K (acquire for $5K CAC × 10 = $50K spend)
- **Month 1-12**: Gross margin 70% = $7K revenue per customer/year
- **Year 1 contribution**: 10 customers × $7K = $70K (vs. $50K CAC spend) = +$20K
- **Year 2**: If 90% retention (9 customers) + 20% expansion (new cohort) = 10.8 customers
  * Revenue: 10.8 × $7K = $75.6K
  * Acquisition cost: Only for new customers (0.8 × $5K = $4K)
  * Contribution: $75.6K - $4K = $71.6K
  * Compounding proves profitability

---

## PART 5: VALUE CHAIN TRANSFORMATION WITH AI

Understanding where AI creates value in your business:

### Pre-AI Value Chain
```
Demand generation → Sales → Delivery → Support → Renewal
                                        ↓
                            (Expensive, inefficient)
```

### Post-AI Value Chain
```
Demand generation (AI content) → Sales (AI qualification) → Delivery (AI automation) → Support (AI triage) → Renewal (AI expansion)
                                       ↓                          ↓                      ↓                    ↓
                              (40% faster)              (60% faster)            (70% resolution)    (20% higher NRR)
```

**Value creation by stage**:

1. **Demand Generation**: AI content generation, personalization, lead scoring
   - Value: 30-50% reduction in demand gen cost
   - Example: Generate 1000 personalized emails with AI (vs 100 manual)

2. **Sales**: AI qualification, proposal generation, deal analysis
   - Value: 40% faster sales cycle, 20% higher win rate
   - Example: Qualify leads overnight with AI scoring

3. **Delivery**: Automation, process optimization, proactive support
   - Value: 60% faster delivery, 30% cost reduction
   - Example: Onboard customer in days with AI automation vs weeks manual

4. **Support**: AI triage, first-contact resolution, escalation
   - Value: 70% of issues resolved by AI, 40% cost reduction
   - Example: Handle 5000 support tickets with 3 AI agents vs 50 humans

5. **Renewal**: Expansion recommendations, health scoring, proactive outreach
   - Value: 20% higher Net Dollar Retention, 30% reduction in churn
   - Example: Predict churn 6 months ahead, intervene proactively

---

## PART 6: BUSINESS MODEL CANVAS FOR AI-NATIVE COMPANIES

### Template

```
┌─────────────────────────────────────────────────────────────────┐
│                    BUSINESS MODEL CANVAS                         │
│                                                                  │
│ Key Partners    │  Key Activities   │  Value Proposition │ Customer│ Customer
│                 │                   │                     │Segments│ Relations
│ - LLM vendor    │ - Model training  │ - Reduce time by   │ - Ent- │ - Embedded
│ - Data          │ - Prompt eng      │   60%              │  erpri │   support
│   sources       │ - Integration     │ - Cost down 40%    │   se   │ - Community
│ - Infrastructure│ - Monitoring      │                     │ - Mid  │ - Support
│                 │                   │                     │  market│ - Onboarding
│
│                 │                   │                     │        │ Key Resources
├────────────────┼───────────────────┼─────────────────────┼────────┼──────────────┤
│ Channels        │                   │                     │        │ - AI engineers
│ - Direct sales  │                   │                     │        │ - Data
│ - Marketplace   │                   │                     │        │ - Infrastructure
│ - Community     │                   │                     │        │ - Models
│
│                 │   REVENUE STREAMS                       │        │
│                 │   - Subscription: $50K/mo              │        │
│                 │   - Per-execution: $0.50/process      │        │
│                 │   - Professional services: $200/hr     │        │
│                 │                                         │        │
│                 │   COST STRUCTURE                        │        │
│                 │   - LLM costs: 15% of revenue         │        │
│                 │   - Infrastructure: 8% of revenue     │        │
│                 │   - Support: 12% of revenue           │        │
│                 │   - R&D: 20% of revenue               │        │
│
└─────────────────────────────────────────────────────────────────┘
```

---

## PART 7: AI-NATIVE COMPANY FINANCIAL PROJECTIONS (3-YEAR)

### Scenario: Autonomous Agent Platform for Enterprise Automation

**Year 1**: Build + Pilot
- Customers: 5 (early adopters)
- ACV: $50K (weighted: 3 × $30K, 2 × $100K)
- ARR: $250K
- Revenue: $100K (acquired Q3-Q4, partial year)
- Costs:
  * Team: $1.2M (CEO, CTO, 2 AI eng, 1 PM, 1 sales)
  * Infrastructure: $100K
  * LLM/ops: $50K
  * Total: $1.35M
- Gross Margin: -$1.25M (investments phase)

**Year 2**: Growth
- Customers: 25 (5 from Y1 + 20 new)
- ACV: $60K (enterprise adoption, more features)
- ARR: $1.5M
- Revenue: $1.5M
- Costs:
  * Team: $2M (add 1 AI eng, 1 customer success, 1 operations)
  * Infrastructure: $300K (scale)
  * LLM/ops: $150K
  * Total: $2.45M
- Gross Margin: -$950K (still investment, but revenue growing)
- ← Critical checkpoint: unit economics prove out, CAC payback <12 months?

**Year 3**: Scale
- Customers: 75 (organic growth 200%, less new sales needed)
- ACV: $75K (expansion revenue, features, automation depth)
- ARR: $5.6M
- Revenue: $5.6M
- Costs:
  * Team: $3M (add 2 more AI engineers, customer success team, 2 sales)
  * Infrastructure: $500K
  * LLM/ops: $400K (scale improves efficiency)
  * Total: $3.9M
- Gross Margin: $1.7M (30% margin, path to profitability)

### Key Milestones
- [ ] Month 12: Unit economics proven (CAC payback <12 months)
- [ ] Month 18: Product-market fit (NPS >50, retention >90%)
- [ ] Month 24: Profitability path clear (gross margin >50%)
- [ ] Month 36: Gross margin >60%, ready for scale financing

---

## DECISION CHECKLIST: WHICH MODEL FOR YOUR COMPANY?

- [ ] **AI-Native?** Does your product require AI to exist?
  - YES → Choose archetype (1-3 above)
  - NO → AI-Enhanced model

- [ ] **Data Flywheel?** Do you have unique data or can you build it at scale?
  - YES → Requires 24-36 month investment, high risk, high reward
  - NO → Choose different archetype

- [ ] **TAM (Total Addressable Market)?** How many potential customers?
  - >$10B TAM → Can support large platform investments (infrastructure, vertical)
  - $1-10B TAM → Focus on vertical specialization or niche
  - <$1B TAM → Must be extremely efficient (developer tools model)

- [ ] **CAC payback period?** Can you acquire customers in <12 months of gross margin?
  - YES → Viable business
  - NO → Reconsider pricing, customer segment, or cost structure

- [ ] **Competitive defensibility?** What makes you better than competitors 2-3 years from now?
  - Data → Data flywheel model
  - Distribution → Marketplace or vertical SaaS
  - Talent → Research lab / proprietary models
  - Domain → Vertical specialization
  - Speed → Fast follower (be better at execution, not innovation)

- [ ] **Gross margin trajectory?** Can you reach 70%+ margin at scale?
  - YES → Pursue
  - NO → Rethink model (too commodity, wrong architecture)

---

**Last Updated**: March 2026
**Reference**: SKILL.md Phase 1 (AI Business Model Design)
