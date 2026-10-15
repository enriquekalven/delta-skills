---
name: stitch-design
description: >
  Run rapid prototyping and generative UI design for Delta engagements using the official
  TDL Prototyping Guide (3-stage prototyping lifecycle, 7-step hypothesis-to-mini-eval loop,
  gcc-delta-tdl sandbox governance, AI Studio vs. Agent Studio vs. ADK matrix) and the Stitch
  MCP Server (create_project, generate_screen_from_text, edit_screens, generate_variants,
  get_screen). Trigger when asked to prototype an agent UI, run a feasibility spike, or
  generate/iterate on screens with Stitch MCP.
metadata:
  version: '3.0'
---

# TDL Prototyping & Stitch Generative UI Design (`stitch-design`)

This skill combines the official **TDL Prototyping Guide** (3-stage prototyping lifecycle, 7-step hypothesis loop, and GCP sandbox governance) with the **Stitch MCP Server** workflow to build high-signal prototypes and UI workbenches grounded in `docs/PRD.md` and `docs/CUJ_MAP.md`.

> [!IMPORTANT]
> **Prerequisite:** sections 4–5 call `mcp_StitchMCP_*` tools, which exist only if a Stitch MCP server is configured in your agent's MCP settings under the server name `StitchMCP` (tool names are `mcp_<server>_<tool>`). If it is not installed, the lifecycle, playbook and governance in sections 1–3 still apply — do the screen generation manually in the Stitch web app and paste the exported HTML/CSS into `docs/STITCH_PROTOTYPE.md`. Do not pretend the tools ran.

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
   - Check pre-built accelerators first before writing from scratch:
     - `go/agentcatalog` & `go/demos` (production reference agents)
     - `go/ge` (Gemini Enterprise connectors)
     - `go/delta-apf` (Agentic Prototyping Framework)
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

## 4. Three-Phase Stitch MCP UI Execution Procedure

### Phase 1: Project Initialization & Initial Screen Generation
1. Read `docs/PRD.md` and `docs/CUJ_MAP.md` to extract the target persona, primary CUJ task flow, HITL role (`Reviewer / Prompt Curator / Approver`), data fields, and status states.
2. Create or select a Stitch project using `mcp_StitchMCP_create_project`.
3. Construct a structured generation prompt specifying layout grid, Material 3 color tokens (`#ffffff` surface, `#f8f9fa` background, `#1a73e8` primary action, `#202124` typography), domain fields, and interactive controls, then invoke `mcp_StitchMCP_generate_screen_from_text` (see [stitch-mcp-workflow.md](references/stitch-mcp-workflow.md)).

### Phase 2: Screen Audit & Targeted Refinement (`edit_screens` / `generate_variants`)
Inspect the generated screen via `mcp_StitchMCP_get_screen` and evaluate it against five concrete criteria:
1. **Primary CTA & Task Hierarchy:** One primary `#1a73e8` button per screen; clear visual path through the CUJ.
2. **Domain Fidelity:** Real field labels, status badges (`PASS`, `HITL REVIEW`, `BLOCKED`), and citations from the PRD—zero placeholder `Lorem ipsum`.
3. **Information Density:** Maximum 4 summary KPIs in the header strip; split-pane or drawer layout for document/trace inspection.
4. **Contrast & Legibility:** High-contrast `#202124` primary text and `#5f6368` secondary labels on light surfaces; `Roboto` / `Inter` typography.
5. **Edge & Empty States:** Explicit UI states for low-confidence warnings, loading skeletons, and human escalation actions.

Apply fixes using `mcp_StitchMCP_edit_screens` (for targeted layout/component fixes) or `mcp_StitchMCP_generate_variants` (to compare layout alternatives).

### Phase 3: Handoff & Component Extraction
Retrieve the approved screen metadata and HTML/CSS structure via `mcp_StitchMCP_get_screen` and document the hypothesis, mini-eval results, screen inventory, Stitch IDs, and component breakdown in `docs/STITCH_PROTOTYPE.md` (or hand off to [frontend-design](../frontend-design/SKILL.md) for production implementation).

---

## 5. References & Examples

- [Stitch MCP Tool Sequence, Sandbox Governance & Prompt Specification](references/stitch-mcp-workflow.md): Parameter contracts, `gcc-delta-tdl` sandbox governance rules, and prompt templates for Stitch MCP tools.
- [Worked Example: Commercial Underwriting Triage Portal via Stitch MCP](examples/stitch-claims-portal-walkthrough.md): End-to-end Stitch MCP tool trace (`create_project` → `generate_screen_from_text` → `edit_screens` → `get_screen`) and resulting `docs/STITCH_PROTOTYPE.md` handoff specification.
