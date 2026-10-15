# Worked Example: Claims Intake & Policy Extraction Service (`docs/TDD.md`)

This example demonstrates a complete `docs/TDD.md` produced from `docs/PRD.md` and `docs/ARCHITECTURE_RECOMMENDATION.md` for Acme Commercial Insurance's FNOL Triage Agent.

---

## 1. System Context & Module Layout

- **Source PRD:** `docs/PRD.md` (Commercial Auto FNOL Intake & Triage Agent)
- **Source Architecture:** `docs/ARCHITECTURE_RECOMMENDATION.md` (Tier 2: Google ADK on Vertex AI Agent Engine + Cloud SQL PostgreSQL + BigQuery)
- **Target Runtime:** Python 3.12, `google-adk>=1.0.0`, `pydantic>=2.7.0`, `httpx>=0.27.0`

```text
src/
  claims_triage/
    __init__.py
    models.py          # Pydantic v2 input/output and citation schemas
    tools.py           # Guidewire lookup and Document AI wrapper tools
    evaluator.py       # Deterministic policy coverage & escalation rules
    agent.py           # ADK LlmAgent and SequentialAgent definition
tests/
  test_models.py
  test_evaluator.py
  test_agent_flow.py
```

---

## 2. Data Schemas & Storage DDL

### 2.1 Domain Models (`src/claims_triage/models.py`)

```python
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class TriageRoutingDecision(str, Enum):
    FAST_TRACK = "FAST_TRACK"
    STANDARD_ADJUSTER = "STANDARD_ADJUSTER"
    SENIOR_COMPLEX = "SENIOR_COMPLEX"
    HUMAN_ESCALATION = "HUMAN_ESCALATION"


class EvidenceCitation(BaseModel):
    document_id: str = Field(..., min_length=1)
    page_number: int = Field(..., ge=1)
    bounding_box: tuple[float, float, float, float] = Field(
        ..., descriptionNormalized="(x0, y0, x1, y1) in [0.0, 1.0]"
    )
    extracted_text: str = Field(..., min_length=1)
    confidence: float = Field(..., ge=0.0, le=1.0)


class FnolExtraction(BaseModel):
    claim_id: str = Field(..., pattern=r"^CLM-\d{4}-\d{5}$")
    policy_number: str = Field(..., pattern=r"^POL-CA-\d{6}$")
    loss_date: date
    vin: str = Field(..., min_length=17, max_length=17)
    claimed_amount_usd: Decimal = Field(..., ge=Decimal("0.00"))
    bodily_injury_reported: bool
    subrogation_indicator: bool
    citations: dict[str, EvidenceCitation]

    @field_validator("vin")
    @classmethod
    def validate_vin_uppercase(cls, v: str) -> str:
        return v.upper()


class TriagePacket(BaseModel):
    claim_id: str
    policy_number: str
    routing_decision: TriageRoutingDecision
    recommended_reserve_usd: Decimal
    escalation_reasons: list[str] = Field(default_factory=list)
    extraction: FnolExtraction
    generated_at: datetime
```

### 2.2 Audit & Telemetry Schema (BigQuery)

```sql
CREATE TABLE IF NOT EXISTS `acme_claims_prod.fnol_triage_audit` (
  claim_id STRING NOT NULL,
  policy_number STRING NOT NULL,
  routing_decision STRING NOT NULL,
  recommended_reserve_usd NUMERIC NOT NULL,
  escalation_reasons ARRAY<STRING>,
  min_citation_confidence FLOAT64 NOT NULL,
  processing_latency_ms INT64 NOT NULL,
  model_version STRING NOT NULL,
  created_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(created_at)
CLUSTER BY routing_decision, policy_number;
```

---

## 3. API & Tool Contracts

### 3.1 `fetch_policy_endorsements` (`FR-2`)
- **Signature:** `def fetch_policy_endorsements(policy_number: str, loss_date: str) -> dict`
- **Upstream Endpoint:** `GET https://guidewire.internal.acme.com/v2/policies/{policy_number}/coverage?as_of={loss_date}`
- **Timeout & Idempotency:** `5.0s` read timeout; safe idempotent `GET`.
- **Error Handling:**

| Condition | Error Code | Retry Policy | Fallback Behavior |
| :--- | :--- | :--- | :--- |
| Invalid policy format | `400 Bad Request` | Do not retry | Route immediately to `HUMAN_ESCALATION` with reason `INVALID_POLICY_NUMBER` |
| Policy not found | `404 Not Found` | Do not retry | Route to `HUMAN_ESCALATION` with reason `POLICY_NOT_FOUND` |
| Guidewire rate limit / 5xx | `429` / `503` | 3 attempts, exponential backoff (`0.5s`, `1.0s`, `2.0s`) | Route to `HUMAN_ESCALATION` with reason `UPSTREAM_GUIDEWIRE_UNAVAILABLE` |

### 3.2 `evaluate_triage_routing` (`FR-3`, `FR-4`)
- **Signature:** `def evaluate_triage_routing(extraction: FnolExtraction, policy_active: bool, deductible_usd: Decimal) -> TriagePacket`
- **Deterministic Rules (`src/claims_triage/evaluator.py`):**
  1. If any required field citation in `extraction.citations` has `confidence < 0.85`, return `TriageRoutingDecision.HUMAN_ESCALATION` with reason `LOW_OCR_CONFIDENCE:{field_name}`.
  2. If `not policy_active`, return `TriageRoutingDecision.HUMAN_ESCALATION` with reason `INACTIVE_POLICY_ON_LOSS_DATE`.
  3. If `extraction.bodily_injury_reported` or `extraction.claimed_amount_usd > Decimal("25000.00")`, return `TriageRoutingDecision.SENIOR_COMPLEX`.
  4. If `extraction.claimed_amount_usd <= Decimal("5000.00")` and not `extraction.subrogation_indicator`, return `TriageRoutingDecision.FAST_TRACK`.
  5. Otherwise, return `TriageRoutingDecision.STANDARD_ADJUSTER`.

---

## 4. Security, IAM & Configuration

| Variable | Example Value | Description |
| :--- | :--- | :--- |
| `GOOGLE_CLOUD_PROJECT` | `acme-claims-prod` | Vertex AI & BigQuery project ID |
| `GUIDEWIRE_BASE_URL` | `https://guidewire.internal.acme.com` | Internal Guidewire REST gateway |
| `MIN_CITATION_CONFIDENCE` | `0.85` | Hard floor before human escalation |

---

## 5. Verification & Acceptance Matrix

| PRD Requirement | Test File | Test Case | Acceptance Command |
| :--- | :--- | :--- | :--- |
| `FR-1`: Validated schema & citations | `tests/test_models.py` | `test_fnol_extraction_validates_vin_and_citations` | `pytest tests/test_models.py -q` |
| `FR-2`: Guidewire retry & fallback | `tests/test_agent_flow.py` | `test_guidewire_503_triggers_human_escalation` | `pytest tests/test_agent_flow.py -q` |
| `FR-3`: Confidence `< 0.85` escalation | `tests/test_evaluator.py` | `test_low_confidence_forces_human_escalation` | `pytest tests/test_evaluator.py -q` |
| `FR-4`: Fast-track vs Senior routing | `tests/test_evaluator.py` | `test_bodily_injury_routes_to_senior_complex` | `pytest tests/test_evaluator.py -q` |
