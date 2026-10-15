# Worked Example: `docs/LOAD_TEST_REPORT.md` — Nova Scotia Health Clinician Search Agent

> [!NOTE]
> Provenance: the architecture, fan-out inputs, optimizations and every impact figure below come from the TDL Toolbox load-testing guide for the **Nova Scotia Health (NSH) Clinician Search Agent** (`ns-health-pso-clinical`, Sept 2026). The quota table is the actual output of `scripts/calculate_agent_quotas.py` on the guide's inputs. Where the guide gives a qualitative result ("eliminated", "drastically lower") no number is invented.

**System:** Cloud Run SSE gateway → ADK workflow agent (Gemini safety classifier → query decomposer → tool retrieval over **Qdrant** vector DB + **GCP FHIR Store** → chunked synthesis → final synthesis on `gemini-2.5-flash/pro`), AlloyDB sessions, `gemini-embedding-001`.
**Business constraint:** evidence-based answers for busy clinicians **without** exceeding Cloud API quotas, triggering HTTP 429, or unsustainable token cost.

---

## 1. Fan-out audit (`calculate_agent_quotas.py`)

Guide inputs: $Q_t ≈ 6$ sub-questions, $C_q ≈ 2–4$ chunks, 20,000 tokens per call, 10 simultaneous doctors, default `QDRANT_GRPC_POOL_SIZE = 8`.

```bash
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py            # Cq = 4
python3 delivery/agent-load-testing/scripts/calculate_agent_quotas.py --chunks-per-subquestion 3
```

| Quantity | Formula | $C_q = 3$ | $C_q = 4$ | Guide's rounded slide figure |
|---|---|---|---|---|
| LLM calls / turn | $1 + 1 + Q_t C_q + 1$ | **21** | **27** | "20 to 30+" (uses ~25) |
| Vector gRPC requests / turn | 30 semantic × 2 (dense + sparse) | 60 | 60 | "60+ vector queries" (18–60 semantic → up to 120 gRPC) |
| Peak LLM RPM | 10 turns × calls | **210** | **270** | 10 × 25 = **250** |
| Peak input TPM | RPM × 20,000 | **4,200,000** | **5,400,000** | 250 × 20,000 = **5,000,000** |
| Concurrent vector gRPC requests | 10 × 60 | 600 | 600 | — |
| Queue waves on 8-channel pool | ⌈600 / 8⌉ | 75 | 75 | "slow synchronized waves, 30+ s" |
| **Quota: `generate_content` RPM (5×)** | 5 × peak | **1,050** | **1,350** | 1,250 |
| **Quota: input TPM (5×)** | 5 × peak | **21,000,000** | **27,000,000** | 25,000,000 |

Actual script output for the default run:

```text
=== Agentic Fan-Out & Vertex AI Quota Sizing ===
LLM calls / turn            : 27  (= 1 safety + 1 decomp + 6 x 4 chunked + 1 final)
Vector gRPC requests / turn : 60  (= 30 semantic x 2 prefetch modes)
-----------------------------------------------
Peak LLM RPM                : 270  (= 10 turns/min x 27)
Peak input TPM              : 5,400,000  (= RPM x 20,000 tokens/call)
Concurrent vector gRPC reqs : 600  -> 75 queue waves at pool size 8
-----------------------------------------------
Quota: generate_content RPM : 1,350  (5x peak)
Quota: input TPM            : 27,000,000  (5x peak)
```

After the guide's fixes (`--grpc-pool-size 128 --cache-hit-ratio 0.6 --admission-cap 8`): 600 concurrent gRPC requests collapse from **75 → 5 queue waves**, peak input TPM after cache drops **5,400,000 → 2,160,000**, and an admission cap of 8 turns holds admitted LLM load at **216 RPM** with 2 turns queued instead of fanning out into 429s.

---

## 2. Failure mode observed before optimization (as described in the guide)

- Decomposition emitted **18–60 concurrent semantic queries → up to 120 concurrent gRPC requests** against a client limited to **8** gRPC connections → requests queued in synchronized waves with **30+ second** stalls.
- Peak clinician load saturated Gemini RPM/TPM → **429** → exponential back-off **1 s → 2 s → 4 s → 8 s**; because final synthesis waits for *all* sub-questions, a single 429 added **+15 to +30 s** of idle wait; 30 parallel retries created a thundering herd and pushed E2E past the **60 s** gateway timeout.
- Prompt bloat: one 103-reading blood-pressure panel dumped as **11,074 characters (~3,000 tokens)**; 21 identical "Never smoked tobacco" entries consumed **~21% of the scratchpad (23,876 chars)**; a 247-document note cluster took **27.6% of the scratchpad (25,800 chars)**.

---

## 3. Optimizations applied and measured impact (guide §8)

| # | Change | Measured impact (guide) |
|---|---|---|
| 1 | `QDRANT_GRPC_POOL_SIZE` **8 → 128** (`env.py`) | Client-side gRPC queuing **eliminated**; multi-query lookups run in parallel without blocking the event loop |
| 2 | Component-valued BP extraction → Min/Max/Mean/Latest (`types.py`) | **11,074 → 4,933 chars (−55.5%)**, **~1,535 tokens/panel** |
| 3 | Chronological run-collapse of identical categorical readings (`types.py`) | **23,876 → 10,204 chars (−57.3%)**, **~3,418 tokens/brief** |
| 4 | Attachment text & narrative boilerplate truncation | **45,000+ chars (~10,500 tokens)** removed per multi-document query |
| 5 | Vertex AI context caching, **1-hour TTL** (`manager.go`) | **50–70% input-token savings**, lower TTFT |
| 6 | Qdrant single-shard routing by patient shard key (`filters.go`) | Faster search RTT; "drastically lower" cluster CPU/memory under load |
| 7 | Traffic queue admission controller (`queue.go`) | **429 quota exhaustion eliminated** during shift-change peaks |
| 8 | Structural scratchpad grouping by FHIR archetype + date (`scratchpad.go`) | Correctly categorized clinical tables, no cell overflow |

Combined prompt reduction from fact compression: **>60% smaller prompts**, on top of the 50–70% cached-token discount.

---

## 4. Quota requests filed (5× peak, from §1)

| Quota | Requested |
|---|---|
| `generate_content_requests_per_minute` | 1,350 ($C_q = 4$) |
| `generate_content_input_tokens_per_minute` | 27,000,000 (10,800,000 if the 60% cache hit ratio is sustained) |
| `online_prediction_requests_per_minute` (embeddings) | 10 turns × 6 sub-questions = 60 peak RPM → × 5 = 300 |
| Cloud Run | max instances 50, concurrency 80 |
| Qdrant | gRPC pool 128; cluster RAM / segment threads sized for 600 concurrent lookups |

---

## 5. Executive recommendations carried into `docs/TDD.md`

1. Multi-layer token optimization (fact compression + context caching) directly lowers cost and latency.
2. A traffic queue is mandatory in architectures where one query triggers **25+ backend calls**.
3. Vector sharding must align with patient isolation (single-shard routing).
4. Size quotas proactively at **5× peak** using the fan-out formula — do not wait for the first 429.
