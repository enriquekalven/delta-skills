# Single-Feature Narrative Specification Template (`docs/product-feature.md`)

```yaml
product_vision: "<Feature Name>"
user_persona:
  identity: "<Name, role, tenure, and operational responsibility>"
  psychographics: "<What they value, what slows them down, and what creates risk in their job>"
  context: "<Physical/digital environment, device constraints, and time pressure>"
problem_statement:
  trigger: "<The exact event that starts the workflow>"
  friction: "<Why the current workflow breaks flow or causes errors>"
  consequence: "<Quantifiable operational, financial, or safety impact of the friction>"
  why_now: "<Market, regulatory, or operational shift making this urgent now>"
ideal_user_journey:
  1: "<Step 1: Trigger occurs in context>"
  2: "<Step 2: Low-friction initiation>"
  3: "<Step 3: Immediate system confirmation>"
  4: "<Step 4: Natural user input / collaboration>"
  5: "<Step 5: Structured synthesis and verification>"
  6: "<Step 6: Resolution and safe handoff>"
emotional_arc:
  1: "<Initial state when problem hits (e.g., Pressured / Overloaded)>"
  2: "<State during capture/interaction (e.g., Focused / Unblocked)>"
  3: "<State upon verification (e.g., Assured / In Control)>"
  4: "<Final state upon completion (e.g., Confident / Ready for next task)>"
stakeholder_impact:
  end_users: "<Direct time, safety, or quality improvement for the persona>"
  google_business: "<Platform adoption, multimodal/agent workload growth, and trust anchor>"
  ecosystem_participants:
    knowledge_creators: "<How subject-matter experts capture and scale domain knowledge>"
    skills_creators: "<New reusable agent skills or evaluators unlocked downstream>"
    app_developers: "<Standardized workflow primitive exposed to line-of-business apps>"
```
