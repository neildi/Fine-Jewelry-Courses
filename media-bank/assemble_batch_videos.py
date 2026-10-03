import subprocess
import os

mb = 'media-bank'
bg_salon = f'{mb}/06-counter-sales-and-consultation/luxury_bridal_salon_bg.jpg'
avatar_hook = f'{mb}/06-counter-sales-and-consultation/neelkanth_intro_hook.mp4'

VIDEOS = [
    {
        'id': 'V02',
        'code': 'C6-M03',
        'title': 'lab-certification-standards',
        'audio': f'{mb}/08-audio-narration/c6_m03_narration.wav',
        'total_dur': 70.217,
        'badge': f'{mb}/07-infographics-and-cards/badge_lab_standards_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_02_gia_vs_ags.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 7.88},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/gia_dossier_dual_specimens.jpg', 'dur': 7.89},
            {'type': 'video', 'src': f'{mb}/01-gemology-and-diamonds/gia_grading_clip.webm', 'dur': 8.53},
            {'type': 'video', 'src': f'{mb}/05-grading-reports-and-plots/gia_ags_ideal_aset_report_clip.mp4', 'dur': 8.70},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/aset_scope_optical_map.jpg', 'dur': 8.31},
            {'type': 'video', 'src': f'{mb}/01-gemology-and-diamonds/gia_diamond_cut_clip.mp4', 'dur': 7.57},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/how_to_hold_loupe_macro.jpg', 'dur': 7.95},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_02_gia_vs_ags.png', 'dur': 8.02},
            {'type': 'outro', 'dur': 5.367}
        ]
    },
    {
        'id': 'V03',
        'code': 'C6-M04',
        'title': 'natural-vs-lab-grown',
        'audio': f'{mb}/08-audio-narration/c6_m04_narration.wav',
        'total_dur': 70.818,
        'badge': f'{mb}/07-infographics-and-cards/badge_diamond_origin_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_03_natural_vs_lab.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 8.99},
            {'type': 'image', 'src': f'{mb}/03-lab-grown-and-crystals/rough_crystal_comparison.jpg', 'dur': 8.47},
            {'type': 'image', 'src': f'{mb}/03-lab-grown-and-crystals/mantle_volcano_kimberlite_diagram.jpg', 'dur': 8.11},
            {'type': 'image', 'src': f'{mb}/03-lab-grown-and-crystals/cvd_plasma_reactor_chamber.jpg', 'dur': 8.01},
            {'type': 'video', 'src': f'{mb}/03-lab-grown-and-crystals/gia_id100_testing_device_clip.mp4', 'dur': 8.76},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/luxury_consultation_couple.jpg', 'dur': 9.34},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/heirloom_vintage_handover.jpg', 'dur': 7.29},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_03_natural_vs_lab.png', 'dur': 6.44},
            {'type': 'outro', 'dur': 5.408}
        ]
    },
    {
        'id': 'V04',
        'code': 'C6-M05',
        'title': 'precious-metals-and-settings',
        'audio': f'{mb}/08-audio-narration/c6_m05_narration.wav',
        'total_dur': 65.620,
        'badge': f'{mb}/07-infographics-and-cards/badge_metals_craft_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_04_metals_and_craftsmanship.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 7.37},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/metal_alloy_rings_comparison.jpg', 'dur': 8.26},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/rhodium_plating_immersion.jpg', 'dur': 6.84},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/platinum_density_patina_macro.jpg', 'dur': 9.43},
            {'type': 'video', 'src': f'{mb}/04-metals-and-craftsmanship/gia_microscope_prong_setting_clip.mp4', 'dur': 8.75},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/bezel_set_diamond_ring_1791043122448.jpg', 'dur': 7.64},
            {'type': 'video', 'src': f'{mb}/04-metals-and-craftsmanship/ring_mandrel_comfort_fit_clip.mp4', 'dur': 6.51},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_04_metals_and_craftsmanship.png', 'dur': 5.83},
            {'type': 'outro', 'dur': 4.99}
        ]
    },
    {
        'id': 'V05',
        'code': 'C6-M06',
        'title': 'ring-sizing-and-fit',
        'audio': f'{mb}/08-audio-narration/c6_m06_narration.wav',
        'total_dur': 66.952,
        'badge': f'{mb}/07-infographics-and-cards/badge_ring_sizing_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_05_ring_sizing_architecture.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 7.81},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/finger_knuckle_measurement_macro.jpg', 'dur': 7.11},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/ring_spin_on_finger_demonstration.jpg', 'dur': 7.76},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/euro_shank_sizing_beads_macro.jpg', 'dur': 8.17},
            {'type': 'video', 'src': f'{mb}/04-metals-and-craftsmanship/ring_mandrel_comfort_fit_clip.mp4', 'dur': 8.49},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/wide_band_vs_narrow_comparison.jpg', 'dur': 8.58},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/ring_slide_on_finger_client.jpg', 'dur': 6.89},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_05_ring_sizing_architecture.png', 'dur': 7.07},
            {'type': 'outro', 'dur': 5.072}
        ]
    },
    {
        'id': 'V06',
        'code': 'C1-M01',
        'title': '4cs-value-hierarchy',
        'audio': f'{mb}/08-audio-narration/c1_m01_narration.wav',
        'total_dur': 65.123,
        'badge': f'{mb}/07-infographics-and-cards/badge_4cs_hierarchy_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_06_4cs_value_hierarchy.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 9.56},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/gia_dossier_macro_specs.jpg', 'dur': 7.23},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/rough_diamond_cleaving_macro.jpg', 'dur': 6.56},
            {'type': 'video', 'src': f'{mb}/01-gemology-and-diamonds/gia_cut_proportions_scintillation_clip.mp4', 'dur': 9.13},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/macro_carat_spread_comparison.jpg', 'dur': 7.85},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/daylight_counter_comparison.jpg', 'dur': 7.55},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/macro_fire_dispersion_colors.jpg', 'dur': 5.64},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_06_4cs_value_hierarchy.png', 'dur': 6.80},
            {'type': 'outro', 'dur': 4.803}
        ]
    },
    {
        'id': 'V07',
        'code': 'C1-M02',
        'title': 'loupe-mastery-protocol',
        'audio': f'{mb}/08-audio-narration/c1_m02_narration.wav',
        'total_dur': 63.112,
        'badge': f'{mb}/07-infographics-and-cards/badge_loupe_mastery_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_07_loupe_mastery_protocol.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 6.98},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/how_to_hold_loupe_macro.jpg', 'dur': 8.21},
            {'type': 'video', 'src': f'{mb}/05-grading-reports-and-plots/diamond_girdle_laser_inscription_clip.mp4', 'dur': 7.58},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/laser_inscription_magnified_macro.jpg', 'dur': 5.67},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/gia_plot_diagram_feather_pinpoint.jpg', 'dur': 7.06},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/side_by_side_spec_audit_pad.jpg', 'dur': 7.35},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/client_smiling_handshake_counter.jpg', 'dur': 7.70},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_07_loupe_mastery_protocol.png', 'dur': 7.42},
            {'type': 'outro', 'dur': 5.142}
        ]
    },
    {
        'id': 'V08',
        'code': 'C1-M05',
        'title': 'fluorescence-and-inclusions',
        'audio': f'{mb}/08-audio-narration/c1_m05_narration.wav',
        'total_dur': 63.922,
        'badge': f'{mb}/07-infographics-and-cards/badge_fluorescence_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_08_fluorescence_and_inclusions.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 8.28},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/online_forum_warning_rumor.jpg', 'dur': 5.48},
            {'type': 'video', 'src': f'{mb}/01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_clip.mp4', 'dur': 7.60},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/fluorescent_daylight_sun_gleam.jpg', 'dur': 9.37},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/microscopic_feather_prong_concealed.jpg', 'dur': 8.52},
            {'type': 'image', 'src': f'{mb}/01-gemology-and-diamonds/gemological_inclusion_types_grid.jpg', 'dur': 7.84},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/eye_clean_face_up_beauty.jpg', 'dur': 6.27},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_08_fluorescence_and_inclusions.png', 'dur': 6.69},
            {'type': 'outro', 'dur': 3.872}
        ]
    },
    {
        'id': 'V09',
        'code': 'C2-M01',
        'title': 'first-90-seconds',
        'audio': f'{mb}/08-audio-narration/c2_m01_narration.wav',
        'total_dur': 62.015,
        'badge': f'{mb}/07-infographics-and-cards/badge_first_90s_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_09_first_90_seconds.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 8.78},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/customer_hesitant_entry.jpg', 'dur': 6.13},
            {'type': 'video', 'src': f'{mb}/06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4', 'dur': 7.00},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/warm_concierge_greeting.jpg', 'dur': 7.96},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/browsing_cases_couple.jpg', 'dur': 6.62},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/advisor_warm_reapproach.jpg', 'dur': 7.90},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/intimate_consultation_tray.jpg', 'dur': 6.07},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_09_first_90_seconds.png', 'dur': 5.54},
            {'type': 'outro', 'dur': 6.015}
        ]
    },
    {
        'id': 'V10',
        'code': 'C2-M05',
        'title': 'defending-value-online-showrooming',
        'audio': f'{mb}/08-audio-narration/c2_m05_narration.wav',
        'total_dur': 68.049,
        'badge': f'{mb}/07-infographics-and-cards/badge_defending_value_outro.png',
        'card': f'{mb}/07-infographics-and-cards/card_10_defending_value.png',
        'scenes': [
            {'type': 'video', 'src': avatar_hook, 'dur': 7.99},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/customer_holding_smartphone_counter.jpg', 'dur': 7.19},
            {'type': 'video', 'src': f'{mb}/06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4', 'dur': 7.75},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/calm_advisor_listening.jpg', 'dur': 7.40},
            {'type': 'image', 'src': f'{mb}/05-grading-reports-and-plots/side_by_side_spec_audit_pad.jpg', 'dur': 9.26},
            {'type': 'image', 'src': f'{mb}/04-metals-and-craftsmanship/bench_polishing_and_steam_clean.jpg', 'dur': 9.68},
            {'type': 'image', 'src': f'{mb}/06-counter-sales-and-consultation/proposal_celebration_couple.jpg', 'dur': 6.52},
            {'type': 'image', 'src': f'{mb}/07-infographics-and-cards/card_10_defending_value.png', 'dur': 5.89},
            {'type': 'outro', 'dur': 6.369}
        ]
    }
]

