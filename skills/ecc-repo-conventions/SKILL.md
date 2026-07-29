---
name: ecc-repo-conventions
description: >
  Enforce standardized repository structure, file naming conventions, state tracking (STATE.md), and environment variables across customer engagements.
  Triggers on: "ecc repo conventions", "repo hygiene", "standardize repo", "repository conventions", "audit repo structure".
---

# Enterprise Codebase Conventions (ECC Repo Conventions)

Establishes and enforces standardized repository organization, configuration rules, and file structures across enterprise customer engagements.

---

## Standard Repository Layout

```
repo-root/
├── .agents/                    # Agent capability mappings & custom rules
├── .evolve/                    # AlphaEvolve experiment configurations
├── docs/                       # Architectural documentation, PRDs, & ADRs
│   ├── PRD.md                  # Product Requirements Document
│   ├── TDD.md                  # Technical Design Document
│   ├── ARCHITECTURE.md         # System Architecture Recommendation
│   └── baseline_kpis.json      # Pre-deployment quantitative baseline
├── experiments/                # AlphaEvolve evaluation & optimization experiments
├── skills/                     # Workspace-scoped agent skills
├── src/                        # Primary application source code
├── tests/                      # Unit, integration, & regression test suites
├── STATE.md                    # Engagement state machine checkpoint
├── README.md                   # Project overview & onboarding guide
├── pyproject.toml / package.json # Project runtime configuration
└── .env.example                # Sanitized environment variable template
```

---

## Mandatory Governance Rules

1. **State Tracking (`STATE.md`)**: Every repository MUST maintain a `STATE.md` file tracking active phase, status, and phase-gate approvals.
2. **Environment Variable Hygiene**: NEVER commit hardcoded secrets, API keys, or GCP credentials. All required environment variables MUST be listed in `.env.example` with blank placeholders.
3. **Artifact Isolation**: Generated outputs, evaluation benchmarks, and architecture diagrams MUST be placed in `docs/` or `experiments/` — never floating in the root directory.
4. **Clean Code & Test Parity**: Every module in `src/` MUST have a corresponding unit test file in `tests/`.

---

## Audit Checklist
- [ ] `STATE.md` exists and reflects current engagement phase.
- [ ] `.env.example` present; zero hardcoded secrets in source files.
- [ ] `docs/` contains PRD, TDD, and architectural recommendation artifacts.
- [ ] Directory layout matches ECC standard structure.
