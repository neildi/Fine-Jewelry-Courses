const fs = require('fs');

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

async function run() {
  console.log('--- Deploying C2-M01 to WordPress Page 1361 ---');
  const payload = fs.readFileSync('c2_m01_final_payload.html', 'utf8');

  const pageRes = await callMcpTool('wp_update_page', {
    page_id: 1361,
    content: payload
  }, 101);

  console.log('Page 1361 updated successfully:', pageRes);
}

run().catch(console.error);
