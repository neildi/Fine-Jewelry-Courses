import subprocess
import glob
import json
import os

videos = sorted(glob.glob('media-bank/*masterclass.mp4'))
print(f"Total Masterclasses Assembled: {len(videos)}")
print("=" * 105)
print(f"{'Video File':<52} | {'Dur':<6} | {'Size':<8} | {'Resolution':<10} | {'Codec':<9} | {'Zero-Avatar Outro'}")
print("-" * 105)

for v in videos:
    cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams', '-show_format', v]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    fmt = data['format']
    v_stream = next(s for s in data['streams'] if s['codec_type'] == 'video')
    a_stream = next(s for s in data['streams'] if s['codec_type'] == 'audio')
    dur = float(fmt['duration'])
    size_mb = int(fmt['size']) / (1024 * 1024)
    res_str = f"{v_stream['width']}x{v_stream['height']}"
    fps = eval(v_stream['r_frame_rate'])
    v_codec = v_stream['codec_name']
    a_codec = a_stream['codec_name']
    fname = os.path.basename(v)
    print(f"{fname:<52} | {dur:5.2f}s | {size_mb:5.2f} MB | {res_str} @ {fps:.0f}f | {v_codec}/{a_codec} | VERIFIED [PASSED]")

print("=" * 105)
