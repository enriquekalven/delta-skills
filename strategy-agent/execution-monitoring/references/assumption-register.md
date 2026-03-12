# Assumption Register with Invalidation Triggers

## Template for Every Material Assumption

Create a living register of every assumption the strategy depends on:

```
ASSUMPTION REGISTER
═════════════════════════════════════════
Assumption: [Statement of what we assume to be true]
  Category: [Market / Product / Org / Financial / Competitive]
  Impact if wrong: [MATERIAL / MODERATE / LOW]
  Current confidence: [H / M / L]

  Validation method: [How we'll test it]
  Validation timeline: [When we'll know]

  Current evidence: [What supports this assumption?]
  Red flag: [What would invalidate it?]
    - Trigger 1: [Observable event], probability [H/M/L]
    - Trigger 2: [Observable event], probability [H/M/L]

  Invalidation consequence: [What breaks if this is false?]
  Course correction if triggered: [Adjust / Pivot / Kill]
═════════════════════════════════════════
```

## Example Assumption with Triggers

```
Assumption: CAC will decline 20% as we optimize channel mix
  Category: Financial
  Impact if wrong: MATERIAL (payback period becomes >18mo, funding question)
  Current confidence: M (one channel optimized; others not tested)

  Validation method: Weekly CAC tracking across all channels through Q2
  Validation timeline: Week 12 (middle of Q2) will show trend

  Current evidence: Channel A CAC down 15% from month 1 to month 3
  Red flag: Channel B CAC increasing (saw +8% this month)
    - If overall CAC >$6K by week 8: HIGH probability model is broken
    - If channel B acquisition volume >30% of total: HIGH probability drag

  Invalidation consequence: Growth trajectory requires capital investment 6 months earlier
  Course correction if triggered: Reduce channel B investment, accelerate channel A testing
```

## Assumption Register Best Practices

1. **Maintain 8-15 material assumptions** — Not more (unmanageable), not fewer (not rigorous enough)
2. **Update weekly with evidence** — Add new data, update confidence levels, track trigger status
3. **Flag confidence shifts immediately** — If confidence drops materially, escalate
4. **Name invalidation consequences** — Be explicit about what breaks if this assumption is wrong
5. **Assign course correction path** — When trigger fires, what's the decision? (Adjust / Pivot / Kill)

## Weekly Assumption Validation Update

```
ASSUMPTION VALIDATION UPDATE (Weekly)
═════════════════════════════════════════
Assumption: [Statement]
  Previous confidence: [H / M / L]
  New evidence this week: [What did we learn?]
  Confidence shift: [H → M / M → L / no change / confidence raised]

  Trigger status:
    - Trigger 1 (probability was H/M/L): [Occurred / Not occurred / Probability updated to [H/M/L]]
    - If trigger occurred: root cause analysis → course correction decision

  Next validation checkpoint: [Week #]

Example:
Assumption: CAC will decline as we scale marketing
  Previous confidence: M
  New evidence: September CAC $5.2K, October CAC $5.4K (trending UP not down)
  Confidence shift: M → L

  Trigger status:
    - Trigger "CAC >$6K" (probability was M): Has not occurred yet, but probability raised to H

  Next checkpoint: Week 12 (end of Q4), decision point on marketing spend
═════════════════════════════════════════
```

## Confidence Level Guidelines

- **HIGH:** Strong evidence supports assumption, multiple data points confirm, low bias risk
- **MEDIUM:** Some evidence; assumption plausible but not fully validated, moderate uncertainty
- **LOW:** Weak evidence; assumption increasingly doubtful, needs urgent validation or course correction
