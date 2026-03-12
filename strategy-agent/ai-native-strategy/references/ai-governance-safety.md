# AI Governance, Safety & Compliance (2026)

## Executive Summary

This reference covers AI governance and compliance frameworks needed for enterprise AI deployment. **Critical context**: EU AI Act compliance deadline is August 26, 2026 (5 months away). 90% of enterprises are unprepared.

**Key frameworks covered**:
1. EU AI Act compliance (HIGH PRIORITY)
2. AI risk assessment methodology
3. Responsible AI deployment checklist
4. Model evaluation and monitoring
5. Data governance for AI
6. Incident response playbook
7. Board-level governance structure

---

## PART 1: EU AI ACT COMPLIANCE FRAMEWORK

### The EU AI Act (August 26, 2026 Deadline)

**Scope**: Applies to all AI systems offered in the EU or affecting EU residents

**Compliance requirement**: By August 26, 2026, ALL high-risk AI systems must be compliant

### Risk Classification System

The EU AI Act classifies AI into 4 risk tiers:

#### Tier 1: Prohibited Risk (BAN)
**What**: AI use cases too dangerous to allow

**Examples**:
- Biometric surveillance/facial recognition (real-time, without consent)
- Emotional recognition in education or workplace
- Social scoring systems (China-style citizen scoring)

**Compliance**: DO NOT DEPLOY in EU. Ever.

**Enforcement**: Criminal penalties, substantial fines

---

#### Tier 2: High-Risk (ARTICLES 8-15)
**What**: AI systems with significant impact on people's rights

**Examples**:
- **Recruitment**: Resume screening, interview assessment
- **Credit/lending**: Loan approval, credit scoring
- **Law enforcement**: Predictive policing, suspect identification
- **Critical infrastructure**: Energy grid, transportation, power distribution
- **Border management**: Travel document verification
- **Education**: Automated student grading, progression

**Compliance Obligations** (Articles 8-15):
1. **Impact Assessment** (Article 19)
   - Document how AI affects rights
   - Identify bias, discriminatory risks
   - Plan mitigation
   - Cost: $50-200K per system (legal + external audit)

2. **Data Governance** (Articles 10-11)
   - Training data must be documented
   - Bias audit required
   - Data labeling specifications
   - Retention policy

3. **Technical Documentation** (Article 11)
   - How does the AI work?
   - What's its accuracy?
   - What are known limitations?
   - What testing was done?
   - 20-50 pages typical per system

4. **Testing and Performance Evaluation** (Article 15)
   - Accuracy on representative test set
   - Fairness across demographic groups
   - Robustness to adversarial inputs
   - Post-market surveillance plan

5. **Human Oversight** (Article 14)
   - Humans must be able to intervene
   - Humans must be trained
   - Human can override AI decision
   - Not fully autonomous

6. **Transparency** (Article 13)
   - Users must be informed AI was used
   - Clear explanation of decision
   - Right to contest decision

7. **Monitoring** (ongoing)
   - Track performance in production
   - Alert if accuracy drops >5%
   - Document incidents
   - Conduct quarterly audits

**Timeline**: Must be compliant by August 26, 2026

**Enforcement**: €30M fine OR 6% of global revenue (whichever is larger)

**Examples of fines** (if enforced like GDPR):
- Company $1B revenue: $60M fine
- Company $100M revenue: $6M fine

---

#### Tier 3: Limited Risk (ARTICLE 50)
**What**: AI systems that require transparency (mostly chatbots)

**Examples**:
- ChatGPT-style conversational AI
- Chatbots providing information
- Content recommendation systems

**Compliance Obligations**:
1. **Transparency** (Article 50)
   - Disclose that AI-generated content was produced by AI
   - Include in terms of use
   - User can verify AI was used

2. **Deepfake disclosure** (if applicable)
   - If AI-generated video/audio of real person
   - Must disclose before sharing

**Timeline**: August 26, 2026 (same date)

**Enforcement**: €10M fine OR 2% global revenue

**Note**: This is much easier than high-risk compliance

---

#### Tier 4: Low-Risk / Minimal Risk
**What**: Most AI systems

**Examples**:
- Email spam filters
- Recommendation systems (Netflix, Amazon, Spotify)
- Content moderation filters
- Analytics and reporting

**Compliance**: Minimal
- Just don't use prohibited techniques
- Responsible AI best practices
- Document what you're doing

