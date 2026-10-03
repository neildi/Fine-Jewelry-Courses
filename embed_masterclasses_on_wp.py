import requests
import json
import os
import re

WP_URL = 'https://jewelswell.com'
API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443'
endpoint = WP_URL + '/wp-json/easy-mcp-ai/v1/mcp'

mapping_file = 'media-bank/wp_live_media_mapping.json'

MODULE_CONFIGS = [
    {
        'page_id': 1638,
        'code': 'C6-M03 (Shape vs Cut)',
        'title': 'Diamond Shape vs. Cut: The Optical Anatomy',
        'video_file': 'C6-M02-shape-vs-cut-masterclass.mp4',
        'card_file': 'card_01_shape_vs_cut.png',
        'duration': '72s',
        'takeaway': 'Shape is personal aesthetic silhouette; Cut is mathematical human craftsmanship governing light return.'
    },
    {
        'page_id': 1308,
        'code': 'C1-M03 (GIA vs AGS)',
        'title': 'Lab Certification Standards: GIA vs. AGS',
        'video_file': 'C6-M03-lab-certification-standards-masterclass.mp4',
        'card_file': 'card_02_gia_vs_ags.png',
        'duration': '70s',
        'takeaway': 'GIA provides the baseline benchmark; AGS optical modeling proves live performance through ray-trace ASET simulation.'
    },
    {
        'page_id': 1639,
        'code': 'C6-M04 (Natural vs Lab)',
        'title': 'Natural vs. Lab-Grown: The Objective Advisory',
        'video_file': 'C6-M04-natural-vs-lab-grown-masterclass.mp4',
        'card_file': 'card_03_natural_vs_lab.png',
        'duration': '71s',
        'takeaway': 'Both are 100% diamond. Advise without stigma: educate on macroeconomic finite rarity vs technological scalable supply.'
    },
    {
        'page_id': 1640,
        'code': 'C6-M05 (Precious Metals & Settings)',
        'title': 'Precious Metals & Settings: Platinum vs. Gold',
        'video_file': 'C6-M05-precious-metals-and-settings-masterclass.mp4',
        'card_file': 'card_04_metals_and_craftsmanship.png',
        'duration': '66s',
        'takeaway': 'Gold flakes away when scratched; platinum displaces metal into a prestigious patina without ever losing mass or prong tenacity.'
    },
    {
        'page_id': 1643,
        'code': 'C6-M08 / C6-M06 (Ring Sizing & Fit)',
        'title': 'Ring Sizing & Fit: Knuckle vs. Base Mechanics',
        'video_file': 'C6-M06-ring-sizing-and-fit-masterclass.mp4',
        'card_file': 'card_05_ring_sizing_architecture.png',
        'duration': '67s',
        'takeaway': 'Never downsize to stop spin. Measure for the knuckle passage, then deploy European square shanks or sizing beads for stability.'
    },
    {
        'page_id': 1306,
        'code': 'C1-M01 (4Cs Hierarchy)',
        'title': 'The 4Cs Hierarchy: Strategic Cut Optimization',
        'video_file': 'C1-M01-4cs-value-hierarchy-masterclass.mp4',
        'card_file': 'card_06_4cs_value_hierarchy.png',
        'duration': '65s',
        'takeaway': 'Cut controls 80% of visual beauty. Strategic cut optimization masks G-H body color and eye-clean VS2 inclusions.'
    },
    {
        'page_id': 1307,
        'code': 'C1-M02 (Loupe Mastery)',
        'title': 'Loupe Mastery: The 3-Point Security Protocol',
        'video_file': 'C1-M02-loupe-mastery-protocol-masterclass.mp4',
        'card_file': 'card_07_loupe_mastery_protocol.png',
        'duration': '63s',
        'takeaway': 'Read the 10x laser inscription, match the physical GIA dossier plot, and verify live on GIA Report Check database.'
    },
    {
        'page_id': 1310,
        'code': 'C1-M05 (Fluorescence & Inclusions)',
        'title': 'Fluorescence & Inclusions: The Eye-Clean Matrix',
        'video_file': 'C1-M05-fluorescence-and-inclusions-masterclass.mp4',
        'card_file': 'card_08_fluorescence_and_inclusions.png',
        'duration': '64s',
        'takeaway': 'Under 0.2% of fluorescent diamonds show haze. In near-colorless stones, blue fluorescence acts as a free natural whitening filter.'
    },
    {
        'page_id': 1361,
        'code': 'C2-M01 (First 90 Seconds)',
        'title': 'The First 90 Seconds: Frictionless Greeting',
        'video_file': 'C2-M01-first-90-seconds-masterclass.mp4',
        'card_file': 'card_09_first_90_seconds.png',
        'duration': '62s',
        'takeaway': 'Never close the sale in the first ninety seconds; open the relationship with concierge hospitality and freedom to stroll.'
    },
    {
        'page_id': 1565,
        'code': 'C2-M05 (Defending Value)',
        'title': 'Defending Value: Overcoming Online Showrooming',
        'video_file': 'C2-M05-defending-value-online-showrooming-masterclass.mp4',
        'card_file': 'card_10_defending_value.png',
        'duration': '68s',
        'takeaway': 'Never apologize for price. Validate the client research, conduct a like-for-like spec audit, and demonstrate local bench accountability.'
    }
]

