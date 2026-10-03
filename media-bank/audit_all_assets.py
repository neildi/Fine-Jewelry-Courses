import os

mb = r'C:\Users\neelk\Downloads\Arena-App\Fine-Jewelry-Courses\media-bank'

# Video 01 (C6-M02)
v01 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '02-shapes-and-cuts/broll_oval_ring.mp4',
    '02-shapes-and-cuts/broll_toi_et_moi.mp4',
    '01-gemology-and-diamonds/gia_raytrace_clip.webm',
    '02-shapes-and-cuts/oval_bow_tie_visual_comparison.jpg',
    '01-gemology-and-diamonds/gia_cut_proportions_scintillation_clip.mp4',
    '01-gemology-and-diamonds/macro_carat_spread_comparison.jpg',
    '01-gemology-and-diamonds/gia_wireframe_clip.webm',
    '07-infographics-and-cards/card_01_shape_vs_cut.png',
    '07-infographics-and-cards/badge_shape_cut_outro.png'
]

# Video 02 (C6-M03)
v02 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '05-grading-reports-and-plots/gia_dossier_dual_specimens.jpg',
    '01-gemology-and-diamonds/gia_grading_clip.webm',
    '05-grading-reports-and-plots/gia_ags_ideal_aset_report_clip.mp4',
    '01-gemology-and-diamonds/aset_scope_optical_map.jpg',
    '01-gemology-and-diamonds/gia_diamond_cut_clip.mp4',
    '05-grading-reports-and-plots/how_to_hold_loupe_macro.jpg',
    '07-infographics-and-cards/card_02_gia_vs_ags.png',
    '07-infographics-and-cards/badge_lab_standards_outro.png'
]

# Video 03 (C6-M04)
v03 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '03-lab-grown-and-crystals/rough_crystal_comparison.jpg',
    '03-lab-grown-and-crystals/mantle_volcano_kimberlite_diagram.jpg',
    '03-lab-grown-and-crystals/cvd_plasma_reactor_chamber.jpg',
    '03-lab-grown-and-crystals/gia_id100_testing_device_clip.mp4',
    '06-counter-sales-and-consultation/luxury_consultation_couple.jpg',
    '06-counter-sales-and-consultation/heirloom_vintage_handover.jpg',
    '07-infographics-and-cards/card_03_natural_vs_lab.png',
    '07-infographics-and-cards/badge_diamond_origin_outro.png'
]

# Video 04 (C6-M05)
v04 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '04-metals-and-craftsmanship/metal_alloy_rings_comparison.jpg',
    '04-metals-and-craftsmanship/rhodium_plating_immersion.jpg',
    '04-metals-and-craftsmanship/platinum_density_patina_macro.jpg',
    '04-metals-and-craftsmanship/gia_microscope_prong_setting_clip.mp4',
    '04-metals-and-craftsmanship/bezel_set_diamond_ring_1791043122448.jpg',
    '04-metals-and-craftsmanship/ring_mandrel_comfort_fit_clip.mp4',
    '07-infographics-and-cards/card_04_metals_and_craftsmanship.png',
    '07-infographics-and-cards/badge_metals_craft_outro.png'
]

# Video 05 (C6-M06)
v05 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '04-metals-and-craftsmanship/finger_knuckle_measurement_macro.jpg',
    '04-metals-and-craftsmanship/ring_spin_on_finger_demonstration.jpg',
    '04-metals-and-craftsmanship/euro_shank_sizing_beads_macro.jpg',
    '04-metals-and-craftsmanship/ring_mandrel_comfort_fit_clip.mp4',
    '04-metals-and-craftsmanship/wide_band_vs_narrow_comparison.jpg',
    '06-counter-sales-and-consultation/ring_slide_on_finger_client.jpg',
    '07-infographics-and-cards/card_05_ring_sizing_architecture.png',
    '07-infographics-and-cards/badge_ring_sizing_outro.png'
]

