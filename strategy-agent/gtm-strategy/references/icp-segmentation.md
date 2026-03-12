# ICP & Segmentation Strategy

## Purpose & Scope

This reference defines the Ideal Customer Profile (ICP), identifies addressable market segments, and designs the buying committee map. The output is a crystal-clear answer to "who should we chase?" without wasting effort on bad-fit customers.

An ICP is not a wish list. It's a customer archetype based on your product's actual value, built from evidence (existing best customers, market research, win/loss analysis).

---

## Part 1: ICP Development Methodology

### The Four Dimensions of ICP

An ICP is never one-dimensional. It describes customers across four lenses:

#### 1. Firmographic (Company Profile)

The objective facts about the business:
- **Industry/Vertical** (SaaS, healthcare, financial services, manufacturing, etc.)
- **Company size** (revenue, employees, market cap)
- **Geography** (countries, regions served)
- **Stage** (pre-seed, early growth, scaling, mature, public)
- **Business model** (B2B SaaS, B2C, marketplace, services, hardware, hybrid)
- **Ownership** (founder-led, VC-backed, private equity, public)

**Example:**
Mid-market SaaS companies ($10-100M ARR) in North America, Series B-C stage, selling vertical software (healthcare, legal, financial).

#### 2. Technographic (Technology Stack)

The tools and infrastructure they use:
- **Tech stack composition** (what systems they run: Salesforce, HubSpot, Workday, custom, legacy)
- **Infrastructure** (cloud: AWS/Azure/GCP vs. on-prem, hybrid)
- **Data maturity** (manual spreadsheets, basic BI, advanced analytics)
- **Integration capability** (API-ready, middleware, closed ecosystem)
- **Spending appetite** (technical debt burden, capex vs. opex orientation)

**Why it matters:** If your product requires cloud infrastructure, on-prem manufacturers aren't a fit. If you integrate deeply with Salesforce, Salesforce-less companies won't buy.

**Example:**
Cloud-first companies running on AWS/Azure, using Salesforce for CRM, wanting API-native integrations. Companies locked into legacy on-prem systems are bad fits.

#### 3. Psychographic (Company Culture & Decision-Making)

