# Platform vs. Product Decisions

A platform is fundamentally different from a product. A product solves a customer's problem. A platform enables third parties to solve problems. Platform decisions carry different economics, require different organizational capabilities, and have different risk profiles. This reference operationalizes platform vs. product decisions.

---

## Platform vs. Product Decision Framework with Scoring

The decision to build a platform should not be made lightly. Platforms require different investments, capabilities, and have different go-to-market. This framework helps you decide.

### When to Build a Platform

Build a platform when **all three** of the following are true:

1. **Large supply/demand mismatch**: Significant number of use cases exist that you cannot build. Third parties could serve these if you enabled them.
   - Example: Salesforce cannot build every industry vertical integration. Platforms exist because AppExchange enables thousands of third parties.
   - Example: Slack cannot build every integration. But thousands of teams need different integrations. Slack App Marketplace solves this.

2. **Ecosystem better than verticalized**: It's more efficient for third parties to build than for you to build everything yourself.
   - Example: Apple could build every app in the App Store. But third parties build faster, with more iteration, and for niches Apple wouldn't fund.
   - Decision rule: "If we had to build all these features ourselves, we would need 10x more people. Third parties can do it for us."

3. **Defensible differentiation**: Control of the platform — you're not commoditized. You have something third parties need and can't get elsewhere.
   - Example: Salesforce has CRM data. No ecosystem has that. They're defensible.
   - Example: Stripe has payment processing. No third party can build that. They're defensible.
   - Bad example: Generic API without defensible data or switching costs. Easily replaced.

### When NOT to Build a Platform

**Do NOT build a platform if:**

- You haven't won the core product market yet. Platform requires mature product, operational excellence, and clear demand. Platformizing early distracts you from PMF.
- The supply/demand mismatch is small or you can serve it with integrations. Integrations are cheaper than platforms.
- You have no defensible differentiation. If third parties could build a better platform, you're wasting effort.

### Platform Viability Scoring

Score 0-2 on each dimension (0 = not viable, 1 = possible, 2 = strong signal):

```
PLATFORM VIABILITY ASSESSMENT
═══════════════════════════════════════════════════

1. Supply/Demand Mismatch        [0/2]
   │ Can we identify >10 use cases third parties would build?
   │ Is there clear customer demand for integrations?
   └─ Score

2. Third-Party Demand             [0/2]
   │ Would third parties build if enabled?
   │ Can we identify 10+ potential partners who want access?
   └─ Score

3. Your Core Defensibility        [0/2]
   │ Do we have IP/data that's defensible?
   │ Can third parties replicate what we do?
   └─ Score

4. TAM of Ecosystem Opportunity   [0/2]
   │ Could ecosystem revenue be >20% of core product revenue?
   │ Is the opportunity material?
   └─ Score

5. Your Operations Readiness      [0/2]
   │ Do we have operational discipline (API reliability, SLAs)?
   │ Can we support third-party developers?
   └─ Score

6. Competitive Moat Creation      [0/2]
   │ Does ecosystem make us harder to compete against?
   │ Does ecosystem lock in customers?
   └─ Score

═══════════════════════════════════════════════════
TOTAL SCORE: [0-12]

INTERPRETATION:
0-4: Do NOT build a platform. Focus on core product.
5-8: Conditional platform. Strong on some dimensions, weak on others. Fix weaknesses first.
9-12: Platform is strategically justified. Build.
```

---

## Platform Economics

Platform economics are fundamentally different from product economics. Understand these before building.

### Network Effects

**Same-Side Network Effects**: Value increases as more of the same type of user joins.

Example: Slack users get more value when more colleagues join (because more people to communicate with).

**Strength Indicator**: User adoption rate accelerates with existing user base.

**Cross-Side Network Effects**: Value increases as more of different types of users join.

Example: Uber riders get value when more drivers join (shorter wait time). Drivers get value when more riders join (more demand).

**Strength Indicator**: Both sides grow in tandem. One side's growth drives the other's.

### Platform Metrics

**Liquidity**: Percentage of supply/demand pairs that result in transaction.

- Formula: Successful transactions / (supply × demand)
- Example: If you have 100 drivers (supply) and 500 riders (demand) and get 300 rides per day, liquidity = 300 / (100 × 500) = 0.006 or 0.6%
- Threshold: >5% liquidity is healthy. <1% is thin market.

