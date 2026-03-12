# Course Correction Decision Logic

## Decision Tree When Metrics or Assumptions Trigger

When a KPI or assumption triggers:

```
COURSE CORRECTION LOGIC
═════════════════════════════════════════

TRIGGER: [KPI crosses RED or MATERIAL assumption confidence drops to LOW]

Step 1: ROOT CAUSE DIAGNOSIS
  What happened? [Specific event or trend]
  Why did we miss? [Root cause analysis]
  Is this permanent or temporary? [Analyze trend]
  Did we miss the signal earlier? [Review weekly data]

Step 2: IMPACT ASSESSMENT
  Does this invalidate strategy? [Yes / Partially / No, tactical only]
  What changes if this is permanent? [Revised forecast]
  Options available: [List all viable paths]

Step 3: DECISION
  IF [Root cause is tactical] AND [Impact is MODERATE]
    → ADJUST (modify tactics, keep strategy intact)
    - Specific adjustment: [Action]
    - Resources required: [What]
    - Expected impact: [Revenue/metric improvement]
    - Timeline to effect: [When we'll see impact]

  IF [Root cause is structural] AND [Impact is HIGH]
    → PIVOT (change strategy, not abandoning but redirecting)
    - Previous strategy: [What we were doing]
    - New strategy: [What we're doing instead]
    - Rationale: [Why this is better]
    - Go/No-go gate: [When we decide if pivot is working]
    - Kill criteria: [What makes pivot fail]

  IF [Root cause invalidates core assumption] AND [Cannot pivot]
    → KILL (stop initiative, reallocate resources)
    - Reason: [Why we're stopping]
    - Learning: [What we're taking forward]
    - Resource reallocation: [Where they go next]
    - Post-mortem scheduled: [When]

Step 4: ESCALATION & DECISION
  Decision authority: [Who decides]
  Board communication: [What gets told to board]
  Team communication: [What gets told to organization]
  Confidence in new direction: [H / M / L]
═════════════════════════════════════════
```

## Trigger-Based Escalation Matrix

Define what merits what:

| Trigger | What Crosses | Decision Type | Escalation |
|---------|---|---|---|
| **KPI misses 2Q consecutive** | AMBER → RED → RED | ADJUST | Monthly exec review |
| **KPI misses 2 of 3 consecutive months** | AMBER → RED | PIVOT or KILL | Immediate board/exec conversation |
| **MATERIAL assumption drops to LOW confidence** | Confidence M → L | Assess / PIVOT | Immediate escalation |
| **Market condition changes materially** | Competitive move, TAM revised -50% | PIVOT or KILL | Immediate |
| **Key person leaves mid-execution** | Leadership Gap risk triggers | ADJUST or PIVOT | Immediate |
| **Capital runway <3 months** | Cash constraint | Reallocation or KILL | Immediate |

## Monthly Course Correction Review

```
MONTHLY COURSE CORRECTION REVIEW
═════════════════════════════════════════
Review period: [Month]
Overall health: [Strategy on pace / Small adjustments needed / Major pivot needed]

Adjustments from last month:
  - [Adjustment 1] — Expected impact: [Metric improvement] — Actual impact: [What happened] — Assessment: [Worked / Partially / Failed]
  - [Adjustment 2] — Expected impact: [Metric improvement] — Actual impact: [What happened] — Assessment: [Worked / Partially / Failed]

New adjustments this month:
  1. [Adjustment] — Rationale: [Why] — Expected impact: [Quantified] — Timeline: [When to effect]
  2. [Adjustment] — Rationale: [Why] — Expected impact: [Quantified] — Timeline: [When to effect]

Assumptions status (any confidence shifts?):
  - [Assumption]: Confidence [H/M/L] (no change) OR changed from [X] to [Y] because [evidence]

Confidence on forecast:
  - Revenue: [X]% probable to hit annual target (was [Y]% last month)
  - Timeline: [X weeks ahead / on pace / Y weeks behind] where earlier forecast had [Z]

Next decision gates:
  - Gate 1: [Specific metric/assumption check] — Date: [Week #] — Decision: [Adjust / Pivot / Kill if [condition]]
═════════════════════════════════════════
```

## Post-Mortem Protocol (If Strategy Fails)

When a strategy doesn't work (pilot invalids, market proves forecast wrong, assumption breaks):

```
STRATEGY POST-MORTEM
═════════════════════════════════════════
Strategy name: [What we were trying to do]
Timeline: [Weeks 1-12]
Outcome: [FAILED / PARTIAL / PIVOTED]
Final metric: [What we measured vs. what we got]

ROOT CAUSE ANALYSIS
  What did we assume would be true? [Core assumption]
  What actually happened? [Reality]
  When did we know it was broken? [Week # when signal emerged]
  Why didn't we course-correct earlier? [What we missed]

FAILURE MODE ANALYSIS
  What surprised us? [What we didn't see coming]
  What signals did we ignore? [Data we had but dismissed]
  What would we have done differently? [Hindsight]

LESSONS EXTRACTED (2-3 only)
  Lesson 1: [Specific learning] — Owner to implement in next strategy: [Who]
  Lesson 2: [Specific learning] — Owner to implement in next strategy: [Who]
  Lesson 3: [Specific learning] — Owner to implement in next strategy: [Who]

RESOURCE REALLOCATION
  People freed up: [Roles] → Reallocated to: [Next initiative]
  Capital unspent: $[X] → Reserved for: [What]

CONFIDENCE FOR NEXT CYCLE
  Do we understand why this failed? [Yes / Partially / No]
  Can we extract 2-3 lessons to prevent this again? [Yes / Partially / No]
  Next strategy confidence: [H / M / L] because [basis]

Next strategy target: [What we're trying next]
═════════════════════════════════════════
```
