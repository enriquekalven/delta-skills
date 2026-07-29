# AlphaEvolve Multi-Domain Skill Evaluation Matrix

This reference documents skill mapping and evaluator benchmarks across **5 industry domains**.

Each entry details:
1. **Trigger Input** (Example prompt)
2. **Usage Rationale** (Context and trade-offs)
3. **Expected Output** (Artifact preview)
4. **Evaluator Benchmark Metric** (Evaluation metric delta)

---

## Domain Mapping Matrix

```mermaid
graph LR
    FinTech ["FinTech & Banking"] --> Scoping ["Scoping & PRD"]
    MedTech ["MedTech & Healthcare"] --> Arch ["Architecture & Boundaries"]
    ECommerce ["E-Commerce & Retail"] --> Impl ["TDD & Performance"]
    DevTools ["DevTools & SaaS"] --> Verification ["QA & Refactoring"]
    Cybersec ["Cybersecurity & Cloud"] --> Launch ["Deploy & Handoff"]
```

---

## Domain 1: FinTech & Banking (Fraud Audit System)

### 1.1 Scoping & Value Proposition
* **Trigger Input**:
  > *"Trigger `opportunity-solution-tree` and `value-proposition` for an Automated Fraud Detection Agent in banking."*
* **Usage Rationale**: Use when mapping compliance goals ("Reduce chargeback fraud") into explicit feature paths prior to implementation.
* **Sample Output**:
  ```
  Outcome: Reduce fraud losses by $2M/yr
  ├── Opportunity: High false-positive rate on international wires
  │   └── Solution: Real-time Risk-Scoring Agent
  ```
* **Evaluator Metric**: +35% scoping precision score, zero feature duplication in requirements.

### 1.2 Security & Boundary Hardening
* **Trigger Input**:
  > *"Run `security-and-hardening` on the wire transfer payload handler."*
* **Usage Rationale**: Validates three-tier boundary security (Input -> Seam -> Storage) for financial transaction pipelines.
* **Sample Output**: `security_audit.md` — Added JWT verification on `/api/v1/wire/transfer` and disabled stack traces on HTTP 500 responses.
* **Evaluator Metric**: Security score improved from `0.40` to `0.98` (remediated 3 OWASP Top 10 vulnerabilities).

---

## Domain 2: MedTech & Healthcare (Patient Intake System)

### 2.1 Domain Modeling & Boundary Isolation
* **Trigger Input**:
  > *"Trigger `domain-modeling` and `api-and-interface-design` to isolate PHI (Protected Health Information) boundaries."*
* **Usage Rationale**: Enforces HIPAA compliance boundaries behind explicit interface contracts.
* **Sample Output**:
  ```typescript
  export interface PatientIntakeAdapter {
    processEncryptedPayload(token: EncryptedPHIToken): Promise<DeidentifiedSummary>;
  }
  ```
* **Evaluator Metric**: 100% isolation of PHI storage from presentation components.

### 2.2 Intent vs. Implementation Audit
* **Trigger Input**:
  > *"Run `intended-vs-implemented` comparing PRD Section 4 against `patient_service.py`."*
* **Usage Rationale**: Detects unauthorized data exposure and architectural drift prior to compliance audits.
* **Sample Output**: 
  `GAP DETECTED: PRD requires AES-256 encryption for patient notes. Code at line 112 writes unencrypted string to temp storage.`
* **Evaluator Metric**: Remediated 1 critical compliance defect before deployment verification.

---

## Domain 3: E-Commerce & Retail (Inventory & Pricing System)

### 3.1 Pretotyping & Assumption Testing
* **Trigger Input**:
  > *"Trigger `brainstorm-experiments-new` and `identify-assumptions-new` for dynamic repricing."*
* **Usage Rationale**: Validates customer purchase behavior under algorithmic pricing prior to building real-time scrapers.
* **Sample Output**:
  ```
  Hypothesis: At least 20% of users who see a "Flash Discount" badge complete checkout within 10 minutes.
  Pretotype: Manual price adjustment test on 100 SKUs for 48 hours.
  ```
* **Evaluator Metric**: Reduced initial development scope by validating baseline demand.

### 3.2 Performance & Core Web Vitals
* **Trigger Input**:
  > *"Trigger `performance-optimization` and `browser-testing-with-devtools` on the checkout workflow."*
* **Usage Rationale**: Use when conversion rates depend on rendering speed.
* **Sample Output**: `LCP reduced from 3.2s to 1.1s` by preloading hero assets and code-splitting secondary bundles.
* **Evaluator Metric**: +14% improvement in automated checkout performance score.

---

## Domain 4: DevTools & SaaS (AST Codebase Refactoring)

### 4.1 AST Code Remediation
* **Trigger Input**:
  > *"Trigger `ast-resilient-remediation` to migrate deprecated `urllib2` calls to `httpx` across 150 files."*
* **Usage Rationale**: Use for large-scale multi-file refactoring where regular expressions risk breaking AST semantics.
* **Sample Output**:
  ```diff
  - import urllib2
  - response = urllib2.urlopen(url)
  + import httpx
  + response = httpx.get(url)
  ```
* **Evaluator Metric**: Refactored 150 files with 0 syntax or AST errors.

### 4.2 Code Simplification & Review
* **Trigger Input**:
  > *"Trigger `code-simplification` and `code-review-and-quality` on `parser.py`."*
* **Usage Rationale**: Reduces cyclomatic complexity and simplifies convoluted legacy functions.
* **Sample Output**: Refactored 280-line nested conditional block into a 40-line strategy pattern.
* **Evaluator Metric**: Cyclomatic complexity reduced from 24 to 4.

---

## Domain 5: Cybersecurity & Cloud (Zero-Trust Policy Auditor)

