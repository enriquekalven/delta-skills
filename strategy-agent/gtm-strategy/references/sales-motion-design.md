# Sales Motion Design

## Purpose & Scope

This reference answers the core question: How should customers buy from us? Should we be Product-Led Growth (PLG), Sales-Led Growth (SLG), or a hybrid? What does the sales process look like? How do we capacity plan?

A sales motion is the repeatable, scalable way you convert leads to customers. It includes discovery, evaluation, negotiation, and onboarding. Design this explicitly or it defaults to chaos.

---

## Part 1: PLG vs. SLG vs. Hybrid Decision Framework

There is no universal best motion. The right motion depends on your customer (how they prefer to buy), your product (how it delivers value), and your constraints (budget, team, runway).

### The PLG vs. SLG Decision Matrix

Score your situation against these dimensions. Weighting varies by company stage and market.

| Dimension | PLG-Favoring | Neutral | SLG-Favoring |
|-----------|--------------|---------|--------------|
| **Product Complexity** | <1 day to value | 1-2 weeks | >2 weeks to value |
| **Economic Buyer** | User is buyer | Multiple parties | Separate from user |
| **ACV** | <$500 | $500-$5K | >$5K |
| **Sales Cycle** | <1 week | 2-4 weeks | >4 weeks |
| **Buying Committee** | 1 person | 2-3 people | 4+ people |
| **Implementation** | Self-service | Light touch | Heavy/custom |
| **Procurement Friction** | None | Some | Extensive |
| **Customer Success** | Low touch | Medium touch | High touch |

### Scoring System

For each dimension, assign a point:
- PLG column: +1 point
- Neutral column: 0 points
- SLG column: -1 point

**Final score interpretation:**
- **+4 to +8:** Pure PLG is optimal. Focus on frictionless product experience, viral loops, community.
- **0 to +3:** PLG + light sales enablement. Self-serve trial, then in-app upgrade or sales conversation for larger deals.
- **-3 to 0:** Hybrid or PLG with heavy sales layer. Free trial shows value, then sales team handles deals >threshold.
- **-4 to -8:** Pure SLG. Outbound or inbound lead gen into structured sales process.
- **<-8:** Enterprise SLG. Complex RFx, heavy evaluation, dedicated account management.

### Example Scoring

**Example A: Project Management Tool (Asana-like)**
- Product Complexity: PLG (+1) — Core value in <1 day
- Economic Buyer: PLG (+1) — User often buys own tool
- ACV: Neutral (0) — Could be $100 or $5K depending on team size
- Sales Cycle: PLG (+1) — Users self-convert in days
- Buying Committee: PLG (+1) — Usually one person or small team
- Implementation: PLG (+1) — Users self-onboard
- Procurement: PLG (+1) — No enterprise procurement
- Customer Success: PLG (+1) — Product is self-explanatory
- **Score: +7 → Pure PLG**

**Example B: Marketing Automation (HubSpot-like)**
- Product Complexity: Neutral (0) — 1-2 weeks to real value
- Economic Buyer: SLG (-1) — CMO or CFO decides, not user
- ACV: Neutral (0) — $500-$5K depending on company
- Sales Cycle: Neutral (0) — 2-4 weeks typical
- Buying Committee: Neutral (0) — 2-4 people
- Implementation: SLG (-1) — Requires setup, integration, content
- Procurement: SLG (-1) — Standard SOW, contracts
- Customer Success: SLG (-1) — Needs onboarding, training
- **Score: -4 → SLG Dominant (but with free trial)**

**Example C: Financial Planning Software for CFOs**
- Product Complexity: SLG (-1) — 3+ weeks to expert-level value
- Economic Buyer: SLG (-1) — CFO or Board decides
- ACV: SLG (-1) — $50K-$500K+
- Sales Cycle: SLG (-1) — 6-12 months typical
- Buying Committee: SLG (-1) — 5+ people (CFO, Controller, CEO, Board, procurement)
- Implementation: SLG (-1) — Custom implementation, data migration
- Procurement: SLG (-1) — Formal RFx, legal review, SOC 2, custom terms
- Customer Success: SLG (-1) — Needs dedicated CSM, training, ongoing optimization
- **Score: -8 → Pure Enterprise SLG**