def render_image_clip(img_path, dur, out_path):
    d_frames = int(dur * 25)
    cmd = [
        'ffmpeg', '-y', '-loop', '1', '-i', img_path,
        '-vf', f"scale=3840:2160,zoompan=z='min(zoom+0.00025,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={d_frames}:s=1920x1080:fps=25",
        '-t', f'{dur:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', out_path
    ]
    subprocess.run(cmd, check=True)

def render_outro_clip(badge_path, dur, out_path):
    cmd = [
        'ffmpeg', '-y', '-loop', '1', '-i', bg_salon,
        '-i', badge_path,
        '-filter_complex', '[0:v]scale=1920:1080,fps=25[bg];[1:v]format=rgba[badge];[bg][badge]overlay=0:0[v]',
        '-map', '[v]', '-t', f'{dur:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', out_path
    ]
    subprocess.run(cmd, check=True)

def assemble_single_video(cfg):
    vid_id = cfg['id']
    code = cfg['code']
    title = cfg['title']
    audio_path = cfg['audio']
    out_mp4 = f"{mb}/{code}-{title}-masterclass.mp4"
    
    print(f"\n========================================================")
    print(f"ASSEMBLING [{vid_id}] {code}: {title}")
    print(f"Target MP4: {out_mp4}")
    print(f"Total Spoken Audio: {cfg['total_dur']:.3f}s")
    print(f"========================================================")

    temp_clips = []
    filter_inputs = []
    filter_chain = []
    
    for idx, sc in enumerate(cfg['scenes']):
        sc_type = sc['type']
        dur = sc['dur']
        clip_out = f"{mb}/tmp_{vid_id}_sc{idx}.mp4"
        
        if sc_type == 'image':
            render_image_clip(sc['src'], dur, clip_out)
            filter_inputs.extend(['-i', clip_out])
            filter_chain.append(f'[{idx}:v]scale=1920:1080,setsar=1,fps=25[v{idx}];')
            temp_clips.append(clip_out)
        elif sc_type == 'outro':
            render_outro_clip(cfg['badge'], dur, clip_out)
            filter_inputs.extend(['-i', clip_out])
            filter_chain.append(f'[{idx}:v]scale=1920:1080,setsar=1,fps=25[v{idx}];')
            temp_clips.append(clip_out)
        elif sc_type == 'video':
            filter_inputs.extend(['-i', sc['src']])
            filter_chain.append(f'[{idx}:v]trim=start=0:end={dur:.3f},setpts=PTS-STARTPTS,scale=1920:1080,setsar=1,fps=25[v{idx}];')

    # Add audio input
    n_inputs = len(cfg['scenes'])
    filter_inputs.extend(['-i', audio_path])
    
    concat_inputs = ''.join([f'[v{i}]' for i in range(n_inputs)])
    filter_chain.append(f'{concat_inputs}concat=n={n_inputs}:v=1:a=0[v]')
    
    full_filter = ''.join(filter_chain)
    
    cmd = [
        'ffmpeg', '-y'
    ] + filter_inputs + [
        '-filter_complex', full_filter,
        '-map', '[v]',
        '-map', f'{n_inputs}:a',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '20',
        '-c:a', 'aac', '-b:a', '192k',
        '-movflags', '+faststart',
        out_mp4
    ]
    
    subprocess.run(cmd, check=True)
    print(f"[SUCCESS] Master video created: {out_mp4}")
    
    # Cleanup temp clips
    for tc in temp_clips:
        if os.path.exists(tc):
            os.remove(tc)

if __name__ == '__main__':
    for v in VIDEOS:
        assemble_single_video(v)
    print("\nALL 9 MASTERCLASS VIDEOS ASSEMBLED AND SYNCHRONIZED PERFECTLY!")
