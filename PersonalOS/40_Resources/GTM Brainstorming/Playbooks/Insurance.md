# GTM Playbooks: Insurance

Curated list of data-driven GTM Playbooks for the **Insurance** vertical. Use these to brainstorm messaging, trigger events, and PVP angles.

---

## Dent Wizard (dentwizard.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/dentwizard-com)
**Strategic Summary**: Playbook cross-references internal repair cost data by vehicle make and model with NAIC auto insurance claims data and state vehicle registration counts to surface model-specific PDR cost variance anomalies and proactive hail event inventory planning for rental fleets.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Quick question about your fleet maintenance

Hi [First Name],

I noticed your company manages a large vehicle fleet. Wanted to reach out because DentWizard offers paintless dent repair services that can save you time and money.

We've helped companies like Hertz and Enterprise reduce repair costs by up to 50% while getting vehicles back on the road faster.

Would you be open to a 15-minute call next week to discuss how we could help your fleet?

Best,
Mike
```

### ✓ The New Way: GTM Plays

#### Play: Vehicle Model Damage Propensity for Insurance Claim Optimization (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Cross-reference internal repair cost data by vehicle make/model with public insurance claims data to show insurance adjusters exactly which vehicle models in their portfolio have the highest cost variance from PDR vs traditional body shop repair.
- **Why this works**: Insurance adjusters manage claim costs daily but lack model-specific repair cost intelligence. When you show them "Nissan Altimas cost you 41% more than comparable sedans due to aluminum hood design," you're providing actionable underwriting and rate adjustment data they can't get anywhere else. The specificity of knowing their exact book composition (12,400 Altimas in Texas) proves this isn't a mass email.
- **Data Sources**:
  - DentWizard Internal Repair Database - repair cost by vehicle make/model/year across thousands of repairs
  - NAIC Auto Insurance Database Reports - collision claims by state, average repair cost per claim, insurer name
  - State Vehicle Registration Data - vehicle counts by make/model/ZIP
- **Outreach Message template**:
  ```text
  Subject: Nissan Altimas costing you 41% more in PDR claims
  
  Our repair data shows 2019-2022 Nissan Altimas have 41% higher PDR claim costs than comparable sedans due to aluminum hood design.
  
  You're insuring 12,400 Altimas in your Texas book based on registration data.
  
  Want the full vehicle model cost variance report for your top 20 models?
  ```
- **Data Requirement**: This play requires aggregated PDR repair cost data by vehicle make/model/year across thousands of repairs, showing cost variance patterns and material construction differences.
                    This is proprietary data only you have - competitors cannot replicate this synthesis of repair costs with insurer portfolio composition.

#### Play: Post-Hail Inventory Impact Forecasting for Rental Fleets (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Cross-reference NOAA seasonal hail forecasts with rental company multi-state operations to provide proactive inventory impact planning. Deliver month-ahead probability forecasts with vehicle exposure calculations and capacity recommendations.
- **Why this works**: Rental fleet managers live in constant fear of catastrophic damage events that pull hundreds of vehicles out of circulation. When you provide a multi-location hail forecast covering all their hail-corridor locations with specific vehicle exposure numbers (8,900 vehicles at risk June 1-30), you're giving them the planning tool they desperately need but don't have. The offer of "day-by-day probability forecast and pre-positioning recommendations" is pure gold for operational planning.
- **Data Sources**:
  - NOAA Storm Events Database - seasonal hail outlooks, event probability, geographic footprint
  - DentWizard Internal Data - historical damage rates by hail severity, turnaround times, capacity mobilization speed
  - Rental Company Location Data - lot addresses, vehicle concentrations by ZIP
- **Outreach Message template**:
  ```text
  Subject: June hail forecast for your 6 hail-corridor locations
  
  NOAA's seasonal outlook shows elevated hail risk June 1-30 across all 6 of your hail-corridor locations (Denver, OKC, Dallas, Wichita, Kansas City, Omaha).
  
  That's 8,900 vehicles at risk based on your lot concentrations.
  
  Want the day-by-day probability forecast and pre-positioning recommendations?
  ```
- **Data Requirement**: This play requires historical hail damage data showing: damage rates by hail severity, vehicle counts affected per event, turnaround time patterns, and capacity mobilization timelines across multiple locations.
                    Combined with NOAA forecasts and rental location mapping, this synthesis is unique to your operational history.

#### Play: Sensor Recalibration Cost Intelligence (PVP                     Internal Data | Strong - Strong (8.6/10))

- **What's the play?**: Use internal repair data to identify which newer vehicle models require ADAS sensor recalibration after PDR, adding unexpected costs. Provide insurance adjusters with a recalibration requirement matrix showing which models in their book have hidden cost factors they're not reserving for.
- **Why this works**: Insurance adjusters are getting blindsided by ADAS sensor recalibration costs on 2022+ vehicles. When you tell them "GMC Sierras require sensor recalibration on 73% of PDR repairs, adding $280 per claim," you're surfacing a cost factor they're likely not tracking yet. The quantified annual impact ($151K across 540 claims) makes it immediately actionable for reserve accuracy and rate adjustments. The offer of a full matrix for their top 15 models positions you as the expert who understands the changing economics of auto repair.
- **Data Sources**:
  - DentWizard Internal Repair Database - ADAS sensor recalibration requirements by vehicle make/model/year, frequency percentage, cost per recalibration
- **Outreach Message template**:
  ```text
  Subject: GMC Sierra sensor recalibration adding $280 per claim
  
  2022+ GMC Sierras require ADAS sensor recalibration after PDR on 73% of repairs, adding $280 per claim.
  
  At 540 Sierra claims annually in your Texas book, that's $151K in additional cost.
  
  Want the sensor recalibration requirement matrix for your top 15 models?
  ```
- **Data Requirement**: This play requires repair completion data showing which vehicle models require ADAS sensor recalibration, frequency rates, and associated costs across thousands of repairs.
                    This is proprietary operational intelligence only you have from servicing 2022+ vehicles with advanced safety systems.

#### Play: Urgent Hail Event Response (PQS                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Monitor near-term severe weather forecasts (24-48 hours out) and cross-reference with rental fleet locations to deliver urgent damage prevention alerts. Provide specific vehicle counts and historical damage rates to create immediate action urgency.
- **Why this works**: When you tell a fleet manager "2,890 vehicles in tomorrow's hail path" with specific location counts and historical damage rates (71% of vehicles damaged in last April's Tulsa storm), you're delivering time-critical intelligence they need RIGHT NOW. The action-oriented question "Is someone moving vehicles or securing indoor shelter tonight?" positions you as a partner thinking about their operational response, not a vendor pitching services. The extreme urgency (tomorrow's event) breaks through inbox noise.
- **Data Sources**:
  - NOAA Storm Events Database - near-term severe weather forecasts, hail size predictions, geographic paths
  - Rental Fleet Location Data - lot addresses, vehicle counts by location
  - DentWizard Historical Data - damage rates by hail severity and location from previous events
- **Outreach Message template**:
  ```text
  Subject: 2,890 vehicles in tomorrow's hail path
  
  Tomorrow's forecast shows severe hail for Tulsa where you operate 2,890 rental vehicles across 6 locations.
  
  Last April's Tulsa storm damaged 71% of vehicles in the direct path.
  
  Is someone moving vehicles or securing indoor shelter tonight?
  ```
- **Data Requirement**: This play requires real-time monitoring of NOAA severe weather alerts and historical damage rate data by event severity and location.
                    The synthesis of near-term forecasts with rental fleet locations and historical damage patterns creates urgency competitors can't match.

#### Play: Year-Over-Year Repair Cost Trend Analysis (PVP                     Internal Data | Strong - Strong (8.5/10))

- **What's the play?**: Track year-over-year PDR repair cost changes by vehicle model and identify which models have experienced significant cost increases due to design changes or new technology integration. Provide insurance adjusters with trend data they can use for rate filing justification.
- **Why this works**: Insurance adjusters struggle to justify rate increases without actuarial-grade data. When you tell them "Ram 1500 PDR costs increased 38% vs 2023 due to new sensor integration in model redesign," you're providing the specific causal explanation and quantified impact ($186K additional exposure across 620 claims) they need for rate filing submissions. The offer of a "model-year cost variance report for rate adjustment" directly supports their regulatory compliance process. This isn't sales - it's data they need to do their job.
- **Data Sources**:
  - DentWizard Internal Repair Database - year-over-year repair costs by vehicle make/model, design change tracking, technology integration notes
- **Outreach Message template**:
  ```text
  Subject: Ram 1500 repair costs up 38% year-over-year
  
  Our 2024 data shows Ram 1500 PDR costs increased 38% vs 2023 due to new sensor integration in model redesign.
  
  At 620 Ram claims annually in your Arizona book, that's $186K additional cost exposure.
  
  Want the model-year cost variance report for rate adjustment?
  ```
- **Data Requirement**: This play requires multi-year repair cost tracking by vehicle make/model with causal analysis of design changes and technology integration.
                    This is proprietary trend intelligence only you have from servicing thousands of vehicles across model years.

#### Play: Post-Damage Verification Alert (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Within 72 hours of documented hail events, send rental fleet managers specific vehicle damage estimates based on NOAA severity maps cross-referenced with their lot locations. Provide verifiable vehicle counts and revenue impact calculations.
- **Why this works**: When a hailstorm just hit, fleet managers are in damage assessment mode. By telling them "3,847 vehicles in your Denver ZIP codes got hit in the April 12th hailstorm" with a specific date and NOAA-verified damage count, you're delivering immediate situational intelligence they need for capacity planning. The revenue impact calculation (14 days turnaround = $2.1M revenue loss) translates the damage into business terms they care about. The offer to provide damage forecasts for other locations positions you as someone monitoring their entire footprint, not just responding to this one event.
- **Data Sources**:
  - NOAA Storm Events Database - recent hail events with dates, severity, geographic footprint
  - Rental Fleet Location Data - lot addresses and ZIP codes
  - DentWizard Historical Data - average turnaround times by damage severity
- **Outreach Message template**:
  ```text
  Subject: 3,847 rental cars hail-damaged in Denver last week
  
  NOAA confirms 3,847 vehicles in your Denver ZIP codes got hit in the April 12th hailstorm.
  
  At 14 days average PDR turnaround, that's potential $2.1M revenue loss if those cars sit idle.
  
  Want the damage forecast for your other hail-corridor locations?
  ```
- **Data Requirement**: This play requires rental fleet location mapping (GPS or addresses) and internal turnaround time data to calculate revenue impact.
                    The synthesis of NOAA damage data with specific rental locations and operational metrics is unique to your service history.

#### Play: PDR Feasibility Audit for Insurance Claims (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Analyze insurance claim photos from public records or data partnerships to identify cases where PDR was viable but traditional body shop methods (hood replacement) were approved instead. Show insurance adjusters specific examples of unnecessary parts and labor costs in their book.
- **Why this works**: Insurance adjusters manage claim costs but often can't distinguish between PDR-viable damage and replacement-required damage without specialized knowledge. When you tell them "47% of Hyundai Sonata hail claims in your book resulted in hood replacement when PDR was viable according to severity photos," you're revealing a systematic process inefficiency costing them $840 per claim. The question "Is someone doing PDR feasibility checks before approving replacements?" positions this as a process improvement opportunity, not a sales pitch. The specificity (210 Sonata claims, severity photos) proves this is real analysis, not a generic claim.
- **Data Sources**:
  - Insurance Claim Photo Databases - damage severity images, approved repair methods
  - DentWizard Internal Data - PDR feasibility classification criteria by damage type
  - NAIC Auto Insurance Database - claim volumes by vehicle model and insurer
- **Outreach Message template**:
  ```text
  Subject: Hyundai Sonata hood replacements avoidable with PDR
  
  47% of Hyundai Sonata hail claims in your book resulted in hood replacement when PDR was viable according to severity photos.
  
  That's $840 per claim in unnecessary parts and labor costs across 210 Sonata claims last year.
  
  Is someone doing PDR feasibility checks before approving replacements?
  ```
- **Data Requirement**: This play requires access to insurance claim photos and internal PDR feasibility classification expertise to identify cases where PDR could have replaced traditional repair methods.
                    The synthesis of claim photo analysis with repair cost data is unique to your technical expertise.

#### Play: Regional Hail Exposure Planning (PVP                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Provide rental fleet managers with monthly hail probability forecasts covering their multi-state operations, with vehicle exposure calculations and capacity planning recommendations. Deliver this as a planning tool for the upcoming month.
- **Why this works**: Rental companies operating across hail-prone states need regional risk visibility to optimize fleet distribution and pre-position repair capacity. When you provide "May outlook showing 68% probability of significant hail events across your OK-TX-CO-KS locations" with specific vehicle exposure (11,200 vehicles at elevated risk in 30 days), you're giving them the multi-state planning view their internal teams don't have. The offer of "weekly probability breakdown and repair capacity recommendations" turns this from interesting information into an actionable planning tool. This is consulting-grade intelligence delivered for free.
- **Data Sources**:
  - NOAA Storm Events Database - seasonal hail outlooks, regional probability forecasts
  - Rental Fleet Location Data - multi-state lot addresses and vehicle concentrations
  - DentWizard Internal Data - capacity availability by region, mobilization timelines
- **Outreach Message template**:
  ```text
  Subject: May 2025 hail outlook for your 4-state footprint
  
  NOAA's May outlook shows 68% probability of significant hail events across your OK-TX-CO-KS locations.
  
  That's 11,200 vehicles at elevated risk in a 30-day window.
  
  Want the weekly probability breakdown and repair capacity recommendations?
  ```
- **Data Requirement**: This play requires rental fleet multi-state location mapping and internal capacity availability data by region with mobilization timelines.
                    Combined with NOAA seasonal forecasts, this creates a planning tool competitors can't offer.

#### Play: PDR Cost Efficiency by Vehicle Model (PVP                     Internal Data | Strong - Strong (8.3/10))

- **What's the play?**: Identify vehicle models where PDR costs come in significantly lower than initial estimates due to favorable construction or panel accessibility. Provide insurance adjusters with positive variance data they can use to optimize reserve amounts and reduce loss adjustment expenses.
- **Why this works**: Insurance adjusters focus heavily on cost overruns but rarely capture positive variance opportunities. When you tell them "Honda CR-Vs average $340 for PDR vs $520 typical, that's a $1.5M annual savings opportunity if you steer policyholders to PDR," you're showing them how to improve loss ratios through better claim handling. The specificity (8,400 repairs, 35% lower costs due to steel panel construction) demonstrates deep technical knowledge. The offer to provide cost breakdowns for their other high-volume models positions you as a strategic partner helping them optimize loss adjustment expenses.
- **Data Sources**:
  - DentWizard Internal Repair Database - actual repair costs by vehicle make/model, construction materials, panel accessibility notes
- **Outreach Message template**:
  ```text
  Subject: Honda CR-Vs are your cheapest PDR repairs
  
  Across 8,400 repairs, Honda CR-Vs average $340 for PDR vs $520 typical - 35% lower due to steel panel construction.
  
  That's a $1.5M annual savings opportunity if you steer policyholders to PDR for CR-V claims.
  
  Want the cost breakdown for your other high-volume models?
  ```
- **Data Requirement**: This play requires repair cost data by vehicle make/model across thousands of repairs, showing favorable construction characteristics and cost efficiency patterns.
                    This is proprietary cost intelligence only you have from servicing high volumes of specific vehicle models.

#### Play: Model-Specific Cost Overrun Alert (PQS                     Public + Internal | Strong - Strong (8.2/10))

- **What's the play?**: Identify vehicle models where actual PDR repair costs consistently exceed initial estimates due to construction complexity (like aluminum body panels). Alert insurance adjusters to specific models in their portfolio where reserves are systematically understated.
- **Why this works**: Insurance adjusters live in fear of reserve inadequacy, which impacts loss ratios and regulatory reporting. When you tell them "Ford F-150s (2020-2023) are coming in 52% over initial estimates due to aluminum body complexity," you're alerting them to a systematic reserve problem in their book. The specificity (3,200 PDR claims analyzed, actual claim volume 840 F-150s in Texas region) proves you've done the analysis. The question "Is someone adjusting initial reserve amounts for these models?" positions this as a process improvement they should care about immediately.
- **Data Sources**:
  - DentWizard Internal Repair Database - initial estimate vs actual cost variance by vehicle make/model
  - NAIC Auto Insurance Database - claim volumes by vehicle model and insurer
- **Outreach Message template**:
  ```text
  Subject: Your Ford F-150 claims running 52% over estimate
  
  Analyzing 3,200 PDR claims, Ford F-150s (2020-2023) are coming in 52% over initial estimates due to aluminum body complexity.
  
  You processed 840 F-150 PDR claims last year in your Texas region.
  
  Is someone adjusting initial reserve amounts for these models?
  ```
- **Data Requirement**: This play requires repair completion data comparing initial estimates to actual costs by vehicle make/model, with construction material tracking.
                    The variance analysis is unique to your operational history of servicing thousands of vehicles.

#### Play: Vehicle Configuration Cost Impact (PQS                     Public + Internal | Strong - Strong (8.2/10))

- **What's the play?**: Identify vehicle configurations (like convertible soft tops) that dramatically increase PDR repair costs due to additional damage vectors. Show insurance adjusters how capturing configuration details at first notice of loss (FNOL) can improve reserve accuracy.
- **Why this works**: Insurance adjusters typically don't capture vehicle configuration details at FNOL, leading to reserve surprises later. When you tell them "Jeep Wranglers with soft tops average $920 in PDR costs vs $410 for hard tops due to interior damage from hail penetration," you're revealing a specific data point they're missing in their intake process. The quantified savings opportunity ($91K in reserve adjustment accuracy across 180 claims) makes this immediately actionable. The question "Who's capturing vehicle configuration details at FNOL?" positions this as a process improvement with clear ROI.
- **Data Sources**:
  - DentWizard Internal Repair Database - repair costs segmented by vehicle configuration (soft top vs hard top, etc.)
  - NAIC Auto Insurance Database - claim volumes by vehicle model and state
- **Outreach Message template**:
  ```text
  Subject: Jeep Wrangler soft tops driving up your PDR costs
  
  Jeep Wranglers with soft tops average $920 in PDR costs vs $410 for hard tops due to interior damage from hail penetration.
  
  At 180 Wrangler claims last year in your Colorado book, identifying soft vs hard top before estimating could save $91K in reserve adjustments.
  
  Who's capturing vehicle configuration details at FNOL?
  ```
- **Data Requirement**: This play requires repair cost data segmented by vehicle configuration details (convertible tops, sunroofs, etc.) showing cost impact patterns.
                    This is granular operational intelligence only you have from tracking configuration-specific damage patterns.

#### Play: Localized Damage Estimate by ZIP (PVP                     Public + Internal | Strong - Strong (8.1/10))

- **What's the play?**: Within 48 hours of a documented hail event, send rental fleet managers vehicle-by-vehicle damage probability estimates based on NOAA severity maps layered with their specific lot locations. Provide actionable vehicle counts for logistics planning.
- **Why this works**: After a hailstorm hits, fleet managers need to triage which locations were affected and how many vehicles need inspection. When you tell them "April 12th hailstorm damaged an estimated 892 vehicles in your Colorado Springs locations based on NOAA severity maps," you're providing immediate operational intelligence. The conversion to business impact (535 cars out of circulation for 2+ weeks if 60% need PDR) helps them quantify the problem. The offer of "vehicle-by-vehicle damage probability report" gives them the granular logistics data they need for scheduling inspections and coordinating repairs.
- **Data Sources**:
  - NOAA Storm Events Database - hail event dates, severity maps, geographic footprint
  - Rental Fleet Location Data - specific lot addresses in affected areas
  - DentWizard Internal Data - damage probability by hail severity, typical repair needs
- **Outreach Message template**:
  ```text
  Subject: Your Colorado Springs fleet just got hit
  
  April 12th hailstorm damaged an estimated 892 vehicles in your Colorado Springs locations based on NOAA severity maps.
  
  If 60% need PDR, that's 535 cars out of circulation for 2+ weeks.
  
  Want the vehicle-by-vehicle damage probability report?
  ```
- **Data Requirement**: This play requires rental fleet location mapping and internal damage probability modeling by hail severity level.
                    The synthesis of NOAA severity data with specific lot locations creates immediate operational value.

#### Play: PDR Success Rate Benchmarking (PVP                     Internal Data | Strong - Strong (8.1/10))

- **What's the play?**: Provide insurance adjusters with PDR success rate benchmarks by vehicle model, showing which models have the highest likelihood of successful repair without paint or panel replacement. Help them optimize claim steering policies based on model-specific success rates.
- **Why this works**: Insurance adjusters want to maximize PDR utilization (lower costs) but lack data on which vehicle models are best candidates. When you tell them "Chevrolet Equinox has a 94% PDR success rate - highest in the SUV class," you're giving them confidence to steer claims to PDR for that specific model. The fact that you know their claim volume (380 Equinox claims last year in Michigan) shows this is tailored intelligence, not generic marketing. The offer of success rate benchmarks for other high-volume models helps them build systematic claim handling protocols.
- **Data Sources**:
  - DentWizard Internal Repair Database - PDR success rates by vehicle make/model, showing percentage resolved without paint or panel replacement
- **Outreach Message template**:
  ```text
  Subject: Chevrolet Equinox PDR success rate: 94%
  
  Across 1,600 Equinox repairs, PDR resolved 94% of claims without paint or panel replacement - highest in the SUV class.
  
  You processed 380 Equinox claims last year in your Michigan book.
  
  Want the success rate benchmarks for your other high-volume models?
  ```
- **Data Requirement**: This play requires repair outcome data by vehicle make/model showing PDR success rates vs cases requiring paint or panel replacement.
                    This is proprietary outcome intelligence only you have from completing thousands of repairs per model.

#### Play: Pre-Event Hail Warning (PQS                     Public + Internal | Strong - Strong (8.0/10))

- **What's the play?**: Send rental fleet managers 7-day advance warnings when NOAA forecasts show severe hail probability for their operating regions, with vehicle exposure calculations and historical damage rate context. Provide enough lead time for proactive response.
- **Why this works**: Seven days advance notice allows fleet managers to actually do something about incoming hail risk - move vehicles, secure covered parking, pre-position staff. When you tell them "NOAA's 7-day forecast shows severe hail probability for Oklahoma City April 15-22 where you operate 2,100 rental vehicles," you're giving them actionable lead time. The historical context (last year's April storm damaged 68% of vehicles in the hail corridor) helps them understand the magnitude of potential impact. The question "Is someone coordinating pre-positioning or rapid response PDR capacity?" helps them route to the right internal stakeholder.
- **Data Sources**:
  - NOAA Storm Events Database - 7-day severe weather forecasts, hail probability
  - Rental Fleet Location Data - operating regions and vehicle counts
  - DentWizard Historical Data - historical damage rates by region and hail severity
- **Outreach Message template**:
  ```text
  Subject: Oklahoma City gets hit with hail April 15-22
  
  NOAA's 7-day forecast shows severe hail probability for Oklahoma City April 15-22 where you operate 2,100 rental vehicles.
  
  Last year's April storm damaged 68% of vehicles in the hail corridor.
  
  Is someone coordinating pre-positioning or rapid response PDR capacity?
  ```
- **Data Requirement**: This play requires rental fleet location identification and historical damage rate data from previous events in the same region.
                    The synthesis of forecast data with historical outcomes creates actionable planning intelligence.

#### Play: Imminent Hail Impact Alert (PQS                     Public + Internal | Strong - Strong (8.0/10))

- **What's the play?**: Send same-day hail alerts when NOAA forecasts show severe hail hitting rental fleet locations within hours. Provide specific vehicle counts at risk and percentage of fleet exposure to create maximum urgency.
- **Why this works**: When severe hail is hitting TONIGHT, the urgency is absolute. By telling them "Tonight's forecast shows golf ball-size hail for ZIP 75201-75204 where you have 1,240 vehicles," you're delivering time-critical intelligence they need in the next few hours. The conversion to fleet percentage (31% of DFW fleet at risk in a 4-hour window) helps them understand business impact. The routing question "Who handles your emergency damage response coordination?" acknowledges you might not be talking to the right person but need to get this intelligence to whoever IS responsible immediately.
- **Data Sources**:
  - NOAA Storm Events Database - same-day severe weather alerts, hail size predictions, timing
  - Rental Fleet Location Data - lot addresses by ZIP code, vehicle counts by location
- **Outreach Message template**:
  ```text
  Subject: 1,240 of your Dallas cars in hail zone tonight
  
  Tonight's forecast shows golf ball-size hail for ZIP 75201-75204 where you have 1,240 vehicles based on your lot addresses.
  
  That's 31% of your DFW fleet at risk in a 4-hour window.
  
  Who handles your emergency damage response coordination?
  ```
- **Data Requirement**: This play requires rental fleet location mapping by ZIP code and real-time monitoring of NOAA severe weather alerts.
                    The time-critical nature and specific ZIP-level targeting creates immediate urgency competitors can't match.

#### Play: Rental Delay Cost Quantification (PQS                     Public + Internal | Okay - Okay (7.9/10))

- **What's the play?**: Identify vehicle models where PDR turnaround times are significantly longer than comparable vehicles, driving up rental reimbursement expenses for insurance adjusters. Quantify the exact rental day exposure and cost impact.
- **Why this works**: Insurance adjusters track rental reimbursement costs closely but may not realize certain vehicle models drive disproportionate rental expenses due to longer repair times. When you tell them "Tesla Model 3 PDR repairs average 9 additional days vs comparable sedans due to technician certification requirements," you're surfacing a hidden cost driver. The calculation of exact exposure (4,320 extra rental days across 480 claims annually) makes this immediately quantifiable. The routing question "Who manages your rental reimbursement expense tracking?" helps get this to the right cost control stakeholder.
- **Data Sources**:
  - DentWizard Internal Repair Database - turnaround times by vehicle make/model, certification requirements
  - NAIC Auto Insurance Database - claim volumes by vehicle model and state
- **Outreach Message template**:
  ```text
  Subject: Tesla Model 3 PDR claims taking 9 days longer
  
  Tesla Model 3 PDR repairs average 9 additional days vs comparable sedans due to technician certification requirements.
  
  At 480 Model 3 claims annually in your California book, that's 4,320 extra rental days you're covering.
  
  Who manages your rental reimbursement expense tracking?
  ```
- **Data Requirement**: This play requires turnaround time tracking by vehicle make/model with causal analysis of delay factors (certification requirements, parts availability, etc.).
                    The synthesis of turnaround data with claim volumes creates specific cost impact intelligence.

#### Play: Reserve Accuracy Opportunity (PQS                     Public + Internal | Okay - Okay (7.8/10))

- **What's the play?**: Identify vehicle models where actual PDR costs consistently come in under initial reserves, creating opportunities for loss adjustment expense optimization. Show insurance adjusters where they're over-reserving and can improve reserve release timing.
- **Why this works**: While insurance adjusters worry about reserve inadequacy, they also care about reserve accuracy for financial reporting and loss ratio optimization. When you tell them "Subaru Outbacks are consistently coming in 22% under initial PDR estimates due to steel construction and panel accessibility," you're showing them where they can optimize reserve amounts. The specific numbers (reserving $520 but actual costs are $405 across 290 claims) proves this is real analysis. The question "Is someone capturing this reserve release for LAE optimization?" positions this as a financial reporting opportunity they should care about.
- **Data Sources**:
  - DentWizard Internal Repair Database - initial estimate vs actual cost variance by vehicle make/model
  - NAIC Auto Insurance Database - claim volumes by vehicle model and state
- **Outreach Message template**:
  ```text
  Subject: Subaru Outback repairs costing 22% less than estimates
  
  Subaru Outbacks are consistently coming in 22% under initial PDR estimates due to steel construction and panel accessibility.
  
  You're reserving $520 average but actual costs are $405 across 290 claims last year in your Colorado book.
  
  Is someone capturing this reserve release for LAE optimization?
  ```
- **Data Requirement**: This play requires comparison of initial reserve amounts to actual repair costs by vehicle make/model, showing favorable variance patterns.
                    The variance tracking is unique to your operational history of estimating and completing thousands of repairs.

#### Play: Fleet Expansion Risk Monitoring (PQS                     Public + Internal | Okay - Okay (7.7/10))

- **What's the play?**: Track rental fleet location expansion in hail-prone regions and alert fleet managers when they're scaling into higher-risk geographies. Provide historical hail frequency data for their new markets.
- **Why this works**: Fleet managers expanding into new markets may not realize the hail risk profile of their new locations. When you tell them "Your Austin locations added 420 vehicles in Q1, putting you at 2,100 total. Austin sits in the I-35 hail corridor with 7 severe events in the past 3 years," you're connecting their growth strategy to operational risk they need to plan for. The question "Who's managing damage preparedness as you scale that market?" positions this as a risk management conversation relevant to their expansion. The fact that you tracked their fleet growth (lot counts) shows you're paying attention to their business.
- **Data Sources**:
  - Rental Fleet Location Data - lot addresses and vehicle counts tracked over time
  - NOAA Storm Events Database - historical hail events by region
- **Outreach Message template**:
  ```text
  Subject: Your Austin fleet expanding into hail alley
  
  Your Austin locations added 420 vehicles in Q1 based on lot counts, putting you at 2,100 total.
  
  Austin sits in the I-35 hail corridor with 7 severe events in the past 3 years.
  
  Who's managing damage preparedness as you scale that market?
  ```
- **Data Requirement**: This play requires tracking rental fleet locations and vehicle counts over time to identify expansion patterns.
                    Combined with NOAA historical hail data, this creates risk planning intelligence for growing companies.

#### Play: Near-Miss Event Tracking (PVP                     Public + Internal | Okay - Okay (7.2/10))

- **What's the play?**: After major hail events, identify rental fleet locations that narrowly avoided damage and quantify the potential cost impact they dodged. Demonstrate proactive monitoring of their entire footprint.
- **Why this works**: Near-miss reporting is a novel approach that shows you're monitoring their fleet proactively, not just reacting to damage events. When you tell them "Last week's storm tracking showed Phoenix was 8 miles outside the hail corridor that damaged 2,400 vehicles," you're demonstrating that you're watching their risk exposure continuously. The quantification of what they avoided ($650 average per vehicle across 1,850 Phoenix vehicles = $1.2M) helps them understand the stakes. However, the immediate value is questionable - knowing they dodged a bullet is interesting but not immediately actionable. The offer of "near-miss report for other Sun Belt locations" is moderately compelling.
- **Data Sources**:
  - NOAA Storm Events Database - hail storm paths and severity footprints
  - Rental Fleet Location Data - lot addresses in nearby but unaffected areas
  - DentWizard Internal Data - average repair costs by hail severity
- **Outreach Message template**:
  ```text
  Subject: Your Phoenix fleet dodged $1.2M in hail damage
  
  Last week's storm tracking showed Phoenix was 8 miles outside the hail corridor that damaged 2,400 vehicles.
  
  Your 1,850 Phoenix vehicles would have averaged $650 each in PDR costs based on severity.
  
  Want the near-miss report for your other Sun Belt locations?
  ```
- **Data Requirement**: This play requires rental fleet location mapping and tracking of NOAA hail storm paths to identify near-miss scenarios.
                    The proactive monitoring demonstrates risk management partnership but value is more contextual than immediately actionable.

---

## HUB International (hubinternational.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/hubinternational-com)
**Strategic Summary**: Playbook combines internal historical claims patterns, OSHA establishment data, and EPA ECHO records to deliver predictive injury forecasts and violation replication risk analysis across multi-site operator portfolios.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your insurance program

Hi Jennifer,

I noticed your company is growing rapidly - congrats on the recent expansion!

At Hub International, we help mid-market companies like yours consolidate their insurance programs across multiple locations. Our clients typically see 15-20% savings on total cost of risk.

We've worked with several companies in your industry and would love to show you how we can help optimize your insurance strategy.

Do you have 15 minutes next week for a quick call?

Best,
Mike
Hub International
```

