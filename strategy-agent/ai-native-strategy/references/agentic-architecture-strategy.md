# Agentic Architecture Strategy & Technical Decisions

> **Pricing & Model Data**: All model costs, context windows, and capability ratings in this document are derived from [`model-economics-config.json`](model-economics-config.json). When prices change, update the config — not this document. The agent should read the config to generate current tables and calculations rather than relying on the static examples below.

## Executive Summary

This reference covers the technical-business bridge for agentic AI systems: how to choose orchestration patterns, LLMs, frameworks, memory systems, reasoning strategies, and protocols to make winning architectural decisions.

**2026 Context**:
- 1,445% surge in multi-agent inquiries
- Only 11% of enterprises have production agentic systems
- 40% of agentic projects expected to fail by 2027
- LLM prices dropped 80% (changing economics)
- Multi-agent frameworks maturing but standards still emerging

---

## PART 1: MULTI-AGENT ORCHESTRATION PATTERNS

### Pattern 1: Supervisor Pattern (Hierarchical)

**Architecture**:
```
                    Supervisor LLM
                    (Decisions)
                    /    |     \
                   /     |      \
              Agent 1  Agent 2  Agent 3
           (Customer)  (Billing) (Technical)
              (Spec) (Spec)     (Spec)
```

**How it works**:
1. User query arrives
2. Supervisor analyzes and determines which agent(s) should handle it
3. Supervisor delegates to appropriate agent
4. Agent executes task, returns result
5. Supervisor synthesizes results and responds to user

**Best for**:
- Structured workflows with clear task boundaries
- Enterprise governance (supervisor controls access, audit trail)
- Medium complexity (5-20 agents)
- Known use cases (customer service, document processing, approvals)

**Pros**:
- ✓ Predictable (supervisor follows rules)
- ✓ Auditable (clear decision path)
- ✓ Safe (can restrict agent capabilities)
- ✓ Easy to debug (isolated agent failures)
- ✓ Production-ready (proven pattern)

**Cons**:
- ✗ Supervisor becomes bottleneck (all decisions go through it)
- ✗ Latency (extra LLM call for supervision)
- ✗ Limited to known use cases (supervisor trained on examples)
- ✗ Doesn't handle emergence (agents can't self-organize)

**Production readiness**: HIGH (11% of enterprises using this pattern)

**Cost estimate** (see model-economics-config.json for current rates):
- LLM calls: 1 supervisor + N agents = (N+1) LLM calls per request
- Example: 5-agent system, 100K requests/month
  * Supervisor cost: 100K × $5 (Claude Opus) / 1M = $0.50/month
  * Agents: 100K × 5 × $5 / 1M = $2.50/month
  * Total: $3/month (plus infrastructure)

**Confidence**: HIGH (battle-tested pattern)

---

### Pattern 2: Swarm Pattern (Peer-to-Peer)

**Architecture**:
```
   Agent 1 ↔ Agent 2 ↔ Agent 3
     ↑         ↓         ↑
     └─────────┼─────────┘
      Agent 4 ↔ Agent 5
```

**How it works**:
1. Agents have equal autonomy (no supervisor)
2. Agents communicate directly with each other
3. Agents self-organize to solve problem
4. Emergence: System behavior is not pre-programmed
5. Example: Research agents debating, synthesizing, exploring unknown territory

**Best for**:
- Unstructured exploration (research, brainstorming)
- Complex problems without clear decomposition
- Autonomous adaptation (agents adjust behavior based on interaction)
- Emergence (outcome is novel, not pre-programmed)

**Pros**:
- ✓ Scalable (no bottleneck)
- ✓ Emergent behavior (novel solutions possible)
- ✓ Autonomous (no central control)
- ✓ Resilient (if one agent fails, others continue)

