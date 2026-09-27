import os

def write_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath}")

# C12 M02: Traffic & Conversion Funnel
c12_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Traffic &amp; Conversion Analytics: The 4-Stage Storefront Funnel</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Measuring customer progression from exterior door swings to closed fine jewelry transactions</text>

  <!-- Funnel Visual on Left -->
  <g transform="translate(50, 110)">
    <!-- Stage 1 -->
    <polygon points="40,0 460,0 410,70 90,70" fill="#38BDF8" fill-opacity="0.85"/>
    <text x="250" y="42" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">1. RAW DOOR SWINGS (1,000 Walk-Ins / Wk)</text>

    <!-- Stage 2 -->
    <polygon points="90,75 410,75 360,145 140,145" fill="#10B981" fill-opacity="0.85"/>
    <text x="250" y="117" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">2. QUALIFIED OPPORTUNITIES (650 Engaged)</text>

    <!-- Stage 3 -->
    <polygon points="140,150 360,150 310,220 190,220" fill="#F59E0B" fill-opacity="0.85"/>
    <text x="250" y="192" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">3. SHOWCASE PRESENTATIONS (320 Trays Out)</text>

    <!-- Stage 4 -->
    <polygon points="190,225 310,225 280,295 220,295" fill="#EC4899" fill-opacity="0.9"/>
    <text x="250" y="267" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">4. CLOSED SALES (140 Sales)</text>
  </g>

  <!-- Detail Metrics on Right -->
  <g transform="translate(550, 100)">
    <!-- Metric 1 -->
    <rect x="0" y="0" width="500" height="75" rx="6" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="20" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">DOOR TRAFFIC FILTERING &amp; TRAFFIC COUNTERS</text>
    <text x="20" y="48" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Filter out staff ins/outs, delivery couriers, and children</text>
    <text x="20" y="65" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Measure peak traffic hours (Saturday 1–4 PM = 42% volume)</text>

    <!-- Metric 2 -->
    <rect x="0" y="85" width="500" height="75" rx="6" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <text x="20" y="110" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">ENGAGEMENT RATE (65% Target)</text>
    <text x="20" y="133" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• % of door swings transitioning past 10-second decompression</text>
    <text x="20" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Direct correlation with greeting speed and 45-degree floor posture</text>

    <!-- Metric 3 -->
    <rect x="0" y="170" width="500" height="75" rx="6" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="20" y="195" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">SHOWCASE PRESENTATION RATE (49% of Engaged)</text>
    <text x="20" y="218" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• % of qualified clients who experience a piece on the velvet tray</text>
    <text x="20" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Physical try-on increases final purchase probability by 3.8×</text>

    <!-- Metric 4 -->
    <rect x="0" y="255" width="500" height="75" rx="6" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <text x="20" y="280" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">STORE CONVERSION RATE (14.0% Overall Store Conversion)</text>
    <text x="20" y="303" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Total Transactions (140) ÷ Raw Door Swings (1,000) = 14.0%</text>
    <text x="20" y="320" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Presentation-to-Close Rate = 140 ÷ 320 = 43.8% Closing Efficiency</text>
  </g>

  <!-- Diagnostic Table Bottom -->
  <g transform="translate(50, 440)">
    <rect x="0" y="0" width="1000" height="190" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">INDUSTRY BENCHMARK CONVERSION TARGETS BY STORE TYPE:</text>

    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="960" height="28" fill="#0F172A"/>
      <text x="15" y="19" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">RETAIL FORMAT</text>
      <text x="250" y="19" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">TYPICAL CONVERSION RANGE</text>
      <text x="580" y="19" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">PRIMARY DRIVER OF VARIANCE</text>

      <text x="15" y="48" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F3F4F6">High-Street Flagship / Street Front</text>
      <text x="250" y="48" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">18% – 25%</text>
      <text x="580" y="48" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">High intentionality; low casual foot traffic</text>

      <text x="15" y="76" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F3F4F6">Luxury Regional Shopping Center / Mall</text>
      <text x="250" y="76" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">11% – 16%</text>
      <text x="580" y="76" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">High casual browser volume; requires strong qualification</text>

      <text x="15" y="104" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F3F4F6">Private Salon / Appointment By-Invitation</text>
      <text x="250" y="104" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">65% – 85%</text>
      <text x="580" y="104" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Pre-qualified budget and pre-selected curated pieces</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m02-traffic-conversion-funnel.svg", c12_m02)

