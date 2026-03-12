# Growth Engine Design

A growth engine is the repeatable system that drives customer acquisition, activation, and expansion. This reference operationalizes growth engine design: growth flywheels, network effects, viral loops, unit economics modeling, and scaling diagnostics.

---

## Growth Flywheel vs. Growth Funnel

**Growth Funnel (Linear):**
Awareness → Consideration → Decision → Purchase → Retention

- Each stage is separate
- Requires constant top-of-funnel effort to maintain velocity
- No compounding
- Works for: Sales-driven, paid channel models

**Growth Flywheel (Circular):**
Customer value creation → Viral/referral effect → New customer acquisition → Repeat

- Each stage feeds the next
- Compounding: each customer acquired brings more customers
- Self-accelerating (flywheel spins faster over time)
- Works for: Network effects, viral loops, marketplace models

### Designing Your Flywheel

```
GROWTH FLYWHEEL TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stage 1 - ACQUISITION
  How do customers arrive?
  - Primary channel: [e.g., paid search, marketplace, partnerships]
  - Secondary channels: [e.g., organic, referral, direct]
  - Typical CAC: [$]
  - Time to acquisition: [Days]

Stage 2 - ACTIVATION
  What must happen for them to be "activated" (ready for core experience)?
  - Key activation action: [e.g., complete profile, first transaction, first team invitation]
  - Activation rate: [%]
  - Activation timeline: [Days to completion]
  - Activation cost: [$]

Stage 3 - VALUE CREATION
  What value do they experience?
  - Core value moment: [e.g., 1st successful transaction, 1st collaboration]
  - Time to value: [Days to core value moment]
  - Aha moment frequency: [# per week/month]
  - % of users reaching aha moment: [%]

Stage 4 - RETENTION
  What causes them to return?
  - Primary retention driver: [e.g., ongoing need, habit, switching costs, community]
  - Retention curve: [% retained after 30/90/365 days]
  - Churn reason (if applicable): [Top 3 reasons customers leave]
  - Re-activation possible? [Yes/No] If yes, how?

Stage 5 - EXPANSION
  How do they expand usage / spend?
  - Expansion mechanism: [e.g., per-seat, per-transaction, premium tier, add-on products]
  - % of customers who expand: [%]
  - Expansion timeline: [Months to first expansion]
  - Avg $ expansion per customer per year: [$]

Stage 6 - VIRAL/REFERRAL EFFECT
  Do they bring others?
  - Viral mechanism: [e.g., "invite a teammate" to use product, "send a link to friend"]
  - Viral coefficient: [# of new users acquired per user who goes through cycle]
  - Viral loop tightness: [Days from activation to inviting others]
  - % of new customers from viral: [% of all new customers]

FLYWHEEL METRICS:
  - Cycle time: [Days from acquisition to when they invite others]
  - Tightness score: [1-10; 10 is tightest possible]
  - Viral coefficient: [<1 = declining; 1 = stable; >1 = compounding]
  - Monthly new customers: [#] of which [%] from viral/referral
  - Year-over-year growth rate: [%] driven by flywheel

WHAT'S MISSING (stage that weakens flywheel):
  [If viral coefficient <1, which stage is the bottleneck?]
  - Activation too slow?
  - Value creation unclear?
  - Retention too low?
  - Expansion rate too low?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Worked Example: Amazon Marketplace Flywheel

```
STAGE 1 - ACQUISITION (Sellers)
  New sellers attracted to Amazon's customer base (100M+ buyers)
  CAC: ~$0 (self-evident pull; sellers find Amazon, not reverse)
  Time to acquisition: Hours to signup

STAGE 2 - ACTIVATION (Sellers)
  Seller uploads first 10 products, sets pricing, activates store
  Activation rate: 80%
  Timeline: 2-3 days
  Cost: $0

STAGE 3 - VALUE CREATION
  First sale occurs; seller sees: buyers find them, Amazon handles payment/shipping
  Time to value: 1-2 weeks (first sale)
  Aha moment: "Customers are coming to me; I didn't have to find them"

