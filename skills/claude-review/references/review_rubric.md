# Multi-Model Peer Review Rubric

This reference defines the evaluation criteria used by reviewer models during Phase 3 of the **Execute-Review-Revise** workflow.

---

## 1. Opus Tier (Simple Coding Tasks)

### Focus Areas
- **Syntax & Type Safety**: Ensure type annotations are strict, imports are correct, and syntax is valid.
- **Edge Case Robustness**: Check for null/undefined handling, boundary conditions, array bounds, and unhandled exceptions.
- **Simplicity & Cleanliness**: Verify that the code avoids over-engineering, unneeded helper functions, or unnecessary state.
- **Code Standard Compliance**: Ensure naming conventions, indentation, and formatting match existing workspace practices.

### Checklist
- [ ] No unhandled promise rejections or missing error boundaries.
- [ ] Functions are short, single-purpose, and easy to test.
- [ ] Variable and function names clearly express intent.
- [ ] No dead code, debug statements, or leftover logs.

---

## 2. Claude Fable 5 Tier (Complex Use Cases)

### Focus Areas
- **Architectural Coherence**: Verify that modular boundaries, interfaces, and data flows align with system design principles.
- **State Management & Concurrency**: Check for race conditions, deadlock risks, async flow correctness, and cache consistency.
- **Security & Threat Surface**: Inspect input sanitization, authentication/authorization boundaries, dependency safety, and secret leak risks.
- **Performance & Resource Efficiency**: Identify memory leaks, $O(N^2)$ loops, excessive RPCs/database queries, and unoptimized I/O.
- **Failure Recovery & Resiliency**: Ensure system degradation is graceful, fallbacks are deterministic, and error states are recoverable.

### Checklist
- [ ] API design maintains backwards compatibility or explicit versioning.
- [ ] Asynchronous code has proper timeouts, cancellation controls, and retry logic.
- [ ] Sensitive data paths conform to least-privilege principles.
- [ ] High-frequency execution paths are profiled for memory and CPU efficiency.
