import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# ==========================================
# C1 SVGs
# ==========================================

svg_c1_optics = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C5A059"/>
      <stop offset="50%" stop-color="#FDF0CD"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
    <filter id="rayGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="16" fill="url(#bgGrad)"/>
  <rect x="2" y="2" width="1096" height="646" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 45)">
    <rect x="0" y="0" width="170" height="24" rx="12" fill="#1E3A8A" fill-opacity="0.6"/>
    <text x="85" y="16" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">OPTICAL PHYSICS</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Diamond Cut Optics &amp; Light Performance</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Ray-tracing analysis: Ideal reflection vs. Shallow/Deep light leakage paths.</text>
  </g>

  <!-- Profile 1: Shallow Cut (Fish-Eye) -->
  <g transform="translate(60, 150)">
    <rect x="0" y="0" width="300" height="440" rx="12" fill="#111827" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="15" y="15" width="120" height="22" rx="4" fill="#EF4444" fill-opacity="0.2"/>
    <text x="75" y="30" fill="#F87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SHALLOW CUT</text>
    <text x="15" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">"Fish-Eye" Effect</text>
    <text x="15" y="80" fill="#9CA3AF" font-family="system-ui, sans-serif" font-size="11">Pavilion too flat (&lt;39.5°). Light strikes pavilion at angle &lt; 24.4° critical angle.</text>

    <!-- Diamond Shape -->
    <g transform="translate(25, 120)">
      <polygon points="50,0 200,0 250,30 0,30" fill="#374151" stroke="#9CA3AF" stroke-width="1.5"/>
      <polygon points="0,30 250,30 125,90" fill="#1F2937" stroke="#9CA3AF" stroke-width="1.5"/>
      <!-- Light rays entering and leaking -->
      <path d="M 80,-30 L 80,0 L 95,50 L 105,100" fill="none" stroke="#F87171" stroke-width="2.5" stroke-dasharray="4,2" filter="url(#rayGlow)"/>
      <path d="M 170,-30 L 170,0 L 155,50 L 145,100" fill="none" stroke="#F87171" stroke-width="2.5" stroke-dasharray="4,2" filter="url(#rayGlow)"/>
      <!-- Leakage callout -->
      <text x="125" y="125" fill="#EF4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">▼ Light Leaks Out Bottom</text>
    </g>

    <!-- Characteristics Box -->
    <g transform="translate(15, 290)">
      <rect x="0" y="0" width="270" height="130" rx="8" fill="#1F2937"/>
      <text x="12" y="24" fill="#F87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Visual Diagnosis on Pad:</text>
      <text x="12" y="46" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Dull grey / glassy dead center ring</text>
      <text x="12" y="66" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Girdle reflection visible through table</text>
      <text x="12" y="86" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Lack of contrast &amp; zero scintillation</text>
      <text x="12" y="108" fill="#9CA3AF" font-family="system-ui, sans-serif" font-size="10">Client feeling: "Looks washed out"</text>
    </g>
  </g>

  <!-- Profile 2: Ideal Cut (GIA Excellent) -->
  <g transform="translate(400, 150)">
    <rect x="0" y="0" width="300" height="440" rx="12" fill="#064E3B" fill-opacity="0.3" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="15" width="140" height="22" rx="4" fill="#10B981" fill-opacity="0.25"/>
    <text x="85" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">EXCELLENT / IDEAL</text>
    <text x="15" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">Total Internal Reflection</text>
    <text x="15" y="80" fill="#9CA3AF" font-family="system-ui, sans-serif" font-size="11">Crown: 34.5°, Pavilion: 40.8°. Light reflects twice internally and returns face-up.</text>

    <!-- Diamond Shape -->
    <g transform="translate(25, 110)">
      <polygon points="50,0 200,0 250,45 0,45" fill="#1E3A8A" fill-opacity="0.4" stroke="#60A5FA" stroke-width="1.5"/>
      <polygon points="0,45 250,45 125,150" fill="#1E293B" stroke="#60A5FA" stroke-width="1.5"/>
      <!-- Perfect ray tracing -->
      <path d="M 80,-30 L 80,0 L 45,95 L 180,105 L 160,-25" fill="none" stroke="#FDE047" stroke-width="2.5" filter="url(#rayGlow)"/>
      <path d="M 170,-30 L 170,0 L 205,95 L 70,105 L 90,-25" fill="none" stroke="#38BDF8" stroke-width="2.5" filter="url(#rayGlow)"/>
      <!-- Return sparkles -->
      <polygon points="160,-25 155,-35 160,-45 165,-35" fill="#FDE047"/>
      <polygon points="90,-25 85,-35 90,-45 95,-35" fill="#38BDF8"/>
      <text x="125" y="-35" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">▲ Maximum Light Return</text>
    </g>

    <!-- Characteristics Box -->
    <g transform="translate(15, 290)">
      <rect x="0" y="0" width="270" height="130" rx="8" fill="#064E3B" fill-opacity="0.5"/>
      <text x="12" y="24" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Visual Output in Light:</text>
      <text x="12" y="46" fill="#ECFDF5" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Brightness:</tspan> Blinding white reflection</text>
      <text x="12" y="66" fill="#ECFDF5" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Fire:</tspan> Intense red, blue &amp; yellow flares</text>
      <text x="12" y="86" fill="#ECFDF5" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Scintillation:</tspan> Crisp dynamic contrast</text>
      <text x="12" y="108" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10">Client feeling: "Explodes with light"</text>
    </g>
  </g>

  <!-- Profile 3: Deep Cut (Nail-Head) -->
  <g transform="translate(740, 150)">
    <rect x="0" y="0" width="300" height="440" rx="12" fill="#111827" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="15" y="15" width="110" height="22" rx="4" fill="#F59E0B" fill-opacity="0.2"/>
    <text x="70" y="30" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DEEP CUT</text>
    <text x="15" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">"Nail-Head" Effect</text>
    <text x="15" y="80" fill="#9CA3AF" font-family="system-ui, sans-serif" font-size="11">Pavilion too steep (&gt;42.0°). Light reflects across to opposite facet and escapes.</text>

    <!-- Diamond Shape -->
    <g transform="translate(25, 90)">
      <polygon points="50,0 200,0 250,45 0,45" fill="#374151" stroke="#9CA3AF" stroke-width="1.5"/>
      <polygon points="0,45 250,45 125,185" fill="#1F2937" stroke="#9CA3AF" stroke-width="1.5"/>
      <!-- Leaking ray tracing -->
      <path d="M 80,-30 L 80,0 L 55,110 L 220,130 L 260,140" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="4,2" filter="url(#rayGlow)"/>
      <path d="M 170,-30 L 170,0 L 195,110 L 30,130 L -10,140" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="4,2" filter="url(#rayGlow)"/>
      <text x="125" y="65" fill="#111827" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">DARK CENTER</text>
      <circle cx="125" cy="22" r="14" fill="#0F172A" stroke="#EF4444" stroke-width="1"/>
    </g>

    <!-- Characteristics Box -->
    <g transform="translate(15, 290)">
      <rect x="0" y="0" width="270" height="130" rx="8" fill="#1F2937"/>
      <text x="12" y="24" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Visual Diagnosis on Pad:</text>
      <text x="12" y="46" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Heavy dark black spot under table</text>
      <text x="12" y="66" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Stone looks small for its carat weight</text>
      <text x="12" y="86" fill="#D1D5DB" font-family="system-ui, sans-serif" font-size="11">• Client pays for hidden "dead" weight</text>
      <text x="12" y="108" fill="#9CA3AF" font-family="system-ui, sans-serif" font-size="10">Client feeling: "Dark &amp; heavy"</text>
    </g>
  </g>
