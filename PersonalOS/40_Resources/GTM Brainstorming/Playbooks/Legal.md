# GTM Playbooks: Legal

Curated list of data-driven GTM Playbooks for the **Legal** vertical. Use these to brainstorm messaging, trigger events, and PVP angles.

---

## Actionstep (actionstep.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/actionstep-com)
**Strategic Summary**: The playbook mines State Bar disciplinary records to identify law firms with trust accounting violations and connects second-violation risk to upcoming presumptive suspension consequences, targeting immigration firms with growing case volume.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Strong (9.4/10)

                Segment: Immigration law firms (10-50 attorneys) with documented State Bar trust accounting violations in past 24 months

                Why it works: This play uses pure government data (State Bar disciplinary records) to mirror an exact painful situation—a trust accounting violation with specific case number, date, and violation details. Managing Partners know they had the violation, but the message creates urgency by connecting it to the "second violation = presumptive suspension" consequence they may not be actively thinking about. The question "How are you tracking reconciliation now?" forces them to confront whether their current manual system (likely spreadsheets or basic QuickBooks) can prevent a repeat violation. Scored 9.4/10 in buyer critique due to perfect situation recognition (10/10), complete data credibility (10/10), and strong emotional resonance (9/10).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - California State Bar Disciplinary Records - Search by attorney/firm name, filter for trust accounting violations (IOLTA reconciliation errors), fields: case_number, attorney_name, filing_date, violation_description, amount_involved
  - Similar databases available for other states: Illinois ARDC, Florida Bar, Texas State Bar
  - EOIR Immigration Attorney Roster - Confirm immigration law specialization
  - Source: California State Bar disciplinary records database
  - Method: Direct lookup by attorney/firm name → case_number and filing_date fields
  - Confidence: 95% (pure government record, publicly verifiable)
  - Source: Same State Bar case record, violation details section
  - Fields: violation_description, violation_count, amount_involved
  - Calculation: Sum of discrepancy amounts: $4,200 + $3,850 + $4,400 = $12,450
  - Confidence: 95% (government case record)
  - Source: California Rules of Professional Conduct, Rule 1.15 (trust account regulations)
  - Standard: Second trust violation = presumptive suspension (3 months minimum per disciplinary guidelines)
  - Confidence: 100% (published regulation)

#### Play:  (PQS |  - Strong (9.2/10)

                Segment: Immigration law firms with past State Bar violations (missed deadlines, trust accounting issues) that have experienced significant review velocity growth (50%+ increase) since the violation date

                Why it works: This play creates a powerful "oh shit" moment by showing the Managing Partner that their case volume has nearly doubled (from 18 to 34 reviews/month) since their last violation, while their deadline tracking system has remained the same. Partners are often aware they're busy and had a violation, but they don't track review growth as a proxy for case volume trends. The non-obvious synthesis is connecting these three data points: (1) past violation proving the system failed once, (2) current high volume, (3) growth trajectory showing strain is increasing. The question "How are you managing it?" forces acknowledgment that manual tracking can't scale. Scored 9.2/10 with perfect marks on insight value (10/10) and effort to reply (10/10).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Google Places API - Track user_ratings_total field monthly to calculate review velocity (current: 34/month, historical: 18/month at violation date), cost: $0.017 per request
  - State Bar Disciplinary Records - Past violation (case number, date, violation type: missed I-485 filing deadline)
  - EOIR Roster - Confirm immigration specialization
  - Source: Google Places API (maps.googleapis.com/maps/api/place/details/json)
  - Method: Poll user_ratings_total monthly for 6 months, calculate delta
  - Data: Month 1 = 512 reviews, Month 6 = 716 reviews
  - Formula: (716 - 512) / 6 months = 34 reviews/month average
  - Confidence: 85% (API data, review rate ≠ all clients but consistent proxy)
  - Source: Google Places API historical tracking + State Bar violation date
  - Violation date: June 2023 (from State Bar case record)
  - Historical data: June 2023 total = 320 reviews, Dec 2022 (6 months prior) = 212 reviews
  - Formula: (320 - 212) / 6 months = 18 reviews/month at violation time
  - Growth: 34/18 = 1.89x = "nearly doubled"
  - Confidence: 80% (requires historical tracking, but verifiable via Google Business Profile insights)
  - Source: State Bar disciplinary records
  - Fields: case_number, violation_type (missed filing deadline for I-485 adjustment of status application)
  - Confidence: 95% (pure government data)

#### Play:  (PQS |  - Strong (8.6/10)

                Segment: High-volume immigration law firms (30+ reviews/month = 360+ annually) with past State Bar violations related to deadline management or case tracking failures

                Why it works: This play connects current high review velocity (34/month) to estimated annual case volume (400+ cases) using disclosed industry assumptions (8-10% client review rate), then links this volume pressure to a past deadline violation. The non-obvious insight is showing the Managing Partner that their review velocity translates to 400+ active cases annually—a scale that their manual tracking system (proven to fail via past violation) cannot reliably handle. The disclosure of the 8-10% review rate methodology shows honest transparency, which builds credibility. Scored 8.6/10 with perfect effort to reply (10/10) and strong insight value (9/10).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Google Places API - Review velocity tracking (user_ratings_total field, monthly polling)
  - Industry benchmark: 8-10% of immigration law clients leave Google reviews (conservative estimate for case volume calculation)
  - State Bar Disciplinary Records - Past violation case number and details
  - Source: Google Places API
  - Method: Same as Play #2 (monthly polling of user_ratings_total)
  - Confidence: 85%
  - Source: Review velocity (above) + industry proxy
  - Calculation: 34 reviews/month × 12 months = 408 reviews/year
  - Industry assumption: 8-10% of immigration clients leave Google reviews (disclosed in message)
  - Formula: 408 reviews ÷ 0.10 (10% rate) = 4,080 clients/year OR ÷ 0.08 (8%) = 5,100/year
  - Conservative estimate: "400+ cases annually" (using 10% rate)
  - Confidence: 60% (uses industry proxy + disclosed assumption, verifiable against actual intake numbers)
  - Disclosure: Message states "given typical 8-10% review rates" to make assumption transparent

#### Play:  (PQS |  - Strong (8.6/10)

                Segment: Immigration law firms with State Bar trust accounting violations that have compliance plan deadlines approaching within 6 months

                Why it works: This play takes the same trust violation data as Play #1 but angles it toward the remediation deadline rather than repeat violation risk. The 18-month compliance plan deadline (September 2025 in this example) creates time-bound urgency. The offer of a "remediation checklist" provides a clear value exchange—the recipient can request something concrete and useful. This approach works well for Partners who are compliance-focused and responsive to deadlines. The question "Want the remediation checklist?" is low-friction (yes/no) and implies you have a solution ready. Scored 8.6/10 with perfect data credibility (10/10) and strong situation recognition (9/10).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - State Bar Disciplinary Records - Case details including compliance_deadline field (18 months from filing date for remediation plan)
  - Calculation: Filing date (March 2024) + 18 months = September 2025 deadline
  - Source: State Bar case record (compliance_deadline or remediation_requirements field)
  - Regulation: State Bar typically requires remediation plan within 18 months of trust violation filing
  - Calculation: Filing date 2024-03-15 + 18 months = 2025-09-15 (September 2025)
  - Confidence: 90% (government deadline + simple date math)

---

## BARBRI (barbri.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/barbri-com)
**Strategic Summary**: The playbook uses internal student performance data with historical bar exam outcome validation to identify at-risk students 8+ weeks before results publish, delivering law school deans specific student names with sub-65% predictive scores and intervention recommendations.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Help your students pass the bar exam

Hi [Dean Name],

I noticed your law school is focused on student success. At BARBRI, we've helped over 1.3 million students pass the bar exam with our proven study methods.

Our platform offers:
• Comprehensive MBE and essay prep
• Expert faculty instruction
• Personalized study plans
• Proven results with 80+ years of experience

Would you be open to a quick 15-minute call to discuss how we can help improve your students' bar passage rates?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: February Exam Early Warning for 18 Students (PVP                     Internal Data | Strong - Strong (9.3/10))

- **What's the play?**: Use BARBRI's student performance data to identify at-risk students 8+ weeks before official bar results publish. Provide law school deans with specific student names and intervention recommendations before failure occurs.
- **Why this works**: Law school deans are measured on bar passage rates but typically get results 6-12 months after the exam - too late to intervene. BARBRI has real-time performance data showing which students are tracking toward failure. The 100% correlation between sub-65% scoring and failure creates urgency. This helps deans serve their students immediately, not just selling a product.
- **Data Sources**:
  - BARBRI Internal Student Performance Data - practice exam scores, module completion rates, MBE simulation results
  - Historical bar exam outcome validation - 3+ exam cycles showing predictive accuracy
- **Outreach Message template**:
  ```text
  Subject: February exam early warning for 18 students
  
  18 of your February test-takers are tracking below 65% on our platform's predictive scoring model.
  
  Every student below 65% at this stage has failed in the past 3 exam cycles.
  
  Should I send you their names and the specific areas they're struggling?
  ```
- **Data Requirement**: This play requires student-level performance data from BARBRI's platform usage (practice exam scores, study hours, topic mastery metrics) linked to actual bar exam outcomes, with historical validation showing predictive accuracy.
                    This is proprietary data only BARBRI has - competitors cannot replicate this predictive intelligence.

#### Play: Bar Passage Risk Prediction Before Official Results (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Provide law school deans with predictive bar passage risk assessments for their current cohort using BARBRI's platform performance data, delivering the insight 8+ weeks before official ABA results publish.
- **Why this works**: Deans are blind to student risk until official bar results publish - by then it's too late to intervene. BARBRI tracks 47 performance indicators showing specific students flagged as high-risk with sub-60% MBE scores and below-threshold essay performance. The 8-week lead time creates an actionable intervention window. This insight helps deans improve student outcomes immediately.
- **Data Sources**:
  - BARBRI Internal Student Performance Data - aggregated across 530+ partner institutions
  - MBE simulation scores and essay performance metrics
  - Historical bar exam outcomes linked to performance patterns
- **Outreach Message template**:
  ```text
  Subject: 18 of your students flagged as high-risk
  
  Based on your students' performance patterns in our platform, 18 are showing high-risk indicators for the February bar exam.
  
  These students have sub-60% scores on simulated MBE and below-threshold essay performance.
  
  Want their names and specific intervention recommendations?
  ```
- **Data Requirement**: This play requires detailed student-level performance data from BARBRI's platform usage, including practice exam scores, study hours, engagement metrics, and topic mastery indicators, linked to actual bar exam outcomes.
                    This is proprietary data only BARBRI has - competitors cannot replicate this level of predictive intelligence.

#### Play: UK Law Firms Expanding into SQE Without Training Infrastructure (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target UK law firms bringing on SQE pathway training contract candidates where the current partner base has zero SQE qualifications themselves (only LPC). Cross-reference LinkedIn hiring data with SRA qualification database to identify mentorship gaps.
- **Why this works**: The partner qualification gap is non-obvious and deeply concerning - trainees entering via SQE pathway won't have mentors who understand the assessment structure. The SRA database cross-reference adds credibility and shows deep research. This identifies a structural problem the firm may not have realized yet.
- **Data Sources**:
  - SRA SQE Training Provider Directory - provider partnerships, qualification records
  - LinkedIn Legal Hiring Data - training contract postings, hiring volume, start dates
  - SRA Qualification Database - partner qualification pathways (LPC vs SQE)
- **Outreach Message template**:
  ```text
  Subject: 12 SQE trainees starting in September
  
  You're bringing on 12 training contract candidates under the SQE pathway in September 2025.
  
  I cross-referenced the SRA database - none of your current partners completed SQE themselves, only LPC.
  
  Is someone already handling the SQE prep and mentorship gap?
  ```

#### Play: Law Schools with 3 Consecutive Years Below ABA Standard (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target law schools with bar passage rates below 75% for three consecutive years (2022-2024), triggering ABA Standard 316 remediation requirements with specific March 1st compliance deadline.
- **Why this works**: The three-year trend proves deep research and is more damning than a single year drop. Citing the specific ABA Standard 316 and March 1st deadline creates immediate urgency. The yes/no question makes it easy to respond. This identifies a compliance crisis that threatens accreditation.
- **Data Sources**:
  - ABA Required Disclosures - Bar Passage Data - bar_passage_rate, year, school_name, first_time_taker_results
- **Outreach Message template**:
  ```text
  Subject: 3 consecutive years below 75% at your school
  
  Your school has posted 72%, 71%, and 68% first-time bar pass rates from 2022-2024.
  
  ABA Standard 316 requires schools below 75% for two years to submit remediation plans by March 1st.
  
  Is someone already drafting your compliance response?
  ```

#### Play: Subject-Specific MBE Performance Breakdown (PVP                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Combine BARBRI's internal MBE performance data by subject area with public LSAC peer school data to show law schools exactly which subjects are dragging down their bar passage rates compared to peer institutions.
- **Why this works**: Identifying that 30% of failing students are attributable to a single MBE subject (Real Property) is immediately actionable for curriculum planning. The 18-point deficit vs peer schools creates competitive pressure. Offering doctrinal course correlation analysis provides instant value for academic planning.
- **Data Sources**:
  - BARBRI Internal MBE Performance Data - subject-level scores aggregated by school
  - LSAC Legal Education Data Library - peer school LSAT medians for benchmarking
- **Outreach Message template**:
  ```text
  Subject: Subject-specific breakdown of your gap
  
  Your MBE subject scores show 18-point deficit in Real Property vs peer schools with 164+ LSAT medians.
  
  That single subject is dragging down 30% of your failing students.
  
  Want the analysis showing which doctrinal courses correlate with the Real Property gap?
  ```
- **Data Requirement**: This play requires aggregated MBE performance data by subject area from BARBRI students, organized by law school and benchmarked against peer institutions with similar LSAT profiles.
                    Combined with public LSAC data to create competitive benchmarks. This synthesis is unique to BARBRI's data.

#### Play: Law Schools Below ABA 75% Standard Threshold (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target law schools with July 2024 bar passage rates below 75%, triggering the two-year ABA remediation clock for potential accreditation review. Use specific school performance data from ABA Required Disclosures.
- **Why this works**: The message demonstrates access to exact data (68% passage rate in July 2024) showing deep research. The ABA 75% threshold violation creates a real accreditation crisis. The two-year remediation clock triggers immediate urgency. Easy routing question removes friction from response.
- **Data Sources**:
  - ABA Required Disclosures - Bar Passage Data - bar_passage_rate, year, jurisdiction, school_name
- **Outreach Message template**:
  ```text
  Subject: Your bar passage rate dropped to 68% in July
  
  Your July 2024 bar passage rate dropped to 68%, putting you 7 points below the ABA's 75% standard threshold.
  
  That triggers the two-year remediation clock for potential accreditation review.
  
  Who's leading your bar support strategy for the February cohort?
  ```

#### Play: High-LSAT Schools with Bar Passage Underperformance (PQS                     Public Data | Strong - Strong (7.8/10))

- **What's the play?**: Target law schools with high incoming LSAT medians (165+) but bar passage rates 12+ points below peer schools with similar LSAT profiles. This indicates curriculum or bar prep integration weakness, not student aptitude issues.
- **Why this works**: The LSAT vs outcome gap is embarrassing and immediately actionable - it proves the problem isn't student quality. The reputation impact hits enrollment concerns directly since prospective students compare these metrics. The 12-point gap vs peers creates competitive pressure.
- **Data Sources**:
  - LSAC Legal Education Data Library - lsat_scores, gpa_medians, school_name
  - ABA Required Disclosures - Bar Passage Data - bar_passage_rate, first_time_taker_results
