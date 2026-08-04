import time
import unittest
from test_execute_review_revise import TokenBucketRateLimiter

class TestTokenBucketRateLimiter(unittest.TestCase):
    def test_basic_allow(self):
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        self.assertTrue(limiter.allow_request(3))
        self.assertTrue(limiter.allow_request(2))
        self.assertFalse(limiter.allow_request(1))

    def test_refill(self):
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=5.0)
        self.assertTrue(limiter.allow_request(2))
        self.assertFalse(limiter.allow_request(1))
        time.sleep(0.3)  # Refills ~1.5 tokens
        self.assertTrue(limiter.allow_request(1))

    def test_invalid_args(self):
        with self.assertRaises(ValueError):
            TokenBucketRateLimiter(capacity=0, refill_rate=1.0)
        
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        with self.assertRaises(ValueError):
            limiter.allow_request(0)

    def test_reset(self):
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        limiter.allow_request(5)
        self.assertLess(limiter.get_remaining_tokens(), 1.0)
        limiter.reset()
        self.assertEqual(limiter.get_remaining_tokens(), 5.0)

if __name__ == "__main__":
    unittest.main()
