import os

def write_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath}")

# C3 M01: Client Profile Data Architecture
c3_m01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Client Profile Data Architecture: The 4 High-Yield Quadrants</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Essential CRM data capture standards for luxury sales consultants vs. prohibited personal data</text>

  <!-- Quadrant 1: Identity & Relationships -->
  <rect x="50" y="100" width="480" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
  <rect x="50" y="100" width="480" height="36" rx="8" fill="#1E293B"/>
  <text x="70" y="124" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#38BDF8">QUADRANT 1: Core Identity &amp; Key Relationships</text>
  
  <text x="70" y="160" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Full Legal Name &amp; Preferred Name / Nickname</text>
  <text x="70" y="180" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Always capture phonetic pronunciation for culturally diverse clients</text>
  <text x="70" y="210" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Verified Contact Channels &amp; Preferred Time/Method</text>
  <text x="70" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Direct SMS vs. WhatsApp vs. Private Email (explicit consent recorded)</text>
  <text x="70" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Partner, Spouse &amp; Significant Other Linkages</text>
  <text x="70" y="280" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Link accounts for cross-gifting, secret surprise proposals, and anniversaries</text>
  <text x="70" y="310" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Executive Assistant / Personal Stylist Details</text>

  <!-- Quadrant 2: Physical Attributes & Sizing -->
  <rect x="570" y="100" width="480" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
  <rect x="570" y="100" width="480" height="36" rx="8" fill="#1E293B"/>
  <text x="590" y="124" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#10B981">QUADRANT 2: Physical Sizing &amp; Wear Preferences</text>
  
  <text x="590" y="160" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Exact Finger Sizing (Per Finger &amp; Hand)</text>
  <text x="590" y="180" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Left Ring Finger (Bridal), Right Ring, Index, Pinky (summer vs. winter)</text>
  <text x="590" y="210" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Wrist Circumference &amp; Preferred Bracelet Drape</text>
  <text x="590" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Snug cuff vs. loose 7.25" tennis link drape; watch lug-to-lug scale</text>
  <text x="590" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Neckline &amp; Chain Length Preferences</text>
  <text x="590" y="280" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  16" Choker vs. 18" Princess vs. 24" Opera layering habits</text>
  <text x="590" y="310" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Pierced Earring Post Length &amp; Sensitivity Allergies (Nickel/Gold)</text>

  <!-- Quadrant 3: Aesthetic Taste & Wishlist -->
  <rect x="50" y="350" width="480" height="200" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
  <rect x="50" y="350" width="480" height="36" rx="8" fill="#1E293B"/>
  <text x="70" y="374" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#F59E0B">QUADRANT 3: Aesthetic Profile &amp; Curated Wishlist</text>
  
  <text x="70" y="410" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Precious Metal Preference Hierarchy</text>
  <text x="70" y="430" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  e.g., 18K Yellow Gold exclusively, Platinum for high-carat diamonds</text>
  <text x="70" y="460" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Gemstone Affinity &amp; Birthstone Connections</text>
  <text x="70" y="480" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Loves unheated sapphires, Colombian emeralds; avoids marquise shapes</text>
  <text x="70" y="510" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Active Wishlist Items with SKU, Target Specs &amp; Price</text>

  <!-- Quadrant 4: Milestone Calendar -->
  <rect x="570" y="350" width="480" height="200" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
  <rect x="570" y="350" width="480" height="36" rx="8" fill="#1E293B"/>
  <text x="590" y="374" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#EC4899">QUADRANT 4: Milestone Calendar &amp; Life Triggers</text>
  
  <text x="590" y="410" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Client &amp; Partner Birthdays (Day &amp; Month)</text>
  <text x="590" y="430" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Trigger partner outreach 4 to 6 weeks prior to event</text>
  <text x="590" y="460" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Wedding &amp; Relationship Anniversaries</text>
  <text x="590" y="480" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">  Year landmark tracking (5th, 10th, 25th major upgrade milestones)</text>
  <text x="590" y="510" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">• Career Milestones, Graduations, Annual Travel Traditions</text>

  <!-- Prohibited Data Banner -->
  <rect x="50" y="570" width="1000" height="85" rx="8" fill="#450A0A" stroke="#EF4444" stroke-width="1.5"/>
  <text x="70" y="595" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FCA5A5">⚠️ STRICT CRM COMPLIANCE: NEVER RECORD IN CLIENT PROFILES</text>
  <text x="70" y="618" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">❌ Speculative wealth/income assumptions ("cheap", "loaded") • ❌ Protected demographic/religious/political opinions</text>
  <text x="70" y="638" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">❌ Personal marital drama or derogatory gossip • ❌ Unencrypted credit card or social security numbers</text>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m01-client-profile-data-architecture.svg", c3_m01)

