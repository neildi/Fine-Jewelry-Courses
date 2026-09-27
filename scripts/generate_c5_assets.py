import os

def write_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath}")

# C5 M01: Retail Installment Credit Mechanics
c5_m01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Consumer Jewelry Financing: Installment Credit &amp; Cash Flow Engine</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Understanding how third-party retail credit operates, merchant discount rates (MDR), and cash settlement</text>

  <!-- 3-Party Architecture Map -->
  <g transform="translate(50, 100)">
    <!-- 1. The Client -->
    <rect x="0" y="0" width="280" height="220" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="36" rx="8" fill="#1E293B"/>
    <text x="20" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">1. CLIENT (Borrower)</text>
    <text x="20" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Selects $8,500 Engagement Ring</text>
    <text x="20" y="80" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Applies for 12-Mo Promo Plan</text>
    <text x="20" y="100" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Receives instant credit line</text>
    <text x="20" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Monthly Payment: $708.33/mo</text>
    <text x="20" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Interest if on time: 0% APR</text>
    <text x="20" y="180" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Key Benefit: Immediate Ring Walkout</text>

    <!-- Center Arrow 1 -->
    <path d="M 290 110 L 350 110" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- 2. The Jewelry Store -->
    <rect x="360" y="0" width="280" height="220" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="360" y="0" width="280" height="36" rx="8" fill="#1E293B"/>
    <text x="380" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#10B981">2. RETAILER (Storefront)</text>
    <text x="380" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Delivers merchandise to client</text>
    <text x="380" y="80" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Receives bank settlement in 48h</text>
    <text x="380" y="100" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Absorbs MDR Fee (e.g. 4.5%)</text>
    <text x="380" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Net Bank Deposit: $8,117.50</text>
    <text x="380" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Credit Default Risk: 0% (Bank held)</text>
    <text x="380" y="180" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Key Benefit: Zero Bad Debt Risk</text>

    <!-- Center Arrow 2 -->
    <path d="M 650 110 L 710 110" stroke="#10B981" stroke-width="2"/>

    <!-- 3. The Financial Institution -->
    <rect x="720" y="0" width="280" height="220" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="720" y="0" width="280" height="36" rx="8" fill="#1E293B"/>
    <text x="740" y="24" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F59E0B">3. LENDER (Bank / FinTech)</text>
    <text x="740" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Underwrites credit score/income</text>
    <text x="740" y="80" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Funds the retailer upfront</text>
    <text x="740" y="100" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">• Manages monthly collections</text>
    <text x="740" y="130" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Revenue: MDR fee + revolving interest</text>
    <text x="740" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">Default Risk: Borne 100% by lender</text>
    <text x="740" y="180" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Key Benefit: Scalable Underwriting</text>
  </g>

  <!-- Comparison of Credit Types -->
  <g transform="translate(50, 350)">
    <rect x="0" y="0" width="1000" height="280" rx="8" fill="#161B22" stroke="#334155"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="15" font-weight="bold" fill="#F3F4F6">REVOLVING STORE CARD vs. EQUAL-PAY PROMOTIONAL INSTALLMENTS</text>
    
    <g transform="translate(20, 50)">
      <!-- Feature Header -->
      <rect x="0" y="0" width="960" height="30" fill="#1E293B"/>
      <text x="15" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#94A3B8">FINANCING ATTRIBUTE</text>
      <text x="280" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">REVOLVING STORE CARD (e.g. Synchrony/Wells)</text>
      <text x="630" y="20" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#10B981">EQUAL PAYMENT INSTALLMENTS (0% APR)</text>

      <!-- Row 1 -->
      <rect x="0" y="32" width="960" height="36" fill="#0F172A"/>
      <text x="15" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Credit Structure</text>
      <text x="280" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Open-end revolving line of credit (reuse for future)</text>
      <text x="630" y="55" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Closed-end fixed term installment (12, 24, 36 mo)</text>

      <!-- Row 2 -->
      <rect x="0" y="70" width="960" height="36" fill="#161B22"/>
      <text x="15" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Deferred vs. True 0%</text>
      <text x="280" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FCA5A5">⚠️ Deferred Interest (retroactive interest if missed)</text>
      <text x="630" y="93" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">✓ True Equal Pay (Fixed equal monthly principal)</text>

      <!-- Row 3 -->
      <rect x="0" y="108" width="960" height="36" fill="#0F172A"/>
      <text x="15" y="131" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Floor Disclosure Mandate</text>
      <text x="280" y="131" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Must explain min monthly pay ≠ payoff amount</text>
      <text x="630" y="131" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Monthly payment exactly pays off total balance</text>

      <!-- Row 4 -->
      <rect x="0" y="146" width="960" height="36" fill="#161B22"/>
      <text x="15" y="169" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Average Retailer Cost</text>
      <text x="280" y="169" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">1.5% to 3.5% Merchant Fee</text>
      <text x="630" y="169" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">4.0% to 7.5% Merchant Fee (subsidized rate)</text>

      <!-- Row 5 -->
      <rect x="0" y="184" width="960" height="36" fill="#0F172A"/>
      <text x="15" y="207" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">Best Client Fit</text>
      <text x="280" y="207" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#38BDF8">Ongoing repeat jewelry collectors &amp; anniversary gifts</text>
      <text x="630" y="207" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#10B981">One-time bridal engagement ring buyers wanting budget ease</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m01-retail-installment-financing-flow.svg", c5_m01)

