---
name: codebase-onboarding-and-mapping
description: >
  Analyze an existing client repository to generate component dependency graphs, directory file maps, and architectural summaries (docs/ONBOARDING.md).
  Triggers on: "codebase onboarding", "map codebase", "onboard to repo", "repo architecture map", "codebase mapping".
---

# Codebase Onboarding & Architecture Mapping

Ingests existing client repositories during Phase 1 (Discover & Define) to rapidly map system architecture, entry points, data flows, and dependencies.

---

## Onboarding Analysis Workflow

```
[Scan Directory Structure] --> [Identify Entry Points & Routers] --> [Map Core Modules & Data Flows] --> [Output ONBOARDING.md]
```

### Analysis Steps

1. **Directory & Tech Stack Scan**: Detect languages, frameworks (`pyproject.toml`, `package.json`, `Dockerfile`), and build systems.
2. **Entry Point Identification**: Locate main execution entry points (`main.py`, `app.py`, `index.js`, CLI commands).
3. **Module Dependency Mapping**: Trace imports and component boundaries.
4. **Data Flow & Seam Discovery**: Identify database schemas, external API endpoints, and internal module seams.

---

## Output Artifact Schema (`docs/ONBOARDING.md`)

```markdown
# Codebase Onboarding & Architectural Map

## 1. System Overview
- **Repository**: [Repo Name]
- **Primary Languages & Frameworks**: [e.g. Python 3.11, Next.js, FastAPI]
- **Deployment Targets**: [e.g. Google Cloud Run, Docker]

## 2. Directory & Component Structure
```
src/
├── api/        # REST & gRPC endpoint handlers
├── core/       # Business logic & domain models
└── db/         # Database models & migrations
```

## 3. Key Entry Points & API Boundaries
| Entry Point | Path | Function / Purpose |
|---|---|---|
| Web API | `src/api/server.py` | FastAPI application runner |
| Worker Agent | `src/worker.py` | Asynchronous task consumer |

## 4. Architectural Observations & Friction Points
- Identified legacy dependencies or missing unit test coverage areas.
- Recommended seams for ADK Agent integration.
```
