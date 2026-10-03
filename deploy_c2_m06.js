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

// Master SVG Block for Figure 6.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M6" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M6" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Hesitation Isolation Matrix™ &amp; The 2-2-2 Cadence</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Diagnostic Objections &amp; High-Conversion Post-Visit Clienteling</text>

      <!-- Left Column: The 3-Step Hesitation Isolation Funnel -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">Hesitation Isolation Funnel™</text>

      <!-- Step 1: Validate and Liberate -->
      <rect x="35" y="115" width="290" height="60" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="50" y="137" font-size="12" font-weight="700" fill="#dfbe54">1. Validate &amp; Liberate</text>
      <text x="50" y="153" font-size="11" fill="#cbd5e1">&ldquo;Of course&mdash;taking time on fine jewelry is completely right.&rdquo;</text>
      <text x="50" y="167" font-size="10" fill="#94a3b8">Relieves customer defensive tension instantly</text>

      <line x1="180" y1="175" x2="180" y2="187" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M6)"/>

      <!-- Step 2: The Three-Category Question -->
      <rect x="35" y="188" width="290" height="74" rx="6" fill="#1e293b" stroke="#c9a227" stroke-width="1.5"/>
      <text x="50" y="210" font-size="12" font-weight="700" fill="#ffffff">2. The 3-Category Isolation Question</text>
      <text x="50" y="228" font-size="11" fill="#cbd5e1">&bull; Category A: The Design / Silhouette</text>
      <text x="50" y="244" font-size="11" fill="#cbd5e1">&bull; Category B: Diamond Optical Specs / Rarity</text>
      <text x="50" y="259" font-size="11" fill="#dfbe54">&bull; Category C: The Investment Bracket</text>

      <line x1="180" y1="262" x2="180" y2="274" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M6)"/>

      <!-- Step 3: Solve or Calendar -->
      <rect x="35" y="275" width="290" height="64" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="50" y="297" font-size="12" font-weight="700" fill="#0f172a">3. Solve on Spot OR Calendar Exit</text>
      <text x="50" y="315" font-size="11" fill="#475569">If simple misunderstanding &rarr; Clarify immediately</text>
      <text x="50" y="331" font-size="11" fill="#15803d" font-weight="600">If real time needed &rarr; Deploy Digital Spec Sheet</text>

      <!-- Frictionless Data Box -->
      <rect x="35" y="355" width="290" height="74" rx="6" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="50" y="377" font-size="12" font-weight="700" fill="#0b0f17">Frictionless Digital Spec Sheet™</text>
      <text x="50" y="395" font-size="11" fill="#475569">&bull; Never hand a dead paper card (90% trash rate)</text>
      <text x="50" y="411" font-size="11" fill="#c9a227" font-weight="700">&bull; Text high-res hand photos + GIA dossier live</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: The 2-2-2 Follow-Up Cadence -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The 2-2-2 Cadence™</text>

      <!-- Touchpoint 1: 48 Hours -->
      <rect x="395" y="115" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="420" cy="138" r="11" fill="#0b0f17"/>
      <text x="420" y="142" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">1</text>
      <text x="440" y="137" font-size="13" font-weight="700" fill="#0b0f17">48 Hours &bull; Memory Bridge SMS</text>
      <text x="440" y="155" font-size="11" fill="#475569">&bull; High-res photo of ring on their hand</text>
      <text x="440" y="171" font-size="11" fill="#0284c7" font-weight="600">&bull; Zero sales pressure; rekindle emotional glow</text>

      <!-- Touchpoint 2: 14 Days -->
      <rect x="395" y="200" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="420" cy="223" r="11" fill="#0b0f17"/>
      <text x="420" y="227" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">2</text>
      <text x="440" y="222" font-size="13" font-weight="700" fill="#0b0f17">14 Days &bull; Fresh Value Bridge</text>
      <text x="440" y="240" font-size="11" fill="#475569">&bull; New custom CAD rendering or stone arrival</text>
      <text x="440" y="256" font-size="11" fill="#475569">&bull; Invitation to side-by-side band comparison</text>

      <!-- Touchpoint 3: 60 Days -->
      <rect x="395" y="285" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="420" cy="308" r="11" fill="#0b0f17"/>
      <text x="420" y="312" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">3</text>
      <text x="440" y="307" font-size="13" font-weight="700" fill="#0b0f17">60 Days &bull; Milestone Horizon</text>
      <text x="440" y="325" font-size="11" fill="#475569">&bull; Anniversary or birthday timeline alignment</text>
      <text x="440" y="341" font-size="11" fill="#15803d" font-weight="600">&bull; Re-activating dormant relationship equity</text>

      <!-- Conversion Proof Box -->
      <rect x="395" y="375" width="290" height="54" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="540" y="396" text-anchor="middle" font-size="11" fill="#15803d" font-weight="700">&check; 50%+ of High-Ticket Sales Are Won</text>
      <text x="540" y="413" text-anchor="middle" font-size="10.5" fill="#166534">During the disciplined 2-2-2 follow-up sequence!</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; Hesitation Isolation &amp; 2-2-2 Cadence</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 6.2:</strong> The Hesitation Isolation Matrix&trade; &amp; The 2-2-2 Cadence &mdash; <span style="color: #475569;">Floor protocol transforming ambiguous stall objections into precise category diagnoses and automated luxury follow-up pipelines.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardIsolation = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The 3-Choice Hesitation Isolation Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;It is really beautiful, but I need to think about it before I make a decision.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Validating &amp; liberating)</em> &ldquo;I completely agree with you. An exceptional piece of fine jewelry should never be rushed, and you should take all the time you need.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Isolating root)</em> &ldquo;Usually when our clients tell me they want to sleep on a decision, it comes down to one of three things: either the design isn't quite 100% right, the diamond specifications aren't exactly what you pictured, or the investment level is a bit outside what feels comfortable. Which of those three is on your mind?&rdquo;</p>
  </div>