# C5 M02: POS Financing Application SOP
c5_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Point-of-Sale Financing Protocol: Privacy &amp; Compliance SOP</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">The 5-step discreet, dignified process for executing credit applications at the counter without awkwardness</text>

  <!-- 5-Step Process Flow -->
  <g transform="translate(50, 100)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="185" height="260" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="92" cy="35" r="18" fill="#38BDF8"/>
    <text x="92" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">1</text>
    <text x="92" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Discreet Bridge</text>
    <text x="15" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Introduce financing as a</text>
    <text x="15" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  standard smart cash flow</text>
    <text x="15" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  management tool.</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Never assume inability to pay</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Offer 0% promo option</text>
    <text x="15" y="230" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Tone: Dignified &amp; Normal</text>

    <!-- Step 2 -->
    <rect x="205" y="0" width="185" height="260" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="297" cy="35" r="18" fill="#10B981"/>
    <text x="297" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">2</text>
    <text x="297" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Tablet Hand-Off</text>
    <text x="220" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Hand sanitized tablet</text>
    <text x="220" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  directly to client.</text>
    <text x="220" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Never ask for SSN or</text>
    <text x="220" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  income aloud across floor.</text>
    <text x="220" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Step back 3 paces for</text>
    <text x="220" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  complete visual privacy.</text>
    <text x="220" y="245" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Privacy: Strict Compliance</text>

    <!-- Step 3 -->
    <rect x="410" y="0" width="185" height="260" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="502" cy="35" r="18" fill="#F59E0B"/>
    <text x="502" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">3</text>
    <text x="502" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Prequalification</text>
    <text x="425" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Run Soft Credit Pull</text>
    <text x="425" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  first (no score impact).</text>
    <text x="425" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Display approved credit</text>
    <text x="425" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  limit to client privately.</text>
    <text x="425" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Client formally accepts</text>
    <text x="425" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">  prior to hard pull submit.</text>
    <text x="425" y="245" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Underwriting: Instant 30s</text>

    <!-- Step 4 -->
    <rect x="615" y="0" width="185" height="260" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <circle cx="707" cy="35" r="18" fill="#EC4899"/>
    <text x="707" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">4</text>
    <text x="707" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Disclosure Terms</text>
    <text x="630" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• State Truth-in-Lending</text>
    <text x="630" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  terms clearly.</text>
    <text x="630" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Clarify monthly due date,</text>
    <text x="630" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  promo period end date,</text>
    <text x="630" y="185" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  and auto-pay setup.</text>
    <text x="630" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#94A3B8">• Provide printed copy.</text>
    <text x="630" y="245" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Legal: TILA Compliance</text>

    <!-- Step 5 -->
    <rect x="820" y="0" width="180" height="260" rx="8" fill="#161B22" stroke="#A855F7" stroke-width="1.5"/>
    <circle cx="910" cy="35" r="18" fill="#A855F7"/>
    <text x="910" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">5</text>
    <text x="910" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Decline Protocol</text>
    <text x="835" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• IF DECLINED:</text>
    <text x="835" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  Never express shock or</text>
    <text x="835" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  embarrass the client.</text>
    <text x="835" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">"The bank will mail a</text>
    <text x="835" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">letter directly. We can split</text>
    <text x="835" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">cards or do layaway!"</text>
    <text x="835" y="245" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#A855F7">Grace: Save Relationship</text>
  </g>

  <!-- Verbatim Scripts Bottom Box -->
  <g transform="translate(50, 390)">
    <rect x="0" y="0" width="1000" height="240" rx="8" fill="#161B22" stroke="#334155"/>
    <rect x="0" y="0" width="1000" height="32" rx="8" fill="#1E293B"/>
    <text x="20" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">VERBATIM FLOOR SCRIPTS: HANDLING FINANCING WITH LUXURY ELEGANCE</text>

    <!-- Script 1 -->
    <rect x="20" y="50" width="465" height="170" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="1"/>
    <text x="35" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">The Unsolicited Seamless Bridge</text>
    <text x="35" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">"Most of our clients take advantage of our 12-month 0% interest</text>
    <text x="35" y="118" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">plan so they can keep their investment capital in their accounts.</text>
    <text x="35" y="136" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">It takes about 45 seconds on our private tablet to check approval</text>
    <text x="35" y="154" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">without affecting your credit score. Shall we take a quick look?"</text>

    <!-- Script 2 -->
    <rect x="515" y="50" width="465" height="170" rx="6" fill="#0F172A" stroke="#10B981" stroke-width="1"/>
    <text x="530" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">The Dignified Soft Decline Transition</text>
    <text x="530" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">"It looks like the bank's automated algorithm needs additional</text>
    <text x="530" y="118" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">verification, which they will send privately by mail. In the meantime,</text>
    <text x="530" y="136" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">we can easily split the total across two personal credit cards, or</text>
    <text x="530" y="154" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">place the piece on our custom 60-day vault layaway hold."</text>
  </g>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m02-pos-financing-application-sop.svg", c5_m02)