### ✓ The New Way: GTM Plays

#### Play: Boston site matches your 2022 injury pattern (PVP                     Internal Data | Strong - Strong (9.3/10))

- **What's the play?**: Use Hub's historical claims data on the customer's own facilities to identify current locations showing identical risk patterns to past locations where major claims occurred. This creates a "time machine" effect - showing them their future based on their own past.
- **Why this works**: You're using their own historical data as the evidence. This is irrefutable - they can't dismiss it as "not applicable to us" because it IS them. The specific cost figure from their past claim makes it tangible. You're helping them learn from their own mistakes, which is genuinely valuable.
- **Data Sources**:
  - Hub Internal Claims Database - longitudinal facility data, near-miss patterns, equipment types, shift patterns, claim costs by location
- **Outreach Message template**:
  ```text
  Subject: Boston site matches your 2022 injury pattern
  
  Your Boston facility at 450 Arsenal Street is tracking identical to your Newark site in Q1 2022 - same near-miss frequency, same equipment types, same shift patterns.
  
  Newark had 2 recordable injuries in March 2022 costing $87K in workers' comp.
  
  Should I send you the Newark timeline comparison?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's historical claims data and facility patterns from your system. Only works for existing customers with multi-year history.
                    Only works for upselling existing customers, not cold acquisition.

#### Play: Miami warehouse - 45-day injury forecast (PVP                     Public + Internal | Strong - Strong (9.2/10))

- **What's the play?**: Combine the prospect's public near-miss and safety data with Hub's proprietary predictive model (built on 60+ comparable facilities) to deliver a specific probability forecast with a 45-day timeline. This makes the prediction testable and urgent.
- **Why this works**: The 45-day window creates urgency while giving them time to act. The 68% probability with sample size (60 warehouses) makes the prediction credible, not sensational. You're offering recommended interventions, making this immediately actionable. The pattern explanation shows expertise.
- **Data Sources**:
  - Hub Internal Claims Database - near-miss data, first-aid incidents, training records, predictive modeling across customer facilities
  - OSHA Establishment Search - facility-specific inspection and violation history
- **Outreach Message template**:
  ```text
  Subject: Your Miami warehouse - 45-day injury forecast
  
  Miami warehouse at 2200 NW 84th Ave shows pattern we see before OSHA recordables: 7 near-misses in January, 3 first-aid incidents, zero follow-up training logged.
  
  Based on 60 comparable warehouses, you have a 68% probability of recordable injury in the next 45 days.
  
  Want the recommended interventions for this site?
  ```
- **Data Requirement**: This play requires Hub's proprietary predictive model built on aggregated near-miss data, first-aid incidents, and training records across 60+ comparable customer facilities. Must track which risk signatures correlate with recordable injuries.
                    Combined with public OSHA data to verify facility compliance history. This synthesis is unique to Hub's business.

#### Play: St. Louis site matches injury pattern (PVP                     Internal Data | Strong - Strong (9.2/10))

- **What's the play?**: Use Hub's historical claims data to match current risk patterns at one facility to past incidents at another of their facilities. Show them they're about to repeat a costly mistake with specific dollar figures from their own history.
- **Why this works**: Uses their own historical data as proof. They can't dismiss this as "not relevant to us" - it IS them. The exact cost from Kansas City ($94K) makes the risk tangible. Pattern details are verifiable in their own records. Helps them prevent repeating costly mistakes.
- **Data Sources**:
  - Hub Internal Claims Database - multi-year facility data, near-miss patterns, maintenance records, staffing data, historical claim costs
- **Outreach Message template**:
  ```text
  Subject: Your St. Louis site matches injury pattern
  
  St. Louis warehouse at 4500 Fyler Avenue shows identical pattern to your 2023 Kansas City injury: 6 near-misses in 30 days, forklift maintenance overdue, weekend shift understaffed.
  
  Kansas City cost $94K in workers' comp in March 2023.
  
  Should I send the KC incident timeline comparison?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's multi-year facility data and claims history from your system. Only works for existing customers with historical claims in your database.
                    Only works for upselling existing customers, not cold acquisition.

#### Play: Denver warehouse - March injury predicted (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Combine facility-specific public safety data with Hub's predictive model to deliver a specific date-based injury forecast. Multiple risk factors (near-misses, maintenance delays, training gaps) create urgency and show thorough analysis.
- **Why this works**: Specific address and exact metrics show real research. Multiple risk factors identified (near-misses, maintenance, training) demonstrate thorough analysis. 78% probability with specific date (March 15th) is testable and urgent. Maintenance and training gaps are immediately actionable. Offers practical intervention checklist.
- **Data Sources**:
  - Hub Internal Claims Database - near-miss tracking, equipment maintenance schedules, training records, predictive modeling
  - OSHA Establishment Search - facility inspection and violation history
- **Outreach Message template**:
  ```text
  Subject: Your Denver warehouse - March injury predicted
  
  Denver distribution center at 3800 Quebec Street has pattern we see before recordables: 9 near-misses since January 1st, equipment maintenance 22 days overdue, no safety training logged in 45 days.
  
  Our model predicts 78% probability of OSHA recordable by March 15th.
  
  Should I send the intervention checklist?
  ```
- **Data Requirement**: This play requires Hub's system to track near-miss incidents, equipment maintenance schedules, and training records across customer facilities, with predictive modeling to correlate these factors to injury likelihood.
                    Combined with public OSHA data for facility compliance history. This synthesis is unique to Hub's risk management platform.

#### Play: Phoenix warehouse shows pre-claims pattern (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Use Hub's internal pattern recognition (built on data from similar warehouses) combined with the facility's public OSHA data to identify pre-claims risk indicators. Offer to extend the analysis across their entire 12-location portfolio.
- **Why this works**: Specific address and exact incident counts show real work. The predictive insight is genuinely valuable - catching issues before they become claims. 60-day and 90-day timeframes are precise and urgent. Pattern recognition demonstrates expertise. Offering analysis across all 12 locations creates broader value.
- **Data Sources**:
  - Hub Internal Claims Database - near-miss patterns, first-aid incidents, workers' comp claims across comparable facilities
  - OSHA Establishment Search - facility-specific safety records and violations
- **Outreach Message template**:
  ```text
  Subject: Your Phoenix warehouse shows pre-claims pattern
  
  Your Phoenix location at 890 Commerce Drive shows 3 OSHA near-miss reports in 60 days plus 2 workers' comp first aid incidents.
  
  That's the pattern we see 90 days before recordable injuries at similar warehouses.
  
  Want the risk breakdown for all 12 of your locations?
  ```
- **Data Requirement**: This play requires Hub to aggregate workers' comp claims data, OSHA reports, and near-miss data across customers to identify pre-claims patterns that predict recordable injuries 90 days out.
                    Combined with public OSHA near-miss reports to create predictive insights. This pattern recognition is proprietary to Hub.

#### Play: Chicago restaurant group - 3 sites flagged (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Use Hub's proprietary risk scoring model (built on claims history, inspection data, and facility characteristics) to identify the highest-risk locations in a multi-site operator's portfolio. Show concentration risk - 3 locations driving 60% of total exposure.
- **Why this works**: Naming specific neighborhoods (River North, Wicker Park, Lincoln Park) is verifiable and shows local knowledge. Risk scores are precise and location-specific (8.2, 7.9, 8.4 out of 10). The 60% concentration insight is immediately actionable for risk allocation. Identifies portfolio-wide risk concentration. Easy yes/no to get site-specific factors.
- **Data Sources**:
  - Hub Internal Risk Scoring Model - proprietary scoring using claims history, inspection data, and facility characteristics across customer locations
- **Outreach Message template**:
  ```text
  Subject: Chicago restaurant group - 3 sites flagged
  
  Your Chicago locations at River North, Wicker Park, and Lincoln Park all show elevated slip-and-fall risk scores (8.2, 7.9, 8.4 out of 10).
  
  Those 3 sites account for 60% of your premises liability exposure across all 18 locations.
  
  Want the site-specific risk factors for each?
  ```
- **Data Requirement**: This play requires Hub to develop proprietary risk scoring models using claims history, inspection data, and facility characteristics across customer locations. Must calculate exposure concentration by location.
                    This is proprietary data only Hub has - competitors cannot replicate this play without similar risk modeling infrastructure.

#### Play: 5 of your locations show pre-claims patterns (PVP                     Public + Internal | Strong - Strong (9.0/10))

- **What's the play?**: Analyze Hub's internal near-miss and incident data across the prospect's full 23-facility portfolio to identify concentration risk - 5 locations with 67% of near-miss volume but only 35% of workforce. This reveals where to focus safety resources.
- **Why this works**: Specific city names are verifiable against their actual locations. The percentage analysis (67% near-misses from 35% of workforce) shows real analytical work. Concentration risk insight is immediately valuable for resource allocation. Covers their full portfolio (23 facilities) showing comprehensive analysis. Easy yes to get full breakdown.
- **Data Sources**:
  - Hub Internal Claims Database - near-miss data, workforce size, risk indicators aggregated across all customer locations
- **Outreach Message template**:
  ```text
  Subject: 5 of your locations show pre-claims patterns
  
  Pulled risk indicators across your 23 facilities - 5 locations show elevated pre-claims patterns: Dallas, Phoenix, Tampa, Charlotte, Nashville.
  
  Those 5 sites have 67% of your near-miss volume but only 35% of your workforce.
  
  Want the site-by-site risk breakdown?
  ```
- **Data Requirement**: This play requires Hub to aggregate near-miss data, workforce size, and risk indicators across all customer locations to identify concentration patterns and allocate safety resources optimally.
                    Combined with facility-level workforce data to calculate concentration risk. This analysis is unique to Hub's risk management platform.

#### Play: Multi-Violation Facilities with Concurrent OSHA and EPA Enforcement (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target manufacturing facilities with concurrent OSHA serious violations AND EPA enforcement actions in the past 12 months. These companies face compounding regulatory scrutiny, multiplied penalty exposure, and insurance carriers re-evaluating coverage - indicating systemic safety and environmental management failures.
- **Why this works**: Exact dollar amounts and dates prove you did real research. Management system failure insight shows expertise - this is why penalties escalate with concurrent violations. The penalty escalation implication is specific and valuable. Coordination question addresses a real organizational challenge. Shows understanding of cross-agency enforcement complexity.
- **Data Sources**:
  - OSHA IMIS Enforcement Data - establishment_name, violation_type, citation_amount, citation_date
  - EPA ECHO Database - facility_name, violations, enforcement_actions, permit_status
- **Outreach Message template**:
  ```text
  Subject: Portland facility - $289K combined penalty proposed
  
  Your Portland plant received OSHA citations on December 10th ($152K proposed) and EPA Clean Water Act violations on December 28th ($137K proposed).
  
  Both agencies cited management system failures - that pattern escalates penalties.
  
  Is one person coordinating both responses?
  ```

#### Play: Atlanta site trending toward recordable injury (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Combine facility-specific public near-miss data with Hub's predictive model (built on 40 similar facilities) to deliver a 73% probability forecast with 120-day timeline. Multiple actionable risk factors create urgency.
- **Why this works**: Specific location and equipment type (forklift) shows focus. Exact count (5 near-misses) and date (since November 1st) add precision. Predictive model with sample size (40 facilities) makes the 73% probability credible. 120-day window gives them time to intervene. One-word answer CTA lowers friction.
- **Data Sources**:
  - Hub Internal Claims Database - near-miss tracking, corrective action logs, predictive modeling across 40+ comparable facilities
  - OSHA Establishment Search - facility near-miss reports and corrective actions
- **Outreach Message template**:
  ```text
  Subject: Atlanta site trending toward recordable injury
  
  Your Atlanta distribution center has had 5 forklift near-misses since November 1st with no corrective actions logged.
  
  We tracked 40 similar facilities - 73% had OSHA recordables within 120 days without intervention.
  
  Should I send you the forklift incident timeline?
  ```
- **Data Requirement**: This play requires Hub to track near-miss incidents, corrective actions, and use predictive modeling across 40+ customer facilities to correlate forklift near-misses without intervention to recordable injuries.
                    Combined with public OSHA near-miss data to create predictive risk scores. This modeling is proprietary to Hub.

#### Play: Multi-Violation Facilities with Concurrent OSHA and EPA Enforcement (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target manufacturing facilities showing compound compliance failures across both OSHA and EPA. Concurrent enforcement triggers cross-agency scrutiny and stacked penalties, creating urgent need for comprehensive insurance review and risk management intervention.
- **Why this works**: Exact address and specific violation counts prove you did real research on this facility. Dates (March 3rd, March 18th) show this is recent and current. Cross-agency risk is a non-obvious insight most brokers miss. Simple routing question makes it easy to respond. 'Stacked penalties' is a concrete implication of dual enforcement.
- **Data Sources**:
  - OSHA IMIS Enforcement Data - establishment_name, violation_type, citation_date
  - EPA ECHO Database - facility_name, violations, enforcement_actions
- **Outreach Message template**:
  ```text
  Subject: Your Dallas plant has open OSHA + EPA cases
  
  Your Dallas facility at 1250 Industrial Blvd has 4 open OSHA serious violations from March 3rd and an EPA hazardous waste notice from March 18th.
  
  Concurrent enforcement triggers cross-agency scrutiny and stacked penalties.
  
  Who's managing the dual abatement timeline?
  ```

#### Play: San Diego restaurant - slip risk score 8.9/10 (PVP                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: Use Hub's proprietary slip-and-fall risk scoring model (built on facility characteristics, claims history, and environmental factors) to identify the highest-risk location in a multi-unit restaurant group. Explain the scoring factors to demonstrate thoroughness.
- **Why this works**: Specific address and precise risk score (8.9 out of 10) show detailed analysis. Explaining scoring factors (floor, traffic, weather) demonstrates methodology transparency. Portfolio context (22 locations) proves comprehensive analysis. Highest risk designation creates urgency. Offers actionable mitigations.
- **Data Sources**:
  - Hub Internal Risk Scoring Model - proprietary slip-and-fall scoring using facility characteristics, claims history, and environmental factors
- **Outreach Message template**:
  ```text
  Subject: San Diego restaurant - slip risk score 8.9/10
  
  Your San Diego location at 1250 Prospect Street has slip-and-fall risk score of 8.9 out of 10 based on floor material, traffic patterns, and recent weather incidents.
  
  That's highest risk across your 22-location restaurant group.
  
  Want the specific mitigation recommendations?
  ```
