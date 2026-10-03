const WP_URL = 'https://jewelswell.com';
const API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443';
const endpoint = `${WP_URL}/wp-json/easy-mcp-ai/v1/mcp`;

async function callMcpTool(name, args, id = 1) {
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    },
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

async function auditPost(id) {
  console.log(`--- Auditing ID: ${id} ---`);
  const terms = ['Shane Decker', 'Decker', 'Kay', 'Effy', 'Blue Nile', 'James Allen', 'Zales', '.c1-article-container', '@import'];
  for (const term of terms) {
    const res = await callMcpTool('wp_replace_in_post', {
      id: id,
      field: 'post_content',
      search: term,
      replace: term,
      max_replacements: -1
    });
    console.log(`  Count of '${term}': ${res.replacements_count}`);
  }
}

async function run() {
  await auditPost(1560); // Page 1560 (C2-M03)
  await auditPost(1764); // Lesson 1764 (C2-M03)
}
run().catch(console.error);
