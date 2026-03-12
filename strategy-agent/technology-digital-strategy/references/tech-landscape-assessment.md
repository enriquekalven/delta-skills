# Technology Landscape Assessment

Complete framework for auditing current-state technology, quantifying technical debt, and assessing architectural maturity.

## Part 1: Current State Architecture Audit

Start with a complete inventory of what's actually running. Not what you think is running. What is.

### The Inventory Checklist

For each production system, document:

**System Identity**
- System name, business purpose, critical to which business process(es)
- Owner team, on-call contact, support model
- Business downtime cost ($ per minute of outage)
- Revenue directly dependent on this system (if any)

**Architecture & Tech Stack**
- Primary language(s) and framework(s)
- Database(s): type (SQL/NoSQL), version, schema maturity
- Key dependencies: external APIs, third-party services, internal service calls
- Deployment model: on-premise, cloud (which provider), hybrid
- Container/orchestration: Docker, Kubernetes, other, or traditional VMs
- Infrastructure: dedicated, shared, serverless, hybrid

**Code & Deployment Quality**
- Code repository location, branching strategy, code review process
- Testing coverage: unit (%), integration (%), end-to-end (%)
- Deployment frequency: per day, per week, per month, per quarter
- Deployment mechanism: manual, semi-automated, fully automated
- Rollback capability: instant, 10 minutes, 1 hour, overnight, none
- Last major version upgrade: language, framework, database (when)

**Operational Observability**
- Monitoring: full stack (application, infrastructure, user), partial, or basic
- Logging: centralized, distributed, or siloed
- Alerting: proactive (detect before users), reactive (users report), or both
- Performance tracking: latency SLAs defined and tracked, or ad hoc
- Incident tracking: post-mortem process in place, or none

**Data & Integration**
- Data sources: internal database, APIs, batch pipelines, real-time streams
- Data consumers: which systems pull from this system
- Integration patterns: REST, gRPC, message queue, database-coupled, or other
- Data freshness requirements: real-time, minutes, hours, daily

### Red Flags to Document

As you build the inventory, flag these patterns:

- **System nobody knows how it works** — Tribal knowledge loss risk, very high
- **No automated tests** — Every change carries unknown risk
- **Manual deployments** — Bottleneck, high human error rate, no rollback safety
- **Monolithic with distributed code** — Team scaling nightmare
- **Third-party vendor lock-in** — High switching cost, limited negotiating power
- **Undocumented APIs** — Brittle integrations, maintenance nightmare
- **Batch processing with large windows** — Limits velocity, creates operational brittleness
- **No disaster recovery plan** — Single-point-of-failure risk
- **Deprecated language or framework** — Hiring and maintenance nightmare
- **High-touch operations** — System requires heroic efforts to keep running
- **Unclear ownership** — When something breaks, who owns it?

---

## Part 2: Technical Debt Quantification

Technical debt is real. Quantify it.

### Four Types of Technical Debt

**Code Debt**
- Poorly written code, long methods, high cyclomatic complexity
- No unit tests or tests that don't cover critical paths
- Copy-paste code instead of reusable components
- Deprecated or old language versions, outdated libraries

Impact: Increased bug rate, slower feature development, harder hiring, higher turnover.

How to quantify:
- Run static analysis (SonarQube, Code Climate, etc.) — flag issues by severity
- Measure: What % of engineering time is spent maintaining vs. building? (Target: 80% building, 20% maintaining)
- Benchmark: How long to add a "simple feature"? If it's 2-3 weeks, code debt is high.
- Track: Defect escape rate (bugs found in production that tests should have caught)

**Architecture Debt**
- Monolithic architecture limiting feature velocity or team scaling
- Tightly coupled services, hard to change one without breaking others
- Poor separation of concerns (business logic mixed with infrastructure)
- Missing abstraction layers, direct dependency on third-party libraries in business logic

Impact: Slower time to market, team scaling bottlenecks, difficulty pivoting product.

How to quantify:
- Measure: Time to release a feature end-to-end (target: 1-2 weeks for most features)
- Track: Lead time for changes (industry leading: <1 day from commit to production)
- Count: How many services must change for a cross-cutting feature? (Target: ≤2)
- Benchmark: Can a new feature be built and deployed by a single team? Or does it require coordination across 5+ teams?

**Infrastructure Debt**
- Manual infrastructure provisioning, no IaC (Infrastructure as Code)
- On-premise data center with legacy hardware, unclear capacity planning
- No auto-scaling, requiring manual intervention during traffic spikes
- Missing CDN, load balancing, or caching layers
- No multi-region redundancy, single point of failure

Impact: Operational brittleness, inability to scale elastically, high ops cost, slow disaster recovery.

