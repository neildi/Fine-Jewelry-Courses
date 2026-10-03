import subprocess
import os

mb = 'media-bank'

clips = [
    (
        f'{mb}/03-lab-grown-and-crystals/gia_id100_diagnostic_plate.jpg',
        f'{mb}/03-lab-grown-and-crystals/gia_id100_testing_device_clip.mp4',
        10.0
    ),
    (
        f'{mb}/01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_plate.jpg',
        f'{mb}/01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_clip.mp4',
        10.0
    ),
    (
        f'{mb}/06-counter-sales-and-consultation/luxury_counter_first_greeting_plate.jpg',
        f'{mb}/06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4',
        10.0
    )
]

for src, dst, dur in clips:
    print(f"Rendering {dst} ({dur}s)...")
    cmd = [
        'ffmpeg', '-y', '-loop', '1', '-i', src,
        '-vf', f'scale=3840:2160,zoompan=z=\'min(zoom+0.00025,1.04)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={int(dur*25)}:s=1920x1080:fps=25',
        '-t', str(dur), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', dst
    ]
    subprocess.run(cmd, check=True)
    print(f"[OK] Rendered {dst}")

print("All diagnostic clips rendered successfully!")
