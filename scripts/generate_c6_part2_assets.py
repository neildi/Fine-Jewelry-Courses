import os

def write_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath}")

# C6 M08: Proposal Logistics Timeline
c6_m08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Proposal Logistics &amp; Stealth Protocol: The Complete Checklist</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Helping the proposer orchestrate a flawless, stress-free surprise engagement milestone</text>

  <!-- 4 Tactical Pillars Grid -->
  <g transform="translate(50, 100)">
    <!-- Pillar 1: Packaging & Secrecy -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. STEALTH PACKAGING</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">The Box Bulge Problem:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Standard luxury boxes are 2.5"</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  cubes that bulge in suit pants</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Ruins surprise during dinner</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">The Solution:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Supply slim 0.75" flat leather</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  pocket proposal box</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Retain master box for home</text>

    <rect x="10" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Floor Rule:</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Give every bridal client both</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">presentation and stealth boxes.</text>

    <!-- Pillar 2: Airport & Travel -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. AIRPORT TRAVEL SECURITY</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">TSA Screening Tactics:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• NEVER put in checked luggage</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Keep in carry-on bag zippered</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  interior pocket (never on body)</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Stealth TSA Note:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Attach discreet printed tag:</text>
    <text x="270" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">  "ENGAGEMENT RING INSIDE.</text>
    <text x="270" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">  PLEASE BE DISCREET."</text>

    <rect x="265" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="270" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Hotel Security:</text>
    <text x="270" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Place in room safe immediately</text>
    <text x="270" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">upon destination arrival.</text>

    <!-- Pillar 3: Insurance Coverage -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. DAY-ZERO INSURANCE</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">The Uninsured Gap Trap:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Many proposers wait until AFTER</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  proposal to insure the ring</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Beach / cliff proposals have</text>
    <text x="525" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  the highest loss risk</text>

    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">The Protocol:</text>
    <text x="525" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Issue appraisal at pickup</text>
    <text x="525" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Guide client to bind policy</text>
    <text x="525" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  BEFORE leaving the store</text>

    <rect x="520" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="525" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Jewelers Mutual / Rider:</text>
    <text x="525" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Ensure coverage covers worldwide</text>
    <text x="525" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">loss, theft, and accidental drop.</text>

    <!-- Pillar 4: Post-Proposal Care -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. POST-PROPOSAL VISIT</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">The Second Reception:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Complimentary post-proposal</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  exact finger re-sizing</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Champagne toast with fiancée</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Wedding Band Bridge:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Introduce wedding bands</text>
    <text x="780" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  during the re-sizing visit</text>
    <text x="780" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Show flush-fit matching bands</text>

    <rect x="775" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="780" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Client Lock-In:</text>
    <text x="780" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Converts proposer into permanent</text>
    <text x="780" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">couple client relationship.</text>
  </g>

  <!-- Summary Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">WHY PROPOSAL LOGISTICS ADVICE BUILDS LIFELONG LOYALTY:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">When you proactively address the proposer's hidden fears — box bulk in a pocket, airport security surprises, and insurance coverage — you transition from a commodity jeweler to an indispensable trusted advisor.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m08-proposal-logistics-timeline.svg", c6_m08)

