const fs = require('fs');
const path = require('path');

const WP_URL = 'https://jewelswell.com';
const API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443';
const endpoint = `${WP_URL}/wp-json/easy-mcp-ai/v1/mcp`;

async function callMcpTool(name, args, id = 1) {
  const headers = {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Antigravity-C2-Deploy/1.0'
  };

  const res = await fetch(endpoint, {
    method: 'POST',
    headers,
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: id,
      method: 'tools/call',
      params: { name, arguments: args }
    })
  });

  const data = await res.json();
  if (data.error) throw new Error(JSON.stringify(data.error));
  return JSON.parse(data.result.content[0].text);
}

// Master SVG Block for Figure 7.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M7" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M7" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Physical Salon Advantage Architecture™ &amp; Optical Defense</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Real-World Light Performance vs. Online Spec-Sheet Algorithms</text>

      <!-- Left Column: The 4 Salon Pillars -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">4 Physical Salon Pillars™</text>

      <!-- Pillar 1 -->
      <rect x="35" y="115" width="290" height="68" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="138" r="11" fill="#0b0f17"/>
      <text x="58" y="142" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">1</text>
      <text x="78" y="137" font-size="13" font-weight="700" fill="#0b0f17">Optical Reality vs. Paper Blueprint</text>
      <text x="78" y="155" font-size="11" fill="#475569">&bull; Report is a blueprint; light return is the portrait</text>
      <text x="78" y="171" font-size="11" fill="#b91c1c" font-weight="600">&bull; Eliminates milky clouds &amp; brown B-grade tints</text>

      <!-- Pillar 2 -->
      <rect x="35" y="195" width="290" height="68" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="218" r="11" fill="#0b0f17"/>
      <text x="58" y="222" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">2</text>
      <text x="78" y="217" font-size="13" font-weight="700" fill="#0b0f17">Tactile Ergonomics &amp; Comfort</text>
      <text x="78" y="235" font-size="11" fill="#475569">&bull; Substantial metal density &bull; Snag-free tips</text>
      <text x="78" y="251" font-size="11" fill="#475569">&bull; Tested in person on finger vs. hollow online cast</text>

      <!-- Pillar 3 -->
      <rect x="35" y="275" width="290" height="68" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="298" r="11" fill="#0b0f17"/>
      <text x="58" y="302" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">3</text>
      <text x="78" y="297" font-size="13" font-weight="700" fill="#0b0f17">Immediate Custody &amp; Zero Risk</text>
      <text x="78" y="315" font-size="11" fill="#475569">&bull; 10x loupe inspection before a dollar is spent</text>
      <text x="78" y="331" font-size="11" fill="#15803d" font-weight="600">&bull; No postal carrier loss, porch theft, or return fees</text>

      <!-- Pillar 4 -->
      <rect x="35" y="355" width="290" height="74" rx="8" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <circle cx="58" cy="378" r="11" fill="#c9a227"/>
      <text x="58" y="382" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="700">4</text>
      <text x="78" y="377" font-size="13" font-weight="700" fill="#0b0f17">The Local Master Bench Covenant</text>
      <text x="78" y="395" font-size="11" fill="#475569">&bull; In-house master goldsmith &bull; Lifetime warranty</text>
      <text x="78" y="411" font-size="11" fill="#c9a227" font-weight="700">&bull; Immediate face-to-face service for decades</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: The Lifetime Covenant Math -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The Lifetime Covenant Math™</text>

      <rect x="395" y="115" width="290" height="235" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <text x="410" y="138" font-size="13" font-weight="700" fill="#0b0f17">Compounded In-House Service Value</text>
      <text x="410" y="156" font-size="11" fill="#64748b">Services included complimentary at our salon:</text>
      <line x1="410" y1="166" x2="665" y2="166" stroke="#f1f5f9" stroke-width="1"/>

      <text x="410" y="186" font-size="11" fill="#334155">&bull; Master Laser Ring Sizing &amp; Fitting</text>
      <text x="655" y="186" text-anchor="end" font-size="11" fill="#0b0f17" font-weight="700">$180</text>

      <text x="410" y="208" font-size="11" fill="#334155">&bull; 5-Year Prong Retipping &amp; Security Checks</text>
      <text x="655" y="208" text-anchor="end" font-size="11" fill="#0b0f17" font-weight="700">$450</text>

      <text x="410" y="230" font-size="11" fill="#334155">&bull; Annual Rhodium Refinishing &amp; Spa Baths</text>
      <text x="655" y="230" text-anchor="end" font-size="11" fill="#0b0f17" font-weight="700">$750</text>

      <text x="410" y="252" font-size="11" fill="#334155">&bull; Insurance Documentation &amp; Appraisals</text>
      <text x="655" y="252" text-anchor="end" font-size="11" fill="#0b0f17" font-weight="700">$350</text>

      <line x1="410" y1="264" x2="665" y2="264" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="410" y="284" font-size="12" fill="#0b0f17" font-weight="700">Total Tangible Lifetime Value:</text>
      <text x="655" y="284" text-anchor="end" font-size="13" fill="#15803d" font-weight="800">+$1,730</text>

      <rect x="405" y="298" width="270" height="42" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="540" y="316" text-anchor="middle" font-size="10.5" fill="#15803d" font-weight="700">&check; Online &ldquo;Discount&rdquo; Is Wiped Out Completely</text>
      <text x="540" y="331" text-anchor="middle" font-size="10" fill="#166534">The customer saves money by choosing our salon!</text>

      <!-- Bottom Principle Box -->
      <rect x="395" y="360" width="290" height="69" rx="8" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="540" y="382" text-anchor="middle" font-size="11" font-weight="700" fill="#dfbe54">The Optical Truth Law™</text>
      <text x="540" y="401" text-anchor="middle" font-size="11" fill="#ffffff" font-style="italic">&ldquo;The grading certificate tells you what the stone has;</text>
      <text x="540" y="417" text-anchor="middle" font-size="11" fill="#ffffff" font-style="italic">Your own eyes tell you what the stone does.&rdquo;</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; Salon Advantage &amp; Optical Defense</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 7.2:</strong> The Physical Salon Advantage Architecture&trade; &amp; Optical Defense &mdash; <span style="color: #475569;">Dual framework contrasting 2D algorithmic online grading against real-world light performance and $1,730+ lifetime bench care.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardBlueprint = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Blueprint vs. Portrait Analogy Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Showing smartphone screen)</em> &ldquo;I found this exact same diamond online&mdash;GIA Triple Ex, F color, VS1&mdash;for eight hundred dollars less. Why shouldn't I just buy it from them?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Warm, unflinching respect &bull; Welcoming the smartphone)</em> &ldquo;I'm so glad you have that pulled up! You've done great research. Let me share why two diamonds with identical GIA reports can look completely different in real life: A GIA report is a blueprint&mdash;it gives you table percentages, depth, and clarity codes. But it is not a portrait.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Online warehouse algorithms often trade stones with subtle milky clouds or brown undertones that don't change the letter grade on paper, but kill light return across a dinner table. Here at our salon, you inspect the stone with your own eyes under 10x magnification before you spend a single dollar.&rdquo;</p>
  </div>
