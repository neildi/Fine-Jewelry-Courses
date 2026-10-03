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

// Master SVG Block for Figure 8.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M8" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M8" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Ethical Attachment Architecture™ &amp; Lifetime Care</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Elevating UPT from 1.0 to 1.4 Through Custodial Hospitality</text>

      <!-- Left Column: The 3 Attachment Tiers -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">3 Attachment Tiers™</text>

      <!-- Tier 1 -->
      <rect x="35" y="115" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="138" r="11" fill="#0b0f17"/>
      <text x="58" y="142" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">1</text>
      <text x="78" y="137" font-size="13" font-weight="700" fill="#0b0f17">Harmonic Fine Jewelry Companions</text>
      <text x="78" y="155" font-size="11" fill="#475569">&bull; The Wedding Band Early-Look Protocol</text>
      <text x="78" y="171" font-size="11" fill="#0284c7" font-weight="600">&bull; Stacked while the ring is warm on the hand</text>

      <!-- Tier 2 -->
      <rect x="35" y="200" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="223" r="11" fill="#0b0f17"/>
      <text x="58" y="227" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">2</text>
      <text x="78" y="222" font-size="13" font-weight="700" fill="#0b0f17">Custodial Care Products</text>
      <text x="78" y="240" font-size="11" fill="#475569">&bull; Signature botanical ultrasonic formulation</text>
      <text x="78" y="256" font-size="11" fill="#475569">&bull; Microfiber travel clutch &amp; polishing kit</text>

      <!-- Tier 3 -->
      <rect x="35" y="285" width="290" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="308" r="11" fill="#0b0f17"/>
      <text x="58" y="312" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">3</text>
      <text x="78" y="307" font-size="13" font-weight="700" fill="#0b0f17">Lifetime Protection Covenant</text>
      <text x="78" y="325" font-size="11" fill="#475569">&bull; Laser prong retipping &amp; sizing coverage</text>
      <text x="78" y="341" font-size="11" fill="#15803d" font-weight="600">&bull; Framed as preservation of love, not fear</text>

      <!-- UPT Math Box -->
      <rect x="35" y="370" width="290" height="58" rx="6" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="180" y="391" text-anchor="middle" font-size="11" fill="#0b0f17" font-weight="700">The Power of 1.4 UPT™</text>
      <text x="180" y="407" text-anchor="middle" font-size="10.5" fill="#64748b">1.0 &rarr; 1.4 UPT adds +$350,000/yr in production</text>
      <text x="180" y="420" text-anchor="middle" font-size="10" fill="#15803d" font-weight="600">Zero additional marketing or walk-in traffic required</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: Ethical Philosophy -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">Ethical Custodianship™</text>

      <!-- Box: Contrasting Approaches -->
      <rect x="395" y="115" width="290" height="110" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5"/>
      <text x="410" y="138" font-size="13" font-weight="700" fill="#b91c1c">&times; Predatory Upselling (Mass Retail)</text>
      <line x1="410" y1="148" x2="665" y2="148" stroke="#fca5a5" stroke-width="1"/>
      <text x="410" y="168" font-size="11" fill="#475569">&bull; Awkward register ambush at point of sale</text>
      <text x="410" y="186" font-size="11" fill="#475569">&bull; Fear-based pressure (&ldquo;what if you lose it?&rdquo;)</text>
      <text x="410" y="204" font-size="11" fill="#991b1b">&bull; Generic third-party brochures with fine-print exclusions</text>

      <rect x="395" y="235" width="290" height="110" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
      <text x="410" y="258" font-size="13" font-weight="700" fill="#15803d">&check; Ethical Custodianship (Jewelswell)</text>
      <line x1="410" y1="268" x2="665" y2="268" stroke="#bbf7d0" stroke-width="1"/>
      <text x="410" y="288" font-size="11" fill="#334155">&bull; Natural companion introduced during curation</text>
      <text x="410" y="306" font-size="11" fill="#334155">&bull; Preserving brilliance and generational security</text>
      <text x="410" y="324" font-size="11" fill="#166534" font-weight="600">&bull; Deepening client trust through comprehensive hospitality</text>

      <!-- Bottom Principle Box -->
      <rect x="395" y="355" width="290" height="74" rx="8" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="540" y="377" text-anchor="middle" font-size="11" font-weight="700" fill="#dfbe54">The Custodial Law™</text>
      <text x="540" y="396" text-anchor="middle" font-size="11" fill="#ffffff" font-style="italic">&ldquo;We never add products to make money;</text>
      <text x="540" y="412" text-anchor="middle" font-size="11" fill="#ffffff" font-style="italic">We add protection &amp; companionship to safeguard their legacy.&rdquo;</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; Ethical Attachment &amp; Custodial Care</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 8.2:</strong> The Ethical Attachment Architecture&trade; &amp; Lifetime Care Covenant &mdash; <span style="color: #475569;">Framework transforming predatory register upsells into seamless custodial hospitality, lifting UPT from 1.0 to 1.4 ethically.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardWeddingBand = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Wedding Band Early-Look Protocol&trade; &bull; Day One Companion Pairing</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(While the solitaire is still warm on her hand)</em> &ldquo;While we have this ring right here on your hand, let me show you something that most couples don't think about until two weeks before the ceremony: how the matching wedding band sits against this gallery.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Slips contoured platinum diamond band next to the solitaire)</em> &ldquo;See how this band locks in flush with zero gap? If you wait until next year, trying to match the metal batch, diamond color, and exact contour can feel like a stressful scavenger hunt. You don't have to decide today, but seeing the completed suite gives you total clarity.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Oh wow... that looks so complete together. Can we just bundle them together today so we don't have to worry about it later?&rdquo;</p>
  </div>