# C12 M03: Average Ticket, UPT, and Product Mix Engine
c12_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The High-Ticket Sales Engine: ATV, UPT &amp; Category Mix</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">The mathematical levers that multiply retail gross margin and store top-line revenue</text>

  <!-- Formula Equation Card -->
  <g transform="translate(50, 100)">
    <rect x="0" y="0" width="1000" height="110" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="25" y="32" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE MASTER RETAIL REVENUE EQUATION:</text>
    
    <g transform="translate(25, 45)">
      <rect x="0" y="10" width="180" height="42" rx="6" fill="#0F172A" stroke="#38BDF8"/>
      <text x="90" y="36" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8" text-anchor="middle">TRAFFIC</text>

      <text x="200" y="36" font-family="Inter, -apple-system, sans-serif" font-size="18" font-weight="bold" fill="#94A3B8">×</text>

      <rect x="225" y="10" width="180" height="42" rx="6" fill="#0F172A" stroke="#10B981"/>
      <text x="315" y="36" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981" text-anchor="middle">CONVERSION %</text>

      <text x="425" y="36" font-family="Inter, -apple-system, sans-serif" font-size="18" font-weight="bold" fill="#94A3B8">×</text>

      <rect x="450" y="10" width="220" height="42" rx="6" fill="#0F172A" stroke="#F59E0B"/>
      <text x="560" y="36" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B" text-anchor="middle">AVG TICKET (ATV)</text>

      <text x="690" y="36" font-family="Inter, -apple-system, sans-serif" font-size="18" font-weight="bold" fill="#94A3B8">=</text>

      <rect x="715" y="10" width="235" height="42" rx="6" fill="#064E3B" stroke="#10B981"/>
      <text x="832" y="36" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#D1FAE5" text-anchor="middle">GROSS SALES ($)</text>
    </g>
  </g>

  <!-- 3 Strategic Levers Grid -->
  <g transform="translate(50, 230)">
    <!-- Lever 1: ATV -->
    <rect x="0" y="0" width="315" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. AVERAGE TICKET (ATV)</text>
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Formula: Total Sales $ ÷ Transactions</text>
    <text x="15" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Example: $350,000 ÷ 140 = $2,500 ATV</text>
    <text x="15" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">How to Drive on Floor:</text>
    <text x="15" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Diamond upgrade laddering (e.g. 1.0ct → 1.25ct)</text>
    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Metal tier upselling (14K → 18K / Platinum)</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 0% financing to bridge payment spread</text>
    <text x="15" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Impact: Expands revenue without extra traffic</text>

    <!-- Lever 2: UPT -->
    <rect x="340" y="0" width="315" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="340" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="355" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. UNITS PER TRANSACTION (UPT)</text>
    <text x="355" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Formula: Total Units Sold ÷ Transactions</text>
    <text x="355" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Example: 182 units ÷ 140 sales = 1.30 UPT</text>
    <text x="355" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">How to Drive on Floor:</text>
    <text x="355" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Companion add-on: Matching diamond studs</text>
    <text x="355" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Wedding band attach at ring purchase</text>
    <text x="355" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Jewelry care kit &amp; travel case attach</text>
    <text x="355" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Impact: High-margin incremental profit</text>

    <!-- Lever 3: Category Mix -->
    <rect x="680" y="0" width="320" height="230" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="0" width="320" height="36" rx="8" fill="#1E293B"/>
    <text x="695" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. CATEGORY PRODUCT MIX</text>
    <text x="695" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Optimal Fine Jewelry Margin Mix:</text>
    <text x="695" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Bridal &amp; Engagement: 45% (High ATV)</text>
    <text x="695" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Fashion Diamond / Gold: 30% (55% Margin)</text>
    <text x="695" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Timepieces: 15% (Brand Prestige)</text>
    <text x="695" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Custom Design &amp; Repair: 10% (75% Margin)</text>
    <text x="695" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Goal: Balance high dollar volume with high margin rate</text>
  </g>

  <!-- Summary Box Bottom -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE COMPOUNDING MULTIPLIER EFFECT:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">If a store increases <strong fill="#10B981">Conversion by 10%</strong>, increases <strong fill="#38BDF8">ATV by 10%</strong>, and lifts <strong fill="#F59E0B">UPT by 5%</strong>:</text>
    <text x="20" y="82" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">Total Store Revenue Increases by +27.05% Without Spending an Extra Dollar on Traffic Advertising.</text>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m03-atv-upt-product-mix-engine.svg", c12_m03)

