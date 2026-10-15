---
name: product-feature-md
description: >
  Generate, critique, or interview to produce a single-feature narrative specification
  (docs/product-feature.md) covering User Persona, Problem Statement, Ideal User Journey,
  Emotional Arc, and Ecosystem Stakeholder Impact before technical architecture is locked.
  Trigger when asked to draft a product-feature.md or user-experience feature brief. Do NOT
  trigger for full system PRDs (use product-md) or technical design docs (use specification-engineer).
metadata:
  version: '5.1'
---

# Single-Feature Narrative Specification (`product-feature-md`)

This skill produces a focused user-and-journey feature specification (`docs/product-feature.md`) that aligns product, design, and engineering on **who** the feature serves, **what friction** it removes, and **how the interaction flows** before implementation details are fixed.

---

## Mandatory 5-Section Structure

Every `docs/product-feature.md` deliverable must include these five sections (see [feature-spec-template.md](references/feature-spec-template.md)):

1. **User Persona:** Concrete identity, role, daily workflow context, and specific constraints (device, environment, time pressure).
2. **Problem Statement:**
   - **Trigger:** The exact event that initiates the need.
   - **Friction:** Why the current workflow is slow, error-prone, or frustrating.
   - **Consequence:** Measurable cost of failure (lost time, rework, SLA risk).
   - **Why Now:** Why solving this friction is urgent now.
3. **Ideal User Journey:** A numbered, step-by-step sequence (`1..N`) describing the end-to-end user experience from trigger to resolution, focusing on user intent and system feedback rather than low-level database or API mechanics.
4. **Emotional Arc:** A numbered progression of user states (`1..N`) mapping the shift from initial friction/anxiety to verification and completion.
5. **Stakeholder & Ecosystem Impact:**
   - **End Users:** Direct workflow improvement.
   - **Google Cloud / Platform:** Product adoption, trust, or consumption unlocked.
   - **Ecosystem Participants:** How Knowledge Creators, Skills Creators, and Application Developers extend or build upon the feature.

---

## Operational Modes

- **Mode 1 — Generate:** Convert rough discovery notes, transcripts, or feature ideas into a complete 5-section `docs/product-feature.md` document.
- **Mode 2 — Interview:** Ask 5 targeted discovery questions (Persona → Trigger & Friction → Ideal Flow → Confidence/Trust Shift → Ecosystem Leverage) before writing `docs/product-feature.md`.
- **Mode 3 — Critique:** Audit an existing feature brief against the Validation Checklist below and rewrite weak or generic sections.

---

## Validation Checklist

- [ ] Contains all 5 required sections (`User Persona`, `Problem Statement`, `Ideal User Journey`, `Emotional Arc`, `Stakeholder & Ecosystem Impact`).
- [ ] Persona names a specific role, environment, and operational constraint (never "a generic user").
- [ ] Problem Statement explicitly defines `Trigger`, `Friction`, `Consequence`, and `Why Now`.
- [ ] Ideal User Journey and Emotional Arc use ordered numbered steps (`1..N`).
- [ ] Stakeholder Impact explicitly addresses End Users, Google Business, Knowledge Creators, Skills Creators, and App Developers.

---

## References & Examples

- [Feature Specification Template](references/feature-spec-template.md): Blank Markdown/YAML structure for `docs/product-feature.md`.
- [Worked Example: Field Technician Hands-Free Defect Capture & Triage](examples/voice-capture-feature-spec.md): Complete `docs/product-feature.md` artifact showing all 5 sections filled out for an industrial field-service feature.