</div>
`;

const cardCareKit = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Hospitality Care Kit Bridge Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Diamonds are natural magnets for hand lotions and cooking oils, which form a microscopic film over the pavilion and dull light return. We want your ring to sparkle twenty years from now exactly as it does under our spotlights today.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Placing signature travel clutch and botanical cleaner on tray)</em> &ldquo;This is our botanical fine jewelry care clutch. It includes our non-ammoniated diamond wash, a jeweler's soft-bristle brush, and a plush microfiber travel pouch so your ring never sits on a hotel nightstand or gym locker bench. We include this with your ring today as our commitment to your piece's lifelong life.&rdquo;</p>
  </div>
</div>
`;

const cardProtection = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Peace-of-Mind Protection Framing Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;I have a general homeowners policy; doesn't that cover everything if something happens?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Homeowners policies are wonderful for catastrophic fire or burglary, but they typically carry a hefty deductible, cap unscheduled jewelry at $1,500, and do not cover daily wear-and-tear like a bent prong, stone loosening, or chipping while gardening.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Our in-house Lifetime Custodial Covenant covers all regular wear with zero deductible: annual laser retipping, rhodium plating, and ring sizing. If you ever look down and notice a prong caught on knitwear, our master bench fixes it on the spot with zero out-of-pocket expense. It lets you wear this ring every day with total freedom and joy.&rdquo;</p>
  </div>
