from PIL import Image, ImageDraw, ImageFont
import os

font_geo = 'media-bank/georgia.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'
if not os.path.exists(font_arial):
    font_arial = font_geo

out_dir = 'media-bank/07-infographics-and-cards'
os.makedirs(out_dir, exist_ok=True)

W, H = 1920, 1080

CARDS_DATA = [
    {
        "id": "card_01_shape_vs_cut",
        "title": "Diamond Shape vs. Cut: The Optical Anatomy Framework",
        "subtitle": "C6-M02 MASTERCLASS: BEYOND THE FACE-UP OUTLINE",
        "prompt_label": "BUYER INQUIRY:",
        "prompt_text": "\"What cut is this oval ring, and why is this other one so much more brilliant?\"",
        "left_title": "AMATEUR TRAP (OUTLINE CONFUSION)",
        "left_quote": [
            "\"Oval is the cut! All ovals sparkle about the same,",
            "this one just costs more because of the carat weight",
            "and brand name.\""
        ],
        "left_bullets": [
            "• Conflates outer outline (shape) with facet geometry (cut quality).",
            "• Misses dangerous central bow-tie obstruction and optical leakage.",
            "• Sacrifices cut precision to push clients into bulky, dull carats.",
            "• Result: Client notices dead spots at home; buyer remorse sets in."
        ],
        "right_title": "MASTER ADVISOR (OPTICAL ANATOMY)",
        "right_quote": [
            "\"Oval is the shape, but cut is the craftsmanship. Notice",
            "how this stone directs light back to your eye with zero dark",
            "bow-tie band across its belly.\""
        ],
        "right_bullets": [
            "• Distinguishes shape (personal design) from cut (human craftsmanship).",
            "• Teaches the 3 light pillars: Brilliance, Fire, and Scintillation.",
            "• Evaluates proportions: Table 54-58%, depth 59-62.5%, crown angles.",
            "• Result: High client confidence, cut appreciation, premium margin."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Shape is personal preference; Cut is pure physics. Never trade optical light return for dead weight.\""
    },
    {
        "id": "card_02_gia_vs_ags",
        "title": "Lab Standards & Light Performance: GIA vs. AGS Decoded",
        "subtitle": "C6-M03 MASTERCLASS: DEMYSTIFYING REPORTS AT THE COUNTER",
        "prompt_label": "CLIENT QUESTION:",
        "prompt_text": "\"Both of these diamonds say 'Triple Excellent'—why does one look significantly brighter?\"",
        "left_title": "AMATEUR TRAP (PAPER-SELLING)",
        "left_quote": [
            "\"Triple Excellent is Triple Excellent—they're the exact",
            "same on paper, so just take whichever one is cheaper",
            "or larger.\""
        ],
        "left_bullets": [
            "• Treats GIA 'Excellent' as a single point instead of a broad range.",
            "• Ignores edge-to-edge optical leakage and subtle light leakage.",
            "• Incapable of explaining ASET scope maps or contrast patterning.",
            "• Result: Sells paper specifications rather than visual beauty."
        ],
        "right_title": "MASTER ADVISOR (OPTICAL PERFORMANCE)",
        "right_quote": [
            "\"GIA Excellent is an elite baseline, but AGS Ideal modeling",
            "measures exact ray-tracing. Notice how this stone delivers",
            "intense red light-return across all 8 arrows.\""
        ],
        "right_bullets": [
            "• Explains ASET colors: Red (direct light), Green (ambient), Blue (contrast).",
            "• Shows how crown and pavilion angle harmony prevents optical leakage.",
            "• Uses the loupe and counter lighting to prove real-world scintillation.",
            "• Result: Client sees tangible value; trusts expert counter advisory."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"A grading report establishes authenticity; your optical demonstration proves extraordinary beauty.\""
    },
    {
        "id": "card_03_natural_vs_lab",
        "title": "Diamond Origin & Advisory: Natural vs. Lab-Grown Integrity",
        "subtitle": "C6-M04 MASTERCLASS: UNBIASED CONSULTATION & VALUE INTEGRITY",
        "prompt_label": "CLIENT DILEMMA:",
        "prompt_text": "\"Should we get a lab-grown diamond to get twice the size, or stick with natural?\"",
        "left_title": "AMATEUR TRAP (BIASED DISMISSAL)",
        "left_quote": [
            "\"Lab diamonds are fake, worthless glass with zero resale value.",
            "Only a natural diamond counts as real love!\""
        ],
        "left_bullets": [
            "• Triggers immediate client defense and breaks consultative trust.",
            "• Makes scientifically false claims (lab diamonds are real carbon crystal).",
            "• Fails to address the client's genuine budget and size desires.",
            "• Result: Client leaves the store and buys from an online discounter."
        ],
        "right_title": "MASTER ADVISOR (TRANSPARENT VALUE)",
        "right_quote": [
            "\"Both are optically and chemically 100% diamond. The question",
            "is whether you value geological rarity and legacy provenance, or",
            "maximizing modern technological scale for your budget.\""
        ],
        "right_bullets": [
            "• Affirms optical equivalence (refractive index 2.42, hardness 10 Mohs).",
            "• Explains macro-economics: Finite geological asset vs scalable supply.",
            "• Empowers the buyer with objective GIA / iD100 testing facts.",
            "• Result: Deep client appreciation, uncompromised integrity, confident close."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Never shame the client's inquiry. Present transparent gemological science and economic truth.\""
    },
    {
        "id": "card_04_metals_and_craftsmanship",
        "title": "Precious Metals & Mounting Longevity: Platinum vs. Gold",
        "subtitle": "C6-M05 MASTERCLASS: SHANK METALLURGY & PRONG SECURITY",
        "prompt_label": "CLIENT QUESTION:",
        "prompt_text": "\"Why is platinum heavier and more expensive than 14K white gold if they look identical?\"",
        "left_title": "AMATEUR TRAP (SURFACE PITCH)",
        "left_quote": [
            "\"Platinum is just the luxury metal celebrities use! They look",
            "the same, but 14K white gold is cheaper so you can spend",
            "more on the center diamond.\""
        ],
        "left_bullets": [
            "• Omits rhodium plating wear and periodic replating costs.",
            "• Fails to explain metal displacement vs brittle metal loss in gold.",
            "• Recommends light, flimsy prongs that risk losing the center stone.",
            "• Result: Center stone falls out in 2 years; store blame and angry client."
        ],
        "right_title": "MASTER ADVISOR (METALLURGICAL MASTERY)",
        "right_quote": [
            "\"White gold wears away metal microscopic layer by layer. Platinum",
            "displaces—it develops a rich patina and holds prongs securely",
            "for generations without thinning out.\""
        ],
        "right_bullets": [
            "• Explains 95% purity and hypoallergenic density of platinum.",
            "• Highlights prong tenacity: Platinum bends under shock; gold can shear.",
            "• Matches metal to lifestyle (active lifestyles benefit from platinum or bezel).",
            "• Result: Long-term heirloom durability, higher ticket value, zero ring damage."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"The mounting is the security vault for the gem. Engineer the setting for a lifetime of daily wear.\""
    },
    {
        "id": "card_05_ring_sizing_architecture",
        "title": "Ring Sizing & Fit Architecture: Knuckle vs. Base Mechanics",
        "subtitle": "C6-M06 MASTERCLASS: ELIMINATING SPINNING & RESIZING FRICTION",
        "prompt_label": "CLIENT ISSUE:",
        "prompt_text": "\"The ring spins constantly on her finger, but if we go smaller it won't pass the knuckle!\"",
        "left_title": "AMATEUR TRAP (FORCED COMPRESSION)",
        "left_quote": [
            "\"Just size it down half a size and push it hard over the joint.",
            "It will stretch over time, or she can just tape the bottom.\""
        ],
        "left_bullets": [
            "• Causes knuckle pain, swelling, and emergency ring removal.",
            "• Fails to diagnose high center-of-gravity top-heavy solitaire physics.",
            "• Ignores comfort-fit inner convex curvature vs standard flat mandrels.",
            "• Result: Client resents wearing the ring; post-sale service headache."
        ],
        "right_title": "MASTER ADVISOR (FIT ARCHITECTURE)",
        "right_quote": [
            "\"When the knuckle is larger than the finger base, sizing down causes",
            "friction. We stabilize the spin using an Euro shank, sizing beads,",
            "or a curved comfort-fit interior.\""
        ],
        "right_bullets": [
            "• Evaluates knuckle pass resistance vs 360-degree base rotation.",
            "• Deploys mechanical solutions: European square shanks or platinum beads.",
            "• Calibrates mandrel readings: Center touch point for comfort-fit bands.",
            "• Result: Effortless glide, zero spin, perfect daily comfort from day one."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Comfort is engineered, not guessed. Measure the knuckle for passage; engineer the shank for stability.\""
    },
    {
        "id": "card_06_4cs_value_hierarchy",
        "title": "The 4Cs Value Hierarchy: Strategic Cut Optimization",
        "subtitle": "C1-M01 MASTERCLASS: BEYOND THE LABORATORY DOSSIER",
        "prompt_label": "BUDGET TRADE-OFF:",
        "prompt_text": "\"Our budget is $10,000. Should we prioritize a D-Color VS1 or a larger carat size?\"",
        "left_title": "AMATEUR TRAP (PAPER PURSUIT)",
        "left_quote": [
            "\"Always get D Color and VVS Clarity! Anything else is imperfect,",
            "even if it means dropping down to a tiny 0.70-carat stone",
            "with an average cut.\""
        ],
        "left_bullets": [
            "• Wastes client capital on invisible laboratory grades at 10x magnification.",
            "• Sacrifices cut quality, resulting in dark, lifeless light performance.",
            "• Ignores that face-up color difference between D and F is imperceptible set.",
            "• Result: Client compares with friends; feels they paid too much for too little."
        ],
        "right_title": "MASTER ADVISOR (THE SWEET SPOT)",
        "right_quote": [
            "\"Cut is the engine of sparkle. By choosing an Excellent cut with G-H",
            "color and an eye-clean VS2, you maximize brilliant face-up diameter",
            "and save thousands without losing beauty.\""
        ],
        "right_bullets": [
            "• Cut optimization masks faint body color through intense white light return.",
            "• Maximizes millimeter spread (6.5mm on a 1ct round vs 6.0mm on deep cut).",
            "• Positions budget where it creates maximum visual impact on the hand.",
            "• Result: Exceeded expectations, stunning visual impact, lifelong customer."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Cut is the only 'C' controlled by human hands. It controls 80% of perceived beauty.\""
    },
    {
        "id": "card_07_loupe_mastery_protocol",
        "title": "Loupe Mastery Protocol: The 3-Point Security Match",
        "subtitle": "C1-M02 MASTERCLASS: COUNTER VERIFICATION & CLIENT CONFIDENCE",
        "prompt_label": "VERIFICATION DRILL:",
        "prompt_text": "\"How do we prove to the client that the diamond in the ring is the exact one on the GIA report?\"",
        "left_title": "AMATEUR TRAP (HAND-WAVING)",
        "left_quote": [
            "\"Trust us, we're a reputable family store. Here is the paperwork,",
            "it matches the invoice in our computer system.\""
        ],
        "left_bullets": [
            "• Relies on verbal reassurance instead of gemological proof.",
            "• Misses the opportunity to educate and delight the client with the loupe.",
            "• Leaves lingering anxiety about stone swapping or mismatch.",
            "• Result: Fragile trust; susceptible to third-party second guessing."
        ],
        "right_title": "MASTER ADVISOR (THE 3-POINT AUDIT)",
        "right_quote": [
            "\"Let's inspect the girdle together under 10x magnification. See this",
            "microscopic laser inscription? Let's verify every digit directly against",
            "the GIA cloud database right now.\""
        ],
        "right_bullets": [
            "• Point 1: 10x Triplet Loupe verification of microscopic girdle laser inscription.",
            "• Point 2: Dossier plot diagram alignment (internal pinpoint/feather matching).",
            "• Point 3: Live GIA Report Check lookup on official portal in front of client.",
            "• Result: Bulletproof transparency, thrilling customer experience, absolute trust."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Transparency builds luxury loyalty. Turn the loupe inspection into an unforgettable ritual.\""
    },
    {
        "id": "card_08_fluorescence_and_inclusions",
        "title": "Fluorescence & Inclusions: The Eye-Clean Screening Matrix",
        "subtitle": "C1-M05 MASTERCLASS: SCIENTIFIC REALITY VS. POPULAR MYTHS",
        "prompt_label": "CLIENT ANXIETY:",
        "prompt_text": "\"The report says 'Medium Blue Fluorescence' and 'Feather'—is this diamond defective?\"",
        "left_title": "AMATEUR TRAP (DEFENSIVE APOLOGY)",
        "left_quote": [
            "\"Yeah, fluorescence can make diamonds cloudy, but don't worry,",
            "we discounted this stone by 15% so it's a bargain!\""
        ],
        "left_bullets": [
            "• Validates false myths and introduces doubt into the customer's mind.",
            "• Discounts prematurely instead of explaining the optical phenomenon.",
            "• Fails to distinguish microscopic feather relief from durability risks.",
            "• Result: Client feels they are buying damaged goods; sale stalls."
        ],
        "right_title": "MASTER ADVISOR (OPTICAL CLARITY)",
        "right_quote": [
            "\"Blue fluorescence is nature's secret enhancer—in daylight, it naturally",
            "cancels faint yellow tints, making near-colorless stones face up whiter.",
            "And this feather is completely eye-clean, tucked safely under a prong.\""
        ],
        "right_bullets": [
            "• Cites GIA research: Less than 0.2% of fluorescent diamonds show milkiness.",
            "• Explains inclusion relief and location: Internal feather vs surface-reaching cleavage.",
            "• Demonstrates under UV light cabinet vs indirect northern daylight.",
            "• Result: Client feels smart, confident, and thrilled with their purchase."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Fluorescence in near-colorless diamonds is an optical asset. Demystify with science, not discounts.\""
    },
    {
        "id": "card_09_first_90_seconds",
        "title": "The First 90 Seconds: Frictionless Luxury Consultation",
        "subtitle": "C2-M01 MASTERCLASS: COUNTER ENGAGEMENT & SHIELD DEFENSE",
        "prompt_label": "WALK-IN MOMENT:",
        "prompt_text": "Client enters the salon and stands near the bridal case with defensive posture.",
        "left_title": "AMATEUR TRAP (INTERROGATION)",
        "left_quote": [
            "\"Hi there! Can I help you find something today? Are you looking",
            "for an engagement ring? What's your target budget?\""
        ],
        "left_bullets": [
            "• Triggers immediate 'Just looking' protective defense shield.",
            "• Introduces financial interrogation before establishing comfort or trust.",
            "• Makes the showroom feel high-pressure and commission-driven.",
            "• Result: Client retreats, avoids eye contact, and exits within 2 minutes."
        ],
        "right_title": "MASTER ADVISOR (HOSPITALITY PROTOCOL)",
        "right_quote": [
            "\"Good afternoon, welcome! Please make yourselves completely at",
            "home and enjoy exploring. My name is Neel—I'll be right nearby if",
            "you'd like to see any piece closer.\""
        ],
        "right_bullets": [
            "• Welcome (0-10s): Warm smile, eye contact, respectful physical space.",
            "• Ease (10-25s): Gives permission to browse without sales hovering.",
            "• Observation (25-65s): Watches genuine style cues and hand orientation.",
            "• Permission (65-90s): 'Are we celebrating a milestone, or exploring styles?'"
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Never try to close the sale in the first 90 seconds. Focus 100% on opening the relationship.\""
    },
    {
        "id": "card_10_defending_value",
        "title": "Defending Value: Overcoming Online Showrooming",
        "subtitle": "C2-M05 MASTERCLASS: DEFENDING MARGIN WITHOUT DISCOUNTING",
        "prompt_label": "PRICE CHALLENGE:",
        "prompt_text": "\"I found a 1.50-carat diamond online for $1,800 less than this ring. Can you match that?\"",
        "left_title": "AMATEUR TRAP (PANIC & DISCOUNT)",
        "left_quote": [
            "\"Online websites sell junk with fake certificates! But if you buy",
            "right now, let me talk to my manager and we'll cut $1,500 off.\""
        ],
        "left_bullets": [
            "• Attacks the competition, instantly appearing desperate and dishonest.",
            "• Immediate discount proves the original price was arbitrary and inflated.",
            "• Erodes all store authority and destroys operational margin.",
            "• Result: Client feels manipulated; leaves to purchase online anyway."
        ],
        "right_title": "MASTER ADVISOR (THE VALUE AUDIT)",
        "right_quote": [
            "\"It makes complete sense to compare—you deserve total confidence.",
            "Let's look at the specifications side by side to ensure we're comparing",
            "the exact same optical make, mounting security, and lifetime service.\""
        ],
        "right_bullets": [
            "• Validates client diligence: Treats comparison as an inquiry into value.",
            "• Audits like-for-like: Center stone make, metal weight, side-stone quality.",
            "• Articulates total ownership value: In-person try-on, sizing, lifelong care.",
            "• Result: Margin preserved, client chooses local relationship with conviction."
        ],
        "bottom_title": "GOLDEN PRINCIPLE:",
        "bottom_text": "\"Never apologize for your price. Help the client audit what they are actually buying.\""
    }
]

def render_card(data):
    img = Image.new('RGB', (W, H), (11, 15, 23)) # Deep Onyx
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rectangle([40, 40, W-40, H-40], outline=(40, 48, 64), width=1)

    f_tag = ImageFont.truetype(font_arial, 15)
    f_h1 = ImageFont.truetype(font_geo, 36)
    f_client = ImageFont.truetype(font_geo, 26)
    f_label = ImageFont.truetype(font_arial, 18)
    f_quote = ImageFont.truetype(font_geo, 23)
    f_desc = ImageFont.truetype(font_arial, 15)

    # Header
    draw.text((80, 70), 'JEWELSWELL ACADEMY  •  ' + data["subtitle"], font=f_tag, fill=(201, 162, 39))
    draw.text((80, 98), data["title"], font=f_h1, fill=(255, 255, 255))

    # Client Prompt Bar
    draw.rectangle([80, 165, W-80, 245], fill=(22, 28, 42), outline=(51, 65, 85), width=1)
    draw.text((110, 192), data["prompt_label"], font=f_label, fill=(148, 163, 184))
    draw.text((290, 188), data["prompt_text"], font=f_client, fill=(223, 190, 84))

    card_y0, card_y1 = 280, 860

    # Left Card (Amateur)
    c1_x0, c1_x1 = 80, 930
    draw.rectangle([c1_x0, card_y0, c1_x1, card_y1], fill=(18, 22, 32), outline=(153, 27, 27), width=2)
    draw.rectangle([c1_x0, card_y0, c1_x1, card_y0 + 55], fill=(153, 27, 27))
    draw.text((c1_x0 + 30, card_y0 + 16), data["left_title"], font=f_label, fill=(255, 255, 255))

    cy = card_y0 + 85
    for line in data["left_quote"]:
        draw.text((c1_x0 + 30, cy), line, font=f_quote, fill=(248, 113, 113))
        cy += 38

    cy += 20
    draw.rectangle([c1_x0 + 30, cy, c1_x1 - 30, cy + 1], fill=(51, 65, 85))
    cy += 25
    for b in data["left_bullets"]:
        draw.text((c1_x0 + 30, cy), b, font=f_desc, fill=(148, 163, 184))
        cy += 36

    # Right Card (Master Advisor)
    c2_x0, c2_x1 = 990, W - 80
    draw.rectangle([c2_x0, card_y0, c2_x1, card_y1], fill=(18, 22, 32), outline=(201, 162, 39), width=2)
    draw.rectangle([c2_x0, card_y0, c2_x1, card_y0 + 55], fill=(201, 162, 39))
    draw.text((c2_x0 + 30, card_y0 + 16), data["right_title"], font=f_label, fill=(11, 15, 23))

    cy = card_y0 + 85
    for line in data["right_quote"]:
        draw.text((c2_x0 + 30, cy), line, font=f_quote, fill=(223, 190, 84))
        cy += 38

    cy += 20
    draw.rectangle([c2_x0 + 30, cy, c2_x1 - 30, cy + 1], fill=(51, 65, 85))
    cy += 25
    for b in data["right_bullets"]:
        draw.text((c2_x0 + 30, cy), b, font=f_desc, fill=(226, 232, 240))
        cy += 36

    # Bottom Takeaway Bar
    draw.rectangle([80, 900, W - 80, 980], fill=(20, 26, 38), outline=(201, 162, 39), width=1)
    draw.text((120, 927), data["bottom_title"], font=f_label, fill=(201, 162, 39))
    draw.text((360, 924), data["bottom_text"], font=f_quote, fill=(255, 255, 255))

    out_file = os.path.join(out_dir, f"{data['id']}.png")
    img.save(out_file)
    print(f"[OK] Generated: {out_file}")

if __name__ == "__main__":
    for card in CARDS_DATA:
        render_card(card)
    print("All 10 infographic cards generated successfully.")
