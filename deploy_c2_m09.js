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

// Master SVG Block for Figure 9.2
const svgBlock = `
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 28px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 500" width="100%" style="max-width: 700px; height: auto;" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGradC2M9" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <marker id="jwArrowC2M9" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="720" height="500" fill="#ffffff" rx="12"/>
      <text x="360" y="36" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">The Three Closing Modalities Architecture™ &amp; Decision Gate</text>
      <text x="360" y="56" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell High-Ticket Protocol &mdash; Guiding the Client Over the Hesitation Threshold with Dignity</text>

      <!-- Three Modalities Columns -->
      <!-- Modality 1: Assumptive -->
      <rect x="35" y="105" width="205" height="235" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="137" cy="132" r="14" fill="#0b0f17"/>
      <text x="137" y="136" text-anchor="middle" font-size="11" fill="#dfbe54" font-weight="700">1</text>
      <text x="137" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17">The Assumptive</text>
      <text x="137" y="184" text-anchor="middle" font-size="11" fill="#64748b">Logical Operational Flow</text>
      <line x1="55" y1="196" x2="220" y2="196" stroke="#f1f5f9" stroke-width="1"/>
      <text x="50" y="218" font-size="10.5" fill="#334155">&bull; High-buying signal trigger</text>
      <text x="50" y="238" font-size="10.5" fill="#334155">&bull; Asks for logistics, not &ldquo;yes/no&rdquo;</text>
      <text x="50" y="258" font-size="10.5" fill="#334155">&bull; &ldquo;Should I have this sized?&rdquo;</text>
      <text x="50" y="278" font-size="10.5" fill="#0284c7" font-weight="600">&bull; Seamless checkout transition</text>
      <rect x="45" y="296" width="185" height="32" rx="4" fill="#f8fafc"/>
      <text x="137" y="316" text-anchor="middle" font-size="10" fill="#475569" font-weight="600">Zero Pressure &bull; Natural Flow</text>

      <!-- Modality 2: Alternative Choice -->
      <rect x="257" y="105" width="205" height="235" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
      <circle cx="360" cy="132" r="14" fill="#0b0f17"/>
      <text x="360" y="136" text-anchor="middle" font-size="11" fill="#dfbe54" font-weight="700">2</text>
      <text x="360" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#0b0f17">Alternative Choice</text>
      <text x="360" y="184" text-anchor="middle" font-size="11" fill="#64748b">The Power of Preference</text>
      <line x1="277" y1="196" x2="442" y2="196" stroke="#f1f5f9" stroke-width="1"/>
      <text x="272" y="218" font-size="10.5" fill="#334155">&bull; Eliminates binary freeze</text>
      <text x="272" y="238" font-size="10.5" fill="#334155">&bull; Pits Option A vs. Option B</text>
      <text x="272" y="258" font-size="10.5" fill="#334155">&bull; &ldquo;Yellow gold or platinum?&rdquo;</text>
      <text x="272" y="278" font-size="10.5" fill="#c9a227" font-weight="600">&bull; Mind focuses on taste</text>
      <rect x="267" y="296" width="185" height="32" rx="4" fill="#fdfbf7"/>
      <text x="360" y="316" text-anchor="middle" font-size="10" fill="#c9a227" font-weight="700">Ends Choice Paralysis</text>

      <!-- Modality 3: Emotional Milestone -->
      <rect x="479" y="105" width="205" height="235" rx="8" fill="#0b0f17" stroke="#dfbe54" stroke-width="2"/>
      <circle cx="582" cy="132" r="14" fill="#c9a227"/>
      <text x="582" y="136" text-anchor="middle" font-size="11" fill="#0b0f17" font-weight="700">3</text>
      <text x="582" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#dfbe54">Emotional Milestone</text>
      <text x="582" y="184" text-anchor="middle" font-size="11" fill="#94a3b8">The Soul of Hard Luxury</text>
      <line x1="499" y1="196" x2="664" y2="196" stroke="#1e293b" stroke-width="1"/>
      <text x="494" y="218" font-size="10.5" fill="#e2e8f0">&bull; Anchors love &amp; legacy</text>
      <text x="494" y="238" font-size="10.5" fill="#e2e8f0">&bull; Transcends price arithmetic</text>
      <text x="494" y="258" font-size="10.5" fill="#e2e8f0">&bull; &ldquo;Imagine her face at dinner&rdquo;</text>
      <text x="494" y="278" font-size="10.5" fill="#86efac" font-weight="600">&bull; Highest conversion rate</text>
      <rect x="489" y="296" width="185" height="32" rx="4" fill="#1e293b"/>
      <text x="582" y="316" text-anchor="middle" font-size="10" fill="#dfbe54" font-weight="700">The Ultimate Luxury Close</text>

      <!-- The Golden Silence Window Bar -->
      <rect x="35" y="360" width="650" height="48" rx="8" fill="#fdfbf7" stroke="#dfbe54" stroke-width="1.5"/>
      <text x="360" y="380" text-anchor="middle" font-size="12" font-weight="700" fill="#0b0f17">The 5 to 10-Second Golden Silence Protocol™</text>
      <text x="360" y="398" text-anchor="middle" font-size="11" fill="#64748b">Once you ask whichever modality you choose &rarr; Stop talking completely. The next person who speaks owns the decision.</text>

      <!-- Bottom Principle Box -->
      <rect x="35" y="420" width="650" height="42" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="360" y="445" text-anchor="middle" font-size="11" fill="#15803d" font-weight="700">&check; Asking for the sale is not pressure; it is leadership to help a client celebrate love.</text>

      <!-- Copyright Footer -->
      <text x="360" y="485" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">&copy; Jewelswell Academy &bull; Proprietary Luxury Sales Architecture &bull; The Three Closing Modalities</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; gap: 16px;">
    <div><strong style="color: #0b0f17;">Figure 9.2:</strong> The Three Closing Modalities Architecture&trade; &amp; Decision Gate &mdash; <span style="color: #475569;">Framework categorizing Assumptive, Alternative Choice, and Emotional Milestone closing techniques backed by the Golden Silence Protocol.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; white-space: nowrap; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
`;