**Enforcement**: None formal (implicit expectations)

---

### Risk Classification Decision Tree

```
Is your AI system used for ANY of these?
├─ Biometric surveillance, emotional recognition, social scoring → PROHIBITED
├─ Recruitment, lending, law enforcement, border, education → HIGH-RISK
├─ Chatbot, recommendation, content filtering → LIMITED-RISK
└─ Other (analytics, spam, general use) → LOW-RISK
```

### Risk Classification for Common Use Cases

| Use Case | Risk Level | Compliance Effort | Timeline |
|----------|-----------|---|---|
| **Customer service chatbot** | Limited | Low (transparency) | 2-4 weeks |
| **Resume screening** | High | High (impact assessment, bias audit) | 12-16 weeks |
| **Loan approval** | High | Very High (regulatory + AI compliance) | 16-20 weeks |
| **Employee monitoring** | High | Very High (privacy + fairness) | 16-20 weeks |
| **Content recommendation** | Limited | Low | 2-4 weeks |
| **Predictive policing** | High/Prohibited | Cannot deploy EU | N/A |
| **Internal analytics** | Low | Minimal | 1-2 weeks |

---

## PART 2: AI RISK ASSESSMENT METHODOLOGY (4x4 Matrix)

### Framework

**Risk = Likelihood × Impact**

### Likelihood Assessment

| Level | Definition | Probability |
|-------|-----------|---|
| **Very Low** | Extremely unlikely, requires multiple failures | 1-10% |
| **Low** | Unlikely under normal conditions | 10-30% |
| **Medium** | Moderately likely, reasonable possibility | 30-70% |
| **High** | Likely to occur in normal operations | 70-90% |
| **Very High** | Almost certain to occur | >90% |

### Impact Assessment

| Level | Definition | Example |
|-------|-----------|---------|
| **Critical** | Loss of life, criminal liability, >$100M loss | AI recommends wrong medication |
| **High** | Substantial harm, regulatory fine, $10-100M loss | Hiring AI systematically discriminates |
| **Medium** | Moderate harm, reputational damage, $1-10M loss | Chatbot gives wrong advice 5% of time |
| **Low** | Minor harm, fixable issue, <$1M loss | System downtime, needs restart |

### Risk Matrix

|  | Very Low Impact | Low Impact | Medium Impact | High Impact | Critical Impact |
|---|---|---|---|---|---|
| **Very High Likelihood** | Medium | High | **CRITICAL** | **CRITICAL** | **CRITICAL** |
| **High Likelihood** | Low | Medium | **HIGH** | **CRITICAL** | **CRITICAL** |
| **Medium Likelihood** | Low | Medium | High | **HIGH** | **CRITICAL** |
| **Low Likelihood** | Minimal | Low | Medium | High | **HIGH** |
| **Very Low Likelihood** | Minimal | Low | Low | Medium | High |

---

### Examples: AI Risk Assessment

**Example 1: Customer Service Chatbot**
- Likelihood chatbot makes mistake: HIGH (LLMs have ~10% hallucination rate)
- Impact of mistake: LOW (user can escalate to human)
- Risk: **MEDIUM**
- Mitigation: Escalation to human, monitoring, user feedback loop

**Example 2: Hiring Recommendation AI**
- Likelihood AI biases against protected group: MEDIUM (possible if training data biased)
- Impact of bias: **HIGH** (discrimination = legal liability, fairness issue)
- Risk: **HIGH**
- Mitigation: Mandatory impact assessment, bias audit, human review all recommendations, annual audit

**Example 3: Autonomous Vehicle**
- Likelihood of accident: MEDIUM (depends on road conditions, testing)
- Impact of accident: **CRITICAL** (loss of life)
- Risk: **CRITICAL**
- Mitigation: Extensive testing (millions of miles), redundancy, fallback to human, insurance

**Example 4: Email Spam Filter**
- Likelihood of misclassifying email: MEDIUM (spam filters are ~95% accurate)
- Impact of error: LOW (email goes to spam, user can recover it)
- Risk: LOW
- Mitigation: Allow user to recover from spam, flag important senders

---

## PART 3: RESPONSIBLE AI DEPLOYMENT CHECKLIST

### Data Governance