# C6 M09: Wedding Band Pairing Matrix
c6_m09 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Wedding Band &amp; Stacking Architecture: Pairing &amp; Metal Compatibility</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Mastering flush-fit profiles, curved contours, chevron jackets, and metal galvanic hardness wear</text>

  <!-- 3 Band Fit Categories Top -->
  <g transform="translate(50, 100)">
    <!-- Flush Fit -->
    <rect x="0" y="0" width="315" height="340" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. STRAIGHT FLUSH FIT</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Head Architecture:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High-set or peg head gallery</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Center stone sits elevated above shank</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Straight band slides completely flush</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Benefits &amp; Versatility:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Band looks stunning when worn alone</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Easy to add 2nd &amp; 3rd anniversary stacks</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Universal classic eternity band match</text>

    <rect x="10" y="250" width="295" height="75" rx="6" fill="#0F172A"/>
    <text x="15" y="275" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Style Recommendation:</text>
    <text x="15" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Best for round solitaires, oval peg heads,</text>
    <text x="15" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and cathedral high-basket mountings.</text>

    <!-- Contoured / Curved -->
    <rect x="340" y="0" width="315" height="340" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="340" y="0" width="315" height="36" rx="8" fill="#1E293B"/>
    <text x="355" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. CONTOURED / CURVED FIT</text>
    
    <text x="355" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Head Architecture:</text>
    <text x="355" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Low-set basket or wide halo</text>
    <text x="355" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Diamond sits flush on the finger</text>
    <text x="355" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Straight band creates an awkward gap</text>

    <text x="355" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Benefits &amp; Considerations:</text>
    <text x="355" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Hugs the exact contours of the ring</text>
    <text x="355" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Creates a unified, cohesive look</text>
    <text x="355" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• May look unbalanced if worn solo</text>

    <rect x="350" y="250" width="295" height="75" rx="6" fill="#0F172A"/>
    <text x="355" y="275" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Style Recommendation:</text>
    <text x="355" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Best for low-profile emerald cuts, halos,</text>
    <text x="355" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and large low-set elongated shapes.</text>

    <!-- Chevron / Jacket -->
    <rect x="680" y="0" width="320" height="340" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="0" width="320" height="36" rx="8" fill="#1E293B"/>
    <text x="695" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. CHEVRON &amp; NESTED JACKET</text>
    
    <text x="695" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Head Architecture:</text>
    <text x="695" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pointed tip (Pear, Marquise) or cluster</text>
    <text x="695" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• V-shape chevron cradles the point</text>
    <text x="695" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Tiara / Crown diamond accents</text>

    <text x="695" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Benefits &amp; Considerations:</text>
    <text x="695" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Dramatic, fashionable royal styling</text>
    <text x="695" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Protects exposed pear/marquise tips</text>
    <text x="695" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Can frame top and bottom as a jacket</text>

    <rect x="690" y="250" width="300" height="75" rx="6" fill="#0F172A"/>
    <text x="695" y="275" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Style Recommendation:</text>
    <text x="695" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Best for pear drops, marquise solitaires,</text>
    <text x="695" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and art-deco bohemian bridal stacks.</text>
  </g>

  <!-- Metal Hardness & Wear Warning Bottom -->
  <g transform="translate(50, 460)">
    <rect x="0" y="0" width="1000" height="170" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EF4444">CRITICAL BENCH RULE: METAL ALLOY COMPATIBILITY IN STACKING</text>
    
    <g transform="translate(20, 50)">
      <text x="0" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">1. <strong fill="#FCA5A5">Never Stack Platinum Against 14K Gold:</strong> Platinum is far denser and harder on contact. Over 2–3 years of daily friction, the platinum band will saw through the softer gold prongs and shank.</text>
      <text x="0" y="45" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">2. <strong fill="#6EE7B7">Match Karat Purity:</strong> Always pair 14K with 14K, 18K with 18K, and Platinum with Platinum to maintain equal wear friction.</text>
      <text x="0" y="70" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">3. <strong fill="#38BDF8">Soldering Consideration:</strong> If spinning causes prong rubbing, advise soldering the engagement ring and band together.</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m09-wedding-band-pairing-matrix.svg", c6_m09)