# C5 M03: Payment Options Decision Matrix
c5_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Payment Solutions Matrix: Layaway vs. Store Credit vs. BNPL</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Strategic evaluation of retail jewelry payment alternatives across operational, margin, and credit dimensions</text>

  <!-- Matrix Table -->
  <g transform="translate(50, 100)">
    <!-- Header -->
    <rect x="0" y="0" width="1000" height="40" rx="6" fill="#1E293B"/>
    <text x="20" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#94A3B8">PAYMENT MECHANISM</text>
    <text x="230" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">VAULT LAYAWAY</text>
    <text x="480" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">STORE FINANCING (0% APR)</text>
    <text x="760" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">BNPL (e.g. Klarna / Affirm)</text>

    <!-- Row 1: Merch Delivery -->
    <rect x="0" y="45" width="1000" height="50" fill="#161B22"/>
    <text x="20" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Merchandise Release</text>
    <text x="230" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FCA5A5">Only after 100% paid in full</text>
    <text x="480" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">Immediate take-home today</text>
    <text x="760" y="75" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">Immediate take-home today</text>

    <!-- Row 2: Retailer Cash Flow -->
    <rect x="0" y="100" width="1000" height="50" fill="#0F172A"/>
    <text x="20" y="130" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Store Cash Settlement</text>
    <text x="230" y="130" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Delayed over 30–120 days</text>
    <text x="480" y="130" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">Full deposit in 24–48 hours</text>
    <text x="760" y="130" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">Full deposit in 24–48 hours</text>

    <!-- Row 3: Merchant Cost (MDR) -->
    <rect x="0" y="155" width="1000" height="50" fill="#161B22"/>
    <text x="20" y="185" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Merchant Processing Fee</text>
    <text x="230" y="185" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">0% (Standard CC swipe only)</text>
    <text x="480" y="185" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FCA5A5">3.5% – 7.0% MDR cost</text>
    <text x="760" y="185" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FCA5A5">4.0% – 6.5% Merchant fee</text>

    <!-- Row 4: Default & Return Risk -->
    <rect x="0" y="210" width="1000" height="50" fill="#0F172A"/>
    <text x="20" y="240" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Default / Credit Risk</text>
    <text x="230" y="240" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#CBD5E1">Store retains item &amp; deposit rules</text>
    <text x="480" y="240" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">0% (Financing bank takes risk)</text>
    <text x="760" y="240" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#6EE7B7">0% (BNPL lender takes risk)</text>

    <!-- Row 5: Ticket Size Sweetspot -->
    <rect x="0" y="265" width="1000" height="50" fill="#161B22"/>
    <text x="20" y="295" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F3F4F6">Optimal Ticket Size</text>
    <text x="230" y="295" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#38BDF8">$500 – $3,000 (No credit check)</text>
    <text x="480" y="295" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#10B981">$3,000 – $50,000+ (High ticket)</text>
    <text x="760" y="295" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#F59E0B">$250 – $2,500 (Self-purchase)</text>
  </g>

  <!-- Floor Recommendation Summary -->
  <g transform="translate(50, 440)">
    <rect x="0" y="0" width="1000" height="190" rx="8" fill="#1E293B"/>
    <text x="20" y="30" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8">STRATEGIC FLOOR GUIDANCE BY CLIENT SITUATION:</text>
    <text x="20" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">1. <strong fill="#10B981">Engagement &amp; Bridal Rings ($5,000+):</strong> Lead with 12–24 Month 0% Store Financing. Keeps cash in client's pocket for wedding expenses while allowing them to upgrade diamond cut and size.</text>
    <text x="20" y="90" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">2. <strong fill="#38BDF8">Holiday / Secret Surprise Gifting (No Credit Check):</strong> Recommend Vault Layaway. Allows client to lock in the piece 60 days before Christmas or anniversary without bank statements appearing on shared mail.</text>
    <text x="20" y="120" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#E2E8F0">3. <strong fill="#F59E0B">Everyday Fashion &amp; Stacking Gold ($500–$2,000):</strong> Offer BNPL (4 interest-free bi-weekly payments) for frictionless Gen Z &amp; Millennial self-purchasers.</text>
  </g>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m03-payment-options-comparison-matrix.svg", c5_m03)

