# Load-Testing & Quota Playbook (Locust SSE harness, report metrics, component quotas)

Companion to [SKILL.md](../SKILL.md). Sections 1–3 restate what the TDL load-testing guide specifies; the code in §2 is a **reference pattern modeled on the guide's described components** (`locustfile.py`, `ClinicalSearchUser`, `OIDCTokenManager`, master/worker seeding, Cloud Run Job execution, GCS report upload). The engagement's actual source is not part of the toolbox export — adapt names and payloads to your agent's `/api/run_sse` contract.

---

## 1. How the guide's Locust suite operates

1. **Realistic clinician workflows:** virtual users (`ClinicalSearchUser`) run Simple / Moderate / Complex queries with **4–8 s think time** between searches.
2. **Distributed master/worker data seeding:** the master downloads `active_patientids.csv` once from GCS and broadcasts IDs to workers over TCP IPC; workers cycle through them.
3. **OIDC auth at scale:** `OIDCTokenManager` refreshes identity tokens for Cloud Run / IAP in parallel so token minting is not the bottleneck.
4. **Streaming-aware timing:** SSE responses are read event-by-event; stage landmarks (safety, decomposer, tool retrieval, synthesis) are recorded as separate Locust request entries.
5. **Headless Cloud Run deployment:** containerized (`locust/Dockerfile`) and executed as a Cloud Run Job (`gcloud run jobs execute load-test`) in `dev` and `uat` CI/CD; on completion the master compiles an executive Markdown report and uploads it to `gs://{PATIENT_ID_BUCKET}/load_test_results/`.

Typical invocation per the guide: `-u 100` (user budget), `-r 5` (ramp rate), `--num-workers` scaled to avoid CPU throttling on the generator side.

---

## 2. Reference harness pattern (`locustfile.py`)

```python
import json
import subprocess
import threading
import time

from locust import HttpUser, between, events, task


class OIDCTokenManager:
    """Shared, thread-safe OIDC bearer token for Cloud Run / IAP targets.

    Refreshes well before the ~1h expiry so hundreds of greenlets never mint tokens
    individually under load.
    """

    def __init__(self, refresh_after_sec: int = 2700) -> None:
        self._lock = threading.Lock()
        self._token = ""
        self._expires_at = 0.0
        self._refresh_after = refresh_after_sec

    def get_token(self) -> str:
        if self._token and time.time() < self._expires_at:
            return self._token
        with self._lock:
            if self._token and time.time() < self._expires_at:
                return self._token
            self._token = subprocess.check_output(
                ["gcloud", "auth", "print-identity-token"], text=True
            ).strip()
            self._expires_at = time.time() + self._refresh_after
            return self._token


TOKENS = OIDCTokenManager()

QUERIES = {
    "02_Simple": "Latest HbA1c for this patient?",
    "03_Moderate": "Summarize blood pressure trend over the last 12 months.",
    "04_Complex": "Build a longitudinal brief: active conditions, medication changes, "
                  "abnormal labs and imaging findings for the last 3 years.",
}


class ClinicalSearchUser(HttpUser):
    wait_time = between(4, 8)  # guide: realistic 4-8 s think time

    @task
    def complex_query(self) -> None:
        self._run("04_Complex")

    @task
    def moderate_query(self) -> None:
        self._run("03_Moderate")

    @task
    def simple_query(self) -> None:
        self._run("02_Simple")

    def _run(self, name: str) -> None:
        patient_id = self.environment.parsed_options.patient_ids.pop()  # seeded by master
        payload = {
            "app_name": "clinical_search_agent",
            "user_id": "loadtest",
            "session_id": f"s-{int(time.time() * 1000)}",
            "new_message": {"role": "user", "parts": [{"text": QUERIES[name]}]},
            "state_delta": {"patient_id": patient_id},
            "streaming": True,
        }
        headers = {
            "Authorization": f"Bearer {TOKENS.get_token()}",
            "Accept": "text/event-stream",
        }
        t0 = time.perf_counter()
        seen_first = False
        with self.client.post(
            "/api/run_sse", json=payload, headers=headers, stream=True,
            catch_response=True, name=f"{name} Streaming RTT",
        ) as resp:
            if resp.status_code != 200:
                resp.failure(f"HTTP {resp.status_code}")  # 429 = quota, 503 = Cloud Run caps
                return
            for line in resp.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data:"):
                    continue
                now = time.perf_counter()
                if not seen_first:
                    seen_first = True
                    _landmark("ttft", now - t0, len(line))
                body = line[5:].strip()
                if body == "[DONE]":
                    break
                try:
                    author = json.loads(body).get("author", "")
                except ValueError:
                    continue
                if author in ("safety_agent", "decomposer_agent", "tool_retrieval", "synthesis_agent"):
                    _landmark(author, now - t0, len(body))
            resp.success()


def _landmark(name: str, seconds: float, size: int) -> None:
    events.request.fire(
        request_type="SSE", name=f"landmark:{name}",
        response_time=seconds * 1000.0, response_length=size, exception=None,
    )
```

---

## 3. Report metrics catalog (read in this order)

| Category | Metric | Why it matters (per the guide) |
|---|---|---|
| Error rates | HTTP status breakdown `200 / 429 / 500 / 503` | **429 = quota exhaustion; 503 = Cloud Run capacity caps** |
| Throughput | 5-second token & request timeline | Pinpoints the exact burst that triggered 429 rate limiting |
| REST latency | `00_Handshake` p50/p95/p99 (AlloyDB session) | High p95 = DB socket contention / pool exhaustion |
| Query latency | `02_Simple`, `03_Moderate`, `04_Complex` streaming RTT | Verifies clinical SLAs per query class |
| Component telemetry | Sub-agent latencies: Safety, Decomposer, Tool Retrieval, Synthesis | Shows whether slowness is the LLM or the retrieval layer |

---

## 4. Component quota checklist (file requests before the test, at 5× peak)

| Component | Quota / limit | Failure signature |
|---|---|---|
| Vertex AI Gemini | `generate_content_requests_per_minute` (RPM) | HTTP 429 → retries → latency spikes |
| Vertex AI Gemini | `generate_content_input_tokens_per_minute` (TPM, millions) | HTTP 429; blocks large longitudinal prompts |
| Vertex AI Embeddings | `online_prediction_requests_per_minute` | Throttled dense-vector creation (`gemini-embedding-001`) |
| Cloud Run service | Container concurrency & max instances (e.g. `80` / `50`) | Queued requests or HTTP 503 |
| Qdrant | `QDRANT_GRPC_POOL_SIZE` (`128`), segment threads, RAM | Vector query queuing, socket timeouts, 30 s+ responses |
| AlloyDB PostgreSQL | Max connections, read-pool instances | Handshake p95 climbs |
| Healthcare API | `fhir_search_requests_per_minute` | FHIR read throttling |

Use `scripts/calculate_agent_quotas.py --json` for the Gemini RPM/TPM numbers; the others come from `docs/TDD.md` capacity assumptions.
