import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# c8-m02-jewelry-intake-condition-map.svg
svg_c8_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%">
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
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#0284C7" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#7DD3FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">BENCH INTAKE PROTOCOL</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Jewelry Intake Condition Mapping Template</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Documenting pre-existing flaws, loose stones, worn prongs, and thin shanks under 10x magnification.</text>
  </g>

  <!-- Left: Annotated Ring Inspection Canvas -->
  <g transform="translate(50, 125)">
    <rect width="520" height="535" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="15" y="15" width="490" height="35" rx="6" fill="#0284C7" fill-opacity="0.3"/>
    <text x="260" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SOLITAIRE &amp; PAVÉ INTAKE SCHEMATIC</text>

    <!-- Ring Drawing -->
    <g transform="translate(160, 80)">
      <!-- Shank Outer & Inner Circle -->
      <circle cx="100" cy="180" r="100" fill="none" stroke="#64748B" stroke-width="12"/>
      <circle cx="100" cy="180" r="88" fill="#0F172A" stroke="#475569" stroke-width="1.5"/>

      <!-- Head / Crown Setting -->
      <polygon points="65,80 135,80 150,30 50,30" fill="#1E293B" stroke="#94A3B8" stroke-width="2"/>

      <!-- Center Diamond Silhouette -->
      <polygon points="70,30 130,30 145,5 55,5" fill="#E2E8F0" stroke="#38BDF8" stroke-width="1.5"/>
      <polygon points="55,5 145,5 100,-25" fill="#F8FAFC" stroke="#38BDF8" stroke-width="1.5"/>

      <!-- 4 Prongs -->
      <circle cx="58" cy="5" r="5" fill="#FBBF24" stroke="#0F172A" stroke-width="1"/>
      <circle cx="142" cy="5" r="5" fill="#EF4444" stroke="#0F172A" stroke-width="1"/>
      <circle cx="70" cy="28" r="4" fill="#FBBF24" stroke="#0F172A" stroke-width="1"/>
      <circle cx="130" cy="28" r="4" fill="#FBBF24" stroke="#0F172A" stroke-width="1"/>

      <!-- Pavé Side Stones on Shoulders -->
      <circle cx="35" cy="115" r="5" fill="#E2E8F0" stroke="#64748B"/>
      <circle cx="20" cy="135" r="5" fill="#EF4444" stroke="#0F172A"/> <!-- Missing stone -->
      <circle cx="12" cy="160" r="5" fill="#E2E8F0" stroke="#64748B"/>

      <circle cx="165" cy="115" r="5" fill="#E2E8F0" stroke="#64748B"/>
      <circle cx="180" cy="135" r="5" fill="#E2E8F0" stroke="#64748B"/>
      <circle cx="188" cy="160" r="5" fill="#E2E8F0" stroke="#64748B"/>

      <!-- Bottom Shank Thinning -->
      <path d="M 90,274 L 110,274" stroke="#EF4444" stroke-width="6"/>

      <!-- Callout Pointers -->
      <!-- Center Stone Chip -->
      <line x1="145" y1="5" x2="220" y2="-10" stroke="#EF4444" stroke-width="1.5"/>
      <rect x="225" y="-22" width="125" height="24" rx="4" fill="#0F172A" stroke="#EF4444" stroke-width="1"/>
      <text x="232" y="-6" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Girdle Chip on Stone</text>

      <!-- Worn Prong -->
      <line x1="142" y1="5" x2="220" y2="25" stroke="#FBBF24" stroke-width="1.5"/>
      <rect x="225" y="15" width="125" height="24" rx="4" fill="#0F172A" stroke="#FBBF24" stroke-width="1"/>
      <text x="232" y="31" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Prong Worn Thin (Retip)</text>

      <!-- Missing Side Stone -->
      <line x1="20" y1="135" x2="-80" y2="135" stroke="#EF4444" stroke-width="1.5"/>
      <rect x="-195" y="123" width="110" height="24" rx="4" fill="#0F172A" stroke="#EF4444" stroke-width="1"/>
      <text x="-188" y="139" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. 1 Missing Accent CZ</text>

      <!-- Shank Thinning -->
      <line x1="100" y1="274" x2="100" y2="330" stroke="#EF4444" stroke-width="1.5"/>
      <rect x="40" y="335" width="120" height="24" rx="4" fill="#0F172A" stroke="#EF4444" stroke-width="1"/>
      <text x="48" y="351" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Shank Worn &lt; 0.8mm</text>
    </g>

    <!-- Disclaimer Footer -->
    <g transform="translate(15, 450)">
      <rect width="490" height="70" rx="6" fill="#0F172A"/>
      <text x="15" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Client Sign-Off Rule (Before Work Begins):</text>
      <text x="15" y="40" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Always show every marked flaw to the client through a 10x microscope or digital screen</text>
      <text x="15" y="56" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">BEFORE they leave the counter to prevent post-repair liability claims.</text>
    </g>
  </g>

  <!-- Right: 6-Point Intake SOP & Disclaimer -->
  <g transform="translate(600, 125)">
    <!-- Checklist Card -->
    <rect width="450" height="535" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <rect x="15" y="15" width="420" height="35" rx="6" fill="#0F172A"/>
    <text x="225" y="38" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">MANDATORY 6-POINT INTAKE CHECKLIST</text>

    <g transform="translate(25, 70)">
      <!-- Check 1 -->
      <rect x="0" y="0" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Stone Tightness Test</text>
      <text x="28" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Gently tap girdle with brass probe under 10x loupe. Check rattle.</text>

      <!-- Check 2 -->
      <rect x="0" y="45" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="59" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="59" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Laser Inscription / Plot Verification</text>
      <text x="28" y="73" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Read GIA report number on girdle and log onto job envelope.</text>

      <!-- Check 3 -->
      <rect x="0" y="90" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="104" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="104" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Metal Karat &amp; Hallmark Identification</text>
      <text x="28" y="118" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Confirm 14K / 18K / PT950 / 925 stamp. Note if unmarked or plated.</text>

      <!-- Check 4 -->
      <rect x="0" y="135" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="149" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="149" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Fragile Stone &amp; Treatment Warning</text>
      <text x="28" y="163" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Flag emeralds, opals, tanzanite, or pearls. Require bench torch caution.</text>

      <!-- Check 5 -->
      <rect x="0" y="180" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="194" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="194" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Exact Gram Weight &amp; Dimensions</text>
      <text x="28" y="208" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Weigh piece on certified scale (e.g. 4.32g) in front of client.</text>

      <!-- Check 6 -->
      <rect x="0" y="225" width="18" height="18" rx="3" fill="#10B981"/>
      <text x="9" y="239" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✓</text>
      <text x="28" y="239" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">6. High-Res Macro Photography</text>
      <text x="28" y="253" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Take 3 photos (Top, Side, Hallmark) and attach directly to POS job ticket.</text>

      <!-- Counter Script -->
      <rect x="-10" y="280" width="420" height="155" rx="6" fill="#0F172A"/>
      <text x="5" y="302" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Counter Script During Condition Mapping:</text>
      <text x="5" y="324" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Let's put this under our digital microscope together.</text>
      <text x="5" y="340" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">See right here on the northwest prong? The gold has worn</text>
      <text x="5" y="356" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">down to paper thickness. While we have it in for sizing,</text>
      <text x="5" y="372" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">our jeweler should retip all 4 prongs to keep your diamond</text>
      <text x="5" y="388" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">100% secure."</text>
      <text x="5" y="415" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Converts routine intake into protective high-margin repair add-on.</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C8-custom-design-repair-workflow/assets/c8-m02-jewelry-intake-condition-map.svg", svg_c8_m02)

