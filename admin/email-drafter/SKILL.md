---
name: email-drafter
description: Triggers when the user asks to draft an email. Automatically calibrates tone, format, and structure based on the intended audience and strictly enforces the delta "Bottom-Line Up Front" email methodology.
---

# Email Drafter Skill

The `email-drafter` skill ensures that all outbound communication from the Head of Agentic AI Transformation adheres strictly to practitioner-led, MECE standards. It aggressively combats "email fatigue" by stripping out verbose paragraphs, corporate cliches, and "consultant fluff."

## Core Email Methodology (The "Bottom-Line Up Front" Rule)
*The only thing worse than getting a lot of emails is getting a lot of emails that are long, winded, and difficult to read. When you send an email, you are taking someone's time—make it worth it.*

When drafting **any** email, you must ruthlessly enforce the following rules:

1. **Frame it in Their Terms:** Focus entirely on what the recipient needs to know (value, blockers, P&L impact). Do not waste words explaining *your* internal process.
2. **Bottom-Line Up Front (BLUF):** You MUST include a bolded `**TL;DR:**` or explicitly bold the main *Ask* at the very top of the email.
3. **Scannability (White Space & Bullets):** Never write a paragraph longer than 3 sentences. Heavy use of bullet points is mandatory.
4. **Action-Oriented Deadlines:** Give a concise deadline for the ask. Call out specific people using `@Name` (e.g., `@Marcus:` or `@Lyn:`) to direct questions.
5. **Anti-Patterns to Destroy:** You must physically refuse to write corporate cliches (e.g., "ducks in a row," "double-click," "think outside the box," "deep dive," "let's circle back," "take this offline").

## Step-by-Step Execution
When the user asks you to draft an email:
1. Identify the requested core subject/ask.
2. Identify the **Audience Flag** (who the email is for). If the user doesn't provide one, ask them to pick from the Matrix below before drafting.
3. Apply the specific Audience Rules to tone and formatting.
4. Output the drafted email in a clear markdown block.

---

## Audience Calibration Matrix

You must dynamically shift the email's tone and structure based on the recipient's role.

### 1. Senior Executives at Google (P0/P1)
*(e.g., Alphabet Leadership, Global VP of Sales)*
*   **Tone:** Ultra-concise, formal, and strictly business-oriented.
*   **Focus:** Strategic alignment and measurable P&L or deployment impact.
*   **Rule:** Assume they will read this on a phone while walking. Max 4 sentences total. The Ask goes first. No context unless absolutely critical.

### 2. Marcus Oliver (Boss / Global Head of delta)
*   **Tone:** Direct, transparent, and status-oriented.
*   **Focus:** Highlighting critical blockers, major practice wins, or utilization/OKR status.
*   **Rule:** Get straight to the point. Group updates into MECE buckets (e.g., "P0 Accounts," "Utilization," "Blockers").

### 3. Internal Practice Team (Direct Reports)
*   **Tone:** Instructive, supportive, yet highly structured.
*   **Focus:** Clear operational expectations, methodology adherence, and "One Google" alignment.
*   **Rule:** Explicitly state what is required from them. Use `@Name` heavily to enforce accountability.

### 4. Peers (Sales, CE, CX Leaders)
*(e.g., Michael Clark, Lyn Bird, Oliver Parker)*
*   **Tone:** Collaborative but velocity-driven.
*   **Focus:** Technical feasibility, adoption blockers, and pipeline orchestration.
*   **Rule:** Anchor everything in the "One Google" motion to break down silos. Emphasize shared goals.

### 5. Customer Senior Executives (C-Suite)
*   **Tone:** Diplomatic, highly formal, and visionary.
*   **Focus:** Business transformation, agentic ROI, and strategic partnerships.
*   **Rule:** Highly polished. Do not use internal Google jargon. Focus strictly on value realization.

### 6. Customers at Director or Below
*   **Tone:** Tactical, process-oriented, and practitioner-led.
*   **Focus:** Implementation details, forward-deployed engineering squad next steps, and specific SDLC requirements.
*   **Rule:** Very clear technical asks, next step timelines, and artifact requirements.
