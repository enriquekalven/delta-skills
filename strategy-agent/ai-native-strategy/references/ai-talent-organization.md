# AI Talent Strategy & Organizational Design

## Executive Summary

Building AI capabilities requires the right people. 2026 is characterized by:
- **Agentic Engineer shortage**: $206K+ salaries, 40% of positions unfilled
- **Rapid skill obsolescence**: Knowledge from 2024 is partially outdated
- **Talent concentration**: Top talent concentrated in 50-100 companies globally
- **Organizational fragmentation**: No consensus on optimal AI team structure

This reference provides team archetypes, role taxonomy, compensation benchmarks, and scaling strategies.

---

## PART 1: AI TEAM ARCHETYPES

### Archetype 1: Centralized Center of Excellence (CoE)

**Structure**:
```
┌─ CTO / SVP ─┐
│             │
└─ Director of AI
   ├─ Senior AI Architect
   ├─ AI Engineer (2-3)
   ├─ ML Ops Engineer
   ├─ AI Product Manager
   └─ AI Ethics Officer (0.5 FTE)
```

**Staffing**:
- **Director of AI**: Reports to CTO, strategy + governance + external relationships
- **Senior AI Architect**: System design, technology selection, architecture reviews
- **AI Engineers**: 2-4 who build POCs, ship products, mentor
- **ML Ops Engineer**: Infrastructure, deployment, monitoring
- **AI Product Manager**: Roadmap, success metrics, stakeholder management
- **AI Ethics Officer**: Part-time, governance, risk assessment

**Budget**: $1.2-1.8M/year (fully loaded)

**Best For**:
- Large enterprises (>$1B revenue)
- Homogeneous AI needs (similar use cases across company)
- Strong governance requirements (regulated industry)
- Centralized technology decisions

**Pros**:
- ✓ Economies of scale (shared infrastructure, knowledge)
- ✓ Knowledge concentration (all expertise in one place)
- ✓ Consistent standards (architecture, security, governance)
- ✓ Easy to measure ROI (separate P&L)
- ✓ Risk management (governance oversight)

**Cons**:
- ✗ Bureaucratic (slower decision-making)
- ✗ Siloed from business (loses context, customer insight)
- ✗ Lower speed to value (business units wait for CoE)
- ✗ Risk of irrelevance (business units start building AI themselves)

**Typical Ramp** (first 18 months):
- **Month 0**: Hire director, architect
- **Month 1-2**: Hire 2 AI engineers, ML ops
- **Month 3**: Hire AI product manager
- **Month 6**: 3rd AI engineer, part-time ethics officer
- **Month 9**: Consider second architect if scale demands
- **Month 12-18**: Build customer success, expand team based on demand

**Common Pitfall**: Hiring director but no senior engineers → Director becomes IC (individual contributor) → Frustration → Departure

---

### Archetype 2: Federated Model

**Structure**:
```
┌─ Business Unit A ──┐
│  AI Engineer (2)   │
└────────────────────┘

┌─ Business Unit B ──┐
│  AI Engineer (2)   │
└────────────────────┘

┌─ Business Unit C ──┐
│  AI Engineer (1)   │
└────────────────────┘

(Loose coordination via Guild, not formal reporting)
```

**Staffing**: 5-10 AI engineers distributed across units + 1 architect for governance

**Budget**: $800K-1.5M/year

**Best For**:
- Decentralized organizations
- Diverse business units with different AI needs
- Speed-focused (each unit moves independently)
- Companies that already distribute engineering

**Pros**:
- ✓ Fast execution (no central bottleneck)
- ✓ Business-aligned (AI engineers embedded with stakeholders)
- ✓ High local ownership (engineers feel part of business unit)
- ✓ Can hire specialists (one unit needs LLM expert, hires them directly)