How to quantify:
- Measure: MTTR (mean time to recovery from outage) — target is <15 minutes for non-catastrophic failures
- Track: Infrastructure utilization — if running at 30% capacity, you're overpaying
- Cost: AWS/cloud bill trends — is it growing faster than revenue? (Red flag if >2x)
- Count: Manual steps required to provision a new service (target: 0, all automated)

**Data Debt**
- No data governance, unclear data ownership, no master data management
- Siloed data, multiple versions of truth (sales data in Salesforce, analytics data in warehouse, operational data in ERP)
- No data catalog, hard to find what data exists and where it is
- Data quality issues: missing values, duplicates, inconsistent definitions across systems
- No data architecture, just accumulated databases and data lakes

Impact: Unreliable insights, duplicate effort, poor ML/AI capability, regulatory risk.

How to quantify:
- Survey: How many data sources do analysts have to reconcile? (Target: 1 canonical source)
- Track: Data quality metrics — % of records with missing critical fields (target: <0.1%)
- Measure: Time to answer basic business questions (target: minutes, not weeks)
- Audit: How many systems store "customer" data? (Target: 1 authoritative source)

### Debt Cost Model

For each category, estimate the cost to carry it forward:

```
DEBT IMPACT ASSESSMENT
═══════════════════════════════════════════════
Debt Type: [Code / Architecture / Infrastructure / Data]
Current Impact: [% of engineering time, $ of operational cost, business risk]
Example: Code debt requiring 25% of sprint for refactoring/bug fixes
Cost per Year: [Person-months of engineering, $ in operational costs, $M in lost revenue]

Payoff Cost: [$X to fix, M months of effort, Team: [Who owns it]]
Payoff Timeline: [6 months, 12 months, ongoing]
Payoff Benefit: [Engineering productivity increases to 95%, deployment safety increases to 99.9%, etc.]

ROI Check: [Payoff cost vs. cost of carrying for next 2 years]
Recommendation: [Fix now / Plan in Q4 / Accept and monitor]
═══════════════════════════════════════════════
```

Key insight: The cost of carrying debt often exceeds the cost of fixing it. But you can't fix everything. Prioritize the debt that's blocking business objectives.

---

## Part 3: Technology Maturity Model

Score current state against a 5-level maturity model across key dimensions.

### Five-Level Maturity Framework

**Level 1: Ad Hoc**
- Processes are unpredictable, poorly controlled, reactive
- Success depends on heroic individual effort
- No documentation, tribal knowledge only
- Example: Deployments require the original developer; if they leave, no one can deploy

**Level 2: Repeatable**
- Some processes are documented and repeatable
- Discipline required to follow processes
- Results are somewhat predictable but still variable
- Example: Deployment process documented, but still requires multiple manual steps and inherent risk

**Level 3: Standardized**
- Processes are documented, standardized, and communicated
- Can be performed with minimal deviation
- Quality is more consistent
- Example: Deployment fully automated, consistent across teams, with rollback capability

**Level 4: Optimized**
- Processes are measured, monitored, and continuously improved
- Focus on incremental improvement, preventing problems
- Metrics inform decisions
- Example: Deployment is optimized for speed and safety; analytics drive continuous improvements

**Level 5: Predictive / Autonomous**
- Processes are predictive, proactive, and self-improving
- Automation and AI assist human decision-making
- Anticipate and prevent issues before they occur
- Example: Deployments are autonomous with human oversight; systems self-heal minor issues

### Maturity Scorecard Template

Score each dimension on 1-5 scale:

| Dimension | Current State | Target State | Gap | Timeline |
|-----------|---------------|--------------|-----|----------|
| **Development Practice** | | | | |
| Code quality & testing | 2 (Manual testing, no standards) | 4 (Automated, measured) | 2 levels | 12 mo |
| Version control & branching | 3 (Git, basic process) | 4 (Trunk-based, strong governance) | 1 level | 6 mo |
| Code review rigor | 2 (Sometimes happens) | 4 (Consistent, blocking gate) | 2 levels | 12 mo |
| **Deployment & Operations** | | | | |
| Deployment automation | 2 (Semi-automated) | 4 (Fully automated) | 2 levels | 12 mo |
| Infrastructure as Code | 1 (Manual provisioning) | 4 (All infra in version control) | 3 levels | 18 mo |
| Monitoring & observability | 2 (Basic logs) | 4 (Comprehensive stack tracing) | 2 levels | 9 mo |
| Incident response | 1 (Ad hoc) | 3 (Documented runbooks) | 2 levels | 6 mo |
| **Architecture** | | | | |
| Service cohesion | 2 (Tightly coupled) | 3 (Well-defined boundaries) | 1 level | 12 mo |
| Scalability | 2 (Manual scaling) | 4 (Auto-scaling) | 2 levels | 12 mo |
| Platform maturity | 1 (No platform) | 4 (Self-service platform) | 3 levels | 24 mo |
| **Data & Analytics** | | | | |
| Data governance | 1 (None) | 3 (Defined ownership) | 2 levels | 12 mo |
| Data quality | 2 (Ad hoc fixes) | 4 (Measured, SLAs) | 2 levels | 18 mo |
| Analytics maturity | 2 (Reactive reporting) | 4 (Predictive analytics) | 2 levels | 18 mo |