- **Outreach Message template**:
  ```text
  Subject: Your 165 LSAT median but 71% bar pass rate
  
  Your incoming class has a 165 LSAT median but your bar passage rate is only 71% - that's 12 points below schools with similar LSAT profiles.
  
  That gap suggests curriculum or bar prep integration issues that hurt your reputation with prospective students.
  
  Who reviews your bar prep curriculum alignment?
  ```

#### Play: SQE Practice Area Qualification Benchmarks (PVP                     Public + Internal | Okay - Okay (7.6/10))

- **What's the play?**: Combine SRA public qualification data with LinkedIn firm headcount estimates to show UK law firms how their SQE qualification depth compares to peer firms by practice area.
- **Why this works**: The practice-area-specific benchmark (23 commercial lit solicitors but only 4 SQE-qualified) is useful for workforce planning. The 8-point deficit vs peer firms creates competitive context. The practice area breakdown would genuinely help planning.
- **Data Sources**:
  - SRA Qualification Database - solicitor qualifications by pathway
  - LinkedIn Legal Hiring Data - firm headcount by practice area
- **Outreach Message template**:
  ```text
  Subject: Your commercial litigation SQE bench strength
  
  I analyzed SQE qualification data for your practice areas - you have 23 commercial lit solicitors but only 4 completed SQE assessments.
  
  That's 8 points below firms of your size in commercial practice.
  
  Want the breakdown by practice area and seniority level?
  ```
- **Data Requirement**: This play requires combining public SRA qualification data with firm headcount estimates from LinkedIn or firm directories to create practice area benchmarks.
                    The synthesis of public qualification data with practice area structure creates competitive intelligence.

#### Play: Bar Passage Risk Assessment 8 Weeks Early (PVP                     Internal Data | Okay - Okay (7.4/10))

- **What's the play?**: Use BARBRI's 47 performance indicators across student platform usage to predict at-risk candidates 8 weeks before official bar results, giving law schools time for targeted intervention.
- **Why this works**: Law schools don't have contemporaneous risk intelligence - official results come months after the exam. The 8-week lead time creates an actionable intervention window. However, the message lacks specificity about which students or what data is actually available.
- **Data Sources**:
  - BARBRI Internal Student Performance Data - 47 performance indicators including practice test scores, study hours, engagement metrics
- **Outreach Message template**:
  ```text
  Subject: Want your February bar risk assessment?
  
  We track 47 performance indicators across your bar prep students and can predict at-risk candidates 8 weeks before official results.
  
  That gives you time to intervene with targeted support before they fail.
  
  Want the February cohort risk breakdown?
  ```
- **Data Requirement**: This play requires student-level performance data from BARBRI's platform usage across practice tests, study hours, and engagement metrics that can be analyzed for predictive risk scoring.
                    This is proprietary data only BARBRI has - competitors lack the performance baseline for prediction.

#### Play: SQE Qualification Pipeline vs Big 4 Benchmarks (PVP                     Public + Internal | Okay - Okay (7.3/10))

- **What's the play?**: Track SRA qualification registrations by firm to create competitive benchmarks showing how UK law firms compare to Big 4 legal arms in SQE qualification velocity.
- **Why this works**: The Big 4 comparison provides relevant competitive context for UK firms worried about talent competition. The quarterly qualification velocity (12 per quarter vs 2 in 6 months) quantifies the gap. Training contract competition is a real concern.
- **Data Sources**:
  - SRA Qualification Registration Data - quarterly SQE completions by firm
  - Firm size and type classification
- **Outreach Message template**:
  ```text
  Subject: Your SQE qualification pipeline vs Big 4
  
  Big 4 legal arms are averaging 12 SQE qualifications per quarter - you've completed 2 in the past 6 months.
  
  That gap affects your ability to compete for SQE-pathway training contracts.
  
  Want the quarterly benchmark data by firm size?
  ```
- **Data Requirement**: This play requires tracking SRA qualification registrations and aggregating them by firm to create competitive benchmarks and quarterly velocity metrics.
                    The synthesis of public SRA data into competitive intelligence requires ongoing tracking and aggregation.

#### Play: High-LSAT Schools with Peer Performance Gap (PQS                     Public Data | Okay - Okay (7.2/10))

- **What's the play?**: Target law schools where incoming LSAT medians (164+) predict 83% bar passage based on peer school data, but actual performance is 71% - losing 15-20 students per cohort who should be passing.
- **Why this works**: The peer comparison with specific LSAT median (164) is data-driven. The 15-20 students lost per cohort is concrete and painful. However, the closing question about "which specific subject areas" feels like it's teasing a product demo rather than delivering insight.
- **Data Sources**:
  - LSAC Legal Education Data Library - lsat_scores, school_name
  - ABA Required Disclosures - Bar Passage Data - bar_passage_rate
- **Outreach Message template**:
  ```text
  Subject: 12-point underperformance vs peer schools
  
  Schools with your 164 LSAT median average 83% bar passage - you're at 71%.
  
  That 12-point gap means you're losing at least 15-20 students per cohort who should be passing.
  
  Want to see which specific subject areas show the biggest disconnect?
  ```

#### Play: SQE Transition Timeline Gap Analysis (PVP                     Public + Internal | Okay - Okay (7.1/10))

- **What's the play?**: Combine SRA registration data showing low SQE adoption with firm size benchmarks to identify UK firms 24+ months behind peers in LPC-to-SQE transition readiness.
- **Why this works**: The LPC vs SQE gap is a real concern for UK firms managing the qualification pathway transition. The "24 months behind" benchmark is specific and alarming. However, this feels like citing the publicly-known LPC phaseout rather than delivering proprietary insight.
- **Data Sources**:
  - SRA Registration Data - SQE assessment registrations by firm over 12 months
  - Firm size classification and peer grouping
- **Outreach Message template**:
  ```text
  Subject: Gap analysis for your SQE transition
  
  Your firm has 67 solicitors qualified under LPC but you've only registered 8 for SQE assessments in the past 12 months.
  
  With the LPC phaseout, that puts you 24 months behind firms of similar size in transition readiness.
  
  Want your practice-area-specific transition timeline?
  ```
- **Data Requirement**: This play requires tracking SRA registration data and combining it with firm size/practice area data to create transition benchmarks and timeline projections.
                    The synthesis of public registration data into competitive transition intelligence requires ongoing tracking.

---

## Everlaw (everlaw.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/everlaw-com)
**Strategic Summary**: Playbook analyzes PACER federal court records to map custodian-level email volume distributions and identify privilege log entries lacking attorney metadata, surfacing prioritization data and privilege waiver risk before opposing counsel files motions to compel.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transform your eDiscovery workflow

Hi [Name],

I noticed on LinkedIn that your firm recently won a major securities case - congrats!

As litigation gets more complex, are you still managing document review manually? Everlaw helps Am Law 200 firms review documents 74% faster with AI-powered analytics.

We've helped firms like yours standardize discovery processes and reduce costs. Would love to show you how our cloud-native platform compares to legacy tools like Relativity.