# C5 M04: FTC Jewelry Disclosure Mandates
c5_m04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">FTC Jewelry Guides Compliance: Counter Disclosure Mandates</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Federal Trade Commission legal requirements for gemstone treatments, synthetic disclosure, and metal stamping</text>

  <!-- 4 Core Compliance Pillars -->
  <g transform="translate(50, 100)">
    <!-- Pillar 1: Lab-Grown Diamonds -->
    <rect x="0" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="15" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">1. LAB-GROWN DIAMONDS</text>
    
    <text x="15" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">✓ APPROVED FTC TERMS:</text>
    <text x="15" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• "Laboratory-Grown"</text>
    <text x="15" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• "Laboratory-Created"</text>
    <text x="15" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• "[Brand]-Created"</text>

    <text x="15" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">❌ ILLEGAL / BARRED TERMS:</text>
    <text x="15" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• "Cultured" (without qualifier)</text>
    <text x="15" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• "Real" or "Natural"</text>
    <text x="15" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• "Found in nature"</text>
    <text x="15" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Omitting modifier on tag/receipt</text>

    <rect x="10" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="15" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Rule:</text>
    <text x="15" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Modifier must have EQUAL</text>
    <text x="15" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">conspicuousness &amp; size.</text>

    <!-- Pillar 2: Gemstone Treatments -->
    <rect x="255" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <rect x="255" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="270" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#10B981">2. GEMSTONE TREATMENTS</text>
    
    <text x="270" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">MANDATORY DISCLOSURE:</text>
    <text x="270" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Emerald Oil / Resin filling</text>
    <text x="270" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Sapphire/Ruby Heat treatment</text>
    <text x="270" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Beryllium diffusion in corundum</text>
    <text x="270" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Lead-glass filled ruby (Hybrid)</text>
    <text x="270" y="160" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Irradiation (Blue Topaz/Diamonds)</text>

    <text x="270" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">SPECIAL CARE NOTICE:</text>
    <text x="270" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Must disclose if treatment is</text>
    <text x="270" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  non-permanent or requires</text>
    <text x="270" y="255" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">  special cleaning caution.</text>

    <rect x="265" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="270" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#10B981">Rule:</text>
    <text x="270" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Written disclosure required</text>
    <text x="270" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">prior to sale completion.</text>

    <!-- Pillar 3: Metal Fineness -->
    <rect x="510" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="510" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="525" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F59E0B">3. METAL KARAT &amp; MARKS</text>
    
    <text x="525" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">TOLERANCES &amp; STANDARDS:</text>
    <text x="525" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 14K must be ≥ 583.3 ppt (58.3%)</text>
    <text x="525" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• 18K must be ≥ 750 ppt (75.0%)</text>
    <text x="525" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Platinum: 950 Plat vs 900 Plat</text>

    <text x="525" y="155" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">TRADEMARK RULE (US):</text>
    <text x="525" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• If quality mark (e.g. "14K") is</text>
    <text x="525" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  stamped, a registered maker's</text>
    <text x="525" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  trademark stamp is mandatory.</text>

    <rect x="520" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="525" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Vermeil Standard:</text>
    <text x="525" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Sterling silver base + min</text>
    <text x="525" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">2.5 microns 10K+ gold plating.</text>

    <!-- Pillar 4: Pricing & Advertising -->
    <rect x="765" y="0" width="235" height="360" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <rect x="765" y="0" width="235" height="36" rx="8" fill="#1E293B"/>
    <text x="780" y="24" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#EC4899">4. PRICING &amp; ADVERTISING</text>
    
    <text x="780" y="60" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">DECEPTIVE PRICING RULES:</text>
    <text x="780" y="80" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FCA5A5">• Fictitious "Original" Prices:</text>
    <text x="780" y="100" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  Cannot mark "Was $10k, Now $5k"</text>
    <text x="780" y="120" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  unless offered at $10k in good</text>
    <text x="780" y="140" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  faith for a substantial period.</text>

    <text x="780" y="175" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">CARAT WEIGHT RANGES:</text>
    <text x="780" y="195" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Fractional weights must state</text>
    <text x="780" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  exact tolerance or decimal (e.g.</text>
    <text x="780" y="235" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  3/4 ct = 0.69 – 0.82 ct).</text>

    <rect x="775" y="270" width="215" height="75" rx="6" fill="#0F172A"/>
    <text x="780" y="290" font-family="Inter, -apple-system, sans-serif" font-size="10" font-weight="bold" fill="#EC4899">Appraisal Trap:</text>
    <text x="780" y="310" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">Never use inflated insurance</text>
    <text x="780" y="325" font-family="Inter, -apple-system, sans-serif" font-size="10" fill="#CBD5E1">values as a sales discount tool.</text>
  </g>

  <!-- Legal Penalties Warning -->
  <rect x="50" y="480" width="1000" height="150" rx="8" fill="#2A1215" stroke="#EF4444" stroke-width="1.5"/>
  <text x="70" y="510" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EF4444">LEGAL &amp; CIVIL PENALTIES FOR FTC NON-COMPLIANCE</text>
  <text x="70" y="535" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">• <strong fill="#FCA5A5">FTC Enforcement:</strong> Civil penalties exceed $50,000 per violation for deceptive commercial practices and false origins.</text>
  <text x="70" y="560" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">• <strong fill="#FCA5A5">Lanham Act Civil Lawsuits:</strong> Competing jewelers and brands can sue for treble damages and attorney fees for mislabeled stones.</text>
  <text x="70" y="585" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">• <strong fill="#FCA5A5">Point of Sale Rule:</strong> All gemstone treatments, lab origins, and metal purities must appear on physical and digital receipts.</text>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m04-ftc-jewelry-disclosure-mandates.svg", c5_m04)

