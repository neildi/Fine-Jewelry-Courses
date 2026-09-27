import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# c1-m02-gia-grading-report-annotated.svg
svg_c1_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 750" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="reportBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="750" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="746" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#C5A059" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#FDF0CD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">LAB REPORT ANATOMY</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Annotated GIA Diamond Grading Report Guide</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Line-by-line guide for walking a client through an authentic GIA grading dossier in 3 minutes.</text>
  </g>

  <!-- Simulated GIA Report Paper -->
  <g transform="translate(50, 125)">
    <rect width="600" height="580" rx="8" fill="url(#reportBg)" stroke="#CBD5E1" stroke-width="2"/>

    <!-- GIA Header -->
    <rect x="0" y="0" width="600" height="45" rx="8" fill="#1E3A8A"/>
    <text x="25" y="28" fill="#FFFFFF" font-family="Georgia, serif" font-size="18" font-weight="700" letter-spacing="2">GIA</text>
    <text x="75" y="28" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="12" font-weight="600">DIAMOND DOSSIER / GRADING REPORT</text>
    <text x="560" y="28" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10" text-anchor="end">GIA.edu/report-check</text>

    <!-- Section 1: Identification -->
    <g transform="translate(25, 60)">
      <text x="0" y="15" fill="#64748B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">GIA REPORT NUMBER</text>
      <text x="0" y="32" fill="#0F172A" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2468135790</text>
      <text x="0" y="50" fill="#64748B" font-family="system-ui, sans-serif" font-size="10">Laser Inscription Registry: GIA 2468135790</text>
      <text x="0" y="68" fill="#64748B" font-family="system-ui, sans-serif" font-size="10">Shape &amp; Cutting Style: Round Brilliant</text>
      <text x="0" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="10">Measurements: 6.48 - 6.51 x 4.01 mm</text>
    </g>

    <line x1="25" y1="160" x2="575" y2="160" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Section 2: Grading Results (4Cs) -->
    <g transform="translate(25, 175)">
      <text x="0" y="12" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="11" font-weight="800">GRADING RESULTS</text>
      <text x="0" y="34" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Carat Weight: <tspan font-weight="700" fill="#0F172A">1.03 carat</tspan></text>
      <text x="0" y="54" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Color Grade: <tspan font-weight="700" fill="#0F172A">F</tspan></text>
      <text x="0" y="74" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Clarity Grade: <tspan font-weight="700" fill="#0F172A">VS1</tspan></text>
      <text x="0" y="94" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Cut Grade: <tspan font-weight="700" fill="#0F172A">Excellent</tspan></text>
    </g>

    <!-- Section 3: Additional Grading Info -->
    <g transform="translate(300, 175)">
      <text x="0" y="12" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="11" font-weight="800">ADDITIONAL INFORMATION</text>
      <text x="0" y="34" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Polish: <tspan font-weight="700" fill="#0F172A">Excellent</tspan></text>
      <text x="0" y="54" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Symmetry: <tspan font-weight="700" fill="#0F172A">Excellent</tspan></text>
      <text x="0" y="74" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Fluorescence: <tspan font-weight="700" fill="#0F172A">None</tspan></text>
      <text x="0" y="94" fill="#334155" font-family="system-ui, sans-serif" font-size="11">Clarity Characteristics: <tspan font-weight="700" fill="#0F172A">Crystal, Pinpoint</tspan></text>
    </g>

    <line x1="25" y1="290" x2="575" y2="290" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Section 4: Proportions Diagram -->
    <g transform="translate(25, 305)">
      <text x="0" y="12" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="11" font-weight="800">PROPORTIONS PROFILE</text>
      <g transform="translate(40, 30)">
        <polygon points="30,0 120,0 150,25 0,25" fill="#E2E8F0" stroke="#64748B" stroke-width="1"/>
        <rect x="0" y="25" width="150" height="6" fill="#94A3B8" stroke="#64748B" stroke-width="1"/>
        <polygon points="0,31 150,31 75,95" fill="#CBD5E1" stroke="#64748B" stroke-width="1"/>
        <text x="75" y="-6" fill="#0F172A" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Table 56%</text>
        <text x="160" y="18" fill="#0F172A" font-family="system-ui, sans-serif" font-size="8">34.5° (15.0%)</text>
        <text x="160" y="65" fill="#0F172A" font-family="system-ui, sans-serif" font-size="8">40.8° (43.0%)</text>
        <text x="75" y="110" fill="#0F172A" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Total Depth: 61.8% | Culet: None</text>
      </g>
    </g>

    <!-- Section 5: Clarity Plotting -->
    <g transform="translate(320, 305)">
      <text x="0" y="12" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="11" font-weight="800">CLARITY PLOT (CROWN &amp; PAVILION)</text>
      <g transform="translate(40, 30)">
        <circle cx="50" cy="50" r="45" fill="#F8FAFC" stroke="#64748B" stroke-width="1"/>
        <polygon points="50,15 75,35 75,65 50,85 25,65 25,35" fill="none" stroke="#94A3B8" stroke-width="0.8"/>
        <!-- Red internal inclusion symbol -->
        <circle cx="60" cy="40" r="2" fill="#EF4444"/>
        <circle cx="45" cy="60" r="1" fill="#EF4444"/>
        <text x="50" y="110" fill="#EF4444" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Red = Internal | Green = External</text>
      </g>
    </g>

    <!-- Security hologram footer -->
    <g transform="translate(25, 485)">
      <rect x="0" y="0" width="550" height="75" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
      <rect x="10" y="12" width="50" height="50" rx="4" fill="#0F172A"/>
      <text x="35" y="42" fill="#94A3B8" font-family="monospace" font-size="8" text-anchor="middle">QR / RFID</text>
      <text x="75" y="28" fill="#0F172A" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Security Features: Microprint, Hologram, Embossed Seal</text>
      <text x="75" y="46" fill="#64748B" font-family="system-ui, sans-serif" font-size="10">Verify online at GIA Report Check or scan QR code on mobile device.</text>
      <text x="75" y="62" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Note: GIA issues grading reports (opinions), NOT commercial 'certificates'.</text>
    </g>
  </g>

  <!-- Right Side Callouts (What to Say & Check) -->
  <g transform="translate(680, 125)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="370" height="135" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
    <text x="15" y="24" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. Laser Inscription Match</text>
    <text x="15" y="46" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">Always loupe the diamond's girdle in front of</text>
    <text x="15" y="64" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">the client to match the report number.</text>
    <text x="15" y="86" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11"><tspan font-weight="700" fill="#F8FAFC">Counter Script:</tspan> "Let's read this microscope</text>
    <text x="15" y="104" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">registry number together so you know it's this exact stone."</text>

    <!-- Card 2 -->
    <rect x="0" y="150" width="370" height="135" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1"/>
    <text x="15" y="24" fill="#34D399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. Triple Excellent Standard</text>
    <text x="15" y="46" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">Check all three: <tspan font-weight="700" fill="#FFFFFF">Cut (Ex), Polish (Ex), Symmetry (Ex)</tspan>.</text>
    <text x="15" y="68" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Polish: Mirror finish without drag lines or burns.</text>
    <text x="15" y="86" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• Symmetry: Facet junction alignment for crisp optical patterns.</text>
    <text x="15" y="106" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Known in the trade as a "Triple Ex" diamond.</text>

    <!-- Card 3 -->
    <rect x="0" y="300" width="370" height="135" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1"/>
    <text x="15" y="24" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">3. Fluorescence Truth at Counter</text>
    <text x="15" y="46" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">Fluorescence (None/Faint/Medium/Strong Blue) is</text>
    <text x="15" y="64" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">a natural reaction to UV light, NOT a defect.</text>
    <text x="15" y="86" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• In I-K colors, medium blue makes the stone face up whiter.</text>
    <text x="15" y="106" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">• In D-F, faint/none is preferred by strict investment collectors.</text>

    <!-- Card 4 -->
    <rect x="0" y="450" width="370" height="130" rx="8" fill="#1E293B" stroke="#EF4444" stroke-width="1"/>
    <text x="15" y="24" fill="#F87171" font-family="system-ui, sans-serif" font-size="13" font-weight="700">4. What NOT to Say (Compliance)</text>
    <text x="15" y="46" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="11">✖ "This certificate guarantees investment value."</text>
    <text x="15" y="66" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="11">✖ "GIA certified this diamond." (GIA reports, doesn't certify)</text>
    <text x="15" y="88" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="11">✔ "This is an independent scientific grading report from GIA."</text>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m02-gia-grading-report-annotated.svg", svg_c1_m02)

# c1-m03-ags-vs-gia-conversion-scale.svg
svg_c1_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="650" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="646" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 40)">
    <text x="0" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5">SCALE CONVERSION MATRIX</text>
    <text x="0" y="50" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">AGS 0–10 Numerical Scale vs. GIA Nomenclature</text>
    <text x="0" y="72" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Translating cut, color, and clarity between American Gem Society (AGS) and GIA standards.</text>
  </g>

  <!-- Comparison Table -->
  <g transform="translate(50, 130)">
    <!-- Cut Section -->
    <g transform="translate(0, 0)">
      <rect width="1000" height="145" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
      <rect x="0" y="0" width="160" height="145" rx="8" fill="#0284C7" fill-opacity="0.3"/>
      <text x="80" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CUT GRADE</text>
      <text x="80" y="80" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Optical &amp; Ray Tracing</text>

      <!-- Grid Headers -->
      <text x="190" y="30" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">AGS Scale (0-10):</text>
      <text x="190" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">GIA Scale:</text>

      <!-- Cells -->
      <g transform="translate(320, 15)">
        <rect x="0" y="0" width="120" height="32" rx="4" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
        <text x="60" y="21" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">0 (Ideal)</text>

        <rect x="135" y="0" width="120" height="32" rx="4" fill="#0F172A"/>
        <text x="195" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 – 2 (Ex)</text>

        <rect x="270" y="0" width="120" height="32" rx="4" fill="#0F172A"/>
        <text x="330" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">3 – 4 (VG)</text>

        <rect x="405" y="0" width="120" height="32" rx="4" fill="#0F172A"/>
        <text x="465" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">5 – 7 (Good)</text>

        <rect x="540" y="0" width="120" height="32" rx="4" fill="#0F172A"/>
        <text x="600" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">8 – 10 (Fair/Poor)</text>
      </g>

      <g transform="translate(320, 65)">
        <rect x="0" y="0" width="120" height="32" rx="4" fill="#1E3A8A" fill-opacity="0.4" stroke="#38BDF8" stroke-width="1"/>
        <text x="60" y="21" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Excellent</text>

        <rect x="135" y="0" width="120" height="32" rx="4" fill="#1E293B"/>
        <text x="195" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Excellent / VG</text>

        <rect x="270" y="0" width="120" height="32" rx="4" fill="#1E293B"/>
        <text x="330" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Very Good</text>

        <rect x="405" y="0" width="120" height="32" rx="4" fill="#1E293B"/>
        <text x="465" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Good</text>

        <rect x="540" y="0" width="120" height="32" rx="4" fill="#1E293B"/>
        <text x="600" y="21" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Fair / Poor</text>
      </g>
      <text x="190" y="125" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Key Floor Fact: AGS 0 'Triple Ideal' is mathematically the most stringent optical standard in retail.</text>
    </g>

    <!-- Color Section -->
    <g transform="translate(0, 165)">
      <rect width="1000" height="145" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1"/>
      <rect x="0" y="0" width="160" height="145" rx="8" fill="#D97706" fill-opacity="0.3"/>
      <text x="80" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">COLOR GRADE</text>
      <text x="80" y="80" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0.0 to 10.0 Scale</text>

      <text x="190" y="30" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">AGS Scale:</text>
      <text x="190" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">GIA Scale:</text>

      <g transform="translate(320, 15)">
        <rect x="0" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="42" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">0.0 (D)</text>
        <rect x="95" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="137" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">0.5 (E)</text>
        <rect x="190" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="232" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1.0 (F)</text>
        <rect x="285" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="327" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1.5 (G)</text>
        <rect x="380" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="422" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2.0 (H)</text>
        <rect x="475" y="0" width="85" height="32" rx="4" fill="#0F172A"/>
        <text x="517" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2.5 (I)</text>
        <rect x="570" y="0" width="95" height="32" rx="4" fill="#0F172A"/>
        <text x="617" y="21" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3.0–10.0 (J–Z)</text>
      </g>

      <g transform="translate(320, 65)">
        <rect x="0" y="0" width="275" height="32" rx="4" fill="#1E3A8A" fill-opacity="0.3"/>
        <text x="137" y="21" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Colorless (D – F)</text>
        <rect x="285" y="0" width="275" height="32" rx="4" fill="#D97706" fill-opacity="0.2"/>
        <text x="422" y="21" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Near Colorless (G – J)</text>
        <rect x="570" y="0" width="95" height="32" rx="4" fill="#78350F" fill-opacity="0.3"/>
        <text x="617" y="21" fill="#FDE047" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Faint to Light</text>
      </g>
      <text x="190" y="125" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Rule: AGS color steps in 0.5 increments. Each 0.5 step corresponds to exactly one GIA letter grade.</text>
    </g>

    <!-- Clarity Section -->
    <g transform="translate(0, 330)">
      <rect width="1000" height="145" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1"/>
      <rect x="0" y="0" width="160" height="145" rx="8" fill="#059669" fill-opacity="0.3"/>
      <text x="80" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CLARITY GRADE</text>
      <text x="80" y="80" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0 to 10 Scale</text>

      <text x="190" y="30" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">AGS Scale:</text>
      <text x="190" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">GIA Scale:</text>

      <g transform="translate(320, 15)">
        <rect x="0" y="0" width="100" height="32" rx="4" fill="#0F172A"/>
        <text x="50" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">0 (FL / IF)</text>
        <rect x="110" y="0" width="100" height="32" rx="4" fill="#0F172A"/>
        <text x="160" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1–2 (VVS1-2)</text>
        <rect x="220" y="0" width="100" height="32" rx="4" fill="#0F172A"/>
        <text x="270" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3–4 (VS1-2)</text>
        <rect x="330" y="0" width="100" height="32" rx="4" fill="#0F172A"/>
        <text x="380" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5–6 (SI1-2)</text>
        <rect x="440" y="0" width="110" height="32" rx="4" fill="#0F172A"/>
        <text x="495" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">7–8 (I1-2)</text>
        <rect x="560" y="0" width="105" height="32" rx="4" fill="#0F172A"/>
        <text x="612" y="21" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">9–10 (I3)</text>
      </g>

      <g transform="translate(320, 65)">
        <rect x="0" y="0" width="100" height="32" rx="4" fill="#065F46" fill-opacity="0.4"/>
        <text x="50" y="21" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Flawless/IF</text>
        <rect x="110" y="0" width="100" height="32" rx="4" fill="#065F46" fill-opacity="0.3"/>
        <text x="160" y="21" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">VVS1 / VVS2</text>
        <rect x="220" y="0" width="100" height="32" rx="4" fill="#1E3A8A" fill-opacity="0.3"/>
        <text x="270" y="21" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">VS1 / VS2</text>
        <rect x="330" y="0" width="100" height="32" rx="4" fill="#D97706" fill-opacity="0.2"/>
        <text x="380" y="21" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">SI1 / SI2</text>
        <rect x="440" y="0" width="225" height="32" rx="4" fill="#991B1B" fill-opacity="0.2"/>
        <text x="552" y="21" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Included (I1 – I3)</text>
      </g>
      <text x="190" y="125" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Counter Script: "AGS 0 is Flawless; AGS 3/4 is VS1/VS2, where inclusions are strictly invisible without a 10x microscope."</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m03-ags-vs-gia-conversion-scale.svg", svg_c1_m03)

