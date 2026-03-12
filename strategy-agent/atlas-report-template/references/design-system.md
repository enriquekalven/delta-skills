# ATLAS Design System v4

## Brand Identity

- **Name:** ATLAS
- **Tagline:** Strategic Intelligence Platform
- **Position:** Bloomberg Terminal meets McKinsey, but AI-native
- **Logo:** Inline SVG triangle with compass circle (inline in topbar only)

## Color Palette

```
PRIMARY
  --navy:         #0F172A    (headers, sidebar bg, topbar wordmark, table headers)
  --wine-red:     #A84D48    (accent, dividers, recommendations, active nav, labels)
  --text:         #1A1A1A    (body text — near-black, NOT #333)

SEMANTIC ACCENTS
  --insight-blue: #2563EB    (insight callouts, links)
  --positive:     #059669    (status pills, positive signals)
  --risk-amber:   #D97706    (risk/caution callouts)

NEUTRALS
  --bg:           #FFFFFF    (page background)
  --bg-warm:      #FAFBFD    (callout backgrounds, bridge paragraphs)
  --bg-light:     #F8FAFC    (skill badges, metric cards)
  --border:       #E5E7EB    (borders, dividers)
  --border-light: #E2E8F0    (badge borders)
  --text-secondary: #64748B  (labels, metadata, sidebar labels)
  --text-tertiary:  #475569  (bridge text, footer)
  --sidebar-text:   #A8B5C7  (sidebar nav links)
  --sidebar-border: #2C3E50  (sidebar dividers)
```

## Typography (All Inter, no serifs)

```
HERO H1:      Inter 56px / 700 / 1.2 line-height / -0.5px letter-spacing / #0F172A
HERO SUBTITLE: Inter 20px / 400 / 1.5 / #64748B
SECTION H2:   Inter 32px / 700 / 1.25 / -0.3px letter-spacing / #0F172A / margin-top 64px
H3:           Inter 20px / 600 / 1.3 / #0F172A / margin-top 32px
H4:           Inter 16px / 600 / #0F172A
BODY:         Inter 16px / 1.75 / 0.2px letter-spacing / #1A1A1A
LABELS:       Inter 11px / 600 / 1.5px letter-spacing / uppercase
SMALL:        Inter 12-13px / 500
```

## Spacing System

```
HERO:           padding 80px 0 64px 0, margin-bottom 64px
SECTIONS:       margin-bottom 80px
H2:             margin-top 64px, margin-bottom 28px
H3:             margin-top 32px, margin-bottom 16px
PARAGRAPHS:     margin-bottom 20px
BRIDGE:         margin 40px 0 48px 0
CALLOUT BOXES:  padding 28px, margin 36px 0
RECOMMENDATION: padding 32px, margin 40px 0
TABLES:         margin 40px 0
METRIC CARDS:   padding 20px, gap 16px
CONTENT MAX:    880px (centered)
SIDEBAR WIDTH:  240px
TOPBAR HEIGHT:  56px (fixed, top 4px for progress bar)
PROGRESS BAR:   4px height, fixed top 0
```

## Component Library

#### Progress Bar (fixed top, 4px height)
`position: fixed; top: 0; height: 4px; background: linear-gradient(to right, #0F172A, #A84D48, #2563EB); z-index: 9999; box-shadow: 0 1px 3px rgba(0,0,0,0.1);`

#### Top Navigation Bar
56px fixed height with ATLAS logo (triangle + compass), "Live Analysis" status pill, AI Confidence % bar, Export button, Share button.

#### Sidebar (NO logo — logo only in topbar)
240px width with engagement details, section navigation with monospace numbering (01, 02, etc.), footer with "Powered by ATLAS v3.1 StrategyOS Engine"

#### Hero Section
Large H1 title, subtitle, divider, active skill badges, metadata (date, skills, depth), verdict bar with verdict label and detail.

#### Section Headers (H2 with section number)
`H2 data-section="SECTION {{N}} OF {{TOTAL}}"` with skill attribution (Primary / Supporting).

#### Bridge Paragraphs
Italic transition text connecting sections, "Why this matters:" energy, margin 40px 0 48px 0.

#### Callout Boxes (3 semantic types)
- RECOMMENDATION (wine-red accent, left border)
- INSIGHT (blue accent, left border)
- RISK FLAG (amber accent, left border)

#### Metric Cards
Grid layout with label, metric-value (large), metric-context (small). First card marked "primary" with different styling.

#### Tables
Navy header (#0F172A white text), alternating rows (#FAFBFD / #FFFFFF), row hover #F0F4FF.

#### Make-or-Break Assumption Box
2px solid #D97706 border, background #FFFBF5, padding 28px, border-radius 8px.

#### Footer
Small logo, tagline, "Powered by ATLAS v3.1 StrategyOS Engine", "© 2026 ATLAS · Confidential"

## Micro-Interactions (REQUIRED CSS)

- Button hover: `transform: translateY(-1px); box-shadow: 0 4px 12px rgba(15,23,42,0.12);`
- Table row hover: `background-color: #F0F4FF;`
- Callout box hover: `border-left-width: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); transform: translateX(2px);`
- Metric card hover: `transform: translateY(-3px); box-shadow: 0 8px 16px rgba(0,0,0,0.06);`
- Nav link active: `border-left-color: #A84D48; background: rgba(168,77,72,0.15); color: #FFFFFF; font-weight: 600;`
- Custom sidebar scrollbar: 6px width, #2C3E50 thumb with 3px radius

## JavaScript (REQUIRED)

**Progress Bar:** Scroll progress gradient from navy → wine-red → blue, fixed top 0, updates on scroll.

**Scrollspy:** Auto-highlight nav links based on current section, smooth updates on scroll with 200px offset.
