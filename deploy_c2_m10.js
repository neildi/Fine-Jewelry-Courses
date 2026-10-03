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

// Master SVG Block for Figure 10.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M10" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M10" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Deliberate Practice Engine™ &amp; Peer Coaching Matrix</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; 4-Week Rotation Cadence &amp; 5-Point Peer Debrief Scoring</text>

      <!-- Left Column: The 4-Week Spaced Repetition Cadence -->
      <text x="180" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">4-Week Rotation Cadence™</text>

      <!-- Week 1 -->
      <rect x="35" y="115" width="290" height="56" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="143" r="11" fill="#0b0f17"/>
      <text x="58" y="147" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">W1</text>
      <text x="78" y="138" font-size="12" font-weight="700" fill="#0b0f17">Greeting &amp; Discovery Fluidity</text>
      <text x="78" y="154" font-size="11" fill="#475569">First 90s decomp &bull; 7 Pillars &bull; 30s synthesis</text>

      <!-- Week 2 -->
      <rect x="35" y="180" width="290" height="56" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="208" r="11" fill="#0b0f17"/>
      <text x="58" y="212" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">W2</text>
      <text x="78" y="203" font-size="12" font-weight="700" fill="#0b0f17">FBES &amp; 10x Loupe Initiation</text>
      <text x="78" y="219" font-size="11" fill="#475569">Tray discipline &bull; Loupe guide &bull; Mirror moment</text>

      <!-- Week 3 -->
      <rect x="35" y="245" width="290" height="56" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="273" r="11" fill="#0b0f17"/>
      <text x="58" y="277" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">W3</text>
      <text x="78" y="268" font-size="12" font-weight="700" fill="#0b0f17">AARE &amp; Margin Protection</text>
      <text x="78" y="284" font-size="11" fill="#475569">Zero-discount stand &bull; Cost-per-wear &bull; Spec shift</text>

      <!-- Week 4 -->
      <rect x="35" y="310" width="290" height="56" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="58" cy="338" r="11" fill="#0b0f17"/>
      <text x="58" y="342" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">W4</text>
      <text x="78" y="333" font-size="12" font-weight="700" fill="#0b0f17">Tri-Modal Closing &amp; Silence</text>
      <text x="78" y="349" font-size="11" fill="#15803d" font-weight="600">Assumptive, Choice &amp; Milestone &bull; 10s Mute</text>

      <!-- 15-Minute Huddle Architecture -->
      <rect x="35" y="375" width="290" height="52" rx="6" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="180" y="396" text-anchor="middle" font-size="11" fill="#0b0f17" font-weight="700">The 15-Minute Morning Huddle™</text>
      <text x="180" y="413" text-anchor="middle" font-size="10.5" fill="#64748b">3m Warmup &rarr; 8m Live Simulation &rarr; 4m Peer Rubric</text>

      <!-- Center Divider -->
      <line x1="360" y1="90" x2="360" y2="445" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Right Column: 5-Point Peer Debrief Rubric -->
      <text x="540" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17" text-transform="uppercase" letter-spacing="0.05em">5-Point Peer Rubric™</text>

      <rect x="395" y="115" width="290" height="250" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      
      <!-- Rubric 1 -->
      <text x="410" y="140" font-size="11" font-weight="700" fill="#0b0f17">1. Spatial Proxemics &amp; 45&deg; Stance</text>
      <text x="665" y="140" text-anchor="end" font-size="11" fill="#c9a227" font-weight="700">/ 5 pts</text>
      <text x="410" y="156" font-size="10" fill="#64748b">Collaborative side-by-side positioning without counter barrier</text>
      <line x1="410" y1="165" x2="665" y2="165" stroke="#f1f5f9" stroke-width="1"/>

      <!-- Rubric 2 -->
      <text x="410" y="185" font-size="11" font-weight="700" fill="#0b0f17">2. 30-Second Discovery Synthesis</text>
      <text x="665" y="185" text-anchor="end" font-size="11" fill="#c9a227" font-weight="700">/ 5 pts</text>
      <text x="410" y="201" font-size="10" fill="#64748b">Restates client vision accurately before touching showcase key</text>
      <line x1="410" y1="210" x2="665" y2="210" stroke="#f1f5f9" stroke-width="1"/>

      <!-- Rubric 3 -->
      <text x="410" y="230" font-size="11" font-weight="700" fill="#0b0f17">3. FBES Emotional Translation</text>
      <text x="665" y="230" text-anchor="end" font-size="11" fill="#c9a227" font-weight="700">/ 5 pts</text>
      <text x="410" y="246" font-size="10" fill="#64748b">Converts 4Cs numbers into optical romance and life sentiment</text>
      <line x1="410" y1="255" x2="665" y2="255" stroke="#f1f5f9" stroke-width="1"/>

      <!-- Rubric 4 -->
      <text x="410" y="275" font-size="11" font-weight="700" fill="#0b0f17">4. AARE Objection Holding Line</text>
      <text x="665" y="275" text-anchor="end" font-size="11" fill="#c9a227" font-weight="700">/ 5 pts</text>
      <text x="410" y="291" font-size="10" fill="#64748b">Validates budget without discounting; offers spec-shift</text>
      <line x1="410" y1="300" x2="665" y2="300" stroke="#f1f5f9" stroke-width="1"/>

      <!-- Rubric 5 -->
      <text x="410" y="320" font-size="11" font-weight="700" fill="#0b0f17">5. Golden Silence Discipline</text>
      <text x="665" y="320" text-anchor="end" font-size="11" fill="#15803d" font-weight="700">/ 5 pts</text>
      <text x="410" y="336" font-size="10" fill="#64748b">Holds 5-10s mute after closing ask with warm eye contact</text>

      <line x1="410" y1="345" x2="665" y2="345" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="410" y="360" font-size="11" font-weight="800" fill="#0b0f17">Total Target Score:</text>
      <text x="665" y="360" text-anchor="end" font-size="12" font-weight="800" fill="#15803d">22 / 25 pts (Master Standard)</text>

      <!-- Bottom Law Box -->
      <rect x="395" y="375" width="290" height="52" rx="6" fill="#0b0f17" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="540" y="396" text-anchor="middle" font-size="10.5" fill="#dfbe54" font-weight="700">The Deliberate Practice Law™</text>
      <text x="540" y="412" text-anchor="middle" font-size="10" fill="#ffffff" font-style="italic">&ldquo;Amateurs practice until they get it right;</text>
      <text x="540" y="423" text-anchor="middle" font-size="10" fill="#ffffff" font-style="italic">Masters practice until they cannot get it wrong.&rdquo;</text>

      <!-- Copyright Footer -->
      <text x="360" y="480" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; Practice Cadence &amp; Peer Rubrics</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 10.2:</strong> The Deliberate Practice Engine&trade; &amp; Peer Coaching Matrix &mdash; <span style="color: #475569;">Weekly 15-minute salon drill framework and 25-point peer evaluation rubric ensuring consistent luxury excellence under pressure.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardSimGuarded = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">Master Simulation Drill: The Guarded Engagement Buyer &bull; 45&deg; Stance</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Peer Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Shoulders tense, arms half-crossed, browsing vitrine nervously)</em> &ldquo;I'm just browsing for engagement rings... not buying anything today.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Takes collaborative 45-degree angle, eyes aligned on vitrine &bull; Zero sales pressure)</em> &ldquo;Welcome! You are in the absolute best part of the journey. Exploring styles without any timeline is the most enjoyable way to discover what speaks to you. Take all the time you need, and if you would like me to pull out a loupe or slide anything onto a velvet pad, I am right here.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #fdfbf7; color: #c9a227; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid #dfbe54; white-space: nowrap;">Coaching</span>
    <p style="margin: 0; color: #64748b; font-style: italic;"><strong>Debrief Focus:</strong> Notice how the advisor's 45-degree stance and unconditional liberation instantly lowers the buyer's heart rate, inviting them to ask a question within 60 seconds.</p>
  </div>