How the organization thinks and decides:
- **Growth orientation** (conservative/steady vs. hypergrowth)
- **Innovation appetite** (early adopters vs. wait-and-see)
- **Risk tolerance** (proven vendors vs. willing to bet on new solutions)
- **Decision speed** (nimble, small teams vs. heavy process/procurement)
- **Buyer persona maturity** (exists vs. doesn't exist)

**Example:**
Founder-led or VP-led organizations (not massive matrixed companies) with fast decision-making. Growth companies reinvesting profits or raising capital. Early adopter mentality.

#### 4. Behavioral (How They Buy & Consume)

Observable patterns in how they engage:
- **Problem awareness** (customer-initiated discovery vs. need to educate)
- **Evaluation style** (self-serve trial vs. requires hands-on demo)
- **Procurement friction** (one-click vs. 6-month vendor evaluation)
- **Usage pattern** (highly engaged, low engagement, power users)
- **Expansion potential** (single seat vs. org-wide, upgrades, adjacent products)

**Example:**
Customers who onboard and get value within 7 days (not 3-month implementations). Companies that expand usage after initial deployment. Self-serve trial completers who move to paid.

### Building ICP from Evidence

Never guess. Build from your best customers:

**Step 1: Identify your best customers (not biggest)**
- Rank by: lifetime value, net revenue retention (expansion %), churn risk (low), NPS (high), time-to-value
- Pull the top 20% and bottom 20% to contrast
- Interview them: why they bought, what problems you solved, how they're using it, would they recommend

**Step 2: Find the pattern**
Across your best customers, what's consistent?
- Do they all come from 3 industries? (Industry pattern)
- Are they all scaling companies? (Stage pattern)
- Do they all run on cloud? (Tech pattern)
- Are they all <100 employees? (Size pattern)

**Step 3: Validate the pattern**
- Can you describe a best customer in one paragraph?
- If you met a company matching that description, would you want to win them? (If no, ICP is wrong)
- Can your sales team recognize an ICP fit in 5 minutes? (If not, ICP is too vague)

**Step 4: Define anti-patterns (what not to pursue)**
- Which customer segments consistently underperform?
- What reasons show up in churn? (Implementation failures, feature mismatches, procurement complexity, low usage)
- Your ICP definition should explicitly exclude these.

---

## Part 2: Segment Attractiveness Scoring

Once you have an ICP, break it into segments. Not all companies in the ICP are equally valuable.

### Segment Definition

A segment is a subset of the ICP differentiated by one or two variables:
- By industry vertical (vertical SaaS companies targeting healthcare vs. legal vs. financial)
- By company size (SMB vs. mid-market vs. enterprise)
- By buying model (land-through-self-serve vs. land-through-sales vs. land-through-channel)
- By use case (single-use case: compliance, vs. multi-use case: operations platform)
- By geo (North America vs. Europe vs. APAC)

### Attractiveness Scoring Matrix

Score each segment 1-10 on these dimensions. Weight based on your constraint:

| Dimension | Scoring Criteria | Weight |
|-----------|-----------------|--------|
| **Market Size** | TAM in segment (addressable by you) | 20% |
| **Growth Rate** | YoY growth rate of segment | 15% |
| **Fit Strength** | % of segment matching your ICP exactly | 15% |
| **Willingness to Pay** | ACV potential in segment | 20% |
| **Competitive Intensity** | # of direct competitors, price pressure | 15% |
| **Acquisition Feasibility** | CAC to win in segment, channels available | 15% |

**Calculation:**
```
Attractiveness Score = (Market Size × 0.20) + (Growth × 0.15) + (Fit × 0.15)
                     + (WTP × 0.20) + (Competition × 0.15) + (Feasibility × 0.15)
```

**Interpretation:**
- **8-10: Green Light Segments** — Size, growth, fit, and feasibility align. Prioritize here.
- **6-7: Amber** — Good opportunity but resolve one constraint (e.g., high competition, lower WTP)
- **<6: Red Light** — Either too small, too competitive, or poor product fit. Avoid.

### Segment Prioritization

Rank segments by attractiveness score. For Phase 1 (launch or repositioning), focus on:
1. Highest attractiveness score
2. Can be won with existing product (no feature builds required)
3. Can be reached with available sales/marketing motion
4. Have existing customers or warm leads to prove

---

## Part 3: Buying Committee Mapping

Who decides? Understanding the buying committee is critical for sales motion design.

### The Six Buyer Roles

Not all companies have all roles, but understanding who you need to influence matters:

#### 1. **Champion** (Internal advocate, usually end user)
- **Who:** The person who will use the tool daily, felt the pain acutely
- **Motivation:** Solve a problem they're experiencing, get recognized for improvement
- **Challenge:** May lack budgetary power; needs help "selling" internally
- **How to work with them:** Early engagement, product training, help them build internal business case

#### 2. **Economic Decision Maker** (Has budget authority)
- **Who:** VP, Director, or C-level (CFO, CRO, COO, CMO) depending on purchase
- **Motivation:** ROI, cost reduction, revenue impact, risk mitigation
- **Challenge:** Distant from the problem; may not understand product value deeply
- **How to work with them:** Business case, benchmarking (what others pay), risk analysis

#### 3. **Technical Evaluator** (Needs to sign off on capability)
- **Who:** CTO, VP Engineering, Head of Infra, or their delegate
- **Motivation:** Integration feasibility, security, scalability, vendor viability
- **Challenge:** Will find reasons to say no (not enough enterprise features, no audit logs, poor API)
- **How to work with them:** Technical depth, security certifications, architecture documentation, reference customers with similar setup

#### 4. **Procurement/Legal** (Controls buying process)
- **Who:** Procurement officer, contracts attorney, legal department
- **Motivation:** Enforce company policy, mitigate legal risk, negotiate best terms
- **Challenge:** Slows deals down, may require SOC 2, standard terms, DPA
- **How to work with them:** Standard contracts, certifications ready, clear negotiation parameters set before engaging

#### 5. **Influencer** (Advises without authority)
- **Who:** Department head, consultant, analyst firm the company trusts
- **Motivation:** Professional reputation, technical correctness, vendor independence
- **Challenge:** Can tank deals even without authority ("we looked at this vendor and recommend against")
- **How to work with them:** Analyst relations, research, advisory boards, technical credentials

#### 6. **Blocker** (Can kill the deal)
- **Who:** Someone who competes with the purchase (e.g., owner of legacy system), dislikes change, has veto power
- **Motivation:** Protect their role, budget, status quo
- **Challenge:** Won't engage openly; works behind scenes
- **How to work with them:** Understand their concern early, design solution that doesn't displace them, involve early

### Buying Committee Mapping by Segment

Different customer segments have different buying committees:

**SMB (Under $10M revenue):**
- Buyer: Founder, CEO, VP (often all one person)
- Technical: May not have dedicated tech person
- Procurement: Usually none; CEO decides
- Committee size: 1-2 people

**Mid-Market ($10-100M revenue):**
- Buyer: VP or Director of relevant function
- Technical: Dedicated tech team or CTO
- Procurement: Often has basic procurement process
- Committee size: 3-5 people
- Sales cycle: 3-6 months typical

**Enterprise ($100M+ revenue):**
- Buyer: SVP/C-level depending on impact
- Technical: Multiple evaluation teams (security, infrastructure, architecture)
- Procurement: Formal process, RFx, standard terms negotiation
- Committee size: 5-10+ people
- Sales cycle: 6-12+ months

**Public Company (Any size):**
- Buyer: Board-visible contracts need finance/legal review
- Technical: Extensive evaluation, procurement, audit trails
- Procurement: Formal vendor management process
- Committee size: Often 10+ people
- Sales cycle: 9-18 months

---

## Part 4: Account Tiering & Differentiated Approach

Not all accounts should receive the same sales motion. Design tiering based on revenue potential and sales effort.

### Three-Tier Model

#### **Tier 1: Enterprise (Strategic)**
- **Criteria:** $500K+ ACV, complex implementation, long sales cycle, multi-department impact
- **Sales Motion:** Account-based marketing (ABM), dedicated enterprise account executive, executive sponsor, custom ROI case studies
- **Sales Cycle:** 6-12 months
- **Success Metrics:** Close rate >30%, CAC Payback <18 months
- **Example:** Fortune 500 companies, large VC-backed scaling startups, government contracts

#### **Tier 2: Mid-Market (Growth)**
- **Criteria:** $50-500K ACV, standard implementation, 3-6 month sales cycle, 2-3 department buyers
- **Sales Motion:** Targeted inbound + outbound, inside sales team, product-focused demos, reference customers
- **Sales Cycle:** 3-6 months
- **Success Metrics:** Close rate >25%, CAC Payback <12 months
- **Example:** Growing SaaS companies, regional branches of larger enterprises, well-funded startups

#### **Tier 3: SMB (Velocity)**
- **Criteria:** <$50K ACV, self-serve or light-touch sales, 1-month sales cycle, one main buyer
- **Sales Motion:** Self-serve trial, low-touch sales, content-driven, community, partner channel
- **Sales Cycle:** <1 month
- **Success Metrics:** Close rate >20%, CAC Payback <6 months, high volume
- **Example:** Startups, small professional services, individual teams within larger companies

### Differentiated Approach Template

For each tier, document:

```
TIER: [Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Target ACV: $[X]
Typical Sales Cycle: [Z] months
Committee Size: [N] people

Positioning: [How we talk about our value to this tier]
Product Configuration: [Feature set, support level, customization]
Pricing: [Model and typical price range]
Packaging: [Do they get the standard tier or custom?]

Sales Motion:
  1. How they find us: [Inbound, outbound, channel, hybrid]
  2. Discovery process: [Length, who engages, proof points needed]
  3. Evaluation: [What do they need to see? POC? Reference? Demo?]
  4. Negotiation: [Are terms flexible? Discounts? Custom contracts?]

Success Criteria:
  - CAC: $[X] target
  - Win Rate: [X]% target
  - Sales Velocity: [X] days from first contact to close
  - Retention: [X]% target
  - Expansion: [What % expand to new seats/features?]

Example Playbook:
  Week 1: [Activity]
  Week 2-3: [Activity]
  Week 4: [Activity]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Part 5: Jobs-to-be-Done Integration

Don't just segment by firmographic. Understand the functional and emotional jobs customers are hiring you to do.

### Jobs Mapping

For each segment, identify the jobs:

**Functional Job:** "What task/outcome does this customer want?"
- Example: "Reduce time to deploy infrastructure from weeks to hours"

**Emotional Job:** "How do they want to feel?"
- Example: "Confident and empowered; not dependent on DevOps team"

**Social Job:** "How do they want to be perceived?"
- Example: "As a modern, efficient engineering leader"

### Using Jobs in Segmentation

Segments with the same job often respond to the same messaging, even if firm demographics differ.

**Example:**
- Large enterprise DevOps team (job: consolidate tools)
- Mid-market startup CTO (job: consolidate tools)
- Both have the same functional job, so same core value prop, but different:
  - Buying committee size
  - Implementation complexity
  - Budget negotiation

Segment by jobs first, then fine-tune by firmographics.

---

## Part 6: Anti-Patterns to Avoid

### ICP Anti-Pattern 1: Too Broad

**Bad:** "Any company using software that has budget"

**Why it fails:** Wastes sales effort on low-fit customers. No focus. High CAC, low win rate.

**Good:** "B2B SaaS companies $5-50M ARR in North America, Series A-C stage, selling into SMB/mid-market, with product-market fit but struggling with sales scaling. Running cloud infrastructure, using standard CRM/martech stack."

### ICP Anti-Pattern 2: Too Narrow

**Bad:** "Only Enterprise Fortune 500 companies spending $5M+ on procurement software"

**Why it fails:** If TAM is only 200 companies globally and you can only win 10% per year, you max out too early.

**Good:** "Enterprise companies ($100M+ revenue) with complex procurement needs + mid-market professional services firms ($10-50M) with distributed teams in procurement-heavy verticals."

### ICP Anti-Pattern 3: Wishful Thinking

**Bad:** "We want to sell to enterprise software companies because they have big budgets."

**Why it fails:** Want != fit. If your product requires 1-week implementations and enterprise deals take 6 months to evaluate, the fit is broken.

**Good:** "We're built for companies that value rapid deployment and self-service. That's founders, small-to-mid teams, and modern engineering orgs. Enterprise is a future play, not Phase 1."

### ICP Anti-Pattern 4: Ignoring Your Best Customers

**Bad:** Chasing a segment different from where you're already winning.

**Why it fails:** Ignores existing product-market fit. Double cost to acquire, longer sales cycles.

**Good:** "Our best customers are IT directors at 50-500 person tech companies. Let's keep winning more of those before expanding to enterprise IT."

---

## Part 7: Putting It Together — ICP Definition Template

```
IDEAL CUSTOMER PROFILE
═══════════════════════════════════════

ONE-SENTENCE DEFINITION
[Your product solves X problem for Y type of company]

FIRMOGRAPHICS
• Industries: [List 2-3 industries]
• Revenue/Size: [$ range or employee count]
• Stage: [Pre-seed, early growth, scaling, mature]
• Geography: [Where you sell]
• Business Model: [SaaS, services, hybrid, etc.]

TECHNOGRAPHICS
• Infrastructure: [Cloud, on-prem, hybrid]
• Key Systems: [CRM, data platform, ERP, etc.]
• Integration: [API-first preference, middleware, etc.]
• Maturity: [Data-driven, team maturity level]

PSYCHOGRAPHICS
• Growth Orientation: [Hypergrowth vs. steady]
• Innovation Appetite: [Early adopter vs. wait-and-see]
• Decision Speed: [Fast vs. heavy process]
• Risk Tolerance: [Willing to bet on new vendors]

BEHAVIORAL (How They Buy)
• Problem Awareness: [Self-identified pain vs. need to educate]
• Evaluation Style: [Self-serve trial vs. hands-on demo]
• Procurement: [1-click vs. 6-month process]
• Usage: [Engaged vs. low-touch]
• Expansion: [Single seat vs. org-wide]

BUYING COMMITTEE COMPOSITION
• Champion: [Who in the customer]
• Economic Buyer: [VP-level of what function]
• Technical Buyer: [What department/role]
• Procurement: [If applicable]
• Committee Size: [Typical range]

JOBS-TO-BE-DONE
• Functional: [What outcome do they need?]
• Emotional: [How do they want to feel?]
• Social: [How do they want to be perceived?]

WHERE YOU WIN
• Best Customer Examples: [Name 2-3 actual customers who match this ICP]
• Win Reasons: [Why they chose you]
• Expansion/Retention: [How they grow with you]

WHERE YOU LOSE
• Bad Fit Examples: [Companies you chased but lost or regret winning]
• Churn Patterns: [If any customers in this segment churn, why?]
• Implementation Failures: [What problems emerge post-sale?]

SEGMENT PRIORITIZATION (If multiple segments)
1. [Segment A] — Attractiveness Score: 8.5 — Target this first
2. [Segment B] — Attractiveness Score: 7.2 — Target after segment A
3. [Segment C] — Attractiveness Score: 6.1 — Explore only after dominance in A & B

ANTI-PATTERNS TO AVOID
• NOT: [What you're explicitly excluding]
• NOT: [What you're explicitly excluding]
═══════════════════════════════════════
```

---

## Quality Gates

Before accepting an ICP definition:

1. **Can you describe a best customer in 30 seconds without lists?** (If not, it's too complex)
2. **Do your top 3 customers match this ICP?** (If not, it's theoretical)
3. **Can your sales team recognize a fit in a discovery call?** (If not, it's not specific enough)
4. **Is there sufficient TAM in this ICP?** (If TAM is 100 companies globally, rethink)
5. **Can you reach these customers with available channels?** (If not, how will you change that?)
