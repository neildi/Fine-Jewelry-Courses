import base64
import requests
import json
import os
import glob
import time

WP_URL = 'https://jewelswell.com'
API_KEY = 'wpmcp_c2e3d4b926c6cc0728f902a73a5f818462925a08a1bce74bd40959fc53480443'
endpoint = WP_URL + '/wp-json/easy-mcp-ai/v1/mcp'

mapping_file = 'media-bank/wp_live_media_mapping.json'
if os.path.exists(mapping_file):
    with open(mapping_file, 'r', encoding='utf-8') as f:
        live_mapping = json.load(f)
else:
    live_mapping = {}

def upload_file(filepath, title, alt='', caption=''):
    fname = os.path.basename(filepath)
    if fname in live_mapping:
        print(f"[SKIP] Already uploaded: {fname} -> {live_mapping[fname]['source_url']}")
        return live_mapping[fname]

    fsize_mb = os.path.getsize(filepath) / (1024 * 1024)
    print(f"\n[UPLOADING] {fname} ({fsize_mb:.2f} MB)...", flush=True)

    with open(filepath, 'rb') as f:
        b64_data = base64.b64encode(f.read()).decode('utf-8')

    payload = {
        'jsonrpc': '2.0',
        'id': int(time.time()),
        'method': 'tools/call',
        'params': {
            'name': 'wp_upload_media',
            'arguments': {
                'filename': fname,
                'content_base64': b64_data,
                'title': title,
                'alt_text': alt,
                'caption': caption
            }
        }
    }

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.post(
                endpoint,
                headers={
                    'Authorization': f'Bearer {API_KEY}',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                json=payload,
                timeout=360
            )

            if res.status_code == 200:
                resp_data = res.json()
                raw_text = resp_data['result']['content'][0]['text']
                info = json.loads(raw_text)
                print(f"[SUCCESS] {fname} uploaded! ID: {info['id']} | URL: {info['source_url']}", flush=True)
                live_mapping[fname] = info
                with open(mapping_file, 'w', encoding='utf-8') as f:
                    json.dump(live_mapping, f, indent=2)
                return info
            else:
                print(f"[RETRY {attempt}/{max_retries}] HTTP {res.status_code} for {fname}. Waiting 5s...", flush=True)
                time.sleep(5)
        except Exception as e:
            print(f"[RETRY {attempt}/{max_retries}] Exception on {fname}: {e}. Waiting 5s...", flush=True)
            time.sleep(5)

    print(f"[FAILED] Failed to upload {fname} after {max_retries} attempts.", flush=True)
    return None

# 1. Dialogue Cards
print("=== 1. UPLOADING DIALOGUE CARDS ===")
cards = sorted(glob.glob('media-bank/07-infographics-and-cards/card_*.png'))
for c in cards:
    base = os.path.splitext(os.path.basename(c))[0]
    title = f"Jewelswell Academy Dialogue Card: {base.replace('_', ' ').title()}"
    upload_file(c, title, alt=title, caption='Executive Dialogue Matrix')

# 2. Masterclass MP4 Videos
print("\n=== 2. UPLOADING MASTERCLASS MP4 VIDEOS ===")
videos = sorted(glob.glob('media-bank/*masterclass.mp4'))
for v in videos:
    base = os.path.splitext(os.path.basename(v))[0]
    title = f"Jewelswell Academy Masterclass Video: {base.replace('-', ' ').title()}"
    upload_file(v, title, caption='1080p Executive Video Masterclass')

print("\nAll uploads completed and recorded to:", mapping_file)
