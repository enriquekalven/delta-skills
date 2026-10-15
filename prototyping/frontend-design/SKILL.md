---
name: frontend-design
description: >
  Build production-ready web UI prototypes and Material 3 / Angular / Lit components following
  Google Design System tokens, an 8-point UI & accessibility verification checklist, and browser
  validation. Trigger when asked to build a web prototype, design a frontend UI, or componentize
  an interface using Google web technologies.
metadata:
  version: '2.0'
---

# Frontend Design & Rapid Prototyping (`frontend-design`)

This skill builds clean, responsive web interfaces in three concrete phases: **Single-File HTML/CSS/JS Prototype → 8-Point UI & Accessibility Audit → Component Handoff (Angular / Lit)**.

---

## Visual & Design System Tokens (Google Material 3 Baseline)

Use explicit CSS custom properties so every prototype is consistent and maintainable:
- **Surfaces & Backgrounds:** `--bg-primary: #ffffff`, `--bg-secondary: #f8f9fa`, `--surface-border: #dadce0`
- **Typography (`Roboto` / `Inter`):** `--text-primary: #202124` (contrast >= 12:1), `--text-secondary: #5f6368` (contrast >= 4.5:1), `--font-mono: 'Roboto Mono', monospace`
- **Semantic Accents:**
  - Primary Action: `#1a73e8` (hover `#1557b0`, subtle fill `#e8f0fe`)
  - Success / Passed Gate: `#1e8e3e` (subtle fill `#e6f4ea`)
  - Warning / HITL Review: `#f9ab00` (text `#b06000`, subtle fill `#fef7e0`)
  - Error / Blocked: `#d93025` (subtle fill `#fce8e6`)
- **Spacing Scale (8px grid):** `4px`, `8px`, `16px`, `24px`, `32px`, `48px`

---

## Three-Phase Execution Procedure

### Phase 1: Self-Contained Interactive Prototype (`index.html`)
1. Build a single, runnable `index.html` containing semantic HTML5 (`<header>`, `<main>`, `<nav>`, `<section>`, `<dialog>`), scoped CSS variables, and interactive JavaScript state (tab switching, filtering, modal/drawer inspection, form validation).
2. Populate the UI with realistic domain data from the engagement (`docs/PRD.md` or `docs/baseline_kpis.json`)—never use `Lorem ipsum` or `TODO` placeholders.

### Phase 2: 8-Point UI & Accessibility Verification
Before presenting the prototype, audit and fix the code against all 8 checks in [ui-review-checklist.md](references/ui-review-checklist.md):
1. **Task Flow & Primary CTA Hierarchy**
2. **Typography Scale & Color Contrast (WCAG AA >= 4.5:1)**
3. **Microcopy & Data Density**
4. **Interactive States (`:hover`, `:focus-visible`, `:disabled`, loading/empty)**
5. **Cognitive Load & Information Grouping**
6. **DOM Semantics & Responsive Grid (`320px` to `1440px`)**
7. **Alignment, Spacing & Icon Consistency**
8. **Zero Runtime Console Errors & Keyboard Navigation**

### Phase 3: Production Componentization (Angular or Lit)
When the user approves the Phase 1/2 prototype, extract the verified layout and state into modular **Angular** or **Lit (Web Components)** with typed props/events and Material Design 3 tokens.

---

## References & Examples

- [8-Point UI & Accessibility Review Checklist](references/ui-review-checklist.md): Concrete engineering rubric for auditing HTML/CSS/JS prototypes before delivery.
- [Worked Example: Commercial Claims HITL Review Console Prototype](examples/agent-ops-console-prototype.md): Complete runnable `index.html` prototype for the Acme Claims FNOL Adjuster Workbench plus its completed 8-point verification scorecard.
