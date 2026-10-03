import os
import subprocess

videos_dir = r"courses/C6-bridal-engagement-mastery/videos"
avatar_video = f"{videos_dir}/neelkanth_intro_greenscreen.mp4"
broll_oval = f"{videos_dir}/broll_oval_ring.mp4"
broll_toi = f"{videos_dir}/broll_toi_et_moi.mp4"
font_georgia = f"{videos_dir}/georgia.ttf"
font_arial = f"{videos_dir}/arial.ttf"
final_output = f"{videos_dir}/C6-M01-lesson-video-master.mp4"

# Timeline:
# 0.0s - 13.0s: Avatar (Neelkanth introduction)
# 13.0s - 18.0s: B-roll Oval Diamond Ring (5s cutaway)
# 18.0s - 23.0s: B-roll Toi et Moi Ring (5s cutaway)
# 23.0s - 33.4s: Avatar (Neelkanth conclusion)
# Audio: Continuous audio from avatar_video throughout all 33.4 seconds!

filter_str = (
    "[0:v]trim=start=0:end=13,setpts=PTS-STARTPTS,scale=1920:1080[v0];"
    "[1:v]trim=start=0:end=5,setpts=PTS-STARTPTS,scale=1920:1080[v1];"
    "[2:v]trim=start=0:end=5,setpts=PTS-STARTPTS,scale=1920:1080[v2];"
    "[0:v]trim=start=23:end=33.4,setpts=PTS-STARTPTS,scale=1920:1080[v3];"
    "[v0][v1][v2][v3]concat=n=4:v=1:a=0[raw_cut];"
    "[raw_cut]drawbox=x=60:y=920:w=760:h=90:color=black@0.75:t=fill,"
    "drawbox=x=60:y=920:w=6:h=90:color=0xC9A227:t=fill,"
    f"drawtext=text='C6-M01 \\: The Modern Bridal Buyer\\'s Journey':x=80:y=935:fontcolor=0xDFBE54:fontsize=26:fontfile='{font_georgia}',"
    f"drawtext=text='Jewelswell Academy  •  Executive Master Curriculum':x=80:y=972:fontcolor=white:fontsize=18:fontfile='{font_arial}'[outv]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", avatar_video,
    "-i", broll_oval,
    "-i", broll_toi,
    "-filter_complex", filter_str,
    "-map", "[outv]",
    "-map", "0:a",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    final_output
]

print("Running master video assembly...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print("SUCCESS! Master video generated at:", final_output)
else:
    print("FFmpeg Error:\n", res.stderr)
