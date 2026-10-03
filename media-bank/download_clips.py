import subprocess
import os
import sys

CLIPS = [
    {
        "url": "https://www.youtube.com/watch?v=nb0DKoRBiSc",
        "section": "*00:10-00:20",
        "output": "media-bank/01-gemology-and-diamonds/gia_cut_proportions_scintillation_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=Y9NMEHqDFsI",
        "section": "*00:15-00:25",
        "output": "media-bank/02-shapes-and-cuts/oval_bow_tie_analysis_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=sePQECnJvBk",
        "section": "*00:20-00:30",
        "output": "media-bank/05-grading-reports-and-plots/gia_ags_ideal_aset_report_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=sKmMSvdd69w",
        "section": "*00:15-00:25",
        "output": "media-bank/03-lab-grown-and-crystals/gia_id100_testing_device_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=BDiUi7Fmlp8",
        "section": "*00:15-00:25",
        "output": "media-bank/04-metals-and-craftsmanship/ring_mandrel_comfort_fit_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=NrIhfnM-c2Q",
        "section": "*00:10-00:20",
        "output": "media-bank/05-grading-reports-and-plots/diamond_girdle_laser_inscription_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=cjBHw2cmQe4",
        "section": "*00:20-00:30",
        "output": "media-bank/01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=kf_ONsn5BZc",
        "section": "*00:10-00:20",
        "output": "media-bank/06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4"
    },
    {
        "url": "https://www.youtube.com/watch?v=hbXWEi_qN3w",
        "section": "*01:10-01:20",
        "output": "media-bank/06-counter-sales-and-consultation/overcoming_online_price_comparison_clip.mp4"
    }
]

def download_clip(item):
    out_file = item["output"]
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"[SKIP] Already exists: {out_file}", flush=True)
        return True

    print(f"\n[DOWNLOADING] {out_file} from {item['url']} ({item['section']})...", flush=True)
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--download-sections", item["section"],
        "-f", "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "--force-keyframes-at-cuts",
        "--no-playlist",
        "-o", out_file,
        item["url"]
    ]
    try:
        res = subprocess.run(cmd, capture_output=False, timeout=120)
        if res.returncode == 0:
            print(f"[SUCCESS] Downloaded: {out_file}", flush=True)
            return True
        else:
            print(f"[ERROR] Non-zero return code for: {out_file}", flush=True)
            return False
    except Exception as e:
        print(f"[EXCEPTION] {e}", flush=True)
        return False

if __name__ == "__main__":
    success_count = 0
    for clip in CLIPS:
        if download_clip(clip):
            success_count += 1
    print(f"\nFinished. Successfully processed {success_count}/{len(CLIPS)} clips.", flush=True)