Do you have 15 minutes next week?
```

### ✓ The New Way: GTM Plays

#### Play: Custodian Volume Distribution Analysis (PVP                     Public + Internal | Strong - Strong (9.6/10))

- **What's the play?**: Analyze production metadata from court filings to map custodian-level email volume distribution. Show litigation teams exactly which 12 custodians account for 74% of all emails, allowing them to prioritize review efforts for maximum efficiency.
- **Why this works**: This is incredibly valuable prioritization data that completely changes the recipient's review strategy. Knowing that 12 of 147 custodians contain 620,000 of 840,000 emails tells them exactly WHERE to focus resources. Even without buying, this distribution data helps them plan review TODAY. The specificity proves genuine analysis work that competitors cannot easily replicate.
- **Data Sources**:
  - PACER - Federal Court Records (production metadata, custodian lists)
  - Internal analysis capability to map email volume by custodian
- **Outreach Message template**:
  ```text
  Subject: 147 custodians but 12 account for 620K emails
  
  Your Acme case has 147 custodians, but we mapped the distribution - 12 custodians account for 620,000 of the 840,000 emails (74%).
  
  The remaining 135 custodians are only 220,000 emails, averaging 1,600 emails each.
  
  Want the prioritized custodian list showing the high-volume twelve?
  ```
- **Data Requirement**: This play requires the ability to analyze production metadata from court filings to map custodian-level email volume distribution.
                    This synthesis work - taking public court data and performing granular analysis - creates proprietary intelligence competitors cannot easily replicate.

#### Play: Privilege Log Gap Analysis (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Review privilege logs filed in court and cross-reference with email metadata to identify entries claiming privilege but lacking corresponding attorney involvement. Surface these 23 specific gaps before opposing counsel files a motion to compel, helping teams avoid sanctions and privilege waiver.
- **Why this works**: This is EXTREMELY valuable because privilege disputes can torpedo cases. The recipient gets granular analysis of THEIR specific privilege log with 23 concrete entries to investigate TODAY. This helps them avoid sanctions and privilege waiver even if they never buy. The analysis requires deep case file work that clearly differentiates from competitor outreach.
- **Data Sources**:
  - PACER - Federal Court Records (privilege logs, motions to compel)
  - Internal capability to cross-reference privilege log metadata patterns
- **Outreach Message template**:
  ```text
  Subject: Your Acme case has 23 privilege log gaps
  
  We reviewed the October privilege log in your Acme securities case and found 23 emails with privilege claims but no corresponding attorney involvement in the metadata.
  
  Opposing counsel filed a motion to compel on November 8th challenging privilege assertions.
  
  Want the list of the 23 flagged entries before the hearing?
  ```
- **Data Requirement**: This play requires the ability to access privilege logs from PACER court filings and cross-reference metadata patterns to identify potential weaknesses.
                    This deep case file analysis - combining public court records with pattern recognition - creates unique intelligence only you can provide.

#### Play: Opposing Counsel Tactical Pattern Analysis (PVP                     Public Data | Strong - Strong (9.3/10))

- **What's the play?**: Research the lead opposing counsel's litigation history across their prior 4 securities cases. Identify their consistent tactical pattern of challenging specific custodians (CFO and VP Finance) 60 days before depositions. Deliver this competitive intelligence to help the recipient anticipate and prepare for the likely next move.
- **Why this works**: This is competitive intelligence the recipient can use immediately to prepare their defense strategy. Knowing that opposing counsel David Brenner focused on CFO/VP Finance email patterns in 3 of 4 prior cases, always 60 days before depositions, helps them anticipate his playbook. This value is delivered regardless of whether they buy. Requires deep legal research synthesis that competitors cannot easily replicate.
- **Data Sources**:
  - PACER - Federal Court Records (historical cases by attorney)
  - Securities Class Action Clearinghouse (case outcomes and tactics)
- **Outreach Message template**:
  ```text
  Subject: Your opposing counsel used this tactic in 4 prior cases
  
  Lead opposing counsel David Brenner used targeted custodian challenges in 4 prior securities cases, requesting court-ordered re-review of specific executives' communications.
  
  In 3 of those cases, he focused on CFO and VP Finance email patterns 60 days before depositions.
  
  Want the pattern analysis showing his typical challenge timeline?
  ```

#### Play: High-Volume Custodian Prioritization (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Analyze production metadata to identify that 2 specific custodians (CFO Sarah Chen and VP Finance Mike Torres) account for 340,000 of the 840,000 total emails in the case. Show the recipient that focusing review on these two executives first provides 40% coverage before the April 2nd CFO deposition, enabling smart resource allocation.
- **Why this works**: This analysis names THEIR specific executives and provides concrete prioritization guidance with immediate action value. The recipient learns WHERE to focus review efforts with a specific custodian breakdown tied to their upcoming deposition deadline. Even without buying, this helps them plan review TODAY. The specificity passes the "how did they know that" test and demonstrates genuine analysis work.
- **Data Sources**:
  - PACER - Federal Court Records (production metadata, custodian names)
  - Internal capability to analyze custodian-level email distribution
- **Outreach Message template**:
  ```text
  Subject: 2 custodians account for 340K of your emails
  
  We mapped the custodian distribution in your Acme case production - 2 custodians (CFO Sarah Chen and VP Finance Mike Torres) account for 340,000 of the 840,000 emails.
  
  Focusing review on those two first gets you 40% coverage before the April 2nd depo.
  
  Want the full custodian breakdown showing communication patterns?
  ```
- **Data Requirement**: This play requires the ability to analyze production metadata showing custodian-level email volume distribution from court filings or public productions.
                    This synthesis - mapping volume distribution to specific executives - creates actionable prioritization intelligence unique to your analysis capabilities.

#### Play: Comparative Case Timeline Analysis (PVP                     Public + Internal | Strong - Strong (7.8/10))

- **What's the play?**: Compare the recipient's Acme case timeline against 4 similar securities litigation cases in PACER. Identify that their CFO deposition is scheduled 6 weeks earlier than comparable cases, creating compressed preparation time they may not have realized. Provide the comparison timeline showing when other firms typically begin CFO prep.
- **Why this works**: This tells the recipient something about competitive positioning they might not have realized - they have LESS time than similar cases to prepare their executive for questioning. The 6 weeks earlier finding creates urgency with specific context beyond their own case bubble. The comparison to similar cases provides actual strategic value they can use immediately.
- **Data Sources**:
  - PACER - Federal Court Records (case timelines, deposition schedules)
  - Internal capability to identify and compare similar case patterns
- **Outreach Message template**:
  ```text
  Subject: Your CFO depo is 6 weeks before similar cases
  
  Court records show 4 other securities cases with similar timelines to Acme, but your CFO deposition is scheduled 6 weeks earlier than theirs.
  
  That means you have less time to prepare your executive for questioning about financial communications.
  
  Want the comparison timeline showing when other firms start CFO prep?
  ```
- **Data Requirement**: This play requires the ability to track case timelines across multiple securities litigation matters in PACER and identify similar case patterns for comparison.
                    This comparative analysis - synthesizing patterns across multiple cases - provides strategic context the recipient cannot easily obtain themselves.

#### Play: Deposition Scheduling Conflict Identification (PQS                     Public Data | Okay - Okay (7.6/10))

- **What's the play?**: Map the court calendar to identify that 5 fact witness depositions (CFO, VP Finance, and 3 operations directors) are scheduled for the same week as pretrial conference. Surface this scheduling nightmare to demonstrate understanding of their coordination challenges.
- **Why this works**: This identifies a real scheduling conflict with concrete visualization of the problem - preparing 5 executives for depositions while simultaneously handling pretrial motions. The synthesis across the court calendar is helpful context about THEIR case timeline. However, the litigation team likely already knows the court calendar, so this is somewhat obvious from the docket.
- **Data Sources**:
  - PACER - Federal Court Records (court calendar, deposition schedules)
- **Outreach Message template**:
  ```text
  Subject: 5 Acme depositions scheduled same week as trial prep
  
  Court calendar shows 5 fact witness depositions scheduled for the week of May 12th, the same week your trial team has pretrial conference.
  
  That's your CFO, VP Finance, and 3 operations directors all being deposed while you're preparing pretrial motions.
  
  Is someone coordinating the depo prep timeline?
  ```

---

## Litera (litera.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/litera-com)
**Strategic Summary**: Playbook tracks lateral hire announcements and law firm press releases to identify document system fragmentation caused by attorneys joining from multiple firms with different precedent libraries.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your legal workflows

Hi [First Name],

I noticed your firm recently announced a new office opening. Congratulations!

At Litera, we help top law firms automate document workflows and increase efficiency. Our AI-powered platform has helped firms like yours reduce document review time by up to 60%.

Would you be open to a quick 15-minute call to discuss how we can help your team work smarter?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Practice Scaling Velocity Gap - Lateral Integration Challenge (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Target law firms that have announced lateral partner or associate hires from multiple different firms. Cross-reference LinkedIn announcements with press releases to identify the source firms these laterals came from.
                    The insight: Each lateral brings their own document templates, precedent libraries, and automation tools from their previous firm. Without standardization, the first client pitch will require manual document assembly instead of pulling from unified firm templates.
- **Why this works**: Naming the specific firms shows deep research. The client pitch risk is real and urgent. The Goodwin Procter playbook is concrete and valuable with a 30-day timeline making it actionable. Even if they don't buy, the playbook helps them serve their clients faster by standardizing lateral onboarding.
- **Data Sources**:
  - LinkedIn lateral hire announcements - hire date, source firm, practice area
  - Law firm press releases - new office launches, practice expansions
  - Company Internal Data - case studies from similar lateral integrations at customer firms
- **Outreach Message template**:
  ```text
  Subject: 8 laterals joining Austin with 4 different document systems
  
  Your 8 Austin lateral hires come from Kirkland, Latham, Skadden, and Gibson Dunn - each uses different precedent libraries and automation tools.
  
  Without standardization, your first client pitch will require manual document assembly instead of pulling from firm templates.
  
  Want the 30-day playbook showing how Goodwin Procter unified 12 laterals in Boston?
  ```
- **Data Requirement**: This play assumes Litera can identify lateral hire announcements and track which firms they come from, plus has case studies from similar expansions.
                    Combined with public lateral hire data, this synthesis creates unique value that competitors cannot replicate.

#### Play: Practice Scaling Velocity Gap - Template Standardization Gap (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Target law firms that have publicly announced new office openings with specific launch dates and lateral hire counts. Identify the source firms these laterals are coming from to understand the document system fragmentation challenge.
                    The insight: Each lateral brings different document templates, clause libraries, and formatting standards from their previous firms. Without proactive template standardization, the team will waste 200+ hours reconciling systems before first client delivery.
- **Why this works**: Specific office, specific date, specific hire count - they did homework. The 200+ hours waste is tangible and believable. Wilson Sonsini reference adds credibility as peer firm. The checklist offer provides immediate value even without buying. Helps them solve a problem they're definitely facing right now.
- **Data Sources**:
  - Law firm press releases - new office announcements with launch dates
  - LinkedIn lateral hire announcements - hire count, source firms
  - Company Internal Data - template standardization checklists from successful office launches
- **Outreach Message template**:
  ```text
  Subject: Your Austin office opens March 2025 without templates
  
  Your Austin office launches March 2025 with 8 lateral hires from 4 different firms.
  
  Each firm uses different document templates, clause libraries, and formatting standards - your team will waste 200+ hours reconciling before first client delivery.
  
  Want the template standardization checklist we built for Wilson Sonsini's Denver launch?
  ```
- **Data Requirement**: This play assumes Litera has tracked office launch challenges with existing customers and can share anonymized best practices.
                    The template checklist helps them serve their clients faster by reducing launch friction.

#### Play: Practice Scaling Velocity Gap - Document System Migration (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target law firms that have announced lateral hires from firms known to have proprietary document automation platforms. Each source firm (Kirkland, Latham, Skadden, Gibson Dunn) has different document systems.
                    The question surfaces a coordination challenge the COO or CIO might not have considered: Without unified templates, teams will spend 40+ hours per matter reconciling formatting and clause variations.
- **Why this works**: Specific firm names show research depth. The 40+ hours per matter is believable. The IT routing question is easy to answer. Surfacing a coordination challenge they might not have considered helps them avoid embarrassing launch issues.
- **Data Sources**:
  - LinkedIn lateral hire announcements - source firms, practice areas
  - Law firm press releases - office expansions, practice growth
- **Outreach Message template**:
  ```text
  Subject: 4 different document systems arriving in Austin
  
  Your Austin laterals come from Kirkland, Latham, Skadden, and Gibson Dunn - each firm has proprietary document automation platforms.
  
  Without unified templates, your team will spend 40+ hours per matter reconciling formatting and clause variations.
  
  Is IT already planning the document system migration?
  ```

#### Play: Practice Scaling Velocity Gap - Precedent Library Gap (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target law firms opening new offices in different jurisdictions (especially Texas, California, New York where local rules differ significantly). The insight: New offices launching without jurisdiction-specific templates force laterals to manually create documents for first 90 days.
                    The question is easy routing to whoever owns template libraries (typically Knowledge Management or Legal Operations).
- **Why this works**: Specific launch date and hire count is good research. The zero precedents problem is real and urgent. The 90-day delay is a tangible business risk. Easy routing question. Provides value by surfacing a blind spot they might have missed.
- **Data Sources**:
  - Law firm press releases - new office announcements with launch dates and locations
  - LinkedIn lateral hire announcements - hire counts, practice areas
- **Outreach Message template**:
  ```text
  Subject: Austin office launches March 2025 with zero precedents
  
  Your Austin office opens March 2025 but your precedent library shows no Texas-specific templates or local court forms.
  
  Your 8 lateral hires will manually create documents instead of using firm standard work product for first 90 days.
  
  Who's building the Austin template library before launch?
  ```

---

## Ocelot (ocelot.ai)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/ocelot-ai)
**Strategic Summary**: Playbook (built for Onit) targets federal contractors with GSA Schedule expirations during active contract performance periods and broker-dealers with FINRA disciplinary actions approaching Form ADV amendment deadlines.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your legal operations

Hi [First Name],

I noticed your team is growing and thought you might be interested in how Onit helps legal departments like yours manage contracts, e-billing, and matter management in one unified platform.

We've helped Fortune 500 companies reduce legal spend by up to 30% and improve visibility across their legal operations.

Would you be open to a quick call next week to explore how we could help [Company Name]?

Best regards,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: DOD Contract Concentration + GSA Schedule Gaps (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target prime federal contractors with high revenue concentration in a single agency (70%+ from DOD) who have GSA Schedule expirations during active contract performance periods. These contractors face portfolio risk where schedule lapses block task order modifications and new awards.
- **Why this works**: You're surfacing a contract management coordination problem they may not be tracking. Showing specific dollar amounts, contract concentration percentages, and exact schedule expiration dates proves you've done deep research into their federal contract portfolio - not just another sales pitch.
- **Data Sources**:
  - SAM.gov - contractor_name, cage_code, contract_count, contract_value, compliance_status
  - USAspending.gov - awarding_agency, contract_value, performance_period
  - GSA Schedules - schedule_number, contract_expiration
- **Outreach Message template**:
  ```text
  Subject: DOD contract concentration + GSA schedule gaps
  
  SAM.gov shows 73% of your federal contract value comes from DOD with $47M in active contracts while GSA Schedule 70 expires April 15, 2025.
  
  Schedule lapses during major contract performance periods block task order modifications and new awards.
  
  Who's coordinating GSA renewals with your active DOD delivery schedules?
  ```

#### Play: FINRA Sanction + Form ADV Amendment Deadlines (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target SEC-registered broker-dealers with FINRA disciplinary actions in the past 12 months who have upcoming Form ADV annual amendment deadlines. These firms must disclose regulatory actions across all state registrations - missed cross-references trigger SEC deficiency letters.
- **Why this works**: You're identifying a real securities compliance coordination problem between FINRA disciplinary disclosure and SEC filing requirements. Showing exact dates and specific form references (Item 11) demonstrates deep regulatory knowledge - you're not guessing, you're citing exact compliance obligations.
- **Data Sources**:
  - FINRA BrokerCheck - firm_name, disciplinary_actions, regulatory_events
  - SEC EDGAR - filing_type, filing_date, form_adv, sec_registration_number
  - Investment Adviser Public Disclosure (IAPD) - adviser_firm_name, regulatory_status
- **Outreach Message template**:
  ```text
  Subject: FINRA sanction October + Form ADV amendment due
  
  Your firm received a FINRA disciplinary action on October 22, 2024 requiring disclosure while your Form ADV annual amendment is due March 31, 2025.
  
  FINRA sanctions require Item 11 disclosure amendments within 30 days plus the annual filing - missed cross-references trigger SEC deficiency letters.
  
  Is compliance coordinating both the disciplinary disclosure and annual amendment?
  ```

#### Play: 73% Revenue from DOD + 3 GSA Schedules Expiring Q2 (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target prime federal contractors with high contract concentration in a single agency (70%+ revenue from DOD) who maintain multiple GSA Schedules all expiring in the same quarter. GSA schedule lapses during high DOD concentration create single-customer dependency risk that legal should track.
- **Why this works**: You're surfacing a contract portfolio risk they may not be monitoring. Showing specific revenue concentration percentages, exact schedule numbers, and expiration timing demonstrates you've analyzed their entire federal contract posture - not just surface-level research.
- **Data Sources**:
  - SAM.gov - contractor_name, cage_code, contract_value, compliance_status
  - USAspending.gov - awarding_agency, contract_value
  - GSA Schedules - schedule_number, contract_expiration
- **Outreach Message template**:
  ```text
  Subject: 73% revenue from DOD + 3 GSA schedules expiring Q2
  
  Your SAM.gov profile shows 73% of contract value concentrated with DOD while you maintain GSA Schedules 70, 84, and 899 all expiring in Q2 2025.
  
  GSA schedule lapses during high DOD concentration create single-customer dependency risk that legal should track.
  
  Is someone monitoring schedule renewals against your DOD contract performance periods?
  ```

#### Play: Form 483 Observations + SAM Expiring March 2025 (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target FDA-regulated drug manufacturers with recent Form 483 observations from facility inspections who have SAM.gov registrations expiring within 90 days. These manufacturers face dual compliance pressure - FDA remediation requirements must be documented before SAM.gov renewal or they risk contract suspension.
- **Why this works**: You're identifying a real compliance coordination problem they're experiencing right now. Both deadlines are verifiable public record, and the timing creates genuine legal operations pressure. This isn't a pitch - it's mirroring their actual situation with specific dates and observation counts.
- **Data Sources**:
  - FDA Establishment Inspection Reports (EIRs) - facility_name, 483_observations, inspection_date
  - SAM.gov - contractor_name, duns_number, active_contract_end_date, compliance_status
- **Outreach Message template**:
  ```text
  Subject: Form 483 observations + SAM expiring March 2025
  
  Your facility received 3 Form 483 observations in the November FDA inspection while your SAM.gov registration expires March 14, 2025.
  
  Missed SAM renewal blocks federal contract eligibility while outstanding 483s trigger follow-up inspections - both hit legal ops simultaneously.
  
  Is someone coordinating the 483 response and SAM renewal timelines?
  ```

#### Play: October FINRA Event Needs Item 11 Disclosure by March 31 (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target broker-dealers with FINRA disciplinary events in the past 12 months that require Item 11 disclosure on upcoming Form ADV annual amendments. Missed or inconsistent disciplinary disclosures between FINRA and SEC filings create audit exposure.
- **Why this works**: You're demonstrating specific knowledge of securities compliance filing requirements. Showing exact violation types, dates, and form item references proves you understand their regulatory obligations - not just another vendor claiming to understand financial services.
- **Data Sources**:
  - FINRA BrokerCheck - firm_name, disciplinary_actions, regulatory_events
  - SEC EDGAR - filing_type, filing_date, form_adv
- **Outreach Message template**:
  ```text
  Subject: October FINRA event needs Item 11 disclosure by March 31
  
  FINRA sanctioned your firm October 22, 2024 for supervision violations - that triggers Item 11 disclosure on your Form ADV amendment due March 31, 2025.
  
  Missed or inconsistent disciplinary disclosures between FINRA and SEC filings create audit exposure.
  
  Who's ensuring the October sanction is reflected in the March ADV filing?
  ```

#### Play: CMS Rating Dropped to 2 Stars + 4 License Renewals Q1 (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target multi-hospital health systems with CMS quality rating declines (from 3 to 2 stars or lower) who have multiple hospital licenses renewing in the same quarter. State boards often cross-reference CMS quality data during renewal reviews - the timing creates documentation overlap.
- **Why this works**: You're identifying a real operational coordination problem between federal quality reporting and state licensing requirements. The specific rating drop, exact renewal count, and Q1 timing demonstrate you've researched their health system portfolio - this is genuine legal operations pain they're experiencing now.
- **Data Sources**:
  - CMS Provider Data - Hospital Compare - provider_name, cms_certification_number, quality_metrics
  - State Health Department Licenses - facility_name, license_expiration, license_status
- **Outreach Message template**:
  ```text
  Subject: CMS rating dropped to 2 stars + 4 license renewals Q1
  
  Your system's overall CMS rating declined from 3 to 2 stars in the October update while you have 4 hospital licenses renewing in Q1 2025.
  
  State boards often cross-reference CMS quality data during renewal reviews - the timing creates documentation overlap.
  
  Is legal coordinating the CMS improvement plan and license renewal submissions?
  ```

#### Play: 2-Star CMS Rating During License Renewal Cycle (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target health systems with declining CMS overall ratings (2 stars or below) who have multiple facility licenses all renewing by the same deadline. State licensing boards request CMS deficiency documentation during renewals - declining ratings trigger additional scrutiny.
- **Why this works**: You're naming specific hospitals and exact deadlines, proving you've mapped their entire health system portfolio. The regulatory coordination issue between CMS and state boards is real - this isn't speculation, it's a documented compliance process they're managing right now.
- **Data Sources**:
  - CMS Provider Data - Hospital Compare - provider_name, quality_metrics, compliance_status
  - State Health Department Licenses - facility_name, license_expiration
- **Outreach Message template**:
  ```text
  Subject: 2-star CMS rating during your license renewal cycle
  
  Your health system dropped to 2 stars overall CMS rating in October with license renewals for Memorial, St. Luke's, Riverside, and County General all due by March 31, 2025.
  
  State licensing boards request CMS deficiency documentation during renewals - declining ratings trigger additional scrutiny.
  
  Who's managing the documentation overlap between CMS and state boards?
  ```

#### Play: 3 Form 483s Open During SAM Renewal Window (PQS                     Public Data | Okay - Okay (7.8/10))

- **What's the play?**: Target FDA-regulated manufacturers with multiple Form 483 observations from recent inspections who have SAM.gov registration renewals in the same month as their FDA response deadlines. FDA follow-up audits often reference contract compliance documentation that requires active SAM registration.
- **Why this works**: You're showing specific dates, observation counts, and connecting FDA remediation to procurement compliance - two systems they may not be coordinating. The connection might be slightly reaching, but the timing pressure is real and verifiable.
- **Data Sources**:
  - FDA Establishment Inspection Reports (EIRs) - facility_name, 483_observations, inspection_date
  - SAM.gov - contractor_name, active_contract_end_date
- **Outreach Message template**:
  ```text
  Subject: 3 Form 483s open during your SAM renewal window
  
  Your November FDA inspection left 3 open Form 483 observations with response due February 10, 2025 - same month your SAM.gov registration expires.
  
  FDA follow-up audits often reference contract compliance documentation that requires active SAM registration.
  
  Who's tracking both deadlines in legal ops?
  ```

---

## Onit (onit.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/onit-com)
**Strategic Summary**: Playbook combines internal contract expiration tracking with FDA OAI re-inspection timelines, LinkedIn executive movement data, and SEC 8-K filings to surface supplier agreement risks and vendor relationship vulnerabilities during leadership transitions.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your legal operations

Hi Sarah,

I noticed you recently posted about managing outside counsel relationships on LinkedIn. That's exactly what Onit helps with.

Our platform centralizes contract management, e-billing, and matter management in one place. We've helped Fortune 500 companies reduce legal spend by 10% on average.

Would love to show you how we can help your team. Are you available for a quick 15-minute call next week?

Best,
Account Executive at Onit
```