- [ ] **Training Data**
  - [ ] Source documented (where did data come from?)
  - [ ] Licensing reviewed (do we have rights to use it?)
  - [ ] Bias audit completed (third-party fairness review)
  - [ ] Retention policy defined (how long do we keep it?)
  - [ ] PII removed (no personal information in training data)

- [ ] **Test Set**
  - [ ] Representative of production (does test set look like real users?)
  - [ ] No distribution shift (test ≈ production)
  - [ ] Documented and versioned (reproducibility)

- [ ] **Data Privacy**
  - [ ] GDPR compliance (if EU data, meet GDPR requirements)
  - [ ] Differential privacy applied (if sensitive)
  - [ ] Access controls enforced (who can see data?)
  - [ ] Retention limits (delete after X months)

---

### Model Evaluation

- [ ] **Accuracy Metrics**
  - [ ] Primary metric defined (accuracy? F1? AUROC?)
  - [ ] Baseline established (vs. previous version, human performance)
  - [ ] Test set performance documented
  - [ ] Confidence intervals calculated

- [ ] **Fairness Metrics**
  - [ ] Disparate impact analysis done (accuracy different across groups?)
  - [ ] Demographic parity checked (equal outcomes for groups?)
  - [ ] Equalized odds evaluated (equal error rates across groups?)
  - [ ] Third-party bias audit completed (for high-risk systems)

- [ ] **Robustness Testing**
  - [ ] Adversarial examples tested (can the model be fooled?)
  - [ ] Edge cases identified (unusual inputs, rare conditions)
  - [ ] Domain shift tested (does model work on different data distribution?)

- [ ] **Explainability**
  - [ ] Model decisions explainable (SHAP, LIME, reasoning traces)
  - [ ] Feature importance documented (which features drive decisions?)
  - [ ] Failure modes identified (when does model fail?)

- [ ] **Safety Evaluation**
  - [ ] Hallucination rate measured (<5% for critical, <10% for non-critical)
  - [ ] Jailbreak testing done (can it be tricked into prohibited outputs?)
  - [ ] Prompt injection tested (if using LLM)
  - [ ] Toxicity/bias outputs detected and mitigated

---

### Safety & Boundaries

- [ ] **Hallucination Mitigation**
  - [ ] Retrieval-augmented generation (RAG) if needed
  - [ ] Fact-checking layer built in
  - [ ] Confidence scores provided
  - [ ] User training on model limitations

- [ ] **Jailbreak / Prompt Injection Prevention**
  - [ ] Input validation (check for adversarial prompts)
  - [ ] Output sanitization (remove harmful outputs)
  - [ ] Boundary examples in prompt ("do not answer X")
  - [ ] Regular red-team testing

- [ ] **Bounded Autonomy**
  - [ ] Autonomy level defined (0-4 scale, see governance section)
  - [ ] Human checkpoints defined (when must human approve?)
  - [ ] Escalation path clear (how does human override?)
  - [ ] Human training plan (staff know how to override)

---

### Monitoring & Operations

- [ ] **Live Monitoring Dashboard**
  - [ ] Accuracy metric tracked (dashboard updated hourly/daily)
  - [ ] Latency monitored (response time SLA)
  - [ ] Cost tracked (tokens/inference cost)
  - [ ] Error rate visible (failures per hour/day)
  - [ ] Hallucination tracking (detect false positives)

- [ ] **Alert Thresholds Set**
  - [ ] Accuracy drop >5% → Investigate, consider rollback
  - [ ] Latency >SLA by 50% → Scale up or optimize
  - [ ] Error rate >1% → Page on-call engineer
  - [ ] Cost spike >20% → Investigate, may indicate abuse
  - [ ] 5+ incidents in a week → Pause feature, debug

- [ ] **Incident Response**
  - [ ] Runbook documented (what to do if AI goes wrong)
  - [ ] Escalation path clear (who to notify, in what order)
  - [ ] Rollback plan in place (can revert to previous version)
  - [ ] Communication plan (who tells customers, what do we say)

- [ ] **Version Control**
  - [ ] Model versions tagged (can reproduce any version)
  - [ ] Data versions tracked (which version trained which model)
  - [ ] Prompt history maintained (prompt changes documented)
  - [ ] Rollback capability proven (tested, not theoretical)

---

### Legal & Compliance

