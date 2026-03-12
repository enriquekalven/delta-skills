# ATLAS Report HTML Design Specification (MANDATORY)

**Every ATLAS report MUST use the exact design system below.** This is non-negotiable — subagents, templates, and any code generating HTML reports must follow this specification verbatim. Do NOT deviate, mix layout patterns, or invent alternative CSS.

### Content Architecture (CRITICAL — READ FIRST)

**ATLAS reports are original strategy deliverables, NOT answer keys to case questions.**

The case PDF / client brief is raw INPUT. The report is an independent consulting deliverable structured around **strategic themes**, exactly like a McKinsey or BCG final presentation.

**Section structure pattern (follow this):**
1. **Executive Summary** — Key metrics, strategic context, core recommendation
2. **Strategic Diagnosis** — Root cause analysis of the business problem (frameworks: issue trees, MECE decomposition, value chain analysis)
3. **[Domain-Specific Theme]** — 2-4 sections named for the strategic theme, NOT the case question. Examples:
   - "Pipeline Valuation" not "Question 2: What is BioFuture's pipeline worth?"
   - "Regional Market Assessment" not "Question 3: How does demand vary by region?"
   - "Workforce Transformation" not "Question 1: What factors should you consider?"
   - "Break-Even Analysis" not "Question 4: Is the investment profitable?"
4. **Market Intelligence** — Real-world context, competitive landscape, industry benchmarks
5. **Decision Framework** — Integrated recommendation with go/no-go criteria
6. **Risk Assessment** — Devil's advocate, kill conditions, mitigation strategies

**Rules:**
- Section titles must be strategic labels (e.g., "Regional Market Assessment — Demand & Capability Heterogeneity"), never "Question 1:", "Question 2:", "Q1:", etc.
- The report should read as if the analyst independently identified the strategic issues — not as if they were responding to a prompt
- Navigation sidebar uses these strategic titles
- `data-section` attributes use "Section 01 of NN" format
- Bridge transitions connect strategic themes, not questions
- If the source material is a practice case with numbered questions, those questions inform WHAT to analyze but NEVER how to label or structure the output

### Critical Layout Rule

**Layout = fixed sidebar + `margin-left` on main. NO CSS Grid on the container wrapper.**

```
.sidebar { position: fixed; top: 60px; left: 0; width: 260px; bottom: 0; }
.main-content { margin-left: 260px; margin-top: 60px; max-width: 1140px; }
.content-inner { max-width: 880px; margin: 0 auto; }
```

⚠️ **NEVER** combine CSS Grid (`grid-template-columns`) on a container with `margin-left` on the main content. This creates a double-offset bug that crushes content into a narrow column.

### CSS Variables (copy verbatim)

```css
:root {
  --navy: #0F172A;
  --wine-red: #A84D48;
  --text: #1A1A1A;
  --insight-blue: #2563EB;
  --positive: #059669;
  --risk-amber: #D97706;
  --bg: #FFFFFF;
  --bg-warm: #FAFBFD;
  --bg-light: #F8FAFC;
  --border: #E5E7EB;
  --border-light: #E2E8F0;
  --text-secondary: #64748B;
  --text-tertiary: #475569;
  --sidebar-text: #A8B5C7;
  --sidebar-border: #2C3E50;
}
```

Font: `'Inter', -apple-system, BlinkMacSystemFont, sans-serif` — loaded via Google Fonts (`Inter:wght@300;400;500;600;700;800`).

### HTML Structure (exact nesting order)