# C12 M04: Inventory Productivity Dashboard
c12_m04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Inventory Productivity &amp; Health: Sell-Through, Turn &amp; GMROI</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Mastering inventory capital efficiency, aged stock depreciation, and Gross Margin Return on Investment</text>

  <!-- 3 Inventory Metric Cards -->
  <g transform="translate(50, 100)">
    <!-- Metric 1: Sell-Through Rate -->
    <rect x="0" y="0" width="315" height="280" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. SELL-THROUGH RATE (STR)</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Formula:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#38BDF8">(Units Sold ÷ Starting Stock) × 100</text>

    <text x="15" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Worked Example:</text>
    <text x="15" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Brought in 50 tennis bracelets in Nov.</text>
    <text x="15" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Sold 35 by Dec 31.</text>
    <text x="15" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">STR = (35 ÷ 50) × 100 = 70.0%</text>

    <text x="15" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Target Benchmarks:</text>
    <text x="15" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Core Bridal: 60–75% per year</text>
    <text x="15" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Holiday Seasonal: 70%+ in 60 days</text>

    <!-- Metric 2: Inventory Turn -->
    <rect x="340" y="0" width="315" height="280" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="340" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="355" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. INVENTORY TURN</text>
    
    <text x="355" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Formula:</text>
    <text x="355" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#10B981">Annual COGS ÷ Average Inventory Cost</text>

    <text x="355" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Worked Example:</text>
    <text x="355" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Annual Cost of Goods Sold = $1.8M</text>
    <text x="355" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Average Vault Inventory Cost = $1.2M</text>
    <text x="355" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Turn = $1.8M ÷ $1.2M = 1.5× Turns/Yr</text>

    <text x="355" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Target Benchmarks:</text>
    <text x="355" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Fine Jewelry Average: 1.0× – 1.4×</text>
    <text x="355" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• High-Performing Store: 1.8× – 2.2×</text>

    <!-- Metric 3: GMROI -->
    <rect x="680" y="0" width="320" height="280" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="0" width="320" height="36" rx="8" fill="#1E293B"/>
    <text x="695" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. GMROI (Profit Efficiency)</text>
    
    <text x="695" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Formula:</text>
    <text x="695" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F59E0B">Gross Margin $ ÷ Average Inventory Cost</text>

    <text x="695" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Worked Example:</text>
    <text x="695" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Gross Margin Generated = $1.6M</text>
    <text x="695" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Average Vault Inventory Cost = $1.0M</text>
    <text x="695" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">GMROI = $1.60 Gross Profit per $1.00</text>

    <text x="695" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Target Benchmarks:</text>
    <text x="695" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Minimum Threshold: &gt; $1.25</text>
    <text x="695" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• High Luxury Benchmark: $1.75 – $2.50</text>
  </g>

  <!-- Aged Inventory Action Protocol Bottom -->
  <g transform="translate(50, 400)">
    <rect x="0" y="0" width="1000" height="230" rx="8" fill="#161B22" stroke="#334155"/>
    <rect x="0" y="0" width="1000" height="32" rx="8" fill="#1E293B"/>
    <text x="20" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EF4444">AGED INVENTORY ACTION PROTOCOL (PREVENTING DEAD CAPITAL)</text>

    <g transform="translate(20, 45)">
      <!-- 0-180 Days -->
      <rect x="0" y="0" width="220" height="160" rx="6" fill="#0F172A" stroke="#10B981"/>
      <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">0 – 180 DAYS: FRESH</text>
      <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Prime showcase placement</text>
      <text x="15" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Full markup price integrity</text>
      <text x="15" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Active client wishlist matching</text>
      <text x="15" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Status: Peak Earning</text>

      <!-- 181-365 Days -->
      <rect x="245" y="0" width="220" height="160" rx="6" fill="#0F172A" stroke="#F59E0B"/>
      <text x="260" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">181 – 365 DAYS: AGING</text>
      <text x="260" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Rotate showcase &amp; lighting</text>
      <text x="260" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Feature in digital newsletter</text>
      <text x="260" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Associate incentive / spiff</text>
      <text x="260" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Status: Attention Needed</text>

      <!-- 366-730 Days -->
      <rect x="490" y="0" width="220" height="160" rx="6" fill="#0F172A" stroke="#EF4444"/>
      <text x="505" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">366 – 730 DAYS: CRITICAL</text>
      <text x="505" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Vendor stock rebalancing/RTV</text>
      <text x="505" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• VIP Private Trunk Show edit</text>
      <text x="505" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Bundle with wedding band</text>
      <text x="505" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Status: Margin Discount</text>

      <!-- 730+ Days -->
      <rect x="735" y="0" width="225" height="160" rx="6" fill="#0F172A" stroke="#94A3B8"/>
      <text x="750" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">730+ DAYS: DEAD CAPITAL</text>
      <text x="750" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Unmount center stone</text>
      <text x="750" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Melt metal for scrap credit</text>
      <text x="750" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Reset stone into modern CAD</text>
      <text x="750" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">Status: Workshop Reclaim</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m04-inventory-productivity-dashboard.svg", c12_m04)