</div>
`;

const cardSideBySide = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Side-by-Side Optical Challenge Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;If you are considering ordering that diamond online, here is my personal invitation: order it with their return policy, bring it into our salon, and we will place it side-by-side with our diamond on a velvet pad under our master gemological loupe.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Wait... you would actually let me bring their ring in here?&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Absolutely! We want you to make this milestone decision with 100% certainty. If the online stone outperforms ours, I will personally shake your hand and mount it for you. But if our cut delivers significantly superior optical fire and dispersion, you will know exactly why our clients choose us.&rdquo;</p>
  </div>
</div>
`;

const cardBenchCovenant = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Lifetime Bench Covenant Valuation Script&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;When you buy from a faceless warehouse website, your relationship ends the moment the cardboard box is dropped on your doorstep. If a prong snags or your finger size fluctuates, you have to insure a parcel, ship your ring across the country, and wait four weeks praying it doesn't get lost in transit.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;At our salon, our master goldsmith works right behind that door. You walk in on a Saturday, enjoy a sparkling water, and we inspect your prongs, give your diamond an ultrasonic steam bath, and hand it back sparkling like the day you married. That lifetime bench covenant represents over seventeen hundred dollars in real service value&mdash;and a lifetime of peace of mind.&rdquo;</p>
  </div>