# C6 M10: Bridal Appraisal & Insurance Lifecycle
c6_m10 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Lifetime Bridal Protection: Appraisal, Insurance &amp; Aftercare</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Protecting client emotional and financial investment through comprehensive documentation and preventative maintenance</text>

  <!-- 4-Stage Lifetime Wheel -->
  <g transform="translate(50, 100)">
    <!-- Stage 1 -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. RETAIL APPRAISAL</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Point of Sale Delivery:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Retail Replacement Value (RRV)</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Full 4Cs specs, metal gram</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  weight, and maker marks</text>
    <text x="15" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• High-res macro photo included</text>

    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Appraisal Warning:</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Never hyper-inflate values</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  (forces client to pay excess</text>
    <text x="15" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  annual insurance premiums)</text>

    <rect x="10" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Update Cadence:</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Re-evaluate every 3–5 years</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">for precious metal shifts.</text>

    <!-- Stage 2 -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. SPECIALIZED INSURANCE</text>
    
    <text x="255" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Policy Comparison:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Homeowners Rider:</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  High deductibles; strict caps;</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  claim may increase home rates</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">• Standalone Jewelry Policy:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">  (Jewelers Mutual / BriteCo)</text>
    <text x="270" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">  $0 deductible; mysterious loss;</text>
    <text x="270" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#D1FAE5">  worldwide travel coverage</text>

    <rect x="265" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="270" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Client Cost:</text>
    <text x="270" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Approx 1% to 2% of appraised</text>
    <text x="270" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">value annually (~$100/$10k).</text>

    <!-- Stage 3 -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. 6-MONTH INSPECTIONS</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Preventative Maintenance:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 10x Loupe prong check</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Stone looseness tap test</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pavé bead wear analysis</text>
    <text x="525" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Ultrasonic &amp; steam cleaning</text>

    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Warranty Validation:</text>
    <text x="525" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Log inspection in CRM</text>
    <text x="525" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Extends store diamond loss</text>
    <text x="525" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  guarantee coverage</text>

    <rect x="520" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="525" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Client Touchpoint:</text>
    <text x="525" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Brings couple back into the</text>
    <text x="525" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">store twice every year.</text>

    <!-- Stage 4 -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. HOME CARE PROTOCOL</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Client Care Education:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• "Last On, First Off" rule</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Remove for gym/weights, pool,</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  gardening, &amp; household bleach</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Safe Home Cleaning:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Warm water + mild Dawn soap</text>
    <text x="780" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Baby soft toothbrush behind head</text>
    <text x="780" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Lint-free microfiber dry</text>

    <rect x="775" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="780" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Chlorine Warning:</text>
    <text x="780" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Chlorine leaches alloys from gold,</text>
    <text x="780" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">causing prongs to snap off.</text>
  </g>

  <!-- Summary Banner -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE LIFETIME VALUE (LTV) BRIDGE OF AFTERCARE:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">When you deliver a museum-grade appraisal binder and schedule the first complimentary 6-month spa check-in before the client leaves the store, you guarantee that this couple will return to you for their wedding bands, first anniversary, and every milestone celebration for decades to come.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m10-bridal-appraisal-insurance-lifecycle.svg", c6_m10)