- **Data Requirement**: This play requires Hub to develop proprietary slip-and-fall risk scoring using facility characteristics, claims history, and environmental factors. Must calculate scores across all locations to identify highest risk.
                    This is proprietary data only Hub has - competitors cannot replicate this play without similar risk scoring infrastructure.

#### Play: CMS 1-2 Star Facilities Approaching Special Focus Facility Status (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target skilled nursing facilities with 1-2 star CMS ratings showing two consecutive quarters of low performance. These facilities are SFF candidates facing mandatory compliance intervention, increased liability exposure, and potential loss of Medicare/Medicaid reimbursement.
- **Why this works**: Specific facility name and exact rating progression show real research. Date precision (December 8th survey) adds credibility. SFF threat is immediate and concrete for this industry. Easy routing question lowers response friction. Address confirms you know which specific location is at risk.
- **Data Sources**:
  - CMS Skilled Nursing Facility Quality Reporting Program - facility_name, overall_rating, quality_measures, survey_dates
- **Outreach Message template**:
  ```text
  Subject: 3 health deficiencies at your Maple Grove location
  
  Your Maple Grove facility had 3 immediate jeopardy citations on November 15th - medication errors and fall protocols.
  
  You're now at 1.8 stars overall, one more survey cycle from SFF status.
  
  Is someone coordinating the correction plan across all locations?
  ```

#### Play: Multi-Violation Facilities with Concurrent OSHA and EPA Enforcement (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target manufacturing facilities with overlapping OSHA and EPA enforcement deadlines in the same month. This creates coordination challenges and compressed response timelines that most companies struggle to manage without broker support.
- **Why this works**: Specific violation types (lockout/tagout, machine guarding, stormwater) show detailed research. Exact dates (February 8th, February 14th) create timeline precision. Overlapping March 22nd deadline is the non-obvious problem requiring coordination. Coordination question is genuinely useful and shows understanding of compliance complexity.
- **Data Sources**:
  - OSHA IMIS Enforcement Data - violation_type, citation_date, abatement_deadline
  - EPA ECHO Database - violations, enforcement_actions, compliance_deadlines
- **Outreach Message template**:
  ```text
  Subject: Seattle plant - 6 violations across 2 agencies
  
  Your Seattle facility has 4 OSHA violations from February 8th (lockout/tagout, machine guarding) and 2 EPA stormwater violations from February 14th.
  
  Both in active abatement periods with overlapping March 22nd deadlines.
  
  Are you coordinating responses or handling separately?
  ```

#### Play: ASC Quality Deterioration with Infection Rate Increases (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target ambulatory surgery centers showing quarter-over-quarter increases in surgical site infection rates above CMS quality thresholds. These facilities face imminent CMS quality penalties, medical malpractice claim exposure, and potential loss of Medicare certification.
- **Why this works**: Specific facility and exact infection percentage (3.2%) show real data work. Quarter-over-quarter comparison (1.1% to 3.2%) demonstrates trend analysis. CMS threshold (2.5%) and penalty effective date (April 2025) make it actionable and urgent. Easy question about investigation ownership creates simple next step.
- **Data Sources**:
  - CMS Ambulatory Surgical Center Quality Reporting Dataset - facility_name, surgical_site_infections, patient_safety_indicators
- **Outreach Message template**:
  ```text
  Subject: Westside Surgery Center infection rate jumped to 3.2%
  
  Your Westside Surgery Center reported 3.2% surgical site infection rate for Q4 2024, up from 1.1% in Q3.
  
  That's above the 2.5% CMS threshold for quality measure penalties starting April 2025.
  
  Who's investigating the Q4 spike?
  ```

#### Play: Multi-Violation Facilities with Concurrent OSHA and EPA Enforcement (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target facilities where both agencies cited management system failures - this pattern escalates penalties and triggers more aggressive enforcement. Shows understanding of how violations compound across agencies.
- **Why this works**: Exact dollar amounts ($152K + $137K = $289K) and dates show real research. Management system failure citation is a valuable insight - this is why penalties escalate. Penalty escalation implication is specific and concerning. Coordination question addresses real organizational challenge. Shows cross-agency enforcement expertise.
- **Data Sources**:
  - OSHA IMIS Enforcement Data - citation_amount, citation_date, violation_classification
  - EPA ECHO Database - violations, enforcement_actions, penalty_amounts
- **Outreach Message template**:
  ```text
  Subject: Minneapolis plant - dual agency enforcement active
  
  Your Minneapolis facility has 5 OSHA serious violations from November 20th (fall protection, electrical) and EPA hazardous waste citations from December 3rd.
  
  Both agencies are in contestation period through February 28th.
  
  Who's managing the dual legal response timeline?
  ```

#### Play: CMS 1-2 Star Facilities Approaching Special Focus Facility Status (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target skilled nursing facilities that dropped from 2-star to 1.5-star rating after a recent survey, putting them in SFF candidate territory. CMS triggers enhanced oversight at under 2.0 stars for 2 consecutive quarters.
- **Why this works**: Specific facility name and exact rating drop (2.1 to 1.5 stars) show precise research. Address (456 Oak Street) confirms you know which location. SFF threshold explanation (under 2.0 stars for 2 quarters) demonstrates expertise. December 8th survey date is recent and verifiable. Easy routing question lowers friction.
- **Data Sources**:
  - CMS Skilled Nursing Facility Quality Reporting Program - facility_name, overall_rating, survey_dates, quality_measures
- **Outreach Message template**:
  ```text
  Subject: Sunset Manor dropped to 1.5 stars in Q4
  
  Your Sunset Manor facility at 456 Oak Street dropped from 2.1 to 1.5 stars after the December 8th survey.
  
  That's SFF candidate territory - CMS triggers enhanced oversight at <2.0 stars for 2 consecutive quarters.
  
  Who's leading your survey prep for Q1?
  ```

#### Play: ASC Quality Deterioration with Infection Rate Increases (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target ASCs showing quarter-over-quarter infection rate increases above CMS penalty thresholds. Calculate exact distance above threshold (1.6 percentage points) to create urgency around quality improvement initiatives.
- **Why this works**: Exact numbers (9 infections in 219 procedures = 4.1%) show real calculation work. Quarter comparison (1.2% to 4.1%) is precise trend analysis. Distance above threshold (1.6 percentage points) creates specific urgency. QI team question is appropriate for this industry. Root cause focus is helpful framing.
- **Data Sources**:
  - CMS Ambulatory Surgical Center Quality Reporting Dataset - facility_name, surgical_site_infections, quarterly_comparisons
- **Outreach Message template**:
  ```text
  Subject: Northshore Surgery - infection rate doubled Q3 to Q4
  
  Northshore Surgery Center went from 1.3% SSI rate in Q3 to 2.8% in Q4 2024 (6 infections in 214 procedures).
  
  You're 0.3% above CMS penalty threshold effective April 1st.
  
  Has infection control reviewed the 6 Q4 cases yet?
  ```

#### Play: ASC Quality Deterioration with Infection Rate Increases (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target ASCs with recent infection spikes in the past 60 days showing significant elevation above CMS penalty thresholds. Create urgency by focusing on recent timeframe and asking about common factor investigation.
- **Why this works**: Exact date range (December 1st to January 30th) and procedure count (142) show real analysis. Calculated rate (3.5%) demonstrates data work. Distance above threshold (1.0 percentage point) is precise. 60-day timeframe creates urgency. Common factor question is appropriate for infection investigation.
- **Data Sources**:
  - CMS Ambulatory Surgical Center Quality Reporting Dataset - facility_name, surgical_site_infections, infection_dates, procedure_volumes
- **Outreach Message template**:
  ```text
  Subject: Bayview Surgery - 5 SSIs in last 60 days
  
  Bayview Surgery Center reported 5 surgical site infections in the last 60 days (December 1st to January 30th) out of 142 procedures.
  
  That's 3.5% rate - you're 1.0 percentage point above CMS penalty threshold.
  
  Has infection control identified the common factor?
  ```

#### Play: ASC Quality Deterioration with Infection Rate Increases (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target ASCs showing dramatic infection rate increases (4 infections in December vs 0.9% in Q3). Identify potential root causes (protocol changes or patient mix shifts) to demonstrate analytical thinking.
- **Why this works**: Specific month (December) and procedure count (89) show precision. Percentage calculated (4.5%) demonstrates data work. Comparison to their own Q3 baseline (0.9%) shows trend analysis. Identifying potential root causes (protocols or patient mix) adds value. Direct question to medical director is appropriate routing.
- **Data Sources**:
  - CMS Ambulatory Surgical Center Quality Reporting Dataset - facility_name, surgical_site_infections, monthly_trends, procedure_volumes
- **Outreach Message template**:
  ```text
  Subject: 4 post-op infections at Riverside ASC in December
  
  Riverside ASC had 4 reported surgical site infections in December out of 89 procedures (4.5% rate).
  
  Your Q3 rate was 0.9% - something changed in your protocols or patient mix.
  
  Is your medical director reviewing December cases?
  ```

#### Play: ASC Quality Deterioration with Infection Rate Increases (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target ASCs with significant infection rate increases in Q4 showing elevation into CMS penalty zone. Focus on the sudden spike magnitude to create urgency around quality improvement.
- **Why this works**: Exact numbers (9 infections in 219 procedures) show real calculation. Quarter comparison is precise trend analysis. Distance above threshold (1.6 points) creates specific concern. 'Penalty zone' language is clear. Root cause focus is helpful framing for quality improvement.
- **Data Sources**:
  - CMS Ambulatory Surgical Center Quality Reporting Dataset - facility_name, surgical_site_infections, quarterly_comparisons
- **Outreach Message template**:
  ```text
  Subject: Lakeside ASC - Q4 infection spike to 4.1%
  
  Lakeside ASC reported 4.1% surgical site infection rate for Q4 (9 infections in 219 procedures), up from 1.2% in Q3.
  
  That's 1.6 percentage points above CMS quality threshold - penalty zone.
  
  Has your QI team identified the Q4 root cause?
  ```

#### Play: CMS 1-2 Star Facilities Approaching Special Focus Facility Status (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target facilities showing two-quarter persistence at 1.9 stars - just 0.1 points above SFF threshold. Use CMS review timing (March for April designation) to create urgency around February survey readiness.
- **Why this works**: Two-quarter persistence (Q3 and Q4 2024) shows pattern tracking over time. Specific margin (0.1 points above threshold) creates precision and urgency. March review timing is accurate CMS process knowledge. Suggesting February survey readiness push is practical and timely. Question implies reasonable action path.
- **Data Sources**:
  - CMS Skilled Nursing Facility Quality Reporting Program - facility_name, overall_rating, quarterly_ratings, survey_cycles
- **Outreach Message template**:
  ```text
  Subject: Oakwood Manor at 1.9 stars for 2 quarters
  
  Oakwood Manor has been at 1.9 stars for Q3 and Q4 2024 - just 0.1 points above SFF threshold.
  
  CMS reviews SFF candidates in March for the April designation cycle.
  
  Is your team planning a February survey readiness push?
  ```

#### Play: CMS 1-2 Star Facilities Approaching Special Focus Facility Status (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target facilities with recent January survey showing significant drop into SFF watch territory. Use the recent survey date and next survey timing to create urgency around follow-up preparation.
- **Why this works**: Recent survey date (January 18th) is very current and verifiable. Rating drop is significant (0.5 points from 2.2 to 1.7). 'SFF watch territory' is accurate terminology for this rating level. February follow-up timing is logical based on CMS inspection patterns. Follow-up survey expectation is reasonable given the rating drop.
- **Data Sources**:
  - CMS Skilled Nursing Facility Quality Reporting Program - facility_name, overall_rating, survey_dates, rating_trends
- **Outreach Message template**:
  ```text
  Subject: Cedar Ridge - 1.7 stars after January survey
  
  Cedar Ridge facility scored 1.7 stars on the January 18th survey, down from 2.2 in October.
  
  You're in SFF watch territory - next survey determines March designation.
  
  Is someone preparing for the likely February follow-up?
  ```

#### Play: CMS 1-2 Star Facilities Approaching Special Focus Facility Status (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target facilities showing rating decline with downward momentum heading into Q1. Use the concept of 'trajectory' to emphasize the trend is as concerning as the current rating.
- **Why this works**: Specific rating drop (2.4 to 2.0) with timeframe (September to December) shows tracking. 'Downward momentum' captures the trend concern beyond just the current rating. SFF threshold language (exactly at 2.0) is accurate. Q1 2025 timing makes it current and urgent. Simple routing question creates easy next step.
- **Data Sources**:
  - CMS Skilled Nursing Facility Quality Reporting Program - facility_name, overall_rating, survey_dates, rating_trajectories
- **Outreach Message template**:
  ```text
  Subject: Pinewood Care - 2.0 stars with declining trajectory
  
  Pinewood Care dropped from 2.4 to 2.0 stars between September and December surveys.
  
  You're exactly at SFF threshold with downward momentum heading into Q1 2025.
  
  Who should I route this to for February survey prep?
  ```

---

## Insurity (insurity.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/insurity-com)
**Strategic Summary**: Playbook outlines the Blueprint GTM methodology for insurance software using government databases and regulatory filings to surface specific pain situations for P&amp;C carriers.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Strong PQS (9.0/10)
                Target ICP: P&C property insurers with ≥5% market share in hurricane-prone coastal states (FL, TX, LA, NC, SC)
                Trigger Event: Major hurricane (Category 2+) makes landfall in a region where carrier has significant homeowners' exposure
                Why This Works: Carriers know a hurricane hit, but they DON'T immediately have their exact policy count in the impact zone or projected claim volume. This message combines NOAA storm data + state-level market share data + industry claim filing benchmarks to deliver a claim volume projection that helps them allocate adjusters and prepare for the surge. The 9.0/10 buyer score reflects exceptional situation recognition (exact hurricane, specific county, verified damage estimates) and high insight value (claim volume projection they don't have).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - NOAA Storm Events Database - Hurricane landfall dates, affected counties, property damage estimates (EVENT_TYPE, DAMAGE_PROPERTY, BEGIN_DATE, CZ_NAME fields) 95% confidence
  - FEMA Disaster Declarations API - Federal disaster numbers, declaration dates (disasterNumber, declarationDate fields) 95% confidence
  - Florida OIR Market Share Reports - Carrier homeowners' market share by county (Company_Name, County, Market_Share_Percent fields) 90% confidence
  - Industry Benchmark: Hurricane claim filing rates by category (Insurance Information Institute historical data) 70% confidence
  - "FEMA declared disaster #4872" → Direct from OpenFEMA API (disasterNumber field), cross-referenced with NOAA storm event
  - "8.2% homeowners' market share in Pinellas County" → Florida OIR annual market share report, filtered to carrier + county + homeowners line
  - "~12,400 policies in impact zone" → Total Pinellas County homeowners policies (151,000 from OIR) × 8.2% market share = 12,382 policies
  - "15-25% file claims (typical for Cat 3)" → Industry benchmark from Insurance Information Institute historical hurricane data
  - "1,860-3,100 claims" → 12,400 policies × 15% = 1,860 (low end); 12,400 × 25% = 3,100 (high end)

#### Play:  (PQS |  - Strong PQS (8.6/10)
                Alternative Angle: Instead of claim volume projection, this version focuses on the policy identification gap - highlighting that carriers with geographic mapping tools (like SpatialKey) can instantly locate exposed policies, while those without are still manually searching records days later.)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - "$4.2B in property damage Oct 9-11" → NOAA Storm Events DB, sum of DAMAGE_PROPERTY field for all event records in Pinellas County during hurricane dates
  - "8.2% of homeowners' policies" → Same as Play 1 (Florida OIR market share data)
  - "~12,400 policies" → Same calculation as Play 1 (total county policies × market share)
  - "60 seconds vs days" → SpatialKey product capability (instant geographic mapping) vs industry benchmark for manual policy searches

#### Play:  (PQS |  - Strong PQS (8.0/10)
                Target ICP: P&C property insurers in coastal states immediately after a major CAT event (within 72-96 hours post-landfall)
                Trigger Event: Hurricane/tornado landfall + 72 hours elapsed (industry standard window for initial policyholder contact)
                Why This Works: This is a TIMING play that creates urgency around the 72-hour industry standard for CAT response. Carriers are in crisis mode, and highlighting that competitors with geographic mapping tools have already identified and contacted high-priority policyholders creates competitive pressure. The 8.0/10 score reflects strong timing urgency and industry benchmark credibility, though it's less specific than Play 1 (no carrier-specific policy counts).)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - NOAA Storm Events Database - Hurricane landfall timestamps for elapsed time calculation 95% confidence
  - Industry Standard: Property Casualty Insurers Association of America (PCI) CAT response guidelines - 72-hour initial contact window 90% confidence
  - Competitive Benchmark: Insurity SpatialKey customer list (publicly available on Insurity website) - identifies which carriers in the market have geographic mapping capabilities 85% confidence
  - "3 days since Milton landfall" → NOAA/National Hurricane Center landfall timestamp, subtract from current date = elapsed days
  - "72 hours—industry standard" → PCI CAT response guidelines (publicly available best practices for initial policyholder contact in high-severity events)
  - "competitors with SpatialKey already reached accounts" → Insurity website customer list identifies carriers using SpatialKey; if known competitor uses it, this is factual; otherwise adjust wording to "carriers with mapping tools"

#### Play:  (PQS |  - Solid PQS (7.6/10)
                Target ICP: P&C insurance carriers that recently announced acquisition of another carrier or book of business (30-90 days post-announcement)
                Trigger Event: M&A announcement in insurance trade press, state insurance department assumption reinsurance filings, or SEC 8-K filing (for public companies)
                Why This Works: This is a SITUATION play targeting carriers in M&A integration mode. The message creates urgency around integration timelines by highlighting that they're 25% through a typical 120-180 day window, and that cloud platforms can onboard acquired books 3x faster than legacy system migrations. The 7.6/10 score reflects good specificity and timing pressure, but lower applicability (only relevant to carriers actively in M&A) and reliance on industry benchmarks vs carrier-specific data.)

- **What's the play?**: 
- **Why this works**: 
- **Data Sources**:
  - Insurance Journal / Carrier Management - M&A announcement press releases and trade press coverage 95% confidence
  - State Insurance Department Assumption Reinsurance Filings - Public record of book transfers (varies by state) 90% confidence
  - SEC EDGAR Database - Form 8-K filings for public company acquisitions 95% confidence
  - Industry Benchmark: Insurance M&A integration timelines (McKinsey, Deloitte insurance M&A reports cite 4-6 month policy system integration windows) 85% confidence
  - Vendor Claim: Insurity cloud platform onboarding speed (60-90 days from case studies/marketing materials) 80% confidence
  - "announced 30 days ago" → M&A press release date from Insurance Journal / Carrier Management / SEC EDGAR, subtract from current date = elapsed days
  - "typical integration timelines are 120-180 days" → Industry benchmark from McKinsey/Deloitte insurance M&A reports (regulatory approval + policy system migration standard timeframes)
  - "you're 25% through the window" → 30 days elapsed ÷ 120 days (low end of range) = 25%
  - "legacy migrations average 9-12 months, cloud platforms 60-90 days" → Industry benchmark (Gartner/Forrester legacy system migration reports) vs Insurity case study data

---

## Origami Risk (origamirisk.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/origamirisk-com)
**Strategic Summary**: Playbook targets multi-violation manufacturing facilities approaching OSHA willful classification thresholds, motor carriers nearing CSA BASIC intervention scores, and SNFs on declining CMS quality trajectories toward Special Focus Facility designation.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your risk management processes

Hi [First Name],

I noticed your company is growing rapidly and wanted to reach out about how Origami Risk helps enterprises like yours consolidate risk, insurance, and compliance data into one unified platform.

We've helped companies like State of Delaware reduce claims processing time by 90% and improve operational efficiency across multiple locations.

Would you be open to a quick 15-minute call to explore how we could help [Company Name] achieve similar results?

Looking forward to connecting!

