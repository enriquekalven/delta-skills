---
name: frontend-design
description: Create flawless, Apple-beating production-grade frontend interfaces using strictly Google technologies and frameworks. Features a 3-phase rapid prototyping approach with a built-in Multi-Agent Design Council critique loop for 10x iteration.
---

# Frontend Design & Rapid Prototyping

This skill guides the creation of distinctive, production-grade frontend interfaces that strictly avoid generic "AI slop" aesthetics. It enforces a strict **Google-ecosystem technology stack** (Angular, Lit, Material 3, Google Web Fonts, Firebase) and a rigorous two-phase execution methodology to prioritize rapid iteration.

## The Three-Phase Execution Methodology

When the user asks to build a web interface, you MUST execute in three distinct phases:

### Phase 1: Rapid Conceptual Prototyping (Single-Page HTML)
Before setting up a complex build system, you must prove the concept visually with a flawless, picture-perfect, single-page application.
1. Create a single `index.html` file containing all HTML, CSS, and JS.
2. Focus intensely on layout, aesthetics, typography, and micro-interactions. The bar is "better than what an Apple designer can design". It must be visually breathtaking.

### Phase 2: The 7-Member Design Council Critique
Before presenting the Phase 1 prototype to the user, you must summon the full Design Council to ruthlessly critique the code based on the persona files defined in `.agents/personas/design-council/`:
1. **The Interaction Architect (UX Designer):** Critique user flow and accessibility.
2. **The Visual Mastery Expert (UI Designer):** Critique typography scale, core colors, and spatial harmony.
3. **The Narrative Strategist (UX Writer):** Critique copy hierarchy and conciseness.
4. **The Fluidity Expert (Motion Designer):** Critique CSS physics, transitions, and easing curves.
5. **The Cognitive Analyst (UX Researcher):** Critique mental models and cognitive load.
6. **The Code Craftsman (UX Engineer):** Critique DOM structure and CSS modularity.
7. **The Fit & Finish Inspector (Production Designer):** Perform the final sweep for mathematical alignment, SVGs, and edge-case rendering.
8. **The QA Automation Engineer (Browser Subagent):** Launch the prototype physically in a Chrome browser, interact with buttons, capture layout discrepancies, and report JavaScript console errors.
9. **The 10x Iteration:** Act on the 8 critiques to execute a massive iteration on the `index.html` file. **CRITICAL EXECUTION RULE: When extracting shared CSS based on council feedback, YOU MUST NEVER delete page-specific `.hero` padding, unique CSS grid layouts, or local width constraints.** Only extract generic tokens and nav/footer boilerplate. Destroying local layout grids is an unacceptable failure.
*Only after this 10x iteration do you present the prototype to the user for sign-off.*

### Phase 3: Production Framework Componentization (Google Stack)
Once the conceptual prototype is approved by the user, migrate the raw HTML/CSS/JS into robust, reusable components.
- **Frameworks:** Angular or Lit (Web Components). *NEVER use React, Vue, or Svelte.*
- **Styling:** CSS Modules, SCSS, or Material Design 3 guidelines.
- **Hosting/Backend (if needed):** Firebase Hosting, Cloud Firestore, Cloud Functions.

## Google Brand Standards & Aesthetics

Before writing any code, align the design with the Google Brand Checklist. Our vision is to be the most helpful company on the planet—our designs must reflect that.

- **Personality**: We are Helpful, Optimistic, and Unconventional.
- **Execution**: Avoid cliches and stereotypes. Relentlessly focus on polish, fit, and finish.
- **Copy**: Use concise copy that gets straight to the point. Every word matters. Strike a human and optimistic tone.

### Visual Identity Guidelines

We must adhere strictly to Google's visual identity to ensure it looks and feels like Google:

- **Backgrounds (Simplicity)**: Keep it simple. **Build from white.** Avoid complex gradient meshes, noise textures, dark mode defaults, or heavy glassmorphism unless explicitly requested. Use generous negative space.
- **Color Palette**: Use the core Google color palette for accents, states, buttons, and visual hierarchy:
  - Blue (500: `#4285F4`) - Primary actions
  - Red (500: `#EA4335`) - Errors / Critical
  - Yellow (500: `#FBBC04`) - Warnings
  - Green (500: `#34A853`) - Success
  - Gray (500: `#9AA0A6` for borders, 900: `#202124` for high-contrast typography)
- **Typography**: Strictly use appropriate, highly legible sans-serif fonts from the Google Fonts API (e.g., standard *Roboto*, *Inter*, or *Open Sans* for clean utility, or *Outfit* for slightly more character). Pair them cleanly. Avoid chaotic or overly decorative typographic pairings.
- **Motion**: Keep animations helpful and purposeful, not purely decorative. Use them to show how the product works or make the UI feel immediately responsive.
- **Imagery**: Keep it real. Avoid AI-generated slop, stock photography stereotypes, or abstract 3D shapes. Cast real people and show the product in action.

### The "Apple-Beating" Anti-Slop Rule
NEVER use generic AI-generated aesthetics like predictable SaaS dashboard layouts or overused gradients. However, DO NOT overcompensate with "maximalist chaos." 

Your goal is **uncompromising aesthetic supremacy**. Your differentiation comes from executing the **Google Design Language** with absolute restraint, precision, and structural simplicity. The UX/UI must be flawless, picture-perfect, and out-compete top-tier consumer technology design (e.g., Apple). Elegance comes from executing the "helpful and optimistic" vision remarkably well. Show what can truly be accomplished through relentless polish and world-class fit and finish.