STAGE 4 - RETENTION
  Ongoing customer demand = ongoing reason to use Amazon
  Retention curve: 95% after 1 year (very high)
  Churn reason: Only if sellers find better opportunity (low risk)

STAGE 5 - EXPANSION
  Seller adds more products, expands categories, increases inventory
  % expanding: 70% of sellers who reach >10 sales/month
  Timeline: Month 3-6
  Expansion: +300-500 SKUs per seller on average

STAGE 6 - VIRAL EFFECT (Buyers)
  Positive buyer experience → buyer tells friends → more buyers → more seller incentive
  Viral mechanism: Word-of-mouth, Facebook/social sharing, "deals" messaging
  Viral coefficient: 1.3+ (each buyer brings 1.3 new buyers)
  Timeline: Each buyer experience drives word-of-mouth over months

FLYWHEEL VIRTUOUS CYCLE:
  More buyers → Better selection for buyers → More satisfied buyers → Word-of-mouth growth
  More sellers → Better selection for buyers → Higher buyer satisfaction → More seller demand
  Network effect compounds: value for both buyers and sellers increases with scale

RESULT: Cycle time = 4-6 weeks from acquisition to expansion; viral coefficient >1
Year-over-year growth: 30%+ compounding (both buyers and sellers)
```

---

## Network Effects Taxonomy

Network effects are the rare growth lever that compounds without capital reinvestment. Design your product for them from the start, or retrofit later.

### Direct Network Effects

**Definition:** Value of the product increases as more users join.

**Mechanism:** More users → more valuable product → more incentive to join

**Examples:**
- Phone networks (more phones → more people to call)
- LinkedIn (more professionals → more valuable network)
- WhatsApp (more people on WhatsApp → more messages possible)
- Marketplace (more sellers → more choice for buyers → more buyers → more sellers)

**Design for Direct Network Effects:**
```
DIRECT NETWORK EFFECT DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Critical Mass: How many users needed before value is obvious?
  - E.g., LinkedIn: ~500 connections before network is valuable
  - E.g., Marketplace: 100+ sellers before selection is meaningful
  - E.g., Social network: 20+ friends before activity is engaging
  Target: Get to critical mass in your beachhead first

Acquire competitors' users: Easier to acquire in beachhead
  - Start with narrow niche (e.g., product managers at tech companies)
  - Acquire all competitors' users in that niche (penetrate 50%+)
  - Then expand to adjacent niches
  - Example: LinkedIn started with tech/finance professionals, not all professionals

Switching costs: How easy is it to leave?
  - High switching cost = stronger network effects
  - E.g., LinkedIn: switching cost high (lose all your professional network)
  - E.g., iPhone: switching cost high (lose all your apps, contacts, habits)
  - Design to increase switching cost: data portability, integrations, habit formation

Viral loop tightness: How fast do users get value from network?
  - Tight = days or weeks
  - Loose = months
  - Tight is better: e.g., Slack (value from first message with 1 person) vs. LinkedIn (value needs 100+ connections)
  - Design for tight loops: minimal critical mass to feel value
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Indirect Network Effects (2-Sided)

**Definition:** Value increases when complementary users join (e.g., app store: developers benefit from more users, users benefit from more apps).

**Mechanism:** More users (demand side) → more developers/suppliers (supply side) → more value for users → more user growth

**Examples:**
- iOS app store (more users → more developers attracted → more apps → more users)
- Uber (more riders → more drivers attracted → faster pickups → more riders)
- Shopify (more stores → more apps/integrators → better stores → more stores)