# C12 M05: Retention and Client Book Health Scorecard
c12_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Client Retention &amp; Book Health Scorecard: The 4 Core Metrics</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Quantifying the long-term value, active retention, and repeat sales efficiency of consultant client books</text>

  <!-- 4 Scorecard Quadrants -->
  <g transform="translate(50, 100)">
    <!-- Metric 1: Active Client Rate -->
    <rect x="0" y="0" width="480" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="480" height="36" rx="8" fill="#1E293B"/>
    <text x="20" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">1. ACTIVE BOOK RATIO (12-Month Recency)</text>
    
    <text x="20" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">Formula: (Clients Purchasing in Last 12 Mo ÷ Total Assigned Clients) × 100</text>
    <text x="20" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Standard Benchmark: 22% – 30% Active</text>
    <text x="20" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Elite Consultant Benchmark: 40% – 55% Active</text>
    <text x="20" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Manager Floor Diagnosis:</text>
    <text x="20" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">If an associate's book falls below 20%, their book is over-bloated with unworked</text>
    <text x="20" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">leads. Reallocate dormant accounts to hungry junior associates.</text>
    <text x="20" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Target: Maintain &gt; 35% Active Book</text>

    <!-- Metric 2: Repeat Purchase Frequency -->
    <rect x="520" y="0" width="480" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="520" y="0" width="480" height="36" rx="8" fill="#1E293B"/>
    <text x="540" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">2. REPEAT PURCHASE RATE (Multi-Buyers)</text>
    
    <text x="540" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">Formula: (Clients with &gt;1 Transaction ÷ Total Transacting Clients) × 100</text>
    <text x="540" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Standard Benchmark: 18% Repeat</text>
    <text x="540" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Elite Luxury Guild Benchmark: 35% – 48% Repeat</text>
    <text x="540" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Manager Floor Diagnosis:</text>
    <text x="540" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">High initial bridal sales without repeat purchases indicates a failure of the</text>
    <text x="540" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">2-2-2 post-sale follow-up cadence.</text>
    <text x="540" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Target: Convert 40% of Bridal into Multi-Buyers</text>

    <!-- Metric 3: Outreach-to-Appointment Rate -->
    <rect x="0" y="250" width="480" height="230" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="0" y="250" width="480" height="36" rx="8" fill="#1E293B"/>
    <text x="20" y="274" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">3. OUTREACH-TO-APPOINTMENT RATIO</text>
    
    <text x="20" y="310" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">Formula: (Booked In-Store Appointments ÷ CRM Outreaches Sent) × 100</text>
    <text x="20" y="335" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Broadcast Mass SMS: 1.5% Appointment Rate (Poor)</text>
    <text x="20" y="355" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Bespoke Video Outreach: 14% – 22% Appointment Rate (High)</text>
    <text x="20" y="385" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Manager Floor Diagnosis:</text>
    <text x="20" y="405" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Measures the personalization quality of consultant text/video outreach.</text>
    <text x="20" y="425" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Higher ratio proves relevance to client tastes.</text>
    <text x="20" y="455" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Target: 1 Appointment per 8 Outreaches (12.5%)</text>

    <!-- Metric 4: Client Lifetime Value (LTV) -->
    <rect x="520" y="250" width="480" height="230" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="520" y="250" width="480" height="36" rx="8" fill="#1E293B"/>
    <text x="540" y="274" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EC4899">4. CLIENT LIFETIME VALUE (LTV)</text>
    
    <text x="540" y="310" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">Formula: Cumulative Total Spend Across Customer Relationship Span</text>
    <text x="540" y="335" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• First Engagement Purchase: $7,500</text>
    <text x="540" y="355" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Wedding Bands: $3,200 • 1st Anniv: $1,800 • 5th Anniv: $8,500</text>
    <text x="540" y="385" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">5-Year Realized LTV = $21,000</text>
    <text x="540" y="405" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Acquisition Cost amortizes to near-zero as repeat sales flow in</text>
    <text x="540" y="425" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">with zero incremental advertising expense.</text>
    <text x="540" y="455" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Target: 3.5× LTV-to-CAC Ratio</text>
  </g>

  <!-- Summary Box Bottom -->
  <g transform="translate(50, 500)">
    <rect x="0" y="0" width="1000" height="130" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE ULTIMATE TRUTH OF FINE JEWELRY RETAIL:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">It costs 6× to 9× more in marketing dollars to attract a brand new walk-in client than to retain an existing collector. <strong fill="#10B981">A healthy client book is the most valuable financial asset in the jewelry store.</strong></text>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m05-client-book-health-scorecard.svg", c12_m05)

