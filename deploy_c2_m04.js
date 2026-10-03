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

// Master SVG Block for Figure 4.3
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M4" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M4" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The 18 Buying Signals Matrix &amp; The Golden Silence Window™</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Diagnostic Detection, Verbal Restraint &amp; Closing Execution</text>

      <!-- Left Column: The 3 Buying Signal Channels -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">3 Diagnostic Channels™</text>

      <!-- Channel A: Physical -->
      <rect x="35" y="115" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="138" r="11" fill="#0b0f17"/>
      <text x="58" y="142" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">A</text>
      <text x="78" y="137" font-size="13" font-weight="700" fill="#0b0f17">Physical &amp; Kinesthetic</text>
      <text x="78" y="155" font-size="11" fill="#475569">&bull; Reluctance to remove ring / caressing metal</text>
      <text x="78" y="171" font-size="11" fill="#475569">&bull; Multiple mirror angles &bull; Relaxed shoulders</text>

      <!-- Channel B: Operational -->
      <rect x="35" y="200" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="223" r="11" fill="#0b0f17"/>
      <text x="58" y="227" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">B</text>
      <text x="78" y="222" font-size="13" font-weight="700" fill="#0b0f17">Logistical &amp; Operational</text>
      <text x="78" y="240" font-size="11" fill="#475569">&bull; Sizing turnaround time &bull; Appraisal inclusions</text>
      <text x="78" y="256" font-size="11" fill="#475569">&bull; Cleaning care routines &bull; Payment terms</text>

      <!-- Channel C: Linguistic -->
      <rect x="35" y="285" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="308" r="11" fill="#0b0f17"/>
      <text x="58" y="312" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">C</text>
      <text x="78" y="307" font-size="13" font-weight="700" fill="#0b0f17">Linguistic / Possessive Shift</text>
      <text x="78" y="325" font-size="11" fill="#475569">&bull; Shift from &ldquo;it&rdquo; to &ldquo;my ring / my pendant&rdquo;</text>
      <text x="78" y="341" font-size="11" fill="#15803d" font-weight="600">&bull; Mental ownership established on the skin</text>

      <!-- Diagnostic Rule Box -->
      <rect x="35" y="375" width="290" height="52" rx="6" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="180" y="396" text-anchor="middle" font-size="11" fill="#0b0f17" font-weight="700">The 1-Signal Rule™</text>
      <text x="180" y="413" text-anchor="middle" font-size="10.5" fill="#64748b">When ANY channel fires &rarr; STOP presenting!</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: The Golden Silence Gate -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The Golden Silence Gate™</text>

      <!-- Step 1: Signal Detected -->
      <rect x="395" y="115" width="290" height="50" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="410" y="136" font-size="12" font-weight="700" fill="#dfbe54">1. Signal Detected &bull; Hard Halt</text>
      <text x="410" y="152" font-size="11" fill="#94a3b8">Zero further specs or 4Cs lecturing</text>

      <line x1="540" y1="165" x2="540" y2="177" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M4)"/>

      <!-- Step 2: The Direct Trial Close -->
      <rect x="395" y="178" width="290" height="50" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="410" y="199" font-size="12" font-weight="700" fill="#0f172a">2. Direct Trial Close / Next Step</text>
      <text x="410" y="215" font-size="11" fill="#475569">&ldquo;We can size this by Thursday. Should I write it up?&rdquo;</text>

      <line x1="540" y1="228" x2="540" y2="240" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M4)"/>

      <!-- Step 3: THE GOLDEN SILENCE (Highlighted) -->
      <rect x="395" y="241" width="290" height="78" rx="8" fill="#fdfbf7" stroke="#dfbe54" stroke-width="2"/>
      <text x="410" y="264" font-size="13" font-weight="700" fill="#0b0f17">3. The 10-15s Golden Silence™</text>
      <text x="410" y="282" font-size="11" fill="#475569">&bull; Step back 2 feet &bull; Relax hands at sides</text>
      <text x="410" y="298" font-size="11" fill="#15803d" font-weight="700">&bull; The next person who speaks loses the close</text>

      <line x1="540" y1="319" x2="540" y2="331" stroke="#15803d" stroke-width="2" marker-end="url(#jwArrowC2M4)"/>

      <!-- Step 4: The Closed Agreement -->
      <rect x="395" y="332" width="290" height="48" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
      <text x="410" y="353" font-size="12" font-weight="700" fill="#15803d">4. Agreement: &ldquo;Yes, let&rsquo;s do it!&rdquo;</text>
      <text x="410" y="369" font-size="11" fill="#166534">Deliver champagne/water, write the ticket</text>

      <!-- Danger Box Below Step 4 -->
      <rect x="395" y="390" width="290" height="37" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
      <text x="540" y="406" text-anchor="middle" font-size="10.5" fill="#b91c1c" font-weight="700">&times; Danger: Breaking Silence Reopens Decision</text>
      <text x="540" y="420" text-anchor="middle" font-size="10" fill="#dc2626">Triggers buyer remorse before card is swiped</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; 18 Buying Signals &amp; Silence Discipline</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 4.3:</strong> The 18 Buying Signals Matrix &amp; The Golden Silence Window&trade; &mdash; <span style="color: #475569;">Diagnostic map connecting kinesthetic and logistical cues to immediate presentation cessation and silent closing discipline.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardSizing = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Sizing Inquiry &amp; Assumptive Close Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Turning ring in spotlight)</em> &ldquo;Could you size this down to a six and a quarter?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;We certainly can. Our master jeweler will laser-weld the seam so the sizing is completely invisible, and I can have it ready for you by Thursday afternoon. Should I write that up for you right now?&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #fdfbf7; color: #c9a227; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid #dfbe54; white-space: nowrap;">Action</span>
    <p style="margin: 0; color: #64748b; font-style: italic;"><strong>The Golden Silence:</strong> The advisor stops talking immediately, takes one gentle step back, and remains quiet and attentive. Within four seconds, the client smiles and nods: &ldquo;Yes, let&rsquo;s do it.&rdquo;</p>
  </div>
