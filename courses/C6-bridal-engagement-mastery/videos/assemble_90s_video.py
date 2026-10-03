import subprocess
import os

vdir = 'courses/C6-bridal-engagement-mastery/videos'

# Inputs:
# 0: neelkanth_in_salon.mp4 (host avatar in luxury VIP salon)
# 1: broll_oval_ring.mp4
# 2: badge_oval.png
# 3: broll_toi_et_moi.mp4
# 4: badge_toi.png
# 5: gia_diamond_cut_clip.mp4 (macro rotating diamond)
# 6: badge_gia.png
# 7: badge_intro.png
# 8: gia_wireframe_clip.webm (computer proportion scanner & loupe evaluation)
# 9: badge_spec_overload.png
# 10: gia_raytrace_clip.webm (tweezers diamond fire)
# 11: broll_hidden_halo.mp4
# 12: broll_bezel_ring.mp4
# 13: badge_consultation.png
# 14: dialogue_card_c6.png (dialogue card)
# 15: badge_heirloom.png
# 16: narration_master.wav (100.28s master audio track)

# First create a 15-second cinematic slow zoom for the dialogue card:
dialogue_vid = f'{vdir}/broll_dialogue_card.mp4'
cmd_diag = [
    'ffmpeg', '-y', '-loop', '1', '-i', f'{vdir}/dialogue_card_c6.png',
    '-vf', 'scale=3840:2160,zoompan=z=\'min(zoom+0.0003,1.05)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=375:s=1920x1080:fps=25',
    '-t', '15', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', dialogue_vid
]
print("Rendering dialogue card video...")
subprocess.run(cmd_diag, check=True)

# Build the complete filter_complex:
# Segments:
# v0: 0.0 - 12.0 (12.0s) host + badge_intro
# v1: 0.0 - 5.0 (5.0s) oval ring + badge_oval
# v2: 0.0 - 5.0 (5.0s) toi et moi + badge_toi
# v3: 3.5 - 8.0 (4.5s) gia scintillation + badge_gia
# v4: 26.5 - 33.4 (6.9s) host
# v5: 15.0 - 23.6 (8.6s) gia computer scanner + badge_spec_overload
# v6: 10.0 - 17.0 (7.0s) gia tweezers diamond fire
# v7: 0.0 - 7.5 (7.5s) broll_hidden_halo (looped if needed)
# v8: 0.0 - 7.5 (7.5s) broll_bezel_ring (looped if needed)
# v9: 10.0 - 18.0 (8.0s) gia gemologist 10x loupe + badge_consultation
# v10: 0.0 - 15.0 (15.0s) dialogue card video
# v11: 15.0 - 28.28 (13.28s) host in salon + badge_heirloom

filter_complex = (
    # v0: Host Intro (12.0s)
    "[0:v]trim=start=0:end=12,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v0_raw];"
    "[7:v]format=rgba[b_intro];"
    "[v0_raw][b_intro]overlay=0:0:enable='between(t,0.5,9.0)':format=auto[v0];"

    # v1: Oval Ring (5.0s)
    "[1:v]trim=start=0:end=5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v1_raw];"
    "[2:v]format=rgba[b_oval];"
    "[v1_raw][b_oval]overlay=0:0[v1];"

    # v2: Toi et Moi Ring (5.0s)
    "[3:v]trim=start=0:end=5,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v2_raw];"
    "[4:v]format=rgba[b_toi];"
    "[v2_raw][b_toi]overlay=0:0[v2];"

    # v3: GIA Rotating Scintillation (4.5s)
    "[5:v]trim=start=3.5:end=8.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v3_raw];"
    "[6:v]format=rgba[b_gia];"
    "[v3_raw][b_gia]overlay=0:0[v3];"

    # v4: Host Interlude (6.9s)
    "[0:v]trim=start=26.5:end=33.4,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v4];"

    # v5: GIA Proportion Scanner (8.6s)
    "[8:v]trim=start=15.0:end=23.6,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v5_raw];"
    "[9:v]format=rgba[b_spec];"
    "[v5_raw][b_spec]overlay=0:0:enable='between(t,0.5,7.5)':format=auto[v5];"

    # v6: GIA Diamond Fire Tweezers (7.0s)
    "[10:v]trim=start=10.0:end=17.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v6];"

    # v7: Hidden Halo Profile (7.5s - slowed 0.67x for majestic pace)
    "[11:v]trim=start=0:end=5,setpts=1.5*PTS,scale=1920:1080,setsar=1,fps=25[v7];"

    # v8: Bezel Setting Profile (7.5s - slowed 0.67x for majestic pace)
    "[12:v]trim=start=0:end=5,setpts=1.5*PTS,scale=1920:1080,setsar=1,fps=25[v8];"

    # v9: GIA Gemologist Loupe (8.0s)
    "[8:v]trim=start=10.0:end=18.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v9_raw];"
    "[13:v]format=rgba[b_cons];"
    "[v9_raw][b_cons]overlay=0:0:enable='between(t,0.5,7.0)':format=auto[v9];"

    # v10: Dialogue Card Presentation (15.0s)
    "[14:v]trim=start=0:end=15,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v10];"

    # v11: Host Outro (13.28s)
    "[0:v]trim=start=15.0:end=28.28,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v11_raw];"
    "[15:v]format=rgba[b_heir];"
    "[v11_raw][b_heir]overlay=0:0:enable='between(t,0.5,10.0)':format=auto[v11];"

    # Concatenate all 12 video segments:
    "[v0][v1][v2][v3][v4][v5][v6][v7][v8][v9][v10][v11]concat=n=12:v=1:a=0[outv]"
)

cmd = [
    'ffmpeg', '-y',
    '-i', f'{vdir}/neelkanth_in_salon.mp4',       # 0
    '-i', f'{vdir}/broll_oval_ring.mp4',          # 1
    '-i', f'{vdir}/badge_oval.png',               # 2
    '-i', f'{vdir}/broll_toi_et_moi.mp4',         # 3
    '-i', f'{vdir}/badge_toi.png',                # 4
    '-i', f'{vdir}/gia_diamond_cut_clip.mp4',     # 5
    '-i', f'{vdir}/badge_gia.png',                # 6
    '-i', f'{vdir}/badge_intro.png',              # 7
    '-i', f'{vdir}/gia_wireframe_clip.webm',      # 8
    '-i', f'{vdir}/badge_spec_overload.png',      # 9
    '-i', f'{vdir}/gia_raytrace_clip.webm',       # 10
    '-i', f'{vdir}/broll_hidden_halo.mp4',        # 11
    '-i', f'{vdir}/broll_bezel_ring.mp4',         # 12
    '-i', f'{vdir}/badge_consultation.png',       # 13
    '-i', f'{dialogue_vid}',                      # 14
    '-i', f'{vdir}/badge_heirloom.png',           # 15
    '-i', f'{vdir}/narration_master.wav',         # 16
    '-filter_complex', filter_complex,
    '-map', '[outv]',
    '-map', '16:a',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '20',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-pix_fmt', 'yuv420p',
    f'{vdir}/C6-M01-lesson-video-90s-master.mp4'
]

print("Rendering 100-second master video...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    sz = os.path.getsize(f'{vdir}/C6-M01-lesson-video-90s-master.mp4')
    print(f"SUCCESS! Master video rendered. File size: {sz / 1024 / 1024:.2f} MB")
else:
    print("Error:\n", res.stderr)