**Design for Indirect Network Effects:**
```
INDIRECT NETWORK EFFECT DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Chicken-egg problem: Suppliers need users; users need suppliers
  - Solution 1: Bootstrap supply yourself (Uber hired drivers, didn't just open marketplace)
  - Solution 2: Find early adopters on both sides (tech-savvy developers, early users)
  - Solution 3: Pay for early supply (subsidize drivers, pay for early developers)

Incentive alignment: Both sides must win
  - Developer incentive: % of revenue, audience size, ease of integration
  - User incentive: functionality, value-add, new features
  - Example: Shopify app developers get 30% of revenue; users get feature extensions

Quality control: Bad supply tanks user experience
  - Example: iOS curation (Apple rejects bad apps) > Google Play (open, more bad apps)
  - Moderate or curate: especially important in early days

Developer experience: Easy to build on your platform
  - APIs, SDKs, documentation, support
  - Example: Stripe (easy API) > Zuora (complex integration)
  - Better DX = more developers = more apps = more user value
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Data Network Effects

**Definition:** Product improves as more data accumulates from user activity.

**Mechanism:** More users → more data → better algorithms → better product → more users

**Examples:**
- Google search (more searches → more data → better ranking → more searches)
- Netflix recommendations (more watched → better recommendations → more watch time)
- Spotify Discover Weekly (more listening → better taste profiles → better playlists)

**Design for Data Network Effects:**
```
DATA NETWORK EFFECT DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data moat: Does scale give you an advantage competitors can't match?
  - Strong moat: Yes (e.g., Google search, Amazon recommendations)
  - Weak moat: No (e.g., basic ML models available to all)
  - Design: Focus on proprietary data + algorithms that competitors can't replicate

Scale required: How much data for noticeable improvement?
  - Small: 1000 data points (e.g., basic recommendation)
  - Large: 1 billion data points (e.g., general search algorithm)
  - Design: Start with smaller data requirements; prove value before scale

Privacy + Data: How do you collect data while respecting privacy?
  - Transparent: Tell users what data you collect and why
  - Value exchange: User gives data; you improve product
  - Example: Apple (privacy-first) vs. Google (data-first)
  - Design: Be clear on data policy from day 1

User control: Can users see/modify their data?
  - High control: User opt-in, can export, can delete (better experience)
  - Low control: Opaque data collection (legal risk, user backlash)
  - Design: User-friendly data control > legal burden
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Marketplace Network Effects

**Definition:** Value increases as both buyers and sellers scale. Typically combines direct + indirect effects.

**Mechanism:** More sellers → more choice → more buyers → more demand → more sellers

**Examples:**
- eBay (more sellers with more inventory → more buyers shopping → more seller opportunity)
- Airbnb (more hosts with more listings → more travelers → more host incentive)
- DoorDash (more restaurants → more delivery options → more customers → more restaurants)

