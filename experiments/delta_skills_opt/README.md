# AlphaEvolve Optimization Experiment for Delta Skills

This directory contains a complete, verified AlphaEvolve experiment designed to hill-climb and optimize the meta-orchestration algorithms in `delta-skills` (`e2e-delivery-workflow`, `synthetic-baseline-protocol`, and `tdl-field-guide`).

## 📁 File Structure

| File | Description |
| --- | --- |
| `initial_program.py` | Seed program containing `# EVOLVE-BLOCK-START` / `# EVOLVE-BLOCK-END` target blocks. |
| `evaluator.py` | CLI-compatible evaluator script (`evaluate_program` & CLI `--program-dir`, `--output-file`). |
| `problem_description.md` | Task specification for LLM mutation prompts in AlphaEvolve. |
| `.evolve/experiment_description.json` | Experiment metadata & configuration. |
| `test_program.py` | Pytest suite testing initial program functionality. |
| `test_evaluator.py` | Pytest suite testing evaluator & CLI compliance. |
| `run_evolution_loop.py` | Hill-climbing control loop harness (supports local simulation & `ae` CLI cloud loop). |
| `pyproject.toml` | `uv` environment configuration. |

---

## 🚀 Running tests & Local Hill-Climbing Loop

### 1. Run pytest suite
```bash
uv run pytest
```

### 2. Run Local Hill-Climbing Evaluation Loop
```bash
uv run python run_evolution_loop.py --mode local --generations 20
```

### 3. Launch Cloud AlphaEvolve Experiment
```bash
ae experiment create --config .evolve/experiment_description.json
ae experiment run <NICKNAME> --evaluator evaluator.py --dashboard
```
