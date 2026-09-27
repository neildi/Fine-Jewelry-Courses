import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# c4-m01-dual-custody-opening-closing-sop.svg
svg_c4_m01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#DC2626" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">LOSS PREVENTION SOP</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Dual-Custody Store Opening &amp; Closing Protocol</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Standard insurer-mandated opening/closing sequence, all-clear signals, and vault protocols.</text>
  </g>

  <!-- Flowchart Columns: Opening vs. Closing -->
  <g transform="translate(50, 125)">
    <!-- Column 1: Opening SOP -->
    <g transform="translate(0, 0)">
      <rect width="480" height="420" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="450" height="35" rx="6" fill="#0284C7" fill-opacity="0.3"/>
      <text x="240" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">STORE OPENING: 4-PHASE SEQUENCE</text>

      <g transform="translate(20, 65)">
        <!-- Phase 1 -->
        <g transform="translate(0, 0)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
          <text x="15" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Perimeter &amp; Vehicle Check (2 Persons Minimum)</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Staff A enters vehicle standoff position; Staff B checks exterior locks &amp; cameras.</text>
        </g>

        <!-- Phase 2 -->
        <g transform="translate(0, 50)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
          <text x="15" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Primary Entry &amp; Interior Sweep</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Staff B enters, relocks front door immediately, disarms alarm within window.</text>
        </g>

        <!-- Phase 3 -->
        <g transform="translate(0, 100)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
          <text x="15" y="20" fill="#10B981" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
          <text x="35" y="14" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">The "All-Clear" Signal (Window Blind / Object)</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Staff B sets physical all-clear signal. Staff A enters only after signal is confirmed.</text>
        </g>

        <!-- Phase 4 -->
        <g transform="translate(0, 150)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
          <text x="15" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Dual-Combination Safe Opening &amp; Setup</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Staff A &amp; B each enter independent halves of safe combination; transfer trays to case.</text>
        </g>

        <rect x="0" y="210" width="440" height="75" rx="6" fill="#0F172A"/>
        <text x="15" y="230" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">STRICT OPENING MANDATE:</text>
        <text x="15" y="248" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">NEVER open a jewelry store alone. If partner has not arrived,</text>
        <text x="15" y="264" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">remain locked inside your vehicle with windows up and notify manager.</text>
      </g>
    </g>

    <!-- Column 2: Closing SOP -->
    <g transform="translate(520, 0)">
      <rect width="480" height="420" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="450" height="35" rx="6" fill="#D97706" fill-opacity="0.3"/>
      <text x="240" y="38" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">STORE CLOSING: 4-PHASE SEQUENCE</text>

      <g transform="translate(20, 65)">
        <!-- Phase 1 -->
        <g transform="translate(0, 0)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="15" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Threshold Lock at Closing Minute</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Lock front doors promptly at scheduled closing. No new clients admitted.</text>
        </g>

        <!-- Phase 2 -->
        <g transform="translate(0, 50)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="15" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Showcase Pull &amp; Tray Stacking</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Trays loaded onto rolling carts under dual supervision; transfer to vault.</text>
        </g>

        <!-- Phase 3 -->
        <g transform="translate(0, 100)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="15" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Nightly Piece Count &amp; Safe Lock Down</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Verify high-value showcase count matches POS perpetual inventory report.</text>
        </g>

        <!-- Phase 4 -->
        <g transform="translate(0, 150)">
          <circle cx="15" cy="15" r="12" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="15" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4</text>
          <text x="35" y="14" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Alarm Arming &amp; Synchronized Exit</text>
          <text x="35" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Both associates exit together, scan parking lot, and depart simultaneously.</text>
        </g>

        <rect x="0" y="210" width="440" height="75" rx="6" fill="#0F172A"/>
        <text x="15" y="230" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">EMPTY SHOWCASE RULE:</text>
        <text x="15" y="248" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Leave showcase doors slightly unlocked and open after pull;</text>
        <text x="15" y="264" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">proves to after-hours burglars that cases are 100% empty, preventing smashed glass.</text>
      </g>
    </g>
  </g>

  <!-- Bottom Alarm Response Rule -->
  <g transform="translate(50, 560)">
    <rect width="1000" height="95" rx="8" fill="#1E293B" stroke="#EF4444" stroke-width="1"/>
    <text x="25" y="25" fill="#EF4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">AFTER-HOURS ALARM RESPONSE DIRECTIVE</text>
    <text x="25" y="48" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• NEVER enter a store alone during an after-hours alarm call. Wait in your locked vehicle across the street until police arrive.</text>
    <text x="25" y="68" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• If police clear the building, two store associates must enter together to inspect safes and reset alarm systems.</text>
  </g>