### ✓ The New Way: GTM Plays

#### Play: 18 Supplier Agreements Expiring During OAI Window (PVP                     Public + Internal | Strong - Strong (9.6/10))

- **What's the play?**: Cross-reference internal contract expiration tracking with FDA OAI classification timeline to identify supplier quality agreements expiring before re-inspection. Deliver a pre-built, prioritized list organized by criticality.
- **Why this works**: This is pure value delivery - you've already done hours of manual tracking and prioritization work they would need to do anyway. The specificity (18 agreements, exact re-inspection window, organized by criticality) proves you understand FDA remediation requirements. No ask, just value.
- **Data Sources**:
  - Onit Contract System - supplier quality agreement expiration dates, agreement types, criticality categorization
  - FDA Inspection Classification Database - OAI classification date, estimated re-inspection timeline
- **Outreach Message template**:
  ```text
  Subject: 18 supplier agreements expiring during your OAI window
  
  Your facility has 18 supplier quality agreements expiring between now and your estimated June re-inspection date.
  
  I pulled the list with supplier names, agreement types, and exact expiration dates prioritized by criticality.
  
  Want the spreadsheet?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's contract data from your system - supplier quality agreements, expiration dates, and criticality categorization.
                    Only works for upselling existing customers, not cold acquisition. The value is in synthesizing their internal contract data with external FDA timelines.

#### Play: Top 5 Renewal Risks This Quarter (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Filter all Q1 contract renewals to surface only the highest-value agreements where the vendor had recent C-suite turnover. Provide complete package with new executive names and LinkedIn profiles for relationship mapping.
- **Why this works**: Legal operations teams are drowning in renewals. You've pre-filtered to the 5 highest-risk contracts and done the executive research legwork. This saves them hours and helps them prioritize relationship management during leadership transitions. The offer to provide LinkedIn profiles shows you've already done the work.
- **Data Sources**:
  - Onit Contract System - renewal dates, contract values, counterparty names
  - LinkedIn Executive Movement - C-suite transitions and announcement dates
  - SEC 8-K Filings - executive departure announcements for public companies
- **Outreach Message template**:
  ```text
  Subject: Your top 5 renewal risks this quarter
  
  You have 12 contracts renewing Q1 2025 - I pulled the 5 highest-value agreements where the vendor had C-suite turnover in the past 90 days.
  
  Total value at risk: $14.2M across these 5 renewals.
  
  Want the list with new executive names and LinkedIn profiles?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's contract portfolio from your system - renewal dates, contract values, and vendor names.
                    Only works for existing customers. The value is correlating their internal renewal pipeline with external executive transition signals.

#### Play: Supplier Agreement Expires During OAI Remediation (PQS                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Identify specific supplier quality agreements expiring between OAI classification and estimated re-inspection window. Surface the timing risk with exact dates and FDA inspection implications.
- **Why this works**: The synthesis of internal contract dates with external FDA re-inspection timing creates genuine strategic value. FDA inspectors specifically verify current supplier agreements during OAI remediation reviews. The specificity (exact supplier name, exact expiration date, exact re-inspection window) proves deep understanding of both their contracts and FDA compliance requirements.
- **Data Sources**:
  - Onit Contract System - supplier quality agreement details, expiration dates
  - FDA Inspection Classification Database - OAI classification dates
  - FDA Re-Inspection Timeline Estimation - typical 6-month window for OAI remediation
- **Outreach Message template**:
  ```text
  Subject: Medline supplier agreement expires during your OAI remediation
  
  Your Medline supplier quality agreement expires April 3rd - that's 45 days before your June OAI re-inspection window.
  
  FDA inspectors specifically look for current supplier agreements when reviewing CAPA effectiveness.
  
  Want me to pull all supplier agreements expiring before your re-inspection?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's supplier agreement data from your contract system - specific suppliers, agreement types, and expiration dates.
                    Only works for existing customers. The value is in connecting their internal contract timeline with external FDA re-inspection requirements.

#### Play: 3 Major Contracts Renewing During Vendor Leadership Changes (PQS                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Identify pattern across multiple high-value contracts all renewing during vendor C-suite transitions. The clustering of leadership changes across multiple vendors creates compounded risk and urgency.
- **Why this works**: One contract renewal during leadership change is notable. THREE contracts totaling $8.4M all facing the same timing issue is a genuine strategic problem requiring prioritization. The pattern recognition shows you're monitoring their entire vendor portfolio, not just cherry-picking one contract. Offers immediate actionable list.
- **Data Sources**:
  - Onit Contract System - Q2 2025 renewal dates, contract values, counterparty details
  - LinkedIn Executive Transitions - C-suite announcements in past 60 days
  - Public Press Releases - vendor leadership changes
- **Outreach Message template**:
  ```text
  Subject: 3 major contracts renewing during vendor leadership changes
  
  You have 3 contracts totaling $8.4M renewing in Q2 2025 - all three vendors announced C-suite transitions in the past 60 days.
  
  New executives often renegotiate inherited agreements within 90 days.
  
  Want the list with renewal dates and new exec names?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's contract renewal pipeline from your system - specific contracts, values, and vendor names for Q2 2025.
                    Only works for existing customers. The pattern recognition across their vendor portfolio is the value.

#### Play: OAI Classification + Supplier Agreements Expiring (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Correlate public FDA OAI classification with internal contract expiration data to identify supplier quality agreements expiring during remediation period. Surface the compliance risk with exact dates and regulatory context.
- **Why this works**: The synthesis is genuinely valuable - combining their internal contract timeline with external FDA enforcement creates strategic timing insight they might miss. Specific facility name, exact OAI date, exact agreement count, and direct FDA compliance connection demonstrates deep understanding of pharmaceutical quality requirements.
- **Data Sources**:
  - Onit Contract System - supplier quality agreement expiration dates
  - FDA Inspection Classification Database - OAI classification dates and facility details
  - FDA Form 483 Database - common observations related to supplier oversight
- **Outreach Message template**:
  ```text
  Subject: Your OAI status + 7 supplier agreements expiring
  
  Your Rockford facility received OAI classification on October 12th - you have 7 supplier quality agreements expiring in the next 120 days.
  
  FDA expects updated supplier oversight during OAI remediation, and expired SQAs are a common 483 observation.
  
  Is someone cross-checking these expirations against your CAPA plan?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's supplier quality agreement data from your contract system with expiration tracking.
                    Only works for existing customers. The value is connecting their internal contract data with external FDA enforcement timeline.

#### Play: IP Litigation Counsel 18% Above Market (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Use aggregated e-billing data across 200+ technology company clients to benchmark the prospect's IP litigation counsel rates. Provide specific rate comparison, annual spend, and calculated savings opportunity.
- **Why this works**: References large dataset (200+ companies) to establish credibility. Shows exact rate overpayment percentage, their actual annual spend, and calculated potential savings. This is proprietary benchmarking data they cannot get elsewhere. The specificity makes it immediately actionable for rate negotiations.
- **Data Sources**:
  - Onit E-Billing System - aggregated outside counsel rates by matter type and industry across 200+ technology clients
  - Annual Spend Tracking - total spend by firm and practice area
- **Outreach Message template**:
  ```text
  Subject: Your IP litigation counsel charges 18% above market
  
  Your primary IP litigation firm bills $520/hour - across 200+ similar tech companies in our system, the median rate is $440/hour for equivalent matters.
  
  You spent $890K with them last year, suggesting $143K in potential rate optimization.
  
  Want the firm-level rate comparison?
  ```
- **Data Requirement**: This play requires aggregated e-billing rate data across 200+ technology company clients, categorized by matter type (IP litigation) with median and percentile benchmarks.
                    This is proprietary data only Onit has - competitors cannot replicate this play. Works for new customer acquisition because YOU have the benchmark data.

#### Play: Contract Renewal During CEO Transition (PQS                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Identify high-value service agreements with auto-renewal dates occurring during vendor CEO transitions. Surface the timing risk with exact contract value, renewal date, and executive departure timeline.
- **Why this works**: The synthesis of internal contract timeline with external executive transition creates genuine strategic insight. New CEOs often review major vendor relationships in first 90 days. The specificity (exact contract value, exact dates, exact executive departure timing) demonstrates you're tracking both their contracts and their vendors' leadership changes.
- **Data Sources**:
  - Onit Contract System - service agreement details, auto-renewal dates, contract values
  - Public Executive Announcements - CEO retirement and transition dates
  - Press Releases - corporate leadership changes
- **Outreach Message template**:
  ```text
  Subject: Your Acme Corp contract renews during CEO transition
  
  Your $2.3M Acme Corp services agreement auto-renews March 15th - Acme just announced their CEO is retiring February 28th.
  
  New leadership often reviews major vendor contracts in their first 90 days.
  
  Should I flag this for early renewal discussion?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's contract data from your system - specific service agreements, renewal dates, and contract values.
                    Only works for existing customers. The value is correlating their internal renewal timeline with external vendor leadership changes.

---

## PCC Energy Group (pccenergy.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/pccenergy-com)
**Strategic Summary**: Playbook (built for Reveal) mines PACER federal dockets to identify law firms facing active TAR methodology challenges, delivering curated defense playbooks with winning briefs and court-tested privilege log templates before response deadlines.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transforming eDiscovery with Transparent AI

Hi [First Name],

I saw your firm recently expanded its litigation practice—congrats! I wanted to reach out because Reveal is revolutionizing eDiscovery with our explainable AI platform.

Unlike traditional black-box TAR solutions, our platform provides complete transparency into AI decision-making, helping legal teams:
• Reduce discovery costs by up to 60%
• Accelerate document review timelines
• Maintain defensible methodologies

We work with AmLaw 100 firms and Fortune 500 companies to streamline their discovery workflows. Would you be open to a 15-minute call to explore how Reveal could benefit your practice?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Defense Playbook for Your Johnson v. State Farm TAR Challenge (PVP                     Public Data | Strong - Strong (9.3/10))

- **What's the play?**: Law firms facing e-discovery methodology challenges get a curated defense playbook with winning briefs, expert declarations, and judicial orders from similar TAR challenges. This targets firms with active motions challenging their AI-driven document review, providing case-specific precedents they can adapt immediately.
- **Why this works**: You're addressing an active fire with immediate deadline pressure. The specificity (knowing their exact case name, motion date, and deadline) passes the "how did they know that?" test. Delivering winning precedents from similar cases provides instant value they'd otherwise spend billable hours researching. This helps them win the case whether they buy or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_filings, filing_date, judge
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: Defense playbook for your Johnson v. State Farm TAR challenge
  
  I mapped your Johnson case TAR motion to 14 similar challenges where firms successfully defended AI methodology.
  
  Pulled the winning briefs, expert declarations, and judicial orders that worked.
  
  Want the defense playbook for your April 12th response?
  ```

#### Play: Privilege Log Template for AI-Assisted Review (PVP                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Law firms ordered to resubmit privilege logs due to AI methodology challenges receive a court-tested template with explanations judges have accepted in similar cases. This targets firms facing specific privilege log rejections where the court questioned AI-driven document classification.
- **Why this works**: The specificity (Judge Martinez, 47 challenged entries, March 28th deadline) proves real research. Providing a ready-to-use template with court-accepted language solves an immediate problem on their calendar. The value is tangible—saves hours of attorney time and reduces risk of further court challenges—whether they engage further or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - E-Discovery Case Database - discovery_issue, document_dispute, ruling_date
- **Outreach Message template**:
  ```text
  Subject: Privilege log template for AI-assisted review
  
  Built a privilege log template that addresses Judge Martinez's 47-entry challenge in cases like yours.
  
  Includes AI methodology explanations courts have accepted in 9 recent antitrust cases.
  
  Want the template for your March 28th resubmission?
  ```

#### Play: Your TAR Methodology Challenged in Johnson v. State Farm (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Target law firms managing active litigation where opposing counsel has filed motions challenging their TAR (Technology-Assisted Review) protocols. PACER dockets reveal specific cases where discovery methodology is under judicial scrutiny, with court-ordered deadlines to justify AI coding decisions.
- **Why this works**: Extreme specificity—you found their actual case name, docket number, motion date, and court deadline. This is a current fire with immediate consequences. The routing question makes it easy to respond. They're wondering "how did you know this?" which is exactly the reaction Blueprint aims for.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, motion_type, judge
  - E-Discovery Case Database - discovery_issue, law_firm, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your TAR methodology challenged in Johnson v. State Farm
  
  Court docket shows opposing counsel filed a motion to compel on March 15th challenging your TAR protocol in Johnson v. State Farm (Case 2:24-cv-01847).
  
  Judge ordered you to provide written justification of AI coding decisions by April 12th.
  
  Who's drafting the AI methodology defense?
  ```

#### Play: AI Methodology Defense for Your TechCorp Sanction (PVP                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Alternative Legal Service Providers (ALSPs) whose clients received sanctions for discovery failures get a methodology defense framework based on ALSPs that successfully defended similar challenges. This targets cases where court orders specifically question the ALSP's TAR transparency.
- **Why this works**: The sanction ($125K, specific client, specific judge, specific date) is public and embarrassing—threatens the ALSP's client relationship and reputation. Providing defenses from 7 similar situations offers immediate value. The transparency gap is precisely what Reveal solves, making this a perfect bridge to the product conversation.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date
  - Lex Machina Litigation Analytics - party_litigation_history, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: AI methodology defense for your TechCorp sanction
  
  Judge Williams' $125K sanction order specifically questions your TAR transparency.
  
  Mapped 7 ALSPs that successfully defended similar challenges with detailed AI workflow documentation.
  
  Want the methodology defense framework?
  ```

#### Play: $125K Sanctions Against Your Client TechCorp (PQS                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Target ALSPs whose clients received court sanctions for deficient ESI (Electronically Stored Information) production, where judicial orders cite lack of TAR transparency as the core problem. This identifies ALSPs with urgent methodology credibility issues that threaten client retention.
- **Why this works**: The specificity (client name, sanction amount, judge, date, case number) proves you did real research. The court order directly implicating ALSP methodology makes this existential—threatens the client relationship. The routing question about protocol review is urgent and practical.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date, parties
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your client TechCorp sanctioned for discovery failures
  
  Judge Williams sanctioned your client TechCorp $125,000 on March 3rd for producing deficient ESI in the patent infringement case (Case 3:24-cv-02156).
  
  Order specifically questions the ALSP's TAR methodology and lack of transparency.
  
  Who's reviewing your AI coding protocols?
  ```