**Cons**:
- ✗ Fragmentation (each unit builds different solutions)
- ✗ Knowledge silos (teams don't share learnings)
- ✗ Reinvention (teams solve same problem 3 different ways)
- ✗ Hard to maintain standards (inconsistent security, monitoring)
- ✗ Coordination overhead (governing decentralized teams is hard)

**Common Pitfall**: Teams go rogue, don't follow company standards → Security/compliance issues → Crisis

---

### Archetype 3: Hub-and-Spoke Hybrid

**Structure**:
```
┌─ Central Hub ─────────────────────┐
│ - AI Architect                     │
│ - 3 Senior AI Engineers (core)    │
│ - Shared ML Ops                    │
│ - AI Product Manager               │
└────────────┬──────────────────────┘
             │
      ┌──────┼──────┬──────┐
      │      │      │      │
   ┌──▼───┐ ┌──▼───┐ ┌──▼───┐
   │Unit A│ │Unit B│ │Unit C│
   │(embed)│ │(embed)│ │(embed)│
   └──────┘ └──────┘ └──────┘
   1-2 AI   1-2 AI   1 AI
   engineers engineers engineer
   (Spoke)  (Spoke)  (Spoke)
```

**Staffing**:
- Core hub: 5-8 senior engineers + architect
- Spokes: 3-5 embedded engineers in key business units
- Governance: 1 architect for standards

**Budget**: $1M-1.5M/year

**Best For**:
- Medium-large enterprises
- Mix of homogeneous (central) + specialized (spokes) needs
- Balance of speed and standards
- Want both efficiency and business alignment

**Pros**:
- ✓ Best of both worlds (central efficiency + local speed)
- ✓ Flexible scaling (add spokes as needed)
- ✓ Knowledge sharing (hub is central)
- ✓ Standards maintained (architect oversees all)
- ✓ Business-aligned (spokes embedded in units)

**Cons**:
- ✗ Complex org design
- ✗ Coordination overhead (hub ↔ spokes + spoke ↔ spoke)
- ✗ Can be confusing (unclear ownership, reporting)
- ✗ Requires strong architect to hold it together

**When to use**: If you have:
- 2-3 core AI use cases (banking hub) + 5-10 business units with specialized needs (spokes)
- $1B+ revenue
- Want to balance scale and speed

---

## PART 2: ROLE TAXONOMY & COMPENSATION (2026)

### Role 1: AI Engineer

**Primary responsibility**: Full-stack AI products (end-to-end: data → model → deployment → monitoring)

**Key skills**:
- LLM expertise (prompt engineering, fine-tuning)
- Python, basic ML (PyTorch, TensorFlow)
- Deployment (Docker, APIs, cloud)
- Data wrangling

**Experience required**: 2-5 years (can be growth role for engineers from other domains)

**2026 Compensation**:
- **Salary**: $140-180K (base)
- **Bonus**: 15-20%
- **Equity**: 0.05-0.15% (if startup), or stock grants if public company
- **Total comp**: $160-220K

**Scarcity**: MEDIUM (not as scarce as agentic engineers, but undersupply)

**Hiring**: Can come from:
- Data science background
- Software engineering + ML course
- ML engineering with product skills

---

### Role 2: ML Engineer

**Primary responsibility**: Classical ML, training pipelines, model optimization

**Key skills**:
- PyTorch, TensorFlow, scikit-learn
- Data pipelines (Spark, Airflow)
- Model training, hyperparameter tuning
- A/B testing, experimentation

**Experience required**: 3-7 years (deeper than AI engineer)

**2026 Compensation**:
- **Salary**: $150-200K
- **Bonus**: 15-20%
- **Equity**: 0.05-0.2%
- **Total comp**: $180-250K

**Scarcity**: LOW-MEDIUM (more supply than agentic engineers)

**Note**: This role is becoming less critical as foundation models dominate. Traditional ML engineer is becoming niche.

---

### Role 3: Agentic Engineer ⭐ (HOTTEST ROLE 2026)

**Primary responsibility**: Multi-agent systems, orchestration, reasoning patterns, production deployment

**Key skills**:
- Multi-agent architecture design
- LLM frameworks (LangGraph, CrewAI, Claude Agent SDK)
- Reasoning patterns (ReAct, Plan-and-Execute, Tree of Thoughts)
- System design (routing, coordination, failure handling)
- Production ops (monitoring, incident response)

**Experience required**: 3-8 years (usually: 5+ years ML/SWE, 1-2 years in multi-agent)

**2026 Compensation** (SHORTAGE-DRIVEN):
- **Salary**: $180-250K (median $206K)
- **Bonus**: 20-30%
- **Equity**: 0.1-0.5% (for startups desperate to hire)
- **Sign-on bonus**: $50-150K (common)
- **Total comp**: $250-400K+

**Scarcity**: **CRITICAL SHORTAGE**
- Only ~1000-2000 globally with production agentic experience
- Demand: 1000s of companies hiring
- Result: Extreme wage inflation, high mobility

**Hiring**: Hard
- Most 2024-2025 hires were at startups
- Can't retrain from traditional ML (different skillset)
- Need to hire 2 junior/mid-level + mentor heavily

**Retention**: Hard
- 18-24 month average tenure (startups pull them away)
- Mitigation: equity refresh, internal startup programs, clear career path

---

### Role 4: ML Ops Engineer

**Primary responsibility**: Infrastructure, deployment, monitoring for ML systems

**Key skills**:
- Kubernetes, Docker, cloud infrastructure
- Monitoring, alerting, incident response
- CI/CD for ML (MLflow, Weights & Biases)
- Cost optimization

**Experience required**: 3-6 years

**2026 Compensation**:
- **Salary**: $140-190K
- **Bonus**: 15-20%
- **Equity**: 0.05-0.1%
- **Total comp**: $160-230K

**Scarcity**: MEDIUM (fewer than ML engineers, but solid supply)

---

### Role 5: AI Product Manager

**Primary responsibility**: AI feature roadmap, user research, success metrics

**Key skills**:
- Understanding of AI capabilities and limitations
- User research, market understanding
- Metrics definition and tracking
- Executive communication

**Experience required**: 5-10 years (usually from traditional product management)

**2026 Compensation**:
- **Salary**: $160-210K
- **Bonus**: 20-30%
- **Equity**: 0.1-0.25%
- **Total comp**: $200-270K

**Scarcity**: MEDIUM-HIGH (fewer PM trained in AI)

---

### Role 6: AI Ethics Officer ⭐ (NEW ROLE)

**Primary responsibility**: Responsible AI, governance, compliance (especially EU AI Act)

**Key skills**:
- AI safety and ethics
- Regulatory knowledge (EU AI Act, emerging frameworks)
- Risk assessment, responsible AI best practices
- Board communication

**Experience required**: Varies (can hire ethicist from academia, or train lawyer/compliance officer)

**2026 Compensation**:
- **Salary**: $140-200K
- **Bonus**: 15-20%
- **Equity**: 0.05-0.15%
- **Total comp**: $160-240K

**Scarcity**: HIGH (very new role, few qualified candidates)

**Why now?**: EU AI Act deadline August 2026 → Regulatory risk → Need ethics expertise

---

### Role 7: Prompt Engineer (COMMODITIZING)

**Primary responsibility**: Prompt optimization, evaluation, edge case handling

**Key skills**:
- Deep understanding of LLM capabilities
- Iterative prompt refinement
- A/B testing prompts
- Cost optimization

**Experience required**: 1-3 years

**2026 Compensation**:
- **Salary**: $100-150K (declining)
- **Bonus**: 10-15%
- **Equity**: 0.02-0.05%
- **Total comp**: $110-175K

**Scarcity**: LOW (commoditizing as prompt engineering becomes easier)

**Note**: This role is being replaced by automated prompt optimization tools. Bounty model emerging ($50-500 per prompt optimization, not full-time).

---

## PART 3: TALENT ACQUISITION STRATEGY FOR AI ROLES

### Sourcing Channels

**University / PhD Programs** (for early-career talent):
- Top AI schools: CMU, Stanford, Berkeley, MIT, Toronto, Cambridge, Oxford
- Acquisition cost: $100K-200K (internships → conversion)
- Timeline: 6-12 months (full recruitment cycle)
- Success rate: 30-50% (many go to startups, big tech)

**Tech Companies** (poaching experienced talent):
- Google, Meta, OpenAI, Anthropic, DeepSeek, Microsoft, Apple
- Acquisition cost: $300-500K (sign-on bonus to overcome staying)
- Timeline: 3-6 months (competing offer cycle)
- Success rate: 20-30% (top tech pays well)

**AI Startups** (mid-career):
- Founders, early employees leaving startups
- Acquisition cost: $150-300K (signing + equity)
- Timeline: 2-4 months
- Success rate: 50-70% (startup risk fatigue)

**Retraining Programs** (engineers → AI):
- Software engineers, data engineers transitioning to AI
- Cost: $200K salary + training + ramp time (low productivity for 6 months)
- Timeline: 9-15 months (learning + becoming productive)
- Success rate: 50% (not all engineers succeed in AI)
- Best for: Large companies with existing engineer base

**Community / Open Source** (for younger talent):
- Kaggle competitors, open-source contributors
- Cost: $0-50K (you find them, no recruiter)
- Timeline: 2-4 months
- Success rate: 70% (highly motivated, self-selected)
- Best for: Developer tools, open-source companies

---

### Agentic Engineer Acquisition (Special Case)

**Challenge**: Only ~1000-2000 globally, high demand

**Strategy 1: Hire senior + train junior** (Recommended)
- Hire 1-2 senior agentic engineers (from startups, big tech)
- They mentor 3-5 junior/mid-level engineers
- 12-18 months to build internal capability
- Cost: $250K (senior) + $150K x 3-5 (junior) = $700K-950K

**Strategy 2: Partner with specialist firm** (Interim solution)
- Hire consulting firm to build initial agentic system
- Learn from them, train internal team
- Cost: $500K-2M for 3-6 month engagement
- Advantage: Faster time-to-value, learning transfer

**Strategy 3: Acquire startup** (Expensive but fast)
- Acquire agentic AI startup with 3-5 engineers
- Cost: $5-20M depending on stage + traction
- Advantage: Instant team, expertise, tech
- Disadvantage: Cultural integration, retention risk

---

## PART 4: UPSKILLING FRAMEWORK

### Level 1: AI-Aware (All employees)

**Objective**: Everyone understands what AI can/can't do, sees opportunities

**Content**:
- What is machine learning? (30 min video)
- What is generative AI? (30 min video)
- How do LLMs work? (1 hour video)
- AI limitations & hallucinations (30 min)
- How AI affects your job (30 min discussion)
- Identifying AI opportunities in your work (1 hour workshop)

**Effort**: 8 hours total

**Timeline**: 2 weeks

**Success metric**: Employees can articulate what AI is, identify 1-2 opportunities in their role

**Cost**: $0-500/person (online course + time)

**Delivery**: Online course (Coursera, LinkedIn Learning) + 1-hour team discussion

---

### Level 2: AI-Literate (Business stakeholders, product managers, strategy)

**Objective**: Understand AI capabilities, tradeoffs, business implications

**Content**:
- Deep dive on LLM capabilities (2 hours)
- Fine-tuning vs. prompt engineering tradeoffs (1 hour)
- Cost economics of AI (1 hour)
- Responsible AI + compliance (1 hour)
- Case studies: Real deployments, failures, successes (2 hours)
- Hands-on: Prompt engineering workshop (2 hours)
- AI strategy + business model implications (2 hours)

**Effort**: 40 hours total

**Timeline**: 8-12 weeks (2-3 hours/week)

**Success metric**: Can brief executives on AI tradeoffs, make informed investment decisions

**Cost**: $5K-10K/person (course + instructor time)

**Delivery**: Mix of self-paced (online) + instructor-led (workshops)

---

### Level 3: AI-Proficient (Engineers building AI products)

**Objective**: Ship AI features, understand architecture, optimize costs

**Content**:
- LLM APIs and frameworks (3 hours)
- Building with Claude, GPT-5.2, Llama (hands-on, 4 hours)
- Prompt engineering at scale (2 hours)
- Fine-tuning decisions and implementation (3 hours)
- Retrieval-Augmented Generation (RAG) patterns (2 hours)
- Multi-agent orchestration (4 hours)
- Cost optimization strategies (2 hours)
- Safety, monitoring, evaluation (3 hours)
- Real-time debugging (1 hour)
- Building production AI systems (hands-on, 5 hours)
- Learning from failures (2 hours)

**Effort**: 200 hours total (mix of self-paced + hands-on projects)

**Timeline**: 6-12 months (5-10 hours/week + project work)

**Success metric**: Can architect simple AI system, ship to production, optimize costs, debug issues

**Cost**: $15K-30K/person (course + mentoring + project time)

**Delivery**: Online course + hands-on projects + mentoring from senior engineer

**Note**: 50% of engineers at this level should be from internal retraining (your engineers), 50% hired

---

### Level 4: AI-Native (AI architects, researchers, founding engineers)

**Objective**: Design cutting-edge agentic systems, navigate novel territory

**Content**:
- Research papers deep-dives (20 hours)
- Advanced architectures: Multi-agent, hierarchical (10 hours)
- Reasoning strategies: ToT, Reflexion, novel approaches (5 hours)
- Safety + alignment (5 hours)
- Building systems that haven't been built before (hands-on, 20 hours)
- Teaching and mentoring (20 hours)
- Contributing to open-source or publishing (20 hours)

**Effort**: 500+ hours (multi-year journey)

**Timeline**: 18-36 months

**Success metric**: Can design novel agentic systems, mentor others, contribute to field

**Cost**: $50K-150K+ (salary for 1-3 years of research/learning)

**Delivery**: Self-directed learning + mentoring + research projects + publication

**Note**: Can't really "train" someone to Level 4. You hire them or grow them over years.

---

## PART 5: COMPENSATION BENCHMARKS (2026)

### Base Salary by Role and Experience

| Role | 2-3 yrs | 3-5 yrs | 5-8 yrs | 8+ yrs |
|------|---------|---------|---------|--------|
| **AI Engineer** | $120-140K | $140-160K | $160-180K | $180-200K |
| **ML Engineer** | $130-150K | $150-170K | $170-190K | $190-210K |
| **Agentic Engineer** | N/A | $180-220K | $220-280K | $280-350K+ |
| **ML Ops Engineer** | $120-140K | $140-160K | $160-180K | $180-200K |
| **AI Product Manager** | $140-160K | $160-190K | $190-220K | $220-250K |
| **AI Ethics Officer** | $120-140K | $140-170K | $170-200K | $200-230K |

### Total Compensation (Salary + Bonus + Equity)

| Role | Early-career | Mid-career | Senior |
|------|---|---|---|
| **AI Engineer** | $160K | $180K | $220K |
| **Agentic Engineer** | N/A | $270K | $350K+ |
| **ML Ops Engineer** | $140K | $170K | $210K |
| **AI Product Manager** | $180K | $220K | $280K |

### Equity (Annual Grant)

| Company Type | AI Engineer | Agentic Eng | Senior |
|---|---|---|---|
| **Startup (pre-Series A)** | 0.1-0.3% | 0.3-1% | 0.5-2% |
| **Startup (Series A-B)** | 0.05-0.15% | 0.15-0.5% | 0.3-1% |
| **Startup (Series C+)** | 0.02-0.1% | 0.1-0.3% | 0.2-0.5% |
| **Public company** | Stock grants worth $50-100K | Stock grants worth $150-300K | Stock grants worth $300K+ |

### Bonus (Annual)

- **Target**: 15-20% of salary (actual: 10-30% depending on performance)
- **Agentic engineers**: 20-30% (to attract/retain scarce talent)

### Sign-on Bonus (for external hires)

- **AI Engineer**: $20-50K
- **Agentic Engineer**: $50-150K
- **Senior/Director**: $100-250K

---

## PART 6: AI CENTER OF EXCELLENCE BLUEPRINT

### Optimal Structure (for $1-5B company)

```
┌──────────────────────────────────────────────────────┐
│  Chief AI Officer (Reports to CTO/SVP)               │
│  (Strategy, external relationships, board)           │
└──────────────┬───────────────────────────────────────┘
               │
        ┌──────┴───────────┬──────────────┬────────────┐
        │                  │              │            │
  ┌─────▼────────┐  ┌──────▼──────┐  ┌────▼────┐  ┌────▼─────┐
  │Architecture  │  │ AI Product  │  │  Risk &  │  │  ML Ops  │
  │ Lead         │  │ Management  │  │ Ethics   │  │ Platform │
  │              │  │             │  │          │  │          │
  │ - Design     │  │ - Roadmap   │  │ - Audit  │  │ - Infra  │
  │ - Tech stack │  │ - Metrics   │  │ - Compliance
  │ - Review     │  │ - Comms     │  │ - Risk   │  │ - Deploy │
  └─────┬────────┘  └─────────────┘  └──────────┘  └──────────┘
        │
   ┌────┴─────────┬──────────┬──────────┐
   │              │          │          │
┌──▼────┐  ┌──────▼──┐  ┌───▼────┐  ┌─▼──┐
│Senior │  │AI Engin │  │AI Engin│  │Data│
│Archi  │  │eer 2    │  │eer 3   │  │Eng │
│ect 1  │  │         │  │        │  │    │
└───────┘  └─────────┘  └────────┘  └────┘
(4-person team, each can lead projects)
```

**Key roles**:

1. **Chief AI Officer** (1 FTE, director-level)
   - Compensation: $250-350K
   - Responsible for: Strategy, board communications, external partnerships
   - Hiring: VP-level from big tech or AI company

2. **Senior AI Architect** (1 FTE, senior engineer-level)
   - Compensation: $220-280K
   - Responsible for: Technology decisions, architecture reviews, frameworks
   - Hiring: 10+ years experience, from Meta/Google/OpenAI

3. **AI Engineers** (3-4 FTE, mid/senior level)
   - Compensation: $160-220K each
   - Responsible for: Building, shipping, mentoring
   - Hiring: Mix of external (hire 2 from startups) + internal retraining (1)

4. **ML Ops Engineer** (1 FTE)
   - Compensation: $160-190K
   - Responsible for: Infrastructure, deployment, monitoring, cost optimization
   - Hiring: From infrastructure team or hire external

5. **AI Product Manager** (1 FTE)
   - Compensation: $190-250K
   - Responsible for: Roadmap, metrics, stakeholder alignment
   - Hiring: From existing product team + training

6. **AI Ethics Officer** (0.5-1 FTE)
   - Compensation: $140-200K
   - Responsible for: Governance, compliance, risk assessment
   - Hiring: Law firm, compliance officer retraining, or specialized hire

**Total headcount**: 6-8 FTE
**Total annual cost**: $1.2-1.8M all-in (salary + benefits + overhead)

### Build Timeline

**Month 0-1: Staffing**
- Recruit Chief AI Officer
- Recruit Senior Architect
- Internal sourcing for 1st AI engineer (if possible)

**Month 2-3: Hiring**
- Chief AI Officer onboarded, starts recruiting
- Architect defines tech stack
- Post openings for 2-3 AI engineers

**Month 4-5: Growing**
- Hire first 2 AI engineers
- ML Ops engineer joins
- Architect designing first POC

**Month 6-9: Execution**
- 2 POCs in progress (under architect guidance)
- ML Ops setting up infrastructure
- AI Product Manager hired

**Month 9-12: Scaling**
- 3rd AI engineer onboarded
- 2-3 POCs move to production
- Ethics officer onboards

**Month 12-18: Optimization**
- Team fully staffed
- Multiple systems in production
- Mentoring structure in place
- Beginning to scale to other business units (if hub-and-spoke)

---

## PART 7: BUILD VS. OUTSOURCE FOR AI TALENT

### Build (Hire Internally)

**When**: AI is core to 3-year strategy

**Pros**:
- ✓ Culture fit (hire for your org)
- ✓ Long-term ownership (accountability)
- ✓ Institutional knowledge (stays with company)
- ✓ Better for secret sauce (proprietary knowledge)

**Cons**:
- ✗ Slow (6-12 months to full productivity)
- ✗ Risky (hire mistakes costly)
- ✗ Expensive ($2M/year for team)
- ✗ Scarce talent (competitive market)

**Cost**: $1.2-2M/year per fully-loaded team
**Timeline**: 12-18 months to useful capacity
**Risk**: High (depends on hiring success)

---

### Outsource (Agency / Consulting)

**When**: Exploratory phase, specific project, short-term need

**Pros**:
- ✓ Speed (start in weeks)
- ✓ Flexibility (scale up/down fast)
- ✓ Specialized expertise (hire for specific skill)
- ✓ Lower commitment (contract-based)

**Cons**:
- ✗ Knowledge walks away (not retained)
- ✗ Quality variable (depends on firm)
- ✗ Dependency (reliant on external partner)
- ✗ Cost (can be $200K-500K for 3-month engagement)

**Cost**: $500K-2M for 3-month engagement
**Timeline**: 2-4 weeks to start
**Risk**: Vendor risk, knowledge loss

---

### Hybrid (Best of Both)

**Structure**: 3-4 core team + specialized outsourcing

**Example**:
- Core team (build): 1 architect + 2 AI engineers ($600K/year)
- Specialized outsourcing (outsource): 6-month engagement for multi-agent expertise ($500K)
- Outcome: Core team learns from specialist, becomes self-sufficient after 6 months

**Cost**: $1.1M year 1 (core + specialist), then $600K year 2+ (core only)
**Timeline**: 2 months to start, 12 months to independence
**Risk**: Medium (depends on knowledge transfer)

---

## TALENT STRATEGY CHECKLIST

- [ ] **Team archetype chosen**: Centralized / Federated / Hub-and-Spoke
- [ ] **Hiring plan** defined (which roles, timeline, budget)
- [ ] **Compensation benchmarked** (competitive vs. market)
- [ ] **Recruiting strategy** (university, tech companies, startups)
- [ ] **Onboarding plan** (knowledge transfer, ramp time)
- [ ] **Retention strategy** (equity, growth, culture)
- [ ] **Build vs. outsource** decision made (with rationale)
- [ ] **Upskilling plan** for existing staff
- [ ] **Budget approved** (3-year forecast)
- [ ] **Success metrics** defined (retention, velocity, quality)

---

**Last Updated**: March 2026
**Reference**: SKILL.md Phase 4 (AI Talent Strategy)
**Key Takeaway**: Agentic engineering is the critical bottleneck. Plan 18 months to build internal capability, or outsource to bridge gap.