</div>
`;

const cardDigitalSpec = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Frictionless Digital Spec Sheet Capture Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Paper business cards end up crumpled in the bottom of a handbag, and you lose track of the details. Let me take a quick studio photo of this ring on your hand under our boutique lighting, and text it straight to your phone along with the exact GIA report number and your finger size so you have it right in your pocket.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Oh, that would be wonderful! My cell number is (555) 382-9014.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #fdfbf7; color: #c9a227; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid #dfbe54; white-space: nowrap;">Outcome</span>
    <p style="margin: 0; color: #64748b; font-style: italic;">Instant, verified mobile phone number captured with 100% client consent and genuine gratitude, setting up the 48-Hour Memory Bridge.</p>
  </div>
</div>
`;

const cardSMSCadence = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The 48-Hour Memory Bridge SMS Protocol&trade;</div>
  <div style="margin-bottom: 10px;">
    <strong style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Timing: 48 Hours Post-Visit &bull; Channel: SMS with Hand Photo</strong>
    <p style="margin: 6px 0 0 0; color: #0b0f17; font-weight: 500;">&ldquo;Good afternoon, Sophia! It was an absolute delight meeting you on Tuesday. I was just organizing our showcase vitrine and thought of how extraordinarily the platinum 2.10ct solitaire balanced on your hand. Here is that studio photo we took so you can keep the memory fresh. No need to reply&mdash;just wanted you to have it. Have a wonderful rest of your week! &mdash; Marcus, Jewelswell Client Advisor&rdquo;</p>
  </div>
  <div>
    <strong style="color: #15803d; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Client Behavioral Response</strong>
    <p style="margin: 4px 0 0 0; color: #475569; font-style: italic;">Because the message contains zero sales pressure and explicitly says &ldquo;no need to reply,&rdquo; the client feels entirely un-threatened. Over 60% of recipients reply voluntarily within 4 hours with questions about sizing, timing, or deposit holds.</p>
  </div>
