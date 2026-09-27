import os

def save_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {path}")

# c2-m01-first-90-seconds-flow.svg
svg_c2_m01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="680" rx="16" fill="url(#bg)"/>
  <rect x="2" y="2" width="1096" height="676" rx="14" fill="none" stroke="#334155" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(50, 35)">
    <rect x="0" y="0" width="190" height="24" rx="12" fill="#0284C7" fill-opacity="0.2"/>
    <text x="95" y="16" fill="#7DD3FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">FLOOR CONVERSATION SOP</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">The First 90 Seconds: Approach &amp; Engagement Map</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Transforming cold browse traffic into open dialogue without triggering defense alarms.</text>
  </g>

  <!-- Flowchart Steps -->
  <g transform="translate(50, 125)">
    <!-- Phase 1: The 10-Foot / 30-Second Rule -->
    <g transform="translate(0, 0)">
      <rect width="310" height="230" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="35" cy="30" r="16" fill="#0284C7"/>
      <text x="35" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1</text>
      <text x="65" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700">The 10-Foot / 30-Sec Buffer</text>
      <text x="65" y="44" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Non-Verbal Proximity Protocol</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• <tspan font-weight="700">Eye contact &amp; warm nod</tspan> within 10 ft</text>
        <text x="0" y="33" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Allow 15–30 seconds of unpressured browsing</text>
        <text x="0" y="51" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Position at 45° angle (never block exit)</text>
        <text x="0" y="69" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Observe case direction &amp; hand gestures</text>
        <rect x="0" y="85" width="280" height="60" rx="4" fill="#0F172A"/>
        <text x="10" y="103" fill="#F87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">CRITICAL MISTAKE:</text>
        <text x="10" y="119" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Pouncing at the threshold forces an immediate</text>
        <text x="10" y="133" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="10">"Just looking!" defense mechanism.</text>
      </g>
    </g>

    <!-- Connector 1 -->
    <g transform="translate(315, 100)">
      <line x1="0" y1="15" x2="25" y2="15" stroke="#38BDF8" stroke-width="2"/>
      <polygon points="25,10 35,15 25,20" fill="#38BDF8"/>
    </g>

    <!-- Phase 2: The Conversational Opener -->
    <g transform="translate(355, 0)">
      <rect width="310" height="230" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <circle cx="35" cy="30" r="16" fill="#059669"/>
      <text x="35" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2</text>
      <text x="65" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700">The Context Opener</text>
      <text x="65" y="44" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Ban "Can I Help You?"</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Greet as a host welcoming a guest</text>
        <text x="0" y="33" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Comment on an observable item or traffic</text>
        <text x="0" y="51" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Share a 5-second backstory on the case</text>
        <rect x="0" y="85" width="280" height="60" rx="4" fill="#0F172A"/>
        <text x="10" y="103" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">APPROVED SCRIPT:</text>
        <text x="10" y="119" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">"Welcome in! That emerald-cut sapphire</text>
        <text x="10" y="133" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">just arrived from our bench this morning."</text>
      </g>
    </g>

    <!-- Connector 2 -->
    <g transform="translate(670, 100)">
      <line x1="0" y1="15" x2="25" y2="15" stroke="#10B981" stroke-width="2"/>
      <polygon points="25,10 35,15 25,20" fill="#10B981"/>
    </g>

    <!-- Phase 3: Transition to Pad & Hands -->
    <g transform="translate(710, 0)">
      <rect width="290" height="230" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <circle cx="35" cy="30" r="16" fill="#D97706"/>
      <text x="35" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">3</text>
      <text x="65" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Piece Out &amp; In Hand</text>
      <text x="65" y="44" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="10" font-weight="600">The Tactile Transition</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Lay velvet pad flat on showcase top</text>
        <text x="0" y="33" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Take ONE hero piece out of the case</text>
        <text x="0" y="51" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11">• Immediately offer piece to client's hand</text>
        <rect x="0" y="85" width="260" height="60" rx="4" fill="#0F172A"/>
        <text x="10" y="103" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">TRANSITION SCRIPT:</text>
        <text x="10" y="119" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">"Let me pull this out so you can feel</text>
        <text x="10" y="133" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">the weight and see it outside the glass."</text>
      </g>
    </g>
  </g>

  <!-- Bottom Strategy Table: Why Traditional Openers Fail -->
  <g transform="translate(50, 395)">
    <rect width="1000" height="235" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="25" y="28" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">OPENER BENCHMARK: WHAT TO RETIRE VS. WHAT TO SAY</text>

    <g transform="translate(25, 45)">
      <!-- Row 1 -->
      <rect x="0" y="0" width="950" height="48" rx="4" fill="#0F172A"/>
      <text x="15" y="28" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✖ "Can I help you with anything?"</text>
      <text x="320" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Client response: "Just looking." (Kills dialogue in 3 seconds).</text>
      <text x="680" y="28" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✔ "Take your time. I love this new case."</text>

      <!-- Row 2 -->
      <rect x="0" y="56" width="950" height="48" rx="4" fill="#1E293B"/>
      <text x="15" y="28" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✖ "What's your budget today?"</text>
      <text x="320" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Premature qualification; signals commission hunger.</text>
      <text x="680" y="28" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✔ "Are we celebrating a special occasion?"</text>

      <!-- Row 3 -->
      <rect x="0" y="112" width="950" height="48" rx="4" fill="#0F172A"/>
      <text x="15" y="28" fill="#EF4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✖ "Are you looking for yourself or a gift?"</text>
      <text x="320" y="28" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Closed binary question; feels like an interrogation.</text>
      <text x="680" y="28" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✔ "Who are we hunting for today?"</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C2-fine-jewelry-sales-conversation/assets/c2-m01-first-90-seconds-flow.svg", svg_c2_m01)

