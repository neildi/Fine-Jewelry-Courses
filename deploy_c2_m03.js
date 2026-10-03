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

// Master SVG Block for Figure 3.4
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M3" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M3" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="480" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The FBES Presentation Architecture™ &amp; Ownership Funnel</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Translating Technical Gemology into Emotional Endowment</text>

      <!-- Left Side: 4-Tier FBES Ladder -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The 4-Tier FBES Ladder™</text>

      <!-- Tier 4: STORY -->
      <rect x="40" y="115" width="280" height="52" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="2"/>
      <text x="55" y="137" font-size="13" font-weight="700" fill="#dfbe54">4. STORY (Provenance &amp; Heritage)</text>
      <text x="55" y="153" font-size="11" fill="#94a3b8">Kimberlite origin, atelier craft, royal legacy, milestone</text>

      <line x1="180" y1="167" x2="180" y2="179" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M3)"/>

      <!-- Tier 3: EMOTION -->
      <rect x="40" y="180" width="280" height="52" rx="6" fill="#1e293b" stroke="#c9a227" stroke-width="1.5"/>
      <text x="55" y="202" font-size="13" font-weight="700" fill="#ffffff">3. EMOTION (Psychological Resonance)</text>
      <text x="55" y="218" font-size="11" fill="#cbd5e1">Room command, quiet pride, peace of mind, love anchor</text>

      <line x1="180" y1="232" x2="180" y2="244" stroke="#c9a227" stroke-width="2" marker-end="url(#jwArrowC2M3)"/>

      <!-- Tier 2: BENEFIT -->
      <rect x="40" y="245" width="280" height="52" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="55" y="267" font-size="13" font-weight="700" fill="#0f172a">2. BENEFIT (Mechanical &amp; Optical)</text>
      <text x="55" y="283" font-size="11" fill="#475569">Zero light leakage, snag-free bezel, generational wear</text>

      <line x1="180" y1="297" x2="180" y2="309" stroke="#94a3b8" stroke-width="2" marker-end="url(#jwArrowC2M3)"/>

      <!-- Tier 1: FEATURE -->
      <rect x="40" y="310" width="280" height="52" rx="6" fill="#f1f5f9" stroke="#e2e8f0" stroke-width="1.5"/>
      <text x="55" y="332" font-size="13" font-weight="700" fill="#64748b">1. FEATURE (Gemological Specs)</text>
      <text x="55" y="348" font-size="11" fill="#64748b">Triple Ex, 57% table, 950 Pt, VS1 &bull; Spec-Sheet Trap!</text>

      <rect x="40" y="375" width="280" height="34" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
      <text x="180" y="396" text-anchor="middle" font-size="11" fill="#b91c1c" font-weight="600">&times; Feature Only = Algorithmic Price Shopping</text>

      <!-- Divider -->
      <line x1="360" y1="90" x2="360" y2="440" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Side: The Physical Choreography -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">The Physical Ownership Arc™</text>

      <!-- Step 1: Velvet Tray -->
      <rect x="400" y="115" width="280" height="70" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="425" cy="138" r="12" fill="#0b0f17"/>
      <text x="425" y="142" text-anchor="middle" font-size="11" fill="#dfbe54" font-weight="700">1</text>
      <text x="448" y="137" font-size="13" font-weight="700" fill="#0b0f17">The Velvet Tray Discipline</text>
      <text x="448" y="155" font-size="11" fill="#475569">&bull; Pad is the sacred stage (Microfiber handle)</text>
      <text x="448" y="171" font-size="11" fill="#475569">&bull; Two-piece ceiling (Zero cognitive overload)</text>

      <!-- Step 2: 10x Loupe -->
      <rect x="400" y="195" width="280" height="70" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="425" cy="218" r="12" fill="#0b0f17"/>
      <text x="425" y="222" text-anchor="middle" font-size="11" fill="#dfbe54" font-weight="700">2</text>
      <text x="448" y="217" font-size="13" font-weight="700" fill="#0b0f17">The 10x Loupe Initiation</text>
      <text x="448" y="235" font-size="11" fill="#475569">&bull; Radical transparency demystifies gemstone</text>
      <text x="448" y="251" font-size="11" fill="#0284c7" font-weight="600">&bull; Transitions dynamic to co-connoisseurs</text>

      <!-- Step 3: Skin Transfer & Mirror -->
      <rect x="400" y="275" width="280" height="85" rx="8" fill="#fdfbf7" stroke="#dfbe54" stroke-width="2"/>
      <circle cx="425" cy="298" r="12" fill="#c9a227"/>
      <text x="425" y="302" text-anchor="middle" font-size="11" fill="#ffffff" font-weight="700">3</text>
      <text x="448" y="297" font-size="13" font-weight="700" fill="#0b0f17">Psychological Try-On &amp; Mirror</text>
      <text x="448" y="315" font-size="11" fill="#475569">&bull; Assumptive transfer: metal warms to 98.6&deg;F</text>
      <text x="448" y="331" font-size="11" fill="#475569">&bull; 3 paces back: full silhouette viewing</text>
      <text x="448" y="347" font-size="11" fill="#15803d" font-weight="700">&bull; 5-Second Golden Silence™ (Let ownership sink in)</text>

      <rect x="400" y="375" width="280" height="34" rx="6" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
      <text x="540" y="396" text-anchor="middle" font-size="11" fill="#15803d" font-weight="600">&check; Skin Contact + Silence = Irreversible Endowment</text>

      <text x="360" y="462" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; FBES Matrix &amp; Physical Choreography</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 3.4:</strong> The FBES Presentation Architecture&trade; &amp; Physical Ownership Arc &mdash; <span style="color: #475569;">Dual framework uniting 4-tier value translation with the behavioral neuroscience of the Endowment Effect.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardLoupe = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The 10x Loupe Initiation Protocol&trade; &bull; Client Engagement Simulation</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Have you ever had the opportunity to look into a high-jewelry diamond through a master cutter's 10x loupe?&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;No, honestly I haven't. It always looked a bit intimidating!&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;It is pure optical magic. Rest the loupe rim right against your eye or glasses. Keep both eyes open to relax your vision. Now, bring the ring up to within an inch of the lens until the table facets snap into view. Look at how crisp those chevron junction lines are&mdash;that razor symmetry is what creates the blinding fire you noticed from across the room.&rdquo;</p>
  </div>
