import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# ==========================================
# C3 SVGs (Clienteling & CRM)
# ==========================================

# c3-m02-2-2-2-clienteling-cadence.svg
svg_c3_222 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="680" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="676" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#0284C7" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#7DD3FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">CLIENTELING STANDARD</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">The 2-2-2 Client Retention &amp; Outreach Cadence</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">The systematic relationship cadence: 2 Days (Gratitude) → 2 Weeks (Check-in) → 2 Months (Complimentary Service).</text>
  </g>

  <!-- 3 Cadence Columns -->
  <g transform="translate(50, 125)">
    <!-- Milestone 1: 2 Days -->
    <g transform="translate(0, 0)">
      <rect width="310" height="420" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="40" rx="6" fill="#0284C7" fill-opacity="0.3"/>
      <text x="155" y="40" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">DAY 2: GRATITUDE &amp; CARE</text>

      <g transform="translate(20, 75)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Channel:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Personalized SMS or Handwritten Note</text>

        <text x="0" y="65" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Core Objective:</text>
        <text x="0" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Confirm receipt, affirm choice, zero sales pitch.</text>

        <rect x="-5" y="115" width="280" height="195" rx="6" fill="#0F172A"/>
        <text x="10" y="137" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Approved Outreach Script:</text>
        <text x="10" y="160" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Hi Sarah, it was such a joy helping</text>
        <text x="10" y="176" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">you find the diamond tennis bracelet</text>
        <text x="10" y="192" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">on Tuesday! I wanted to make sure you</text>
        <text x="10" y="208" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">got home safely with the appraisal docs.</text>
        <text x="10" y="224" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Wear it in good health, and please text</text>
        <text x="10" y="240" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">me anytime if you need anything!"</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Goal: Eliminate buyer's remorse immediately.</text>
      </g>
    </g>

    <!-- Milestone 2: 2 Weeks -->
    <g transform="translate(345, 0)">
      <rect width="310" height="420" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="40" rx="6" fill="#059669" fill-opacity="0.3"/>
      <text x="155" y="40" fill="#34D399" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">WEEK 2: REACTION &amp; FIT</text>

      <g transform="translate(20, 75)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Channel:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Warm Phone Call or 1-to-1 Text</text>

        <text x="0" y="65" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Core Objective:</text>
        <text x="0" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Inquire about the proposal/event reaction.</text>

        <rect x="-5" y="115" width="280" height="195" rx="6" fill="#0F172A"/>
        <text x="10" y="137" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Approved Outreach Script:</text>
        <text x="10" y="160" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Hi Michael! I know you had the Napa</text>
        <text x="10" y="176" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">trip planned for this past weekend —</text>
        <text x="10" y="192" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">how did the proposal go?! We're all</text>
        <text x="10" y="208" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">rooting for you here at the store! How</text>
        <text x="10" y="224" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">did the ring fit on her finger?"</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Goal: Celebrate outcome &amp; verify ring size.</text>
      </g>
    </g>

    <!-- Milestone 3: 2 Months -->
    <g transform="translate(690, 0)">
      <rect width="310" height="420" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="40" rx="6" fill="#D97706" fill-opacity="0.3"/>
      <text x="155" y="40" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MONTH 2: COMPLIMENTARY SPA</text>

      <g transform="translate(20, 75)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Channel:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Personal Email / WhatsApp Invitation</text>

        <text x="0" y="65" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Core Objective:</text>
        <text x="0" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Invite back into store for free ultrasonic cleaning.</text>

        <rect x="-5" y="115" width="280" height="195" rx="6" fill="#0F172A"/>
        <text x="10" y="137" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Approved Outreach Script:</text>
        <text x="10" y="160" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Hi Jessica, it's been about two months</text>
        <text x="10" y="176" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">since you picked up your engagement ring.</text>
        <text x="10" y="192" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Stop by anytime this week for an espresso</text>
        <text x="10" y="208" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">and a complimentary ultrasonic sparkle</text>
        <text x="10" y="224" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">clean and prong inspection on our bench!"</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Goal: In-store foot traffic for wedding band look.</text>
      </g>
    </g>
  </g>

  <!-- Bottom CRM Golden Rule -->
  <g transform="translate(50, 565)">
    <rect width="1000" height="90" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="25" y="25" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">THE COMPOUNDING LAW OF CLIENTELING</text>
    <text x="25" y="48" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• An associate who executes the 2-2-2 cadence on every client builds a personal client book that delivers 60%+ of their annual sales volume</text>
    <text x="25" y="68" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">  by Year 3 through repeat purchases, wedding bands, anniversaries, and zero-acquisition-cost referrals.</text>
  </g>