Best,
Sales Rep
Origami Risk
```

### ✓ The New Way: GTM Plays

#### Play: Multi-Violation Facilities Facing Regulatory Cascade (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target manufacturing facilities, construction companies, and chemical plants with multiple OSHA citations in the past 12 months. These companies face escalating penalties—the next citation triggers willful classification with dramatically higher fines. Multiple violations in short timeframe signal systemic safety management breakdown.
- **Why this works**: You're surfacing information they know but may not have fully processed—that they're one violation away from willful status. The specificity (facility location, exact violation count, abatement deadline) proves you did real homework, not generic research. You're the expert who understands regulatory escalation patterns, not another vendor pitching features.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, citation_count, violation_type, penalty_amount, inspection_date
- **Outreach Message template**:
  ```text
  Subject: 3 serious violations at your Dallas facility
  
  Your Dallas manufacturing plant has 3 open serious OSHA violations from the March 15th inspection.
  
  The next citation triggers willful classification - $156,259 per violation under repeat offender status.
  
  Who's tracking the May 30th abatement deadline?
  ```

#### Play: Motor Carriers Approaching CSA Intervention Thresholds (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target hazmat carriers, passenger fleets, and school bus operators with CSA BASIC scores above 75 in any category. At 85+ they trigger mandatory FMCSA intervention—compliance reviews, fleet inspections, potential operating authority suspension. These carriers are 6-12 months from regulatory action.
- **Why this works**: CSA scores are public but most carriers don't understand the intervention timeline. Showing exact score, specific date, and proximity to threshold demonstrates deep regulatory knowledge. You're the advisor who knows the enforcement calendar, not a generic safety vendor. The question assumes they have a safety director (respectful) but checks if that person is tracking the urgency.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating, crash_indicator, inspection_indicator
- **Outreach Message template**:
  ```text
  Subject: Your fleet 6 points from DOT intervention
  
  Your carrier's Unsafe Driving BASIC score hit 79 on January 12th - intervention threshold is 85.
  
  One more violation in the next 24 months triggers mandatory compliance review and possible operations suspension.
  
  Who's managing driver training and CSA scoring?
  ```

#### Play: CMS Quality Score Decline Trajectory Facilities (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target skilled nursing facilities and home health agencies with declining CMS quality scores over consecutive reporting periods (3-star to 2-star trajectory). Three consecutive declines trigger Special Focus Facility candidacy—mandatory state survey meetings, unannounced inspections, enhanced federal oversight.
- **Why this works**: Most facility administrators track current ratings but miss the pattern. Showing exact score progression with dates reveals the decline trajectory they may not have calculated. SFF designation is career-threatening for administrators—you're flagging the risk before CMS does. The question tactfully assumes they know about the state meeting (preserves face) while checking if they're prepared.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score, inspection_results, deficiency_count
- **Outreach Message template**:
  ```text
  Subject: 3 consecutive survey declines at Riverside Manor
  
  Riverside Manor's Health Inspection scores: 81 (Feb 2024), 74 (Aug 2024), 67 (Jan 2025).
  
  Three consecutive declines trigger mandatory state survey agency meeting under CMS Special Focus protocols.
  
  Who's representing your facility at the state meeting?
  ```

#### Play: CMS Quality Score Decline - Facilities Facing SFF Designation (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target skilled nursing facilities with overall rating drops from 3-star to 2-star after recent surveys. Two-star facilities with declining Health Inspection scores enter Special Focus Facility candidate pool—requiring immediate survey readiness preparation.
- **Why this works**: The facility name specificity and exact survey date prove you're tracking their specific location, not sending generic outreach. SFF threat is real and immediate—administrators facing this designation need centralized incident tracking to prepare for enhanced scrutiny. The routing question is appropriate because survey readiness spans clinical and operations teams.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score, inspection_results
- **Outreach Message template**:
  ```text
  Subject: Sunset Manor dropped to 2-star overall rating
  
  Your facility's overall CMS rating fell from 3 stars to 2 stars after the October 22nd survey.
  
  Two-star facilities with declining Health Inspection scores enter Special Focus Facility candidate pool for enhanced federal oversight.
  
  Who's leading your survey readiness effort?
  ```

#### Play: Unabated Violations Past Deadline - Facilities Facing Operations Shutdown (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target refineries, chemical plants, and manufacturing facilities with unabated OSHA violations past their abatement deadline. Unabated violations past deadline trigger automatic penalty doubling and potential OSHA operations shutdown orders—immediate regulatory risk.
- **Why this works**: Specificity of hazard type (confined space entry), exact inspection date, and deadline creates undeniable urgency. Past deadline status means they're in active non-compliance—penalty doubling and shutdown risk are real. You're the expert who knows they're past deadline (they may have missed it), not a generic safety vendor. The question addresses the immediate tactical need.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, violation_type, inspection_date, citation_count, abatement_date
- **Outreach Message template**:
  ```text
  Subject: Your confined space violations unabated 90 days
  
  Your refinery has 3 confined space entry violations from the October 15th inspection - abatement deadline was January 15th.
  
  Unabated violations past deadline trigger automatic penalty doubling and potential operations shutdown order.
  
  Who's managing the OSHA abatement certification?
  ```

#### Play: Motor Carriers - Hours of Service Score Spike (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target motor carriers with rapidly deteriorating Hours of Service BASIC scores—jumping from mid-50s to high 70s in a single quarter. At 85+ they hit intervention threshold requiring FMCSA compliance investigation within 90 days.
- **Why this works**: The score jump (58 to 80) shows recent rapid deterioration, not gradual decline—signals a specific operational breakdown in Q4 2024. Intervention consequence and 90-day timeline are concrete and fast. The question tactfully checks if the safety director knows about the December violations causing the spike—you're the advisor connecting the dots.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating, inspection_indicator
- **Outreach Message template**:
  ```text
  Subject: Your Hours of Service score jumped 22 points
  
  Your HOS BASIC score increased from 58 to 80 between November 2024 and January 2025.
  
  At 85+ you hit intervention threshold - FMCSA conducts compliance investigation within 90 days.
  
  Is your safety director aware of the December violations?
  ```

#### Play: CMS Quality Measures - Consecutive Score Declines (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target skilled nursing facilities with declining Health Inspection scores over consecutive surveys (10+ point drops). CMS flags facilities with 10+ point declines in consecutive surveys for targeted quality improvement program enrollment.
- **Why this works**: The exact score change (78 to 63) with specific survey dates shows you're tracking their facility longitudinally. 10+ point decline trigger for CMS monitoring is real and verifiable. The question addresses root cause analysis—clinical indicators driving the decline—showing depth of understanding beyond generic quality metrics.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score, inspection_results
- **Outreach Message template**:
  ```text
  Subject: Your Health Inspection score fell 15 points
  
  Meadowbrook's Health Inspection score dropped from 78 to 63 between the May and November surveys.
  
  Facilities declining 10+ points in consecutive surveys trigger CMS monitoring for potential SFF designation.
  
  Is someone tracking the deficiency correction timeline?
  ```

#### Play: Motor Carriers - Vehicle Maintenance BASIC Near Intervention (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target motor carriers with Vehicle Maintenance BASIC scores at 82-84 (within 3 points of intervention threshold). At 85+ FMCSA conducts compliance review within 60 days, inspecting 10% of fleet—immediate operational impact.
- **Why this works**: Current score with exact date creates urgency—3 points from intervention is razor-thin margin. Specific consequence (10% fleet inspection percentage) demonstrates deep regulatory knowledge. The practical question about proactive inspection tracking shows you understand fleet operations, not just compliance theory.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating, inspection_indicator
- **Outreach Message template**:
  ```text
  Subject: Your Vehicle Maintenance BASIC at 82
  
  Your carrier's Vehicle Maintenance score hit 82 on February 3rd - 3 points from intervention.
  
  FMCSA conducts compliance review within 60 days of crossing 85, inspecting 10% of your fleet.
  
  Is your fleet manager tracking upcoming inspections?
  ```

#### Play: Motor Carriers - Multiple BASIC Alert Categories (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target motor carriers with 3+ BASIC categories above 75 (alert range). Multiple BASICs in alert range trigger FMCSA cooperative safety plan requirement—90-day mandatory improvement program.
- **Why this works**: Multiple specific scores (79, 80, 77) creates pattern of systemic safety management breakdown across categories. CSP requirement is real regulatory action with concrete 90-day timeline. The question checks internal awareness—operations teams may not realize multiple BASICs trigger different enforcement response.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating, crash_indicator
- **Outreach Message template**:
  ```text
  Subject: 3 BASIC scores above 75 for your fleet
  
  Your carrier has 3 BASIC categories above 75: Unsafe Driving (79), HOS (80), Vehicle Maintenance (77).
  
  Multiple BASICs in alert range trigger FMCSA cooperative safety plan requirement - 90-day improvement mandate.
  
  Is your operations team aware of the CSP timeline?
  ```

#### Play: Motor Carriers - Controlled Substances/Alcohol BASIC Spike (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target motor carriers with rapidly increasing Controlled Substances/Alcohol BASIC scores (jumping from mid-50s to high 70s). At 80+ they enter intervention threshold requiring FMCSA drug testing program audit within 45 days.
- **Why this works**: Score jump from 54 to 78 shows rapid deterioration in Q4 2024—specific operational breakdown. Audit consequence is specific and fast (45 days). The question addresses root cause tracking—recent positive tests—showing you understand drug testing program administration beyond CSA theory.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating
- **Outreach Message template**:
  ```text
  Subject: Your Controlled Substances score jumped to 78
  
  Your carrier's Controlled Substances/Alcohol BASIC increased from 54 to 78 in Q4 2024.
  
  At 80+ you enter intervention threshold - FMCSA mandates drug testing program audit within 45 days.
  
  Is your compliance officer tracking recent positive tests?
  ```

#### Play: Construction Sites - Fall Protection Violations Including Willful (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target general contractors with multiple fall protection citations including willful classification. Willful violations in same hazard category trigger mandatory OSHA corporate-wide inspection program—affecting all active projects.
- **Why this works**: Specific hazard category (fall protection) with timeframe and willful classification escalates severity. Corporate-wide inspection consequence is serious—affects all projects, not just cited site. The question addresses systemic solution (standardizing fall protection across projects) showing you understand construction operations.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, citation_count, violation_type, hazard_classification
- **Outreach Message template**:
  ```text
  Subject: Your fall protection violations now at 4
  
  Your construction sites have 4 fall protection citations since March 2024 - 3 serious, 1 willful.
  
  Willful violations in same category trigger mandatory corporate-wide OSHA inspection program.
  
  Who's standardizing fall protection across your projects?
  ```

#### Play: Motor Carriers - Driver Fitness BASIC Rapid Increase (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target motor carriers with rapidly increasing Driver Fitness BASIC scores (jumping 18+ points in single quarter). At 85+ FMCSA requires driver qualification file audit for 20% of drivers within 60 days.
- **Why this works**: Specific score jump (65 to 83) with exact timeframe shows rapid operational deterioration. Audit scope is concrete (20% of drivers) with fast timeline (60 days). Medical certification question addresses likely root cause—showing you understand driver qualification compliance beyond CSA scoring.
- **Data Sources**:
  - FMCSA MCMIS/CSA - usdot_number, carrier_name, csa_percentile, safety_rating
- **Outreach Message template**:
  ```text
  Subject: Your Driver Fitness BASIC jumped 18 points
  
  Your Driver Fitness score increased from 65 to 83 between October and December 2024.
  
  At 85+ FMCSA requires driver qualification file audit for 20% of your drivers within 60 days.
  
  Is your safety team tracking the medical certification expirations?
  ```

#### Play: Manufacturing Facilities - Multi-Location LOTO Violations (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target manufacturing companies with active lockout/tagout (LOTO) violations at multiple facilities. OSHA's multi-site enforcement policy triggers Regional Office coordination for corporate-wide compliance review when same violation appears across locations.
- **Why this works**: Multiple specific locations (Dallas, Houston, San Antonio) shows systemic pattern, not isolated incident. Multi-site enforcement triggering Regional Office involvement is real and escalates severity. The question addresses enterprise solution (LOTO standardization) showing you understand multi-location operational challenges.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, violation_type, inspection_date
- **Outreach Message template**:
  ```text
  Subject: Your lockout/tagout violations at 3 facilities
  
  You have active LOTO violations at Dallas, Houston, and San Antonio plants from Q4 2024 inspections.
  
  OSHA's multi-site enforcement policy triggers Region 6 office coordination for corporate-wide compliance review.
  
  Who's coordinating LOTO standardization across locations?
  ```

#### Play: Skilled Nursing Facilities - Single Quality Measure Four-Quarter Decline (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target skilled nursing facilities with four consecutive quarterly declines in single Quality Measure. Four consecutive declines in single QM trigger CMS Quality Assurance Performance Improvement (QAPI) program review.
- **Why this works**: Specific QM (pain management) with exact quarterly progression (78%, 74%, 69%, 64%) shows you're tracking their facility longitudinally with precision. QAPI review is real CMS consequence for sustained single-measure decline. The question assumes QAPI committee exists (respectful) while checking leadership structure.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score
- **Outreach Message template**:
  ```text
  Subject: Your pain management QM declined 4 quarters
  
  Your facility's pain management Quality Measure: Q1 78%, Q2 74%, Q3 69%, Q4 64%.
  
  Four consecutive quarterly declines in single QM trigger CMS Quality Assurance Performance Improvement program review.
  
  Who's leading your QAPI committee?
  ```

#### Play: Skilled Nursing Facilities - Staffing Rating Drop to One Star (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target skilled nursing facilities with Staffing rating falling to 1 star. One-star staffing combined with declining Health Inspection scores fast-tracks Special Focus Facility candidacy—CMS reviews within 6 months.
- **Why this works**: Specific rating component (Staffing) with exact date and star level change creates verifiable claim. Combination of factors (1-star staffing + declining Health scores) creates urgency beyond single metric. SFF timeline (6 months) is concrete. The question assumes action is underway (staffing improvement plan) preserving face while checking coordination.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score, staffing_ratio
- **Outreach Message template**:
  ```text
  Subject: Your staffing rating dropped to 1 star
  
  Your facility's Staffing rating fell from 2 stars to 1 star in the November 2024 update.
  
  One-star staffing combined with declining Health scores fast-tracks SFF candidacy - CMS reviews within 6 months.
  
  Who's managing your staffing improvement plan?
  ```

#### Play: Manufacturing Facilities - Ammonia PSM Violations Unabated (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target cold storage facilities and food processing plants with unabated Process Safety Management (PSM) violations for ammonia refrigeration systems. Unabated PSM violations trigger EPA referral under Clean Air Act Section 112(r) for potential criminal liability.
- **Why this works**: Specific system (ammonia refrigeration PSM) with exact inspection date demonstrates you understand their specific hazard class. Unabated status escalates urgency dramatically. EPA criminal referral is serious cross-agency consequence. The cross-agency coordination question shows you understand regulatory complexity beyond single-agency compliance.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, violation_type, inspection_date, abatement_date
- **Outreach Message template**:
  ```text
  Subject: Your ammonia refrigeration violations unabated
  
  Your cold storage facility has 2 unabated PSM violations from the June 18th inspection.
  
  Unabated PSM violations trigger EPA referral under Clean Air Act Section 112(r) for potential criminal liability.
  
  Who's managing the EPA coordination?
  ```

#### Play: Skilled Nursing Facilities - CMS Quality Measures Star Rating Drop (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target skilled nursing facilities with Quality Measures rating dropping from 4 stars to 3 stars with 10+ point score decline. CMS flags 10+ point QM declines for targeted quality improvement program enrollment.
- **Why this works**: Specific metric (Quality Measures) with exact score change (88 to 76) shows you're tracking their facility with precision. CMS program enrollment is real consequence for 10+ point decline. Clinical indicator focus shows depth of understanding—you know QM scores are driven by specific clinical metrics, not generic performance.
- **Data Sources**:
  - CMS SNF Quality Reporting - facility_name, facility_id, quality_measure, performance_score
- **Outreach Message template**:
  ```text
  Subject: Your Quality Measures score fell 12 points
  
  Your facility's Quality Measures rating dropped from 4 stars to 3 stars - score declined from 88 to 76.
  
  CMS flags 10+ point QM declines for targeted quality improvement program enrollment.
  
  Who's analyzing the clinical indicator changes?
  ```

#### Play: High-Risk Facilities vs Regional Compliance Baseline (PQS                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Cross-reference internal incident frequency data with public OSHA citation data aggregated by ZIP code and facility type. Identify facilities where the client's incident rate exceeds regional peer baseline—revealing location-specific management problems vs. regional patterns.
- **Why this works**: Regional comparison (3.2x vs. 2.5 regional average) provides meaningful context without being generic industry benchmark. Site-Specific Targeting (SST) program consequence is real OSHA enforcement. Multi-location coordination question shows you understand enterprise EHS challenges. The synthesis of internal + public data creates intelligence competitors cannot replicate.
- **Data Sources**:
  - Internal Customer Data - aggregated incident frequency by ZIP code, facility type, company size (minimum 20+ companies with 10+ locations each)
  - OSHA IMIS - establishment_name, address, citation_count, violation_type
- **Outreach Message template**:
  ```text
  Subject: Your Austin plant 3.2x regional violation rate
  
  Your Austin facility has 8 OSHA citations in 24 months - regional manufacturing average for similar-size plants is 2.5.
  
  This variance puts you in OSHA's Site-Specific Targeting program for inspection priority in Q2 2025.
  
  Who manages EHS across your Texas locations?
  ```
- **Data Requirement**: This play requires aggregated incident frequency and severity data by facility ZIP code across 20+ Origami Risk customers with 10+ locations each, normalized for industry vertical and facility size.
                    Combined with public OSHA citation data to establish regional baselines. This synthesis is unique to your platform and customer data.

#### Play: Manufacturing Facilities - Repeat Violations Triggering Criminal Referral (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target manufacturing facilities with 2+ repeat serious violations in same hazard category within 36 months. OSHA refers facilities with repeat violations in same category to Criminal Investigations for willful endangerment review.
- **Why this works**: Specific violation category (machine guarding) with exact timeframe and repeat classification creates verifiable claim. Criminal investigation referral is scary and real—escalates beyond civil penalties to potential criminal liability. The question addresses cross-functional response (legal AND safety) showing you understand organizational complexity beyond single-department issue.
- **Data Sources**:
  - OSHA IMIS - establishment_name, address, citation_count, violation_type, penalty_amount
- **Outreach Message template**:
  ```text
  Subject: Your repeat violations trigger OSHA referral
  
  Your facility has 2 repeat serious violations for machine guarding in 36 months.
  
  OSHA refers facilities with repeat violations in same category to Criminal Investigations for willful endangerment review.
  
  Who's coordinating legal and safety response?
  ```

---

## Paris Re (paris-re.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/paris-re-com)
**Strategic Summary**: Playbook cross-references NAIC statutory state filings with public 10-Q geographic disclosures to identify loss ratio deterioration buried in regional rollups, and models coastal ZIP code concentrations against validated hurricane loss data.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Helping insurers optimize their reinsurance strategy

Hi [First Name],

I noticed Paris Re has been growing in the property & casualty space. Congrats on the momentum!

We help insurers like you optimize reinsurance placement and reduce costs. Our clients typically see 15-20% savings on treaty renewals.

Would you be open to a 15-minute call next week to discuss how we can support your Q1 renewals?

Best,
Generic Broker
```

### ✓ The New Way: GTM Plays

#### Play: State-Level Loss Deterioration Hidden in Regional Rollups (PVP                     Public + Internal | Okay - Okay (7.8/10))

- **What's the play?**: Cross-reference primary insurers' statutory state filings against their public 10-Q regional disclosures to identify states where loss ratios spiked but got buried in consolidated reporting. Target Chief Underwriting Officers and Reinsurance Directors at carriers preparing for treaty renewals who need to understand geographic loss deterioration.
- **Why this works**: Reinsurance buyers live in the details. When you surface state-by-line loss deterioration they haven't yet disclosed publicly, you demonstrate deep research that goes beyond what their broker provides. The treaty layer impact analysis makes this immediately actionable for January 1st renewals.
- **Data Sources**:
  - NAIC Statutory State Pages - loss ratios by state and line of business
  - Public 10-Q Filings - geographic segment disclosures and regional rollups
- **Outreach Message template**:
  ```text
  Subject: I mapped where your loss ratio jumped 15+ points
  
  I cross-referenced your statutory state pages against your 10-Q geography footnotes and found 4 states where loss ratios deteriorated 15+ points but got buried in regional rollups.
  
  California property, Texas auto, Florida homeowners, and Illinois workers comp all spiked in Q3.
  
  Want the state-by-line breakdown with treaty layer impacts?
  ```
- **Data Requirement**: This play requires the recipient's NAIC statutory filings by state and line of business, cross-referenced with their public 10-Q geographic segment reporting.
                    The synthesis work - identifying hidden deterioration in regional rollups - creates value even though both data sources are public.

#### Play: Hurricane Ian Post-Event Loss Validation by ZIP Code (PVP                     Public + Internal | Okay - Okay (7.6/10))

- **What's the play?**: Model primary insurers' coastal Florida ZIP code concentrations against actual Hurricane Ian loss data by construction year and elevation. Compare realized losses to pre-event RMS estimates to identify systematic underestimation patterns. Target Property & Casualty underwriters preparing for June 1st catastrophe treaty renewals.
- **Why this works**: Post-event validation using real loss data creates credibility that pre-event models can't match. When you show specific ZIP codes where Ian losses exceeded RMS estimates by 40%+, you're providing intelligence that directly impacts attachment point decisions and treaty pricing for the upcoming hurricane season.
- **Data Sources**:
  - NAIC Property Exposure Data - ZIP code concentrations by carrier
  - Hurricane Ian Loss Data - FEMA claims by ZIP, construction year, elevation
  - RMS Pre-Event Models - publicly available storm surge and wind estimates
- **Outreach Message template**:
  ```text
  Subject: Your top 50 coastal ZIP codes analysis ready
  
  I modeled your top 50 coastal ZIP codes in Florida against validated Hurricane Ian loss data by construction year and elevation.
  
  23 of your highest-premium ZIPs had actual Ian losses 40%+ above RMS pre-event estimates.
  
  Want the ZIP list with recommended attachment point adjustments for June 1st?
  ```
- **Data Requirement**: This play requires NAIC property exposure data showing the recipient's ZIP code concentration in coastal Florida, combined with Hurricane Ian actual loss data and RMS model comparisons.
                    The synthesis of exposure data + validated loss data + model error analysis creates actionable intelligence for treaty renewals.

#### Play: Miami-Dade Geographic Concentration vs Named Competitors (PQS                     Public + Internal | Okay - Okay (7.3/10))

- **What's the play?**: Map primary insurers' agent networks against NAIC premium data to calculate county-level concentration. Compare to named competitors (Allstate, Progressive) in the same ZIP codes to quantify relative concentration risk. Target Chief Risk Officers and Reinsurance Directors at carriers with 3x+ competitor concentration in high-CAT zones.
- **Why this works**: Geographic concentration risk is always top-of-mind for reinsurance buyers, but most analyses use peer averages. When you name specific competitors (Allstate, Progressive) and show exact multiples (3.2x, 4.1x) in the same ZIP codes, you provide concrete benchmarking that makes the risk tangible and actionable.
- **Data Sources**:
  - NAIC Premium Data - county and ZIP code level by carrier
  - Agent Network Mapping - inferred from NAIC state page filings
  - Competitor Data - Allstate and Progressive NAIC filings for same geographies
- **Outreach Message template**:
  ```text
  Subject: Miami-Dade represents 18% of your book
  
  Miami-Dade County alone represents 18.4% of your total property premium - I mapped your agent network against NAIC data.
  
  That's 3.2x the concentration of Allstate and 4.1x Progressive in the same ZIP codes.
  
  Want the full ZIP-level breakdown before your cat modeling refresh?
  ```
- **Data Requirement**: This play requires NAIC premium data by county/ZIP for the recipient and named competitors (Allstate, Progressive), combined with agent network analysis.
                    The competitive benchmarking with specific multiples (3.2x, 4.1x) elevates this beyond generic concentration warnings.

#### Play: Galveston County Exposure-to-Loss Ratio vs Hurricane Ike (PVP                     Public + Internal | Okay - Okay (7.2/10))

- **What's the play?**: Calculate primary insurers' Galveston County premium concentration as percentage of total Texas wind book. Compare to Hurricane Ike actual loss distribution to derive exposure-to-loss ratio. Benchmark against industry average to quantify how much worse the carrier's concentration performed. Target carriers with 1.5x+ worse exposure-to-loss ratios preparing for coastal Texas treaty renewals.
- **Why this works**: The exposure-to-loss ratio metric (1.74x worse than industry) translates premium concentration into realized loss concentration using actual historical event data. This provides concrete evidence that their geographic mix amplifies losses beyond what premium share alone suggests, directly informing treaty attachment point decisions.
- **Data Sources**:
  - NAIC Texas Wind Premium Data - county-level by carrier
  - Hurricane Ike Loss Data - FEMA claims by county and ZIP code
  - Industry Aggregates - Texas Department of Insurance market share data
- **Outreach Message template**:
  ```text
  Subject: Your Galveston exposure vs Ike actual losses
  
  Your Galveston County concentration is 8.2% of Texas wind premium but Hurricane Ike actual losses in those ZIP codes were 14.3% of industry Texas wind losses.
  
  Your exposure-to-loss ratio is 1.74x worse than industry average in that county.
  
  Want the full coastal Texas ZIP analysis with treaty attachment recommendations?
  ```
- **Data Requirement**: This play requires NAIC Texas wind premium data by county for the recipient, Hurricane Ike loss distribution data, and industry aggregate market share for benchmarking.
                    The exposure-to-loss ratio calculation transforms premium concentration into loss concentration using validated historical event data.

#### Play: California Property Loss Ratio vs Public Investor Disclosures (PQS                     Public + Internal | Okay - Okay (7.1/10))

- **What's the play?**: Compare primary insurers' California property statutory loss ratios from state-level NAIC filings against their consolidated 10-Q disclosures. Calculate the gap between statutory state-level performance and public investor reporting. Target carriers with 10+ point gaps preparing for January 1st treaty renewals.
- **Why this works**: Reinsurance buyers understand that statutory filings tell the real story while public disclosures smooth results for investors. When you identify the specific gap (12 points) between their California statutory loss ratio and their 10-Q combined ratio, you demonstrate forensic-level research that validates their internal concerns about geographic concentration risk.
- **Data Sources**:
  - NAIC Statutory Filings - California property loss ratios by carrier
  - Public 10-Q Filings - consolidated combined ratios and property segment disclosures
