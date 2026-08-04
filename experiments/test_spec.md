# Test Specification: Async Job Worker Queue

Build an asynchronous job worker queue in Python with the following features:
1. `Job` dataclass with `job_id`, `payload`, `status` (`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`), and `result`.
2. `AsyncJobQueue` class:
   - `enqueue(job_id, payload)`: Enqueues a new job.
   - `process_next(worker_fn)`: Pops next pending job, executes `worker_fn(payload)` asynchronously, handles exceptions, updates status and result.
   - `get_status(job_id)`: Returns job status and result.
3. Include clean docstrings and type annotations.
