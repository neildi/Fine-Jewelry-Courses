from PIL import Image, ImageDraw, ImageFont
import os

font_geo = 'media-bank/georgia.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'
if not os.path.exists(font_arial):
    font_arial = font_geo

out_dir = 'media-bank/07-infographics-and-cards'
os.makedirs(out_dir, exist_ok=True)

BADGES = [
    {
        "filename": "badge_shape_cut_outro.png",
        "title": "C6-M02 : DIAMOND SHAPE VS. CUT",
        "rule": "Shape is personal preference; Cut is pure physics. Never trade optical light return for dead weight.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_lab_standards_outro.png",
        "title": "C6-M03 : GIA VS. AGS STANDARDS",
        "rule": "A grading report establishes baseline specs; optical modeling and the loupe prove true beauty.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_diamond_origin_outro.png",
        "title": "C6-M04 : NATURAL VS. LAB-GROWN ADVISORY",
        "rule": "Never shame the client's inquiry. Present transparent gemological science and economic truth.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_metals_craft_outro.png",
        "title": "C6-M05 : METALS & MOUNTING LONGEVITY",
        "rule": "The mounting is the security vault for the gem. Engineer the setting for a lifetime of daily wear.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_ring_sizing_outro.png",
        "title": "C6-M06 : RING SIZING & FIT ARCHITECTURE",
        "rule": "Measure the knuckle for passage; engineer the shank for stability to eliminate spinning forever.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_4cs_hierarchy_outro.png",
        "title": "C1-M01 : THE 4CS VALUE HIERARCHY",
        "rule": "Cut is the only C controlled by human hands. It controls 80% of face-up perceived beauty.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_loupe_mastery_outro.png",
        "title": "C1-M02 : LOUPE MASTERY & 3-POINT VERIFY",
        "rule": "Transparency builds luxury loyalty. Turn the 10x loupe inspection into an unforgettable ritual.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_fluorescence_outro.png",
        "title": "C1-M05 : FLUORESCENCE & INCLUSIONS",
        "rule": "Fluorescence in near-colorless diamonds is an optical asset. Demystify with science, not discounts.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_first_90s_outro.png",
        "title": "C2-M01 : THE CRITICAL FIRST 90 SECONDS",
        "rule": "Never try to close the sale in the first 90 seconds. Focus 100% on opening the relationship.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    },
    {
        "filename": "badge_defending_value_outro.png",
        "title": "C2-M05 : DEFENDING VALUE & OVERCOMING SHOWROOMING",
        "rule": "Never apologize for your price. Guide the client through a transparent, like-for-like value audit.",
        "tag": "JEWELSWELL ACADEMY  •  EXECUTIVE CAPSTONE RULE"
    }
]

for b in BADGES:
    img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Lower-third box centered or elegant left
    x0, y0 = 120, 840
    x1, y1 = 1800, 990

    # Rounded translucent dark slate box
    draw.rectangle([x0, y0, x1, y1], fill=(11, 15, 23, 235))
    # Gold left accent bar
    draw.rectangle([x0, y0, x0 + 8, y1], fill=(201, 162, 39, 255))
    # Gold top hairline
    draw.rectangle([x0, y0, x1, y0 + 1], fill=(51, 65, 85, 200))

    f_tag = ImageFont.truetype(font_arial, 15)
    f_title = ImageFont.truetype(font_geo, 26)
    f_rule = ImageFont.truetype(font_geo, 22)

    draw.text((x0 + 35, y0 + 20), b["tag"], font=f_tag, fill=(201, 162, 39))
    draw.text((x0 + 35, y0 + 48), b["title"], font=f_title, fill=(255, 255, 255))
    draw.text((x0 + 35, y0 + 95), f'"{b["rule"]}"', font=f_rule, fill=(223, 190, 84))

    out_file = os.path.join(out_dir, b["filename"])
    img.save(out_file)
    print(f"[OK] Generated Outro Badge: {out_file}")

print("All 10 Outro Badges generated successfully.")
