# Worked Example: Commercial Underwriting SOV Triage Portal (`docs/STITCH_PROTOTYPE.md`)

## 1. Context & Target CUJ
- **Linked PRD:** Commercial Property Underwriting Co-Pilot (`CUJ-01: Reconcile Statement of Values (SOV) against Policy Appetite`)
- **Primary Persona:** Senior Commercial Property Underwriter reviewing a 42-location manufacturing schedule ($118.4M Total Insured Value).

---

## 2. Executed Stitch MCP Tool Trace

### Step 1: Create Project
```json
{
  "tool": "mcp_StitchMCP_create_project",
  "arguments": {
    "title": "Acme Commercial Property Underwriting Workbench"
  },
  "response": {
    "projectId": "stitch-proj-uw-2026-09"
  }
}
```

### Step 2: Generate Initial Screen (`mcp_StitchMCP_generate_screen_from_text`)
```json
{
  "tool": "mcp_StitchMCP_generate_screen_from_text",
  "arguments": {
    "projectId": "stitch-proj-uw-2026-09",
    "deviceType": "DESKTOP",
    "prompt": "Desktop enterprise underwriting workbench for reconciling a Commercial Property Statement of Values (SOV). Top bar (56px, #ffffff) with Submission #SUB-2026-4410 (Midwest Precision Stamping Inc.), status badge 'HITL REVIEW: TIV VARIANCE DETECTED' (#fef7e0 fill, #b06000 text), and primary CTA button 'Approve & Bind Quote Draft' (#1a73e8). 4-card KPI strip: Declared Total TIV ($118,400,000), Summed Schedule TIV ($121,150,000 — +2.3% variance flagged), FEMA High-Flood Locations (3 of 42), Historical 5-Yr Loss Ratio (31.4%). Main split workspace (55% left / 45% right, #f8f9fa canvas, #ffffff cards, 8px radius, #dadce0 borders): Left pane shows the 42-location normalized SOV table with columns Location ID, Address, Construction Class, Building TIV, Flood Zone, and Extraction Confidence badge. Right pane shows the source broker Excel/PDF viewer anchored to Row 14 (Peoria Plant #3) highlighting an unscheduled $2.75M warehouse annex."
  },
  "response": {
    "screenId": "scr-uw-sov-reconcile-v1",
    "status": "COMPLETED"
  }
}
```

### Step 3: Audit & Targeted Iteration (`mcp_StitchMCP_edit_screens`)
**Audit Findings on `scr-uw-sov-reconcile-v1`:**
1. Both `Approve & Bind Quote Draft` and `Request Broker Clarification` rendered as solid blue `#1a73e8` buttons (violates Check #1: single primary CTA).
2. Missing an explicit inline override reason selector when the underwriter accepts the $2.75M Peoria Plant #3 variance.

```json
{
  "tool": "mcp_StitchMCP_edit_screens",
  "arguments": {
    "projectId": "stitch-proj-uw-2026-09",
    "selectedScreenIds": ["scr-uw-sov-reconcile-v1"],
    "prompt": "1. Change 'Request Broker Clarification' in the top action bar to a secondary outlined button (#ffffff background, 1px #dadce0 border, #202124 text) so 'Approve & Bind Quote Draft' (#1a73e8) is the sole primary filled CTA. 2. In the right-hand Peoria Plant #3 variance card, add an inline select dropdown 'Override Reason Code' with options ['Confirmed via Endorsement #4', 'Exclude Annex from Binder', 'Hold for Broker Re-submission'] and an 'Apply Resolution' button."
  },
  "response": {
    "screenId": "scr-uw-sov-reconcile-v2",
    "status": "COMPLETED"
  }
}
```

---

## 3. Production Component Handoff Summary

| Screen ID | Screen Title | Target Angular Component | Bound API / BigQuery State |
|---|---|---|---|
| `scr-uw-sov-reconcile-v2` | SOV Reconciliation & Variance Workbench | `SovReconciliationWorkbenchComponent` | `GET /v1/submissions/{id}/sov`, `POST /v1/submissions/{id}/overrides` (`uw_audit.agent_decisions`) |
