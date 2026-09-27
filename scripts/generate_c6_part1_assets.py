import os

def write_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath}")

# C6 M01: Modern Bridal Buyer Journey Map
c6_m01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The Modern Bridal Path-to-Purchase: Psychology &amp; Decision Stages</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Navigating solo vs. couple dynamics, digital research overload, and proposal milestone anxiety</text>

  <!-- 4-Phase Journey Map -->
  <g transform="translate(50, 100)">
    <!-- Phase 1 -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">PHASE 1: Digital Discovery</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Buyer Mindset:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 3–6 months pre-purchase</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Browses Instagram, TikTok, Pinterest</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Confused by 4Cs specs &amp; pricing</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Core Emotional Driver:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Fear of overpaying or choosing the wrong style</text>

    <rect x="10" y="220" width="215" height="125" rx="6" fill="#0F172A"/>
    <text x="15" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Advisor Floor Strategy:</text>
    <text x="15" y="270" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Publish educational video content</text>
    <text x="15" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Offer transparent online scheduling</text>
    <text x="15" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Provide low-pressure digital guides</text>

    <!-- Phase 2 -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">PHASE 2: The Joint Exploration</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Buyer Mindset:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 78% of couples shop together first</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Partner tries on shapes (Oval, Pear)</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pinpoints finger size &amp; metal tone</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Core Emotional Driver:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Excitement of shared milestone commitment</text>

    <rect x="265" y="220" width="215" height="125" rx="6" fill="#0F172A"/>
    <text x="270" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Advisor Floor Strategy:</text>
    <text x="270" y="270" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Build private wishlist profile</text>
    <text x="270" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Focus on how it feels on her hand</text>
    <text x="270" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Record exact finger size &amp; favorite 2</text>

    <!-- Phase 3 -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">PHASE 3: Solo Return &amp; Budget</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Buyer Mindset:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Purchaser returns alone</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Focuses on final stone selection</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Budget balancing (Carat vs Quality)</text>

    <text x="525" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Core Emotional Driver:</text>
    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Desire to be the hero &amp; deliver perfection</text>

    <rect x="520" y="220" width="215" height="125" rx="6" fill="#0F172A"/>
    <text x="525" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Advisor Floor Strategy:</text>
    <text x="525" y="270" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Pull her exact wishlist notes</text>
    <text x="525" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Re-engineer 4Cs to hit target price</text>
    <text x="525" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Offer 0% financing for diamond upgrade</text>

    <!-- Phase 4 -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">PHASE 4: Proposal Execution</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Buyer Mindset:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High logistical tension</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Hiding ring box, travel security</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Proposal timing countdown</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Core Emotional Driver:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Anxiety about surprise secrecy &amp; logistics</text>

    <rect x="775" y="220" width="215" height="125" rx="6" fill="#0F172A"/>
    <text x="780" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Advisor Floor Strategy:</text>
    <text x="780" y="270" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Provide slim flat pocket ring box</text>
    <text x="780" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Complete insurance appraisal binder</text>
    <text x="780" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">• Reassure with free post-proposal sizing</text>
  </g>

  <!-- Bottom Core Insight Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE CRITICAL BRIDAL SELLING PRINCIPLE:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">The modern engagement ring purchase is rarely a single transaction — it is a high-trust, multi-visit relationship.</text>
    <text x="20" y="80" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• When both partners are present: <strong fill="#10B981">Never talk price or discount numbers in front of the recipient</strong> — focus entirely on aesthetics and emotion.</text>
    <text x="20" y="102" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">• When the buyer returns alone: <strong fill="#F59E0B">Execute precision commercial closure</strong> with the exact specs and reassurance they need.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m01-bridal-buyer-journey-map.svg", c6_m01)