---

## Part 2: PLG Playbooks

### When PLG Works

- Product solves a clear problem that users recognize immediately
- Time-to-value is <7 days (ideally <24 hours)
- User is the economic decision maker or can buy without approval
- ACV is <$500 (or customers expand to higher ACV over time)
- Freemium model is defensible (not giving away the whole solution)

### PLG Mechanisms (Choose 1-2)

#### 1. **Free Trial Model**
Users get full access to the product for a limited time (14-30 days), then pay.

**Conversion mechanics:**
- Day 1-3: User discovers value, gets hooked
- Day 7: "You're out of daily actions" or "Upgrade to continue"
- Day 14: Trial ending, upgrade offer, risk of churn
- Day 21: Final upgrade reminder

**Metrics:**
- Trial activation rate (% who set up workspace and complete key action)
- Time-to-value (days to first success)
- Trial-to-paid conversion (30-50% typical for strong PLG)
- Payback period (how long to recover CAC if paying for free trial)

**Best for:** Enterprise software, specialized tools, productivity apps

#### 2. **Freemium Model**
Perpetual free tier (limited features or usage) + paid tiers with more features.

**Design principle:** Free tier must deliver real value (not a demo), but should hit a natural limitation that requires paid.

**Conversion mechanics:**
- Free users: Can do their core job, but with limits (1 project, 5 projects, team size, feature gates)
- Hit the limit: Upgrade prompt (contextual, in-moment, not nagging)
- Upgrade offer: Clear value (new features, usage increase, team expansion)

**Metrics:**
- Free-to-paid conversion (5-15% typical, depends heavily on limit design)
- Time-to-upgrade (months to years depending on how fast they hit the ceiling)
- CAC (often near-zero for freemium; revenue comes from expansion)
- LTV (expansion revenue is key; single-seat users often have low LTV)

**Best for:** Tools with natural freemium architecture (Figma, Slack, Dropbox, Notion)

#### 3. **Reverse Trial Model**
Customer enters credit card upfront, then gets X days free, then charged.

**When it works:** When you have strong product conviction and churn will be low

**Conversion mechanics:**
- User enters card to access product
- Gets X days free (often 14 days)
- Auto-charges on day 15 unless user cancels
- High-touch onboarding during trial to lock in value

**Metrics:**
- Trial completion → charge conversion (60-80% typical; lower if onboarding is poor)
- Immediate churn (users canceling after first charge)
- CAC (card data on file increases CAC because of payment processing; offset by lower CAC-to-paid friction)

**Best for:** High confidence product, strong onboarding, low implementation friction

#### 4. **Open Source → Commercial**
Free, open-source community product + paid commercial tier.

**Mechanics:**
- Open-source brings users, builds trust, creates community
- Paid tier adds commercial features, support, compliance, dedicated deployments
- Community users self-select: those who need commercial features pay; hobbyists stay free

**Metrics:**
- Adoption rate (GitHub stars, downloads)
- Conversion rate (% of active users who buy commercial license)
- Revenue per user (typically low, 2-5% of user base)
- Community strength (GitHub PRs, ecosystem growth)

**Best for:** Infrastructure, developer tools, data platforms (React, Node.js, Kubernetes commercial versions)

### PLG Optimization Levers

Once the basic model is in place:

**1. Activation Optimization**
- Reduce steps to first success from 10 to 3
- Remove optional setup (ask for it after first value)
- Create "aha moments" (moment where user realizes value)
- Measure: % of users who complete key action by day 1

**2. Engagement Optimization**
- In-app onboarding (tooltips, walkthroughs, progressive disclosure)
- Viral loops (referral, invitations, shared projects)
- Community (forums, help docs, user community)
- Measure: weekly active users, retention by cohort

**3. Upgrade Optimization**
- Contextual upgrade prompts (in-moment when user hits limit)
- Clear value (show what new tier enables)
- Risk mitigation (money-back guarantee, pause instead of cancel)
- Measure: trial-to-paid conversion, CAC payback

**4. Expansion Optimization**
- Usage-based pricing (more usage = more revenue)
- Natural upsells (freemium → paid, seat expansion, module add-ons)
- Engagement data to identify upgrade opportunities
- Measure: net revenue retention, expansion revenue %

