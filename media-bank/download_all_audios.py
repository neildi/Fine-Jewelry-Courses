import urllib.request
import os

audio_map = {
    'c6_m04_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=554e26a0-2a5d-44ca-a44d-c285ef0867ea.wav',
    'c6_m05_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=f0263d06-45fa-4414-917f-c9aa8841a13d.wav',
    'c6_m06_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=12cd5475-2206-4f43-9171-c653ca57485e.wav',
    'c1_m01_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=07d8342e-829a-4397-8079-9930abbc5ca2.wav',
    'c1_m02_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=e564e420-069c-4536-b142-c4466e685220.wav',
    'c1_m05_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=9ca75840-690e-47b0-9698-8dafe374d3bf.wav',
    'c2_m01_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=2967331f-a2fb-4ca9-bc68-0110e8d3485f.wav',
    'c2_m05_narration.wav': 'https://resource2.heygen.ai/text_to_speech/bc3e4c3175fd49d2adbb9af7ca8babeb/a3dc8f81b0c6498aac3d17fb879b467d/id=ad979a50-9c7a-47de-b2c7-59091b9515a7.wav'
}

dest_dir = r'C:\Users\neelk\Downloads\Arena-App\Fine-Jewelry-Courses\media-bank\08-audio-narration'
os.makedirs(dest_dir, exist_ok=True)

for fname, url in audio_map.items():
    dest_path = os.path.join(dest_dir, fname)
    print(f"Downloading {fname} from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as f:
        f.write(resp.read())
    print(f"Saved {fname} ({os.path.getsize(dest_path)} bytes)")

print("All audio narration files downloaded successfully!")