# C12 M06: Weekly Store KPI Dashboard Mockup
c12_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Executive Weekly Store Dashboard: Fine Jewelry Performance</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Store 104 — Week 42 Performance Summary (Sales vs Plan, Conversion, ATV, and Staff Leaderboard)</text>

  <!-- Top Metrics Bar -->
  <g transform="translate(50, 95)">
    <!-- Metric 1: Total Sales -->
    <rect x="0" y="0" width="235" height="85" rx="6" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">WEEKLY SALES</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="22" font-weight="bold" fill="#10B981">$184,500</text>
    <text x="15" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#10B981">▲ 108.5% of Plan ($170k)</text>

    <!-- Metric 2: Conversion -->
    <rect x="255" y="0" width="235" height="85" rx="6" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="270" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">STORE CONVERSION</text>
    <text x="270" y="55" font-family="Inter, -apple-system, sans-serif" font-size="22" font-weight="bold" fill="#38BDF8">16.4%</text>
    <text x="270" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#38BDF8">▲ +1.8% vs LY (14.6%)</text>

    <!-- Metric 3: ATV -->
    <rect x="510" y="0" width="235" height="85" rx="6" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="525" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">AVERAGE TICKET (ATV)</text>
    <text x="525" y="55" font-family="Inter, -apple-system, sans-serif" font-size="22" font-weight="bold" fill="#F59E0B">$3,481</text>
    <text x="525" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F59E0B">Plan: $3,200 (53 Sales)</text>

    <!-- Metric 4: UPT & Margin -->
    <rect x="765" y="0" width="235" height="85" rx="6" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <text x="780" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">GROSS MARGIN %</text>
    <text x="780" y="55" font-family="Inter, -apple-system, sans-serif" font-size="22" font-weight="bold" fill="#EC4899">52.3%</text>
    <text x="780" y="75" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#EC4899">UPT: 1.34 Units/Sale</text>
  </g>

  <!-- Middle: Associate Leaderboard & Category Breakdown -->
  <g transform="translate(50, 200)">
    <!-- Associate Table -->
    <rect x="0" y="0" width="580" height="290" rx="8" fill="#161B22" stroke="#334155"/>
    <rect x="0" y="0" width="580" height="32" rx="8" fill="#1E293B"/>
    <text x="20" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">SALES CONSULTANT SCORECARD</text>

    <g transform="translate(15, 40)">
      <!-- Table Header -->
      <text x="10" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">CONSULTANT</text>
      <text x="170" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">SALES ($)</text>
      <text x="270" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">% PLAN</text>
      <text x="350" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">CONV %</text>
      <text x="440" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#94A3B8">ATV</text>

      <!-- Row 1 -->
      <rect x="0" y="30" width="550" height="36" rx="4" fill="#0F172A"/>
      <text x="10" y="53" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">1. Sarah Jenkins</text>
      <text x="170" y="53" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">$64,200</text>
      <text x="270" y="53" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#10B981">128%</text>
      <text x="350" y="53" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">21.2%</text>
      <text x="440" y="53" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">$4,280</text>

      <!-- Row 2 -->
      <rect x="0" y="70" width="550" height="36" rx="4" fill="#161B22"/>
      <text x="10" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">2. Michael Chang</text>
      <text x="170" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">$48,100</text>
      <text x="270" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#10B981">114%</text>
      <text x="350" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">17.5%</text>
      <text x="440" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">$3,700</text>

      <!-- Row 3 -->
      <rect x="0" y="110" width="550" height="36" rx="4" fill="#0F172A"/>
      <text x="10" y="133" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">3. Elena Rostova</text>
      <text x="170" y="133" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">$42,800</text>
      <text x="270" y="133" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F59E0B">95%</text>
      <text x="350" y="133" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">15.1%</text>
      <text x="440" y="133" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">$3,057</text>

      <!-- Row 4 -->
      <rect x="0" y="150" width="550" height="36" rx="4" fill="#161B22"/>
      <text x="10" y="173" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">4. David Vance</text>
      <text x="170" y="173" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">$29,400</text>
      <text x="270" y="173" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#EF4444">78%</text>
      <text x="350" y="173" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FCA5A5">11.8%</text>
      <text x="440" y="173" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">$2,450</text>

      <!-- Coaching Callout -->
      <rect x="0" y="195" width="550" height="42" rx="4" fill="#2A1215" stroke="#EF4444"/>
      <text x="10" y="221" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">Coaching Priority: David Vance — Conversion miss (11.8%). Coach on 1st 90s discovery.</text>
    </g>

    <!-- Category Mix Box -->
    <rect x="605" y="0" width="395" height="290" rx="8" fill="#161B22" stroke="#334155"/>
    <rect x="605" y="0" width="395" height="32" rx="8" fill="#1E293B"/>
    <text x="625" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">CATEGORY SALES BREAKDOWN</text>

    <g transform="translate(625, 50)">
      <text x="0" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Bridal &amp; Engagement</text>
      <text x="260" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">$88,500 (48%)</text>
      <rect x="0" y="28" width="350" height="10" rx="3" fill="#334155"/>
      <rect x="0" y="28" width="168" height="10" rx="3" fill="#38BDF8"/>

      <text x="0" y="65" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Diamond Fashion &amp; Gold</text>
      <text x="260" y="65" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">$55,300 (30%)</text>
      <rect x="0" y="73" width="350" height="10" rx="3" fill="#334155"/>
      <rect x="0" y="73" width="105" height="10" rx="3" fill="#10B981"/>

      <text x="0" y="110" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Luxury Timepieces</text>
      <text x="260" y="110" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">$24,000 (13%)</text>
      <rect x="0" y="118" width="350" height="10" rx="3" fill="#334155"/>
      <rect x="0" y="118" width="45" height="10" rx="3" fill="#F59E0B"/>

      <text x="0" y="155" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Custom &amp; Repair Services</text>
      <text x="260" y="155" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EC4899">$16,700 (9%)</text>
      <rect x="0" y="163" width="350" height="10" rx="3" fill="#334155"/>
      <rect x="0" y="163" width="31" height="10" rx="3" fill="#EC4899"/>

      <text x="0" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Total Gross Margin Rate: 52.3% (Target: 50.0%)</text>
    </g>
  </g>

  <!-- Bottom Takeaway -->
  <g transform="translate(50, 510)">
    <rect x="0" y="0" width="1000" height="120" rx="8" fill="#1E293B"/>
    <text x="20" y="28" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">STORE MANAGER ACTION ITEMS FOR WEEK 43:</text>
    <text x="20" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">1. Run 15-minute morning huddle on diamond studs attach to lift UPT from 1.34 to 1.45.</text>
    <text x="20" y="78" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">2. Pair David Vance with Sarah Jenkins on Saturday floor shifts for discovery shadow coaching.</text>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m06-weekly-store-kpi-dashboard-mockup.svg", c12_m06)

