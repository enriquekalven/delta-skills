---
name: stitch-design
description: >
  Run rapid prototyping and generative UI design for Delta engagements using the official
  TDL Prototyping Guide (3-stage prototyping lifecycle, 7-step hypothesis-to-mini-eval loop,
  gcc-delta-tdl sandbox governance, AI Studio vs. Agent Studio vs. ADK matrix), the official
  Delta Brand & UI Guidelines (Google brand color palette, Google Sans / Caveat Bold typography,
  co-branding rules), and the Stitch MCP Server. Trigger when asked to prototype an agent UI,
  apply Delta brand guidelines, run a feasibility spike, or generate screens with Stitch MCP.
metadata:
  version: '3.2'
---

# TDL Prototyping, Brand Guidelines & Stitch Generative UI (`stitch-design`)

This skill codifies **Toolbox Asset #15 (TDL Prototyping Guide)** and **Toolbox Asset #13 (Delta Brand & UI Guidelines)** alongside the **Stitch MCP Server** workflow to build high-signal prototypes and UI workbenches grounded in `docs/PRD.md` and `docs/CUJ_MAP.md`.

> [!IMPORTANT]
> **Prerequisite:** section 5 calls `mcp_StitchMCP_*` tools, which exist only if a Stitch MCP server is configured in your agent's MCP settings under the server name `StitchMCP` (tool names are `mcp_<server>_<tool>`). If it is not installed, the lifecycle, playbook, and brand guidelines in sections 1–4 still apply — do the screen generation manually in the Stitch web app or build a single-file HTML/CSS/JS prototype verified against [`ui-review-checklist.md`](references/ui-review-checklist.md). Do not pretend the tools ran.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Phase 1 Foundations (Weeks 1–2):** Stage 2 Feasibility (up to 2 weeks, actual customer data); Stage 1 Workshop Prototyping (`2–4 hours`, 100% synthetic) runs earlier, during discovery |
| **Reads (Inputs)** | `docs/PRD.md`, `docs/CUJ_MAP.md` |
| **Writes (Outputs)** | `docs/STITCH_PROTOTYPE.md` (plus single-file `index.html` workbench or Stitch MCP screens) |

---

## 1. The 3-Stage TDL Prototyping Lifecycle (guide §1–3)

Match prototype fidelity, data governance, and timebox strictly to the engagement stage:

| Stage | Timing | Primary Goal | Data Rule | Timebox & Output |
|---|---|---|---|---|
| **Stage 1: Qualification / Discovery Vibe-Coding** | Pre-Kickoff / Week 0–1 | Align with customer on *what* problem we are solving and make the future-state CUJ tangible. | **100% Synthetic / Mocked Data** in `gcc-delta-tdl` (Argolis) or local environment. Zero customer PII/regulated data. | **2–4 hours.** Clickable Stitch UI or AI Studio vibe-coded app; disposable by default. |
| **Stage 2: Feasibility Studies** | Weeks 1–2 (Foundations) | Prove *whether* the hardest technical/reasoning bottleneck works on the customer's real data distribution. | **Sanitized or Approved Customer Golden Dataset (10–30 items)** inside approved sandbox/customer project. | **Up to 2 weeks.** Working ADK/Agent Studio spike + **10–30 item mini-eval scorecard**. |
| **Stage 3: Iterative Build & Demo Spikes** | Weeks 3–10 (Build Sprints) | De-risk specific technical implementations inside the production codebase (net-new tool schema, latency bottleneck, HITL drawer UX). Guide: prototyping activity "naturally diminishes" here. | Production-grade customer data and live API endpoints in the customer environment. | Timebox per spike (guide gives no fixed duration). Validated pattern graduated into the production codebase or discarded. |

---

## 2. The 7-Step TDL Prototyping Playbook Loop

Every prototype or spike must execute this 7-step loop—never ship a prototype based on "demo vibes" alone:

1. **Write a One-Sentence Hypothesis:**
   - Format: *"We believe an agent can **[do action X]** on **[inputs Y]** at **[roughly quality/latency threshold Z]**."*
2. **Pick the Data Mode & Environment:**
   - Synthetic data $\rightarrow$ shared sandbox (`gcc-delta-tdl` on Argolis) or Stitch MCP / AI Studio.
   - Real customer data $\rightarrow$ strictly inside the customer-approved GCP project (`*-nonprod`) after Part III Developer Clearance.
3. **Set a Hard Timebox:**
   - `2–4 hours` for Stage 1 UI/vibe-coding; up to 2 weeks for Stage 2 technical feasibility on actual customer data.
4. **Build the Smallest Thing That Tests the Hypothesis:**
   - Check pre-built accelerators first before writing from scratch (`go/agentcatalog`, `go/demos`, `go/ge`, `go/delta-apf`).
5. **Run a 10–30 Example Mini-Eval (Trust the Score, Not the Vibe):**
   - Run the prototype against 10–30 representative examples (including messy edge cases) and score pass/fail against the hypothesis threshold.