# c8-m03-cad-to-casting-7-stage-pipeline.svg
svg_c8_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#8B5CF6" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#C4B5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">CUSTOM PIPELINE</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">The 7-Stage CAD-to-Casting Custom Workflow</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Standard timeline, milestone client approvals, and bench production steps from sketch to finished piece.</text>
  </g>

  <!-- 7 Pipeline Stages -->
  <g transform="translate(50, 125)">
    <!-- Stage 1 -->
    <g transform="translate(0, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#0284C7"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
      <text x="45" y="28" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Concept &amp; Sketch</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 1–3</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Client discovery</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Hand sketch / mood</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Center stone select</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• 50% deposit taken</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">GATE 1:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Deposit &amp; rough sketch sign-off.</text>
    </g>

    <!-- Stage 2 -->
    <g transform="translate(145, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#0284C7"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
      <text x="45" y="28" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3D CAD Model</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 4–7</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Matrix / Rhino build</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Shrinkage tolerance</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Stone seat recesses</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Metal weight calc</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">TECHNICAL:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Allow 1.5% casting scale factor.</text>
    </g>

    <!-- Stage 3 -->
    <g transform="translate(290, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#D97706"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
      <text x="45" y="28" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Render Approval</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 8–10</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• 360° photo render</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Client review meeting</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Minor CAD tweaks</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Final aesthetic sign</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">GATE 2:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Written CAD sign-off prevents remakes.</text>
    </g>

    <!-- Stage 4 -->
    <g transform="translate(435, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#059669"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4</text>
      <text x="45" y="28" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3D Wax CAM Print</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 11–13</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• High-res resin/wax</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• In-store try-on option</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Finger fit check</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Tree sprue gating</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#34D399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">TACTILE:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Wax model confirms profile height.</text>
    </g>

    <!-- Stage 5 -->
    <g transform="translate(580, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#DC2626"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">5</text>
      <text x="45" y="28" fill="#F87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Lost-Wax Casting</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 14–16</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Investment plaster</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Burnout oven cycle</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Vacuum/Centrifuge</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Quench &amp; pickle</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#F87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">FOUNDRY:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Gold/Pt metal poured into cavity.</text>
    </g>

    <!-- Stage 6 -->
    <g transform="translate(725, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="12" fill="#7E22CE"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">6</text>
      <text x="45" y="28" fill="#C084FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Setting &amp; Polish</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 17–20</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Sprue cut &amp; clean</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Microscope setting</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Magnetic tumble</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• High-luster rouge</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#C084FC" font-family="system-ui, sans-serif" font-size="9" font-weight="700">BENCH CRAFT:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Prongs cut, burred, and tightened.</text>
    </g>

    <!-- Stage 7 -->
    <g transform="translate(870, 0)">
      <rect width="130" height="260" rx="6" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
      <circle cx="25" cy="25" r="12" fill="#10B981"/>
      <text x="25" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">7</text>
      <text x="45" y="28" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">10-Point QC Delivery</text>
      <text x="12" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Day 21 (Final)</text>
      <text x="12" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Full QC audit check</text>
      <text x="12" y="98" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Final appraisal doc</text>
      <text x="12" y="116" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Luxury reveal box</text>
      <text x="12" y="134" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">• Balance collected</text>
      <rect x="8" y="180" width="114" height="65" rx="4" fill="#0F172A"/>
      <text x="14" y="200" fill="#34D399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">DELIVERY:</text>
      <text x="14" y="215" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="8">Celebratory client hand-off reveal.</text>
    </g>
  </g>

  <!-- Bottom Timeline & Margin Summary -->
  <g transform="translate(50, 420)">
    <rect width="1000" height="230" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="25" y="28" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">CUSTOM DESIGN BENCHMARKS &amp; MARGIN RULES</text>

    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="300" height="160" rx="6" fill="#0F172A"/>
      <text x="15" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Typical Turnaround Time:</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Standard Custom Build: <tspan font-weight="700" fill="#FFFFFF">3 to 4 Weeks</tspan></text>
      <text x="15" y="60" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Rush Production: <tspan font-weight="700" fill="#FFFFFF">10 to 14 Days (+25% fee)</tspan></text>
      <text x="15" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Under-promise and over-deliver: Quote 4 weeks,</text>
      <text x="15" y="96" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">deliver in 21 days for maximum client delight.</text>

      <rect x="325" y="0" width="300" height="160" rx="6" fill="#0F172A"/>
      <text x="15" y="22" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Financial &amp; Margin Target:</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Gross Margin Target: <tspan font-weight="700" fill="#FFFFFF">55% to 65%</tspan></text>
      <text x="15" y="60" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Non-refundable deposit: <tspan font-weight="700" fill="#FFFFFF">50% upfront</tspan></text>
      <text x="15" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Deposit covers 100% of raw metal and</text>
      <text x="15" y="96" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">casting costs, rendering the job zero-risk.</text>

      <rect x="650" y="0" width="300" height="160" rx="6" fill="#0F172A"/>
      <text x="15" y="22" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Heirloom Stone Liability:</text>
      <text x="15" y="42" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Always unmount client stone together</text>
      <text x="15" y="60" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Inspect hidden girdle flaws under prongs</text>
      <text x="15" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Require signed stone reset disclaimer</text>
      <text x="15" y="96" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">before resetting fragile emeralds or tanzanites.</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C8-custom-design-repair-workflow/assets/c8-m03-cad-to-casting-7-stage-pipeline.svg", svg_c8_m03)

print("Course C8 SVGs generated!")
