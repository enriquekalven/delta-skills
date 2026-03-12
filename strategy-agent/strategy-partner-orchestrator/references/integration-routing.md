# Routing Decision Tree & Execution Sequencing

**Purpose:** Entry/exit conditions, handoff protocols, and failure paths for all 16 skills. Execution order rules and bidirectional flow management.

**Version:** 5.0 | **Updated:** 2026-03-10

---

## Routing Entry/Exit For Each Skill

Entry conditions trigger when to invoke a skill. Exit conditions define when it completes and hands off to the next skill. Success criteria and failure paths direct response.

### Market Intelligence

**Entry Conditions:**
- Any engagement where external competitive/market context needed
- Diagnostic work is about to start (feeds into diagnosis)
- Strategy decision depends on current market data (not dated information)
- Urgency: HIGH (real-time market conditions critical to decision)

**Exit Conditions:**
- Market intelligence package complete (competitor analysis + trend + benchmarks)
- Confidence on market position established (at least M)
- Key assumptions about market documented and tagged

**Handoff Protocol:**
- Output: Competitor Playbook + Market Trend Brief
- Send to: Strategy Partner, Rumelt Forge, Product Innovation, GTM Strategy
- Timing: Day 0.5-1.5 parallel with initial diagnostic kick-off

**Success Criteria:**
- Competitor positioning clear (what they do, how they win, what they're doing now)
- Market trend identified (growing, consolidating, disrupting?)
- Benchmarks provided for comparison (customer acquisition costs, pricing, growth rates)
- Confidence tagged (all findings marked H/M/L with source)

**Failure Path:**
- If <3 independent sources found: Flag as low confidence, proceed with caveats
- If competitor analysis stale (>60 days old): Escalate to user for updated intel
- If trend unclear (conflicting sources): Present both perspectives, don't force conclusion
- NEVER halt engagement; always proceed with fallback analysis

---

### Strategy Partner

**Entry Conditions:**
- User brings undefined or complex problem ("We're not growing fast enough")
- Situation needs framing before strategic decision can be made
- Diagnosis confidence unknown (<70%)
- Problem classification unclear
- Business context requires interpretation

**Exit Conditions:**
- Diagnosis complete with ≥70% confidence (or ≤70% confidence explicitly flagged)
- Problem classified (Competitive / Growth / Operational / Financial / Org / Tech / GTM / M&A / Other)
- Root cause hypothesis clear
- Decision frame defined (if-then logic on key levers)
- Next recommended skill identified

**Handoff Protocol:**
- Output: Strategy Partner Context Package (decision frame + diagnosis + assumptions flagged)
- Primary handoff to: Rumelt Forge (if strategic decision needed)
- Secondary handoff to: Domain skills if functional decision (e.g., to Technology Strategy if "how do we modernize?")
- Timing: After Day 1-2 of diagnosis

**Success Criteria:**
- 3+ independent findings with evidence
- Decision frame is MECE (mutually exclusive, collectively exhaustive)
- Assumptions explicit and tagged for validation
- Confidence score documented (% on analytical base)
- Kill conditions identified (what would invalidate this diagnosis?)

**Failure Path:**
- Request additional analysis before proceeding to Rumelt Forge
- Trigger Hypothesis Testing to validate key assumptions (if time allows)
- Flag to user: "Diagnosis has gaps; recommend additional data collection before strategy forge"
- Proceed to Rumelt Forge with caveats (medium confidence, not high)

---

### Rumelt Strategy Forge

**Entry Conditions:**
- Strategy Partner diagnosis complete with ≥70% confidence
- Decision is strategic (requires creating a coherent strategy kernel)
- User is committing to strategy work (not just exploration)
- Next 12+ months will be shaped by this strategy

**Exit Conditions:**
- Crux identified and articulated in 1 sentence
- Strategy Kernel complete (diagnosis + guiding policy + coherent actions)
- Coherence test passed (≥70/100 across internal/external/execution dimensions)
- Bad Strategy Detector ≥8/16
- All downstream handoffs identified (which execution skills need output?)

**Handoff Protocol:**
- Output: Rumelt Forge Output Package (kernel + validation scores + kill conditions)
- Routing TO EACH SKILL:
  - Operating Model: "Design org structure to deliver Actions 1-3"
  - GTM Strategy: "How do we take this guiding policy to market?"
  - Financial Strategy: "Can we resource this? What are unit economics?"
  - People & Talent: "What talent model executes these actions?"
  - Product Innovation: "What product roadmap supports this strategy?"
  - Technology Strategy: "What tech capabilities enable this kernel?"
  - Change Management: "What change program rolls this out?"
  - Execution Monitoring: "What KPIs do we track for this strategy?"
  - M&A & Corp Dev: "Are there M&A moves that accelerate this strategy?"
- Timing: After Day 1 of Rumelt work, outputs go to all downstream skills

**Success Criteria:**
- Crux is SINGULAR (not multiple challenges rolled together)
- Guiding Policy is asymmetric (competitors can't easily copy)
- Coherent Actions are SPECIFIC (owner named, timeline explicit, not vague)
- Kernel survives Downside scenario test (strategy still viable if conditions change)
- All execution skills can answer "How do I use this?" (not abstract)

**Failure Path:**
- Halt and request additional diagnostic input from Strategy Partner
- Identify what's missing (capability gap? market understanding? competitive data?)
- Re-forge kernel with new information
- If still fails: Surface to user as "strategy not viable with current constraints" → pivot or accept higher risk

---

## Execution Order & Phases

### Three-Phase Model

**PHASE 1: DIAGNOSIS & INTELLIGENCE (Days 0-2)**

Purpose: Understand situation, gather market context, identify problem

Skills running (parallel):
- Strategy Partner (primary diagnostic)
- Market Intelligence (external context)
- Hypothesis Testing (if needed to validate critical assumptions)

Skills on hold: All execution design skills (GTM, Operating Model, Financial, People, Technology)

Gate: Strategy Partner confidence ≥70% on diagnosis OR escalate for more analysis

---

**PHASE 2: STRATEGY CREATION & ANALYSIS (Days 2-4)**

Purpose: Forge coherent strategy, model growth/financials, understand execution implications

Skills running (parallel):
- Rumelt Strategy Forge (primary strategy creation, depends on Phase 1 completion)
- Growth Strategy (models growth scenarios)
- GTM Strategy (preliminary motion design)
- Financial Strategy (models unit economics and profitability)
- Product Innovation (assesses PMF and roadmap)
- Technology Strategy (assesses tech requirements)
- AI-Native Strategy (scenario simulations, contradiction detection)

Skills on hold: Operating Model, People & Talent, Change Management, M&A (pending strategy kernel lock)

Gate: Rumelt Forge coherence ≥70/100 AND all functional analyses complete

---

**PHASE 3: EXECUTION DESIGN & PLANNING (Days 4-6)**

Purpose: Design execution approach, org structure, people plan, change program

Skills running (parallel):
- Operating Model (org design to execute strategy)
- People & Talent (talent plan for org design)
- Change Management (change program design)
- M&A & Corp Dev (if M&A is part of strategy)
- Capital & Resource Strategy (allocate resources across initiatives)
- Execution Monitoring (define KPIs and tracking)

All prior skills: Available for iteration/refinement

Gate: All execution plans locked; ready for ATLAS report

---

**CONTINUOUS (All Phases):**
- AI-Native Strategy (real-time intelligence, scenario simulation, contradiction detection)
- Execution Monitoring (begins reporting as plans finalize)

---

### Cannot Proceed Rules

**RULE 1: Rumelt Forge Cannot Start Before Strategy Partner**

- Rumelt Forge REQUIRES Strategy Partner diagnostic output
- Exception: If Strategy Partner output delayed, Rumelt can request "diagnostic hypothesis" from user and proceed at higher risk (confidence capped at MEDIUM, not HIGH)
- Escalation: If more than 4 hours into Rumelt and still waiting for SP output, halt and request user input

**RULE 2: Execution Design Cannot Start Before Rumelt Forge**

- Operating Model, GTM, Financial, People all REQUIRE Rumelt kernel to design against
- Cannot lock org structure without knowing Coherent Actions (from Rumelt)
- Cannot lock talent plan without knowing org structure
- Parallel option: Can START preliminary GTM/Financial analysis while Rumelt is forging, but cannot LOCK designs until kernel finalized

**RULE 3: Financial Strategy Cannot Lock Until Growth Strategy Complete**

- Unit economics depend on growth assumptions (CAC, LTV, payback)
- Financial can model preliminary projections while Growth works, but cannot finalize model until Growth provides validated assumptions
- Timeline: Growth typically completes within 24 hours of Rumelt output

**RULE 4: People & Talent Cannot Lock Until Operating Model Complete**

- Talent plan depends on org structure (what roles, how many?)
- Can START preliminary talent assessment, but cannot finalize hiring plan until org structure locked
- Gate: Operating Model must complete before People & Talent finalizes headcount

**RULE 5: Change Management Cannot Start Until Org/People/Process Changes Clear**

- Change program design depends on knowing WHAT is changing (org structure, processes, roles, culture)
- Can START change readiness assessment in parallel, but cannot finalize change program until execution designs locked
- Gate: Operating Model + People & Talent + Process redesigns must be clear before Change Management finalizes plan

**RULE 6: ATLAS Report Cannot Finalize Until All Skills Complete**

- Report synthesizes outputs from all participating skills
- Must have structured outputs from every skill that was invoked
- Can generate preliminary report draft after Phase 2, but cannot finalize until Phase 3 complete

---

### Parallel Execution Allowed

**Skills That CAN Run in Parallel (No Dependency):**
- Strategy Partner + Market Intelligence (Market Intelligence feeds SP, but SP can proceed without)
- Rumelt Forge + Growth Strategy (once Strategy Partner output available)
- Rumelt Forge + GTM Strategy (once Strategy Partner output available)
- Rumelt Forge + Financial Strategy (once Strategy Partner output available)
- Rumelt Forge + Product Innovation (once Strategy Partner output available)
- Rumelt Forge + Technology Strategy (once Strategy Partner output available)
- GTM Strategy + Financial Strategy (can run parallel, then reconcile CAC assumptions)
- GTM Strategy + Product Innovation (can run parallel, then reconcile feature priorities)
- AI-Native Strategy (can run parallel with ALL skills, continuous)

---

### Typical Time Offsets Between Dependent Skills

| Dependent Skill | Required Input From | Typical Delay | Notes |
|---|---|---|---|
| Rumelt Forge | Strategy Partner | 1 day | Can start Rumelt after SP completes (end of Day 1) |
| Growth Strategy | Strategy Partner | 0.5 day | Can start parallel to Rumelt after SP diagnosis |
| GTM Strategy | Product Innovation | 1 day | Product needs to define positioning first |
| GTM Strategy | Growth Strategy | 0.5 day | Can start GTM preliminary while Growth calculates unit econ |
| Financial Strategy | Growth Strategy | 1 day | Needs Growth unit econ assumptions |
| Financial Strategy | GTM Strategy | 1 day | Needs CAC assumption from GTM |
| Operating Model | Rumelt Forge | 1 day | Needs Coherent Actions from Rumelt |
| People & Talent | Operating Model | 0.5 day | Needs org structure from OM |
| Change Management | Operating Model + People + Process | 1 day | Needs to know what's changing |
| Capital & Resource Strategy | Financial Strategy + Rumelt | 1 day | Needs capital requirements + prioritization |
| Execution Monitoring | All functional skills | 1-2 days | Needs KPI targets and assumption registers from all |
| ATLAS Report | All Phase 2-3 skills | 1 day | Needs structured outputs from all |

---

## Bidirectional Flow Protocols (Max 2 Iterations)

Some skill pairs must iterate and converge on shared assumptions. This prevents infinite loops while ensuring consistency.

### Growth ↔ Financial Strategy (Growth-CAC-LTV Loop)

**Iteration Loop:**
1. Growth Strategy produces initial unit economics (CAC, LTV, payback assumptions)
2. Financial Strategy validates CAC/LTV assumptions against market benchmarks
3. If Financial's benchmarks differ from Growth's assumptions: Financial wins (benchmarked against real market data)
4. Growth adjusts unit economics to Financial's validated assumptions
5. Financial re-models projections with adjusted unit econ
6. If outcomes changed materially: iterate once more (Iteration 2)
7. If Iteration 2 converges: LOCK (proceed to execution design)
8. If Iteration 2 diverges: Escalate to user for decision

**Convergence Criteria (Success):**
- CAC assumption within ±15% between Growth and Financial
- LTV assumption within ±20% between Growth and Financial
- Payback period within ±2 months
- Both skills sign off on unit economics as "realistic and benchmarked"

**Escalation Path (If No Convergence):**
- User decision required: Which unit economics assumption do we proceed with?
- Flag risk: "Growth and Financial cannot agree on unit economics; proceeding with MEDIUM confidence"
- Escalate to Execution Monitoring: Track actual CAC/LTV closely (this is high-risk assumption)

**Max Iterations:** 2 (If not converged after 2 iterations, escalate)

**Timeline:** Growth produces Iteration 1 by Day 2; Financial validates by end Day 2; if needed, Iteration 2 by Day 3

---

### GTM ↔ Financial Strategy (CAC Validation Loop)

**Iteration Loop:**
1. GTM Strategy proposes customer acquisition approach and estimates CAC
2. Financial Strategy validates CAC against market benchmarks (what are comparable companies spending?)
3. If Financial's benchmarks show GTM's CAC too high: Financial flags "GTM motion may be uneconomical"
4. GTM adjusts customer acquisition approach (different channels, messaging, segments) to lower CAC
5. Financial re-models profitability with adjusted CAC
6. If breakeven timeline acceptable: LOCK
7. If not: iterate once more (Iteration 2)

**Convergence Criteria (Success):**
- CAC assumption agreed (within ±15%)
- LTV:CAC ratio ≥3:1 (viable unit economics)
- Both skills confirm "go-to-market is economically viable"

**Escalation Path (If No Convergence):**
- Business model may not be viable at current pricing/cost structure
- Recommend pricing increase OR cost reduction OR different customer segment
- If no path to viable CAC: Escalate to Rumelt Forge → may require strategy pivot

**Max Iterations:** 2 (If not converged after 2 iterations, halt and recommend strategy pivot)

**Timeline:** GTM produces Iteration 1 by Day 2; Financial validates by end Day 2; if needed, Iteration 2 by Day 3

---

### GTM ↔ Product Strategy (Feature Priority Loop)

**Iteration Loop:**
1. Product Strategy proposes feature roadmap based on PMF signal
2. GTM Strategy proposes feature priorities based on market positioning and customer needs
3. If different priorities: Product wins if PMF confidence ≥70%; else Strategy Partner validates
4. GTM adjusts positioning and messaging to align with Product priorities
5. Product prioritizes features to support GTM positioning
6. If alignment achieved: LOCK
7. If still misaligned: iterate once more (Iteration 2)

**Convergence Criteria (Success):**
- Product and GTM agree on top 3 customer-winning features
- Product roadmap supports GTM positioning (not conflicting)
- GTM motion emphasizes features that drive retention/expansion

**Escalation Path (If No Convergence):**
- Escalate to Strategy Partner: "Product and GTM cannot agree on feature priority"
- Strategy Partner validates underlying assumptions (does product really have PMF?)
- If PMF unclear: Recommend Hypothesis Testing to validate
- If PMF clear: Product positioning wins, GTM adjusts motion

**Max Iterations:** 2 (If not converged after 2 iterations, escalate to Strategy Partner)

**Timeline:** Product produces Iteration 1 by Day 2; GTM responds by end Day 2; if needed, Iteration 2 by Day 3

---

## Universal Confidence Scale

All skills use this single confidence framework for consistency:

**H (High) ≥75%:** Well-grounded finding. Multiple independent sources confirm. Market data support confidence is justified. PROCEED with recommendation.

**M (Medium) 60-75%:** Finding is supported by evidence, but uncertainty remains. One or two assumptions critical. Market data supports direction but not magnitude. PROCEED WITH CAVEATS. Communicate assumptions and uncertainties. Monitor assumptions closely.

**L (Low) <60%:** Finding is directional or early-stage. Significant assumptions. Limited evidence. Needs more analysis or validation. ESCALATE OR REQUEST MORE ANALYSIS. Do not lock plans. Use for exploration only.

---

## Time-Based Execution Chart

```
Day 0-1:  Strategy Partner ──┐
          Market Intelligence ├→ Rumelt Forge decision
          Hypothesis Testing ──┘

Day 1-3:  Rumelt Forge ────────┐
          Growth Strategy      │
          GTM Strategy        ├→ Execution Design
          Financial Strategy  │
          Product Innovation  ├→
          Technology Strategy ┤
          AI-Native (cont.)   │
                              │
Day 3-5:                      ├→ Operating Model ──┐
                              │                     ├→ Change Mgmt
                              ├→ People & Talent ──┘
                              │
                              ├→ M&A & Corp Dev
                              │
                              └→ Capital & Resource

Day 5-6:                             Change Management ──┐
                                                          ├→ Execution Monitoring
                                     (From all skills) ──┘

Throughout: AI-Native Strategy (parallel, continuous)
           Market Intelligence (updates, continuous)
           ATLAS Report Template (synthesizes all, Day 6)
```

---

## Skill Dependency Matrix

```
SKILL DEPENDENCY MATRIX (X = one depends on other / P = can run parallel)

                    | SP | HT | RFG | GS | GTM | FS | CAP | PI | TS | OM | PT | CM | EM | AI | M&A | ATLAS |
--------------------|----|----|-----|----|----|----|----|----|----|----|----|----|----|-----|-----|-------|
Strategy Partner    |    | P  | →   | P  | P  | P  | P  | P  | P  | P  | P  | P  | P  | P   | P   | ←    |
Hyp. Testing        | ←  |    | ←   | ←  | ←  | ←  |    | ←  | ←  |    |    |    |    | P   |     |      |
Rumelt Forge        | ←  |    |     | P  | P  | P  | ←  | P  | P  | →  | →  | →  | →  | P   | →   | ←    |
Growth Strategy     | ←  | ←  |     |    | P  | →  |    | ←  |    |    |    |    |    | P   |     | ←    |
GTM Strategy        | ←  | ←  |     | ←  |    | ↔  |    | ↔  |    |    |    |    |    | P   |     | ←    |
Financial Strategy  | ←  | ←  | ←   | ←  | ↔  |    | →  | ←  |    |    |    |    |    | P   |     | ←    |
Capital & Resource  |    |    | ←   |    |    | ←  |    |    |    |    | ←  |    |    | P   |     | ←    |
Product Innovation  | ←  | ←  |     | ←  | ↔  | ←  |    |    | →  |    |    |    |    | P   |     | ←    |
Technology Strategy | ←  | ←  |     |    |    | ←  |    | ↔  |    | ←  | ←  |    |    | P   |     | ←    |
Operating Model     | ←  |    | ←   |    |    |    |    |    | ←  |    | →  | →  |    | P   |     | ←    |
People & Talent     | ←  |    | ←   |    |    |    | ←  |    | ←  | ←  |    | →  |    | P   |     | ←    |
Change Management   |    |    | ←   |    |    |    |    |    |    | ←  | ←  |    | ←  | P   |     | ←    |
Execution Monitoring| ←  | ←  | ←   | ←  | ←  | ←  | ←  | ←  | ←  | ←  | ←  | ←  |    | ←   | ←   | ←    |
AI-Native Strategy  | P  | P  | P   | P  | P  | P  | P  | P  | P  | P  | P  | P  | P  |     | P   | P    |
M&A & Corp Dev      | ←  |    | ←   |    |    | ←  |    |    |    |    |    |    |    | P   |     | ←    |
ATLAS Report        | ←  |    | ←   | ←  | ←  | ←  | ←  | ←  | ←  | ←  | ←  | ←  | ←  | P   | ←   |      |

Legend:
→ = This skill (row) DEPENDS ON skill (column) / must wait for output
← = Skill (column) depends on this skill (row) / this skill must complete first
↔ = Bidirectional dependency / both must iterate and converge
P = Can run PARALLEL (no dependency)
blank = No interaction
```

---

## Escalation Thresholds by Skill

| Skill | Finding Type | Escalation Threshold | Escalation Target | Action |
|---|---|---|---|---|
| **Strategy Partner** | Diagnosis confidence | <70% | Request more analysis | Strategy Partner must do additional research before handing to Rumelt Forge |
| **Rumelt Forge** | Coherence score | <70/100 | Request additional diagnostics | Rumelt must request more analysis from Strategy Partner (gaps identified) |
| **Rumelt Forge** | Bad Strategy Detector | <8/16 | Major revision needed | Strategy is too risky; recommend significant kernel changes |
| **Growth Strategy** | Market opportunity size | <70% on TAM | Validate with primary research | Do not lock revenue targets until market size confidence ≥70% |
| **GTM Strategy** | CAC assumption | <70% confidence | Validate with Financial benchmarks | GTM must reconcile CAC with Financial's market benchmarks (Financial wins) |
| **Financial Strategy** | Unit economics | <70% confidence | Validate with Growth/GTM | Financial model must be grounded in validated growth/GTM assumptions |
| **Product Innovation** | PMF assessment | <70% confidence | Validate with Hypothesis Testing | Do not lock feature roadmap until PMF clarity ≥70% |
| **Technology Strategy** | Tech feasibility | <70% confidence | Escalate to Operating Model | Org/hiring changes may be needed to execute tech roadmap |
| **Operating Model** | Org structure impact | <70% confidence | Escalate to Change Management | Major org change requires higher change readiness before proceeding |
| **People & Talent** | Hiring feasibility | <70% confidence | Escalate to Capital & Resource Strategy | May require expanded budget/timeline to hire needed talent |
| **Change Management** | Adoption forecast | <70% confidence | Extend timeline or increase enablement | Do not proceed with aggressive timeline if adoption forecast <70% |