</svg>"""

save_svg("courses/C4-store-security-loss-prevention/assets/c4-m01-dual-custody-opening-closing-sop.svg", svg_c4_m01)

# c4-m06-form-8300-cash-compliance-tree.svg
svg_c4_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <text x="95" y="16" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">IRS &amp; FINCEN COMPLIANCE</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">IRS Form 8300 Cash Compliance Decision Tree</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Reporting cash payments over $10,000, 24-hour aggregation rules, and anti-structuring prohibitions.</text>
  </g>

  <!-- Decision Tree Flow -->
  <g transform="translate(50, 125)">
    <!-- Root Trigger -->
    <g transform="translate(340, 0)">
      <rect width="320" height="70" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="2"/>
      <text x="160" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Payment Received at Counter</text>
      <text x="160" y="50" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Cash, Cashier's Check, Traveler's Checks, Money Orders</text>
    </g>

    <!-- Branch 1: Under $10k -->
    <g transform="translate(40, 110)">
      <line x1="450" y1="-40" x2="160" y2="0" stroke="#94A3B8" stroke-width="1.5"/>
      <rect width="280" height="220" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <rect x="15" y="15" width="250" height="30" rx="4" fill="#059669" fill-opacity="0.3"/>
      <text x="140" y="35" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TOTAL CASH ≤ $10,000</text>

      <g transform="translate(15, 60)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Standard POS Processing:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Complete regular sales receipt</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Log standard client profile</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• No Form 8300 required</text>

        <rect x="0" y="90" width="250" height="55" rx="4" fill="#0F172A"/>
        <text x="10" y="110" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">WATCH FOR 24-HR RULE:</text>
        <text x="10" y="126" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9">If client pays $6,000 today &amp; $5,000</text>
        <text x="10" y="138" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9">tomorrow for same item, Form 8300 TRIGGERS.</text>
      </g>
    </g>

    <!-- Branch 2: Over $10,000 in Cash -->
    <g transform="translate(360, 110)">
      <line x1="140" y1="-40" x2="140" y2="0" stroke="#EF4444" stroke-width="2"/>
      <rect width="280" height="220" rx="8" fill="#1E293B" stroke="#EF4444" stroke-width="1.5"/>
      <rect x="15" y="15" width="250" height="30" rx="4" fill="#991B1B" fill-opacity="0.4"/>
      <text x="140" y="35" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TOTAL CASH &gt; $10,000</text>

      <g transform="translate(15, 60)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">MANDATORY FORM 8300:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Collect Government Photo ID</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Collect SSN / ITIN / Passport #</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Record Employer &amp; Occupation</text>

        <rect x="0" y="90" width="250" height="55" rx="4" fill="#0F172A"/>
        <text x="10" y="110" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">15-DAY FILING CLOCK:</text>
        <text x="10" y="126" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="9">Store leadership must e-file with</text>
        <text x="10" y="138" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="9">FinCEN BSA E-Filing within 15 days.</text>
      </g>
    </g>

    <!-- Branch 3: Structuring Suspected -->
    <g transform="translate(680, 110)">
      <line x1="-180" y1="-40" x2="140" y2="0" stroke="#F59E0B" stroke-width="1.5"/>
      <rect width="280" height="220" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="250" height="30" rx="4" fill="#D97706" fill-opacity="0.3"/>
      <text x="140" y="35" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SUSPICIOUS / STRUCTURING</text>

      <g transform="translate(15, 60)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Structuring Red Flags:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Client pays $9,900 to avoid ID</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Asks to split onto multiple fake names</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Cancels sale when Form 8300 mentioned</text>

        <rect x="0" y="90" width="250" height="55" rx="4" fill="#0F172A"/>
        <text x="10" y="110" fill="#EF4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700">STRICT LAW: NO TIPPING OFF</text>
        <text x="10" y="126" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="9">File Form 8300 Box 1b (Suspicious).</text>
        <text x="10" y="138" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="9">Never advise client on how to avoid it.</text>
      </g>
    </g>
  </g>

  <!-- Bottom Regulatory Warning -->
  <g transform="translate(50, 520)">
    <rect width="1000" height="135" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="25" y="28" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">WHAT IS "CASH" UNDER FEDERAL LAW?</text>

    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="300" height="70" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">INCLUDED AS CASH (Form 8300):</text>
      <text x="15" y="40" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• U.S. and Foreign Currency Bills</text>
      <text x="15" y="56" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Cashier's Checks / Bank Drafts &lt; $10k face</text>

      <rect x="325" y="0" width="300" height="70" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">NOT CASH (Exempt from Form 8300):</text>
      <text x="15" y="40" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Personal Checks (any amount)</text>
      <text x="15" y="56" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">• Credit Cards / Debit Cards / Wire Transfers</text>

      <rect x="650" y="0" width="300" height="70" rx="4" fill="#0F172A"/>
      <text x="15" y="22" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">PENALTIES FOR NON-COMPLIANCE:</text>
      <text x="15" y="40" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="10">• Civil fines up to $25,000+ per violation</text>
      <text x="15" y="56" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="10">• Criminal structuring charges for staff</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C4-store-security-loss-prevention/assets/c4-m06-form-8300-cash-compliance-tree.svg", svg_c4_m06)

print("Course C4 SVGs generated!")
