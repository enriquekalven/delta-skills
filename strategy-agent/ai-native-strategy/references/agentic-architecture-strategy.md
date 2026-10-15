# Agentic Architecture Strategy & Cost Reference

All token pricing and capability tiers reference [`model-economics-config.json`](model-economics-config.json).

---

## 1. Multi-Agent Orchestration Topologies

| Pattern | Topology | Best For | Token Multiplier | Production Readiness |
| :--- | :--- | :--- | :--- | :--- |
| **Single Agent + Deterministic Tools** | `User -> Agent -> Tools` | Bounded workflows ($\le 5$ tools, linear verification) | `1.0x – 1.3x` | **High** (Default choice) |
| **Supervisor / Router** | `Supervisor -> Specialist Agents 1..N` | Distinct domain boundaries, strict IAM tool segregation | `1.4x – 2.2x` | **High** |
| **Sequential Pipeline** | `Agent A -> Validator -> Agent B` | Document extraction $\rightarrow$ deterministic rule check $\rightarrow$ action | `1.3x – 1.8x` | **High** |
| **Parallel Fan-Out / Gather** | `Orchestrator -> [A, B, C] -> Synthesizer` | Independent checks (e.g., legal, financial, compliance review) | `1.5x – 2.5x` (lowest latency) | **High** |
| **Peer Swarm / Debate** | `Agent 1 <-> Agent 2 <-> Agent 3` | Open-ended research or adversarial red-teaming | `4.0x – 10.0x` | **Low–Medium** (Non-deterministic loop risk) |

### Selection Rule
1. Start with a **Single Agent + Deterministic Tools** or a **Sequential Pipeline**.
2. Introduce a **Supervisor / Router** only when tool count exceeds 10–12 or when sub-workflows require separate service-account IAM permissions.
3. Avoid unbounded **Peer Swarms** in transactional production paths unless bounded by hard turn and token budgets.

---

## 2. Token Unit Economics (Verified Math)

Assuming an **80% input / 20% output** token split per workflow execution:

$$\text{Blended Cost per 1M Tokens} = 0.80 \times \text{Input Rate} + 0.20 \times \text{Output Rate}$$

| Model Tier | Input ($/1M) | Output ($/1M) | Blended ($/1M) | Cost per 100K Tasks (@ 15K tokens/task = 1.5B tokens) |
| :--- | :--- | :--- | :--- | :--- |
| **Claude Opus 4.6** | `$5.00` | `$25.00` | `$9.00` | `$13,500` |
| **Gemini 3 Pro** | `$2.50` | `$10.00` | `$4.00` | `$6,000` |
| **GPT-5.2** | `$1.75` | `$14.00` | `$4.20` | `$6,300` |
| **DeepSeek-R1** | `$0.50` | `$2.00` | `$0.80` | `$1,200` |
| **Llama 4 Scout (Self-Hosted est.)** | `$0.40` | `$0.40` | `$0.40` | `$600` |

### Model Cascade / Downsampling Formula
Routing fraction $p$ of routine steps to a fast/low-cost tier ($C_{\text{fast}}$) and $(1 - p)$ of complex reasoning steps to a frontier model ($C_{\text{frontier}}$):

$$C_{\text{blended}} = p \cdot C_{\text{fast}} + (1 - p) \cdot C_{\text{frontier}}$$

- **Example (70% Llama 4 Scout / Flash + 30% Claude Opus 4.6):**
  - $C_{\text{blended}} = 0.70(\$0.40) + 0.30(\$9.00) = \$0.28 + \$2.70 = \$2.98\text{ per 1M tokens}$ (**66.9% cost reduction** vs. 100% Opus).

---

## 3. Memory & Context Architecture

| Pattern | Mechanism | Best For | Tradeoff |
| :--- | :--- | :--- | :--- |
| **Stateless + Structured Payload** | Pass only extracted JSON state between steps | Transactional triage, claims, underwriting | Lowest token cost; no cross-session memory |
| **Prompt Caching + Prefix Pinning** | Cache static system instructions, schemas, and policy manuals | Repeated queries over a stable 20K–100K token policy corpus | Cuts input token cost by 50%–75% on cached prefix |
| **Dual-Layer (Hot Window + Vector/SQL Cold Store)** | Keep last $k$ turns in context; retrieve historical facts via hybrid search / SQL | Customer support, multi-session case management | Requires indexing pipeline and citation verification |
