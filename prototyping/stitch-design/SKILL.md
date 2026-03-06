---
name: stitch-design
description: Create flawless, Apple-beating production-grade frontend interfaces using the Stitch MCP server for rapid generative prototyping and iterative refinement. Features a 3-phase approach leveraging AI generation and a built-in Multi-Agent Design Council critique loop for 10x iteration.
---

# Stitch Design & Generative Prototyping

This skill guides the creation of distinctive, production-grade frontend interfaces utilizing the power of the Stitch MCP Server for generative design. It enforces a rigorous three-phase execution methodology to prioritize rapid iteration while strictly adhering to Google Brand Standards.

## The Three-Phase Execution Methodology

When the user asks to design, generate, or build a web interface using Stitch, you MUST execute in three distinct phases:

### Phase 1: Rapid Conceptual Prototyping (Stitch Generation)
Instead of manually writing HTML/CSS/JS, you will use the Stitch MCP server to instantiate a concept based on the user's prompt.
1. Formulate a comprehensive text prompt describing the UI, emphasizing flawless, "Apple-beating" aesthetics, layout, typography, and intended micro-interactions.
2. If working on a new concept, use `mcp_StitchMCP_create_project` to get a `projectId`.
3. Use the `mcp_StitchMCP_generate_screen_from_text` tool, providing the `projectId` and your crafted `prompt`. Wait for this process to complete (it may take a few minutes).

### Phase 2: The 7-Member Design Council Critique
Before presenting the generated Phase 1 prototype as "final", you must conceptually summon the full Design Council to ruthlessly critique the generated output defined in `references/design-council/`:
1. **The Interaction Architect (UX Designer):** Critique user flow and accessibility.
2. **The Visual Mastery Expert (UI Designer):** Critique typography scale, core colors, and spatial harmony.
3. **The Narrative Strategist (UX Writer):** Critique copy hierarchy and conciseness.
4. **The Fluidity Expert (Motion Designer):** Critique visual rhythm and transition opportunities.
5. **The Cognitive Analyst (UX Researcher):** Critique mental models and cognitive load.
6. **The Code Craftsman (UX Engineer):** Critique structural logic of the design.
7. **The Fit & Finish Inspector (Production Designer):** Perform the final sweep for alignment, contrast, and edge-cases.

**The 10x Iteration via Stitch:** 
Act on the critiques to execute targeted improvements:
- If exploring broad alternatives based on critique, use `mcp_StitchMCP_generate_variants`.
- If applying specific refinements to a component or layout, use `mcp_StitchMCP_edit_screens` with the `projectId`, `selectedScreenIds`, and a highly specific `prompt` addressing the critique.

### Phase 3: Production Handoff
Once the generative iterations have satisfied the Design Council's high bar for Google-quality design:
1. Retrieve the final screen details using `mcp_StitchMCP_get_screen`.
2. Present the generated screen to the user for final sign-off.
3. Be prepared to extract specific components or layout strategies from the design if the user requests migration to robust frameworks (Angular, Lit).

## Google Brand Standards & Aesthetics

Before prompting Stitch, ensure your instructions align with the Google Brand Checklist. Our designs must be Helpful, Optimistic, and Unconventional.

- **Personality**: We are Helpful, Optimistic, and Unconventional.
- **Execution**: Relentlessly focus on polish, fit, and finish.

### Visual Identity Guidelines (For Prompting)

Instruct the Stitch model to adhere strictly to Google's visual identity:
- **Backgrounds**: Keep it simple. Build from white. Avoid complex gradient meshes, noise textures, and heavy glassmorphism unless explicitly requested. Use generous negative space.
- **Color Palette (Include in prompt constraints)**: Use the core Google color palette for accents, states, buttons, and visual hierarchy:
  - Blue (500: `#4285F4`) - Primary actions
  - Red (500: `#EA4335`) - Errors / Critical
  - Yellow (500: `#FBBC04`) - Warnings
  - Green (500: `#34A853`) - Success
  - Gray (500: `#9AA0A6` for borders, 900: `#202124` for high-contrast typography)
- **Typography**: Strictly request appropriate, highly legible sans-serif fonts (e.g., standard Google Fonts like *Roboto*, *Inter*, or *Open Sans* for clean utility, or *Outfit* for slightly more character). Pair them cleanly.
- **Imagery**: Instruct the model to avoid AI-generated slop, stock photography stereotypes, or abstract 3D shapes.

### The Anti-Slop Rule
In your prompts to Stitch, explicitly forbid generic SaaS dashboard layouts or overused gradients. Your goal is **uncompromising aesthetic supremacy**. Your differentiation comes from executing the **Google Design Language** with absolute restraint, precision, and structural simplicity. The UX/UI must be flawless, picture-perfect, and out-compete top-tier consumer technology design (e.g., Apple). Elegance comes from executing the "helpful and optimistic" vision remarkably well.
