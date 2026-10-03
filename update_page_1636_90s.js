const fs = require('fs');

async function run() {
  const WP_URL = 'https://jewelswell.com';
  const API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443';
  const endpoint = `${WP_URL}/wp-json/easy-mcp-ai/v1/mcp`;
  
  console.log('Fetching live page 1636...');
  const resGet = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method: 'tools/call',
      params: {
        name: 'wp_get_page',
        arguments: { page_id: 1636 }
      }
    })
  });
  
  const dataGet = await resGet.json();
  const page = JSON.parse(dataGet.result.content[0].text);
  
  const oldSrc = 'https://jewelswell.com/wp-content/uploads/2026/10/c6_m01_the_modern_bridal_buyers_journey_master.mp4';
  const newSrc = 'https://jewelswell.com/wp-content/uploads/2026/10/c6_m01_masterclass_90s_executive_lesson.mp4';
  
  if (!page.content.includes(oldSrc)) {
    console.log('Warning: oldSrc not found, checking if already updated or looking for video tag');
  }
  
  let updatedContent = page.content.replace(oldSrc, newSrc);
  updatedContent = updatedContent.replace('4K Master &bull; 1080p Stream', 'Executive Master &bull; 100s Full Lesson &bull; 1080p');
  updatedContent = updatedContent.replace('Jewelswell Production &bull; 1080p HD', 'Jewelswell Production &bull; 100s Master &bull; 1080p HD');
  
  console.log('Updating page 1636 with 100-second master video...');
  const resUp = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 2,
      method: 'tools/call',
      params: {
        name: 'wp_update_page',
        arguments: {
          page_id: 1636,
          content: updatedContent
        }
      }
    })
  });
  
  const dataUp = await resUp.json();
  console.log('Update Result:', JSON.stringify(dataUp, null, 2));
}

run().catch(console.error);
