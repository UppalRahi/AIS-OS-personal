# GTM Playbooks: Other

Curated list of data-driven GTM Playbooks for the **Other** vertical. Use these to brainstorm messaging, trigger events, and PVP angles.

---

## AGRIVI (agrivi.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/agrivi-com)
**Strategic Summary**: The playbook targets farms on the FDA Food Traceability List approaching harvest seasons and farms with active pesticide applicator licenses, using USDA NASS data to create urgency around FSMA compliance deadlines and retailer contract risk.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transform Your Farm Operations

Hi [First Name],

I saw your farm is growing and I wanted to reach out about AGRIVI's farm management platform.

We help farms like yours improve efficiency and visibility across operations. Our platform centralizes all your production data so you can make better decisions.

Would you be interested in seeing a demo?

Best,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: FSMA Covered Farms on Food Traceability List (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target farms on FDA's Food Traceability List for leafy greens with harvest seasons approaching. The compliance deadline was January 20, 2026, and their spring harvest will be the first real test of their traceability systems.
                    If they can't provide lot-level traceability within 24 hours when a retailer demands it, they lose the contract immediately.
- **Why this works**: The FDA list is publicly verifiable, which creates instant credibility. The retailer contract risk is immediate and real - this isn't about regulatory fines, it's about revenue loss from broken contracts.
                    The timing (March harvest, 62 days from deadline) aligns perfectly with their operational reality, making this feel urgent rather than spammy.
- **Data Sources**:
  - FDA Firm and Supplier Database - FSMA registration status, farm location, Food Traceability List inclusion
  - USDA NASS Quick Stats - Regional harvest schedules by crop type
- **Outreach Message template**:
  ```text
  Subject: You're on FDA's Food Traceability List - March harvest
  
  Your farm grows leafy greens and is on FDA's Food Traceability List - compliance deadline was January 20, 2026, but your March 2025 harvest is already high-risk.
  
  If a retailer demands lot-level traceability during this harvest and you can't provide it within 24 hours, you lose the contract.
  
  Who's running your traceability testing?
  ```

#### Play: Pesticide Licensed Farms with Recent Application Activity (PQS                     Public Data | Okay - Okay (7.7/10))

- **What's the play?**: Target farms with active pesticide applicator licenses showing recent application activity. These farms must manually coordinate crew scheduling for each application, and peer farms with similar application frequencies report 25% lower labor costs using automated systems.
- **Why this works**: The specific license number increases credibility and proves you've done real research. The October timing is recent and relevant, making this feel like a timely observation rather than generic outreach.
                    The peer comparison (25% lower costs) provides concrete evidence of inefficiency without being accusatory.
- **Data Sources**:
  - State Agriculture Department License Databases - Pesticide applicator license numbers, application dates, farm location
  - USDA NASS Quick Stats - Regional application frequency benchmarks
- **Outreach Message template**:
  ```text
  Subject: Your pesticide license shows 3 applications in October
  
  Your farm's pesticide applicator license (CA-DPR #45821) shows 3 applications in October 2024 - all required manual crew coordination.
  
  Peer farms with similar application frequencies use automated work order systems and report 25% lower labor costs.
  
  Who schedules your pesticide application crews?
  ```

#### Play: Cooperative Members with Expiring Certifications (PQS                     Public Data | Okay - Okay (7.6/10))

- **What's the play?**: Target agricultural cooperatives with member farms holding organic or GAP certifications expiring within 90 days. If any member farm's certification lapses, the entire cooperative's buyer contracts require re-verification, putting all members at risk.
- **Why this works**: The specific number (8 farms) and timeframe (Q2 2025) create credibility. Cooperative contract risk is real - one farm's failure affects everyone, which makes this a coordination problem the manager must solve.
                    The weakness is not providing farm names, which prevents immediate verification, but the routing question helps identify the right internal contact.
- **Data Sources**:
  - USDA Organic Integrity Database - Certification status and expiration dates
  - USDA GAP/GHP Database - GAP certification status and timelines
  - USDA Agricultural Cooperative Statistics - Cooperative member counts
- **Outreach Message template**:
  ```text
  Subject: 8 of your member farms have certifications expiring Q2
  
  Your cooperative has 8 member farms with organic or GAP certifications expiring between April and June 2025.
  
  If any farm's certification lapses, the entire cooperative's buyer contracts require re-verification.
  
  Who's tracking member certification renewals?
  ```

#### Play: Real-Time Compliance Tracker for Cooperatives (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Deliver a real-time compliance tracker showing certification expiration dates, documentation gaps, and traceability system compatibility across all member farms. The cooperative manager gets proactive visibility into which farms are non-compliant before auditors discover it.
- **Why this works**: The tracker is immediately useful for coordination - this directly addresses the manager's pain of herding 47+ independent operations toward compliance. It's proactive risk management that helps them avoid audit failures.
                    The easy yes/no question removes friction from responding.
- **Data Sources**:
  - USDA Agricultural Cooperative Statistics - Cooperative registration and member counts
  - USDA Organic Integrity Database - Member farm certification expiration dates
  - Internal Customer Data - Documentation completeness and system usage by farm location
- **Outreach Message template**:
  ```text
  Subject: Member farm compliance tracker for your 47 farms
  
  I built a real-time compliance tracker for your cooperative's 47 member farms - shows certification expiration dates, documentation gaps, and traceability system compatibility.
  
  You'll know which farms are non-compliant before the auditor does.
  
  Want the tracker?
  ```
- **Data Requirement**: This play assumes your company has:
                    Aggregated public certification data cross-referenced with member farm lists, plus internal tracking of which farms use different traceability systems (FarmLogs, AgriWebb, paper records, etc.)
                    Combined with cooperative member lists from USDA to create farm-specific compliance tracking.

#### Play: Farm-by-Farm Compliance Report for Cooperatives (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Deliver a complete compliance audit showing which member farms use different traceability systems, which have expiring certifications, and which have incomplete spray records. The report gives the cooperative manager everything needed to coordinate members and avoid certification risks.
- **Why this works**: Specific numbers (47 farms, 12 different systems, 8 expiring certifications, 5 incomplete records) increase credibility. The report offer is immediately actionable and directly addresses the manager's coordination pain.
                    The easy yes/no response removes friction.
- **Data Sources**:
  - USDA Agricultural Cooperative Statistics - Member farm counts
  - USDA Organic Integrity Database - Certification expiration dates
  - Internal Customer Data - Software usage by farm, documentation completeness
- **Outreach Message template**:
  ```text
  Subject: I mapped all 47 of your member farms' compliance gaps
  
  I pulled data on your cooperative's 47 member farms and found 12 using different traceability systems, 8 with expiring certifications in Q2 2025, and 5 with incomplete spray records.
  
  You can't enforce documentation standards without knowing who's non-compliant.
  
  Want the full farm-by-farm compliance report?
  ```
- **Data Requirement**: This play assumes your company has:
                    Cross-referenced cooperative member lists with public certification databases AND internal data showing which farms use competing software vs. your platform vs. paper records
                    If you have this data, this play becomes highly differentiated - competitors can't replicate it.

#### Play: 24-Hour Traceability Test Scenario (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Deliver a pre-built 24-hour traceability test using the farm's typical lot sizes and retailer specifications. The test lets them validate their system before the first retailer audit, preventing contract loss from failed traceability requirements.
- **Why this works**: The March 15 harvest date is verifiable from planting schedules, creating urgency. The test scenario is immediately useful preparation, and the retailer audit threat is real - failed traceability = lost contracts.
                    Easy yes/no response removes friction.
- **Data Sources**:
  - USDA NASS Quick Stats - Regional planting and harvest schedules
  - FDA FSMA Database - Food Traceability List requirements
  - Internal Customer Data - Typical lot sizes and retailer traceability specifications by farm
- **Outreach Message template**:
  ```text
  Subject: Your traceability test for March 15 harvest
  
  Your strawberry harvest starts March 15, 2025 - I built a 24-hour traceability test scenario using your farm's typical lot sizes and retailer requirements.
  
  If you can't pass this test, you'll fail the first retailer audit and lose the contract.
  
  Want the test scenario?
  ```
- **Data Requirement**: This play assumes your company has:
                    Knowledge of the farm's crop type, planting schedule, typical lot sizes, and retailer traceability requirements (24-hour window, specific data fields, etc.)
                    Combined with public harvest timing data to create farm-specific test scenarios.

#### Play: FSMA Traceability Test Checklist (PVP                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Deliver a complete 24-hour traceability test checklist customized for the farm's March leafy greens harvest. The checklist lets them validate their system can trace a lot from field to cooler within the FSMA-required 24-hour window, preventing retailer audit failures.
- **Why this works**: March harvest timing is accurate from public data, and the 24-hour requirement is a real FSMA rule. The test checklist is immediately actionable preparation.
                    Low-commitment ask (just want the checklist?) makes responding easy.
- **Data Sources**:
  - FDA FSMA Database - 24-hour traceability requirements
  - USDA NASS Quick Stats - Regional harvest timing by crop
  - Internal Customer Data - Typical lot sizes and retailer specifications
- **Outreach Message template**:
  ```text
  Subject: 24-hour traceability test for your March harvest
  
  Your farm's March 2025 leafy greens harvest requires 24-hour lot-level traceability under FSMA rules - I built a test using your typical lot sizes and retailer specs.
  
  If you can't trace a lot from field to cooler in under 24 hours, you'll fail the first retailer audit.
  
  Want the test checklist?
  ```
- **Data Requirement**: This play assumes your company has:
                    Knowledge of the farm's crop type, lot sizes, and typical retailer traceability requirements
                    This helps the farm manager prepare for retailer audits and maintain contracts.

#### Play: Peer Labor Cost Comparison Report (PVP                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Deliver a peer comparison report showing the farm's Q3 labor costs against 23 similar operations in their county. The breakdown by crop, crew size, and overtime patterns shows exactly where the efficiency gap exists.
- **Why this works**: The peer comparison (23 farms) feels legitimate and localized (Monterey County). The breakdown by crop/crew is immediately actionable, directly addressing cost pressure every farm manager feels.
                    Low-commitment ask makes responding easy.
- **Data Sources**:
  - Internal Customer Data - Aggregated labor costs by region, crop type, and farm size
  - USDA NASS Quick Stats - County-level production data for peer matching
- **Outreach Message template**:
  ```text
  Subject: Your Q3 labor costs vs. 23 peer farms
  
  I compared your farm's Q3 2024 labor costs against 23 peer farms in Monterey County with similar acreage - you're spending 38% more per acre.
  
  The analysis breaks down by crop, crew size, and overtime patterns so you can see exactly where the gap is.
  
  Want the peer comparison report?
  ```
- **Data Requirement**: This play assumes your company has:
                    Internal customer data to benchmark labor costs by region, crop type, and farm size across 50+ operations
                    If you have this data, this play is highly differentiated - public sources don't provide operational cost benchmarks.

#### Play: Labor Savings Breakdown Analysis (PVP                     Public + Internal | Strong - Strong (8.0/10))

- **What's the play?**: Deliver a complete labor optimization analysis showing $340K in potential annual savings from reducing overtime and improving work order scheduling. The breakdown shows exactly which crews, days, and crops have inefficiencies.
- **Why this works**: $340K savings is compelling and specific. The crew-level detail makes it immediately actionable rather than vague advice.
                    The weakness is assuming knowledge of exact costs creates some skepticism, but the specific number and detailed breakdown overcome this.
- **Data Sources**:
  - Internal Customer Data - Labor cost modeling based on farm size, crop mix, and regional wage data
  - USDA NASS Quick Stats - Regional labor cost benchmarks
- **Outreach Message template**:
  ```text
  Subject: I found $340K in labor savings for your farm
  
  I analyzed your Q3 2024 harvest labor costs ($847K) against optimal crew allocation patterns - you could save $340,000 annually by reducing overtime and improving work order scheduling.
  
  The analysis shows exactly which crews, which days, and which crops have the inefficiencies.
  
  Want the savings breakdown?
  ```
- **Data Requirement**: This play assumes your company has:
                    Labor cost modeling capability based on farm size, crop mix, and regional wage data to estimate potential savings
                    This assumes AGRIVI can model labor optimization based on operational parameters rather than having actual cost records.

#### Play: Farm Labor Cost Comparison by Crop (PVP                     Public + Internal | Okay - Okay (7.9/10))

- **What's the play?**: Deliver a detailed labor cost comparison showing the farm spent $847K on harvest labor in Q3 - 38% above the county average. The breakdown by crew and crop identifies where allocation inefficiencies exist.
- **Why this works**: Very specific numbers ($847K) increase credibility. County-level peer comparison is relevant and localized. The breakdown offer is actionable.
                    Skepticism about knowing exact costs is a weakness, but the specific amount and county comparison partially overcome this.
- **Data Sources**:
  - Internal Customer Data - Estimated labor costs from farm size, crop type, and regional wage data
  - USDA NASS Quick Stats - County-level labor cost benchmarks
- **Outreach Message template**:
  ```text
  Subject: You spent $847K on harvest labor in Q3
  
  Your farm spent $847,000 on harvest labor in Q3 2024 - that's 38% above the $614,000 average for farms your size in Monterey County.
  
  The gap suggests crew allocation inefficiencies or overtime costs that could be reduced.
  
  Want the breakdown by crew and crop?
  ```
- **Data Requirement**: This play assumes your company has:
                    Ability to estimate labor costs from farm size, crop type, and regional wage data, OR internal customer benchmarks to model typical spending
                    Combined with USDA county-level data to create localized peer comparisons.

---

## Athena AG (athenaag.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/athenaag-com)
**Strategic Summary**: The playbook mines state OCM license databases and compliance enforcement records to identify cultivation facilities with open violations approaching renewal windows, creating urgency around license suspension risk during regulatory review.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Optimize Your Cannabis Cultivation

Hi [Name],

I saw your post about expanding your grow operation and wanted to reach out!

Athena AG provides science-backed nutrient systems that help cannabis cultivators achieve consistent, premium-quality harvests. Our clients see improved yields and reduced operational costs.

We've helped companies like Jungle Boys achieve industry-leading results. I'd love to show you how we can help your facility too.

Are you available for a quick 15-minute call this week?

Best,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: License Renewal Window with Compliance Violation History (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target cultivation facilities with licenses expiring in the next 90 days that have documented METRC or quality-related compliance violations in the past 12 months. These facilities face heightened renewal scrutiny - unresolved violations can trigger license suspension or denial.
                    The intersection of renewal deadline + violation history creates maximum urgency. Quality consistency directly impacts compliance status, making Athena AG's standardized nutrient protocols the exact solution these facilities need before renewal inspection.
- **Why this works**: You're not pitching nutrients. You're demonstrating awareness of their specific compliance risk at the exact moment it matters most. The specificity (exact expiration date, violation categories) proves you're not guessing - you pulled their records. This isn't a sales email, it's a compliance intelligence alert.
- **Data Sources**:
  - New York OCM Licenses (Socrata Open Data) - License_Expiration_Date, License_Status, Facility_Name
  - New York State OCM Compliance Enforcement Actions - Violation_Category, Enforcement_Status, Corrective_Action_Plan_Status
- **Outreach Message template**:
  ```text
  Subject: Your Colorado license renewal opens January 15th
  
  Your Colorado cultivation license renews January 15th and you have 2 open compliance violations from August (pesticide documentation and waste disposal).
  
  Unresolved violations can trigger license suspension or denial at renewal.
  
  Who's handling the violation remediation before January?
  ```

#### Play: License Renewal Window with Compliance Violation History (Variant 2) (PQS                     Public Data | Strong - Strong (7.9/10))

- **What's the play?**: Same targeting strategy as above, but with slightly different framing emphasizing the enhanced review process that facilities with violations face during renewal.
- **Why this works**: The phrase "still showing as open" implies you checked their status recently, adding recency and urgency. By asking if someone is "already working with the state," you're giving them an easy routing question while subtly suggesting this might be falling through the cracks.
- **Data Sources**:
  - New York OCM Licenses - License_Expiration_Date, Facility_Name
  - New York OCM Compliance Enforcement Actions - Violation_Category, Enforcement_Status
- **Outreach Message template**:
  ```text
  Subject: 2 open violations before your January renewal
  
  You have 2 compliance violations from August (pesticide documentation gap and waste disposal) still showing as open in Colorado's tracking system.
  
  License renewals with unresolved violations get flagged for enhanced review or denial.
  
  Is someone already working with the state on remediation?
  ```

#### Play: Facility Expansion Immediately Post-Approval (PQS                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Target cultivation facilities that received capacity expansion permit approvals within the past 30 days. These facilities are entering the highest-risk operational phase where nutrient protocol scaling failures cause permanent quality damage. The expansion approval is a matter of public record with specific square footage and location data.
- **Why this works**: The timing is perfect - they just got approved and are likely in the planning phase. The 20-30% yield drop statistic is a genuine concern they may not have considered. By asking who's designing the nutrient program, you're positioning yourself as the expert they need to consult right now.
- **Data Sources**:
  - California DCC License Summary Report - License_Issued_Date (for new expanded capacity licenses)
  - Massachusetts Cannabis Control Commission Open Data - License_Type, License_Issuance_Date
- **Outreach Message template**:
  ```text
  Subject: Your Michigan expansion approved December 3rd
  
  Michigan approved your 25,000 sq ft expansion permit on December 3rd for the Ann Arbor facility.
  
  Most cultivation expansions experience 20-30% yield drop in the first 2 cycles due to nutrient protocol scaling issues.
  
  Who's designing the nutrient program for the new canopy space?
  ```
- **Data Requirement**: This play assumes your company has:
                    Internal benchmarking data on yield performance during facility expansions across multiple customers, showing typical first-cycle performance drops when nutrient protocols aren't properly scaled.
                    Combined with public permit approval data to identify the exact moment of expansion.

#### Play: Facility Expansion Immediately Post-Approval (Variant 2) (PQS                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Same expansion targeting, but with more technical detail about the specific scaling challenges they'll face. Emphasizes the non-linear nature of protocol scaling.
- **Why this works**: By calculating the 180% capacity increase and mentioning specific technical requirements (irrigation system adjustments, EC management), you demonstrate deep cultivation expertise. The phrase "won't scale linearly" resonates with experienced growers who understand the complexity.
- **Data Sources**:
  - Public permit records - Expansion square footage, approval dates, facility location
  - Internal data - Technical protocol scaling requirements
- **Outreach Message template**:
  ```text
  Subject: 25,000 sq ft expansion starting in Ann Arbor
  
  Your December 3rd permit approval adds 25,000 sq ft to your Ann Arbor facility - that's a 180% capacity increase.
  
  Your current nutrient protocol for 14,000 sq ft won't scale linearly without irrigation system adjustments and EC management changes.
  
  Is someone mapping out the scaled feeding infrastructure?
  ```
- **Data Requirement**: This play assumes your company has:
                    Technical cultivation expertise and documented protocol scaling methodologies showing the specific adjustments required when expanding facility capacity.

#### Play: Premium Craft Producer Margin Optimization (PQS                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: Target craft cannabis cultivators producing 10,000-20,000 lbs annually whose nutrient cost per pound is significantly above peer average. Use aggregated internal data to show them exactly how much they're overspending compared to similar craft operations.
- **Why this works**: Craft growers are always optimizing margins while maintaining premium quality. By showing them peer-specific benchmarks (not generic industry data), you're providing intelligence they literally cannot get anywhere else. The $126K figure is material enough to get executive attention.
- **Data Sources**:
  - Internal customer data - Nutrient costs, production volume, facility size
  - Public harvest reports - California DCC data for production ranges
- **Outreach Message template**:
  ```text
  Subject: Your $38/lb nutrient cost vs. craft average
  
  Premium craft cultivators in your production range (10,000-20,000 lbs annually) average $29/lb in nutrient costs.
  
  You're at $38/lb - that's a $126,000 annual margin opportunity on your 14,000 lb yield.
  
  Who owns nutrient cost optimization on your team?
  ```
- **Data Requirement**: This play assumes your company has:
                    Aggregated nutrient cost and production data from 20+ premium craft cannabis customers, normalized per pound of flower and stratified by facility size categories.
                    This is highly differentiated intelligence that competitors cannot replicate without your customer base.

#### Play: Terpene Consistency Issues Detection (PQS                     Internal Data | Strong - Strong (8.2/10))

- **What's the play?**: Target premium craft producers experiencing terpene profile inconsistency by analyzing their feeding schedules against benchmarks from producers with stable terpene expression. The nitrogen timing issue is a specific technical insight that resonates with quality-focused growers.
- **Why this works**: Terpene consistency is the holy grail for craft cannabis - it's what differentiates premium products. By connecting their feeding schedule data to a specific quality problem they're likely experiencing, you demonstrate both technical expertise and genuine understanding of their challenges.
- **Data Sources**:
  - Internal customer data - Feeding schedules, terpene consistency metrics, quality ratings
- **Outreach Message template**:
  ```text
  Subject: Terpene consistency issues in your flower batches
  
  Premium craft producers with inconsistent terpene profiles typically have nitrogen timing issues in weeks 3-5 of flower.
  
  Your nutrient schedule shows 40% higher nitrogen during that window compared to producers with stable terpene expression.
  
  Is someone tracking terpene variance across your harvest cycles?
  ```
- **Data Requirement**: This play assumes your company has:
                    Detailed feeding schedule data and quality metrics from craft cannabis customers, with the ability to correlate nutrient timing to terpene consistency outcomes.
                    This level of data synthesis creates massive differentiation and demonstrates deep cultivation science expertise.

#### Play: Nutrient Cost Benchmarking Analysis (PVP                     Internal Data | Strong - Strong (9.3/10))

- **What's the play?**: Deliver a complete cost benchmarking analysis showing exactly where their nutrient spending sits relative to peer craft growers. The $126K margin improvement figure is calculated, specific, and immediately actionable.
- **Why this works**: This isn't a pitch - it's a financial analysis they would pay a consultant to provide. The specificity of knowing their exact costs, yield, and peer comparison makes it impossible to ignore. The breakdown offer creates natural next-step engagement.
- **Data Sources**:
  - Internal aggregated customer data - Nutrient costs per pound across 47 premium craft cultivators
- **Outreach Message template**:
  ```text
  Subject: Your nutrient cost per pound vs. 12 other craft growers
  
  We track nutrient costs across 47 premium craft cultivators and your $38/lb flower cost is 31% above the craft average of $29/lb.
  
  That's $126,000 in potential margin improvement on your 14,000 lb annual yield.
  
  Want the breakdown showing where the $9/lb gap comes from?
  ```
- **Data Requirement**: This play assumes your company has:
                    Aggregated nutrient cost and yield data across premium craft cannabis customers, normalized per pound of flower with peer comparison analytics.
                    This is proprietary intelligence that helps the recipient identify specific cost optimization opportunities.

#### Play: Protocol-Level Cost Optimization Recommendations (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Go beyond just showing the cost gap - offer the specific protocol changes that close it. The promise of "3 specific protocol changes" makes the value concrete and immediately actionable.
- **Why this works**: You're not just diagnosing the problem, you're offering the solution. The comparison to a specific peer group (10,000-20,000 lbs annually) adds credibility. The easy yes-question makes engagement frictionless.
- **Data Sources**:
  - Internal protocol and cost data - Specific nutrient protocols from craft customers segmented by production volume
- **Outreach Message template**:
  ```text
  Subject: $126K margin gap in your nutrient program
  
  Compared to 12 other craft cultivators producing 10,000-20,000 lbs annually, your nutrient cost per pound is $38 vs. their $29 average.
  
  On 14,000 lbs that's $126,000 you're leaving on the table.
  
  Want me to show you the 3 specific protocol changes that close the gap?
  ```
- **Data Requirement**: This play assumes your company has:
                    Aggregated nutrient protocol and cost data across craft cannabis customers segmented by production volume, with identified best practices.
                    Provides actionable protocol improvements that directly impact the recipient's bottom line.

#### Play: Feeding Schedule Correction for Terpene Consistency (PVP                     Internal Data | Strong - Strong (9.4/10))

- **What's the play?**: Deliver the exact technical insight connecting their feeding schedule to the terpene consistency problem they're experiencing. Then offer the corrected schedule specific to their strain mix.
- **Why this works**: This is the highest-scoring message because it solves a quality problem that directly impacts their product differentiation and pricing power. The technical specificity (40% higher nitrogen in weeks 3-5) combined with the diagnosis of terpene inconsistency shows expert-level understanding.
- **Data Sources**:
  - Internal feeding schedule and quality data - Correlation analysis between nutrient timing and terpene consistency
- **Outreach Message template**:
  ```text
  Subject: Your feeding schedule vs. top craft growers
  
  We analyzed feeding schedules from 23 premium craft operations and yours shows 40% higher nitrogen in weeks 3-5 of flower compared to the top quartile.
  
  That nitrogen excess correlates with the terpene profile inconsistency you're probably seeing batch-to-batch.
  
  Want the corrected feeding schedule for your strain mix?
  ```
- **Data Requirement**: This play assumes your company has:
                    Detailed feeding schedule data and quality metrics from craft cannabis customers, with the ability to correlate nutrient timing to terpene consistency and provide strain-specific recommendations.
                    Solves a quality consistency problem that directly impacts the recipient's product differentiation and pricing power.

#### Play: Expansion Scale-Up Protocol Package (PVP                     Public + Internal | Strong - Strong (9.0/10))

- **What's the play?**: When a facility gets expansion approval, immediately deliver a ready-to-implement nutrient scale-up protocol preventing the typical first-cycle yield drop. The protocol is already built based on their specific expansion scope.
- **Why this works**: The prospect is entering a high-risk phase where mistakes are costly. By having already built something specific for their facility, you demonstrate proactive expertise. The technical detail (irrigation modifications, EC stacking adjustments, strain-specific schedules) shows this isn't generic.
- **Data Sources**:
  - Public permit data - Expansion square footage, approval dates
  - Internal scale-up protocols - Documented methodology from previous customer expansions
- **Outreach Message template**:
  ```text
  Subject: Nutrient scale-up plan for your 25,000 sq ft expansion
  
  Based on your December 3rd permit for 25,000 sq ft in Ann Arbor, we built a nutrient scale-up protocol that prevents the typical 20-30% first-cycle yield drop.
  
  It includes irrigation modifications, EC stacking adjustments, and strain-specific feeding schedules for your increased canopy.
  
  Want me to send the complete scale-up protocol for your facility?
  ```
- **Data Requirement**: This play assumes your company has:
                    Documented nutrient protocol progression from 8-12 customers who successfully scaled facility size 2x+ while maintaining or improving quality metrics, including timeline of SOP changes, cost-per-pound at each scale tier, and quality consistency scores.
                    Provides a ready-to-implement protocol that protects yield during a critical expansion phase.

#### Play: Violation Remediation Template Package (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: For facilities with violations facing renewal, deliver a complete remediation checklist with state-specific submission templates. The value is immediate and usable whether they buy Athena AG products or not.
- **Why this works**: This is pure permissionless value. The templates would save massive time and the Colorado-specific experience (each state has different processes) adds credibility. By helping them succeed regardless of purchase, you build genuine trust and reciprocity.
- **Data Sources**:
  - Public violation tracking data - Specific violations and deadlines
  - Internal remediation templates - State-specific compliance processes
- **Outreach Message template**:
  ```text
  Subject: Violation remediation checklist for January 15th renewal
  
  For your 2 open Colorado violations (pesticide docs and waste disposal), we built a 45-day remediation checklist with state submission templates.
  
  It's based on 18 successful violation closures before renewal windows in Colorado specifically.
  
  Want the checklist and template package for your January 15th deadline?
  ```
- **Data Requirement**: This play assumes your company has:
                    Internal remediation templates and state-specific compliance processes developed from helping previous customers resolve violations.
                    Provides immediately actionable compliance tools that help the recipient avoid license suspension regardless of purchase.

#### Play: Irrigation System Design for Expansion (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: For facilities with expansion permits, deliver optimized irrigation design specs preventing the common mistake of over-sizing pumps by 40% (which wastes $18K+ annually on energy).
- **Why this works**: You're providing engineering-level value for free. The energy cost savings is a bonus they hadn't considered, and the specificity about their facility layout shows you've done real analysis. This is consulting-grade deliverable as a cold outreach.
- **Data Sources**:
  - Public permit data - Square footage, location
  - Internal irrigation engineering expertise - Facility design analysis
- **Outreach Message template**:
  ```text
  Subject: Irrigation design for your Ann Arbor expansion
  
  Your 25,000 sq ft expansion needs 180% more irrigation capacity but most cultivators over-size pumps by 40% and waste $18,000+ annually on energy.
  
  We mapped the optimal irrigation zones and pump sizing for your specific canopy layout at the Ann Arbor facility.
  
  Want the irrigation design specs and equipment recommendations?
  ```
- **Data Requirement**: This play assumes your company has:
                    Irrigation engineering expertise and facility design analysis capabilities, with benchmarks on common sizing mistakes and their cost impacts.
                    Provides engineering specifications that reduce both capital costs and ongoing operating expenses.

---

## BigSal (Trouw Nutrition) (bigsal.com.br)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/bigsal-com-br)
**Strategic Summary**: The playbook runs 18-month satellite analysis of specific Brazilian farm properties using PRODES and SICAR data to identify seasonal degradation patterns, and uses GTA transport records to build reverse breeding season timelines with optimized intervention windows.

### ✕ The Old Way (Generic Outreach)
```text
Assunto: Melhore o desempenho do seu rebanho

Olá [Nome],

Vi que sua fazenda em [região] tem foco em pecuária de corte. A BigSal oferece suplementos minerais de alta qualidade que podem ajudar a melhorar a produtividade do seu rebanho.

Nossa tecnologia DRY garante que os minerais não empedrram mesmo em condições úmidas, e temos cases de sucesso em toda a região Norte.

Teria 15 minutos esta semana para uma conversa rápida sobre como podemos ajudar?

Atenciosamente,
[Nome do SDR]
```

### ✓ The New Way: GTM Plays

#### Play: Análise de 18 meses da sua capacidade de pastagem (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Run satellite analysis of the specific property covering 18 months to identify seasonal degradation patterns and critical areas where supplementation would deliver better ROI than pasture reform. This combines public satellite data with proprietary ROI models.
- **Why this works**: You're surfacing information the prospect forgot they needed. The specificity of 18 months of their exact property data proves you're not guessing. Identifying where supplementation beats reform directly solves a capital allocation decision they face.
                    If this is real (not a template), it's analysis nobody else offers for free.
- **Data Sources**:
  - PRODES/TerraBrasilis - Deforestation monitoring with coordinates, dates, area measurements
  - SICAR/CAR - Property boundaries and land use type
  - Internal ROI models - Supplementation cost vs pasture reform cost by degradation type
- **Outreach Message template**:
  ```text
  Assunto: Análise de 18 meses da sua capacidade de pastagem
  
  Rodei análise de satélite da sua propriedade em [município] cobrindo 18 meses (jan 2023-jun 2024).
  
  Identifiquei 3 padrões sazonais de degradação que se repetem e 2 áreas críticas onde suplementação intensiva seria mais ROI-eficiente que reforma.
  
  Envio o relatório completo com mapas?
  ```
- **Data Requirement**: This play requires capability to run multi-period satellite analysis and correlate pasture degradation patterns with supplementation ROI models vs pasture reform costs.
                    Combined with public satellite data to create property-specific analysis. This synthesis is unique to your business.

#### Play: Timeline reversa da sua estação de monta (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Use GTA transport data showing 340 matrices moved in October to build a reverse timeline to January breeding season. Mark 8 critical intervention windows with dosages optimized for tropical humid climate and verification checklists for each phase.
- **Why this works**: Reverse timeline approach is smart and practical. The 340 matrices figure is real data from their operation. 8 critical windows with specific dosages for tropical humid climate shows deep understanding of their context. If this is real, it's extremely actionable.
- **Data Sources**:
  - GTA - Animal Transport Guide showing origin property, cattle count, transport date
  - Internal breeding protocols - Intervention windows optimized for tropical humid climates with dosage recommendations
- **Outreach Message template**:
  ```text
  Assunto: Timeline reversa da sua estação de monta
  
  Peguei sua movimentação de 340 matrizes em outubro e construí timeline reversa até janeiro.
  
  Marquei 8 janelas críticas de intervenção nutricional com dosagens específicas para clima tropical úmido e checklist de verificação para cada fase.
  
  Envio a timeline completa agora?
  ```
- **Data Requirement**: This play requires proprietary protocols for reverse-engineering breeding season preparation with intervention windows optimized for tropical humid climates.
                    Combined with public GTA transport data to create timeline specific to their operation.

#### Play: Sua estação de monta começa em 45 dias (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Use GTA records showing 340 matrices moved in October (typical pre-season preparation pattern) to identify breeding season starting in January. Create urgency around the 6-week window to optimize body condition and pregnancy rates.
- **Why this works**: GTA data is specific to THEIR operation - impressive. The timing of 45 days is precise and urgent. The connection between October movement and January breeding shows deep understanding of cattle operations. This is genuinely useful - reminds them to act NOW.
- **Data Sources**:
  - GTA - Guia de Trânsito Animal showing origin property, cattle count (340 matrices), transport date (October)
  - Regional breeding season timing (January start for Northern Brazil)
- **Outreach Message template**:
  ```text
  Assunto: Sua estação de monta começa em 45 dias
  
  Registros da GTA mostram sua propriedade movimentou 340 matrizes em outubro - padrão típico de preparação pré-estação.
  
  Com início estimado em janeiro, você tem 6 semanas para otimizar a condição corporal e taxas de prenhez.
  
  Quem está coordenando o protocolo de suplementação pré-cobertura?
  ```

#### Play: Checklist pré-estação para sua propriedade em [município] (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Cross-reference GTA data (340 matrices, October movement) with local climate conditions and breeding season chronology to create a 6-week checklist with 12 specific nutritional readiness verification points tailored to their January window.
- **Why this works**: Combines public data (GTA) with local context - genuine synthesis. 6-week checklist is specific and actionable. 12 verification points sounds concrete, not generic. Clear value - helps them not lose valuable breeding season days. This is HYBRID done right - public data + proprietary knowledge.
- **Data Sources**:
  - GTA - Animal transport records showing 340 matrices moved in October
  - INMET - Climate data for municipality showing humidity, rainfall patterns
  - Internal protocols - Nutritional readiness checklists correlated with climate and breeding timing from successful customer outcomes
- **Outreach Message template**:
  ```text
  Assunto: Checklist pré-estação para sua propriedade em [município]
  
  Cruzei seus dados de GTA (340 matrizes, movimentação outubro) com condições climáticas locais e cronograma de estação.
  
  Montei um checklist de 6 semanas com 12 pontos de verificação de prontidão nutricional específicos para sua janela de janeiro.
  
  Envio o checklist agora?
  ```
- **Data Requirement**: This play requires proprietary protocols correlating climate data, breeding season timing, and nutritional readiness checklists from successful customer outcomes.
                    Helps the rancher maximize breeding success rates by providing a concrete action plan during the critical pre-breeding window.

#### Play: Mapa de risco de degradação para sua pastagem (PVP                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Cross-reference satellite imagery of specific property with precipitation data and regional fire history to identify 3 high-risk degradation areas in next 90 days. Provide area-specific supplementation adjustment recommendations.
- **Why this works**: Combines multiple public data sources - genuine synthesis. 3 specific areas is actionable, not generic. Recommendations by area deliver immediate value. If this is real (not a template), it's gold - nobody else does this analysis for free. Provides proactive risk management.
- **Data Sources**:
  - PRODES/TerraBrasilis - Satellite imagery with coordinates and dates
  - INMET - Precipitation data for municipality
  - IBAMA Fire History Database - Regional fire patterns
  - Internal degradation risk models - Area-specific supplementation recommendations based on risk factors
- **Outreach Message template**:
  ```text
  Assunto: Mapa de risco de degradação para sua pastagem
  
  Cruzei imagens de satélite da sua propriedade em [município] com dados de precipitação e histórico de queimadas da região.
  
  Identifiquei 3 áreas de alto risco de degradação mineral nos próximos 90 dias com recomendações de ajuste de suplementação por área.
  
  Quero enviar o mapa de risco completo?
  ```
- **Data Requirement**: This play requires capability to synthesize satellite imagery, precipitation data, and fire history into pasture degradation risk models with area-specific supplementation recommendations.
                    Provides proactive risk management for pasture degradation, allowing the rancher to adjust supplementation strategy before productivity losses occur.

---

## Cemetery Workstation (allfuneral.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/allfuneral-com)
**Strategic Summary**: The playbook uses Secretary of State business registry filings to identify multi-location funeral home operators and quantify the operational cost of fragmented record management across locations.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Strong (7.6/10)
                
                
                    Target: Funeral homes operating 2+ physical locations without centralized digital record management.
                    Trigger: Multiple business entities under same ownership (detected via Secretary of State filings + Google Maps verification).
                    Pain: Each location uses different paper filing systems, creating daily operational chaos - inter-location record lookups, ownership transfer confusion, staff time wasted calling between sites, compliance risk when state auditors request consolidated records.
                

                
                    Why This Works (Buyer Perspective)
                    Situation Recognition (8/10): Exact addresses and establishment years prove research - mirrors their reality precisely.
                    Data Credibility (9/10): Secretary of State records are publicly verifiable, time estimate is disclosed as industry benchmark.
                    Insight Value (6/10): They know they have multiple locations, but quantifying the wasted time (12-15 hours/week) is somewhat novel.
                    Effort to Reply (8/10): Easy yes/no or short description of their current situation.
                    Emotional Resonance (7/10): Creates curiosity about hidden operational costs, though not an immediate crisis.
                

                
                    Subject: 3 locations, 1 question
                    Your business operates funeral homes at 1425 Main Street (since 2008), 892 Oak Avenue (since 2015), and 3401 Riverside Drive (since 2019)—when families call asking about burial records, which location do they try first?

Most multi-site operators lose 12-15 hours per week on inter-location record lookups.

Does this match what you're seeing?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Multi-location detection: Secretary of State Business Registry (fields: business_name, dba, entity_address, filing_date) - 85% confidence
  - Location verification: Google Maps Places API (fields: place_id, name, address, location) - 90% confidence
  - Time estimate: Industry operational benchmark (2-3 daily inter-location queries × 30-45 min each × 5 days) - 50% confidence, disclosed as "most operators"

#### Play:  (PQS |  - Strong (8.0/10)
                
                
                    Target: Same as Play #1 (multi-location operators) but emphasizes growth angle.
                    Trigger: Business expansion from 1 location to 3+ over time period (detected via filing date sequencing).
                    Pain: As locations increase, operational complexity grows exponentially - each new site adds inter-location coordination burden, record management becomes chaotic, growth amplifies existing inefficiencies.
                

                
                    Why This Works (Buyer Perspective)
                    Situation Recognition (8/10): Growth trajectory from 2008 to today is accurate and specific.
                    Data Credibility (9/10): Business expansion timeline is verifiable via government records.
                    Insight Value (7/10): Connecting growth to operational complexity (2-3 queries daily, 20-40 min each) is somewhat novel.
                    Effort to Reply (9/10): Very easy yes/no or brief description.
                    Emotional Resonance (7/10): Makes them reflect on cumulative time waste as business has grown.
                

                
                    Subject: location sync question
                    I see your business has grown from 1 location in 2008 to 3 locations today—when someone at your Main Street office needs to check plot availability at your Riverside location, how long does that take?

Most multi-site funeral operators report 2-3 such queries daily, each requiring 20-40 minutes between calling, searching, and confirming.

Does that sound familiar?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Growth timeline: Secretary of State Business Registry (fields: filing_date sorted ascending, entity count) - 90% confidence
  - Operational estimate: Industry benchmark (2.5 avg daily queries × 30 min = 75 min/day ≈ 6.25 hours/week) - 60% confidence, disclosed as "most multi-site operators report"

#### Play:  (PQS |  - Strong (8.2/10)
                
                
                    Target: Funeral homes serving 100+ families annually with no visible online records portal.
                    Trigger: High Google review velocity (>100 reviews/12 months) + absence of online burial records features on website.
                    Pain: Paper records accumulate faster than staff can organize, every family inquiry = 10-15 min file search, high volume + paper system = staff overtime just to keep up, cannot sell plots online (miss after-hours revenue), competitive risk from digitally-enabled competitors.
                

                
                    Why This Works (Buyer Perspective)
                    Situation Recognition (9/10): Exact review count (147) is verifiable, absence of online portal is accurate.
                    Data Credibility (8/10): Google review data is immediately verifiable, calculation (245+ services) shows transparent methodology with disclosed 60% assumption.
                    Insight Value (7/10): Connecting review velocity to service volume estimate is novel, "20+ hours per week" quantifies hidden cost.
                    Effort to Reply (9/10): Very easy open-ended question ("How are you managing?") invites genuine response.
                    Emotional Resonance (8/10): Creates urgency about operational burden, sparks curiosity about better solutions.
                

                
                    Subject: 147 reviews, paper records?
                    Your funeral home received 147 Google reviews in the last 12 months—if even 60% of families leave reviews, that's 245+ services annually—and I don't see an online burial records portal on your website.

High-volume paper-based operations typically spend 20+ hours per week just on file searches and record maintenance.

How are you managing this?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Review velocity: Google Maps Places API (fields: reviews[].time filtered to last 365 days, COUNT) - 95% confidence
  - Service volume estimate: Calculation using industry review rate benchmark (147 reviews ÷ 0.60 assumed rate = 245 services) - 60% confidence, assumption disclosed in message
  - Website inspection: Manual crawl for absence of "search records," "find a grave," "plot map," "burial lookup" features - 85% confidence
  - Time estimate: Industry benchmark (5-8 daily lookups × 30 min + filing time ≈ 20 hours/week) - 50% confidence, disclosed as "typically"

#### Play:  (PQS |  - Good (7.0/10)
                
                
                    Target: Same as Play #3 (high-volume operators) but uses qualification question approach.
                    Trigger: Same detection method (review velocity proxy).
                    Pain: Opens dialogue to understand current system before describing pain - less assumptive, more consultative.
                

                
                    Why This Works (Buyer Perspective)
                    Situation Recognition (8/10): Volume estimate (245+ families) is specific and calculation is transparent.
                    Data Credibility (8/10): Review count and calculation methodology are disclosed and verifiable.
                    Insight Value (6/10): Volume estimate is interesting, but "exponential chaos" claim is conceptual (not quantified like Play #3's "20+ hours").
                    Effort to Reply (7/10): Easy to answer but "what's your current system?" feels like discovery question (lower motivation).
                    Emotional Resonance (6/10): "Exponential record chaos" is evocative but vague compared to specific time cost.
                

                
                    Subject: busy year
                    You served 245+ families last year based on your 147 Google reviews—with that volume, are you still using paper burial records or have you moved to digital?

Paper-based high-volume operations face exponential record chaos as services increase.

What's your current system?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Service volume estimate: Same calculation as Play #3 (147 reviews ÷ 0.60 rate = 245 services) - 60% confidence
  - "Exponential chaos" claim: Operational principle (qualitative, not quantified) - 70% confidence as general industry observation

---

## Global Music Rights (globalmusicrights.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/globalmusicrights-com)
**Strategic Summary**: Playbook (attributed to GetixHealth) targets dialysis facilities with declining CMS quality scores and open enforcement actions to surface compounding Medicare reimbursement risk.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Improve your revenue cycle

Hi [CFO First Name],

I noticed your hospital has been growing. Congrats on the recent expansion!

At GetixHealth, we help healthcare providers like you optimize revenue cycle management. Our clients see 50% faster collections and 12% revenue increases.

We combine technology + people to reduce denials, speed up claims, and improve cash flow.

Would love to show you how we're different. Open to a quick call next week?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: ESRD Facilities with Quality Measure Decline Plus Open CMS Enforcement Actions (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Target dialysis facilities that show declining quality scores (survival rates, hospitalization rates, infection rates) combined with recent provider exclusions or open CMS enforcement actions. These facilities face immediate Medicare reimbursement risk - quality penalties stack with billing compliance issues to create cash flow crisis.
- **Why this works**: Dialysis facilities operate under strict Medicare conditions of participation with highly regulated reimbursement. When quality measures decline AND enforcement actions are open, the CFO knows they're facing compounding payment risk. This message shows you understand their dual regulatory pressure with exact dates and metrics - they can't ignore it.
- **Data Sources**:
  - CMS Provider Data Catalog - Dialysis Facility Reports - quality_measures, survival_rates, hospitalization_rates, infection_rates
  - HHS OIG Excluded Individuals List - provider_name, exclusion_reason, exclusion_date
- **Outreach Message template**:
  ```text
  Subject: Your Fresenius center's 2-star drop plus open enforcement
  
  Fresenius Dallas East (456 Oak Ave) dropped from 4 stars to 2 stars in the September ESRD QIP update.
  
  You also have an open CMS enforcement action filed August 22nd for infection control protocols.
  
  Who's managing the QIP recovery plan?
  ```

#### Play: Payer-Specific Denial Rate Alerts for Underperforming Providers (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Use aggregated denial data from your 200+ provider customers to show prospects their exact denial rates by specific payers, benchmarked against the network average. Reveal which payers are causing outsized denials and which specific CPT codes need immediate coding attention before accounts age past 120 days.
- **Why this works**: CFOs and RCM directors track denial rates religiously but lack external benchmarks to know if they're underperforming. When you tell them "your Aetna denial rate on CPT codes 27447 and 27130 is 41% - the regional average is 22%", you're giving them intelligence they can't get anywhere else. The specificity (exact payer, exact codes, exact comparison) proves you have real data, not generic industry stats.
- **Data Sources**:
  - Internal Customer Data - aggregated denial rates by payer, claim type, facility type with median benchmarks
- **Outreach Message template**:
  ```text
  Subject: Aetna is denying 41% of your ortho claims
  
  St. Mary's Orthopedic Group - your Aetna denial rate on CPT codes 27447 and 27130 is 41%.
  
  The regional average for these codes is 22%. That's $89,000 stuck in appeals every quarter.
  
  Want the prior auth pattern analysis?
  ```
- **Data Requirement**: This play requires aggregated insurance denial data across 50+ healthcare provider customers, segmented by payer name, claim type (inpatient/outpatient/emergency), facility type, and CPT codes. You need median and percentile denial rates calculated monthly, plus claim-level detail including denial reason codes.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: ESRD Facilities with Dual Open CMS Enforcement Actions (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target dialysis facilities with multiple open CMS enforcement actions combined with declining Standardized Hospitalization Ratio (SHR) above the national target of 1.0. These facilities face compounding regulatory pressure that directly impacts reimbursement and creates urgent need for operational cleanup.
- **Why this works**: Two open enforcement actions signal systematic compliance breakdown, not isolated incidents. When combined with SHR deterioration, the CFO knows they're in serious trouble. The precision of citing exact enforcement dates, specific SHR metrics, and the national benchmark proves you pulled their actual data - this isn't a generic template.
- **Data Sources**:
  - CMS Dialysis Facility Reports - quality_measures, survival_rates, hospitalization_rates, SHR metric
  - HHS OIG Excluded Individuals List - enforcement_actions, citation_dates
- **Outreach Message template**:
  ```text
  Subject: Your dialysis center has 2 open CMS actions
  
  Your DaVita center at 789 Elm St has 2 open CMS enforcement actions from July 18th and September 3rd.
  
  Your Standardized Hospitalization Ratio increased from 0.89 to 1.24 in Q3 2024 - above the national target of 1.0.
  
  Is someone coordinating the dual enforcement response?
  ```

#### Play: Critical Access Hospitals Approaching CMS Star Rating Threshold with Recent Survey Deficiencies (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target Critical Access Hospitals with 2-3 star ratings that have recent state survey deficiencies with specific deficiency tag citations. These facilities are at immediate risk of dropping to 1-star and triggering CMS Special Focus Facility designation, which means payment penalties and mandatory targeted review.
- **Why this works**: CFOs at Critical Access Hospitals live in fear of losing their designation - it means survival. When you cite their exact facility name, address, specific deficiency tags (F880, F881, F882), exact citation date, and exact star rating drop, they know you pulled their actual survey data. This level of specificity is impossible to fake and proves you understand their urgent situation.
- **Data Sources**:
  - CMS Hospital General Information - facility_name, address, hospital_type, number_of_beds
  - Medicare.gov Care Compare Tool - star_ratings, quality_scores, inspection_dates
  - State Health Department Inspection Records - deficiency_count, deficiency_tags, citation_date
- **Outreach Message template**:
  ```text
  Subject: Memorial Hospital's 3 infection control citations
  
  Memorial Hospital (123 Main St, Springfield) had 3 infection control deficiencies cited on October 15th - Tag F880, F881, F882.
  
  Your overall rating dropped from 3.2 to 2.7 stars, triggering CMS targeted review eligibility in Q1 2025.
  
  Is someone already handling the Plan of Correction deadline?
  ```

#### Play: Ambulatory Surgery Centers with Accreditation Renewal Windows During High Complication Periods (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target ASCs with accreditation renewals in the next 90 days that show elevated complication rates above 3.5% threshold AND have open state inspection deficiencies. Failed accreditation means loss of Medicare billing privileges - this is an existential threat to ASC operations.
- **Why this works**: ASCs depend entirely on procedure reimbursement with minimal inpatient revenue. When you cite their exact facility name, specific Q4 complication rate, exact accreditation renewal date, and calculate the exact days remaining (22 days), you demonstrate surgical precision in understanding their timeline pressure. The administrator knows you pulled their actual accreditation schedule - this isn't a guess.
- **Data Sources**:
  - CMS Ambulatory Surgery Center Procedures - facility_name, accreditation_status, complication_rates, infection_rates
  - State Health Department Inspection Records - inspection_date, deficiency_count, plan_of_correction_status
- **Outreach Message template**:
  ```text
  Subject: Your ASC's accreditation renewal is March 2025
  
  SurgiCare Center (321 Pine Rd, Austin) has AAAHC accreditation expiring March 15, 2025.
  
  Your Q3 2024 complication rate increased to 4.2% from 2.1% in Q2 - above the 3.5% threshold for standard renewal.
  
  Who's preparing the accreditation documentation?
  ```

#### Play: The 7 Denial Codes Costing Providers the Most Revenue (PVP                     Internal Data | Strong - Strong (8.5/10))

- **What's the play?**: Analyze the recipient's last 6 months of insurance claim denials to identify the specific denial codes causing 70%+ of their rejected claims. Show them which of those denial codes are preventable with upstream authorization workflow changes, then offer both the diagnosis (denial code analysis) and solution (workflow fixes).
- **Why this works**: RCM directors track denial rates in aggregate but rarely have time to analyze which specific codes are causing the most pain. When you tell them "7 denial codes account for 73% of your rejected claims, and 5 of those 7 are preventable," you're giving them a roadmap to immediate revenue recovery. The specificity proves you analyzed their actual data, not generic industry patterns.
- **Data Sources**:
  - Internal Customer Data - 6 months of claim submissions, denial reason codes, payer-specific patterns
- **Outreach Message template**:
  ```text
  Subject: The 7 denial codes costing you the most
  
  Analyzed your last 6 months of UnitedHealthcare denials - 7 denial codes account for 73% of your rejected claims.
  
  5 of those 7 are preventable with upstream authorization workflow changes.
  
  Want the denial code analysis and workflow fixes?
  ```
- **Data Requirement**: This play requires 6 months of the recipient's claim submission and denial data, including denial reason codes, claim details, and payer information. Requires claim-level analytics capability to identify patterns and calculate preventability.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Procedure-Level Complication Trend Analysis for Accreditation Defense (PVP                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: Break down the ASC's overall complication rate into 3 procedure categories with different risk profiles. Show them that 2 of those categories are trending down (improvement) while 1 is driving the overall increase. This gives them a defensible narrative for their accreditation survey - they can demonstrate improvement in most areas alongside the concerning trend.
- **Why this works**: ASC administrators facing accreditation renewals during high complication periods are terrified of losing their designation. When you give them a procedure-level breakdown showing "2 of 3 categories trending down, 1 driving the increase," you're handing them the exact documentation they need for their survey. This transforms a scary overall number into a nuanced story of improvement with one problem area to address.
- **Data Sources**:
  - Internal Customer Data - procedure-level complication data by category, quarterly trends
- **Outreach Message template**:
  ```text
  Subject: Your complication trend analysis for Joint Commission
  
  Texas Surgical Center's Q4 complication rate of 4.8% breaks down into 3 procedure categories with different risk profiles.
  
  2 of those categories are trending down, 1 is driving the overall increase.
  
  Want the procedure-level breakdown for your survey documentation?
  ```
- **Data Requirement**: This play requires procedure-level complication data for the recipient's facility, segmented by procedure category with quarterly trends. Assumes access through RCM operations or quality reporting partnership.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Payer-Specific Denial Rate Benchmarking with Financial Impact (PVP                     Internal Data | Strong - Strong (8.3/10))

- **What's the play?**: Show CFOs their exact denial rate for a specific major payer (UnitedHealthcare, Blue Cross, Aetna) benchmarked against 200+ similar providers in your network. Calculate the monthly delayed revenue impact based on their claim volume, then offer a breakdown by denial code so they can see exactly where to focus remediation efforts.
- **Why this works**: CFOs want to know two things: (1) Are we underperforming? (2) How much is it costing us? When you tell them "your UnitedHealthcare denial rate is 34% vs network average of 18% - that's $127,000 in delayed revenue per month," you're answering both questions with precision. The financial impact calculation proves you know their volume, and the offer to break it down by denial code shows you have actionable detail.
- **Data Sources**:
  - Internal Customer Data - aggregated denial rates by payer across 200+ providers, recipient claim volume data
- **Outreach Message template**:
  ```text
  Subject: Your UnitedHealthcare denial rate is 34%
  
  Our RCM data across 200+ providers shows your UnitedHealthcare denial rate at 34% - the network average is 18%.
  
  That's $127,000 in delayed revenue per month based on your claim volume.
  
  Want the breakdown by denial code?
  ```
- **Data Requirement**: This play requires aggregated insurance denial data across 200+ healthcare provider customers, segmented by payer name, with median benchmarks. Also requires access to the recipient's claim volume to calculate financial impact.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Infection Control Protocol Templates from Peer Facility Resolutions (PVP                     Public + Internal | Strong - Strong (8.1/10))

- **What's the play?**: Pull the specific infection control protocol failures cited in the recipient's August CMS enforcement action (public data). Then offer them the compliance documentation, protocol templates, and training materials from 6 peer facilities that resolved identical violations in under 60 days (internal data).
- **Why this works**: Dialysis facility administrators facing infection control enforcement actions are under extreme time pressure to remediate. When you offer "protocol templates and training materials from 6 centers that resolved identical violations in under 60 days," you're giving them a proven resolution path. The combination of citing their specific violations (proves you pulled their data) plus offering ready-to-use resources creates immediate value.
- **Data Sources**:
  - CMS Enforcement Actions Database - enforcement_date, violation_type, citation_details
  - Internal Customer Data - compliance documentation, protocol templates, training materials from successful remediations
- **Outreach Message template**:
  ```text
  Subject: Your infection control protocol gaps
  
  Your DaVita center's August enforcement action cited 4 specific infection control protocol failures.
  
  Pulled the compliance documentation from 6 centers that resolved identical violations in under 60 days.
  
  Want the protocol templates and training materials?
  ```
- **Data Requirement**: This play requires documented protocol templates and training materials from ESRD facilities that successfully resolved infection control enforcement actions. Assumes you have supported ESRD clients through similar enforcement situations and captured their resolution approaches.
                    Combined with public CMS enforcement data, this creates unique synthesis only you can deliver.

#### Play: ASC Accreditation Renewal with Urgent Timeline During High Complication Period (PQS                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Target ASCs with Joint Commission accreditation survey windows opening in the next 30 days that show Q4 complication rates above 4.0%. Calculate the exact days remaining until their survey window opens, creating extreme urgency around their preparation timeline.
- **Why this works**: ASC administrators know their accreditation renewal dates but may not realize how little time remains. When you tell them "Your Joint Commission survey window opens January 15, 2025 - 22 days from now" combined with "Your Q4 complication rate is 4.8%," you're creating a deadline-driven panic. The precision of the days-until calculation shows you're tracking their calendar, not guessing.
- **Data Sources**:
  - CMS Ambulatory Surgery Center Procedures - facility_name, accreditation_status, complication_rates, survey_window_dates
- **Outreach Message template**:
  ```text
  Subject: Your 4.8% complication rate during renewal window
  
  Texas Surgical Center (555 Medical Blvd, Houston) shows 4.8% complication rate in Q4 2024.
  
  Your Joint Commission accreditation survey window opens January 15, 2025 - 22 days from now.
  
  Is someone tracking the complication trend analysis for the survey?
  ```

---

## funeralOne (funeralone.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/funeralone-com)
**Strategic Summary**: Playbook demonstrates the Blueprint GTM methodology contrast using Google review counts, website metadata, and competitor comparisons to create hyper-specific outreach for funeral homes.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Strong PQS (7.2/10)

                Target Segment: Independent funeral homes serving 10-15+ families per month without professional tribute video software, manually creating videos using consumer-grade tools or outsourcing.

                Pain Identified: High service volume creates video production bottleneck. Manual creation takes 2-4 hours per tribute video, resulting in 30-60+ hours monthly spent on video work. This causes staff burnout, quality inconsistency, and operational inefficiency.

                Why This Works: Funeral home directors KNOW they spend time creating videos, but haven't quantified the monthly time cost. By using their Google review count (which families leave at 80-100% rate) as a proxy for service volume, we can estimate their monthly video workload and present it as verifiable data they can check.

                Product Fit: 9/10 - funeralOne's Easy Tribute Creator directly solves manual video creation bottlenecks by providing professional-quality templates, automated workflows, and consistent output quality.

                
                    Subject: 14 tributes, 42 hours
                    Your funeral home received 14 Google reviews in the last 30 days—at typical industry review rates, that's roughly 14-16 services.

If you're creating tribute videos manually at 3 hours each, that's 42-48 hours per month on video production alone.

Does this match what you're seeing?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Situation Recognition (8/10): Exact review count is verifiable, service estimate matches reality
  - Data Credibility (7/10): Google data is credible, assumptions are disclosed
  - Insight Value (6/10): They know they spend time on videos, but haven't quantified the monthly cost
  - Effort to Reply (9/10): "Does this match what you're seeing?" is simple yes/no
  - Emotional Resonance (6/10): Confirms what they suspect, moderate urgency

#### Play:  (PQS |  - Strong PQS (7.2/10)

                
                    Subject: Video bottleneck
                    I pulled your Google Business data—14 reviews last month suggests you're running 14-16 services.

Most funeral homes creating tribute videos manually spend 2-4 hours per family, putting you at 30-60 hours monthly on video work.

Is that time investment manageable with current staffing?
                

                Why This Variant Works: Same data foundation as #1A, but frames the question around staffing capacity rather than verification. The wider time range (2-4 hours vs. 3 hours) accounts for variation in video complexity. Slightly higher emotional resonance due to staffing pressure angle.)

- **What's the play?**: 
- **Why this works**: 

#### Play:  (PQS |  - Strong PQS (7.8/10)

                Target Segment: Independent funeral homes with 5+ year old websites (copyright date ≤2020, non-responsive design) facing competitive pressure from modernized local competitors.

                Pain Identified: Outdated web presence signals "behind the times" to families researching funeral homes online. Modern families research 3-5 funeral homes before deciding, and outdated websites (non-mobile-friendly, old design patterns, missing features) create trust issues and competitive disadvantage.

                Why This Works: Funeral home directors KNOW their website is old (they see it every day), but haven't compared it to specific local competitors or understood the feature gaps. By naming exact competitors who've modernized and identifying specific missing features (like online arrangement tools), we create competitive pressure and actionable context.

                Product Fit: 8/10 - funeralOne's website design service directly solves outdated web presence by providing modern responsive designs, mobile optimization, and integrated tools for online obituaries and arrangements.

                
                    Subject: Web comparison
                    I checked your website (© 2019, non-responsive) against your 4 nearest competitors.

Three have modernized in the last 18 months—Smith & Sons, Heritage Memorial, and Riverside Funeral Home all have responsive sites with online arrangement tools.

Want to see the side-by-side comparison?)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Situation Recognition (8/10): Specific competitor names increase verifiability and relevance
  - Data Credibility (8/10): All claims can be verified by visiting named competitor websites
  - Insight Value (7/10): Knowing WHICH competitors modernized and WHAT features they added is new intel
  - Effort to Reply (9/10): "Want to see the side-by-side comparison?" is simple yes/no
  - Emotional Resonance (7/10): Specific competitor names trigger competitive instinct, seeing name next to modernized competitors creates pressure

#### Play:  (PQS |  - Strong PQS (7.4/10)

                
                    Subject: Your 2019 website
                    Your website footer shows © 2019 and fails Google's mobile-friendly test—meanwhile, I tracked 247 "funeral home near me" mobile searches for your city last month.

68% of families now research on mobile before calling.

Want the local competitor breakdown?
                

                Why This Variant Works: Instead of naming specific competitors, this version adds mobile search volume data to create urgency. The "247 searches" and "68% mobile research" stats provide context the director doesn't have access to. Slightly lower score than #2B due to search volume being less verifiable by the recipient (requires SEO tool access).

                
                    Additional Calculation for #2A:
                    Claim: "247 'funeral home near me' mobile searches for your city last month"
                    → Source: Google Keyword Planner or SEMrush or similar SEO tool
                    → Method: Query mobile search volume for "[City] funeral homes" and related terms
                    → Confidence: 60-70% (data exists but requires paid tool access, not verifiable by recipient)
                    → Note: This is the weakest data point in all 4 messages - least verifiable

                    Claim: "68% of families now research on mobile before calling"
                    → Source: Industry research or Google Consumer Insights
                    → Confidence: 70% (industry stat, not company-specific))

- **What's the play?**: 
- **Why this works**: 

---