```html
<body>
  <!-- 1. Progress bar (fixed top, 4px height) -->
  <div id="progress-bar"></div>

  <!-- 2. Topbar (dark navy, fixed at top:4px, 56px height) -->
  <div class="topbar">
    <div class="topbar-left">
      <div class="topbar-logo">
        <svg viewBox="0 0 32 32" fill="none">
          <polygon points="16,3 29,28 3,28" stroke="#A84D48" stroke-width="2" fill="none"/>
          <circle cx="16" cy="18" r="6" stroke="#fff" stroke-width="1.5" fill="none"/>
        </svg>
        <span class="topbar-wordmark">ATLAS</span>
      </div>
      <span class="status-pill">{{engagement_mode}}</span>
    </div>
    <div class="topbar-right">
      <div class="confidence-bar">
        AI Confidence
        <div class="confidence-fill">
          <div class="confidence-fill-inner" style="width: {{confidence_pct}}%"></div>
        </div>
        {{confidence_pct}}%
      </div>
    </div>
  </div>

  <!-- 3. Sidebar (dark navy, fixed, 260px wide) -->
  <div class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-label">Engagement</div>
      <div class="sidebar-detail"><strong>Client:</strong> {{client_name}}</div>
      <div class="sidebar-detail"><strong>Challenge:</strong> {{challenge}}</div>
      <div class="sidebar-detail"><strong>Type:</strong> {{engagement_type}}</div>
      <div class="sidebar-detail"><strong>Mode:</strong> {{speed_mode}}</div>
      <div class="sidebar-detail"><strong>Date:</strong> {{date}}</div>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-label">Navigation</div>
    </div>
    <nav class="sidebar-nav" id="nav">
      <!-- One link per section: -->
      <a href="#section-id" class="active">
        <span class="nav-num">01</span> Section Title
      </a>
      <!-- ... repeat for each section -->
    </nav>
    <div class="sidebar-footer">
      <div class="sidebar-footer-text">
        Powered by ATLAS v3.1<br>StrategyOS Engine<br><br>
        &copy; 2026 ATLAS &middot; Confidential
      </div>
    </div>
  </div>

  <!-- 4. Main content (margin-left: 260px, NO grid wrapper) -->
  <div class="main-content">
    <div class="content-inner">

      <!-- 4a. Hero block -->
      <div class="hero">
        <h1>{{report_title}}</h1>
        <p class="hero-subtitle">{{subtitle}}</p>
        <div class="hero-badges">
          <span class="badge active">{{skill_name}}</span>
          <!-- ... one badge per active skill -->
        </div>
        <div class="hero-meta">
          <span>{{date}}</span>
          <span>{{skill_count}} Active Skills</span>
          <span>{{speed_mode}} Engagement</span>
          <span>Case Source: {{source}}</span>
        </div>
        <div class="verdict-bar">
          <div>
            <div class="verdict-label">Strategic Verdict</div>
            <div class="verdict-text">{{verdict_headline}}</div>
            <div class="verdict-detail">{{verdict_detail}}</div>
          </div>
        </div>
      </div>

      <!-- 4b. Sections (use <div class="section">, NOT <section>) -->
      <div class="section" id="{{section-id}}">
        <h2 data-section="Section {{NN}} of {{total}}">{{Section Title}}</h2>
        <!-- content: paragraphs, components, callouts -->
      </div>

      <!-- 4c. Bridges between sections -->
      <div class="bridge">{{transition text}}</div>

      <!-- 4d. Report footer -->
      <div class="report-footer">
        <div class="report-footer-text">
          <!-- ATLAS SVG logo + engagement details + copyright -->
        </div>
      </div>

    </div>
  </div>
</body>
```

### Component Library (use these exact class names)

**Callouts** — three variants:
```html
<div class="callout callout-recommendation">  <!-- wine-red border -->
  <div class="callout-label">{{LABEL}}</div>
  <p style="margin:0">{{content}}</p>
</div>
<div class="callout callout-insight">          <!-- blue border -->
<div class="callout callout-risk">             <!-- amber border -->
```

**Metrics Grid:**
```html
<div class="metrics-grid">
  <div class="metric-card primary">  <!-- primary = wine-red border -->
    <div class="metric-label">{{label}}</div>
    <div class="metric-value">{{value}}</div>
    <div class="metric-context">{{context}}</div>
  </div>
  <!-- ... more metric-cards (omit "primary" for standard styling) -->
</div>
```

