#!/usr/bin/env python3
"""Model Garden Vertex AI Opus 5 API Runner.

This script executes real Zero Data Retention (ZDR) API calls to Anthropic Claude Opus 5
hosted on Google Cloud Vertex AI Model Garden.
"""

import os
import sys

def call_opus(prompt: str) -> str:
    """Calls Vertex AI Model Garden Anthropic Opus 5 ZDR endpoint."""
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT") or "project-maui"
    region = os.environ.get("CLOUD_ML_REGION", "global")
    model_name = os.environ.get("CLAUDE_MODEL_NAME", "claude-opus-5")

    try:
        from anthropic import AnthropicVertex
    except ImportError:
        raise ImportError(
            "The 'anthropic[vertex]' package is missing. "
            "Please run: pip install anthropic[vertex]"
        )

    # Initialize Anthropic Client via Vertex AI Application Default Credentials
    client = AnthropicVertex(region=region, project_id=project_id)

    # Call Model Garden ZDR Opus 5 endpoint
    message = client.messages.create(
        model=model_name,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract text from content blocks (handling thinking blocks if present)
    text_blocks = [block.text for block in message.content if getattr(block, "type", "") == "text"]
    if text_blocks:
        return "\n".join(text_blocks)

    return str(message.content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_prompt = " ".join(sys.argv[1:])
    else:
        input_prompt = sys.stdin.read()

    if not input_prompt.strip():
        print("Error: Empty prompt provided.", file=sys.stderr)
        sys.exit(1)

    output = call_opus(input_prompt)
    print(output)
