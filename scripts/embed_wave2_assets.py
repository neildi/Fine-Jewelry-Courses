import os

def embed_image_if_not_present(filepath, marker, image_block):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    first_line_of_block = [line for line in image_block.strip().split('\n') if '<img' in line][0]
    src_match = [part for part in first_line_of_block.split() if 'src=' in part][0]
    if src_match in content:
        print(f"Already embedded {src_match} in {filepath}")
        return

    if marker in content:
        new_content = content.replace(marker, f"{marker}\n\n{image_block}\n", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully embedded into {filepath}")
    else:
        print(f"Marker '{marker}' not found in {filepath}")

embeddings = [
    # C3
    ("courses/C3-clienteling-and-crm/articles/M01-client-profile-what-to-capture-what-to-leave-out.md",
     "## The seven fields worth capturing from nearly every client",
     """<figure>
  <img src="../assets/c3-m01-client-profile-data-architecture.svg" alt="Client Profile Data Architecture" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> Client Profile Data Architecture — The 4 high-yield data quadrants (Identity, Physical Sizing, Aesthetic Wishlist, Milestone Calendar) vs. strictly prohibited CRM records.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M03-crm-daily-and-weekly-workflows.md",
     "## The daily habit: know what today has already promised",
     """<figure>
  <img src="../assets/c3-m03-crm-daily-weekly-rhythm.svg" alt="CRM Daily and Weekly Operating Rhythm" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> CRM Daily &amp; Weekly Operating Rhythm — The 15-minute morning routine and structured weekly clienteling playbook.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M04-segmenting-your-book-finding-and-prioritizing-vics.md",
     "## Five signals that actually identify a VIC",
     """<figure>
  <img src="../assets/c3-m04-client-book-segmentation-pyramid.svg" alt="Client Book Segmentation Pyramid" width="100%" />
  <figcaption><strong>Figure 4.1:</strong> The 80/20 Luxury Clienteling Pyramid — Time allocation, revenue contribution, and contact cadences across VIC, Core, Developing, and Base customer tiers.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M05-life-event-triggers-birthdays-anniversaries-milestones.md",
     "## Beyond \"happy anniversary\"",
     """<figure>
  <img src="../assets/c3-m05-milestone-anticipation-timeline.svg" alt="Life-Event Milestone Anticipation Horizon" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> Life-Event Milestone Anticipation — The 6-week outreach horizon and lead-time requirements for anniversaries, decade birthdays, and push presents.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M06-personalized-outreach-without-sounding-like-spam.md",
     "## The fix is almost embarrassingly simple",
     """<figure>
  <img src="../assets/c3-m06-personalized-outreach-anatomy.svg" alt="3-Part Luxury Outreach Formula" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> The 3-Part Luxury Outreach Formula — Personal anchor, curated value trigger, and low-pressure CTA vs. generic marketing spam.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M07-winning-back-a-lapsed-client.md",
     "## The Win-Back Framework: Reconnect Before You Reoffer",
     """<figure>
  <img src="../assets/c3-m07-lapsed-client-winback-protocol.svg" alt="Lapsed Client Winback Protocol" width="100%" />
  <figcaption><strong>Figure 7.1:</strong> Lapsed Client Re-Engagement Ladder — 4-stage reactivation protocol (90-Day, 180-Day Spa, 270-Day VIP Trunk, 365-Day Note) and root-cause solutions.</figcaption>
</figure>"""),

    ("courses/C3-clienteling-and-crm/articles/M08-building-a-referral-engine-through-clienteling.md",
     "## The Three Moments When Referral-Asking Actually Works",
     """<figure>
  <img src="../assets/c3-m08-referral-engine-flywheel.svg" alt="Organic Luxury Referral Flywheel" width="100%" />
  <figcaption><strong>Figure 8.1:</strong> The Luxury Referral Flywheel — 5-stage organic referral generation and verbatim luxury concierge scripts.</figcaption>
</figure>"""),

    # C5
    ("courses/C5-financing-credit-compliance/articles/M01-consumer-financing-basics-how-retail-installment-credit-works-at-the-counter.md",
     "## What a Retail Installment Contract Actually Is",
     """<figure>
  <img src="../assets/c5-m01-retail-installment-financing-flow.svg" alt="Retail Installment Credit Mechanics" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> Consumer Installment Credit Mechanics — 3-party architecture (Client, Retailer, Lender), MDR settlement, and Revolving vs. Equal-Pay comparison.</figcaption>
</figure>"""),

    ("courses/C5-financing-credit-compliance/articles/M02-running-a-financing-application-at-the-point-of-sale.md",
     "## Handling a Declined Application",
     """<figure>
  <img src="../assets/c5-m02-pos-financing-application-sop.svg" alt="POS Financing Application SOP" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> Point-of-Sale Financing Protocol — 5-step private compliance flow (Discreet Bridge, Tablet Hand-Off, Prequalification, TILA Disclosures, Dignified Decline).</figcaption>
</figure>"""),

    ("courses/C5-financing-credit-compliance/articles/M03-layaway-vs-financing-vs-buy-now-pay-later-choosing-the-right-option.md",
     "## Layaway: The Store Holds the Item, the Customer Owns Nothing Yet",
     """<figure>
  <img src="../assets/c5-m03-payment-options-comparison-matrix.svg" alt="Payment Solutions Matrix" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> Payment Solutions Matrix — Strategic comparison of Vault Layaway, Store Financing (0% APR), and Buy-Now-Pay-Later (BNPL).</figcaption>
</figure>"""),

    ("courses/C5-financing-credit-compliance/articles/M04-ftc-disclosure-rules-treatments-lab-grown-and-advertising-claims.md",
     "## The FTC Jewelry Guides: The Regulatory Backbone",
     """<figure>
  <img src="../assets/c5-m04-ftc-jewelry-disclosure-mandates.svg" alt="FTC Jewelry Guides Compliance Mandates" width="100%" />
  <figcaption><strong>Figure 4.1:</strong> FTC Jewelry Guides Compliance Mandates — Mandatory gemstone treatments, synthetic terminology, karat fineness tolerances, and deceptive pricing rules.</figcaption>
</figure>"""),

    ("courses/C5-financing-credit-compliance/articles/M05-aml-basics-for-jewelry-retail.md",
     "## Why Jewelry Dealers Have AML Obligations in the First Place",
     """<figure>
  <img src="../assets/c5-m05-aml-red-flags-decision-tree.svg" alt="AML Compliance and Red Flags Tree" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> Anti-Money Laundering (AML) &amp; FinCEN Decision Tree — Form 8300 thresholds, OFAC sanctions, and top 6 jewelry retail red flags.</figcaption>
</figure>"""),

    ("courses/C5-financing-credit-compliance/articles/M06-memo-consignment-and-ucc-1-protecting-the-stores-legal-interest.md",
     "## UCC-1 Filings: How a Vendor Protects Its Interest in Memo Goods",
     """<figure>
  <img src="../assets/c5-m06-memo-consignment-ucc1-workflow.svg" alt="UCC-1 Consignment and Memo Protection Lifecycle" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> Consignment &amp; Memo Inventory Protection — UCC-1 Financing Statement lifecycle, PMSI priority, and bankruptcy lien risk.</figcaption>
</figure>"""),

    # C6
    ("courses/C6-bridal-engagement-mastery/articles/M01-the-modern-engagement-ring-buyer-trends-psychology-and-the-path-to-purchase.md",
     "## The Headline Shift: Away From Maximalism, Toward Intentionality",
     """<figure>
  <img src="../assets/c6-m01-bridal-buyer-journey-map.svg" alt="Modern Bridal Path to Purchase Journey Map" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> The Modern Bridal Path-to-Purchase — 4-phase buyer psychology (Digital Discovery, Joint Exploration, Solo Return, Proposal Execution).</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M02-diamond-shape-vs-cut-why-theyre-not-the-same-thing.md",
     "## The Core Distinction",
     """<figure>
  <img src="../assets/c6-m02-diamond-shapes-and-facet-architectures.svg" alt="Diamond Shape vs Cut Architectures" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> Diamond Shape vs. Cut Architecture — Brilliant Cut vs. Step Cut vs. Mixed Cut facet families and optical performance dynamics.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M03-gia-vs-ags-reading-certificates-and-choosing-the-right-lab.md",
     "## The Core Methodological Difference: Proportion Buckets vs. Measured Light Performance",
     """<figure>
  <img src="../assets/c6-m03-bridal-lab-selection-matrix.svg" alt="Bridal Grading Lab Selection Guide" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> Bridal Grading Lab Comparative Guide — GIA, AGS, IGI, and GCAL strictness benchmarks and retail counter positioning.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M04-natural-lab-grown-and-simulants-advising-without-bias.md",
     "## What Each Option Actually Is",
     """<figure>
  <img src="../assets/c6-m04-bridal-stone-origin-advisor.svg" alt="Ethical Bridal Stone Origin Advisor" width="100%" />
  <figcaption><strong>Figure 4.1:</strong> Ethical Bridal Stone Advisory — Objective comparison of Natural Diamonds, Lab-Grown Diamonds, and Simulants with verbatim presentation scripts.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M05-metals-and-settings-durability-style-and-the-yellow-gold-resurgence.md",
     "## Gold Karats: The Durability Trade-Off Most Buyers Don't Expect",
     """<figure>
  <img src="../assets/c6-m05-bridal-settings-and-metals-guide.svg" alt="Bridal Settings and Precious Metals Guide" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> Bridal Settings &amp; Precious Metals Guide — Solitaire, Bezel, Halo, and Pavé architectures paired with Platinum and Karat Gold wear characteristics.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M06-ring-sizing-fit-and-comfort-getting-it-right-the-first-time.md",
     "## Measuring Accurately: What Actually Affects the Number",
     """<figure>
  <img src="../assets/c6-m06-ring-sizing-and-fit-mechanics.svg" alt="Ring Sizing and Fit Mechanics" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> Ring Sizing, Fit &amp; Comfort Mechanics — Knuckle anatomy, comfort-fit dome profiles, biological fluctuations, and surprise proposal sizing hacks.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M07-the-custom-design-and-cad-workflow-for-bridal.md",
     "## The Five-Stage Workflow",
     """<figure>
  <img src="../assets/c6-m07-bridal-custom-cad-milestones.svg" alt="Custom Bridal CAD Design Milestones" width="100%" />
  <figcaption><strong>Figure 7.1:</strong> Custom Bridal Design Pipeline — 5 milestone approval gates (Concept, CAD Renders, Wax Try-On, Bench Casting/Setting, Final Unveiling).</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M08-the-proposal-logistics-conversation-secrecy-timing-and-same-day-pickup.md",
     "## Discreet Packaging and Pickup",
     """<figure>
  <img src="../assets/c6-m08-proposal-logistics-timeline.svg" alt="Proposal Logistics and Stealth Protocol" width="100%" />
  <figcaption><strong>Figure 8.1:</strong> Proposal Logistics &amp; Stealth Protocol — Pocket-friendly stealth boxes, airport travel security, day-zero insurance, and post-proposal re-sizing.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M09-wedding-bands-and-stacking-pairing-matching-metals-and-the-second-sale.md",
     "## Pairing a Band with the Engagement Ring: Contour, Not Just Color",
     """<figure>
  <img src="../assets/c6-m09-wedding-band-pairing-matrix.svg" alt="Wedding Band Pairing and Stacking Matrix" width="100%" />
  <figcaption><strong>Figure 9.1:</strong> Wedding Band &amp; Stacking Architecture — Straight Flush Fit vs. Contoured vs. Chevron Jackets and metal alloy friction wear rules.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M10-appraisal-insurance-and-aftercare-protecting-the-purchase-for-a-lifetime.md",
     "## The Three Insurance Paths, and What Each Actually Covers",
     """<figure>
  <img src="../assets/c6-m10-bridal-appraisal-insurance-lifecycle.svg" alt="Lifetime Bridal Protection Lifecycle" width="100%" />
  <figcaption><strong>Figure 10.1:</strong> Lifetime Bridal Protection Lifecycle — Point-of-sale retail appraisals, standalone jewelry insurance, 6-month prong inspections, and home care rules.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M11-selling-bridal-across-demographics-and-life-stages.md",
     "## Self-Purchasers: A Growing, Not Niche, Segment",
     """<figure>
  <img src="../assets/c6-m11-demographic-bridal-personas.svg" alt="Demographic Bridal Personas" width="100%" />
  <figcaption><strong>Figure 11.1:</strong> Demographic Bridal Personas — 4 customer archetypes (Traditionalist, Modern Minimalist, Eco &amp; Unique, High-Carat Maximalist) and tailored sales framing.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M12-ethical-standards-in-high-ticket-bridal-selling.md",
     "## FTC Disclosure Requirements Are Not Optional",
     """<figure>
  <img src="../assets/c6-m12-ethical-selling-code-pillars.svg" alt="Ethical Selling Standards in Bridal" width="100%" />
  <figcaption><strong>Figure 12.1:</strong> Ethical Standards in High-Ticket Bridal Selling — The 4 core pillars (Unbiased Disclosure, No Fear/Guilt, Transparent Pricing, Conflict-Free Sourcing).</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M13-selling-bridal-in-cruise-and-port-retail-environments.md",
     "## Understanding the Environment You're Selling In",
     """<figure>
  <img src="../assets/c6-m13-cruise-port-compressed-sales-cycle.svg" alt="Port of Call Bridal Sales Velocity" width="100%" />
  <figcaption><strong>Figure 13.1:</strong> Port-of-Call Bridal Sales Velocity — The 180-minute compressed execution model for high-ticket jewelry sales in cruise retail.</figcaption>
</figure>"""),

    ("courses/C6-bridal-engagement-mastery/articles/M14-selling-bridal-in-luxury-hotel-and-private-appointment-settings-capstone.md",
     "## The Format: What Private and Hotel-Based Bridal Selling Actually Looks Like",
     """<figure>
  <img src="../assets/c6-m14-private-salon-bridal-experience.svg" alt="Private Salon Bridal Luxury Blueprint" width="100%" />
  <figcaption><strong>Figure 14.1:</strong> The Private Salon Bridal Experience — Atmospheric staging, curated tray presentation, interactive gemological reveal, and white-glove concierge close.</figcaption>
</figure>"""),

    # C12
    ("courses/C12-retail-kpis-reporting/articles/M02-conversion-and-traffic-measuring-what-you-cant-see.md",
     "## What Conversion Rate Should Actually Look Like in a Jewelry Store",
     """<figure>
  <img src="../assets/c12-m02-traffic-conversion-funnel.svg" alt="Store Traffic and Conversion Funnel" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> Traffic &amp; Conversion Analytics — The 4-stage fine jewelry storefront funnel (Door Swings, Qualified Opportunities, Showcase Presentations, Closed Sales).</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M03-average-ticket-upt-and-mix.md",
     "## Reading the Two Numbers Together, Not Separately",
     """<figure>
  <img src="../assets/c12-m03-atv-upt-product-mix-engine.svg" alt="High Ticket Sales Engine ATV UPT" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> The High-Ticket Sales Engine — Interplay between Average Ticket (ATV), Units Per Transaction (UPT), and optimal margin category mix.</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M04-inventory-kpis-sell-through-turn-gmroi.md",
     "## Jewelry's Inventory Turn Is Genuinely, Structurally Slow",
     """<figure>
  <img src="../assets/c12-m04-inventory-productivity-dashboard.svg" alt="Inventory Productivity and Health Dashboard" width="100%" />
  <figcaption><strong>Figure 4.1:</strong> Inventory Productivity &amp; Health — Sell-Through %, Inventory Turn, GMROI formula benchmarks, and the 4-phase aged inventory action protocol.</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M05-retention-and-client-book-kpis.md",
     "## The 30-Day Window Is the Single Biggest Leak",
     """<figure>
  <img src="../assets/c12-m05-client-book-health-scorecard.svg" alt="Client Retention and Book Health Scorecard" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> Client Retention &amp; Book Health Scorecard — Active Book Ratio, Repeat Purchase Rate, Outreach-to-Appointment Conversion, and Lifetime Value (LTV).</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M06-building-the-weekly-dashboard.md",
     "## A Four-Row Structure That Answers the Right Question at Each Level",
     """<figure>
  <img src="../assets/c12-m06-weekly-store-kpi-dashboard-mockup.svg" alt="Executive Weekly Store Dashboard" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> Executive Weekly Store Dashboard — Real-world store scorecard tracking sales vs. plan, consultant leaderboards, category mix, and coaching actions.</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M07-diagnosing-a-miss.md",
     "## The Sales Equation, and Why Order Matters",
     """<figure>
  <img src="../assets/c12-m07-sales-miss-root-cause-tree.svg" alt="Sales Miss Root Cause Diagnostic Tree" width="100%" />
  <figcaption><strong>Figure 7.1:</strong> Sales Miss Root-Cause Diagnostic Tree — Step-by-step troubleshooting for Traffic Deficits, Conversion Misses, ATV Erosion, and UPT Collapse.</figcaption>
</figure>"""),

    ("courses/C12-retail-kpis-reporting/articles/M08-reporting-up-the-one-page-store-review.md",
     "## Building the One-Page Version",
     """<figure>
  <img src="../assets/c12-m08-one-page-store-performance-review.svg" alt="One Page Store Performance Review" width="100%" />
  <figcaption><strong>Figure 8.1:</strong> The 1-Page Executive Store Performance Review — Standardized executive reporting template covering P&amp;L snapshot, KPI variances, wins/losses, and corrective action plans.</figcaption>
</figure>""")
]

for filepath, marker, block in embeddings:
    embed_image_if_not_present(filepath, marker, block)

print("Wave 2 asset embeddings completed!")