# C5 M05: AML Red Flags Decision Tree
c5_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Anti-Money Laundering (AML) Compliance: Red Flags &amp; SAR Decision Tree</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">FinCEN 31 CFR Chapter X compliance protocols for luxury dealers in precious metals, stones, and jewelry</text>

  <!-- Flowchart Decision Tree -->
  <g transform="translate(50, 100)">
    <!-- Root Trigger -->
    <rect x="360" y="0" width="280" height="60" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="2"/>
    <text x="500" y="25" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8" text-anchor="middle">CUSTOMER TRANSACTION INITIATED</text>
    <text x="500" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#9CA3AF" text-anchor="middle">High-value purchase, trade-in, or payment</text>

    <!-- Branch 1: Cash > $10,000 -->
    <path d="M 400 60 L 200 120" stroke="#38BDF8" stroke-width="1.5"/>
    <rect x="80" y="120" width="240" height="110" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="100" y="145" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">CASH / CASH EQUIV &gt; $10k</text>
    <text x="100" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Single or related 24-hr transactions</text>
    <text x="100" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Includes cashier's checks &lt;$10k</text>
    <text x="100" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Action: File IRS Form 8300 (15 days)</text>

    <!-- Branch 2: Structuring / Suspicious Red Flags -->
    <path d="M 500 60 L 500 120" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="380" y="120" width="240" height="110" rx="8" fill="#2A1215" stroke="#EF4444" stroke-width="1.5"/>
    <text x="400" y="145" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">SUSPICIOUS RED FLAGS</text>
    <text x="400" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Offers $9,900 cash to avoid ID</text>
    <text x="400" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#FECACA">• Unconcerned with price or quality</text>
    <text x="400" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EF4444">Action: Notify Compliance Officer / SAR</text>

    <!-- Branch 3: High Risk Geographic / PEP -->
    <path d="M 600 60 L 800 120" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="680" y="120" width="240" height="110" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="700" y="145" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#F59E0B">OFAC / SANCTIONS CHECK</text>
    <text x="700" y="170" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Politically Exposed Person (PEP)</text>
    <text x="700" y="190" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• High-risk sanctioned country wire</text>
    <text x="700" y="215" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Action: OFAC Specially Designated List</text>
  </g>

  <!-- AML Red Flags Summary Grid -->
  <g transform="translate(50, 360)">
    <rect x="0" y="0" width="1000" height="260" rx="8" fill="#161B22" stroke="#334155"/>
    <rect x="0" y="0" width="1000" height="32" rx="8" fill="#1E293B"/>
    <text x="20" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#F3F4F6">TOP 6 JEWELRY RETAIL AML RED FLAGS (FinCEN GUIDELINES)</text>

    <g transform="translate(20, 45)">
      <!-- Flag 1 -->
      <rect x="0" y="0" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="15" y="22" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">1. Structuring Below $10k</text>
      <text x="15" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Buyer asks to pay $9,500 in cash</text>
      <text x="15" y="63" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">today and $9,500 cash tomorrow.</text>

      <!-- Flag 2 -->
      <rect x="330" y="0" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="345" y="22" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">2. Reluctance to Provide ID</text>
      <text x="345" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Refuses standard government ID</text>
      <text x="345" y="63" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">or offers fraudulent documents.</text>

      <!-- Flag 3 -->
      <rect x="660" y="0" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="675" y="22" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">3. Price &amp; Quality Indifference</text>
      <text x="675" y="45" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Buys high-value loose diamonds or gold</text>
      <text x="675" y="63" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">bars without caring about cut or value.</text>

      <!-- Flag 4 -->
      <rect x="0" y="105" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="15" y="127" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">4. Third-Party Wire Transfers</text>
      <text x="15" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Payment arrives from an unrelated</text>
      <text x="15" y="168" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">offshore entity or shell company.</text>

      <!-- Flag 5 -->
      <rect x="330" y="105" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="345" y="127" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">5. Immediate Refund Demands</text>
      <text x="345" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Pays large cash sum, cancels order</text>
      <text x="345" y="168" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">next morning, asks for store check.</text>

      <!-- Flag 6 -->
      <rect x="660" y="105" width="300" height="90" rx="6" fill="#0F172A" stroke="#334155"/>
      <text x="675" y="127" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#EF4444">6. Unknown Walk-In Gold Liquidation</text>
      <text x="675" y="150" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">Selling large batches of scrap gold</text>
      <text x="675" y="168" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">or unset gems below market value.</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m05-aml-red-flags-decision-tree.svg", c5_m05)