#### Play: Dual-Track Production Protocol for SEC + DOJ Requests (PVP                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Public companies managing parallel SEC civil investigations and DOJ criminal inquiries receive a dual-track protocol showing how other companies navigated this with defensible AI workflows. This targets companies with 8-K disclosures of concurrent regulatory investigations requiring document production to multiple agencies.
- **Why this works**: Parallel investigations create unique pressure—civil and criminal standards differ, but you're using the same document set. Providing precedents from 6 companies in similar situations offers immediate risk mitigation. The value (reducing regulatory/criminal exposure) is tangible whether they buy or not.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, docket_number, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: Dual-track production protocol for SEC + DOJ requests
  
  Your parallel SEC/DOJ investigation requires defensible methodology for both civil and criminal standards.
  
  Mapped 6 companies that successfully navigated this with transparent AI workflows.
  
  Want the dual-track protocol and case examples?
  ```

#### Play: Your Privilege Log in the Sherman Act Case (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target public companies managing antitrust litigation where courts ordered privilege log resubmission due to insufficient AI methodology explanations. PACER dockets reveal specific cases where opposing counsel successfully challenged privilege claims based on lack of TAR transparency.
- **Why this works**: The specificity (case name, judge, deadline, 47 challenged entries) demonstrates real research. AI methodology challenges in privilege contexts are high-stakes—risks waiving privilege entirely. The preparedness question acknowledges urgency without being pushy.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - SEC EDGAR Filings (8-K) - company_name, litigation_summary, case_description
- **Outreach Message template**:
  ```text
  Subject: Your privilege log in the Sherman Act case
  
  Court docket shows Judge Martinez ordered you to re-submit your privilege log by March 28th in US v. Acme Corp (antitrust case).
  
  Opposing counsel challenged 47 entries as insufficiently specific about AI-assisted review.
  
  Is your team prepared to defend how AI flagged those documents?
  ```

#### Play: Defense Brief for Your 12 FOIA Lawsuits (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Federal agencies facing multiple FOIA non-compliance lawsuits get a consolidated defense strategy based on agencies that successfully defended similar challenges. This targets agencies with patterns of FOIA litigation citing inadequate search methodology.
- **Why this works**: 12 lawsuits in Q1 is a pattern that signals systemic process failure. All cite the same issue (search methodology), which Reveal directly addresses. Providing successful defenses from 8 similar agencies offers immediate litigation support. Court-accepted protocols reduce future lawsuit risk.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline, request_status
- **Outreach Message template**:
  ```text
  Subject: Defense brief for your 12 FOIA lawsuits
  
  Your 12 Q1 FOIA lawsuits all cite search methodology inadequacy.
  
  Pulled successful defenses from 8 agencies facing similar challenges plus court-accepted AI search protocols.
  
  Want the consolidated defense strategy?
  ```

#### Play: Standard AI Workflow Documentation for Client Cases (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: ALSPs facing methodology challenges across multiple client cases receive standardized AI workflow documentation templates based on what courts accepted in recent similar cases. This targets ALSPs with patterns of discovery disputes questioning predictive coding transparency.
- **Why this works**: The pattern (3 clients all facing methodology demands) indicates systemic ALSP process issues, not isolated incidents. Court-accepted documentation templates offer immediate tactical value. Standardization improves operational efficiency. Protecting multiple client relationships makes the stakes clear.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity, docket_trends
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, party_litigation_history
- **Outreach Message template**:
  ```text
  Subject: Standard AI workflow documentation for client cases
  
  Your 3 challenged clients all face demands for detailed predictive coding methodology.
  
  Built standardized AI workflow docs based on what courts accepted in 11 recent cases.
  
  Want the documentation templates?
  ```

#### Play: 3 Discovery Motions Filed Against Your Firm This Quarter (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target law firms with multiple discovery methodology challenges in the same quarter, where opposing counsel consistently cites inability to verify AI-driven review decisions. PACER reveals patterns of discovery disputes across a firm's active dockets, indicating systemic process issues rather than isolated incidents.
- **Why this works**: Pattern recognition across 3 specific named cases demonstrates thorough research. The insight (systemic risk vs. isolated incident) is valuable—suggests the firm's standard process is vulnerable. The tracking question is practical and non-confrontational.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_type, filing_date, law_firm
  - E-Discovery Case Database - discovery_issue, case_name, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions filed against your firm this quarter
  
  PACER shows 3 separate motions challenging your document production methodology across Johnson v. State Farm, Martinez class action, and Chen securities case.
  
  All three cite inability to verify AI-driven review decisions.
  
  Is someone tracking the pattern across these cases?
  ```

#### Play: Backlog Reduction Plan for Your 347 Pending Requests (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Federal agencies with large FOIA backlogs receive a backlog reduction roadmap based on agencies that reduced similar volumes by 60% in 6 months using defensible AI search. This targets agencies with publicly disclosed backlogs and increasing processing times.
- **Why this works**: The specificity (347 requests) from public FOIA.gov data proves research. The 60% reduction outcome is compelling. Court-approved methodologies address the agency's litigation risk exposure. The planning tool has value independent of purchase.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline
- **Outreach Message template**:
  ```text
  Subject: Backlog reduction plan for your 347 pending requests
  
  Analyzed 4 agencies that reduced 300+ request backlogs by 60% in 6 months using defensible AI search.
  
  Built a roadmap based on their implementations and court-approved methodologies.
  
  Want the backlog reduction plan?
  ```

#### Play: Remediation Plan for Your DOE Compliance Review (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Universities under Department of Education compliance reviews for inadequate Title IX records preservation receive remediation frameworks based on universities with similar findings that achieved DOE approval. This targets institutions with published compliance findings and imminent remediation deadlines.
- **Why this works**: The April 30th DOE deadline is specific and urgent. Providing approved remediation plans from 3 similar institutions reduces guesswork and risk. DOE acceptance is the key outcome—failure risks federal funding. The compliance framework has immediate value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: Remediation plan for your DOE compliance review
  
  Your April 30th DOE remediation deadline requires documented records preservation improvements.
  
  Pulled accepted remediation plans from 3 universities with similar findings and DOE approval letters.
  
  Want the remediation framework?
  ```

#### Play: 12 FOIA Lawsuits Filed Against Your Agency in Q1 (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target federal agencies with multiple FOIA non-compliance lawsuits in a short period, where plaintiff complaints consistently cite excessive delay and inadequate search methodology. PACER dockets reveal patterns of FOIA litigation indicating systemic agency process failures.
- **Why this works**: 12 lawsuits in Q1 is an alarming pattern that agency leadership cannot ignore. All cite search methodology—directly in Reveal's wheelhouse. The coordination question acknowledges complexity without being judgmental. The litigation defense need is immediate.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline
- **Outreach Message template**:
  ```text
  Subject: 12 FOIA lawsuits filed against your agency in Q1
  
  PACER shows 12 separate FOIA non-compliance lawsuits filed against your agency between January-March 2025.
  
  All cite excessive delay in records production and inadequate search methodology.
  
  Is someone coordinating the litigation defense strategy?
  ```

#### Play: Legal Hold Protocol for Your 8 Title IX Cases (PVP                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Universities managing multiple concurrent Title IX investigations with different preservation scopes and DOE deadlines receive a master legal hold tracker based on protocols from universities that passed DOE compliance reviews. This targets institutions with 990 disclosures of multiple active investigations.
- **Why this works**: The specificity (8 concurrent investigations from 990 filing) proves research. Coordination across multiple investigations with different scopes is genuinely complex. DOE-approved protocols reduce compliance risk. The tracker provides immediate organizational value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Legal hold protocol for your 8 Title IX cases
  
  Your 8 concurrent Title IX investigations each have different preservation scopes and DOE deadlines.
  
  Built a master legal hold tracker based on protocols from 5 universities that passed DOE compliance reviews.
  
  Want the tracker and protocol templates?
  ```

#### Play: DOE Compliance Review at State University (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target universities with published Department of Education compliance review findings citing inadequate Title IX records preservation, where DOE ordered remediation plan submission with specific deadlines. This identifies institutions under regulatory pressure to demonstrate defensible document review processes.
- **Why this works**: Published DOE findings (specific agency, date) prove research. The April 30th remediation deadline is urgent. Records preservation is the exact problem Reveal solves. The routing question (Is GC leading?) is simple and practical.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: DOE compliance review at State University
  
  Department of Education published compliance review findings on February 18th citing inadequate records preservation in 2 Title IX cases at your institution.
  
  DOE ordered remediation plan submission by April 30th.
  
  Is General Counsel leading the response?
  ```

#### Play: SEC + DOJ Both Requesting Discovery from Acme Corp (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target public companies with 8-K disclosures of parallel SEC civil investigations and DOJ criminal inquiries both demanding electronic communications discovery. This identifies companies managing dual-track document production with different legal standards but overlapping document sets.
- **Why this works**: Specific 8-K filing date proves research. Parallel SEC/DOJ pressure is high-stakes—civil plus potential criminal exposure. The defensibility concern is legitimate and urgent. The routing question is practical and easy to answer.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: SEC + DOJ both requesting discovery from Acme Corp
  
  Your 8-K filed January 22nd discloses parallel SEC investigation and DOJ criminal inquiry both demanding electronic communications.
  
  You're producing to two agencies with different standards using the same document set.
  
  Who's ensuring your AI coding methodology is defensible to both?
  ```

#### Play: 3 Discovery Motions Against Clients Using Your Services (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target ALSPs whose top client law firms are facing multiple discovery methodology challenges, where Lex Machina and Docket Navigator reveal higher TAR challenge rates versus peer ALSPs. This identifies ALSPs with client relationship risks due to defensibility gaps in their current AI review processes.
- **Why this works**: Naming 3 specific clients demonstrates research. The pattern (all challenge predictive coding methodology) indicates systemic ALSP issues. AI workflow documentation is the gap Reveal fills. The tracking question is practical and non-threatening.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions against clients using your services
  
  PACER shows 3 motions to compel filed against your clients in February - TechCorp, BioPharma Inc, and Global Logistics.
  
  All three challenge predictive coding methodology and request detailed AI workflow documentation.
  
  Is your team tracking this pattern?
  ```

#### Play: Your Agency's 347 Pending FOIA Requests (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target federal agencies with large FOIA request backlogs and increasing processing times visible through FOIA.gov public data. This identifies agencies under pressure to accelerate records production while maintaining defensible search methodologies.
- **Why this works**: Specific numbers from FOIA.gov (347 requests, 89 increase, processing time 47→63 days) prove thorough research. The trend is concerning and verifiable. Processing time increase demonstrates growing problem. The routing question is practical.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline, document_count
- **Outreach Message template**:
  ```text
  Subject: Your agency's 347 pending FOIA requests
  
  FOIA.gov shows your agency has 347 requests pending over 90 days as of February 2025 - up 89 requests from November.
  
  Your average processing time increased from 47 to 63 days this quarter.
  
  Who's managing the backlog reduction plan?
  ```

#### Play: Your Title IX Investigation Disclosure in the 990 (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target universities with Form 990 disclosures of multiple active Title IX investigations, where Department of Education opened cases with document preservation orders. This identifies institutions managing multiple concurrent investigations requiring coordinated legal hold processes.
- **Why this works**: Specific 990 disclosure (8 investigations, 3 opened in Q4 2024) proves research. Legal hold compliance across 8 cases is genuinely complex. The coordination question is practical and acknowledges operational reality without being judgmental.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Your Title IX investigation disclosure in the 990
  
  Your 2024 Form 990 Schedule O discloses 8 active Title IX investigations at State University.
  
  Department of Education opened 3 of those cases in Q4 2024 with document preservation orders.
  
  Who's managing legal hold across all 8 investigations?
  ```

---

## Reveal (relyhome.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/relyhome-com)
**Strategic Summary**: Playbook uses PACER dockets and e-discovery case databases to target law firms with active TAR methodology challenges, delivering defense playbooks and court-tested privilege log templates before deadlines.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transforming eDiscovery with Transparent AI

Hi [First Name],

I saw your firm recently expanded its litigation practice—congrats! I wanted to reach out because Reveal is revolutionizing eDiscovery with our explainable AI platform.

Unlike traditional black-box TAR solutions, our platform provides complete transparency into AI decision-making, helping legal teams:
• Reduce discovery costs by up to 60%
• Accelerate document review timelines
• Maintain defensible methodologies

We work with AmLaw 100 firms and Fortune 500 companies to streamline their discovery workflows. Would you be open to a 15-minute call to explore how Reveal could benefit your practice?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Defense Playbook for Your Johnson v. State Farm TAR Challenge (PVP                     Public Data | Strong - Strong (9.3/10))

- **What's the play?**: Law firms facing e-discovery methodology challenges get a curated defense playbook with winning briefs, expert declarations, and judicial orders from similar TAR challenges. This targets firms with active motions challenging their AI-driven document review, providing case-specific precedents they can adapt immediately.
- **Why this works**: You're addressing an active fire with immediate deadline pressure. The specificity (knowing their exact case name, motion date, and deadline) passes the "how did they know that?" test. Delivering winning precedents from similar cases provides instant value they'd otherwise spend billable hours researching. This helps them win the case whether they buy or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_filings, filing_date, judge
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: Defense playbook for your Johnson v. State Farm TAR challenge
  
  I mapped your Johnson case TAR motion to 14 similar challenges where firms successfully defended AI methodology.
  
  Pulled the winning briefs, expert declarations, and judicial orders that worked.
  
  Want the defense playbook for your April 12th response?
  ```

#### Play: Privilege Log Template for AI-Assisted Review (PVP                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Law firms ordered to resubmit privilege logs due to AI methodology challenges receive a court-tested template with explanations judges have accepted in similar cases. This targets firms facing specific privilege log rejections where the court questioned AI-driven document classification.
- **Why this works**: The specificity (Judge Martinez, 47 challenged entries, March 28th deadline) proves real research. Providing a ready-to-use template with court-accepted language solves an immediate problem on their calendar. The value is tangible—saves hours of attorney time and reduces risk of further court challenges—whether they engage further or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - E-Discovery Case Database - discovery_issue, document_dispute, ruling_date
- **Outreach Message template**:
  ```text
  Subject: Privilege log template for AI-assisted review
  
  Built a privilege log template that addresses Judge Martinez's 47-entry challenge in cases like yours.
  
  Includes AI methodology explanations courts have accepted in 9 recent antitrust cases.
  
  Want the template for your March 28th resubmission?
  ```

#### Play: Your TAR Methodology Challenged in Johnson v. State Farm (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Target law firms managing active litigation where opposing counsel has filed motions challenging their TAR (Technology-Assisted Review) protocols. PACER dockets reveal specific cases where discovery methodology is under judicial scrutiny, with court-ordered deadlines to justify AI coding decisions.
- **Why this works**: Extreme specificity—you found their actual case name, docket number, motion date, and court deadline. This is a current fire with immediate consequences. The routing question makes it easy to respond. They're wondering "how did you know this?" which is exactly the reaction Blueprint aims for.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, motion_type, judge
  - E-Discovery Case Database - discovery_issue, law_firm, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your TAR methodology challenged in Johnson v. State Farm
  
  Court docket shows opposing counsel filed a motion to compel on March 15th challenging your TAR protocol in Johnson v. State Farm (Case 2:24-cv-01847).
  
  Judge ordered you to provide written justification of AI coding decisions by April 12th.
  
  Who's drafting the AI methodology defense?
  ```