</div>
`;

const cardMirror = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Assumptive Try-On &amp; 5-Second Golden Silence Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Extending ring gracefully by the shank)</em> &ldquo;Slide this onto your ring finger. Let's see how this proportion and knife-edge shank balance against your hand.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Slips the ring on, hand touches warm metal)</em> &ldquo;Oh wow... that feels surprisingly substantial.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Hands angled mirror, steps back three paces)</em> &ldquo;Take a look right here. Step back three paces and let your arm drop naturally to your side. That is how the world will see you wearing it.&rdquo; <em>(Maintains 5 full seconds of respectful Golden Silence)</em></p>
  </div>
</div>
`;

const cardFBES = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The 4-Tier FBES Luxury Translation Script&trade; &bull; Bridal Solitaire Execution</div>
  <div style="margin-bottom: 10px;">
    <strong style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Tier 1: Feature</strong>
    <p style="margin: 4px 0 0 0; color: #1e293b;">&ldquo;This center stone is a GIA Triple Excellent cut grade in 950 hand-forged platinum with an exact 57% table and 34.5&deg; crown angle.&rdquo;</p>
  </div>
  <div style="margin-bottom: 10px;">
    <strong style="color: #0284c7; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Tier 2: Benefit</strong>
    <p style="margin: 4px 0 0 0; color: #1e293b;">&ldquo;What that exact geometry achieves is zero light leakage. Every beam entering the crown bounces internally like a mirrored chamber and explodes back out as white brilliance and rainbow dispersion, while the platinum shank holds it with absolute lifelong security.&rdquo;</p>
  </div>
  <div style="margin-bottom: 10px;">
    <strong style="color: #c9a227; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Tier 3: Emotion</strong>
    <p style="margin: 4px 0 0 0; color: #1e293b;">&ldquo;When you walk into an evening celebration or a candlelit dinner, this ring commands the room before you speak a single word. You get the quiet serenity of knowing you wear unmatched optical life that never dims.&rdquo;</p>
  </div>
  <div>
    <strong style="color: #dfbe54; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Tier 4: Story</strong>
    <p style="margin: 4px 0 0 0; color: #0b0f17; font-weight: 500;">&ldquo;Fewer than five percent of diamonds mined on earth can be cut to this relentless standard of precision. The master cutter chose to sacrifice precious carat weight from the raw rough crystal solely so that this diamond would possess a legendary optical life.&rdquo;</p>
  </div>