# C6 M02: Diamond Shape vs Cut Architectures
c6_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Diamond Shape vs. Cut: Facet Architecture &amp; Light Performance</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Demystifying geometric silhouettes vs. optical cutting quality across the 3 core facet families</text>

  <!-- 3 Facet Categories -->
  <g transform="translate(50, 100)">
    <!-- Family 1: Brilliant Cuts -->
    <rect x="0" y="0" width="315" height="420" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. BRILLIANT CUT FAMILY</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Facet Geometry:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Triangular &amp; kite-shaped facets</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Radiates from center to girdle</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Maximizes scintillation &amp; fire</text>

    <!-- Visual Shapes -->
    <g transform="translate(20, 140)">
      <!-- Round -->
      <circle cx="35" cy="35" r="25" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="35" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Round (57/58f)</text>

      <!-- Oval -->
      <ellipse cx="115" cy="35" rx="18" ry="25" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="115" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Oval</text>

      <!-- Pear -->
      <path d="M 195 10 C 210 30, 215 50, 195 60 C 175 50, 180 30, 195 10 Z" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="195" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Pear / Drop</text>

      <!-- Marquise -->
      <path d="M 270 10 C 290 35, 290 35, 270 60 C 250 35, 250 35, 270 10 Z" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="270" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Marquise</text>
    </g>

    <text x="15" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Light Performance Characteristics:</text>
    <text x="15" y="270" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Highest brilliance and sparkle</text>
    <text x="15" y="290" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Superior inclusion masking (hides SI1)</text>
    <text x="15" y="310" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Oval/Pear elongate finger silhouette</text>

    <rect x="10" y="335" width="295" height="70" rx="6" fill="#0F172A"/>
    <text x="15" y="355" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Optical Warning:</text>
    <text x="15" y="375" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Elongated shapes (Oval/Marquise/Pear)</text>
    <text x="15" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">exhibit varying degrees of "Bow-Tie" shadow.</text>

    <!-- Family 2: Step Cuts -->
    <rect x="340" y="0" width="315" height="420" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="340" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="355" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. STEP CUT FAMILY</text>
    
    <text x="355" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Facet Geometry:</text>
    <text x="355" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Rectilinear, parallel step facets</text>
    <text x="355" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Concentric "hall-of-mirrors" effect</text>
    <text x="355" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Elegant, architectural vintage clean lines</text>

    <!-- Visual Shapes -->
    <g transform="translate(360, 140)">
      <!-- Emerald -->
      <polygon points="20,10 60,10 70,20 70,50 60,60 20,60 10,50 10,20" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
      <text x="40" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Emerald Cut</text>

      <!-- Asscher -->
      <polygon points="130,10 160,10 170,20 170,50 160,60 130,60 120,50 120,20" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
      <text x="145" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Asscher (Square)</text>

      <!-- Baguette -->
      <rect x="220" y="15" width="45" height="40" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
      <text x="242" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Baguette</text>
    </g>

    <text x="355" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Clarity &amp; Color Exposure:</text>
    <text x="355" y="270" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Wide open table acts as a clear window</text>
    <text x="355" y="290" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Cannot hide inclusions (VS2+ recommended)</text>
    <text x="355" y="310" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Highlights pure crystal transparency</text>

    <rect x="350" y="335" width="295" height="70" rx="6" fill="#0F172A"/>
    <text x="355" y="355" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Counter Rule:</text>
    <text x="355" y="375" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Step cuts require higher clarity (VS1/VS2)</text>
    <text x="355" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and higher color (D–G) due to open facets.</text>

    <!-- Family 3: Mixed / Modified -->
    <rect x="680" y="0" width="320" height="420" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="0" width="320" height="36" rx="8" fill="#1E293B"/>
    <text x="695" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. MIXED &amp; MODIFIED CUTS</text>
    
    <text x="695" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Facet Geometry:</text>
    <text x="695" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Combines step outline with brilliant faceting</text>
    <text x="695" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Hybrid optical performance</text>
    <text x="695" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Modern maximum sparkle in geometric outlines</text>

    <!-- Visual Shapes -->
    <g transform="translate(700, 140)">
      <!-- Cushion -->
      <rect x="15" y="10" width="50" height="50" rx="12" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="40" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Cushion (Pillow)</text>

      <!-- Radiant -->
      <polygon points="120,10 160,10 170,20 170,50 160,60 120,60 110,50 110,20" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="140" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Radiant Cut (70f)</text>

      <!-- Princess -->
      <rect x="220" y="10" width="50" height="50" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="245" y="75" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1" text-anchor="middle">Princess (Square)</text>
    </g>

    <text x="695" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Best of Both Worlds:</text>
    <text x="695" y="270" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Radiant: Cut-corner emerald shape + brilliance</text>
    <text x="695" y="290" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Cushion: Antique romantic softness + intense fire</text>
    <text x="695" y="310" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Princess: Sharp 90° modern architectural corners</text>

    <rect x="690" y="335" width="300" height="70" rx="6" fill="#0F172A"/>
    <text x="695" y="355" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Setting Warning:</text>
    <text x="695" y="375" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Princess corners are vulnerable to chipping;</text>
    <text x="695" y="390" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">must be protected by V-prong or bezel corners.</text>
  </g>

  <!-- Summary Rule Banner -->
  <g transform="translate(50, 540)">
    <rect x="0" y="0" width="1000" height="95" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">THE CRITICAL DISTINCTION TO TEACH THE CLIENT:</text>
    <text x="20" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F3F4F6">"Shape" is the exterior outline silhouette (e.g. Oval, Pear, Emerald) chosen for aesthetic taste.</text>
    <text x="20" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">"Cut" is the mathematical precision, symmetry, and Polish of the facets that unlocks optical light performance and fire.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m02-diamond-shapes-and-facet-architectures.svg", c6_m02)

