# Stitch MCP Tool Sequence, Sandbox Governance & Prompt Specification

## 1. TDL Sandbox Governance & Single-Project Rule (`gcc-delta-tdl`)

When prototyping before customer GCP access is cleared (Stage 1) or testing synthetic patterns (Stage 2):
1. **Single-Project Rule (`gcc-delta-tdl`) — from the guide:** "all custom prototypes must be built inside a single, consolidated Argolis project" so other TDLs can access, reuse and enhance assets. Project ID `gcc-delta-tdl`.
2. **Data boundary — from the guide:** use synthetic data to move fast early; switch to real data only when feasibility is the question, and never "touch real customer data without going through the access/governance process". Never paste customer PII/PHI into Stitch or AI Studio prompts.
3. **Resource hygiene — repo recommendation (not in the guide):** label prototype Cloud Run services, Vertex endpoints and buckets (`owner`, `engagement`, `stage=prototype`) and scale to zero or delete after the demo/spike.

---

## 2. Stitch MCP Tool Execution Order

| Step | MCP Tool Name | Required Arguments | Purpose |
|---|---|---|---|
| **1** | `mcp_StitchMCP_create_project` | `title`: string | Initializes a Stitch workspace and returns `projectId`. |
| **2** | `mcp_StitchMCP_generate_screen_from_text` | `projectId`: string, `prompt`: string, `deviceType`: `"DESKTOP"` \| `"MOBILE"` | Generates initial screen(s) from a structured specification prompt (§3). |
| **3** | `mcp_StitchMCP_get_screen` | `projectId`: string, `screenId`: string | Retrieves generated screen metadata, DOM structure, and screenshot URI for inspection. |
| **4a** | `mcp_StitchMCP_edit_screens` | `projectId`: string, `selectedScreenIds`: string[], `prompt`: string | Applies targeted layout, token, or field edits to existing screens. |
| **4b** | `mcp_StitchMCP_generate_variants` | `projectId`: string, `selectedScreenIds`: string[], `prompt`: string, `variantCount`: number | Explores alternative layout arrangements (e.g., split-pane vs. tabbed drawer). |

---

## 3. Structured Stitch Prompt Template

Always structure `prompt` arguments for `generate_screen_from_text` and `edit_screens` with explicit layout, HITL role controls, data, and token constraints:

```text
ROLE & SCREEN PURPOSE:
Desktop enterprise workbench for <User Role> acting as <HITL Role: Reviewer | Prompt Curator | Approver> executing <CUJ Goal>.

PROTOTYPE HYPOTHESIS BEING TESTED:
"We believe an agent can <do action X> on <inputs Y> at <quality/latency threshold Z>."

LAYOUT STRUCTURE:
- Top bar (56px height, #ffffff, 1px bottom border): App title, active record ID, status pill, and user profile.
- Summary KPI strip (4 metric cards in a 4-column grid, 16px gap): <Metric 1>, <Metric 2>, <Metric 3>, <Metric 4>.
- Main split workspace (2 columns, 55% / 45% width, 24px gap):
  - Left pane: Structured data table with confidence pills, AI reasoning trace summary, and HITL action toolbar.
  - Right pane: Source PDF/log evidence viewer with highlighted bounding-box citation callouts.

DESIGN TOKENS (Delta Brand & UI Guidelines, SKILL.md §4):
- Primary: #4285f4 | Accents: #ea4335, #fbbc05, #34a853 | Neutrals: #ffffff, #f8f9fa, #eeeeee, #b7b7b7, #797979, #434343, #000000
- Font: Google Sans (Google Sans Text for body; tabular-nums for figures)
- One primary CTA ("<Specific Verb + Object>"); secondary action as an outlined button ("<Escalation / Override Action>")

REALISTIC SYNTHETIC DOMAIN DATA TO RENDER:
- <Row 1 with exact synthetic IDs, dollar amounts, timestamps, and confidence score>
- <Row 2 with exact synthetic IDs, dollar amounts, timestamps, and confidence score>
```