---

## Part 4: Application Portfolio Rationalization (TIME Model)

Gartner's TIME model: categorize every application into one of four buckets.

### TIME Framework

**Tolerate** — Legacy systems that are stable, low-risk, low-cost to maintain
- Keep running as-is until business case for retirement emerges
- Accept the constraint: can't easily integrate or innovate with this system
- Typical: older COTS software, legacy systems with small user base, systems near end of vendor support

Action: Minimize investment, document exit criteria, monitor for instability

**Invest** — Strategic systems where the business is investing for growth
- Modernize code quality, architecture, infrastructure
- These are your competitive advantage systems
- Typical: core platform, customer-facing systems, systems with frequent changes

Action: Allocate resources for continuous improvement, upgrade tech stack, refactor toward standards

**Migrate** — Systems that are important but on aging technology
- Value is in the business capability, not the current implementation
- Need to move to a new platform (cloud, modern architecture, etc.)
- Typical: ERP systems that need modernization, on-premise systems moving to cloud

Action: Plan migration in waves (quick wins first, foundational capability next, transformational last)

**Eliminate** — Legacy systems that are stalling the business or no longer needed
- Retiring/consolidating into another system
- Not worth maintaining, even if functional
- Typical: duplicate systems, systems with single aged owner, technical anchors preventing progress

Action: Plan decommissioning, manage data archival, communicate retirement to users

### Portfolio Rationalization Template

```
APPLICATION PORTFOLIO ANALYSIS
═══════════════════════════════════════════════

TOLERATE (Legacy but stable)
System: [Name]  |  Tech: [Stack]  |  Users: [Estimate]  |  Annual Cost: [$]
  → Current support burden: [% of team capacity]
  → Exit criteria: [Business condition that triggers retirement]
  → Risk: [If system fails, impact is...]

INVEST (Strategic, worth improving)
System: [Name]  |  Tech: [Stack]  |  Users: [Estimate]  |  Annual Cost: [$]
  → Investment focus: [Code quality / Architecture refactor / Cloud migration / Feature growth]
  → Timeline: [12-24 months typical]
  → Expected return: [Faster release cycle / Better reliability / New capabilities]

MIGRATE (Aging but needed, move platform)
System: [Name]  |  Current: [On-prem ERP]  |  Target: [Cloud SaaS + extensions]
  → Reason to migrate: [Support ending / High maintenance burden / Missing cloud capabilities]
  → Migration approach: [Big bang / Phased / Run-in-parallel]
  → Estimated cost: [$X over Y months]
  → Risks: [Data cutover / User adoption / Hidden customizations]

ELIMINATE (Legacy liability, can sunset)
System: [Name]  |  Tech: [Stack]  |  Users: [Very few]  |  Annual Cost: [$]
  → Why eliminate: [Duplicate capability / Technical anchor / Business model changed]
  → Decommissioning plan: [Data archival, user migration to replacement, timeline]
  → Timeline: [12-18 months typical]
  → Go-live of replacement: [Date]
═══════════════════════════════════════════════
```

---

## Part 5: Capability Heat Map

Map critical business capabilities against current technical capability maturity.

### Heat Map Matrix Template

List 6-8 capabilities critical to the business. For each:
1. Rate current technical capability maturity (1-5 scale)
2. Rate required maturity for business objectives (1-5 scale)
3. Identify gap

Example capabilities:
- **Real-time customer data access** (for personalization, fraud detection, compliance)
- **Multi-channel order management** (for omnichannel retail)
- **Autonomous data processing** (for ML-driven decisions)
- **API-first integrations** (for partner ecosystem)
- **Geographic distribution** (for global scale)
- **Security & compliance automation** (for regulatory requirements)
- **Customer journey orchestration** (for marketing effectiveness)