</svg>"""

svg_c1_4cs = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="#E5C378"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="700" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="696" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 40)">
    <text x="0" y="20" fill="url(#gold)" font-family="system-ui, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5">JEWELSWELL COUNTER DRILL</text>
    <text x="0" y="50" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="24" font-weight="700">The 4Cs Sales Floor Demonstration Matrix</text>
    <text x="0" y="72" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">What the client asks vs. What the associate demonstrates with stones on the pad.</text>
  </g>

  <!-- 4 Quadrants -->
  <!-- 1. CUT -->
  <g transform="translate(50, 130)">
    <rect width="480" height="240" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#0284C7"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">1</text>
    <text x="65" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">CUT — "The Human Artistry"</text>
    <text x="65" y="50" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="600">GIA: Excellent | Very Good | Good | Fair | Poor</text>

    <text x="20" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#F8FAFC">Client Question:</tspan> "Why does this one sparkle so much more?"</text>
    <text x="20" y="110" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#38BDF8">Counter Move:</tspan> Rock two stones under the spot light.</text>
    <text x="20" y="130" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Point out <tspan font-weight="700" fill="#FFFFFF">Brightness</tspan> (white return) vs <tspan font-weight="700" fill="#FFFFFF">Fire</tspan> (rainbow dispersion).</text>
    <text x="20" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Show that cut controls 100% of light return; color &amp; clarity cannot compensate.</text>

    <rect x="20" y="175" width="440" height="45" rx="6" fill="#0F172A"/>
    <text x="30" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11"><tspan font-weight="700" fill="#FBBF24">Rule of Thumb:</tspan> Never compromise below Very Good cut for bridal;</text>
    <text x="30" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">an Excellent cut masks minor body tint and slight inclusions.</text>
  </g>

  <!-- 2. COLOR -->
  <g transform="translate(570, 130)">
    <rect width="480" height="240" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#D97706"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">2</text>
    <text x="65" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">COLOR — "The Absence of Tint"</text>
    <text x="65" y="50" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="600">D-F (Colorless) | G-J (Near Colorless) | K-M (Faint)</text>

    <text x="20" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#F8FAFC">Client Question:</tspan> "Do I need a D color stone to look white?"</text>
    <text x="20" y="110" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#FBBF24">Counter Move:</tspan> Place a G/H next to a D/E upside-down on a white card.</text>
    <text x="20" y="130" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Show that face-up in platinum/white gold, G-H reads icy white to the eye.</text>
    <text x="20" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• In yellow or rose gold, I-J stones match warmth seamlessly at 25-35% savings.</text>

    <rect x="20" y="175" width="440" height="45" rx="6" fill="#0F172A"/>
    <text x="30" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11"><tspan font-weight="700" fill="#FBBF24">Floor Phrasing:</tspan> "Color is graded through the side against pure white.</text>
    <text x="30" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Face up in a setting, cut brilliance masks subtle warmth effortlessly."</text>
  </g>

  <!-- 3. CLARITY -->
  <g transform="translate(50, 400)">
    <rect width="480" height="240" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#059669"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">3</text>
    <text x="65" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">CLARITY — "Earth's Birthmarks"</text>
    <text x="65" y="50" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="600">FL/IF | VVS1-2 | VS1-2 | SI1-2 | I1-3 (Graded under 10x)</text>

    <text x="20" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#F8FAFC">Client Question:</tspan> "Does this diamond have flaws in it?"</text>
    <text x="20" y="110" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#34D399">Counter Move:</tspan> Hand them the 10x loupe and define 'Eye-Clean'.</text>
    <text x="20" y="130" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• 5 Factors: Size, Number, Location (prong vs table), Relief (dark vs clear), Nature.</text>
    <text x="20" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Explain that VS2/SI1 gives 100% eye-clean appearance at counter distance.</text>

    <rect x="20" y="175" width="440" height="45" rx="6" fill="#0F172A"/>
    <text x="30" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11"><tspan font-weight="700" fill="#34D399">Floor Phrasing:</tspan> "Inclusions are diamond fingerprints from 100 miles below ground.</text>
    <text x="30" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Our goal is an eye-clean stone where no feature interferes with light return."</text>
  </g>

  <!-- 4. CARAT -->
  <g transform="translate(570, 400)">
    <rect width="480" height="240" rx="10" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#7E22CE"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">4</text>
    <text x="65" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700">CARAT — "Mass, Not Physical Size"</text>
    <text x="65" y="50" fill="#C084FC" font-family="system-ui, sans-serif" font-size="11" font-weight="600">1.00 ct = 200 mg = 100 Points | Spread vs Depth</text>

    <text x="20" y="85" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#F8FAFC">Client Question:</tspan> "I want a 1.00ct stone. Why does this 0.90ct look just as big?"</text>
    <text x="20" y="110" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12"><tspan font-weight="700" fill="#C084FC">Counter Move:</tspan> Measure diameter with mm gauge on the pad.</text>
    <text x="20" y="130" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• An Excellent cut 0.90ct spreads ~6.2mm; a deep 1.00ct spreads only ~6.2mm.</text>
    <text x="20" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Explain 'Magic Price Thresholds' at 1.00ct, 1.50ct, 2.00ct.</text>

    <rect x="20" y="175" width="440" height="45" rx="6" fill="#0F172A"/>
    <text x="30" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11"><tspan font-weight="700" fill="#C084FC">Floor Phrasing:</tspan> "You don't wear a scale on your finger; you wear mm spread.</text>
    <text x="30" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Shopping just below round numbers gives you identical visual size at exceptional value."</text>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m01-light-performance-optics.svg", svg_c1_optics)
save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m01-4cs-summary-matrix.svg", svg_c1_4cs)

print("C1 base SVGs saved successfully!")