# C3 M03: CRM Daily and Weekly Workflows
c3_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">CRM Daily &amp; Weekly Operating Rhythm: The 15-Minute Morning Engine</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Systematic daily habits that generate 60–75% of repeat fine jewelry book sales</text>

  <!-- 15-Min Daily Flow Box -->
  <rect x="50" y="100" width="1000" height="260" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
  <rect x="50" y="100" width="1000" height="36" rx="8" fill="#1E293B"/>
  <text x="70" y="124" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#38BDF8">THE 15-MINUTE MORNING CRM ROUTINE (Pre-Store Opening: 9:45 – 10:00 AM)</text>

  <!-- Step 1 -->
  <rect x="70" y="150" width="215" height="185" rx="6" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <circle cx="100" cy="175" r="14" fill="#38BDF8"/>
  <text x="96" y="180" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">1</text>
  <text x="125" y="180" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F3F4F6">Milestone Alerts</text>
  <text x="85" y="210" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Review Birthdays</text>
  <text x="85" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Review Anniversaries</text>
  <text x="85" y="250" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">(Occurring in 4–6 wks)</text>
  <text x="85" y="280" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#38BDF8">Target: 3 Partner Calls/Texts</text>

  <!-- Step 2 -->
  <rect x="310" y="150" width="215" height="185" rx="6" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <circle cx="340" cy="175" r="14" fill="#10B981"/>
  <text x="336" y="180" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">2</text>
  <text x="365" y="180" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F3F4F6">2-2-2 Cadence</text>
  <text x="325" y="210" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Day 2 Thank You SMS</text>
  <text x="325" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Wk 2 Fit/Reaction Call</text>
  <text x="325" y="250" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Mo 2 Spa Invitation</text>
  <text x="325" y="280" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#10B981">Target: 4 Touchpoints</text>

  <!-- Step 3 -->
  <rect x="550" y="150" width="215" height="185" rx="6" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <circle cx="580" cy="175" r="14" fill="#F59E0B"/>
  <text x="576" y="180" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">3</text>
  <text x="605" y="180" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F3F4F6">Wishlist Match</text>
  <text x="565" y="210" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Check New Intake Memos</text>
  <text x="565" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Match fresh gems to VIPs</text>
  <text x="565" y="250" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Snap 5-sec macro video</text>
  <text x="565" y="280" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F59E0B">Target: 2 Private Previews</text>

  <!-- Step 4 -->
  <rect x="790" y="150" width="235" height="185" rx="6" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <circle cx="820" cy="175" r="14" fill="#EC4899"/>
  <text x="816" y="180" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">4</text>
  <text x="845" y="180" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F3F4F6">Service Follow-Up</text>
  <text x="805" y="210" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Repair / Custom ready</text>
  <text x="805" y="230" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• Appraisal delivery alerts</text>
  <text x="805" y="250" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Special order arrivals</text>
  <text x="805" y="280" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#EC4899">Target: High-Touch Service</text>

  <!-- Weekly Rhythm -->
  <rect x="50" y="380" width="1000" height="260" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
  <rect x="50" y="380" width="1000" height="36" rx="8" fill="#1E293B"/>
  <text x="70" y="404" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#10B981">WEEKLY STRATEGIC CLIENTELING CADENCE</text>

  <g transform="translate(70, 435)">
    <!-- Monday -->
    <rect x="0" y="0" width="180" height="180" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">MONDAY</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Weekend Traffic Review</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Log all weekend walk-ins</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Complete profile cards</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Tag undecided bridal leads</text>
    <text x="15" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Action: Pipeline audit</text>

    <!-- Wednesday -->
    <rect x="200" y="0" width="180" height="180" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="215" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">WEDNESDAY</text>
    <text x="215" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">VIC Private Curation</text>
    <text x="215" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Top 20 client book review</text>
    <text x="215" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Preview new collection</text>
    <text x="215" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Schedule salon viewings</text>
    <text x="215" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Action: 5 VIP touches</text>

    <!-- Thursday -->
    <rect x="400" y="0" width="180" height="180" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="415" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">THURSDAY</text>
    <text x="415" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Lapsed Book Reactivation</text>
    <text x="415" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Filter 180+ day silence</text>
    <text x="415" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Complimentary prong check</text>
    <text x="415" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pearl restringing invite</text>
    <text x="415" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Action: 5 Win-backs</text>

    <!-- Friday -->
    <rect x="600" y="0" width="180" height="180" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="615" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">FRIDAY</text>
    <text x="615" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Weekend Staging</text>
    <text x="615" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Confirm appts on calendar</text>
    <text x="615" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pull trays in advance</text>
    <text x="615" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Prep personalized cards</text>
    <text x="615" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Action: Staged trays</text>

    <!-- Sunday / EOW -->
    <rect x="800" y="0" width="160" height="180" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="815" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#A855F7">SUNDAY</text>
    <text x="815" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Metrics &amp; Scorecard</text>
    <text x="815" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Total client outreach: 50</text>
    <text x="815" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Appointments held: 6</text>
    <text x="815" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Sales from CRM: $42,000</text>
    <text x="815" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#A855F7">Goal: 65% Book Sales</text>
  </g>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m03-crm-daily-weekly-rhythm.svg", c3_m03)