**Cons**:
- ✗ Hard to predict behavior (emergence is unpredictable)
- ✗ Difficult to debug (complex interaction patterns)
- ✗ Not suitable for safety-critical (can't guarantee outcomes)
- ✗ Frameworks immature (LangGraph Swarm, CrewAI still learning)
- ✗ Hard to implement production governance

**Production readiness**: MEDIUM (frameworks exist, but patterns still evolving)

**Cost estimate** (see model-economics-config.json for current rates):
- Higher LLM costs (agents debate, iterate, may call multiple times)
- Example: 5 agents exploring solution, takes 10 rounds of discussion
  * Cost: 10 rounds × 5 agents × $5 / 1M tokens = Much higher than supervisor
  * Better for high-value decisions (where exploration cost is justified)

**Confidence**: MEDIUM (pattern is emerging, success is variable)

---

### Pattern 3: Hierarchical Pattern (Multi-Level Supervision)

**Architecture**:
```
                    Top Supervisor
                    (Strategy)
                   /     |      \
                  /      |       \
            Team Lead 1  Lead 2   Lead 3
          (Customer)   (Finance)  (Ops)
           / | \         / | \      / | \
          A1 A2 A3      A4 A5 A6   A7 A8 A9
```

**How it works**:
1. Top supervisor handles strategic decisions (which team should handle it?)
2. Team leads handle tactical decisions (which agent in team?)
3. Individual agents execute tasks
4. Results bubble up: Agent → Team Lead → Supervisor → User

**Best for**:
- Large enterprises (10+ agents across multiple teams)
- Multi-department automation (HR, Finance, Operations)
- Complex governance (different rules for different teams)
- Organizational structure already hierarchical

**Pros**:
- ✓ Scalable to 50+ agents
- ✓ Encapsulation (teams are isolated, can be managed separately)
- ✓ Clear accountability (each level has owner)
- ✓ Governance at each level
- ✓ Easy to manage (teams are independent units)

**Cons**:
- ✗ Latency (multiple supervision layers)
- ✗ Complexity (many moving parts)
- ✗ Overhead (each layer adds supervision cost)
- ✗ Bottlenecks at each level
- ✗ Hard to debug (multi-layer interactions)

**Production readiness**: MEDIUM (pattern is viable but operationally complex)

**Cost estimate** (see model-economics-config.json for current rates):
- Multiple supervision layers increase LLM costs
- Example: 30 agents in 3 teams of 10
  * Top supervisor: 100K × $5 / 1M = $0.50
  * 3 team leads: 300K × $5 / 1M = $1.50
  * 30 agents: 3M × $5 / 1M = $15
  * Total: $17/month (plus infrastructure)

**Confidence**: MEDIUM-HIGH (viable for large enterprises)

---

### Pattern 4: Hybrid (Supervisor + Specialized Swarms)

**Architecture**:
```
               Supervisor
                (Routing)
               /    |     \
              /     |      \
        Swarm 1  Swarm 2  Swarm 3
       (Research) (Analysis) (Synthesis)
        Agent A    Agent D    Agent G
        Agent B    Agent E    Agent H
        Agent C    Agent F    Agent I
```

**How it works**:
1. Supervisor routes to specialized swarms
2. Each swarm operates autonomously (peer-to-peer within swarm)
3. Supervisor aggregates results from swarms
4. Combines structure (swarms are managed) with emergence (within swarms)

**Best for**:
- Complex, multi-stage problems
- Combination of structure (need predictability) + emergence (need exploration)
- Example: Research synthesis (research swarm explores, analysis swarm evaluates, synthesis swarm combines)

**Pros**:
- ✓ Combines benefits of supervisor (structure) + swarm (emergence)
- ✓ Scalable and flexible
- ✓ Predictable at top level, emergent at sub-level

**Cons**:
- ✗ Very complex
- ✗ High latency (multiple interaction layers)
- ✗ Hard to debug (complicated emergent behavior)
- ✗ Frameworks don't support well yet

**Production readiness**: LOW (emerging pattern, few production examples)

**Confidence**: MEDIUM (pattern is promising but immature)

---

### Pattern Selection Decision Tree

```
Start here: How many agents do you need?

<5 agents?
├─ YES → Supervisor (simplest, most robust)
│   └─ Structured workflow? Governance critical?
│       ├─ YES → Supervisor
│       └─ NO → Evaluate swarm if fully exploratory
│
5-20 agents?
├─ YES → Supervisor (still manageable) OR Swarm (if exploratory)
│   └─ Clear task decomposition available?
│       ├─ YES → Supervisor
│       └─ NO → Swarm
│
20-100 agents?
├─ YES → Hierarchical
│   └─ Organized into teams already?
│       ├─ YES → Hierarchical (follows org structure)
│       └─ NO → Hybrid (groups by function)
│
>100 agents?
└─ YES → Hierarchical + Distributed
    └─ Very complex, rarely necessary
```

---

## PART 2: LLM SELECTION MATRIX (2026)

### Model Comparison

> **[GENERATED FROM CONFIG]** The agent should read `model-economics-config.json` and render the current LLM comparison matrix below. The following static snapshot was accurate as of 2026-03-10:

| Dimension | GPT-5.2 | Claude Opus 4.6 | Gemini 3 | Llama 4 Scout | DeepSeek-R1 | Qwen 3 | Preference |
|-----------|---------|---------|----------|---------|------------|--------|---|
| **Input Cost** | $1.75/1M | $5/1M | $2.50/1M | $0.40/1M | $0.50/1M | $0.30/1M | Cost-critical: Llama Scout or DeepSeek |
| **Output Cost** | $14/1M | $25/1M | $10/1M | $0.40/1M | $2/1M | $1.50/1M | Cost-critical: Llama Scout or Qwen |
| **Context Window** | 200K | 200K | 1M | 10M | 128K | 128K | Long-context: Gemini 3 or Llama Scout |
| **Reasoning Quality** | Excellent | Excellent | Good | Emerging | Strong | Emerging | Nuanced: Claude > GPT-5.2 > DeepSeek |
| **Instruction Following** | Good | Excellent | Good | Good | Good | Good | Consistency: Claude Opus |
| **Multimodal** | Image/video | Text (can see images) | Image/video/audio | Text | Text | Text | Images: Gemini 3 or GPT-5.2 |
| **Latency** | ~100-300ms | ~100-300ms | ~50-200ms | Varies (self-hosted) | ~100-300ms | ~100-200ms | Speed: Gemini 3 or self-hosted |
| **Safety/Jailbreak** | Medium | High | Medium | Varies | Medium | Medium | Safety: Claude Opus |
| **Availability** | Stable | Stable | Stable | Open-source | Stable | Stable | Reliability: GPT-5.2, Claude, Gemini |
| **Lock-in Risk** | HIGH | MEDIUM | MEDIUM | NONE | MEDIUM | NONE | Portability: Llama, DeepSeek, Qwen |
| **Production Maturity** | HIGH | HIGH | HIGH | MEDIUM | MEDIUM | MEDIUM | Battle-tested: GPT-5.2, Claude, Gemini |

### Model Selection by Use Case

**High-Stakes Reasoning** (strategic decisions, complex analysis):
- **#1**: Claude Opus 4.6 (excellent nuance, reasoning)
- **#2**: GPT-5.2 (strong reasoning, speed)
- **#3**: DeepSeek-R1 (emerging, good at complex thinking)
- Cost tradeoff: Claude $25/1M output vs. GPT-5.2 $14 vs. DeepSeek $2 (see model-economics-config.json for current rates)
- Verdict: If budget allows, Claude. Otherwise GPT-5.2.

**Cost-Critical Processing** (high-volume classification, summarization):
- **#1**: Llama 4 Scout ($0.40/1M, self-hosted)
- **#2**: Qwen 3 ($0.30/1M)
- **#3**: DeepSeek-R1 ($0.50/1M)
- Verdict: Llama Scout if you can self-host, otherwise Qwen.

**Long-Context Tasks** (analyze 100-page documents, 10K token contexts):
- **#1**: Llama 4 Scout (10M token context)
- **#2**: Gemini 3 (1M token context)
- **#3**: Claude Opus (200K token context)
- Verdict: Llama Scout is only 10M option; Gemini 3 is good fallback.

**Multimodal** (images, video, audio):
- **#1**: Gemini 3 (best multimodal)
- **#2**: GPT-5.2 (image + video)
- **#3**: Claude Opus (image support limited)
- Verdict: Gemini 3 if multimodal is core, otherwise Claude.

**Fast, Predictable Latency** (real-time applications):
- **#1**: Gemini 3 (50-200ms)
- **#2**: Self-hosted Llama (latency depends on infrastructure)
- Verdict: Gemini 3 if consistency matters.

**Open-Source / No Lock-In**:
- **#1**: Llama 4 Scout (fully open)
- **#2**: Qwen 3 (open, China-based)
- **#3**: DeepSeek-R1 (open, China-based)
- Verdict: Llama Scout if you want US-friendly open-source.

### Unit Economics Impact

> **[GENERATED FROM CONFIG]** The agent should read `model-economics-config.json` and render the current unit economics table below. The following static snapshot was accurate as of 2026-03-10:

**Example**: Process 1M tokens/month

| Model | Monthly Cost | Annual Cost | For $10K/month subscription | Margin |
|-------|------|-------|---|---|
| Llama 4 Scout (self-hosted) | ~$400 | $4.8K | $10K revenue | 96% margin |
| Qwen 3 | $300 | $3.6K | $10K revenue | 97% margin |
| GPT-5.2 | $1.75K | $21K | $10K revenue | NEGATIVE |
| Claude Opus | $5K | $60K | $10K revenue | NEGATIVE |
| DeepSeek-R1 | $1.5K | $18K | $10K revenue | NEGATIVE |

**Key insight**: Model choice can make or break unit economics
- Llama Scout: Margin works at any scale
- Claude/GPT-5.2: Margin only works at high volume (need $100K+ annual revenue per customer)

### LLM Selection Framework

```
Decision: Which LLM should we use?

Question 1: Are you cost-sensitive (margin <70% acceptable)?
├─ NO (premium positioning) → Claude Opus or GPT-5.2
├─ YES → Continue to Question 2

Question 2: Do you need long context (>200K tokens)?
├─ YES → Llama 4 Scout (only 10M option)
├─ NO → Continue to Question 3

Question 3: Do you need multimodal (images, video)?
├─ YES → Gemini 3
├─ NO → Continue to Question 4

Question 4: Are you willing to self-host / operate infrastructure?
├─ YES → Llama 4 Scout or Qwen 3
├─ NO → GPT-5.2 or Claude (managed APIs)

Question 5: Do you need excellent reasoning?
├─ YES → Claude Opus > GPT-5.2 > DeepSeek-R1
├─ NO → Cheaper model (Llama, Qwen, or commodity)
```

---

## PART 3: AGENT FRAMEWORK COMPARISON

### Framework Landscape (2026)

| Framework | Creator | Monthly Downloads | GitHub Stars | Best For | Learning Curve | Maturity |
|-----------|---------|------------------|-------------|----------|---|---|
| **LangGraph** | LangChain | 38M | 45K | Agentic workflows, enterprise, multiple LLMs | Steep | HIGH |
| **CrewAI** | Crew | 3.2M | 44K | Team-based agents, multi-agent, ease-of-use | Gentle | MEDIUM |
| **Claude Agent SDK** | Anthropic | 200K | 12K | Claude-native systems, built-in safety, tool use | Gentle | HIGH |
| **OpenAI Agents SDK** | OpenAI | 1M | 8K | GPT-native, tight integration, function calling | Gentle | MEDIUM |
| **Microsoft Agent Framework** | Microsoft | 500K | 5K | Enterprise, Teams integration, Copilot ecosystem | Steep | MEDIUM |
| **Google ADK** | Google | 300K | 4K | Multimodal, Gemini integration, search integration | Moderate | MEDIUM |

### Framework Selection Criteria

**Criterion 1: Are you locked into one LLM?**

| Decision | Framework | Why |
|----------|-----------|-----|
| Using Claude exclusively | **Claude Agent SDK** | Built for Claude, best tool use, safety features |
| Using GPT-5.2 exclusively | **OpenAI Agents SDK** | Native integration, function calling optimized |
| Using Gemini exclusively | **Google ADK** | Native integration, search/multimodal support |
| Multi-LLM strategy | **LangGraph or CrewAI** | Support any LLM, flexibility |

**Criterion 2: Do you need enterprise governance?**

| Need | Framework | Why |
|------|-----------|-----|
| Yes (audit, monitoring, control) | **LangGraph** | Built for enterprise, extensive monitoring, control flow |
| No (startup speed) | **CrewAI** | Fastest to MVP, less bureaucracy |

**Criterion 3: Do you need multi-agent?**

| Need | Framework | Why |
|------|-----------|-----|
| Yes (5+ agents, orchestration) | **LangGraph or CrewAI** | Both support multi-agent well |
| No (single agent or simple chain) | **Claude Agent SDK** | Simpler, less overhead |

**Criterion 4: Do you want open-source?**

| Need | Framework | Why |
|------|-----------|-----|
| Yes (no vendor lock-in) | **LangGraph or CrewAI** | Both open-source, self-hostable |
| No (prefer managed) | **Claude Agent SDK, OpenAI, Google** | Fully managed services |

### Framework Recommendation by Profile

**Startup Building AI Agent Product**:
- **#1**: CrewAI (fast MVP, gentle learning curve, multi-agent support)
- **#2**: LangGraph (more powerful, steeper curve, but scales better)

**Enterprise Automating Internal Workflows**:
- **#1**: LangGraph (governance, monitoring, enterprise features)
- **#2**: Claude Agent SDK (simplicity, safety, good enough for internal)

**Building Claude-Native Product**:
- **#1**: Claude Agent SDK (purpose-built, best tool integration)
- **#2**: LangGraph (if you need enterprise scale)

**Building Multi-LLM Platform**:
- **#1**: LangGraph (supports any LLM, most flexible)
- **#2**: CrewAI (good multi-LLM support, simpler)

**Building Vertical AI**:
- **#1**: Claude Agent SDK or LangGraph (depending on governance needs)
- **#2**: Specialized framework (build custom for your domain)

---

## PART 4: MEMORY ARCHITECTURE PATTERNS

### Dual-Layer Memory (2026 Best Practice)

**Architecture**:
```
User Request
    ↓
┌─────────────────────────────────────┐
│ HOT PATH (Fast, Expensive)          │
│ ├─ Current task context              │
│ ├─ Recent conversation history       │
│ ├─ LLM context window (200K tokens)  │
│ └─ Live for duration of request      │
└─────────────────────────────────────┘
    ↓ (query)
┌─────────────────────────────────────┐
│ COLD PATH (Slow, Cheap)             │
│ ├─ Vector database (embeddings)      │
│ ├─ Knowledge graph (facts)           │
│ ├─ Chat history (months of data)     │
│ └─ Always available, persistent      │
└─────────────────────────────────────┘
```

**How it works**:
1. **Hot path**: Current task, recent context loaded into LLM context window
2. **Cold path**: Agent queries cold path ("what did we discuss last month about Project X?")
3. **Retrieval**: Relevant memories injected into hot path
4. **Reasoning**: LLM reasons with current task + injected context
5. **Result**: Agent responds with full context

**Memory Types**:

| Type | What | Where | Retrieval | Example |
|------|------|-------|-----------|---------|
| **Episodic** | "What happened?" | Chat history, logs | BM25 search, semantic search | "What did user say about problem X?" |
| **Semantic** | "What did we learn?" | Knowledge graph, facts, extracted insights | Structured query | "What's the user's budget?" |
| **Procedural** | "How should I do this?" | Workflow rules, best practices, templates | Rule engine | "What's the approval process for expenses?" |

### Memory Architecture Decision

**Pattern A: In-Context Only** (simplest)
- All memory in LLM context window
- Pro: Simple, no infrastructure
- Con: Limited memory (200K tokens), expensive
- Cost: ~$0.30 per request (200K tokens in)
- Best for: Short conversations, simple agents

**Pattern B: Dual-Layer** (recommended for production)
- Hot path (recent context in LLM) + Cold path (vector DB + knowledge graph)
- Pro: Scales to unlimited memory, flexible, efficient
- Con: More complex, additional infrastructure
- Cost: ~$0.50 per request (hot + cold path retrieval)
- Best for: Long-running agents, complex memory needs

**Pattern C: Retrieval-Augmented Generation (RAG)** (specialized)
- All memory in vector database, always retrieved
- Pro: Flexible, powerful
- Con: Retrieval overhead, cost increases with memory size
- Cost: ~$0.05-0.30 per retrieval (depends on database)
- Best for: Document-heavy workflows

### Memory Cost Model

**Example**: Customer service agent handling 10K conversations/month

**In-Context Only**:
- 10K conversations × 200K avg tokens × $5 / 1M = $10K/month
- Problem: Can't remember previous conversations

**Dual-Layer**:
- Hot path: 10K × 50K tokens (recent only) × $5 / 1M = $2.5K/month
- Cold path retrieval: 10K × 2 retrievals × 500 tokens × $5 / 1M = $0.05K/month
- Vector DB: ~$200/month (Pinecone, Weaviate)
- Total: $2.7K/month (70% cheaper, unlimited memory)

**Verdict**: Dual-layer wins on cost AND memory capacity

### Memory Retrieval Strategy

**Question 1: When should agent retrieve memory?**
- Per-step (every agent action) → More accurate, more expensive
- Per-task (once per user request) → Cheaper, may miss context
- Per-session (once per conversation) → Very cheap, risky

**Recommendation**: Per-task (good balance)

**Question 2: What should agent retrieve?**
- Semantic search ("similar conversations") → Best for discovery
- Structured query ("get user's budget") → Best for facts
- BM25 (keyword search) → Good fallback, cheap

**Recommendation**: Semantic search for memory, structured for facts

---

## PART 5: REASONING STRATEGY SELECTION

### Strategy 1: ReAct (Reason + Act)

**Pattern**:
```
Thought: Let me think about this...
Action: Call tool X with params
Observation: Tool returned Y
Thought: Now I understand...
Action: Call tool Z with params
Observation: Tool returned A
Final answer: Based on observations...
```

**How it works**: Agent alternates between thinking and tool use

**Best for**: Clear task decomposition with tools available
**Token overhead**: ~1.5x (thinking steps add tokens)
**Confidence**: HIGH (proven pattern)

**Example**: Customer support agent
```
Thought: User asked about order status
Action: lookup_order_status(order_id=12345)
Observation: Order shipped, arrives tomorrow
Thought: I have the info
Action: none
Final: Your order shipped and arrives tomorrow
```

---

### Strategy 2: Plan-and-Execute

**Pattern**:
```
PLAN:
1. Understand the problem
2. Break into sub-tasks
3. Execute each sub-task
4. Synthesize results

EXECUTE:
[Run each sub-task sequentially]
```

**How it works**: Agent plans approach first, then executes

**Best for**: Long-horizon tasks, complex dependencies
**Token overhead**: ~1.2x (planning adds cost)
**Confidence**: HIGH (proven for complex reasoning)

**Example**: Project planning agent
```
PLAN:
1. Understand project scope
2. Identify risks
3. Create timeline
4. Resource allocation

EXECUTE:
[Each step runs in sequence]
```

---

### Strategy 3: Tree of Thoughts (ToT)

**Pattern**:
```
Initial problem
    ├─ Thought 1 → Thought 1a → Result A (prune if low score)
    ├─ Thought 1b → Result B
    ├─ Thought 2 → Thought 2a → Result C
    └─ Thought 2b → Result D (prune)

Select best: B or C?
Continue from best...
```

**How it works**: Explore multiple reasoning paths, prune low-confidence branches

**Best for**: High-stakes decisions, novel problems
**Token overhead**: **3-5x** (explores many paths)
**Cost impact**: **VERY HIGH** (only use when justified)
**Confidence**: MEDIUM (powerful but expensive)

**When to use**:
- [ ] Decision worth >$100K?
- [ ] Novel territory (no precedent)?
- [ ] High risk of error?

If all YES → Consider ToT. Otherwise, ReAct is more efficient.

**Example**: Strategic decision
```
Path 1: Acquire competitor
  ├─ Sub-path 1a: Integration costs high
  ├─ Sub-path 1b: Data value justified
  └─ Score: Medium (8/10)

Path 2: Build internally
  ├─ Sub-path 2a: Timeline 2+ years
  ├─ Sub-path 2b: Talent availability?
  └─ Score: Low (4/10)

Select Path 1, continue...
```

---

### Strategy 4: Pre-Act (Parallel Execution)

**Pattern**:
```
Agent pre-computes all needed tool calls
├─ Tool 1: get_customer_data()
├─ Tool 2: get_order_history()
├─ Tool 3: get_product_details()
└─ Tool 4: get_recommendations()

Execute all in parallel
↓
Synthesize results
```

**How it works**: Agent determines all tool calls upfront, executes in parallel

**Best for**: Independent tasks, latency-critical
**Token overhead**: ~1.1x (minimal, just planning)
**Latency benefit**: Parallel execution saves time
**Confidence**: HIGH (effective for batch work)

**Example**: Customer 360 view
```
Pre-compute:
- get_customer_profile()
- get_account_balance()
- get_open_tickets()
- get_recent_purchases()

Execute all in parallel (save 70% latency vs sequential)
Synthesize into 360 view
```

---

### Strategy 5: Reflexion (Self-Evaluation + Iteration)

**Pattern**:
```
Initial response
    ↓
Agent evaluates: "Is this good?"
    ├─ YES → Return result
    └─ NO → Revise, iterate
        ↓
    Agent evaluates again
```

**How it works**: Agent generates, self-evaluates, iterates until satisfied

**Best for**: Creative tasks, content generation, open-ended problems
**Token overhead**: Variable (depends on iterations, typically 2-3x)
**Confidence**: MEDIUM (good for creative, risky for factual)

**Example**: Content generation
```
Draft 1: Write marketing email
Evaluate: "Is tone right? Too salesy?"
Revise: Remove hard sell, emphasize value
Evaluate: "Better, but still needs edge"
Revise: Add social proof, urgency
Evaluate: "Good, release"
```

---

### Reasoning Strategy Selection Framework

```
Decision: Which reasoning strategy?

Question 1: Do you have clear task decomposition (known steps)?
├─ YES → Use ReAct or Plan-and-Execute
│   ├─ Linear sequence? → ReAct
│   └─ Complex dependencies? → Plan-and-Execute
├─ NO → Continue to Question 2

Question 2: Is this high-stakes (>$100K impact)?
├─ YES → Consider Tree of Thoughts (but expensive)
├─ NO → Continue to Question 3

Question 3: Are task steps independent (can parallelize)?
├─ YES → Use Pre-Act
├─ NO → Continue to Question 4

Question 4: Is this exploratory/creative (open-ended)?
├─ YES → Use Reflexion
├─ NO → ReAct is default fallback
```

### Cost Comparison (1000 requests)

| Strategy | ReAct | Plan-Execute | ToT | Pre-Act | Reflexion |
|----------|-------|---|---|---|---|
| Token overhead | 1.5x | 1.2x | 4x | 1.1x | 2.5x |
| Total cost | $7.50 | $6K | $20K | $5.5K | $12.5K |
| Latency | Baseline | +10% | +30% (explore) | -50% (parallel) | +50% (iterate) |
| Best for | Standard | Complex | High-stakes | Batch | Creative |

---

## PART 6: PROTOCOL LANDSCAPE

### Protocol 1: MCP (Model Context Protocol)

**Purpose**: Standard for connecting agents to tools, data, APIs

**How it works**:
- Agent: "I need to access customer database"
- MCP: Validates permission, connects to database
- Agent: Queries database via standard interface
- Result: Returned to agent

**Adoption**: Emerging standard (2026)
- Anthropic leading specification
- LangChain, LangGraph integrating
- Growing ecosystem of MCP servers (databases, APIs, services)

**Benefit**: Reduce vendor lock-in, reuse tools across platforms

**Status**: Maturing, not yet dominant

---

### Protocol 2: A2A (Agent-to-Agent)

**Purpose**: Standard for agent-to-agent communication (peer discovery, delegation, negotiation)

**How it works**:
```
Agent A: "I need data from financial system"
Agent B: "I have that, here are the terms"
Agent A: "Accepted, sending request..."
Agent B: "Data sent"
```

**Current status**: Experimental (2025-2026)
- No dominant standard yet
- OpenAI, Anthropic, others exploring
- Expected standardization 2026-2027

**Use case**: Multi-agent systems without central supervisor

**Risk**: Still emerging, don't bet on specific protocol yet

---

### Protocol 3: AG-UI (Agent-User Interface)

**Purpose**: Standard for agent-user interaction patterns

**Emerging patterns**:
- Tool use (agent calls tools, returns results)
- Structured output (agent returns JSON, not freeform text)
- Turn-based interaction (clear user-agent exchange)
- Streaming (agent streams response in real-time)

**Status**: Evolving, Claude Agent SDK pioneering patterns

---

### Protocol 4: WebMCP

**Purpose**: MCP over HTTP/WebSocket (cloud-based tool connectivity)

**How it works**: MCP protocol transmitted over web

**Status**: Emerging (2026)

---

### Strategic Protocol Decision

```
Question: Which protocols should you build on?

#1: Build MCP-native
- Agents can connect to any MCP-compatible tool
- Future-proofs against single LLM vendor
- Increases flexibility, reduces lock-in
- Cost: Some additional abstraction layer

#2: Use standard APIs (REST, GraphQL)
- More mature, better tooling
- Wider ecosystem support
- Less emerging risk

#3: Proprietary APIs
- Most control, most lock-in
- Fastest to ship
- Risk: New protocols emerge, you're stuck

RECOMMENDATION: MCP-native if possible (emerging standard, good practices)
```

---

## PART 7: PRODUCTION DEPLOYMENT PATTERNS

### Bounded Autonomy & Human-in-the-Loop

**Autonomy Levels**:

| Level | Definition | Example | Risk | Use Case |
|-------|-----------|---------|------|----------|
| **0** | Suggest, human approves all | Agent suggests, human clicks "do it" | NONE | High-stakes (hiring, $100K+ decisions) |
| **1** | Act within bounds, human reviews | Agent processes support ticket, human reviews | LOW | Medium-stakes ($1K-10K) |
| **2** | Act, alert on variance | Agent optimizes ad spend, alerts if >20% change | MEDIUM | Operational ($100-1K) |
| **3** | Autonomous, human oversight at meta-level | Agent manages SLA independently | HIGH | Critical ops, well-tested |
| **4** | Full autonomous, human out of loop | Agent trades autonomously | VERY HIGH | Rare, only if bulletproof |

**Recommendation by domain**:
- Healthcare/finance: Level 0-1 (human always in loop)
- Customer-facing: Level 1-2 (human reviews high-impact actions)
- Internal operations: Level 2-3 (human oversight at meta level)
- Trading/autonomous: Level 3-4 (only if extensively tested)

### Checkpoint Protocol

**Checkpoints**: Decision points where agent must check before proceeding

```
Agent workflow:
1. Understand request
2. Gather data
3. [CHECKPOINT] If action >$10K, ask human approval
4. Execute action
5. [CHECKPOINT] If confidence <70%, alert human
6. Confirm result
```

**Checkpoint types**:
- Financial ($): If transaction >$X, require approval
- Uncertainty: If model confidence <Y%, require human input
- Exception: If unexpected condition detected, escalate
- Rate-limit: Max N actions per period before review

---

## PART 8: COST OPTIMIZATION STRATEGIES

### Strategy 1: Token Reduction

**Techniques**:
- Shorter system prompts (remove unnecessary detail)
- Context window optimization (only load relevant history)
- Smarter retrieval (get fewer but better results)
- Prompt caching (reuse expensive computations)

**Expected savings**: 30-50% reduction in tokens

**Example**:
- Current: 500 tokens/request × 100K requests = 50M tokens/month = $250/month
- Optimized: 300 tokens/request × 100K = 30M tokens/month = $150/month
- Savings: $100/month ($1.2K/year)

---

### Strategy 2: Model Downsampling

**Technique**: Use cheaper models for straightforward tasks, expensive models only for complex reasoning

**Example**:
- 70% of requests are simple (classification, lookup) → Use Llama Scout ($0.40/1M)
- 30% of requests are complex (reasoning) → Use Claude Opus ($5/1M)
- Blended cost: 0.7 × $0.40 + 0.3 × $5 = $1.88/1M (vs. $5 if all Claude)
- Savings: 62%

---

### Strategy 3: Batch Processing

**Technique**: Group independent requests, process together

**Example**:
- Process 1000 customer support tickets one-by-one: 1000 separate API calls
- Process in batch (100 at a time): 10 batch API calls + 1 synthesis call = 11 calls
- Token efficiency: Better batching reduces overhead
- Savings: 10-40% depending on task

---

### Strategy 4: Prompt Caching

**Technique**: Cache expensive computations (system prompt, context, examples)

**How it works**:
```
Request 1: System prompt (expensive, cached) + context
Request 2: System prompt (reused from cache) + different context
Request 3: System prompt (reused from cache) + different context
```

**Savings**: First request expensive, subsequent requests cheap (reuse cache)

**Use case**: Same system prompt for many requests (good for agent systems)

---

## Architecture Decision Checklist

- [ ] **Orchestration pattern chosen**: Supervisor / Swarm / Hierarchical / Hybrid
- [ ] **LLM selected** with unit economics validated
- [ ] **Framework chosen** (LangGraph / CrewAI / Claude Agent SDK / other)
- [ ] **Memory architecture designed** (hot/cold path, retrieval strategy)
- [ ] **Reasoning strategy selected** (ReAct / Plan-Execute / ToT / Pre-Act / Reflexion)
- [ ] **Protocol strategy** (MCP-native, standard APIs, or proprietary)
- [ ] **Autonomy level defined** (0-4) with checkpoint protocol
- [ ] **Cost optimizations** identified (token reduction, model downsampling, batching)
- [ ] **Production readiness** assessed (scalability, monitoring, incident response)
- [ ] **Scaling plan** defined (from MVP to 10x load)

---

**Last Updated**: March 2026
**Reference**: SKILL.md Phase 3 (Agentic Architecture Strategy)
