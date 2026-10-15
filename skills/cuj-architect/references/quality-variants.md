# User Intents & Quality Measurement Variants

This reference documents the exhaustive list of user intents for AI touchpoints and how to measure their quality variants.

## Exhaustive Intent Categories
- **Answer**: Provide a direct response to a query.
- **Retrieve**: Fetch specific information or pattern matching.
- **Get insights**: Extract non-obvious patterns or conclusions.
- **Visualize**: Represent data or concepts graphically.
- **Route**: Direct a task, person, or information to a destination.
- **Execute**: Perform a series of technical or functional actions.
- **Analyze**: Examine components in detail to discover tendencies.
- **Diagnose**: Identify the nature of a problem or situation.
- **Prioritize**: Determine the order for dealing with items.
- **Transform**: Change the form or character of data (e.g., Normalize).
- **Summarize**: Provide a brief statement of the main points.
- **Companionship**: Provide social or emotional engagement.
- **Create**: Generate new content or assets.
- **Plan**: Design a sequence of steps to achieve a goal.
- **Entertain**: Provide amusement or enjoyment.
- **Guide**: Lead or direct toward a solution or decision.
- **Teach**: Impart knowledge or skill.
- **Facilitate**: Make an action or process easier.
- **Proxy**: Act on behalf of the user.
- **Fix a problem**: Resolve a technical or functional issue.
- **Make a decision**: Choose between alternatives.
- **Follow a process**: Guide through a standardized sequence of steps.

## Quality Measurement Variants
The user's intent dictates exactly how the AI will be evaluated.

### Example Variants:
| Intent | Measurement Focus | Metrics |
| :--- | :--- | :--- |
| **Guide - Fix a problem** | Resolution Effectiveness | Contextual relevance, Effectiveness at solving problem, Executable status, Factuality |
| **Guide - Make a decision** | Choice Clarity | Contextual relevance, Highlights key differences, Presents clear choices, Factuality |
| **Summarize** | Conciseness & Accuracy | Information density, Factuality, Lack of hallucination |
| **Execute** | Success Rate | Completion rate, Accuracy of action, Latency |
| **Retrieve** | Precision & Recall | Relevance of results, Speed, Pattern match accuracy |

---

> [!IMPORTANT]
> When assigning an intent to a Step or CUI, always pick from the exhaustive list above and define the corresponding quality measurement variants.