# c2-m02-discovery-questioning-tree.svg
svg_c2_m02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <text x="90" y="16" fill="#C4B5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">DISCOVERY ARCHITECTURE</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">The 4-Pillar Discovery Questioning Tree</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Surfacing the real motivation, recipient lifestyle, aesthetic taste, and comfortable investment range.</text>
  </g>

  <!-- 4 Discovery Pillars Columns -->
  <g transform="translate(50, 125)">
    <!-- Pillar 1: Occasion & Milestone -->
    <g transform="translate(0, 0)">
      <rect width="235" height="500" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="205" height="35" rx="6" fill="#0284C7" fill-opacity="0.3"/>
      <text x="117" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. OCCASION</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Target Intel to Uncover:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Proposal deadline</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Milestone anniversary (10/25yr)</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Birthday / Push present</text>
        <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Self-purchase / Promotion</text>

        <line x1="0" y1="110" x2="205" y2="110" stroke="#334155" stroke-width="1"/>

        <text x="0" y="130" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Primary Question Script:</text>
        <rect x="-5" y="145" width="215" height="100" rx="4" fill="#0F172A"/>
        <text x="8" y="165" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"What is the story behind</text>
        <text x="8" y="181" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">this piece? Are we marking</text>
        <text x="8" y="197" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">a specific date or celebrating</text>
        <text x="8" y="213" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">a big milestone?"</text>

        <rect x="-5" y="260" width="215" height="150" rx="4" fill="#0F172A"/>
        <text x="8" y="280" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Follow-Up Pivot:</text>
        <text x="8" y="298" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">"If they say anniversary:</text>
        <text x="8" y="314" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">'How many wonderful years?</text>
        <text x="8" y="330" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">Did she keep her original band</text>
        <text x="8" y="346" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">or are we looking to build</text>
        <text x="8" y="362" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">a brand new stack?'"</text>
      </g>
    </g>

    <!-- Pillar 2: Recipient Lifestyle -->
    <g transform="translate(255, 0)">
      <rect width="235" height="500" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <rect x="15" y="15" width="205" height="35" rx="6" fill="#059669" fill-opacity="0.3"/>
      <text x="117" y="38" fill="#34D399" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. RECIPIENT</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Target Intel to Uncover:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Daily work &amp; hand use</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Active sports / outdoor habits</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• High-profile social events</text>
        <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Sensitive skin / allergies</text>

        <line x1="0" y1="110" x2="205" y2="110" stroke="#334155" stroke-width="1"/>

        <text x="0" y="130" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Primary Question Script:</text>
        <rect x="-5" y="145" width="215" height="100" rx="4" fill="#0F172A"/>
        <text x="8" y="165" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Tell me a little about her day.</text>
        <text x="8" y="181" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Is she hands-on at work,</text>
        <text x="8" y="197" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">or looking for something strictly</text>
        <text x="8" y="213" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">for evening wear?"</text>

        <rect x="-5" y="260" width="215" height="150" rx="4" fill="#0F172A"/>
        <text x="8" y="280" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Setting Selection Impact:</text>
        <text x="8" y="298" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">High activity / medical hands:</text>
        <text x="8" y="314" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">Recommend bezel, low-profile</text>
        <text x="8" y="330" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">basket, or platinum.</text>
        <text x="8" y="346" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Avoid high peg-heads or</text>
        <text x="8" y="362" fill="#FDA4AF" font-family="system-ui, sans-serif" font-size="10">fragile emeralds.</text>
      </g>
    </g>

    <!-- Pillar 3: Aesthetic Taste -->
    <g transform="translate(510, 0)">
      <rect width="235" height="500" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="205" height="35" rx="6" fill="#D97706" fill-opacity="0.3"/>
      <text x="117" y="38" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. AESTHETICS</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Target Intel to Uncover:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Metal tone preference</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Modern minimalist vs Vintage</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Diamond shape inclination</text>
        <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Color vs Classic white</text>

        <line x1="0" y1="110" x2="205" y2="110" stroke="#334155" stroke-width="1"/>

        <text x="0" y="130" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Primary Question Script:</text>
        <rect x="-5" y="145" width="215" height="100" rx="4" fill="#0F172A"/>
        <text x="8" y="165" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"When you look at the jewelry</text>
        <text x="8" y="181" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">she wears most often, is it</text>
        <text x="8" y="197" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">yellow gold, white metal,</text>
        <text x="8" y="213" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">or bold statement pieces?"</text>

        <rect x="-5" y="260" width="215" height="150" rx="4" fill="#0F172A"/>
        <text x="8" y="280" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Phone Photo Hack:</text>
        <text x="8" y="298" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">"Do you have a quick photo</text>
        <text x="8" y="314" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">of her on your phone?</text>
        <text x="8" y="330" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">I can read her neckline, ring</text>
        <text x="8" y="346" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">proportions, and preferred</text>
        <text x="8" y="362" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">style in 10 seconds."</text>
      </g>
    </g>

    <!-- Pillar 4: Investment Budget -->
    <g transform="translate(765, 0)">
      <rect width="235" height="500" rx="8" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
      <rect x="15" y="15" width="205" height="35" rx="6" fill="#7E22CE" fill-opacity="0.3"/>
      <text x="117" y="38" fill="#C084FC" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">4. INVESTMENT</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Target Intel to Uncover:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Target price corridor</text>
        <text x="0" y="53" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Flexibility on quality vs size</text>
        <text x="0" y="71" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Financing interest</text>
        <text x="0" y="89" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">• Trade-in asset availability</text>

        <line x1="0" y1="110" x2="205" y2="110" stroke="#334155" stroke-width="1"/>

        <text x="0" y="130" fill="#C084FC" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Range Corridor Script:</text>
        <rect x="-5" y="145" width="215" height="100" rx="4" fill="#0F172A"/>
        <text x="8" y="165" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"To make sure I show you options</text>
        <text x="8" y="181" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">that feel comfortable,</text>
        <text x="8" y="197" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">is there an investment range</text>
        <text x="8" y="213" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">you had in mind for this?"</text>

        <rect x="-5" y="260" width="215" height="150" rx="4" fill="#0F172A"/>
        <text x="8" y="280" fill="#C084FC" font-family="system-ui, sans-serif" font-size="10" font-weight="700">If Client is Hesitant:</text>
        <text x="8" y="298" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">"No problem at all. We have</text>
        <text x="8" y="314" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">stunning pieces in this look</text>
        <text x="8" y="330" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">ranging from $2,500 to $8,000.</text>
        <text x="8" y="346" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">I'll show you three distinct</text>
        <text x="8" y="362" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">tiers so you can compare."</text>
      </g>
    </g>
  </g>
