---
name: stitch-design
description: >
  Run rapid prototyping and generative UI design for Delta engagements using the official
  TDL Prototyping Guide (3-stage prototyping lifecycle, 7-step hypothesis-to-mini-eval loop,
  gcc-delta-tdl sandbox governance, AI Studio vs. Agent Studio vs. ADK matrix), the official
  Delta Brand & UI Guidelines (Google Material 3 color palette, Google Sans/Roboto typography,
  co-branding rules), and the Stitch MCP Server. Trigger when asked to prototype an agent UI,
  apply Delta brand guidelines, run a feasibility spike, or generate screens with Stitch MCP.
metadata:
  version: '3.2'
---

# TDL Prototyping, Brand Guidelines & Stitch Generative UI (`stitch-design`)

This skill codifies **Toolbox Asset #15 (TDL Prototyping Guide)** and **Toolbox Asset #13 (Delta Brand & UI Guidelines)** alongside the **Stitch MCP Server** workflow to build high-signal prototypes and UI workbenches grounded in `docs/PRD.md` and `docs/CUJ_MAP.md`.

> [!IMPORTANT]
> **Prerequisite:** sections 5–6 call `mcp_StitchMCP_*` tools, which exist only if a Stitch MCP server is configured in your agent's MCP settings under the server name `StitchMCP` (tool names are `mcp_<server>_<tool>`). If it is not installed, the lifecycle, playbook, and brand guidelines in sections 1–4 still apply — do the screen generation manually in the Stitch web app or build a single-file HTML/CSS/JS prototype verified against [`ui-review-checklist.md`](references/ui-review-checklist.md). Do not pretend the tools ran.

---

## Quick-Start & File Contract

| Attribute | Specification |
| :--- | :--- |
| **Engagement Phase & Timebox** | **Stage 1 Discovery (`2–4 hours`, synthetic) & Stage 2 Feasibility (`2–5 days`, Golden Dataset)** |
| **Time-to-Market (TTM) Compression** | **28.0h manual $\rightarrow$ 3.5h skill-guided (`87.5%` faster interactive prototype & mini-eval validation)** |
| **Reads (Inputs)** | `docs/PRD.md`, `docs/CUJ_MAP.md` |
| **Writes (Outputs)** | `docs/STITCH_PROTOTYPE.md` (plus single-file `index.html` workbench or Stitch MCP screens) |
| **Value Realization Linkage** | De-risks the hardest technical/UX assumption in `<4 hours` with a **10–30 item mini-eval scorecard** before committing Sprint 1 engineering capacity |

---

## 1. The 3-Stage TDL Prototyping Lifecycle (guide §1–3)

Match prototype fidelity, data governance, and timebox strictly to the engagement stage:

| Stage | Timing | Primary Goal | Data Rule | Timebox & Output |
|---|---|---|---|---|
| **Stage 1: Qualification / Discovery Vibe-Coding** | Pre-Kickoff / Week 0–1 | Align with customer on *what* problem we are solving and make the future-state CUJ tangible. | **100% Synthetic / Mocked Data** in `gcc-delta-tdl` (Argolis) or local environment. Zero customer PII/regulated data. | **2–4 hours.** Clickable Stitch UI or AI Studio vibe-coded app; disposable by default. |
| **Stage 2: Feasibility Studies** | Weeks 1–2 (Foundations) | Prove *whether* the hardest technical/reasoning bottleneck works on the customer's real data distribution. | **Sanitized or Approved Customer Golden Dataset (10–30 items)** inside approved sandbox/customer project. | **Up to 2 weeks.** Working ADK/Agent Studio spike + **10–30 item mini-eval scorecard**. |
| **Stage 3: Iterative Build & Demo Spikes** | Weeks 3–10 (Build Sprints) | De-risk specific technical implementations inside the production codebase (net-new tool schema, latency bottleneck, HITL drawer UX). Guide: prototyping activity "naturally diminishes" here. | Production-grade customer data and live API endpoints in the customer environment. | Timebox per spike (guide gives no fixed duration; a day or two is typical). Validated pattern graduated into the production codebase or discarded. |

---

## 2. The 7-Step TDL Prototyping Playbook Loop

Every prototype or spike must execute this 7-step loop—never ship a prototype based on "demo vibes" alone:

1. **Write a One-Sentence Hypothesis:**
   - Format: *"We believe an agent can **[do action X]** on **[inputs Y]** at **[roughly quality/latency threshold Z]**."*
2. **Pick the Data Mode & Environment:**
   - Synthetic data $\rightarrow$ shared sandbox (`gcc-delta-tdl` on Argolis) or Stitch MCP / AI Studio.
   - Real customer data $\rightarrow$ strictly inside the customer-approved GCP project (`*-nonprod`) after Part III Developer Clearance.