</div>
`;

async function deployM08() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1572_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Bridal Pairing Mastery: Selling the Wedding Band on Day One.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The Bridal Pairing Architecture™: Presenting the Wedding Band on Day One with Zero Pressure.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 8.2 right before "<h2>The Three-Tier Attachment Architecture</h2>"
  if (!rawContent.includes('Figure 8.2:')) {
    rawContent = rawContent.replace(
      '<h2>The Three-Tier Attachment Architecture</h2>',
      svgBlock + '\n\n<h2>The Three-Tier Attachment Architecture</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Wedding Band) right after "<h3>The Master Floor Script: The Companion Presentation</h3>"
  if (!rawContent.includes('The Wedding Band Early-Look Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Master Floor Script: The Companion Presentation</h3>',
      '<h3>The Master Floor Script: The Companion Presentation</h3>\n\n' + cardWeddingBand
    );
  }

  // 4. Insert Dialogue Card 2 (Care Kit) right after "<h3>The Two-Touch Care Presentation</h3>"
  if (!rawContent.includes('The Hospitality Care Kit Bridge Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Two-Touch Care Presentation</h3>',
      '<h3>The Two-Touch Care Presentation</h3>\n\n' + cardCareKit
    );
  }

  // 5. Insert Dialogue Card 3 (Protection) right after "<h3>The Script: Framing Protection as Love, Not Fear</h3>"
  if (!rawContent.includes('The Peace-of-Mind Protection Framing Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Script: Framing Protection as Love, Not Fear</h3>',
      '<h3>The Script: Framing Protection as Love, Not Fear</h3>\n\n' + cardProtection
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m08_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M08-add-ons-protection-plans-and-care-products-done-ethically.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1572 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1572,
    content: rawContent
  }, 801);
  console.log('Page 1572 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1774 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 802).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 803).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 804).catch(() => {});

  // Insert Figure 8.2 into Lesson 1774 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'Figure 8.2:',
    replace: 'Figure 8.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 8.2 and Dialogue Cards into Lesson 1774...');
    await callMcpTool('wp_replace_in_post', {
      id: 1774,
      field: 'post_content',
      search: '<h2>The Three-Tier Attachment Architecture</h2>',
      replace: svgBlock + '\n\n<h2>The Three-Tier Attachment Architecture</h2>',
      max_replacements: 1
    }, 805);
  }

  // Insert Wedding Band Card into Lesson 1774
  const checkWB = await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'The Wedding Band Early-Look Protocol&trade;',
    replace: 'The Wedding Band Early-Look Protocol&trade;',
    max_replacements: -1
  });
  if (checkWB.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1774,
      field: 'post_content',
      search: '<h3>The Master Floor Script: The Companion Presentation</h3>',
      replace: '<h3>The Master Floor Script: The Companion Presentation</h3>\n\n' + cardWeddingBand,
      max_replacements: 1
    }, 806);
  }

  // Insert Care Kit Card into Lesson 1774
  const checkCK = await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'The Hospitality Care Kit Bridge Protocol&trade;',
    replace: 'The Hospitality Care Kit Bridge Protocol&trade;',
    max_replacements: -1
  });
  if (checkCK.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1774,
      field: 'post_content',
      search: '<h3>The Two-Touch Care Presentation</h3>',
      replace: '<h3>The Two-Touch Care Presentation</h3>\n\n' + cardCareKit,
      max_replacements: 1
    }, 807);
  }

  // Insert Protection Card into Lesson 1774
  const checkProt = await callMcpTool('wp_replace_in_post', {
    id: 1774,
    field: 'post_content',
    search: 'The Peace-of-Mind Protection Framing Protocol&trade;',
    replace: 'The Peace-of-Mind Protection Framing Protocol&trade;',
    max_replacements: -1
  });
  if (checkProt.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1774,
      field: 'post_content',
      search: '<h3>The Script: Framing Protection as Love, Not Fear</h3>',
      replace: '<h3>The Script: Framing Protection as Love, Not Fear</h3>\n\n' + cardProtection,
      max_replacements: 1
    }, 808);
  }

  console.log('=== Step 4: Verification Audit of Both 1572 and 1774 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 8.2:', 'The Wedding Band Early-Look Protocol',
    'The Hospitality Care Kit Bridge Protocol', 'The Peace-of-Mind Protection Framing Protocol'
  ];
  for (const id of [1572, 1774]) {
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

  console.log('=== C2-M08 Deployment & Verification Complete! ===');
}

deployM08().catch(console.error);