# C6 M11: Demographic Bridal Personas
c6_m11 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Demographic Bridal Personas: 4 Core Buyer Archetypes</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Tailoring language, design presentation, and value framing across distinct generational customer segments</text>

  <!-- 4 Personas Grid -->
  <g transform="translate(50, 100)">
    <!-- Persona 1: The Traditionalist -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. THE TRADITIONALIST</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Profile &amp; Priorities:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Values classic timeless elegance</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Prefers Natural GIA diamonds</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Round brilliant or Cushion cut</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Metal &amp; Mounting:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Platinum or 18K Yellow Gold solitaire</text>

    <text x="15" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Effective Sales Angle:</text>
    <text x="15" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Focus on heritage, enduring rarity,</text>
    <text x="15" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">and multi-generational legacy value.</text>

    <rect x="10" y="275" width="215" height="70" rx="6" fill="#0F172A"/>
    <text x="15" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Key Phrase:</text>
    <text x="15" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"A timeless heirloom that will look</text>
    <text x="15" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">just as iconic in fifty years."</text>

    <!-- Persona 2: The Modern Minimalist -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. MODERN MINIMALIST</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Profile &amp; Priorities:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Clean architectural lines</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Step cut (Emerald/Asscher) or Oval</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Rejects heavy ornate halos</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Metal &amp; Mounting:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Ultra-thin 1.6mm band or Bezel cup</text>

    <text x="270" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Effective Sales Angle:</text>
    <text x="270" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Focus on diamond clarity purity,</text>
    <text x="270" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">understated luxury, and daily comfort.</text>

    <rect x="265" y="275" width="215" height="70" rx="6" fill="#0F172A"/>
    <text x="270" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Key Phrase:</text>
    <text x="270" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Pure geometric design that lets</text>
    <text x="270" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">the diamond speak for itself."</text>

    <!-- Persona 3: Eco & Unique -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. ECO &amp; UNIQUE</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Profile &amp; Priorities:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Values sustainability &amp; ethics</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Open to Lab-Grown or Sapphires</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Vintage details, milgrain, east-west</text>

    <text x="525" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Metal &amp; Mounting:</text>
    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">100% Recycled Gold or Fairmined 18K</text>

    <text x="525" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Effective Sales Angle:</text>
    <text x="525" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Focus on traceable supply chain,</text>
    <text x="525" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">bespoke individuality, and artistry.</text>

    <rect x="520" y="275" width="215" height="70" rx="6" fill="#0F172A"/>
    <text x="525" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Key Phrase:</text>
    <text x="525" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"A uniquely expressive design crafted</text>
    <text x="525" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">with verified ethical provenance."</text>

    <!-- Persona 4: High-Carat Maximalist -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. HIGH-CARAT MAXIMALIST</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Profile &amp; Priorities:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Maximum finger presence &amp; flash</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• 3.0ct to 5.0ct+ center stone</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Elongated Radiant, Oval, or Pear</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Metal &amp; Mounting:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">Hidden halo + 3/4 diamond pavé shank</text>

    <text x="780" y="210" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Effective Sales Angle:</text>
    <text x="780" y="230" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Showcase 360° light performance,</text>
    <text x="780" y="248" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">scintillation, and statement scale.</text>

    <rect x="775" y="275" width="215" height="70" rx="6" fill="#0F172A"/>
    <text x="780" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Key Phrase:</text>
    <text x="780" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">"Unrivaled stage presence that</text>
    <text x="780" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">commands the entire room."</text>
  </g>

  <!-- Summary Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">HOW TO IDENTIFY PERSONAS IN THE FIRST 60 SECONDS:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Observe their phone lock screen, watch choice, and jewelry worn into the store. Ask: <em>"When you envision your everyday style, do you gravitate toward clean architectural lines, vintage antique romance, or bold statement brilliance?"</em></text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m11-demographic-bridal-personas.svg", c6_m11)

# C6 M12: Ethical Selling Code Pillars
c6_m12 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Ethical Standards in High-Ticket Bridal Selling: 4 Core Pillars</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Protecting consumer trust, preventing predatory tactics, and upholding the integrity of the fine jewelry profession</text>

  <!-- 4 Pillars Cards -->
  <g transform="translate(50, 100)">
    <!-- Pillar 1 -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. UNBIASED DISCLOSURE</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">The Standard:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Full FTC material disclosure</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Disclose all gemstone heat,</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  fracture filling &amp; oils</text>
    <text x="15" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Clear natural vs lab origins</text>

    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Prohibited Practice:</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Hiding treatments on invoice</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Ambiguous terminology</text>
    <text x="15" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  ("cultured" diamond)</text>

    <rect x="10" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="15" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Principle:</text>
    <text x="15" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Trust is built on 100% upfront</text>
    <text x="15" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">technical honesty.</text>

    <!-- Pillar 2 -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. NO FEAR OR GUILT</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">The Standard:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Respect the client's stated</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  budget comfort zone</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Guide with joyful pride</text>
    <text x="270" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Re-engineer 4Cs to fit</text>

    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Prohibited Practice:</text>
    <text x="270" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• "Two months' salary" guilt</text>
    <text x="270" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Shaming budget limits</text>
    <text x="270" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• High-pressure urgency closes</text>

    <rect x="265" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="270" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Principle:</text>
    <text x="270" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Never let a client leave with</text>
    <text x="270" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">financial remorse or dread.</text>

    <!-- Pillar 3 -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. TRANSPARENT PRICING</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">The Standard:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Fair, honest markup baseline</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Accurate stone itemization</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  (Center + Setting + Labor)</text>
    <text x="525" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Consistent policy across staff</text>

    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Prohibited Practice:</text>
    <text x="525" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Fake "Today Only 50% Off"</text>
    <text x="525" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Inflated appraisal discounts</text>
    <text x="525" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Bait-and-switch certificates</text>

    <rect x="520" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="525" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Principle:</text>
    <text x="525" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">A luxury house never plays</text>
    <text x="525" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">used-car pricing games.</text>

    <!-- Pillar 4 -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. CONFLICT-FREE SOURCING</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">The Standard:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Kimberley Process compliance</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Responsible Jewellery Council</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  (RJC) certified chain-of-custody</text>
    <text x="780" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Verifiable mine origin records</text>

    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Prohibited Practice:</text>
    <text x="780" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Unvetted grey-market parcels</text>
    <text x="780" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Buying untraced rough gold</text>
    <text x="780" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Misrepresenting origin source</text>

    <rect x="775" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="780" y="295" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Principle:</text>
    <text x="780" y="315" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Symbol of love must carry</text>
    <text x="780" y="330" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">a clean, proud human legacy.</text>
  </g>

  <!-- Summary Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE RETAIL REPUTATION MANDATE:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">In high-ticket bridal, a single high-pressure deceptive sale costs the store tens of thousands in lost referral revenue. Advisors who practice radical integrity and empathy build unbreakable client books that compound over decades.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m12-ethical-selling-code-pillars.svg", c6_m12)

