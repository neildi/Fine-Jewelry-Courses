from PIL import Image, ImageDraw, ImageFont
import os

font_geo = 'media-bank/georgia.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'
if not os.path.exists(font_arial):
    font_arial = font_geo

W, H = 1920, 1080

def create_base(title, category_tag):
    img = Image.new('RGB', (W, H), (11, 15, 23)) # Deep Onyx
    draw = ImageDraw.Draw(img)
    draw.rectangle([40, 40, W-40, H-40], outline=(40, 48, 64), width=1)
    draw.rectangle([44, 44, W-44, H-44], outline=(201, 162, 39), width=1)
    
    f_tag = ImageFont.truetype(font_arial, 15)
    f_h1 = ImageFont.truetype(font_geo, 34)
    draw.text((80, 70), 'JEWELSWELL ACADEMY  •  ' + category_tag.upper(), font=f_tag, fill=(201, 162, 39))
    draw.text((80, 98), title, font=f_h1, fill=(255, 255, 255))
    return img, draw

# 1. GIA iD100 Testing Device Diagnostic Plate
def gen_id100_plate():
    img, draw = create_base("Laboratory Screening: GIA iD100™ Luminescence Spectroscopy", "Lab-Grown & Synthetic Screening")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: Instrument Specs
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(96, 165, 250), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(96, 165, 250))
    draw.text((150, 218), "INSTRUMENT ARCHITECTURE: GIA iD100™", font=f_lbl, fill=(11, 15, 23))

    # Device Screen Box
    draw.rectangle([160, 300, 880, 520], fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    draw.text((190, 330), "OPTICAL LUMINESCENCE SENSOR", font=f_sub, fill=(148, 163, 184))
    
    # Digital Display
    draw.rectangle([220, 370, 820, 480], fill=(5, 46, 22), outline=(34, 197, 94), width=3)
    draw.text((260, 405), "GIA iD100: PASS (NATURAL)", font=f_val, fill=(74, 222, 128))
    draw.text((260, 445), "Detection Speed: < 2.0 Seconds", font=f_sub, fill=(134, 239, 172))

    draw.text((160, 560), "SCREENING PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 595), "• Standard thermal pens FAIL: Both natural and lab diamonds conduct heat identically", font=f_sub, fill=(248, 113, 113))
    draw.text((160, 630), "• Uses UV laser luminescence spectroscopy to detect nitrogen-vacancy centers", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 665), "• Accurately screens mounted or loose diamonds down to 0.005 carats", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 700), "• 100% referral accuracy for CVD & HPHT synthetic lab-grown diamonds", font=f_lbl, fill=(96, 165, 250))

    # Box 2: Counter Protocol
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "SHOWROOM SCREENING PROTOCOL", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 300), "The Transparent Intake Demonstration:", font=f_val, fill=(255, 255, 255))
    draw.text((1040, 350), "Step 1: Test In Full View of the Client", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 385), "• Never take a trade-in or repair ring 'into the back' to test", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 420), "• Place probe on table facet directly on the consultation pad", font=f_sub, fill=(226, 232, 240))

    draw.text((1040, 480), "Step 2: Read Live Result Aloud Together", font=f_lbl, fill=(34, 197, 94))
    draw.text((1040, 515), "• 'Pass' confirms geological natural origin instantly", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 550), "• 'Refer' indicates laboratory synthesis requiring full spectroscopy", font=f_sub, fill=(226, 232, 240))

    draw.text((1040, 620), "Step 3: Document on Intake Receipt", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 655), "• Records instrument serial number and timestamp", font=f_sub, fill=(226, 232, 240))
    draw.text((1040, 690), "• Protects store against post-service origin disputes", font=f_sub, fill=(148, 163, 184))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "SECURITY PROTOCOL:", font=f_lbl, fill=(201, 162, 39))
    draw.text((420, 918), "\"Science, not guesswork. Advanced optical screening guarantees 100% chain-of-custody integrity.\"", font=f_note, fill=(255, 255, 255))

    out_file = "media-bank/03-lab-grown-and-crystals/gia_id100_testing_device_clip.mp4" # We will render as MP4 clip!
    out_jpg = "media-bank/03-lab-grown-and-crystals/gia_id100_diagnostic_plate.jpg"
    img.save(out_jpg)
    print("[OK] Generated:", out_jpg)

