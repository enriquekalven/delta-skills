# Experiment Design Template

Standardized format for designing and executing lean tests.

## EXPERIMENT DESIGN MATRIX

```
HYPOTHESIS: [Statement of what we're testing]
  Null hypothesis: Assume [opposite]. We test to refute or support.

PRIMARY METRIC (What evidence is this test?)
  Metric: [Specific, measurable outcome]
  Target: [Success threshold] (what confidence does this achieve?)
  Why this metric? [Why does this metric validate the hypothesis?]

EXPERIMENT DESIGN
  Methodology: [Survey / Prototype / Experiment / Pilot]
  Population: [Who we're testing with?]
  Sample size: [#] (confidence level: [90% / 95%])
  Timeline: [Duration of test]
  Cost: $[Total budget]

  Experimental design:
    Control: [What's the baseline?]
    Treatment: [What are we changing?]
    Randomization: [How are we assigning subjects?]

SUCCESS CRITERIA
  Metric achieves [threshold]? → Hypothesis supported, confidence [from X% to Y%]
  Metric misses [threshold]? → Hypothesis challenged, confidence [from X% to Y%]
  What if result is inconclusive? → Next test: [What do we do]

RISK MITIGATION
  What could confound this test? [External factor]
  How are we controlling for it? [Approach]

DECISION TREE
  IF metric > [threshold], confidence rises to Y% → PROCEED to next hypothesis
  IF metric < [threshold], confidence drops to Z% → PIVOT (redesign value prop / segment / channel)
  IF metric is inconclusive → RETRY with [design change] or TEST at scale

RESOURCE REQUIREMENTS
  People: [Roles needed]
  Time: [Weeks]
  Capital: $[Budget]
  Data/Tools: [What we need access to]
```

## Common Experiment Types

### Customer Interview / Anecdote
```
Sample size: 2-3 customers (targeted segment)
Timeline: 1 week
Cost: $1-2K (incentives + researcher time)

Success metric: Pattern emerges (same need/pain mentioned 2+ times)
Success threshold: 2/3 mention core problem; willing to try solution
```

### Survey Validation
```
Sample size: 20-50 respondents (representative of target segment)
Timeline: 1-2 weeks
Cost: $3-5K (tool + incentives + analysis)

Success metric: % who say they'd consider / buy / use
Success threshold: 40%+ conversion rate at proposed price/feature set
```

### MVP / Prototype Test
```
Sample size: 50+ active users
Timeline: 2-8 weeks
Cost: $10-50K (build + recruitment + support)

Success metric: Day-7 retention, activation rate, NPS
Success threshold: [Your target metric] ≥ [Your target threshold]
```

### Pricing Experiment
```
Sample size: 100+ prospects
Timeline: 3-4 weeks
Cost: $8-15K

Success metric: Conversion rate by price point
Success threshold: 40%+ conversion at target price

Methodology: Show 3-5 price points; measure willingness to pay
```

### Pilot / Paid Campaign
```
Sample size: 50+ customer conversions
Timeline: 4-8 weeks
Cost: $20-100K

Success metric: CAC, LTV, payback period
Success threshold: CAC ≤ $[target]; LTV/CAC ≥ 3:1; payback ≤ 12 months

Methodology: Real paid campaign; measure acquisition efficiency
```

## Experiment Execution Checklist

**SETUP PHASE**
- [ ] Recruit subjects / participants (Target: [#], recruited: [#])
- [ ] Build MVP / create survey / set up experiment
- [ ] Train facilitators / test setup
- [ ] Baseline metric captured (if applicable)

**EXECUTION PHASE**
- [ ] Participants onboarded (Completed: [#] / [#])
- [ ] Weekly progress check (Completion: [%])
- [ ] Interim data review (any surprises? Adjust?)

**ANALYSIS PHASE**
- [ ] Data collected and cleaned
- [ ] Primary metric calculated: [Value] (target was [threshold])
- [ ] Statistical significance assessed (if applicable)
- [ ] Qualitative feedback synthesized

**DECISION POINT**
- Result: [Metric value] vs. [Target]
- Hypothesis: [SUPPORTED / CHALLENGED / INCONCLUSIVE]
- Confidence change: [X% → Y%]
- Decision: [PROCEED / RETRY / PIVOT / KILL]

**LEARNING CAPTURE**
- What surprised us? [Observation]
- What did we get wrong? [Assumption fail]
- What's next? [Next test or next action]