# C3 M04: Segmenting Your Book
c3_m04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Client Book Segmentation: The 80/20 Luxury Clienteling Pyramid</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Prioritizing sales consultant time, investment allocation, and contact frequency across customer tiers</text>

  <!-- Pyramid Graphics -->
  <polygon points="270,120 120,480 420,480" fill="#161B22" stroke="#334155" stroke-width="2"/>

  <!-- Tier 1 Top: VIC -->
  <polygon points="270,120 230,200 310,200" fill="#F59E0B" fill-opacity="0.9"/>
  <text x="270" y="170" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0B0E14" text-anchor="middle">VIC (Top 5%)</text>

  <!-- Tier 2: Core VIP -->
  <polygon points="230,200 190,290 350,290 310,200" fill="#38BDF8" fill-opacity="0.85"/>
  <text x="270" y="250" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0B0E14" text-anchor="middle">Core Repeat (15%)</text>

  <!-- Tier 3: Developing -->
  <polygon points="190,290 150,380 390,380 350,290" fill="#10B981" fill-opacity="0.8"/>
  <text x="270" y="340" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0B0E14" text-anchor="middle">Developing (30%)</text>

  <!-- Tier 4: Base / Lapsed -->
  <polygon points="150,380 120,480 420,480 390,380" fill="#64748B" fill-opacity="0.7"/>
  <text x="270" y="435" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Base &amp; Occasional (50%)</text>

  <!-- Detail Cards on Right -->
  <!-- VIC Card -->
  <rect x="470" y="110" width="580" height="95" rx="6" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="490" y="135" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">TIER 1: VERY IMPORTANT CLIENTS (VIC) — Top 5% of Book</text>
  <text x="490" y="158" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Generates 45–55% of annual commission • LTV &gt; $50,000+ • Multiple high-ticket pieces/yr</text>
  <text x="490" y="180" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">Cadence: 1–2 personalized touches/month • First-look trunk shows • Private salon champagne tastings</text>

  <!-- Core Repeat Card -->
  <rect x="470" y="215" width="580" height="95" rx="6" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="490" y="240" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">TIER 2: CORE REPEAT COLLECTORS — Next 15% of Book</text>
  <text x="490" y="263" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Generates 25–30% of sales • LTV $10,000–$50,000 • Reliable annual anniversary/holiday buyers</text>
  <text x="490" y="285" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">Cadence: 6–8 curated touches/year • Milestone date anticipation • Designer launch invitations</text>

  <!-- Developing Card -->
  <rect x="470" y="320" width="580" height="95" rx="6" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
  <text x="490" y="345" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">TIER 3: DEVELOPING / HIGH POTENTIAL — 30% of Book</text>
  <text x="490" y="368" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Generates 15% of sales • First-time engagement ring or luxury watch buyers</text>
  <text x="490" y="390" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">Cadence: 2-2-2 post-sale sequence • Wedding band bridge • 1st anniversary upgrade outreach</text>

  <!-- Base Card -->
  <rect x="470" y="425" width="580" height="95" rx="6" fill="#161B22" stroke="#64748B" stroke-width="1.5"/>
  <text x="490" y="450" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#94A3B8">TIER 4: BASE &amp; OCCASIONAL BUYERS — Bottom 50% of Book</text>
  <text x="490" y="473" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Small gift buyers, minor repairs, walk-in impulse purchases • Under $2,500 LTV</text>
  <text x="490" y="495" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">Cadence: Automated store newsletter • Annual jewelry cleaning invite • Seasonal promotional triggers</text>

  <!-- Bottom Rule -->
  <rect x="50" y="540" width="1000" height="100" rx="8" fill="#1E293B"/>
  <text x="70" y="570" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE GOLDEN RULE OF BOOK TIME ALLOCATION:</text>
  <text x="70" y="598" font-family="Inter, -apple-system, sans-serif" font-size="13" fill="#F3F4F6">Invest 60% of daily outreach time into Tier 1 (VICs), 25% into Tier 2 (Core), and 15% into Tier 3 (Developing).</text>
  <text x="70" y="622" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#9CA3AF">Never let routine transactional administrative work crowd out proactive personal outreach to your top 20% relationships.</text>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m04-client-book-segmentation-pyramid.svg", c3_m04)

