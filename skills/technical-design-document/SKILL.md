---
name: technical-design-document
description: >
  Synthesize meeting notes, architecture charts, API boundaries, and codebase indexes into an ironclad 6-section Technical Design Document (TDD)
  with system architecture diagrams, data flow models, trust boundaries, and Architecture Decision Records (ADRs).
  Triggers on: "technical design document", "tdd doc", "write tdd", "create tdd", "synthesize design", "technical design".
---

# Technical Design Document (TDD) Synthesis Protocol

This skill guides Technical Deployment Leads (TDLs) through synthesizing customer discovery notes, legacy codebase indexes, and system requirements into a formal, production-grade **Technical Design Document (TDD)** during Phase 2 (Weeks 3-6) before code implementation begins.

---

## 🏗️ The 6-Section Technical Design Document Template

A complete Technical Design Document must contain the following 6 sections:

```
1. EXECUTIVE SUMMARY & PROBLEM STATEMENT
2. SYSTEM ARCHITECTURE & COMPONENT MAP (Mermaid Diagram)
3. DATA FLOW & SEAM CONTRACTS (API Interfaces)
4. SECURITY, DATA PRIVACY & TRUST BOUNDARIES (InfoSec)
5. EVALUATION, TELEMETRY & OBSERVABILITY PIPELINE
6. ARCHITECTURE DECISION RECORDS (ADRs)
```

---

## 📋 Section Breakdown & Content Requirements

### Section 1: Executive Summary & Problem Statement
* High-level business goal and target CUJ (Customer User Journey).
* Explicit Technical Scope (Goals vs. Non-Goals).
* High-level performance latency and cost bounds.

### Section 2: System Architecture & Component Map
Visual Mermaid topology diagram showing model runtimes, adapters, databases, and external enterprise API gateways:
```mermaid
graph TD
    Client["Client Interface (Web/Voice)"] --> Gateway["API Gateway / SSO"]
    Gateway --> Agent Engine["Vertex AI ADK Python Reasoning Engine"]
    Agent Engine --> Tools["Tool Integrations / Adapters"]
    Tools --> Enterprise Systems["Enterprise ERP / CRM Databases"]
    Agent Engine --> Memory["Memory Bank / State Store"]
```

### Section 3: Data Flow & Seam Contracts
* Input/Output JSON schema definitions.
* Module boundary definitions adhering to the **Deep Module Principle** (simple interface, complex implementation).
* Error handling and fallback semantics (e.g. model degradation fallbacks).

### Section 4: Security, Data Privacy & Trust Boundaries
* STRIDE-A threat matrix summary.
* PII/PHI de-identification boundaries.
* Identity and Access Management (IAM) least-privilege profiles.
* Environment isolation rules (Argolis PoC vs. Client VPC Production).

### Section 5: Evaluation, Telemetry & Observability Pipeline
* Ground truth dataset selection strategy.
* `google-agents-cli-eval` scoring rubrics and Eval-on-Commit regression thresholds.
* Cloud Trace telemetry and BigQuery logging configuration.

### Section 6: Architecture Decision Records (ADRs)
Sequential log of architectural trade-offs:
* **ADR-001**: Choice of Agent Framework (e.g., Vertex AI ADK vs. LangChain).
* **ADR-002**: Database / State Persistence Strategy.
* **ADR-003**: Model Mixture (e.g., Gemini Flash for extraction vs. Gemini Pro for reasoning).

---

## ✋ Phase 2 TDD Verification Gate
- [ ] System topology diagram generated (Mermaid)
- [ ] Seam API contracts defined
- [ ] InfoSec trust boundaries and IAM profiles verified
- [ ] ADRs logged and committed to repository (`docs/TDD.md`)
- [ ] Client Principal Infrastructure Architect signed off on TDD