</div>
`;

const cardSimHaggler = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">Master Simulation Drill: The Aggressive Discount Push &bull; AARE Defense</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Peer Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;Look, I'll take this 2.50ct platinum solitaire right now for cash, but you have to knock twenty percent off the tag.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Unflinching warm smile &bull; AARE Step 1 &amp; 2)</em> &ldquo;I admire a decisive buyer, and I respect your directness. Our prices are strictly calculated to reflect true optical rarity and in-house master fabrication, so our price is firm. We never inflate tags just to bargain down later.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(AARE Step 4: Spec Shift)</em> &ldquo;If staying within that exact dollar amount is your priority, let me show you this sister stone with identical 8.8mm spread in a G-VS1. It looks identical across a room and hits your exact budget without cutting corners on craft. Let's compare them on the pad.&rdquo;</p>
  </div>
</div>
`;

const cardPeerDebrief = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The 3-Minute Peer Debrief Protocol&trade; &bull; Objective Coaching Script</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Peer Coach</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Your 30-second discovery synthesis was textbook&mdash;you scored 5/5 on active listening because you repeated her exact words about clinical gloves. However, during the closing ask, you spoke after only two seconds of silence when she hesitated on sizing.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Peer Coach</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;Let's re-run just the final 30 seconds: Deliver the assumptive question about Friday delivery, then lock your posture, maintain warm eye contact, and count silently to seven before saying a single word. Reset and go!&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #fdfbf7; color: #c9a227; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid #dfbe54; white-space: nowrap;">Result</span>
    <p style="margin: 0; color: #64748b; font-style: italic;">Instant micro-correction builds muscle memory. The associate masters the silence rule without risking real revenue on the showroom floor.</p>
  </div>