#### Play: AI Methodology Defense for Your TechCorp Sanction (PVP                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Alternative Legal Service Providers (ALSPs) whose clients received sanctions for discovery failures get a methodology defense framework based on ALSPs that successfully defended similar challenges. This targets cases where court orders specifically question the ALSP's TAR transparency.
- **Why this works**: The sanction ($125K, specific client, specific judge, specific date) is public and embarrassing—threatens the ALSP's client relationship and reputation. Providing defenses from 7 similar situations offers immediate value. The transparency gap is precisely what Reveal solves, making this a perfect bridge to the product conversation.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date
  - Lex Machina Litigation Analytics - party_litigation_history, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: AI methodology defense for your TechCorp sanction
  
  Judge Williams' $125K sanction order specifically questions your TAR transparency.
  
  Mapped 7 ALSPs that successfully defended similar challenges with detailed AI workflow documentation.
  
  Want the methodology defense framework?
  ```

#### Play: $125K Sanctions Against Your Client TechCorp (PQS                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Target ALSPs whose clients received court sanctions for deficient ESI (Electronically Stored Information) production, where judicial orders cite lack of TAR transparency as the core problem. This identifies ALSPs with urgent methodology credibility issues that threaten client retention.
- **Why this works**: The specificity (client name, sanction amount, judge, date, case number) proves you did real research. The court order directly implicating ALSP methodology makes this existential—threatens the client relationship. The routing question about protocol review is urgent and practical.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date, parties
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your client TechCorp sanctioned for discovery failures
  
  Judge Williams sanctioned your client TechCorp $125,000 on March 3rd for producing deficient ESI in the patent infringement case (Case 3:24-cv-02156).
  
  Order specifically questions the ALSP's TAR methodology and lack of transparency.
  
  Who's reviewing your AI coding protocols?
  ```

#### Play: Dual-Track Production Protocol for SEC + DOJ Requests (PVP                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Public companies managing parallel SEC civil investigations and DOJ criminal inquiries receive a dual-track protocol showing how other companies navigated this with defensible AI workflows. This targets companies with 8-K disclosures of concurrent regulatory investigations requiring document production to multiple agencies.
- **Why this works**: Parallel investigations create unique pressure—civil and criminal standards differ, but you're using the same document set. Providing precedents from 6 companies in similar situations offers immediate risk mitigation. The value (reducing regulatory/criminal exposure) is tangible whether they buy or not.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, docket_number, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: Dual-track production protocol for SEC + DOJ requests
  
  Your parallel SEC/DOJ investigation requires defensible methodology for both civil and criminal standards.
  
  Mapped 6 companies that successfully navigated this with transparent AI workflows.
  
  Want the dual-track protocol and case examples?
  ```

#### Play: Your Privilege Log in the Sherman Act Case (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target public companies managing antitrust litigation where courts ordered privilege log resubmission due to insufficient AI methodology explanations. PACER dockets reveal specific cases where opposing counsel successfully challenged privilege claims based on lack of TAR transparency.
- **Why this works**: The specificity (case name, judge, deadline, 47 challenged entries) demonstrates real research. AI methodology challenges in privilege contexts are high-stakes—risks waiving privilege entirely. The preparedness question acknowledges urgency without being pushy.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - SEC EDGAR Filings (8-K) - company_name, litigation_summary, case_description
- **Outreach Message template**:
  ```text
  Subject: Your privilege log in the Sherman Act case
  
  Court docket shows Judge Martinez ordered you to re-submit your privilege log by March 28th in US v. Acme Corp (antitrust case).
  
  Opposing counsel challenged 47 entries as insufficiently specific about AI-assisted review.
  
  Is your team prepared to defend how AI flagged those documents?
  ```

#### Play: Defense Brief for Your 12 FOIA Lawsuits (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Federal agencies facing multiple FOIA non-compliance lawsuits get a consolidated defense strategy based on agencies that successfully defended similar challenges. This targets agencies with patterns of FOIA litigation citing inadequate search methodology.
- **Why this works**: 12 lawsuits in Q1 is a pattern that signals systemic process failure. All cite the same issue (search methodology), which Reveal directly addresses. Providing successful defenses from 8 similar agencies offers immediate litigation support. Court-accepted protocols reduce future lawsuit risk.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline, request_status
- **Outreach Message template**:
  ```text
  Subject: Defense brief for your 12 FOIA lawsuits
  
  Your 12 Q1 FOIA lawsuits all cite search methodology inadequacy.
  
  Pulled successful defenses from 8 agencies facing similar challenges plus court-accepted AI search protocols.
  
  Want the consolidated defense strategy?
  ```

#### Play: Standard AI Workflow Documentation for Client Cases (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: ALSPs facing methodology challenges across multiple client cases receive standardized AI workflow documentation templates based on what courts accepted in recent similar cases. This targets ALSPs with patterns of discovery disputes questioning predictive coding transparency.
- **Why this works**: The pattern (3 clients all facing methodology demands) indicates systemic ALSP process issues, not isolated incidents. Court-accepted documentation templates offer immediate tactical value. Standardization improves operational efficiency. Protecting multiple client relationships makes the stakes clear.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity, docket_trends
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, party_litigation_history
- **Outreach Message template**:
  ```text
  Subject: Standard AI workflow documentation for client cases
  
  Your 3 challenged clients all face demands for detailed predictive coding methodology.
  
  Built standardized AI workflow docs based on what courts accepted in 11 recent cases.
  
  Want the documentation templates?
  ```

#### Play: 3 Discovery Motions Filed Against Your Firm This Quarter (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target law firms with multiple discovery methodology challenges in the same quarter, where opposing counsel consistently cites inability to verify AI-driven review decisions. PACER reveals patterns of discovery disputes across a firm's active dockets, indicating systemic process issues rather than isolated incidents.
- **Why this works**: Pattern recognition across 3 specific named cases demonstrates thorough research. The insight (systemic risk vs. isolated incident) is valuable—suggests the firm's standard process is vulnerable. The tracking question is practical and non-confrontational.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_type, filing_date, law_firm
  - E-Discovery Case Database - discovery_issue, case_name, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions filed against your firm this quarter
  
  PACER shows 3 separate motions challenging your document production methodology across Johnson v. State Farm, Martinez class action, and Chen securities case.
  
  All three cite inability to verify AI-driven review decisions.
  
  Is someone tracking the pattern across these cases?
  ```

#### Play: Backlog Reduction Plan for Your 347 Pending Requests (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Federal agencies with large FOIA backlogs receive a backlog reduction roadmap based on agencies that reduced similar volumes by 60% in 6 months using defensible AI search. This targets agencies with publicly disclosed backlogs and increasing processing times.
- **Why this works**: The specificity (347 requests) from public FOIA.gov data proves research. The 60% reduction outcome is compelling. Court-approved methodologies address the agency's litigation risk exposure. The planning tool has value independent of purchase.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline
- **Outreach Message template**:
  ```text
  Subject: Backlog reduction plan for your 347 pending requests
  
  Analyzed 4 agencies that reduced 300+ request backlogs by 60% in 6 months using defensible AI search.
  
  Built a roadmap based on their implementations and court-approved methodologies.
  
  Want the backlog reduction plan?
  ```

#### Play: Remediation Plan for Your DOE Compliance Review (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Universities under Department of Education compliance reviews for inadequate Title IX records preservation receive remediation frameworks based on universities with similar findings that achieved DOE approval. This targets institutions with published compliance findings and imminent remediation deadlines.
- **Why this works**: The April 30th DOE deadline is specific and urgent. Providing approved remediation plans from 3 similar institutions reduces guesswork and risk. DOE acceptance is the key outcome—failure risks federal funding. The compliance framework has immediate value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: Remediation plan for your DOE compliance review
  
  Your April 30th DOE remediation deadline requires documented records preservation improvements.
  
  Pulled accepted remediation plans from 3 universities with similar findings and DOE approval letters.
  
  Want the remediation framework?
  ```

#### Play: 12 FOIA Lawsuits Filed Against Your Agency in Q1 (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target federal agencies with multiple FOIA non-compliance lawsuits in a short period, where plaintiff complaints consistently cite excessive delay and inadequate search methodology. PACER dockets reveal patterns of FOIA litigation indicating systemic agency process failures.
- **Why this works**: 12 lawsuits in Q1 is an alarming pattern that agency leadership cannot ignore. All cite search methodology—directly in Reveal's wheelhouse. The coordination question acknowledges complexity without being judgmental. The litigation defense need is immediate.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline
- **Outreach Message template**:
  ```text
  Subject: 12 FOIA lawsuits filed against your agency in Q1
  
  PACER shows 12 separate FOIA non-compliance lawsuits filed against your agency between January-March 2025.
  
  All cite excessive delay in records production and inadequate search methodology.
  
  Is someone coordinating the litigation defense strategy?
  ```

#### Play: Legal Hold Protocol for Your 8 Title IX Cases (PVP                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Universities managing multiple concurrent Title IX investigations with different preservation scopes and DOE deadlines receive a master legal hold tracker based on protocols from universities that passed DOE compliance reviews. This targets institutions with 990 disclosures of multiple active investigations.
- **Why this works**: The specificity (8 concurrent investigations from 990 filing) proves research. Coordination across multiple investigations with different scopes is genuinely complex. DOE-approved protocols reduce compliance risk. The tracker provides immediate organizational value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Legal hold protocol for your 8 Title IX cases
  
  Your 8 concurrent Title IX investigations each have different preservation scopes and DOE deadlines.
  
  Built a master legal hold tracker based on protocols from 5 universities that passed DOE compliance reviews.
  
  Want the tracker and protocol templates?
  ```

#### Play: DOE Compliance Review at State University (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target universities with published Department of Education compliance review findings citing inadequate Title IX records preservation, where DOE ordered remediation plan submission with specific deadlines. This identifies institutions under regulatory pressure to demonstrate defensible document review processes.
- **Why this works**: Published DOE findings (specific agency, date) prove research. The April 30th remediation deadline is urgent. Records preservation is the exact problem Reveal solves. The routing question (Is GC leading?) is simple and practical.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: DOE compliance review at State University
  
  Department of Education published compliance review findings on February 18th citing inadequate records preservation in 2 Title IX cases at your institution.
  
  DOE ordered remediation plan submission by April 30th.
  
  Is General Counsel leading the response?
  ```

#### Play: SEC + DOJ Both Requesting Discovery from Acme Corp (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target public companies with 8-K disclosures of parallel SEC civil investigations and DOJ criminal inquiries both demanding electronic communications discovery. This identifies companies managing dual-track document production with different legal standards but overlapping document sets.
- **Why this works**: Specific 8-K filing date proves research. Parallel SEC/DOJ pressure is high-stakes—civil plus potential criminal exposure. The defensibility concern is legitimate and urgent. The routing question is practical and easy to answer.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: SEC + DOJ both requesting discovery from Acme Corp
  
  Your 8-K filed January 22nd discloses parallel SEC investigation and DOJ criminal inquiry both demanding electronic communications.
  
  You're producing to two agencies with different standards using the same document set.
  
  Who's ensuring your AI coding methodology is defensible to both?
  ```

#### Play: 3 Discovery Motions Against Clients Using Your Services (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target ALSPs whose top client law firms are facing multiple discovery methodology challenges, where Lex Machina and Docket Navigator reveal higher TAR challenge rates versus peer ALSPs. This identifies ALSPs with client relationship risks due to defensibility gaps in their current AI review processes.
- **Why this works**: Naming 3 specific clients demonstrates research. The pattern (all challenge predictive coding methodology) indicates systemic ALSP issues. AI workflow documentation is the gap Reveal fills. The tracking question is practical and non-threatening.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions against clients using your services
  
  PACER shows 3 motions to compel filed against your clients in February - TechCorp, BioPharma Inc, and Global Logistics.
  
  All three challenge predictive coding methodology and request detailed AI workflow documentation.
  
  Is your team tracking this pattern?
  ```

#### Play: Your Agency's 347 Pending FOIA Requests (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target federal agencies with large FOIA request backlogs and increasing processing times visible through FOIA.gov public data. This identifies agencies under pressure to accelerate records production while maintaining defensible search methodologies.
- **Why this works**: Specific numbers from FOIA.gov (347 requests, 89 increase, processing time 47→63 days) prove thorough research. The trend is concerning and verifiable. Processing time increase demonstrates growing problem. The routing question is practical.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline, document_count
- **Outreach Message template**:
  ```text
  Subject: Your agency's 347 pending FOIA requests
  
  FOIA.gov shows your agency has 347 requests pending over 90 days as of February 2025 - up 89 requests from November.
  
  Your average processing time increased from 47 to 63 days this quarter.
  
  Who's managing the backlog reduction plan?
  ```

#### Play: Your Title IX Investigation Disclosure in the 990 (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target universities with Form 990 disclosures of multiple active Title IX investigations, where Department of Education opened cases with document preservation orders. This identifies institutions managing multiple concurrent investigations requiring coordinated legal hold processes.
- **Why this works**: Specific 990 disclosure (8 investigations, 3 opened in Q4 2024) proves research. Legal hold compliance across 8 cases is genuinely complex. The coordination question is practical and acknowledges operational reality without being judgmental.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Your Title IX investigation disclosure in the 990
  
  Your 2024 Form 990 Schedule O discloses 8 active Title IX investigations at State University.
  
  Department of Education opened 3 of those cases in Q4 2024 with document preservation orders.
  
  Who's managing legal hold across all 8 investigations?
  ```

---

## Reveal (revealdata.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/revealdata-com)
**Strategic Summary**: Playbook uses PACER federal dockets and e-discovery case databases to target law firms facing active TAR methodology challenges with pre-built defense playbooks and court-tested privilege log templates.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transforming eDiscovery with Transparent AI

Hi [First Name],

I saw your firm recently expanded its litigation practice—congrats! I wanted to reach out because Reveal is revolutionizing eDiscovery with our explainable AI platform.

Unlike traditional black-box TAR solutions, our platform provides complete transparency into AI decision-making, helping legal teams:
• Reduce discovery costs by up to 60%
• Accelerate document review timelines
• Maintain defensible methodologies

We work with AmLaw 100 firms and Fortune 500 companies to streamline their discovery workflows. Would you be open to a 15-minute call to explore how Reveal could benefit your practice?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Defense Playbook for Your Johnson v. State Farm TAR Challenge (PVP                     Public Data | Strong - Strong (9.3/10))

- **What's the play?**: Law firms facing e-discovery methodology challenges get a curated defense playbook with winning briefs, expert declarations, and judicial orders from similar TAR challenges. This targets firms with active motions challenging their AI-driven document review, providing case-specific precedents they can adapt immediately.
- **Why this works**: You're addressing an active fire with immediate deadline pressure. The specificity (knowing their exact case name, motion date, and deadline) passes the "how did they know that?" test. Delivering winning precedents from similar cases provides instant value they'd otherwise spend billable hours researching. This helps them win the case whether they buy or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_filings, filing_date, judge
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: Defense playbook for your Johnson v. State Farm TAR challenge
  
  I mapped your Johnson case TAR motion to 14 similar challenges where firms successfully defended AI methodology.
  
  Pulled the winning briefs, expert declarations, and judicial orders that worked.
  
  Want the defense playbook for your April 12th response?
  ```

#### Play: Privilege Log Template for AI-Assisted Review (PVP                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Law firms ordered to resubmit privilege logs due to AI methodology challenges receive a court-tested template with explanations judges have accepted in similar cases. This targets firms facing specific privilege log rejections where the court questioned AI-driven document classification.
- **Why this works**: The specificity (Judge Martinez, 47 challenged entries, March 28th deadline) proves real research. Providing a ready-to-use template with court-accepted language solves an immediate problem on their calendar. The value is tangible—saves hours of attorney time and reduces risk of further court challenges—whether they engage further or not.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - E-Discovery Case Database - discovery_issue, document_dispute, ruling_date
- **Outreach Message template**:
  ```text
  Subject: Privilege log template for AI-assisted review
  
  Built a privilege log template that addresses Judge Martinez's 47-entry challenge in cases like yours.
  
  Includes AI methodology explanations courts have accepted in 9 recent antitrust cases.
  
  Want the template for your March 28th resubmission?
  ```

#### Play: Your TAR Methodology Challenged in Johnson v. State Farm (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Target law firms managing active litigation where opposing counsel has filed motions challenging their TAR (Technology-Assisted Review) protocols. PACER dockets reveal specific cases where discovery methodology is under judicial scrutiny, with court-ordered deadlines to justify AI coding decisions.
- **Why this works**: Extreme specificity—you found their actual case name, docket number, motion date, and court deadline. This is a current fire with immediate consequences. The routing question makes it easy to respond. They're wondering "how did you know this?" which is exactly the reaction Blueprint aims for.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, motion_type, judge
  - E-Discovery Case Database - discovery_issue, law_firm, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your TAR methodology challenged in Johnson v. State Farm
  
  Court docket shows opposing counsel filed a motion to compel on March 15th challenging your TAR protocol in Johnson v. State Farm (Case 2:24-cv-01847).
  
  Judge ordered you to provide written justification of AI coding decisions by April 12th.
  
  Who's drafting the AI methodology defense?
  ```

