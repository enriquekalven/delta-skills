# Execute-Review-Revise Workflow Example Walkthrough

This document illustrates how the **Execute-Review-Revise** skill operates in practice.

---

## Scenario: User requests a caching wrapper for an API call

### 1. Phase 1: Baseline Execution (Gemini 3.6 Flash)
The primary model immediately builds the baseline implementation in the workspace (e.g., `src/cache.ts`).

```typescript
export class ApiCache<T> {
  private cache = new Map<string, { data: T; timestamp: number }>();
  constructor(private ttlMs: number = 60000) {}

  get(key: string): T | null {
    const item = this.cache.get(key);
    if (!item) return null;
    if (Date.now() - item.timestamp > this.ttlMs) {
      this.cache.delete(key);
      return null;
    }
    return item.data;
  }

  set(key: string, data: T): void {
    this.cache.set(key, { data, timestamp: Date.now() });
  }
}
```

---

### 2. Phase 2: Complexity Triage & Assignment
- **Assessment**: Simple utility class (Single file, localized logic).
- **Designated Reviewer**: **Opus Tier Reviewer**.

---

### 3. Phase 3: Peer Review Critique (Opus Tier Subagent)

**Critique Output**:
```markdown
### Peer Review Report
- **Reviewer Tier**: Opus Tier
- **Complexity Assessment**: Simple Coding
- **Overall Verdict**: NEEDS_REVISION

#### Key Findings:
1. **Memory Leak**: Expired entries are only deleted on `get()`. If keys are written once and never read again, memory grows unbounded.
2. **Missing Invalidation/Clear**: No method provided to purge cache manually.

#### Recommended Revisions:
- Add a periodic sweep or max size eviction rule.
- Add `.clear()` and `.delete(key)` methods.
```

---

### 4. Phase 4: Revision & Refinement (Gemini 3.6 Flash)
The primary model applies the recommended fixes:

```typescript
export class ApiCache<T> {
  private cache = new Map<string, { data: T; timestamp: number }>();

  constructor(
    private ttlMs: number = 60000,
    private maxEntries: number = 500
  ) {}

  get(key: string): T | null {
    const item = this.cache.get(key);
    if (!item) return null;
    if (Date.now() - item.timestamp > this.ttlMs) {
      this.cache.delete(key);
      return null;
    }
    return item.data;
  }

  set(key: string, data: T): void {
    if (this.cache.size >= this.maxEntries) {
      const oldestKey = this.cache.keys().next().value;
      if (oldestKey !== undefined) this.cache.delete(oldestKey);
    }
    this.cache.set(key, { data, timestamp: Date.now() });
  }

  delete(key: string): boolean {
    return this.cache.delete(key);
  }

  clear(): void {
    this.cache.clear();
  }
}
```

The user is presented with the final revised code and a summary of what changed during review.
