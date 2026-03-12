# Pricing & Packaging Strategy

## Purpose & Scope

This reference answers: What should customers pay? How should we structure value capture? What packaging tiers make sense? How do we optimize pricing for unit economics and customer satisfaction?

Pricing is the most underlevered lever in GTM. A 10% price increase on the same volume compounds to 10-15% improvement in operating leverage. Yet most companies treat pricing as an afterthought. Don't.

---

## Part 1: Value-Based Pricing Methodology

The fundamental principle: Price based on value delivered, not on cost or competitive price. If you solve a $500K problem, $50K is a bargain. If you solve a $5K problem, $50K is robbery.

### Understanding Willingness-to-Pay (WTP)

Your customer's willingness to pay is determined by:
1. **Value of benefit received** — How much better off are they? Quantify it. ($500K saved, 3 months faster time-to-market, 20% productivity increase)
2. **Cost of alternative** — What would they do if you didn't exist? (Build it themselves: $200K + 6 months + ongoing maintenance. Or use inferior tool: $50K/year + 10% quality loss)
3. **Risk of change** — How much pain to switch vendors? (Learning curve, integration, team retraining, switching to a known vendor costs 20% of the savings)

**Formula: Price = (Benefit - Alternative Cost - Risk Buffer) × 70-80% of savings**

Example:
- Benefit: A customer saves 3 FTEs (3 × $150K = $450K/year)
- Alternative: Would hire contractors (3 × $100K = $300K/year) — so net benefit is $150K/year
- Risk buffer: 30% for switching risk = $45K
- Suggested price: ($150K - $45K) × 70% = $73.5K/year

At $73.5K price, customer has $76.5K/year in captured value. They're thrilled.

### Three Pricing Research Methods

#### 1. **Van Westendorp Price Sensitivity Analysis**

Ask customers four questions:
1. "At what price would you consider this product a bargain?" (Very cheap)
2. "At what price would you consider this product expensive?" (Too expensive)
3. "At what price would the product be too cheap, making you question its quality?" (Below this, seems low-quality)
4. "At what price would you consider this product reasonably priced?" (Fair price)

**Interpretation:**
- Acceptable price range: Between the "cheap" and "too expensive" answers
- Optimal price point: Where the "reasonably priced" and "too cheap" lines intersect
- Avoid going above "too expensive" — above this price, too many say "no"

**Limitations:** Hypothetical. What people say they'll pay doesn't match what they actually pay.

#### 2. **Gabor-Granger Method**

Ask customers directly: "Would you buy this product at $[X]?"

Start at what you think is the right price. If they say yes, raise it. If they say no, lower it. Repeat with different customer segments.

**Output:** Price acceptance curve (% saying yes at each price point)

**Finding the sweet spot:**
- The price where 40-50% say "yes" is typically optimal
- This balances revenue (fewer customers at higher price vs. more customers at lower price)

**Limitations:** Still hypothetical. But more concrete than Van Westendorp.

#### 3. **Conjoint Analysis (Advanced)**

Show customers product configurations with different features and price points. Ask which they prefer.

Example:
- Option A: 5 users, 10 integrations, email support — $500/month
- Option B: 10 users, 25 integrations, email support — $750/month
- Option C: 5 users, 25 integrations, phone support — $800/month
- "Which would you choose?"

Repeat this 30+ times with different combinations. Model emerges showing:
- How much customers value each feature
- How much they'll pay for each feature
- Optimal packaging and price point

**Limitations:** Complex to execute. Requires sample size (200+). But most reliable method.

### Practical Alternative: Ask Customers

Best approach: Interview your top 10 customers.

**What to ask:**
- "How much would you pay if we removed feature X?"
- "What would you pay if we added feature Y?"
- "If you had to switch to the next-best vendor, what would they charge?"
- "What percentage of our value do we capture vs. you keep?"

Their answers reveal willingness-to-pay far better than any survey.

---

## Part 2: Packaging Design Framework

Packaging is the art of bundling features, users, support, and volume into tiers that maximize revenue while aligning with how customers see value.

### Three Packaging Archetypes

#### 1. **Good-Better-Best (Feature-Based)**

Most common for B2B SaaS. Tiers differ by feature access.

**Design:**
- **Good ($X/month):** Core features, solves the basic job. 2-5 core features.
- **Better ($2-3X):** Core features + advanced features. 10-15 features total.
- **Best ($4-10X):** Everything + premium features + support. All features + priority support + custom.

**Example (Project Management):**
- Good: Up to 5 projects, 10 team members, email support — $99/month
- Better: Unlimited projects, 50 team members, templates, portfolio view, Slack integration — $299/month
- Best: Everything + custom workflows, advanced reporting, SSO, phone support, dedicated success manager — $999+/month

