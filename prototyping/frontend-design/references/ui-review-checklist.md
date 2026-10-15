# 8-Point UI & Accessibility Verification Checklist

Run every frontend prototype through these 8 deterministic checks before presenting it to the user.

| # | Dimension | Pass Criteria | Common Defect to Fix |
|---|---|---|---|
| **1** | **Task Flow & Primary Action** | Each view has exactly one primary filled CTA (`#1a73e8`); secondary actions use outlined or ghost buttons. User can complete the primary CUJ in <= 3 clicks. | Multiple competing primary blue buttons in the same card or header. |
| **2** | **Typography & Contrast (WCAG AA)** | Body text >= `14px` (`0.875rem`), line-height `1.5`. Text contrast >= `4.5:1` (`#202124` or `#5f6368` on `#ffffff`/`#f8f9fa`). Numeric columns use `font-variant-numeric: tabular-nums`. | Light gray text (`#9aa0a6`) used for readable labels on white backgrounds. |
| **3** | **Microcopy & Domain Data** | Every button uses a specific `Verb + Object` label (e.g., `Approve & Commit to Guidewire`, not `Submit`). Realistic domain records populate all tables/cards. | Generic labels (`Click Here`, `Item 1`, `Lorem ipsum`). |
| **4** | **Interactive States & Feedback** | Every interactive control defines `:hover`, `:focus-visible` (`2px solid #1a73e8`), and `:disabled` styles. Actions trigger immediate visual confirmation (toast, badge update, or state transition). | Clicking a button produces no state change in the DOM. |
| **5** | **Cognitive Load & Progressive Disclosure** | Summary cards show <= 4 key metrics per card; dense raw JSON/log payloads are placed inside expandable `<details>` or inspection drawers. | Dumping 30 raw fields into a single ungrouped table row. |
| **6** | **DOM Semantics & Responsive Grid** | Uses semantic landmarks (`<header>`, `<main>`, `<aside>`, `<table>` with `<th scope="col">`). CSS Grid/Flexbox adapts cleanly from `768px` tablet to `1440px` desktop without horizontal overflow. | Hardcoded pixel widths (`width: 1200px`) causing horizontal scrollbars. |
| **7** | **8px Grid Alignment & Status Badges** | Padding and gaps use multiples of `4px`/`8px`. Status pills pair color with text + icon (`PASS`, `HITL REVIEW`, `BLOCKED`) so status is never conveyed by color alone. | Misaligned card headers or status dots with no text label. |
| **8** | **Zero Console Errors & Keyboard Access** | All interactive buttons/tabs are reachable via `Tab` and operable via `Enter`/`Space`; zero `Uncaught ReferenceError` or `TypeError` in browser DevTools console. | `div` elements with `onclick` missing `button` semantics or throwing null-reference errors. |
