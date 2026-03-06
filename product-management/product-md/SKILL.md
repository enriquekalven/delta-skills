---
name: product-md
description: >
  Generate, critique, or update a full-scale Product Requirements Document (PRD) using
  advanced Product Management frameworks (like RICE scoring) and structured Markdown.
  This covers product strategy, user journeys, specific features, metrics, and non-functional requirements.
  
  Trigger this skill when the user asks to write a full PRD, a strategy document,
  prioritize a feature backlog, or structure a new product definition.
---

document_definition:
  what_it_is: |
    A comprehensive `product-md` document is a structured Markdown PRD. It acts as a 
    high-level contract between business and product teams to define what is in scope 
    vs. out of scope, acting as a north star for external and development teams.
  what_it_is_not:
    - It is NOT just a feature list or a technical architecture document (though it informs them).
    - It does NOT dictate *how* the engineering team should code the solution, but rather *what* needs to be built and *why*.

specification_sections:
  1_header_and_vision:
    goal: Provide executive alignment and high-level summary.
    must_include:
      metadata: Author, Contributors, Status, Last Updated, and linked docs (UXR, Design, Engineering).
      vision: A very brief (1-2 sentence) summary of the envisioned product.
  2_background_and_context:
    goal: Establish the problem space, motivation, and potential business impact.
    must_include:
      problem_motivation: Describe the current process and proposed solution.
      potential_impact: Metrics that motivate the product.
      key_definitions: Glossary of terms.
      target_users: Table of User Types, Expected Number of Users, and what they need the product to do.
  3_product_strategy:
    goal: Detail how the product achieves its goals and the parameters of the build.
    must_include:
      goals: Specific objectives and causal effects (e.g., "Because then, we will...").
      principles_and_values: E.g., Configurable, Scalable, Scoping strictness.
      key_assumptions: Availability of data sources, resources, etc.
      scope: Explicit "In Scope" and "Out of Scope" sections.
      phasing: MVP launch targets and strategic reasoning behind phasing.
      metrics_for_success: Table of Metrics, Targets, and Reason (OKRs/KPIs).
  4_user_journeys_and_features:
    goal: Exhaustively map what needs to be built tied directly to user roles.
    must_include:
      user_roles: Table of Roles and Descriptions.
      cuj_inventory: Critical User Journeys table (ID, Priority, User Role, Use Case).
      features_inventory: Table mapping Features across CUJs with priority.
      feature_details: Specific sub-sections detailing the requirements for each feature.
  5_non_functional_and_risks:
    goal: Address systemic parameters.
    must_include:
      latency: Requirements around speed/response.
      privacy: Data handling, compliance, etc.
      caveats_and_risks: Potential blockers or downsides.
      open_issues: Outstanding tracking items.
      human_comments: Include human comment tags like `<!-- HUMAN-ldap: comment -->` for collaboration.

prioritization_framework:
  method: RICE Score Analysis
  formula: "Score = (Reach * Impact * Confidence) / Effort"
  variables:
    reach: "How many users will this impact over a single quarter?"
    impact: "How much will this increase standard metrics? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)"
    confidence: "How confident are we about our estimates? (100%=high, 80%=medium, 50%=low)"
    effort: "How many 'person-months' will this take?"
  usage: "Automatically applied when asked to prioritize a feature backlog or determine MVP phasing."

llm_operational_modes:
  mode_1_generate:
    input: Rough notes, a problem statement, or a feature specification.
    output: A robust, Markdown-formatted PRD using the template structure.
    behavior:
      - Automatically populate missing strategic context using reasonable assumptions (and mark them as assumptions).
      - Output the final document in the `docs/` directory format (e.g., `docs/prd_v1.md`).
      - Generate the operational status JSON block upon completion.
  mode_2_prioritize:
    input: A list of feature ideas or an existing backlog.
    output: A scored RICE table outlining features by priority and phasing.
    behavior:
      - Estimate Reach, Impact, Confidence, and Effort dynamically if not provided.
      - Justify the scoring.
  mode_3_critique:
    input: An existing PRD draft.
    output: A review against the product validation checklist.
    behavior:
      - Highlight missed success metrics, vague requirements (*how* instead of *what*), and missing non-functional considerations.

validation_checklist:
  - User problem is clearly defined and validated.
  - Requirements explicitly state *what* needs to be built, not *how* it should be coded.
  - Analytics and success metrics are explicitly defined.
  - Dependencies and risks are highlighted.
  - Outputs include standard JSON status reporting.

standard_outputs:
  - format: "Markdown document saved to the `docs/` directory (e.g., `docs/prd_v1.md`)."
  - internal_status: |
      json {
        "agent": "product-manager",
        "status": "completed",
        "artifact_generated": "docs/prd_v1.md",
        "key_decisions": ["Prioritized Feature X over Feature Y due to higher impact score"]
      }
