---
name: agent-load-testing
description: >
  Load-test multi-agent Google Cloud systems the way the TDL Toolbox load-testing guide does:
  separate E2E user latency from model telemetry, model the 6-level parallelism stack
  (Locust workers -> virtual users -> Cloud Run gateway -> agent fan-out -> embedding/vector/FHIR
  -> Gemini synthesis), compute per-turn LLM fan-out and 5x-peak Vertex AI quotas with a
  deterministic calculator, diagnose the HTTP 429 retry amplification cascade, and apply the
  guide's 8 production optimizations. Triggers on "load test the agent", "agent quota sizing",
  "fan-out math", "429 retry cascade", "locust sse", "vertex rpm tpm quota".
metadata:
  version: '1.1'
---

# Multi-Agent Load Testing & Vertex AI Quota Sizing (`agent-load-testing`)

Source: TDL Toolbox *Executive Consulting Guide: Load Testing Design, Multi-Tier Parallelism, Infrastructure Quotas, Reports & Metrics, and Performance Optimizations* (Nova Scotia Health Clinician Search Agent, `ns-health-pso-clinical`, Sept 2026). Every number below is taken from that guide; anything this skill adds on top is marked **(repo convention)**.

**Reads:** `docs/TDD.md` (agent DAG, tools, models), `docs/PRD.md` (user concurrency targets).
**Writes:** `docs/LOAD_TEST_REPORT.md`.

---

## 1. Two latencies, never confused

| Perspective | What it measures | Where it comes from |
|---|---|---|
| **E2E user latency** | "Send" pressed in the UI → last token rendered. Sum of every sequential stage: safety classifier → query decomposition → tool/data retrieval (Qdrant + FHIR, 0 tokens) → chunked synthesis → final synthesis, **plus** queueing and any 429 back-off. | Locust client timers on the SSE stream |
| **Model telemetry latency** | One Gemini call: **input-token prefill** (grows with prompt/context size) + **output decode** (grows with generated tokens). | Vertex AI / sub-agent telemetry |

A fast model does not imply a fast turn: the guide's clinician query fans out into 20–30+ LLM calls, so E2E is dominated by fan-out, retrieval pools and quota behaviour.

---

## 2. The 6-level parallelism stack (what to scale at each level)

| Level | What runs in parallel | Component | Scaling control |
|---|---|---|---|
| **1. Load generator cluster** | Locust worker containers | Master + workers (`locust/Dockerfile`) on Cloud Run Jobs / Kubernetes | `--num-workers` |
| **2. Virtual users** | gevent greenlets, one per simulated clinician | `ClinicalSearchUser` (`locustfile.py`), `OIDCTokenManager` | `-u 100` users, `-r 5` ramp |
| **3. Server & gateway** | Cloud Run containers holding SSE streams | Cloud Run autoscaler, AlloyDB PostgreSQL | Max instances (e.g. `50`), concurrency (e.g. `80`), AlloyDB `max_connections` |
| **4. Agent core fan-out** | Sub-question research items | `ClinicalWorkflowAgent`, `asyncio.gather()` | `MAX_SUBQUESTIONS` (avg ≈ 6) |
| **5a/5b/5c. Retrieval** | Dense embeddings / dual dense+sparse vector prefetch / FHIR reads | `gemini-embedding-001`; Qdrant (`QDRANT_GRPC_POOL_SIZE`); Healthcare API | Embedding RPM quota + `_EMBED_SEMAPHORE`; gRPC pool `8 → 128`; `fhir_search_requests_per_minute` |
| **6. LLM synthesis** | Chunked Markdown synthesis over fact payloads | `gemini-2.5-flash` / `pro` | `generate_content_requests_per_minute`, `input_tokens_per_minute` |

---

## 3. Fan-out math and quota sizing (`scripts/calculate_agent_quotas.py`)

The guide's formula, implemented verbatim:

$$\text{LLM calls / turn} = 1\ (\text{Safety}) + 1\ (\text{Decomposition}) + (Q_t \times C_q)\ (\text{chunked synthesis}) + 1\ (\text{Final synthesis})$$

- $Q_t$ = sub-questions per query (guide average **≈ 6**); $C_q$ = chunks per sub-question (guide **≈ 2–4**).
- Result in the guide: **20–30+ LLM calls and 60+ vector queries per single turn** ("18 to 60 concurrent semantic queries, each spawning dense + sparse lookups — up to 120 concurrent gRPC requests").
- Guide's worked example: **10 doctors × 25 calls = 250 RPM; 250 × 20,000 tokens = 5,000,000 input TPM.**
- **Proactive quota sizing: provision 5× peak** ("5× Peak Multiplier based on the fan-out formulas").