# C12 M07: Sales Miss Root Cause Diagnostic Tree
c12_m07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Sales Miss Root-Cause Diagnostic Tree: The 4 Failure Nodes</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Systematically troubleshooting store performance deficits instead of blaming the market or economy</text>

  <!-- Root Problem Top -->
  <g transform="translate(50, 100)">
    <rect x="360" y="0" width="280" height="60" rx="8" fill="#450A0A" stroke="#EF4444" stroke-width="2"/>
    <text x="500" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FCA5A5" text-anchor="middle">STORE MISSED SALES TARGET (-15%)</text>
    <text x="500" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA" text-anchor="middle">Isolate Which Metric Lever Broke First</text>

    <!-- 4 Diagnostic Branches -->
    <!-- Node 1: Traffic Miss -->
    <path d="M 400 60 L 115 130" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="130" width="230" height="340" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="130" width="230" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="152" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. TRAFFIC DEFICIT</text>
    
    <text x="15" y="185" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Symptom:</text>
    <text x="15" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Door swings down &gt;15%</text>
    <text x="15" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Conversion &amp; ATV normal</text>

    <text x="15" y="260" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Root Causes:</text>
    <text x="15" y="280" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Mall foot traffic slump</text>
    <text x="15" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Consultant CRM outreach stopped</text>
    <text x="15" y="316" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Bad weather / road closures</text>

    <rect x="10" y="340" width="210" height="115" rx="6" fill="#0F172A"/>
    <text x="15" y="365" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Corrective Action:</text>
    <text x="15" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Mandate 10 daily CRM client</text>
    <text x="15" y="408" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">  outreaches per consultant</text>
    <text x="15" y="426" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Host private VIP salon event</text>

    <!-- Node 2: Conversion Miss -->
    <path d="M 460 60 L 370 130" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="130" width="230" height="340" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="130" width="230" height="32" rx="8" fill="#1E293B"/>
    <text x="270" y="152" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. CONVERSION MISS</text>
    
    <text x="270" y="185" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Symptom:</text>
    <text x="270" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High traffic, low sales count</text>
    <text x="270" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Conversion drops below 12%</text>

    <text x="270" y="260" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Root Causes:</text>
    <text x="270" y="280" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Staff overwhelmed / understaffed</text>
    <text x="270" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Weak discovery; rushing closes</text>
    <text x="270" y="316" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Clumsy handling of "just looking"</text>

    <rect x="265" y="340" width="210" height="115" rx="6" fill="#0F172A"/>
    <text x="270" y="365" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Corrective Action:</text>
    <text x="270" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Adjust peak schedule staffing</text>
    <text x="270" y="408" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Drill "First 90 Seconds" opener</text>
    <text x="270" y="426" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Mandatory tray pull on walk-ins</text>

    <!-- Node 3: ATV Erosion -->
    <path d="M 540 60 L 625 130" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="130" width="230" height="340" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="130" width="230" height="32" rx="8" fill="#1E293B"/>
    <text x="525" y="152" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. ATV EROSION</text>
    
    <text x="525" y="185" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Symptom:</text>
    <text x="525" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Sales count solid, $ miss</text>
    <text x="525" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• ATV falls from $3,500 to $1,900</text>

    <text x="525" y="260" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Root Causes:</text>
    <text x="525" y="280" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Selling from own wallet (fear)</text>
    <text x="525" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Premature discounting at counter</text>
    <text x="525" y="316" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Lack of diamond size upselling</text>

    <rect x="520" y="340" width="210" height="115" rx="6" fill="#0F172A"/>
    <text x="525" y="365" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Corrective Action:</text>
    <text x="525" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Practice 4Cs ladder upselling</text>
    <text x="525" y="408" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Restrict unapproved discounts</text>
    <text x="525" y="426" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Promote 12-mo 0% financing</text>

    <!-- Node 4: UPT Collapse -->
    <path d="M 600 60 L 880 130" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="130" width="235" height="340" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="130" width="235" height="32" rx="8" fill="#1E293B"/>
    <text x="780" y="152" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. UPT COLLAPSE</text>
    
    <text x="780" y="185" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Symptom:</text>
    <text x="780" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• UPT hovers at 1.05</text>
    <text x="780" y="225" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Every sale is a single item</text>

    <text x="780" y="260" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Root Causes:</text>
    <text x="780" y="280" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Ringing sale immediately upon 'yes'</text>
    <text x="780" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• Forgetting companion pieces</text>
    <text x="780" y="316" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#FECACA">• No care product add-on</text>

    <rect x="775" y="340" width="215" height="115" rx="6" fill="#0F172A"/>
    <text x="780" y="365" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Corrective Action:</text>
    <text x="780" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Train the "While I write this up"</text>
    <text x="780" y="408" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">  companion presentation move</text>
    <text x="780" y="426" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Set 1.35 UPT store standard</text>
  </g>

  <!-- Summary Box Bottom -->
  <g transform="translate(50, 500)">
    <rect x="0" y="0" width="1000" height="130" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE GENERAL MANAGER'S DIAGNOSTIC CREED:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Never say <em>"Sales were down this week because nobody was buying."</em> Isolate the exact broken mathematical variable (Traffic, Conversion, ATV, or UPT) and execute targeted behavioral coaching within 24 hours.</text>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m07-sales-miss-root-cause-tree.svg", c12_m07)

