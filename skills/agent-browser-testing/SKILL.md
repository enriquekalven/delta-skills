---
name: agent-browser-testing
description: >
  Performs HTTP web endpoint health checks, verifies HTML structure, and executes Playwright CLI headless browser screenshot testing.
  Triggers on: "agent browser", "browser testing", "playwright test", "visual ui testing", "dev tools testing", "browser automation".
---

# Web Endpoint & Browser Testing (`agent-browser-testing`)

Teaches AI agents how to verify web application endpoints. Combines fast HTTP status checks, doctype/asset tag verification, and Playwright CLI headless screenshot audits.

---

## 1. When to Use

- Verifying web application availability after modifying HTML, CSS, or JS code.
- Checking HTTP status codes (`200 OK` vs `404 / 500`).
- Capturing Playwright full-page screenshots via `--playwright` flag.

---

## 2. Automated Endpoint Verifier CLI

Run the included health tester to verify local or deployed web endpoints:

```bash
python3 skills/agent-browser-testing/scripts/run_browser_test.py --url https://delta-tdl-user-guide.web.app --playwright
```

---

## 3. Chrome DevTools MCP Protocol

When Chrome DevTools MCP is enabled, execute structured UI verification steps:

1. **Navigate & Inspect DOM**:
   - Navigate to `http://localhost:8080`.
   - Inspect active elements, button handlers, and CSS computed styles.
2. **Console Error Interception**:
   - Capture `console.error` and `console.warn` logs.
   - Fail verification if unhandled JS exceptions occur.
3. **Visual Screenshot Capture**:
   - Take full-page screenshots at desktop (`1920x1080`) and mobile (`375x812`) breakpoints.