</div>
`;

async function deployM10() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1576_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Mastering the Floor: 50 Scenarios Every Diamond Salesperson Must Rehearse.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The Deliberate Practice Engine™: Salon Simulations and Peer Coaching for High-Ticket Advisors.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 10.2 right before "<h2>The Deliberate Practice Framework</h2>"
  if (!rawContent.includes('Figure 10.2:')) {
    rawContent = rawContent.replace(
      '<h2>The Deliberate Practice Framework</h2>',
      svgBlock + '\n\n<h2>The Deliberate Practice Framework</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Guarded) right after "<h2>Master Simulation A: The Guarded First-Time Engagement Buyer</h2>"
  if (!rawContent.includes('Master Simulation Drill: The Guarded Engagement Buyer')) {
    rawContent = rawContent.replace(
      '<h2>Master Simulation A: The Guarded First-Time Engagement Buyer</h2>',
      '<h2>Master Simulation A: The Guarded First-Time Engagement Buyer</h2>\n\n' + cardSimGuarded
    );
  }

  // 4. Insert Dialogue Card 2 (Haggler) right after "<h2>Master Simulation B: The Aggressive Price Haggler</h2>"
  if (!rawContent.includes('Master Simulation Drill: The Aggressive Discount Push')) {
    rawContent = rawContent.replace(
      '<h2>Master Simulation B: The Aggressive Price Haggler</h2>',
      '<h2>Master Simulation B: The Aggressive Price Haggler</h2>\n\n' + cardSimHaggler
    );
  }

  // 5. Insert Dialogue Card 3 (Peer Debrief) right after "<h2>The 5-Point Peer Debrief Scoring Rubric</h2>"
  if (!rawContent.includes('The 3-Minute Peer Debrief Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h2>The 5-Point Peer Debrief Scoring Rubric</h2>',
      '<h2>The 5-Point Peer Debrief Scoring Rubric</h2>\n\n' + cardPeerDebrief
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m10_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M10-role-play-scripts-and-a-weekly-practice-cadence.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1576 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1576,
    content: rawContent
  }, 1001);
  console.log('Page 1576 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1778 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 1002).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 1003).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 1004).catch(() => {});

  // Insert Figure 10.2 into Lesson 1778 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'Figure 10.2:',
    replace: 'Figure 10.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 10.2 and Dialogue Cards into Lesson 1778...');
    await callMcpTool('wp_replace_in_post', {
      id: 1778,
      field: 'post_content',
      search: '<h2>The Deliberate Practice Framework</h2>',
      replace: svgBlock + '\n\n<h2>The Deliberate Practice Framework</h2>',
      max_replacements: 1
    }, 1005);
  }

  // Insert Guarded Card into Lesson 1778
  const checkGuard = await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'Master Simulation Drill: The Guarded Engagement Buyer',
    replace: 'Master Simulation Drill: The Guarded Engagement Buyer',
    max_replacements: -1
  });
  if (checkGuard.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1778,
      field: 'post_content',
      search: '<h2>Master Simulation A: The Guarded First-Time Engagement Buyer</h2>',
      replace: '<h2>Master Simulation A: The Guarded First-Time Engagement Buyer</h2>\n\n' + cardSimGuarded,
      max_replacements: 1
    }, 1006);
  }

  // Insert Haggler Card into Lesson 1778
  const checkHag = await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'Master Simulation Drill: The Aggressive Discount Push',
    replace: 'Master Simulation Drill: The Aggressive Discount Push',
    max_replacements: -1
  });
  if (checkHag.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1778,
      field: 'post_content',
      search: '<h2>Master Simulation B: The Aggressive Price Haggler</h2>',
      replace: '<h2>Master Simulation B: The Aggressive Price Haggler</h2>\n\n' + cardSimHaggler,
      max_replacements: 1
    }, 1007);
  }

  // Insert Peer Debrief Card into Lesson 1778
  const checkDeb = await callMcpTool('wp_replace_in_post', {
    id: 1778,
    field: 'post_content',
    search: 'The 3-Minute Peer Debrief Protocol&trade;',
    replace: 'The 3-Minute Peer Debrief Protocol&trade;',
    max_replacements: -1
  });
  if (checkDeb.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1778,
      field: 'post_content',
      search: '<h2>The 5-Point Peer Debrief Scoring Rubric</h2>',
      replace: '<h2>The 5-Point Peer Debrief Scoring Rubric</h2>\n\n' + cardPeerDebrief,
      max_replacements: 1
    }, 1008);
  }

  console.log('=== Step 4: Verification Audit of Both 1576 and 1778 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 10.2:', 'Master Simulation Drill: The Guarded Engagement Buyer',
    'Master Simulation Drill: The Aggressive Discount Push', 'The 3-Minute Peer Debrief Protocol'
  ];
  for (const id of [1576, 1778]) {
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

  console.log('=== C2-M10 Deployment & Verification Complete! ===');
}

deployM10().catch(console.error);
