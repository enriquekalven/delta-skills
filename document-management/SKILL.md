---
name: document-management
description: Handles the creation, formatting, and generation of Microsoft Word documents using the delta-word-template. Trigger this skill when the user asks to "create a new word document", "generate a word doc from a template", or "put this in a word document". Do NOT trigger this skill for simple text files, markdown files, or when just summarizing text unless explicitly asked to output a Word file (.docx).
---

# Document Management Skill

This skill empowers the agent to autonomously generate stylized Microsoft Word (`.docx`) documents from the official `delta-word-template.dotx` using a specialized XML-injection Python script. 

## Capabilities

1. **Word Document Auto-Scaffolding:** Injects arbitrary structured content (Headings, Normal text) directly into the corporate Word template.
2. **Strict XML Validation Preservation:** Uses a specialized raw-string replacement script to ensure Word's strict schema validators do not reject the generated file as corrupted.
3. **Automatic XML Escaping:** The script automatically escapes special characters (such as `&`, `<`, `>`) in the JSON text to prevent document corruption.

## Execution Steps

When a user requests to generate a Word document, follow these exact steps:

### Step 1: Content Planning
Determine what content the user wants in the document.
1. Outline the sections (e.g., Title, Introduction, Bullet points).
2. Structure this content into a temporary JSON file. The JSON must be an array of objects, where each object has a `style` and a `text` property. Supported styles are: `Heading1`, `Heading2`, and `Normal`.

**Example JSON struct (save as `/tmp/doc_content.json`):**
```json
[
    {"style": "Heading1", "text": "Project Overview"},
    {"style": "Normal", "text": "This document outlines the core objectives..."},
    {"style": "Heading2", "text": "Key Deliverables"}
]
```

### Step 2: Create the JSON file
Use the `write_to_file` tool to save the planned JSON structure to a temporary location (e.g. `/tmp/content.json` or in the current working directory).

### Step 3: Execute the Generation Script
Call the `generate_docx.py` script located in this skill's `scripts/` directory to build the `.docx` file.

**Command:**
```bash
python3 .agents/skills/document-management/scripts/generate_docx.py \
    --template "knowledge/general/context-library/delta-word-template.dotx" \
    --output "[DESIRED_OUTPUT_PATH.docx]" \
    --content "[PATH_TO_JSON_FILE.json]"
```

### Step 4: Verification & Cleanup
1. Run `unzip -t [DESIRED_OUTPUT_PATH.docx]` to ensure the zip archive was built correctly without corruption.
2. Delete the temporary JSON file used for content staging.
3. Notify the user that their document is ready for review.
