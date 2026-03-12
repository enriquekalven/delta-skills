# Signal Validation Protocol

## Validation Checklist

When a signal arrives, validate before acting:

```
SIGNAL VALIDATION CHECKLIST
═════════════════════════════════════════
Signal: [What we heard]
Source: [Where it came from]
Date: [When]

VALIDATION QUESTIONS
  [ ] Is this from a Tier 1 source? (If yes, confidence boost to HIGH)
  [ ] Can we cross-reference with another independent source? (If yes, confidence boost)
  [ ] What's the bias in the source? (Vendor bias? Competitive bias? Self-interest?)
  [ ] Is this recent or old information being resurfaced? (Recency check)
  [ ] Would this signal be visible in other places if true? (Why haven't we seen it elsewhere?)
  [ ] Is this a one-off or a pattern? (Is this part of bigger trend?)
  [ ] What's the opposite scenario? (Why might we be wrong about this?)

CONFIDENCE ASSESSMENT
  Initial credibility: [LOW / MEDIUM / HIGH]
  After validation: [LOW / MEDIUM / HIGH]
  Reason for change: [What we learned]

DECISION
  [ ] ACCEPT — Source is reliable, signal is clear → Add to intelligence
  [ ] MONITOR — Signal is interesting but unconfirmed → Track across more sources
  [ ] REJECT — Signal fails validation → Discard or tag as speculation
═════════════════════════════════════════
```

## Validation Best Practices

1. **Cross-Reference Obsessively** — Never trust a single source, especially for Tier 3-4 signals
2. **Name Your Bias** — Explicitly identify confirmation bias, availability bias, recency bias
3. **Check the Opposite** — What evidence would contradict this signal?
4. **Assess Recency** — Is this fresh or recycled news?
5. **Evaluate Visibility** — If true, shouldn't we see this elsewhere?

## Confidence Level Definitions

- **HIGH:** Tier 1 source OR 3+ independent sources confirm, low bias risk, clear implication
- **MEDIUM:** 2 Tier 1/2 sources confirm, moderate bias risk, implication needs interpretation
- **LOW:** Single Tier 3-4 source OR conflicting sources OR high bias risk, implications uncertain