# C6 M03: Bridal Lab Selection Matrix
c6_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Bridal Grading Lab Guide: GIA vs. AGSL vs. IGI vs. GCAL</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Navigating laboratory grading strictness, market liquidity, and trade confidence in bridal retail</text>

  <!-- Lab Comparison Grid -->
  <g transform="translate(50, 100)">
    <!-- GIA -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">GIA (Gemological Institute)</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Market Role:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Global benchmark standard</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Creator of the 4Cs system</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Highest resale value retention</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Grading Strictness:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Ultra-Conservative (Color/Clarity)</text>

    <text x="15" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Primary Application:</text>
    <text x="15" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Natural Diamonds &amp; High-Ticket</text>

    <rect x="10" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Floor Positioning:</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"GIA is the gold standard that</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">every other lab is judged against."</text>

    <!-- AGS / AGSL -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">AGS (American Gem Society)</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Market Role:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pioneer in 3D Cut Ray Tracing</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• "Triple Zero" (0-0-0) standard</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Integrated into GIA in 2022</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Grading Strictness:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Most Rigorous Cut Grade (ASET)</text>

    <text x="270" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Primary Application:</text>
    <text x="270" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Super-Ideal Natural Diamonds</text>

    <rect x="265" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="270" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Floor Positioning:</text>
    <text x="270" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"AGS 000 certifies peak optical</text>
    <text x="270" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">performance and ray-traced fire."</text>

    <!-- IGI -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">IGI (International Gem)</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Market Role:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Dominant leader in Lab-Grown</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High-speed turnaround</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Broad global retail presence</text>

    <text x="525" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Grading Strictness:</text>
    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Moderate (Can be 1/2 grade softer)</text>

    <text x="525" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Primary Application:</text>
    <text x="525" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Lab-Grown Diamonds &amp; Commercial</text>

    <rect x="520" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="525" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Floor Positioning:</text>
    <text x="525" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"IGI is the international volume</text>
    <text x="525" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">leader for certified lab-grown gems."</text>

    <!-- GCAL -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">GCAL (Gem Certification)</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Market Role:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 8X Ultimate Cut Grade standard</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Zero-tolerance optical analysis</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Guaranteed grading warranty</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Grading Strictness:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Ultra-Strict Precision 8X Cut</text>

    <text x="780" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Primary Application:</text>
    <text x="780" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Premium Natural &amp; 8X Lab-Grown</text>

    <rect x="775" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="780" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Floor Positioning:</text>
    <text x="780" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"GCAL 8X provides guaranteed</text>
    <text x="780" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">microscopic optical perfection."</text>
  </g>

  <!-- Bottom Guidance Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">HOW TO DISCUSS LAB DIFFERENCES WITHOUT TRASHING OTHER CERTIFICATES:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Never tell a client that a competing lab's report is "fake" or "worthless".</text>
    <text x="20" y="80" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Explain that each laboratory operates with its own specific calibration criteria: <strong fill="#10B981">GIA</strong> is the conservative universal pricing baseline; <strong fill="#38BDF8">AGS &amp; GCAL</strong> specialize in optical ray tracing; and <strong fill="#F59E0B">IGI</strong> is the global benchmark for lab-grown diamond evaluation.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m03-bridal-lab-selection-matrix.svg", c6_m03)