def call_mcp(name, args):
    res = requests.post(
        endpoint,
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        json={
            'jsonrpc': '2.0',
            'id': 1,
            'method': 'tools/call',
            'params': {'name': name, 'arguments': args}
        },
        timeout=60
    )
    data = res.json()
    if 'result' in data and 'content' in data['result']:
        raw = data['result']['content'][0]['text']
        try:
            return json.loads(raw)
        except Exception:
            return {'text': raw}
    elif 'error' in data:
        raise RuntimeError(f"MCP error: {data['error']}")
    return data

def build_embed_html(cfg, video_url, card_url):
    html = f"""
<!-- JEWELSWELL ACADEMY EXECUTIVE MASTERCLASS VIDEO & DISCOVERY MATRIX -->
<div class="jw-masterclass-executive-block" style="margin: 36px 0; background: #0b0f17; border: 1px solid #c9a227; border-radius: 14px; overflow: hidden; box-shadow: 0 12px 36px rgba(0,0,0,0.6);">
  <div style="background: linear-gradient(90deg, #111827 0%, #1a2234 100%); padding: 16px 24px; border-bottom: 1px solid rgba(201,162,39,0.3); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
    <div style="display: flex; align-items: center; gap: 12px;">
      <span style="background: #c9a227; color: #0b0f17; font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 4px; letter-spacing: 1.2px; text-transform: uppercase;">Executive Masterclass</span>
      <span style="color: #ffffff; font-family: Georgia, serif; font-size: 18px; font-weight: 600;">{cfg['title']}</span>
    </div>
    <div style="display: flex; align-items: center; gap: 16px;">
      <span style="color: #94a3b8; font-size: 13px; font-weight: 500;">⏱️ {cfg['duration']}</span>
      <span style="background: rgba(34,197,94,0.15); color: #4ade80; font-size: 12px; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(34,197,94,0.3);">1080p HD</span>
    </div>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000000;">
    <video controls preload="metadata" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain;">
      <source src="{video_url}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div style="padding: 16px 24px; background: #0f172a; border-top: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
    <span style="color: #cbd5e1; font-size: 13.5px; line-height: 1.5;">✨ <strong>Core Takeaway:</strong> {cfg['takeaway']}</span>
    <span style="color: #c9a227; font-size: 12.5px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px;">Jewelswell Academy</span>
  </div>
</div>

<div class="jw-dialogue-matrix-figure" style="margin: 32px 0; text-align: center;">
  <img src="{card_url}" alt="{cfg['title']} Discovery Matrix" style="width: 100%; max-width: 960px; height: auto; border-radius: 12px; border: 1px solid rgba(201,162,39,0.3); box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />
</div>
<!-- END JEWELSWELL ACADEMY EXECUTIVE MASTERCLASS -->
"""
    return html.strip()

def embed_all():
    if not os.path.exists(mapping_file):
        print("Media mapping file not found!")
        return

    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    for cfg in MODULE_CONFIGS:
        pid = cfg['page_id']
        v_key = cfg['video_file']
        c_key = cfg['card_file']

        if v_key not in mapping or c_key not in mapping:
            print(f"[SKIP] Media not yet fully uploaded for {cfg['code']} (v={v_key in mapping}, c={c_key in mapping})")
            continue

        v_url = mapping[v_key]['source_url']
        c_url = mapping[c_key]['source_url']

        print(f"\n[EMBEDDING] {cfg['code']} -> Page ID: {pid}...")
        pg = call_mcp('wp_get_page', {'page_id': pid})
        content = pg.get('content', '')

        embed_block = build_embed_html(cfg, v_url, c_url)

        # Check if already embedded
        if 'jw-masterclass-executive-block' in content:
            # Replace existing block
            pattern = re.compile(r'<!-- JEWELSWELL ACADEMY EXECUTIVE MASTERCLASS VIDEO & DISCOVERY MATRIX -->.*?<!-- END JEWELSWELL ACADEMY EXECUTIVE MASTERCLASS -->', re.DOTALL)
            if pattern.search(content):
                new_content = pattern.sub(embed_block, content)
            else:
                new_content = embed_block + '\n\n' + content
        else:
            # Insert right after the first heading or intro paragraph
            if '</h1>' in content:
                parts = content.split('</h1>', 1)
                new_content = parts[0] + '</h1>\n\n' + embed_block + '\n\n' + parts[1]
            elif '<h2' in content:
                parts = content.split('<h2', 1)
                new_content = parts[0] + embed_block + '\n\n<h2' + parts[1]
            else:
                new_content = embed_block + '\n\n' + content

        res = call_mcp('wp_update_page', {'page_id': pid, 'content': new_content})
        print(f"[SUCCESS] Updated Page ID {pid} ({cfg['code']})!")

if __name__ == '__main__':
    embed_all()
