---
name: product-feature-md
description: >
  Generate, critique, or interview to produce a narrative-driven product-feature.md
  that defines the User, Problem, Journey, and Emotional Arc without manifest
  solution description or technical implementation details. Version 5.0.
  
  Trigger this skill when the user asks to generate, outline, or critique a product specification, product-feature.md document, or when exploring user journeys and product narratives.
  Do NOT trigger this skill for technical PRDs, architecture documents, system invariants, or database schema design.
---

document_definition:
  what_it_is: |
    A `product-feature.md` is a narrative specification formatted entirely in YAML. It ignores *how* the system is built (databases, APIs, logic) and focuses entirely on *who* uses it, *how it feels*, and the *impact* it creates.
  what_it_is_not:
    - It is NOT a technical PRD.
    - It does NOT contain functional requirements, system invariants, or edge cases.
    - It does NOT discuss data models, compliance, or architecture.
    - It does NOT use technical jargon (e.g., "Latency," "JSON," "React," "Endpoint").

specification_sections:
  1_user_persona:
    goal: Create a persona so detailed it feels like a real person.
    must_include:
      identity: Name, role, background, and specific context (e.g., "A tired parent of two," not just "A parent").
      psychographics: Their motivations, fears, daily frustrations, and what they value most.
      context: Where are they when they have the problem? What devices are they using? What is their state of mind?
  2_problem_statement:
    goal: Define the friction clearly enough that a stranger would empathize.
    must_include:
      trigger: What happens that causes the problem?
      friction: Why is the current state hard, slow, or annoying?
      consequence: Why does this matter? (e.g., wasted money, lost time, emotional stress).
      why_now: Why is it critical to solve this specific pain?
  3_ideal_user_journey:
    goal: A cinematographic description of the solution in action.
    format: A numbered list of steps.
    must_include:
      happy_path: A step-by-step narrative of the user interacting with the solution.
      simplicity: Focus on the flow, not the UI buttons (e.g., "She captures the thought instantly," rather than "She presses the blue button").
      resolution: How the interaction ends and the problem is resolved.
  4_emotional_arc:
    goal: Map the user's feelings from the start of the problem to the resolution.
    format: A numbered list of emotional states corresponding to the journey.
    must_include:
      progression: Distinct emotional shifts (e.g., from Frustration to Relief).
  5_stakeholder_impact:
    goal: Define the value and changes this outcome brings to the broader ecosystem.
    must_include:
      end_users: The ultimate life improvement or capability unlocked for the primary persona.
      google_business: Strategic alignment, platform habituation, or new opportunities created.
      ecosystem_participants:
        knowledge_creators: How this expands their audience, reach, or monetization.
        skills_creators: New capabilities or primitives they can build upon.
        app_developers: How this simplifies their integrations or provides new narrative constraints to build against.

anti_patterns:
  - pattern: Tech Implementation (Mentions "React," "Database," "API")
    fix: Remove. Focus on the human action.
  - pattern: UI-Centricity ("User clicks the blue button")
    fix: Focus on intent ("User confirms the action").
  - pattern: Generic Persona ("The User" or "Anyone")
    fix: Force specific detail. Give them a name and a neurosis.
  - pattern: Business Speak ("Increases retention by 20%")
    fix: Focus on user and strategic value ("Makes the user feel loyal").
  - pattern: Vague Emotions ("Happy," "Good")
    fix: Use precise words ("Empowered," "Relieved," "Validated").
  - pattern: Missing "Why" (Describes problem but not consequence)
    fix: Add the cost of not solving the problem.
  - pattern: Ignoring the Ecosystem (Failing to define impact beyond the end user)
    fix: Ensure Knowledge Creators, Skills Creators, and App Developers are addressed.