# C6 M13: Cruise Port Compressed Sales Cycle
c6_m13 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Port-of-Call Bridal Sales Velocity: The 180-Minute Execution Model</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Selling high-ticket bridal jewelry under tight cruise ship port departure time constraints</text>

  <!-- 4-Stage Compressed Clock -->
  <g transform="translate(50, 100)">
    <!-- Stage 1: Minutes 0-15 -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">STAGE 1: 0 – 15 MIN</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Immediate Engagement:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Warm vacation greeting</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Determine Ship &amp; All-Aboard</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  time (e.g. 4:30 PM departure)</text>
    <text x="15" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Rapid discovery: Anniv vs Proposal</text>

    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Duty-Free Positioning:</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Frame tax-free &amp; duty-free</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  island savings immediately</text>

    <rect x="10" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Action:</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Offer cold beverage, seat couple</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">at private presentation counter.</text>

    <!-- Stage 2: Minutes 15-45 -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">STAGE 2: 15 – 45 MIN</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">The Curated 3-Piece Edit:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pull max 3 showstopper rings</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Place directly on her finger</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Pair with natural sunlight view</text>

    <text x="270" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Vacation Emotion Anchor:</text>
    <text x="270" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• "Every time she looks at this,</text>
    <text x="270" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  she will remember this voyage."</text>

    <rect x="265" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="270" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Action:</text>
    <text x="270" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Isolate the single winning ring;</text>
    <text x="270" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">remove other distraction pieces.</text>

    <!-- Stage 3: Minutes 45-75 -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">STAGE 3: 45 – 75 MIN</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Rapid Bench Execution:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Measure exact finger size</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Rush sizing to on-site bench</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  (Guaranteed 45-min turnaround)</text>
    <text x="525" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Complete POS transaction</text>

    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Trust Reassurance:</text>
    <text x="525" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• GIA Certificate in hand</text>
    <text x="525" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• US Service Center warranty</text>

    <rect x="520" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="525" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Action:</text>
    <text x="525" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Provide customs declaration slip</text>
    <text x="525" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">and certified appraisal packet.</text>

    <!-- Stage 4: Minutes 75-120 -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">STAGE 4: 75 – 120 MIN</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#CBD5E1">Delivery &amp; Ship Return:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Ring polished, cleaned &amp; boxed</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Worn out of store onto ship</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  for formal captain's dinner</text>

    <text x="780" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Failsafe Pier Courier:</text>
    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• If intricate bench sizing runs</text>
    <text x="780" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  late, bonded courier delivers</text>
    <text x="780" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  directly to ship purser desk</text>

    <rect x="775" y="260" width="215" height="85" rx="6" fill="#0F172A"/>
    <text x="780" y="285" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Action:</text>
    <text x="780" y="305" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Capture digital email/SMS for</text>
    <text x="780" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">post-cruise clienteling cadence.</text>
  </g>

  <!-- Summary Box -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE CRITICAL SUCCESS FACTOR IN PORT RETAIL:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Speed without rushing elegance. Travelers will make major $10k+ purchase decisions in under an hour if they feel complete security regarding authentic GIA certification, on-site master jeweler sizing, and domestic warranty service centers.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m13-cruise-port-compressed-sales-cycle.svg", c6_m13)

