import asyncio
import unittest
from test_claude_harness_output import AsyncJobQueue, JobStatus

class TestAsyncJobQueue(unittest.IsolatedAsyncioTestCase):
    async def test_enqueue_and_process_sync_worker(self):
        queue = AsyncJobQueue()
        job = await queue.enqueue("j1", {"x": 10, "y": 20})
        self.assertEqual(job.status, JobStatus.PENDING)

        def sync_worker(payload):
            return payload["x"] + payload["y"]

        processed_job = await queue.process_next(sync_worker)
        self.assertIsNotNone(processed_job)
        self.assertEqual(processed_job.status, JobStatus.COMPLETED)
        self.assertEqual(processed_job.result, 30)

        status, result = queue.get_status("j1")
        self.assertEqual(status, JobStatus.COMPLETED)
        self.assertEqual(result, 30)

    async def test_process_async_worker_failure(self):
        queue = AsyncJobQueue()
        await queue.enqueue("j2", "error_payload")

        async def async_failing_worker(payload):
            await asyncio.sleep(0.01)
            raise ValueError("Task processing failed")

        processed_job = await queue.process_next(async_failing_worker)
        self.assertIsNotNone(processed_job)
        self.assertEqual(processed_job.status, JobStatus.FAILED)
        self.assertIsInstance(processed_job.result, ValueError)

if __name__ == "__main__":
    unittest.main()
