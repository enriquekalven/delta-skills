"""Async Job Worker Queue.

This module provides an asynchronous job queue mechanism using asyncio,
dataclasses, and string enums for tracking task states and outcomes.
"""

import asyncio
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, Optional, Tuple, Union


class JobStatus(str, Enum):
    """Enumeration of possible job execution states."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class Job:
    """Dataclass representing a job unit in the queue.

    Attributes:
        job_id: Unique string identifier for the job.
        payload: Input data payload required for processing.
        status: Execution status of the job (PENDING, RUNNING, COMPLETED, FAILED).
        result: Execution output payload upon completion or Exception on failure.
    """

    job_id: str
    payload: Any
    status: Union[JobStatus, str] = JobStatus.PENDING
    result: Any = None


class AsyncJobQueue:
    """Asynchronous job worker queue providing FIFO scheduling and status tracking."""

    def __init__(self) -> None:
        """Initialize an empty job queue and tracking dictionary."""
        self._queue: asyncio.Queue[str] = asyncio.Queue()
        self._jobs: Dict[str, Job] = {}
        self._lock: asyncio.Lock = asyncio.Lock()

    async def enqueue(self, job_id: str, payload: Any) -> Job:
        """Enqueue a new job into the queue.

        Args:
            job_id: Unique identifier for the job.
            payload: Payload data associated with the job.

        Returns:
            The created Job instance.

        Raises:
            ValueError: If job_id already exists in the queue.
        """
        async with self._lock:
            if job_id in self._jobs:
                raise ValueError(f"Job with ID '{job_id}' already exists in queue.")
            job = Job(job_id=job_id, payload=payload, status=JobStatus.PENDING)
            self._jobs[job_id] = job
            await self._queue.put(job_id)
            return job

    async def process_next(
        self,
        worker_fn: Callable[[Any], Any],
    ) -> Optional[Job]:
        """Pops the next pending job from the queue, executes worker_fn(payload) asynchronously,
        and updates the job status and result accordingly.

        Args:
            worker_fn: A sync or async function accepting payload and returning a result.

        Returns:
            The processed Job object, or None if the queue is empty.
        """
        try:
            job_id = self._queue.get_nowait()
        except asyncio.QueueEmpty:
            return None

        job = self._jobs.get(job_id)
        if job is None:
            return None

        job.status = JobStatus.RUNNING

        try:
            if asyncio.iscoroutinefunction(worker_fn):
                job.result = await worker_fn(job.payload)
            else:
                job.result = worker_fn(job.payload)
            job.status = JobStatus.COMPLETED
        except Exception as exc:
            job.result = exc
            job.status = JobStatus.FAILED
        finally:
            self._queue.task_done()

        return job

    def get_status(self, job_id: str) -> Tuple[Union[JobStatus, str], Any]:
        """Returns the current status and result for the given job_id.

        Args:
            job_id: Unique identifier of the job.

        Returns:
            A tuple of (status, result).

        Raises:
            KeyError: If job_id is not found in the queue.
        """
        if job_id not in self._jobs:
            raise KeyError(f"Job with ID '{job_id}' not found.")
        job = self._jobs[job_id]
        return job.status, job.result