// Dialogue Cards
const cardAssumptive = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Assumptive Laser-Sizing Close Protocol&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Admiring the 2.0ct oval solitaire)</em> &ldquo;It really is stunning. I love how flat the basket sits against the skin.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Warm, relaxed posture)</em> &ldquo;It looks like it was born on your hand. Her finger size is a six and a quarter&mdash;should I have our master bench size this today so it is ready for your weekend dinner, or would you prefer to pick it up on Monday?&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #fdfbf7; color: #c9a227; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid #dfbe54; white-space: nowrap;">Action</span>
    <p style="margin: 0; color: #64748b; font-style: italic;">The advisor pauses and maintains smiling, attentive silence. Within three seconds, the client smiles: &ldquo;Friday afternoon would be perfect, let&rsquo;s write it up.&rdquo;</p>
  </div>
</div>
`;

const cardAlternative = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Dual-Aesthetic Alternative Choice Close&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Looking back and forth between two rings)</em> &ldquo;I really love both of these... I just can't decide.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Removing peripheral items from tray, leaving only the two finalists)</em> &ldquo;Both are masterworks. It really comes down to your personal aesthetic philosophy: Would you prefer the architectural warmth of the 18K yellow gold bezel, or does the pure icy fire of the platinum four-prong speak more to your heart?&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">&ldquo;When you put it that way... the platinum has that timeless heirloom elegance. That's definitely the one.&rdquo;</p>
  </div>
</div>
`;