# c1-m04-disclosure-decision-tree.svg
svg_c1_m04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#B91C1C" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">FTC COMPLIANCE PROTOCOL</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Natural vs. Lab-Grown vs. Simulant Disclosure Flowchart</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Mandatory legal terminology, physical differences, and customer-facing counter scripts.</text>
  </g>

  <!-- 3 Main Columns -->
  <!-- Column 1: Natural Diamonds -->
  <g transform="translate(50, 130)">
    <rect width="310" height="500" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="15" y="15" width="280" height="40" rx="6" fill="#0284C7" fill-opacity="0.3"/>
    <text x="155" y="40" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">1. NATURAL DIAMOND</text>

    <g transform="translate(20, 75)">
      <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Origin &amp; Geology</text>
      <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Formed 1–3 billion years ago</text>
      <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 100+ miles deep in Earth's mantle</text>
      <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Brought up by kimberlite eruptions</text>
      <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 100% pure carbon, Mohs 10</text>

      <line x1="0" y1="110" x2="270" y2="110" stroke="#334155" stroke-width="1"/>

      <text x="0" y="130" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">FTC Permitted Terms</text>
      <text x="0" y="150" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">"Diamond" (unqualified refers only to natural), "Natural Diamond", "Earth-mined".</text>

      <line x1="0" y1="180" x2="270" y2="180" stroke="#334155" stroke-width="1"/>

      <text x="0" y="200" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Value Proposition</text>
      <text x="0" y="220" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Finite global geological supply</text>
      <text x="0" y="238" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Heirloom provenance &amp; emotional permanence</text>
      <text x="0" y="256" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Established global trade liquidity</text>

      <rect x="-5" y="280" width="280" height="110" rx="6" fill="#0F172A"/>
      <text x="10" y="302" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Counter Presentation Script:</text>
      <text x="10" y="322" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"A natural diamond is a billion-year-old</text>
      <text x="10" y="338" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">miracle of nature. For couples looking for</text>
      <text x="10" y="354" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">rarity, history, and timeless permanence,</text>
      <text x="10" y="370" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">it has no substitute."</text>
    </g>
  </g>

  <!-- Column 2: Lab-Grown Diamonds -->
  <g transform="translate(395, 130)">
    <rect width="310" height="500" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
    <rect x="15" y="15" width="280" height="40" rx="6" fill="#059669" fill-opacity="0.3"/>
    <text x="155" y="40" fill="#34D399" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">2. LAB-GROWN (LGD)</text>

    <g transform="translate(20, 75)">
      <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Origin &amp; Physics</text>
      <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Grown in lab reactor via CVD or HPHT</text>
      <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Same chemical (C), optical, physical stats</text>
      <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Identical Mohs 10 hardness &amp; sparkle</text>
      <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Requires lab spectrometer to detect</text>

      <line x1="0" y1="110" x2="270" y2="110" stroke="#334155" stroke-width="1"/>

      <text x="0" y="130" fill="#34D399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">FTC Mandatory Terms</text>
      <text x="0" y="150" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">MUST use: "Laboratory-Grown", "Laboratory-Created", or "[Brand]-Created Diamond".</text>

      <line x1="0" y1="180" x2="270" y2="180" stroke="#334155" stroke-width="1"/>

      <text x="0" y="200" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Value Proposition</text>
      <text x="0" y="220" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 70–85% lower cost per carat</text>
      <text x="0" y="238" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Allows massive 2ct–4ct size on budget</text>
      <text x="0" y="256" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11">• Note: Industrial supply limits resale value</text>

      <rect x="-5" y="280" width="280" height="110" rx="6" fill="#0F172A"/>
      <text x="10" y="302" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Counter Presentation Script:</text>
      <text x="10" y="322" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"It is physically and chemically genuine</text>
      <text x="10" y="338" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">diamond grown in a laboratory. It lets you</text>
      <text x="10" y="354" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">maximize your finger spread and budget today,</text>
      <text x="10" y="370" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">though it does not carry natural rarity."</text>
    </g>
  </g>

  <!-- Column 3: Simulants (Moissanite / CZ) -->
  <g transform="translate(740, 130)">
    <rect width="310" height="500" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="15" y="15" width="280" height="40" rx="6" fill="#D97706" fill-opacity="0.3"/>
    <text x="155" y="40" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">3. SIMULANTS (CZ / MOISSANITE)</text>

    <g transform="translate(20, 75)">
      <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Composition &amp; Optics</text>
      <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• NOT diamond material</text>
      <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Moissanite: Silicon Carbide (SiC, Mohs 9.25)</text>
      <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• CZ: Cubic Zirconia (ZrO2, Mohs 8.5)</text>
      <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Moissanite is doubly refractive (facet doubling)</text>

      <line x1="0" y1="110" x2="270" y2="110" stroke="#334155" stroke-width="1"/>

      <text x="0" y="130" fill="#EF4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Strict FTC Prohibitions</text>
      <text x="0" y="150" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11">NEVER use the word "Diamond" alone. Prohibited: "Moissanite Diamond", "CZ Diamond".</text>

      <line x1="0" y1="180" x2="270" y2="180" stroke="#334155" stroke-width="1"/>

      <text x="0" y="200" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Value Proposition</text>
      <text x="0" y="220" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Ultra-low entry price point</text>
      <text x="0" y="238" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Travel / fashion substitute jewelry</text>
      <text x="0" y="256" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11">• CZ scratches &amp; clouds over time</text>

      <rect x="-5" y="280" width="280" height="110" rx="6" fill="#0F172A"/>
      <text x="10" y="302" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Counter Presentation Script:</text>
      <text x="10" y="322" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Moissanite is an imitation gemstone that</text>
      <text x="10" y="338" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">looks like a diamond. It offers extreme fire</text>
      <text x="10" y="354" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">at a fashion price, but is a completely</text>
      <text x="10" y="370" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">different mineral from genuine diamond."</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m04-disclosure-decision-tree.svg", svg_c1_m04)

