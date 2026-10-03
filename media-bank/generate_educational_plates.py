from PIL import Image, ImageDraw, ImageFont
import os
import math

font_geo = 'media-bank/georgia.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'
if not os.path.exists(font_arial):
    font_arial = font_geo

W, H = 1920, 1080

def create_base(title, category_tag):
    img = Image.new('RGB', (W, H), (11, 15, 23)) # Deep Onyx
    draw = ImageDraw.Draw(img)
    # Subtle border
    draw.rectangle([40, 40, W-40, H-40], outline=(40, 48, 64), width=1)
    # Top tags
    f_tag = ImageFont.truetype(font_arial, 15)
    f_h1 = ImageFont.truetype(font_geo, 36)
    draw.text((80, 70), 'JEWELSWELL ACADEMY  •  ' + category_tag.upper(), font=f_tag, fill=(201, 162, 39))
    draw.text((80, 98), title, font=f_h1, fill=(255, 255, 255))
    return img, draw

# 1. Carat Spread Comparison Plate
def gen_carat_spread():
    img, draw = create_base("Carat Weight vs. Millimeter Spread (Face-Up Diameter)", "Optical Anatomy & Proportions")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 30)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Excellent Cut 1.00ct (6.5mm)
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), "IDEAL CUT — OPTIMIZED WEIGHT DISTRIBUTION", font=f_lbl, fill=(11, 15, 23))
    
    # Diamond circle
    draw.ellipse([340, 310, 700, 670], outline=(223, 190, 84), width=4, fill=(26, 34, 52))
    draw.text((450, 470), "6.5 mm", font=f_val, fill=(255, 255, 255))
    draw.text((435, 520), "1.00 Carat Round", font=f_lbl, fill=(148, 163, 184))

    draw.text((160, 710), "• Table: 56%  |  Depth: 61.2%  |  Crown Angle: 34.5°", font=f_lbl, fill=(226, 232, 240))
    draw.text((160, 750), "• Total Internal Reflection: 98% Light Directed to Eye", font=f_lbl, fill=(223, 190, 84))
    draw.text((160, 790), "• Result: Looks huge, brilliant, and masks tint face-up", font=f_sub, fill=(148, 163, 184))

    # Box 2: Deep Cut 1.00ct (5.9mm)
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(153, 27, 27), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(153, 27, 27))
    draw.text((1030, 218), "DEEP CUT — WEIGHT TRAPPED IN PAVILION (AMATEUR TRAP)", font=f_lbl, fill=(255, 255, 255))
    
    # Diamond circle
    draw.ellipse([1260, 340, 1540, 620], outline=(248, 113, 113), width=4, fill=(26, 34, 52))
    draw.text((1330, 465), "5.9 mm", font=f_val, fill=(248, 113, 113))
    draw.text((1315, 515), "1.00 Carat Round", font=f_lbl, fill=(148, 163, 184))

    draw.text((1040, 710), "• Table: 64%  |  Depth: 67.5% (Extremely Deep Pavilion)", font=f_lbl, fill=(226, 232, 240))
    draw.text((1040, 750), "• Severe Light Leakage: Light Escapes Out the Bottom", font=f_lbl, fill=(248, 113, 113))
    draw.text((1040, 790), "• Result: Looks like a 0.75ct diamond on the finger; dark center", font=f_sub, fill=(148, 163, 184))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SALES COUNTER RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Carat is weight, not visual size. A well-cut 0.90ct stone outshines a deep 1.10ct stone every time.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/macro_carat_spread_comparison.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 2. ASET Scope Optical Map
