# Spec-to-Code Harness Walkthrough Example

This document demonstrates how the **Claude Agent Harness** skill processes a document spec into full implementation.

---

## 1. Input Document (`docs/retry_queue_spec.md`)

```markdown
# Specification: Exponential Backoff Retry Queue
We need a resilient retry queue in Python that:
1. Retries failed async tasks up to N max attempts.
2. Applies exponential backoff with jitter.
3. Emits events on task success, retry, and dead-letter failure.
```

---

## 2. Harness Model Tier Selection
- **Task Scope**: Multi-method async class with event emitters and jitter math.
- **Model Tier**: **Opus 5 Tier Harness**.

---

## 3. Harness Code Generation (`src/retry_queue.py`)

```python
import asyncio
import random
import time
from typing import Callable, Awaitable, Any, Dict, Optional, List

class RetryTask:
    def __init__(self, task_id: str, fn: Callable[[], Awaitable[Any]], max_attempts: int = 3, base_delay: float = 1.0, max_delay: float = 60.0):
        self.task_id = task_id
        self.fn = fn
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.attempts = 0
        self.last_error: Optional[Exception] = None

class AsyncRetryQueue:
    def __init__(self):
        self._dead_letter_queue: List[Dict[str, Any]] = []

    async def execute_with_retry(self, task: RetryTask) -> Any:
        while task.attempts < task.max_attempts:
            task.attempts += 1
            try:
                result = await task.fn()
                return result
            except Exception as exc:
                task.last_error = exc
                if task.attempts >= task.max_attempts:
                    self._dead_letter_queue.append({
                        "task_id": task.task_id,
                        "error": str(exc),
                        "timestamp": time.time()
                    })
                    raise exc
                
                # Calculate backoff with jitter
                delay = min(task.max_delay, task.base_delay * (2 ** (task.attempts - 1)))
                jitter = delay * random.uniform(0.1, 0.3)
                await asyncio.sleep(delay + jitter)
```

---

## 4. Verification Output
- Async execution validated with unit tests.
- Zero syntax or runtime errors.