**Design for Marketplace Network Effects:**
```
MARKETPLACE NETWORK EFFECT DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Supply-side growth: How do you attract sellers/suppliers?
  - Pull (natural): Sellers come because buyers are there (late-stage, only if demand exists)
  - Push (operational): Marketplace actively recruits sellers (early-stage, requires capital)
  - Hybrid: Start with push (seed supply), transition to pull
  - Typical ratio early-stage: 80% push / 20% pull. Mature: 20% push / 80% pull

Demand-side growth: How do you attract buyers?
  - Better supply → easier to acquire buyers (word-of-mouth, product differentiation)
  - Pricing incentives (discounts, fee waivers to early buyers)
  - Must reach critical mass of supply first (otherwise poor buyer experience)

Quality control: Bad supply or bad buyers tank the marketplace
  - Seller quality: Vet before listing (Airbnb reviews profiles; Uber vets drivers)
  - Buyer quality: Prevent fraud and bad behavior (eBay escrow, DoorDash rating)
  - Dispute resolution: Handle conflicts quickly (both sides must trust the platform)

Liquidity: Can buyers and sellers transact easily?
  - Low friction: 1-click purchase, clear pricing, fast delivery
  - E.g., DoorDash optimized for: <3 minute to browse, <2 minute to order, 30-40 min delivery
  - Friction kills marketplaces: too slow = users leave

Unit economics: Both supply and demand sides must be profitable
  - Take rate: % of transaction value kept by marketplace
  - Typical: 15-30% (too low = underfunded; too high = expensive for users/sellers)
  - Example: Uber (Uber keeps 25% of fare), DoorDash (30% from restaurants, fees from customers)
  - Design: Transparent take rate, value clearly communicated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Viral Loops & Viral Coefficient

**Viral Coefficient (k):** Number of new users acquired per existing user.

**Types of Viral:**
- **Organic Viral (k = 1.2+):** Users inherently invite others (e.g., WhatsApp, Slack, viral videos)
- **Incentivized Viral (k = 1.1+):** Offer incentive for referral (e.g., Dropbox +500MB for referral)
- **Marketing Viral (k = 0.8-1.2):** Viral messaging + paid seeding (e.g., Super Bowl ads that spread on social)

### Viral Coefficient Modeling

```
VIRAL COEFFICIENT CALCULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Viral Coefficient (k) = (% of users who share) × (# invited per sharer) × (% of invitees who convert)

Example:
- 40% of users share their Slack workspace with teammates
- Each sharer invites 3 teammates on average
- 30% of invitees join
- k = 0.4 × 3 × 0.3 = 0.36 (subviral; declining without external fuel)

Example (Optimized):
- 70% of users share (product change: easier sharing)
- Each sharer invites 3 teammates (unchanged)
- 50% of invitees join (improved messaging: "your team is already using Slack")
- k = 0.7 × 3 × 0.5 = 1.05 (viral; sustainable growth)

VIRAL LOOP TIGHTNESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Viral Loop Time: Days from activation to when user invites others
- Tight loop (days 1-3): User invites immediately after experiencing value
  - Example: Slack (share link day 1, teammates join day 1-2)
  - Effect: Faster growth curve; k can be <1 but growth still fast
- Loose loop (weeks 2-4): User invites only after becoming confident
  - Example: LinkedIn (invite people after 2 weeks of usage)
  - Effect: Slower growth curve; need k >1 to sustain

GROWTH IMPACT (with k and loop time):
  - k = 0.5, loop time = 1 day: Declining fast (each user loses 50% in next cycle)
  - k = 1.0, loop time = 1 day: Steady-state growth (no compounding, but stable)
  - k = 1.5, loop time = 1 day: Exponential growth (10x in ~10 days)
  - k = 1.05, loop time = 30 days: Slow compounding (10x in ~300 days)

GOAL: k >1 + tight loop time (ideally <7 days)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### How to Design for Viral

```
VIRAL LOOP DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Identify the viral mechanic
  - What is the user action that brings others?
  - Example: Send a message in Slack → invite teammate
  - Example: Get a recommendation on Spotify → share with friend

Step 2: Make viral inevitable (not optional)
  - Don't rely on users choosing to share
  - Make sharing inherent to core experience
  - Example: Slack message → can only be read if recipient joins Slack
  - Counter-example: "Click here to invite friends" (optional, low share rate)

Step 3: Minimize friction in invite
  - Make it 1-click to invite
  - Pre-fill their contact list
  - Explain what invitee will see/experience
  - Example: Slack "Copy invite link" (one click)
  - Counter-example: Require email address, subject line, custom message (too much friction)

Step 4: Optimize conversion from invite
  - When invitee clicks link, show value immediately
  - Reduce signup friction (pre-fill from inviter)
  - Pre-authenticate via social
  - Example: "Your friend [Name] wants to chat with you. Join in 1 click"
  - Counter-example: Generic signup page, inviter name hidden

Step 5: Measure viral coefficient (weekly)
  - Track: % new users from viral / % from other channels
  - Track: k = (new users this week from viral) / (total activated users 1 week ago)
  - If k <1, which step is broken?
    - Low share rate? Make sharing more obvious
    - Low invitee conversion? Improve messaging or reduce friction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Unit Economics Deep Dive

**Fundamental Truth:** If unit economics don't work, scale makes it worse (not better).

### CAC: Customer Acquisition Cost

```
CAC CALCULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Direct Method:
  CAC = (Total marketing spend in period) / (# new customers in period)

  Example:
    Marketing spend: $100K (ads, content, events)
    New customers: 10
    CAC = $10K per customer

Blended Method (multiple channels):
  CAC = [(Ad spend) + (Sales salary) + (Events) + (Tools)] / (Total new customers)

  Example:
    Ad spend: $50K
    Sales salary (1 AE @ $150K × 40% to new customer acquisition): $60K
    Events: $10K
    Tools/overhead: $5K
    Total marketing: $125K
    New customers: 10 (7 from ads, 3 from events/sales)
    Blended CAC = $12.5K per customer

Channel-Specific CAC:
  CAC (paid ads) = $7K (50K / 7 customers)
  CAC (events) = $5K (15K / 3 customers)
  CAC (sales/partnerships) = $15K (60K / 4 customers)

PAYBACK PERIOD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SaaS/Subscription Model:
  Payback period = CAC / (Monthly revenue per customer × Gross margin %)

  Example:
    CAC: $10K
    Monthly revenue (ACV/12): $2K
    Gross margin: 80%
    Payback = $10K / ($2K × 0.8) = 6.25 months

  Target: <12 months (ideally <6 months for venture-scale growth)

One-Time Purchase Model:
  Payback period = CAC / (Revenue per customer × Gross margin %)

  Example:
    CAC: $200
    Revenue per customer: $500
    Gross margin: 60%
    Payback = $200 / ($500 × 0.6) = 0.67 years = 8 months

CHANNEL ECONOMICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Evaluate each channel:
  Channel: [Name]
  CAC: [$]
  Payback period: [Months]
  Scalability: [Can you 2x spend and get 2x customers? Or does CAC rise?]
  LTV: [$]
  CAC:LTV ratio: [Ideal: 1:3 to 1:5]

Decision:
  - CAC:LTV >1:3 AND payback <12 months → SCALE THIS CHANNEL
  - CAC:LTV 1:2 AND payback 12-18 months → OPTIMIZE, then scale
  - CAC:LTV <1:2 OR payback >18 months → PAUSE or KILL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### LTV: Lifetime Value

```
LTV CALCULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Simple Method:
  LTV = (Average annual revenue per customer) × (Average customer lifetime in years) × (Gross margin %)

  Example:
    ACV: $10K
    Avg lifetime: 3 years (before churn)
    Gross margin: 80%
    LTV = $10K × 3 × 0.8 = $24K

More Precise Method (accounts for churn):
  LTV = (ARPU × Gross margin) / (Monthly churn rate)

  Example:
    ARPU (annual revenue per user): $10K
    Gross margin: 80%
    Monthly churn: 2%
    LTV = ($10K × 0.8) / 0.02 = $400K

  (Note: This assumes retention continues indefinitely at current churn rate)

SaaS Cohort Method (most accurate):
  Track cohort: What did Year 1 customers spend? Year 2? Year 3?
  Sum across all years = actual LTV

  Example:
    Cohort Year 1 spend: $10K ACV
    Cohort Year 2 spend: $8K (70% retained)
    Cohort Year 3 spend: $6K (75% of Year 2 retained)
    Cohort Year 4 spend: $4K (67% of Year 3 retained)
    LTV = $10K + $8K + $6K + $4K = $28K

CAC:LTV RATIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Benchmark:
  - <1:1: Negative unit economics (burning money)
  - 1:1 to 1:2: Poor (unprofitable)
  - 1:2 to 1:3: Acceptable (break-even or small profit)
  - 1:3 to 1:5: Healthy (sustainable)
  - 1:5+: Excellent (can afford to pay for growth)

Example:
  Channel A: CAC $10K, LTV $50K → Ratio 1:5 → SCALE
  Channel B: CAC $10K, LTV $20K → Ratio 1:2 → OPTIMIZE
  Channel C: CAC $10K, LTV $10K → Ratio 1:1 → KILL or PIVOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Contribution Margin & Profitability

```
CONTRIBUTION MARGIN (for scaling decisions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Contribution Margin = (Revenue - Variable Costs) / Revenue

Example:
  Revenue: $100 (annual per customer)
  COGS: $20 (hosting, processing)
  Contribution margin: ($100 - $20) / $100 = 80%

Contribution Margin per Customer:
  = ACV × Contribution margin %
  = $100 × 0.8 = $80

Can you scale?
  - If CAC payback <12 months and contribution margin >60%: YES, scale
  - If contribution margin <40%: Scaling is inefficient (each new customer is low-margin)

Fixed vs. Variable Costs:
  Variable costs (scale with customers): COGS, payment processing, hosting
  Fixed costs (don't scale): R&D, marketing, sales team salaries

  Path to profitability:
  - Increase contribution margin (lower COGS, not variable costs)
  - Increase customer revenue (upsell, expand)
  - Spread fixed costs over more customers (scale)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Scaling Diagnostics: What Breaks at 10x?

When you try to scale 10x (e.g., $1M to $10M revenue), some growth lever breaks. Diagnose early.

### Product Scaling Breaks

**Symptom:** As users scale, product experience degrades (slower, less reliable, doesn't scale to enterprise needs)

**Diagnostic:**
- Concurrent users: Can product handle 10x concurrent usage?
- Data volume: Can database handle 10x data?
- Feature complexity: Can product evolve fast enough while supporting scale?

**Fix:**
- Re-architect for scale (move from monolith to microservices, denormalize DB, etc.)
- Timeline: 3-6 months to re-architect
- Cost: $500K-2M in engineering

### Sales Scaling Breaks

**Symptom:** Sales team hits productivity ceiling; new reps underperform; sales cycle doesn't scale

**Diagnostic:**
- Sales productivity: # of customers per AE per year
  - At $1M: 10 customers per AE
  - At $10M: Still 10 customers per AE? Or only 8 due to complexity?
- If productivity declining: Sales scaling broken

**Fix:**
- Hire experienced sales leader (VP Sales, not just more AEs)
- Invest in sales enablement (playbooks, proof assets, training)
- Optimize sales process (reduce cycle time, improve close rate)
- Timeline: 6-9 months to find/hire VP Sales; 3-6 months for improvements
- Cost: $300K-500K (VP Sales + enablement)

### Customer Success Scaling Breaks

**Symptom:** Churn rising as customer base scales; support tickets backing up; customer happiness declining

**Diagnostic:**
- Support ticket volume: Growing faster than revenue? (indication of broken CS)
- NPS: Declining as customer base scales?
- Churn: Rising?

**Fix:**
- Hire VP CS; build CS infrastructure (knowledge base, self-serve, tier-based support)
- Automate onboarding (product tutorials, interactive guides)
- Implement health scoring (proactive intervention for at-risk customers)
- Timeline: 3-6 months to infrastructure
- Cost: $200K-400K

### Pricing Scaling Breaks

**Symptom:** Pricing model doesn't scale; high-value customers see low cost; revenue per customer plateaus

**Diagnostic:**
- Do you have a pricing strategy (value-based) or just pricing (cost+margin)?
- As customers grow, do they expand spend with you? (should be 2-3x)
- Are high-value customers subsidizing low-value?

**Fix:**
- Move to value-based pricing (tied to customer outcome, not cost)
- Implement usage-based pricing (customers pay for value they get)
- Create pricing tiers (capture customer segments at different price points)
- Timeline: 2-3 months to redesign
- Cost: $100K-200K (pricing consultant, sales training)

### Go-to-Market Scaling Breaks

**Symptom:** Acquiring customers in market 1 was easy; market 2 is hard; customer acquisition cost rising

**Diagnostic:**
- Is your product solving a universal problem or market-specific problem?
- Can the same messaging work across markets?
- Do you need different channels per market?

**Fix:**
- Develop market-specific GTM (messaging, channels, partnerships)
- Hire country/regional GMs (they understand local market)
- Localize (not just translate; adapt to local needs)
- Timeline: 6-12 months per new market
- Cost: $1M-2M (local team, localization, marketing)

### Culture/Organization Scaling Breaks

**Symptom:** Company was nimble; now bloated; decision-making slow; people leaving

**Diagnostic:**
- Decision cycle time: Increased?
- Employee satisfaction: Declining?
- Attrition: Rising?

**Fix:**
- Clarify roles/structure (move from flat to hierarchical when >50 people)
- Implement operating rhythm (weekly/monthly reviews instead of ad-hoc meetings)
- Hire management team (CAOs, team leads)
- Establish values/culture documentation (codify what made you special)
- Timeline: Ongoing (cultural change is slow)
- Cost: $500K-1M (hiring, org consulting)

### How to Diagnose Which Breaks First

```
GROWTH SCALING DIAGNOSTIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For each lever, assess current state:

Product:
  - Can it handle 10x users? [Yes / At risk / No]
  - How many engineers to re-architect? [#]
  - Timeline to scale-ready? [Months]

Sales:
  - Sales per AE: [# per year]
  - Is this declining as company scales? [Yes / No]
  - Do you have experienced VP Sales? [Yes / No]
  - Sales cycle length: [Months] — is it increasing? [Yes / No]

CS/Support:
  - Support tickets per customer: [#]
  - Is this increasing? [Yes / No]
  - Churn rate: [%] — is it increasing? [Yes / No]
  - NPS: [Score] — is it declining? [Yes / No]

Pricing:
  - ACV: [$]
  - Expansion rate: [% per year] — is it declining? [Yes / No]
  - High-value customer concentration: [Top 5 = ?% of revenue]
  - Is pricing value-based or cost-based? [Value / Cost]

GTM:
  - % of revenue from initial market: [%]
  - CAC in market 2: [$ vs market 1]
  - Can same channels work 10x? [Yes / No]

Org:
  - Decision cycle time (idea to decision): [Days]
  - Employee NPS: [Score]
  - Attrition: [%]
  - Do you have management layer? [Yes / No]

PRIORITY REPAIR:
  Identify which lever is weakest (most "At risk" or "No" answers)
  Start there. Fix before trying to scale further.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Worked Examples: Growth Loops in Action

### Example 1: Slack Growth Flywheel

```
SLACK GROWTH ENGINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STAGE 1 - ACQUISITION
  How: Sales (direct, partner) + word-of-mouth from existing customers
  CAC: ~$500-1000 (enterprise) or self-serve (low CAC for freemium)

STAGE 2 - ACTIVATION
  What: Install Slack, create workspace, invite first 3 teammates
  Timeline: Same day (very fast)
  Activation rate: 95%+ (product is self-evident)

STAGE 3 - VALUE CREATION
  When: First message sent in channel
  Time to value: Hours
  Aha: "My team is collaborating in one place instead of email"

STAGE 4 - RETENTION
  Why: Switching cost (all team data in Slack) + daily habit
  Retention: 99%+ after 1 year (very sticky)
  Churn: Only if company dissolves

STAGE 5 - EXPANSION
  How: Per-seat pricing; power users purchase upgrades
  Expansion rate: 3-5% per year (average customer expands from 5 to 8 seats)
  Revenue: Initially $100/seat/month; expands to $300/month avg through add-ons

STAGE 6 - VIRAL EFFECT
  Mechanism: Employee joins Slack at Company A; changes jobs to Company B; already knows Slack
  Coefficient: 0.3-0.5 (not purely viral, but employee mobility drives adoption)
  Timeline: 6-12 months (employee changes jobs, introduces Slack at new company)

GROWTH ENGINE PERFORMANCE
  Monthly new customers: 50K+
  YoY growth: 100%+ (at IPO)
  Primary driver: Sales (70%) + viral/word-of-mouth (30%)
  Payback period: 6-12 months (enterprise)
  CAC:LTV: 1:7 (excellent)

KEY TO SUCCESS
  1. Activation was instant (minimal onboarding friction)
  2. Value was immediate (first message is valuable)
  3. Retention was natural (switching cost)
  4. Expansion came from additional use cases (additional channels, apps)
  5. Viral came from employee mobility (not purely viral product loop)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Example 2: DoorDash Marketplace Flywheel

```
DOORWASH GROWTH ENGINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TWO-SIDED MARKETPLACE: Consumers (demand) & Restaurants (supply)

SUPPLY SIDE (Restaurants):
  Acquisition: Door-knocking, partnerships with restaurant groups
  CAC: $5K-10K per restaurant (sales rep time)
  Activation: Menu uploaded, delivery zones set, 2+ drivers in area
  Value: "I can reach customers who want delivery; DoorDash handles order management"
  Expansion: Restaurants increase menu items, add new delivery zones

DEMAND SIDE (Consumers):
  Acquisition: Paid ads, word-of-mouth, app discovery
  CAC: $3-5 per customer (paid ads in competitive markets)
  Activation: Download app, add address, browse 3+ restaurants
  Value: "I can find my favorite restaurant and get it delivered in 30 minutes"
  Expansion: Order more frequently (habit), order more items per order

DRIVER SIDE (Fulfillment):
  Acquisition: Gig marketplace (workers list themselves)
  Activation: Pass background check, accept 1st delivery
  Value: "Flexible income, keep 80%+ of delivery fee"
  Expansion: Drivers work more hours as demand grows

FLYWHEEL MECHANICS
  More restaurants → More selection for consumers → More likely to order → More consumer demand
  More consumers → More orders → Higher earnings per delivery → More drivers attracted → Faster delivery times
  Faster delivery → Better consumer experience → More reorders → Growth compounds

GROWTH IMPACT
  Cycle time: 2-3 weeks (consumer acquisition to becoming regular; restaurant ramp to profitability)
  Viral coefficient: 0.5-0.7 (word-of-mouth helps, but requires paid acquisition to scale)
  Monthly growth: 20-30% YoY in early years
  Unit economics: CAC $3 (consumer), Payback 60-90 days, LTV $300-500, Ratio 1:4

KEY TO SUCCESS
  1. Solved chicken-egg problem: Seed restaurants first (supply), then acquire customers (demand)
  2. Hyper-local focus: Dominate single city before expanding (100% penetration of restaurants, then geo expansion)
  3. Driver flexibility: Attracted drivers as gig economy grew (network effect of driver supply)
  4. Speed as differentiator: 30-minute delivery was novel (now table stakes)
  5. Unit economics discipline: Knew CAC, LTV, payback before scaling; scaled profitably
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Summary: Growth Engine Design Checklist

```
GROWTH ENGINE DESIGN CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Flywheel Mapped
  - All 6 stages defined (acquisition, activation, value, retention, expansion, viral)
  - Cycle time calculated (days from acquisition to re-investment/viral)
  - Tightest bottleneck identified

□ Network Effects Assessed
  - Which network effect applies? (direct, indirect, data, marketplace, or none)
  - Can you design for it? (what changes?)
  - What's critical mass? (when is product valuable?)

□ Viral Coefficient Modeled
  - k = % share × # invited × % convert
  - Is k >1? (sustainable) or <1? (requires paid acquisition)
  - Can you improve share rate? Invite experience? Conversion?

□ Unit Economics Locked In
  - CAC calculated by channel (not blended guess)
  - LTV calculated (not assumed)
  - CAC:LTV ratio ≥ 1:3 for scale
  - Payback period ≤ 12 months
  - Contribution margin ≥ 60%

□ Scaling Diagnostics Run
  - Which lever breaks at 10x? (product, sales, CS, pricing, GTM, org)
  - Timeline to fix? (estimate)
  - Investment required? (budget)

□ 30-60-90 Day Plan
  - Month 1: [Growth initiative]
  - Month 2: [Optimization based on Month 1 learning]
  - Month 3: [Scale if metrics support; pivot if not]
  - Success metrics: [Specific thresholds per month]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