# C3 M05: Life Event Triggers Timeline
c3_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Life-Event Milestone Anticipation: The 6-Week Outreach Horizon</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">How fine jewelry professionals orchestrate stress-free milestone gifting without feeling pushy</text>

  <!-- Timeline Bar -->
  <line x1="100" y1="200" x2="1000" y2="200" stroke="#334155" stroke-width="4"/>

  <!-- Milestone Node: T-6 Weeks -->
  <circle cx="150" cy="200" r="18" fill="#38BDF8"/>
  <text x="150" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">T-6W</text>
  <rect x="70" y="235" width="160" height="150" rx="6" fill="#161B22" stroke="#38BDF8" stroke-width="1"/>
  <text x="80" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">Initial Radar Check</text>
  <text x="80" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Check spouse's wishlist</text>
  <text x="80" y="305" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Review past sizes &amp; metal</text>
  <text x="80" y="325" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Low-friction note to partner:</text>
  <text x="80" y="345" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#38BDF8">"Thinking of Sarah's 40th..."</text>

  <!-- Milestone Node: T-4 Weeks -->
  <circle cx="360" cy="200" r="18" fill="#10B981"/>
  <text x="360" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">T-4W</text>
  <rect x="280" y="235" width="160" height="150" rx="6" fill="#161B22" stroke="#10B981" stroke-width="1"/>
  <text x="290" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">Curated Presentation</text>
  <text x="290" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Send 3-option digital lookbook</text>
  <text x="290" y="305" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• High-res video of stones</text>
  <text x="290" y="325" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Custom sizing window</text>
  <text x="290" y="345" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#10B981">"Curated these 3 matches"</text>

  <!-- Milestone Node: T-2 Weeks -->
  <circle cx="570" cy="200" r="18" fill="#F59E0B"/>
  <text x="570" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">T-2W</text>
  <rect x="490" y="235" width="160" height="150" rx="6" fill="#161B22" stroke="#F59E0B" stroke-width="1"/>
  <text x="500" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">Selection &amp; Sizing</text>
  <text x="500" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Client selects piece</text>
  <text x="500" y="305" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Workshop sizing &amp; polish</text>
  <text x="500" y="325" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Custom hand engraving</text>
  <text x="500" y="345" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#F59E0B">"Secured &amp; sent to bench"</text>

  <!-- Milestone Node: T-3 Days -->
  <circle cx="780" cy="200" r="18" fill="#EC4899"/>
  <text x="780" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">T-3D</text>
  <rect x="700" y="235" width="160" height="150" rx="6" fill="#161B22" stroke="#EC4899" stroke-width="1"/>
  <text x="710" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">Gift-Wrap &amp; Pickup</text>
  <text x="710" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Signature ribbon wrapping</text>
  <text x="710" y="305" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Discreet pickup or courier</text>
  <text x="710" y="325" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Blank gift card included</text>
  <text x="710" y="345" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#EC4899">"Wrapped &amp; ready to delight"</text>

  <!-- Milestone Node: T+2 Days -->
  <circle cx="950" cy="200" r="18" fill="#A855F7"/>
  <text x="950" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">T+2D</text>
  <rect x="880" y="235" width="150" height="150" rx="6" fill="#161B22" stroke="#A855F7" stroke-width="1"/>
  <text x="890" y="260" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#A855F7">Reaction Check</text>
  <text x="890" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Warm celebration check-in</text>
  <text x="890" y="305" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Offer minor sizing tweaks</text>
  <text x="890" y="325" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Update profile reaction</text>
  <text x="890" y="345" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#A855F7">"How did she love it?"</text>

  <!-- Milestone Categories Grid -->
  <rect x="50" y="420" width="1000" height="220" rx="8" fill="#161B22" stroke="#334155"/>
  <text x="70" y="450" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#F3F4F6">THE 4 CORE MILESTONE CATEGORIES &amp; LEAD-TIME REQUIREMENTS</text>

  <g transform="translate(70, 470)">
    <!-- Cat 1 -->
    <rect x="0" y="0" width="220" height="145" rx="6" fill="#0F172A" stroke="#38BDF8"/>
    <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">Major Anniversaries</text>
    <text x="15" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• 1st: Gold / Eternity Band</text>
    <text x="15" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• 5th: Sapphire upgrade</text>
    <text x="15" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• 10th: Diamond anniversary</text>
    <text x="15" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Lead Time: 6–8 Weeks</text>

    <!-- Cat 2 -->
    <rect x="245" y="0" width="220" height="145" rx="6" fill="#0F172A" stroke="#10B981"/>
    <text x="260" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">Decade Birthdays</text>
    <text x="260" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• 30th, 40th, 50th, 60th</text>
    <text x="260" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Significant statement rings</text>
    <text x="260" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• High-carat tennis bracelets</text>
    <text x="260" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Lead Time: 4–6 Weeks</text>

    <!-- Cat 3 -->
    <rect x="490" y="0" width="220" height="145" rx="6" fill="#0F172A" stroke="#F59E0B"/>
    <text x="505" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">Push Presents &amp; Kids</text>
    <text x="505" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Child arrival celebration</text>
    <text x="505" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Birthstone stacking bands</text>
    <text x="505" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Engraved initial medallions</text>
    <text x="505" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Lead Time: 3–4 Weeks</text>

    <!-- Cat 4 -->
    <rect x="735" y="0" width="220" height="145" rx="6" fill="#0F172A" stroke="#EC4899"/>
    <text x="750" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">Career &amp; Personal Wins</text>
    <text x="750" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Partner promotion / exit</text>
    <text x="750" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Luxury timepiece purchase</text>
    <text x="750" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Self-purchasing celebration</text>
    <text x="750" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Lead Time: Immediate</text>
  </g>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m05-milestone-anticipation-timeline.svg", c3_m05)