# C6 M04: Bridal Stone Origin Advisor
c6_m04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Ethical Bridal Stone Advisory: Natural vs. Lab-Grown vs. Simulant</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Guiding engagement ring clients with unbiased facts, value retention transparency, and emotional respect</text>

  <!-- 3-Way Comparative Pillars -->
  <g transform="translate(50, 100)">
    <!-- Pillar 1: Natural -->
    <rect x="0" y="0" width="315" height="370" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">NATURAL DIAMOND</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Origin &amp; Geological Story:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Formed 1–3 billion years ago deep in Earth</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Finite global supply; natural rarity</text>

    <text x="15" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Value &amp; Price Profile:</text>
    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Higher initial investment ($5,000–$50,000+)</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Historical market liquidity &amp; heirloom value</text>

    <text x="15" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Client Archetype Fit:</text>
    <text x="15" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Values ancient geological rarity, tradition,</text>
    <text x="15" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">and multi-generational heirloom symbolism.</text>

    <rect x="10" y="275" width="295" height="80" rx="6" fill="#0F172A"/>
    <text x="15" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Floor Presentation Script:</text>
    <text x="15" y="320" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"A natural diamond is an ancient miracle of Earth</text>
    <text x="15" y="338" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">that took billions of years to reach her hand."</text>

    <!-- Pillar 2: Lab-Grown -->
    <rect x="340" y="0" width="315" height="370" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="340" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="355" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">LABORATORY-GROWN DIAMOND</text>
    
    <text x="355" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Origin &amp; Technological Story:</text>
    <text x="355" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Grown in reactor via HPHT or CVD in weeks</text>
    <text x="355" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 100% identical physical, optical, chemical</text>

    <text x="355" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Value &amp; Price Profile:</text>
    <text x="355" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 70–90% lower price per carat</text>
    <text x="355" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Depreciating market replacement cost</text>

    <text x="355" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Client Archetype Fit:</text>
    <text x="355" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Wants maximum carat size (2.5ct–4ct+) and</text>
    <text x="355" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">flawless clarity within an accessible budget.</text>

    <rect x="350" y="275" width="295" height="80" rx="6" fill="#0F172A"/>
    <text x="355" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Floor Presentation Script:</text>
    <text x="355" y="320" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"It gives you the exact sparkle of diamond</text>
    <text x="355" y="338" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">physics while maximizing finger coverage today."</text>

    <!-- Pillar 3: Simulants -->
    <rect x="680" y="0" width="320" height="370" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="0" width="320" height="36" rx="8" fill="#1E293B"/>
    <text x="695" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">DIAMOND SIMULANTS (Moissanite/CZ)</text>
    
    <text x="695" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Origin &amp; Material Composition:</text>
    <text x="695" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Moissanite: Silicon Carbide (SiC)</text>
    <text x="695" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Cubic Zirconia: Zirconium Dioxide (ZrO2)</text>

    <text x="695" y="135" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Value &amp; Price Profile:</text>
    <text x="695" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Nominal cost ($50 – $800)</text>
    <text x="695" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Double refraction / disco-ball rainbow fire</text>

    <text x="695" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Client Archetype Fit:</text>
    <text x="695" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Temporary travel ring or temporary placeholder</text>
    <text x="695" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">prior to purchasing a permanent heirloom.</text>

    <rect x="690" y="275" width="300" height="80" rx="6" fill="#0F172A"/>
    <text x="695" y="298" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Floor Presentation Script:</text>
    <text x="695" y="320" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"A distinct gemstone material that mimics diamond</text>
    <text x="695" y="338" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">appearance at an entry travel price point."</text>
  </g>

  <!-- Advisory Code Banner -->
  <g transform="translate(50, 490)">
    <rect x="0" y="0" width="1000" height="140" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">THE GOLDEN RULE OF ETHICAL BRIDAL ADVISING:</text>
    <text x="20" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F3F4F6">Never judge, shame, or push a client toward one origin based on your commission preference.</text>
    <text x="20" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Be 100% transparent about physical facts, origin, and secondary market value dynamics. When clients feel fully informed without pressure, they trust your guidance for life.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m04-bridal-stone-origin-advisor.svg", c6_m04)

