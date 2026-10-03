import subprocess
import os

mb = 'media-bank'

# 1. Bow-Tie Optical Analysis Plate (7.5s):
bowtie_vid = f'{mb}/02-shapes-and-cuts/broll_bowtie_plate.mp4'
cmd_bt = [
    'ffmpeg', '-y', '-loop', '1', '-i', f'{mb}/02-shapes-and-cuts/oval_bow_tie_visual_comparison.jpg',
    '-vf', 'scale=3840:2160,zoompan=z=\'min(zoom+0.0003,1.05)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=188:s=1920x1080:fps=25',
    '-t', '7.5', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', bowtie_vid
]
subprocess.run(cmd_bt, check=True)

# 2. Carat spread plate (9.0s):
carat_vid = f'{mb}/01-gemology-and-diamonds/broll_carat_spread.mp4'
cmd1 = [
    'ffmpeg', '-y', '-loop', '1', '-i', f'{mb}/01-gemology-and-diamonds/macro_carat_spread_comparison.jpg',
    '-vf', 'scale=3840:2160,zoompan=z=\'min(zoom+0.0003,1.05)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=225:s=1920x1080:fps=25',
    '-t', '9.0', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', carat_vid
]
subprocess.run(cmd1, check=True)

# 3. Dialogue Card (8.5s):
card_vid = f'{mb}/07-infographics-and-cards/broll_card_01.mp4'
cmd2 = [
    'ffmpeg', '-y', '-loop', '1', '-i', f'{mb}/07-infographics-and-cards/card_01_shape_vs_cut.png',
    '-vf', 'scale=3840:2160,zoompan=z=\'min(zoom+0.00025,1.04)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=213:s=1920x1080:fps=25',
    '-t', '8.5', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', card_vid
]
subprocess.run(cmd2, check=True)

# 4. Outro Plate (7.31s):
outro_vid = f'{mb}/07-infographics-and-cards/broll_outro_01.mp4'
cmd3 = [
    'ffmpeg', '-y', '-loop', '1', '-i', f'{mb}/06-counter-sales-and-consultation/luxury_bridal_salon_bg.jpg',
    '-i', f'{mb}/07-infographics-and-cards/badge_shape_cut_outro.png',
    '-filter_complex', '[0:v]scale=1920:1080,fps=25[bg];[1:v]format=rgba[badge];[bg][badge]overlay=0:0[v]',
    '-map', '[v]', '-t', '7.31', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', outro_vid
]
subprocess.run(cmd3, check=True)

# Now assemble master 10-scene video matching exact 72.31s audio:
# s0: 0.0 - 8.5 (8.5s) Host Avatar Hook (Intro only)
# s1: 0.0 - 5.0 (5.0s) Oval Ring B-roll
# s2: 0.0 - 3.5 (3.5s) Toi et Moi B-roll
# s3: 0.0 - 8.0 (8.0s) GIA 3D Raytrace Clip
# s4: 0.0 - 7.5 (7.5s) Bow-Tie Optical Analysis Plate
# s5: 0.0 - 9.0 (9.0s) GIA Cut Proportions Scintillation Clip
# s6: 0.0 - 9.0 (9.0s) Carat Spread Millimeter Plate
# s7: 0.0 - 6.0 (6.0s) GIA Wireframe Scanner / Loupe Clip
# s8: 0.0 - 8.5 (8.5s) Dialogue Card Infographic Plate
# s9: 0.0 - 7.31 (7.31s) Outro Summary Badge Plate (Zero avatar at end!)

out_mp4 = f'{mb}/C6-M02-shape-vs-cut-masterclass.mp4'

cmd_master = [
    'ffmpeg', '-y',
    '-i', f'{mb}/06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',       # 0
    '-i', f'{mb}/02-shapes-and-cuts/broll_oval_ring.mp4',                           # 1
    '-i', f'{mb}/02-shapes-and-cuts/broll_toi_et_moi.mp4',                          # 2
    '-i', f'{mb}/01-gemology-and-diamonds/gia_raytrace_clip.webm',                  # 3
    '-i', bowtie_vid,                                                               # 4
    '-i', f'{mb}/01-gemology-and-diamonds/gia_cut_proportions_scintillation_clip.mp4', # 5
    '-i', carat_vid,                                                                # 6
    '-i', f'{mb}/01-gemology-and-diamonds/gia_wireframe_clip.webm',                 # 7
    '-i', card_vid,                                                                 # 8
    '-i', outro_vid,                                                                # 9
    '-i', f'{mb}/08-audio-narration/c6_m02_narration.wav',                          # 10
    '-filter_complex', (
        '[0:v]trim=start=0:end=8.5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v0];'
        '[1:v]trim=start=0:end=5.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v1];'
        '[2:v]trim=start=0:end=3.5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v2];'
        '[3:v]trim=start=0:end=8.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v3];'
        '[4:v]trim=start=0:end=7.5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v4];'
        '[5:v]trim=start=0:end=9.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v5];'
        '[6:v]trim=start=0:end=9.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v6];'
        '[7:v]trim=start=0:end=6.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v7];'
        '[8:v]trim=start=0:end=8.5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v8];'
        '[9:v]trim=start=0:end=7.31,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v9];'
        '[v0][v1][v2][v3][v4][v5][v6][v7][v8][v9]concat=n=10:v=1:a=0[v]'
    ),
    '-map', '[v]',
    '-map', '10:a',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '20',
    '-c:a', 'aac', '-b:a', '192k',
    '-movflags', '+faststart',
    out_mp4
]

print("Assembling Video 1 (C6-M02: Diamond Shape vs Cut)...")
subprocess.run(cmd_master, check=True)
print("Master video rendered successfully:", out_mp4)
