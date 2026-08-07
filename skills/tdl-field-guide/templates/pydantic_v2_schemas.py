"""
Production-Ready Pydantic v2 Schema Template

Features:
- Pydantic v2 BaseModel & ConfigDict
- Strict type validation
- OpenAPI JSON Schema metadata & examples
- Custom validators
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator


class AgentRequestSchema(BaseModel):
    """Schema for incoming Agent Execution Requests."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "session_id": "sess_12345",
                "prompt": "Recommend GCP Agent architecture for PRD",
                "max_tokens": 2048,
                "metadata": {"user_role": "architect"}
            }
        }
    )

    session_id: str = Field(..., min_length=5, max_length=64, description="Unique session identifier")
    prompt: str = Field(..., min_length=1, max_length=10000, description="User or system prompt input")
    max_tokens: Optional[int] = Field(2048, ge=1, le=8192, description="Token budget limit")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Contextual key-value metadata")

    @field_validator("prompt")
    @classmethod
    def validate_prompt_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Prompt must not be empty or whitespace-only.")
        return v


class AgentResponseSchema(BaseModel):
    """Schema for outgoing Agent Execution Responses."""
    model_config = ConfigDict(frozen=True)

    session_id: str = Field(..., description="Unique session identifier")
    status: str = Field(..., example="COMPLETED")
    output_text: str = Field(..., description="Generated text or response payload")
    execution_time_ms: float = Field(..., ge=0.0, description="Processing time in milliseconds")
    token_usage: Dict[str, int] = Field(default_factory=dict, description="Token consumption metrics")