# C6 M05: Bridal Settings & Metals Guide
c6_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Bridal Settings &amp; Precious Metals: Durability &amp; Style Architecture</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Analyzing setting styles, security mechanics, and precious metal wear characteristics for lifetime bridal wear</text>

  <!-- 4 Setting Types Top Row -->
  <g transform="translate(50, 100)">
    <!-- Setting 1: Solitaire Prong -->
    <rect x="0" y="0" width="235" height="230" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="15" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">4 vs. 6-Prong Solitaire</text>
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 4-Prong: Maximizes light entry &amp;</text>
    <text x="15" y="78" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  shows more diamond surface</text>
    <text x="15" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 6-Prong: Superior stone security;</text>
    <text x="15" y="123" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  protects girdle if one prong snags</text>
    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Wear Profile: Daily care required;</text>
    <text x="15" y="173" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">prongs require check every 6 mos.</text>
    <text x="15" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Security: Moderate to High</text>

    <!-- Setting 2: Bezel -->
    <rect x="255" y="0" width="235" height="230" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <text x="270" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">Bezel &amp; Half-Bezel</text>
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Full metal rim encases the girdle</text>
    <text x="270" y="78" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Zero prongs to snag on knitwear</text>
    <text x="270" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Flush, sleek modern aesthetic</text>
    <text x="270" y="123" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Makes diamond appear 10% larger</text>
    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Wear Profile: Best for medical,</text>
    <text x="270" y="173" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">fitness, active lifestyle wearers.</text>
    <text x="270" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Security: Highest / Maximum</text>

    <!-- Setting 3: Halo -->
    <rect x="510" y="0" width="235" height="230" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="525" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">Halo &amp; Hidden Halo</text>
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Halo: Micro-pavé perimeter frame</text>
    <text x="525" y="78" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  adds +0.50ct equivalent visual scale</text>
    <text x="525" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Hidden Halo: Subtle gallery pavé</text>
    <text x="525" y="123" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  visible from side profile view</text>
    <text x="525" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Wear Profile: Multiple micro-prongs</text>
    <text x="525" y="173" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">require ultrasonic inspection care.</text>
    <text x="525" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Security: Moderate (Pavé care)</text>

    <!-- Setting 4: Pavé & Cathedral -->
    <rect x="765" y="0" width="235" height="230" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <text x="780" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EC4899">Cathedral &amp; Pavé Shank</text>
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Cathedral arches slope upward</text>
    <text x="780" y="78" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  to protect center head from torque</text>
    <text x="780" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Pavé shank: Hand-beaded diamonds</text>
    <text x="780" y="123" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  running 1/2 or 3/4 around band</text>
    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Wear Profile: French cut / U-cut pavé</text>
    <text x="780" y="173" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">delivers 360° sparkle.</text>
    <text x="780" y="205" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Structural Rigidity: High</text>
  </g>

  <!-- Metals Hierarchy Comparison Bottom -->
  <g transform="translate(50, 350)">
    <rect x="0" y="0" width="1000" height="280" rx="8" fill="#161B22" stroke="#334155"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#F3F4F6">PRECIOUS METALS COMPARATIVE MATRIX: BRIDAL WEARABILITY</text>

    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="960" height="30" fill="#1E293B"/>
      <text x="15" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">ALLOY / METAL</text>
      <text x="200" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">PURITY &amp; HARDNESS</text>
      <text x="420" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">MAINTENANCE &amp; WEAR PATTERN</text>
      <text x="720" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">FLOOR ADVICE</text>

      <!-- Platinum -->
      <rect x="0" y="32" width="960" height="42" fill="#0F172A"/>
      <text x="15" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">Platinum (PT950)</text>
      <text x="200" y="58" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">95% Pure • Dense &amp; Malleable</text>
      <text x="420" y="58" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Displaces metal (no loss); develops matte patina</text>
      <text x="720" y="58" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#38BDF8">Hypoallergenic; lifetime prong durability</text>

      <!-- 18K Yellow Gold -->
      <rect x="0" y="76" width="960" height="42" fill="#161B22"/>
      <text x="15" y="102" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">18K Yellow Gold</text>
      <text x="200" y="102" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">75.0% Gold (750) • Rich hue</text>
      <text x="420" y="102" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Never tarnishes; warm butter tone; softer wear</text>
      <text x="720" y="102" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#F59E0B">Trending #1 bridal luxury metal resurgence</text>

      <!-- 14K White Gold -->
      <rect x="0" y="120" width="960" height="42" fill="#0F172A"/>
      <text x="15" y="146" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">14K White Gold</text>
      <text x="200" y="146" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">58.3% Gold (585) • Hard alloy</text>
      <text x="420" y="146" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Requires rhodium re-plating every 12–18 months</text>
      <text x="720" y="146" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Affordable bright white; check nickel allergies</text>

      <!-- 14K Rose Gold -->
      <rect x="0" y="164" width="960" height="42" fill="#161B22"/>
      <text x="15" y="190" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EC4899">14K Rose Gold</text>
      <text x="200" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">58.3% Gold + Copper alloy</text>
      <text x="420" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Highly durable; warm pink blush; no plating</text>
      <text x="720" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#EC4899">Romantic vintage look; flatters olive/warm skin</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m05-bridal-settings-and-metals-guide.svg", c6_m05)

