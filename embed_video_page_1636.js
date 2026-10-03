const fs = require('fs');

async function run() {
  const WP_URL = 'https://jewelswell.com';
  const API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443';
  const endpoint = `${WP_URL}/wp-json/easy-mcp-ai/v1/mcp`;
  
  const page = JSON.parse(fs.readFileSync('courses/C6-bridal-engagement-mastery/videos/page_1636_backup.json', 'utf8'));
  
  const videoPlayerHtml = `

<!-- === JEWELSWELL MASTERCLASS EXECUTIVE VIDEO PLAYER === -->
<div class="jw-video-masterclass-container" style="margin: 32px 0 40px 0; background: #0b0f17; border-radius: 16px; overflow: hidden; border: 1px solid #334155; box-shadow: 0 16px 40px rgba(0,0,0,0.35);">
  <div style="padding: 14px 20px; background: linear-gradient(90deg, #0b0f17 0%, #1e293b 100%); border-bottom: 1px solid rgba(226,232,240,0.1); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #dfbe54; box-shadow: 0 0 10px #dfbe54;"></span>
      <span style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: #dfbe54;">Executive Masterclass Video &bull; Module 1</span>
    </div>
    <span style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.08em; background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 4px;">Jewelswell Production &bull; 1080p HD</span>
  </div>
  <div style="position: relative; width: 100%; aspect-ratio: 16/9; background: #000000;">
    <video controls preload="metadata" poster="https://jewelswell.com/wp-content/uploads/2026/10/c6_m01_video_poster.jpg" style="width: 100%; height: 100%; display: block; object-fit: contain;">
      <source src="https://jewelswell.com/wp-content/uploads/2026/10/c6_m01_the_modern_bridal_buyers_journey_master.mp4" type="video/mp4">
      Your browser does not support HTML5 video playback.
    </video>
  </div>
  <div style="padding: 14px 20px; background: #0f172a; border-top: 1px solid rgba(226,232,240,0.08); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
    <div style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; font-size: 13px; color: #e2e8f0;">
      <strong style="color: #dfbe54;">Instructor:</strong> Neelkanth Mahtani &bull; Executive Luxury Gemology &amp; Sales Director
    </div>
    <div style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; font-size: 12px; color: #94a3b8;">
      Featuring GIA Scintillation Dynamics &bull; 18K Yellow Gold Solitaire &bull; Toi et Moi Composition
    </div>
  </div>
</div>
<!-- === END JEWELSWELL MASTERCLASS EXECUTIVE VIDEO PLAYER === -->

`;

  const targetHeading = "<h1>Module 1: The Modern Bridal Buyer's Journey</h1>";
  if (!page.content.includes(targetHeading)) {
    throw new Error('Target heading not found in content!');
  }
  
  const updatedContent = page.content.replace(targetHeading, targetHeading + videoPlayerHtml);
  
  console.log('Sending update to page 1636...');
  const res = await fetch(endpoint, {
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
        name: 'wp_update_page',
        arguments: {
          page_id: 1636,
          content: updatedContent
        }
      }
    })
  });
  
  const data = await res.json();
  console.log('Update result:', JSON.stringify(data, null, 2));
}

run().catch(console.error);