</svg>"""

save_svg("courses/C2-fine-jewelry-sales-conversation/assets/c2-m02-discovery-questioning-tree.svg", svg_c2_m02)

# c2-m03-feature-benefit-emotion-bridge.svg
svg_c2_m03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="100%" height="100%">
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
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#059669" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">PRESENTATION ARCHITECTURE</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Feature → Benefit → Emotion Storytelling Bridge</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Translating technical metallurgy and gemology into enduring emotional value.</text>
  </g>

  <!-- 3-Tier Bridge Diagram -->
  <g transform="translate(50, 130)">
    <!-- Column 1: Feature (The Fact) -->
    <g transform="translate(0, 0)">
      <rect width="290" height="460" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="260" height="35" rx="6" fill="#0284C7" fill-opacity="0.3"/>
      <text x="145" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. FEATURE (The Spec)</text>

      <g transform="translate(20, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">What it IS (Technical):</text>
        <text x="0" y="35" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Lab report numbers, metal alloy,</text>
        <text x="0" y="50" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">prong count, carat weight.</text>

        <!-- Examples -->
        <g transform="translate(0, 75)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Example A: Platinum</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"This ring is solid PT950</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">platinum alloy."</text>
        </g>

        <g transform="translate(0, 155)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Example B: Excellent Cut</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"This diamond carries a GIA</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">Triple Excellent cut grade."</text>
        </g>

        <g transform="translate(0, 235)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Example C: Bezel Setting</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"The center stone is enclosed</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">in a full metal collar rim."</text>
        </g>
      </g>
    </g>

    <!-- Arrow 1 -->
    <g transform="translate(305, 230)">
      <line x1="0" y1="20" x2="35" y2="20" stroke="#38BDF8" stroke-width="3"/>
      <polygon points="35,12 50,20 35,28" fill="#38BDF8"/>
    </g>

    <!-- Column 2: Benefit (The Function) -->
    <g transform="translate(365, 0)">
      <rect width="290" height="460" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <rect x="15" y="15" width="260" height="35" rx="6" fill="#059669" fill-opacity="0.3"/>
      <text x="145" y="38" fill="#34D399" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. BENEFIT (The Function)</text>

      <g transform="translate(20, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">What it DOES for Them:</text>
        <text x="0" y="35" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Durability, maintenance savings,</text>
        <text x="0" y="50" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">optical brightness, comfort.</text>

        <!-- Examples -->
        <g transform="translate(0, 75)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Functional Benefit:</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"It never loses metal when polished</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">and never requires rhodium dipping."</text>
        </g>

        <g transform="translate(0, 155)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Functional Benefit:</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"It bounces maximum light even in</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">dim candle-lit restaurants."</text>
        </g>

        <g transform="translate(0, 235)">
          <rect width="250" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Functional Benefit:</text>
          <text x="10" y="38" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">"It will never snag on her knit sweaters</text>
          <text x="10" y="52" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10">or catch during her hospital rounds."</text>
        </g>
      </g>
    </g>

    <!-- Arrow 2 -->
    <g transform="translate(670, 230)">
      <line x1="0" y1="20" x2="35" y2="20" stroke="#10B981" stroke-width="3"/>
      <polygon points="35,12 50,20 35,28" fill="#10B981"/>
    </g>

    <!-- Column 3: Emotion (The Meaning) -->
    <g transform="translate(730, 0)">
      <rect width="270" height="460" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="240" height="35" rx="6" fill="#D97706" fill-opacity="0.3"/>
      <text x="135" y="38" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. EMOTION (The Meaning)</text>

      <g transform="translate(15, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">How it Makes Them FEEL:</text>
        <text x="0" y="35" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Confidence, pride, romance,</text>
        <text x="0" y="50" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">lifelong peace of mind.</text>

        <!-- Examples -->
        <g transform="translate(0, 75)">
          <rect width="240" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Story Script:</text>
          <text x="10" y="38" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"You are giving her a piece that</text>
          <text x="10" y="52" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">her granddaughter will wear unchanged."</text>
        </g>

        <g transform="translate(0, 155)">
          <rect width="240" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Story Script:</text>
          <text x="10" y="38" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Every time her hand moves, everyone</text>
          <text x="10" y="52" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">across the room notices the fire."</text>
        </g>

        <g transform="translate(0, 235)">
          <rect width="240" height="65" rx="4" fill="#0F172A"/>
          <text x="10" y="20" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Story Script:</text>
          <text x="10" y="38" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"She will never have to take it off or</text>
          <text x="10" y="52" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">worry about losing the stone."</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""

save_svg("courses/C2-fine-jewelry-sales-conversation/assets/c2-m03-feature-benefit-emotion-bridge.svg", svg_c2_m03)

# c2-m05-price-objection-ladder.svg
svg_c2_m05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%">
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
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#EF4444" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">OBJECTION NAVIGATION</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">The 4-Step Price Objection Ladder</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">Handling "That's more than I wanted to spend" with dignity, margin protection, and zero discounting.</text>
  </g>

  <!-- Ladder Steps -->
  <g transform="translate(50, 120)">
    <!-- Step 1 -->
    <g transform="translate(0, 0)">
      <rect width="1000" height="110" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="45" cy="55" r="22" fill="#0284C7"/>
      <text x="45" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">1</text>
      <text x="85" y="40" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700">ACKNOWLEDGE &amp; VALIDATE (Do Not Flinch)</text>
      <text x="85" y="60" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12">Never apologize for the price tag or rush to drop margin. Agree that fine jewelry is an important investment.</text>
      <text x="85" y="85" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Script: "I completely understand. When you're looking at something this fine, you want every dollar to make total sense."</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(0, 125)">
      <rect width="1000" height="110" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <circle cx="45" cy="55" r="22" fill="#059669"/>
      <text x="45" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">2</text>
      <text x="85" y="40" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700">ISOLATE: IS IT THE PRICE OR THE PIECE?</text>
      <text x="85" y="60" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12">Determine if they love the aesthetic design first. If they dislike the style, a 20% discount will still not close the sale.</text>
      <text x="85" y="85" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Script: "Setting the price aside for just one second — is this the design and look you truly love for her?"</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(0, 250)">
      <rect width="1000" height="110" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <circle cx="45" cy="55" r="22" fill="#D97706"/>
      <text x="45" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">3</text>
      <text x="85" y="40" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700">ADJUST THE VALUE LEVERS (Engineering to Budget)</text>
      <text x="85" y="60" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12">If budget is strict, adjust the 4Cs variables (e.g. F to H color, VS1 to SI1, 14k gold, or lab-grown) to preserve design.</text>
      <text x="85" y="85" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Script: "We can keep this exact mounting design and shift to an eye-clean SI1 center to bring it right to your $4,500 target."</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(0, 375)">
      <rect width="1000" height="140" rx="8" fill="#1E293B" stroke="#A855F7" stroke-width="1.5"/>
      <circle cx="45" cy="70" r="22" fill="#7E22CE"/>
      <text x="45" y="77" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">4</text>
      <text x="85" y="40" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="700">OFFER CONSTRUCTIVE PAYMENT &amp; TRADE SOLUTIONS</text>
      <text x="85" y="60" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12">Introduce 12-month promotional financing, layaway, or gold trade-in credit before even considering price concession.</text>
      <rect x="85" y="75" width="880" height="45" rx="4" fill="#0F172A"/>
      <text x="95" y="95" fill="#C084FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Financing Script: "With our 12-month zero-interest program, you don't have to compromise on the diamond;</text>
      <text x="95" y="110" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">it comes out to $375 a month, keeping your cash completely untouched."</text>
    </g>
  </g>
</svg>"""

