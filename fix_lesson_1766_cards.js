const fs = require('fs');

const WP_URL = 'https://jewelswell.com';
const API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443';
const endpoint = `${WP_URL}/wp-json/easy-mcp-ai/v1/mcp`;

async function callMcpTool(name, args, id = 1) {
  const headers = {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
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

async function run() {
  console.log('Inserting Sizing Card...');
  const res1 = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: '<h3>Category B: Verbal &amp; Logistical Signals (The Practical Mindset)</h3>',
    replace: '<h3>Category B: Verbal &amp; Logistical Signals (The Practical Mindset)</h3>\n\n' + cardSizing,
    max_replacements: 1,
    regex: false
  });
  console.log('Result Sizing Card:', res1);

  console.log('Inserting Possessive Card...');
  const res2 = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>',
    replace: '<h3>Category C: Linguistic Signals (The Possessive Pronoun Shift)</h3>\n\n' + cardPossessive,
    max_replacements: 1,
    regex: false
  });
  console.log('Result Possessive Card:', res2);

  // Check counts
  const checkS = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Sizing Inquiry',
    replace: 'The Sizing Inquiry',
    max_replacements: -1
  });
  console.log('The Sizing Inquiry count in 1766:', checkS.replacements_count);

  const checkP = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Possessive Pronoun Pivot Protocol',
    replace: 'The Possessive Pronoun Pivot Protocol',
    max_replacements: -1
  });
  console.log('The Possessive Pronoun Pivot Protocol count in 1766:', checkP.replacements_count);

  const checkPart = await callMcpTool('wp_replace_in_post', {
    id: 1766,
    field: 'post_content',
    search: 'The Partner Validation',
    replace: 'The Partner Validation',
    max_replacements: -1
  });
  console.log('The Partner Validation count in 1766:', checkPart.replacements_count);
}

run().catch(console.error);