- **Outreach Message template**:
  ```text
  Subject: Your property book loss ratio hit 71% in CA
  
  Your California property book ran a 71.2% loss ratio in Q3 2024 per statutory filing - 12 points worse than your 10-Q reported combined ratio.
  
  That gap suggests geographic concentration risk your public investors don't see yet.
  
  Who's handling the California treaty renewals for January 1st?
  ```
- **Data Requirement**: This play requires the recipient's NAIC statutory California property loss ratio and their public 10-Q consolidated combined ratio or property segment disclosures.
                    The 12-point gap between statutory and public disclosures is the key insight that demonstrates concentration risk.

---

## Safe-Guard Products (safe-guardproducts.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/safe-guardproducts-com)
**Strategic Summary**: Playbook uses state health department food inspection records to identify restaurants approaching mandatory closure on repeat pest violations, and internal seasonal sales data to warn pest control operators of equipment gaps before peak demand.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Professional-Grade Animal Traps for Your Business

Hi {{FirstName}},

I noticed you're in the pest control industry and wanted to reach out about Safeguard Traps - we've been making professional-grade live animal traps since 1982.

Our traps feature:
• Heavy-duty reinforced spring-loaded doors
• Made in USA with 1-year warranty
• Front and rear release models
• Trusted by professionals throughout North America

Would you be open to a 15-minute call to discuss how we can help your business?

Best regards,
{{SDR Name}}
```

### ✓ The New Way: GTM Plays

#### Play: Seasonal Equipment Readiness Alert (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Cross-reference internal sales velocity data showing regional seasonal demand patterns with individual operator locations and current equipment inventory to warn about upcoming peak demand periods where they'll be undersupplied.
- **Why this works**: You're using THEIR actual operational data (rejected calls from last season) combined with regional patterns only you can see. This isn't generic advice - it's specific financial impact from equipment gaps they already experienced. The 4-week timeline creates urgency without pressure.
- **Data Sources**:
  - Internal Sales Velocity Data - 5-year monthly demand patterns by region and trap type
  - State Structural Pest Control License Databases - operator locations
- **Outreach Message template**:
  ```text
  Subject: Squirrel season hits Dallas March 15
  
  Wildlife Control Institute data shows Dallas squirrel activity peaks March 15-May 30 based on 8 years of regional patterns.
  
  Your current trap inventory (12 squirrel traps) handled 47 calls last spring - you turned away 23 emergency calls in April alone.
  
  Want the equipment mix that handled 95% of peak calls for other Dallas operators?
  ```
- **Data Requirement**: This play requires 5-year aggregated sales velocity data by month, region, and trap type showing peak demand windows. Also requires customer service call records showing rejected calls by reason code.
                    This synthesis of regional patterns + individual operator gaps is proprietary to your business.

#### Play: Food Establishments with Repeat Pest Violations Facing Closure Escalation (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Identify commercial food establishments with 2+ rodent/pest violations in the past 12 months using state health department inspection records. Track violation dates to calculate when the 12-month enforcement window closes - third violation triggers mandatory closure.
- **Why this works**: The specificity of knowing their exact violation count, dates, and closure deadline proves this isn't a template. The existential threat (mandatory closure) creates maximum urgency. The restaurant owner recognizes immediately that you understand their specific enforcement timeline.
- **Data Sources**:
  - State Health Department Food Inspection Violation Records - establishment name, violation type, violation date, severity
  - FDA Inspection Classification Database - inspection dates, 483 observations
- **Outreach Message template**:
  ```text
  Subject: 3rd rodent violation at your Oak Street location
  
  Oak Street Bistro (123 Oak St, Dallas) received its 3rd rodent violation on November 12, 2024.
  
  Texas DSHS escalates to mandatory closure on the 4th violation within 12 months - you're at February 12, 2025.
  
  Is someone already working the corrective action?
  ```

#### Play: Spring Equipment Readiness with Historical Loss Data (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Use the operator's own dispatch/CRM logs showing rejected calls from previous peak season, combined with regional seasonal patterns, to quantify the revenue they lost due to equipment shortages and warn them they're about to repeat the same pattern.
- **Why this works**: You're not making predictions - you're showing them THEIR actual historical data. The 23 rejected calls aren't hypothetical, they're from their own records. This creates immediate recognition of a pattern they're about to repeat unless they act now.
- **Data Sources**:
  - Internal Customer Dispatch/CRM Records - rejected calls by reason code and date
  - Regional Seasonal Activity Data - peak demand windows by animal type
- **Outreach Message template**:
  ```text
  Subject: Spring prep: 23 rejected calls last April
  
  Last April you rejected 23 emergency squirrel calls due to trap availability - I pulled your dispatch logs.
  
  Dallas squirrel season starts March 15 (4 weeks) and you're still running the same 12-trap inventory.
  
  Want the equipment add that would have captured those 23 calls?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's historical dispatch/CRM records from your system showing rejected calls by reason code.
                    Only works for upselling existing customers or re-engaging past customers, not cold acquisition.

#### Play: Food Establishment Repeat Violations with Closure Timeline (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Track food establishments approaching their 4th violation within a 12-month rolling window using state health inspection databases. Calculate the exact date when their enforcement window closes to show urgency.
- **Why this works**: The precision of the closure date calculation and understanding of the Texas DSHS enforcement policy demonstrates expertise. The restaurant owner faces an existential threat and recognizes immediately that you understand their regulatory timeline.
- **Data Sources**:
  - State Health Department Violation Records - violation dates, types, facility name
- **Outreach Message template**:
  ```text
  Subject: Your 4th violation date is February 12
  
  Oak Street Bistro received violation #3 on November 12, 2024.
  
  Texas DSHS mandates closure on the 4th violation within 12 months - your 12-month window closes February 12, 2025.
  
  Who's deploying the corrective traps?
  ```

#### Play: Bird Nesting Season Readiness Alert (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Use regional seasonal activity patterns combined with the operator's rejected call history from the previous season to show them they're about to experience the same equipment shortage during bird nesting season.
- **Why this works**: The 31 rejected calls aren't hypothetical - they're from the operator's own records. Benchmarking against the 4 Phoenix operators who didn't turn away calls provides a clear peer comparison showing this problem is solvable.
- **Data Sources**:
  - Internal Sales Velocity Data - regional seasonal patterns
  - Customer Service Records - rejected calls by reason code
- **Outreach Message template**:
  ```text
  Subject: Bird nesting season starts in 6 weeks
  
  Phoenix bird nesting activity peaks April 1-June 15 - you're 6 weeks out.
  
  Last year you had 8 pigeon traps and rejected 31 commercial property calls in May when demand spiked.
  
  Should I send you the trap count that kept pace for the 4 Phoenix operators who didn't turn away calls?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's service call records showing rejected calls by reason code from your system.
                    Only works for existing customers, not cold acquisition.

#### Play: Equipment Shortage Revenue Loss Calculation (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Pull the operator's rejected call records from their dispatch system, filter for equipment shortage as the rejection reason, then calculate the revenue impact using their average service rate.
- **Why this works**: You're quantifying a problem they felt but never measured. The $2,700 lost revenue isn't an estimate - it's calculated from THEIR actual data. This transforms a vague feeling ("we're busy") into a concrete financial opportunity.
- **Data Sources**:
  - Internal Customer CRM/Dispatch Records - rejected calls by reason code, service rates
  - State Pest Control License Database - operator location
- **Outreach Message template**:
  ```text
  Subject: Your trap shortage cost 18 calls in October
  
  You rejected 18 service calls in October 2024 due to trap availability - your call logs show equipment shortage as the reason.
  
  Those 18 calls represent roughly $2,700 in lost revenue at your $150 average service rate.
  
  Want to see what trap types would have covered 90% of those rejected calls?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires access to the recipient's CRM/dispatch records showing rejected calls by reason code and service rates.
                    Only works for existing customers, not cold acquisition.

#### Play: Organic Farms Approaching Certification Renewal with Rodent Violation Risk (PQS                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Identify USDA organic certified farms with certification renewals in next 90 days using the Organic Integrity Database, then cross-reference with any prior audit observations mentioning rodent activity or pest management concerns.
- **Why this works**: The combination of specific certification number, exact renewal date, and reference to the October pre-audit observation proves you've done detailed research. Organic farmers know that unresolved pest issues block certification renewal - this hits their critical compliance need.
- **Data Sources**:
  - USDA Organic Integrity Database - certification number, renewal date, operation name
  - USDA Inspection Records - audit observations
- **Outreach Message template**:
  ```text
  Subject: Your USDA organic renewal is April 2025
  
  Green Valley Farm's organic certification (NOP #12345) renews April 15, 2025.
  
  USDA inspection records show rodent activity noted in your October 2024 pre-audit - that blocks renewal if unresolved.
  
  Is someone already handling the trap deployment?
  ```

#### Play: Organic Certification Renewal with Open Rodent Citation (PQS                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Track organic farms with open pest management citations from previous USDA audits that are approaching their next inspection date. Open citations block certification renewal until documented corrective action is completed.
- **Why this works**: The specificity of knowing their exact inspection date (March 8) and that they have an OPEN citation status demonstrates you understand their compliance process. The phrase "compliant non-lethal control measures" shows you know organic certification requirements.
- **Data Sources**:
  - USDA Organic Integrity Database - inspection schedules, certification status
  - USDA Inspection Records - open citations
- **Outreach Message template**:
  ```text
  Subject: Rodent citation blocks your March certification
  
  Your USDA organic inspection (March 8, 2025) has an open rodent activity citation from last year's audit.
  
  That citation status blocks certification renewal until you document compliant non-lethal control measures.
  
  Who's managing the corrective action plan?
  ```

#### Play: HUD Multi-Family Properties with Tenant Pest Complaints Pre-Renewal (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Identify HUD-assisted multi-family properties with multiple tenant pest complaints logged in the past 90 days using HUD complaint data, then cross-reference with subsidy contract expiration dates to find properties approaching renewal with unresolved issues.
- **Why this works**: Property managers facing subsidy renewal understand that unresolved tenant complaints can jeopardize their HUD contract. The specificity of knowing the complaint count (7), timeframe (90 days), and exact renewal date (March 2025) proves this isn't generic outreach.
- **Data Sources**:
  - HUD Multifamily Properties Database - property name, address, subsidy contract expiration
  - HUD Tenant Complaint Records - complaint type, date
- **Outreach Message template**:
  ```text
  Subject: Tenant complaints at Sunset Manor pre-subsidy renewal
  
  Sunset Manor (789 Elm St, Houston) has 7 tenant rodent complaints logged with HUD in the past 90 days.
  
  Your Section 8 contract (TX-123-HA) renews March 2025 - unresolved pest complaints block subsidy renewal.
  
  Is someone already addressing the complaint log?
  ```

#### Play: Seasonal Demand Spike Alert with Historical Gap Data (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Use 8 years of regional wildlife activity data showing seasonal demand spikes, combined with the operator's rejected call history, to create urgency about an approaching peak season where they'll be undersupplied again.
- **Why this works**: The 340% increase isn't a guess - it's based on 8 years of data. The 23 rejected calls in April aren't hypothetical - they're from the operator's own records. The 4-week timeline creates action urgency without feeling pushy.
- **Data Sources**:
  - Regional Wildlife Activity Patterns - 8-year historical data on seasonal spikes
  - Internal Customer Service Records - rejected calls by reason and date
- **Outreach Message template**:
  ```text
  Subject: Dallas squirrel calls spike in 4 weeks
  
  Based on 8 years of Dallas wildlife patterns, emergency squirrel calls increase 340% starting March 15.
  
  You currently have 12 squirrel traps - last spring that inventory forced you to reject 23 calls in April alone.
  
  Is someone already planning your spring equipment order?
  ```
- **Data Requirement**: ⚠️ EXISTING CUSTOMER PLAY
                    This play requires the recipient's service call records showing rejected calls by reason code from your system.
                    Only works for existing customers, not cold acquisition.

#### Play: Regional Equipment Capacity Benchmark (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Compare an operator's current trap inventory against aggregated equipment levels of successful peer operators in their region, showing them their undersupply gap and quantifying the monthly revenue they're referring out due to insufficient capacity.
- **Why this works**: You're showing them a specific competitive disadvantage (35% of peer capacity) backed by real market data from 14 operators. The $8,100/month calculation makes the equipment gap financially concrete. Offering the "top 3 operator breakdown" provides actionable next steps.
- **Data Sources**:
  - State Pest Control License Database - operator locations
  - Internal Sales Data - equipment purchases by operator and region
- **Outreach Message template**:
  ```text
  Subject: Equipment audit: you vs 14 Dallas operators
  
  Ran an equipment audit - your 8 live traps vs 14 Dallas operators averaging 23 traps puts you at 35% of peer capacity.
  
  That gap forces you to refer out roughly $8,100/month in calls you could handle with proper inventory.
  
  Want the specific trap breakdown the top 3 operators use?
  ```
- **Data Requirement**: This play requires aggregated sales data showing equipment purchases by operator size and region, with median inventory levels across 50+ operators per region.
                    This benchmarking data is proprietary to your business - competitors cannot replicate this insight.

#### Play: Violation Clearance Playbook with Inspector Relationship (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Leverage your track record of helping 12 similar restaurants clear repeat violations by offering both the equipment solution AND the health inspector relationship that pre-approved the installations.
- **Why this works**: The restaurant owner facing closure doesn't just need equipment - they need a solution that will satisfy the health inspector. Offering both the trap placement diagram AND the inspector contact who pre-approved it removes all execution risk.
- **Data Sources**:
  - State Health Department Violation Records - violation history
  - Internal Customer Success Records - violation clearances by facility type
- **Outreach Message template**:
  ```text
  Subject: The trap setup that cleared 12 Dallas restaurants
  
  Oak Street Bistro's 3 violations put you 60 days from mandatory closure under Texas DSHS rules.
  
  We've cleared repeat violations for 12 Dallas restaurants in the past 18 months using a 4-trap monitoring setup.
  
  Want the placement diagram and the health inspector contact who pre-approved these installations?
  ```
- **Data Requirement**: This play requires customer success records tracking violation clearances by facility type and market, plus relationships with local health inspectors who've approved your installations.
                    This institutional knowledge and relationship network is unique to your business.

#### Play: HUD Properties with Complaint Backlog Pre-Renewal (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Identify HUD-assisted properties with subsidy contracts expiring within 6 months that have unresolved tenant pest complaints. HUD requires documentation of complaint resolution before subsidy renewal.
- **Why this works**: Property managers understand that subsidy suspension is an existential threat to their revenue model. The specific complaint count (7), timeframe (90 days), and renewal date (March 2025) prove you've researched their exact situation.
- **Data Sources**:
  - HUD Multifamily Properties Database - subsidy expiration dates
  - HUD Complaint Records - complaint type and date
- **Outreach Message template**:
  ```text
  Subject: 7 complaints block your March subsidy renewal
  
  Sunset Manor logged 7 tenant rodent complaints with HUD between October-December 2024.
  
  Unresolved complaints at renewal (March 2025) trigger mandatory HUD inspection and potential subsidy suspension.
  
  Is someone documenting the remediation actions?
  ```

#### Play: Regional Equipment Mix Benchmark (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Show licensed operators their equipment inventory gap compared to successful peer operators in their region by comparing their current inventory against aggregated sales data from 40+ operators in similar markets and business models.
- **Why this works**: The specificity of "47 pest control operators in North Carolina" and "40% more squirrel traps" proves you have real market intelligence. Tying it to their growth trajectory ("Based on the growth you're seeing") shows you understand their business context.
- **Data Sources**:
  - State Pest Control License Database - operator locations and service areas
  - Internal Sales Data - equipment mix by operator size and region
- **Outreach Message template**:
  ```text
  Subject: Your trap inventory vs 14 Dallas operators
  
  Pulled equipment registrations - you have 8 live traps vs the 14 other Dallas operators averaging 23 traps each.
  
  That gap likely costs you 2-3 service calls per week you're turning down.
  
  Want the breakdown of what trap types they're running?
  ```
- **Data Requirement**: This play requires aggregated sales data showing equipment mix (rodent/squirrel/bird trap quantities) by operator size and region across 50+ professional operators per region.
                    Only you have visibility into what successful operators are buying - competitors cannot replicate this benchmark.

#### Play: HUD Complaint Resolution Playbook (PVP                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Offer property managers facing HUD subsidy renewal a documented resolution process based on your experience clearing complaint backlogs for 9 similar properties, including the documentation template that HUD accepts.
- **Why this works**: Property managers don't just need traps - they need a solution that satisfies HUD's documentation requirements. Offering the proven timeline (45 days) and the accepted documentation template removes all execution risk and provides complete confidence.
- **Data Sources**:
  - HUD Multifamily Properties Database - complaint counts, renewal dates
  - Internal Customer Success Records - complaint clearance timeline by property type
- **Outreach Message template**:
  ```text
  Subject: Complaint resolution plan for HUD renewal
  
  Sunset Manor's 7 tenant pest complaints need documented resolution before your March 2025 HUD contract renewal.
  
  We've helped 9 Houston Section 8 properties clear complaint backlogs averaging 45 days from trap deployment to HUD acceptance.
  
  Should I send you the documentation template HUD accepts?
  ```
- **Data Requirement**: This play requires customer success records tracking complaint resolution timelines for HUD-assisted properties, plus HUD-accepted documentation templates.
                    This institutional knowledge of HUD requirements and proven resolution timelines is unique to your business.

#### Play: Organic Certification Audit Compliance Guide (PVP                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Offer organic farms approaching certification renewal a proven 3-trap setup that passes USDA audits, backed by your experience with 47 certified organic operations and including the placement guide that satisfies auditors.
- **Why this works**: Organic farmers facing certification renewal need documented non-lethal pest management practices. Offering a setup that "passes USDA audits 100% of the time" removes all compliance risk and provides complete confidence during a high-stakes renewal period.
- **Data Sources**:
  - USDA Organic Integrity Database - certification numbers, renewal dates
  - Internal Customer Records - organic farm customers with successful audit outcomes
- **Outreach Message template**:
  ```text
  Subject: Non-lethal trap options for your NOP audit
  
  Your USDA NOP certification (Cert #12345) requires documented non-lethal rodent control for the March 2025 renewal.
  
  We supply 47 certified organic farms in Texas - here's the 3-trap setup that passes USDA audits 100% of the time.
  
  Want me to send you the equipment list and placement guide?
  ```
- **Data Requirement**: This play requires customer records showing which customers are certified organic operations, plus audit compliance documentation showing successful USDA audit outcomes.
                    This track record of audit compliance and proven setup configurations is proprietary to your business.

#### Play: Regional Equipment Gap Analysis (PVP                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Benchmark an operator's trap inventory against the Fort Worth market average using aggregated sales data, then tie the undersupply to their inability to handle peak season emergency calls.
- **Why this works**: The 56% below market average is a specific competitive disadvantage. Tying it to "peak squirrel season (March-May)" shows you understand their seasonal revenue patterns. Offering the "top 3 operator equipment mix" provides clear actionable guidance.
- **Data Sources**:
  - State Pest Control License Database - operator locations
  - Internal Sales Data - equipment purchases by market
- **Outreach Message template**:
  ```text
  Subject: You're short 15 traps vs Fort Worth peers
  
  Your 12 live traps are 56% below the Fort Worth operator average of 27 traps.
  
  That undersupply forces you to reject emergency calls during peak squirrel season (March-May).
  
  Should I send you the equipment mix of the top 3 operators here?
  ```
- **Data Requirement**: This play requires aggregated sales data showing equipment purchases by operator and market, with median inventory levels calculated across 20+ operators per region.
                    Only you have visibility into market equipment benchmarks - competitors cannot provide this comparison.

---

## Sedgwick (sedgwick.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/sedgwick-com)
**Strategic Summary**: Playbook uses FDA warning letters and internal recall outcome data from 7,000+ managed recalls to build pre-completed customer notification trees, and uses MSHA mine safety data to surface multi-facility POV threshold risk.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your claims management

Hi [First Name],

I noticed you're hiring for compliance roles at [Company]. Congrats on the growth!

At Sedgwick, we help companies like yours manage complex claims across multiple jurisdictions. Our JURIS platform provides real-time visibility and our 33,000 experts handle everything from workers' comp to product recalls.

We work with 78 of the Fortune 100, including leaders in manufacturing, healthcare, and energy.

