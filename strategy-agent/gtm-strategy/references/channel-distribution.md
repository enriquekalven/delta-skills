# Channel & Distribution Strategy

## Purpose & Scope

This reference answers: How do we reach customers? Direct sales, indirect (channel partners), marketplaces, or hybrid? How do we structure partner programs? What's the economics by channel?

Distribution is force multiplication. Selling through 100 partners reaches more customers than 10 direct salespeople. The tradeoff: less control, margin sharing, partner dependency. Design the channel mix strategically.

---

## Part 1: Channel Strategy Framework

### The Channel Decision Matrix

Different channels have different characteristics. Choose based on your ICP, ACV, sales cycle, and margin tolerance.

| Dimension | Direct Sales | Channel/Reseller | Marketplace | Hybrid |
|-----------|--------------|------------------|-------------|--------|
| **Control** | High | Low | Medium | Medium |
| **Speed to Scale** | Slow (hiring) | Fast (partners) | Fast (listing) | Medium |
| **Margin** | 70%+ | 30-50% (partner margin) | 30-50% (platform cut) | Varies |
| **CAC** | High | Low (partners have warm relationships) | Variable | Medium |
| **Best For** | Complex, high-ACV deals | Broad TAM, established partnerships | Horizontal products, SMB | Most B2B SaaS |
| **Execution Complexity** | Medium | High (partner management) | Low (platform handles) | High |

### Four Channel Archetypes

#### 1. **Direct Sales**
You own the customer relationship end-to-end.

**When it works:**
- High ACV (>$50K) justifies sales headcount
- Complex, consultative buying process
- Need to control customer experience and expand account
- Small enough TAM that you can reach it with internal team

**Structure:**
- Inside sales team (outbound, inbound, light-touch)
- Field sales team (enterprise, on-site meetings)
- Sales engineers (technical evaluation, proof of concept)

**Unit economics:**
- CAC: $20-100K (depending on ACV, cycle, win rate)
- Typical quota: $200K-$1M per rep per year
- Need 3:1 pipeline-to-close ratio

#### 2. **Channel (Reseller/Partner)**
Partners sell on your behalf, take margin, handle implementation/support.

**When it works:**
- TAM is too broad for direct sales to reach
- Partners have existing customer relationships (warm leads)
- Implementation or customization needed (partners specialize in that)
- Geographic expansion without hiring local teams
- Customers prefer to buy from trusted local vendor

**Partner Types:**
- **Resellers:** Buy from you, resell to end customer at markup. Own customer relationship, support, implementation. Pros: incentivized (their margin is their motivation); cons: less control, brand dilution risk
- **Integrators/Consultants:** Don't resell, but recommend and integrate your product for their customers. Pros: high-touch, consultative; cons: no revenue from resale, harder to incentivize
- **ISV (Independent Software Vendors):** Embed your product into their product, resell as integrated solution. Pros: high-value integrations, scale; cons: complex technical integration, revenue share negotiation
- **MSP (Managed Service Provider):** Manage and support your product for customers. Pros: recurring revenue, customer success; cons: less control over customer experience
- **Affiliate:** Lightweight partnership where partners recommend you, get commission per customer. Pros: low friction, scale; cons: low commitment, poor quality often

**Unit economics:**
- CAC: Low (partners already have relationships)
- Margin: Split between you and partner (e.g., you get 50%, partner gets 50% of customer revenue)
- Partner costs: Training, enablement, co-marketing, tools, partner management
- Complexity: Managing 10 partners requires almost as much effort as managing 50 direct customers

#### 3. **Marketplace**
Third-party platform (AppStore, AWS Marketplace, Salesforce AppExchange) handles discovery, billing, trust.

**When it works:**
- Product solves a non-core problem for the marketplace user (e.g., Salesforce integration for Salesforce users)
- SMB/mid-market customers (self-serve, low CAC)
- Horizontal product (applies across many industries)
- Don't have distribution advantage (equal playing field on marketplace)

**How it works:**
- You list your product on marketplace
- Customers discover, try, and buy through platform
- Marketplace takes 30-50% cut
- You manage support, updates, customer relationship

