# Agent Skills

This repository contains a collection of agentic skills designed for AI assistants. Each skill is documented using the `SKILL.md` format, which outlines its purpose, triggers, inputs, and step-by-step instructions. See the master directory in [SKILL.md](SKILL.md).

## Structure

Skills are organized into the following top-level directories:

- **strategy-agent:** Strategic advisory skills (diagnosis, decision framing, financial/market/M&A/operating-model analysis, and executive report generation). See [strategy-agent/SKILLS_INDEX.md](strategy-agent/SKILLS_INDEX.md).
- **strategy-house:** Builds a "Strategy House" and prioritized opportunity matrix from 10-Ks, earnings transcripts, and investor materials.
- **business-process-redesign:** Maps current ("As-Is") workflows, identifies bottlenecks, and redesigns "To-Be" processes around human-agent collaboration.
- **ai-value-sizing:** Maps use cases to value pillars, runs TAM/SAM/SOM market sizing, and models 3-year ROI/TCO and unit economics.
- **cuj-architect:** Maps AI-enhanced Critical User Journeys (`Outcome -> Stage -> CUJ -> Task -> Step -> CUI`) and quality measurement variants.
- **usecase-canvas:** Creates delta use-case canvases (`create-delta-ucc`) and business value propositions.
- **workshop-intake:** Guides customer discovery and workshop intake calls to capture strategic, technical, and logistical requirements.
- **product-management:** Generates full Product Requirements Documents (`product-md`) and single-feature specifications (`product-feature-md`).
- **prototyping:** Rapid UI prototyping (`frontend-design` and Stitch MCP `stitch-design`).
- **ai-coding:** Goal-driven AI coding on Google Cloud Vertex AI Model Garden (`claude-agent-harness`): work is bound to executable acceptance checks and iterates until they pass.
- **delivery:** Engagement execution and architecture governance (`tdl-field-guide`, `synthetic-baseline-protocol`, `gcp-agent-architecture-advisor`).
- **utils:** Foundational meta-skills (`skill-creator`, `specification-engineer`, `prompt-engineer`).

## Usage

Each skill folder contains a `SKILL.md` file with YAML frontmatter (`name`, `description`) and instructions. Start at the root [SKILL.md](SKILL.md) to pick the right skill for a task, then read that skill's `SKILL.md`.

## Validation

Run the zero-dependency validator to check YAML frontmatter (`name` matching folder, `description` length) and verify that relative markdown links resolve:

```bash
python3 scripts/validate_skills.py
```
