# MVP/MLP Definition Protocol

For product and feature hypotheses, define minimum viable and lovable products.

## MVP/MLP SCOPE DEFINITION

```
CORE HYPOTHESIS: [What we're validating]
  Customer need: [What problem we're solving]
  Core value prop: [Essential capability]

MINIMUM VIABLE PRODUCT (MVP)
  Must have:
    1. [Feature 1 — core flow]
    2. [Feature 2 — core outcome]
    3. [Feature 3 — friction elimination]

  Must NOT have:
    1. [Feature X — nice-to-have]
    2. [Feature Y — optimization]

  Success metric: [Activation % / Retention Day X / NPS threshold]
  Success threshold: [Confidence rise from X% to Y%]

MINIMUM LOVABLE PRODUCT (MLP)
  MVP +
    1. [Polish / UX refinement]
    2. [Reliability / edge case handling]
    3. [Onboarding / documentation]

  Purpose: [Move from "people will use" to "people love"]
  Success metric: [NPS / Usage intensity / Referral]

TIMELINE & COST
  MVP build: [Weeks] — Cost: $[X]
  MVP test: [Weeks] — Cost: $[Y]
  MLP refinement: [Weeks] — Cost: $[Z]
  Total: [Weeks] — $[X+Y+Z]

KILL CRITERIA
  If MVP metric < [threshold]: Hypothesis fails, kill or pivot
  If MVP metric [threshold-20%]: Borderline, proceed to MLP with skepticism
  If MVP metric > [threshold]: Hypothesis supported, proceed to scale
```

## Example: Draft Document Feature with AI

```
CORE HYPOTHESIS: Users will draft documents 2+ times per week using AI suggestions (without collaboration)

MINIMUM VIABLE PRODUCT
  Must have:
    1. Draft a document with AI suggestion engine (suggests next sentence)
    2. Save draft and open later
    3. Basic formatting (bold, italics, lists)

  Must NOT have:
    1. Collaboration / real-time co-editing
    2. Sharing or version history
    3. Advanced formatting (tables, custom styles)
    4. AI model fine-tuning

  Success metric: Day-7 retention (% who return after first use)
  Success threshold: ≥60% Day-7 retention = supported; <50% = challenged

  Timeline: 3 weeks to build, 2 weeks to test with 30 users
  Cost: $15K

MINIMUM LOVABLE PRODUCT
  MVP + Real-time collaboration + Sharing + Version history

  Purpose: Move from "people will draft" to "teams will draft together"
  Success metric: NPS ≥ 40
  Timeline: 2 weeks additional build
  Cost: $10K additional

KILL CRITERIA
  If MVP Day-7 retention < 50%: Users aren't returning; rethink value prop or UI
  If MVP retention 50-60%: Borderline; proceed to MLP to test with collaboration
  If MVP retention > 60%: Hypothesis supported; proceed to scale with confidence
```

## Design Principles for MVP/MLP

### MVP Should
- Solve the core problem (nothing less)
- Be buildable in 2-4 weeks (not 6+ months)
- Have a clear success metric (not "let's see what happens")
- Be testable with 30-100 users (not 1000s)
- Have a kill criteria (if metric X < Y, hypothesis fails)

### MVP Should NOT
- Include everything you imagine customers might want
- Require perfect UX or design (functional is OK)
- Have all edge cases handled (you'll learn which matter)
- Include optimizations (do that in MLP or post-launch)

### MLP Should
- Polish MVP based on user feedback
- Add secondary features users requested
- Improve reliability and UX
- Prepare for scale (onboarding, support, documentation)

## Using MVP/MLP in Testing

```
Phase 1: MVP → Test with 30-50 users
  ├─ If success metric met → Confidence 40% → 75%
  ├─ If metric close → Proceed to MLP with conditions
  └─ If metric missed → Kill hypothesis or redesign value prop

Phase 2: MLP → Test with 100-200 users
  ├─ If success metric met → Confidence 75% → 85%+
  ├─ If NPS strong → Ready for scale
  └─ If feedback shows issues → Iterate once more before scale

Phase 3: Scale
  ├─ Launch to all customers
  ├─ Monitor metrics at scale
  └─ Add advanced features based on usage patterns
```