**Challenges:**
- Discovery is hard (thousands of apps, yours is hidden)
- Organic lift is minimal; you need to drive traffic through ads or marketing
- Dependency (platform can change terms, remove you, prioritize competitors)
- Customer relationship is platform's, not yours (you don't get email, can't upsell directly)

**Unit economics:**
- CAC: Can be very low (marketplace handles discovery)
- Margin: 50-70% (after marketplace cut)
- Success depends on: quality (high ratings), reviews (proof social), continuous updates (algorithmic boost)

#### 4. **Hybrid**
Combination of direct + channel + marketplace, where each channel serves different customer segments.

**Example:**
- Enterprise (>$1M potential): Direct sales
- Mid-market ($100-500K): Channel partners or direct inbound
- SMB (<$50K): Marketplace + self-serve + freemium
- Geographic regions: Channel partners (Asia, Europe); direct (US)

**Why hybrid works:**
- Each segment gets the right sales motion
- Enterprise gets white-glove service; SMB gets low-touch
- If one channel stutters, others carry the load
- Revenue mix is more stable

---

## Part 2: Building a Channel Partner Program

If you decide to go channel, design the program explicitly.

### Phase 1: Partner Selection

Not all potential partners are good fits. Choose strategically.

**Ideal Partner Profile (for Resellers):**
- Existing customer relationships in your ICP
- Complementary offering (what they sell doesn't conflict with you)
- Reputation for customer service (they represent your brand)
- Sales/delivery capability (not just a name on a contract)
- Commitment (willing to invest in training, sales enablement)

**Red Flags:**
- Too many product lines (you'll be deprioritized)
- No relationships in your target segment
- History of bad customer satisfaction
- Just wants to add you to their portfolio (low commitment)

**Discovery:**
- Industry analyst reports (Forrester, Gartner report top partners)
- Customer referrals ("who did you buy from?")
- Trade shows (who's in your booth ecosystem?)
- LinkedIn/web search (companies selling similar solutions, check their partners)
- Existing customers (ask "who did you already work with for similar projects?")

### Phase 2: Program Design

Document the entire program:

```
CHANNEL PARTNER PROGRAM
═══════════════════════════════════════

PROGRAM TIERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Tier Name] (Entry requirements)
  Margin: [X]% for each customer sold
  Support: [What we provide]
  Requirements: [What they commit to]
  Incentives: [Bonus structure, co-marketing]

Example:
Silver Partner (First 3 customers closed)
  Margin: 30%
  Support: Email support, quarterly training, marketing assets
  Requirements: Sell 3 customers in year 1
  Incentives: Silver badge, case study co-marketing, joint webinar

Gold Partner (10+ customers closed, $500K ARR)
  Margin: 35%
  Support: Dedicated partner manager, bi-weekly training, co-selling opportunities
  Requirements: Sell 10+ customers/year, maintain 90%+ gross retention
  Incentives: Gold badge, co-marketing, partner community

Platinum Partner (50+ customers closed, $2M+ ARR)
  Margin: 40% or revenue share
  Support: Executive relationship, co-planning, co-selling, enablement budget
  Requirements: Named commitment to your solution, dedicated team
  Incentives: Exclusive territory/vertical, co-marketing budget, board presentation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PARTNER ECONOMICS
  Gross Margin: [X]% (you keep this, partner makes theirs from professional services)
  Partner Margin: [X]% (partner keeps this)
  Payment Terms: [When partners pay, when they get paid by customers]
  MRR vs. Perpetual: [If monthly, do you hold the customer relationship and risk?]

ENABLEMENT
  Onboarding: [2-day in-person, 3-week virtual, self-paced online?]
  Sales Training: [How to discover, qualify, demo, negotiate]
  Product Training: [Architecture, features, how to troubleshoot]
  Marketing Assets: [Case studies, data sheets, slide decks, email templates]
  Sales Tools: [Pricing guide, objection handling, competitive positioning]
  Ongoing Support: [Email? Slack? Dedicated person? Response time?]

EXPECTATIONS
  Forecast: [Partners commit to quarterly/annual forecast]
  Growth: [Expected growth rate (e.g., 20% YoY)]
  Quality: [Customer satisfaction targets, churn expectations]
  Communication: [Weekly, monthly, quarterly check-ins]
  Exclusivity: [Can partners sell competitors' products?]

GOVERNANCE
  Partner Manager: [Person responsible for each partner]
  QBR (Quarterly Business Review): [Quarterly performance review + planning]
  Escalation: [What issues escalate, who handles]
  Termination: [Conditions for ending partnership, notice period]

CONFLICT RESOLUTION
  Territory: [Do partners have exclusive geography/vertical?]
  Channel Conflict: [What if you sell direct to their customer?]
  Pricing: [Can partners offer discounts? What's the floor?]
  Support: [If customer isn't happy, who handles?]
═══════════════════════════════════════
```

### Phase 3: Partner Enablement

Poor enablement = poor sales. Invest in partner success upfront.

**Minimum Enablement Package:**
1. **Sales Playbook** (20 pages)
   - How to discover pain (conversation guide)
   - How to position (vs. competitors, vs. alternatives)
   - How to demo ( 15-min, 45-min, deep-dive versions)
   - How to objection-handle (top 10 objections)
   - Deal structure (pricing, terms, contract)

2. **Product Training** (2 days)
   - Product architecture (under the hood)
   - Features deep-dive (every feature, when to use)
   - Troubleshooting common issues
   - How to escalate to your team

3. **Marketing Assets**
   - Case studies (3-5 from similar customer types)
   - Data sheets and one-pagers
   - Email templates for outreach
   - LinkedIn posts, social templates
   - Competitive positioning (vs. top 3 competitors)
   - ROI calculator (show customer impact)

4. **Tools & Systems**
   - Partner portal (where they access materials, training, submit forecasts)
   - CRM integration (tracking partner pipeline)
   - Deal registration (partners register opportunities to get credit)
   - Co-selling tools (you can join their calls remotely if needed)

### Phase 4: Partner Management

The hard part: ongoing management.

**Quarterly Business Reviews (QBRs):**
- Review last quarter: Customers closed, pipeline, win/loss
- Forecast next quarter and year
- Identify bottlenecks (product, support, sales enablement, customer success)
- Plan go-forward (marketing, co-selling, training)
- Adjust tier/incentives if performance warrants

**Tiering Enforcement:**
- Tiers should have real consequences (Silver does NOT get Platinum support)
- Tiers should be motivational (path to higher tier is clear)
- Tier migration should be automatic (hit the metrics, you advance)

**Red Flags (Address Immediately):**
- Partner gets deals but customer churn is high (quality issue)
- Partner talks to competitor (commitment issue)
- Partner doesn't invest in your product (laziness or deprioritization)
- Pipeline forecast is wildly wrong (forecast quality issue)

**Churn & Replacement:**
- Some partners will underperform or leave
- Have a pipeline of new partners to recruit
- Exit non-performing partners gracefully
- Don't be dependent on any one partner (if it's 50%+ of channel revenue, diversify)

---

## Part 3: Marketplace Strategy

If you're listing on a marketplace, design intentionally.

### Which Marketplaces to Enter?

Not all marketplaces are equal. Prioritize.

**Marketplace attractiveness score:**
- TAM in marketplace: How many potential customers use this platform? (Salesforce AppExchange: 100K+ customers. Smaller marketplace: 10K)
- Customer overlap: What % of your target ICP uses this platform?
- Competition: How many similar products are listed? (5 vs. 500 is a big difference)
- Search volume: Can customers find you? (Good SEO in marketplace = discovery)
- Conversion rate: What % of visitors convert to trial/paid? (Varies by marketplace)

**High-priority marketplaces:**
- Salesforce AppExchange (if you integrate with Salesforce)
- AWS Marketplace (if you serve AWS customers)
- Microsoft Azure Marketplace (if you serve Microsoft customers)
- Vertical marketplaces (e.g., HubSpot App Marketplace for HubSpot integrations)

**Lower-priority marketplaces:**
- Generic app marketplaces (discovery is hard)
- Vertical marketplaces in vertical you don't serve
- Marketplaces with low customer overlap

### Marketplace Organic Growth Levers

**Lever 1: Quality & Reviews**
- High product quality = high ratings
- High ratings = algorithmic boost in search
- Ratings compound (higher ranking = more visibility = more reviews)
- Target: 4.5+ stars on any marketplace. Below 4.0 is a serious problem.

**Lever 2: Continuous Updates**
- Active development = algorithmic signals (platform prioritizes maintained apps)
- Regular bug fixes and feature releases
- Good changelog (customers see you're actively improving)
- Frequency: Monthly minimum updates; quarterly is better

**Lever 3: Customer Reviews & Social Proof**
- Ask happy customers to leave reviews
- Respond to all reviews (positive and negative)
- Negative reviews are opportunities (show you listen, fix issues)
- User community (forums, Discord, Slack) = organic advocates

**Lever 4: SEO & Searchability**
- Marketplace has internal SEO (keywords, description matter)
- Choose keywords customers search for ("Salesforce integration," "contact sync," not your brand)
- Optimize description for keywords (but not keyword stuffing)
- Example: "Sync contacts from X to Salesforce" > "X Integration"

### Marketplace Paid Growth Levers

Organic growth is slow. Most successful marketplace sellers also drive paid traffic.

**Lever 1: Marketplace Ads**
- Some marketplaces (AWS, Azure, Salesforce) offer paid placement
- Cost: CPC or CPM varies by marketplace
- ROI: Convert marketplace visitor → trial → paid customer
- Typical CAC: $500-5K depending on conversion

**Lever 2: Demand Generation Outside Marketplace**
- Google Ads: "X Salesforce integration" (send to marketplace page, not your website)
- Content marketing: Blog posts that rank for keywords, link to marketplace
- Email: If you have existing users, tell them about marketplace version
- Community: Reddit, forums, Slack communities where prospects hang out

**Lever 3: Co-Marketing with Marketplace Owner**
- Some platforms (Salesforce, HubSpot) feature new apps
- Getting featured = visibility boost
- Requirements vary (build feature, case study, beta participation)

### Marketplace Unit Economics

**Typical scenario:**
- Product: $99/month subscription
- Marketplace takes: 30% ($29.70)
- You get: $69.30/month
- CAC to acquire customer (via ads + organic): $500
- Payback: $500 ÷ $69.30 = 7.2 months
- 12-month LTV: $69.30 × 12 = $831.60
- If churn is 5% monthly, LTV is lower

**Breakeven rule:** Marketplace CAC must be <3x monthly price.
- If price is $99/month and you're paying $500 CAC, you need 5 months to break even
- If you can't achieve 70%+ retention by month 5, you're losing money

---

## Part 4: Distribution Cost Modeling

Model the full cost by channel to understand true CAC and profitability.

### Direct Sales Cost Model

```
DIRECT SALES COST (Annual)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sales Team
  10 AE @ $200K fully loaded: $2,000,000
  1 Sales Manager @ $250K: $250,000
  Sales Support (ops, admin): $200,000
  Total Sales Team: $2,450,000

Sales Development Team (SDRs)
  5 SDRs @ $100K fully loaded: $500,000
  1 SDR Manager: $100,000
  Total SDR: $600,000

Sales Operations
  Tools (Salesforce, Outreach, etc.): $150,000
  Stack (meeting software, analytics): $50,000
  Total Tools: $200,000

Sales Development (Demand Gen)
  Content, email, events: $500,000

Total Sales & Marketing Cost: $3,750,000

Revenue Target: $15,000,000 ARR (from sales channel only)
CAC (fully loaded): $3,750,000 ÷ 150 customers = $25,000 per customer

Assuming $100K ACV: CAC is 25% of ACV. Breakeven if customer stays >3 months.
Assuming 80% gross margin: Gross profit per customer = $80,000. Payback = 3.75 months. ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Channel Partner Cost Model

```
CHANNEL PARTNER PROGRAM COST (Annual)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Partner Team
  2 Partner Managers @ $150K: $300,000
  Partner Operations (enablement, systems): $150,000
  Total Partner Team: $450,000

Partner Enablement & Marketing
  Sales playbooks, training: $100,000
  Co-marketing budget (shared with partners): $200,000
  Partner portal/systems: $50,000
  Total Enablement: $350,000

Channel Margin Loss
  10 partners, 20 customers closed per partner = 200 customers
  $100K ACV × 200 customers = $20,000,000 revenue
  Partner margin (if 35% partner take): $7,000,000 to partners
  Company margin loss vs. direct: $7,000,000

Total Channel Cost: $450,000 operations + $350,000 enablement + $7,000,000 margin loss
                  = $7,800,000

Revenue from Channel: $20,000,000 ARR
CAC (fully loaded): $7,800,000 ÷ 200 customers = $39,000 per customer

BUT: This is expensive CAC, BUT you're closing 200 customers (vs. 30 with direct sales of $2.45M budget)
Scale advantage: You're building 200-customer business, not 30-customer business, with only 3x cost
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Marketplace Cost Model

```
MARKETPLACE COST (Annual)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Marketplace Management
  Partner manager (0.5 FTE): $75,000
  Marketplace updates/optimization: $50,000
  Total: $125,000

Marketplace Ads & Promotion
  Paid placement: $200,000
  Paid traffic (Google Ads to marketplace): $200,000
  Co-marketing budget: $50,000
  Total: $450,000

Marketplace Revenue (Example)
  200 customers acquired through marketplace
  $99/month = $1,188/year per customer = $237,600 annual
  Marketplace takes 30%: $71,280 to platform
  Company revenue: $166,320

Wait, that's only $237K revenue from marketplace. Not worth it at this scale.

Now scale it:
  5,000 customers acquired through marketplace (Slack example)
  $100/month = $1,200/year per customer = $6,000,000 annual
  Marketplace takes 30%: $1,800,000 to platform
  Company revenue: $4,200,000
  Blended CAC: $575,000 cost ÷ 5,000 customers = $115 CAC
  ROI: 5,000 customers × $100/month × 12 months = $6M revenue
        vs. $575K cost = 10x ROAS

Takeaway: Marketplaces only work at scale (1000+ customers).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Part 5: International Distribution

Selling globally requires different channels by region.

### By Region

**North America:**
- Direct sales (large ACV, complex)
- Inbound (strong demand)
- Marketplace (AWS, Salesforce has large user bases)

**Europe:**
- Channel partners (large, complex, many local languages)
- Direct (UK, Germany, France have large economies)
- Distribution partners (for GDPR, data residency requirements)

**Asia-Pacific:**
- Channel partners (relationships are critical; local presence required)
- Local subsidiaries (if large market like China, Japan)
- Marketplace (limited; often have regional competitors)

**Latin America, Middle East, Africa:**
- Distribution partners (with local support, language)
- Avoid direct unless >$50M ARR and dedicated team

### Considerations by Region

- **Language:** Do you localize product and sales materials? (High cost: ~10% of revenue)
- **Data residency:** Does region require data stored locally? (GDPR, CCPA, China data laws)
- **Payment:** Do local payment methods work? (ACH in US, SEPA in EU, local methods in Asia)
- **Support:** Do you have local support team? Or 24-hour support in headquarters timezone?
- **Partner taxation:** Tax implications of partner channel vs. direct subsidiary

---

## Quality Gates for Channel Strategy

Before committing to a channel:

1. **Do you have 3 potential partners identified?** (If not, channel won't work; too few options)
2. **Have you interviewed them?** ("Are you interested? Can you reach our ICP? What margins do you need?")
3. **Can you model profitability by channel?** (Know the CAC, margin, and payback period)
4. **Is channel commitment resource-matched?** (Can you dedicate partner manager? Support team?)
5. **Do you have direct sales model working first?** (Don't use channel to learn how to sell; learn direct first)
6. **Is your product + integration + support good enough for partners to succeed?** (If you can't support partners, they'll fail)