#### Play: AI Methodology Defense for Your TechCorp Sanction (PVP                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Alternative Legal Service Providers (ALSPs) whose clients received sanctions for discovery failures get a methodology defense framework based on ALSPs that successfully defended similar challenges. This targets cases where court orders specifically question the ALSP's TAR transparency.
- **Why this works**: The sanction ($125K, specific client, specific judge, specific date) is public and embarrassing—threatens the ALSP's client relationship and reputation. Providing defenses from 7 similar situations offers immediate value. The transparency gap is precisely what Reveal solves, making this a perfect bridge to the product conversation.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date
  - Lex Machina Litigation Analytics - party_litigation_history, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: AI methodology defense for your TechCorp sanction
  
  Judge Williams' $125K sanction order specifically questions your TAR transparency.
  
  Mapped 7 ALSPs that successfully defended similar challenges with detailed AI workflow documentation.
  
  Want the methodology defense framework?
  ```

#### Play: $125K Sanctions Against Your Client TechCorp (PQS                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Target ALSPs whose clients received court sanctions for deficient ESI (Electronically Stored Information) production, where judicial orders cite lack of TAR transparency as the core problem. This identifies ALSPs with urgent methodology credibility issues that threaten client retention.
- **Why this works**: The specificity (client name, sanction amount, judge, date, case number) proves you did real research. The court order directly implicating ALSP methodology makes this existential—threatens the client relationship. The routing question about protocol review is urgent and practical.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, sanction_amount, judge, order_date, parties
  - E-Discovery Case Database - discovery_issue, ruling_date, attorney_names
- **Outreach Message template**:
  ```text
  Subject: Your client TechCorp sanctioned for discovery failures
  
  Judge Williams sanctioned your client TechCorp $125,000 on March 3rd for producing deficient ESI in the patent infringement case (Case 3:24-cv-02156).
  
  Order specifically questions the ALSP's TAR methodology and lack of transparency.
  
  Who's reviewing your AI coding protocols?
  ```

#### Play: Dual-Track Production Protocol for SEC + DOJ Requests (PVP                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Public companies managing parallel SEC civil investigations and DOJ criminal inquiries receive a dual-track protocol showing how other companies navigated this with defensible AI workflows. This targets companies with 8-K disclosures of concurrent regulatory investigations requiring document production to multiple agencies.
- **Why this works**: Parallel investigations create unique pressure—civil and criminal standards differ, but you're using the same document set. Providing precedents from 6 companies in similar situations offers immediate risk mitigation. The value (reducing regulatory/criminal exposure) is tangible whether they buy or not.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, docket_number, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: Dual-track production protocol for SEC + DOJ requests
  
  Your parallel SEC/DOJ investigation requires defensible methodology for both civil and criminal standards.
  
  Mapped 6 companies that successfully navigated this with transparent AI workflows.
  
  Want the dual-track protocol and case examples?
  ```

#### Play: Your Privilege Log in the Sherman Act Case (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target public companies managing antitrust litigation where courts ordered privilege log resubmission due to insufficient AI methodology explanations. PACER dockets reveal specific cases where opposing counsel successfully challenged privilege claims based on lack of TAR transparency.
- **Why this works**: The specificity (case name, judge, deadline, 47 challenged entries) demonstrates real research. AI methodology challenges in privilege contexts are high-stakes—risks waiving privilege entirely. The preparedness question acknowledges urgency without being pushy.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, court_orders, judge, deadline_dates
  - SEC EDGAR Filings (8-K) - company_name, litigation_summary, case_description
- **Outreach Message template**:
  ```text
  Subject: Your privilege log in the Sherman Act case
  
  Court docket shows Judge Martinez ordered you to re-submit your privilege log by March 28th in US v. Acme Corp (antitrust case).
  
  Opposing counsel challenged 47 entries as insufficiently specific about AI-assisted review.
  
  Is your team prepared to defend how AI flagged those documents?
  ```

#### Play: Defense Brief for Your 12 FOIA Lawsuits (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Federal agencies facing multiple FOIA non-compliance lawsuits get a consolidated defense strategy based on agencies that successfully defended similar challenges. This targets agencies with patterns of FOIA litigation citing inadequate search methodology.
- **Why this works**: 12 lawsuits in Q1 is a pattern that signals systemic process failure. All cite the same issue (search methodology), which Reveal directly addresses. Providing successful defenses from 8 similar agencies offers immediate litigation support. Court-accepted protocols reduce future lawsuit risk.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline, request_status
- **Outreach Message template**:
  ```text
  Subject: Defense brief for your 12 FOIA lawsuits
  
  Your 12 Q1 FOIA lawsuits all cite search methodology inadequacy.
  
  Pulled successful defenses from 8 agencies facing similar challenges plus court-accepted AI search protocols.
  
  Want the consolidated defense strategy?
  ```

#### Play: Standard AI Workflow Documentation for Client Cases (PVP                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: ALSPs facing methodology challenges across multiple client cases receive standardized AI workflow documentation templates based on what courts accepted in recent similar cases. This targets ALSPs with patterns of discovery disputes questioning predictive coding transparency.
- **Why this works**: The pattern (3 clients all facing methodology demands) indicates systemic ALSP process issues, not isolated incidents. Court-accepted documentation templates offer immediate tactical value. Standardization improves operational efficiency. Protecting multiple client relationships makes the stakes clear.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity, docket_trends
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, party_litigation_history
- **Outreach Message template**:
  ```text
  Subject: Standard AI workflow documentation for client cases
  
  Your 3 challenged clients all face demands for detailed predictive coding methodology.
  
  Built standardized AI workflow docs based on what courts accepted in 11 recent cases.
  
  Want the documentation templates?
  ```

#### Play: 3 Discovery Motions Filed Against Your Firm This Quarter (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target law firms with multiple discovery methodology challenges in the same quarter, where opposing counsel consistently cites inability to verify AI-driven review decisions. PACER reveals patterns of discovery disputes across a firm's active dockets, indicating systemic process issues rather than isolated incidents.
- **Why this works**: Pattern recognition across 3 specific named cases demonstrates thorough research. The insight (systemic risk vs. isolated incident) is valuable—suggests the firm's standard process is vulnerable. The tracking question is practical and non-confrontational.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, motion_type, filing_date, law_firm
  - E-Discovery Case Database - discovery_issue, case_name, attorney_names, law_firm
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions filed against your firm this quarter
  
  PACER shows 3 separate motions challenging your document production methodology across Johnson v. State Farm, Martinez class action, and Chen securities case.
  
  All three cite inability to verify AI-driven review decisions.
  
  Is someone tracking the pattern across these cases?
  ```

#### Play: Backlog Reduction Plan for Your 347 Pending Requests (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Federal agencies with large FOIA backlogs receive a backlog reduction roadmap based on agencies that reduced similar volumes by 60% in 6 months using defensible AI search. This targets agencies with publicly disclosed backlogs and increasing processing times.
- **Why this works**: The specificity (347 requests) from public FOIA.gov data proves research. The 60% reduction outcome is compelling. Court-approved methodologies address the agency's litigation risk exposure. The planning tool has value independent of purchase.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline
- **Outreach Message template**:
  ```text
  Subject: Backlog reduction plan for your 347 pending requests
  
  Analyzed 4 agencies that reduced 300+ request backlogs by 60% in 6 months using defensible AI search.
  
  Built a roadmap based on their implementations and court-approved methodologies.
  
  Want the backlog reduction plan?
  ```

#### Play: Remediation Plan for Your DOE Compliance Review (PVP                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Universities under Department of Education compliance reviews for inadequate Title IX records preservation receive remediation frameworks based on universities with similar findings that achieved DOE approval. This targets institutions with published compliance findings and imminent remediation deadlines.
- **Why this works**: The April 30th DOE deadline is specific and urgent. Providing approved remediation plans from 3 similar institutions reduces guesswork and risk. DOE acceptance is the key outcome—failure risks federal funding. The compliance framework has immediate value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: Remediation plan for your DOE compliance review
  
  Your April 30th DOE remediation deadline requires documented records preservation improvements.
  
  Pulled accepted remediation plans from 3 universities with similar findings and DOE approval letters.
  
  Want the remediation framework?
  ```

#### Play: 12 FOIA Lawsuits Filed Against Your Agency in Q1 (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target federal agencies with multiple FOIA non-compliance lawsuits in a short period, where plaintiff complaints consistently cite excessive delay and inadequate search methodology. PACER dockets reveal patterns of FOIA litigation indicating systemic agency process failures.
- **Why this works**: 12 lawsuits in Q1 is an alarming pattern that agency leadership cannot ignore. All cite search methodology—directly in Reveal's wheelhouse. The coordination question acknowledges complexity without being judgmental. The litigation defense need is immediate.
- **Data Sources**:
  - PACER Federal Dockets - case_name, docket_number, filing_date, case_type, parties
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, response_deadline
- **Outreach Message template**:
  ```text
  Subject: 12 FOIA lawsuits filed against your agency in Q1
  
  PACER shows 12 separate FOIA non-compliance lawsuits filed against your agency between January-March 2025.
  
  All cite excessive delay in records production and inadequate search methodology.
  
  Is someone coordinating the litigation defense strategy?
  ```

#### Play: Legal Hold Protocol for Your 8 Title IX Cases (PVP                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Universities managing multiple concurrent Title IX investigations with different preservation scopes and DOE deadlines receive a master legal hold tracker based on protocols from universities that passed DOE compliance reviews. This targets institutions with 990 disclosures of multiple active investigations.
- **Why this works**: The specificity (8 concurrent investigations from 990 filing) proves research. Coordination across multiple investigations with different scopes is genuinely complex. DOE-approved protocols reduce compliance risk. The tracker provides immediate organizational value.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Legal hold protocol for your 8 Title IX cases
  
  Your 8 concurrent Title IX investigations each have different preservation scopes and DOE deadlines.
  
  Built a master legal hold tracker based on protocols from 5 universities that passed DOE compliance reviews.
  
  Want the tracker and protocol templates?
  ```

#### Play: DOE Compliance Review at State University (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target universities with published Department of Education compliance review findings citing inadequate Title IX records preservation, where DOE ordered remediation plan submission with specific deadlines. This identifies institutions under regulatory pressure to demonstrate defensible document review processes.
- **Why this works**: Published DOE findings (specific agency, date) prove research. The April 30th remediation deadline is urgent. Records preservation is the exact problem Reveal solves. The routing question (Is GC leading?) is simple and practical.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date, resolution_date
- **Outreach Message template**:
  ```text
  Subject: DOE compliance review at State University
  
  Department of Education published compliance review findings on February 18th citing inadequate records preservation in 2 Title IX cases at your institution.
  
  DOE ordered remediation plan submission by April 30th.
  
  Is General Counsel leading the response?
  ```

#### Play: SEC + DOJ Both Requesting Discovery from Acme Corp (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target public companies with 8-K disclosures of parallel SEC civil investigations and DOJ criminal inquiries both demanding electronic communications discovery. This identifies companies managing dual-track document production with different legal standards but overlapping document sets.
- **Why this works**: Specific 8-K filing date proves research. Parallel SEC/DOJ pressure is high-stakes—civil plus potential criminal exposure. The defensibility concern is legitimate and urgent. The routing question is practical and easy to answer.
- **Data Sources**:
  - SEC EDGAR Filings (8-K) - company_name, cik, filing_date, litigation_summary, case_description
  - PACER Federal Dockets - case_name, case_type, parties
- **Outreach Message template**:
  ```text
  Subject: SEC + DOJ both requesting discovery from Acme Corp
  
  Your 8-K filed January 22nd discloses parallel SEC investigation and DOJ criminal inquiry both demanding electronic communications.
  
  You're producing to two agencies with different standards using the same document set.
  
  Who's ensuring your AI coding methodology is defensible to both?
  ```

#### Play: 3 Discovery Motions Against Clients Using Your Services (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target ALSPs whose top client law firms are facing multiple discovery methodology challenges, where Lex Machina and Docket Navigator reveal higher TAR challenge rates versus peer ALSPs. This identifies ALSPs with client relationship risks due to defensibility gaps in their current AI review processes.
- **Why this works**: Naming 3 specific clients demonstrates research. The pattern (all challenge predictive coding methodology) indicates systemic ALSP issues. AI workflow documentation is the gap Reveal fills. The tracking question is practical and non-threatening.
- **Data Sources**:
  - PACER Federal Dockets - case_name, parties, motion_activity
  - Lex Machina Litigation Analytics - litigation_metrics, case_outcomes, attorney_profiles
- **Outreach Message template**:
  ```text
  Subject: 3 discovery motions against clients using your services
  
  PACER shows 3 motions to compel filed against your clients in February - TechCorp, BioPharma Inc, and Global Logistics.
  
  All three challenge predictive coding methodology and request detailed AI workflow documentation.
  
  Is your team tracking this pattern?
  ```

#### Play: Your Agency's 347 Pending FOIA Requests (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target federal agencies with large FOIA request backlogs and increasing processing times visible through FOIA.gov public data. This identifies agencies under pressure to accelerate records production while maintaining defensible search methodologies.
- **Why this works**: Specific numbers from FOIA.gov (347 requests, 89 increase, processing time 47→63 days) prove thorough research. The trend is concerning and verifiable. Processing time increase demonstrates growing problem. The routing question is practical.
- **Data Sources**:
  - Federal FOIA Request Disclosure Logs - agency_name, request_date, request_status, response_deadline, document_count
- **Outreach Message template**:
  ```text
  Subject: Your agency's 347 pending FOIA requests
  
  FOIA.gov shows your agency has 347 requests pending over 90 days as of February 2025 - up 89 requests from November.
  
  Your average processing time increased from 47 to 63 days this quarter.
  
  Who's managing the backlog reduction plan?
  ```

#### Play: Your Title IX Investigation Disclosure in the 990 (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target universities with Form 990 disclosures of multiple active Title IX investigations, where Department of Education opened cases with document preservation orders. This identifies institutions managing multiple concurrent investigations requiring coordinated legal hold processes.
- **Why this works**: Specific 990 disclosure (8 investigations, 3 opened in Q4 2024) proves research. Legal hold compliance across 8 cases is genuinely complex. The coordination question is practical and acknowledges operational reality without being judgmental.
- **Data Sources**:
  - Title IX Case Database - university_name, investigation_status, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Your Title IX investigation disclosure in the 990
  
  Your 2024 Form 990 Schedule O discloses 8 active Title IX investigations at State University.
  
  Department of Education opened 3 of those cases in Q4 2024 with document preservation orders.
  
  Who's managing legal hold across all 8 investigations?
  ```

