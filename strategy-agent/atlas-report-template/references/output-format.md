# ATLAS Report Output Format

## Complete Output Specification

Every ATLAS report produces a single, self-contained HTML file with the following components.

### Structure & Components

- **Metadata Block:** Frontmatter with company name, engagement title, date generated, list of skills used, verdict label (PROCEED/PIVOT/PAUSE/INVESTIGATE)

- **8-Section Core Structure:**
  - Section 01: Executive Summary
  - Section 02: Strategic Diagnosis
  - Section 03: The Crux Decision
  - Section 04: Product/Solution Architecture
  - Section 05: Technology & Build
  - Section 06: Financial Model
  - Section 07: Go-to-Market
  - Section 08: Risk Assessment

  (See [Section Structure & Critique Framework](section-structure.md) for complete structure and content requirements)

- **Fixed Progress Bar:** 4px gradient bar at top (navy → wine-red → blue) tracking scroll position. Updates dynamically as user scrolls. Box shadow provides subtle depth.

- **Fixed Navigation Sidebar:** 240px width with company metadata, section navigation with monospace numbering (01, 02, etc.), skill attribution for current section, footer attribution

- **Premium Components:**
  - Hero section with large H1 title, subtitle, metadata badges
  - Section headers (H2) with "SECTION {{N}} OF 8" label and primary/supporting skill attribution
  - Bridge paragraphs (italic, warm background) connecting sections
  - Recommendation boxes (wine-red left border, actionable content)
  - Insight callouts (blue left border, analysis depth)
  - Risk flags (amber left border, mitigation strategies)
  - Metric cards with 3-column grid layout (label, value, context)
  - Data tables with navy header rows, alternating row colors, hover states
  - Make-or-break assumption box with amber 2px border and yellow-tinted background

### Visual & Interaction Design

**Micro-Interactions:**
- Button hover: subtle lift (translateY -1px) + shadow
- Table row hover: light blue background (#F0F4FF)
- Callout box hover: border thickens, shadow appears, slight rightward translation
- Metric card hover: lift (translateY -3px) + enhanced shadow
- Nav link active: wine-red left border, tinted background, white text

**JavaScript Functionality:**
- Progress bar updates on scroll with color gradient progression
- Scrollspy automatically highlights current section in sidebar nav
- Smooth scroll behavior for all internal nav links
- Custom sidebar scrollbar styling

**Final Attribution:** Footer with ATLAS logo (SVG), tagline "Strategic Intelligence Platform", engine version, copyright notice "© 2026 ATLAS · Confidential"

### File Output

- **Format:** Single HTML file, self-contained with inline CSS and JavaScript
- **Naming:** `{{company}}-{{engagement}}-strategy.html`
- **Directory:** Saved to `/web/` directory
- **Encoding:** UTF-8, responsive to all viewport sizes
- **Print-Friendly:** CSS media queries for clean PDF export
