# Coherence Test
> Reference: rumelt-strategy-forge | Phase: Validation | Authority: Rumelt (2011)

---

## Overview
The Coherence Test is the final validation gate. A strategy that fails this test is not a strategy—it's a wish list. All 11 tests must pass or receive remediation before execution. This reference operationalizes Rumelt's coherence framework with methodology, calibration, and repair protocols.

---

## Part 1: The 11 Tests with Methodology & Examples

### INTERNAL COHERENCE (Foundation: 35% weight)

#### Test 1: Reinforcement Bias
**Methodology**: For each action, ask: does it *increase* the effectiveness of other actions, or is it independent? Map dependencies.
- **Passing Example**: Netflix's streaming + original content + algorithm. Streaming data trains algorithm. Algorithm drives viewing. Originals create exclusive content. Virtuous cycle.
- **Failing Example**: Kodak diversifying into pharmaceutical imaging while defending film. Actions don't reinforce—they dilute focus and resources.
- **Remediation**: Remove independent actions. Redraw the strategy around *dependent* pieces that amplify each other.

#### Test 2: Tradeoff Clarity
**Methodology**: For each action, identify what you *don't* do. State the tradeoff explicitly. If you can't, you're trying to do everything.
- **Passing Example**: Ikea chooses: "We will NOT offer delivery, assembly, customization, or luxury materials." Clear sacrifices enable flat-pack, self-assembly, low-cost model.
- **Failing Example**: "We'll compete on quality, cost, speed, and customization." All four = no choice = no strategy.
- **Remediation**: Force ranking of 3-5 core objectives. Write the "We will NOT" statement. Eliminate scope creep.

#### Test 3: Resource Concentration
**Methodology**: Plot your budget/talent allocation. Is 60%+ concentrated in the crux (the one thing that breaks if it fails)? Or evenly distributed?
- **Passing Example**: SpaceX 80% of engineering talent on reusable rockets (the crux). Everything else is secondary.
- **Failing Example**: Spreading budget evenly across 8 business units, each underfunded. No unit has critical mass to execute.
- **Remediation**: Identify the crux. Reallocate until 60-75% of resources flow there. Accept underfunding elsewhere.

#### Test 4: Sequencing Deliberateness
**Methodology**: List your 5-7 key moves in order. For each, ask: *must* this precede the next? Are prerequisites explicit?
- **Passing Example**: Amazon: (1) build logistics infrastructure, (2) establish Prime, (3) add marketplace, (4) launch AWS. Each unlocks the next.
- **Failing Example**: Launching product, scaling marketing, and building compliance simultaneously with no sequencing logic.
- **Remediation**: Create Gantt-style dependency map. Reorder moves. Delay initiatives until prerequisites are met.

---

### EXTERNAL COHERENCE (Advantage: 30% weight)

#### Test 5: Competitive Asymmetry
**Methodology**: Ask a thoughtful competitor to predict your next three moves. If they're right, you're not creating asymmetry.
- **Passing Example**: Southwest's point-to-point model (not hub-and-spoke) surprised competitors who couldn't match it without dismantling existing hubs. True asymmetry.
- **Failing Example**: "We'll improve customer service and cut costs." Every competitor will say the same. No surprise = no advantage.
- **Remediation**: Invert your constraint. What if you *required* a different competitive position? Build strategy around that inversion.

#### Test 6: Environmental Alignment
**Methodology**: Identify 2-3 major environmental shifts (tech, regulation, culture, demographics). Does your strategy swim *with* them or against them?
- **Passing Example**: Tesla's EV strategy aligns with regulatory emissions tightening and cultural shift to sustainability. Environmental currents help.
- **Failing Example**: Blockbuster's late-stage focus on retail stores as streaming emerged. Swimming hard against the current.
- **Remediation**: Rewrite strategy to *exploit* the environmental shift, not resist it. Make the environment your ally, not your obstacle.