**Tables:**
```html
<div class="table-wrapper">
  <table>
    <thead><tr><th>...</th></tr></thead>
    <tbody><tr><td>...</td></tr></tbody>
  </table>
</div>
```

**Assumption Boxes:**
```html
<div class="assumption-box">
  <div class="assumption-box-title">{{TITLE}}</div>
  <p>{{content}}</p>
</div>
```

**Confidence Tags** (inline):
```html
<span class="conf conf-h">HIGH</span>
<span class="conf conf-m">MEDIUM</span>
<span class="conf conf-l">LOW</span>
```

**Market Tags** (inline):
```html
<span class="market-tag above">{{text}}</span>   <!-- green -->
<span class="market-tag below">{{text}}</span>   <!-- amber -->
<span class="market-tag inline-note">{{text}}</span> <!-- blue -->
```

**Risk Matrix:**
```html
<div class="risk-matrix">
  <div class="risk-item high|medium|low">
    <div class="risk-severity">{{HIGH|MEDIUM|LOW}}</div>
    <div class="risk-title">{{title}}</div>
    <div class="risk-desc">{{description}}</div>
  </div>
</div>
```

**Bar Charts:**
```html
<div class="bar-chart">
  <div class="bar-row">
    <div class="bar-label">{{label}}</div>
    <div class="bar-track">
      <div class="bar-fill blue|green|amber|red" style="width: {{pct}}%">{{value}}</div>
    </div>
  </div>
</div>
```

**Deal Grid / Card Grid:**
```html
<div class="deal-grid">
  <div class="deal-card best">  <!-- "best" = green border -->
    <div class="deal-name">{{name}}</div>
    <div class="deal-meta">{{meta}}</div>
    <div class="deal-stat"><strong>{{label}}:</strong> {{value}}</div>
  </div>
</div>
```

**Waterfall Chart:**
```html
<div class="waterfall">
  <div class="wf-col">
    <div class="wf-val">{{value}}</div>
    <div class="wf-bar positive|negative|neutral" style="height: {{px}}px"></div>
    <div class="wf-label">{{label}}</div>
  </div>
</div>
```

**Timeline:**
```html
<div class="timeline">
  <div class="timeline-step">  <!-- add class="future" for unfilled dot -->
    <div class="timeline-dot"></div>
    <div class="timeline-year">{{year/phase}}</div>
    <div class="timeline-desc">{{description}}</div>
    <div class="timeline-amount pos|neg">{{amount}}</div>
  </div>
</div>
```

### JavaScript (copy verbatim)

```javascript
// Progress Bar
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  document.getElementById('progress-bar').style.width = pct + '%';
});

// Scrollspy via IntersectionObserver (NOT manual scroll position)
const sections = document.querySelectorAll('.section');
const navLinks = document.querySelectorAll('#nav a');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`#nav a[href="#${id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-200px 0px -60% 0px', threshold: 0 });
sections.forEach(s => observer.observe(s));

// Smooth scroll on nav click
navLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});
```

### Responsive Breakpoint

```css
@media (max-width: 1024px) {
  .sidebar { display: none; }
  .main-content { margin-left: 0; padding: 0 32px 80px; }
  .hero h1 { font-size: 36px; }
  .metrics-grid { grid-template-columns: repeat(2, 1fr); }
  .risk-matrix { grid-template-columns: 1fr; }
  .timeline { flex-direction: column; }
  .timeline-step::before { display: none; }
}
```

### Subagent Instructions

When delegating HTML report generation to a subagent:
1. **ALWAYS** include this entire design specification in the subagent prompt
2. The subagent must copy the CSS verbatim — no modifications, no "improvements"
3. Layout pattern is non-negotiable: `position: fixed` sidebar + `margin-left: 260px` main
4. The subagent must NOT use CSS Grid on any container/wrapper element
5. After generation, verify the HTML file opens correctly (visual check preferred over code review alone)