---

## Part 3: SLG Playbooks

### When SLG Works

- Product value is clear but requires explanation (>1 week to realize)
- Economic buyer is different from user (budget owner, procurement owner)
- ACV is $5K+ (enough to justify dedicated sales effort)
- Selling into existing processes (RFx, vendor evaluation, procurement)
- Complex implementation or integration needed

### SLG Channels (Choose 1-3)

#### 1. **Outbound Model**
Sales team identifies and reaches out to target accounts.

**Process:**
- Week 0-1: Build ICP-based prospect list (firmographic, technographic, behavioral fit)
- Week 1-2: Outreach campaign (email sequences, LinkedIn, calls)
- Week 2-3: Discovery calls with interested prospects
- Week 3-4: Product demo with champion
- Week 4-6: Evaluation with technical/buying committee
- Week 6-8: Proposal and negotiation
- Week 8-12: Legal/procurement, contract signature, implementation

**Metrics:**
- Outreach volume (emails/calls per rep per day)
- Response rate (% who reply) — 2-5% typical
- Qualified lead rate (% of responses who are real opportunities) — 20-40%
- Opportunity conversion (% of qualified leads who buy) — 20-40%
- Sales cycle length (days from first contact to close) — 60-90 days
- CAC (fully loaded: salary, commission, tools, overhead ÷ new customer count)

**Best for:** Mid-market and enterprise SaaS, vertical software, highly targeted niches

#### 2. **Inbound Model**
Prospects find you (content, SEO, ads, community) and self-qualify.

**Process:**
- Prospect discovers via blog, PPC ads, SEO, community, analyst reports
- Lands on website, reads content, understands problem
- Self-qualifies: "This solves my problem"
- Downloads resource, signs up for webinar, or requests demo
- Inbound lead enters CRM, routed to sales team
- Demo and sales motion begin (similar to outbound from this point)

**Metrics:**
- Website traffic
- Lead generation rate (% of visitors who become leads) — 2-5% typical
- Lead quality (% of leads who become qualified opportunities) — 20-40%
- Lead response time (how fast sales responds to inbound lead) — <1 hour ideal
- Inbound sales cycle (often faster than outbound; 45-60 days vs. 90+)
- CAC (often lower than outbound if demand is organic)

**Best for:** Established brands, strong content marketing, mature markets with existing demand

#### 3. **Account-Based Marketing (ABM)**
Highly targeted campaigns to a small list of high-value accounts.

**Process:**
- Identify top 100 accounts worth $500K+ ACV
- Research each account (org structure, budget cycles, recent news, growth)
- Build custom outreach (personalized email, custom content, executive engagement)
- Sales + marketing align (same targets, same messaging, coordinated cadence)
- Each account gets 5-10 targeted touches from sales + marketing
- Sales follow up with discovery once interest is evident

**Metrics:**
- Account penetration (% of target accounts contacted)
- Engagement rate (% who open email, visit website, attend event)
- Opportunity conversion (% of engaged accounts that move to sales)
- Average ACV (typically 3-5x higher than non-ABM deals)
- Sales cycle (often longer due to complexity, 6-12 months)
- CAC (per account, not per lead; much higher per lead but lower per revenue dollar)

**Best for:** Enterprise SaaS, executive sales, large contract values, relationship-driven sales

#### 4. **Channel/Partner-Led Model**
Partners or resellers sell on your behalf.

**Process:**
- Recruit and certify channel partners (integrators, resellers, consultants, agencies)
- Provide partners with sales tools, training, and pricing
- Partners find, sell, and sometimes implement for customers
- Company provides technical support, customer success, relationship oversight

**Metrics:**
- Partner recruitment and retention
- Partner pipeline (deals in progress)
- Partner close rate (% of partner-sourced leads that close)
- Partner CAC (lower than direct sales if partners have warm relationships)
- Partner margin (partner discount, partner commissions)
- Conflict with direct sales (do you also sell direct to their customers?)

**Best for:** Companies with broad TAM requiring scale, complex implementations, geographic expansion, existing channel relationships

