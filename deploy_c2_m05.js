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

// Master SVG Block for Figure 5.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M5" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M5" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Value-Anchor Reframing Architecture™ &amp; Margin Defense</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; The 4-Step AARE Funnel &amp; The Economics of Zero Discounting</text>

      <!-- Left Column: The 4-Step AARE Funnel -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The AARE Margin Funnel™</text>

      <!-- Step 1: Acknowledge -->
      <rect x="35" y="115" width="290" height="54" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="50" y="137" font-size="12" font-weight="700" fill="#dfbe54">1. ACKNOWLEDGE (Validate Without Conceding)</text>
      <text x="50" y="153" font-size="11" fill="#cbd5e1">&ldquo;I completely respect that $15,000 is a serious investment.&rdquo;</text>

      <line x1="180" y1="169" x2="180" y2="181" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M5)"/>

      <!-- Step 2: Anchor -->
      <rect x="35" y="182" width="290" height="54" rx="6" fill="#1e293b" stroke="#c9a227" stroke-width="1.5"/>
      <text x="50" y="204" font-size="12" font-weight="700" fill="#ffffff">2. ANCHOR (Re-Establish Value Pillars)</text>
      <text x="50" y="220" font-size="11" fill="#94a3b8">Triple-Ex optical fire, hand-forged 950 Pt, lifetime care</text>

      <line x1="180" y1="236" x2="180" y2="248" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M5)"/>

      <!-- Step 3: Reframe -->
      <rect x="35" y="249" width="290" height="54" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="50" y="271" font-size="12" font-weight="700" fill="#0f172a">3. REFRAME (The Cost-Per-Wear Formula)</text>
      <text x="50" y="287" font-size="11" fill="#475569">40 years of daily pride = $1.02/day (Pence vs. value)</text>

      <line x1="180" y1="303" x2="180" y2="315" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M5)"/>

      <!-- Step 4: Explore -->
      <rect x="35" y="316" width="290" height="54" rx="6" fill="#fdfbf7" stroke="#dfbe54" stroke-width="2"/>
      <text x="50" y="338" font-size="12" font-weight="700" fill="#0b0f17">4. EXPLORE (Zero-Discount Options)</text>
      <text x="50" y="354" font-size="11" fill="#15803d" font-weight="600">Preferred financing &bull; Spec shift &bull; Value attachment</text>

      <!-- Golden Rule Callout -->
      <rect x="35" y="385" width="290" height="42" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="180" y="403" text-anchor="middle" font-size="11" fill="#15803d" font-weight="700">&check; Never change the price to match the item.</text>
      <text x="180" y="418" text-anchor="middle" font-size="10.5" fill="#166534">Change the item to match the client's budget!</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: The Brutal Economics of Discounting -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The Brutal Economics™</text>

      <!-- Box: 10% Discount Impact -->
      <rect x="395" y="115" width="290" height="120" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5"/>
      <text x="410" y="138" font-size="13" font-weight="700" fill="#b91c1c">The 10% Discount Illusion</text>
      <text x="410" y="160" font-size="11" fill="#475569">Assume $10,000 Retail at 50% Margin ($5,000 Gross Profit):</text>
      <line x1="410" y1="170" x2="665" y2="170" stroke="#fca5a5" stroke-width="1"/>
      <text x="410" y="188" font-size="11" fill="#334155">&bull; 10% Discount ($1,000 off) cuts net profit to $4,000</text>
      <text x="410" y="206" font-size="11" fill="#b91c1c" font-weight="700">&bull; Result: A 20% to 33% Loss in Store Net Profit!</text>
      <text x="410" y="224" font-size="11" fill="#991b1b">&bull; You must sell 33% MORE jewelry just to break even!</text>

      <!-- Box: Brand Perception Erosion -->
      <rect x="395" y="250" width="290" height="110" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <text x="410" y="273" font-size="13" font-weight="700" fill="#0b0f17">Psychological Damage of Discounting</text>
      <text x="410" y="295" font-size="11" fill="#475569">&bull; Signals that initial prices are inflated arbitrary tags</text>
      <text x="410" y="313" font-size="11" fill="#475569">&bull; Destroys prestige &amp; client trust in provenance</text>
      <text x="410" y="331" font-size="11" fill="#c9a227" font-weight="600">&bull; Trains clients to never purchase without haggling</text>
      <text x="410" y="349" font-size="11" fill="#64748b">&bull; High-jewelry maisons (Cartier, Bulgari) NEVER discount</text>

      <!-- Firm Stand Box -->
      <rect x="395" y="375" width="290" height="52" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="540" y="396" text-anchor="middle" font-size="12" font-weight="700" fill="#dfbe54">The 5-Word Firm Stand™</text>
      <text x="540" y="414" text-anchor="middle" font-size="11.5" fill="#ffffff" font-style="italic">&ldquo;No, this is our price.&rdquo; (With a warm smile)</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; AARE Protocol &amp; Margin Defense</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 5.2:</strong> The Value-Anchor Reframing Architecture&trade; &amp; Margin Defense Funnel &mdash; <span style="color: #475569;">Diagnostic roadmap connecting the 4-Step AARE protocol to mathematical margin protection and luxury tag integrity.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardAARE = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Value-Anchor Reframing Protocol&trade; &bull; $18,000 Solitaire Defense</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Eighteen thousand is higher than I anticipated. Can you do fifteen thousand if I buy it today?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Warm, unflinching smile &bull; Validating without conceding)</em> &ldquo;I completely understand&mdash;eighteen thousand dollars is a significant milestone investment, and you want to be certain every dollar represents extraordinary value.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Anchoring value)</em> &ldquo;Our pricing is meticulously calibrated to reflect what makes this piece rare: the center diamond is a certified Triple-Ex cut with zero light leakage, hand-set into a solid 950 platinum mounting that will never thin or wear down over generations, backed by our lifetime complimentary spa service and annual prong inspection. Because we maintain rigorous craft standards, our pricing is firm.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Exploring options)</em> &ldquo;If keeping your commitment closer to fifteen thousand is essential, we have two elegant paths: we can explore our preferred interest-free financing over 12 months, or I can curate a stone at 1.40 carats with identical face-up fire that hits fifteen thousand exactly. Which direction would feel most comfortable?&rdquo;</p>
  </div>