**Pros:**
- Clear mental model (customers understand tiers)
- Encourages upsell (feature gaps drive upgrades)
- Works at any price point

**Cons:**
- Feature gates create friction (customer needs 1 premium feature, has to buy whole tier)
- Hard to optimize — each change affects revenue mix
- Competitors can match feature-for-feature

#### 2. **Usage-Based (Consumption)**

Price based on how much the customer uses the product.

**Design:**
- Base price covers X amount. Above X, you pay per unit.
- Metrics: API calls, seats, storage, bandwidth, queries, transactions

**Example (Cloud Storage):**
- Starts free: 5GB storage
- Then $0.50 per GB per month above 5GB

**Example (PLG SaaS):**
- Free: 1,000 API calls per month
- $0.01 per call above 1,000

**Pros:**
- Aligns price with value (bigger problems = bigger price)
- Removes feature gating (customer can use anything they want)
- Customer onboards at low cost (free or cheap), expands as usage grows
- Fair (pay for what you use)

**Cons:**
- Revenue unpredictability (can't forecast)
- Customer can't predict their bill (causes churn if surprised)
- Can optimize away usage to reduce costs (not ideal for you)

**Critical Success Factor:** Customers must be able to estimate their usage/bill in advance. Otherwise they'll churn when surprised.

#### 3. **Hybrid (Seat + Usage + Features)**

Most sophisticated. Combines seat-based, usage-based, and feature tiers.

**Design:**
- Base: Seats (employees) × monthly cost
- Usage: Core consumption (API calls, storage) included; above threshold, overage charges
- Features: Access to advanced features at each tier

**Example (HubSpot-like):**
- Base: $50/month per user (up to 3 users = $150)
- Usage: 10,000 contacts included. $500 per 10K additional contacts. (500K contacts = $25K/year overage)
- Features: Starter tier = basic CRM. Professional = automation + advanced reporting. Enterprise = custom workflows + priority support

**Pros:**
- Aligns with how value is delivered
- Reduces feature gating (customer doesn't lose money by using more)
- Scales with customer growth

**Cons:**
- Complex to communicate
- Customer can't predict bill
- Needs clear usage tracking/monitoring

---

## Part 3: Pricing Psychology Principles

### 1. **Anchoring**
Customers use the first number they see as a reference point.

**Application:**
- Show expensive tier first (anchors expectation upward)
- Show your competitor's price before yours (if you're cheaper)
- Display annual price, then divide by 12 (looks smaller than showing monthly)
- Example: "$600/year" looks cheaper than "$50/month" even though it's identical

### 2. **The Decoy Effect**
Adding a third option can increase sales of a higher-priced tier.

**Design:**
- Good: $99
- Better: $299 (attractive compared to Good)
- Best: $499

Problem: 60% pick Good, 40% pick Better, no one picks Best.

**Solution:** Add a decoy:
- Good: $99
- Better: $299
- Decoy ("Better Plus"): $399 (expensive, fewer features than Best)
- Best: $499

Now: Best looks like a bargain compared to Decoy. Sales shift toward Best.

### 3. **Bundling**
Offer multiple services together at a lower combined price than separate.

**Example:**
- Email alone: $50/month
- CRM alone: $75/month
- Email + CRM separately: $125/month
- Email + CRM bundled: $99/month

Bundled looks like a deal (save $26) even though you're lowering price.

### 4. **Versioning**
Segment customers by willingness to pay without lowering price for everyone.

**Example:**
- Product Standard (digital download): $29
- Product Plus (digital + 2 consultations): $99
- Product Enterprise (digital + consultations + implementation): $499

Different customers see different value in add-ons. Some buy Plus for consultations. Some buy Standard. All happy.

### 5. **Reference Prices**
Customers compare your price to:
- Competitors
- Products they've seen before
- Perceived value of alternative

**Application:**
- Benchmark against competitors (if you're 20% cheaper, make it visible)
- Show ROI (customer saves $100K, pays $10K, sees 10:1 return)
- Avoid commoditizing (if only selling on price, you lose)

### 6. **Price Framing**
How you present price matters more than the number.

**Examples:**
- "$100/month" feels expensive
- "$3.33/day" feels cheap (same thing)
- "Starts at $99" anchors the conversation upward
- "As low as $9" anchors downward
- Emphasize savings/value: "Save $10K/year" vs. "Costs $5K/year"

---

## Part 4: Competitive Pricing Analysis

You must understand what competitors charge and why.

### Competitive Pricing Matrix

| Competitor | Price | Positioning | Target Segment | Features |
|------------|-------|-------------|-----------------|----------|
| [Competitor A] | $[X]/month | Low-cost, high-volume | SMB | Core features |
| [Competitor B] | $[X]/month | Premium, support-heavy | Enterprise | All features + support |
| [Your Company] | $[X]/month | Mid-market, balanced | Mid-market | Balanced feature set |

### Pricing Intelligence Sources

1. **Public websites** — Check pricing pages (most complete)
2. **G2/Capterra reviews** — Reviewers often mention price
3. **Trial signups** — Sign up, go through trial, see pricing at upgrade
4. **Sales conversations** — Ask competitors' customers "how much do you pay?"
5. **Financial filings** — Public companies disclose ARR, customer count (can back into average price)
6. **Win/loss analysis** — When you lose to a competitor, ask "was it price?" and "what did they quote?"

### Interpreting Competitive Pricing

**If competitors charge $X and you charge $Y:**
- **Y < X by 20%+:** You're the discount player. Risk: margin pressure, customer expectations, race-to-bottom
- **Y = X:** You're competitive. Risk: no differentiation
- **Y > X by 20%+:** You're premium. Risk: need to justify premium (brand, support, features, outcomes)

**When to price above competitors:**
- Your product delivers demonstrable superior outcomes (higher ROI, fewer integrations needed, faster time-to-value)
- Your target segment has higher willingness to pay
- You have strong brand or customer lock-in
- You serve a specific need competitors don't address well

**When to price below competitors:**
- You're disrupting with a newer technology or approach
- You're targeting a lower-tier customer (SMB vs. enterprise)
- You're building market share (low prices to gain volume)
- You're more efficient (lower CAC, lower COGS, lower support cost)

---

## Part 5: Price Change Management Playbook

Changing prices is high-risk, high-reward. Mishandled, it causes churn. Handled right, it's revenue growth.

### When to Change Prices

**Raise prices when:**
- Product is increasingly valuable (feature expansion, improved efficiency, new integrations)
- Demand is outpacing supply (long sales cycles, requests for custom contracts)
- Unit economics need improvement (CAC is too high relative to LTV)
- Market has moved (competitors are more expensive, you're underpriced)

**Don't raise prices when:**
- Product is stagnant (no new value to justify it)
- Customer churn is high (raising prices makes it worse)
- You're in a price war (you'll lose)

### Price Change Tactics

#### Tactic 1: **Grandfather Existing Customers**
- New customers get new pricing
- Existing customers keep old pricing (for 1-2 years)
- At renewal, move to new pricing

**Pros:** Minimal churn
**Cons:** Revenue dips for 2 years as cohorts turn over
**Best for:** Price increases 10-20%

#### Tactic 2: **Proactive Communication + Value Reminder**
- Announce price increase 60 days in advance
- Explain what's new (features, efficiency, support)
- Offer 1-year locked price if they commit by deadline

**Pros:** Signals growth and investment. Customers understand.
**Cons:** Some will churn. Some will negotiate.
**Best for:** Price increases 10-30%, where value justification is clear

#### Tactic 3: **Shift to New Pricing Model** (e.g., feature-based → usage-based)
- Existing customers: Option A (stay on old pricing) or Option B (move to new model, calculated to be similar or better value)
- New customers: New model only
- Optionally: Incentivize migration (1% discount if they move, then raise on new model later)

**Pros:** Can increase revenue without "raising prices" (framed as modernization)
**Cons:** Confusing if not communicated well
**Best for:** Major pricing model overhaul

#### Tactic 4: **Value-Based Discounting** (Lower price for high-value behaviors)
- Customers who commit to 3-year contracts get 15% discount
- Customers who agree to case study/reference get 10% discount
- Early adopters of new feature get grandfathered pricing

**Pros:** Rewards valuable behaviors; increases retention (multi-year lock-in)
**Cons:** Discounts compound (hard to raise prices later)
**Best for:** Transitioning between pricing models

### Pre-Launch Checklist

Before changing prices:
1. **Model the impact** — What's churn elasticity? (For every 10% price increase, expect X% churn. Use historical data.)
2. **Segment analysis** — Will all segments bear the increase? (Might need to increase prices on mid-market but hold for SMB)
3. **Grandfather policy** — How long do existing customers keep old pricing?
4. **Communication plan** — How will you announce? Email? Sales call? Website banner?
5. **Support training** — What objections will you get? How do sales/support respond?
6. **Timing** — Best time: during low churn season, aligned with renewals, not during market downturn

---

## Part 6: Monetization Strategy by Business Model

Different business models require different pricing approaches.

### B2B SaaS (Most Common)

**Pricing model:** Seat-based, usage-based, or hybrid

**Typical pricing:**
- SMB: $99-$499/month (low user count, basic support)
- Mid-market: $1-10K/month (medium user count, advanced features, business support)
- Enterprise: $10K-$500K+/year (unlimited users, custom features, dedicated success)

**Key metric:** CAC < LTV ÷ 3 (i.e., price high enough to recover CAC in <3 years)

### Enterprise Software (Long Sales Cycles)

**Pricing model:** Value-based (custom quotes), not standardized

**Typical pricing:**
- Starts at $250K/year (minimum commitment)
- Could be $1-10M+/year depending on size, usage, customization

**Why pricing isn't published:** Every deal is different (company size, usage, risk, implementation complexity). Competitor pricing would be wrong anchor.

**Key metric:** Months-to-productive implementation (faster = higher price justified)

### Marketplace/Platform

**Pricing model:** Take rate (% of transaction) or subscription + take rate

**Typical pricing:**
- Take rate: 5-30% of transaction value
- Subscription: $500-5K/month flat + take rate

**Why this model:** Aligns incentive (you make money when customers make money)

**Challenge:** Lower take rates (e.g., 5%) mean high payment volume. If processing cost is 3%, margin is thin.

### Usage-Based/API

**Pricing model:** Per API call, per GB, per user, per request

**Typical pricing:**
- Starts free or cheap (first 1M calls free, then $0.001 per call)
- Scales up to tiered (bulk discounts: 1-10M calls at one rate, 10-100M at lower rate)

**Why this model:** Transparent, fair, aligns with value

**Challenge:** Unpredictable revenue. Customers optimize usage to reduce costs. Need good usage monitoring/alerts.

### Freemium

**Pricing model:** Free tier + paid tiers

**Typical pricing:**
- Free: 1 project, 5 team members, basic features
- Paid: $X/month, scales up to $Y/month for power users

**Key ratio:** Free-to-paid conversion (typically 5-15%). Below 5% means free tier is too generous or paid tier doesn't offer enough value.

---

## Part 7: Pricing Anti-Patterns

### Anti-Pattern 1: Race-to-Bottom

**Symptom:** Competitor lowers price. You lower price to match. Market becomes commoditized.

**Why it fails:** Margin compression, hard to differentiate, unsustainable

**Fix:** Don't compete on price. Compete on value (outcomes, speed, support, integration). Communicate why you're different.

### Anti-Pattern 2: Feature Gating That Frustrates

**Symptom:** Feature is critical for the job. But it's in the high tier. Customer is frustrated, feels gated.

**Why it fails:** Churn. Bad word of mouth. Perception of unfairness.

**Fix:** Gate features that enable expansion (more users, advanced analytics), not features required for core job.

### Anti-Pattern 3: Annual Lock-in Backlash

**Symptom:** You require 1-3 year annual contracts. Customer feels trapped. Doesn't expand. Leaves at renewal.

**Why it fails:** Customer satisfaction drops if they feel forced into commitment.

**Fix:** Offer month-to-month at +20% price premium. Customers who value flexibility pay more. Those who commit get discount.

### Anti-Pattern 4: Pricing Doesn't Align with Value

**Symptom:** You're pricing on seat count. But customer value is based on revenue impact or usage.

**Why it fails:** Customers are either overpaying (high value, low seats) or underpaying (low value, high seats). Bad unit economics or bad customer outcomes.

**Fix:** Audit your top 10 customers. Calculate true value. Price should correlate with value received, not arbitrary metric.

### Anti-Pattern 5: Misalignment Between Packaging and Buying Committee

**Symptom:** Your Good tier ($99) is for SMB, but it still requires CFO approval. Or your Enterprise tier ($100K) has a 10-person evaluation.

**Why it fails:** Wrong customer in the tier (buyers can't approve purchase), slow close, friction

**Fix:** Tier by buying committee size and authority, not just features.

---

## Quality Gates for Pricing & Packaging

Before launching:

1. **Can you explain your pricing in 30 seconds to a customer?** (If not, it's too complex)
2. **Do customers understand why tiers exist?** (Survey 5 customers: "Why did you pick tier X?")
3. **Is pricing correlated with value?** (Higher tier should solve bigger problem, not just have more features)
4. **Can you defend pricing vs. key competitors?** (Why you + not them?)
5. **Are you making margin?** (Revenue × 70%+ gross margin minimum for most SaaS. If not, cost structure is wrong, not pricing.)
6. **Have you stress-tested elasticity?** (Run scenarios: -10% price impact? +20% impact? What happens to unit economics?)