# C6 M06: Ring Sizing & Fit Mechanics
c6_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Ring Sizing, Fit &amp; Comfort: Getting It Right the First Time</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Knuckle anatomy, seasonal biological fluctuations, comfort-fit dome profiles, and spin remedies</text>

  <!-- Left: Sizing Mechanics & Knuckle Types -->
  <g transform="translate(50, 100)">
    <rect x="0" y="0" width="480" height="380" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="480" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">ANATOMY OF RING FIT &amp; KNUCKLE VARIATIONS</text>

    <!-- Case A: Conical Finger -->
    <rect x="15" y="50" width="450" height="95" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="30" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">A. Conical Finger (Base larger than knuckle)</text>
    <text x="30" y="98" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Finger tapers outward toward hand base</text>
    <text x="30" y="118" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Risk: Ring can slide off easily when hands are cold or wet</text>
    <text x="30" y="136" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Fitting Rule: Snug fit at base; should require a gentle twist to remove</text>

    <!-- Case B: Prominent Knuckle -->
    <rect x="15" y="155" width="450" height="105" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="30" y="180" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">B. Prominent Knuckle (Knuckle wider than base)</text>
    <text x="30" y="203" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Sized to clear knuckle, then spins loosely at the base</text>
    <text x="30" y="223" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Heavy center diamond causes top-heavy flop</text>
    <text x="30" y="245" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Fitting Remedies: Sizing beads, horseshoe spring, or Euro-shank</text>

    <!-- Case C: Band Width Adjustment -->
    <rect x="15" y="270" width="450" height="95" rx="6" fill="#0F172A" stroke="#334155"/>
    <text x="30" y="295" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">C. Shank Width Compensation</text>
    <text x="30" y="318" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Narrow shank (1.5mm–2mm): Fits true to size</text>
    <text x="30" y="338" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Wide band (6mm+ or stacked set): <strong fill="#10B981">Must size up 1/4 to 1/2 size</strong></text>
  </g>

  <!-- Right: Comfort Fit vs Standard + Environmental -->
  <g transform="translate(560, 100)">
    <rect x="0" y="0" width="490" height="380" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="0" y="0" width="490" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">STANDARD FIT vs. COMFORT FIT PROFILE</text>

    <!-- Cross Section Comparison -->
    <g transform="translate(20, 50)">
      <!-- Standard -->
      <rect x="0" y="0" width="215" height="150" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#CBD5E1">Standard Flat Fit</text>
      <!-- Diagram -->
      <rect x="30" y="45" width="150" height="20" rx="2" fill="#334155" stroke="#94A3B8"/>
      <text x="15" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Flat interior surface</text>
      <text x="15" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Edges create skin friction</text>
      <text x="15" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">Feels tighter over knuckle</text>

      <!-- Comfort Fit -->
      <rect x="235" y="0" width="215" height="150" rx="6" fill="#0F172A" stroke="#10B981"/>
      <text x="250" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">Comfort Fit (Domed)</text>
      <!-- Diagram -->
      <path d="M 265 45 Q 340 55, 415 45 L 415 65 Q 340 65, 265 65 Z" fill="#064E3B" stroke="#10B981"/>
      <text x="250" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">• Convex rounded interior</text>
      <text x="250" y="110" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">• Glides smoothly over knuckle</text>
      <text x="250" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Standard for men's bands</text>
    </g>

    <!-- Seasonal & Biological Fluctuations -->
    <g transform="translate(20, 220)">
      <rect x="0" y="0" width="450" height="140" rx="6" fill="#0F172A"/>
      <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">BIOLOGICAL SIZING VARIABLES TO EXPLAIN:</text>
      <text x="15" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• <strong fill="#F3F4F6">Temperature:</strong> Fingers expand up to 1/2 size in hot summer / humidity</text>
      <text x="15" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• <strong fill="#F3F4F6">Time of Day:</strong> Hands are smallest in morning; largest in late afternoon</text>
      <text x="15" y="90" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• <strong fill="#F3F4F6">Dominant Hand:</strong> Dominant hand ring finger is almost always 1/4–1/2 size larger</text>
      <text x="15" y="115" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Advise client to measure at room temperature during midday</text>
    </g>
  </g>

  <!-- Bottom Best Practice Banner -->
  <g transform="translate(50, 500)">
    <rect x="0" y="0" width="1000" height="130" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">SECRECY SIZING HACKS FOR SURPRISE PROPOSALS:</text>
    <text x="20" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">1. <strong fill="#10B981">Borrow an Existing Ring:</strong> Ensure it is worn on the left ring finger (not middle or right hand).</text>
    <text x="20" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">2. <strong fill="#38BDF8">The Soap/Candle Impression:</strong> Press her ring into a bar of soap, or trace inside circumference on paper.</text>
    <text x="20" y="95" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F59E0B">3. <strong fill="#F59E0B">The Best Friend / Sister Ally:</strong> Have her try on a friend's engagement ring casually during lunch.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m06-ring-sizing-and-fit-mechanics.svg", c6_m06)

