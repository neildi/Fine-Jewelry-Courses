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
    # Luxury border
    draw.rectangle([40, 40, W-40, H-40], outline=(40, 48, 64), width=1)
    draw.rectangle([44, 44, W-44, H-44], outline=(201, 162, 39), width=1)
    
    # Top tags
    f_tag = ImageFont.truetype(font_arial, 15)
    f_h1 = ImageFont.truetype(font_geo, 34)
    draw.text((80, 70), 'JEWELSWELL ACADEMY  •  ' + category_tag.upper(), font=f_tag, fill=(201, 162, 39))
    draw.text((80, 98), title, font=f_h1, fill=(255, 255, 255))
    return img, draw

# 1. GIA Dossier Dual Specimens (V02)
def gen_gia_dossier_dual():
    img, draw = create_base("GIA Dossier Specification Audit: Triple Excellent Boundaries", "Grading Standards & Performance")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Borderline Triple Ex (62.9% Depth)
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(245, 158, 11), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(245, 158, 11))
    draw.text((150, 218), "SPECIMEN A: BORDERLINE EXCELLENT (STEEP/DEEP)", font=f_lbl, fill=(11, 15, 23))
    
    draw.rectangle([160, 300, 880, 520], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.text((180, 320), "GIA Report: #6224819034", font=f_sub, fill=(148, 163, 184))
    draw.text((180, 350), "1.01 ct Round Brilliant  |  F Color  |  VS1 Clarity", font=f_val, fill=(255, 255, 255))
    draw.text((180, 400), "• Table: 59%  |  Total Depth: 62.9% (Borderline Deep)", font=f_lbl, fill=(245, 158, 11))
    draw.text((180, 435), "• Crown Angle: 35.5°  |  Pavilion Angle: 41.2°", font=f_lbl, fill=(226, 232, 240))
    draw.text((180, 470), "• Cut Grade: GIA Excellent (Steep/Deep Combination)", font=f_lbl, fill=(245, 158, 11))

    draw.text((160, 560), "OPTICAL BEHAVIOR ANALYSIS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 600), "• Facet angles cause slight ring leakage under table edge", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 635), "• Millimeter spread: 6.35 mm (Sacrifices 0.15mm diameter)", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 670), "• ASET Score: AGS 2-3 (Good light return, minor leakage)", font=f_sub, fill=(148, 163, 184))
    draw.text((160, 720), "Retail Trap: Sold at full premium solely on paper grade.", font=f_lbl, fill=(248, 113, 113))

    # Box 2: Optimum Sweet Spot (61.4% Depth)
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "SPECIMEN B: SWEET SPOT EXCELLENT / AGS 0 IDEAL", font=f_lbl, fill=(11, 15, 23))

    draw.rectangle([1040, 300, 1760, 520], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.text((1060, 320), "GIA Report: #2185491024", font=f_sub, fill=(148, 163, 184))
    draw.text((1060, 350), "1.00 ct Round Brilliant  |  G Color  |  VS2 Clarity", font=f_val, fill=(255, 255, 255))
    draw.text((1060, 400), "• Table: 56%  |  Total Depth: 61.4% (Optimal)", font=f_lbl, fill=(34, 197, 94))
    draw.text((1060, 435), "• Crown Angle: 34.5°  |  Pavilion Angle: 40.8°", font=f_lbl, fill=(226, 232, 240))
    draw.text((1060, 470), "• Cut Grade: GIA Excellent + AGS 0 Ideal Light Return", font=f_lbl, fill=(34, 197, 94))

    draw.text((1040, 560), "OPTICAL BEHAVIOR ANALYSIS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 600), "• Total Internal Reflection: Zero table edge windowing", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 635), "• Millimeter spread: 6.51 mm (Visibly larger face-up)", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 670), "• ASET Score: AGS 0 Ideal (Intense red light return)", font=f_sub, fill=(148, 163, 184))
    draw.text((1040, 720), "Master Advantage: Masks G-color face up; saves client $1,400.", font=f_lbl, fill=(34, 197, 94))

    # Bottom Takeaway
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "MASTER PROTOCOL:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Never sell the grade alone. Audit crown and pavilion angles to verify optical performance.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/gia_dossier_dual_specimens.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 2. Rough Crystal Comparison (V03)
def gen_rough_crystal():
    img, draw = create_base("Crystal Growth Morphology: Natural Octahedral vs. CVD Cuboid", "Gemological Physics & Origin")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Natural Octahedron
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), "NATURAL DIAMOND — OCTAHEDRAL GEOLOGICAL CRYSTAL", font=f_lbl, fill=(11, 15, 23))
    
    # Octahedron drawing
    draw.polygon([(520, 310), (370, 480), (670, 480)], outline=(223, 190, 84), fill=(30, 40, 60), width=3)
    draw.polygon([(520, 650), (370, 480), (670, 480)], outline=(223, 190, 84), fill=(24, 32, 48), width=3)
    draw.line([(520, 310), (520, 650)], fill=(201, 162, 39), width=2)
    draw.text((460, 470), "Type Ia", font=f_val, fill=(255, 255, 255))

    draw.text((160, 690), "• Geological Growth: 1.0 to 3.3 Billion Years in Earth's Mantle", font=f_lbl, fill=(226, 232, 240))
    draw.text((160, 725), "• Nitrogen Chemistry: Aggregated A & B nitrogen clusters (98% of natural)", font=f_sub, fill=(201, 162, 39))
    draw.text((160, 760), "• Supply Metric: Finite, diminishing global mine yields", font=f_sub, fill=(148, 163, 184))
    draw.text((160, 795), "• Value Frame: Multi-generational provenance, heritage asset", font=f_lbl, fill=(255, 255, 255))

    # Box 2: CVD Tabular Cuboid
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(96, 165, 250), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(96, 165, 250))
    draw.text((1030, 218), "LAB-GROWN — TABULAR CUBOID CVD / HPHT CRYSTAL", font=f_lbl, fill=(11, 15, 23))

    # Cube drawing
    draw.rectangle([1250, 340, 1550, 620], outline=(96, 165, 250), fill=(24, 38, 65), width=3)
    draw.text((1330, 470), "Type IIa", font=f_val, fill=(255, 255, 255))

    draw.text((1040, 690), "• Technological Growth: 300 to 500 Hours in Plasma Reactor", font=f_lbl, fill=(226, 232, 240))
    draw.text((1040, 725), "• Carbon Purity: 100% Carbon; zero nitrogen impurities (Type IIa)", font=f_sub, fill=(96, 165, 250))
    draw.text((1040, 760), "• Supply Metric: Exponentially scalable manufacturing capacity", font=f_sub, fill=(148, 163, 184))
    draw.text((1040, 795), "• Value Frame: Maximum carat size per budget dollar today", font=f_lbl, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "ACADEMY DIRECTIVE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Both are 100% diamond. Advise without stigma: align with the client's emotional priorities.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/03-lab-grown-and-crystals/rough_crystal_comparison.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 3. Mantle Kimberlite Diagram (V03)
def gen_kimberlite_diagram():
    img, draw = create_base("Geological Provenance: The Kimberlite Pipe Journey", "Earth Science & Diamond Formation")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 24)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Cross section layers
    # Layer 1: Earth Surface
    draw.rectangle([120, 200, 1800, 320], fill=(45, 55, 72), outline=(74, 85, 104), width=1)
    draw.text((150, 220), "CONTINENTAL CRUST (0 – 35 KM DEPTH)", font=f_lbl, fill=(201, 162, 39))
    draw.text((150, 255), "• Sedimentary & metamorphic rock layers", font=f_sub, fill=(226, 232, 240))
    draw.text((150, 280), "• Showcase mining operations (open pit & underground)", font=f_sub, fill=(148, 163, 184))

    # Layer 2: Lithospheric Mantle
    draw.rectangle([120, 340, 1800, 560], fill=(30, 41, 59), outline=(51, 65, 85), width=1)
    draw.text((150, 360), "UPPER MANTLE & DIAMOND STABILITY ZONE (150 – 200 KM DEPTH)", font=f_lbl, fill=(245, 158, 11))
    draw.text((150, 395), "• Temperature: 1,150°C – 1,350°C  |  Pressure: 45,000 – 60,000 Atmospheres", font=f_val, fill=(255, 255, 255))
    draw.text((150, 440), "• Carbon crystallizes into isometric diamond lattice over 1 to 3 billion years", font=f_sub, fill=(226, 232, 240))
    draw.text((150, 475), "• Diamonds do NOT form from coal; they predate terrestrial plant life on Earth", font=f_sub, fill=(201, 162, 39))
    draw.text((150, 510), "• Preserved in deep cratonic mantle keels beneath ancient continental shields", font=f_sub, fill=(148, 163, 184))

    # Layer 3: Kimberlite Volcanic Conduit
    draw.rectangle([120, 580, 1800, 850], fill=(24, 30, 45), outline=(220, 38, 38), width=2)
    draw.text((150, 600), "KIMBERLITE SUPERSONIC MAGMA ERUPTION (THE ELEVATOR)", font=f_lbl, fill=(248, 113, 113))
    draw.text((150, 635), "• Violent, deep-seated volcanic eruptions traveling at up to 100 km/h", font=f_sub, fill=(226, 232, 240))
    draw.text((150, 670), "• Rapid ascent quenches crystals: prevents diamond from graphitizing back into carbon", font=f_val, fill=(255, 255, 255))
    draw.text((150, 715), "• Less than 1 in 200 kimberlite pipes contain commercial gem-grade diamonds", font=f_sub, fill=(201, 162, 39))
    draw.text((150, 750), "• Most recent known kimberlite eruption: over 40 million years ago", font=f_sub, fill=(148, 163, 184))
    draw.text((150, 785), "• Geological Rarity: Natural diamonds are physical artifacts of deep terrestrial history", font=f_lbl, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SALES DISCOVERY INSIGHT:", font=f_lbl, fill=(201, 162, 39))
    draw.text((440, 918), "\"When a buyer chooses natural, they are investing in finite geological antiquity.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/03-lab-grown-and-crystals/mantle_volcano_kimberlite_diagram.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 4. Rhodium Plating Immersion (V04)
def gen_rhodium_plating():
    img, draw = create_base("Metallurgy of White Gold & The Rhodium Replating Lifecycle", "Precious Metals & Craftsmanship")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 3 Column layout
    cols = [
        ("STAGE 1: 18K ALLOY CORE", "Natural Warm Tone", (201, 162, 39), 120,
         ["• 75% Pure Yellow Gold", "• 25% White Alloys (Nickel/Palladium)", "• Has natural faint champagne/warm hue", "• Requires electroplating for mirror white"]),
        ("STAGE 2: RHODIUM FLASH", "0.5 – 1.0 Micron Barrier", (226, 232, 240), 680,
         ["• Precious member of Platinum family", "• Hardness: 6.0 Mohs (resists scratching)", "• Ultra-reflective, brilliant white mirror finish", "• Applied via electroplating bath at 45°C"]),
        ("STAGE 3: ABRASION LIFECYCLE", "12 – 24 Month Renewal", (245, 158, 11), 1240,
         ["• Daily friction against steering wheels/desks", "• Gradually reveals warm gold core underneath", "• Requires bench polish and replating", "• Routine maintenance, not a metal defect"])
    ]

    for title, subtitle, color, x, bullets in cols:
        draw.rectangle([x, 220, x + 540, 830], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 540, 280], fill=color)
        draw.text((x + 20, 238), title, font=f_lbl, fill=(11, 15, 23) if color != (226, 232, 240) else (11, 15, 23))
        
        draw.text((x + 30, 310), subtitle, font=f_val, fill=color)
        y = 380
        for b in bullets:
            draw.text((x + 30, y), b, font=f_sub, fill=(226, 232, 240))
            y += 50
        
        draw.rectangle([x + 30, 650, x + 510, 790], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
        if "STAGE 1" in title:
            draw.text((x + 45, 680), "CORE PURITY:", font=f_lbl, fill=(201, 162, 39))
            draw.text((x + 45, 715), "18k = 750/1000 Purity", font=f_sub, fill=(255, 255, 255))
        elif "STAGE 2" in title:
            draw.text((x + 45, 680), "PLATING THICKNESS:", font=f_lbl, fill=(226, 232, 240))
            draw.text((x + 45, 715), "0.75 Micron Industry Standard", font=f_sub, fill=(255, 255, 255))
        else:
            draw.text((x + 45, 680), "CLIENT DISCLOSURE:", font=f_lbl, fill=(245, 158, 11))
            draw.text((x + 45, 715), "Inform buyers before purchase.", font=f_sub, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "METALLURGICAL COUNSEL:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"Explain replating upfront: turning routine maintenance into a trusted showroom visit.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/rhodium_plating_immersion.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 5. Platinum Density & Patina (V04)
def gen_platinum_patina():
    img, draw = create_base("Platinum vs. Gold Mechanics: Metal Displacement vs. Metal Loss", "Precious Metals & Craftsmanship")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Gold Abrasion
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(245, 158, 11), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(245, 158, 11))
    draw.text((150, 218), "14K / 18K GOLD ABRASION: MICRO-METAL LOSS", font=f_lbl, fill=(11, 15, 23))
    
    draw.text((160, 290), "When Gold Is Scratched:", font=f_val, fill=(255, 255, 255))
    draw.text((160, 335), "• A tiny particle of gold is flaked away and permanently lost", font=f_sub, fill=(245, 158, 11))
    draw.text((160, 370), "• Over 20 years, prong tips thin and wear down significantly", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 405), "• Requires retipping or rebuilding prong heads every 7–10 years", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 440), "• Ring shank gradually loses mass and becomes thinner at base", font=f_sub, fill=(148, 163, 184))

    # Cross section drawing of gold gouge
    draw.rectangle([160, 500, 880, 680], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.line([(200, 600), (450, 600), (500, 640), (550, 600), (840, 600)], fill=(245, 158, 11), width=4)
    draw.text((460, 655), "Metal Flaked Off (Permanent Mass Loss)", font=f_sub, fill=(248, 113, 113))

    draw.text((160, 720), "DENSITY & PURITY METRIC:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 755), "• Density: 15.5 g/cm³  |  Purity: 58.5% (14k) to 75.0% (18k)", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 790), "• Solder points can brittle under sharp shock or thermal stress", font=f_sub, fill=(148, 163, 184))

    # Box 2: Platinum Displacement
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(226, 232, 240), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(226, 232, 240))
    draw.text((1030, 218), "PLATINUM DISPLACEMENT: ZERO METAL LOSS / PATINA", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 290), "When Platinum Is Scratched:", font=f_val, fill=(255, 255, 255))
    draw.text((1040, 335), "• Metal is simply pushed aside (displaced) into microscopic ridges", font=f_sub, fill=(34, 197, 94))
    draw.text((1040, 370), "• ZERO volume or mass is lost from the mounting or prongs", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 405), "• Develops a satiny, vintage sheen known as the 'Patina of Success'", font=f_sub, fill=(201, 162, 39))
    draw.text((1040, 440), "• Superior tenacity: prongs deform rather than break under impact", font=f_sub, fill=(226, 232, 240))

    # Cross section drawing of platinum furrow
    draw.rectangle([1040, 500, 1760, 680], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.line([(1080, 600), (1330, 600), (1360, 580), (1400, 620), (1440, 580), (1470, 600), (1720, 600)], fill=(226, 232, 240), width=4)
    draw.text((1300, 640), "Metal Displaced into Ridge (Mass Retained)", font=f_sub, fill=(34, 197, 94))

    draw.text((1040, 720), "DENSITY & PURITY METRIC:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 755), "• Density: 21.45 g/cm³ (60% heavier in hand)  |  Purity: 95.0% (Pt950)", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 790), "• Hypoallergenic: 100% skin-safe; zero nickel or allergenic alloys", font=f_sub, fill=(34, 197, 94))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "EXECUTIVE TAKEAWAY:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Platinum is the engineered vault. It never thins out; it holds the gem with unmatched tenacity.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/platinum_density_patina_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 6. European Shank & Sizing Beads (V05)
def gen_euro_shank():
    img, draw = create_base("Anti-Spin Shank Architecture: Euro-Shanks & Interior Sizing Beads", "Ergonomic Sizing & Fit Mechanics")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: European Square Shank
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), "SOLUTION 1: EUROPEAN SQUARE SHANK (FLAT BASE CORNERS)", font=f_lbl, fill=(11, 15, 23))

    # Blueprint drawing
    draw.rectangle([160, 290, 880, 580], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.arc([360, 320, 680, 540], start=180, end=0, fill=(201, 162, 39), width=6)
    draw.line([(360, 430), (380, 530), (660, 530), (680, 430)], fill=(201, 162, 39), width=6)
    draw.text((430, 480), "Square Base", font=f_val, fill=(255, 255, 255))

    draw.text((160, 610), "MECHANICAL PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 645), "• Flattens bottom contour to match natural finger base cross section", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 680), "• Prevents top-heavy solitaire heads from rolling sideways into web", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 715), "• Comfortable between adjacent fingers; provides ergonomic stability", font=f_sub, fill=(148, 163, 184))
    draw.text((160, 760), "Best For: Solitaires over 1.50ct or heavy three-stone settings.", font=f_lbl, fill=(34, 197, 94))

    # Box 2: Sizing Beads
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(96, 165, 250), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(96, 165, 250))
    draw.text((1030, 218), "SOLUTION 2: PLATINUM INTERIOR SIZING BEADS", font=f_lbl, fill=(11, 15, 23))

    # Blueprint drawing
    draw.rectangle([1040, 290, 1760, 580], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.ellipse([1240, 320, 1560, 540], outline=(96, 165, 250), width=6)
    draw.ellipse([1280, 470, 1315, 505], fill=(255, 255, 255), outline=(96, 165, 250), width=2)
    draw.ellipse([1485, 470, 1520, 505], fill=(255, 255, 255), outline=(96, 165, 250), width=2)
    draw.text((1340, 480), "Dual Sizing Beads", font=f_sub, fill=(255, 255, 255))

    draw.text((1040, 610), "MECHANICAL PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 645), "• Beads compress flesh at the fleshy finger base without resistance", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 680), "• Preserves full inner diameter for passing over the wide knuckle", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 715), "• Reduces effective ring size by 1/4 to 1/2 size at base only", font=f_sub, fill=(148, 163, 184))
    draw.text((1040, 760), "Best For: Clients with 1.0+ size difference between knuckle and base.", font=f_lbl, fill=(96, 165, 250))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "FIT MASTERY:", font=f_lbl, fill=(201, 162, 39))
    draw.text((360, 918), "\"Measure for the knuckle passage; deploy shank architecture to lock the base.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/euro_shank_sizing_beads_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 7. Wide Band vs Narrow (V05)
def gen_wide_vs_narrow():
    img, draw = create_base("Shank Width vs. Finger Surface Contact: The Size Adjustment Rule", "Ergonomic Sizing & Fit Mechanics")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: 2mm Whisper Band
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), "2.0 MM WHISPER BAND (MINIMAL SURFACE FRICTION)", font=f_lbl, fill=(11, 15, 23))

    draw.rectangle([160, 320, 880, 420], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.rectangle([480, 360, 560, 380], fill=(201, 162, 39)) # 2mm representation
    draw.text((320, 362), "Band Width: 2mm", font=f_lbl, fill=(255, 255, 255))

    draw.text((160, 470), "MECHANICAL BEHAVIOR:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 510), "• Displaces minimal skin tissue", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 545), "• Low friction coefficient: slips over knuckle with zero drag", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 580), "• True Sizing: Finger measurement matches ring gauge exactly", font=f_val, fill=(34, 197, 94))
    draw.text((160, 630), "• Target: Finger Size 6.0 = Order Ring Size 6.0", font=f_lbl, fill=(255, 255, 255))

    # Box 2: 7mm Wide Band
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(245, 158, 11), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(245, 158, 11))
    draw.text((1030, 218), "7.0 MM WIDE BAND (HIGH SURFACE CONTACT DRAG)", font=f_lbl, fill=(11, 15, 23))

    draw.rectangle([1040, 320, 1760, 420], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.rectangle([1320, 345, 1480, 395], fill=(245, 158, 11)) # 7mm representation
    draw.text((1180, 362), "Band Width: 7mm", font=f_lbl, fill=(255, 255, 255))

    draw.text((1040, 470), "MECHANICAL BEHAVIOR:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 510), "• Compresses large surface area of finger tissue simultaneously", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 545), "• Traps moisture and creates high suction resistance over joint", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 580), "• Required Compensation: Add +0.25 to +0.50 Size", font=f_val, fill=(245, 158, 11))
    draw.text((1040, 630), "• Target: Finger Size 6.0 = Order Ring Size 6.25 to 6.50", font=f_lbl, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "BENCH CALIBRATION RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"Wider bands trap more flesh. Always adjust size up for bands exceeding 4 millimeters.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/wide_band_vs_narrow_comparison.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 8. Ring Spin Demonstration (V05)
def gen_ring_spin():
    img, draw = create_base("The Knuckle-to-Base Differential: Diagnosing Ring Spin", "Ergonomic Sizing & Fit Mechanics")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    draw.rectangle([120, 200, 1800, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)

    # Left: Caliper illustration
    draw.rectangle([160, 250, 900, 800], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.text((200, 280), "ANATOMICAL MEASUREMENT PROFILE:", font=f_lbl, fill=(201, 162, 39))

    draw.text((200, 340), "Point A: Proximal Knuckle Joint", font=f_val, fill=(255, 255, 255))
    draw.text((200, 380), "• Width: 17.5 mm (Rigid bone & cartilage structure)", font=f_sub, fill=(226, 232, 240))
    draw.text((200, 410), "• Does NOT compress or give way during passage", font=f_sub, fill=(148, 163, 184))

    draw.text((200, 480), "Point B: Finger Resting Base", font=f_val, fill=(255, 255, 255))
    draw.text((200, 520), "• Width: 16.2 mm (Soft muscular & fleshy tissue)", font=f_sub, fill=(226, 232, 240))
    draw.text((200, 550), "• 1.3 mm gap causes standard round ring to spin under diamond weight", font=f_sub, fill=(248, 113, 113))

    draw.text((200, 620), "Resulting Buyer Complaint:", font=f_lbl, fill=(245, 158, 11))
    draw.text((200, 655), "\"My ring always turns upside down and punches into my palm.\"", font=f_note, fill=(255, 255, 255))

    # Right: Advisory Protocol
    draw.rectangle([940, 250, 1760, 800], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.text((980, 280), "CORRECTIVE SIZING PROTOCOL:", font=f_lbl, fill=(34, 197, 94))

    draw.text((980, 340), "Step 1: Never Force-Downsize the Whole Ring", font=f_val, fill=(255, 255, 255))
    draw.text((980, 380), "• If you downsize to fit the base, client cannot get it past the knuckle", font=f_sub, fill=(248, 113, 113))
    draw.text((980, 410), "• Leads to panic, swollen joints, and emergency hospital cutting", font=f_sub, fill=(148, 163, 184))

    draw.text((980, 480), "Step 2: Deploy Ergonomic Interior Stabilizers", font=f_val, fill=(255, 255, 255))
    draw.text((980, 520), "• Interior sizing bumps / speed bumps (platinum or gold)", font=f_sub, fill=(226, 232, 240))
    draw.text((980, 550), "• Horseshoe spring insert or European square contour", font=f_sub, fill=(226, 232, 240))
    draw.text((980, 580), "• Solves rotation permanently while ensuring effortless removal", font=f_sub, fill=(34, 197, 94))

    draw.text((980, 650), "The Counter Test:", font=f_lbl, fill=(201, 162, 39))
    draw.text((980, 685), "Verify 'gentle pop' over the knuckle, perfectly upright rest at base.", font=f_sub, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SALES RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((360, 918), "\"A ring that fits the knuckle but spins at the base needs engineering, not sizing down.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/ring_spin_on_finger_demonstration.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 9. GIA Dossier Macro Specs (V06)
def gen_dossier_specs():
    img, draw = create_base("GIA Dossier Specification Anatomy: The 4Cs Hierarchy", "Diamond Fluency & Value Optimization")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 4 Columns for 4Cs
    cols = [
        ("CUT (CONTROLS 80%)", "Human Craftsmanship", (34, 197, 94), 120,
         ["• Total Internal Reflection", "• Controls Brilliance & Fire", "• Masks body color & inclusions", "• NEVER compromise: Excellent only"]),
        ("CARAT (WEIGHT)", "Scale Mass, Not Size", (201, 162, 39), 540,
         ["• 1.00 Carat = 0.200 Grams", "• Check mm spread (6.5mm = 1ct)", "• Buy under 'magic numbers' (0.95ct)", "• Saves 15–25% on paper premium"]),
        ("COLOR (NATURAL)", "Faint Warmth Masking", (96, 165, 250), 960,
         ["• D-E-F: Colorless (Full Premium)", "• G-H-I: Near Colorless (Sweet Spot)", "• Top cut reflects pure white light", "• Face-up identical in ring mount"]),
        ("CLARITY (INCLUSIONS)", "The Eye-Clean Matrix", (245, 158, 11), 1380,
         ["• FL-VVS: Laboratory Spec (Overkill)", "• VS1-VS2: 100% Eye-Clean Standard", "• SI1: Exceptional Value if clean", "• Save budget for maximum Cut/Carat"])
    ]

    for title, subtitle, color, x, bullets in cols:
        draw.rectangle([x, 220, x + 380, 830], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 380, 280], fill=color)
        draw.text((x + 15, 238), title, font=f_lbl, fill=(11, 15, 23))
        
        draw.text((x + 20, 310), subtitle, font=f_val, fill=color)
        y = 380
        for b in bullets:
            draw.text((x + 20, y), b, font=f_sub, fill=(226, 232, 240))
            y += 50
        
        draw.rectangle([x + 20, 660, x + 360, 790], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
        if "CUT" in title:
            draw.text((x + 30, 685), "ADVISOR PRIORITY:", font=f_lbl, fill=(34, 197, 94))
            draw.text((x + 30, 720), "Rank #1: Non-negotiable", font=f_sub, fill=(255, 255, 255))
        elif "CARAT" in title:
            draw.text((x + 30, 685), "ADVISOR PRIORITY:", font=f_lbl, fill=(201, 162, 39))
            draw.text((x + 30, 720), "Rank #2: Match expectation", font=f_sub, fill=(255, 255, 255))
        elif "COLOR" in title:
            draw.text((x + 30, 685), "ADVISOR PRIORITY:", font=f_lbl, fill=(96, 165, 250))
            draw.text((x + 30, 720), "Rank #3: Optimize G-H", font=f_sub, fill=(255, 255, 255))
        else:
            draw.text((x + 30, 685), "ADVISOR PRIORITY:", font=f_lbl, fill=(245, 158, 11))
            draw.text((x + 30, 720), "Rank #4: Eye-clean VS2/SI1", font=f_sub, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "STRATEGIC REALLOCATION:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"Downgrade Color and Clarity to near-colorless eye-clean; upgrade Cut to Triple Ex.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/05-grading-reports-and-plots/gia_dossier_macro_specs.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 10. Rough Cleaving & Laser Sawing (V06)
def gen_rough_cleaving():
    img, draw = create_base("Rough Diamond Planning: Weight Retention vs. Optical Excellence", "Diamond Fluency & Cut Mastery")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Commercial Cut (Weight Priority)
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(248, 113, 113), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(248, 113, 113))
    draw.text((150, 218), "PATH A: WEIGHT-RETENTION CUTTING (COMMERCIAL YIELD)", font=f_lbl, fill=(11, 15, 23))

    draw.text((160, 290), "Cutter Sacrifices Light for Weight:", font=f_val, fill=(255, 255, 255))
    draw.text((160, 335), "• Cutter leaves thick girdle and deep pavilion to preserve rough mass", font=f_sub, fill=(248, 113, 113))
    draw.text((160, 370), "• Rough yield: Retains 60–65% of original crystal weight", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 405), "• Resulting Grade: GIA Good or Fair Cut", font=f_sub, fill=(248, 113, 113))
    draw.text((160, 440), "• Light escapes out the bottom; diamond looks dead and undersized", font=f_sub, fill=(148, 163, 184))

    # Box 2: Ideal Cut (Light Priority)
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "PATH B: OPTICALLY ENGINEERED EXCELLENT CUT (LIGHT PRIORITY)", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 290), "Cutter Sacrifices 50%+ Rough for Optics:", font=f_val, fill=(255, 255, 255))
    draw.text((1040, 335), "• Facets precisely ground to strict mathematical 34.5° / 40.8° tolerances", font=f_sub, fill=(34, 197, 94))
    draw.text((1040, 370), "• Rough yield: Only 40–45% of crystal preserved as polished gem", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 405), "• Resulting Grade: GIA Triple Excellent / AGS 0 Ideal", font=f_sub, fill=(34, 197, 94))
    draw.text((1040, 440), "• Total Internal Reflection: Maximum brilliance, fire, and scintillation", font=f_sub, fill=(201, 162, 39))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "CUTTER'S PARADOX:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"An Excellent cut represents a master polisher throwing away half the rough to achieve magic.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/rough_diamond_cleaving_macro.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 11. Spectral Fire Dispersion (V06)
def gen_spectral_fire():
    img, draw = create_base("Optical Physics: White Brilliance vs. Chromatic Fire Dispersion", "Diamond Fluency & Light Performance")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 3 Pillars
    pillars = [
        ("BRILLIANCE (WHITE LIGHT)", "Total Internal Reflection", (255, 255, 255), 120,
         ["• Unbroken white light return", "• Reflected directly from crown facets", "• Governed by pavilion angle (40.8°)", "• Gives diamond its clean, stark glow"]),
        ("FIRE (SPECTRAL DISPERSION)", "Prismatic Color Splitting", (245, 158, 11), 680,
         ["• Diamond Refractive Index = 2.417", "• Dispersion Rating = 0.044 (Very High)", "• Splits white sunlight into rainbow sparks", "• Red (656nm) to Violet (397nm)"]),
        ("SCINTILLATION (SPARKLE)", "Dynamic Movement & Contrast", (96, 165, 250), 1240,
         ["• Alternating flashes of light and dark", "• Created as observer or ring moves", "• Blue ASET contrast facets prevent blackout", "• The 'alive' personality of the gem"])
    ]

    for title, subtitle, color, x, bullets in pillars:
        draw.rectangle([x, 220, x + 540, 830], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 540, 280], fill=color)
        draw.text((x + 20, 238), title, font=f_lbl, fill=(11, 15, 23))
        
        draw.text((x + 30, 310), subtitle, font=f_val, fill=color)
        y = 380
        for b in bullets:
            draw.text((x + 30, y), b, font=f_sub, fill=(226, 232, 240))
            y += 50

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "PRESENTATION RULE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Take the diamond out from counter spotlights to daylight: true fire needs dynamic natural light.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/macro_fire_dispersion_colors.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 12. Inclusion Types Grid (V08)
def gen_inclusion_grid():
    img, draw = create_base("Gemological Inclusions: Harmless Fingerprints vs. Structural Risks", "Diamond Fluency & Clarity")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 24)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    quads = [
        ("PINPOINT (SAFE)", "Microscopic Mineral Crystal", (34, 197, 94), 120, 220,
         ["• Tiny dot under 10x loupe", "• Completely invisible face-up", "• Zero durability impact", "• Pure nature fingerprint"]),
        ("CLOUD (CAUTION IF DENSE)", "Cluster of Micro Pinpoints", (245, 158, 11), 980, 220,
         ["• Light haze or localized fog", "• Benign in VS1/VS2 grades", "• Avoid if report notes 'clarity based on clouds not shown'", "• May cause milkiness in SI2/I1"]),
        ("NEEDLE (SAFE)", "Thin Mineral Ingrowth Rod", (34, 197, 94), 120, 530,
         ["• Fine crystal under table or star", "• Completely transparent face-up", "• Zero structural risk", "• Excellent VS2 buying opportunity"]),
        ("FEATHER (EVALUATE LOCATION)", "Internal Cleavage / Fracture", (248, 113, 113), 980, 530,
         ["• Safe if fully contained inside crystal", "• HIGH RISK if breaking open at girdle", "• Can propagate if struck by bench hammer", "• Master move: Conceal under prong"])
    ]

    for title, subtitle, color, x, y, bullets in quads:
        draw.rectangle([x, y, x + 820, y + 260], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, y, x + 820, y + 50], fill=color)
        draw.text((x + 20, y + 14), title, font=f_lbl, fill=(11, 15, 23))
        
        draw.text((x + 30, y + 70), subtitle, font=f_val, fill=color)
        by = y + 110
        for b in bullets:
            draw.text((x + 30, by), b, font=f_sub, fill=(226, 232, 240))
            by += 32

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "EYE-CLEAN DEFINITION:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"No inclusions visible to unaided eye at 10 inches. Stop chasing paper; celebrate eye-clean beauty.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/gemological_inclusion_types_grid.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 13. Microscopic Feather Under Prong (V08)
def gen_feather_prong():
    img, draw = create_base("Strategic Setting Architecture: Concealing Inclusions Under Prongs", "Diamond Fluency & Clarity")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    draw.rectangle([120, 200, 1800, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)

    # Drawing of diamond girdle with prong
    draw.rectangle([160, 250, 900, 800], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.ellipse([300, 320, 760, 740], outline=(201, 162, 39), width=4, fill=(15, 23, 42))
    
    # 4 Prongs
    draw.rectangle([510, 300, 550, 360], fill=(226, 232, 240)) # 12 o'clock
    draw.rectangle([510, 700, 550, 760], fill=(226, 232, 240)) # 6 o'clock
    draw.rectangle([280, 510, 340, 550], fill=(226, 232, 240)) # 9 o'clock
    draw.rectangle([720, 510, 780, 550], fill=(226, 232, 240)) # 3 o'clock
    
    # Feather indicator
    draw.line([(715, 525), (735, 535)], fill=(248, 113, 113), width=3)
    draw.text((580, 560), "Feather at 3:00 Concealed", font=f_sub, fill=(34, 197, 94))

    # Right text
    draw.rectangle([940, 250, 1760, 800], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    draw.text((980, 280), "THE BENCH SETTING STRATEGY:", font=f_lbl, fill=(34, 197, 94))

    draw.text((980, 340), "Rule 1: Orient Inclusions Under Prongs", font=f_val, fill=(255, 255, 255))
    draw.text((980, 380), "• Before setting, setter plots the exact coordinates of peripheral feathers", font=f_sub, fill=(226, 232, 240))
    draw.text((980, 410), "• Rotating stone aligns inclusion directly under a platinum prong claw", font=f_sub, fill=(226, 232, 240))
    draw.text((980, 440), "• Converts a visible SI1 inclusion into a 100% eye-clean face-up presentation", font=f_sub, fill=(34, 197, 94))

    draw.text((980, 510), "Rule 2: Protect From Mechanical Shock", font=f_val, fill=(255, 255, 255))
    draw.text((980, 550), "• Prong acts as an armor shell over the feather's entry point", font=f_sub, fill=(226, 232, 240))
    draw.text((980, 580), "• Eliminates accidental direct impact against hard surfaces", font=f_sub, fill=(226, 232, 240))

    draw.text((980, 650), "Client Transparency Protocol:", font=f_lbl, fill=(201, 162, 39))
    draw.text((980, 685), "\"Show the client on the loupe: 'Notice how our setter positioned this feather safely under the prong.'\"", font=f_note, fill=(255, 255, 255))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "MASTER ADVICE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((360, 918), "\"Setting technique turns modest grading plots into breathtaking jewelry.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/microscopic_feather_prong_concealed.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 14. Fluorescence Daylight Sun Gleam (V08)
def gen_fluorescence_sun():
    img, draw = create_base("Fluorescence Optical Science: The Daylight UV Advantage", "Diamond Fluency & Fluorescence")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Indoor Incandescent
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(245, 158, 11), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(245, 158, 11))
    draw.text((150, 218), "ENVIRONMENT 1: INDOOR WARM LIGHT (NO UV)", font=f_lbl, fill=(11, 15, 23))

    draw.text((160, 290), "I-Color Diamond with Medium Blue Fluoresc.:", font=f_val, fill=(255, 255, 255))
    draw.text((160, 340), "• Incandescent lighting contains zero ultraviolet wavelengths", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 375), "• Shows natural subtle warm champagne body color", font=f_sub, fill=(245, 158, 11))
    draw.text((160, 410), "• Fluorescence is completely dormant (inactive)", font=f_sub, fill=(148, 163, 184))
    draw.text((160, 445), "• Looks like a standard warm-toned natural diamond", font=f_sub, fill=(226, 232, 240))

    # Box 2: Outdoor Sunlight
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(96, 165, 250), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(96, 165, 250))
    draw.text((1030, 218), "ENVIRONMENT 2: NATURAL OUTDOOR SUNLIGHT (RICH UV)", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 290), "Same Diamond Under 365nm Solar UV:", font=f_val, fill=(255, 255, 255))
    draw.text((1040, 340), "• Solar UV light triggers boron/nitrogen submicroscopic excitation", font=f_sub, fill=(96, 165, 250))
    draw.text((1040, 375), "• Emits crisp royal blue light from within the crystal", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 410), "• Blue is complementary to yellow: cancels yellow warmth completely", font=f_val, fill=(34, 197, 94))
    draw.text((1040, 455), "• Visually jumps 1 to 2 color grades: face-up appears as an icy G/H color!", font=f_lbl, fill=(255, 255, 255))
    draw.text((1040, 500), "• Price advantage: Purchased at 10–15% discount for I-color spec", font=f_sub, fill=(34, 197, 94))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "GIA RESEARCH FACT:", font=f_lbl, fill=(201, 162, 39))
    draw.text((400, 918), "\"Fewer than 0.2% of fluorescent diamonds show haziness. In near-colorless, it is free whitening power.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/01-gemology-and-diamonds/fluorescent_daylight_sun_gleam.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# 15. Bench Polishing & Steam Cleaning (V10)
def gen_bench_steam():
    img, draw = create_base("Showroom Value Infrastructure: Lifetime Bench Service & Accountability", "Defending Value & Showrooming")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 4 Service Pillars
    pillars = [
        ("IN-PERSON AUDIT", "Zero Guesswork", (201, 162, 39), 120,
         ["• Touch, feel, and weight in hand", "• Verified comfort-fit curvature", "• Loupe inspection with advisor", "• Zero transit or mail anxiety"]),
        ("LOCAL BENCH", "Immediate Accountability", (34, 197, 94), 540,
         ["• Master jewelers on-site", "• Ultrasonic cavitation spa", "• 100 PSI dry steam sanitation", "• Same-day ring sizing"]),
        ("LIFETIME CHECK", "Preventive Security", (96, 165, 250), 960,
         ["• Semi-annual prong tightness audit", "• Microscope structural inspection", "• Complimentary rhodium restoration", "• Insurance appraisal updates"]),
        ("HUMAN PROVENANCE", "Generational Relationship", (245, 158, 11), 1380,
         ["• We stand behind every solder joint", "• Trade-up & upgrade guarantees", "• A trusted family jeweler for life", "• Can an online cart offer this?"])
    ]

    for title, subtitle, color, x, bullets in pillars:
        draw.rectangle([x, 220, x + 380, 830], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 380, 280], fill=color)
        draw.text((x + 15, 238), title, font=f_lbl, fill=(11, 15, 23))
        
        draw.text((x + 20, 310), subtitle, font=f_val, fill=color)
        y = 380
        for b in bullets:
            draw.text((x + 20, y), b, font=f_sub, fill=(226, 232, 240))
            y += 50

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SHOWROOM DEFENSE SCRIPT:", font=f_lbl, fill=(201, 162, 39))
    draw.text((450, 918), "\"You are not just buying a loose carbon crystal. You are investing in lifetime security and service.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/04-metals-and-craftsmanship/bench_polishing_and_steam_clean.jpg"
    img.save(out_file)
    print("[OK] Generated:", out_file)

# Helper function to generate high-luxury counter and consultation narrative plates
def gen_counter_interaction_plate(out_filename, title, subtitle, step_num, advisor_script, client_mindset, key_takeaway):
    img, draw = create_base(title, "Counter Mastery & Client Engagement")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 28)
    f_sub = ImageFont.truetype(font_arial, 16)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Context & Psychology
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(201, 162, 39), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(201, 162, 39))
    draw.text((150, 218), f"STEP {step_num}: CLIENT PSYCHOLOGY & INTERACTION CONTEXT", font=f_lbl, fill=(11, 15, 23))

    draw.text((160, 300), subtitle, font=f_val, fill=(255, 255, 255))
    draw.text((160, 370), "CLIENT INTERNAL EMOTION:", font=f_lbl, fill=(245, 158, 11))
    
    # Wrap client_mindset
    y = 410
    for line in client_mindset:
        draw.text((160, y), line, font=f_sub, fill=(226, 232, 240))
        y += 35

    # Box 2: Master Advisor Delivery
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "MASTER ADVISOR PROTOCOL & VERBATIM SCRIPT", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 300), "Verbatim Counter Delivery:", font=f_val, fill=(34, 197, 94))
    
    draw.rectangle([1040, 350, 1760, 560], fill=(26, 34, 52), outline=(51, 65, 85), width=1)
    y = 370
    for line in advisor_script:
        draw.text((1060, y), line, font=f_note, fill=(255, 255, 255))
        y += 40

    draw.text((1040, 600), "BEHAVIORAL SIGNALS:", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 640), "• Maintain open posture at comfortable 45-degree showcase angle", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 675), "• Never block the doorway; grant unconditional freedom to browse", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 710), "• Focus on emotion, lifestyle, and design before price discussion", font=f_sub, fill=(34, 197, 94))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "ACADEMY DIRECTIVE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((400, 918), f'"{key_takeaway}"', font=f_note, fill=(255, 255, 255))

    img.save(out_filename)
    print("[OK] Generated:", out_filename)