### 5.1 Deployment & Registry Synchronization
* **Trigger Input**:
  > *"Trigger `google-agents-cli-deploy` and `google-agents-cli-publish` for Cloud Run."*
* **Usage Rationale**: Deploys ADK agents to production infrastructure and registers them with Gemini Enterprise.
* **Sample Output**:
  ```bash
  Service Deployed: https://security-agent-prod-xyz.run.app
  Gemini Enterprise Status: Registered (ID: sec-audit-v1)
  ```
* **Evaluator Metric**: 100% automated service account binding with zero manual configuration errors.

### 5.2 Handoff Documentation
* **Trigger Input**:
  > *"Generate `shipping-artifacts` for customer handoff."*
* **Usage Rationale**: Compiles complete operational handoff documentation.
* **Sample Output**: Generates documentation suite: `architecture.md`, `flows.md`, `permissions.md`, `variables.md`, `tests.md`.
* **Evaluator Metric**: Reduced operational handoff verification time.

---

## Master Skill Index

| Skill Name | Repository Source | Primary Category | Trigger | Benefit |
|---|---|---|---|---|
| [`idea-refine`](https://github.com/addyosmani/agent-skills/tree/main/skills/idea-refine) | `addyosmani/agent-skills` | Scoping | *"Trigger idea-refine"* | Structured solution exploration |
| [`opportunity-solution-tree`](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/opportunity-solution-tree) | `phuryn/pm-skills` | Strategy | *"Trigger opportunity-solution-tree"* | Connects outcomes to features |
| [`spec-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/spec-driven-development) | `addyosmani/agent-skills` | Architecture | *"Trigger spec-driven-development"* | Enforces spec prior to code |
| [`create-prd`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/create-prd) | `phuryn/pm-skills` | Requirements | *"Trigger create-prd"* | Defines goals and non-goals |
| [`grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) | `mattpocock/skills` | Architecture | *"Trigger grill-with-docs"* | Generates ADRs & context docs |
| [`domain-modeling`](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) | `mattpocock/skills` | Architecture | *"Trigger domain-modeling"* | Ubiquitous language bounds |
| [`codebase-design`](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) | `mattpocock/skills` | Architecture | *"Trigger codebase-design"* | Deep module design |
| [`api-and-interface-design`](https://github.com/addyosmani/agent-skills/tree/main/skills/api-and-interface-design) | `addyosmani/agent-skills` | API Seams | *"Trigger api-and-interface-design"* | Interface contract stability |
| [`planning-and-task-breakdown`](https://github.com/addyosmani/agent-skills/tree/main/skills/planning-and-task-breakdown) | `addyosmani/agent-skills` | Planning | *"Trigger planning-and-task-breakdown"* | Atomic task decomposition |
| [`to-tickets`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) | `mattpocock/skills` | Planning | *"Trigger to-tickets"* | Dependency graph mapping |
| [`incremental-implementation`](https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation) | `addyosmani/agent-skills` | Building | *"Trigger incremental-implementation"* | Vertical slicing |
| [`test-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/test-driven-development) | `addyosmani/agent-skills` | Building | *"Trigger test-driven-development"* | Red-Green-Refactor execution |
| [`implement`](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement) | `mattpocock/skills` | Building | *"Trigger implement"* | Ticket-to-code implementation |
| [`source-driven-development`](https://github.com/addyosmani/agent-skills/tree/main/skills/source-driven-development) | `addyosmani/agent-skills` | Building | *"Trigger source-driven-development"* | Documentation-grounded code |
| [`intended-vs-implemented`](https://github.com/phuryn/pm-skills/tree/main/pm-ai-shipping/skills/intended-vs-implemented) | `phuryn/pm-skills` | QA Gate | *"Trigger intended-vs-implemented"* | Intent vs code audit |
| [`security-and-hardening`](https://github.com/addyosmani/agent-skills/tree/main/skills/security-and-hardening) | `addyosmani/agent-skills` | Security | *"Trigger security-and-hardening"* | Security boundary enforcement |
| [`ast-resilient-remediation`](https://github.com/addyosmani/agent-skills/tree/main/skills/ast-resilient-remediation) | `addyosmani/agent-skills` | Refactoring | *"Trigger ast-resilient-remediation"* | Multi-file AST rewrites |
| [`code-review-and-quality`](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality) | `addyosmani/agent-skills` | Review | *"Trigger code-review-and-quality"* | Multi-axis pre-merge review |
| [`shipping-artifacts`](https://github.com/phuryn/pm-skills/tree/main/pm-ai-shipping/skills/shipping-artifacts) | `phuryn/pm-skills` | Handoff | *"Trigger shipping-artifacts"* | Handoff documentation packet |
| [`shipping-and-launch`](https://github.com/addyosmani/agent-skills/tree/main/skills/shipping-and-launch) | `addyosmani/agent-skills` | Deployment | *"Trigger shipping-and-launch"* | Pre-launch & rollback manifests |
| [`google-agents-cli-adk-code`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-adk-code) | `google/agents-cli` | Agent Code | *"Trigger google-agents-cli-adk-code"* | ADK Python code patterns |
| [`google-agents-cli-deploy`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-deploy) | `google/agents-cli` | Cloud Deploy | *"Trigger google-agents-cli-deploy"* | Automated Cloud Run/GKE deploy |
| [`google-agents-cli-eval`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-eval) | `google/agents-cli` | Evaluation | *"Trigger google-agents-cli-eval"* | Regression suite evaluation |
| [`google-agents-cli-publish`](https://github.com/google/agents-cli/tree/main/skills/google-agents-cli-publish) | `google/agents-cli` | Registry | *"Trigger google-agents-cli-publish"* | Registry index synchronization |