</div>
`;

async function deployM03() {
  console.log('=== Step 1: Reading and Updating Local Markdown File ===');
  let rawContent = fs.readFileSync('production_page_1560_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Translating the 4Cs into Romance: Why Men and Women Buy Diamonds.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The 4-Tier Presentation Architecture™: Translating Gemological Specs into Romance and Lifelong Sentiment.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 3.4 right before "<h2>Worked Master FBES Scripts</h2>"
  if (!rawContent.includes('Figure 3.4:')) {
    rawContent = rawContent.replace(
      '<h2>Worked Master FBES Scripts</h2>',
      svgBlock + '\n\n<h2>Worked Master FBES Scripts</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Loupe) right after "<h3>The Psychological Impact of the Loupe</h3>"
  if (!rawContent.includes('The 10x Loupe Initiation Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Psychological Impact of the Loupe</h3>',
      cardLoupe + '\n\n<h3>The Psychological Impact of the Loupe</h3>'
    );
  }

  // 4. Insert Dialogue Card 2 (Mirror) right after "<h3>The Mirror Moment</h3>"
  if (!rawContent.includes('The Assumptive Try-On &amp; 5-Second Golden Silence Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>The Mirror Moment</h3>',
      cardMirror + '\n\n<h3>The Mirror Moment</h3>'
    );
  }

  // 5. Insert Dialogue Card 3 (FBES) right before "<h2>The FBES Translation Matrix: Floor Reference Guide</h2>"
  if (!rawContent.includes('The 4-Tier FBES Luxury Translation Script&trade;')) {
    rawContent = rawContent.replace(
      '<h2>The FBES Translation Matrix: Floor Reference Guide</h2>',
      cardFBES + '\n\n<h2>The FBES Translation Matrix: Floor Reference Guide</h2>'
    );
  }

  // Save the full updated HTML payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m03_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated markdown file
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M03-presenting-piece-story-craft-value.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1560 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1560,
    content: rawContent
  }, 301);
  console.log('Page 1560 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1764 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 302).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 303).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 304).catch(() => {});

  // Insert Figure 3.4 into Lesson 1764 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'Figure 3.4:',
    replace: 'Figure 3.4:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 3.4 and Dialogue Cards into Lesson 1764...');
    await callMcpTool('wp_replace_in_post', {
      id: 1764,
      field: 'post_content',
      search: '<h2>Worked Master FBES Scripts</h2>',
      replace: svgBlock + '\n\n<h2>Worked Master FBES Scripts</h2>',
      max_replacements: 1
    }, 305);
  }

  // Insert Loupe Card into Lesson 1764
  const checkLoupe = await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'The 10x Loupe Initiation Protocol&trade;',
    replace: 'The 10x Loupe Initiation Protocol&trade;',
    max_replacements: -1
  });
  if (checkLoupe.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1764,
      field: 'post_content',
      search: '<h3>The Psychological Impact of the Loupe</h3>',
      replace: cardLoupe + '\n\n<h3>The Psychological Impact of the Loupe</h3>',
      max_replacements: 1
    }, 306);
  }

  // Insert Mirror Card into Lesson 1764
  const checkMirror = await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'The Assumptive Try-On &amp; 5-Second Golden Silence Protocol&trade;',
    replace: 'The Assumptive Try-On &amp; 5-Second Golden Silence Protocol&trade;',
    max_replacements: -1
  });
  if (checkMirror.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1764,
      field: 'post_content',
      search: '<h3>The Mirror Moment</h3>',
      replace: cardMirror + '\n\n<h3>The Mirror Moment</h3>',
      max_replacements: 1
    }, 307);
  }

  // Insert FBES Card into Lesson 1764
  const checkFBES = await callMcpTool('wp_replace_in_post', {
    id: 1764,
    field: 'post_content',
    search: 'The 4-Tier FBES Luxury Translation Script&trade;',
    replace: 'The 4-Tier FBES Luxury Translation Script&trade;',
    max_replacements: -1
  });
  if (checkFBES.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1764,
      field: 'post_content',
      search: '<h2>The FBES Translation Matrix: Floor Reference Guide</h2>',
      replace: cardFBES + '\n\n<h2>The FBES Translation Matrix: Floor Reference Guide</h2>',
      max_replacements: 1
    }, 308);
  }

  console.log('=== Step 4: Verification Audit of Both 1560 and 1764 ===');
  const terms = ['Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales', '.c1-article-container', 'Figure 3.4:', 'The 10x Loupe Initiation Protocol'];
  for (const id of [1560, 1764]) {
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

  console.log('=== C2-M03 Deployment & Verification Complete! ===');
}

deployM03().catch(console.error);