```bash
# Guide inputs (Qt=6, Cq=4, 20k tokens/call, 10 simultaneous doctors, gRPC pool 8):
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py
# -> 27 LLM calls/turn, 270 peak RPM, 5,400,000 peak TPM, quota 1,350 RPM / 27,000,000 TPM,
#    600 concurrent vector gRPC requests = 75 queue waves on an 8-channel pool

# After the guide's fixes (pool 128, 60% context-cache hits, admission cap 8 turns):
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py \
  --grpc-pool-size 128 --cache-hit-ratio 0.6 --admission-cap 8
```

All parameters are explicit CLI flags; the script contains no hidden constants. `--json` emits the full breakdown for `docs/LOAD_TEST_REPORT.md`.

---

## 4. The HTTP 429 retry amplification cascade

1. Peak load saturates the Vertex AI RPM/TPM quota → a sub-agent call returns **429**.
2. The SDK backs off **1s → 2s → 4s → 8s** while the parent turn stays open.
3. Final synthesis waits on *all* sub-questions, so one 429 adds **+15 to +30 s of idle wait** to the whole answer.
4. **Thundering herd:** 30 parallel workers retry together and trigger secondary limits.
5. E2E latency crosses the gateway timeout (e.g. **60 s**) → the browser shows an error even though the backend eventually finishes.

Mitigations the guide builds into the architecture: global concurrency semaphores (`_EMBED_SEMAPHORE`), a traffic-queue admission controller, context caching + fact compression (prompt size **−60%+**), and 5× proactive quota sizing.

---

## 5. The guide's 8 production optimizations (with its measured impact)

| # | Optimization | Code location | Measured impact reported in the guide |
|---|---|---|---|
| 1 | **Vector search channel expansion** — `QDRANT_GRPC_POOL_SIZE` `8 → 128` (16× concurrency) | `env.py` | Eliminated client-side gRPC queuing that had caused **30+ second** synchronized waves |
| 2 | **Multi-component vital-sign compression** (BP panels: component-valued extraction → Min/Max/Mean/Latest) | `types.py` | 103-reading panel **11,074 → 4,933 chars (−55.5%)**, ≈ **1,535 tokens** saved per panel |
| 3 | **Stable-value categorical collapse** (identical consecutive readings → date spans) | `types.py` | **23,876 → 10,204 chars (−57.3%)**, ≈ **3,418 tokens** saved per patient brief |
| 4 | **Attachment text & narrative boilerplate truncation** | retrieval formatting | **45,000+ chars (≈ 10,500 tokens)** of boilerplate removed per multi-document query |
| 5 | **Vertex AI context caching** (static system instructions, **1-hour TTL**) | `manager.go` | **50–70% input-token savings**; lower TTFT by skipping redundant prefill |
| 6 | **Qdrant single-shard query routing** (route to the patient shard key instead of broadcasting) | `filters.go` | Lower search RTT and "drastically lower" cluster memory/CPU under load |
| 7 | **Traffic queue admission controller** | `queue.go` | Eliminated 429 quota exhaustion during shift-change peaks |
| 8 | **Structural scratchpad compression** (facts grouped by FHIR archetype + date) | `workflowagent/scratchpad.go` | Properly categorized clinical tables, no cell overflow |

---

## 6. Procedure

1. Pull $Q_t$, $C_q$, models, retrieval tools and token sizes from `docs/TDD.md`; pull the peak user target from `docs/PRD.md`.
2. Run `calculate_agent_quotas.py`; file the quota requests (Gemini RPM/TPM, embedding RPM, FHIR RPM, Cloud Run max instances) **before** the load test, at 5× peak.
3. Run the Locust suite (reference harness in [references/load-testing-and-quota-playbook.md](references/load-testing-and-quota-playbook.md)) as a Cloud Run Job against `dev`/`uat`; collect the report the master uploads to GCS.
4. Read the report in the guide's order: HTTP status breakdown (429 = quota, 503 = Cloud Run caps) → 5-second throughput timeline (find the burst that triggered 429s) → per-stage sub-agent latencies → E2E p50/p95/p99 for simple / moderate / complex queries.
5. Apply the optimizations in §5 in order of the bottleneck found; re-run; write `docs/LOAD_TEST_REPORT.md` with the before/after table **using only measured numbers**.

---

## 7. References & worked example

- [scripts/calculate_agent_quotas.py](scripts/calculate_agent_quotas.py) — deterministic fan-out / quota calculator (stdlib only, unit-tested).
- [references/load-testing-and-quota-playbook.md](references/load-testing-and-quota-playbook.md) — Locust SSE harness pattern (`ClinicalSearchUser`, `OIDCTokenManager`, landmark timers), report metrics catalog, component quota checklist.
- [examples/clinical-search-load-test-report.md](examples/clinical-search-load-test-report.md) — the guide's Nova Scotia Health case written up as `docs/LOAD_TEST_REPORT.md`, with the calculator's actual output and only the impacts the guide reports.