</div>
`;

const cardPossessive = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Possessive Pronoun Pivot Protocol&trade; &bull; Linguistic Ownership Shift</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;How would I clean my diamond ring at home? Does it need special solution, or can I use warm water?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Validating ownership)</em> &ldquo;Warm water with a drop of gentle dish soap and a soft-bristle brush will keep your diamond bursting with light. We also provide our signature botanical cleaning kit with your purchase today, and you are always welcome to bring it by anytime for our ultrasonic spa bath. Let&rsquo;s package that cleaning kit together with your documentation.&rdquo;</p>
  </div>
</div>
`;

const cardPartner = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Partner Validation &amp; The 2-Foot Step-Back Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Extends hand toward partner, eyes lighting up)</em> &ldquo;Look at this... what do you think?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Takes two physical steps back, allowing private sightlines between couple)</em> &ldquo;It looks like it was custom-sculpted for your hand.&rdquo; <em>(Turns warmly to partner, smiling, and remains silent)</em></p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Partner</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;It is stunning. You look so happy. Let&rsquo;s take it.&rdquo;</p>
  </div>
</div>
`;

async function deployM04() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1562_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Buying Signals on the Diamond Counter: How to Stop Selling and Start Writing.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The Non-Verbal Buying Signal Matrix™: Converting Psychological Ownership into the Completed Transaction.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 4.3 right before "<h2>The 18 Diagnostic Buying Signals of Hard Luxury</h2>"
  if (!rawContent.includes('Figure 4.3:')) {
    rawContent = rawContent.replace(
      '<h2>The 18 Diagnostic Buying Signals of Hard Luxury</h2>',
      svgBlock + '\n\n<h2>The 18 Diagnostic Buying Signals of Hard Luxury</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Sizing) right after "<h3>Category B: Verbal & Logistical Signals (The Practical Mindset)</h3>"
  if (!rawContent.includes('The Sizing Inquiry &amp; Assumptive Close Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Category B: Verbal & Logistical Signals (The Practical Mindset)</h3>',
      '<h3>Category B: Verbal & Logistical Signals (The Practical Mindset)</h3>\n\n' + cardSizing
    );
  }

  // 4. Insert Dialogue Card 2 (Possessive) right after "<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>"
  if (!rawContent.includes('The Possessive Pronoun Pivot Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>',
      '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>\n\n' + cardPossessive
    );
  }

  // 5. Insert Dialogue Card 3 (Partner / 2-Foot Step-Back) right after "<h3>The 2-Foot Step-Back Protocol</h3>"
  if (!rawContent.includes('The Partner Validation &amp; The 2-Foot Step-Back Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The 2-Foot Step-Back Protocol</h3>',
      '<h3>The 2-Foot Step-Back Protocol</h3>\n\n' + cardPartner
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m04_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M04-buying-signals-when-to-stop-talking.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1562 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1562,
    content: rawContent
  }, 401);
  console.log('Page 1562 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1766 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 402).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 403).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 404).catch(() => {});

  // Insert Figure 4.3 into Lesson 1766 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'Figure 4.3:',
    replace: 'Figure 4.3:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 4.3 and Dialogue Cards into Lesson 1766...');
    await callMcpTool('wp_replace_in_post', {
      id: 1766,
      field: 'post_content',
      search: '<h2>The 18 Diagnostic Buying Signals of Hard Luxury</h2>',
      replace: svgBlock + '\n\n<h2>The 18 Diagnostic Buying Signals of Hard Luxury</h2>',
      max_replacements: 1
    }, 405);
  }

  // Insert Sizing Card into Lesson 1766
  const checkSizing = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Sizing Inquiry &amp; Assumptive Close Protocol&trade;',
    replace: 'The Sizing Inquiry &amp; Assumptive Close Protocol&trade;',
    max_replacements: -1
  });
  if (checkSizing.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1766,
      field: 'post_content',
      search: '<h3>Category B: Verbal & Logistical Signals (The Practical Mindset)</h3>',
      replace: '<h3>Category B: Verbal & Logistical Signals (The Practical Mindset)</h3>\n\n' + cardSizing,
      max_replacements: 1
    }, 406);
  }

  // Insert Possessive Card into Lesson 1766
  const checkPossessive = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Possessive Pronoun Pivot Protocol&trade;',
    replace: 'The Possessive Pronoun Pivot Protocol&trade;',
    max_replacements: -1
  });
  if (checkPossessive.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1766,
      field: 'post_content',
      search: '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>',
      replace: '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>\n\n' + cardPossessive,
      max_replacements: 1
    }, 407);
  }

  // Insert Partner Card into Lesson 1766
  const checkPartner = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Partner Validation &amp; The 2-Foot Step-Back Protocol&trade;',
    replace: 'The Partner Validation &amp; The 2-Foot Step-Back Protocol&trade;',
    max_replacements: -1
  });
  if (checkPartner.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1766,
      field: 'post_content',
      search: '<h3>The 2-Foot Step-Back Protocol</h3>',
      replace: '<h3>The 2-Foot Step-Back Protocol</h3>\n\n' + cardPartner,
      max_replacements: 1
    }, 408);
  }

  console.log('=== Step 4: Verification Audit of Both 1562 and 1766 ===');
  const terms = ['Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales', '.c1-article-container', 'Figure 4.3:', 'The Sizing Inquiry & Assumptive Close Protocol'];
  for (const id of [1562, 1766]) {
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

  console.log('=== C2-M04 Deployment & Verification Complete! ===');
}

deployM04().catch(console.error);