# C5 M06: Memo, Consignment, and UCC-1 Workflow
c5_m06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <rect width="1100" height="680" fill="#0B0E14" rx="12"/>
  
  <text x="50" y="45" font-family="Inter, -apple-system, sans-serif" font-size="24" font-weight="bold" fill="#F3F4F6">Consignment &amp; Memo Inventory: UCC-1 Legal Protection Lifecycle</text>
  <text x="50" y="70" font-family="Inter, -apple-system, sans-serif" font-size="14" fill="#9CA3AF">Protecting store and consignor assets from bankruptcy claims through perfected Uniform Commercial Code filings</text>

  <!-- 4-Stage Lifecycle Map -->
  <g transform="translate(50, 100)">
    <!-- Stage 1 -->
    <rect x="0" y="0" width="235" height="250" rx="8" fill="#161B22" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="117" cy="35" r="18" fill="#38BDF8"/>
    <text x="117" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">1</text>
    <text x="117" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Written Agreement</text>
    <text x="15" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Explicit Title Retention clause</text>
    <text x="15" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Stated consignment period</text>
    <text x="15" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Agreed net payout vs split %</text>
    <text x="15" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Risk of loss / Insurance terms</text>
    <text x="15" y="200" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Document: Signed Contract</text>

    <!-- Stage 2 -->
    <rect x="255" y="0" width="235" height="250" rx="8" fill="#161B22" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="372" cy="35" r="18" fill="#10B981"/>
    <text x="372" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">2</text>
    <text x="372" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">UCC-1 Filing</text>
    <text x="270" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• File Financing Statement with</text>
    <text x="270" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  Secretary of State (UCC-1)</text>
    <text x="270" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Identify specific goods/collateral</text>
    <text x="270" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Must file BEFORE delivery</text>
    <text x="270" y="200" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#10B981">Legal: Perfected Interest</text>

    <!-- Stage 3 -->
    <rect x="510" y="0" width="235" height="250" rx="8" fill="#161B22" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="627" cy="35" r="18" fill="#F59E0B"/>
    <text x="627" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">3</text>
    <text x="627" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Notice to Creditors</text>
    <text x="525" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Search existing secured lenders</text>
    <text x="525" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Send formal written notice to</text>
    <text x="525" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  retailer's inventory banks</text>
    <text x="525" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• Prevents bank floating lien seizure</text>
    <text x="525" y="200" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B">Protection: PMSI Priority</text>

    <!-- Stage 4 -->
    <rect x="765" y="0" width="235" height="250" rx="8" fill="#161B22" stroke="#EC4899" stroke-width="1.5"/>
    <circle cx="882" cy="35" r="18" fill="#EC4899"/>
    <text x="882" y="41" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">4</text>
    <text x="882" y="75" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="bold" fill="#F3F4F6" text-anchor="middle">Sale or Return</text>
    <text x="780" y="105" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• If Sold: Remit agreed proceeds</text>
    <text x="780" y="125" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">  within contract window (e.g. 10d)</text>
    <text x="780" y="145" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• If Unsold: Formal return receipt</text>
    <text x="780" y="165" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#E2E8F0">• File UCC-3 termination statement</text>
    <text x="780" y="200" font-family="Inter, -apple-system, sans-serif" font-size="11" font-weight="bold" fill="#EC4899">Settlement: Closed Loop</text>
  </g>

  <!-- The Danger Scenario Box -->
  <g transform="translate(50, 380)">
    <rect x="0" y="0" width="1000" height="250" rx="8" fill="#2A1215" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="1000" height="32" rx="8" fill="#450A0A"/>
    <text x="20" y="22" font-family="Inter, -apple-system, sans-serif" font-size="14" font-weight="bold" fill="#EF4444">⚠️ THE CONSIGNMENT TRAP: WHAT HAPPENS WITHOUT A UCC-1 FILING</text>

    <text x="20" y="60" font-family="Inter, -apple-system, sans-serif" font-size="12" fill="#FECACA">If an estate collector or diamond wholesaler places an $80,000 diamond on memo/consignment without filing a UCC-1:</text>
    
    <g transform="translate(20, 80)">
      <rect x="0" y="0" width="460" height="140" rx="6" fill="#161B22" stroke="#EF4444"/>
      <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FCA5A5">Under UCC Article 9:</text>
      <text x="15" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• Goods on consignment are deemed owned by the retailer</text>
      <text x="15" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  as far as creditors and bankruptcy courts are concerned.</text>
      <text x="15" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• A simple "Memo Slip" is <strong fill="#EF4444">NOT ENOUGH</strong> to defeat a bank lien.</text>
    </g>

    <g transform="translate(500, 80)">
      <rect x="0" y="0" width="460" height="140" rx="6" fill="#161B22" stroke="#EF4444"/>
      <text x="15" y="25" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#FCA5A5">The Catastrophic Outcome:</text>
      <text x="15" y="50" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• If the retailer files Chapter 11 bankruptcy, the bank seizes</text>
      <text x="15" y="70" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">  the consignor's diamond to pay off general store debt.</text>
      <text x="15" y="95" font-family="Inter, -apple-system, sans-serif" font-size="11" fill="#CBD5E1">• The original owner becomes an unsecured creditor (pennies on $).</text>
    </g>
  </g>
</svg>"""
write_svg("courses/C5-financing-credit-compliance/assets/c5-m06-memo-consignment-ucc1-workflow.svg", c5_m06)

print("C5 SVG assets generated successfully!")