3. **Set a Hard Timebox:**
   - `2–4 hours` for Stage 1 UI/vibe-coding; `2–5 days` (max 2 weeks) for Stage 2 technical feasibility spikes.
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
| **Best Stage** | **Stage 1:** Discovery vibe-coding & multi-screen UI alignment (2–4 hrs) | **Stage 2:** Rapid prompt/tool prototyping & Vertex grounding tests (1–3 days) | **Stage 2 & Stage 3:** Complex multi-agent DAGs, custom deterministic tools, & production graduation |
| **Environment** | Argolis / Browser (`gcc-delta-tdl` single-project rule) | Shared Sandbox (`gcc-delta-tdl`) or Customer GCP Console | Local IDE / Cloud Workstations $\rightarrow$ Vertex Agent Engine or Cloud Run |
| **Data Allowed** | **100% Synthetic / Public Only** | Synthetic in `gcc-delta-tdl`; Customer data in Customer GCP Project | Customer data in Customer VPC-SC Project |
| **Graduation Path** | Export HTML/CSS tokens (`mcp_StitchMCP_get_screen`) & prompts into ADK repo | Export agent config / prompts to ADK Python code | Direct hardening into production repo |

---

## 4. Delta Brand & UI Guidelines (Toolbox Asset #13)

Apply the official Google Cloud Delta brand tokens across all prototypes, slide decks, and customer-facing UI workbenches:

| Token Category | Token Name / Usage | Hex / Specification |
|---|---|---|
| **Primary Brand Colors** | Google Blue (Primary CTA / Links) · Google Green (Success / Passed Gate) · Google Yellow (Warning / HITL Review) · Google Red (Error / Blocked) | `#4285F4` · `#34A853` · `#FBBC04` · `#EA4335` |
| **Secondary / Interactive Accents** | Dark Blue (Hover/Active) · Dark Green · Dark Yellow · Dark Red | `#1967D2` · `#188038` · `#F29900` · `#C5221F` |
| **Surfaces & Neutrals** | Surface Primary (`#FFFFFF`) · Background Secondary (`#F8F9FA`) · Border (`#DADCE0`) · Text Secondary (`#5F6368`, contrast $\ge 4.5:1$) · Text Primary (`#202124`, contrast $\ge 12:1$) | Material Design 3 light-surface baseline |
| **Typography** | **Headlines / Titles:** `Google Sans` (`Inter` fallback) · **Body / UI Labels:** `Roboto` · **Code / Traces / Metrics:** `Roboto Mono` | 8px spacing grid (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`) |
| **Co-Branding Lockup** | Header lockup: `Google Cloud × [Customer Name]` with equal visual weight and a `1px solid #DADCE0` vertical divider (`16px` horizontal padding). | Never distort customer logos or mix unapproved accent colors |

---

## 5. Three-Phase Stitch MCP UI Execution Procedure

1. **Phase 1 — Project Initialization & Initial Screen Generation:** Read `docs/PRD.md` and `docs/CUJ_MAP.md` to extract persona, primary CUJ task flow, HITL role (`Reviewer / Prompt Curator / Approver`), and status states. Invoke `mcp_StitchMCP_create_project` and `mcp_StitchMCP_generate_screen_from_text` (or build a single-file Material 3 HTML workbench if Stitch MCP is unavailable).
2. **Phase 2 — Screen Audit & Targeted Refinement:** Audit against [ui-review-checklist.md](references/ui-review-checklist.md) (one `#4285F4` primary CTA per screen, real domain labels, max 4 summary KPIs, WCAG contrast, explicit HITL/empty/error states).
3. **Phase 3 — Handoff & Component Extraction:** Document the 1-sentence hypothesis, 10–30 item mini-eval results, throwaway-vs-graduate decision, and component breakdown in `docs/STITCH_PROTOTYPE.md`.

---

## 6. Customer Sign-Off & Quality Gate

| Gate Criterion | Approve When | Reject If |
| :--- | :--- | :--- |
| **Hypothesis & 10–30 Mini-Eval** | States a testable 1-sentence hypothesis, runs a **10–30 example mini-eval**, and records an explicit **Throwaway vs. Graduate** decision. | Ships a prototype on "demo vibes" without testing against 10–30 representative examples. |
| **Sandbox Data Segregation** | Stage 1 prototypes in `gcc-delta-tdl` use **100% synthetic data**; real customer data never leaves the approved customer GCP project. | Uploads regulated customer PII/PHI/PCI into a shared Argolis sandbox or public tool. |
| **Delta Brand & HITL UX** | Applies Material 3 tokens (`#4285F4`, `#34A853`, `#FBBC04`, `#EA4335`, Google Sans/Roboto) and includes an interactive HITL review/escalation drawer. | Contains `Lorem ipsum` placeholders, dead buttons, or no UI path for low-confidence human review. |

---

## 7. References & Examples

- [Stitch MCP Tool Sequence, Sandbox Governance & Prompt Specification](references/stitch-mcp-workflow.md): Parameter contracts, `gcc-delta-tdl` sandbox governance rules, and prompt templates for Stitch MCP tools.
- [8-Point UI & Accessibility Review Checklist](references/ui-review-checklist.md): Engineering rubric for auditing HTML/CSS/JS prototypes before delivery.
- [Worked Example: Commercial Underwriting Triage Portal via Stitch MCP](examples/stitch-claims-portal-walkthrough.md): End-to-end Stitch MCP tool trace (`create_project` → `generate_screen_from_text` → `edit_screens` → `get_screen`) and resulting `docs/STITCH_PROTOTYPE.md` handoff specification.
- [Worked Example: Commercial Claims HITL Review Console Prototype](examples/agent-ops-console-prototype.md): Complete runnable `index.html` prototype for the Acme Claims FNOL Adjuster Workbench plus its completed 8-point verification scorecard.