---

## Zapproved (zapproved.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/zapproved-com)
**Strategic Summary**: Playbook monitors SEC EDGAR 8-K filings for litigation disclosures and delivers proprietary cost and custodian-scope benchmarks to corporate legal teams to quantify outside counsel savings from in-house eDiscovery.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your legal holds

Hi Sarah,

I saw your company just expanded the legal operations team - congrats!

Zapproved helps legal teams automate legal holds and reduce time spent on ediscovery by 70%. We work with 350+ enterprise customers including Fortune 500 companies.

Would you be open to a quick 15-minute call next week to see how we can help?

Best,
Alex
```

### ✓ The New Way: GTM Plays

#### Play: SEC 8-K Litigation Disclosures: Outside Counsel Cost Benchmarks (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, immediately deliver cost benchmarks for similar cases showing how much outside counsel document review typically costs and how in-house review capacity reduces those costs.
- **Why this works**: VPs of Legal Operations are measured on reducing outside counsel spend. This message delivers concrete cost data they can use to justify budget for legal operations software and in-house review capacity. The $220K savings figure directly addresses their primary KPI.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures, filing dates
  - Internal Customer Data - Cost reduction percentages from customer litigations showing in-house vs outside counsel review costs
- **Outreach Message template**:
  ```text
  Subject: Your shareholder suit - outside counsel cost benchmarks
  
  Your March 8-K disclosed securities litigation - our data shows similar cases cost $340K-$580K in outside counsel document review fees.
  
  Companies that review 60% in-house reduce those costs by $220K on average.
  
  Want the cost breakdown for securities litigation ediscovery?
  ```
- **Data Requirement**: This play requires aggregated cost data from customer litigations showing in-house vs outside counsel review costs by case type (securities, product liability, regulatory).
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: SEC 8-K Litigation Disclosures: Custodian Scope Benchmarks (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, deliver benchmarks showing how many custodians similar cases typically require and warn about scope creep during discovery.
- **Why this works**: Legal teams consistently underestimate custodian scope and face compliance gaps when the hold expands 3x during discovery. The 47 custodian benchmark gives them a concrete planning number they can't get elsewhere.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
  - Internal Customer Data - Aggregated custodian count data across customer legal holds by litigation type
- **Outreach Message template**:
  ```text
  Subject: Securities litigation at your company - custodian scope data
  
  Your shareholder derivative suit disclosed in the March 8-K will require legal holds - our data shows securities cases average 47 custodians across 6 departments.
  
  Most legal teams start with 12-15 custodians and expand 3x during discovery, causing compliance gaps.
  
  Want the custodian scope breakdown for similar cases?
  ```
- **Data Requirement**: This play requires aggregated custodian count data across customer legal holds by litigation type, with expansion patterns during discovery.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: SEC 8-K Litigation Disclosures: Discovery Timeline Benchmarks (PVP                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, deliver timeline benchmarks showing typical discovery phases and warning about underestimation patterns.
- **Why this works**: Legal teams need realistic timelines to set expectations with stakeholders and plan resources. The 400+ case dataset gives credibility to the benchmarks and the 62% underestimation stat creates urgency.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
  - Internal Customer Data - Aggregated timeline data across 400+ customer legal holds in securities litigation cases
- **Outreach Message template**:
  ```text
  Subject: Your 8-K litigation - discovery timeline benchmarks
  
  Your March 8-K shareholder suit typically takes 18 months from filing to discovery completion - but 62% of legal teams underestimate hold duration and face custodian expansion.
  
  We track hold timelines across 400+ securities cases and can show you the typical phases.
  
  Want the discovery timeline breakdown for shareholder derivative suits?
  ```
- **Data Requirement**: This play requires aggregated timeline data across 400+ customer legal holds in securities litigation cases, with phase breakdowns and underestimation patterns.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: SEC 8-K Litigation Disclosures: Hold Duration Benchmarks (PVP                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, immediately deliver hold duration benchmarks for similar cases to help them plan resources and set expectations.
- **Why this works**: The 18 month benchmark is genuinely useful planning data the legal team doesn't have. Addressing the 40% underestimation pattern shows you understand their blind spots and helps them avoid resource planning failures.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
  - Internal Customer Data - Aggregated hold duration data across customer litigations by case type
- **Outreach Message template**:
  ```text
  Subject: Your 8-K disclosed litigation - 18 month hold average
  
  Your March 8-K disclosed the shareholder derivative suit - our data shows similar securities cases average 18 months from filing to discovery completion.
  
  Most legal teams underestimate hold duration by 40% and face scope creep when custodians aren't tracked from day one.
  
  Want the benchmark data for securities litigation hold timelines?
  ```
- **Data Requirement**: This play requires aggregated hold duration data across customer litigations by case type (securities, product liability, regulatory), with underestimation patterns.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: SEC 8-K Litigation Disclosures: Data Preservation Scope (PVP                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, deliver system scope benchmarks showing typical preservation requirements across Microsoft 365, email archives, and collaboration tools.
- **Why this works**: The 78% expansion to collaboration tools stat addresses the legal team's IT dependency pain point. The system scope breakdown helps them coordinate with IT and plan multi-system preservation.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
  - Internal Customer Data - System scope expansion data across customer legal holds by litigation type
- **Outreach Message template**:
  ```text
  Subject: 8-K litigation disclosure - your data preservation scope
  
  Your March 8-K shareholder suit will require holds across Microsoft 365, email archives, and likely Slack - our data shows 78% of securities cases expand to collaboration tools during discovery.
  
  Most IT teams can't deploy holds across all three systems without legal operations coordination.
  
  Want the system scope breakdown for securities litigation holds?
  ```
- **Data Requirement**: This play requires data on system scope expansion across customer legal holds by litigation type (Microsoft 365, Google Vault, Slack, email archives).
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: SEC 8-K Litigation Disclosures: Custodian Compliance Tracking (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, ask who's handling custodian compliance tracking while highlighting the 40-50 custodian scope and visibility challenges.
- **Why this works**: The 40-50 custodian range is realistic and concerning. Tracking compliance is a real pain point for VPs of Legal Operations who lack visibility into who's acknowledged holds and who's non-compliant. This addresses a specific blind spot.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures, filing dates
- **Outreach Message template**:
  ```text
  Subject: Shareholder suit from your 8-K - custodian tracking ready?
  
  Your March 8-K disclosed the shareholder derivative suit - these cases typically involve 40-50 custodians across multiple departments.
  
  Without automated tracking, legal teams lose visibility into who's acknowledged holds and who's non-compliant.
  
  Who's handling custodian compliance tracking?
  ```

#### Play: SEC 8-K Litigation Disclosures: Legal Hold Deployment (PQS                     Public Data | Okay - Okay (7.8/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, ask who's managing legal hold deployment while highlighting the 48-hour timeline and typical custodian scope.
- **Why this works**: The specific 8-K filing reference shows real research. The 48-hour timeline creates genuine urgency. Securities litigation scope (finance, legal, exec) is accurate. But the insight is somewhat obvious - they know they have litigation and need holds.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
- **Outreach Message template**:
  ```text
  Subject: Your March 8-K litigation disclosure - hold deployment?
  
  Your March 8-K disclosed the shareholder derivative suit against the board.
  
  Securities litigation typically requires holds across finance, legal, and executive teams within 48 hours of filing.
  
  Is someone already managing the legal hold deployment?
  ```

#### Play: SEC 8-K Litigation Disclosures: Multi-System Data Preservation (PQS                     Public Data | Okay - Okay (7.6/10))

- **What's the play?**: When a public company files an 8-K disclosing securities litigation, ask if IT is handling multi-system preservation deployment while highlighting typical 3-5 day delays.
- **Why this works**: The specific 8-K filing reference shows research. Multi-system preservation is the exact pain point legal teams face. The 3-5 day delay is realistic and concerning. But the insight is somewhat obvious - they know they need multi-system holds.
- **Data Sources**:
  - SEC EDGAR Database - 8-K current reports, litigation disclosures
- **Outreach Message template**:
  ```text
  Subject: March 8-K litigation - multi-system data preservation
  
  Your March 8-K disclosed shareholder litigation requires immediate data preservation across Microsoft 365, email archives, and collaboration tools.
  
  Most legal teams depend on IT to deploy holds across these systems, creating 3-5 day delays.
  
  Is IT already working on the preservation deployment?
  ```

---

## iManage (imanage.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/imanage-com)
**Strategic Summary**: Playbook outlines the Blueprint GTM methodology for legal tech using PACER court records, state bar directories, and case filing velocity signals to identify firms in compliance or growth situations.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Strong PQS (8.0/10)

            Trigger Event: Law firm has court-ordered document production deadline within 30-90 days AND hired 5+ associates in past quarter

            Why This Works: The prospect knows they have an eDiscovery case. They know they hired new attorneys. But they haven't quantified the INTERACTION between these two facts—that new attorneys who don't know the file structure slow eDiscovery response time. This synthesis creates a moment of realization: "Oh, that's why our last document production took so long.")

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - PACER Federal Court Records - Search case dockets for document production orders and deadlines
  - Indeed Jobs API + LinkedIn Jobs - Track attorney hiring velocity by firm
  - Martindale-Hubbell - Verify firm size and structure
  - Data Source: PACER API - docket_entries[].text search for document production deadlines
  - Calculation: Extract deadline date from docket order → Calculate days until deadline from current date
  - Confidence: 95% (pure government data, court order is public record)
  - Verification: Prospect can verify by searching PACER case 1:24-cv-03847 SDNY
  - Data Source: Indeed + LinkedIn Jobs API - company_name, job_title="Associate Attorney", posting_date in Q1 2025
  - Calculation: Count job postings matching criteria in Jan-Mar 2025
  - Confidence: 80% (job postings are proxy for hires; some hires may not be posted publicly)
  - Verification: Prospect can check HR records for Q1 associate start dates
  - Data Source: Industry benchmark - EDRM eDiscovery metrics + assumption (new attorneys 2-3x slower at document location)
  - Calculation: Baseline document retrieval time (4-6 days) × new attorney inefficiency factor (2x) = 8-12 day delay
  - Confidence: 60% (industry benchmark + reasonable assumption, not firm-specific)
  - Disclosure: Word "typically" signals this is an estimate
  - Situation Recognition: 9/10 (hyper-specific case number, exact deadline, hire count)
  - Data Credibility: 8/10 (PACER data is verifiable, hire count is directionally correct)
  - Insight Value: 7/10 (connection between new hires and eDiscovery timeline is somewhat non-obvious)
  - Effort to Reply: 9/10 ("Want the full analysis?" = one-word reply)
  - Emotional Resonance: 7/10 (creates mild urgency with 34-day countdown)

#### Play:  (PQS |  - Solid PQS (7.2/10)

            Alternative Message (Same Segment):

            Subject: 34 days to produce

Case 1:24-cv-03847 requires document production by May 15—that's 34 days with 7 Q1 associates still learning your file structure.

Most firms underestimate how new attorney onboarding slows eDiscovery by 40-60% in the first 90 days.

Does this timeline match what your team is seeing?

            
                Calculation Worksheet
                CLAIM (REVISED): "new attorney onboarding slows eDiscovery by 40-60% in first 90 days"
                
                    Data Source: Association of Corporate Counsel eDiscovery survey - reports 50% efficiency loss for new legal staff in first quarter
                    Calculation: Apply 50% (+/- 10% margin) to eDiscovery document collection phase
                    Confidence: 55% (industry survey + extrapolation to eDiscovery context)
                    Disclosure: "Most firms" signals this is industry data, not their specific numbers
                
            

            Buyer Critique Score: 7.2/10 - Slightly lower than 1A because industry benchmark feels less compelling than firm-specific delay estimate, but still passes Strong PQS threshold.)

- **What's the play?**: 
- **Why this works**: 

#### Play:  (PQS |  - Strong PQS (8.6/10)

            Trigger Event: Law firm's federal case filings increased 30%+ year-over-year with zero attorney hiring in past 6 months

            Why This Works: The prospect knows they're busier. But they haven't seen the QUANTIFICATION of exactly how much busier (30% more cases, exact numbers) alongside the CONSTRAINT (same headcount). This creates a "capacity crisis" realization—they're scaling work without scaling resources. The non-obvious insight is the RATIO: more documents per attorney, same manual retrieval systems.)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - PACER Federal Court Records - Track case filing counts by firm and year
  - Indeed + LinkedIn Jobs - Detect absence of attorney job postings (proxy for no hiring)
  - Martindale-Hubbell - Verify firm attorney count
  - Data Source: PACER API - GET /cases?firm="[Firm Name]"&filing_year=[YEAR]
  - Calculation: COUNT(cases where filing_year=2024) = 43; COUNT(cases where filing_year=2023) = 33; % change = (43-33)/33 = 30.3%
  - Confidence: 95% (pure government data, public court records)
  - Verification: Search PACER for firm name, filter by year, count cases
  - Data Source: Indeed + LinkedIn Jobs API - Search for attorney job postings at firm in past 6 months
  - Calculation: GET /jobs?company="[Firm Name]"&title="Attorney"&date_posted=past_6_months → COUNT() = 0
  - Confidence: 70% (absence of postings doesn't guarantee no hires; some firms hire via referrals without posting)
  - Verification: Check HR records for attorney hires Oct 2024 - April 2025
  - Data Source: Martindale-Hubbell Legal Directory - attorney_count field from firm profile
  - Calculation: Direct field value = 237
  - Confidence: 90% (authoritative legal directory, self-reported by firms)
  - Verification: Check firm's website "About" page or Martindale profile
  - Situation Recognition: 10/10 (exact case counts, firm name, headcount—hyper-specific)
  - Data Credibility: 9/10 (PACER + Martindale are authoritative, fully verifiable)
  - Insight Value: 8/10 (quantification of 30% with exact numbers is new insight, even if prospect knew they were "busier")
  - Effort to Reply: 9/10 (yes/no question, very easy)
  - Emotional Resonance: 7/10 (creates realization of quantifiable squeeze)

#### Play:  (PQS |  - Solid PQS (7.6/10)

            Alternative Message (Same Segment):

            Subject: 30% more cases, same staff

I pulled your PACER filing data—43 federal cases in 2024 vs 33 in 2023, but your headcount held at 237.

Most firms see document retrieval time increase 50% faster than caseload when scaling without DMS upgrades.

Does this match what your team is experiencing?

            
                Calculation Worksheet
                CLAIM: "document retrieval time increase 50% faster than caseload"
                
                    Data Source: Legal technology survey data - document retrieval scales non-linearly with caseload
                    Calculation: Industry research suggests retrieval time scales at 1.5x rate of caseload growth → 30% caseload × 1.5x = 45% retrieval increase (rounded to "50% faster")
                    Confidence: 55% (industry benchmark, not firm-specific)
                    Disclosure: "Most firms" indicates industry data
                
            

            Buyer Critique Score: 7.6/10 - Lower than 2A because industry stat is less compelling than firm-specific numbers, but still passes Solid PQS threshold.)

- **What's the play?**: 
- **Why this works**: 

---