def gen_aset_map():
    img, draw = create_base("ASET Scope Diagnostics: Decoding Light Performance", "Gemological Optical Verification")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 4 Quadrants / Legend
    legends = [
        ("RED (45° – 75° ANGLES)", "Direct Light Return & Intense Face-Up Brilliance", (220, 38, 38), 120, 220),
        ("GREEN (0° – 45° ANGLES)", "Lower-Angle Ambient Light Reflection from Horizon", (34, 197, 94), 980, 220),
        ("BLUE (75° – 90° ANGLES)", "Controlled Contrast & Obstruction (Essential for Scintillation)", (59, 130, 246), 120, 530),
        ("WHITE / CLEAR AREAS", "Severe Light Leakage (Light Escaping Through the Pavilion)", (148, 163, 184), 980, 530),
    ]

    for title, desc, color, x, y in legends:
        draw.rectangle([x, y, x + 820, y + 260], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, y, x + 820, y + 55], fill=color)
        draw.text((x + 25, y + 16), title, font=f_lbl, fill=(255, 255, 255))
        
        # Color sample circle
        draw.ellipse([x + 35, y + 90, x + 155, y + 210], fill=color, outline=(255, 255, 255), width=2)
        
        draw.text((x + 190, y + 105), desc, font=f_val, fill=(255, 255, 255))
        if "RED" in title:
            draw.text((x + 190, y + 150), "• Desired in 70%+ of table and crown facets for elite performance.", font=f_sub, fill=(226, 232, 240))
        elif "GREEN" in title:
            draw.text((x + 190, y + 150), "• Complements red; maintains brightness in dim ambient environments.", font=f_sub, fill=(226, 232, 240))
        elif "BLUE" in title:
            draw.text((x + 190, y + 150), "• Must be crisp and symmetric (e.g., 8-arrow pattern), not chaotic.", font=f_sub, fill=(226, 232, 240))
        else:
            draw.text((x + 190, y + 150), "• Windowing or fisheye defect; indicates poor pavilion angles.", font=f_sub, fill=(248, 113, 113))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(201, 162, 39), width=1)
    draw.text((160, 922), "ASET ADVISORY PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"Do not rely solely on 'Triple Excellent' on paper. An ASET map exposes real-world light leakage.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/aset_scope_optical_map.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 3. Knuckle vs Base Sizing Mechanics
def gen_knuckle_mechanics():
    img, draw = create_base("Knuckle vs. Base Mechanics: Solving Solitaire Spin", "Bridal Fit & Sizing Engineering")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(153, 27, 27), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(153, 27, 27))
    draw.text((150, 218), "THE AMATEUR SIZING DILEMMA", font=f_lbl, fill=(255, 255, 255))
    
    draw.text((160, 300), "Knuckle Diameter: 17.5 mm (US Size 7.25)", font=f_val, fill=(248, 113, 113))
    draw.text((160, 350), "Finger Base Diameter: 16.0 mm (US Size 5.5)", font=f_val, fill=(148, 163, 184))
    
    draw.text((160, 430), "• Sizing down to Size 5.5:", font=f_lbl, fill=(255, 255, 255))
    draw.text((180, 470), "Ring cannot cross the knuckle. Causes bruising, pain, and panic.", font=f_sub, fill=(248, 113, 113))

    draw.text((160, 540), "• Sizing up to Size 7.25:", font=f_lbl, fill=(255, 255, 255))
    draw.text((180, 580), "Glides past knuckle, but spins 180° upside-down on the finger base.", font=f_sub, fill=(248, 113, 113))

    draw.text((160, 660), "• Root Cause:", font=f_lbl, fill=(223, 190, 84))
    draw.text((180, 700), "Top-heavy solitaire center of gravity + loose cylindrical shank gap.", font=f_sub, fill=(226, 232, 240))

    # Master Architectural Solution
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(201, 162, 39))
    draw.text((1030, 218), "THE MASTER FIT ARCHITECTURE", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 300), "SOLUTION 1: SIZING BEADS (PLATINUM/GOLD)", font=f_val, fill=(223, 190, 84))
    draw.text((1040, 345), "• Two interior dome beads create spring tension at bottom of finger.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 380), "• Lets knuckle pass smoothly, then locks shank upright on the base.", font=f_sub, fill=(226, 232, 240))

    draw.text((1040, 450), "SOLUTION 2: EURO SHANK (SQUARE BASE)", font=f_val, fill=(223, 190, 84))
    draw.text((1040, 495), "• Subtle squared corners at 4 and 8 o'clock stabilize adjacent fingers.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 530), "• Counterbalances heavy diamond centerstone with zero ring tilt.", font=f_sub, fill=(226, 232, 240))

    draw.text((1040, 600), "SOLUTION 3: COMFORT-FIT INTERIOR", font=f_val, fill=(223, 190, 84))
    draw.text((1040, 645), "• Convex inner curve reduces friction over the joint by 40%.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 680), "• Always read center apex of the curve on a tapered sizing mandrel.", font=f_sub, fill=(201, 162, 39))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "MASTER SIZING RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((400, 918), "\"Measure the knuckle for passage; engineer the shank architecture for lifetime stability.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/finger_knuckle_measurement_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 4. Metallurgy Comparison
def gen_metals_comparison():
    img, draw = create_base("Mounting Metallurgy: Platinum 950 vs. 14K/18K Gold", "Precious Metals & Longevity")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    metals = [
        ("PLATINUM 950", "95% Pure Platinum + 5% Ruthenium/Iridium", "Displaces metal; develops rich patina", "High Tenacity: Prongs bend without snapping", (223, 190, 84), 120),
        ("18K YELLOW / ROSE GOLD", "75% Pure Gold + 25% Copper/Silver Alloy", "Warm rich luster; high tarnish resistance", "Moderate: Prongs require retipping at 7-10 yrs", (234, 179, 8), 680),
        ("14K WHITE GOLD", "58.3% Pure Gold + Nickel/Zinc + Rhodium", "Requires periodic rhodium replating (12-18mo)", "Rigid/Brittle: Can shear under severe blunt force", (226, 232, 240), 1240),
    ]

    for title, alloy, wear, security, color, x in metals:
        draw.rectangle([x, 220, x + 520, 850], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 520, 280], fill=(26, 34, 52))
        draw.rectangle([x, 220, x + 8, 280], fill=color)
        draw.text((x + 25, 238), title, font=f_lbl, fill=color)

        draw.text((x + 25, 310), "ALLOY COMPOSITION:", font=f_lbl, fill=(148, 163, 184))
        draw.text((x + 25, 345), alloy, font=f_sub, fill=(255, 255, 255))

        draw.text((x + 25, 430), "WEAR PROFILE OVER 20 YEARS:", font=f_lbl, fill=(148, 163, 184))
        draw.text((x + 25, 465), wear, font=f_sub, fill=(226, 232, 240))

        draw.text((x + 25, 550), "PRONG SECURITY & TENACITY:", font=f_lbl, fill=(148, 163, 184))
        draw.text((x + 25, 585), security, font=f_sub, fill=(226, 232, 240))

        draw.text((x + 25, 670), "LIFESTYLE RECOMMENDATION:", font=f_lbl, fill=(148, 163, 184))
        if "PLATINUM" in title:
            draw.text((x + 25, 705), "• Best for active lifestyles & 2ct+ diamonds.", font=f_sub, fill=(223, 190, 84))
            draw.text((x + 25, 735), "• 100% Hypoallergenic for sensitive skin.", font=f_sub, fill=(223, 190, 84))
        elif "YELLOW" in title:
            draw.text((x + 25, 705), "• Modern luxury resurgence; complements G-J stones.", font=f_sub, fill=(234, 179, 8))
            draw.text((x + 25, 735), "• Classic heirloom warmth, zero plating maintenance.", font=f_sub, fill=(234, 179, 8))
        else:
            draw.text((x + 25, 705), "• Economical bright white finish.", font=f_sub, fill=(226, 232, 240))
            draw.text((x + 25, 735), "• Advise client on routine rhodium immersion care.", font=f_sub, fill=(226, 232, 240))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "METALLURGICAL RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((400, 918), "\"Gold loses microscopic metal with wear; Platinum displaces. Never compromise center stone security.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/metal_alloy_rings_comparison.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 5. 3-Point Laser Inscription Verification Protocol
def gen_loupe_protocol():
    img, draw = create_base("The 3-Point Counter Verification Protocol", "Gemological Security & Intake")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    steps = [
        ("POINT 1: 10X LOUPE GIRDLE INSCRIBE", "Read microscopic GIA report number on stone girdle", "Hold 10x triplet loupe to cheek; bring diamond to focus. Verify laser characters under bright, directional counter lighting.", (201, 162, 39), 120),
        ("POINT 2: PHYSICAL DOSSIER PLOT MATCH", "Align inclusion diagram with actual stone anatomy", "Cross-check pinpoint and feather plot coordinates against stone under 10x. Confirm exact carat, color, and cut grades.", (59, 130, 246), 680),
        ("POINT 3: LIVE GIA CLOUD REPORT CHECK", "Real-time digital authentication in front of client", "Open gia.edu/report-check on store tablet. Confirm archived laboratory PDF record matches physical stone and certificate.", (34, 197, 94), 1240),
    ]

    for title, subtitle, desc, color, x in steps:
        draw.rectangle([x, 220, x + 520, 850], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 520, 280], fill=color)
        draw.text((x + 25, 238), title, font=f_lbl, fill=(11, 15, 23))

        draw.text((x + 25, 320), subtitle, font=f_val, fill=(255, 255, 255))
        draw.text((x + 25, 420), "PROCEDURAL INSTRUCTION:", font=f_lbl, fill=(148, 163, 184))
        
        # Word wrap desc
        words = desc.split()
        cur_line = ""
        y = 460
        for w in words:
            if len(cur_line + " " + w) > 35:
                draw.text((x + 25, y), cur_line, font=f_sub, fill=(226, 232, 240))
                y += 30
                cur_line = w
            else:
                cur_line = cur_line + " " + w if cur_line else w
        if cur_line:
            draw.text((x + 25, y), cur_line, font=f_sub, fill=(226, 232, 240))

        draw.text((x + 25, 620), "CLIENT PSYCHOLOGY:", font=f_lbl, fill=color)
        if "POINT 1" in title:
            draw.text((x + 25, 655), "Transforms passive buying into thrilling scientific discovery.", font=f_sub, fill=(223, 190, 84))
        elif "POINT 2" in title:
            draw.text((x + 25, 655), "Eliminates all anxiety regarding stone substitution or error.", font=f_sub, fill=(223, 190, 84))
        else:
            draw.text((x + 25, 655), "Establishes bulletproof institutional authority and credibility.", font=f_sub, fill=(223, 190, 84))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "INTAKE STANDARD:", font=f_lbl, fill=(201, 162, 39))
    draw.text((360, 918), "\"Transparency builds luxury loyalty. Never hand over a diamond without completing the 3-Point Audit.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/how_to_hold_loupe_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

if __name__ == "__main__":
    gen_carat_spread()
    gen_aset_map()
    gen_knuckle_mechanics()
    gen_metals_comparison()
    gen_loupe_protocol()
    print("Core educational diagram plates rendered.")

# 6. GIA Plot Diagram & Inclusions
def gen_plot_diagram():
    img, draw = create_base("Diamond Clarity Plotting & Inclusion Mapping", "GIA Lab Standards & Plot Anatomy")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Left: Crown Plot
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), "CROWN PLOT (FACE-UP VIEW)", font=f_lbl, fill=(11, 15, 23))
    
    # Octagon Table
    draw.polygon([(460, 340), (580, 340), (660, 420), (660, 540), (580, 620), (460, 620), (380, 540), (380, 420)], outline=(223, 190, 84), width=3, fill=(26, 34, 52))
    # Pinpoint
    draw.ellipse([450, 410, 460, 420], fill=(239, 68, 68))
    draw.text((475, 405), "Red: Internal Pinpoint (Microscopic)", font=f_sub, fill=(248, 113, 113))

    # Feather near edge
    draw.line([(630, 520), (645, 545)], fill=(239, 68, 68), width=3)
    draw.text((660, 530), "Feather (Under Prong)", font=f_sub, fill=(34, 197, 94))

    draw.text((160, 710), "KEY GRADING RULES FOR EYE-CLEANLINESS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 750), "• Pinpoint under table: Invisible without 10x magnification.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 785), "• Feather at girdle edge: Can be safely masked beneath mounting prong.", font=f_sub, fill=(226, 232, 240))

    # Right: Pavilion Plot
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(51, 65, 85), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(30, 41, 59))
    draw.text((1030, 218), "PAVILION PLOT (LOWER VIEW)", font=f_lbl, fill=(255, 255, 255))
    
    draw.ellipse([1260, 340, 1540, 620], outline=(148, 163, 184), width=3, fill=(26, 34, 52))
    draw.ellipse([1395, 475, 1405, 485], fill=(223, 190, 84))
    draw.text((1420, 470), "Culet (Point)", font=f_sub, fill=(148, 163, 184))

    draw.text((1040, 710), "GIA SYMBOL LEGEND:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 750), "• RED = Internal Inclusion (Pinpoint, Crystal, Cloud, Feather)", font=f_sub, fill=(248, 113, 113))
    draw.text((1040, 785), "• GREEN = External Blemish (Natural, Nick, Scratch, Polish mark)", font=f_sub, fill=(34, 197, 94))
    draw.text((1040, 820), "• BLACK = Extra Facet (Not affecting clarity grade)", font=f_sub, fill=(148, 163, 184))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "COUNTER DRILL:", font=f_lbl, fill=(201, 162, 39))
    draw.text((360, 918), "\"Always match the red inclusion markers on the plot to the actual stone under 10x. It proves stone identity.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/gia_plot_diagram_feather_pinpoint.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 7. Laser Inscription Magnified Macro
def gen_laser_inscription():
    img, draw = create_base("Girdle Laser Inscription: 20x Verification View", "Gemological Security & GIA Dossier")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 32)
    f_sub = ImageFont.truetype(font_arial, 16)
    f_note = ImageFont.truetype(font_geo, 22)

    # Simulated Girdle Facet
    draw.rectangle([120, 240, 1800, 800], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    
    # Diamond faceted girdle band
    draw.rectangle([160, 420, 1760, 580], fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((200, 360), "MICROSCOPIC GIRDLE SURFACE (20X MAGNIFICATION)", font=f_lbl, fill=(148, 163, 184))
    
    # Microscopic Inscription Text
    draw.text((450, 475), "G I A   2 1 8 5 4 9 1 0 2 4", font=f_val, fill=(223, 190, 84))
    draw.rectangle([380, 470, 425, 530], outline=(223, 190, 84), width=2)
    draw.text((392, 485), "G", font=f_lbl, fill=(223, 190, 84))

    draw.text((200, 640), "GIA INSCRIPTION PROTOCOL STANDARDS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((200, 680), "• Inscribed automatically on all GIA Diamond Dossier reports.", font=f_sub, fill=(226, 232, 240))
    draw.text((200, 715), "• Depth is microscopic (fractions of a micron)—has zero effect on clarity grade.", font=f_sub, fill=(226, 232, 240))
    draw.text((200, 750), "• Validates stone identity permanently without risking stone structure.", font=f_sub, fill=(226, 232, 240))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "VERIFICATION STANDARD:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Read the inscription digits aloud with the client. It converts skepticism into absolute certainty.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/laser_inscription_magnified_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 8. Showrooming Side-by-Side Audit Pad
def gen_showroom_audit_pad():
    img, draw = create_base("Like-for-Like Value Audit: The Showrooming Defense", "Fine Jewelry Sales Conversation")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 24)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    rows = [
        ("1. Center Diamond Cut Make", "Deep cut, light leakage, unverified bow tie", "Ideal proportions, verified ASET light return"),
        ("2. Mounting Construction", "Hollow, lightweight casting (<2.5g), thin prongs", "Solid comfort-fit shank (>4.5g), heavy prongs"),
        ("3. Diamond Origin & Verification", "Third-party soft cert, no laser inscription check", "GIA Dossier + Live 3-Point Counter Inscription Match"),
        ("4. Sizing & Alteration Friction", "Client pays shipping & waiting 4-6 weeks for resize", "Immediate in-house bench sizing & exact knuckle fit"),
        ("5. Lifetime Care & Accountability", "Voicemail customer service, return restocking fee", "Complimentary lifetime cleaning, inspection & local bond"),
    ]

    # Header row
    draw.rectangle([120, 220, 1800, 280], fill=(201, 162, 39))
    draw.text((150, 240), "COMPARISON FACTOR", font=f_lbl, fill=(11, 15, 23))
    draw.text((650, 240), "ONLINE COMMODITY LISTING", font=f_lbl, fill=(11, 15, 23))
    draw.text((1250, 240), "JEWELSWELL LUXURY SHOWROOM", font=f_lbl, fill=(11, 15, 23))

    y = 290
    for factor, bad, good in rows:
        draw.rectangle([120, y, 1800, y + 100], fill=(18, 24, 36), outline=(40, 48, 64), width=1)
        draw.text((150, y + 35), factor, font=f_val, fill=(255, 255, 255))
        draw.text((650, y + 38), bad, font=f_sub, fill=(248, 113, 113))
        draw.text((1250, y + 38), good, font=f_sub, fill=(34, 197, 94))
        y += 110

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SHOWROOMING DEFENSE SCRIPT:", font=f_lbl, fill=(201, 162, 39))
    draw.text((480, 918), "\"When two items have different quality, service, and security, their prices cannot be compared.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/side_by_side_spec_audit_pad.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 9. Online Forum Warning vs GIA Research (Fluorescence)
def gen_fluorescence_myth():
    img, draw = create_base("Diamond Fluorescence: Internet Myth vs. GIA Scientific Truth", "Gemological Research & Optics")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 16)
    f_note = ImageFont.truetype(font_geo, 22)

    # Left: The Internet Rumor
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(153, 27, 27), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(153, 27, 27))
    draw.text((150, 218), "THE INTERNET FORUM MYTH", font=f_lbl, fill=(255, 255, 255))
    
    draw.text((160, 310), "\"Never buy a diamond with fluorescence! It makes the", font=f_val, fill=(248, 113, 113))
    draw.text((160, 350), "stone look milky, hazy, and destroys its resale value.\"", font=f_val, fill=(248, 113, 113))

    draw.text((160, 450), "• Fallacy 1: Assumes all fluorescence causes visible haze.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 500), "• Fallacy 2: Discounts stones without checking face-up optics.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 550), "• Fallacy 3: Pushes buyers toward paying unnecessary premiums.", font=f_sub, fill=(226, 232, 240))

    # Right: GIA Research Truth
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "GIA SCIENTIFIC STUDY FINDINGS", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 310), "< 0.2% Of Fluorescent Diamonds Show Haze", font=f_val, fill=(223, 190, 84))
    draw.text((1040, 350), "In the Vast Majority, It Is an Optical Asset.", font=f_val, fill=(255, 255, 255))

    draw.text((1040, 450), "• Natural Color Whitener: Daylight UV cancels faint yellow in I-K stones.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 500), "• Zero Structural Impact: Does not alter diamond hardness or durability.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 550), "• Incredible Value: Saves client 5-15% while delivering superior face-up color.", font=f_sub, fill=(34, 197, 94))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "MASTER ADVISORY PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"Demystify fluorescence with live daylight observation. Science turns anxiety into client delight.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/online_forum_warning_rumor.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 10. CVD vs HPHT Crystal Growth Diagram