save_svg("courses/C2-fine-jewelry-sales-conversation/assets/c2-m05-price-objection-ladder.svg", svg_c2_m05)

# c2-m09-three-closing-pathways.svg
svg_c2_m09 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="100%" height="100%">
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
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#10B981" fill-opacity="0.2"/>
    <text x="90" y="16" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">CLOSING ARCHITECTURE</text>
    <text x="0" y="52" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Three Natural Closing Pathways for Fine Jewelry</text>
    <text x="0" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="13">High-ticket closing techniques that feel like seamless client service rather than high-pressure sales.</text>
  </g>

  <!-- 3 Closing Columns -->
  <g transform="translate(50, 130)">
    <!-- 1. The Assumptive Next-Step Close -->
    <g transform="translate(0, 0)">
      <rect width="310" height="460" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#0284C7" fill-opacity="0.3"/>
      <text x="155" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. ASSUMPTIVE NEXT STEP</text>

      <g transform="translate(20, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">When to Use:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Client has given 2+ strong buying</text>
        <text x="0" y="50" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">signals (trying on, smiling, timing).</text>

        <line x1="0" y1="70" x2="270" y2="70" stroke="#334155" stroke-width="1"/>

        <text x="0" y="90" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">How it Operates:</text>
        <text x="0" y="110" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Assumes the decision is made and moves</text>
        <text x="0" y="125" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">naturally to sizing, packaging, or timing.</text>

        <rect x="-5" y="150" width="280" height="150" rx="6" fill="#0F172A"/>
        <text x="10" y="172" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Dialogue Script:</text>
        <text x="10" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Let's measure her finger size right</text>
        <text x="10" y="211" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">now so our bench jeweler can have</text>
        <text x="10" y="227" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">this sized and polished in our</text>
        <text x="10" y="243" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">signature box by Thursday morning."</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Focuses on excitement &amp; logistics.</text>
      </g>
    </g>

    <!-- 2. The Alternative Choice Close -->
    <g transform="translate(345, 0)">
      <rect width="310" height="460" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#059669" fill-opacity="0.3"/>
      <text x="155" y="38" fill="#34D399" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. ALTERNATIVE CHOICE</text>

      <g transform="translate(20, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">When to Use:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Client is torn between two finalist</text>
        <text x="0" y="50" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">pieces on the pad.</text>

        <line x1="0" y1="70" x2="270" y2="70" stroke="#334155" stroke-width="1"/>

        <text x="0" y="90" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">How it Operates:</text>
        <text x="0" y="110" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Shifts the decision from "Buy vs. Don't Buy"</text>
        <text x="0" y="125" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">to "Option A vs. Option B".</text>

        <rect x="-5" y="150" width="280" height="150" rx="6" fill="#0F172A"/>
        <text x="10" y="172" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Dialogue Script:</text>
        <text x="10" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"Between the platinum solitaire and the</text>
        <text x="10" y="211" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">yellow gold hidden-halo, which one</text>
        <text x="10" y="227" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">do you feel she would light up</text>
        <text x="10" y="243" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">looking at every single day?"</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Either choice is a successful close.</text>
      </g>
    </g>

    <!-- 3. The Direct Milestone Close -->
    <g transform="translate(690, 0)">
      <rect width="310" height="460" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="15" y="15" width="280" height="35" rx="6" fill="#D97706" fill-opacity="0.3"/>
      <text x="155" y="38" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. DIRECT MILESTONE</text>

      <g transform="translate(20, 65)">
        <text x="0" y="15" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700">When to Use:</text>
        <text x="0" y="35" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">Direct, analytical client; or compressed</text>
        <text x="0" y="50" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">timeframe / upcoming trip.</text>

        <line x1="0" y1="70" x2="270" y2="70" stroke="#334155" stroke-width="1"/>

        <text x="0" y="90" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">How it Operates:</text>
        <text x="0" y="110" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Directly pairs the jewelry piece with the</text>
        <text x="0" y="125" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">upcoming milestone and asks for permission.</text>

        <rect x="-5" y="150" width="280" height="150" rx="6" fill="#0F172A"/>
        <text x="10" y="172" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Floor Dialogue Script:</text>
        <text x="10" y="195" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">"It hits your exact target budget,</text>
        <text x="10" y="211" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">the diamond is GIA Triple Excellent, and</text>
        <text x="10" y="227" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">it's ready for your anniversary Saturday.</text>
        <text x="10" y="243" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">Shall we wrap this up for you today?"</text>
        <text x="10" y="270" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Clean, respectful, and definitive.</text>
      </g>
    </g>
  </g>
</svg>"""

save_svg("courses/C2-fine-jewelry-sales-conversation/assets/c2-m09-three-closing-pathways.svg", svg_c2_m09)

print("Course C2 SVGs generated!")