```
CAPABILITY MATURITY HEAT MAP
═══════════════════════════════════════════════

Capability: [Name]              Current: 2   |   Required: 4   |   Gap: 2 levels (12-18 months)
Capability: [Name]              Current: 3   |   Required: 3   |   Gap: None (at target)
Capability: [Name]              Current: 1   |   Required: 4   |   Gap: 3 levels (18-24 months)
...

COLOR CODING
🟢 Green [Gap ≤ 1 level, on track]
🟡 Yellow [Gap 1-2 levels, requires focused effort]
🔴 Red [Gap ≥ 3 levels, strategic blocker]

CRITICAL PATH
Capabilities that are blockers for others:
  → Data capability → AI capability → Personalization capability
  → API maturity → Partner ecosystem → Revenue growth

Priority order for investment:
  1. [Capability with highest business impact]
  2. [Capability that enables others]
  3. [Capability that addresses risk/compliance]
═══════════════════════════════════════════════
```

---

## Part 6: Anti-Patterns & Worked Examples

Common patterns that indicate trouble:

**Anti-Pattern: "We're transforming to microservices"**
- Red flag: No clear business driver. Just following the trend.
- Red flag: No plan for how to organize teams. "Microservices by architecture, monolithic by organization."
- Red flag: No platform engineering investment. Teams managing Kubernetes, security, logging individually.
- Reality check: Microservices are only better if you have 50+ engineers, multiple teams, and clear business need for independent deployment.

**Anti-Pattern: "We built a data lake"**
- Red flag: Dumped data in without governance, ownership, or catalog.
- Red flag: Now it's a "data swamp" — no one knows what's in there or whether it's accurate.
- Reality check: Data lakes are expensive and complex. Most organizations aren't ready. Start with a data warehouse and good governance instead.

**Anti-Pattern: "Our tech stack is [trendy thing]"**
- Red flag: Chosen for resume appeal, not business fit.
- Red flag: No one knows how to operate it; support is tribal knowledge.
- Reality check: Boring, well-understood technology that your team can operate is better than cutting-edge technology that requires heroic effort.

**Anti-Pattern: "Refactoring will fix this"**
- Red flag: Confusing symptoms (slow deployment, high bug rate) with root cause (architecture debt).
- Red flag: No measurement of whether refactoring is actually helping.
- Reality check: Refactor the architecture and processes, not just the code.

### Worked Example: E-commerce Platform

**Current State:**
- Monolithic Rails app, 6 years old, 50 engineers
- PostgreSQL database, single point of failure
- Manual deployments, 2 per week, 15-minute rollback window (requires devops person)
- No automated tests, 40% test coverage
- Tech debt: 30% of engineering time spent on bug fixes and debt

**Assessment:**
- Code debt: MEDIUM-HIGH (no standards, high churn)
- Architecture debt: HIGH (monolith limits team scaling, can't deploy independently)
- Infrastructure debt: MEDIUM (on-premise, manual deployment)
- Data debt: LOW (PostgreSQL is well-governed, but single DB limits scale)

**Recommendation:**

1. **Immediate (Next 3 months):**
   - Invest in testing infrastructure (add test coverage from 40% → 70%)
   - Automate deployments (reduce from manual to 1-click, 5-minute recovery)
   - Start monitoring (implement application-level metrics, logging)
   - Payoff: Reduce deployment risk, increase velocity, establish visibility

2. **Medium-term (6-12 months):**
   - Establish platform engineering team (3-5 engineers)
   - Migrate to cloud (AWS) with containerization
   - Extract first high-change microservice (payment processing)
   - Payoff: Reduce infrastructure costs, enable independent deployment, unblock teams

3. **Long-term (12-24 months):**
   - Continue extracting microservices (1 per quarter)
   - Implement data warehouse separate from transactional database
   - Automate infrastructure provisioning (Terraform)
   - Payoff: Achieve target maturity (Level 3-4), enable scaling to 100+ engineers

**Timeline & Cost:**
- Phase 1: 3 engineers, 3 months, $150K
- Phase 2: 5 engineers, 9 months, $450K + infrastructure ($200K/year)
- Phase 3: 8 engineers, 12 months, $500K + infrastructure

**ROI:**
- Reduce deployment from 2x per week to 10x per day (5x faster time to value)
- Reduce infrastructure cost by 30% (move from on-prem to cloud with better utilization)
- Free up 15 engineers from "keeping the lights on" to feature development
- **Payoff period: 18 months**

---

## Output Checklist

Every technology landscape assessment should produce:

- [ ] Complete system inventory (all production systems documented)
- [ ] Tech debt quantified by type with cost-to-carry vs. cost-to-fix analysis
- [ ] Maturity scorecard with current state, target state, gaps, and timelines
- [ ] Application portfolio rationalization (TIME buckets assigned)
- [ ] Capability heat map (6-8 business capabilities mapped to technical maturity)
- [ ] Top 3 findings with clear "so what" implications
- [ ] Recommended investment priorities for next 12 months
- [ ] Confidence assessment (data quality, completeness, assumptions)