# C3 M06: Personalized Outreach Anatomy
c3_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The 3-Part Luxury Outreach Formula: High-Conversion Architecture</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Transforming generic marketing spam into compelling, personalized client conversations</text>

  <!-- Left Side: Formula Anatomy -->
  <g transform="translate(50, 100)">
    <!-- Part 1 -->
    <rect x="0" y="0" width="480" height="145" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">PART 1: The Personal Anchor (Context &amp; Relevance)</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• References specific past conversation, piece owned, or personal event</text>
    <text x="15" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Establishes immediate genuine rapport — proves this is not a blast text</text>
    <text x="15" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" font-style="italic" fill="#38BDF8">"Hi Marcus, I hope your trip to Aspen was wonderful! While you were away..."</text>

    <!-- Part 2 -->
    <rect x="0" y="165" width="480" height="145" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="0" y="165" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="187" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">PART 2: The Curated Value Trigger (The "Why Now")</text>
    <text x="15" y="220" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Introduces a rare piece, new arrival match, or private VIP privilege</text>
    <text x="15" y="240" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Focuses on exclusivity, craft details, or perfect gemstone pairing</text>
    <text x="15" y="270" font-family="Inter, -apple-system, sans-serif" font-size="11" font-style="italic" fill="#F59E0B">"...this rare unheated 3.2ct Ceylon sapphire just arrived from cutting in Sri Lanka..."</text>

    <!-- Part 3 -->
    <rect x="0" y="330" width="480" height="145" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="0" y="330" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="352" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">PART 3: Low-Pressure Call-to-Action (Frictionless)</text>
    <text x="15" y="385" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Soft invite with zero sales pressure — preserves relationship dignity</text>
    <text x="15" y="405" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Easy binary reply: photo preview, video walkthrough, or quick salon espresso</text>
    <text x="15" y="435" font-family="Inter, -apple-system, sans-serif" font-size="11" font-style="italic" fill="#10B981">"Would you like me to send a 10-second video of how it catches the sunlight?"</text>
  </g>

  <!-- Right Side: Comparison Box -->
  <g transform="translate(560, 100)">
    <!-- Bad Example -->
    <rect x="0" y="0" width="490" height="230" rx="8" fill="#2A1215" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="490" height="32" rx="8" fill="#450A0A"/>
    <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EF4444">❌ THE GENERIC SPAM OUTREACH (Zero Conversion)</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">"Dear customer, we are having our annual Spring Diamond Sale! Come</text>
    <text x="15" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">in this weekend to save 20% off all selected showcases. We have huge</text>
    <text x="15" y="95" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">inventory in stock. Let me know when you can stop by!"</text>
    
    <text x="15" y="130" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FCA5A5">Why it fails:</text>
    <text x="15" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Treats luxury client as a generic broadcast target</text>
    <text x="15" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Cheapens brand prestige by leading with discounts</text>
    <text x="15" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Triggers instant SMS unsubscribe / spam report</text>

    <!-- Good Example -->
    <rect x="0" y="250" width="490" height="225" rx="8" fill="#062E25" stroke="#10B981" stroke-width="1.5"/>
    <rect x="0" y="250" width="490" height="32" rx="8" fill="#064E3B"/>
    <text x="15" y="272" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">✓ THE BESPOKE LUXURY OUTREACH (74% Response Rate)</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#D1FAE5">"Hi Eleanor! I was thinking of your emerald-cut platinum ring from last</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#D1FAE5">December. Our master cutter just finished an exquisite east-west eternity</text>
    <text x="15" y="345" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#D1FAE5">band that nests alongside it flawlessly. No obligation at all — I made a</text>
    <text x="15" y="365" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#D1FAE5">brief video showing how the step facets mirror yours. May I send it over?"</text>

    <text x="15" y="400" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#6EE7B7">Why it succeeds:</text>
    <text x="15" y="420" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">• Hyper-relevant aesthetic pairing with owned heirloom</text>
    <text x="15" y="440" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">• Creates curiosity and private privilege with zero commercial tension</text>
  </g>

  <!-- Bottom Best Practice Banner -->
  <rect x="50" y="590" width="1000" height="55" rx="8" fill="#1E293B"/>
  <text x="70" y="623" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6">GOLDEN RULE OF MEDIA IN OUTREACH: Always attach a 5–10 second crisp video in natural window light rather than flat static stock images.</text>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m06-personalized-outreach-anatomy.svg", c3_m06)

