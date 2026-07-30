# AlphaEvolve Optimization Matrix Cheat-Sheet

Quick-reference evaluation matrix for applying AlphaEvolve evolutionary search to enterprise software domains.

---

## Domain Fitness & Scoring Matrix

| Domain | Best Evaluator Strategy | Target Fitness Metric | Concurrency (`-j`) | EVOLVE-BLOCK Scope |
|---|---|---|---|---|
| **SQL / BigQuery Query Opt** | Execution time ratio vs baseline | Execution latency (ms) | 4 | `WHERE`, `JOIN` & aggregation clauses |
| **Prompt & System Instruction Opt** | LLM-as-judge + test assertion suite | Accuracy score ($[0.0, 1.0]$) | 8 | System prompt & zero-shot examples |
| **Subagent Cost & Route Opt** | Cost & latency weighted composite | Composite score ($[0.0, 1.0]$) | 8 | Routing rules & model tier selection |
| **Algorithm / AST Remediation** | Pytest assertion suite + benchmark | Execution speed + pass rate | 4 | Pure algorithmic functions |

---

## Evaluator Rules
1. **CLI Compatibility**: Accept `--program-dir` and `--output-file`.
2. **NaN / Inf Guard**: Return `None` if execution fails or yields non-finite numbers.
3. **Execution Floor**: Enforce `timeout_seconds=30` to prevent hung evaluator loops.