# C12 M08: The 1-Page Store Review
c12_m08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The 1-Page Executive Store Performance Review Template</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Standardized monthly reporting architecture for store directors presenting up to ownership &amp; executive leadership</text>

  <!-- 4-Quadrant Monthly Executive Sheet -->
  <g transform="translate(50, 100)">
    <!-- Quadrant 1: P&L Financial Snapshot -->
    <rect x="0" y="0" width="480" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">SECTION 1: P&amp;L FINANCIAL SNAPSHOT</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Gross Sales Revenue:</text>
      <text x="240" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">$742,000 (106% vs Plan)</text>

      <text x="0" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Cost of Goods Sold (COGS):</text>
      <text x="240" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">$356,160 (48.0%)</text>

      <text x="0" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Gross Margin Dollars ($):</text>
      <text x="240" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">$385,840 (52.0% Margin)</text>

      <text x="0" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Store Operating Expenses:</text>
      <text x="240" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">$188,000 (Rent, Payroll, Ops)</text>

      <text x="0" y="125" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Store 4-Wall EBITDA:</text>
      <text x="240" y="125" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">$197,840 (26.7% Net Cash)</text>
    </g>

    <!-- Quadrant 2: Core KPI Scorecard -->
    <rect x="520" y="0" width="480" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="520" y="0" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="535" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">SECTION 2: OPERATIONAL KPI VARIANCES</text>

    <g transform="translate(535, 45)">
      <text x="0" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Total Door Traffic:</text>
      <text x="240" y="20" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">4,120 Swings (+4.2% YoY)</text>

      <text x="0" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Store Conversion Rate:</text>
      <text x="240" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">15.8% (Target: 14.5%)</text>

      <text x="0" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Average Ticket (ATV):</text>
      <text x="240" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">$3,420 (Plan: $3,250)</text>

      <text x="0" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Units Per Transaction (UPT):</text>
      <text x="240" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">1.28 (Target: 1.35 — Alert)</text>

      <text x="0" y="125" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Annualized Inventory Turn:</text>
      <text x="240" y="125" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">1.45× (Healthy Benchmark)</text>
    </g>

    <!-- Quadrant 3: Win / Loss Analysis -->
    <rect x="0" y="250" width="480" height="230" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="0" y="250" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="272" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">SECTION 3: WIN / LOSS QUALITATIVE ANALYSIS</text>

    <g transform="translate(15, 295)">
      <text x="0" y="15" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Top Month Wins:</text>
      <text x="0" y="35" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Closed $48,000 custom 4.2ct Colombian emerald suite.</text>
      <text x="0" y="55" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• CRM anniversary campaign generated $112,000 in repeat sales.</text>

      <text x="0" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Primary Misses &amp; Bottlenecks:</text>
      <text x="0" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Lost two 3.0ct diamond sales to competitor due to memo delay.</text>
      <text x="0" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• UPT dropped to 1.28 due to rush during weekend peak hours.</text>
    </g>

    <!-- Quadrant 4: Corrective Strategic Action Plan -->
    <rect x="520" y="250" width="480" height="230" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="520" y="250" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="535" y="272" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">SECTION 4: CORRECTIVE ACTION PLAN (NEXT 30 DAYS)</text>

    <g transform="translate(535, 295)">
      <text x="0" y="15" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Action 1: Memo Partner Pre-Approval</text>
      <text x="0" y="35" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Establish 24-hour express loose diamond overnight memo pipeline.</text>

      <text x="0" y="65" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Action 2: UPT Multi-Item Staging</text>
      <text x="0" y="85" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Pre-set companion diamond earrings on every bridal presentation tray.</text>

      <text x="0" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Action 3: Peak Floor Coverage Rebalancing</text>
      <text x="0" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Shift 1 associate from Tuesday morning to Saturday 1–5 PM peak rush.</text>
    </g>
  </g>

  <!-- Bottom Executive Footer -->
  <g transform="translate(50, 500)">
    <rect x="0" y="0" width="1000" height="130" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">EXECUTIVE PRESENTATION STANDARD:</text>
    <text x="20" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">A high-performing store review balances quantitative P&amp;L rigor with honest qualitative floor diagnosis and clear accountability owners for each corrective action.</text>
  </g>
</svg>"""
write_svg("courses/C12-retail-kpis-reporting/assets/c12-m08-one-page-store-performance-review.svg", c12_m08)

print("C12 SVG assets generated successfully!")