# C6 M07: Bridal Custom CAD Milestones
c6_m07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Custom Bridal Design Pipeline: 5 Milestone Approval Gates</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">From client Pinterest mood board to finished bespoke bridal heirloom with zero expectation mismatches</text>

  <!-- 5 Stage Flow Pipeline -->
  <g transform="translate(50, 100)">
    <!-- Gate 1 -->
    <rect x="0" y="0" width="185" height="340" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="92" cy="35" r="18" fill="#38BDF8"/>
    <text x="92" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">1</text>
    <text x="92" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Concept &amp; Deposit</text>
    <text x="15" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Mood board review</text>
    <text x="15" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Select center stone</text>
    <text x="15" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Hand sketch sign-off</text>
    <text x="15" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 50% Custom Deposit</text>
    
    <rect x="10" y="240" width="165" height="85" rx="6" fill="#0F172A"/>
    <text x="15" y="265" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Gate 1 Approval:</text>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Written design brief</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">&amp; center diamond locked</text>

    <!-- Gate 2 -->
    <rect x="205" y="0" width="185" height="340" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="297" cy="35" r="18" fill="#10B981"/>
    <text x="297" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">2</text>
    <text x="297" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">3D CAD Renders</text>
    <text x="220" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 3D digital model built</text>
    <text x="220" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 4-angle photorealistic</text>
    <text x="220" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  360° video renders</text>
    <text x="220" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Max 2 revision rounds</text>
    
    <rect x="215" y="240" width="165" height="85" rx="6" fill="#0F172A"/>
    <text x="220" y="265" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Gate 2 Approval:</text>
    <text x="220" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">CAD proportion &amp; head</text>
    <text x="220" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">height signed by client</text>

    <!-- Gate 3 -->
    <rect x="410" y="0" width="185" height="340" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="502" cy="35" r="18" fill="#F59E0B"/>
    <text x="502" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">3</text>
    <text x="502" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Wax/Resin Try-On</text>
    <text x="425" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 3D printed physical wax</text>
    <text x="425" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• In-store finger try-on</text>
    <text x="425" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Client checks scale,</text>
    <text x="425" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  profile height &amp; fit</text>
    
    <rect x="420" y="240" width="165" height="85" rx="6" fill="#0F172A"/>
    <text x="425" y="265" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Gate 3 Approval:</text>
    <text x="425" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Physical wax approved</text>
    <text x="425" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">before casting metal</text>

    <!-- Gate 4 -->
    <rect x="615" y="0" width="185" height="340" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <circle cx="707" cy="35" r="18" fill="#EC4899"/>
    <text x="707" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">4</text>
    <text x="707" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Casting &amp; Setting</text>
    <text x="630" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Lost-wax casting</text>
    <text x="630" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Master bench clean-up</text>
    <text x="630" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Microscope diamond setting</text>
    <text x="630" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Hand polish &amp; hallmark</text>
    
    <rect x="625" y="240" width="165" height="85" rx="6" fill="#0F172A"/>
    <text x="630" y="265" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Bench Quality:</text>
    <text x="630" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">10-point internal QC</text>
    <text x="630" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">prong tightness check</text>

    <!-- Gate 5 -->
    <rect x="820" y="0" width="180" height="340" rx="8" fill="#161B22" stroke="#A855F7" stroke-width="1.5"/>
    <circle cx="910" cy="35" r="18" fill="#A855F7"/>
    <text x="910" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">5</text>
    <text x="910" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Final Unveiling</text>
    <text x="835" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Champagne reveal</text>
    <text x="835" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Appraisal &amp; GIA binder</text>
    <text x="835" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Balance payment</text>
    <text x="835" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Lifetime warranty hand-off</text>
    
    <rect x="830" y="240" width="160" height="85" rx="6" fill="#0F172A"/>
    <text x="835" y="265" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#A855F7">Final Milestone:</text>
    <text x="835" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Total client delight &amp;</text>
    <text x="835" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">referral foundation</text>
  </g>

  <!-- Timeline & Turnaround Summary -->
  <g transform="translate(50, 470)">
    <rect x="0" y="0" width="1000" height="160" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">STANDARD BRIDAL CUSTOM TIMELINE: 3 TO 5 WEEKS TOTAL</text>
    <text x="20" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• <strong fill="#38BDF8">CAD Modeling &amp; Rendering:</strong> 3–5 Business Days</text>
    <text x="20" y="82" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#10B981">• <strong fill="#10B981">Wax Printing &amp; Client Try-On:</strong> 2–4 Business Days</text>
    <text x="20" y="104" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F59E0B">• <strong fill="#F59E0B">Casting, Bench Assembly, Setting &amp; QC:</strong> 8–12 Business Days</text>
    <text x="20" y="128" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">⚠️ Always buffer 5 extra days during peak holiday/Valentine's rush.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m07-bridal-custom-cad-milestones.svg", c6_m07)

print("C6 Part 1 SVG assets generated successfully!")
