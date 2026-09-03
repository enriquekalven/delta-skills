#!/usr/bin/env python3
"""Google Cloud Vertex AI Model Garden - Anthropic Claude Opus 5 Runner.

This script executes Zero Data Retention (ZDR) API calls to Anthropic Claude Opus 5
hosted on Google Cloud Vertex AI Model Garden. It adheres to Google Cloud Professional
Services Organization (PSO) enterprise delivery standards.
"""

from __future__ import annotations

import argparse
import os
import random
import re
import subprocess
import sys
import time
from typing import Optional


def discover_project_id() -> Optional[str]:
    """Auto-discovers GCP project ID from environment or gcloud config."""
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT")
    if project_id:
        return project_id.strip()

    try:
        res = subprocess.run(
            ["gcloud", "config", "get-value", "project"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if res.returncode == 0 and res.stdout.strip() and "(unset)" not in res.stdout:
            return res.stdout.strip()
    except Exception:
        pass
    return None


def call_opus_model_garden(
    prompt: str,
    project_id: str,
    region: str = "us-central1",
    model_name: str = "claude-opus-5",
    max_tokens: int = 4096,
    temperature: float = 0.2,
    max_retries: int = 4,
) -> str:
    """Calls Vertex AI Model Garden Anthropic Opus 5 ZDR endpoint with exponential backoff."""
    try:
        from anthropic import AnthropicVertex
    except ImportError:
        raise ImportError(
            "The 'anthropic[vertex]' package is required for Vertex AI Model Garden calls.\n"
            "Install it via: pip install --upgrade 'anthropic[vertex]'"
        )

    # Initialize client with Application Default Credentials (ADC)
    client = AnthropicVertex(region=region, project_id=project_id)

    system_prompt = (
        "You are an expert Google Cloud Principal Software Engineer operating as a PSO AI Coding Solution. "
        "Your role is to produce complete, robust, secure, and production-ready implementations adhering to "
        "Google Cloud architecture standards. NEVER output placeholders, TODO stubs, or incomplete implementations."
    )

    last_error: Optional[Exception] = None
    for attempt in range(1, max_retries + 1):
        try:
            print(
                f"[Model Garden] Calling {model_name} in {region} (project: {project_id})...",
                file=sys.stderr,
            )
            message = client.messages.create(
                model=model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt,
                messages=[{"role": "user", "content": prompt}],
            )

            # Extract pure text blocks
            text_blocks = [
                block.text for block in message.content if getattr(block, "type", "") == "text"
            ]
            if text_blocks:
                return "\n".join(text_blocks)
            return str(message.content)

        except Exception as exc:
            last_error = exc
            error_msg = str(exc)
            if "DefaultCredentialsError" in error_msg or "could not be found" in error_msg:
                raise PermissionError(
                    "Google Cloud Application Default Credentials (ADC) not found.\n"
                    "Please run: gcloud auth application-default login"
                ) from exc

            if attempt == max_retries:
                raise RuntimeError(
                    f"Vertex AI Model Garden call failed after {max_retries} attempts: {exc}"
                ) from exc

            # Exponential backoff with jitter
            backoff = (2 ** attempt) + random.uniform(0.5, 1.5)
            print(
                f"⚠️ Transient API error (attempt {attempt}/{max_retries}): {exc}. "
                f"Retrying in {backoff:.1f}s...",
                file=sys.stderr,
            )
            time.sleep(backoff)

    if last_error:
        raise last_error
    return ""


def extract_and_write_files(content: str, output_dir: str) -> list[str]:
    """Parses markdown file blocks (FILE: path\\n```lang\\ncode```) and writes to disk."""
    pattern = re.compile(
        r"(?:FILE:\s*([^\n\r`]+)\s*)?```(?:[a-zA-Z0-9_\-\.]+)?\s*\n(.*?)```",
        re.DOTALL,
    )
    written_files = []
    matches = list(pattern.finditer(content))

    for idx, match in enumerate(matches):
        filepath = match.group(1)
        code = match.group(2)
        if not filepath:
            filepath = f"generated_artifact_{idx + 1}.txt"
        else:
            filepath = filepath.strip()

        target_path = os.path.join(output_dir, filepath)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(code)
        written_files.append(target_path)
        print(f"  [Wrote] {target_path}", file=sys.stderr)

    return written_files


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Invoke Anthropic Claude Opus 5 on Google Cloud Vertex AI Model Garden (ZDR)"
    )
    parser.add_argument("prompt_pos", nargs="*", help="Optional positional prompt string")
    parser.add_argument("-p", "--prompt", help="Direct text prompt for generation")
    parser.add_argument("-s", "--spec", help="Path to specification or PRD document to implement")
    parser.add_argument("-f", "--file", help="Path to source or context file")
    parser.add_argument("-r", "--review", help="Path to source file to review & harden")
    parser.add_argument("-o", "--output-dir", help="Directory to extract generated files into")
    parser.add_argument("--project", help="GCP Project ID (default: auto-detected)")
    parser.add_argument(
        "--region",
        default=os.environ.get("CLOUD_ML_REGION", "us-central1"),
        help="Vertex AI region (default: us-central1 or CLOUD_ML_REGION)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("CLAUDE_MODEL_NAME", "claude-opus-5"),
        help="Model Garden model name (default: claude-opus-5)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help="Maximum generation tokens (default: 4096)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Generation temperature (default: 0.2 for precise coding)",
    )
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    project_id = args.project or discover_project_id()
    if not project_id:
        print(
            "Error: Google Cloud Project ID could not be identified.\n"
            "Set GOOGLE_CLOUD_PROJECT env var or pass --project <project_id>.",
            file=sys.stderr,
        )
        sys.exit(1)

    prompt = ""
    if args.spec:
        if not os.path.isfile(args.spec):
            print(f"Error: Spec file not found: {args.spec}", file=sys.stderr)
            sys.exit(1)
        with open(args.spec, "r", encoding="utf-8") as f:
            spec_text = f.read()
        prompt = (
            f"Please implement complete, production-grade source code for the following specification.\n\n"
            f"--- SPECIFICATION: {args.spec} ---\n{spec_text}"
        )
    elif args.review:
        if not os.path.isfile(args.review):
            print(f"Error: Review file not found: {args.review}", file=sys.stderr)
            sys.exit(1)
        with open(args.review, "r", encoding="utf-8") as f:
            code_text = f.read()
        prompt = (
            f"Please perform a Google Cloud enterprise security, reliability, and code quality review on this file.\n\n"
            f"--- SOURCE CODE: {args.review} ---\n{code_text}"
        )
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            prompt = f.read()
    elif args.prompt:
        prompt = args.prompt
    elif args.prompt_pos:
        prompt = " ".join(args.prompt_pos)
    else:
        if not sys.stdin.isatty():
            prompt = sys.stdin.read()

    if not prompt.strip():
        print(
            "Error: No prompt provided. Use --spec <file>, --prompt <text>, --review <file>, or pass text via stdin.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        output = call_opus_model_garden(
            prompt=prompt,
            project_id=project_id,
            region=args.region,
            model_name=args.model,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
        )

        if args.output_dir:
            print(f"[Model Garden] Extracting code blocks to: {args.output_dir}...", file=sys.stderr)
            files = extract_and_write_files(output, args.output_dir)
            print(f"[Model Garden] Successfully created {len(files)} file(s).", file=sys.stderr)
        else:
            print(output)

    except Exception as err:
        print(f"\n[Model Garden Error] {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