**Match Quality**: How well does matching meet both parties' needs?

- Measured as: Successful completion rate (did transaction complete), repeat rate (do parties transact again), rating (both parties satisfied)
- Example: 90% of Uber rides go to completion, 7/10 average rating
- Threshold: >85% completion, >4/5 stars

**Multi-Homing Costs**: How easy is it for participants to use multiple platforms?

- High multi-homing cost (hard to switch): You're defensible
- Example: Sellers on Amazon have high friction to sell elsewhere (marketing, fulfillment, payment processing all different)
- Low multi-homing cost (easy to switch): You're vulnerable
- Example: App developers on App Store can easily build for Google Play (only difference is some UI adaptation)

**Take Rate**: Percentage of transaction value you capture.

- Formula: Platform revenue / Total transaction value
- Example: Uber takes 25% of ride cost. Stripe takes 2.9% + $0.30. Etsy takes 5%.
- Threshold: 15-30% for demand-side platform, 5-10% for supply-side, 2-3% for payment-type platform

**Provider/Consumer Ratio**: How many providers to serve one consumer? Or one provider serves how many consumers?

- Healthy platform: One-to-many (one provider serves many consumers, or one consumer served by many providers)
- Unhealthy: Balanced (one-to-one mapping, means no real platform, just two-sided transaction)

### Cold Start Problem

The hardest part of platform building: you need supply to attract demand, and demand to attract supply. Which do you subsidize first?

**Supply-Side Cold Start**: Get supply first (sign up partners/creators/providers), then attract demand.