# c1-m05-clarity-inclusion-plotting-symbols.svg
svg_c1_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
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
    <text x="90" y="16" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">GIA CLARITY PLOT KEY</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Inclusion &amp; Blemish Visual Plotting Guide</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">GIA plotting symbols, Red vs. Green coding, and the 5 clarity grade-setting factors.</text>
  </g>

  <!-- Left: Internal Inclusions (Red) -->
  <g transform="translate(50, 120)">
    <rect width="480" height="420" rx="10" fill="#1E293B" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="15" y="15" width="450" height="35" rx="6" fill="#991B1B" fill-opacity="0.4"/>
    <text x="25" y="38" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="14" font-weight="700">INTERNAL INCLUSIONS (Drawn in RED)</text>

    <g transform="translate(25, 70)">
      <!-- Feather -->
      <path d="M 0,15 Q 15,5 30,15 M 10,10 L 15,20 M 20,8 L 25,18" stroke="#EF4444" stroke-width="2" fill="none"/>
      <text x="45" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Feather (Ftr)</text>
      <text x="45" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Internal fracture/cleavage plane. Near girdle = durability risk.</text>

      <!-- Pinpoint -->
      <circle cx="15" cy="55" r="2.5" fill="#EF4444"/>
      <text x="45" y="54" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Pinpoint (Pp)</text>
      <text x="45" y="68" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Tiny mineral crystal seen at 10x as a minuscule dot.</text>

      <!-- Cloud -->
      <ellipse cx="15" cy="95" rx="12" ry="7" fill="none" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="2,2"/>
      <text x="45" y="94" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Cloud (Cld)</text>
      <text x="45" y="108" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Dense cluster of microscopic pinpoints. Can cause haze if large.</text>

      <!-- Crystal -->
      <polygon points="15,130 23,138 15,146 7,138" fill="none" stroke="#EF4444" stroke-width="1.5"/>
      <text x="45" y="134" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Crystal (Xtl)</text>
      <text x="45" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Mineral trapped inside diamond (garnet, diopside, diamond crystal).</text>

      <!-- Needle -->
      <line x1="5" y1="180" x2="25" y2="170" stroke="#EF4444" stroke-width="2"/>
      <text x="45" y="174" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Needle (Ndl)</text>
      <text x="45" y="188" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Long, thin rod-like mineral inclusion.</text>

      <!-- Twinning Wisp -->
      <path d="M 5,215 Q 15,200 25,225" fill="none" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3,2"/>
      <text x="45" y="214" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Twinning Wisp (W)</text>
      <text x="45" y="228" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Distortion along crystal growth twin plane.</text>

      <!-- Cavity / Knot -->
      <circle cx="15" cy="255" r="7" fill="#EF4444" fill-opacity="0.3" stroke="#EF4444" stroke-width="1.5"/>
      <text x="45" y="254" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Cavity (Cv) / Knot (K)</text>
      <text x="45" y="268" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Opening where surface crystal fell out / crystal reaching surface.</text>

      <!-- Laser Drill Hole -->
      <line x1="5" y1="300" x2="25" y2="300" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="25" cy="300" r="2" fill="#EF4444"/>
      <text x="45" y="294" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Laser Drill Hole (LDH)</text>
      <text x="45" y="308" fill="#EF4444" font-family="system-ui, sans-serif" font-size="10">Man-made clarity treatment channel. MANDATORY disclosure.</text>
    </g>
  </g>

  <!-- Right: External Blemishes (Green) -->
  <g transform="translate(570, 120)">
    <rect width="480" height="420" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
    <rect x="15" y="15" width="450" height="35" rx="6" fill="#065F46" fill-opacity="0.4"/>
    <text x="25" y="38" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="14" font-weight="700">EXTERNAL BLEMISHES (Drawn in GREEN)</text>

    <g transform="translate(25, 70)">
      <!-- Natural -->
      <polygon points="5,10 25,10 20,25 10,25" fill="#10B981" fill-opacity="0.5" stroke="#10B981" stroke-width="1"/>
      <text x="45" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Natural (N)</text>
      <text x="45" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Original unpolished rough skin left on girdle by cutter to save weight.</text>

      <!-- Indented Natural -->
      <polygon points="5,50 25,50 15,65" fill="#10B981" stroke="#EF4444" stroke-width="1.5"/>
      <text x="45" y="54" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Indented Natural (IN - Red/Green)</text>
      <text x="45" y="68" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Rough skin dipping below the facet surface into the stone.</text>

      <!-- Extra Facet -->
      <polygon points="10,90 25,95 20,110 5,105" fill="none" stroke="#10B981" stroke-width="1.5"/>
      <text x="45" y="94" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Extra Facet (EF)</text>
      <text x="45" y="108" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Additional facet placed without symmetry to polish away a defect.</text>

      <!-- Scratch / Polish Lines -->
      <line x1="5" y1="135" x2="25" y2="145" stroke="#10B981" stroke-width="1"/>
      <line x1="5" y1="140" x2="25" y2="150" stroke="#10B981" stroke-width="1"/>
      <text x="45" y="134" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Scratch (S) / Polish Lines (PL)</text>
      <text x="45" y="148" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Surface abrasions or wheel marks. Affects Polish grade.</text>

      <!-- Nick / Pit -->
      <circle cx="15" cy="180" r="3" fill="#10B981"/>
      <text x="45" y="174" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Nick (Nk) / Pit (P)</text>
      <text x="45" y="188" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Tiny surface opening on a facet junction or girdle edge.</text>

      <!-- Surface Graining -->
      <path d="M 5,215 L 25,215" stroke="#10B981" stroke-width="1.5" stroke-dasharray="2,2"/>
      <text x="45" y="214" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Surface Graining (SGr)</text>
      <text x="45" y="228" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Internal crystal growth structure intersecting the polished surface.</text>

      <!-- Summary Card inside green box -->
      <rect x="0" y="260" width="430" height="75" rx="6" fill="#0F172A"/>
      <text x="15" y="280" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Grade Impact on IF vs VVS1:</text>
      <text x="15" y="298" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">An Internally Flawless (IF) diamond has ZERO internal red inclusions,</text>
      <text x="15" y="314" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">but may have minor external green blemishes (naturals, extra facets).</text>
    </g>
  </g>

  <!-- Bottom 5 Factors Banner -->
  <g transform="translate(50, 560)">
    <rect width="1000" height="105" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="20" y="25" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">THE 5 GIA CLARITY GRADING DETERMINANTS</text>

    <g transform="translate(20, 40)">
      <rect x="0" y="0" width="180" height="50" rx="4" fill="#0F172A"/>
      <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. SIZE</text>
      <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Larger = lower clarity grade.</text>

      <rect x="195" y="0" width="180" height="50" rx="4" fill="#0F172A"/>
      <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. NUMBER</text>
      <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Quantity of visible marks.</text>

      <rect x="390" y="0" width="180" height="50" rx="4" fill="#0F172A"/>
      <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. LOCATION</text>
      <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Under table vs. hidden by prong.</text>

      <rect x="585" y="0" width="180" height="50" rx="4" fill="#0F172A"/>
      <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. RELIEF</text>
      <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">High contrast (black) vs. clear.</text>

      <rect x="780" y="0" width="180" height="50" rx="4" fill="#0F172A"/>
      <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">5. NATURE</text>
      <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Inclusion type &amp; durability risk.</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m05-clarity-inclusion-plotting-symbols.svg", svg_c1_m05)

