---
name: Meeting Preparation
description: Generates a comprehensive brief before an important meeting.
---

# Meeting Preparation Skill

## Instructions
When requested to prepare for a meeting (e.g., `/prep [meeting_name]`):
1. **Input Gathering:** Ask the user for the meeting topic, attendees, and any past related documents if not already evident from Calendar MCP context.
2. **Research Context:** Use local semantic search (`grep_search`) or MCP integrations (like Drive/Notion) to find recent context involving these stakeholders or projects.
3. **Generate Brief:** Create a document with the following structure:
   - **Objective:** What is the primary goal of this meeting?
   - **Key Stakeholders:** Who is attending and what is their likely stance or context?
   - **Talking Points:** 3-5 strategic points to cover.
   - **Questions to Ask:** 2-3 probing questions to uncover risks, blockers, or opportunities.
4. **Draft Output:** Generate the output in the session and offer to save it locally as `prep_[topic]_[date].md`.
