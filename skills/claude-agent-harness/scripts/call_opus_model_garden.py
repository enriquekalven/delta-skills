#!/usr/bin/env python3
"""Model Garden Vertex AI Opus 5 API Runner.

This script executes Zero Data Retention (ZDR) API calls to Anthropic Claude Opus 5
hosted on Google Cloud Vertex AI Model Garden.
"""

import argparse
import os
import sys
import time

def call_opus(prompt: str) -> str:
    """Calls Vertex AI Model Garden Anthropic Opus 5 ZDR endpoint with retry backoff."""
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT")
    region = os.environ.get("CLOUD_ML_REGION", "us-central1")
    model_name = os.environ.get("CLAUDE_MODEL_NAME", "claude-opus-5")

    if not project_id:
        raise ValueError(
            "GOOGLE_CLOUD_PROJECT environment variable is not set.\n"
            "Please run: export GOOGLE_CLOUD_PROJECT='your-project-id'"
        )

    try:
        from anthropic import AnthropicVertex
    except ImportError:
        raise ImportError(
            "The 'anthropic[vertex]' package is missing.\n"
            "Please run: pip install anthropic[vertex]"
        )

    # Initialize Anthropic Client via Vertex AI Application Default Credentials
    client = AnthropicVertex(region=region, project_id=project_id)

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            message = client.messages.create(
                model=model_name,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
            )
            text_blocks = [block.text for block in message.content if getattr(block, "type", "") == "text"]
            if text_blocks:
                return "\n".join(text_blocks)
            return str(message.content)
        except Exception as e:
            if attempt == max_retries:
                raise e
            wait_time = 2 ** attempt
            print(f"⚠️ Model Garden API call failed (attempt {attempt}/{max_retries}): {e}. Retrying in {wait_time}s...", file=sys.stderr)
            time.sleep(wait_time)


def parse_args():
    parser = argparse.ArgumentParser(description="Call Vertex AI Model Garden Opus 5 ZDR Endpoint")
    parser.add_argument("prompt_pos", nargs="*", help="Direct prompt arguments")
    parser.add_argument("-p", "--prompt", help="Direct prompt string")
    parser.add_argument("-s", "--spec", help="Path to specification or PRD document to implement")
    parser.add_argument("-f", "--file", help="Path to file to process")
    parser.add_argument("-r", "--review", help="Path to code file to review against best practices")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    prompt = ""

    if args.spec:
        if not os.path.exists(args.spec):
            print(f"Error: Specification file not found: {args.spec}", file=sys.stderr)
            sys.exit(1)
        with open(args.spec, "r", encoding="utf-8") as f:
            content = f.read()
        prompt = (
            f"Please generate complete, production-ready implementation code for the following specification.\n\n"
            f"--- SPECIFICATION DOCUMENT ({args.spec}) ---\n{content}"
        )
    elif args.review:
        if not os.path.exists(args.review):
            print(f"Error: Target file for review not found: {args.review}", file=sys.stderr)
            sys.exit(1)
        with open(args.review, "r", encoding="utf-8") as f:
            content = f.read()
        prompt = (
            f"Please review the following baseline code against logic bugs, edge cases, thread safety, security, and simplicity.\n\n"
            f"--- CODE UNDER REVIEW ({args.review}) ---\n{content}"
        )
    elif args.file:
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        prompt = content
    elif args.prompt:
        prompt = args.prompt
    elif args.prompt_pos:
        prompt = " ".join(args.prompt_pos)
    else:
        if not sys.stdin.isatty():
            prompt = sys.stdin.read()

    if not prompt.strip():
        print("Error: No prompt or input file provided. Use --spec <file>, --review <file>, --prompt <text>, or pass as argument.", file=sys.stderr)
        sys.exit(1)

    try:
        output = call_opus(prompt)
        print(output)
    except Exception as err:
        print(f"Error invoking Model Garden Opus 5: {err}", file=sys.stderr)
        sys.exit(1)