# Video 06 (C1-M01)
v06 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '05-grading-reports-and-plots/gia_dossier_macro_specs.jpg',
    '01-gemology-and-diamonds/rough_diamond_cleaving_macro.jpg',
    '01-gemology-and-diamonds/gia_cut_proportions_scintillation_clip.mp4',
    '01-gemology-and-diamonds/macro_carat_spread_comparison.jpg',
    '06-counter-sales-and-consultation/daylight_counter_comparison.jpg',
    '01-gemology-and-diamonds/macro_fire_dispersion_colors.jpg',
    '07-infographics-and-cards/card_06_4cs_value_hierarchy.png',
    '07-infographics-and-cards/badge_4cs_hierarchy_outro.png'
]

# Video 07 (C1-M02)
v07 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '05-grading-reports-and-plots/how_to_hold_loupe_macro.jpg',
    '05-grading-reports-and-plots/diamond_girdle_laser_inscription_clip.mp4',
    '05-grading-reports-and-plots/laser_inscription_magnified_macro.jpg',
    '05-grading-reports-and-plots/gia_plot_diagram_feather_pinpoint.jpg',
    '05-grading-reports-and-plots/side_by_side_spec_audit_pad.jpg',
    '06-counter-sales-and-consultation/client_smiling_handshake_counter.jpg',
    '07-infographics-and-cards/card_07_loupe_mastery_protocol.png',
    '07-infographics-and-cards/badge_loupe_mastery_outro.png'
]

# Video 08 (C1-M05)
v08 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '01-gemology-and-diamonds/online_forum_warning_rumor.jpg',
    '01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_clip.mp4',
    '01-gemology-and-diamonds/fluorescent_daylight_sun_gleam.jpg',
    '01-gemology-and-diamonds/microscopic_feather_prong_concealed.jpg',
    '01-gemology-and-diamonds/gemological_inclusion_types_grid.jpg',
    '06-counter-sales-and-consultation/eye_clean_face_up_beauty.jpg',
    '07-infographics-and-cards/card_08_fluorescence_and_inclusions.png',
    '07-infographics-and-cards/badge_fluorescence_outro.png'
]

# Video 09 (C2-M01)
v09 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '06-counter-sales-and-consultation/customer_hesitant_entry.jpg',
    '06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4',
    '06-counter-sales-and-consultation/warm_concierge_greeting.jpg',
    '06-counter-sales-and-consultation/browsing_cases_couple.jpg',
    '06-counter-sales-and-consultation/advisor_warm_reapproach.jpg',
    '06-counter-sales-and-consultation/intimate_consultation_tray.jpg',
    '07-infographics-and-cards/card_09_first_90_seconds.png',
    '07-infographics-and-cards/badge_first_90s_outro.png'
]

# Video 10 (C2-M05)
v10 = [
    '06-counter-sales-and-consultation/neelkanth_intro_hook.mp4',
    '06-counter-sales-and-consultation/customer_holding_smartphone_counter.jpg',
    '06-counter-sales-and-consultation/luxury_counter_first_greeting_clip.mp4',
    '06-counter-sales-and-consultation/calm_advisor_listening.jpg',
    '05-grading-reports-and-plots/side_by_side_spec_audit_pad.jpg',
    '04-metals-and-craftsmanship/bench_polishing_and_steam_clean.jpg',
    '06-counter-sales-and-consultation/proposal_celebration_couple.jpg',
    '07-infographics-and-cards/card_10_defending_value.png',
    '07-infographics-and-cards/badge_defending_value_outro.png'
]

videos = {
    'V01': v01, 'V02': v02, 'V03': v03, 'V04': v04, 'V05': v05,
    'V06': v06, 'V07': v07, 'V08': v08, 'V09': v09, 'V10': v10
}

all_missing = {}
for name, asset_list in videos.items():
    missing = []
    # Check intra-video repetition
    seen = set()
    dupes = []
    for a in asset_list:
        if a in seen:
            dupes.append(a)
        seen.add(a)
        full_p = os.path.join(mb, a)
        if not os.path.exists(full_p):
            missing.append(a)
    if dupes:
        print(f"[{name}] WARNING: REPETITIONS DETECTED: {dupes}")
    all_missing[name] = missing
    print(f"[{name}] Total: {len(asset_list)} | Missing: {len(missing)}")

print("\n--- Summary of Missing Assets ---")
unique_missing = set()
for name, m_list in all_missing.items():
    for item in m_list:
        unique_missing.add(item)
print(f"Total Unique Assets to Generate/Sustain: {len(unique_missing)}")
for item in sorted(unique_missing):
    print(" -", item)
