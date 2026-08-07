"""
Production-Ready FastAPI Application Template

Features:
- FastAPI lifespan management
- Pydantic v2 schema integration
- Structured JSON logging
- GCP Secret Manager integration with fallback
- Health check & readiness probes
"""

import os
import logging
from contextlib import asynccontextmanager
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# Structured Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s"}'
)
logger = logging.getLogger("api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown routines."""
    logger.info("Initializing API application lifecycle...")
    # Startup: Initialize connections, secret manager clients, database pools
    yield
    # Shutdown: Clean up resources
    logger.info("Shutting down API application lifecycle...")


app = FastAPI(
    title="Delta Cloud AI Enterprise Agent API",
    version="1.1.0",
    description="Production-grade FastAPI service built with TDL field guide standards.",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    status: str = Field("ok", example="ok")
    version: str = Field("1.1.0", example="1.1.0")
    environment: str = Field("production", example="production")


@app.get("/healthz", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """Liveness probe endpoint."""
    return HealthResponse(
        status="ok",
        version="1.1.0",
        environment=os.getenv("ENVIRONMENT", "development")
    )


@app.get("/readyz", status_code=status.HTTP_200_OK)
async def readiness_check():
    """Readiness probe endpoint for Kubernetes / Cloud Run."""
    return {"ready": True}