# c1-m06-colored-stone-top-10-matrix.svg
svg_c1_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 780" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="780" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="776" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#E11D48" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">COLORED GEMSTONES</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Top 10 Colored Stones: Species, Durability &amp; Floor Care</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Counter reference for Mohs hardness, toughness, standard treatments, and cleaning safety.</text>
  </g>

  <!-- Table Header -->
  <g transform="translate(50, 120)">
    <rect width="1000" height="35" rx="6" fill="#1E293B"/>
    <text x="20" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">GEMSTONE</text>
    <text x="180" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">MINERAL SPECIES</text>
    <text x="340" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">MOHS / TOUGHNESS</text>
    <text x="520" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">ROUTINE TREATMENT</text>
    <text x="760" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">CLEANING SAFETY</text>
  </g>

  <!-- Rows -->
  <g transform="translate(50, 160)">
    <!-- 1. Sapphire -->
    <g transform="translate(0, 0)">
      <rect width="1000" height="52" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#2563EB"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Sapphire</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Corundum</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 9 / Excellent</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Heat (routine, stable)</text>
      <text x="760" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11">✔ Ultrasonic &amp; Steam Safe</text>
    </g>

    <!-- 2. Ruby -->
    <g transform="translate(0, 56)">
      <rect width="1000" height="52" rx="4" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#DC2626"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Ruby</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Corundum</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 9 / Excellent</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Heat / Flux (Glass-fill caution)</text>
      <text x="760" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11">✔ Safe (Warm soapy if filled)</text>
    </g>

    <!-- 3. Emerald -->
    <g transform="translate(0, 112)">
      <rect width="1000" height="52" rx="4" fill="#0F172A" stroke="#EF4444" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#059669"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Emerald</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Beryl</text>
      <text x="340" y="30" fill="#EF4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 7.5–8 / Fair–Poor</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Cedarwood Oil / Resin fill</text>
      <text x="760" y="30" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✖ NEVER Ultrasonic / Steam</text>
    </g>

    <!-- 4. Tanzanite -->
    <g transform="translate(0, 168)">
      <rect width="1000" height="52" rx="4" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#4F46E5"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Tanzanite</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Zoisite</text>
      <text x="340" y="30" fill="#F59E0B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 6–7 / Fair</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Routine Heat (brown to violet)</text>
      <text x="760" y="30" fill="#F59E0B" font-family="system-ui, sans-serif" font-size="11">⚠ Warm soapy water only</text>
    </g>

    <!-- 5. Aquamarine -->
    <g transform="translate(0, 224)">
      <rect width="1000" height="52" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#38BDF8"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Aquamarine</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Beryl</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 7.5–8 / Good</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Heat (removes green tint)</text>
      <text x="760" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11">✔ Ultrasonic safe if un-fractured</text>
    </g>

    <!-- 6. Opal -->
    <g transform="translate(0, 280)">
      <rect width="1000" height="52" rx="4" fill="#1E293B" stroke="#EF4444" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#F472B6"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Opal</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Hydrated Silica</text>
      <text x="340" y="30" fill="#EF4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 5.5–6.5 / Poor</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Untreated / Sugar-acid / Smoke</text>
      <text x="760" y="30" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✖ Sensitive to heat &amp; shock</text>
    </g>

    <!-- 7. Tourmaline -->
    <g transform="translate(0, 336)">
      <rect width="1000" height="52" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#10B981"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Tourmaline</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Complex Silicate</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 7–7.5 / Fair</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Heat / Irradiation</text>
      <text x="760" y="30" fill="#F59E0B" font-family="system-ui, sans-serif" font-size="11">⚠ Avoid thermal shock &amp; steam</text>
    </g>

    <!-- 8. Amethyst / Citrine -->
    <g transform="translate(0, 392)">
      <rect width="1000" height="52" rx="4" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#9333EA"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Amethyst / Citrine</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Quartz</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 7 / Good</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Heat (amethyst to citrine)</text>
      <text x="760" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11">✔ Ultrasonic safe</text>
    </g>

    <!-- 9. Peridot -->
    <g transform="translate(0, 448)">
      <rect width="1000" height="52" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#84CC16"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Peridot</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Olivine</text>
      <text x="340" y="30" fill="#F59E0B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 6.5–7 / Fair</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">None (idiochromatic green)</text>
      <text x="760" y="30" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11">✖ Avoid acid, steam, shock</text>
    </g>

    <!-- 10. Garnet -->
    <g transform="translate(0, 504)">
      <rect width="1000" height="52" rx="4" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <circle cx="28" cy="26" r="10" fill="#7F1D1D"/>
      <text x="45" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Garnet (Pyrope/Tsavorite)</text>
      <text x="180" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12">Garnet Group</text>
      <text x="340" y="30" fill="#10B981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mohs 6.5–7.5 / Good</text>
      <text x="520" y="30" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Virtually never treated</text>
      <text x="760" y="30" fill="#34D399" font-family="system-ui, sans-serif" font-size="11">✔ Ultrasonic usually safe</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m06-colored-stone-top-10-matrix.svg", svg_c1_m06)