</svg>"""

save_svg("courses/C3-clienteling-and-crm/assets/c3-m02-2-2-2-clienteling-cadence.svg", svg_c3_222)

# ==========================================
# C12 SVGs (Retail KPIs & Reporting)
# ==========================================

# c12-m01-retail-kpi-hierarchy-pyramid.svg
svg_c12_kpi = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="700" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="696" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#10B981" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">STORE METRICS &amp; KPIS</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Jewelry Retail KPI Cascade Hierarchy</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Connecting Top-Line P&amp;L Financial Health (GMROI) directly to Sales Floor Behaviors.</text>
  </g>

  <!-- KPI Hierarchy Blocks -->
  <g transform="translate(50, 125)">
    <!-- Level 1: Top-Line Executive Financials -->
    <g transform="translate(250, 0)">
      <rect width="500" height="95" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="2"/>
      <rect x="15" y="12" width="470" height="25" rx="4" fill="#D97706" fill-opacity="0.3"/>
      <text x="250" y="30" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">LEVEL 1: EXECUTIVE P&amp;L PROFITABILITY</text>
      <text x="25" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Gross Margin $ | GMROI (Gross Margin Return on Inventory) | Comp-Store Sales %</text>
      <text x="25" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Formula: GMROI = (Gross Margin $ / Average Inventory at Cost) | Target: &gt; 1.8 to 2.5</text>
    </g>

    <!-- Connector 1 -->
    <line x1="500" y1="95" x2="500" y2="135" stroke="#F59E0B" stroke-width="2"/>

    <!-- Level 2: Store Operational Productivity -->
    <g transform="translate(130, 135)">
      <rect width="740" height="105" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="12" width="710" height="25" rx="4" fill="#0284C7" fill-opacity="0.3"/>
      <text x="370" y="30" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">LEVEL 2: STORE TRAFFIC &amp; SALES REVENUE ENGINE</text>
      <text x="25" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Total Net Sales $ = Door Traffic × Closing Conversion % × Average Ticket Value (ATV)</text>
      <text x="25" y="82" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Conversion Target:</tspan> 18% – 25% (Bridal) | <tspan font-weight="700">Inventory Turn:</tspan> 1.0 – 1.4x annually</text>
    </g>

    <!-- Connector 2 -->
    <line x1="250" y1="240" x2="250" y2="280" stroke="#38BDF8" stroke-width="2"/>
    <line x1="500" y1="240" x2="500" y2="280" stroke="#38BDF8" stroke-width="2"/>
    <line x1="750" y1="240" x2="750" y2="280" stroke="#38BDF8" stroke-width="2"/>

    <!-- Level 3: Associate Floor Levers -->
    <g transform="translate(0, 280)">
      <!-- Lever A: Conversion -->
      <g transform="translate(0, 0)">
        <rect width="310" height="230" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
        <rect x="15" y="15" width="280" height="30" rx="4" fill="#059669" fill-opacity="0.3"/>
        <text x="155" y="35" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">A. CONVERSION DRIVERS</text>
        <g transform="translate(15, 60)">
          <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Behavioral Levers:</text>
          <text x="0" y="33" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• 1st 90s context opener</text>
          <text x="0" y="49" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• 4-pillar discovery depth</text>
          <text x="0" y="65" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Fast 1st piece out on pad</text>
          <text x="0" y="81" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Objection isolation skill</text>
          <rect x="0" y="100" width="280" height="50" rx="4" fill="#0F172A"/>
          <text x="10" y="120" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Coaching Metric:</text>
          <text x="10" y="136" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9">Inquiries to Pad Presentation ratio.</text>
        </g>
      </g>

      <!-- Lever B: Average Ticket Value -->
      <g transform="translate(345, 0)">
        <rect width="310" height="230" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
        <rect x="15" y="15" width="280" height="30" rx="4" fill="#D97706" fill-opacity="0.3"/>
        <text x="155" y="35" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">B. AVERAGE TICKET (ATV)</text>
        <g transform="translate(15, 60)">
          <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Behavioral Levers:</text>
          <text x="0" y="33" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Top-down price anchoring</text>
          <text x="0" y="49" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Platinum vs gold upgrade</text>
          <text x="0" y="65" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Diamond 4Cs value trade-up</text>
          <text x="0" y="81" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• 12-mo financing promotion</text>
          <rect x="0" y="100" width="280" height="50" rx="4" fill="#0F172A"/>
          <text x="10" y="120" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Coaching Metric:</text>
          <text x="10" y="136" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9">% of sales presented with financing.</text>
        </g>
      </g>

      <!-- Lever C: Units Per Transaction & Attach -->
      <g transform="translate(690, 0)">
        <rect width="310" height="230" rx="8" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
        <rect x="15" y="15" width="280" height="30" rx="4" fill="#7E22CE" fill-opacity="0.3"/>
        <text x="155" y="35" fill="#C084FC" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">C. UPT &amp; ATTACH %</text>
        <g transform="translate(15, 60)">
          <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Behavioral Levers:</text>
          <text x="0" y="33" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Wedding band at engagement</text>
          <text x="0" y="49" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Matching earrings / necklace</text>
          <text x="0" y="65" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Jewelry care &amp; cleaner kits</text>
          <text x="0" y="81" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Extended warranty attach</text>
          <rect x="0" y="100" width="280" height="50" rx="4" fill="#0F172A"/>
          <text x="10" y="120" fill="#C084FC" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Coaching Metric:</text>
          <text x="10" y="136" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9">UPT Target: 1.35 to 1.65 items/trans.</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Bottom Diagnostic Rule -->
  <g transform="translate(50, 645)">
    <text x="500" y="20" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Root-Cause Rule: A revenue miss is never "just sales" — diagnose whether Traffic, Conversion, ATV, or UPT dropped.</text>
  </g>
</svg>"""

save_svg("courses/C12-retail-kpis-reporting/assets/c12-m01-retail-kpi-hierarchy-pyramid.svg", svg_c12_kpi)

print("Wave 2 priority SVGs generated!")