</div>
`;

const cardCostPerWear = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Cost-Per-Wear Amortization Script&trade; &bull; 40-Year Heirloom Math</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Ten thousand dollars feels like an indulgence for an anniversary band.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;I respect that thought. Let's look at how fine jewelry lives in your life compared to anything else you buy: A luxury handbag or vacation costs thousands and depreciates or ends in days. This band will live on your finger every single day for the next forty years. That amortizes to sixty-eight cents a day.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;For sixty-eight cents a day, you look down at your hand every morning and feel the pride of thirty years of shared partnership. When you look at it through the lens of a lifetime, it isn't an expense&mdash;it is an heirloom.&rdquo;</p>
  </div>
</div>
`;

const cardSpecShift = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Spec-Shift Curation Protocol&trade; &bull; Gemological Budget Alignment</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;I love the size of this 2.0-carat solitaire, but twelve thousand is my hard limit. Can you bring the price down to twelve?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;I honor your twelve-thousand-dollar boundary completely. Rather than discount this piece and compromise on our standards, let me show you how smart gemological engineering gives you the exact look you love within your budget.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Presenting curated comparison)</em> &ldquo;This stone is an E-color VVS2 at fourteen thousand. Here is an F-color VS1 with an identical GIA Triple-Ex cut. Face-up on your hand, the human eye cannot distinguish the difference in color or clarity, and the diameter is an identical 8.1 millimeters. But this stone is exactly eleven thousand eight hundred dollars. You get the 2.0-carat visual presence you fell in love with, and stay comfortably under your twelve thousand dollar limit.&rdquo;</p>
  </div>