- Advantage: Supply is sticky (they've invested time building). Once supply is there, demand is attracted.
- Disadvantage: High cost to acquire supply (need to convince them to build).
- Example: Stripe started with supply (built it themselves), then made it easy for others to integrate. Now supply is abundant.

**Demand-Side Cold Start**: Get demand first (users), then attract supply.

- Advantage: Supply follows demand (creators see users wanting content). Natural incentive.
- Disadvantage: Early demand is poor experience (not much choice of supply).
- Example: YouTube attracted users, then creators followed (knowing they could make money).

**Subsidize**: Pay early participants (supply or demand) to join and use the platform. Once liquidity is achieved, reduce subsidies.

- Example: DoorDash subsidized both restaurants (onboarding incentives) and users (discounts) to build liquidity.

---

## API Strategy Design

An API is how third parties access your platform. Choosing which APIs to offer, how public to make them, and how to govern them is core platform strategy.

### API Tiers

**Tier 1: Internal APIs**
- Scope: Your own engineers and services use
- Access: Internal only, no external partners
- Documentation: Detailed, internal wiki
- SLA: High (internal teams depend on it)
- Monetization: None (internal cost center)
- Decision: Required if you have microservices or multiple teams accessing core data/services

**Tier 2: Partner APIs**
- Scope: Strategic partners and ecosystem players
- Access: Approved partners only, not public
- Documentation: High-quality, partner developer portal
- SLA: Medium-high (partners depend on it, but fewer of them)
- Monetization: Usually included in deal, sometimes revenue-share on usage
- Decision: Build when you want to enable ecosystem but want control over who participates

**Tier 3: Public APIs**
- Scope: Anyone can access
- Access: Public, API key signup
- Documentation: Excellent, self-serve, with community contributions
- SLA: Medium (you have many users but small individual impact)
- Monetization: Usage-based billing, freemium tier, premium support
- Decision: Build when supply/demand gap is large and you want to maximize ecosystem

### API Strategy Decision Framework

| Decision | Internal Only | Partner APIs | Public APIs |
|----------|---|---|---|
| **When to Choose** | Early stage, no ecosystem demand | Strategic ecosystem control, limited partners | Large ecosystem opportunity, many potential partners |
| **Upfront Cost** | Low (simple auth, internal documentation) | Medium (partner programs, NDA, support) | High (public documentation, versioning, breaking changes) |
| **Ongoing Cost** | Low (support only internal teams) | Medium (partner support, governance) | High (community support, breaking change management) |
| **Control** | Complete | Medium (govern partners) | Low (cannot control what they build) |
| **Defensibility** | High (network effect from integrations) | Medium (partners locked in) | Low (partners can move elsewhere) |
| **Ecosystem Revenue** | None | Low-medium | High |

### API Governance

**What to Control**:
- **Authentication**: You control who accesses the API. API key, OAuth, etc.
- **Rate Limiting**: You control how much traffic each partner sends. Prevents abuse.
- **Data Access**: You control what data partners can access. Sensitive data stays private.
- **SLA**: You control uptime guarantees. Publish SLA, monitor, report.

**What to Open**:
- **Feature Set**: Let partners build what they want on top of your API
- **Webhook Events**: Publish events (order created, payment processed), let partners act on them
- **Custom Fields**: Let customers add custom data (in public APIs)
- **Data Export**: Let customers access their data (increasingly legal requirement)

---

## Platform Governance: Balancing Control and Ecosystem Growth

The tension in platforms: control (makes you defensible) vs. openness (makes ecosystem grow). This framework helps you navigate.

### Three Governance Archetypes

**Walled Garden** (Apple, WeChat)
- High control: Curate partners, reject bad apps, control user experience
- Limited openness: Few partners, high bar to join
- Result: Defensible, high quality user experience, but slower ecosystem growth
- Unit economics: High take rate (30-40%), fewer partners = more revenue per partner
- Risk: Ecosystem feels limited. Users want what Apple didn't build.

**Open Ecosystem** (Android, AWS)
- Low control: Any developer can build, minimum quality bars
- High openness: Thousands of partners, low bar to join
- Result: Rapid ecosystem growth, user choice, but quality variance
- Unit economics: Low take rate (5-10%), many partners = revenue at scale
- Risk: Fragmentation and quality issues damage core platform

**Segmented Governance** (Salesforce, Shopify)
- Medium control: Different rules for different tiers of partners
- Strategic openness: Core strategic partners get special treatment, others follow standard path
- Result: Control where it matters, openness where it scales
- Unit economics: Tiered take rate (20% for premium partners, 10% for standard, 5% for self-serve)
- Risk: Perceived unfairness from partners

### Governance Decision Matrix

```
HIGH CONTROL
     │
   4 │  Walled Garden         Segmented Governance
     │  (Few partners, high   (Strategic control,
     │   quality, high take)  medium ecosystem)
     │
   3 │─────────────────────────────────────────────
     │
     │
   2 │  Open Ecosystem
     │  (Many partners,
     │   variable quality,
LOW  │   low take rate)
     │
CONTROL
     └───────────────────────────────────────────────
       LOW ← ECOSYSTEM GROWTH → HIGH
```

Choose the quadrant that matches your strategy:
- Want to defensible and premium? Walled Garden
- Want rapid growth and can tolerate quality variance? Open Ecosystem
- Want both? Segmented Governance (harder to execute)

### Policies to Define

**Partner Quality Standards**:
- What makes a good partner? (customer ratings, performance, support responsiveness)
- What's the bar to be listed? (5+ customers, >4.0 rating)
- What happens if partner falls below bar? (removal, remediation plan)

**Revenue Sharing**:
- What's the take rate for different partner types?
- Is it tiered by volume? (first million transactions at 10%, next million at 8%)
- Are there discounts for strategic partners?

**Data Access**:
- What customer data can partners see?
- Can partners see usage of their app vs. competitors'?
- GDPR/compliance: how do you enforce?

**Intellectual Property**:
- Can partners build on your API and then go elsewhere?
- Can partners resell as white-label?
- Do you have rights to anonymized data about partner behavior?

---

## Developer Ecosystem Building Playbook

If you've decided to build a platform, operationalize ecosystem development:

### Phase 1: Onboarding (First Developers)

**Goal**: Get first 10 developers building and shipping something.

**Tactics**:
- **Hand-hold first developers**: Don't rely on self-serve. Assign someone to help them.
- **Quick wins**: Help them build something useful in <2 weeks so they see value fast
- **Document as you go**: Every question they ask becomes documentation
- **Create proof points**: Get them to case study (marketing)

**Success metric**: First developer ships in <2 weeks.

### Phase 2: Self-Service (Scaling Beyond Hand-Holding)

**Goal**: Developers can get started without personal help.

**Tactics**:
- **Excellent documentation**: Code samples, API reference, tutorials, architecture guides
- **SDK and libraries**: Reduce time to first API call (should be <10 minutes)
- **Sandbox environment**: Let them test without hitting production
- **Quickstart repository**: Working example they can run immediately
- **Community**: Forum or Slack where developers help each other

**Success metric**: 80% of developers can get to first API call without asking for help.

### Phase 3: Monetization (Scaling Through Incentives)

**Goal**: Developers want to invest in building (because it's profitable).

**Tactics**:
- **Revenue share**: If they sell something built on your platform, they make money
- **Revenue guarantee**: Pay best developers to build what you want
- **Marketplaces**: Make it easy to sell their app (payment processing, discovery, customer support)
- **Co-marketing**: Help them market (feature on your blog, case study, webinar)

**Success metric**: Top 10% of developers are making >$50k/year from your platform.

### Phase 4: Ecosystem Maturity (Self-Sustaining)

**Goal**: Ecosystem is self-sustaining. You don't need to recruit developers — they recruit each other.

**Tactics**:
- **Community events**: Conferences, hackathons, office hours
- **Certification program**: Badging so customers know who's qualified
- **Partner tiers**: VIP tiers with benefits (support, co-marketing, revenue guarantees)
- **Ecosystem strategy**: Help align ecosystem to fill gaps (identify what's missing, recruit partners to build it)

**Success metric**: 50%+ of new developer signups come from community referral, not your recruiting.

---

## Platform Metrics: Health Scoring

Monitor these platform-specific metrics to assess health:

```
PLATFORM HEALTH SCORECARD
═══════════════════════════════════════════════════

Liquidity                           [0-1.0]
├─ Target: >0.05 (5%)
├─ Trend: [↑ ↓ →]
└─ Implication: [Healthy / Thin market / Critical]

Match Quality                       [0-10 or 0-100%]
├─ Target: >4.0 stars or >85% completion
├─ Trend: [↑ ↓ →]
└─ Implication: [High satisfaction / Mixed / Poor]

Supply-Side Growth                  [YoY % growth]
├─ Target: >20% YoY
├─ Trend: [↑ ↓ →]
└─ Implication: [Ecosystem expanding / Slowing / Declining]

Demand-Side Growth                  [YoY % growth]
├─ Target: >20% YoY
├─ Trend: [↑ ↓ →]
└─ Implication: [Core platform growing / Slowing / Declining]

Take Rate                           [% of transaction]
├─ Target: Sustainable for company, competitive for supply
├─ Trend: [↑ ↓ →]
└─ Implication: [Defensible / At market / Too low]

Multi-Homing Cost                   [Qualitative assessment]
├─ Assessment: [High / Medium / Low]
└─ Implication: [Defensible / Neutral / Vulnerable]

Developer Retention                 [% active developers YoY]
├─ Target: >70%
├─ Trend: [↑ ↓ →]
└─ Implication: [Healthy ecosystem / Churn / At risk]

Top-10 Developer Concentration      [% of ecosystem revenue]
├─ Target: <30%
├─ Trend: [↑ ↓ →]
└─ Implication: [Diverse / Dependent on few / Risky]

═══════════════════════════════════════════════════

OVERALL PLATFORM HEALTH: [Healthy / At Risk / Critical]
```

---

## Anti-Patterns: Premature Platformization

### Premature Platform (Before Product Success)

**Signal**: Building a platform before core product has PMF.

**Why it fails**: No demand for ecosystem because core product isn't valuable yet. You're optimizing for scale before finding value.

**Fix**: Win the core product market first. Platform comes after.

### Platform Without Defensibility

**Signal**: Generic API that third parties could replicate. No defensible advantage.

**Example**: Generic ecommerce platform where any third party could replicate the API. Stripe does payments, you do order management, but no unique data or integration.

**Why it fails**: Third parties don't need you. They build everywhere.

**Fix**: Platform only defensible if you have something unique (data, switching costs, regulatory barriers).

### Ecosystem Instead of Building

**Signal**: Using ecosystem to avoid building things you should build yourself.

**Example**: SaaS company says "our strategy is ecosystem" to justify not building mobile app, not improving performance, etc.

**Why it fails**: Ecosystem complements. Doesn't replace core product improvements.

**Fix**: Ecosystem is leverage, not substitution. Build what you're uniquely positioned to build.

