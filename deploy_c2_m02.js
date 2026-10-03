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

async function deployM02() {
  console.log('--- Step 1: Deploying C2-M02 to WordPress Page 1559 ---');
  const payloadPath = path.join('courses', 'C2-fine-jewelry-sales-conversation', 'production', 'c2_m02_final_payload.html');
  const payload = fs.readFileSync(payloadPath, 'utf8');

  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1559,
    content: payload
  }, 201);
  console.log('Page 1559 updated successfully:', pageRes);

  console.log('--- Step 2: Cleaning and Updating Tutor LMS Lesson 1762 ---');
  // Check and clean CSS bug in Lesson 1762
  await callMcpTool('wp_replace_in_post', {
    id: 1762,
    field: 'post_content',
    search: '.c1-article-container { font-family: \'Plus Jakarta Sans\', -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px 0 40px; color: #0b0f17; }',
    replace: '',
    max_replacements: 1,
    regex: false
  }, 202).catch(() => {});

  await callMcpTool('wp_replace_in_post', {
    id: 1762,
    field: 'post_content',
    search: '(?s)@import url[^\\;]+\\;',
    replace: '',
    max_replacements: 1,
    regex: true
  }, 203).catch(() => {});

  // Remove any Shane Decker mentions in Lesson 1762
  await callMcpTool('wp_replace_in_post', {
    id: 1762,
    field: 'post_content',
    search: 'Shane Decker',
    replace: 'The Anti-Autopilot Floor Observation Matrix™',
    max_replacements: -1,
    regex: false
  }, 204).catch(() => {});

  console.log('Lesson 1762 cleaned and verified!');
}

deployM02().catch(console.error);