# C3 M07: Lapsed Client Winback Protocol
c3_m07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Lapsed Client Re-Engagement Ladder: Systematic 4-Stage Winback Protocol</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Reactivating silent past clients without awkwardness, discounting, or aggressive sales pitches</text>

  <!-- Step 1: 90 Days -->
  <rect x="50" y="110" width="230" height="340" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
  <rect x="50" y="110" width="230" height="36" rx="8" fill="#1E293B"/>
  <text x="65" y="134" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">STAGE 1: 90-Day Silence</text>
  
  <text x="65" y="170" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">The Casual Touchpoint</text>
  <text x="65" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Goal: Keep name warm</text>
  <text x="65" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• No product selling</text>
  <text x="65" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Life interest share</text>
  
  <rect x="60" y="260" width="210" height="175" rx="6" fill="#0F172A"/>
  <text x="70" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Recommended Script:</text>
  <text x="70" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Hi David, was thinking of</text>
  <text x="70" y="328" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">that vintage Chronograph</text>
  <text x="70" y="346" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">we talked about. Saw this</text>
  <text x="70" y="364" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">article on dial restorations</text>
  <text x="70" y="382" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and thought of you!"</text>

  <!-- Step 2: 180 Days -->
  <rect x="310" y="110" width="230" height="340" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
  <rect x="310" y="110" width="230" height="36" rx="8" fill="#1E293B"/>
  <text x="325" y="134" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">STAGE 2: 180-Day Silence</text>
  
  <text x="325" y="170" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Service &amp; Spa Value</text>
  <text x="325" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Goal: Re-enter store</text>
  <text x="325" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Complimentary care</text>
  <text x="325" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 6-month prong check</text>
  
  <rect x="320" y="260" width="210" height="175" rx="6" fill="#0F172A"/>
  <text x="330" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Recommended Script:</text>
  <text x="330" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Hi Claire, it's been 6</text>
  <text x="330" y="328" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">months since you took home</text>
  <text x="330" y="346" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">your diamond necklace. Pop</text>
  <text x="330" y="364" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">in for our master ultrasonic</text>
  <text x="330" y="382" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">spa &amp; espresso on us!"</text>

  <!-- Step 3: 270 Days -->
  <rect x="570" y="110" width="230" height="340" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
  <rect x="570" y="110" width="230" height="36" rx="8" fill="#1E293B"/>
  <text x="585" y="134" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">STAGE 3: 270-Day Silence</text>
  
  <text x="585" y="170" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">VIP Private Preview</text>
  <text x="585" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Goal: Spark fresh curiosity</text>
  <text x="585" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Vault trunk show invite</text>
  <text x="585" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High-value aesthetic match</text>
  
  <rect x="580" y="260" width="210" height="175" rx="6" fill="#0F172A"/>
  <text x="590" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Recommended Script:</text>
  <text x="590" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Hi Arthur, our Italian high-</text>
  <text x="590" y="328" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">jewelry trunk show arrives</text>
  <text x="590" y="346" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">next Thursday. I reserved</text>
  <text x="590" y="364" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">2 private preview slots for</text>
  <text x="590" y="382" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">our top collectors."</text>

  <!-- Step 4: 365+ Days -->
  <rect x="830" y="110" width="220" height="340" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
  <rect x="830" y="110" width="220" height="36" rx="8" fill="#1E293B"/>
  <text x="845" y="134" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EC4899">STAGE 4: 365+ Days</text>
  
  <text x="845" y="170" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Handwritten Sincere Note</text>
  <text x="845" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Goal: Reopen relationship</text>
  <text x="845" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Physical luxury card</text>
  <text x="845" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Mailed with stamp</text>
  
  <rect x="840" y="260" width="200" height="175" rx="6" fill="#0F172A"/>
  <text x="850" y="285" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Recommended Card:</text>
  <text x="850" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Happy 1-Year Anniversary!</text>
  <text x="850" y="328" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">It was such an honor helping</text>
  <text x="850" y="346" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">you choose the ring. May</text>
  <text x="850" y="364" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">this milestone be filled</text>
  <text x="850" y="382" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">with joy. — Julian"</text>

  <!-- Diagnostic Checklist Below -->
  <rect x="50" y="475" width="1000" height="170" rx="8" fill="#1E293B"/>
  <text x="70" y="505" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">WHY CLIENTS LAPSE &amp; HOW TO FIX THE ROOT CAUSE:</text>
  <text x="70" y="535" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">1. <strong fill="#F3F4F6">Consultant Neglect (68% of lapsed clients):</strong> They didn't leave because they were angry; they felt forgotten after the sale.</text>
  <text x="70" y="560" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">2. <strong fill="#F3F4F6">Service Failure (14%):</strong> A delayed repair or stiff counter interaction. <em>Solution: Call directly, own the error with grace, offer white-glove resolution.</em></text>
  <text x="70" y="585" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">3. <strong fill="#F3F4F6">Consultant Turnover (18%):</strong> Original salesperson left. <em>Solution: Reassign to a senior advisor with a formal warm introduction letter.</em></text>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m07-lapsed-client-winback-protocol.svg", c3_m07)