</div>
`;

async function deployM07() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1569_dump.html', 'utf8');

  // 1. Insert Master Vector Figure 7.2 right before "<h2>The Four Pillars of the Physical Salon Advantage</h2>"
  if (!rawContent.includes('Figure 7.2:')) {
    rawContent = rawContent.replace(
      '<h2>The Four Pillars of the Physical Salon Advantage</h2>',
      svgBlock + '\n\n<h2>The Four Pillars of the Physical Salon Advantage</h2>'
    );
  }

  // 2. Insert Dialogue Card 1 (Blueprint) right after "<h3>The Master Script: The Blueprint Analogy</h3>"
  if (!rawContent.includes('The Blueprint vs. Portrait Analogy Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Master Script: The Blueprint Analogy</h3>',
      '<h3>The Master Script: The Blueprint Analogy</h3>\n\n' + cardBlueprint
    );
  }

  // 3. Insert Dialogue Card 2 (Side by Side) right after "<h2>The Side-by-Side Optical Challenge</h2>"
  if (!rawContent.includes('The Side-by-Side Optical Challenge Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>The Side-by-Side Optical Challenge</h2>',
      '<h2>The Side-by-Side Optical Challenge</h2>\n\n' + cardSideBySide
    );
  }

  // 4. Insert Dialogue Card 3 (Bench Covenant) right after "<h2>Pillar 4: The Local Bench Covenant</h2>"
  if (!rawContent.includes('The Lifetime Bench Covenant Valuation Script&trade;')) {
    rawContent = rawContent.replace(
      '<h2>Pillar 4: The Local Bench Covenant</h2>',
      '<h2>Pillar 4: The Local Bench Covenant</h2>\n\n' + cardBenchCovenant
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m07_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M07-online-comparison-and-the-showrooming-client.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1569 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1569,
    content: rawContent
  }, 701);
  console.log('Page 1569 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1772 ===');
  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1772,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 702).catch(() => {});

  // Insert Figure 7.2 into Lesson 1772 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1772,
    field: 'post_content',
    search: 'Figure 7.2:',
    replace: 'Figure 7.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 7.2 and Dialogue Cards into Lesson 1772...');
    await callMcpTool('wp_replace_in_post', {
      id: 1772,
      field: 'post_content',
      search: '<h2>The Four Pillars of the Physical Salon Advantage</h2>',
      replace: svgBlock + '\n\n<h2>The Four Pillars of the Physical Salon Advantage</h2>',
      max_replacements: 1
    }, 703);
  }

  // Insert Blueprint Card into Lesson 1772
  const checkBP = await callMcpTool('wp_replace_in_post', {
    id: 1772,
    field: 'post_content',
    search: 'The Blueprint vs. Portrait Analogy Protocol&trade;',
    replace: 'The Blueprint vs. Portrait Analogy Protocol&trade;',
    max_replacements: -1
  });
  if (checkBP.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1772,
      field: 'post_content',
      search: '<h3>The Master Script: The Blueprint Analogy</h3>',
      replace: '<h3>The Master Script: The Blueprint Analogy</h3>\n\n' + cardBlueprint,
      max_replacements: 1
    }, 704);
  }

  // Insert Side by Side Card into Lesson 1772
  const checkSBS = await callMcpTool('wp_replace_in_post', {
    id: 1772,
    field: 'post_content',
    search: 'The Side-by-Side Optical Challenge Protocol&trade;',
    replace: 'The Side-by-Side Optical Challenge Protocol&trade;',
    max_replacements: -1
  });
  if (checkSBS.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1772,
      field: 'post_content',
      search: '<h2>The Side-by-Side Optical Challenge</h2>',
      replace: '<h2>The Side-by-Side Optical Challenge</h2>\n\n' + cardSideBySide,
      max_replacements: 1
    }, 705);
  }

  // Insert Bench Covenant Card into Lesson 1772
  const checkBC = await callMcpTool('wp_replace_in_post', {
    id: 1772,
    field: 'post_content',
    search: 'The Lifetime Bench Covenant Valuation Script&trade;',
    replace: 'The Lifetime Bench Covenant Valuation Script&trade;',
    max_replacements: -1
  });
  if (checkBC.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1772,
      field: 'post_content',
      search: '<h2>Pillar 4: The Local Bench Covenant</h2>',
      replace: '<h2>Pillar 4: The Local Bench Covenant</h2>\n\n' + cardBenchCovenant,
      max_replacements: 1
    }, 706);
  }

  console.log('=== Step 4: Verification Audit of Both 1569 and 1772 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 7.2:', 'The Blueprint vs. Portrait Analogy Protocol',
    'The Side-by-Side Optical Challenge Protocol', 'The Lifetime Bench Covenant Valuation Script'
  ];
  for (const id of [1569, 1772]) {
    console.log(`Auditing ID ${id}:`);
    for (const term of terms) {
      const res = await callMcpTool('wp_replace_in_post', {
        id: id,
        field: 'post_content',
        search: term,
        replace: term,
        max_replacements: -1
      });
      console.log(`  - '${term}': count = ${res.replacements_count}`);
    }
  }

  console.log('=== C2-M07 Deployment & Verification Complete! ===');
}

deployM07().catch(console.error);