Would you be open to a 15-minute call to discuss how we can optimize your claims operations?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Your Recall Notification Tree for 14 SKUs (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Target medical device or pharmaceutical manufacturers who received FDA warning letters. Map their at-risk product lines and build a complete customer notification tree showing who needs to be contacted and in what order.
                    This play delivers immediate strategic value: the notification tree with account counts and sequencing strategy they can use whether they hire you or not.
- **Why this works**: The specificity is stunning - 14 SKUs, 2,847 accounts, 18,300 end-users. This isn't a pitch, it's pre-completed work.
                    The strategic insight about "who reports first" addresses a critical brand reputation concern. This demonstrates deep understanding of recall mechanics that competitors can't replicate without doing the same analysis.
- **Data Sources**:
  - FDA Warning Letters Database - facility name, warning date, violation scope
  - Internal Recall Database - product distribution patterns, notification tree templates, timing roadmaps from 7,000+ managed recalls
- **Outreach Message template**:
  ```text
  Subject: Your recall notification tree for 14 SKUs
  
  Based on your November 14th warning letter scope, we mapped which 14 SKUs are at risk and built the customer notification tree showing 2,847 direct accounts and 18,300 downstream end-users.
  
  The notification sequencing determines whether you control the narrative or CLIA labs report adverse events first.
  
  Want the notification tree and timing roadmap?
  ```
- **Data Requirement**: This play requires Sedgwick's internal database of recall notification patterns from managing 7,000+ recalls, including product distribution mapping methodologies and notification sequencing strategies.
                    Combined with public FDA warning letter details. This synthesis is unique to Sedgwick's recall management expertise.

#### Play: 3 of Your Mines Approaching POV Thresholds (PQS                     Public Data | Strong - Strong (9.1/10))

- **What's the play?**: Target coal mine operators with multiple facilities simultaneously approaching MSHA's pattern of violations (POV) threshold. The play demonstrates portfolio-level risk analysis that individual mine managers may not have visibility into.
                    This works because it shows cross-facility pattern recognition that the company's own safety teams might miss when focused on individual sites.
- **Why this works**: The portfolio view (Pike County: 4, Harlan County: 3, Bell County: 4) demonstrates you analyzed their entire operation, not just one facility.
                    The insight about "compounding scrutiny" when multiple sites approach POV simultaneously is non-obvious and genuinely valuable. This triggers an "oh shit" moment for whoever oversees safety across locations.
- **Data Sources**:
  - MSHA Mine Safety Database - mine_name, mine_id, violation_count (S&S violations), inspection_date
- **Outreach Message template**:
  ```text
  Subject: 3 of your mines approaching POV thresholds
  
  Pike County has 4 S&S violations, Harlan County has 3, and Bell County has 4 - all within their 90-day windows.
  
  Collectively you're tracking toward pattern violations at 3 sites simultaneously, which compounds MSHA scrutiny.
  
  Is anyone coordinating abatement across these three mines?
  ```

#### Play: Ventilation Pattern Analysis for Your 3 Mines (PVP                     Public Data | Strong - Strong (9.0/10))

- **What's the play?**: Analyze MSHA violation reports across multiple facilities owned by the same operator to identify systemic engineering issues. When the same violation type appears across different sites, it signals a corporate-level problem rather than site-specific failures.
                    Deliver a root cause hypothesis based on actual inspection report analysis - this is actionable intelligence they can use immediately.
- **Why this works**: The "not coincidence" framing is bold and attention-grabbing. Identifying the same violation pattern (ventilation systems) across 3 facilities within 60 days demonstrates you actually read the inspection reports, not just pulled violation counts.
                    The systemic engineering issue insight elevates the conversation from site-level operations to corporate safety strategy. This lands on the desk of the VP of Safety, not just mine managers.
- **Data Sources**:
  - MSHA Mine Safety Database - mine_name, violation_type, inspection_date, inspection_reports (full text)
- **Outreach Message template**:
  ```text
  Subject: Ventilation pattern analysis for your 3 mines
  
  All 3 of your mines (Pike, Harlan, Bell) have S&S violations in ventilation systems within 60 days - that's not coincidence.
  
  We pulled the inspection reports and found identical plan deficiencies that suggest a systemic engineering issue across your operation.
  
  Want the root cause analysis?
  ```

#### Play: 4 High-Severity MSHA Citations at Your Pike County Mine (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target coal mines that are one violation away from MSHA's pattern of violations (POV) threshold. This creates urgency because POV status triggers mandatory safety conferences and potential closure orders.
                    The specificity of counting violations for them (4 of 5) demonstrates active monitoring and creates a sense of "someone is paying attention to this."
- **Why this works**: The POV threshold is a concrete regulatory trigger with severe consequences (closure orders). Counting the violations for them (4 of 5, one away) makes the urgency visceral.
                    Specific location (Pike County KY), date (Dec 3), and violation types (ventilation and roof control) prove this isn't a template. The question about tracking/coordination addresses an operational gap they likely have.
- **Data Sources**:
  - MSHA Mine Safety Database - mine_name, mine_id, violation_count (S&S), inspection_date, violation_type
- **Outreach Message template**:
  ```text
  Subject: 4 high-severity MSHA citations at your Pike County mine
  
  Your Pike County KY mine received 4 significant and substantial violations on December 3rd for ventilation and roof control.
  
  MSHA's pattern of violations threshold is 5 S&S citations in 90 days - you're one away from POV status and potential closure orders.
  
  Is someone tracking the violation count and abatement schedule?
  ```

#### Play: 12 Facilities in Your Portfolio with Dual Violations (PQS                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Target large manufacturers or industrial companies with multiple facilities. Cross-reference EPA ECHO and OSHA databases to identify facilities with violations from both agencies within 30 days of each other.
                    This portfolio-level analysis reveals systemic compliance gaps that corporate risk managers need to see but often don't have visibility into.
- **Why this works**: The portfolio scope (12 facilities) demonstrates enterprise-level analysis. Highlighting 3 facilities "in escalation zones" with joint enforcement notices creates immediate urgency.
                    The deliverable (facility list with abatement deadlines) is concrete and actionable. This non-obvious synthesis across properties is exactly what VP of Risk Management needs but doesn't have time to compile themselves.
- **Data Sources**:
  - EPA ECHO Database - facility_name, facility_address, violation_count, inspection_date
  - OSHA Inspections Database - establishment_name, establishment_address, citation_count, inspection_date
- **Outreach Message template**:
  ```text
  Subject: 12 facilities in your portfolio with dual violations
  
  We found 12 facilities across your portfolio with open EPA and OSHA violations within 30 days of each other.
  
  Three of them (Dallas, Midland, Houston) are already in penalty escalation zones with joint enforcement notices.
  
  Want the full facility list with abatement deadlines?
  ```

#### Play: Your FDA Warning Letter from November 14th (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target pharmaceutical and medical device manufacturers who received FDA warning letters for sterile manufacturing violations. Use historical data to show that warning letters are leading indicators of recalls within 180 days.
                    The timeline pressure (day 45 of 180) creates urgency while the 62% recall conversion rate makes the risk concrete.
- **Why this works**: The specific date (Nov 14) and violation type (CGMP in sterile manufacturing) prove you read their actual warning letter. The 62% stat backed by 2019-2024 data is powerful and credible.
                    Timeline pressure (day 45 of 180) creates urgency without being alarmist. The question assumes sophistication (recall team exists) which flatters rather than condescends. This is genuinely non-obvious insight about warning letter trajectories.
- **Data Sources**:
  - FDA Warning Letters Database - facility_name, warning_date, violation_type
  - FDA Recalls Database - recall_date, facility_name (to calculate conversion rates)
- **Outreach Message template**:
  ```text
  Subject: Your FDA warning letter from November 14th
  
  FDA issued a warning letter to your facility on November 14th for CGMP violations in sterile manufacturing.
  
  62% of warning letters in sterile products lead to voluntary recalls within 180 days - you're at day 45.
  
  Is your recall coordination team already mobilized?
  ```

#### Play: Your Mine is 1 Citation Away from POV Status (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Similar to the Pike County play but with emphasis on the 90-day rolling window. Track coal mines with 4 S&S violations since a specific start date to show they're approaching the POV threshold within MSHA's calculation period.
                    The focus on "mandatory safety conferences and potential closure orders" makes the consequences concrete.
- **Why this works**: Strong urgency (1 away from threshold). Specific timeframe (since Sept 5, 90-day window) shows you understand MSHA's calculation methodology.
                    POV consequences are concrete and scary (closure orders). The question about coordinating with MSHA on abatement timeline is appropriate and shows understanding of the regulatory process.
- **Data Sources**:
  - MSHA Mine Safety Database - mine_name, mine_id, violation_count (S&S), inspection_date
- **Outreach Message template**:
  ```text
  Subject: Your mine is 1 citation away from POV status
  
  Pike County mine has 4 S&S violations since September 5th - MSHA's pattern threshold is 5 in 90 days.
  
  POV status triggers mandatory safety conferences and potential closure orders for subsequent violations.
  
  Who's coordinating with MSHA on the abatement timeline?
  ```

#### Play: Your Warning Letter Mentions 8 Sterile Product Lines (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target pharmaceutical manufacturers with FDA warning letters that cite multiple product lines. Read the actual warning letter to count specific product lines mentioned, then demonstrate understanding of how recall complexity varies by product type.
                    The insight about ophthalmics having 4x the notification burden of injectables shows deep domain expertise.
- **Why this works**: Specific product line count (8) from actual letter proves you read it carefully. The ophthalmics vs injectables comparison (4x notification burden) is insightful and demonstrates specialized knowledge.
                    The question addresses prioritization strategy, which is genuinely valuable - they probably haven't thought through which lines to address first. This is non-obvious synthesis of the warning letter that adds strategic value.
- **Data Sources**:
  - FDA Warning Letters Database - facility_name, warning_date, violation_scope (full letter text)
- **Outreach Message template**:
  ```text
  Subject: Your warning letter mentions 8 sterile product lines
  
  FDA's November 14th letter cites CGMP violations across 8 specific product lines in your sterile suite.
  
  Each product line has different distribution channels and recall complexity - ophthalmics have 4x the notification burden of injectables.
  
  Who's prioritizing which lines to address first?
  ```

#### Play: EPA and OSHA Both Cited Your Midland Plant in October (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target manufacturing facilities with EPA and OSHA violations within the same 30-day window. The dual enforcement signals systemic safety/compliance failures that create compounded regulatory liability.
                    The penalty multiplier insight (willful classification at $156K per violation) makes the financial risk concrete.
- **Why this works**: Specific facility address (1234 Industrial Blvd) and dates (Oct 15, Oct 22) establish credibility. Quantified penalty risk ($156K) makes it concrete.
                    The "joint enforcement increases penalty multipliers" angle is non-obvious and valuable. Easy routing question. They demonstrated cross-agency data synthesis that most vendors wouldn't bother with.
- **Data Sources**:
  - EPA ECHO Database - facility_name, facility_address, violation_date, violation_type
  - OSHA Inspections Database - establishment_name, establishment_address, citation_date, citation_severity
- **Outreach Message template**:
  ```text
  Subject: EPA and OSHA both cited your Midland plant in October
  
  Your Midland TX facility (1234 Industrial Blvd) received EPA CAA violations on October 15th and OSHA serious citations on October 22nd.
  
  Joint enforcement increases penalty multipliers - your next violation at this site could trigger willful classification at $156K per OSHA violation.
  
  Who's managing the dual abatement timeline?
  ```

#### Play: 180-Day Recall Window Closing for Your Facility (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target pharmaceutical and medical device manufacturers with FDA warning letters for sterile CGMP violations. Emphasize the timeline countdown (day 45 of 180-day typical window before recalls) to create urgency.
                    The 62% recall conversion rate based on 2019-2024 data makes the risk quantifiable.
- **Why this works**: Timeline countdown (day 45) creates urgency. Specific violation type and data range (2019-2024) make the 62% stat credible.
                    The question about recall prep is appropriate and assumes they need it (maybe presumptuous but acceptable given the data). Similar to the other warning letter variant but slightly weaker execution.
- **Data Sources**:
  - FDA Warning Letters Database - facility_name, warning_date, violation_type
  - FDA Recalls Database - recall_date, facility_name (to calculate conversion rates)
- **Outreach Message template**:
  ```text
  Subject: 180-day recall window closing for your facility
  
  Your November 14th FDA warning letter puts you at day 45 of the typical 180-day window before recalls.
  
  Sterile CGMP violations have the highest recall conversion rate at 62% based on 2019-2024 FDA data.
  
  Who's leading recall preparedness planning?
  ```

#### Play: Recall Cost Forecast for Your Sterile Line (PVP                     Public + Internal | Okay - Okay (7.8/10))

- **What's the play?**: Target manufacturers with FDA warning letters. Model recall cost scenarios using Sedgwick's internal database of 340+ similar recalls to provide median cost estimates by product type and violation category.
                    The deliverable (cost breakdown by recall scope) offers planning value whether they engage or not.
- **Why this works**: Uses their specific warning letter as anchor point. The $4.7M median cost is specific and scary. Claims proprietary database (340 recalls) though hard to verify.
                    The deliverable (cost breakdown by recall scope) is concrete. However, this edges toward industry benchmarks dressed up as insight - it somewhat fails the competitor test as other recall management firms could send similar data.
- **Data Sources**:
  - FDA Warning Letters Database - facility_name, warning_date, violation_type
  - Internal Recall Cost Database - median costs by product type, violation category, recall scope (from 340+ managed recalls)
- **Outreach Message template**:
  ```text
  Subject: Recall cost forecast for your sterile line
  
  Based on your November 14th FDA warning letter, we modeled recall scenarios for your sterile product line using our database of 340 similar recalls.
  
  The median direct cost for CGMP-triggered sterile recalls is $4.7M across notification, logistics, and replacement inventory.
  
  Want the full cost breakdown by recall scope?
  ```
- **Data Requirement**: This play requires Sedgwick's internal database of recall costs from 340+ managed events, segmented by product type, violation category, and recall scope (median costs across notification, logistics, inventory replacement).
                    This is proprietary data only Sedgwick has from managing thousands of recalls.

#### Play: Joint Enforcement Timeline for Your 3 Texas Plants (PVP                     Public + Internal | Okay - Okay (7.6/10))

- **What's the play?**: Target manufacturers with multiple facilities facing dual EPA-OSHA enforcement within 30 days. Build a consolidated response strategy showing optimal abatement sequencing to minimize penalty exposure across all sites.
                    The portfolio scope (3 facilities) demonstrates enterprise-level thinking.
- **Why this works**: Multi-facility scope shows portfolio thinking. The EPA-OSHA coordination insight about penalty negotiations is valuable.
                    However, the deliverable is vague - what's actually in the roadmap? Feels like consulting pitch, not immediate value. Doesn't pass "actionable without reply" test. Would need more specificity to be truly strong.
- **Data Sources**:
  - EPA ECHO Database - facility_name, facility_address, violation_date
  - OSHA Inspections Database - establishment_name, establishment_address, citation_date
  - Internal Compliance Playbooks - consolidated response strategies, abatement sequencing templates, penalty negotiation frameworks
- **Outreach Message template**:
  ```text
  Subject: Joint enforcement timeline for your 3 Texas plants
  
  Dallas, Midland, and Houston all have EPA-OSHA double violations within 30 days - EPA typically coordinates with OSHA on penalty negotiations when violations overlap.
  
  We built a consolidated response strategy showing optimal abatement sequencing to minimize penalty exposure across all three sites.
  
  Want the three-facility compliance roadmap?
  ```
- **Data Requirement**: This play requires Sedgwick's internal playbooks for coordinated EPA-OSHA enforcement responses, including penalty negotiation frameworks and multi-site compliance sequencing strategies.
                    Combined with public violation data to create facility-specific roadmaps.

#### Play: Your POV Avoidance Playbook for Pike County (PVP                     Public + Internal | Okay - Okay (7.4/10))

- **What's the play?**: Target coal mines approaching MSHA's pattern of violations threshold. Map violation patterns across 84 days to identify high-risk systems likely to trigger the 5th citation that would push them into POV status.
                    Offer a playbook covering inspection timing, abatement sequencing, and MSHA conference preparation.
- **Why this works**: Specific facility (Pike County) and timeframe (84 days) establish credibility. The "3 high-risk systems" claim is interesting but unverified.
                    The playbook sounds valuable but what's actually in it? This is more consulting/advisory than data insight. Doesn't give them anything actionable without a call. Would need more specificity about the deliverable.
- **Data Sources**:
  - MSHA Mine Safety Database - mine_name, violation_type, violation_date, inspection_date
  - Internal Coal Mine Claims Database - pattern analysis from managing mine safety claims, POV avoidance strategies, MSHA conference prep templates
- **Outreach Message template**:
  ```text
  Subject: Your POV avoidance playbook for Pike County
  
  We mapped the S&S violation patterns at Pike County across 84 days and identified 3 high-risk systems likely to trigger the 5th citation.
  
  Our playbook shows inspection timing, abatement sequencing, and MSHA conference prep for mines in POV risk.
  
  Want the violation pattern analysis?
  ```
- **Data Requirement**: This play requires Sedgwick's internal knowledge base from managing coal mine claims, including pattern analysis capabilities and POV avoidance playbooks with inspection timing and abatement sequencing strategies.
                    Combined with public MSHA violation data to identify high-risk systems.

#### Play: Dual Abatement Timeline for Your Midland Plant (PVP                     Public + Internal | Okay - Okay (7.2/10))

- **What's the play?**: Target facilities with overlapping EPA and OSHA violation abatement deadlines. Build a coordination timeline showing both agencies' inspection schedules, penalty escalation triggers, and optimal response sequencing.
                    The "dual-track roadmap" positions Sedgwick as coordination experts.
- **Why this works**: Specific to their facility and dates (Oct 15, Oct 22). The "dual-track roadmap" sounds valuable.
                    But what exactly is in it? Too vague about deliverable. This feels like a consulting pitch, not a data insight. Doesn't pass "so what" test - not actionable without meeting. Needs more concrete preview of the actual value.
- **Data Sources**:
  - EPA ECHO Database - facility_name, violation_date, abatement_deadline
  - OSHA Inspections Database - establishment_name, citation_date, abatement_deadline
  - Internal Compliance Templates - dual-track coordination timelines, penalty escalation frameworks, response sequencing strategies
- **Outreach Message template**:
  ```text
  Subject: Dual enforcement timeline for your Midland plant
  
  Your Midland facility has EPA CAA violations (Oct 15) and OSHA serious citations (Oct 22) with overlapping abatement deadlines.
  
  We built a coordination timeline showing both agencies' inspection schedules, penalty escalation triggers, and optimal response sequencing.
  
  Want the dual-track compliance roadmap?
  ```
- **Data Requirement**: This play requires Sedgwick's internal templates and playbooks for dual EPA-OSHA enforcement coordination, including inspection schedule tracking, penalty escalation triggers, and response sequencing frameworks.
                    Combined with public violation and abatement deadline data.

---

## Sixfold (sixfold.ai)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/sixfold-ai)
**Strategic Summary**: Playbook uses internal pharmaceutical cold chain carrier performance data combined with FDA inspection records to deliver ready-to-submit audit documentation, and forecasts automotive shipment exceptions from historical exception patterns.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Real-time visibility for your supply chain

Hi [First Name],

I noticed you recently posted about supply chain challenges on LinkedIn - congrats on the growth!

At Sixfold, we help companies like yours gain real-time visibility across all carriers and modes of transportation. Our platform integrates with 175+ carriers to give you proactive exception management and reduce those frustrating check calls.

Companies like Nestlé and Kingspan have saved thousands of hours with our solution.

Are you available for a 15-minute call next week to discuss how we can help optimize your logistics operations?

Best,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: Carrier Temperature Data for Your FDA File (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Pharmaceutical distributors facing FDA 483 observations for temperature monitoring need documented proof of carrier cold chain performance. Pull actual temperature compliance records for all carriers serving their facility and present it as ready-to-use audit documentation.
- **Why this works**: You're solving an immediate compliance documentation burden. Compiling carrier temperature data manually would take their team weeks. You're delivering it ready-to-submit to FDA inspectors. This isn't a sales pitch - it's directly usable compliance evidence they need right now.
- **Data Sources**:
  - Sixfold Temperature Monitoring Data - temperature excursion incidents, carrier performance by route
  - FDA Wholesale Drug Distributor and 3PL Licensing Database - facility addresses, inspection dates
- **Outreach Message template**:
  ```text
  Subject: Carrier temperature data for your FDA file
  
  Pulled temperature compliance records for all carriers serving your Pennsylvania facility in Q4 2024.
  
  FedEx Cold Chain: 8 excursions, UPS Healthcare: 3 excursions, DHL Medical: 1 excursion on your lanes.
  
  Want the full audit trail showing carrier performance against your 483 temperature monitoring requirement?
  ```
- **Data Requirement**: This play requires temperature monitoring data from pharmaceutical cold chain shipments by carrier, with ability to filter by destination facility and time period.
                    Combined with public FDA facility inspection records. This synthesis is unique to Sixfold's visibility platform.

#### Play: April Automotive Parts Shipment Exception Forecast (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Automotive manufacturers with JIT component delivery cannot absorb multi-day delays without production line shutdowns. Use historical exception rate patterns to predict exactly when and where April bottlenecks will occur, then offer carrier-by-carrier routing alternatives before the disruptions hit.
- **Why this works**: This is pure predictive value. You're telling them "April will be bad for Detroit shipments" with specific percentages and offering the solution (carrier routing data) before they even ask. For JIT operations, this prevents line shutdowns that cost tens of thousands per hour.
- **Data Sources**:
  - Sixfold Shipment Tracking Data - exception rates by commodity, region, carrier, and month
- **Outreach Message template**:
  ```text
  Subject: Your April automotive parts shipments
  
  Automotive parts shipments through Detroit have 23% exception rates every April due to port congestion and carrier capacity constraints.
  
  You ship JIT components that can't absorb 3-day delays without line shutdowns.
  
  Want the carrier-by-carrier breakdown for April so you can route around the bottlenecks?
  ```
- **Data Requirement**: This play requires historical exception rate data by commodity type, region, carrier, and month from tracking millions of shipments across customer base.
                    This is proprietary data only Sixfold has - competitors cannot replicate this play.

#### Play: March Cold Chain Exception Forecast for Perishable Routes (PVP                     Internal Data | Strong - Strong (8.9/10))

- **What's the play?**: Cold chain distributors shipping perishable goods from California to Northeast face predictable seasonal overload during March produce season. Deliver week-by-week exception forecasts and alternative routing options before the disruptions cause spoilage losses.
- **Why this works**: Spoilage losses from delays directly impact their bottom line. You're providing both the warning (31% exception rates in March) and the solution (alternative routes) with timing specific enough to act on. This prevents a predictable problem rather than reacting to it.
- **Data Sources**:
  - Sixfold Shipment Tracking Data - exception rates by commodity, lane, season, and carrier
- **Outreach Message template**:
  ```text
  Subject: March exception rates for your cold chain routes
  
  Cold chain shipments from California to Northeast distributors hit 31% exception rates every March during produce season carrier overload.
  
  Your perishable goods can't sit in delays without spoilage losses.
  
  Want the week-by-week forecast and alternative routing options for March 2025?
  ```
- **Data Requirement**: This play requires aggregated exception rate patterns by commodity, lane, season, and carrier from tracking data across food/beverage distribution customers.
                    This is proprietary data only Sixfold has - competitors cannot replicate this play.

#### Play: February Exception Forecast for Electronics Shipments (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Electronics distributors shipping high-value components from West Coast ports to Midwest face predictable February delays from weather and Chinese New Year backlog. Provide daily exception probability forecasts for their top shipping lanes to enable proactive routing decisions.
- **Why this works**: High-value electronics sitting in weather delays represents significant capital risk. The granularity (daily probabilities by lane) makes this immediately actionable - they can route around high-risk days. The seasonal drivers (weather, CNY) are visible and credible.
- **Data Sources**:
  - Sixfold Shipment Tracking Data - exception forecasting by commodity, lane, and day
- **Outreach Message template**:
  ```text
  Subject: February exception forecast for your lanes
  
  Electronics shipments from West Coast ports to Midwest distributors average 19% exception rates every February due to weather and Chinese New Year backlog.
  
  You're shipping high-value components that can't sit in weather delays.
  
  Want the daily exception probability forecast for your top 5 lanes in February 2025?
  ```
- **Data Requirement**: This play requires exception rate forecasting model by commodity, lane, and day based on historical patterns, weather data, and seasonal events across electronics distribution customers.
                    This is proprietary data only Sixfold has - competitors cannot replicate this play.

#### Play: Q2 Automotive Shipment Risk from Carrier Capacity Shifts (PQS                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: JIT automotive manufacturers shipping through Ohio face predictable Q2 exception spikes when carriers shift capacity after spring maintenance schedules. Use historical patterns to identify prospects who will face this issue in April-June and mirror the specific risk with timing and percentages.
- **Why this works**: The specificity (27% exception rates, Q2, Ohio, carrier capacity shifts, line shutdown costs) shows deep understanding of their operations. The timing (Q2 is coming soon) creates urgency. The question routes easily to their planning team.
- **Data Sources**:
  - Sixfold Shipment Tracking Data - seasonal exception analysis by commodity, lane, and quarter
- **Outreach Message template**:
  ```text
  Subject: Your Q2 automotive shipment risk
  
  JIT automotive parts shipments through Ohio have 27% exception rates in Q2 every year due to carrier capacity shifts after spring maintenance schedules.
  
  Your production lines can't absorb multi-day component delays without shutdown costs.
  
  Is your team planning carrier redundancy for April through June?
  ```
- **Data Requirement**: This play requires seasonal exception rate analysis by commodity type, shipping lane, and quarter from historical tracking data across automotive manufacturing customers.
                    This is proprietary data only Sixfold has - competitors cannot replicate this play.

#### Play: FedEx Cold Chain Temperature Failures in Your Region (PQS                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Pharmaceutical manufacturers with FDA 483 observations for temperature monitoring need to know if their current carriers are creating additional compliance risk. Mirror back specific temperature excursion data for carriers serving their facility with geographic precision.
- **Why this works**: The specificity (12 excursions, Newark and Philadelphia, Q4, tied to their September FDA inspection) makes this feel like investigative research done specifically for them. The connection between carrier performance and their FDA commitments creates immediate urgency.
- **Data Sources**:
  - Sixfold Temperature Monitoring Data - temperature excursions by carrier, route, timeframe
  - FDA Inspection Classification Database - facility inspection dates and findings
- **Outreach Message template**:
  ```text
  Subject: 12 FedEx temperature failures in your region
  
  FedEx Cold Chain logged 12 temperature excursions on pharma routes through Newark and Philadelphia in Q4.
  
  Your September FDA inspection cited inadequate transit temperature controls.
  
  Who's monitoring your carriers against those 483 commitments?
  ```
- **Data Requirement**: This play requires temperature monitoring data from pharmaceutical shipments by carrier, route, and time period across customer network.
                    Combined with public FDA inspection records. This synthesis is unique to Sixfold's visibility platform.

#### Play: Cold Chain Carrier Performance vs FDA Standards (PQS                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Pharmaceutical facilities with FDA temperature monitoring citations need to validate their carriers meet compliance standards. Mirror back specific temperature excursion data for carriers serving their facility with exact counts and timing tied to their FDA inspection findings.
- **Why this works**: The specificity (4 excursions, UPS Healthcare, New Jersey facility, Nov-Dec 2024, September FDA inspection) demonstrates detailed research. The direct connection to their compliance gap creates immediate urgency. Easy routing question.
- **Data Sources**:
  - Sixfold Temperature Monitoring Data - temperature excursion data by carrier and facility
  - FDA Inspection Classification Database - facility inspection dates and findings
- **Outreach Message template**:
  ```text
  Subject: Your cold chain carriers vs FDA standards
  
  UPS Healthcare had 4 temperature excursions on pharmaceutical shipments to your New Jersey facility in November and December 2024.
  
  Your facility's FDA inspection in September flagged inadequate transit temperature monitoring.
  
  Who's validating carrier performance against those inspection findings?
  ```
- **Data Requirement**: This play requires temperature excursion data from pharmaceutical shipments by carrier and destination facility, cross-referenced with FDA inspection timing.
                    Combined with public FDA inspection records. This synthesis is unique to Sixfold's visibility platform.

#### Play: Pharma Shipments Using FedEx Cold Chain with Recent Excursions (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Pharmaceutical manufacturers facing FDA 483 observations need to know if their carrier choices are creating additional compliance risk. Mirror back specific temperature excursion data with carrier name, region, timeframe, and direct connection to their FDA compliance obligations.
- **Why this works**: The specificity (FedEx Cold Chain, Q4 2024, 12 excursions, Northeast corridor) combined with the direct tie to their September 483 observation creates immediate concern. The question is easy to route and directly addresses their compliance gap.
- **Data Sources**:
  - Sixfold Temperature Monitoring Data - temperature excursions by carrier and region
  - FDA Inspection Classification Database - facility inspection dates and findings
- **Outreach Message template**:
  ```text
  Subject: Your pharma shipments using FedEx Cold Chain
  
  FedEx Cold Chain had 12 temperature excursions in Q4 2024 across pharmaceutical shipments in the Northeast corridor.
  
  Your facility received a 483 observation in September for temperature monitoring during transit.
  
  Is someone tracking your carrier's cold chain performance against your FDA commitments?
  ```
- **Data Requirement**: This play requires aggregated temperature excursion data across pharmaceutical shipments by carrier and region from customer base.
                    Combined with public FDA inspection records. This synthesis is unique to Sixfold's visibility platform.

---

## Vantage Risk (vantagerisk.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/vantagerisk-com)
**Strategic Summary**: The playbook identifies oil &amp; gas facilities with unresolved EPA violations and expiring Title V air permits, and demolition contractors with repeat OSHA serious violations approaching willful reclassification deadlines, targeting risks that create uninsurable exposures.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Quick question about your insurance strategy

Hi [First Name],

I noticed on LinkedIn that [Company] recently expanded operations into [State]. Congrats on the growth!

I'm reaching out because Vantage Risk specializes in providing specialty insurance and reinsurance solutions for companies with complex risk profiles. We've helped similar organizations in [Industry] optimize their coverage while reducing costs.

Would you be open to a brief call next week to explore how we might help [Company] with your insurance needs?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: EPA Violation Facilities with Expiring Permits in Enforcement Escalation (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target oil & gas operators and power generation facilities with recent EPA violations AND permits expiring in next 90 days. These facilities face enforcement escalation - permit renewal will trigger enhanced scrutiny and cleanup cost exposure they can't get traditional coverage for.
- **Why this works**: Specific facility address and exact violation count prove real research. The connection between open violations and permit renewal risk is crystal clear. Exact expiration date creates urgency. Simple routing question makes it easy to respond.
- **Data Sources**:
  - EPA ECHO (Enforcement and Compliance History Online) - facility_name, violation_type, violation_date, enforcement_action, permit_status
  - Construction Industry License and Permit Database - permit_expiration, complaint_history
- **Outreach Message template**:
  ```text
  Subject: 3 EPA violations at Dallas plant, permit expires March 2025
  
  Your Dallas facility at 4501 Industrial Blvd has 3 unresolved EPA violations from the June 2024 inspection.
  
  Your Title V air permit expires March 15, 2025 - EPA rarely renews permits with open violations, triggering shutdown risk.
  
  Who's managing the violation abatement timeline?
  ```

#### Play: OSHA Pattern Violators with Open Abatement Deadlines (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target demolition and asbestos abatement contractors with 2+ serious violations of same type in 18 months PLUS open abatement deadlines. These contractors face willful violation reclassification - creating uninsurable workers comp exposure with standard carriers.
- **Why this works**: Exact inspection date and violation count show specific research. Clear financial consequence with actual penalty amounts ($16,131 vs $161,323). Imminent deadline creates urgency. Simple routing question makes it easy to answer.
- **Data Sources**:
  - OSHA Inspection and Citation Database - establishment_name, citation_type, violation_code, penalty_amount, abate_date, classification
  - Construction Industry License and Permit Database - license_status, complaint_history
- **Outreach Message template**:
  ```text
  Subject: 3 serious citations at Memphis plant deadline January 8th
  
  Your Memphis facility has 3 open serious violations from the October 22nd OSHA inspection with abatement deadline January 8, 2025.
  
  Missing this deadline triggers willful reclassification - penalties jump from $16,131 to $161,323 per violation.
  
  Who's tracking the abatement completion?
  ```

#### Play: OSHA Pattern Violators with Open Abatement Deadlines (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target contractors with 3+ serious violations across multiple inspections in 36 months. OSHA classifies these as pattern violators - the next citation triggers enhanced enforcement and possible criminal referral.
- **Why this works**: Specific facility address and exact violation timeline demonstrate research depth. Clear pattern violator classification risk. Criminal referral mention is serious and attention-grabbing. Easy yes/no about current management status.
- **Data Sources**:
  - OSHA Inspection and Citation Database - establishment_name, citation_type, violation_code, classification
  - Construction Industry License and Permit Database - complaint_history, license_status
- **Outreach Message template**:
  ```text
  Subject: Your Atlanta plant has 4 violations in 18 months
  
  Atlanta Manufacturing at 2200 Commerce Dr has 4 serious violations across 3 inspections since July 2023.
  
  OSHA classifies 3+ serious violations in 36 months as pattern violators - your next citation triggers enhanced enforcement and possible criminal referral.
  
  Is someone already managing the pattern violation status?
  ```

#### Play: EPA Violation Facilities with Expiring Permits in Enforcement Escalation (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target facilities with EPA consent orders expiring without compliance certification. Expired consent orders trigger automatic referral to DOJ for civil enforcement - penalties start at $59,973 per day per violation.
- **Why this works**: Specific consent order count and expiration date show research. DOJ referral consequence is severe. Per-day penalty amount is concrete and scary. Easy yes/no about current certification status.
- **Data Sources**:
  - EPA ECHO (Enforcement and Compliance History Online) - facility_name, enforcement_action, violation_date, permit_status
- **Outreach Message template**:
  ```text
  Subject: Portland plant has 2 consent orders expiring Q1 2025
  
  Portland Chemical's 2 EPA consent orders from 2023 violations expire March 31, 2025 without compliance certification.
  
  Expired consent orders trigger automatic referral to DOJ for civil enforcement - penalties start at $59,973 per day per violation.
  
  Is the compliance certification package already in review?
  ```

#### Play: CMS 1-2 Star Facilities Approaching SFF Designation with Staffing Gaps (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target home health agencies with 1-2 star ratings showing declining outcome trends AND no recent hiring for compliance/quality roles. These facilities are on track for Special Focus Facility designation - they need emergency liability coverage before CMS enforcement escalates.
- **Why this works**: Specific facility name and exact date show they researched us. SFF designation threat is real and actionable. Simple routing question makes it easy to answer. Direct about the rating but focused on solution.
- **Data Sources**:
  - CMS Home Health Care Agencies Dataset - provider_name, star_rating, quality_measures, patient_outcomes
  - CMS Home Health Quality Reporting Program Data - outcome_measures, improvement_measures
- **Outreach Message template**:
  ```text
  Subject: Sunset Manor dropped to 2 stars October 15th
  
  Sunset Manor's CMS rating fell from 3 stars to 2 stars in the October 15th survey.
  
  This puts you in the SFF candidate pool - CMS triggers enhanced oversight at 2 consecutive surveys below 3 stars.
  
  Who's leading your survey prep for the next cycle?
  ```

#### Play: EPA Violation Facilities with Expiring Permits in Enforcement Escalation (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target facilities added to EPA's High Priority Violator list. HPV status requires EPA headquarters approval to remove and blocks all permit renewals until resolved.
- **Why this works**: Exact date of HPV listing is very specific. HPV consequences are severe and clear. Shows understanding of EPA process (Region 6, HQ approval). Easy question about current engagement status.
- **Data Sources**:
  - EPA ECHO (Enforcement and Compliance History Online) - facility_name, violation_type, enforcement_action, permit_status
- **Outreach Message template**:
  ```text
  Subject: Houston site moved to High Priority Violator status
  
  Your Houston facility was added to EPA's High Priority Violator list on November 18, 2024 for Clean Water Act violations.
  
  HPV status requires EPA headquarters approval to remove and blocks all permit renewals until resolved.
  
  Is your compliance team already engaging with Region 6 enforcement?
  ```

#### Play: OSHA Pattern Violators with Open Abatement Deadlines (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target facilities with scheduled OSHA follow-up inspections to verify abatement. Failed follow-up inspections trigger willful upgrade and criminal referral consideration.
- **Why this works**: Specific inspection date creates urgency. Shows they tracked the follow-up scheduling. Criminal referral mention is serious. Direct question about completion status.
- **Data Sources**:
  - OSHA Inspection and Citation Database - establishment_name, citation_type, abate_date, classification
- **Outreach Message template**:
  ```text
  Subject: Chicago facility inspection scheduled January 15th
  
  OSHA scheduled follow-up inspection at Chicago Manufacturing for January 15, 2025 to verify abatement of 3 serious violations from August.
  
  You still have 1 open serious violation with incomplete abatement - failed follow-up inspections trigger willful upgrade and criminal referral consideration.
  
  Are all 3 abatements actually complete?
  ```

#### Play: EPA Violation Facilities with Expiring Permits in Enforcement Escalation (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target facilities with RCRA permits expiring in next 90 days AND open enforcement actions. EPA typically requires enforcement actions closed before permit renewal.
- **Why this works**: Exact day count creates immediate urgency. Specific facility and enforcement count. Clear consequence (permit won't renew). Easy yes/no question about abatement status.
- **Data Sources**:
  - EPA ECHO (Enforcement and Compliance History Online) - facility_name, enforcement_action, permit_status, permit_expiration
- **Outreach Message template**:
  ```text
  Subject: Your Fort Worth permit expires in 89 days
  
  Fort Worth Chemical's RCRA permit expires March 15, 2025 - that's 89 days from now.
  
  You have 2 open enforcement actions from September that EPA typically requires closed before renewal.
  
  Is the abatement plan already submitted to Region 6?
  ```

#### Play: OSHA Pattern Violators with Open Abatement Deadlines (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Target facilities with abatement deadlines in next 30 days. Missing the deadline by even one day triggers automatic willful upgrade - penalties jump 10x from $16,131 to $161,323 per violation.
- **Why this works**: Exact day count creates immediate urgency. Specific violation type (machine guarding). Stark penalty comparison is compelling. Simple yes/no about documentation status.
- **Data Sources**:
  - OSHA Inspection and Citation Database - establishment_name, citation_type, violation_code, penalty_amount, abate_date
- **Outreach Message template**:
  ```text
  Subject: Your Phoenix plant abatement deadline is 23 days away
  
  Phoenix Operations has abatement deadline December 30, 2024 for 2 serious machine guarding violations from September inspection.
  
  Missing this deadline by even one day triggers automatic willful upgrade - $161,323 per violation instead of $16,131.
  
  Is the abatement documentation already submitted?
  ```

#### Play: CMS 1-2 Star Facilities Approaching SFF Designation with Staffing Gaps (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target healthcare facilities with recent G-level citations (inadequate care planning). G-level citations trigger mandatory revisit within 6 months - another poor survey puts facility at immediate SFF designation.
- **Why this works**: Specific survey date and deficiency count. G-level citation detail shows research depth. Clear consequence timeline (6 month revisit). POC question shows understanding of their compliance world.
- **Data Sources**:
  - CMS Home Health Care Agencies Dataset - provider_name, quality_measures
  - CMS Home Health Quality Reporting Program Data - outcome_measures
- **Outreach Message template**:
  ```text
  Subject: Oakwood Care cited for 8 deficiencies December 3rd
  
  Oakwood Care received 8 deficiencies in the December 3rd survey, including 2 G-level citations for inadequate care planning.
  
  G-level citations trigger mandatory revisit within 6 months - another poor survey puts you at immediate SFF designation.
  
  Who's leading the POC implementation?
  ```

#### Play: CMS 1-2 Star Facilities Approaching SFF Designation with Staffing Gaps (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target healthcare facilities with staffing ratings below 2 stars AND RN hours below CMS threshold (0.55 per resident day). CMS uses staffing as primary SFF designation factor.
- **Why this works**: Extremely specific metrics - they know our exact data. Direct link between staffing and SFF risk is clear. Easy yes/no question. Slightly technical with the 0.42 metric but still clear.
- **Data Sources**:
  - CMS Home Health Care Agencies Dataset - provider_name, star_rating, quality_measures
- **Outreach Message template**:
  ```text
  Subject: Your staffing score at 1.8 triggers SFF risk
  
  Sunset Manor's staffing rating is 1.8 stars with RN hours at 0.42 per resident day - below the 0.55 threshold.
  
  CMS uses staffing as a primary SFF designation factor, and you're one survey away from enhanced oversight.
  
  Is someone already working on the RN coverage gap?
  ```

#### Play: CMS 1-2 Star Facilities Approaching SFF Designation with Staffing Gaps (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Target healthcare facilities with consistent low staffing ratings across 3+ quarters. CMS uses 3-quarter trends for SFF designation - persistent low ratings trigger enforcement.
- **Why this works**: Specific multi-quarter trend data. Exact percentage below threshold is concrete. Clear SFF designation risk. Simple routing question about improvement plan.
- **Data Sources**:
  - CMS Home Health Care Agencies Dataset - provider_name, star_rating, quality_measures
- **Outreach Message template**:
  ```text
  Subject: Riverside Manor staffing at 1.6 stars for 3 quarters
  
  Riverside Manor has maintained 1.6 star staffing rating for Q2, Q3, and Q4 2024 - CMS uses 3-quarter trends for SFF designation.
  
  Your RN hours are 0.38 per resident day, 31% below the 0.55 minimum CMS targets for non-SFF facilities.
  
  Who's managing your staffing improvement plan?
  ```

---

## Vertafore (vertafore.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/vertafore-com)
**Strategic Summary**: The playbook combines internal policy renewal calendar data with state insurance department rate filing records and DOI complaint records to identify carrier rate increase collisions with renewal windows and trace integration failures to specific customer complaints.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your agency operations

Hi [First Name],

I noticed your agency has been growing - congrats on the recent LinkedIn post about your team expansion!

At Vertafore, we help insurance agencies like yours modernize their operations with our leading AMS platform. We process over 200M transactions annually and serve 15,000+ agencies.

Our clients see improved efficiency, better client retention, and revenue growth without adding headcount.

Do you have 15 minutes next week to discuss how we can help [Company Name] scale more efficiently?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Workers Comp Rate Increase Collision with Renewal Window (PVP                     Public + Internal | Strong - Strong (9.6/10))

- **What's the play?**: Cross-reference public rate filing data with internal policy renewal calendars to identify carriers whose rate increases collide with high-volume renewal periods. Deliver a ranked list of at-risk accounts by premium size and historical rate sensitivity.
- **Why this works**: Rate increases during peak renewal periods create massive lapse risk. By identifying the exact collision and ranking accounts by risk, you're delivering actionable intelligence the carrier can use immediately to preserve book. This helps them serve policyholders better by proactively managing rate-sensitive accounts.
- **Data Sources**:
  - State Insurance Department Rate Filing Records - effective dates, filing dates
  - Vertafore Policy Administration System - renewal calendars, premium data, policy counts
- **Outreach Message template**:
  ```text
  Subject: 1,847 renewals in your rate increase window
  
  Your February 15th rate increase hits exactly when 1,847 policies renew (February 1-28).
  
  We ranked those accounts by premium size and lapse risk based on prior rate sensitivity.
  
  Should I send you the top 200 at-risk accounts?
  ```
- **Data Requirement**: This play requires policy renewal calendar data and premium data from Vertafore's carrier policy administration systems, combined with public rate filing records from state insurance departments.
                    This synthesis of internal renewal timing with public rate filings is unique to Vertafore's platform.

#### Play: Integration Failures Causing Regulatory Complaints (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Cross-reference Vertafore platform transaction error logs with public DOI complaint records to identify agencies where system integration failures directly caused customer complaints. Provide transaction IDs and error details for forensic analysis.
- **Why this works**: Agencies often don't connect system errors to customer complaints. By showing them the exact dates and transaction IDs where integration failures caused service issues, you're providing forensic evidence they can use to prevent future E&O claims. This helps them serve clients better by identifying root causes of service failures.
- **Data Sources**:
  - State Department of Insurance Complaint Records - complaint dates, agency names
  - Vertafore Platform Transaction Error Logs - transaction IDs, error types, dates
- **Outreach Message template**:
  ```text
  Subject: October integration errors caused 2 complaints
  
  Two of your October DOI complaints trace directly to carrier integration failures on October 14th and October 19th.
  
  We pulled the specific transaction logs showing the policy updates that failed to transmit.
  
  Want the transaction IDs and error details?
  ```
- **Data Requirement**: This play requires transaction error logs from Vertafore's integration platform, including transaction IDs, error types, timestamps, and affected policies.
                    Combined with public DOI complaint records. This forensic connection is unique to Vertafore's platform data.

#### Play: March Rate Increase Renewal Collision Analysis (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Identify carriers whose rate increase effective dates collide with their highest-volume renewal months. Quantify the exact number of affected policies and provide a renewal distribution calendar showing the collision impact.
- **Why this works**: Carriers often don't see the connection between rate filing timing and lapse rates. By showing them the exact policy count and distribution, plus offering a calendar and high-risk account list, you're delivering complete actionable intelligence. This helps them preserve book and serve policyholders by proactively managing retention.
- **Data Sources**:
  - State Insurance Department Rate Filing Records - effective dates
  - Vertafore Policy Administration System - renewal calendars, policy counts by month
- **Outreach Message template**:
  ```text
  Subject: Your rate increase hits 2,100 renewals in March
  
  Your workers comp rate increase filing effective March 1st collides with 2,100 policy renewals that same month.
  
  Carriers with this collision see higher lapse rates in the affected month versus baseline.
  
  Want the renewal distribution calendar and high-risk accounts?
  ```
- **Data Requirement**: This play requires policy renewal calendar data from Vertafore's carrier policy administration systems, showing monthly renewal distribution and policy counts.
                    Combined with public rate filing data. The synthesis of renewal timing with rate increases is unique to Vertafore.

#### Play: Integration Failure Correlation with Complaint Timing (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Identify agencies where carrier integration failures occurred within the same timeframe as regulatory complaints filed against them. Quantify the E&O claim risk pattern observed across other agencies with this correlation.
- **Why this works**: This is genuinely non-obvious intelligence. Agencies may know they have integration issues and may know they have complaints, but connecting the two with specific dates and transaction IDs is forensic-level analysis. The E&O risk quantification makes it urgent and actionable.
- **Data Sources**:
  - Vertafore Platform Integration Logs - carrier API errors, transaction failures, dates
  - State DOI Complaint Records - complaint dates, agency names
- **Outreach Message template**:
  ```text
  Subject: 3 integration errors correlate with your complaints
  
  Your agency had 3 carrier integration failures in Q4 that align with timing of regulatory complaints filed against you.
  
  Agencies with this pattern see higher E&O claim rates within 12 months.
  
  Want the specific transaction IDs and complaint dates?
  ```
- **Data Requirement**: This play requires Vertafore's carrier integration error logs with transaction-level detail (transaction IDs, error types, timestamps).
                    Combined with public DOI complaint records. The pattern analysis across customer base is proprietary to Vertafore.

#### Play: Commercial Lines Renewal Rate Benchmark Gap (PVP                     Internal Data | Strong - Strong (8.6/10))

- **What's the play?**: Use aggregated renewal rate data from Vertafore's AMS platform to show agencies how their commercial lines renewal performance compares to peer agencies in their state. Quantify the revenue gap and offer a breakdown by carrier.
- **Why this works**: Renewal rate is directly tied to agency profitability. By showing the specific line of business (commercial lines) and offering a peer comparison by carrier, you're providing immediately actionable intelligence. The agency can verify the dollar impact and identify exactly where the problem is. This helps them even if they don't buy anything.
- **Data Sources**:
  - Vertafore AMS Platform - policy renewal completion rates by line of business, state, agency size
- **Outreach Message template**:
  ```text
  Subject: Your commercial lines renewals at 68%
  
  Your commercial lines renewal rate is 68% - 19 points below comparable Texas agencies at 87%.
  
  That gap represents roughly $180K in lost annual commissions on your current book.
  
  Should I send the peer comparison by carrier?
  ```
- **Data Requirement**: This play requires aggregated policy renewal completion rates by line of business (commercial lines, personal lines, etc.) across Vertafore's AMS customer base, segmented by state and agency size tier.
                    This benchmark data is proprietary to Vertafore - only they see renewal performance across 15,000+ agencies.

#### Play: October Integration Failures Matching Complaint Timing (PQS                     Public + Internal | Strong - Strong (8.2/10))

- **What's the play?**: Identify agencies where Vertafore platform integration failures occurred during the same week as DOI complaints were filed against them. Connect the dots between system errors and customer service failures with specific dates.
- **Why this works**: This mirrors their exact situation with forensic precision. The specific date range (October 12-18) and complaint count (3) prove you did the research. The E&O premium impact makes it urgent. The routing question makes it easy to respond.
- **Data Sources**:
  - Vertafore Platform Integration Error Logs - dates, error counts, agency IDs
  - Texas Department of Insurance Complaint Records - complaint dates, agency names
- **Outreach Message template**:
  ```text
  Subject: Integration failures match your October complaints
  
  You had 5 carrier integration failures between October 12-18 that match the timing of 3 DOI complaints filed against your agency.
  
  Texas agencies with this correlation pattern face E&O premium increases at renewal.
  
  Is your E&O broker aware of the October incidents?
  ```
- **Data Requirement**: This play requires Vertafore's integration error logs showing failure dates, error counts, and affected agencies.
                    Combined with public DOI complaint records. The date correlation analysis is unique to Vertafore's platform data.

#### Play: March Rate Hike Affecting 41% of Q1 Renewals (PQS                     Public + Internal | Strong - Strong (8.0/10))

- **What's the play?**: Identify carriers whose March 1st rate increases affect a disproportionately high percentage of their Q1 renewal base. Use comparative context (highest in state) to emphasize the scale of the problem.
- **Why this works**: The specific policy count (2,100) and percentage (41%) are highly credible. The comparative context (highest in Texas) provides useful benchmarking. The routing question is easy to answer. Could be stronger if it offered more immediate value beyond highlighting the problem.
- **Data Sources**:
  - State Insurance Department Rate Filing Records - effective dates
  - Vertafore Policy Administration System - renewal calendars, Q1 renewal counts
- **Outreach Message template**:
  ```text
  Subject: March rate hike hits 2,100 renewals
  
  Your March 1st rate increase affects 2,100 workers comp policies renewing that same month - 41% of your Q1 renewal base.
  
  That's the highest collision rate we've seen among regional carriers in Texas this year.
  
  Who's managing the retention strategy for March?
  ```
- **Data Requirement**: This play requires policy renewal data from Vertafore's carrier policy administration systems, showing monthly and quarterly renewal counts.
                    Combined with public rate filing data. The comparative analysis across carriers is proprietary to Vertafore.

---

## Warrantech (warrantech.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/warrantech-com)
**Strategic Summary**: The playbook cross-references dealer inventory VINs against NHTSA recall databases and internal claims frequency data to identify open powertrain recalls that void warranty coverage and vehicle models with significantly higher-than-average transmission claim rates.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Warranty Solutions for [Dealership Name]

Hi [First Name],

I noticed you're a Finance Manager at [Dealership]. I wanted to reach out because Warrantech helps dealerships like yours increase F&I revenue through our comprehensive vehicle service contracts.

We work with dealerships nationwide to provide fully insured protection plans that your customers love. Our award-winning service includes 24/7 claims support and an easy online platform.

Are you available for a quick 15-minute call next week to discuss how we can help [Dealership] grow F&I penetration?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: 7 Explorers with Open Powertrain Recalls (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Cross-reference dealer inventory with NHTSA recall database to identify vehicles with open powertrain recalls that void extended warranty coverage until completed.
                    Deliver VIN-specific list of affected vehicles with recall campaign numbers so the dealer can prioritize recall completion before selling.
- **Why this works**: Recalls are a known administrative burden, but the warranty voiding detail is critical and often overlooked. Showing you've done the VIN-level research proves this isn't generic advice.
                    The F&I manager immediately sees this protects their customers from denied warranty claims and saves them from future reputation damage.
- **Data Sources**:
  - CIS Automotive API - dealer inventory VINs
  - NHTSA Recall Database - open recall campaigns by VIN
  - Warrantech Internal Warranty Database - VINs with warranty-impacting recall status
- **Outreach Message template**:
  ```text
  Subject: 7 of your Explorers have active recall campaigns
  
  7 of your 12 Ford Explorers have open NHTSA recall campaigns - 4 are powertrain-related that void extended warranty coverage until completed.
  
  Customers buying these without recall completion risk denied claims.
  
  Want the VIN list with recall campaign numbers?
  ```
- **Data Requirement**: This play requires dealer inventory VINs cross-referenced against NHTSA recall database and Warrantech's internal warranty database to identify warranty-impacting campaigns.
                    Combined with public recall data, this synthesis prevents customer claim denials and is unique to your business.

#### Play: High-Claims 2020 Jeep Wranglers in Inventory (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Use Warrantech's aggregated claims data to identify vehicle models with significantly higher transmission claims than comparable vehicles.
                    Cross-reference against dealer's current inventory to flag specific high-risk units and provide VIN-level risk profiles.
- **Why this works**: The claims data is proprietary and highly valuable - the dealer cannot get this insight anywhere else. The 42% higher claims stat is specific and alarming.
                    Helps the F&I manager have informed protection plan conversations and protects customers from expensive surprise repairs, improving customer satisfaction scores.
- **Data Sources**:
  - CIS Automotive API - dealer inventory by make/model/year
  - Warrantech Internal Claims Database - aggregated claims frequency and cost by vehicle make/model/year (minimum 50 contracts per model)
- **Outreach Message template**:
  ```text
  Subject: Your 2020 Jeep Wranglers = 42% higher claims
  
  The 8 used 2020 Jeep Wranglers on your lot have 42% higher transmission claims than comparable SUVs.
  
  Without extended coverage, buyers face $3,800 average transmission repairs within 48 months.
  
  Want me to flag which VINs have the highest risk profiles?
  ```
- **Data Requirement**: This play requires aggregated claims data by vehicle make/model/year across 500+ service contracts, with minimum 50 contracts per model to ensure privacy-safe aggregation. Includes median claim frequency, average claim cost, and approval rates.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: 12 High-Claims Ford Explorers on Your Lot (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Analyze dealer's current inventory using CIS Automotive API, then cross-reference against Warrantech's aggregated claims data to identify specific high-risk vehicles.
                    Deliver VIN-level breakdown showing which units have significantly higher powertrain claims than segment average.
- **Why this works**: The specificity is shocking - they know you analyzed THEIR actual inventory, not just generic advice. The 37% claims data helps them sell protection plans more effectively.
                    The VIN-level breakdown is immediately actionable and helps the F&I manager protect customers from surprise repair costs.
- **Data Sources**:
  - CIS Automotive API - dealer inventory by make/model/year/VIN
  - Warrantech Internal Claims Database - aggregated claims frequency by vehicle type (minimum 50 contracts per model)
- **Outreach Message template**:
  ```text
  Subject: 12 high-claims units sitting on your lot
  
  You have 12 2019-2021 Ford Explorers in inventory - these models average 37% higher powertrain claims than segment.
  
  Customers buying these without extended coverage face $4,200 average repair costs in year 3-5.
  
  Want the VIN-level claims risk breakdown?
  ```
- **Data Requirement**: This play requires aggregated claims data by vehicle make/model/year and ability to cross-reference against dealer inventory feeds or manual VIN entry.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Pattern Analysis for CFPB Complaints (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Analyze CFPB complaint narratives for dealership to identify common patterns across multiple complaints (e.g., "rushed through paperwork", "didn't understand coverage").
                    Map complaint patterns to typical F&I process flows to identify specific procedural gaps causing customer confusion.
- **Why this works**: They analyzed the actual complaint text and identified the root cause ("disclosure timing") rather than just pointing out the problem exists.
                    The process audit findings help the dealer fix the underlying issue, not just respond to complaints. This is immediately useful and actionable.
- **Data Sources**:
  - CFPB Consumer Complaint Database - complaint narratives, dates, resolution status
  - Warrantech Internal F&I Best Practices - typical process flows and disclosure timing patterns
- **Outreach Message template**:
  ```text
  Subject: Pattern in your 3 complaints = disclosure timing
  
  All 3 Q1 CFPB complaints mention 'rushed through paperwork' and 'didn't understand coverage' - the common thread is disclosure timing.
  
  I mapped the complaint narratives to your likely F&I process flow and flagged the 2 disclosure steps causing confusion.
  
  Want the process audit findings?
  ```
- **Data Requirement**: This play requires ability to analyze CFPB complaint text and map patterns to typical F&I process flows based on industry best practices.
                    Combined with Warrantech's F&I expertise, this synthesis helps dealers fix root causes of customer complaints.

#### Play: Template Response for CFPB Complaints (PVP                     Public + Internal | Strong - Strong (9.0/10))

- **What's the play?**: Analyze dealership's specific CFPB complaints to identify common themes (e.g., "unclear service contract terms"), then draft templated responses addressing each complaint narrative.
                    Include coverage clarification language that satisfies CFPB consent order patterns based on analysis of similar enforcement actions.
- **Why this works**: Pre-drafted responses save hours of work and reduce stress around regulatory compliance. The templates are specific to their actual complaints, not generic.
                    Helps resolve regulatory risk faster and demonstrates deep understanding of CFPB enforcement patterns.
- **Data Sources**:
  - CFPB Consumer Complaint Database - complaint narratives specific to this dealership
  - FTC/CFPB Consent Orders - language patterns for satisfactory responses
- **Outreach Message template**:
  ```text
  Subject: Template response for your 3 CFPB complaints
  
  All 3 of your Q1 CFPB complaints mention 'unclear service contract terms' - I drafted response templates addressing each narrative.
  
  The templates include coverage clarification language that satisfies CFPB consent order patterns.
  
  Want me to send the draft responses?
  ```
- **Data Requirement**: This play requires analysis of CFPB complaint narratives and knowledge of CFPB consent order language patterns from similar enforcement actions.
                    Combined with regulatory expertise, this helps dealers resolve complaints faster and reduce regulatory risk.

#### Play: 15 Nissan Rogues with CVT Warranty Gaps (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Identify Nissan Rogues in dealer inventory (known for CVT transmission failures), then check VIN-level warranty status against Nissan's extended CVT warranty database.
                    Deliver VIN-by-VIN breakdown showing which vehicles are covered by extended warranty and which are not, helping dealer avoid selling high-risk unprotected units.
- **Why this works**: CVT transmission failures are a well-known problem in Nissan Rogues, so the context is immediately credible. The VIN-level warranty check is immediately useful.
                    Helps dealer avoid selling unprotected high-risk units and protects customers from expensive failures. Low-effort ask to receive high-value data.
- **Data Sources**:
  - CIS Automotive API - dealer inventory VINs for Nissan Rogues
  - Nissan Extended CVT Warranty Database - VIN-level coverage status
- **Outreach Message template**:
  ```text
  Subject: 15 Nissan Rogues in your inventory need coverage
  
  You have 15 used 2018-2020 Nissan Rogues - these CVT transmissions fail at 2.3x the rate of competitors.
  
  Nissan extended the CVT warranty to 84k miles on some VINs but not all - want me to check which of yours are covered?
  
  Should I send the VIN-by-VIN warranty status?
  ```
- **Data Requirement**: This play requires dealer inventory VINs cross-referenced against Nissan's CVT extended warranty VIN database.
                    The VIN-level warranty check protects customers from buying high-risk vehicles outside extended coverage.

#### Play: Compliance Checklist for FTC Consent Order (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Analyze dealership's specific FTC consent order to extract all quarterly filing requirements, submission dates, and required documentation.
                    Build a compliance checklist mapping each requirement to consent decree sections, including FTC contact procedures.
- **Why this works**: A ready-made compliance checklist saves real time and reduces stress around regulatory deadlines. The specificity to their consent order timeline makes it immediately useful.
                    Helps them avoid missing deadlines that trigger penalties or breach notifications.
- **Data Sources**:
  - FTC Enforcement Actions Database - specific consent order language and requirements
- **Outreach Message template**:
  ```text
  Subject: Compliance checklist for your March 2027 deadline
  
  Your FTC consent order expires March 2027 - I built a quarterly compliance checklist mapping each filing requirement to the consent decree sections.
  
  It includes submission dates, required documentation, and FTC contact procedures.
  
  Want me to send the full compliance calendar?
  ```
- **Data Requirement**: This play requires analysis of FTC consent order language and ability to generate compliance checklists mapped to specific dealer enforcement actions.
                    The checklist is customized to their specific consent order, not a generic template.

#### Play: $67K Claims Exposure Across Pre-Owned Inventory (PVP                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Analyze dealer's pre-owned inventory using Warrantech's aggregated claims data to calculate total claims exposure across all high-risk units.
                    Identify the top 18 models carrying the highest powertrain claims risk over 36 months and provide dollar exposure estimate.
- **Why this works**: The specific inventory count (43 units) and dollar exposure ($67K) shows you analyzed their actual lot. The claims data is proprietary and valuable.
                    Helps F&I manager prioritize which units need protection plan recommendations to reduce dealership risk.
- **Data Sources**:
  - CIS Automotive API - dealer inventory by make/model/year
  - Warrantech Internal Claims Database - aggregated claims cost by vehicle type over 36 months
- **Outreach Message template**:
  ```text
  Subject: Your pre-owned inventory has $67K claims exposure
  
  Across your 43 pre-owned units, the top 18 models carry $67,000 in average powertrain claims risk over the next 36 months.
  
  That's based on actual claims data for those exact year/make/model combinations.
  
  Who's deciding which units get protection plan recommendations?
  ```
- **Data Requirement**: This play requires aggregated claims data by year/make/model and ability to calculate exposure across a dealer's current inventory.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: CFPB Service Contract Complaints Pattern (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Identify dealerships with 3+ CFPB complaints filed in Q1 2025 specifically about service contract sales, all mentioning similar themes like "unclear coverage terms" and "pressure tactics".
                    The pattern across multiple complaints signals systemic F&I execution gaps requiring process fixes, not just individual complaint responses.
- **Why this works**: Very specific date range (Q1 2025) and exact complaint themes extracted from CFPB narratives. The pattern identification ("unclear coverage" in all 3) is immediately actionable.
                    Helps dealer fix root cause before regulatory scrutiny escalates. Easy routing question makes response low-friction.
- **Data Sources**:
  - CFPB Consumer Complaint Database - dealership_name, complaint_type, financial_product, narrative text, date, state
- **Outreach Message template**:
  ```text
  Subject: CFPB flagged 3 service contract complaints this quarter
  
  The CFPB database shows 3 complaints about service contract sales at your dealership filed in Q1 2025.
  
  All 3 mention 'unclear coverage terms' and 'pressure tactics' in the narrative.
  
  Who's reviewing F&I disclosure scripts for compliance gaps?
  ```

#### Play: CFPB Complaint Surge in 60 Days (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Identify dealerships with sharp increases in CFPB complaints about F&I practices in a short window (e.g., 4 complaints in 60 days vs trailing 12-month average).
                    The sudden surge signals operational changes, staff turnover, or process breakdowns requiring immediate attention before regulatory scrutiny intensifies.
- **Why this works**: Specific date range (January 15 - March 15, 2025) and complaint count show they did research. The 300% increase is alarming and creates urgency.
                    Easy question about internal ownership. Helps prevent regulatory scrutiny and reputational damage.
- **Data Sources**:
  - CFPB Consumer Complaint Database - dealership_name, complaint_type, financial_product, date, state
- **Outreach Message template**:
  ```text
  Subject: 4 CFPB complaints about your F&I in 60 days
  
  Your dealership received 4 CFPB consumer complaints about F&I practices between January 15 and March 15, 2025.
  
  That's a 300% increase versus your trailing 12-month average.
  
  Is someone tracking the common themes across those complaints?
  ```

#### Play: FTC Consent Order Quarterly Reports Due (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Identify dealerships under FTC consent orders for warranty/service contract violations with upcoming quarterly compliance reporting deadlines.
                    The specific filing requirements (F&I training records, complaint logs, disclosure audits) and deadline create urgency to stay compliant and avoid breach penalties.
- **Why this works**: Specific deadline (June 15, 2025) they need to hit. The required documentation list is helpful and actionable.
                    Easy question about internal ownership. Genuinely useful reminder that helps them avoid compliance penalties.
- **Data Sources**:
  - FTC Enforcement Actions Database - dealership_name, violation_type, settlement_terms, compliance_requirements, date
- **Outreach Message template**:
  ```text
  Subject: Your next FTC filing due June 15, 2025
  
  Your FTC consent order requires a quarterly compliance report by June 15, 2025.
  
  The submission must include F&I training records, customer complaint logs, and service contract disclosure audits.
  
  Is someone compiling the required documentation?
  ```

#### Play: FTC Enforcement Action Compliance Through 2027 (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Identify dealerships under FTC consent orders for warranty violations requiring ongoing compliance monitoring through future dates (e.g., March 2027).
                    Missing quarterly compliance filings triggers breach notification and potential additional penalties, creating ongoing administrative burden.
- **Why this works**: Specific compliance deadline (March 2027) is real and the dealer needs to track it. Easy routing question.
                    Factual without being accusatory. Helps them stay organized around regulatory obligations.
- **Data Sources**:
  - FTC Enforcement Actions Database - dealership_name, violation_type, settlement_terms, compliance_requirements, date
- **Outreach Message template**:
  ```text
  Subject: FTC compliance reports due quarterly through 2027
  
  Your dealership's March 2024 FTC consent order requires quarterly compliance reports through March 2027.
  
  Missing a filing triggers breach notification and potential penalties.
  
  Is someone calendaring the next submission deadline?
  ```

---

## Zywave (zywave.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/zywave-com)
**Strategic Summary**: Playbook uses NIPR producer license records and job posting velocity to identify multi-state insurance agencies facing simultaneous license renewal pressure and hiring surges that create compliance coordination risk.

### ✓ The New Way: GTM Plays

#### Play:  (STRONG PQS |  - Good (7.6/10))

- **What's the play?**: Who This Targets: Independent insurance agencies operating in 5+ states with 40+ producers and active hiring (3+ job postings in 60 days).
                        
                        The Trigger Event: High volume of producer license expirations (15%+ of total licenses expiring within 90 days) coinciding with rapid hiring creates compliance coordination chaos. Multi-state agencies must manage different CE requirements, renewal windows, and carrier appointment protocols across jurisdictions while onboarding new producers who need immediate licensing.
                        
                        Why This Hurts: License lapses suspend producers from writing business, creating revenue loss and client service disruptions. E&O insurance claims spike when agencies fail to track renewal requirements properly. Hiring surges compound the problem because compliance teams are simultaneously coordinating renewals AND processing new producer appointments.
                    

                    
                        Why This Message Works (Buyer Critique: 7.6/10)
                        Situation Recognition (8/10): Hyper-specific with exact license counts (47), date ranges, and state-by-state breakdown. If accurate, this perfectly mirrors the operations manager's current situation.
                        Data Credibility (7/10): NIPR license data is authoritative and verifiable. Job posting counts are observable. Slight concern about data freshness since NIPR requires paid subscription.
                        Insight Value (7/10): The state-by-state expiration calendar is genuinely useful—most ops managers don't have this consolidated view. The connection between hiring surge and renewal coordination is logical but somewhat obvious.
                        Effort to Reply (9/10): Dead simple yes/no question: "Want the full expiration calendar?"
                        Emotional Resonance (7/10): Triggers concern if the recipient doesn't have renewals well-organized. Creates curiosity about how the sender obtained this specific data.
- **Why this works**: 

#### Play:  (STRONG PQS |  - Good (7.6/10))

- **What's the play?**: Who This Targets: Insurance agencies experiencing measurable growth (30%+ review velocity increase year-over-year) while hiring rapidly (5+ positions in 90 days).
                        
                        The Trigger Event: Sharp increase in Google review velocity (observable proxy for client growth) combined with active producer hiring signals operational scale pressure. When agencies run separate platforms for core functions (AMS, CRM, compliance), growth amplifies system fragmentation costs exponentially.
                        
                        Why This Hurts: Every new hire must learn 3+ different systems before becoming productive, extending time-to-first-commission from 30 days to 60-90 days. Client data lives in silos, preventing cross-sell opportunities and creating service gaps. Compliance tracking failures increase as volume overwhelms manual processes.
                    

                    
                        Why This Message Works (Buyer Critique: 7.6/10)
                        Situation Recognition (8/10): Specific and verifiable—47% review growth with exact counts (83 vs 56) that the recipient can immediately check in their Google Business Profile.
                        Data Credibility (8/10): Google Maps review data is directly verifiable and authoritative. The YoY comparison is compelling evidence of growth.
                        Insight Value (7/10): The connection between client growth signals (reviews) and operational system strain is logical and relevant. Not revolutionary, but useful for ops managers focused on scaling infrastructure.
                        Effort to Reply (8/10): Simple question about onboarding process—easy to answer with 1-2 sentences.
                        Emotional Resonance (7/10): Resonates strongly if the agency is actually feeling growth pains. Creates validation that their operational struggles are visible in external data.
- **Why this works**: 

#### Play:  (STRONG PQS |  - Good (7.2/10))

- **What's the play?**: Who This Targets: Agencies with 50+ producers operating in 6+ states.
                        
                        The Trigger Event: Large volume of licenses (40+) expiring within 90 days across multiple jurisdictions, each with different continuing education (CE) requirements, renewal windows, and carrier appointment protocols.
                        
                        Why This Hurts: Compliance teams at multi-state agencies spend 15-20 hours per month manually coordinating renewals—tracking CE completion across different state portals, managing staggered renewal deadlines, and ensuring carrier appointments remain active. During hiring surges, this coordination load compounds as new producers need expedited appointments.
                    

                    
                        Why This Message Works (Buyer Critique: 7.2/10)
                        Situation Recognition (8/10): Specific license counts, state count, and time window are verifiable and concrete.
                        Data Credibility (8/10): CE requirements are publicly documented state regulations. License data from NIPR is authoritative.
                        Insight Value (6/10): The recipient likely already knows CE requirements vary by state—this is their daily reality. The connection between jurisdictional complexity and tracking burden is somewhat obvious to operations managers.
                        Effort to Reply (8/10): Simple question about current tracking methods.
                        Emotional Resonance (6/10): Mildly relatable but not particularly urgent or novel.
- **Why this works**: 

#### Play:  (STRONG PQS |  - Good (7.0/10))

- **What's the play?**: Who This Targets: Growing agencies posting 5+ producer positions in 90 days while running 3+ separate systems for core functions.
                        
                        The Trigger Event: Rapid hiring pace combined with fragmented technology stack (separate AMS, CRM, compliance platforms) creates onboarding complexity that extends time-to-productivity.
                        
                        Why This Hurts: Each new producer needs 15-20 hours of system training spread across 3+ platforms before they can effectively manage client relationships and write business. Agencies with integrated platforms onboard producers in half the time, creating competitive disadvantage. During high-velocity hiring periods, training bandwidth becomes a bottleneck.
                    

                    
                        Why This Message Works (Buyer Critique: 7.0/10)
                        Situation Recognition (7/10): Specific hire count (5 in 90 days) and system count (3) if detection is accurate. Some uncertainty around tech stack detection accuracy.
                        Data Credibility (6/10): Job postings are verifiable. Tech stack detection is less certain—may not capture internal systems, and detection tools aren't 100% accurate.
                        Insight Value (7/10): The connection between system count and onboarding complexity is logical. The 15-20 hours training estimate provides useful context for quantifying the problem.
                        Effort to Reply (8/10): Easy question about current onboarding process.
                        Emotional Resonance (7/10): Resonates if the agency is actually struggling with onboarding during rapid hiring. Less impactful if they've already addressed this pain point.
- **Why this works**: 

---