- [ ] **EU AI Act Compliance** (if applicable)
  - [ ] Risk classification done (Prohibited / High / Limited / Low)
  - [ ] Impact assessment completed (for high-risk)
  - [ ] Bias audit commissioned (third-party, for high-risk)
  - [ ] Documentation package prepared (50-100 pages)
  - [ ] Human oversight designed (humans can intervene)

- [ ] **Data Processing Agreement**
  - [ ] DPA signed (with any third-party LLM vendors)
  - [ ] Data residency specified (where does data live?)
  - [ ] Data deletion guaranteed (vendor will delete on request)
  - [ ] Subprocessors disclosed (who has access to data?)

- [ ] **Intellectual Property**
  - [ ] Training data licensing reviewed
  - [ ] Copyright for AI-generated content addressed
  - [ ] Patent implications assessed (could we be infringing?)

- [ ] **Insurance**
  - [ ] Errors & Omissions (E&O) policy reviewed
  - [ ] AI coverage included (many policies exclude AI)
  - [ ] Coverage limits adequate ($1M? $10M? $100M?)
  - [ ] Disclosure made (tell insurer you're using AI)

---

### Governance & Oversight

- [ ] **Responsibility Assigned**
  - [ ] Owner named (who's accountable for this AI system?)
  - [ ] Escalation path defined (if problems arise)
  - [ ] Review cadence set (monthly? quarterly?)

- [ ] **Audit Trail**
  - [ ] Decisions logged (who approved this? When?)
  - [ ] Changes tracked (what changed, when, who approved?)
  - [ ] Incidents documented (what went wrong, how was it fixed?)
  - [ ] Retention policy (keep logs for X years)

- [ ] **Regular Reviews**
  - [ ] Monthly: Operational metrics (accuracy, latency, cost)
  - [ ] Quarterly: Performance audit (fairness, drift, edge cases)
  - [ ] Annual: Security review (vulnerability assessment)
  - [ ] Annual: Risk re-assessment (has risk profile changed?)

---

## PART 4: MODEL EVALUATION & MONITORING FRAMEWORKS

### Pre-Deployment Evaluation

**Phase 1: Functionality Testing**
- Does the model work at all?
- Core metrics: Accuracy, precision, recall, F1
- Test on representative data
- Baseline: How does it compare to previous version or human performance?

**Phase 2: Fairness & Bias Testing**
- Disparate impact analysis: Are error rates equal across demographic groups?
- Demographic parity: Are positive outcomes equal across groups?
- Equalized odds: Are false positives and false negatives equal across groups?
- Intersectionality: Test combinations (e.g., "Women in Tech field")

**Phase 3: Robustness Testing**
- Adversarial examples: Can the model be fooled by crafted inputs?
- Edge cases: Unusual but valid inputs
- Domain shift: Does the model work on different but related data?
- Stress testing: What happens with 10x traffic?

**Phase 4: Safety Testing**
- Hallucination: How often does the model make up facts? (<5% target)
- Jailbreak: Can the model be tricked into harmful outputs?
- Toxicity: Does the model output offensive content?
- Prompt injection: Can users manipulate the model via creative prompts?

---

### Production Monitoring

**Core Metrics Dashboard**:

| Metric | Target | Alert | Frequency |
|--------|--------|-------|-----------|
| **Accuracy** | Baseline | >5% drop | Hourly |
| **Fairness Gap** | <10% | >10% | Daily |
| **Latency (p95)** | <2s | >5s | Hourly |
| **Cost per Inference** | $0.05 | >$0.10 | Daily |
| **Error Rate** | <0.5% | >1% | Hourly |
| **Hallucination Rate** | <5% | >10% | Daily |
| **Incident Count** | 0 | >3/week | Weekly |

**Data Drift Monitoring**:
- Input distribution changing? (Monitor embedding drift)
- Label distribution shifting? (Are positive outcomes different?)
- New classes appearing? (Data looks different than training set?)

**Escalation Rules**:
- Accuracy drops >5% → Investigate root cause
- Fairness gap widens >10% → Risk assessment needed
- Cost spike >20% → May indicate abuse or inefficiency
- 5+ incidents in a week → Consider pausing feature

---

## PART 5: DATA GOVERNANCE FOR AI

### Training Data Governance

- [ ] **Documentation**
  - Source: Where does the data come from?
  - Collection date: When was it collected?
  - Curation: Who selected it? Any selection bias?
  - Size: How many examples?
  - Distribution: Balanced? Skewed?

- [ ] **Privacy & Security**
  - PII removed? (No names, SSNs, emails in training data)
  - Encryption in transit? (Data encrypted during collection/storage)
  - Access controls? (Who can see the data?)
  - Retention limits? (Delete after X months)

- [ ] **Licensing**
  - Do we have rights to use this data?
  - Commercial use allowed?
  - Attribution required?
  - Any restrictions?

- [ ] **Bias Assessment**
  - Demographic representation analyzed?
  - Underrepresented groups identified?
  - Mitigation strategy planned?
  - Third-party audit commissioned?

---

### Inference Data Governance

- [ ] **Collection Policy**
  - What data do we collect when AI is used?
  - How long do we keep it?
  - Who has access?
  - Can users request deletion?

- [ ] **Privacy Controls**
  - Differential privacy applied? (Add noise to prevent memorization)
  - Anonymization done? (PII removed)
  - Data minimization? (Collect only what's necessary)
  - Retention limits? (Delete after X days/weeks)

- [ ] **User Rights**
  - Right to access: Users can see what data we have about them
  - Right to delete: Users can request data deletion
  - Right to contest: Users can challenge AI decision
  - Transparency: Users know AI was used

---

## PART 6: AI INCIDENT RESPONSE PLAYBOOK

### Incident Classification

**Tier 1 (Low)**: Confusion, minor error
- Example: Chatbot gives confusing response
- Response: Monitor, log, fix in next release
- Communication: Internal only
- Timeline: Fix in 1-2 weeks

**Tier 2 (Medium)**: Functional issue causing user impact
- Example: AI-driven feature has 10% error rate
- Response: Pause feature, investigate, implement safeguards
- Communication: Notify affected users if applicable
- Timeline: Fix in 1-4 weeks

**Tier 3 (High)**: Serious issue with legal/reputational risk
- Example: Hiring AI systematically discriminates against protected group
- Response: Immediate pause, legal review, forensic analysis
- Communication: Executive brief, customer notification, regulatory notification if required
- Timeline: Fix in weeks, escalate to board

**Tier 4 (Critical)**: Loss of life, criminal liability, existential risk
- Example: Autonomous system executes unauthorized financial transaction
- Response: Immediate shutdown, executive + legal emergency
- Communication: Regulatory notification, customer notification, media (if unavoidable)
- Timeline: Immediate action, ongoing response

---

### Response Protocol

**Discovery (Minute 1)**
- Detect via:
  * Automated monitoring (alert triggered)
  * User report (customer calls)
  * Testing (caught in testing before launch)
  * Security review (auditor finds issue)

**Triage (Minute 5-15)**
- Classify tier (1-4)
- Identify owner (who owns this AI system?)
- Notify stakeholders (product, engineering, legal, risk)

**Containment (Minute 15-60)**
- If Tier 2+: Pause or throttle system
- Prevent spread: Limit scope of damage
- Preserve evidence: Capture logs, configuration, data
- Document: What happened, when, what we observed

**Root Cause Analysis (Hour 1-4)**
- Why did this happen?
  * Data issue? (Training data, inference data)
  * Model issue? (Hallucination, bias, edge case)
  * Prompt issue? (Instructions incomplete, ambiguous)
  * Integration issue? (Connected to wrong system, bad API)
  * Operator issue? (Misconfiguration, wrong threshold)

**Fix (Hour 4-48)**
- Implement solution:
  * Retrain model (if data issue)
  * Adjust prompt (if instructions issue)
  * Add safeguards (rule-based filters, additional checks)
  * Fix integration (correct connection, data flow)
  * Adjust thresholds (increase human review for edge cases)

**Validation (Hour 48-72)**
- Test fix doesn't introduce new problems
- Peer review (someone else validates fix)
- Dry-run testing (test in staging environment)

**Rollout (Day 3-7)**
- Staged rollout: Deploy to 10% of users, monitor
- If successful: Expand to 50%, then 100%
- If issues: Rollback to previous version
- Monitor for regression: Did we solve the problem?

**Communication (Ongoing)**

Tier 1-2: Notify product team, consider customer communication
Tier 3: Notify executives, legal, customer communication
Tier 4: Executive emergency, board notification, regulatory notification, media management

**Postmortem (Week 1-2)**
- What happened?
- Why did it happen?
- What systemic issue allowed it?
- How do we prevent this class of incident?
- What process changes needed?

---

## PART 7: BOARD-LEVEL AI GOVERNANCE STRUCTURE

### Board Committee Composition

**Risk Committee** (or new AI Governance Subcommittee)

Members:
- **Chair**: Chief Risk Officer (or CISO)
- **Chief Technology Officer**: Responsible for AI systems, architecture decisions
- **General Counsel**: Legal implications, regulatory compliance
- **Chief Compliance Officer**: Regulatory obligations, audit coordination
- **Independent board member with AI expertise** (if available; otherwise hire advisor)

Frequency: Quarterly minimum (every 3 months), more often if incidents

---

### Oversight Framework

**Quarterly Review** (every 3 months)

- [ ] Incident review: What went wrong this quarter?
- [ ] Risk assessment refresh: New risks emerged?
- [ ] Compliance status: Are we compliant with EU AI Act, sectoral regulations?
- [ ] Regulatory updates: New rules, enforcement actions?
- [ ] Audit results: Third-party audit findings

**Semi-Annual Review** (every 6 months)

- [ ] Risk re-assessment: Full risk portfolio review
- [ ] Third-party audit results: Independent evaluation of systems
- [ ] Emerging threats: New attack vectors, regulatory challenges
- [ ] Competitive landscape: How are competitors approaching AI governance?
- [ ] Board education: Deep dive on specific AI risk (e.g., hallucinations, bias)

**Annual Review** (every year)

- [ ] Strategy alignment: Does AI strategy still align with business?
- [ ] Budget review: Are we investing enough in AI governance?
- [ ] Regulatory outlook: What's coming in next 12 months?
- [ ] Insurance review: Is coverage adequate?
- [ ] Organizational structure: Do we have right team, skills, budget?

---

### Key Decisions Requiring Board Approval

- [ ] **Deploying high-risk AI systems** (hiring, lending, law enforcement)
  - Board must approve before launch
  - Must have impact assessment, bias audit
  - Human oversight designed

- [ ] **Material incidents** (Tier 3-4)
  - Board must be notified immediately
  - Weekly updates on status + fix
  - Board must approve incident disclosure

- [ ] **Significant regulatory change** (new laws, enforcement)
  - Board must be notified
  - Compliance plan must be approved
  - Budget implications reviewed

- [ ] **Major investment in AI governance** (>$5M)
  - Board must approve budget
  - ROI/impact assessment required
  - Timeline for compliance

- [ ] **Acquisition / Partnership** with AI implications
  - Board must assess AI risk
  - Compliance status reviewed
  - Integration plan for AI systems

---

### Board Dashboard (KPIs)

Monthly Report to Board should include:

| KPI | Target | Current | Status |
|-----|--------|---------|--------|
| **Compliance Status** | 100% of systems compliant | 85% | ⚠️ |
| **Incident Count (Tier 3+)** | 0 | 1 this month | ⚠️ |
| **Audit Pass Rate** | 100% | 95% | ⚠️ |
| **High-Risk Systems** | Monitored | 5 systems | ✓ |
| **Board-Approved Systems** | All major systems | 12/15 approved | ⚠️ |
| **Insurance Coverage** | $50M+ for AI | $25M | ⚠️ |
| **Regulatory Changes** | Monitored monthly | 3 new regulations | ℹ️ |

---

## GOVERNANCE CHECKLIST

- [ ] **Risk Classification**: All AI systems classified (Prohibited / High / Limited / Low)
- [ ] **Impact Assessment**: High-risk systems have impact assessments
- [ ] **Bias Audit**: High-risk systems have third-party bias audits
- [ ] **Monitoring**: All systems have live monitoring dashboard
- [ ] **Incident Response**: Playbook documented, team trained
- [ ] **Board Governance**: Committee established, oversight framework defined
- [ ] **Regulatory Compliance**: EU AI Act (if applicable), sectoral regulations
- [ ] **Insurance**: Coverage reviewed, AI included, limits adequate
- [ ] **Data Governance**: Training data documented, privacy controls in place
- [ ] **Escalation**: Clear path for issues, board notification protocol defined

---

**Last Updated**: March 2026
**Reference**: SKILL.md Phase 5 (AI Governance & Safety)
**CRITICAL**: EU AI Act deadline is August 26, 2026 (5 months away)