# 2. UV Fluorescence Comparison Dark Chamber Plate
def gen_uv_chamber_plate():
    img, draw = create_base("Long-Wave UV Fluorescence Diagnostics: 365nm Emission Analysis", "Diamond Fluency & Fluorescence")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 24)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # 4 Stones in Dark Chamber
    stones = [
        ("NONE (INERT)", "Zero UV Reaction", (71, 85, 105), 120, "• 65–70% of natural diamonds", "• No emission under 365nm UV", "• Baseline standard"),
        ("FAINT BLUE", "Subtle Glow", (96, 165, 250), 540, "• Very slight pastel blue tint", "• Undetectable in daylight", "• Zero haziness risk"),
        ("MEDIUM BLUE", "Crisp Royal Glow", (59, 130, 246), 960, "• Definite blue glow in UV box", "• Helps whiten I-J body colors", "• Exceptional value sweet spot"),
        ("STRONG / VERY STRONG", "Electric Cobalt Blue", (37, 99, 235), 1380, "• Intense neon blue emission", "• Under 0.2% show oiliness", "• Inspect for transparency")
    ]

    for title, subtitle, color, x, b1, b2, b3 in stones:
        draw.rectangle([x, 220, x + 380, 830], fill=(18, 24, 36), outline=color, width=2)
        draw.rectangle([x, 220, x + 380, 280], fill=color)
        draw.text((x + 15, 238), title, font=f_lbl, fill=(255, 255, 255) if color != (71, 85, 105) else (226, 232, 240))
        
        # Circle representing diamond under UV
        draw.ellipse([x + 110, 320, x + 270, 480], fill=(10, 15, 25), outline=color, width=4)
        if "STRONG" in title:
            draw.ellipse([x + 130, 340, x + 250, 460], fill=(37, 99, 235))
        elif "MEDIUM" in title:
            draw.ellipse([x + 140, 350, x + 240, 450], fill=(59, 130, 246))
        elif "FAINT" in title:
            draw.ellipse([x + 150, 360, x + 230, 440], fill=(96, 165, 250))
        
        draw.text((x + 30, 520), subtitle, font=f_val, fill=color)
        draw.text((x + 30, 580), b1, font=f_sub, fill=(226, 232, 240))
        draw.text((x + 30, 620), b2, font=f_sub, fill=(226, 232, 240))
        draw.text((x + 30, 660), b3, font=f_sub, fill=(148, 163, 184))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "ACADEMY DIRECTIVE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((400, 918), "\"Blue fluorescence in near-colorless diamonds is nature's built-in whitening filter.\"", font=f_note, fill=(255, 255, 255))

    out_jpg = "media-bank/01-gemology-and-diamonds/diamond_fluorescence_uv_comparison_plate.jpg"
    img.save(out_jpg)
    print("[OK] Generated:", out_jpg)

# 3. Luxury Counter Greeting Dynamic Protocol Plate
def gen_greeting_protocol_plate():
    img, draw = create_base("The 90-Second Frictionless Greeting: Luxury Hospitality vs Pressure", "Counter Consultation Mastery")
    f_lbl = ImageFont.truetype(font_arial, 18)
    f_val = ImageFont.truetype(font_geo, 26)
    f_sub = ImageFont.truetype(font_arial, 15)
    f_note = ImageFont.truetype(font_geo, 22)

    # Box 1: The Discounter Pounce Trap
    draw.rectangle([120, 200, 920, 850], fill=(18, 24, 36), outline=(248, 113, 113), width=2)
    draw.rectangle([120, 200, 920, 260], fill=(248, 113, 113))
    draw.text((150, 218), "THE AMATEUR TRAP: INTERROGATION POUNCE", font=f_lbl, fill=(11, 15, 23))

    draw.text((160, 300), "Fatal Opening Questions:", font=f_val, fill=(248, 113, 113))
    draw.text((160, 350), "• \"Can I help you with something today?\"", font=f_lbl, fill=(226, 232, 240))
    draw.text((160, 385), "• \"What price range or budget were you looking at?\"", font=f_lbl, fill=(226, 232, 240))
    draw.text((160, 420), "• \"Are you buying today or just browsing?\"", font=f_lbl, fill=(226, 232, 240))

    draw.text((160, 490), "PSYCHOLOGICAL CONSEQUENCE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((160, 530), "• Client instantly feels cornered and pressured", font=f_sub, fill=(226, 232, 240))
    draw.text((160, 565), "• Triggers automatic defensive barrier: 'We're just looking'", font=f_sub, fill=(248, 113, 113))
    draw.text((160, 600), "• Client retreats toward exit within 60 seconds", font=f_sub, fill=(148, 163, 184))

    # Box 2: Jewelswell Hospitality Protocol
    draw.rectangle([1000, 200, 1800, 850], fill=(18, 24, 36), outline=(34, 197, 94), width=2)
    draw.rectangle([1000, 200, 1800, 260], fill=(34, 197, 94))
    draw.text((1030, 218), "JEWELSWELL ACADEMY: HOSPITALITY RECEPTION", font=f_lbl, fill=(11, 15, 23))

    draw.text((1040, 300), "The 3-Beat Welcome Protocol:", font=f_val, fill=(34, 197, 94))
    draw.text((1040, 350), "Beat 1: Warm Human Welcome (No Sales Angle)", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 385), "\"Welcome in! Happy Saturday. How is your afternoon going?\"", font=f_note, fill=(255, 255, 255))

    draw.text((1040, 450), "Beat 2: Name Introduction & Permission to Stroll", font=f_lbl, fill=(34, 197, 94))
    draw.text((1040, 485), "\"My name is Alex. Please take your time and explore our cases freely.\"", font=f_note, fill=(255, 255, 255))

    draw.text((1040, 550), "Beat 3: Hospitality Offering & Release", font=f_lbl, fill=(201, 162, 39))
    draw.text((1040, 585), "\"Can I offer you an espresso or sparkling water while you look?\"", font=f_note, fill=(255, 255, 255))

    draw.text((1040, 650), "Beat 4: Step Back 3 Paces", font=f_lbl, fill=(226, 232, 240))
    draw.text((1040, 685), "Give them breathing room. Observe which cases hold their attention.", font=f_sub, fill=(148, 163, 184))

    # Bottom
    draw.rectangle([120, 890, 1800, 980], fill=(20, 26, 38), outline=(51, 65, 85), width=1)
    draw.text((160, 922), "CORE PRINCIPLE:", font=f_lbl, fill=(201, 162, 39))
    draw.text((380, 918), "\"Never close the sale in the first ninety seconds; open the relationship.\"", font=f_note, fill=(255, 255, 255))

    out_jpg = "media-bank/06-counter-sales-and-consultation/luxury_counter_first_greeting_plate.jpg"
    img.save(out_jpg)
    print("[OK] Generated:", out_jpg)

if __name__ == "__main__":
    gen_id100_plate()
    gen_uv_chamber_plate()
    gen_greeting_protocol_plate()