# c1-m07-pearl-types-and-value-factors.svg
svg_c1_m07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="pearlShine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#CBD5E1"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="700" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="696" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#38BDF8" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#7DD3FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">ORGANIC GEMOLOGY</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Pearl Varieties &amp; GIA 7 Value Factors</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Akoya vs. South Sea vs. Tahitian vs. Freshwater, grading vocabulary, and counter care rules.</text>
  </g>

  <!-- 4 Pearl Types Grid -->
  <g transform="translate(50, 120)">
    <!-- Akoya -->
    <g transform="translate(0, 0)">
      <rect width="235" height="240" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="117" cy="55" r="28" fill="url(#pearlShine)" stroke="#CBD5E1" stroke-width="1"/>
      <text x="117" y="110" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Akoya Pearls</text>
      <text x="117" y="128" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Japan &amp; China | Pinctada fucata</text>

      <text x="15" y="155" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Size:</tspan> 2mm – 10mm (avg 7-8mm)</text>
      <text x="15" y="173" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Luster:</tspan> Sharp, mirror-like gloss</text>
      <text x="15" y="191" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Color:</tspan> White/Cream + Rose overtone</text>
      <text x="15" y="215" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">The classic bridal single strand standard.</text>
    </g>

    <!-- South Sea -->
    <g transform="translate(255, 0)">
      <rect width="235" height="240" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <circle cx="117" cy="55" r="34" fill="#FEF3C7" stroke="#FBBF24" stroke-width="1"/>
      <text x="117" y="110" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">South Sea Pearls</text>
      <text x="117" y="128" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Australia &amp; Indonesia | P. maxima</text>

      <text x="15" y="155" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Size:</tspan> 8mm – 20mm (avg 11-14mm)</text>
      <text x="15" y="173" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Luster:</tspan> Deep, satiny velvety glow</text>
      <text x="15" y="191" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Color:</tspan> White, Silver, Golden</text>
      <text x="15" y="215" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">The "Queen of Pearls" — highest ticket value.</text>
    </g>

    <!-- Tahitian -->
    <g transform="translate(510, 0)">
      <rect width="235" height="240" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <circle cx="117" cy="55" r="32" fill="#1E293B" stroke="#34D399" stroke-width="2"/>
      <circle cx="110" cy="48" r="8" fill="#34D399" fill-opacity="0.3"/>
      <text x="117" y="110" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Tahitian Pearls</text>
      <text x="117" y="128" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">French Polynesia | P. margaritifera</text>

      <text x="15" y="155" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Size:</tspan> 8mm – 18mm (avg 9-12mm)</text>
      <text x="15" y="173" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Luster:</tspan> Metallic, shimmering overtone</text>
      <text x="15" y="191" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Color:</tspan> Peacock green, aubergine, charcoal</text>
      <text x="15" y="215" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Naturally black (never dyed when fine).</text>
    </g>

    <!-- Freshwater -->
    <g transform="translate(765, 0)">
      <rect width="235" height="240" rx="8" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
      <circle cx="117" cy="55" r="26" fill="#FAF5FF" stroke="#C084FC" stroke-width="1"/>
      <text x="117" y="110" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Freshwater Pearls</text>
      <text x="117" y="128" fill="#C084FC" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">China | Hyriopsis cumingii</text>

      <text x="15" y="155" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Size:</tspan> 2mm – 15mm (avg 6-9mm)</text>
      <text x="15" y="173" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Luster:</tspan> Soft, porcelain finish</text>
      <text x="15" y="191" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Structure:</tspan> 100% solid nacre (no bead)</text>
      <text x="15" y="215" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Extreme durability at accessible price points.</text>
    </g>
  </g>

  <!-- Bottom 7 Value Factors + Care -->
  <g transform="translate(50, 390)">
    <rect width="1000" height="270" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1"/>

    <!-- 7 Factors Grid -->
    <g transform="translate(25, 20)">
      <text x="0" y="15" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="14" font-weight="700">GIA 7 PEARL VALUE FACTORS</text>

      <g transform="translate(0, 30)">
        <!-- 1 -->
        <rect x="0" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. SIZE</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Larger diameter</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">exponentially</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">increases value.</text>

        <!-- 2 -->
        <rect x="135" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. SHAPE</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Round &gt; Near-Round</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">&gt; Oval &gt; Drop &gt;</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Button &gt; Baroque.</text>

        <!-- 3 -->
        <rect x="270" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. COLOR</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Bodycolor +</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Overtone +</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Orient (iridescence).</text>

        <!-- 4 -->
        <rect x="405" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. LUSTER</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Most important:</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Excellent (sharp)</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">to Poor (dim/chalky).</text>

        <!-- 5 -->
        <rect x="540" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">5. SURFACE</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Clean to Heavily</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Blemished (pits,</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">bumps, cracks).</text>

        <!-- 6 -->
        <rect x="675" y="0" width="125" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">6. NACRE</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Thickness &amp;</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">quality. Thin</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">nacre blinks bead.</text>

        <!-- 7 -->
        <rect x="810" y="0" width="135" height="90" rx="6" fill="#0F172A"/>
        <text x="10" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">7. MATCHING</text>
        <text x="10" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Uniformity of size,</text>
        <text x="10" y="58" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">color &amp; luster</text>
        <text x="10" y="74" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">across full strand.</text>
      </g>
    </g>

    <!-- Floor Care & Handling Rule -->
    <g transform="translate(25, 160)">
      <rect width="950" height="85" rx="6" fill="#0F172A" stroke="#E11D48" stroke-width="1"/>
      <text x="20" y="24" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">FLOOR CLIENT CARE MANTRA: "LAST THING ON, FIRST THING OFF"</text>
      <text x="20" y="46" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Organic calcium carbonate (aragonite) has Mohs 2.5–4.0 hardness. Easily dissolved by perfumes, hairspray, acids, and chlorine.</text>
      <text x="20" y="66" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Clean ONLY with damp soft cloth. Store flat in chamois pouch (never hang on hook; silk threads stretch). Restring every 12–24 months.</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m07-pearl-types-and-value-factors.svg", svg_c1_m07)

