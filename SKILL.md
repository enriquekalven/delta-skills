---
name: delta-skills-directory
description: >
  Master registry and navigation index for all advanced agentic skills in the delta-skills repository.
  Triggers immediately when asked to "list available skills", "find a skill", or "understand the capabilities of this workspace".
metadata:
  author: antigravity@
  version: '1.0'
---

# Delta Skills Ecosystem Directory

Welcome to the **Delta Skills Ecosystem**. This repository contains a catalog of highly-specialized, production-grade agentic skills optimized for advanced AI agents. Each skill is designed under strict architectural guidelines: progressive disclosure of context, mathematically-defensible frameworks, and robust human-in-the-loop safeguards.

---

## 1. Value Realization & Business Case Sizing
Grounded metrics, financial sizing, and ROI validation models to prove the business case for AI initiatives.

*   **[ai-value-sizing](ai_value_sizing/SKILL.md)**
    *   *Role:* Expert Strategic Value Realization Consultant & TCO Architect.
    *   *Trigger:* When analyzing the financial potential of an idea, running market sizing, or drafting an investment-ready ROI/TCO business case.
    *   *Key Deliverable:* Sizing Funnel (TAM/SAM/SOM), 3-Year ROI/NPV scenarios.

---

## 2. Business Process Redesign (BPR)
Operations and workflow engineering to redesign traditional manual processes around collaborative human-agent models.

*   **[business-process-redesign](business-process-redesign/SKILL.md)**
    *   *Role:* Elite Business Process Architect and Operations Engineer.
    *   *Trigger:* When mapping current ("As-Is") workflows, evaluating manual bottlenecks, and drafting optimized ("To-Be") agentic processes.
    *   *Key Deliverable:* As-Is findings report, To-Be process design specs, Human-Agent interaction matrices.

---

## 3. Enterprise Strategy & Corporate Advisory
High-fidelity consulting frameworks to align executive vision, analyze competitor moves, and architect enterprise operating models.

*   **[strategy-partner-orchestrator](strategy-agent/strategy-partner-orchestrator/SKILL.md)**
    *   *Role:* Senior Strategy Partner & Chief Advisor.
    *   *Trigger:* Entry point for complex business problems requiring multi-skill strategy diagnosis, decision framing, and execution tracking.
    *   *Key Deliverable:* Integrated strategy roadmap, sequence of specialist sub-skills.
    *   *Specialist Sub-Skills (See [Strategy Index](strategy-agent/SKILLS_INDEX.md)):*
        *   **[ai-native-strategy](strategy-agent/ai-native-strategy/SKILL.md)**: CAIO advisor for AI business models and agent architecture.
        *   **[rumelt-strategy-forge](strategy-agent/rumelt-strategy-forge/SKILL.md)**: Strategic crux diagnosis and coordinated action design.
        *   **[operating-model](strategy-agent/operating-model/SKILL.md)**: Translating strategy into organizational process structures.
        *   **[market-intelligence](strategy-agent/market-intelligence/SKILL.md)**: Real-time benchmark and competitor dynamic validation.
        *   **[financial-strategy](strategy-agent/financial-strategy/SKILL.md)**: CFO-level P&L analysis and capital structuring.
        *   *(For others like Growth, GTM, Change Management, and M&A, visit the [Strategy Index](strategy-agent/SKILLS_INDEX.md))*

*   **[strategy-house](strategy-house/SKILL.md)**
    *   *Role:* Strategic Planner & Synthesizer.
    *   *Trigger:* When building a structured "Strategy House" and "Opportunity Matrix" starting from 10-Ks and earnings calls.
    *   *Key Deliverable:* Vision, Pillars, Prioritized Use Cases, and OKRs/KPIs maps.

---

## 4. Product Design & Journey Mapping
UX and Product Design frameworks to align features to user achievements and evaluate specific AI touchpoint quality.

*   **[ai-enhanced-cuj-strategist](cuj-architect/SKILL.md)**
    *   *Role:* Expert UX/AI Product Strategist.
    *   *Trigger:* When generating an AI CUJ, mapping user journeys, or evaluating exact quality measurement variants.
    *   *Key Deliverable:* Modernized hierarchy maps (Outcome → Stage → CUJ → Task → CUI), linguistic value proposition formulations.

*   **[create-delta-ucc](usecase-canvas/create-delta-ucc/SKILL.md)**
    *   *Role:* Product Marketer & Value Proposition Designer.
    *   *Trigger:* When designing delta use-case canvases or establishing target audience value definitions.
    *   *Key Deliverable:* High-impact business use case canvases.

---

## 5. Product Management & Requirements
Writing detailed, modular, and bulletproof specifications for feature engineering and development handoff.

*   **[product-md](product-management/product-md/SKILL.md)**
    *   *Role:* Senior Technical Product Manager.
    *   *Trigger:* When generating a full Product Requirements Document (PRD) for major releases.
    *   *Key Deliverable:* Comprehensive PRD (User Journeys, Non-functional requirements, telemetry).

*   **[product-feature-md](product-management/product-feature-md/SKILL.md)**
    *   *Role:* Feature Architect.
    *   *Trigger:* When drafting requirements and specifications for a single, localized product feature.
    *   *Key Deliverable:* Modular feature requirements sheet.

---

## 6. Prototyping & Frontend Engineering
Accelerated UI generation, design system construction, and component stitching.

*   **[stitch-design](prototyping/stitch-design/SKILL.md)**
    *   *Role:* Rapid Prototyper.
    *   *Trigger:* Stitching together multiple design mockups and components into a unified frontend stream.
    *   *Key Deliverable:* Stitched interactive prototypes.

*   **[frontend-design](prototyping/frontend-design/SKILL.md)**
    *   *Role:* Senior Frontend Engineer & UX Designer.
    *   *Trigger:* When designing responsive layouts, styling systems, and high-fidelity UI screens.
    *   *Key Deliverable:* Production-grade HTML/CSS/JS frontend mockups.

---

## 7. Systems Engineering & Core Development Tools
Meta-level skills to create, standardise, and optimize agent systems.

*   **[skill-creator](utils/skill-creator/SKILL.md)**
    *   *Role:* Systems & Specification Architect.
    *   *Trigger:* When asked to initialize or build a new autonomous skill for the agent ecosystem.
    *   *Key Deliverable:* Validated, frontmatter-compliant skill directories.

*   **[specification-engineer](utils/specification-engineer/SKILL.md)**
    *   *Role:* Tech Spec Architect.
    *   *Trigger:* When translating complex operational logic into rigorous, structured technical specifications.
    *   *Key Deliverable:* System architecture specs.

*   **[prompt-engineer](utils/prompt-engineer/SKILL.md)**
    *   *Role:* Prompt Design Specialist.
    *   *Trigger:* Designing and refining prompt templates to prevent model laziness and optimize inference accuracy.
    *   *Key Deliverable:* Standardized prompt template files.

---

## Skill Integration & Handoff Rules

AI Agents using this repository should locate the corresponding directory of a skill and read its dedicated `SKILL.md` file for full step-by-step execution instructions. 

When encountering complex requests (e.g., *"design a strategy for our onboarding portal and map the automation ROI"*), agents should orchestrate multiple skills:
1.  Use **[strategy-partner-orchestrator](strategy-agent/strategy-partner-orchestrator/SKILL.md)** to set up the diagnostic base.
2.  Use **[business-process-redesign](business-process-redesign/SKILL.md)** to map and optimize the onboarding flow.
3.  Use **[ai-value-sizing](ai_value_sizing/SKILL.md)** to calculate the 3-year ROI / TCO business case.
