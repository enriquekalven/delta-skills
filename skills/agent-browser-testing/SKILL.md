---
name: agent-browser-testing
description: >
  Automates real browser UI testing, visual screenshot capture, form interaction, and network console error interception using Playwright, Chrome DevTools MCP, and CLI HTTP verifiers.
  Triggers on: "agent browser", "browser testing", "playwright test", "visual ui testing", "dev tools testing", "browser automation".
---

# Real Browser & Visual UI Testing (`agent-browser-testing`)

Teaches AI agents how to test web applications in real browsers. Combines **Playwright CLI**, **Chrome DevTools MCP**, and automated HTTP health verifiers to capture DOM state, verify visual rendering, intercept console errors, and validate frontend user journeys.

---

## 1. When to Use

- Verifying web UI functionality after modifying HTML, CSS, or JS code.
- Checking for frontend console errors, broken static assets, or failing API calls (`500 / 404`).
- Testing responsive designs across Desktop (1920x1080) and Mobile (375x812) viewports.

---

## 2. Automated Endpoint Verifier CLI

Run the included health tester to verify local or deployed web endpoints:

```bash
python3 skills/agent-browser-testing/scripts/run_browser_test.py --url https://delta-tdl-user-guide.web.app
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