</div>
`;

async function deployM05() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1565_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Holding Gross Margins on the Diamond Counter: The Psychology of Price Confidence.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The Value-Anchor Reframing Architecture™: Protecting Gross Margins and Brand Equity on the Luxury Floor.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 5.2 right before "<h2>The 4-Step AARE Framework for Price Objections</h2>"
  if (!rawContent.includes('Figure 5.2:')) {
    rawContent = rawContent.replace(
      '<h2>The 4-Step AARE Framework for Price Objections</h2>',
      svgBlock + '\n\n<h2>The 4-Step AARE Framework for Price Objections</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (AARE) right after "<h2>Step 1: Acknowledge (Validate Without Conceding)</h2>"
  if (!rawContent.includes('The Value-Anchor Reframing Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>Step 1: Acknowledge (Validate Without Conceding)</h2>',
      '<h2>Step 1: Acknowledge (Validate Without Conceding)</h2>\n\n' + cardAARE
    );
  }

  // 4. Insert Dialogue Card 2 (Cost-Per-Wear) right after "<h3>Worked Floor Script: The Cost-Per-Wear Calculation</h3>"
  if (!rawContent.includes('The Cost-Per-Wear Amortization Script&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Worked Floor Script: The Cost-Per-Wear Calculation</h3>',
      '<h3>Worked Floor Script: The Cost-Per-Wear Calculation</h3>\n\n' + cardCostPerWear
    );
  }

  // 5. Insert Dialogue Card 3 (Spec Shift) right after "<h3>Solution 2: The Spec Shift (Smart Gemological Curation)</h3>"
  if (!rawContent.includes('The Spec-Shift Curation Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Solution 2: The Spec Shift (Smart Gemological Curation)</h3>',
      '<h3>Solution 2: The Spec Shift (Smart Gemological Curation)</h3>\n\n' + cardSpecShift
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m05_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M05-price-objections-without-discounting.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1565 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1565,
    content: rawContent
  }, 501);
  console.log('Page 1565 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1768 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 502).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 503).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 504).catch(() => {});

  // Insert Figure 5.2 into Lesson 1768 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'Figure 5.2:',
    replace: 'Figure 5.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 5.2 and Dialogue Cards into Lesson 1768...');
    await callMcpTool('wp_replace_in_post', {
      id: 1768,
      field: 'post_content',
      search: '<h2>The 4-Step AARE Framework for Price Objections</h2>',
      replace: svgBlock + '\n\n<h2>The 4-Step AARE Framework for Price Objections</h2>',
      max_replacements: 1
    }, 505);
  }

  // Insert AARE Card into Lesson 1768
  const checkAARE = await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'The Value-Anchor Reframing Protocol&trade;',
    replace: 'The Value-Anchor Reframing Protocol&trade;',
    max_replacements: -1
  });
  if (checkAARE.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1768,
      field: 'post_content',
      search: '<h2>Step 1: Acknowledge (Validate Without Conceding)</h2>',
      replace: '<h2>Step 1: Acknowledge (Validate Without Conceding)</h2>\n\n' + cardAARE,
      max_replacements: 1
    }, 506);
  }

  // Insert Cost Per Wear Card into Lesson 1768
  const checkCPW = await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'The Cost-Per-Wear Amortization Script&trade;',
    replace: 'The Cost-Per-Wear Amortization Script&trade;',
    max_replacements: -1
  });
  if (checkCPW.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1768,
      field: 'post_content',
      search: '<h3>Worked Floor Script: The Cost-Per-Wear Calculation</h3>',
      replace: '<h3>Worked Floor Script: The Cost-Per-Wear Calculation</h3>\n\n' + cardCostPerWear,
      max_replacements: 1
    }, 507);
  }

  // Insert Spec Shift Card into Lesson 1768
  const checkSS = await callMcpTool('wp_replace_in_post', {
    id: 1768,
    field: 'post_content',
    search: 'The Spec-Shift Curation Protocol&trade;',
    replace: 'The Spec-Shift Curation Protocol&trade;',
    max_replacements: -1
  });
  if (checkSS.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1768,
      field: 'post_content',
      search: '<h3>Solution 2: The Spec Shift (Smart Gemological Curation)</h3>',
      replace: '<h3>Solution 2: The Spec Shift (Smart Gemological Curation)</h3>\n\n' + cardSpecShift,
      max_replacements: 1
    }, 508);
  }

  console.log('=== Step 4: Verification Audit of Both 1565 and 1768 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 5.2:', 'The Value-Anchor Reframing Protocol',
    'The Cost-Per-Wear Amortization Script', 'The Spec-Shift Curation Protocol'
  ];
  for (const id of [1565, 1768]) {
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

  console.log('=== C2-M05 Deployment & Verification Complete! ===');
}

deployM05().catch(console.error);