# c1-m08-precious-metals-hallmarks.svg
svg_c1_m08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
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
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#EAB308" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">METALLURGY &amp; MARKS</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Precious Metals, Alloys &amp; Hallmark Standards</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Gold karatage, Platinum vs. White Gold trade-offs, and international stamp identification.</text>
  </g>

  <!-- Metals Comparison Columns -->
  <g transform="translate(50, 120)">
    <!-- 1. Gold Karatage -->
    <g transform="translate(0, 0)">
      <rect width="310" height="380" rx="8" fill="#1E293B" stroke="#EAB308" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#EAB308" fill-opacity="0.2"/>
      <text x="155" y="38" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">GOLD KARATAGE &amp; PURITY</text>

      <g transform="translate(20, 65)">
        <text x="0" y="18" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">24K (Fineness 999 / 99.9%)</text>
        <text x="0" y="34" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Pure gold. Very soft, easily deformed; standard in Asia/India.</text>

        <text x="0" y="60" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="12" font-weight="700">18K (Fineness 750 / 75.0%)</text>
        <text x="0" y="76" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">18 parts gold, 6 parts alloy. Luxury maison standard; rich color.</text>

        <text x="0" y="102" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">14K (Fineness 585 / 58.5%)</text>
        <text x="0" y="118" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">14 parts gold, 10 parts alloy. US bridal workhorse; high durability.</text>

        <text x="0" y="144" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">10K (Fineness 417 / 41.7%)</text>
        <text x="0" y="160" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Legal minimum in US to be called gold. Very hard, highly alloyed.</text>

        <rect x="-5" y="185" width="280" height="110" rx="6" fill="#0F172A"/>
        <text x="10" y="205" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Gold Color Recipes:</text>
        <text x="10" y="225" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#EAB308">Yellow Gold:</tspan> Gold + Copper + Silver</text>
        <text x="10" y="243" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#F87171">Rose Gold:</tspan> Gold + Copper (75% Au / 25% Cu)</text>
        <text x="10" y="261" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#E2E8F0">White Gold:</tspan> Gold + Nickel/Palladium + Rhodium</text>
      </g>
    </g>

    <!-- 2. Platinum vs White Gold -->
    <g transform="translate(345, 0)">
      <rect width="310" height="380" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#0284C7" fill-opacity="0.2"/>
      <text x="155" y="38" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">PLATINUM (PT950 / PT900)</text>

      <g transform="translate(20, 65)">
        <text x="0" y="18" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Properties &amp; Metallurgy</text>
        <text x="0" y="36" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 90–95% pure elemental platinum</text>
        <text x="0" y="54" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 60% denser than 14k gold (heavy heft)</text>
        <text x="0" y="72" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 100% naturally white (no plating)</text>
        <text x="0" y="90" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Hypoallergenic (ideal for sensitive skin)</text>

        <line x1="0" y1="110" x2="270" y2="110" stroke="#334155" stroke-width="1"/>

        <text x="0" y="130" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Patina vs. Gold Metal Loss</text>
        <text x="0" y="150" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">When gold scratches, metal is scraped away. When platinum scratches, metal merely displaces (patina), which can be burnished back without losing mass.</text>

        <rect x="-5" y="185" width="280" height="110" rx="6" fill="#0F172A"/>
        <text x="10" y="205" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Counter Script on Re-plating:</text>
        <text x="10" y="225" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"White gold is yellow gold bleached with alloys</text>
        <text x="10" y="241" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">and rhodium plated; it needs re-dipping.</text>
        <text x="10" y="257" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Platinum is naturally white forever and never</text>
        <text x="10" y="273" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">changes color."</text>
      </g>
    </g>

    <!-- 3. Sterling Silver & Alternative Metals -->
    <g transform="translate(690, 0)">
      <rect width="310" height="380" rx="8" fill="#1E293B" stroke="#94A3B8" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#64748B" fill-opacity="0.3"/>
      <text x="155" y="38" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">STERLING &amp; CONTEMPORARY</text>

      <g transform="translate(20, 65)">
        <text x="0" y="18" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Sterling Silver 925</text>
        <text x="0" y="36" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• 92.5% silver, 7.5% copper</text>
        <text x="0" y="54" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Tarnishes from sulfur exposure (Ag2S)</text>
        <text x="0" y="72" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Soft: Mohs 2.5–3.0 (fashion, not bridal)</text>

        <line x1="0" y1="95" x2="270" y2="95" stroke="#334155" stroke-width="1"/>

        <text x="0" y="115" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Men's Contemporary Metals</text>
        <text x="0" y="133" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#FFFFFF">Titanium:</tspan> Lightweight, hard, cannot resize</text>
        <text x="0" y="151" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#FFFFFF">Tungsten Carbide:</tspan> Scratch-proof, brittle (shatters under impact), cannot resize</text>
        <text x="0" y="169" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#FFFFFF">Tantalum / Cobalt:</tspan> Dense, shatter-resistant</text>

        <rect x="-5" y="185" width="280" height="110" rx="6" fill="#0F172A"/>
        <text x="10" y="205" fill="#F87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Crucial Resizing Warning:</text>
        <text x="10" y="225" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Always inform clients buying Tungsten,</text>
        <text x="10" y="241" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Titanium, or Carbon Fiber that the ring</text>
        <text x="10" y="257" fill="#EF4444" font-family="system-ui, sans-serif" font-size="10">CANNOT BE RESIZED on the jeweler's bench;</text>
        <text x="10" y="273" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">it must be fully replaced if size changes.</text>
      </g>
    </g>
  </g>

  <!-- International Hallmarks Bar -->
  <g transform="translate(50, 520)">
    <rect width="1000" height="145" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="25" y="28" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">INTERNATIONAL HALLMARK RECOGNITION GUIDE</text>

    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="220" height="75" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">United States (FTC)</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Karat mark + Maker's Trademark</text>
      <text x="15" y="58" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">e.g., "14K", "18K", "PLAT"</text>

      <rect x="245" y="0" width="220" height="75" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">United Kingdom (Assay)</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Sponsor + Fineness + Town + Year</text>
      <text x="15" y="58" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">e.g., 750 (Crown), Anchor (Bham)</text>

      <rect x="490" y="0" width="220" height="75" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">European Millesimal</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Pure parts per 1,000</text>
      <text x="15" y="58" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">375 (9K), 585 (14K), 750 (18K), 950 (Pt)</text>

      <rect x="735" y="0" width="220" height="75" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">BIS Hallmark (India)</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">BIS Logo + Karat/Fineness (22K916)</text>
      <text x="15" y="58" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">+ 6-digit alphanumeric HUID code</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C1-diamond-gemstone-fluency/assets/c1-m08-precious-metals-hallmarks.svg", svg_c1_m08)

print("All C1 SVGs created successfully!")