6. **Make an Explicit Throwaway-vs-Graduate Decision:**
   - **Throwaway (Default for Stage 1):** Keep the validated UX specs, prompts, and eval learnings; discard the vibe-coded scaffold.
   - **Graduate (Stage 2/3 ADK Code):** Refactor into the production repo only if built on the target ADK/Cloud Run stack with tests.
7. **Record Learnings in `docs/STITCH_PROTOTYPE.md` or `docs/TDD.md`:**
   - Document which prompts, tool schemas, and UI patterns passed or failed the mini-eval.

---

## 3. Tool & Sandbox Selection Matrix

| Dimension | Google AI Studio / Stitch MCP | Vertex AI Agent Studio (GCP Console) | Custom Code-First ADK (`google-adk`) |
|---|---|---|---|
| **Best Stage** | **Stage 1:** Discovery vibe-coding & multi-screen UI alignment (2–4 hrs) | **Stage 2:** Rapid prompt/tool prototyping & Vertex grounding tests | **Stage 2 & Stage 3:** Complex multi-agent DAGs, custom deterministic tools, & production graduation |
| **Environment** | Argolis / Browser (`gcc-delta-tdl` single-project rule) | Shared Sandbox (`gcc-delta-tdl`) or Customer GCP Console | Local IDE / Cloud Workstations $\rightarrow$ Vertex Agent Engine or Cloud Run |
| **Data Allowed** | **100% Synthetic / Public Only** | Synthetic in `gcc-delta-tdl`; Customer data in Customer GCP Project | Customer data in Customer VPC-SC Project |
| **Graduation Path** | Export HTML/CSS tokens (`mcp_StitchMCP_get_screen`) & prompts into ADK repo | Export agent config / prompts to ADK Python code | Direct hardening into production repo |

---

## 4. Delta Brand & UI Guidelines (Toolbox Asset #13)

Apply the official Google Cloud Delta brand tokens across all prototypes, slide decks, and customer-facing UI workbenches:

| Token Category | Usage (per the guide) | Hex / Specification |
|---|---|---|
| **Primary color** | Blue is the primary color for all branded materials; prefer a monochromatic scheme. | `#4285F4` (other palette blues: `#185ABC` · `#1C4587` · `#AECBFA` · `#EFF5FE` · `#E9F1FF`) |
| **Accents** | Original Google brand colors as accents only; solid rainbow colors are out. | `#EA4335` · `#FBBC05` · `#34A853` |
| **Neutrals** | Text color must contrast enough with its background. | `#FFFFFF` · `#F8F9FA` · `#EEEEEE` · `#B7B7B7` · `#797979` · `#434343` · `#000000` |
| **Typography** | Primary: `Google Sans` for all header and body text (`Google Sans Text` is also acceptable for body). Secondary: `Caveat Bold` for callouts and emphasis only; no other handwritten typefaces. | — |
| **Co-branding** | Use Google and delta logos together with extreme caution with external customers; official or promotional delta co-branding with the Google or GC logo needs branding-team approval. | — |

---

## 5. Three-Phase Stitch MCP UI Execution Procedure

1. **Phase 1 — Project Initialization & Initial Screen Generation:** Read `docs/PRD.md` and `docs/CUJ_MAP.md` to extract persona, primary CUJ task flow, HITL role (`Reviewer / Prompt Curator / Approver`), and status states. Invoke `mcp_StitchMCP_create_project` and `mcp_StitchMCP_generate_screen_from_text` (or build a single-file HTML workbench if Stitch MCP is unavailable).
2. **Phase 2 — Screen Audit & Targeted Refinement:** Audit against [ui-review-checklist.md](references/ui-review-checklist.md) (one primary CTA per screen, real domain labels, max 4 summary KPIs, WCAG contrast, explicit HITL/empty/error states).
3. **Phase 3 — Handoff & Component Extraction:** Document the 1-sentence hypothesis, 10–30 item mini-eval results, throwaway-vs-graduate decision, and component breakdown in `docs/STITCH_PROTOTYPE.md`.

---

## 6. References & Examples

- [Stitch MCP Tool Sequence, Sandbox Governance & Prompt Specification](references/stitch-mcp-workflow.md): Parameter contracts, `gcc-delta-tdl` sandbox governance rules, and prompt templates for Stitch MCP tools.
- [8-Point UI & Accessibility Review Checklist](references/ui-review-checklist.md): Engineering rubric for auditing HTML/CSS/JS prototypes before delivery.
- [Worked Example: Commercial Underwriting Triage Portal via Stitch MCP](examples/stitch-claims-portal-walkthrough.md): End-to-end Stitch MCP tool trace (`create_project` → `generate_screen_from_text` → `edit_screens` → `get_screen`) and resulting `docs/STITCH_PROTOTYPE.md` handoff specification.
- [Worked Example: Commercial Claims HITL Review Console Prototype](examples/agent-ops-console-prototype.md): Complete runnable `index.html` prototype for the Acme Claims FNOL Adjuster Workbench plus its completed 8-point verification scorecard.