</div>
`;

async function deployM06() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1567_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Closing the 'Be-Back': Why Post-Visit Cadence Wins 50% More Diamond Sales.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The 2-2-2 Clienteling Architecture™: Transforming Floor Walkouts into High-Value Lifelong Clients.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 6.2 right before "<h2>The 3-Step Hesitation Isolation Technique</h2>"
  if (!rawContent.includes('Figure 6.2:')) {
    rawContent = rawContent.replace(
      '<h2>The 3-Step Hesitation Isolation Technique</h2>',
      svgBlock + '\n\n<h2>The 3-Step Hesitation Isolation Technique</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Isolation) right after "<h2>Step 2: Isolate the Root (The Three-Category Choice)</h2>"
  if (!rawContent.includes('The 3-Choice Hesitation Isolation Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>Step 2: Isolate the Root (The Three-Category Choice)</h2>',
      '<h2>Step 2: Isolate the Root (The Three-Category Choice)</h2>\n\n' + cardIsolation
    );
  }

  // 4. Insert Dialogue Card 2 (Digital Spec Sheet) right after "<h2>The Digital Spec Sheet: Capturing Contact Info Without Friction</h2>"
  if (!rawContent.includes('The Frictionless Digital Spec Sheet Capture Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>The Digital Spec Sheet: Capturing Contact Info Without Friction</h2>',
      '<h2>The Digital Spec Sheet: Capturing Contact Info Without Friction</h2>\n\n' + cardDigitalSpec
    );
  }

  // 5. Insert Dialogue Card 3 (SMS Cadence) right after "<h2>Touchpoint 1: 48 Hours (The Gratitude & Memory Bridge)</h2>"
  if (!rawContent.includes('The 48-Hour Memory Bridge SMS Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>Touchpoint 1: 48 Hours (The Gratitude & Memory Bridge)</h2>',
      '<h2>Touchpoint 1: 48 Hours (The Gratitude & Memory Bridge)</h2>\n\n' + cardSMSCadence
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m06_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M06-ill-think-about-it-and-the-follow-up-that-wins.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1567 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1567,
    content: rawContent
  }, 601);
  console.log('Page 1567 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1770 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 602).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 603).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 604).catch(() => {});

  // Insert Figure 6.2 into Lesson 1770 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'Figure 6.2:',
    replace: 'Figure 6.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 6.2 and Dialogue Cards into Lesson 1770...');
    await callMcpTool('wp_replace_in_post', {
      id: 1770,
      field: 'post_content',
      search: '<h2>The 3-Step Hesitation Isolation Technique</h2>',
      replace: svgBlock + '\n\n<h2>The 3-Step Hesitation Isolation Technique</h2>',
      max_replacements: 1
    }, 605);
  }

  // Insert Isolation Card into Lesson 1770
  const checkIso = await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'The 3-Choice Hesitation Isolation Protocol&trade;',
    replace: 'The 3-Choice Hesitation Isolation Protocol&trade;',
    max_replacements: -1
  });
  if (checkIso.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1770,
      field: 'post_content',
      search: '<h2>Step 2: Isolate the Root (The Three-Category Choice)</h2>',
      replace: '<h2>Step 2: Isolate the Root (The Three-Category Choice)</h2>\n\n' + cardIsolation,
      max_replacements: 1
    }, 606);
  }

  // Insert Digital Spec Card into Lesson 1770
  const checkSpec = await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'The Frictionless Digital Spec Sheet Capture Protocol&trade;',
    replace: 'The Frictionless Digital Spec Sheet Capture Protocol&trade;',
    max_replacements: -1
  });
  if (checkSpec.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1770,
      field: 'post_content',
      search: '<h2>The Digital Spec Sheet: Capturing Contact Info Without Friction</h2>',
      replace: '<h2>The Digital Spec Sheet: Capturing Contact Info Without Friction</h2>\n\n' + cardDigitalSpec,
      max_replacements: 1
    }, 607);
  }

  // Insert SMS Cadence Card into Lesson 1770
  const checkSMS = await callMcpTool('wp_replace_in_post', {
    id: 1770,
    field: 'post_content',
    search: 'The 48-Hour Memory Bridge SMS Protocol&trade;',
    replace: 'The 48-Hour Memory Bridge SMS Protocol&trade;',
    max_replacements: -1
  });
  if (checkSMS.replacements_count === 0) {
    // Check if &amp; is in the header on Lesson 1770
    let targetHeading = '<h2>Touchpoint 1: 48 Hours (The Gratitude &amp; Memory Bridge)</h2>';
    const checkH = await callMcpTool('wp_replace_in_post', {
      id: 1770,
      field: 'post_content',
      search: targetHeading,
      replace: targetHeading,
      max_replacements: -1
    });
    if (checkH.replacements_count === 0) {
      targetHeading = '<h2>Touchpoint 1: 48 Hours (The Gratitude & Memory Bridge)</h2>';
    }

    await callMcpTool('wp_replace_in_post', {
      id: 1770,
      field: 'post_content',
      search: targetHeading,
      replace: targetHeading + '\n\n' + cardSMSCadence,
      max_replacements: 1
    }, 608);
  }

  console.log('=== Step 4: Verification Audit of Both 1567 and 1770 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 6.2:', 'The 3-Choice Hesitation Isolation Protocol',
    'The Frictionless Digital Spec Sheet Capture Protocol', 'The 48-Hour Memory Bridge SMS Protocol'
  ];
  for (const id of [1567, 1770]) {
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

  console.log('=== C2-M06 Deployment & Verification Complete! ===');
}

deployM06().catch(console.error);