if __name__ == "__main__":
    print("Generating remaining educational & consultation plates...")
    gen_gia_dossier_dual()
    gen_rough_crystal()
    gen_kimberlite_diagram()
    gen_rhodium_plating()
    gen_platinum_patina()
    gen_euro_shank()
    gen_wide_vs_narrow()
    gen_ring_spin()
    gen_dossier_specs()
    gen_rough_cleaving()
    gen_spectral_fire()
    gen_inclusion_grid()
    gen_feather_prong()
    gen_fluorescence_sun()
    gen_bench_steam()

    # Counter Consultation Plates
    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/customer_hesitant_entry.jpg",
        "The Guarded Entry: Overcoming Initial Sales Defense",
        "Lowering the 90-Second Client Shield",
        "01",
        ["\"Welcome to Jewelswell! Take your time and enjoy",
         "the collection. My name is Alex—please explore freely,",
         "and let me know if you would like to try anything on.\""],
        ["• Client anticipates high-pressure sales interrogation",
         "• Fear of being judged on budget or appearance",
         "• Prepared to utter defensive reflex: 'We're just looking'"],
        "Acknowledge and release. Do not pounce; create emotional safety."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/warm_concierge_greeting.jpg",
        "The Hospitality Frame: Concierge Welcome vs Interrogation",
        "Replacing 'Can I Help You?' with Luxury Hospitality",
        "02",
        ["\"Good afternoon! Welcome to the salon. Feel free to",
         "stroll through our diamond gallery. Can I offer you",
         "sparkling water or an espresso while you take a look?\""],
        ["• Client feels honored as a guest rather than a target",
         "• Hospitality resets heart rate and dissolves shopping tension",
         "• Transforms transactional sales pitch into concierge hospitality"],
        "Treat every visitor like a VIP guest entering a private salon."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/browsing_cases_couple.jpg",
        "Silent Observation: Tracking Visual Fascination Patterns",
        "Reading Client Body Language Before Re-Approaching",
        "03",
        ["(Observe in silence: Note where their eyes linger)",
         "• Notice which showcase holds their attention for >15 seconds",
         "• Observe whether client leans in or points out shapes to partner"],
        ["• Couple points to elongated oval and vintage milgrain setting",
         "• They are actively imagining wearability and aesthetics",
         "• Uninterrupted time allows genuine preference to emerge"],
        "Observe where their eyes linger before speaking. Let their taste guide your entry."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/advisor_warm_reapproach.jpg",
        "The Taste-Based Reapproach: Validating Client Aesthetic",
        "Re-entering the Conversation with Validation",
        "04",
        ["\"That elongated emerald cut has such timeless, crisp lines.",
         "Is that a geometric silhouette you have always admired,",
         "or are you exploring different shapes today?\""],
        ["• Client feels validated and flattered regarding their aesthetic taste",
         "• Question cannot be answered with 'just looking'",
         "• Opens effortless narrative regarding personal style"],
        "Compliment their taste, not the price tag. Open the relationship."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/intimate_consultation_tray.jpg",
        "The Velvet Presentation: Transitioning to Private Seating",
        "Moving from Counter Showcase to Private Viewing Pad",
        "05",
        ["\"Let us take this out into natural light on our velvet tray.",
         "Fine jewelry cannot be judged behind showcase glass—",
         "you need to see how it moves and catches the light.\""],
        ["• Overcomes glass barrier separating buyer from precious item",
         "• Tactile intimacy increases psychological ownership by 40%",
         "• Comfortable seated posture eliminates buyer fatigue"],
        "Get the jewelry out of the case. Intimacy with the piece creates the sale."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/customer_holding_smartphone_counter.jpg",
        "The Smartphone Defense: Responding to Online Listings",
        "Overcoming 'I Saw It Online For Less'",
        "06",
        ["\"It makes complete sense that you checked online. With an",
         "investment this important, you deserve complete transparency",
         "and 100% confidence. Let us look at the full specs together.\""],
        ["• Client expects immediate defensive hostility or panicked discounting",
         "• Holding phone is a test of your professional composure",
         "• Respectful validation instantly differentiates you from amateurs"],
        "Never attack the online listing. Validate their research and audit the facts."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/calm_advisor_listening.jpg",
        "Active Consultative Listening: Composure Under Pressure",
        "Maintaining Total Executive Poise",
        "07",
        ["\"Tell me more about what you liked about that stone.",
         "Was it the carat weight, or did the clarity catch your eye?",
         "Let us pull up the full proportions diagram together.\""],
        ["• Advisor displays relaxed, composed eye contact and steady tone",
         "• No defensive posturing, no flustered stammering",
         "• Signals unshakeable authority and expertise in fine gemology"],
        "Calm authority wins trust. Amateurs panic; master advisors educate."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/proposal_celebration_couple.jpg",
        "Celebrating the Moment: The Emotional Purchase Close",
        "Connecting Fine Jewelry to Lifelong Memory",
        "08",
        ["\"Congratulations to both of you! This ring will be part",
         "of your family story for generations. We are honored to",
         "take care of this piece for the rest of your lives.\""],
        ["• Client remembers the warmth, joy, and peace of mind of the purchase",
         "• Purchase is sealed with genuine shared celebration",
         "• Creates lifelong client loyalty and organic word-of-mouth referrals"],
        "Fine jewelry is not a commodity—it is the physical anchor of life's greatest moments."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/client_smiling_handshake_counter.jpg",
        "The 3-Point Security Handshake: Proven Authenticity",
        "Sealing Trust with GIA Verification",
        "09",
        ["\"We have verified the laser inscription together, confirmed",
         "the dossier plot, and checked the official GIA online registry.",
         "You have complete, unshakeable proof of what you own.\""],
        ["• Zero post-purchase remorse or second-guessing",
         "• Client leaves showroom completely confident and empowered",
         "• Ready to enthusiastically recommend the store to friends"],
        "Transparency turns shoppers into lifelong brand ambassadors."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/luxury_consultation_couple.jpg",
        "The Objective Origin Consultation: Natural vs. Lab-Grown",
        "Educating on Rarity vs Technological Supply",
        "10",
        ["\"Both are 100% genuine diamond. Our role is simply to",
         "educate you on the difference between geological rarity",
         "and manufactured supply, so you can make the right choice.\""],
        ["• Client feels fully respected regardless of budget or origin preference",
         "• Zero shaming or condescending comments",
         "• Client gains clear economic and emotional understanding"],
        "Empower the client's choice with science and macroeconomic clarity."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/heirloom_vintage_handover.jpg",
        "Generational Provenance: The Natural Diamond Legacy",
        "The Emotional Value of Heirloom Provenance",
        "11",
        ["\"When you look at this natural diamond, you are holding",
         "a crystal that formed deep within the Earth over a billion",
         "years ago. It is an enduring heirloom for generations.\""],
        ["• Buyer connects with timeless permanence and geological antiquity",
         "• Emotion transcends commodity price comparisons",
         "• Justifies premium through generational pride and permanence"],
        "Heirloom value cannot be manufactured in a plasma reactor."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/daylight_counter_comparison.jpg",
        "The Daylight Side-by-Side Test: Proving Cut Beauty",
        "Moving Beyond Showroom Spotlights",
        "12",
        ["\"Let us step over toward the window into natural daylight.",
         "Notice how this Excellent cut stone sparkles with intense",
         "fire, completely masking its near-colorless G grade.\""],
        ["• Buyer sees undeniable visual proof with their own eyes",
         "• Demonstrates why spending on Cut outperforms spending on Color/Clarity",
         "• Creates immediate aha moment and eliminates buyer hesitation"],
        "Let the diamond's live performance in daylight close the sale."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/ring_slide_on_finger_client.jpg",
        "The Gentle Knuckle Pop: Delivering Flawless Fit",
        "Verifying Passage Resistance and Resting Comfort",
        "13",
        ["\"Notice that gentle, reassuring resistance as it glides",
         "past the knuckle, and then how smoothly it settles comfortably",
         "without spinning or pinching at the base. That is precision fit.\""],
        ["• Immediate tactile comfort and reassurance of security",
         "• Eliminates fear of the ring falling off or feeling tight",
         "• Confirms elite bespoke craftsmanship and tailored fitting"],
        "Precision in fit is felt in the hands, not read on a sizing gauge."
    )

    gen_counter_interaction_plate(
        "media-bank/06-counter-sales-and-consultation/eye_clean_face_up_beauty.jpg",
        "The Eye-Clean Standard: Face-Up Optical Radiance",
        "Demystifying Clarity Inclusions at the Counter",
        "14",
        ["\"Notice that at normal conversational distance, this SI1 diamond",
         "is completely eye-clean—its intense scintillation outshines",
         "any microscopic internal pinpoint. That is smart value.\""],
        ["• Buyer realizes they don't need to pay thousands extra for VVS specs",
         "• Focus shifts to brilliant face-up sparkle and millimeter spread",
         "• Buyer feels intelligent and empowered by the advisor's guidance"],
        "Celebrate what the human eye sees. Eye-clean is the connoisseur's choice."
    )

    print("All educational and consultation plates generated successfully!")