# C6 M14: Private Salon Bridal Experience Capstone
c6_m14 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">The Private Salon Bridal Experience: Luxury Appointment Blueprint</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Orchestrating high-net-worth VIP bridal appointments in luxury hotel suites and private salon viewing rooms</text>

  <!-- 4 Environmental & Experiential Quadrants -->
  <g transform="translate(50, 100)">
    <!-- Quadrant 1 -->
    <rect x="0" y="0" width="480" height="170" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. ATMOSPHERIC &amp; SENSORY STAGING</text>
    <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Lighting: Balanced 5500K diamond grading lamps + warm 3000K ambient</text>
    <text x="15" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Hospitality: Chilled boutique champagne, sparkling mineral water, espresso</text>
    <text x="15" y="95" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Sound: Low-decibel acoustic jazz; complete acoustic privacy from floor</text>
    <text x="15" y="115" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Materials: Heavy weighted leather or suede consultation pads and brass loupes</text>
    <text x="15" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Goal: Complete sensory decompression and luxury exclusivity</text>

    <!-- Quadrant 2 -->
    <rect x="520" y="0" width="480" height="170" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="520" y="0" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="535" y="22" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. PRE-STAGED CURATED TRAY</text>
    <text x="535" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Pre-selected 3–4 hero pieces based on pre-appointment phone discovery</text>
    <text x="535" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Loose diamonds displayed in stone papers alongside empty designer mountings</text>
    <text x="535" y="95" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Clean, uncluttered table — never overwhelm client with 20 distracting rings</text>
    <text x="535" y="115" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Individual leather ring risers for each option</text>
    <text x="535" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Goal: Hyper-focused, intentional aesthetic evaluation</text>

    <!-- Quadrant 3 -->
    <rect x="0" y="190" width="480" height="170" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="0" y="190" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="15" y="212" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. INTERACTIVE GEMOLOGICAL REVEAL</text>
    <text x="15" y="245" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Invite client to hold 10x triplet loupe and gemological tweezers</text>
    <text x="15" y="265" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• High-definition digital microscope feed to 4K monitor for inscription verify</text>
    <text x="15" y="285" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Ideal-Scope / ASET light reflector demonstration of optical symmetry</text>
    <text x="15" y="305" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Educate through fascination rather than sales pressure</text>
    <text x="15" y="335" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Goal: Transfer expert confidence to the buyer</text>

    <!-- Quadrant 4 -->
    <rect x="520" y="190" width="480" height="170" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="520" y="190" width="480" height="32" rx="8" fill="#1E293B"/>
    <text x="535" y="212" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. WHITE-GLOVE CONCIERGE CLOSING</text>
    <text x="535" y="245" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Discreet electronic billing link or private wireless terminal</text>
    <text x="535" y="265" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Leather-bound appraisal portfolio and certificate sleeve presentation</text>
    <text x="535" y="285" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Personalized thank you gift (e.g. crystal champagne flutes or travel pouch)</text>
    <text x="535" y="305" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#94A3B8">• Private vehicle escort to valet upon departure</text>
    <text x="535" y="335" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Goal: Unforgettable milestone dignity from arrival to exit</text>
  </g>

  <!-- Summary Banner -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="1000" height="150" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">THE PRIVATE APPOINTMENT CONVERSION ADVANTAGE:</text>
    <text x="20" y="58" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Walk-in floor traffic averages 15–22% closing rates, whereas <strong fill="#10B981">private scheduled bridal salon appointments close at 70–85%</strong> with a 2.4× higher average ticket. The private appointment is the pinnacle sales format of the fine jewelry industry.</text>
  </g>
</svg>"""
write_svg("courses/C6-bridal-engagement-mastery/assets/c6-m14-private-salon-bridal-experience.svg", c6_m14)

print("C6 Part 2 SVG assets generated successfully!")
