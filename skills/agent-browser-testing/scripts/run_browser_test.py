#!/usr/bin/env python3
"""
HTTP Endpoint & HTML Structure Verifier for Agent Workflows.

Performs fast HTTP status checks, verifies HTML doctype, counts scripts/stylesheets,
and provides Playwright CLI command invocation for full headless rendering.

Usage:
  python3 scripts/run_browser_test.py --url https://delta-tdl-user-guide.web.app
"""

import sys
import argparse
import urllib.request
import urllib.error
import re
import subprocess
import shutil
from typing import Dict, Any


def test_url_health(url: str) -> Dict[str, Any]:
    print(f"🌐 Testing Web Endpoint: {url} ...")
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Delta-Agent-Browser-Tester/1.3.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status_code = response.getcode()
            html_content = response.read().decode('utf-8', errors='ignore')

        # Basic HTML checks
        has_doctype = "<!DOCTYPE html" in html_content or "<!doctype html" in html_content
        has_title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
        title = has_title_match.group(1).strip() if has_title_match else "No title tag found"

        # Check for asset links and script tags
        script_count = len(re.findall(r'<script', html_content, re.IGNORECASE))
        link_count = len(re.findall(r'<link', html_content, re.IGNORECASE))

        return {
            "status_code": status_code,
            "success": status_code == 200,
            "title": title,
            "has_doctype": has_doctype,
            "script_tags": script_count,
            "css_link_tags": link_count,
            "html_length_bytes": len(html_content)
        }
    except urllib.error.HTTPError as e:
        return {"status_code": e.code, "success": False, "error": f"HTTP Error {e.code}"}
    except urllib.error.URLError as e:
        return {"status_code": 0, "success": False, "error": f"URL Connection Error: {e.reason}"}
    except Exception as e:
        return {"status_code": 0, "success": False, "error": str(e)}


def run_playwright_cli(url: str) -> bool:
    """Invokes Playwright CLI if installed for real browser rendering & screenshot."""
    npx_path = shutil.which("npx")
    if not npx_path:
        print("💡 Note: Playwright CLI (npx) not found locally. Using HTTP endpoint verifier.")
        return False

    print(f"🎭 Running Headless Playwright Screenshot & Console Audit on {url}...")
    try:
        cmd = ["npx", "playwright", "screenshot", url, "screenshot.png", "--full-page"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if res.returncode == 0:
            print("📸 Captured full-page Playwright screenshot: screenshot.png")
            return True
        else:
            print(f"⚠️ Playwright CLI exited with code {res.returncode}. Fallback to HTTP verifier.")
            return False
    except Exception as e:
        print(f"⚠️ Playwright CLI execution skipped: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Agent Browser & HTTP Structure Tester")
    parser.add_argument("--url", type=str, required=True, help="Target Web URL to test")
    parser.add_argument("--playwright", action="store_true", help="Run full headless Playwright screenshot audit")
    args = parser.parse_args()

    result = test_url_health(args.url)

    print("=" * 60)
    print(f"📊 Endpoint Health Report: {args.url}")
    print("=" * 60)

    if result["success"]:
        print(f"✅ HTTP Status       : {result['status_code']} OK")
        print(f"📄 Page Title        : {result['title']}")
        print(f"📐 HTML Length       : {result['html_length_bytes']} bytes")
        print(f"📜 Script Tags       : {result['script_tags']}")
        print(f"🎨 CSS Link Tags     : {result['css_link_tags']}")
        print("=" * 60)
        print("✨ HTTP VERIFICATION PASSED.")

        if args.playwright:
            run_playwright_cli(args.url)
    else:
        print(f"❌ Verification Failed: {result.get('error')}")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
