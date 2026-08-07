---
name: rm-slop
description: >
  Audit technical documentation, PRDs, and architecture guides to strip out AI slop, corporate buzzwords, and hand-wavy claims.
  Translates complex jargon into plain-English, human-grounded technical instructions with falsifiable rules.
  Triggers on: "rm-slop", "rm slop", "humanize docs", "anti ai slop", "strip buzzwords", "plain english docs", "clean technical documentation", "de-jargon".
---

# Plain-English & Anti-AI Slop Documentation Auditor (`rm-slop`)

Audits technical documentation, PRDs, and guides to detect and eliminate **AI Slop**—corporate filler, non-falsifiable hand-waving, hallucinated package names, and impenetrable jargon—replacing them with grounded, plain-English instructions that non-technical stakeholders and first-time developers easily understand.

---

## 1. AI Slop Audit Taxonomy

The auditor scans documents against 4 specific failure modes:

| Category | AI Slop Signal | Plain-English Replacement Rule | Example |
| :--- | :--- | :--- | :--- |
| **A. Corporate Fluff & Buzzwords** | Empty hype terms (*"seamless synergistic paradigm"*, *"holistic transformation"*, *"cutting-edge"*). | Delete the filler or state the exact technical mechanism. | *"Seamless integration"* ➔ *"Connects via REST API over TLS 1.3"* |
| **B. Non-Falsifiable Hand-Waving** | Unmeasurable adjectives (*"ultra-scalable"*, *"highly robust"*, *"enterprise-grade"*). | Replace with concrete, measurable metrics or technical rules (`IF <condition> THEN <action>`). | *"Ultra-scalable service"* ➔ *"Autoscales from 1 to 50 Cloud Run instances under 200ms target latency"* |
| **C. Hallucinated Aliases & Bad Packages** | Invalid package names, fake imports, or incorrect release statuses. | Replace with PyPI/npm verified identifiers and exact GCP product names. | *"@google/adk"* ➔ *"google-adk PyPI package"* |
| **D. Passive Bureaucratic Jargon** | Passive voice and bloated process language (*"Verification shall be facilitated by stakeholders"*). | Convert to direct, active-voice developer instructions. | *"Verification shall be facilitated"* ➔ *"Run `pytest` and confirm 100% pass rate"* |

---

## 2. 3-Pass De-Slop Execution Protocol

### Pass 1: Automated Slop & Buzzword Scan
Run the automated scanner CLI tool:
```bash
python3 skills/rm-slop/scripts/scan_doc_slop.py --file <target_doc.md>
```
Review the generated **Plain-English Score** and line-by-line findings.

### Pass 2: Technical Grounding & Falsification Check
For every section in the document:
1. **Enforce Falsifiable Rules**: Ensure every claim follows the `IF <measurable condition> THEN <action>` pattern.
2. **Verify Product Identifiers**: Check that all package names (`google-adk`, `fastapi`, `pydantic`), imports, and GCP product names are 100% accurate.
3. **Insert Code Examples**: Replace hand-wavy descriptions with copy-pasteable code snippets or concrete JSON schemas.

### Pass 3: Humanization & Plain-English Polish
1. **Read-Aloud Test**: Read each paragraph aloud. If a sentence sounds like a corporate marketing press release, rewrite it in conversational plain English.
2. **Use Plain Analogies**: Explain complex multi-tier architectural choices using simple real-world metaphors.
3. **Active Voice Enforcement**: Convert all passive sentences into direct imperative instructions (*"Do X"*, *"Run Y"*).

---

## 3. Output Schema: De-Slop Audit Report (`docs/DE_SLOP_AUDIT.md`)

When auditing a document, output the findings and revised plain-English document to `docs/DE_SLOP_AUDIT.md`:

```markdown
# AI Slop & Plain-English Audit Report

- **Target Document**: `docs/PRD.md`
- **Initial Plain-English Score**: 65 / 100
- **Final De-Slopped Score**: 98 / 100

## 1. Summary of Slop Stripped

| Line | Original AI Slop | Plain-English Grounded Revision | Rationale |
| :--- | :--- | :--- | :--- |
| 14 | *"Seamlessly leverage a holistic paradigm"* | *"Connects via REST API to Cloud Run"* | Replaced generic fluff with exact technical protocol |
| 28 | *"Ultra-scalable enterprise architecture"* | *"Autoscales from 1 to 20 instances under 100ms latency"* | Replaced unmeasurable hand-waving with concrete metric |
| 45 | *"Install `@google/adk`"* | *"Install PyPI package `google-adk`"* | Fixed hallucinated package identifier |

## 2. Revised Plain-English Document

[Insert full revised document here with clear headings, active voice, and grounded metrics]
```
