---
name: skill-creator
description: Guides the creation and initialization of new agent skills. Trigger this skill immediately whenever the user types `/skill-creator` or asks to create/update an autonomous skill.
---

# Skill Creator (Gemini 3.1 Pro Pipeline)

This skill guides the process of creating highly effective, reusable agent skills specifically optimized for the **Gemini 3.1 Pro** ecosystem. A skill is a self-contained directory that teaches the agent how to handle specific, repeatable workflows by combining instructions, scripts, and reference files.

## Mandatory Architectural Standards
When creating a new skill, you MUST adhere to the following framework defined in our `agentskills-specification.md`:

1.  **Progressive Disclosure:** Gemini has massive context, but fast inference requires lean instructions. The primary `SKILL.md` file MUST stay under 5,000 words. Push heavyweight domain knowledge to the `references/` folder and executable logic to the `scripts/` folder.
2.  **The 3-Pass Test (`description` block formatting):** The `description` in the YAML frontmatter controls when a skill activates. You must write descriptions that pass:
    *   **Obvious Triggers:** Explicit phrases that should fire this skill (e.g., "Trigger when user says...").
    *   **Edge Cases:** Define the boundaries so Gemini doesn't get confused.
    *   **Negative Triggers:** Explicitly state when NOT to trigger the skill (e.g., "Do NOT trigger this skill just because the user mentions the word 'email' in passing").
3.  **Cross-Tool Orchestration:** Assume the agent will coordinate across multiple Google tools. Design skills that seamlessly hand off tasks (e.g., extracting a doc, executing Python, then formatting the final output).

## Execution Steps

When the user types `/skill-creator`, follow these steps in order. **Do not skip ahead.**

### Step 1: Understand the Goal & Context
Ask the user what kind of skill they want to build. Ask them for:
1. The exact phrase or scenario that should trigger the skill (Obvious Trigger).
2. What scenario should explicitly *not* trigger the skill (Negative Trigger).

### Step 2: Plan the Architecture
Analyze the user's requirements against the `agentskills-specification.md` (located in `references/`). Plan the skill's contents using the Progressive Disclosure model:
-   **Core `SKILL.md`:** What are the high-level operational instructions?
-   **Scripts (`scripts/`):** Are there repetitive actions that require bash/python execution?
-   **References (`references/`):** Is there domain knowledge or templates needed that should be loaded on-demand rather than polluting the core `SKILL.md`?

### Step 3: Initialize the Directory
Once the user approves the plan, establish the skill directory.
Ensure it has the following structure:
- `[skill-name]/SKILL.md`
- `[skill-name]/scripts/` (optional)
- `[skill-name]/references/` (optional)

### Step 4: Write `SKILL.md`
Draft the `SKILL.md` using `references/skill-template.md` as your structural base.
**Crucial Formatting Rules:**
1.  **YAML Frontmatter:** Must be at the very top.
    ```yaml
    ---
    name: [kebab-case-name]
    description: [Comprehensive trigger definition passing the 3-Pass Test, including Negative Triggers]
    ---
    ```
2.  **Instructional Constraints:** Write the body using clear, objective commands. To prevent "Model Laziness," use explicit phrases like "You MUST NOT do X" or "It is CRITICAL that you complete Y."
3.  **Examples:** Include concrete usage scenarios to guide the Gemini engine during inference.

### Step 5: Review and Iterate
Present the generated `SKILL.md` and file structure to the user. Ask if they want to tweak the instructions or upload additional reference materials into the `references/` folder.