def gen_crystal_growth():
    img, draw = create_base("Diamond Synthesis: CVD vs. HPHT Crystal Growth", "Laboratory-Grown Science & Detection")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 16)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: CVD
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(59, 130, 246), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(59, 130, 246))
    draw.text((150, 218), "CHEMICAL VAPOR DEPOSITION (CVD)", font=f_lbl, fill=(255, 255, 255))
    
    draw.text((160, 310), "Vacuum Chamber + Microwave Gas Plasma", font=f_val, fill=(223, 190, 84))
    draw.text((160, 360), "• Carbon gases (CH4) energized into plasma at 800-1000°C.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 410), "• Pure carbon atoms precipitate layer-by-layer onto diamond seed plates.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 460), "• Growth Morphology: Tabular cube / flat wafer.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 510), "• Diagnostic Features: Striated strain patterns; often Type IIa purity.", font=f_sub, fill=(148, 163, 184))

    # Box 2: HPHT
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(201, 162, 39))
    draw.text((1030, 218), "HIGH PRESSURE HIGH TEMPERATURE (HPHT)", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 310), "Hydraulic Multi-Anvil Press (1400°C & 60,000 Atm)", font=f_val, fill=(223, 190, 84))
    draw.text((1040, 360), "• Replicates Earth's deep mantle pressure using metallic flux (Fe, Ni, Co).", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 410), "• Carbon dissolves into molten metal and crystallizes on diamond seed.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 460), "• Growth Morphology: Cuboctahedral crystals.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 510), "• Diagnostic Features: Hourglass growth sectors; metallic flux inclusions.", font=f_sub, fill=(148, 163, 184))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "DETECTION CRITERIA:", font=f_lbl, fill=(201, 162, 39))
    draw.text((380, 918), "\"Because both CVD and HPHT test as 100% diamond on standard thermal pens, use the GIA iD100 to screen.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/03-lab-grown-and-crystals/cvd_plasma_reactor_chamber.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 11. Oval Diamond Bow-Tie Optical Analysis Plate
def gen_bowtie_comparison():
    img, draw = create_base("The Fancy Shape Bow-Tie Effect: Optical Analysis", "Fancy Shape Geometry & Cut Quality")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Severe Bow-Tie
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(153, 27, 27), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(153, 27, 27))
    draw.text((150, 218), "SEVERE BOW-TIE (OPTICAL DEFECT)", font=f_lbl, fill=(255, 255, 255))
    
    # Oval outline
    draw.ellipse([340, 310, 700, 620], outline=(248, 113, 113), width=4, fill=(26, 34, 52))
    # Dark bow-tie shape across center
    draw.polygon([(420, 420), (620, 510), (420, 510), (620, 420)], fill=(5, 5, 8), outline=(248, 113, 113), width=1)
    draw.text((455, 450), "BLACK BAND", font=f_lbl, fill=(248, 113, 113))

    draw.text((160, 700), "DIAGNOSTIC CHARACTERISTICS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 735), "• Persistent dark shadow across width of stone that stays black in motion.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 770), "• Caused by steep pavilion angles reflecting observer's head/shadow back.", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 805), "• Kills center sparkle; looks dull and lifeless in natural room lighting.", font=f_sub, fill=(248, 113, 113))

    # Box 2: Controlled / Lively Bow-Tie
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "BALANCED / HIGH-PERFORMANCE OVAL", font=f_lbl, fill=(11, 15, 23))

    # Oval outline
    draw.ellipse([1220, 310, 1580, 620], outline=(34, 197, 94), width=4, fill=(26, 34, 52))
    # Lively subtle facet lines
    draw.line([(1400, 310), (1400, 620)], fill=(223, 190, 84), width=2)
    draw.line([(1220, 465), (1580, 465)], fill=(223, 190, 84), width=2)
    draw.polygon([(1350, 430), (1450, 430), (1480, 465), (1450, 500), (1350, 500), (1320, 465)], outline=(255, 255, 255), width=2, fill=(30, 41, 59))
    draw.text((1340, 452), "LIVELY FIRE", font=f_lbl, fill=(223, 190, 84))

    draw.text((1040, 700), "IDEAL PERFORMANCE CHARACTERISTICS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 735), "• Subtle contrast pattern that breaks up into flashing scintillation when moved.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 770), "• Proportions calibrated: Table 54-58%, Depth 59-62.5%, L:W 1.35-1.45.", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 805), "• Delivers edge-to-edge brightness, crisp fire, and excellent scintillation.", font=f_sub, fill=(34, 197, 94))

    # Bottom takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SALES COUNTER RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Some bow-tie is natural in elongated shapes. The goal is lively contrast, never a black dead band.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/02-shapes-and-cuts/oval_bow_tie_visual_comparison.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)
