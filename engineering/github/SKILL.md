---
name: github
description: Triggers whenever the user asks to interact with GitHub, including creating a new repository, opening or reviewing a pull request, searching through a codebase, or managing issues. Do NOT trigger this skill if the user is just asking a general question about Git commands (e.g., "how do I run git commit"). Only trigger when attempting to mutate or read data directly from the GitHub platform.
---

# GitHub Operations Master

This skill enables complete integration with GitHub via the configured MCP (Model Context Protocol) server. It grants you the ability to autonomously map out repositories, create new ones, manage pull requests, and write/read files directly to the platform.

## Execution Rules

### 1. Zero-Assumption Data Retrieval
*   **Mandatory:** When asked to review a repository or pull request, you MUST NOT hallucinate the file contents based on context. You MUST use the `github` MCP server tools to search and fetch the exact current state of the files.
*   **Prohibited:** Do not guess branch names. If you are instructed to create a PR, always verify the default branch (usually `main` or `master`) first by reading the repository metadata.

### 2. Repository Creation
When asked to create a new repository:
1.  **Clarify Scope:** If the user did not specify public/private, assume **private** unless instructed otherwise.
2.  **Initialize:** Automatically initialize the repository with a `README.md` and a basic `.gitignore` relevant to the project's tech stack (ask if unsure).
3.  **Confirm:** Once created, return the exact clone URL to the user.

### 3. Pull Requests (PRs)
When asked to create or review a Pull Request:
1.  **Feature Branch:** Always ensure changes are pushed to a newly created feature branch, not the default branch.
2.  **Descriptive Titles:** Auto-generate a descriptive title and summary for the PR conforming to conventional commit standards (e.g., `feat: added authentication`, `fix: resolved race condition`).
3.  **Diff Review:** When reviewing an existing PR, fetch the diff, analyze the changed lines, and provide a structured, bulleted summary of the logical changes (not just line-by-line syntax).

### 4. Code Search & File Operations
*   Use GitHub search to aggressively pinpoint files before reading them broadly.
*   When editing a file directly via GitHub (not local), ensure you provide a valid commit message that explains the intrinsic "Why" of the change.

## Tool Orchestration
You should seamlessly handoff operations between your local file editing tools (if working on local files tracked by git) and the `github` MCP tools for platform-level operations (creating repos, managing issues/PRs).

If a `github` API call fails due to formatting, **do not immediately ask the user**. You MUST review your syntax, check the precise requirements of the `github` tool, and retry the execution before citing failure.
