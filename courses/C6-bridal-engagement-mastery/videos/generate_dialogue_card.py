from PIL import Image, ImageDraw, ImageFont

font_geo = 'courses/C6-bridal-engagement-mastery/videos/georgia.ttf'
font_arial = 'courses/C6-bridal-engagement-mastery/videos/arial.ttf'

W, H = 1920, 1080
img = Image.new('RGB', (W, H), (11, 15, 23)) # Deep Onyx
draw = ImageDraw.Draw(img)

# Outer subtle border
draw.rectangle([40, 40, W-40, H-40], outline=(40, 48, 64), width=1)

# Header banner
f_tag = ImageFont.truetype(font_arial, 15)
f_h1 = ImageFont.truetype(font_geo, 36)
f_client = ImageFont.truetype(font_geo, 28)
f_label = ImageFont.truetype(font_arial, 18)
f_quote = ImageFont.truetype(font_geo, 24)
f_desc = ImageFont.truetype(font_arial, 15)

draw.text((80, 70), 'JEWELSWELL ACADEMY  •  COUNTER SIMULATION SUITE', font=f_tag, fill=(201, 162, 39))
draw.text((80, 98), 'The Consultation Protocol: Navigating "Different"', font=f_h1, fill=(255, 255, 255))

# Client speech bubble
draw.rectangle([80, 165, W-80, 245], fill=(22, 28, 42), outline=(51, 65, 85), width=1)
draw.text((110, 192), 'CLIENT PROMPT:', font=f_label, fill=(148, 163, 184))
draw.text((290, 188), '"We want something that feels different."', font=f_client, fill=(223, 190, 84))

# Left Card: Amateur Trap
card_y0, card_y1 = 280, 860
card1_x0, card1_x1 = 80, 930
draw.rectangle([card1_x0, card_y0, card1_x1, card_y1], fill=(18, 22, 32), outline=(153, 27, 27), width=2)
# Badge
draw.rectangle([card1_x0, card_y0, card1_x1, card_y0 + 55], fill=(153, 27, 27))
draw.text((card1_x0 + 30, card_y0 + 16), 'AMATEUR TRAP  (INVENTORY PITCH)', font=f_label, fill=(255, 255, 255))

t1_lines = [
    '"Oh, then you definitely need an elongated oval with',
    'a hidden halo! It is our number one trending ring',
    'and everyone on Instagram is buying it right now."'
]
cy = card_y0 + 90
for line in t1_lines:
    draw.text((card1_x0 + 30, cy), line, font=f_quote, fill=(248, 113, 113))
    cy += 40

# Fatal errors bullet list
cy += 30
draw.rectangle([card1_x0 + 30, cy, card1_x1 - 30, cy + 1], fill=(51, 65, 85))
cy += 30
bullets1 = [
    '• Assumes "different" always equals high-volume social trends.',
    '• Makes the consultation transactional rather than advisory.',
    '• Alienates buyers seeking quiet, understated, or heritage style.',
    '• Result: Heightened comparison shopping & price commoditization.'
]
for b in bullets1:
    draw.text((card1_x0 + 30, cy), b, font=f_desc, fill=(148, 163, 184))
    cy += 36

# Right Card: Master Advisor
card2_x0, card2_x1 = 990, W - 80
draw.rectangle([card2_x0, card_y0, card2_x1, card_y1], fill=(18, 22, 32), outline=(201, 162, 39), width=2)
# Badge
draw.rectangle([card2_x0, card_y0, card2_x1, card_y0 + 55], fill=(201, 162, 39))
draw.text((card2_x0 + 30, card_y0 + 16), 'MASTER ADVISOR  (DISCOVERY FRAMEWORK)', font=f_label, fill=(11, 15, 23))

t2_lines = [
    '"When you say different, do you imagine something',
    'distinctive in shape—like an architectural bezel—or',
    'quiet elegance with a subtle, personal side detail?"'
]
cy = card_y0 + 90
for line in t2_lines:
    draw.text((card2_x0 + 30, cy), line, font=f_quote, fill=(223, 190, 84))
    cy += 40

# Master disciplines bullet list
cy += 30
draw.rectangle([card2_x0 + 30, cy, card2_x1 - 30, cy + 1], fill=(51, 65, 85))
cy += 30
bullets2 = [
    '• Validates research without rushing into sales catalogs.',
    '• Slows the appointment pace down to build emotional custody.',
    '• Uncovers whether priority is presence, comfort, or symbolism.',
    '• Result: Immediate client trust, zero price pushback, high close rate.'
]
for b in bullets2:
    draw.text((card2_x0 + 30, cy), b, font=f_desc, fill=(226, 232, 240))
    cy += 36

# Bottom takeaway bar
draw.rectangle([80, 900, W - 80, 980], fill=(20, 26, 38), outline=(201, 162, 39), width=1)
draw.text((120, 927), 'CAPSTONE PRINCIPLE:', font=f_label, fill=(201, 162, 39))
draw.text((360, 924), '"In luxury bridal, never pitch the trend. Discover the identity."', font=f_quote, fill=(255, 255, 255))

out_path = 'courses/C6-bridal-engagement-mastery/videos/dialogue_card_c6.png'
img.save(out_path)
print('Generated dialogue card:', out_path)