#### Test 7: Competitive Targeting
**Methodology**: Identify the specific weakness or inertia you're targeting. Is it *this* competitor's weakness, not a generic statement?
- **Passing Example**: Disruptors target incumbent cost structures (e.g., Tesla vs. Detroit's vertical integration). Specific target.
- **Failing Example**: "We'll be more innovative and customer-focused." Applies to no one's weakness in particular.
- **Remediation**: Name the competitor. Name their specific constraint (cost, regulation, organizational lag, installed base). Build strategy to exploit it.

---

### EXECUTION COHERENCE (Reality Check: 35% weight)

#### Test 8: Proximate Objective Feasibility
**Methodology**: What's the first testable milestone in 6 months? Can you reach it with current resources? If not, you're starting at the wrong place.
- **Passing Example**: Stripe's first objective: process payments in 7 lines of code. Feasible. Provable. Built on existing tech (web APIs).
- **Failing Example**: "Become the market leader." Too distant. Not testable in 6 months with available resources.
- **Remediation**: Break first objective into smaller chunks. Find the one you can achieve with existing capabilities. Success builds credibility for next phase.

#### Test 9: Organizational Capability Alignment
**Methodology**: List required capabilities for success. For each, ask: do we have it? Hire it? Or does it require transformation we don't have capacity for?
- **Passing Example**: Apple's retail model required new capabilities (store design, customer service), but they could hire and train. Capability gap was closeable.
- **Failing Example**: Hardware company pivoting to AI-driven services requiring 5 years of R&D and a culture it doesn't have. Capability gap is existential.
- **Remediation**: Tier capabilities as: have it, can acquire it, must build it. Only bet on "must build" if you have the transformation capacity. Otherwise, partner or delay.

#### Test 10: Feedback & Measurement
**Methodology**: Define how you'll know in 6-12 months if this is working. Be specific: which metrics? What threshold triggers pivot vs. double-down?
- **Passing Example**: "Customer acquisition cost <$30 and 3-month payback." Measurable. Decision-forcing. Clear go/no-go.
- **Failing Example**: "Improve customer satisfaction." Vague. Won't force learning or course-correction.
- **Remediation**: Replace soft metrics with hard ones. Add leading indicators (effort, engagement) not just lagging ones (revenue). Define the threshold for abandonment.

#### Test 11: Abandonment Conditions
**Methodology**: Pre-commit: at what point do you stop? Under what conditions do you pivot or exit? Write it *now*, before emotion clouding sunk costs.
- **Passing Example**: "If monthly churn exceeds 5% for 2 quarters, we pivot distribution model." Pre-committed. Unemotional.
- **Failing Example**: No pre-committed exit. Will escalate resource investment indefinitely, hoping to force success.
- **Remediation**: Define 2-3 abandonment thresholds now. Write them in the strategy document. Commit to reviewing them quarterly, not emotionally deciding at each crisis.

---

## Part 2: Weighted Scoring System

Not all tests equal. Weight distribution reflects dependencies:

| Test | Category | Weight | Rationale |
|------|----------|--------|-----------|
| 1. Reinforcement | Internal | 10% | Foundation; weak here breaks everything |
| 2. Tradeoff Clarity | Internal | 10% | Without this, tests 3-7 collapse |
| 3. Concentration | Internal | 8% | Amplifies coherence above; affects execution |
| 4. Sequencing | Internal | 7% | Tactical; less foundational than 1-2 |
| 5. Asymmetry | External | 12% | Core competitive advantage test |
| 6. Alignment | External | 10% | Environmental tailwind vs. headwind |
| 7. Targeting | External | 8% | Specificity; amplifies asymmetry |
| 8. Proximate Objective | Execution | 12% | Reality check; can you even start? |
| 9. Capability Alignment | Execution | 11% | Execution bottleneck |
| 10. Measurement | Execution | 7% | Learning & course-correction |
| 11. Abandonment | Execution | 5% | Sunk-cost prevention; less critical if 10 is strong |

**Scoring**: Y=full weight, P=50% weight, N=0 weight. Aggregate to /100.

**Thresholds**:
- **≥85**: Release to execution. Strategy is coherent.
- **70-84**: Remediate before execution. Specific tests fail; cascade likely.
- **<70**: Reject. Fundamental incoherence. Rebuild from architecture.

---

## Part 3: Calibration Examples

### Strategy A: 4/11 (Score: ~32/100) — Rejected
**Strategy**: "We'll enter the enterprise software market, compete on ease-of-use, offer lower pricing than Salesforce, expand globally, and also build a mobile app."

- Test 1 (Reinforcement): N. Easy-to-use doesn't reinforce lower pricing. Neither reinforces global expansion.
- Test 2 (Tradeoff): N. No "we will NOT" statement. Trying to do everything.
- Test 3 (Concentration): N. Resources spread across product, pricing, geography, mobile. No crux.
- Test 4 (Sequencing): N. All initiatives simultaneous. No prerequisite logic.
- Test 5 (Asymmetry): N. Salesforce can copy all moves. No surprise.
- Test 6 (Alignment): P. Enterprise consolidation is real, but strategy doesn't leverage it.
- Test 7 (Targeting): N. Generic "compete better." Not targeting Salesforce's specific inertia.
- Test 8 (Proximate Objective): N. "Enter market" is too broad. No testable 6-month milestone.
- Test 9 (Capability): N. Requires enterprise sales (don't have), global ops (don't have), mobile engineering (don't have).
- Test 10 (Measurement): N. No metrics defined.
- Test 11 (Abandonment): N. No exit criteria.

**Verdict**: Fundamental incoherence. Not a strategy; a brainstorm. Reject and restart.

---

### Strategy B: 7/11 (Score: ~72/100) — Remediate
**Strategy**: "Become the low-cost leader in residential solar by owning vertically integrated supply chain (manufacturing, installation, financing). Start in Southwest US (high sun, high permitting velocity). First objective: 500 installations in 18 months with <$3/watt installed cost. Measure success by cost and customer acquisition cost."

- Test 1 (Reinforcement): Y. Manufacturing, installation, financing all reinforce (financing enables customers, installation drives volume, manufacturing drives unit cost).
- Test 2 (Tradeoff): Y. Clear: "We will NOT compete on installation speed or premium finishes. We will NOT enter commercial or utility-scale."
- Test 3 (Concentration): Y. 80% resources in Southwest Southwest, 60% of capital in supply chain integration.
- Test 4 (Sequencing): Y. Manufacturing (6m) → Installation ops (3m) → Financing (6m). Prerequisites explicit.
- Test 5 (Asymmetry): P. Vertical integration is hard to copy, but competitors can match over time. Not fully asymmetric.
- Test 6 (Alignment): Y. Regulatory push toward renewables, customer cost sensitivity rising.
- Test 7 (Targeting): Y. Targeting incumbent installers' fragmentation and high margins. Specific weakness.
- Test 8 (Proximate Objective): Y. 500 installations + <$3/watt is testable, achievable.
- Test 9 (Capability): P. Have installation experience, but manufacturing and financing are new capabilities. Can hire, but transformation risk.
- Test 10 (Measurement): Y. Cost per watt and CAC are clear metrics.
- Test 11 (Abandonment): N. No explicit exit condition if costs don't reach $3/watt or CAC stays above threshold.

**Score**: 72/100. **Remediation**: Add abandonment condition: "If cost doesn't reach <$3.50/watt by month 18, pivot to model-3PL model and exit manufacturing." Add explicit capability plan for financing hiring. Then release.

---

### Strategy C: 10/11 (Score: ~98/100) — Release
**Strategy**: "Build B2B2C embedded finance for SMB merchants via point-of-sale integration. Crux: merchant data from POS enables credit decisioning at transaction level. Year 1: integrate with 3 POS vendors (Square, Toast, Shopify). Target: 10k merchants, $50M in financed volume, 8% default rate. Measurement: monthly cohort default rates and repeat financing rate (target 40%). Abandon if default >12% or repeat rate <20% by month 12."

- Test 1 (Reinforcement): Y. POS data enables credit, financing drives merchant loyalty, loyalty drives more transactions (generating data).
- Test 2 (Tradeoff): Y. "We will NOT compete on checkout speed or price. We will NOT finance inventory or equipment, only transaction-level working capital."
- Test 3 (Concentration): Y. 70% resources in transaction-level underwriting and POS integrations. Everything else secondary.
- Test 4 (Sequencing): Y. POS integrations (months 1-4) → underwriting model (2-6) → merchant launch (6-12).
- Test 5 (Asymmetry): Y. Transaction-level data is hard to replicate. Competitors lack real-time decisioning. True asymmetry.
- Test 6 (Alignment): Y. SMB digital adoption accelerating, demand for working capital rising, fintech tailwinds.
- Test 7 (Targeting): Y. Targets Square/Shopify's transaction friction and underserved merchant credit.
- Test 8 (Proximate Objective): Y. 10k merchants, $50M in financed volume are testable, achievable with 1 POS vendor MVP.
- Test 9 (Capability): Y. Have credit scoring, merchant data; POS integration within engineering scope.
- Test 10 (Measurement): Y. Cohort default rates, repeat rate, volume all quantified.
- Test 11 (Abandonment): Y. Default >12% and repeat <20% are hard gates for pivot.

**Verdict**: **Release to execution.** Strategy is coherent, externally differentiated, executionally grounded.

---

## Part 4: The Coherence Cascade

Failing one test often cascades to others:

```
Test 2 Failure (Unclear Tradeoffs)
  ↓
Test 1 Failure (Actions don't reinforce; no unified strategic logic)
  ↓
Test 3 Failure (Resources spread thin, no concentration on crux)
  ↓
Test 4 Failure (No sequencing logic; all moves simultaneous)
  ↓
Test 8 Failure (First objective bloated; requires all moves at once, infeasible)
  ↓
Test 9 Failure (Can't execute because you need too many capabilities)
```

**Alternative Cascade**:
```
Test 5 Failure (Not asymmetric; predictable)
  ↓
Test 7 Failure (Targeting generic competitors, not specific weakness)
  ↓
Test 6 Failure (Swimming against environmental current; requires exceptional strength)
  ↓
Test 9 Failure (Exceptional strength is capability you don't have)
```

**Rule**: If you fix Test 2 (tradeoff clarity), Tests 1, 3, 4 often follow. If you fix Test 5 (asymmetry), Tests 6 and 7 align. Prioritize cascade origins.

---

## Part 5: Integration with Strategy Partner

| Gate | Owner | Checks | Relation |
|------|-------|--------|----------|
| **Quality Gate** | Strategy Partner (SP) | Analytical rigor, data quality, assumption validity | Input validation |
| **Coherence Test** | This framework | Strategic logic, internal consistency, execution feasibility | Output validation |

**Workflow**:
1. SP validates that your analysis is sound (data, logic, reasoning).
2. Coherence Test validates that your *strategy* is coherent (does it hang together?).
3. Together: sound analysis + coherent strategy = executable strategy.

SP catches "you're analyzing the wrong thing." Coherence Test catches "your analysis is right, but your strategy doesn't hold together."

---

## Part 6: Coherence Repair Protocol

**If score <70**: Use this repair sequence.

1. **Fix Test 2 (Tradeoff Clarity)** first. Write "We will NOT" statements. Forces clarity on all downstream tests.
2. **Then Test 1 (Reinforcement)**. Redraw strategy around mutually-reinforcing actions. Delete independent ones.
3. **Then Test 5 (Asymmetry)**. Is this differentiating? Or copying competitors? If copying, reposition.
4. **Then Test 8 (Proximate Objective)**. Can you actually start? If not, find a smaller first step within your capability.
5. **Then Test 11 (Abandonment)**. Force pre-commitment to exit conditions. Prevents sunk-cost escalation during repair.
6. **Retest all 11**. Cascade fixes often unlock others. Re-score and verify threshold crossed.

**Time allocation**: 2 days on Tests 2, 1, 5. 1 day on Tests 8, 11. Then re-test.

---

## Part 7: Output Template

```markdown
## Coherence Assessment: [Strategy Name]

**Weighted Score**: __/100  |  **Status**: [RELEASE / REMEDIATE / REJECT]

### Test Scores
| Test | Result | Weight | Score | Notes |
|------|--------|--------|-------|-------|
| 1. Reinforcement | Y/P/N | 10% | __ | |
| 2. Tradeoff | Y/P/N | 10% | __ | |
| 3. Concentration | Y/P/N | 8% | __ | |
| 4. Sequencing | Y/P/N | 7% | __ | |
| 5. Asymmetry | Y/P/N | 12% | __ | |
| 6. Alignment | Y/P/N | 10% | __ | |
| 7. Targeting | Y/P/N | 8% | __ | |
| 8. Proximate | Y/P/N | 12% | __ | |
| 9. Capability | Y/P/N | 11% | __ | |
| 10. Measurement | Y/P/N | 7% | __ | |
| 11. Abandonment | Y/P/N | 5% | __ | |

### Cascade Risk
- [Test X] failure cascades to [Tests Y, Z]
- Recommend fixing [Test A] first

### Remediation Plan (if <85)
1. [Action] (Owner, timeline)
2. [Action] (Owner, timeline)
3. Retest by [date]

### Release Criteria Met?
- ✓ All tests Y, or P with documented mitigation
- ✓ Cascade risks addressed
- ✓ Proximate objective feasible within 6 months
- ✓ Abandonment conditions pre-committed
```

---

## Closing

The Coherence Test is not negotiable. It answers the hardest question: does this strategy actually *work*, or is it an incoherent pile of good ideas? No strategy ships without a passing score. Cascading failures are your warning system—fix them before they sink execution.

---

**Last Updated**: 2026-03-09 | **Authority**: Richard Rumelt, *Good Strategy, Bad Strategy*
