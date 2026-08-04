import time
import threading
from typing import Dict, Any, Optional

class TokenBucketRateLimiter:
    """Thread-safe Token Bucket Rate Limiter with monotonic timing and full API support."""
    
    def __init__(self, capacity: int, refill_rate: float):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be greater than 0.")
            
        self.capacity: float = float(capacity)
        self.refill_rate: float = float(refill_rate)  # tokens per second
        self.tokens: float = float(capacity)
        self.last_refill: float = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self, now: float) -> None:
        """Helper to refill tokens based on elapsed time (must be called under lock)."""
        elapsed = now - self.last_refill
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now

    def allow_request(self, tokens_requested: int = 1) -> bool:
        if tokens_requested <= 0:
            raise ValueError("tokens_requested must be greater than 0.")

        with self._lock:
            now = time.monotonic()
            self._refill(now)

            if self.tokens >= tokens_requested:
                self.tokens -= tokens_requested
                return True
            return False

    def get_remaining_tokens(self) -> float:
        """Returns the current number of available tokens after applying pending refills."""
        with self._lock:
            now = time.monotonic()
            self._refill(now)
            return self.tokens

    def reset(self) -> None:
        """Resets the bucket to full capacity and resets the refill clock."""
        with self._lock:
            self.tokens = self.capacity
            self.last_refill = time.monotonic()
