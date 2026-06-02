# GTM Playbooks: Retail &amp; eCommerce

Curated list of data-driven GTM Playbooks for the **Retail &amp; eCommerce** vertical. Use these to brainstorm messaging, trigger events, and PVP angles.

---

## AutoSigma (autosigma.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/autosigma-com)
**Strategic Summary**: The playbook scrapes dealer inventory and pricing across all locations to audit multi-store offer consistency, and benchmarks promotional update velocity against aggregated peer dealerships to show lag versus the competitive market.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline Your Dealership Marketing

Hi [Name],

I noticed your dealership has been expanding - congrats on the growth! I wanted to reach out because AutoSigma helps dealerships like yours save time on marketing asset creation.

We work with top dealership groups to deploy promotional campaigns 4x faster. Our platform syndicates offers across all your channels automatically, keeping your messaging consistent.

Would you be open to a quick 15-minute call to discuss how we can help [Dealership Name] accelerate campaign deployment?

Looking forward to connecting!

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Built 3-Store Offer Sync Audit (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Scrape dealer pricing across all their locations and identify instances where identical vehicles show different pricing or terms. Deliver the completed audit before asking for anything.
- **Why this works**: You've already done the work. The prospect gets immediate value - a pricing conflict report they can use today to fix internal inconsistencies. The specificity (14 instances, 6 cases over $500 variance) proves this isn't generic research.
- **Data Sources**:
  - Dealer website inventory and pricing pages (scraped)
  - Internal AutoSigma platform data (if available for multi-location variance detection)
- **Outreach Message template**:
  ```text
  Subject: Built you a 3-store offer sync audit
  
  Pulled your current offers across Norman, Edmond, and Tulsa - found 14 instances where identical vehicles show different terms.
  
  This includes 6 cases where the variance exceeds $500 on the same VIN class.
  
  Want me to send the audit spreadsheet?
  ```
- **Data Requirement**: This play requires scraping dealer website pricing across multiple locations and identifying variance by VIN/trim level.
                    Combined with internal platform data to detect patterns. This synthesis is proprietary to your business.

#### Play: Promotional Velocity Laggards vs Peer Groups (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Use aggregated campaign deployment metrics from your customer base to show prospects exactly how their offer update frequency compares to peer dealerships of similar size, geography, and franchise type.
- **Why this works**: Dealerships operate in competitive local markets. Showing them they're updating offers 40% slower than peers (18 days vs 11 days) creates urgency - they're losing competitive positioning every cycle. The peer comparison is data they cannot get elsewhere.
- **Data Sources**:
  - AutoSigma Internal Platform Data - campaign deployment timestamps, offer update frequency by dealership
- **Outreach Message template**:
  ```text
  Subject: You're updating offers 40% slower than peers
  
  Based on promotional velocity data, your dealership updates offers every 18 days vs the 11-day average for Oklahoma dealer groups your size.
  
  That's 7 extra days competitors are running fresh offers while yours go stale.
  
  Want to see the velocity breakdown by channel?
  ```
- **Data Requirement**: This play requires aggregated promotional update frequency across 20+ dealerships, segmented by size, geography, and franchise type.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: OEM Launch Timeline Analysis (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Track the prospect's historical performance on OEM asset deployment deadlines over their last 6-8 model launches. Show them the pattern: they're systematically missing deadlines by an average of 9 days, indicating an approval bottleneck.
- **Why this works**: You're offering diagnostic data they likely don't track themselves. Showing a pattern (4 of 6 missed deadlines) reframes the problem from "bad luck" to "systematic bottleneck" - which has a fix. The analysis is already done; they just need to see it.
- **Data Sources**:
  - AutoSigma Internal Platform Data - OEM asset deployment timestamps, approval workflow tracking
  - OEM manufacturer launch calendars (public)
- **Outreach Message template**:
  ```text
  Subject: Tracked your last 8 OEM launches
  
  Analyzed your last 8 model year launches - average time from OEM asset drop to live deployment is 14 days vs 6-day dealer group average.
  
  That's costing you 8 days of first-mover advantage on every single launch.
  
  Want the launch timeline breakdown?
  ```
- **Data Requirement**: This play requires tracking customer OEM launch timelines and benchmarking against peer performance over multiple launches.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Memorial Day Launch Timing Gap (PVP                     Internal Data | Strong - Strong (8.9/10))

- **What's the play?**: Track when the prospect launched their holiday sale campaigns compared to peer dealerships. Show them they were 12 days late on Memorial Day, missing the peak shopping window and losing 40-60 potential units.
- **Why this works**: Holiday campaigns are massive revenue drivers. Quantifying the late launch in lost units (40-60) makes the opportunity cost concrete. Offering Q3 holiday timeline data turns this into forward-looking value - they can fix it for the next cycle.
- **Data Sources**:
  - AutoSigma Internal Platform Data - campaign launch dates by dealership
  - Peer benchmark data from comparable dealership groups
- **Outreach Message template**:
  ```text
  Subject: Your Memorial Day launch was 12 days late
  
  Your Memorial Day sale went live May 29th - the average Oklahoma dealer launched May 17th, capturing 12 extra selling days.
  
  That's potentially 40-60 lost units based on typical holiday conversion rates.
  
  Want the launch timeline data for Q3 holidays?
  ```
- **Data Requirement**: This play requires tracking campaign launch dates across dealerships and identifying late launchers vs peer benchmarks.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Pricing Conflict Identification Across Locations (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Scrape all dealership locations' inventory and pricing, then flag cases where identical models show mismatched lease/finance terms. Highlight internal cannibalization (one location undercutting another).
- **Why this works**: Pricing conflicts across locations are embarrassing and costly - they erode customer trust and create internal competition. The specificity (9 conflicts, OKC undercutting Norman by $1,200+) proves you did the work. You're just offering to send the results.
- **Data Sources**:
  - Dealer website inventory and pricing pages (scraped)
  - AutoSigma internal platform data (if available for multi-location pricing monitoring)
- **Outreach Message template**:
  ```text
  Subject: Found 9 pricing conflicts across your stores
  
  Scraped your 4 locations yesterday - found 9 vehicle models where lease/finance terms don't match despite identical inventory.
  
  Including 2 cases where your OKC store undercuts Norman by $1,200+ on the same trim.
  
  Want the conflict list?
  ```
- **Data Requirement**: This play requires scraping dealer website pricing across locations and identifying internal pricing conflicts by VIN/trim.
                    Combined with internal platform data to monitor multi-location pricing consistency. This synthesis is proprietary to your business.

#### Play: OEM Launch Asset Deadline Violation - Tahoe (PQS                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Monitor OEM manufacturer launch calendars and cross-reference with dealer website/digital channel asset updates. Identify dealerships that missed the OEM-mandated launch deadline and are still showing outdated assets.
- **Why this works**: OEM compliance is a massive pressure point for franchised dealers. Missing a deadline by 11 days is embarrassing and risks co-op reimbursement. Being singled out as one of 3 Oklahoma metro dealers still behind creates urgency - they're publicly lagging.
- **Data Sources**:
  - OEM manufacturer launch calendars (public from manufacturer franchise documents)
  - Dealer website asset verification (manual check or scraping)
- **Outreach Message template**:
  ```text
  Subject: Your Tahoe assets 11 days behind schedule
  
  GM mandated March 15th launch assets for the 2025 Tahoe refresh - your site still shows 2024 imagery as of March 26th.
  
  That's 11 days past the OEM deadline and you're one of 3 Chevy dealers in Oklahoma metro still behind.
  
  Who's handling the asset approvals?
  ```

#### Play: OEM Compliance Deadline Performance Pattern (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Track the prospect's OEM compliance performance over their last 6 launches. Show them they missed 4 of 6 deadlines by an average of 9 days - indicating a systematic approval bottleneck, not random failures.
- **Why this works**: Reframing repeated failures as a "systematic bottleneck" vs "bad luck" shifts the conversation to solutions. The timeline analysis is diagnostic data they likely don't track themselves. You're offering to help them fix the root cause.
- **Data Sources**:
  - AutoSigma Internal Platform Data - OEM asset deployment timestamps, deadline compliance tracking
  - OEM manufacturer launch calendars (public)
- **Outreach Message template**:
  ```text
  Subject: Mapped your last 6 OEM compliance deadlines
  
  Pulled your last 6 OEM asset deadlines vs actual deployment dates - you missed 4 of 6 by an average of 9 days.
  
  That pattern suggests a systematic approval bottleneck, not just bad luck.
  
  Want the timeline analysis?
  ```
- **Data Requirement**: This play requires tracking customer OEM compliance performance over time and identifying patterns of deadline misses.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: OEM Launch Deadline Violation - F-150 (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Track OEM manufacturer launch deadlines and verify dealer digital channels still show placeholder or outdated content 8+ days after the deadline. Flag the co-op reimbursement penalty risk.
- **Why this works**: Combining OEM deadline pressure with financial risk (co-op penalty) creates urgency. The 8-day delay is specific and verifiable. Asking "Is someone already working the approval backlog?" frames this as a helpful check-in, not a sales pitch.
- **Data Sources**:
  - OEM manufacturer launch calendars (public from Ford franchise documents)
  - Dealer website and digital channel asset verification (manual check or scraping)
- **Outreach Message template**:
  ```text
  Subject: Ford flagged your F-150 launch delay
  
  Ford's April 1st launch deadline for 2025 F-150 marketing assets passed 8 days ago - your digital channels still show placeholder content.
  
  That puts you at risk for Q2 co-op reimbursement penalties.
  
  Is someone already working the approval backlog?
  ```

#### Play: Promotional Offer Volume Gap vs Peers (PVP                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: Track the total number of promotional offers deployed by the prospect vs peer dealerships in the same quarter. Show them they deployed 8 offers while peers averaged 14 - that's 6 fewer chances to capture in-market buyers.
- **Why this works**: Promotional volume is a proxy for market presence. Deploying 6 fewer offers than peers means 6 fewer opportunities to capture buyers actively shopping. Offering a gap analysis (which offer types they're missing) turns this into actionable intelligence.
- **Data Sources**:
  - AutoSigma Internal Platform Data - promotional campaign count by dealership and quarter
- **Outreach Message template**:
  ```text
  Subject: Your Q1 offer count: 8 vs peer average of 14
  
  You deployed 8 promotional offers in Q1 while comparable Oklahoma dealer groups averaged 14.
  
  That's 6 fewer chances to capture in-market buyers with timely incentives.
  
  Want to see which offer types you're missing?
  ```
- **Data Requirement**: This play requires tracking promotional campaign frequency across dealerships and benchmarking volume by quarter.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Multi-Location Pricing Variance - Different Silverado Offers (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Scrape all dealer group locations and identify cases where the same vehicle model shows different rebate amounts or promotional terms across locations. Surface the customer confusion angle.
- **Why this works**: Pricing inconsistency is embarrassing and erodes customer trust. The specificity (3 locations, Silverado 1500, $2,500 vs $3,000 vs $2,200 rebates) proves you did the research. Customers calling corporate about the variance makes it urgent.
- **Data Sources**:
  - Dealer website inventory and promotional offer pages (scraped across all locations)
- **Outreach Message template**:
  ```text
  Subject: 3 different Silverado offers live right now
  
  Your Tulsa, Norman, and OKC stores are all running different Silverado 1500 offers - $2,500 vs $3,000 vs $2,200 rebates.
  
  Customers calling corporate are asking why the same truck costs different amounts at your locations.
  
  Is someone already standardizing these?
  ```

#### Play: OEM Launch Deadline Violation - Honda Accord (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Track Honda OEM launch deadlines and verify dealer digital channels (website, Google Ads) still show 2024 model imagery 28 days after the 2025 Accord asset deadline. Flag the lost search traffic opportunity.
- **Why this works**: 28 days late is brutally specific and verifiable. Framing the delay as "missing new model search traffic" ties it to lost revenue - competitors are capturing buyers searching for the 2025 model. The question "Is the approval process stuck?" is helpful, not salesy.
- **Data Sources**:
  - OEM manufacturer launch calendars (public from Honda franchise documents)
  - Dealer website and Google Ads asset verification (manual check or scraping)
- **Outreach Message template**:
  ```text
  Subject: Your 2025 Accord assets still pending
  
  Honda's March 1st asset deadline for 2025 Accord passed 28 days ago - your site and Google Ads still show 2024 model imagery.
  
  You're missing the new model search traffic spike while competitors capture it.
  
  Is the approval process stuck somewhere?
  ```

#### Play: Multi-Location Pricing Variance - Same Yukon Config (PQS                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Scrape dealer group websites and identify cases where the exact same vehicle configuration shows different monthly pricing across locations. Surface the trust erosion angle - customers calling to ask which price is real.
- **Why this works**: Very specific - same vehicle, exact amounts ($847/mo vs $974/mo). The customer trust angle resonates because inconsistent pricing damages brand reputation. Offering to send the variance report is a low-commitment ask.
- **Data Sources**:
  - Dealer website inventory and pricing pages (scraped)
  - AutoSigma internal platform data (if available for real-time pricing monitoring)
- **Outreach Message template**:
  ```text
  Subject: Your Yukon pricing varies by $127/month
  
  Same 2025 Yukon Denali config shows $847/mo in Norman and $974/mo in Edmond as of today.
  
  Customers are calling asking which price is real - this erodes trust across your brand.
  
  Should I send you the variance report?
  ```
- **Data Requirement**: This play requires real-time monitoring of dealer pricing across locations to detect inconsistencies by VIN/config.
                    Combined with internal platform data to verify variance patterns. This synthesis is proprietary to your business.

#### Play: Multi-Location Pricing Variance - Norman vs Edmond (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Scrape dealer group websites and identify cases where the same vehicle model shows different lease pricing across locations. Surface the customer confusion angle - they're cross-shopping your stores and getting different prices.
- **Why this works**: Specific to their dealerships - Norman vs Edmond locations, 2025 Camry, $299 vs $349. The customer confusion angle hits home because inconsistent pricing costs deals. The routing question is easy to answer.
- **Data Sources**:
  - Dealer website inventory and pricing pages (scraped)
  - AutoSigma internal platform data (if available for multi-location pricing monitoring)
- **Outreach Message template**:
  ```text
  Subject: Your 3 locations showing different pricing this week
  
  Your Norman location shows $299/mo lease on the 2025 Camry while Edmond shows $349 for the same trim.
  
  That's confusing customers cross-shopping your stores and likely costing you deals.
  
  Who's managing offer consistency across locations?
  ```
- **Data Requirement**: This play requires monitoring dealer website pricing across multiple locations to detect variance by vehicle trim.
                    Combined with internal platform data to identify multi-location pricing inconsistencies. This synthesis is proprietary to your business.

#### Play: Holiday Campaign Late Launch - July 4th (PQS                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: Track when the prospect launched their July 4th sale compared to peer dealerships. Show them they went live 22 days late (June 27th vs peer average June 5th), missing the entire pre-holiday shopping window.
- **Why this works**: Holiday campaigns are revenue drivers. Launching 22 days late means missing the peak shopping window - the comparison to peers makes the gap concrete. The routing question is low-pressure and easy to answer.
- **Data Sources**:
  - AutoSigma Internal Platform Data - campaign launch dates by dealership
- **Outreach Message template**:
  ```text
  Subject: You took 22 days to launch July 4th sale
  
  Your July 4th event went live June 27th - peer dealers launched June 5th, capturing 22 extra pre-holiday selling days.
  
  That's the entire peak shopping window for that holiday.
  
  Who manages the promotional calendar?
  ```
- **Data Requirement**: This play requires tracking campaign launch timing across customers and identifying late launchers vs peer benchmarks.
                    This is proprietary data only you have - competitors cannot replicate this play.

---

## Bevz (bevz.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/bevz-com)
**Strategic Summary**: The playbook uses state liquor license databases and TTB COLA registry to identify newly licensed stores and cross-reference competitive craft beer SKU counts within 0.8 miles of the prospect&#x27;s location.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your alcohol delivery operations

Hi [First Name],

I noticed your store is now on DoorDash - congrats on the expansion!

Managing orders across multiple platforms can be challenging. Bevz helps independent liquor stores like yours consolidate delivery management, sync menus automatically, and reduce order errors.

Would you be open to a quick call to discuss how we're helping stores increase delivery revenue by 30%?

Best,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: New License + Vendor Intelligence (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: When new liquor stores receive their license approval, immediately deliver a curated list of local craft distributors who already service their ZIP code - including the exact products their nearest competitors stock and minimum order quantities.
                    This combines state license database timing signals with proprietary distributor network data and competitive product intelligence to accelerate the new store's launch.
- **Why this works**: New license holders are in launch mode - they need to stock inventory fast. Providing complete vendor contacts with MOQs and proven local product mix eliminates weeks of sourcing work.
                    The specificity (8 distributors in their exact ZIP, 5 carrying the top 12 SKUs from nearby competitors) proves you've done homework they'd otherwise pay a consultant to do.
- **Data Sources**:
  - State Liquor License Databases - license approval date, address, license type
  - TTB COLA Registry - approved alcohol products by brand and type
  - Internal Distributor Network Data - distributor coverage by ZIP, contact info, MOQs
  - Internal Customer Inventory Data - product mix by SKU category for similar stores
- **Outreach Message template**:
  ```text
  Subject: Craft beer vendors active in your ZIP
  
  Your license approved November 18th - I pulled 8 craft distributors already servicing your ZIP code (78701).
  
  Five of them stock the top 12 craft SKUs your three nearest competitors carry.
  
  Want their contact info and minimum order quantities?
  ```
- **Data Requirement**: This play requires distributor partnership data showing coverage by ZIP code, plus inventory data from existing customers showing which products move fastest in specific geographies.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: New License + Inventory Gap Detection (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Target newly-licensed liquor stores within 48 hours of license approval and surface competitive intelligence about nearby stores' product mix - specifically identifying gaps in the new store's planned inventory.
                    This combines real-time license approval tracking with competitive product intelligence to help new stores avoid launch mistakes.
- **Why this works**: The exact license approval date and address prove you're monitoring their specific situation in real-time. Telling them "three competitors within 0.8 miles stock 12+ craft beer SKUs" when they planned zero craft inventory creates immediate urgency.
                    New license holders are making critical inventory decisions RIGHT NOW. Pointing out a blind spot with specific competitive data (not generic advice) makes you the person who prevented a costly mistake.
- **Data Sources**:
  - State Liquor License Databases - license approval date, address, license type, planned inventory (from application)
  - Internal Customer Inventory Data - product mix by SKU category for nearby competitors
  - Geographic Proximity Analysis - competitor mapping within radius
- **Outreach Message template**:
  ```text
  Subject: Your new license approved - craft beer gap?
  
  Your alcohol license at 456 Commerce St was approved November 18th.
  
  Three competitors within 0.8 miles stock 12+ craft beer SKUs - your application shows zero craft inventory planned.
  
  Who's handling your initial product mix decisions?
  ```
- **Data Requirement**: This play requires inventory data from existing retailer customers showing product mix by SKU category, combined with geographic competitor mapping.
                    Public license data + your proprietary inventory intelligence creates this insight.

---

## CarFluent (car-fluent.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/car-fluent-com)
**Strategic Summary**: The playbook uses US Census Bureau Hispanic population data and Google Maps review language detection to identify dealerships with Spanish-speaking customer presence but no bilingual digital capabilities, combined with competitor bilingual site analysis.

### ✓ The New Way: GTM Plays

#### Play:  (PQS |  - Good (7.2/10)
                

                Target dealerships in counties with rapid Hispanic population growth (15%+ increase over 5 years) that still have English-only websites. These dealers are missing a growing market opportunity that competitors may be capturing.

                
                    Why This Works
                    Buyer Perspective (7.2/10):
                    
                        Situation Recognition (8/10): ZIP code specificity makes it feel tailored to their location
                        Data Credibility (8/10): Census data is authoritative and verifiable
                        Insight Value (7/10): Absolute number (620k) and ZIP-level data is more concrete than county averages
                        Effort to Reply (7/10): Question connects to their observable reality (foot traffic vs online leads)
                        Emotional Resonance (6/10): Creates curiosity about market opportunity
                    
                    Texada Test: ✅ Hyper-specific (exact ZIP, exact growth %), ✅ Factually grounded (Census API), ✅ Non-obvious (ZIP-level growth rate not commonly known))

- **What's the play?**: 
- **Why this works**: 

#### Play:  (PQS |  - Good (7.0/10)
                

                Target dealerships in high-Hispanic counties where competitors have recently launched bilingual websites, creating competitive disadvantage for English-only dealers.

                
                    Why This Works
                    Buyer Perspective (7.0/10):
                    
                        Situation Recognition (7/10): Specific competitor count and county data, but many dealers get competitive intel pitches
                        Data Credibility (8/10): Census data + competitor websites are both verifiable
                        Insight Value (6/10): Useful if dealer isn't tracking competitors closely, but may already know
                        Effort to Reply (9/10): Easy yes/no question
                        Emotional Resonance (5/10): Competitive threat creates some urgency, but depends on dealer's awareness
                    
                    Texada Test: ✅ Hyper-specific (exact county %, competitor count), ✅ Factually grounded (Census + observable websites), ⚠️ Non-obvious (competitor sites may be known to dealer))

- **What's the play?**: 
- **Why this works**: 

#### Play:  (PQS |  - Good (7.4/10)
                

                Target high-volume dealerships (100+ Google reviews) where significant percentage of reviews are in Spanish, indicating Spanish-speaking customer base, yet the dealership website remains English-only. This reveals both customer presence AND unmet accessibility need.

                
                    Why This Works
                    Buyer Perspective (7.4/10):
                    
                        Situation Recognition (8/10): Review analysis is specific to their dealership, not generic demographic data
                        Data Credibility (7/10): Google review counts are verifiable, language detection is checkable
                        Insight Value (7/10): Dealer hasn't analyzed review language - this is non-obvious synthesis
                        Effort to Reply (9/10): Easy yes/no question
                        Emotional Resonance (6/10): Creates curiosity - "I didn't know that about my reviews"
                    
                    Texada Test: ✅ Hyper-specific (exact review counts from THEIR business), ✅ Factually grounded (Google reviews public), ✅ Non-obvious (review language analysis not commonly done))

- **What's the play?**: 
- **Why this works**: 

#### Play:  (PQS |  - Good (7.0/10)
                

                Highlight the statistical gap between Spanish review percentage and county Hispanic population percentage to signal potential market underservice or friction in the buying process for Spanish-speaking customers.

                
                    Why This Works
                    Buyer Perspective (7.0/10):
                    
                        Situation Recognition (7/10): Specific to their review data
                        Data Credibility (7/10): Numbers verifiable, interpretation disclosed with "may signal"
                        Insight Value (7/10): Gap between review % and demographics is interesting finding
                        Effort to Reply (7/10): Connects to internal data they can check
                        Emotional Resonance (6/10): Triggers curiosity about market opportunity
                    
                    Texada Test: ✅ Hyper-specific (exact percentages), ✅ Factually grounded (with proper qualifiers), ✅ Non-obvious (review language analysis + demographic comparison))

- **What's the play?**: 
- **Why this works**: 

---

## Circana (circana.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/circana-com)
**Strategic Summary**: Playbook uses internal POS velocity data, competitive launch tracking, retailer pricing feeds, and promotional calendar intelligence to alert CPG brands when competitors launch price-undercut SKUs in their shelf sets with quantified share capture risk.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Unlock Real-Time Consumer Insights

Hi [FirstName],

I noticed your company is focused on retail analytics. At Circana, we help brands like yours gain visibility into consumer demand and optimize supply chain performance.

Our AI-powered platform provides real-time insights across channels, enabling better demand forecasting and inventory management.

Would you be open to a quick 15-minute call to explore how we can help you reduce stock-outs and improve margin?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Competitive Launch Collision: Nestle Pricing Attack (PVP                     Public + Internal | Strong - Strong (9.6/10))

- **What's the play?**: Alert CPG brands when competitors launch similar products at their shared retailers with aggressive pricing, then provide tactical counter-recommendations based on historical promotional lift data.
- **Why this works**: This is the intelligence every brand wishes they had but can't get anywhere else. You're not just warning about a competitive threat - you're quantifying the share risk and providing the exact playbook to defend it. The specificity (competitor name, SKU count, pricing gap, predicted share loss) proves you're not guessing.
- **Data Sources**:
  - New product launch tracking database
  - Retailer pricing feeds
  - Historical launch impact models
  - Shelf set placement intelligence
- **Outreach Message template**:
  ```text
  Subject: Nestle launching 2 SKUs in your shelf set April
  
  Nestle is launching 2 new SKUs in your shelf set at Target starting April 8th - both priced $0.40 below your current SKUs.
  
  Based on similar launches, they'll capture 12-18% category share in the first 8 weeks unless you respond.
  
  Should I send the recommended pricing and promotion counter-moves?
  ```
- **Data Requirement**: This play requires new product tracking, retailer pricing feeds, historical launch impact modeling, and shelf set placement intelligence from your platform.
                    This level of competitive intelligence synthesis is unique to Circana - competitors cannot replicate this play.

#### Play: Price Gap Defense: Unilever Walmart Entry (PVP                     Public + Internal | Strong - Strong (9.7/10))

- **What's the play?**: Identify when competitors enter with significant price undercutting, quantify the share capture risk using historical price-gap models, and offer strategic pricing options.
- **Why this works**: Pricing decisions involve massive margin implications. Showing the exact dollar gap ($0.75), the timeline (April 2nd), and the modeled share loss (25-30%) gives them everything needed to make an informed decision. The offer to see "pricing strategy options I modeled" positions you as strategic advisor, not vendor.
- **Data Sources**:
  - New product launch tracking
  - Retailer pricing feeds
  - Historical price-gap impact modeling
  - Share capture analysis
- **Outreach Message template**:
  ```text
  Subject: Unilever pricing $0.75 below you in April
  
  Unilever is launching a direct substitute to your SKU at Walmart on April 2nd priced at $4.25 vs your $5.00.
  
  Based on similar $0.75 gaps, they'll capture 25-30% category share in 8 weeks without a pricing or value-pack response.
  
  Want the pricing strategy options I modeled?
  ```
- **Data Requirement**: Requires new product launch tracking, retailer pricing intelligence, historical price-gap impact modeling, and predictive share capture analysis.
                    This pricing intelligence and predictive modeling is proprietary to Circana's platform.

#### Play: Promotional Calendar Gap: General Mills Safeway (PVP                     Public + Internal | Strong - Strong (9.5/10))

- **What's the play?**: Cross-reference competitive promotional calendars with recipient's planned promotions to identify timing gaps that will cause them to lose market share during critical launch windows.
- **Why this works**: Promotional planning is done quarters in advance. Surfacing a 3-week gap between their competitor's BOGO launch and their own promotional calendar gives them time to fix it. The specificity (BOGO, weeks 1-3, February 25th launch vs March 15th response) makes the vulnerability undeniable.
- **Data Sources**:
  - New product launch tracking
  - Retailer promotional calendar intelligence
  - Recipient's promotional schedule analysis
- **Outreach Message template**:
  ```text
  Subject: General Mills launching against you February 25th
  
  General Mills is launching 3 SKUs in your yogurt category at Safeway on February 25th with BOGO promotion weeks 1-3.
  
  Your current promotional calendar shows no activity until March 15th - 3 weeks after their launch.
  
  Want the counter-promotion playbook with timing recommendations?
  ```
- **Data Requirement**: Requires competitive launch tracking, retailer promotional calendar partnerships, and analysis of recipient's promotional gaps.
                    Only Circana has visibility into both competitive launches and retailer promotional windows simultaneously.

#### Play: Competitive Launch Alert: Kellogg Kroger Promotion (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Monitor competitive product launches at shared retailers and alert brands when direct competitors enter with promotional pricing during periods when the recipient has no promotional activity scheduled.
- **Why this works**: Brands are blindsided by competitive launches all the time. Giving them advance notice (March 18th launch) with specific promotional details (15% discount, 4 weeks) and pointing out their vulnerability (no promo scheduled) creates urgency. The offer of a "counter-tactic playbook" positions you as the advisor who can help them defend.
- **Data Sources**:
  - Public product launch tracking
  - Retailer promotional calendar data
  - Recipient's promotional schedule analysis
- **Outreach Message template**:
  ```text
  Subject: Competitor launching in your category March 18th
  
  Kellogg's is launching a direct competitor to your granola SKU on March 18th at Kroger with 15% promotional discount for 4 weeks.
  
  Your current SKU has no promotional calendar scheduled during their launch window.
  
  Want the counter-tactic playbook we built?
  ```
- **Data Requirement**: Combines public product launch tracking, retailer promotional calendar intelligence from partnerships, and analysis of recipient's promotional schedule.
                    This synthesis of competitive intelligence is unique to Circana's platform coverage.

#### Play: New Product Launch: Velocity Curve Failure (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Track new SKU launches against historical velocity curve benchmarks and alert brands when their launch is tracking significantly below expected trajectory, diagnosing whether the gap is demand or execution.
- **Why this works**: New product launches represent massive investment. Brand teams are desperate to know if their launch is succeeding or failing in real-time, not 6 months later. Showing exact week tracking (week 8, 340 units vs 850 expected) with urgency framing (60% below curve, missing adoption window) creates immediate need for intervention.
- **Data Sources**:
  - Public product launch announcements
  - Circana POS velocity data
  - Historical launch curve benchmarks
- **Outreach Message template**:
  ```text
  Subject: Your February launch tracking 60% below curve
  
  Your new SKU launched February 12th is at week 8 with 340 units/week velocity - typical curve for this category shows 850 units/week by week 8.
  
  At 60% below expected curve, you're missing the critical adoption window before competitors respond.
  
  Want the velocity trend analysis with intervention recommendations?
  ```
- **Data Requirement**: Combines public product launch announcements with proprietary POS velocity tracking and historical launch curve benchmarks.
                    Only Circana has the historical launch data to build accurate velocity curve benchmarks across categories.

#### Play: Launch Failure: Distribution Not Promotion (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Compare new product distribution reach against category benchmarks and diagnose when limited distribution is capping velocity before promotional spend can be effective.
- **Why this works**: Brands often throw promotional dollars at struggling launches without realizing the root cause is distribution, not demand. Showing the exact distribution gap (2,200 stores vs 10,000 benchmark, 22% of target) and explaining why promotional spend won't work yet saves them wasted budget and redirects to the real fix.
- **Data Sources**:
  - Public store count data
  - Circana retailer distribution tracking
  - Historical launch distribution benchmarks
- **Outreach Message template**:
  ```text
  Subject: Your launch missing 78% of distribution target
  
  Your February launch is in 2,200 Target stores but category benchmarks show successful launches hit 10,000 stores by week 6 - you're at 22% of target distribution.
  
  Limited distribution is capping your velocity curve before promotional spend can work.
  
  Should I send the distribution gap analysis with expansion priorities?
  ```
- **Data Requirement**: Combines public store count data with retailer distribution tracking and historical launch success benchmarks for store expansion.
                    Circana's retailer partnerships provide distribution tracking that competitors cannot access.

#### Play: SKU Velocity Gap: Walmart Performance (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Use aggregated velocity data to show CPG brands exactly where their SKUs are underperforming category benchmarks at specific retailers, quantifying the weekly revenue loss.
- **Why this works**: Every SKU matters to brand performance. Showing exact velocity gap (127 vs 210 units/week) at a specific retailer (Walmart) with quantified dollar impact ($18K/week) makes the problem undeniable and urgent. The offer for "full velocity report across your top 6 SKUs" creates immediate value expansion opportunity.
- **Data Sources**:
  - Circana Internal POS Data - aggregated velocity by SKU, retailer, shelf set
  - Category benchmark database
- **Outreach Message template**:
  ```text
  Subject: Your SKU #4782 selling 40% below category
  
  Your SKU #4782 at Walmart is moving 127 units/week while category average is 210 units/week in that same shelf set.
  
  That's a 40% velocity gap costing you an estimated $18K/week in that single retailer.
  
  Want the full velocity report across your top 6 SKUs?
  ```
- **Data Requirement**: This play requires aggregated POS velocity data across retail partners with SKU-level granularity and category benchmarks.
                    This is proprietary data synthesis only Circana has - the ability to benchmark a brand's velocity against category across major retailers.

#### Play: Velocity Decline: Competitive Entry Diagnosis (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Alert brands when their SKU velocity drops quarter-over-quarter at specific retailers and correlate the decline with competitive SKU entries on exact dates.
- **Why this works**: Velocity declines often happen gradually and go unnoticed until quarterly reviews. Showing exact decline (1,240 to 890 units/week, 28% drop) and connecting it to a specific competitive event (2 new SKUs on January 15th) turns a vague concern into an actionable diagnosis. The offer to show "which SKUs are capturing your velocity" positions you as the investigator who's already done the work.
- **Data Sources**:
  - Circana weekly POS velocity tracking
  - Historical velocity comparison database
  - New SKU launch monitoring at shelf-set level
- **Outreach Message template**:
  ```text
  Subject: Your velocity down 28% at Albertsons vs Q4
  
  Your top 5 SKUs at Albertsons dropped from 1,240 units/week average in Q4 to 890 units/week in January - that's a 28% velocity decline.
  
  That drop coincides with 2 new competitive SKUs entering your shelf set on January 15th.
  
  Want the competitive analysis showing which SKUs are capturing your velocity?
  ```
- **Data Requirement**: Requires weekly POS velocity tracking with historical comparison capability and new SKU launch monitoring at shelf-set level.
                    Circana's real-time velocity tracking combined with competitive SKU monitoring is proprietary to the platform.

#### Play: Launch vs Launch: Pattern Recognition (PVP                     Internal Data | Strong - Strong (8.9/10))

- **What's the play?**: Compare current product launch performance to the same brand's previous successful launch to identify replicable issues in pricing, distribution, or promotional strategy.
- **Why this works**: Using their own past success as the benchmark is more powerful than category averages. Showing exact week-over-week comparison (410 vs 920 units/week at week 6, 55% gap) makes the underperformance undeniable. Framing it as "replicable issues" rather than random failure suggests there's a fixable pattern.
- **Data Sources**:
  - Circana historical launch tracking for the same company
  - Velocity curves stored over time
- **Outreach Message template**:
  ```text
  Subject: Week 6 velocity 55% below your last launch
  
  Your March 3rd SKU launch is tracking 410 units/week at week 6 - your previous successful launch was at 920 units/week at the same point.
  
  That 55% gap suggests replicable issues from pricing, distribution depth, or promotional strategy.
  
  Should I send the side-by-side launch comparison?
  ```
- **Data Requirement**: Requires tracking of the same company's historical product launches with velocity curves stored longitudinally.
                    Only possible with Circana's multi-year tracking of brand launch performance across products.

#### Play: Shelf-Level Diagnosis: Wegmans Organic Line (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Use shelf-level velocity data to compare recipient's SKUs against adjacent products in the same shelf position, diagnosing pricing or packaging issues causing velocity gaps.
- **Why this works**: Comparing performance to adjacent shelf neighbors (not just category average) isolates execution issues. Showing exact velocity gap (340 vs 620 units/week) and identifying likely causes (pricing premium, packaging) demonstrates diagnostic capability. The offer for "shelf performance analysis with fix recommendations" positions you as problem-solver, not data vendor.
- **Data Sources**:
  - Circana POS data with shelf-level positioning intelligence
  - Retailer pricing feeds
  - Adjacent SKU performance benchmarks
- **Outreach Message template**:
  ```text
  Subject: Your SKU velocity 45% below at Wegmans
  
  Your organic line at Wegmans is moving 340 units/week while similar organic SKUs in adjacent shelf positions average 620 units/week.
  
  That 45% gap suggests either pricing ($0.60 premium vs neighbors) or packaging visibility issues.
  
  Want the shelf performance analysis with fix recommendations?
  ```
- **Data Requirement**: Requires POS data with shelf-level positioning intelligence, pricing feeds, and adjacent SKU performance benchmarks.
                    Circana's shelf-level granularity with pricing context is proprietary competitive intelligence.

#### Play: Multi-SKU Underperformance: Target Distribution (PVP                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: Identify when multiple SKUs from the same brand are tracking 35-50% below category benchmarks at a specific retailer, suggesting systemic pricing, placement, or promotional issues.
- **Why this works**: One underperforming SKU might be a product issue. Three underperforming SKUs at the same retailer (35-50% below benchmarks) signals a systemic execution problem that's fixable in Q1. The specificity (3 SKUs, Target, same shelf position) makes the pattern undeniable. Offering "SKU breakdown with recommended fixes" positions you as the diagnostic expert.
- **Data Sources**:
  - Circana retail POS data with category benchmarking
  - Shelf placement intelligence
- **Outreach Message template**:
  ```text
  Subject: 3 SKUs underperforming at Target stores
  
  Pulled velocity data for your Target distribution - 3 SKUs are tracking 35-50% below category benchmarks in the same shelf position.
  
  That velocity gap suggests either pricing, placement, or promotion issues fixable in Q1.
  
  Should I send the SKU breakdown with recommended fixes?
  ```
- **Data Requirement**: Requires retail POS data with category benchmarking capability and shelf placement intelligence.
                    Circana's ability to benchmark multiple SKUs simultaneously against category at specific retailers is proprietary.

#### Play: Launch Curve Diagnosis: Early Peak Problem (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Identify when new product launches peak earlier than category benchmarks and then decline, diagnosing promotional timing or distribution depth issues.
- **Why this works**: An early peak followed by decline (week 4 vs expected week 6-7) is a specific failure pattern that suggests fixable execution issues. Showing exact velocity (620 units/week) with expected timing (40% higher at week 6-7) demonstrates diagnostic capability. The offer for "diagnostic breakdown" positions you as the expert who understands what went wrong.
- **Data Sources**:
  - Public launch announcements
  - Circana weekly velocity tracking
  - Historical category launch curve benchmarks
- **Outreach Message template**:
  ```text
  Subject: Your January launch peaked at week 4 not week 6
  
  Your January 14th launch peaked at 620 units/week in week 4, then declined - category pattern shows peak should hit week 6-7 at 40% higher velocity.
  
  Early peak + decline suggests promotional timing or distribution depth issues.
  
  Should I send the diagnostic breakdown?
  ```
- **Data Requirement**: Combines public launch announcements with proprietary weekly velocity tracking and historical category launch curve benchmarks.
                    Only Circana has the historical launch data to identify early peak patterns across categories.

#### Play: Recall Supplier Vetting Gap (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Cross-reference FDA recall trace-back data with FSIS inspection records to identify food manufacturers whose March 2024 recalls traced to suppliers with prior non-compliance citations, revealing supplier vetting gaps.
- **Why this works**: This is forensic-level data synthesis. You're connecting their recall to suppliers who had red flags 6-18 months before the incident. The implication is clear: their supplier vetting process missed something obvious. The routing question ("Who owns supplier compliance audits now?") is easy to answer and creates urgency.
- **Data Sources**:
  - FDA Recall Database - recall date, contaminant, supplier trace-back
  - USDA FSIS Inspection Directory - supplier inspection history, non-compliance citations
- **Outreach Message template**:
  ```text
  Subject: 2 of your suppliers cited before your recall
  
  Cross-checked your March 2024 recall suppliers against FSIS inspection records - 2 had non-compliance citations 6-18 months prior.
  
  That pattern suggests your supplier vetting process missed red flags.
  
  Who owns supplier compliance audits now?
  ```

#### Play: Current Supplier Ongoing Violations (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Identify food manufacturers whose current suppliers (based on recall trace-back) have ongoing FSIS citations in the past 12 months, including recent violations within 6 weeks, creating immediate compliance risk.
- **Why this works**: This isn't about a past recall - it's about ongoing risk RIGHT NOW. Showing exact location (Tennessee processor), citation count (4 times in 12 months), and recency (6 weeks ago, sanitation violations) creates urgency. The routing question ("Is your quality team aware of their recent inspection history?") implies they might not be monitoring this proactively.
- **Data Sources**:
  - FDA Recall Database - supplier trace-back from past recalls
  - USDA FSIS Inspection Directory - ongoing citation history by facility
- **Outreach Message template**:
  ```text
  Subject: Your supplier in Tennessee cited 4 times
  
  One of your current ingredient suppliers (based on your March recall trace-back) is a Tennessee processor cited 4 times by FSIS in the past 12 months.
  
  Their last citation was 6 weeks ago for sanitation violations.
  
  Is your quality team aware of their recent inspection history?
  ```

#### Play: Recall Supplier Compliance Pattern (PQS                     Public Data | Strong - Okay (7.8/10))

- **What's the play?**: Identify FDA-regulated food manufacturers whose March 2024 recalls traced to 3 suppliers, where 2 of those suppliers had prior FSIS non-compliance citations in the 18 months before the recall.
- **Why this works**: This is highly specific public data synthesis across FDA and USDA databases. You're showing exact recall date (March 2024), contaminant (listeria), supplier count (3), and compliance pattern (2 had prior citations in 18 months). The routing question is easy to answer and creates urgency about current supplier auditing processes.
- **Data Sources**:
  - FDA Recall Database - recall date, contaminant type, supplier trace-back
  - USDA FSIS Inspection Directory - supplier compliance history, citation timing
- **Outreach Message template**:
  ```text
  Subject: Your March 2024 recall traced to 3 suppliers
  
  Your March 2024 FDA recall (listeria contamination) traced back to 3 ingredient suppliers in the FSIS database.
  
  Two of those suppliers had prior FSIS non-compliance citations in the 18 months before your recall.
  
  Is anyone auditing your current supplier compliance status?
  ```

---

## ComplyAuto (complyauto.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/complyauto-com)
**Strategic Summary**: Playbook uses OSHA Establishment Search and FTC Safeguards Rule breach notification database to identify dealerships approaching willful violation reclassification and those with permanent public breach records creating compounding regulatory and reputational risk.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Quick question about compliance

Hi Mike,

I noticed on LinkedIn that ABC Auto Group recently expanded to three new locations. Congrats on the growth!

I wanted to reach out because ComplyAuto works with dealerships like CarMax and AutoNation to help with compliance challenges across multiple regulatory areas.

Our platform automates compliance tracking, provides real-time reporting, and integrates with your existing systems. We've helped dealerships reduce compliance violations by 40% and save 20 hours per week on manual compliance tasks.

Would you have 15 minutes next week to explore how we might be able to help ABC Auto Group stay ahead of regulatory requirements?

Best,
Sarah
ComplyAuto
```

### ✓ The New Way: GTM Plays

#### Play: Play 1: OSHA Repeat Violations - Willful Classification Risk (PQS | Strong - Strong (9.2/10))

- **What's the play?**: Target auto dealerships with recent OSHA citations classified as "Repeat" violations - these dealerships are one violation away from "Willful" classification with 10x penalty increases.
                    These dealerships have documented safety compliance failures with escalating regulatory consequences.
- **Why this works**: You're referencing their specific OSHA inspection with exact citation number and date. They know they were cited, but the NON-OBVIOUS insight is the escalation path they may not have calculated.
                    "Repeat" violations automatically escalate to "Willful" on the third occurrence, jumping penalties from $15,625 to $156,259 per instance. Plus mandatory OSHA Severe Violator Enforcement Program (SVEP) enrollment with quarterly inspections for 3 years.
                    This isn't generic safety fear - it's THEIR facility, THEIR inspection timeline, THEIR escalation risk with specific dollar amounts they can verify.
- **Outreach Message template**:
  ```text
  Subject: Your OSHA Repeat status
  
  OSHA inspection #1598334 on November 18, 2025 cited your service department for fall protection violations (penalty: $43,200) - classified as "Repeat" since you had the same violation in 2023.
  
  That Repeat classification means your next identical violation automatically escalates to "Willful" status, jumping penalties to $156,259 per instance plus mandatory SVEP enrollment.
  
  How are you tracking daily fall protection compliance to avoid that third strike?
  ```

#### Play: Play 2: Data Breach Post-Breach Compliance Gap (PQS | Strong - Strong (9.0/10))

- **What's the play?**: Target dealerships with recent data breaches reported to the FTC (effective May 2024, breaches affecting 500+ customers with unencrypted data must be reported).
                    These dealerships are exposed in the PUBLIC FTC breach database with heightened FTC audit risk and class-action lawsuit vulnerability.
- **Why this works**: They know they had a breach, but the NON-OBVIOUS insights are: (a) breach notification is PERMANENT public record, (b) 3.2x higher class-action lawsuit probability within 24 months, (c) public database listing damages reputation when prospects Google them.
                    The FTC Safeguards Rule breach database is searchable online. This isn't just regulatory risk - it's reputational damage that affects sales.
                    Post-breach, they're under heightened scrutiny and must demonstrate remediation to avoid FTC enforcement action.
- **Outreach Message template**:
  ```text
  Subject: FTC breach record
  
  The public FTC breach database shows your [Location] dealership's August 2025 incident (847 unencrypted customer records compromised).
  
  Post-breach, you're 3.2x more likely to face class-action lawsuits within 24 months, and the public database listing amplifies reputational risk with prospects searching your dealership online.
  
  Want our post-breach compliance roadmap template?
  ```

#### Play: Play 3: OSHA Multi-Citation Pattern - Systemic Safety Failure (PQS | Strong - Strong (9.0/10))

- **What's the play?**: Target dealerships with multiple OSHA citations within 36 months showing a pattern of safety compliance failure.
                    These dealerships are on a trajectory toward Willful violations and OSHA Severe Violator Enforcement Program (SVEP) enrollment.
- **Why this works**: You're showing them a PATTERN they may not have calculated: two citations in 36 months for the same violation type puts them "one violation away" from Willful classification.
                    The NON-OBVIOUS insight is the enforcement escalation timeline. Two Willful violations trigger mandatory SVEP enrollment with quarterly OSHA inspections for 3 years - operational nightmare.
                    This message demonstrates you've analyzed their historical OSHA record and see the trajectory they're on.
- **Outreach Message template**:
  ```text
  Subject: Willful risk calculation
  
  Your facility's OSHA record shows two fall protection citations in 36 months (2023: $28,400, 2025: $43,200) - that pattern puts you one violation away from Willful classification.
  
  Willful violations carry $156,259 per instance, and two Willful violations trigger mandatory Severe Violator Enforcement Program (SVEP) enrollment with quarterly inspections for 3 years.
  
  Do you have automated daily safety compliance documentation in place?
  ```

#### Play: Play 4: FTC Safeguards Rule Post-Breach Audit Risk (PQS | Strong - Strong (8.8/10))

- **What's the play?**: Target dealerships with reported breaches showing specific customer counts and data types compromised.
                    Focus on breaches with unencrypted data (SSNs, financial information) that trigger FTC Safeguards Rule violations.
- **Why this works**: You're referencing their exact breach with specific customer count and data types. They know they had a breach, but the NON-OBVIOUS insights are the regulatory cascade: 65% FTC audit probability within 18 months + permanent public exposure.
                    The FTC Safeguards Rule breach notification requirement (effective May 2024) means their breach is PUBLIC RECORD. This creates both regulatory and reputational consequences.
                    Post-breach dealerships are in a compliance gap: they must demonstrate remediation to avoid FTC enforcement, but many lack the automated systems to prove ongoing compliance.
- **Outreach Message template**:
  ```text
  Subject: Your breach notification
  
  Your dealership reported a data breach to the FTC on [Date] affecting 1,247 customers' SSNs and financial data per the public Safeguards Rule notification database.
  
  That breach notification triggers FTC audit probability (65% within 18 months per compliance data), plus you're now exposed in the public breach database permanently.
  
  Have you completed the post-breach Safeguards Rule compliance assessment?
  ```

#### Play: Play 5: EPA RCRA Significant Noncompliance - Mandatory Enforcement (PQS | Strong - Strong (8.4/10))

- **What's the play?**: Target auto dealerships with service departments in EPA RCRA Significant Noncompliance (SNC) status for hazardous waste violations.
                    SNC status is EPA's enforcement designation for facilities with serious compliance failures - triggers mandatory enforcement action within 180 days.
- **Why this works**: You're referencing their exact EPA facility ID and SNC designation. They know they have an EPA problem, but the NON-OBVIOUS insight is the mandatory enforcement timeline.
                    SNC status means EPA regional offices MUST initiate enforcement action (typically Notice of Violation with corrective action deadlines) within 180 days. This often results in consent decrees with daily penalties up to $50,000/day until violations are corrected.
                    This isn't "you might get fined" - this is "EPA enforcement is coming, here's the timeline."
- **Outreach Message template**:
  ```text
  Subject: EPA SNC status
  
  Your facility (EPA ID CAD000123456) has been in Significant Noncompliance for 4 consecutive quarters per EPA ECHO - last inspection flagged improper storage of used oil and solvents.
  
  SNC status triggers mandatory EPA enforcement within 180 days, typically resulting in consent decrees with daily penalties ($50,000/day) until corrected.
  
  Are you tracking the enforcement timeline internally?
  ```

---

## LogicBroker (logicbroker.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/logicbroker-com)
**Strategic Summary**: Playbook cross-references CPSC complaint databases with customer product catalogs to flag recall-pattern SKUs, and maps supplier compliance decay timelines using FDA warning letters and internal order history.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline your supplier network

Hi {{FirstName}},

I saw you're a VP at a retail company managing supplier relationships. Congrats on the LinkedIn post about Q4 growth!

LogicBroker helps companies like yours automate order processing and inventory sync across hundreds of suppliers. We work with brands like Samsung and Home Depot.

Would love 15 minutes to show you how we can reduce manual work and scale your vendor network.

Best,
SDR Name
```

### ✓ The New Way: GTM Plays

#### Play: CPSC Complaint Tracking Across Multiple SKUs and Channels (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: For children's product manufacturers selling across 4+ channels (Amazon, Walmart, Target, D2C), cross-reference CPSC complaint database with their product catalog to identify complaint language clustering that matches historical recall patterns.
- **Why this works**: They track ALL my SKUs (12) across multiple channels. The cross-channel synthesis is something I can't easily do. Recall pattern matching is genuinely valuable. I need to know which 2 SKUs immediately.
- **Data Sources**:
  - CPSC SaferProducts Database - product_name, manufacturer_name, complaint_type, complaint_date, hazard_description
  - Internal Product Catalog - active SKUs, product names, channel distribution
- **Outreach Message template**:
  ```text
  Subject: CPSC complaint tracking across your 12 SKUs
  
  Built a complaint tracker for all 12 of your children's product SKUs across CPSC, Amazon reviews, and Walmart incident reports.
  
  Found complaint language clustering on 2 SKUs that matches historical recall patterns.
  
  Want the full analysis and which 2 SKUs?
  ```
- **Data Requirement**: This play requires product catalog data showing customer's active SKUs and can correlate with public complaint databases.
                    Combined with public CPSC records and marketplace review data to identify recall risk patterns unique to their product mix.

#### Play: Supplier Compliance Decay Timeline Prediction (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Map the compliance decay pattern for their top 20 suppliers over 24 months, showing average time from first FDA/USDA warning to facility shutdown. Identify which current suppliers are approaching critical failure timeline thresholds.
- **Why this works**: Proprietary analysis using MY supplier data - genuinely non-obvious. The 127-day pattern is specific and actionable. Tells me exactly how many are at risk (2 suppliers). I need to know which 2 immediately.
- **Data Sources**:
  - Company Internal Order Processing Data - supplier order failure rates, chargeback frequency, violation timeline correlation
  - FDA Warning Letters Database - violation dates, facility names, violation types
  - USDA FSIS Inspection Directory - inspection types, facility classifications
- **Outreach Message template**:
  ```text
  Subject: Your supplier compliance timeline
  
  Mapped the compliance decay pattern for your top 20 suppliers over 24 months - found the average time from first warning to facility shutdown is 127 days.
  
  2 of your current suppliers are at day 89 and day 103 in that timeline right now.
  
  Want the timeline analysis and which 2 suppliers?
  ```
- **Data Requirement**: This play requires aggregated supplier compliance event data and correlation with customer's active supplier list showing historical violation-to-failure timelines.
                    This synthesis of compliance patterns with business impact timelines is unique to LogicBroker's platform data.

#### Play: Real-Time Supplier FDA/USDA Compliance Feed (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Build a compliance tracker for their 47 active suppliers that monitors FDA/USDA warning letters, recalls, and facility shutdowns daily. Show current status with 3 suppliers having active warnings and 1 with recall in progress.
- **Why this works**: They did the work for ME specifically - 47 suppliers is my exact network. Real-time monitoring solves a genuine blind spot. Low commitment ask - just send the report. This is genuinely valuable even if I don't buy.
- **Data Sources**:
  - Company Internal Supplier Network Data - active supplier list
  - FDA Warning Letters Database - company names, violation types, dates issued
  - USDA FSIS Enforcement Reports - facility names, enforcement actions
  - FDA Recall Database - company names, recall dates, product types
- **Outreach Message template**:
  ```text
  Subject: Real-time feed of your supplier FDA status
  
  I built a compliance tracker for your 47 active suppliers - it monitors FDA/USDA warning letters, recalls, and facility shutdowns daily.
  
  Right now it shows 3 suppliers with active warnings and 1 with a recall in progress.
  
  Want me to send you the current status report?
  ```
- **Data Requirement**: This play requires visibility into customer's active supplier network from platform integration data.
                    Combined with daily monitoring of public compliance databases to provide personalized real-time alerts.

#### Play: Supplier Risk Score Across Network (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Calculate compliance risk scores for their 47 suppliers based on warning letter history, recall patterns, and facility inspection frequency. Identify 8 suppliers scoring in high-risk category with scored list and methodology.
- **Why this works**: Proprietary scoring methodology applied to MY suppliers. The 8 high-risk count is specific and actionable. Low commitment ask. This is genuinely valuable for procurement decisions.
- **Data Sources**:
  - Company Internal Supplier Network Data - active supplier list
  - FDA Warning Letters Database - company names, violation history, dates
  - FDA Recall Database - recall frequency, product types
  - FDA Inspections Dashboard - facility inspection frequency, citations
- **Outreach Message template**:
  ```text
  Subject: Supplier risk score for your network
  
  Calculated compliance risk scores for your 47 suppliers based on warning letter history, recall patterns, and facility inspection frequency.
  
  8 suppliers score in the high-risk category right now.
  
  Want the scored list and the criteria?
  ```
- **Data Requirement**: This play requires supplier network data and proprietary risk scoring algorithm based on public compliance records.
                    The scoring methodology is unique to your analysis - competitors cannot replicate the risk assessment framework.

#### Play: Multi-Channel Coordinated Inventory Hold Mapping (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: For manufacturers with CPSC complaint spikes, map their exact distribution footprint across all 6 channels (Amazon, Walmart, Target, Wayfair, Overstock, D2C) to prepare for coordinated inventory holds if CPSC escalates.
- **Why this works**: They know my exact distribution footprint - 6 specific channels. The coordinated hold scenario is something I haven't planned for. This is genuinely helpful for risk planning. Low commitment ask.
- **Data Sources**:
  - Company Internal Multi-Channel Distribution Data - SKU distribution across channels
  - CPSC SaferProducts Database - complaint counts, product names
- **Outreach Message template**:
  ```text
  Subject: Your products sold through 6 channels
  
  Your XR-240 table is currently listed on Amazon, Walmart, Target, Wayfair, Overstock, and your D2C site.
  
  With 7 active CPSC complaints, you'll need coordinated inventory holds across all 6 channels if CPSC escalates.
  
  Want the channel-by-channel SKU map?
  ```
- **Data Requirement**: This play requires multi-channel distribution data showing where customer's products are sold.
                    Combined with CPSC complaint data to provide contingency planning for coordinated product safety responses.

#### Play: DEA Renewal Readiness Across Multiple Facilities (PVP                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: For pharmacy distributors with 3 DEA-registered facilities with Q1 2025 renewals, map open FDA citations at each location and closure letter status to create facility-by-facility renewal readiness report.
- **Why this works**: They know my exact facility count and renewal dates. The citation mapping is genuinely helpful. Low commitment ask. This saves me hours of manual tracking.
- **Data Sources**:
  - Company Internal Facility Location Data - DEA registrations, facility addresses
  - DEA Registered Distributors Lookup - registration numbers, expiration dates
  - FDA Inspections Dashboard - facility citations, violation details
- **Outreach Message template**:
  ```text
  Subject: DEA renewal checklist for your 3 facilities
  
  You have 3 DEA-registered facilities with renewals in Q1 2025 (March 15, April 2, April 18).
  
  I mapped the open FDA citations at each location and the closure letter status.
  
  Want the facility-by-facility renewal readiness report?
  ```
- **Data Requirement**: This play requires facility location data to correlate DEA registrations with FDA inspection records.
                    The cross-agency synthesis creates a compliance readiness view unique to your multi-facility network.

#### Play: CPSC Complaint Pattern Recognition on Specific Products (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Identify children's product manufacturers whose specific product models have complaint spikes with clustered language in CPSC database (e.g., 7 complaints in 49 days with 6 mentioning "tipping hazard"). CPSC's pattern recognition flags products when similar complaint language clusters.
- **Why this works**: Very specific - exact time window and specific complaint language. The pattern recognition insight is non-obvious. I can verify this in the CPSC database quickly. Good routing question.
- **Data Sources**:
  - CPSC SaferProducts Database - product_name, manufacturer_name, complaint_type, complaint_date, hazard_description
- **Outreach Message template**:
  ```text
  Subject: CPSC complaint pattern on XR-240
  
  Your XR-240 table had 7 complaints in 49 days - 6 mention "tipping hazard" specifically.
  
  CPSC's pattern recognition flags products when similar complaint language clusters like this.
  
  Who's handling the product safety review?
  ```

#### Play: DEA Renewal with Open FDA Citations at Specific Facility (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Identify DEA-registered pharmacy distributors with registration renewals in next 60 days who have 2+ open FDA citations from recent inspections at specific facilities. Provide exact facility address, exact citation types, and exact renewal countdown.
- **Why this works**: Very specific - exact address, exact date, exact citation types. The 47-day countdown creates urgency. Simple routing question. The connection between FDA and DEA is genuinely helpful.
- **Data Sources**:
  - DEA Registered Distributors Lookup - distributor_name, registration_number, expiration_date, address
  - FDA Inspections Dashboard - facility_name, inspection_citations, violation_details, business_address
- **Outreach Message template**:
  ```text
  Subject: March DEA renewal + August FDA gaps
  
  Your DEA registration at 1247 Commerce Blvd renews in 47 days.
  
  The 2 open FDA citations from August 12 (storage temperature + record-keeping) can trigger DEA renewal conditions.
  
  Who's handling the FDA closure letters?
  ```

#### Play: Amazon Safety Flag with CPSC Complaint Dual-Track Risk (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Identify manufacturers whose products were flagged by Amazon's automated safety monitoring (based on customer review language) AND have active CPSC complaints, creating dual-track risk where both CPSC and Amazon could pull the listing.
- **Why this works**: Specific platform (Amazon) and exact date. The dual-track risk insight is non-obvious. I can verify the Amazon flag in Seller Central. Good routing question.
- **Data Sources**:
  - Amazon Seller Central Safety Notifications - product ASINs, flag dates, review language triggers
  - CPSC SaferProducts Database - product_name, manufacturer_name, complaint_count
- **Outreach Message template**:
  ```text
  Subject: Amazon flagged your XR-240 for safety review
  
  Amazon's automated safety monitoring flagged your XR-240 table on November 8 based on customer review language.
  
  That flag combined with 7 CPSC complaints creates dual-track risk - both CPSC and Amazon could pull the listing.
  
  Who's coordinating the Amazon seller performance response?
  ```

#### Play: CPSC Complaint Spike Approaching Informal Review Threshold (PQS                     Public Data | Strong - Strong (8.3/10))

- **What's the play?**: Identify children's product manufacturers with specific product models showing 350%+ complaint spike versus prior 6 months, putting them in range where CPSC typically initiates informal review (7+ complaints in 60 days).
- **Why this works**: Specific product model and exact complaint count. The 350% spike calculation adds context. CPSC review threshold is genuinely concerning. Simple routing question.
- **Data Sources**:
  - CPSC SaferProducts Database - product_name, manufacturer_name, complaint_type, complaint_date
- **Outreach Message template**:
  ```text
  Subject: Your Model XR-240 has 7 CPSC complaints filed
  
  The CPSC database shows 7 consumer complaints filed against your Model XR-240 children's table between September 15 and November 3.
  
  That's a 350% spike versus the prior 6 months and puts you in the range where CPSC typically initiates informal review.
  
  Is someone already coordinating the CPSC response?
  ```

#### Play: DEA Renewal with FDA Facility Compliance Gaps (PQS                     Public Data | Strong - Strong (8.1/10))

- **What's the play?**: Identify pharmacy distributors with DEA registrations renewing within 60 days who have 2+ open FDA facility citations. DEA can delay renewal or add conditions when FDA compliance gaps exist at renewal time.
- **Why this works**: Specific to my actual situation - they know my DEA renewal date. The FDA citation overlap is something I might have missed. Easy routing question. Could feel slightly accusatory but it's factual.
- **Data Sources**:
  - DEA Registered Distributors Lookup - distributor_name, registration_number, expiration_date
  - FDA Inspections Dashboard - facility_name, inspection_citations, violation_details
- **Outreach Message template**:
  ```text
  Subject: Your DEA renewal due with 2 open FDA citations
  
  Your DEA registration renews March 15, 2025, but you have 2 open FDA facility citations from the August inspection.
  
  DEA can delay renewal or add conditions when FDA compliance gaps exist at renewal time.
  
  Is someone coordinating the FDA response before March?
  ```

#### Play: Supplier Warning Letter with Active Order Routing (PQS                     Public + Internal | Strong - Strong (7.9/10))

- **What's the play?**: Identify food/meat distributors who routed orders in past 30 days to suppliers who received FDA warning letters for sanitation violations. Show exact order volume and specific channels affected (Walmart, Kroger, Sysco).
- **Why this works**: Specific supplier and exact date. They know my order volume (47) and specific channels. The inherited risk is real. Question could be more yes/no focused.
- **Data Sources**:
  - FDA Warning Letters Database - company_name, violation_type, date_issued
  - Company Internal Order Routing Data - supplier order volume, channel distribution
- **Outreach Message template**:
  ```text
  Subject: Valley Meat Co warning letter affects your orders
  
  Valley Meat Co received an FDA warning letter on October 29 for sanitation violations at their processing facility.
  
  You routed 47 orders to them in the past 30 days across Walmart, Kroger, and Sysco channels.
  
  Do you have automated supplier compliance monitoring?
  ```
- **Data Requirement**: This play requires order routing data showing customer's supplier order volume and channel distribution.
                    Combined with public FDA warning letter data to identify inherited compliance risk across channels.

#### Play: Multiple Suppliers with Recent FDA Warning Letters (PQS                     Public Data | Okay - Okay (7.8/10))

- **What's the play?**: Identify food distributors whose supplier network includes 3+ suppliers who received FDA warning letters in past 90 days. If still routing orders to them, they're inheriting compliance risk across all channels.
- **Why this works**: Specific suppliers with exact dates - this is research. The inherited risk angle is something I hadn't considered. I can verify these warning letters in 60 seconds. The question is clear but could be yes/no instead of open-ended.
- **Data Sources**:
  - FDA Warning Letters Database - company_name, violation_type, date_issued
- **Outreach Message template**:
  ```text
  Subject: 3 of your suppliers lost FDA compliance
  
  In the past 90 days, 3 suppliers in your network had FDA warning letters: Acme Foods (Oct 3), Valley Meat Co (Oct 29), and Riverdale Dairy (Nov 12).
  
  If you're still routing orders to them, you're inheriting their compliance risk across all your channels.
  
  Do you have real-time supplier compliance tracking?
  ```

---

## PetCircle (petcircle.com.au)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/petcircle-com-au)
**Strategic Summary**: Playbook uses internal order history and usage velocity to project stockout dates aligned with seasonal demand spikes, and calculates emergency order upcharges versus bulk contract pricing to quantify reactive purchasing costs.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Streamline Your Pet Supply Management

Hi [First Name],

I noticed your facility serves hundreds of animals each month. That's impressive!

At PetCircle, we help organizations like yours save time and money on pet supplies through our convenient auto-delivery subscription service. We offer 7000+ products at competitive prices with fast home delivery.

Are you available for a quick 15-minute call next Tuesday to discuss how we can help optimize your supply chain?

Best regards,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: Play: Holiday Grooming Supply Depletion Alert (PVP                     Internal Data | Strong - Strong (9.2/10))

- **What's the play?**: Track usage velocity by product and facility to project exact stockout dates, then flag when depletion aligns with seasonal demand spikes.
                    This play calculates when a facility will run out of critical supplies based on their historical usage patterns, then adds urgency by connecting it to upcoming seasonal demand.
- **Why this works**: You're surfacing a problem they haven't noticed yet. The specific date creates immediate urgency, and the seasonal context (holiday boarding rush) makes the stakes crystal clear.
                    The buyer thinks: "How did they know exactly when I'll run out? And they're right - I can't afford to be short during the holidays."
- **Data Sources**:
  - Internal Order History - product SKU, order date, quantity, usage velocity calculation
  - Seasonal Demand Patterns - historical volume spikes by product category and time period
- **Outreach Message template**:
  ```text
  Subject: Your shampoo stock runs out next Tuesday
  
  Based on your 14-day usage cycle for grooming supplies, your FURminator shampoo inventory hits zero on December 17th.
  
  That's right before the holiday boarding rush when grooming volume spikes 40%.
  
  Want me to expedite your reorder?
  ```
- **Data Requirement**: This play requires historical order data by SKU and facility, with usage velocity calculations (units consumed per day/week) and seasonal demand intelligence.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Play: Emergency Order Cost Analysis (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Identify facilities placing emergency same-day orders, then calculate the exact upcharge they paid versus bulk contract pricing.
                    This turns reactive purchasing behavior into a quantified pain point with specific dates and dollar amounts.
- **Why this works**: This isn't about what COULD happen - it's about what ALREADY happened. You're showing them money they've already lost, with specific dates and products they can verify.
                    The buyer thinks: "They tracked my emergency orders? That $1,247 is real money I wasted. I don't want to keep doing this."
- **Data Sources**:
  - Internal Order History - order date, delivery speed, product SKU, price paid
  - Bulk Contract Pricing Database - standard pricing by SKU for comparison
- **Outreach Message template**:
  ```text
  Subject: Your Nov emergency orders cost $1,247 extra
  
  You placed 3 emergency same-day orders in November - Hill's Science Diet on the 8th, Purina Pro Plan on the 15th, and Royal Canin on the 23rd.
  
  Those emergency orders cost $1,247 more than your bulk contract pricing.
  
  Want me to set up automatic reorder alerts?
  ```
- **Data Requirement**: This play requires purchase history showing emergency order patterns (same-day delivery, rush charges) and the ability to calculate markup differential versus standard pricing.
                    Combined with your internal pricing data to quantify the exact cost of reactive ordering. This synthesis is unique to your business.

#### Play: Play: Seasonal Prevention Inventory Alert (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Track reorder cadence by product category and geography, then flag when orders are overdue relative to historical patterns - especially during peak demand seasons.
                    Combines order history tracking with regional seasonal intelligence to create time-sensitive alerts.
- **Why this works**: The message connects their routine reorder pattern to a revenue impact (missed appointments during peak season). It's not just about inventory - it's about client service and revenue protection.
                    The buyer thinks: "They know my exact reorder cycle AND the seasonal context. Running out during testing season would be a disaster."
- **Data Sources**:
  - Internal Order History - product SKU, order intervals by facility, days since last order
  - Regional Seasonal Demand Data - peak periods by geography and product category
- **Outreach Message template**:
  ```text
  Subject: Heartworm prevention due in 4 days
  
  Your facility reorders Heartgard Plus every 21 days like clockwork, and your last order was 17 days ago.
  
  January-March is heartworm testing season in Florida, and running out means turning away preventive care appointments.
  
  Should I send your standard case quantity?
  ```
- **Data Requirement**: This play requires reorder pattern tracking by product and facility, with deviation detection (when current interval exceeds historical average) plus regional seasonal demand intelligence.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Play: Safety Stock Depletion Alert (PVP                     Internal Data | Strong - Strong (9.0/10))

- **What's the play?**: Monitor reorder cadence by SKU and facility, flagging when orders are overdue relative to historical patterns and safety stock thresholds.
                    This creates proactive alerts before stockouts occur, positioned around client service impact.
- **Why this works**: You're preventing a problem before it becomes urgent. The specific reorder interval (10-12 days) shows you're tracking their business, and the client appointment consequence makes the stakes real.
                    The buyer thinks: "They know my exact reorder pattern. And they're right - I can't reschedule appointments because I ran out."
- **Data Sources**:
  - Internal Order History - product SKU, order frequency by facility, days since last order
- **Outreach Message template**:
  ```text
  Subject: 13 days since your last Royal Canin order
  
  You reorder Royal Canin Veterinary Diet every 10-12 days, but it's been 13 days and you're likely down to your safety stock.
  
  Running out mid-week means client appointments get rescheduled or you pay retail markup.
  
  Should I queue your standard order?
  ```
- **Data Requirement**: This play requires reorder cadence tracking by SKU and facility, with alerts triggered when current interval exceeds historical average.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Play: USDA Repeat Violation Escalation Risk (PQS                     Public Data | Strong - Strong (8.9/10))

- **What's the play?**: Target USDA-licensed facilities with 3+ direct noncompliances from recent inspections, especially those facing license suspension review.
                    These facilities are under regulatory pressure and need to demonstrate operational improvements immediately.
- **Why this works**: You're citing specific inspection dates and violation types they can verify. The license suspension escalation is real and terrifying - this isn't theoretical pain, it's an urgent operational crisis.
                    The buyer thinks: "They reviewed my actual USDA report. They know exactly what we're facing. We need help."
- **Data Sources**:
  - USDA Animal Care Public Search Tool - facility name, inspection date, violation type, noncompliance count
- **Outreach Message template**:
  ```text
  Subject: November 14 inspection at Premier Pet Resort
  
  Your Premier Pet Resort Dallas location received 3 direct noncompliances on November 14, 2024 - enclosure maintenance, veterinary program, and feeding documentation.
  
  USDA Regional Director reviews facilities with 3+ citations for potential license suspension.
  
  Who's submitting your corrective action response?
  ```

#### Play: Play: Weekend Stockout Prevention (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Track reorder frequency by facility size and product category, then alert facilities when reorder windows align with high-risk timing (weekends, holidays).
                    This combines usage pattern tracking with operational risk awareness.
- **Why this works**: You're preventing an expensive, stressful problem (emergency weekend retail runs at 3x cost). The specificity of the facility size comparison and the concrete cost multiplier make this feel personalized and credible.
                    The buyer thinks: "They know facilities my size reorder every 11 days. And they're right - weekend emergencies are expensive and annoying."
- **Data Sources**:
  - Internal Order History - facility size, product SKU, reorder frequency patterns, days since last order
- **Outreach Message template**:
  ```text
  Subject: Your Hill's Science Diet reorder is due Thursday
  
  Our data shows facilities your size (18-24 kennels) reorder Hill's Science Diet every 11 days, and your last bulk order was 9 days ago.
  
  Running out over the weekend means emergency retail runs at 3x your bulk cost.
  
  Want me to auto-flag your reorder windows?
  ```
- **Data Requirement**: This play requires order history data showing reorder frequency patterns by facility size category and product SKU, with the ability to calculate days since last order.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Play: High-Volume Shelters with Flat Budget Allocation (PQS                     Public Data | Strong - Strong (8.8/10))

- **What's the play?**: Target animal shelters where intake volume increased significantly year-over-year but county budget allocation stayed flat.
                    This creates quantifiable financial pressure - more animals on the same budget means cost-cutting or shortages.
- **Why this works**: You've done the math they're already agonizing over. The $53,856 annual shortfall is the exact conversation they're having with county commissioners and board members.
                    The buyer thinks: "How did they calculate our exact budget gap? This is the problem keeping me up at night."
- **Data Sources**:
  - Shelter Animals Count Database - annual intake volume by facility
  - GuideStar/Candid Nonprofit Directory - annual budget, program expenses
- **Outreach Message template**:
  ```text
  Subject: 528 more animals, same food budget
  
  Animal Care Services took in 528 more animals in Q4 2024 vs Q4 2023, but your county allocation for 2025 stayed at $487,000.
  
  At current food costs, that's a $53,856 annual shortfall just in kibble and canned food.
  
  Who's managing the budget reallocation?
  ```

#### Play: Play: Veterinary Clinics Facing DEA Audit During Staff Turnover (PQS                     Public Data | Strong - Strong (8.7/10))

- **What's the play?**: Target veterinary clinics with recent vet tech job postings that have DEA registration renewals coming up within 90 days.
                    New staff handling controlled substances during audit periods is the highest-risk scenario for veterinary practices.
- **Why this works**: You've connected two separate pain points (new staff + DEA audit) into a single urgent crisis. The timing creates genuine urgency, and the #1 violation trigger claim feels authoritative.
                    The buyer thinks: "They know our DEA renewal date AND tracked our hiring. This is exactly the risk we're worried about."
- **Data Sources**:
  - LinkedIn Job Postings - vet tech positions, posting date
  - DEA Controlled Substance Registration Database - registration number, renewal date
- **Outreach Message template**:
  ```text
  Subject: 2 vet techs left, DEA audit is March
  
  Your clinic posted 2 vet tech positions in October, and your DEA registration renewal is March 2025 - that means inventory audit.
  
  New staff handling Schedule II drugs without complete training is the #1 DEA violation trigger.
  
  Is someone shadowing the new techs on controlled substance protocols?
  ```

#### Play: Play: Multi-Vendor Logistics Burden Analysis (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Identify facilities receiving deliveries from multiple pet supply vendors by tracking delivery patterns at physical addresses, then quantify the administrative burden.
                    This turns visible operational complexity into quantified time waste.
- **Why this works**: You're surfacing hidden costs they haven't calculated. The specific address and delivery count prove you're not guessing, and quantifying the 8-12 hours monthly makes the pain concrete.
                    The buyer thinks: "They counted my deliveries? I never calculated how much time I waste on logistics. That's real labor cost."
- **Data Sources**:
  - Public Delivery Records - truck visits by address (observable)
  - Internal Efficiency Data - average time per delivery for receiving/inventory/reconciliation
- **Outreach Message template**:
  ```text
  Subject: 892 Commerce Drive gets 11 deliveries monthly
  
  Your facility at 892 Commerce Drive receives deliveries from 5 different pet supply vendors - I counted 11 separate truck visits in November.
  
  Each delivery requires staff time for receiving, inventory, and reconciliation - that's 8-12 hours monthly just on logistics.
  
  Want to see what single-vendor consolidation looks like?
  ```
- **Data Requirement**: This play requires the ability to observe delivery patterns at customer locations (public) plus internal benchmarking data on time spent per delivery for receiving/inventory tasks.
                    Combined with your internal efficiency data from single-vendor customers to quantify the hidden administrative burden. This synthesis is unique to your business.

#### Play: Play: Veterinary Clinics with Compliance Violations During Staff Turnover (PQS                     Public Data | Strong - Strong (8.6/10))

- **What's the play?**: Target veterinary clinics with state board disciplinary citations in past 18 months AND concurrent staff reductions visible through LinkedIn employee counts or multiple open positions.
                    The combination signals operational chaos - compliance issues AND staffing problems mean supply management is likely suffering.
- **Why this works**: You've identified a clinic under extreme stress from two converging problems. The state board focus on inventory reconciliation is accurate and creates genuine urgency around getting operations under control.
                    The buyer thinks: "They tracked both our violations AND our hiring. We're barely keeping up - we need help."
- **Data Sources**:
  - State Veterinary Board Disciplinary Records - clinic name, violation type, violation date
  - LinkedIn Company Pages - employee count changes, job postings
- **Outreach Message template**:
  ```text
  Subject: 2 vet techs left, Oak Street Vet lost 2 techs in October
  
  Oak Street Veterinary Clinic in Portland posted 2 vet tech openings in October 2024, and your last state board inspection flagged controlled substance documentation gaps.
  
  Staff turnover breaks institutional knowledge on DEA inventory protocols.
  
  Who's training the new techs on documentation?
  ```

#### Play: Play: Shelter Intake Volume Spike with Budget Constraint (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target animal shelters where quarterly intake volume jumped significantly year-over-year but budget stayed flat, creating immediate supply pressure.
                    This is acute operational stress - more animals arriving but no additional funding to handle them.
- **Why this works**: You're quantifying the exact problem they're living. The 528 more animals is verifiable in their records, and the flat county allocation is the frustration they're dealing with daily.
                    The buyer thinks: "They know our exact intake numbers AND our budget situation. This is the crisis we're managing right now."
- **Data Sources**:
  - Shelter Animals Count Database - quarterly intake volume by facility
  - County Budget Records - annual allocation by department
- **Outreach Message template**:
  ```text
  Subject: 1,847 intakes vs 1,319 last year
  
  Your Q4 2024 intake of 1,847 animals is 40% higher than Q4 2023's 1,319, but your 2025 county allocation stayed flat at $487,000.
  
  That's 528 more animals on the same food and medical budget.
  
  Is your procurement team already adjusting supplier contracts?
  ```

#### Play: Play: Multiple Hires During Controlled Substance Compliance Issues (PQS                     Public Data | Strong - Strong (8.5/10))

- **What's the play?**: Target veterinary clinics that hired 3+ new vet techs since September AND had state board inspections noting controlled substance documentation inconsistencies.
                    State boards specifically look for correlation between staffing changes and compliance lapses.
- **Why this works**: You've identified the exact operational risk the state board will scrutinize. The state board focus on inventory reconciliation during next inspection is accurate and creates genuine urgency.
                    The buyer thinks: "They know we hired 3 people AND had documentation issues. The next inspection will focus on this. We need to get ahead of it."
- **Data Sources**:
  - LinkedIn Job Postings - vet tech positions, posting date, number of openings
  - State Veterinary Board Inspection Records - inspection date, violation type
- **Outreach Message template**:
  ```text
  Subject: 3 new hires, controlled substance gaps flagged
  
  River City Animal Hospital hired 3 new vet techs since September, and your October state board inspection noted controlled substance documentation inconsistencies.
  
  State boards correlate staffing changes with compliance lapses - your next inspection will focus on inventory reconciliation.
  
  Who's overseeing the DEA training program?
  ```

#### Play: Play: Shelter Intake Surge with Food Cost Calculation (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target shelters where intake jumped 40%+ quarter-over-quarter, then calculate the exact monthly food cost increase based on current market pricing.
                    This turns intake data into immediate budget pressure with specific dollar amounts.
- **Why this works**: You're doing their budget math for them. The 40% intake increase is verifiable, and the $4,488/month food cost calculation is the exact number they need to justify budget requests.
                    The buyer thinks: "They calculated exactly what this intake surge costs us. This is the number I need for the county budget meeting."
- **Data Sources**:
  - Shelter Animals Count Database - quarterly intake volume by facility
  - Market Food Pricing Data - average cost per bag/unit by product type
- **Outreach Message template**:
  ```text
  Subject: Your shelter intake jumped 40% in Q4
  
  Animal Care Services of San Antonio took in 1,847 animals in Q4 2024 vs 1,319 in Q4 2023 - that's 40% more mouths to feed on the same budget.
  
  At your current $8.50/bag food cost, that's an extra $4,488/month in just kibble.
  
  Who handles your bulk supply ordering?
  ```

#### Play: Play: USDA Repeat Violations with Civil Penalty Risk (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Target facilities with the same USDA violation cited in multiple inspections within a 12-month period, triggering escalated enforcement procedures.
                    Repeat violations within 12 months move facilities into higher scrutiny categories with potential civil penalties.
- **Why this works**: You've identified facilities in the escalation pathway. The specific violation type, dates, and civil penalty amounts are all verifiable and create genuine fear of regulatory consequences.
                    The buyer thinks: "They reviewed multiple inspection reports. We're on the repeat violation track. Those civil penalties are real."
- **Data Sources**:
  - USDA Animal Care Public Search Tool - facility name, inspection date, violation type, repeat violation tracking
  - USDA Enforcement Guidelines - civil penalty schedules by violation type
- **Outreach Message template**:
  ```text
  Subject: Repeat enclosure violations at your facility
  
  Your facility had enclosure maintenance cited in both the June 2024 and November 2024 USDA inspections.
  
  Repeat violations within 12 months trigger USDA escalated enforcement - potential civil penalties up to $11,000 per violation.
  
  Is someone coordinating your physical plant upgrades?
  ```

#### Play: Play: Clinics with Open Positions During Compliance Issues (PQS                     Public Data | Strong - Strong (8.2/10))

- **What's the play?**: Target veterinary clinics with 3+ open vet tech positions since September AND state inspection violations in the past 90 days.
                    The combination signals understaffing during compliance follow-up periods - heightened operational risk.
- **Why this works**: You've connected hiring pressure with compliance issues into a single crisis narrative. The documentation risks during follow-up are real and the question is helpful, not accusatory.
                    The buyer thinks: "They tracked our job postings AND our inspection results. We are stretched thin during follow-up. This is exactly our problem."
- **Data Sources**:
  - LinkedIn Job Postings - vet tech positions, posting date, number of openings
  - State Veterinary Board Inspection Records - inspection date, violation type
- **Outreach Message template**:
  ```text
  Subject: 3 open positions at River City Animal Hospital
  
  River City Animal Hospital has 3 vet tech positions open since September, and your state inspection in August noted medication storage and labeling issues.
  
  New staff onboarding during compliance follow-up creates documentation risks.
  
  Is someone already coordinating the training and follow-up?
  ```

---

## Rebuy Engine (rebuyengine.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/rebuyengine-com)
**Strategic Summary**: Playbook matches TTB alcohol producer permit cohorts to internal AOV and conversion benchmarks to show merchants falling behind peers who adopted personalization features within 90 days of launch.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Increase Your AOV with AI Personalization

Hi [First Name],

I noticed you're focused on ecommerce growth at [Company]. Congrats on the recent product launch!

At Rebuy, we help Shopify merchants like you increase average order value through AI-powered personalization. Our Smart Cart technology has helped brands lift AOV by up to 18%.

We work with 3,000+ brands including [Competitor]. Would love to show you how we can drive similar results for [Company].

Are you available for a 15-minute call next week?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Your TTB Cohort Averaging 38% Higher AOV (PQS                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Target TTB-permitted alcohol merchants (wineries/distilleries) by matching their permit date to a cohort, then show them their AOV performance gap versus peers who launched at the same time. The 12% widening gap in 60 days creates urgency.
- **Why this works**: Peer comparison creates instant urgency - nobody wants to fall behind their direct competitors. The specific cohort match (Q2 2024 permits) proves you did real research, and the widening gap shows the problem is accelerating. The routing question makes it easy to forward internally.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date, permit_type
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date, permit_type
  - Company Internal Data - AOV by merchant, permit cohort matching
- **Outreach Message template**:
  ```text
  Subject: Your TTB cohort averaging 38% higher AOV
  
  The 47 alcohol merchants who got TTB permits in your quarter are averaging $142 AOV versus your $102.
  
  They're using cart personalization you're not - the gap widened 12% in the last 60 days.
  
  Is someone tracking why your AOV is falling behind?
  ```
- **Data Requirement**: This play assumes your company has:
                    Internal AOV data across alcohol merchant customers and can match them to TTB permit dates to create cohort comparisons. Requires tracking performance trends over time (60-day gap analysis).
                    If you have this data, this play becomes highly differentiated - competitors can't replicate cohort-specific benchmarking.

#### Play: Your Q2 2024 TTB Cohort Outpacing You 38% (PQS                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Same cohort targeting as above, but add conversion rate gap (4.2% vs 2.8%) and attribute the performance difference to specific feature adoption timing (Smart Cart within 90 days). Shows both the problem and the pattern that causes it.
- **Why this works**: Adding the conversion rate gap makes the impact multi-dimensional - it's not just AOV, it's also losing more carts. The 90-day Smart Cart timing gives them a specific implementation pattern to verify and creates urgency to catch up. Recipient can validate their actual 2.8% rate, which builds trust.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - AOV, cart conversion rate, feature adoption timing by cohort
- **Outreach Message template**:
  ```text
  Subject: Your Q2 2024 TTB cohort outpacing you 38%
  
  The 47 merchants who launched alcohol sales in Q2 2024 are hitting $142 AOV - you're at $102.
  
  Their cart conversion rate is 4.2% versus your 2.8% because they deployed Smart Cart within 90 days.
  
  Who owns your checkout optimization?
  ```
- **Data Requirement**: This play assumes your company has:
                    Conversion rate tracking by merchant, feature adoption timing data (when Smart Cart was enabled), and ability to correlate adoption timing to performance outcomes across TTB cohorts.
                    The 90-day timing insight requires tracking feature deployment dates relative to permit issuance.

#### Play: Your Subscription Revenue 0% vs Cohort 41% (PQS                     Public + Internal | Strong - Strong (8.3/10))

- **What's the play?**: Target TTB alcohol merchants with zero subscription revenue and show them their Q2 2024 cohort is averaging 41% recurring revenue. Add the profitability timing insight - early adopters (first 120 days) hit profitability 5 months faster.
- **Why this works**: Being at 0% when peers are at 41% is embarrassing - creates immediate competitive pressure. The profitability timing (5 months faster) gives them a CFO-friendly talking point. The easy yes/no routing question makes it simple to engage.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - subscription revenue percentage, profitability timing by cohort
- **Outreach Message template**:
  ```text
  Subject: Your subscription revenue 0% vs cohort 41%
  
  Your Q2 2024 TTB cohort is averaging 41% subscription revenue - you're at 0%.
  
  The 19 merchants who deployed subscriptions in their first 120 days hit profitability 5 months faster.
  
  Is subscription revenue on your roadmap?
  ```
- **Data Requirement**: This play assumes your company has:
                    Subscription revenue tracking as percentage of total GMV across alcohol customers, profitability timing data by merchant, and ability to correlate subscription adoption timing (first 120 days) to financial outcomes.
                    The 5-month profitability acceleration requires access to merchant financial milestones or self-reported data.

#### Play: Your Cart Abandonment 73% vs Cohort 52% (PQS                     Public + Internal | Strong - Strong (8.5/10))

- **What's the play?**: Target TTB alcohol merchants with above-average cart abandonment (73%) and benchmark them against their Q2 2024 cohort average (52%). Calculate the revenue impact at their current traffic volume - $180K annual lost revenue makes it tangible.
- **Why this works**: The 21-point gap is specific and embarrassing. The $180K calculation shows they understand the merchant's traffic volume, which builds credibility. Cart abandonment is a KPI every ecommerce leader tracks, so they can verify this is accurate. The routing question is easy to answer.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - cart abandonment rates, traffic volume, revenue impact modeling
- **Outreach Message template**:
  ```text
  Subject: Your cart abandonment 73% vs cohort 52%
  
  Your Q2 2024 TTB cohort is averaging 52% cart abandonment - you're at 73%.
  
  The 21% gap represents roughly $180K in annual lost revenue at your current traffic.
  
  Who's responsible for your cart experience?
  ```
- **Data Requirement**: This play assumes your company has:
                    Cart abandonment rate tracking by merchant, traffic volume data for revenue impact modeling, and cohort benchmarking capabilities across TTB-permitted alcohol merchants.
                    The $180K calculation requires traffic data and average order value to model lost revenue opportunity.

#### Play: Benchmarks for Your 47-Merchant TTB Cohort (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Offer a complete performance report for the prospect's specific Q2 2024 TTB cohort - AOV, conversion, cart abandonment, subscription mix. Position them in the bottom quartile on 3/4 metrics but top quartile on traffic quality, giving them both urgency and hope.
- **Why this works**: The specific cohort size (47 merchants) and timing (Q2 2024) prove real research. Bottom quartile on 3/4 metrics is concerning but the top quartile traffic quality creates optimism - they have the right audience, just need better conversion tools. Low commitment ask - just wants to see the data.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - performance metrics by cohort, quartile analysis, anonymized benchmarking
- **Outreach Message template**:
  ```text
  Subject: Benchmarks for your 47-merchant TTB cohort
  
  Built a performance report for the 47 alcohol merchants in your Q2 2024 TTB cohort - AOV, conversion, cart abandonment, subscription mix.
  
  You're in the bottom quartile on 3 of 4 metrics but top quartile on traffic quality.
  
  Want the full breakdown with anonymized merchant positions?
  ```
- **Data Requirement**: This play assumes your company has:
                    Aggregated performance metrics across alcohol merchant customers with ability to anonymize and create quartile rankings. Requires traffic quality scoring methodology.
                    This is pure PVP - the recipient gets valuable competitive intelligence whether they buy or not.

#### Play: Your Alcohol Cohort's Conversion Tactics Ranked (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Analyze the 47 Q2 2024 TTB merchants and rank their 12 most common cart optimization tactics by ROI and implementation time. Surface the top 3 tactics that took under 2 weeks to deploy and lifted AOV by $28-$35 on average.
- **Why this works**: ROI ranking plus implementation time is exactly what a CRO Manager needs to prioritize - removes all guesswork. The $28-$35 AOV lift in under 2 weeks is compelling. The recipient gets actionable value whether they buy Rebuy or not - they can implement these tactics with any vendor. Low commitment ask.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - feature adoption patterns, ROI by tactic, implementation timing data
- **Outreach Message template**:
  ```text
  Subject: Your alcohol cohort's conversion tactics ranked
  
  Analyzed the 47 Q2 2024 TTB merchants - ranked their 12 most common cart optimization tactics by ROI and implementation time.
  
  Top 3 tactics took under 2 weeks to deploy and lifted AOV by $28-$35 on average.
  
  Want the ranked list with implementation guides?
  ```
- **Data Requirement**: This play assumes your company has:
                    Feature adoption tracking showing which cart optimization tactics are most common, revenue attribution by feature to calculate ROI, and implementation timing data to show how long each tactic takes to deploy.
                    This provides vendor-agnostic value - the tactics work regardless of platform choice.

#### Play: 3 Alcohol Merchants in Your Cohort Hitting $180 AOV (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Identify the top 3 performers in the prospect's Q2 2024 TTB cohort consistently hitting $180+ AOV (76% higher than prospect's $102). Map their exact personalization setup - specifically the 4 cart triggers they're using that the prospect isn't. All deployable in under 10 days.
- **Why this works**: $180 AOV is 76% higher than their $102 - that's massive and aspirational. The specific cohort match proves real research. 10 days implementation time makes it feel achievable. Before/after metrics let them model the impact. They get value even without buying - can see what top performers are doing.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - AOV by merchant, top performer identification, feature configuration documentation
- **Outreach Message template**:
  ```text
  Subject: 3 alcohol merchants in your cohort hitting $180 AOV
  
  Found 3 merchants in your Q2 2024 TTB cohort consistently hitting $180+ AOV - mapped their exact personalization setup.
  
  They're using 4 specific cart triggers you're not, all deployable in under 10 days.
  
  Want the implementation playbook with their before/after metrics?
  ```
- **Data Requirement**: This play assumes your company has:
                    Ability to identify top performers within cohorts, feature configuration documentation showing which cart triggers are enabled, and before/after performance data to show impact of specific features.
                    This provides a concrete roadmap the recipient can use to build their optimization plan.

#### Play: Subscription Playbook from Your 19 TTB Peers (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Document how 19 of the Q2 2024 TTB cohort launched subscriptions in their first 120 days - setup, offer structure, pricing models. Show the performance split: 41% subscription revenue for early adopters vs 12% for late adopters. Offer the complete playbook with templates.
- **Why this works**: Specific count (19 merchants) and timing (120 days) shows research depth. The 41% vs 12% split between early/late adopters is powerful - shows timing matters. Playbook with templates means they can act immediately. They get value regardless of buying - can use the templates to launch their own program.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - subscription adoption patterns, offer structure documentation, revenue performance by timing
- **Outreach Message template**:
  ```text
  Subject: Subscription playbook from your 19 TTB peers
  
  19 of your Q2 2024 TTB cohort launched subscriptions in first 120 days - documented their setup, offer structure, pricing models.
  
  They're averaging 41% subscription revenue versus 12% for late adopters.
  
  Want the playbook with offer templates and customer messaging?
  ```
- **Data Requirement**: This play assumes your company has:
                    Subscription adoption tracking by merchant with timing data, offer structure documentation, pricing model analysis, and revenue performance comparison between early vs late adopters.
                    The templates provide immediate implementation value regardless of platform choice.

#### Play: Cart Recovery Tactics from 47 Alcohol Merchants (PVP                     Public + Internal | Strong - Strong (9.0/10))

- **What's the play?**: Analyze cart abandonment patterns across the Q2 2024 TTB cohort and identify the 8 specific tactics that moved abandonment from 73% to 52%. Rank them by ROI, implementation complexity, and time to impact. Offer complete recovery playbook with email templates and timing sequences.
- **Why this works**: Uses the prospect's exact abandonment rate (73%) and shows the path to cohort average (52%). ROI ranking plus complexity means they can prioritize based on their resources. Email templates and timing sequences are immediately actionable. They get implementation value whether they buy or not.
- **Data Sources**:
  - TTB Wine Producer Permit List - permit_holder_name, permit_date
  - TTB Spirits Producer Permit List - permit_holder_name, permit_date
  - Company Internal Data - cart abandonment patterns, recovery tactics analysis, ROI by tactic, implementation templates
- **Outreach Message template**:
  ```text
  Subject: Cart recovery tactics from 47 alcohol merchants
  
  Analyzed cart abandonment patterns across your Q2 2024 TTB cohort - identified the 8 tactics that moved abandonment from 73% to 52%.
  
  Ranked them by ROI, implementation complexity, and time to impact.
  
  Want the recovery playbook with email templates and timing sequences?
  ```
- **Data Requirement**: This play assumes your company has:
                    Cart abandonment data by merchant, recovery tactic analysis showing which approaches work best, ROI and complexity scoring, and email/sequence templates from successful implementations.
                    This provides a complete playbook the recipient can implement with any platform.

---

## Rundoo (rundoo.ai)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/rundoo-ai)
**Strategic Summary**: Playbook combines public construction permit filings with internal transaction history to alert store owners when regular contractor customers file permits, predicting material needs before they order.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Modernize Your Hardware Store Operations

Hi Mike,

I noticed your store has been around for 15 years - congrats on that milestone!

Running a hardware store is challenging, especially when you're juggling inventory, customers, and payments all day. That's where Rundoo comes in.

Our all-in-one platform helps independent retailers like you:
✓ Track inventory in real-time
✓ Process payments faster
✓ Manage customer relationships
✓ Get business intelligence insights

We've helped 500+ stores modernize their operations. Would love to show you how we can help your store too.

Do you have 15 minutes next week for a quick call?

Best,
Sarah
```

### ✓ The New Way: GTM Plays

#### Play: Proactive Contractor Material Alerts (PVP                     Public + Internal | Strong - Strong (9.4/10))

- **What's the play?**: Cross-reference public construction permit filings with internal transaction history to predict exactly when specific contractors will need materials. Alert store owners with full contact details, job address, and material list before the contractor even places the order.
- **Why this works**: This is surveillance that helps them be proactive with THEIR customers. The full contact details (name, phone, email) mean they can call the contractor TODAY. The specific materials list and date show you've done the homework. This strengthens contractor relationships by anticipating needs.
- **Data Sources**:
  - State/County Construction Permit Databases - permit type, filing date, project address, contractor information
  - Internal Customer Transaction History - contractor purchasing patterns by job type
- **Outreach Message template**:
  ```text
  Subject: Thompson HVAC pulling permit tomorrow - needs materials March 22
  
  Thompson HVAC (Don, 405-555-1847, don@thompsonhvac.com) filed for 4-ton AC replacement at 892 Maple Ave yesterday.
  
  Based on their pattern, they'll need refrigerant, copper line sets, and condensate pumps on March 22.
  
  Should I flag when your regular contractors file permits?
  ```
- **Data Requirement**: This play combines public permit data with your historical transaction data showing contractor purchasing patterns by job type.
                    The synthesis of permit timing + contractor behavior patterns is unique to your business.

#### Play: Location-Based Fulfillment Optimization (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Identify large material orders from permit filings, then analyze which of the prospect's locations has sufficient inventory and proximity to fulfill efficiently. Alert them to fulfillment gaps where they have inventory at the wrong location.
- **Why this works**: The full contact info means they can call Mike TODAY. The specific quantity (800 2x4s) is actionable. The 340 vs 920 inventory split shows you see their actual stock. The 12 vs 31 minutes shows you mapped the routes. This helps them win large material orders by positioning inventory correctly.
- **Data Sources**:
  - State/County Construction Permit Databases - project address, start date, contractor details
  - Internal Real-Time Inventory Data - stock levels by SKU and location
  - Geographic Mapping - drive time from store locations to job sites
- **Outreach Message template**:
  ```text
  Subject: Baxter Construction needs 800 2x4s at Riverside site March 20
  
  Baxter Construction (Mike, mike@baxterconstruction.com, 214-555-8821) starts framing at 445 Industrial Blvd on March 20 - needs ~800 2x4x8s.
  
  Your Westside location is 12 minutes from the site but only stocks 340 studs - Eastside has 920 but that's 31 minutes away.
  
  Want me to flag these location-based fulfillment gaps?
  ```
- **Data Requirement**: This play requires real-time inventory visibility across all store locations plus geographic analysis capabilities.
                    The synthesis of permit data + inventory positioning + route mapping creates unique fulfillment intelligence.

#### Play: Cross-Location Stockout Alerts (PVP                     Internal Data | Strong - Strong (9.2/10))

- **What's the play?**: Track failed order requests and out-of-stock situations at each location, then cross-reference with inventory at other locations. Alert store owners when contractors are being turned away from one location while another location has plenty in stock.
- **Why this works**: Carlos is a REAL contractor they know - this is about THEIR actual customer. March 4 and 8 are specific dates they could verify. The 47 rolls at Westside shows the inventory IS there, just wrong location. This helps them prevent contractor attrition by fixing location-specific stockout patterns.
- **Data Sources**:
  - Internal Failed Order Tracking - out-of-stock requests by location, date, and customer
  - Internal Real-Time Inventory Data - stock levels by SKU across all locations
- **Outreach Message template**:
  ```text
  Subject: Martinez Plumbing requested PEX twice at Eastside - you're out
  
  Martinez Plumbing (Carlos, 512-555-2903) requested 1/2" PEX tubing at your Eastside location on March 4 and March 8 - both times out of stock.
  
  Your Westside store has 47 rolls but Carlos isn't driving 14 miles - he's probably switching suppliers.
  
  Should I send you these cross-location stockout alerts?
  ```
- **Data Requirement**: This play requires tracking failed orders, out-of-stock requests, and real-time inventory across all locations.
                    This is proprietary operational data only you have - competitors cannot replicate this insight.

#### Play: Permit-Driven Demand Forecasting (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Monitor construction permit filings in the store's service area, then use internal data on contractor purchasing patterns to predict when material demand will spike. Alert store owners with specific dates and product categories so they can stock appropriately.
- **Why this works**: 47 permits is specific and verifiable. The 18-day lead time shows you understand contractor behavior. March 21-28 gives them time to stock up. This helps them serve THEIR customers better by being prepared. The offer to share the permit list with project addresses and square footage adds immediate value.
- **Data Sources**:
  - State/County Construction Permit Databases - permit type, filing date, project location, square footage
  - Internal Transaction Analysis - time between permit filing and material purchase by trade type
- **Outreach Message template**:
  ```text
  Subject: 47 electrical permits filed in your zone last week
  
  47 commercial electrical permits filed within 8 miles of your store between March 3-10 - average material pull happens 18 days after filing.
  
  That means March 21-28 you'll see demand spikes for conduit, wire, and panels if contractors source locally.
  
  Want the permit list with project addresses and square footage?
  ```
- **Data Requirement**: This play combines public permit data with internal analysis of contractor purchasing timing patterns from your transaction history.
                    The 18-day lead time insight comes from analyzing when your contractor customers typically purchase after permit filing.

#### Play: Geographic Inventory Imbalance Analysis (PVP                     Internal Data | Strong - Strong (8.9/10))

- **What's the play?**: Analyze inventory distribution across multiple locations and identify SKUs that are overstocked at one location while generating failed orders at another. Quantify the revenue impact of these imbalances with specific examples.
- **Why this works**: Specific SKU and quantities show you're looking at their actual inventory. 8 lost requests is a real revenue leak they didn't know about. 11 miles is the actual distance between their locations. This directly impacts contractor retention. The offer to show top 15 products with this imbalance extends the value.
- **Data Sources**:
  - Internal Real-Time Inventory Data - stock levels by SKU and location
  - Internal Failed Order Tracking - unfulfilled requests by location and SKU
  - Geographic Data - distance between store locations
- **Outreach Message template**:
  ```text
  Subject: Your Northside store has 14 Kohler K-596 but Southside has 0
  
  Your Northside location stocks 14 Kohler K-596 faucets but your Southside store is out - Southside had 8 contractor requests last month that went unfilled.
  
  Contractors are driving 11 miles to Northside or buying elsewhere when they need it at Southside.
  
  Want the top 15 products with this imbalance?
  ```
- **Data Requirement**: This play requires real-time inventory visibility across locations plus failed order/request tracking to identify geographic imbalances.
                    This is proprietary operational intelligence only you have - competitors cannot see these inventory distribution inefficiencies.

#### Play: Construction Growth Proximity Intelligence (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Identify clusters of construction projects starting in specific areas, calculate which store location is closest, then alert owners to proactively position inventory where contractor demand will concentrate. Include contractor contacts and material profiles based on project types.
- **Why this works**: 6 projects with specific date range is actionable. 18 minutes is the REAL drive time difference. Material profiles means you've thought about what they need to stock. This helps them position inventory where demand is coming. The verification that permits are filed and contractors are identified adds credibility.
- **Data Sources**:
  - State/County Construction Permit Databases - project locations, start dates, contractor details
  - Geographic Mapping - drive time from store locations to project sites
  - Internal Transaction Patterns - typical material needs by project type
- **Outreach Message template**:
  ```text
  Subject: 6 commercial builds starting in Riverside - Westside is 18 min closer
  
  6 commercial construction projects breaking ground in Riverside between March 15-April 2 (permits filed, verified with contractors).
  
  Your Westside store is 18 minutes closer than Eastside for these sites - contractors will default to Westside for daily material runs.
  
  Want the project list with contractor contacts and material profiles?
  ```
- **Data Requirement**: This play combines public permit data, project timelines, and geographic analysis with your understanding of contractor purchasing patterns by project type.
                    The material profile prediction comes from analyzing what contractors typically purchase for similar project types.

#### Play: High-Frequency Contractor Payment Terms Analysis (PVP                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: Analyze contractor purchasing frequency and cross-reference with payment terms to identify cases where high-frequency buyers are on generous payment terms, creating cash flow inefficiencies. Quantify the working capital impact and provide specific contractor counts.
- **Why this works**: $67K is a specific, alarming number that gets attention. The 4+ times weekly detail shows you did homework. The solution (Net 15, deposits) is actionable. It feels like you're looking at their actual AR data. The cash flow implication ($67K tied up) is real and motivating.
- **Data Sources**:
  - Internal Transaction Database - purchase frequency and order value by contractor customer
  - Internal Accounts Receivable Data - payment terms, outstanding balances, days-to-payment by contractor
- **Outreach Message template**:
  ```text
  Subject: Your top 8 contractors owe $67K on Net 60
  
  Your 8 highest-volume contractors (buying 4+ times weekly) currently have $67K outstanding on Net 60 terms.
  
  They're treating your store like a line of credit while buying materials for active jobs - you could switch them to Net 15 or require deposits.
  
  Want their names and current balances?
  ```
- **Data Requirement**: This play requires aggregated accounts receivable data, purchase frequency tracking, and payment terms analysis across your contractor customer base.
                    This is proprietary financial intelligence only you have - competitors cannot see these cash flow optimization opportunities.

#### Play: Contractor Payment Terms Mismatch Alert (PVP                     Internal Data | Okay - Okay (7.8/10))

- **What's the play?**: Identify contractors who purchase very frequently (multiple times per week) but are on generous payment terms, creating situations where the store is essentially financing contractor working capital. Quantify the exposure per contractor.
- **Why this works**: This tells them something they can't easily see across their systems. The cash flow implication is real and specific to THEIR store. The 12 contractors number shows scale. Easy yes/no question makes response low-friction. However, without seeing actual data, the numbers might feel made up - less strong than the $67K version.
- **Data Sources**:
  - Internal Transaction Database - purchase frequency and order value by contractor
  - Internal Payment Terms Records - payment terms and outstanding AR by contractor
- **Outreach Message template**:
  ```text
  Subject: 12 contractors buying weekly but paying Net 60?
  
  I analyzed contractor purchase patterns at hardware stores in your region - 12 of your regulars buy 3+ times per week but you're extending Net 60 terms.
  
  That's $18K-$45K tied up per contractor while they're on your shelf weekly - you're financing their cash flow.
  
  Want the list with their weekly purchase frequency?
  ```
- **Data Requirement**: This play requires transaction-level data showing purchase frequency and payment terms by contractor customer.
                    The range ($18K-$45K) requires calculating typical outstanding AR for high-frequency contractor accounts.

---

## ShelfWise (shelfwise.ai)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/shelfwise-ai)
**Strategic Summary**: Playbook uses internal store execution data and public NDC product launch dates to identify which stores historically miss new SKU placements and build pre-launch audit schedules targeting the worst performers.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transform your retail execution

Hi {{FirstName}},

I noticed your company is focused on retail execution. At ShelfWise, we help CPG brands like yours ensure perfect shelf placement with AI-powered image recognition.

Our platform reduces audit time by 70% and gives you real-time visibility into planogram compliance across your entire retail network.

Are you available for a 15-minute call next week to discuss how we can help optimize your shelf execution?

Best,
ShelfWise SDR
```

### ✓ The New Way: GTM Plays

#### Play: Pre-Launch Audit Schedule for Slow-Executing Stores (PVP                     Public + Internal | Strong - Strong (9.3/10))

- **What's the play?**: Monitor public press releases announcing new product launches, then cross-reference against internal store execution performance data to identify the 120 highest-risk locations where new SKU placement historically fails. Build a complete 90-day pre-launch audit schedule prioritizing stores with 40% miss rates vs 12% chain average.
- **Why this works**: You're solving a problem the prospect didn't even know they had yet. The specificity of knowing which exact stores underperform on new SKU launches - before the launch happens - demonstrates proprietary intelligence they cannot get elsewhere. This is proactive consultative value, not reactive sales pitching.
- **Data Sources**:
  - Company press releases - new product launch announcements with dates and retail partners
  - Internal ShelfWise audit data - historical new SKU placement success rates by individual store location
- **Outreach Message template**:
  ```text
  Subject: Pre-launch audit schedule for your April rollout
  
  Your press release shows new migraine relief SKU launching April across CVS and Walgreens - built you a 90-day pre-launch audit schedule targeting the 120 slowest-executing stores in both chains.
  
  Those 120 stores miss 40% of new SKU deadlines vs. 12% chain average.
  
  Want the audit schedule with store priority rankings?
  ```
- **Data Requirement**: This play requires tracking new SKU placement success rates by individual store location across retail chains, showing which stores chronically underperform on launch execution.
                    This synthesis of public launch data + proprietary store performance patterns is unique to ShelfWise.

#### Play: New Product Launch Missing from Target Stores with Revenue Impact (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Cross-reference public NDC directory marketing_start_date with internal planogram compliance tracking to identify stores where new SKUs launched but never appeared on shelves. Calculate revenue impact using category velocity data. Deliver complete store list with district manager contacts.
- **Why this works**: Quantifying lost revenue from execution failures transforms this from "we think there's a problem" to "here's exactly how much money you're leaving on the table." The specificity of store count, revenue projection, and contact list makes this immediately actionable. This is consultative intelligence, not a sales pitch.
- **Data Sources**:
  - National Drug Code (NDC) Directory - marketing_start_date for new product launches
  - Internal ShelfWise planogram data - shelf placement timing by store location
  - Category velocity benchmarks - revenue projections based on product category
- **Outreach Message template**:
  ```text
  Subject: 23 Target stores still missing your Tylenol Cold launch
  
  Your Tylenol Cold + Flu Severe launched January 10 at Target, but 23 stores across Southeast region show no shelf placement as of February 15.
  
  Those stores represent $180K in projected Q1 revenue based on category velocity.
  
  Want the store addresses and district manager contacts?
  ```
- **Data Requirement**: This play requires tracking shelf placement timing across retail chains and category-based revenue projection models to calculate lost revenue from missing SKUs.
                    Combines public NDC launch data with proprietary execution tracking - a synthesis only ShelfWise can deliver.

#### Play: Portfolio Expansion Missing from Walmart Stores with Competitor Shelf Share Gain (PVP                     Public + Internal | Strong - Strong (9.0/10))

- **What's the play?**: Track new product category entries via NDC directory, then cross-reference against internal planogram tracking to identify stores where client's new SKUs are completely absent despite category resets completing. Show which competitor gained shelf facings during the same reset period. Deliver store list with planogram manager contacts.
- **Why this works**: Losing shelf space to a competitor during a portfolio expansion is painful and embarrassing. Quantifying the store count (340) and showing competitor gained facings during the same reset creates urgency - this isn't a delay, it's a competitive loss. The offer of planogram manager contacts makes this immediately actionable.
- **Data Sources**:
  - National Drug Code (NDC) Directory - new product launches and category expansion
  - Internal ShelfWise planogram data - category reset timing and competitor shelf share changes by store
- **Outreach Message template**:
  ```text
  Subject: Your digestive health gap at 340 Walmart stores
  
  Your portfolio expanded into digestive health Q3 2024, but 340 Walmart stores in Southern region show zero shelf presence for your 4 new SKUs despite category resets October-November.
  
  Pepto-Bismol gained 12 shelf facings during same resets at those locations.
  
  Want the store list with planogram manager emails?
  ```
- **Data Requirement**: This play requires tracking planogram changes and competitor shelf share movements during category resets by store location.
                    Competitive intelligence synthesis only ShelfWise can provide through systematic shelf audits.

#### Play: Portfolio Expansion Category Benchmark Gaps (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Track new product launches via NDC directory marketing_start_date, then compare recipient's shelf compliance metrics against aggregated category benchmarks from internal ShelfWise data. Show them their percentile ranking vs peer brands in same category and regional market. Identify specific underperforming stores.
- **Why this works**: Competitive benchmarking is always valuable, but category-specific benchmarks during portfolio expansion create urgency. Showing them they're at 45th percentile when category median is 72nd percentile - with the exact underperforming store list - demonstrates proprietary intelligence they cannot get from any competitor.
- **Data Sources**:
  - National Drug Code (NDC) Directory - new product launches showing portfolio expansion
  - Internal ShelfWise category benchmarks - aggregated planogram adherence, shelf share, out-of-stock rates by category and region
- **Outreach Message template**:
  ```text
  Subject: Built you a gap analysis for 215 CVS stores
  
  Cross-referenced your 8 new allergy SKUs against CVS planograms nationwide - 215 stores are missing 3+ of your products despite category resets in November.
  
  Those gaps represent 22% of your CVS distribution not executing on expansion.
  
  Want the store-by-SKU matrix with regional VP contacts?
  ```
- **Data Requirement**: This play requires aggregated shelf compliance metrics by OTC product category and regional market, with percentile benchmarks across 20+ brands in same category.
                    Proprietary benchmark data only ShelfWise possesses through systematic cross-brand audits.

#### Play: FDA Citation Stores vs Compliant Locations Audit Frequency Analysis (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Cross-reference openFDA Drug Enforcement Reports API showing specific store locations with enforcement actions against internal audit frequency data. Compare audit visit patterns at cited stores vs compliant locations. Show correlation between low audit frequency and citation risk. Deliver store-level audit frequency recommendations.
- **Why this works**: This isn't just mirroring the problem (FDA citations) - it's diagnosing root cause through data analysis. Showing that cited stores averaged 4.2 audits/year vs 8.7 at compliant ones, with quantified prevention opportunity (70%), transforms this into strategic consultation. You're helping them prevent future enforcement actions, not just react to past ones.
- **Data Sources**:
  - openFDA Drug Enforcement Reports API - specific store locations with enforcement actions
  - Internal ShelfWise audit frequency data - visit patterns by store location over time
- **Outreach Message template**:
  ```text
  Subject: Your 14 citation stores vs. compliant locations
  
  Compared your 14 FDA-cited stores against your 200+ compliant locations - cited stores average 4.2 shelf audits per year vs. 8.7 at compliant ones.
  
  Doubling audit frequency at high-risk stores could prevent 70% of future citations based on compliance correlation.
  
  Want the audit frequency analysis by store?
  ```
- **Data Requirement**: This play requires audit visit frequency patterns by store location and correlation analysis between audit frequency and compliance outcomes.
                    Root cause analysis synthesis combining public enforcement data with proprietary audit patterns.

#### Play: New Product Launch at Slow-Executing Retail Chains with Store-Level Gaps (PVP                     Public + Internal | Strong - Strong (8.7/10))

- **What's the play?**: Monitor NDC directory for new product marketing_start_date, then cross-reference against internal planogram compliance data showing which stores haven't completed shelf resets 30 days post-launch. Identify stores with historical slow execution patterns (45-60 days longer than chain average). Deliver complete store list with compliance manager contacts.
- **Why this works**: The specificity of knowing exact product name, launch date, store count, and regional breakdown demonstrates real research. Historical execution pattern data (47 stores taking 45-60 days longer) proves this isn't speculation - it's based on proprietary performance tracking. The offer of compliance manager contacts makes this immediately actionable.
- **Data Sources**:
  - National Drug Code (NDC) Directory - marketing_start_date showing new product launches
  - Internal ShelfWise planogram data - shelf reset timing and historical execution patterns by store
- **Outreach Message template**:
  ```text
  Subject: Your Advil launch at 47 lagging Kroger stores
  
  Your new Advil Migraine SKU launched March 15 at Kroger, but 47 stores in Ohio/Michigan region show zero shelf resets 30 days post-launch based on planogram compliance data.
  
  Those 47 stores historically take 45-60 days longer than chain average for new SKU placement.
  
  Want the store list with compliance manager contacts?
  ```
- **Data Requirement**: This play requires planogram compliance tracking data from existing retail customers showing shelf reset timing patterns and historical store-level execution performance.
                    Combines public launch data with proprietary execution intelligence only ShelfWise possesses.

#### Play: FDA Citation Stores Outside Field Coverage Zones (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Cross-reference openFDA Drug Enforcement Reports API showing specific stores with violations against inferred field team coverage patterns from audit frequency data. Identify stores falling outside active rep territories. Show structural gap causing compliance failures. Offer territory coverage optimization recommendations.
- **Why this works**: This isn't just listing FDA citations - it's diagnosing WHY the citations happened through territory analysis. Showing that 8 of 11 cited stores fall outside active coverage zones reveals a structural problem the prospect didn't know existed. The offer of territory adjustment recommendations positions this as strategic consultation, not sales outreach.
- **Data Sources**:
  - openFDA Drug Enforcement Reports API - specific store locations with violations
  - Internal ShelfWise audit data - inferred field team coverage patterns from audit frequency by territory
- **Outreach Message template**:
  ```text
  Subject: Mapped your FDA citation stores to field coverage
  
  Pulled the 11 stores from your September FDA citations and overlaid your field team territories - 8 stores fall outside active rep coverage zones.
  
  Those 8 locations have no scheduled audits in your Q4 visit calendar.
  
  Want the coverage gap map with suggested territory adjustments?
  ```
- **Data Requirement**: This play requires field team coverage patterns inferred from audit frequency data, showing which stores receive regular visits vs those outside active territories.
                    Territory analysis synthesis only possible through ShelfWise's systematic audit tracking.

#### Play: OTC Manufacturers with Recent FDA Enforcement Actions - Specific Store Citations (PQS                     Public Data | Strong - Strong (8.4/10))

- **What's the play?**: Query openFDA Drug Enforcement Reports API for recent warning letters and enforcement actions against OTC drug manufacturers. Filter for planogram violations and non-compliant shelf placement. Extract specific retail chain names, city locations, and store counts from enforcement records. Pull exact citation dates and corrective action deadlines (typically 30 days from warning letter date).
- **Why this works**: The specificity of city-level store locations (Philadelphia 3 stores, Boston 2 stores, Newark 1 store) combined with exact deadline dates creates verifiable urgency. This isn't generic FUD about FDA compliance - it's mirroring their exact regulatory pressure with documentary evidence. The simple yes/no question makes it easy to respond while acknowledging the situation.
- **Data Sources**:
  - openFDA Drug Enforcement Reports API - manufacturer_name, product_name, recall_date, recall_reason, distribution_pattern (includes store locations)
- **Outreach Message template**:
  ```text
  Subject: September FDA letters at your CVS locations
  
  Your CVS accounts in Philadelphia (3 stores), Boston (2 stores), and Newark (1 store) received FDA warning letters September 12-18 for OTC planogram violations.
  
  The 30-day corrective action deadline is October 18.
  
  Is your field team already auditing those 6 locations?
  ```

#### Play: New Product Launch Timing vs Slow Chain Execution at Seasonal Peak (PVP                     Public + Internal | Strong - Strong (8.2/10))

- **What's the play?**: Monitor press releases and NDC directory for new product launches with specific dates, then cross-reference against internal historical shelf reset timing data by retail chain. Identify launches at chains with slow execution (50+ days to complete resets). Calculate execution window vs seasonal sales peak to show timing risk. Question prompts field team pre-positioning.
- **Why this works**: Linking launch timing to seasonal sales peaks creates urgency - the 14-day execution window during allergy season is tight. Historical execution data (50+ days post-launch for these chains) proves this isn't speculation. The question about field team pre-positioning suggests a solution without pitching, making the recipient think "can we actually do that?"
- **Data Sources**:
  - Company press releases and NDC directory - product launch dates
  - Internal ShelfWise historical data - shelf reset timing patterns by retail chain for prior year launches
- **Outreach Message template**:
  ```text
  Subject: Your Claritin launch timing at slow chains
  
  Your new Claritin Eye SKU launches April 1 at Albertsons and Safeway - both chains historically take 50+ days post-launch to complete shelf resets based on prior year data.
  
  Allergy season peak buying is mid-April to early May, giving you 14-day execution window.
  
  Is your field team pre-positioning for faster placement?
  ```
- **Data Requirement**: This play requires historical shelf reset timing patterns by retail chain for category launches, showing median days to complete shelf placement after launch date.
                    Timing risk analysis combining public launch data with proprietary execution patterns.

#### Play: Portfolio Expansion Missing from Kroger Stores Despite Reset Completion (PQS                     Public + Internal | Strong - Strong (8.1/10))

- **What's the play?**: Track new product launches via NDC directory marketing_start_date showing portfolio expansion into new categories. Cross-reference against internal planogram compliance data showing stores where client's new SKUs are absent despite category resets completing chain-wide. Use Kroger's public reset completion rate to prove SKUs were excluded from resets, not just delayed.
- **Why this works**: The distinction between delay vs exclusion is critical - 85% reset completion chain-wide proves Kroger finished category resets, yet your SKUs are missing from 190 stores. This isn't a field execution problem, it's a merchandising relationship problem. The routing question targets the right person (merchandising contact) to fix it.
- **Data Sources**:
  - National Drug Code (NDC) Directory - marketing_start_date showing new product launches
  - Internal ShelfWise planogram data - category reset completion status and SKU presence by store
- **Outreach Message template**:
  ```text
  Subject: Your cough/cold expansion missing 190 Kroger stores
  
  Your portfolio added 6 cough/cold SKUs in Q4 2024, but 190 Kroger stores in Midwest show no placement as of January 15 despite category resets completing December 20.
  
  Kroger's compliance team reports 85% reset completion chain-wide, meaning your SKUs were excluded.
  
  Who's following up with Kroger merchandising?
  ```
- **Data Requirement**: This play requires category reset completion verification and SKU-level presence tracking by store location to distinguish between execution delays and merchandising exclusions.
                    Reset completion analysis only possible through ShelfWise's systematic planogram tracking.

#### Play: Portfolio Expansion with Shelf Share Loss to Competitor (PQS                     Public + Internal | Okay - Okay (7.9/10))

- **What's the play?**: Track new product category entries via NDC directory showing portfolio expansion. Cross-reference against internal shelf share tracking data showing loss of shelf facings to specific competitor during same quarter. Identify stores where new SKUs are absent from planograms. Question routing to person responsible for shelf execution.
- **Why this works**: Linking portfolio expansion to competitor shelf share gain creates competitive urgency - they expanded into pain relief but lost ground to Bayer during the same period. Specific percentages (34% to 26%, Bayer gained 6 points) and store count (180+ missing new product) make the problem concrete. Easy routing question makes response simple.
- **Data Sources**:
  - National Drug Code (NDC) Directory - new product launches showing portfolio expansion
  - Internal ShelfWise shelf share data - facings by brand and competitor across stores over time
- **Outreach Message template**:
  ```text
  Subject: Your pain relief shelf share dropped 8 points
  
  Your pain relief category shelf share at Walgreens dropped from 34% to 26% between Q3 and Q4 2024, while Bayer gained 6 points in same period.
  
  Your new arthritis cream launched Q4 but isn't showing in planogram data at 180+ stores.
  
  Is someone tracking the placement gaps?
  ```
- **Data Requirement**: This play requires shelf share tracking by category across retail chains, showing changes in facings over time and competitor movements during same period.
                    Competitive shelf intelligence only ShelfWise can provide through systematic audits.

#### Play: OTC Manufacturers with Recent FDA Enforcement Actions - General Targeting (PQS                     Public Data | Okay - Okay (7.8/10))

- **What's the play?**: Query openFDA Drug Enforcement Reports API for recent enforcement actions (recalls, warning letters) against OTC drug manufacturers. Filter for shelf placement and planogram compliance violations. Extract manufacturer name, retail chains mentioned in violation, and approximate timeframe. Reference 30-day corrective action deadlines typical of FDA warning letters.
- **Why this works**: FDA enforcement citations create real urgency with hard deadlines. Mentioning specific retail accounts (Walgreens, CVS, Rite Aid) and the 30-day response window demonstrates research and understanding of regulatory pressure. The routing question is easy to answer and helps reach the right person responsible for corrective actions.
- **Data Sources**:
  - openFDA Drug Enforcement Reports API - manufacturer_name, recall_reason, recall_date, distribution_pattern
- **Outreach Message template**:
  ```text
  Subject: FDA cited shelf placement at 3 accounts
  
  FDA enforcement letters from September 2024 flagged non-compliant OTC shelf placement at your Walgreens, CVS, and Rite Aid accounts in Northeast region.
  
  Each citation triggers mandatory corrective action plans with 30-day response deadlines to FDA.
  
  Who's coordinating the shelf audit responses?
  ```

---

## Shop By Payment (shopbypayment.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/shopbypayment-com)
**Strategic Summary**: Playbook uses internal shopping session data to identify vehicles in a dealer&#x27;s inventory that would hit the most popular payment filter ranges with term adjustments, turning browsing data into an actionable VIN list.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transform Your Digital Retail Experience

Hi [First Name],

I saw your dealership is hiring for digital marketing roles and wanted to reach out.

Shop By Payment helps dealerships like yours modernize the online shopping experience with transparent payment options. Our truPayments® engine provides real-time, personalized payment calculations that increase conversion rates.

We've helped dealerships across the country improve their mobile retail performance and compete with online retailers like Carvana and Vroom.

Would you be open to a 15-minute call to discuss how we can help [Dealership Name] drive more online conversions?

Best,
Sales Rep
```

### ✓ The New Way: GTM Plays

#### Play: Payment Term Mismatch - Regional Inventory Optimization (PVP                     Internal Data | Strong - Strong (9.3/10))

- **What's the play?**: Use aggregated shopping session data from your platform to show dealerships exactly which payment ranges their customers are filtering for, then identify which vehicles in their inventory could hit those payment targets with term adjustments.
                    This play reveals hidden conversion opportunities by matching existing inventory to actual customer demand patterns.
- **Why this works**: You're delivering an immediate action list (40 specific vehicles) based on their own customers' behavior. The specificity of the payment target ($289), shopper percentage (68%), and exact vehicle count creates instant credibility.
                    The dealer can implement this today without buying anything - just adjust term structure on identified VINs.
- **Data Sources**:
  - Shop By Payment Internal Data - Shopping session payment filters, inventory VIN data, term length modeling
- **Outreach Message template**:
  ```text
  Subject: $289 monthly puts 40 more vehicles in play
  
  Your Fort Worth inventory has 40 vehicles that would hit the $289 payment target (68% of your shoppers filter here) if you moved from 72 to 78-month terms.
  
  Right now those vehicles show $340-$365 monthly and get scrolled past.
  
  Want the VIN list with payment projections at 78 months?
  ```
- **Data Requirement**: This play requires aggregated shopping session data showing payment filter preferences by geography, plus inventory payment modeling at different term lengths.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Payment Term Mismatch - Conversion Rate Impact (PVP                     Internal Data | Strong - Strong (9.1/10))

- **What's the play?**: Analyze actual shopping sessions on the dealer's website to identify payment filter preferences, then show them the inventory gap between what customers want and what's available at standard terms.
                    The play provides both the problem diagnosis (only 12 vehicles match the 68% demand) and the solution (specific VINs that would match with term adjustments).
- **Why this works**: This is their own website data reflected back to them with surgical precision. The session count (847), filter percentage (68%), and inventory mismatch (12 vehicles) proves you've done deep analysis they likely haven't.
                    The VIN list offer is concrete and immediately actionable - they can validate your analysis and implement the fix within hours.
- **Data Sources**:
  - Shop By Payment Internal Data - Shopping session behavior, payment filter usage, inventory matching algorithms
- **Outreach Message template**:
  ```text
  Subject: $289/month sweet spot for your Fort Worth inventory
  
  Analyzed 847 shopping sessions on your site - 68% of customers filtering for $250-$325 monthly payments.
  
  Your current inventory has only 12 vehicles in that payment range with standard 72-month terms.
  
  Want the list of VINs that would hit $289 if you adjusted term structure?
  ```
- **Data Requirement**: This play requires shopping session tracking with payment filter preferences captured across dealer websites, plus inventory analysis capabilities.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Deal Completion Time Benchmarking - Abandonment Analysis (PVP                     Public + Internal | Strong - Strong (8.9/10))

- **What's the play?**: Track deal completion times for dealers using your platform, segment by dealer type (BHPH, franchise, size, geography), then identify where specific dealers are losing customers in their process.
                    This play pinpoints the exact stage where deals fall apart (F&I presentation) and quantifies the abandonment rate (23%).
- **Why this works**: You're revealing a hidden revenue leak with precise metrics. The 23% abandonment rate at a specific process stage is data they likely don't track themselves.
                    The peer comparison (15 similar dealers, 2.8 hour average) provides context that makes their 4.2 hours feel urgent. The stage-by-stage breakdown offer is exactly what they need to fix the problem.
- **Data Sources**:
  - Shop By Payment Internal Data - Deal flow timing, abandonment tracking by stage, dealer segmentation
  - State Motor Vehicle Dealer Licensing Boards - Dealer verification and classification
- **Outreach Message template**:
  ```text
  Subject: 23% abandon rate after F&I presentation starts
  
  Your Fort Worth location shows 23% deal abandonment after F&I presentation begins - that's 84 extra minutes vs the 2.8-hour Texas BHPH peer average.
  
  Compared 15 similar dealers and isolated where your process adds friction.
  
  Want the stage-by-stage timing breakdown with abandonment triggers?
  ```
- **Data Requirement**: This play requires deal flow tracking with stage-level timing and abandonment data, plus peer segmentation by dealer characteristics (type, size, geography).
                    Combined with state licensing data for dealer verification. This synthesis is unique to your platform.

#### Play: Deep Subprime Approval Rate vs Regional Delinquency Arbitrage (PVP                     Public + Internal | Strong - Strong (8.8/10))

- **What's the play?**: Cross-reference internal approval/decline data from your lender network with public delinquency statistics by geography to identify risk concentration patterns that dealers can't see in their own data.
                    This play reveals where dealers are approving customers in high-delinquency ZIP codes, creating portfolio risk exposure.
- **Why this works**: You're connecting two data points the dealer tracks separately (their approval behavior + regional delinquency trends) to surface hidden risk they would have missed.
                    The ZIP-level analysis offer is highly actionable - they can adjust underwriting criteria by geography or avoid specific territories to protect portfolio performance.
- **Data Sources**:
  - Shop By Payment Internal Data - Approval/decline rates by credit tier and geography
  - CFPB Auto Finance Data Pilot - Delinquency rates by geography and credit tier
- **Outreach Message template**:
  ```text
  Subject: 18.2% delinquency heat map for your 5-county footprint
  
  Harris County delinquency hit 18.2% last quarter while your deep subprime approvals run 34% above county BHPH average.
  
  That approval-delinquency gap signals potential portfolio risk in specific ZIPs within your coverage area.
  
  Want the ZIP-level breakdown showing where your approvals concentrate vs delinquency hotspots?
  ```
- **Data Requirement**: This play requires approval/decline tracking by geography and credit tier from your lender network, combined with CFPB public delinquency statistics.
                    This synthesis of internal approval patterns with public risk data is unique to your platform.

#### Play: Payment Term Mismatch - Inventory Conversion Analysis (PVP                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: Track payment filter behavior across dealer websites to identify shopper preferences by region and vehicle type, then model which existing inventory vehicles could match those preferences with term structure changes.
                    This play quantifies the exact conversion gap (68% demand vs 12 vehicles available) and provides a specific solution (40 vehicles that could fit with 78-month terms).
- **Why this works**: The specificity is overwhelming - 68% shopper preference, 12 current matches, 340-unit total inventory, 40 vehicles identified for term adjustment.
                    Every number is verifiable from their own data, and the solution (extend to 78 months) is immediately implementable without new inventory acquisition.
- **Data Sources**:
  - Shop By Payment Internal Data - Payment filter usage, inventory analysis, term modeling
- **Outreach Message template**:
  ```text
  Subject: 68% of your shoppers filtering $250-$325 payments
  
  Your Fort Worth site shows 68% of shoppers using payment filters between $250-$325.
  
  Only 12 vehicles in your 340-unit inventory hit that range at standard terms.
  
  Want me to show which 40 vehicles would fit if you extended to 78 months?
  ```
- **Data Requirement**: This play requires payment filter tracking across dealer websites with inventory matching capabilities and term structure modeling.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Deal Completion Time Benchmarking by Peer Segment (PVP                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Track deal completion times from test drive to signature across dealers using your platform, segment by true peer characteristics (dealer type, size, geography), then identify process bottlenecks for specific dealers.
                    This play provides peer benchmarking that's actually relevant (15 comparable Texas BHPH dealers) rather than generic averages.
- **Why this works**: The peer comparison is genuinely useful - not all dealers, but 15 comparable BHPH dealers in Texas. The 4.2 vs 2.8 hour differential is specific and actionable.
                    The 23% abandonment rate tied to a specific stage (F&I presentation) gives them a concrete target for improvement. The time breakdown offer is exactly what they need to diagnose the problem.
- **Data Sources**:
  - Shop By Payment Internal Data - Deal completion timing, stage-level tracking, abandonment rates
  - State Motor Vehicle Dealer Licensing Boards - Dealer classification and verification
- **Outreach Message template**:
  ```text
  Subject: Your 4.2-hour deal time vs 2.8-hour peer average
  
  Tracked deal completion times for 15 comparable BHPH dealers in Texas - average is 2.8 hours from test drive to signature.
  
  Your Fort Worth location averages 4.2 hours, and 23% of deals abandon after F&I presentation starts.
  
  Want the breakdown of where those 84 extra minutes are going?
  ```
- **Data Requirement**: This play requires comprehensive deal flow timing data from quote through completion, with peer segmentation by dealer characteristics.
                    Combined with state licensing data for accurate peer matching. This synthesis is unique to your platform.

#### Play: Deep Subprime Approval Rate vs Regional Delinquency Arbitrage (PVP                     Public + Internal | Strong - Strong (8.4/10))

- **What's the play?**: Compare dealer approval rates by credit tier against regional delinquency patterns to identify risk mismatches - dealers approving customers at higher rates in geographies with elevated delinquency.
                    This play reveals a counterintuitive opportunity or hidden risk depending on the dealer's situation.
- **Why this works**: You're showing them a pattern they can't see in their own data - their approval rate differential (34 points above average) combined with geographic delinquency context (18.2% in Harris County).
                    The delinquency heat map offer provides immediate risk management value they can use to adjust underwriting criteria by territory.
- **Data Sources**:
  - Shop By Payment Internal Data - Approval rates by credit tier and geography
  - CFPB Auto Finance Data Pilot - Regional delinquency statistics
- **Outreach Message template**:
  ```text
  Subject: Your subprime approvals outpacing Harris County delinquency
  
  Your deep subprime approval rate is 34% higher than typical BHPH dealers in Harris County, where delinquency just hit 18.2%.
  
  That gap means you're approving customers other dealers reject - but those customers are statistically more likely to default in this ZIP.
  
  Want the delinquency heat map for your coverage area?
  ```
- **Data Requirement**: This play requires approval rate tracking by credit tier and geography from dealers using your platform, combined with CFPB public delinquency data.
                    This synthesis of internal approval patterns with public risk metrics is unique to your platform.

#### Play: Payment Term Mismatch - Shopping Session Analysis (PQS                     Internal Data | Strong - Strong (8.1/10))

- **What's the play?**: Track payment filter behavior across dealer websites to quantify shopper demand patterns, then mirror that data back to dealers with the inventory gap clearly identified.
                    This PQS variant focuses on reflection rather than solution delivery - showing the dealer their own data in a way that reveals the problem.
- **Why this works**: The session count (847) and filter percentage (68%) demonstrate you have visibility into their website behavior. The inventory gap (12 vehicles vs 68% demand) is a clear problem statement.
                    The routing question is straightforward and non-threatening - just asking if the inventory manager has this visibility, which they likely don't.
- **Data Sources**:
  - Shop By Payment Internal Data - Shopping session tracking, payment filter preferences
- **Outreach Message template**:
  ```text
  Subject: 847 shopping sessions filtering $250-$325 payments
  
  Last 30 days show 847 shopping sessions on your Fort Worth site with 68% filtering for $250-$325 monthly payments.
  
  Your inventory has 12 vehicles matching that range at standard 72-month terms.
  
  Is your inventory manager seeing this payment filter data?
  ```
- **Data Requirement**: This play requires shopping session tracking with payment filter preference capture across dealer websites.
                    This is proprietary data only you have - competitors cannot replicate this play.

#### Play: Deal Completion Time Benchmarking - Process Bottleneck (PQS                     Public + Internal | Strong - Strong (8.0/10))

- **What's the play?**: Compare dealer deal completion times against peer benchmarks, identify the specific process stage where delays occur, then mirror that data back with a simple routing question.
                    This PQS variant focuses on reflection and awareness-building rather than delivering the full diagnostic.
- **Why this works**: The peer comparison (2.8 hours for comparable Texas BHPH dealers) provides useful context. The 84 extra minutes quantifies waste, and identifying the F&I presentation stage adds urgency.
                    The routing question is non-threatening and likely to surface an internal communication gap - the F&I manager probably doesn't know about the 2.8-hour peer benchmark.
- **Data Sources**:
  - Shop By Payment Internal Data - Deal completion timing by stage and dealer segment
  - State Motor Vehicle Dealer Licensing Boards - Dealer classification for peer matching
- **Outreach Message template**:
  ```text
  Subject: 84 extra minutes per deal at Fort Worth location
  
  Your Fort Worth location averages 4.2 hours per deal completion vs 2.8 hours for comparable Texas BHPH dealers.
  
  That's 84 extra minutes per transaction, and abandonment spikes at the F&I presentation stage.
  
  Is your F&I manager aware of the 2.8-hour peer benchmark?
  ```
- **Data Requirement**: This play requires deal completion metrics tracked across platform users, segmented by dealer type for accurate peer benchmarking.
                    Combined with state licensing data for dealer classification. This synthesis is unique to your platform.

#### Play: Deep Subprime Approval Rate vs Regional Delinquency Arbitrage (PQS                     Public + Internal | Okay - Okay (7.9/10))

- **What's the play?**: Mirror back the dealer's approval rate differential compared to market average, combined with regional delinquency context, to surface potential risk exposure they may not be monitoring.
                    This PQS variant asks a routing question to determine who owns the risk monitoring function.
- **Why this works**: The approval differential (34 percentage points) and delinquency statistic (18.2% in Q4) are both specific and verifiable. The question about monitoring correlation is reasonable and non-threatening.
                    Slight risk of sounding accusatory, but the data specificity should overcome that concern.
- **Data Sources**:
  - Shop By Payment Internal Data - Approval rates by credit tier
  - CFPB Auto Finance Data Pilot - Regional delinquency statistics
- **Outreach Message template**:
  ```text
  Subject: Your approvals 34 points above Harris County average
  
  Deep subprime approval rate at your dealership runs 34 percentage points higher than Harris County BHPH average.
  
  County delinquency climbed to 18.2% in Q4 - highest in your 5-county footprint.
  
  Who's monitoring the correlation between your approval criteria and regional default patterns?
  ```
- **Data Requirement**: This play requires approval rate tracking by credit tier from dealers using your platform, combined with CFPB public delinquency data by geography.
                    This synthesis of internal approval metrics with public risk data is unique to your platform.

#### Play: Deep Subprime Approval Rate vs Regional Delinquency Arbitrage (PQS                     Public + Internal | Okay - Okay (7.8/10))

- **What's the play?**: Reflect the dealer's approval rate performance against regional benchmarks, paired with delinquency context, to surface risk patterns they may not be tracking.
                    This PQS variant focuses on mirroring the situation with a simple routing question about F&I team awareness.
- **Why this works**: The approval differential (34 points) and delinquency statistic (18.2%) provide specific context. The routing question about F&I team tracking is straightforward.
                    Slightly weaker than other variants due to the more generic question structure, but still demonstrates data visibility the dealer likely lacks.
- **Data Sources**:
  - Shop By Payment Internal Data - Approval rates by credit tier and geography
  - CFPB Auto Finance Data Pilot - Regional delinquency statistics
- **Outreach Message template**:
  ```text
  Subject: 34% approval gap vs 18.2% delinquency in your market
  
  Your deep subprime approval rate exceeds Harris County BHPH average by 34 points.
  
  Local delinquency hit 18.2% last quarter - highest in your 5-county footprint.
  
  Is your F&I team tracking the approval-to-delinquency correlation?
  ```
- **Data Requirement**: This play requires approval rate data from dealers using your platform, combined with CFPB regional delinquency statistics.
                    This synthesis of internal approval patterns with public risk metrics is unique to your platform.

#### Play: Deep Subprime Approval Rate vs Regional Delinquency Arbitrage (PQS                     Public + Internal | Okay - Okay (7.7/10))

- **What's the play?**: Mirror the dealer's approval rate differential against market benchmarks, combined with regional delinquency context, to surface potential risk exposure.
                    This PQS variant asks who owns the monitoring function to determine organizational responsibility.
- **Why this works**: The specific approval differential (34 percentage points) and delinquency statistic (18.2%) demonstrate data visibility. The question about monitoring correlation is organizational and non-threatening.
                    Slight risk of sounding accusatory with the "who's monitoring" framing, but the data specificity should overcome that.
- **Data Sources**:
  - Shop By Payment Internal Data - Approval rates by credit tier
  - CFPB Auto Finance Data Pilot - Regional delinquency data
- **Outreach Message template**:
  ```text
  Subject: Your approvals 34 points above Harris County average
  
  Deep subprime approval rate at your dealership runs 34 percentage points higher than Harris County BHPH average.
  
  County delinquency climbed to 18.2% in Q4 - highest in your 5-county footprint.
  
  Who's monitoring the correlation between your approval criteria and regional default patterns?
  ```
- **Data Requirement**: This play requires approval rate tracking by credit tier from your platform, combined with CFPB public delinquency statistics.
                    This synthesis of internal approval data with public risk metrics is unique to your platform.

---

## The AutoMiner (theautominer.com)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/theautominer-com)
**Strategic Summary**: The playbook cross-references internal service DMS records with sales CRM data to identify dealership service-only customers never targeted for vehicle sales, and correlates service timing patterns with promotional campaign calendars to surface timing misalignments.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Transform Your Dealership's Customer Data

Hi [First Name],

I noticed your dealership has been growing and wanted to reach out about how we help dealerships like yours consolidate customer data across CRM, DMS, and multiple touchpoints.

TheAutoMiner is an award-winning CDP that unifies fragmented customer profiles and activates first-party data for targeted campaigns. We work with BMW, Audi, and other leading brands.

Our platform offers:
• Automated data hygiene and deduplication
• Direct integration with Meta and Google
• Multi-channel campaign deployment
• 2023 AWA Award winner

Would you be open to a quick call next week to discuss how we can help you maximize marketing ROI?

Best,
[SDR Name]
```

### ✓ The New Way: GTM Plays

#### Play: Play: Hidden Audience Expansion Opportunity (PVP                     Internal Data | Strong - Strong (9.3/10))

- **What's the play?**: Identify dealerships with service-only customers who have never been targeted for sales. These are high-trust prospects the dealership is completely ignoring for vehicle sales opportunities.
- **Why this works**: This reveals a massive blind spot in the dealership's marketing strategy. Service trust transferring to sales is psychologically compelling, and adding trade-in timing makes it immediately actionable. The specific number (1,847) makes the opportunity tangible and urgent.
- **Data Sources**:
  - Company Internal Data - service DMS records cross-referenced with sales CRM to identify customers in one system but not the other
- **Outreach Message template**:
  ```text
  Subject: You're sitting on 1,847 service-only customers
  
  Your service department has 1,847 customers with no sales purchase record in your CRM.
  
  These people trust your service bay but you've never marketed vehicles to them.
  
  Want the list with their current vehicle age and likely trade-in timing?
  ```
- **Data Requirement**: This play assumes AutoMiner can identify customers who exist in the service DMS but not in the sales CRM, representing hidden audience expansion opportunities.
                    This is proprietary cross-system analysis only AutoMiner can provide by unifying fragmented dealership data.

#### Play: Play: Service Campaign Timing Misalignment (PVP                     Public + Internal | Strong - Strong (9.1/10))

- **What's the play?**: Analyze dealership service records to identify when customers actually need services (tire rotations, oil changes) and compare against when the dealership runs promotional campaigns. Surface timing gaps that cause wasted ad spend.
- **Why this works**: This is genuinely valuable insight the marketing director can't get elsewhere. The specificity of analyzing their actual service patterns (67% need tires in June-July) combined with campaign timing data proves this isn't guessing. It explains underperformance and provides a clear path to improvement.
- **Data Sources**:
  - Internal Service Records - tire rotation dates, service completion records
  - NADA Research Data (public) - typical service intervals for validation
- **Outreach Message template**:
  ```text
  Subject: Your tire promo timing misses peak need by 6 weeks
  
  Your tire promotion runs August-September, but your service records show 67% of customers need tires in June-July based on last rotation dates.
  
  You're promoting after most customers already bought elsewhere.
  
  Want the optimal campaign calendar based on your actual service cycles?
  ```
- **Data Requirement**: This play requires access to service records to calculate tire rotation cycles and compare against current marketing campaign timing from email/CRM data.
                    Combined with public manufacturer guidelines to validate intervals. This synthesis is unique to AutoMiner's platform.

#### Play: Play: Brake Service Seasonal Clustering (PVP                     Internal Data | Strong - Strong (8.8/10))

- **What's the play?**: Aggregate service completion records by category and month to identify seasonal demand patterns. Show dealerships when natural demand peaks for each service type so they can time campaigns optimally.
- **Why this works**: 68% in two months is a striking seasonal pattern that makes timing misalignment obvious. Offering month-by-month breakdowns for all service categories positions AutoMiner as the data intelligence partner who can optimize the entire campaign calendar, not just fix one issue.
- **Data Sources**:
  - Company Internal Data - service completion records aggregated by category and month across 24 months
- **Outreach Message template**:
  ```text
  Subject: Your brake customers cluster in November-December
  
  68% of your brake service completions happen in November-December based on 24 months of records.
  
  But your brake promotions run March-April when natural demand is lowest.
  
  Want the month-by-month service pattern breakdown for all categories?
  ```
- **Data Requirement**: This play assumes AutoMiner can aggregate service completion records by category and month to identify seasonal demand patterns that inform campaign timing.
                    Only AutoMiner sees this pattern across unified service data - competitors cannot replicate this analysis.

#### Play: Play: Competitor Vehicle Owners in Service Bay (PVP                     Internal Data | Strong - Strong (8.7/10))

- **What's the play?**: Parse service records to identify customers servicing competitor brand vehicles at the dealership's service department. These are warm leads - already comfortable with the dealership's team, just driving the wrong brand.
- **Why this works**: The insight that they can identify competitor brand owners in the dealership's own service records is clever and non-obvious. Vehicle age segmentation shows understanding of the sales process. These are genuinely warm leads the sales team is completely missing.
- **Data Sources**:
  - Company Internal Data - service records parsed to identify vehicle makes/models being serviced
- **Outreach Message template**:
  ```text
  Subject: 289 of your service customers drive competitor brands
  
  I found 289 customers servicing non-[brand] vehicles at your shop based on service records.
  
  They're already comfortable with your team - just driving the wrong logo.
  
  Want me to segment them by vehicle age for your trade-in campaigns?
  ```
- **Data Requirement**: This play assumes AutoMiner can parse service records to identify vehicle makes/models being serviced that don't match the dealership's brand, revealing competitor vehicle owners.
                    This cross-sell opportunity is hidden in plain sight in the dealership's data - only visible through AutoMiner's unified platform.

#### Play: Play: Post-Sale Service Inquiry Waste (PQS                     Public + Internal | Strong - Strong (8.6/10))

- **What's the play?**: Cross-reference service completion records from DMS against email marketing campaign recipient lists to identify customers who received promotional campaigns after they already purchased the service. Shows concrete waste in marketing budget.
- **Why this works**: This demonstrates concrete waste in the marketing budget with a specific number (412 customers). The synthesis of service records + campaign data is non-obvious and requires unified data systems. The easy yes/no question makes responding frictionless.
- **Data Sources**:
  - Internal Service Records - service completion dates by category
  - Internal Marketing Data - email campaign recipient lists and send dates
- **Outreach Message template**:
  ```text
  Subject: June tire customers got your September promo
  
  I cross-referenced your tire service records with your email campaign dates - 412 customers who bought tires in June received your tire promotion in September.
  
  That's wasted ad spend targeting customers who already converted.
  
  Should I send you the breakdown by service type?
  ```
- **Data Requirement**: This play requires AutoMiner to match service completion records from DMS against email marketing campaign recipient lists to identify timing mismatches.
                    This synthesis requires unified data access across service and marketing systems - exactly what AutoMiner provides.

#### Play: Play: Overdue Oil Changes (PVP                     Internal Data | Strong - Strong (8.5/10))

- **What's the play?**: Track service intervals from DMS records and calculate overdue status based on manufacturer recommendations. Surface customers whose oil changes are severely overdue as at-risk engines.
- **Why this works**: 847 days combined is creative math that emphasizes urgency. The "at-risk engines" angle positions this as customer care rather than just sales outreach. Prioritization by days overdue shows actionable thinking. 73 customers is manageable volume for actual follow-up.
- **Data Sources**:
  - Company Internal Data - service interval tracking from DMS records with manufacturer maintenance schedules
- **Outreach Message template**:
  ```text
  Subject: Your oil change customers are overdue by 847 days combined
  
  You have 73 customers whose last oil change was 6+ months ago - that's 847 total days overdue.
  
  These aren't lost customers, they're at-risk engines driving around your market.
  
  Want me to send you their contact info prioritized by days overdue?
  ```
- **Data Requirement**: This play assumes AutoMiner can track service intervals from DMS records and calculate overdue status based on manufacturer recommendations.
                    This customer care insight helps prevent vehicle damage while creating re-engagement opportunities - unique to AutoMiner's service data visibility.

#### Play: Play: Lapsed Service Customers (PVP                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: Identify customers who completed service 6+ months ago but never rescheduled. These are low-hanging fruit - they already trust the service department, just need re-engagement. Prioritize by customer lifetime value for maximum impact.
- **Why this works**: This is specific and immediately actionable - the service director could call these customers today. The "already trust your service" positioning is smart. Top 50 prioritization shows understanding that they can't call 342 people, so focus on highest value. Easy yes/no response removes friction.
- **Data Sources**:
  - Company Internal Data - service completion history from DMS with customer lifetime value calculations
- **Outreach Message template**:
  ```text
  Subject: 342 service customers haven't scheduled their next visit
  
  You have 342 customers who completed service 6+ months ago but never rescheduled.
  
  These are low-hanging fruit - they already trust your service department.
  
  Want me to send you the top 50 highest-value customers from this list?
  ```
- **Data Requirement**: This play assumes AutoMiner has consolidated customer service history from the DMS to identify lapsed service customers and calculate lifetime value.
                    Only AutoMiner can prioritize by customer value across unified data - this isn't possible with fragmented systems.

#### Play: Play: Multi-Vehicle Households (PVP                     Internal Data | Strong - Strong (8.4/10))

- **What's the play?**: De-duplicate customers across service records by contact info to identify multi-vehicle households being treated as separate customers. Enable household-level marketing instead of vehicle-level campaigns.
- **Why this works**: 312 multi-vehicle households represent significant expansion potential. Household marketing vs single vehicle targeting is smart positioning that shows understanding of modern marketing best practices. Fleet mapping would genuinely help personalize campaigns and reduce waste by treating households as units.
- **Data Sources**:
  - Company Internal Data - service records de-duplicated by contact information to identify multi-vehicle households
- **Outreach Message template**:
  ```text
  Subject: 312 service customers own multiple vehicles
  
  I found 312 customers in your service records who've brought in 2+ different vehicles.
  
  You're only marketing to them based on one vehicle - missing the household opportunity.
  
  Want me to map out their full household fleet for targeted campaigns?
  ```
- **Data Requirement**: This play assumes AutoMiner can de-duplicate customers across service records by contact info to identify multi-vehicle households.
                    Household-level marketing requires unified customer data - exactly the core value AutoMiner provides to dealerships.

#### Play: Play: Scheduling Drop-Off Leak (PQS                     Internal Data | Strong - Strong (8.3/10))

- **What's the play?**: Track service inquiry volume (phone, web, chat) and compare against scheduled appointments to calculate conversion drop-off rate. Identify the leak in the funnel where inquiries go cold before becoming appointments.
- **Why this works**: 23% drop-off is specific and concerning. The math converting to 43 appointments and $21,500 makes it tangible and urgent. The question about tracking shows understanding of process gaps. This identifies a fixable operational leak the service director should address immediately.
- **Data Sources**:
  - Company Internal Data - service inquiry tracking (phone, web, chat) compared against scheduled appointments
- **Outreach Message template**:
  ```text
  Subject: You're losing 23% of service inquiries at scheduling
  
  Your service inquiry volume is 187/month but only 144 appointments get scheduled - 23% drop-off rate.
  
  That's 43 lost appointments monthly, potentially $21,500 in lost RO revenue.
  
  Is someone tracking where these inquiries go cold?
  ```
- **Data Requirement**: This play assumes AutoMiner can track service inquiry volume (phone, web, chat) and compare against scheduled appointments to calculate conversion drop-off.
                    This operational visibility requires unified data across inquiry channels and scheduling systems - only possible with AutoMiner's CDP.

#### Play: Play: Thursday Capacity Gap (PQS                     Internal Data | Strong - Strong (8.2/10))

- **What's the play?**: Analyze appointment scheduling patterns across days of the week to identify capacity utilization gaps. Show service directors when they're turning away high-demand customers while low-demand slots sit empty.
- **Why this works**: 43% vs 89% capacity is a striking inefficiency visualization. This addresses operational optimization, not just marketing - showing broader value. Identifying who handles routing is smart because it targets the right stakeholder for process change. Easy question to answer.
- **Data Sources**:
  - Company Internal Data - appointment scheduling patterns analyzed by day of week to identify capacity utilization
- **Outreach Message template**:
  ```text
  Subject: Your Thursday service slots sit empty
  
  Your service department runs at 43% capacity on Thursdays versus 89% on Saturdays based on appointment data.
  
  You're turning away Saturday customers while Thursday bays sit empty.
  
  Who handles your service appointment routing?
  ```
- **Data Requirement**: This play assumes AutoMiner can analyze appointment scheduling patterns across days of the week to identify capacity utilization gaps.
                    This operational intelligence helps optimize service department revenue - only visible through AutoMiner's unified scheduling data.

#### Play: Play: Parts Counter Walk-Ins (PQS                     Internal Data | Strong - Strong (8.1/10))

- **What's the play?**: Access parts department transaction records and cross-reference against CRM/DMS to identify customers not in marketing databases. These are DIY customers and independent mechanic clients the dealership is completely ignoring for marketing opportunities.
- **Why this works**: 94 monthly walk-ins is significant volume being ignored. The DIY/indie mechanic segmentation is smart - these are real audience segments with different needs. Parts invoices having contact info is realistic. This opens a genuinely new audience the marketing director hadn't considered.
- **Data Sources**:
  - Company Internal Data - parts department transaction records cross-referenced against CRM/DMS customer databases
- **Outreach Message template**:
  ```text
  Subject: Your parts counter sees 94 walk-ins monthly
  
  Your parts department logs 94 walk-in customers monthly who aren't in your service or sales databases.
  
  These are DIY customers or indie mechanic clients you're not marketing to.
  
  Should I pull the contact info from parts invoices?
  ```
- **Data Requirement**: This play assumes AutoMiner can access parts department transaction records and cross-reference against CRM/DMS to identify customers not in marketing databases.
                    This hidden audience expansion opportunity requires unified data across all dealership departments - exactly AutoMiner's core capability.

---

## Waltsco (waltsco.ca)

**Showcase URL**: [Full Blueprint Playbook](https://playbooks.blueprintgtm.com/waltsco-ca)
**Strategic Summary**: The playbook targets Amazon Canada NHP sellers using Health Canada&#x27;s LNHPD database to identify products with licensed NPNs that are missing required bilingual labeling elements on their Amazon listings ahead of CFIA enforcement.

### ✕ The Old Way (Generic Outreach)
```text
Subject: Quick question about your Amazon Canada strategy

Hi [First Name],

I noticed you're selling on Amazon Canada—congrats on entering the marketplace!

At Waltsco, we help brands like yours optimize their Amazon presence to drive more sales. We've helped companies see 30-400% growth through our listing optimization and PPC management services.

Our full-service account management includes:
- Listing optimization & A+ content
- PPC advertising management
- Catalog audits & keyword research
- Brand protection

Would you have 15 minutes next week to explore how we can help grow your Amazon Canada business?

Best,
Generic SDR
```

### ✓ The New Way: GTM Plays

#### Play: Play 1: NHP Amazon Sellers Missing Compliance Labels (PQS | Strong - 7.8/10)

- **What's the play?**: Target Amazon Canada sellers of Natural Health Products (NHPs) whose listings don't display required Health Canada compliance information. Health Canada requires all NHPs to display their Natural Product Number (NPN) and bilingual labeling. Amazon Canada sellers often miss this, creating compliance risk and potential listing suppression.
- **Why this works**: You're citing their specific NPN from Health Canada's official database—a number they had to apply for and wait months to receive. When you reference their exact product with its 8-digit NPN and point out what's missing from their Amazon listing, you demonstrate you've done real research. This isn't a generic "compliance" pitch—it's their product, their NPN, their gap.
- **Outreach Message template**:
  ```text
  Subject: NPN 80123456 listing gap
  
  Your "Vitamin D3 2000IU" with NPN 80123456 is live on Amazon Canada, but the listing is missing the required French dosage instructions from your Health Canada approval.
  
  CFIA's bilingual labeling enforcement increased 40% in Q4 2025—NHP listings without French text are getting flagged.
  
  Want me to send you the exact text from your LNHPD record to add?
  ```

#### Play: Play 2: Import Volume Surge Without Listing Updates (PQS | Okay - 7.2/10)

- **What's the play?**: Target Amazon sellers who show significant import volume increases in US customs data but haven't updated their Amazon listings to reflect new products or inventory capacity. A surge in imports often means new SKUs or restocking—but without optimized listings, that inventory sits.
- **Why this works**: Import data is public but most Amazon sellers don't know competitors (or you) can see it. When you reference their specific supplier name and shipment counts from customs records, you demonstrate intelligence they didn't expect anyone to have. The insight—import velocity without listing velocity—is non-obvious and actionable.
- **Outreach Message template**:
  ```text
  Subject: 23 shipments from Shenzhen
  
  Your customs records show 23 sea shipments from Shenzhen Huawei Electronics in the past 90 days—up from 8 in the same period last year.
  
  Your Amazon storefront still shows 47 SKUs. Are the new imports going live soon, or sitting in FBA limbo?
  
  Need help with listing optimization for the new products?
  ```

#### Play: Play 1: Complete NHP Listing Compliance Audit (PVP | Strong - 8.0/10)

- **What's the play?**: Deliver a ready-to-use compliance checklist for their specific NHP products. Pull their approved Health Canada text (warnings, dosage, contraindications) and compare it against what's actually on their Amazon listing. Give them the exact copy they need to add—in both English and French—before you ask for anything.
- **Why this works**: You're doing 2-3 hours of compliance work for free. They can copy-paste the French text you provide directly into their listing. Whether they hire Waltsco or not, you've demonstrated exactly what kind of value you deliver. Most will think: "If this is what they give away free, what do they do when I pay them?"
- **Outreach Message template**:
  ```text
  Subject: Your missing French label text
  
  I pulled your NPN 80123456 record from Health Canada. Your Amazon listing is missing three required French elements:
  
  1. Dosage: "Prendre 1 capsule par jour avec de la nourriture"
  2. Caution: "Consulter un praticien de soins de santé si vous êtes enceinte ou si vous allaitez"
  3. Contraindication: "Ne pas utiliser si vous prenez des anticoagulants"
  
  Copy-paste ready. Want the full bilingual label breakdown for your other 12 NPNs?
  ```

#### Play: Play 2: Supplier Diversification Analysis (PVP | Okay - 7.5/10)

- **What's the play?**: Analyze their import records to show supplier concentration risk. If 80%+ of their shipments come from one supplier, they're vulnerable to delays, price increases, and quality issues. Provide a list of alternative suppliers who ship the same HS codes to competitors.
- **Why this works**: Supply chain is every Amazon seller's anxiety in 2026. When you show them they're 85% dependent on one supplier—and name three alternatives their competitors use—you're delivering consulting-level insight for free. The implicit message: Waltsco understands the whole Amazon ecosystem, not just listings.
- **Outreach Message template**:
  ```text
  Subject: 85% supplier risk
  
  Your import records show 85% of your 2025 shipments came from Shenzhen Huawei Electronics.
  
  Three of your Amazon competitors split their sourcing across 3-4 suppliers. One alternative for your HS code 8471.30: Dongguan Lianxing—they ship to 12 US importers in your category with faster port times.
  
  Want the full supplier diversification analysis?
  ```

---

