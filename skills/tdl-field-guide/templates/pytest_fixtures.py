"""
Production-Ready PyTest Fixtures Template

Features:
- Async HTTP client fixture via httpx
- Isolated environment variable overrides
- Mock GCP Secret Manager client
"""

import pytest
import os
from typing import AsyncGenerator
from unittest.mock import MagicMock
from httpx import AsyncClient, ASGITransport
from fastapi_main import app


@pytest.fixture(scope="session")
def env_override():
    """Provides isolated environment variable overrides during test suite execution."""
    os.environ["ENVIRONMENT"] = "testing"
    os.environ["GOOGLE_CLOUD_PROJECT"] = "test-project-maui"
    yield
    os.environ.pop("ENVIRONMENT", None)


@pytest.fixture
async def async_client(env_override) -> AsyncGenerator[AsyncClient, None]:
    """Provides an AsyncClient for testing FastAPI endpoints without running a network server."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_secret_manager():
    """Provides a mock client for GCP Secret Manager."""
    mock_client = MagicMock()
    mock_client.access_secret_version.return_value.payload.data.decode.return_value = "mock_secret_val"
    return mock_client