llm_operational_modes:
  mode_1_generate:
    input: Rough notes, transcripts, or a feature list.
    output: Structured YAML `product-feature.md` following the 5-section format.
    behavior:
      - Strip all technical details.
      - Infer emotional context and ecosystem impact if missing.
      - Dramatize the persona.
      - Structure outputs exactly matching the YAML keys.
    prompt: "I will transform these notes into a narrative `product-feature.md` in YAML format. I will strip out the tech, focus on the emotional journey, and define the stakeholder impact. Processing..."
  mode_2_critique:
    input: An existing draft.
    output: A YAML critique focusing on empathy, clarity, and completeness.
    behavior:
      - Persona Check: Is this a real person?
      - Problem Check: Do I feel the pain?
      - Journey Check: Is it cinematic or robotic?
      - Emotional Check: Are the emotions distinct and sequential?
      - Impact Check: Are all ecosystem stakeholders represented?
  mode_3_interview:
    behavior: Ask deep, psychological, and strategic questions to build the narrative. Do not ask about features.
    sequence:
      - The Person: "Who is this for? What keeps them up at night? What is their specific context?"
      - The Pain: "Walk me through the moment the problem hits. What are they trying to do? How does the failure feel?"
      - The Solution: "If magic existed, what would the perfect experience look like? Don't tell me screens, tell me the story."
      - The Feeling: "How do they feel before, during, and after?"
      - The Impact: "How does this change the game for Google, knowledge creators, and developers building in this space?"

minimal_complete_example: |
  product_vision: QuickVoice
  user_persona:
    identity: Marcus, the Commuter Creative. 34-year-old creative director.
    psychographics: Values flow states, hates friction. Anxious about losing sparks of inspiration.
    context: Spends 2 hours a day driving. Tries to use voice assistants but transcription errors and activation delays break his flow.
  problem_statement:
    trigger: A complex idea strikes him on the highway.
    friction: Voice assistants require specific syntax ("Take a note that..."), forcing a shift from "creative brain" to "command brain."
    consequence: He loses the nuance of the idea, leading to a feeling of wasted potential and professional anxiety.
    why_now: Commute times are increasing, and current voice AI is still optimized for commands, not open-ended capture.
  ideal_user_journey:
    1: Marcus is driving and a complex idea strikes him.
    2: Without looking down, he taps a single, large gesture area on his mounted phone.
    3: The phone vibrates instantly to confirm it is listening.
    4: Marcus speaks naturally, rambling and brainstorming without pausing for syntax.
    5: He stops speaking. The system intuitively knows he is done, gives a confirmation chime, and saves the audio plus a perfect summary.
    6: Marcus keeps driving, knowing the idea is safe.
  emotional_arc:
    1: Anxious (Afraid of losing the thought while driving).
    2: Focused (Capturing the idea without breaking his driving flow).
    3: Secure (Hearing the chime and knowing it is caught).
    4: Satisfied (The mental load is released).
  stakeholder_impact:
    end_users: Achieves a zero-friction state for capturing raw thought without breaking context or compromising safety.
    google_business: Deepens habituation of voice-first interactions and creates a high-trust anchor for personal AI assistance.
    ecosystem_participants:
      knowledge_creators: Can easily aggregate and publish their unstructured thoughts into coherent newsletters or posts.
      skills_creators: Can build specialized downstream processors (e.g., "Format Marcus's rants into pitch decks").
      app_developers: Gain access to a standardized "raw thought" input primitive, removing the burden of building custom audio-capture workflows.

validation_checklist:
  - Structure: Is the document strictly formatted in YAML frontmatter style?
  - Structure: Are there exactly 5 sections (Persona, Problem, Journey, Arc, Stakeholder Impact)?
  - Persona: Does the persona have a name and a specific psychological struggle?
  - Problem: Is the "Consequence" of the problem clearly defined?
  - Journey: Is the journey a numbered list/array?
  - Journey: Is the journey free of UI jargon (clicks, menus, screens)?
  - Arc: Is the Emotional Arc a numbered list/array?
  - Arc: Is there a clear linear progression of distinct states?
  - Impact: Are End Users, Google, Knowledge Creators, Skills Creators, and App Developers all explicitly addressed?
  - Sanitization: Are all technical terms (Database, API, JSON) removed?