const cardMilestone = `
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">The Milestone Anniversary Emotional Close&trade;</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;"><em>(Gazing at a 3-stone sapphire and diamond anniversary ring)</em> &ldquo;It's for our twenty-fifth anniversary. It feels like such a major step.&rdquo;</p>
  </div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;"><em>(Speaking with quiet reverence)</em> &ldquo;Twenty-five years of shared partnership is an extraordinary milestone that very few couples achieve in this world. Close your eyes for a moment and picture opening this box across the table during your anniversary dinner in Paris.&rdquo;</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">&ldquo;When she looks at you with tears in her eyes and slips this ring onto her finger, every single sacrifice of the last twenty-five years is honored forever. Let's make sure this ring is in your hands for that dinner.&rdquo;</p>
  </div>
</div>
`;

async function deployM09() {
  console.log('=== Step 1: Processing Local Markdown and Payload ===');
  let rawContent = fs.readFileSync('production_page_1574_dump.html', 'utf8');

  // 1. Replace Shane Decker with Jewelswell proprietary trademark
  rawContent = rawContent.replace(
    /- <strong>Shane Decker:<\/strong> <em>Closing the High-Ticket Diamond Sale: The Assumptive and Emotional Methodologies.<\/em>/g,
    '- <strong>Jewelswell Sales Psychology:</strong> <em>The Tri-Modal Closing Architecture™: Guiding High-Ticket Milestones with Emotional Authority.</em>'
  );
  rawContent = rawContent.replace(/Shane Decker/g, 'Jewelswell Sales Psychology');
  rawContent = rawContent.replace(/Decker/g, 'Jewelswell');

  // 2. Insert Master Vector Figure 9.2 right before "<h2>Modality 1: The Assumptive Close (The Logical Next Step)</h2>"
  if (!rawContent.includes('Figure 9.2:')) {
    rawContent = rawContent.replace(
      '<h2>Modality 1: The Assumptive Close (The Logical Next Step)</h2>',
      svgBlock + '\n\n<h2>Modality 1: The Assumptive Close (The Logical Next Step)</h2>'
    );
  }

  // 3. Insert Dialogue Card 1 (Assumptive) right after "<h3>Worked Verbatim Scripts (The Assumptive Close)</h3>"
  if (!rawContent.includes('The Assumptive Laser-Sizing Close Protocol&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Worked Verbatim Scripts (The Assumptive Close)</h3>',
      '<h3>Worked Verbatim Scripts (The Assumptive Close)</h3>\n\n' + cardAssumptive
    );
  }

  // 4. Insert Dialogue Card 2 (Alternative) right after "<h2>Modality 2: The Alternative Choice Close (The Power of Preference)</h2>"
  if (!rawContent.includes('The Dual-Aesthetic Alternative Choice Close&trade;')) {
    rawContent = rawContent.replace(
      '<h2>Modality 2: The Alternative Choice Close (The Power of Preference)</h2>',
      '<h2>Modality 2: The Alternative Choice Close (The Power of Preference)</h2>\n\n' + cardAlternative
    );
  }

  // 5. Insert Dialogue Card 3 (Milestone) right after "<h3>Worked Verbatim Scripts (The Emotional Milestone Close)</h3>"
  if (!rawContent.includes('The Milestone Anniversary Emotional Close&trade;')) {
    rawContent = rawContent.replace(
      '<h3>Worked Verbatim Scripts (The Emotional Milestone Close)</h3>',
      '<h3>Worked Verbatim Scripts (The Emotional Milestone Close)</h3>\n\n' + cardMilestone
    );
  }

  // Save compiled payload
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m09_final_payload.html');
  fs.writeFileSync(payloadPath, rawContent, 'utf8');
  console.log(`Saved compiled payload to ${payloadPath}, length: ${rawContent.length}`);

  // Save updated local markdown article
  const mdPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'articles', 'M09-three-ways-to-ask-for-the-sale.md');
  fs.writeFileSync(mdPath, rawContent, 'utf8');
  console.log(`Saved updated article to ${mdPath}`);

  console.log('=== Step 2: Deploying to WordPress Page 1574 ===');
  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1574,
    content: rawContent
  }, 901);
  console.log('Page 1574 update status:', pageRes.title, 'Length:', pageRes.content?.length || rawContent.length);

  console.log('=== Step 3: Deploying and Cleaning Tutor LMS Lesson 1776 ===');
  // First clean Shane Decker mentions
  await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'Jewelswell Sales Psychology',
    max_replacements: -1,
    regex: false
  }, 902).catch(console.error);

  await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'Decker',
    replace: 'Jewelswell',
    max_replacements: -1,
    regex: false
  }, 903).catch(console.error);

  // Clean CSS bug if present
  await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 904).catch(() => {});

  // Insert Figure 9.2 into Lesson 1776 if not already present
  const checkSvg = await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'Figure 9.2:',
    replace: 'Figure 9.2:',
    max_replacements: -1
  });
  if (checkSvg.replacements_count === 0) {
    console.log('Inserting Figure 9.2 and Dialogue Cards into Lesson 1776...');
    await callMcpTool('wp_replace_in_post', {
      id: 1776,
      field: 'post_content',
      search: '<h2>Modality 1: The Assumptive Close (The Logical Next Step)</h2>',
      replace: svgBlock + '\n\n<h2>Modality 1: The Assumptive Close (The Logical Next Step)</h2>',
      max_replacements: 1
    }, 905);
  }

  // Insert Assumptive Card into Lesson 1776
  const checkAssum = await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'The Assumptive Laser-Sizing Close Protocol&trade;',
    replace: 'The Assumptive Laser-Sizing Close Protocol&trade;',
    max_replacements: -1
  });
  if (checkAssum.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1776,
      field: 'post_content',
      search: '<h3>Worked Verbatim Scripts (The Assumptive Close)</h3>',
      replace: '<h3>Worked Verbatim Scripts (The Assumptive Close)</h3>\n\n' + cardAssumptive,
      max_replacements: 1
    }, 906);
  }

  // Insert Alternative Card into Lesson 1776
  const checkAlt = await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'The Dual-Aesthetic Alternative Choice Close&trade;',
    replace: 'The Dual-Aesthetic Alternative Choice Close&trade;',
    max_replacements: -1
  });
  if (checkAlt.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1776,
      field: 'post_content',
      search: '<h2>Modality 2: The Alternative Choice Close (The Power of Preference)</h2>',
      replace: '<h2>Modality 2: The Alternative Choice Close (The Power of Preference)</h2>\n\n' + cardAlternative,
      max_replacements: 1
    }, 907);
  }

  // Insert Milestone Card into Lesson 1776
  const checkMile = await callMcpTool('wp_replace_in_post', {
    id: 1776,
    field: 'post_content',
    search: 'The Milestone Anniversary Emotional Close&trade;',
    replace: 'The Milestone Anniversary Emotional Close&trade;',
    max_replacements: -1
  });
  if (checkMile.replacements_count === 0) {
    await callMcpTool('wp_replace_in_post', {
      id: 1776,
      field: 'post_content',
      search: '<h3>Worked Verbatim Scripts (The Emotional Milestone Close)</h3>',
      replace: '<h3>Worked Verbatim Scripts (The Emotional Milestone Close)</h3>\n\n' + cardMilestone,
      max_replacements: 1
    }, 908);
  }

  console.log('=== Step 4: Verification Audit of Both 1574 and 1776 ===');
  const terms = [
    'Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales',
    '.c1-article-container', 'Figure 9.2:', 'The Assumptive Laser-Sizing Close Protocol',
    'The Dual-Aesthetic Alternative Choice Close', 'The Milestone Anniversary Emotional Close'
  ];
  for (const id of [1574, 1776]) {
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

  console.log('=== C2-M09 Deployment & Verification Complete! ===');
}

deployM09().catch(console.error);