### Sales Process Design

Once you choose your inbound/outbound mix, design the sales process explicitly:

**Stage 1: Lead Generation**
- Entry criteria: [What makes someone a lead?]
- Activities: [What does sales do to qualify?]
- Exit criteria: [What proves they're sales-qualified (SQL)?]
- Duration: [Typical length to SQL]

**Example:**
- Entry: Website visitor who downloads resource or requests demo
- Activities: Sales calls within 24 hours, asks 3 discovery questions, assesses fit
- Exit: Budget confirmed, timeline confirmed, champion identified
- Duration: 3-7 days

**Stage 2: Discovery**
- Entry criteria: [What makes someone an opportunity?]
- Activities: [What sales conversation happens?]
- Exit criteria: [What proves they're a real prospect?]
- Duration: [Typical length]

**Example:**
- Entry: SQL who passes fit assessment (right ICP, has budget, has timeline)
- Activities: 30-45 min discovery call; map pain points, budget, buying committee, decision timeline
- Exit: Pain-budget-timeline-authority (PITA) confirmed; clear next step scheduled
- Duration: 7-14 days

**Stage 3: Evaluation**
- Entry criteria: [What qualifies for a demo?]
- Activities: [What does the evaluation entail?]
- Exit criteria: [What proves product is a fit?]
- Duration: [Typical evaluation time]

**Example:**
- Entry: Prospect has confirmed pain, budget, timeline, and authority
- Activities: Product demo tailored to their use case; POC offer if complex; reference customer call
- Exit: Evaluation committee agrees product solves problem; pricing discussion begins
- Duration: 14-30 days

**Stage 4: Proposal & Negotiation**
- Entry criteria: [When do you send a proposal?]
- Activities: [Proposal, pricing discussion, legal/procurement]
- Exit criteria: [What closes the deal?]
- Duration: [Typical negotiation time]

**Example:**
- Entry: Prospect agrees product fits and is willing to consider purchase
- Activities: Send SOW with pricing, answer procurement questions, negotiate terms, legal review
- Exit: Contract signed, payment terms agreed, kickoff scheduled
- Duration: 14-30 days (can extend if procurement is heavy)

**Stage 5: Closed Won**
- Handoff to customer success, implementation begins

---

## Part 4: Hybrid Motion Design

Most companies don't fit pure PLG or pure SLG. Instead, they use hybrid motion: bottom-up (users discover and self-serve) + top-down (sales closes bigger deals with multiple stakeholders).

### Hybrid Mechanics

**Bottom-up engine (PLG-like):**
- Free trial or freemium product
- Users discover, self-onboard, use product
- Hit a ceiling (feature, users, usage, support needs)
- Self-upgrade or contact sales for larger deal

**Top-down engine (SLG-like):**
- Sales team pursues larger accounts (10+ users, company-wide rollout)
- Sales team prospects early in customer lifecycle (before they self-discover)
- Sales team focuses on negotiating, procurement, enterprise features
- Sales team handles contract renewal, expansion

### Design Questions for Hybrid

1. **At what ACV does a deal go to sales vs. stay self-serve?**
   - Example: Deals <$5K go fully self-serve; $5-25K get a light-touch sales conversation; >$25K require full sales engagement

2. **Do bottom-up and top-down compete or reinforce?**
   - Reinforce: User discovers product, gets value, becomes champion; sales then sells to team/company
   - Compete: Sales tries to close a prospect, but product's free tier already converted them (and sales loses commission)
   - Design the commission structure and handoff clearly to avoid misalignment

3. **What's the expansion strategy from small-to-large?**
   - Example: Free user starts with $100/month plan. Over 1 year, expands to $1K/month as team grows. At $500 MRR run rate, sales takes over the account for enterprise negotiation.

### Example: Slack's Hybrid

**Bottom-up:** Teams discover Slack, self-onboard via free tier, hit user/message limits

**Top-down:** Once team has 500+ users (signaling enterprise-scale adoption), Slack enterprise sales engages for:
- Procurement and contract requirements
- Custom integrations and administration
- Discounted pricing on multi-year contracts

Result: Organic adoption + land-and-expand + sales expansion = 10x LTV compared to pure PLG or pure SLG

---

## Part 5: Sales Capacity Planning

You can't scale without knowing how many reps you need.

### Capacity Planning Model

**Step 1: Define the target**
- Year 1 target ARR: $[X]
- Year 1 target # of new customers: [N]

**Step 2: Calculate average contract value (ACV) for new customers**
- ACV = Target ARR ÷ Target # of customers
- Example: $5M ARR ÷ 100 customers = $50K ACV

**Step 3: Estimate quota per rep**
- Quota per rep = target reps' annual achievement
- Example: Enterprise sales quotas typically $500K-$1M per rep per year
- Example: Mid-market quotas typically $200-300K per rep per year
- Example: SMB/self-serve quotas typically $50-100K per rep per year (lower because less interaction needed)

**Step 4: Calculate reps needed**
- Reps needed = Target ARR ÷ Quota per rep
- Example: $5M target ARR ÷ $250K quota per rep = 20 reps needed

**Step 5: Account for ramp and turnover**
- New reps take 6 months to full productivity (apply 50% productivity year 1)
- Annual turnover is 20-30% in sales
- Add buffer: need to hire 25-30% more reps than pure quota math suggests

**Step 6: Build out pipeline requirements**
- Sales cycle (e.g., 90 days)
- Win rate (e.g., 25%)
- Pipeline coverage ratio (typically 3:1 to 5:1; need $3-5 of pipeline to close $1 of revenue)
- SAOs needed = (ACV × Reps) ÷ Win Rate ÷ Coverage Ratio
- Example: ($50K × 20) ÷ 0.25 ÷ 3 = 13,333 SAOs needed per year = 1,111 per month

**Step 7: Calculate cost**
- Sales rep fully loaded cost: $150-250K depending on segment (SMB lower, enterprise higher)
- Sales operations, tools, training: 30-40% on top
- Total sales org cost = Reps × Fully loaded cost
- Example: 20 reps × $200K × 1.35 = $5.4M in sales costs for $5M revenue (not sustainable)
- This is why you need: higher ACV, higher win rate, shorter cycle, or higher CAC:LTV ratio

---

## Part 6: Sales Process Anti-Patterns

### Anti-Pattern 1: No Documented Sales Process

**Symptom:** Each rep does it differently. No two deals follow the same process. Can't forecast.

**Why it fails:** Unpredictable results, hard to onboard new reps, can't optimize.

**Fix:** Document the exact process. Stage gates. Exit criteria. Tools. It should be teachable.

### Anti-Pattern 2: Sales Process Doesn't Match Customer Journey

**Symptom:** Sales process has 7 stages but customers want to buy in 3 steps. Or you're gate-keeping discovery when customers self-educate online first.

**Why it fails:** Friction. Lost deals.

**Fix:** Map the customer journey independently of sales process. Design sales process to fit how customers buy.

### Anti-Pattern 3: No Definition of "Qualified"

**Symptom:** Any lead goes to sales. Reps waste time on unqualified prospects. Pipeline is padded.

**Why it fails:** Wrong CAC, wrong win rate, demoralized reps.

**Fix:** Explicit qualification criteria (BANT: Budget, Authority, Need, Timeline. Or PITA: Pain, Intent, Timeline, Authority). Train on it. Hold reps accountable.

### Anti-Pattern 4: Sales-Marketing Misalignment

**Symptom:** Marketing hands off poor-fit leads. Sales says "these aren't ready." Finger-pointing.

**Why it fails:** Bad unit economics, missed revenue, internal conflict.

**Fix:** Marketing-sales SLA. Explicit definition of MQL. Regular reviews. Adjust lead criteria or marketing spend based on data.

---

## Quality Gates for Sales Motion Design

Before executing:

1. **Can you describe the sales process in 5 minutes without slides?** (If not, it's not clear)
2. **Do you have actual customers to learn from?** (Interview 3-5 recent customers about their buying journey)
3. **Is the sales cycle realistic for your product?** (Validate: ask your champion "how long did this take?")
4. **Do your reps understand why each stage exists?** (Not just following steps)
5. **Have you identified the biggest bottleneck?** (Long eval stage? Procurement delays? Low qualification?) Fix that first.