# C3 M08: Building a Referral Engine
c3_m08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The Luxury Referral Engine: The 5-Stage Organic Flywheel</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Generating high-net-worth peer referrals without desperate requests or tacky cash bounties</text>

  <!-- Flywheel Flow Nodes -->
  <g transform="translate(60, 110)">
    <!-- Node 1 -->
    <rect x="0" y="0" width="180" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="90" cy="40" r="22" fill="#0F172A" stroke="#38BDF8" stroke-width="2"/>
    <text x="90" y="46" font-family="Inter, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#38BDF8" text-anchor="middle">1</text>
    <text x="90" y="85" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Flawless Unboxing</text>
    <text x="15" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Impeccable packaging</text>
    <text x="15" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pristine polish &amp; presentation</text>
    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Handwritten note included</text>
    <text x="15" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Outcome: High emotion</text>

    <!-- Node 2 -->
    <rect x="200" y="0" width="180" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="290" cy="40" r="22" fill="#0F172A" stroke="#10B981" stroke-width="2"/>
    <text x="290" y="46" font-family="Inter, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#10B981" text-anchor="middle">2</text>
    <text x="290" y="85" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">The Compliment Spark</text>
    <text x="215" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Worn in social settings</text>
    <text x="215" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Friends notice sparkle &amp; cut</text>
    <text x="215" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• "Where did you get that?"</text>
    <text x="215" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Outcome: Social pride</text>

    <!-- Node 3 -->
    <rect x="400" y="0" width="180" height="230" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="490" cy="40" r="22" fill="#0F172A" stroke="#F59E0B" stroke-width="2"/>
    <text x="490" y="46" font-family="Inter, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#F59E0B" text-anchor="middle">3</text>
    <text x="490" y="85" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">The Referral Bridge</text>
    <text x="415" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Proactive advisor touchpoint</text>
    <text x="415" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• "If a friend is looking..."</text>
    <text x="415" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• White-glove concierge offer</text>
    <text x="415" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Outcome: Effortless intro</text>

    <!-- Node 4 -->
    <rect x="600" y="0" width="180" height="230" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <circle cx="690" cy="40" r="22" fill="#0F172A" stroke="#EC4899" stroke-width="2"/>
    <text x="690" y="46" font-family="Inter, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#EC4899" text-anchor="middle">4</text>
    <text x="690" y="85" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">VIP Peer Welcome</text>
    <text x="615" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Referred peer arrives</text>
    <text x="615" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Mention referring friend</text>
    <text x="615" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Red carpet appointment</text>
    <text x="615" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Outcome: Instant trust</text>

    <!-- Node 5 -->
    <rect x="800" y="0" width="180" height="230" rx="8" fill="#161B22" stroke="#A855F7" stroke-width="1.5"/>
    <circle cx="890" cy="40" r="22" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
    <text x="890" y="46" font-family="Inter, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#A855F7" text-anchor="middle">5</text>
    <text x="890" y="85" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Grateful Recognition</text>
    <text x="815" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Immediate handwritten thank you</text>
    <text x="815" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Fine champagne / floral gift</text>
    <text x="815" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Deepened loyalty lock-in</text>
    <text x="815" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#A855F7">Outcome: Perpetual loop</text>
  </g>

  <!-- Verbatim Scripts Comparison -->
  <g transform="translate(60, 370)">
    <rect x="0" y="0" width="470" height="250" rx="8" fill="#161B22" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="470" height="32" rx="8" fill="#450A0A"/>
    <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EF4444">❌ THE CLUMSY / DESPERATE REFERRAL ASK</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">"We really survive on word of mouth, so if you have any friends</text>
    <text x="15" y="73" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">getting engaged, please tell them to come see me. If you send</text>
    <text x="15" y="91" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">someone in who buys, I can give you a $100 store credit card!"</text>
    
    <text x="15" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FCA5A5">Why it fails:</text>
    <text x="15" y="145" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Makes the sales consultant look desperate for commission</text>
    <text x="15" y="165" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Insults high-net-worth clients by treating friendship as a bounty</text>
    <text x="15" y="185" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Degrades the luxury exclusivity of the retail house</text>

    <!-- Professional Script -->
    <rect x="500" y="0" width="480" height="250" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="500" y="0" width="480" height="32" rx="8" fill="#064E3B"/>
    <text x="515" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">✓ THE LUXURY CONCIERGE REFERRAL SCRIPT</text>
    <text x="515" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">"Julian, working together on Sophia's emerald ring was a genuine</text>
    <text x="515" y="73" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">pleasure. Many of our clients have close friends who find fine</text>
    <text x="515" y="91" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">jewelry shopping intimidating. If anyone in your circle ever</text>
    <text x="515" y="109" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">needs private advice or a private salon viewing, please pass</text>
    <text x="515" y="127" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">along my personal mobile. I will take extraordinary care of them."</text>
    
    <text x="515" y="160" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#6EE7B7">Why it succeeds:</text>
    <text x="515" y="180" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#D1FAE5">• Positions you as an elite private advisor helping their peer group</text>
    <text x="515" y="200" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#D1FAE5">• Gives the client social capital to offer exclusive access to friends</text>
  </g>
</svg>"""
write_svg("courses/C3-clienteling-and-crm/assets/c3-m08-referral-engine-flywheel.svg", c3_m08)

print("C3 SVG assets generated successfully!")
