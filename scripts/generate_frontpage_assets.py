"""Generate the 17 frontpage assets: the master hero banner plus one 16:9
masterclass cover per course (C1-C14, C16, C17).

Output: assets/frontpage/*.svg   (1600 x 900, 16:9)

Run from the repository root:  python3 scripts/generate_frontpage_assets.py
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jw_svg_kit import (  # noqa: E402
    COURSE_ACCENT, DIM, GOLD, MUTED, TEXT, WHITE,
    esc, save, svg_doc, text_el, wrap,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "frontpage")

W, H = 1600, 900


# ----------------------------------------------------------------- emblems
def em_diamond(cx, cy, r, accent):
    """Brilliant-cut diamond seen face-up: table, star and bezel facets."""
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in range(-90, 270, 45)]
    girdle = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    tr = r * 0.42
    tpts = [(cx + tr * math.cos(math.radians(a)), cy + tr * math.sin(math.radians(a)))
            for a in range(-90, 270, 45)]
    table = " ".join(f"{x:.1f},{y:.1f}" for x, y in tpts)
    spokes = "".join(
        f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{tpts[i][0]:.1f}" '
        f'y2="{tpts[i][1]:.1f}" stroke="{accent}" stroke-width="1.6" '
        f'stroke-opacity="0.75"/>' for i in range(8))
    return f'''<g>
    <polygon points="{girdle}" fill="url(#accent)" fill-opacity="0.18" stroke="{accent}" stroke-width="2.4"/>
    <polygon points="{table}" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-width="1.8"/>
    {spokes}
  </g>'''


def em_octahedron(cx, cy, r, accent):
    """Rough diamond octahedron / carbon lattice cell."""
    t, b = (cx, cy - r), (cx, cy + r)
    l, rt = (cx - r * 0.78, cy), (cx + r * 0.78, cy)
    f, bk = (cx - r * 0.34, cy + r * 0.30), (cx + r * 0.34, cy - r * 0.30)
    def ln(p, q, op="0.85", dash=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" '
                f'stroke="{accent}" stroke-width="2" stroke-opacity="{op}"{d}/>')
    edges = "".join(ln(a, b_) for a, b_ in
                    [(t, l), (t, rt), (t, f), (t, bk), (b, l), (b, rt), (b, f), (b, bk)])
    edges += ln(l, f) + ln(f, rt) + ln(rt, bk, "0.4", "5 4") + ln(bk, l, "0.4", "5 4")
    nodes = "".join(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="5" fill="{accent}"/>'
                    for p in [t, b, l, rt, f, bk])
    return f'<g><polygon points="{t[0]:.1f},{t[1]:.1f} {rt[0]:.1f},{rt[1]:.1f} {b[0]:.1f},{b[1]:.1f} {l[0]:.1f},{l[1]:.1f}" fill="url(#accent)" fill-opacity="0.14"/>{edges}{nodes}</g>'


def em_nodes(cx, cy, r, accent, n=7, hub=True):
    """Relationship / network node cluster."""
    pts = [(cx + r * math.cos(math.radians(-90 + i * 360 / n)),
            cy + r * math.sin(math.radians(-90 + i * 360 / n))) for i in range(n)]
    out = []
    for i, (x, y) in enumerate(pts):
        if hub:
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" '
                       f'stroke="{accent}" stroke-width="1.5" stroke-opacity="0.55"/>')
        nx, ny = pts[(i + 1) % n]
        out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{nx:.1f}" y2="{ny:.1f}" '
                   f'stroke="{accent}" stroke-width="1.2" stroke-opacity="0.28"/>')
    for x, y in pts:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{accent}" fill-opacity="0.9"/>')
    if hub:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="url(#accent)" '
                   f'fill-opacity="0.35" stroke="{accent}" stroke-width="2.4"/>')
    return "<g>" + "".join(out) + "</g>"


def em_shield(cx, cy, r, accent):
    """Vault / dual-custody security shield with keyhole."""
    top, half, bot = cy - r, r * 0.80, cy + r
    return f'''<g>
    <path d="M {cx} {top} L {cx + half} {top + r * 0.30} L {cx + half} {cy + r * 0.20}
             Q {cx + half} {bot - r * 0.10} {cx} {bot}
             Q {cx - half} {bot - r * 0.10} {cx - half} {cy + r * 0.20}
             L {cx - half} {top + r * 0.30} Z"
          fill="url(#accent)" fill-opacity="0.16" stroke="{accent}" stroke-width="2.6"/>
    <circle cx="{cx}" cy="{cy - r * 0.12}" r="{r * 0.20:.1f}" fill="none" stroke="{accent}" stroke-width="2.4"/>
    <rect x="{cx - r * 0.06:.1f}" y="{cy - r * 0.12:.1f}" width="{r * 0.12:.1f}" height="{r * 0.34:.1f}" fill="{accent}"/>
    <circle cx="{cx - r * 0.44:.1f}" cy="{cy + r * 0.44:.1f}" r="7" fill="{accent}" fill-opacity="0.8"/>
    <circle cx="{cx + r * 0.44:.1f}" cy="{cy + r * 0.44:.1f}" r="7" fill="{accent}" fill-opacity="0.8"/>
  </g>'''


def em_card(cx, cy, r, accent):
    """Retail credit card with installment ticks."""
    w, h = r * 1.7, r * 1.10
    x, y = cx - w / 2, cy - h / 2
    ticks = "".join(
        f'<rect x="{x + w * 0.10 + i * (w * 0.20):.1f}" y="{y + h + 22:.1f}" '
        f'width="{w * 0.14:.1f}" height="9" rx="4" fill="{accent}" '
        f'fill-opacity="{0.9 - i * 0.18:.2f}"/>' for i in range(4))
    return f'''<g>
    <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="14"
          fill="url(#accent)" fill-opacity="0.18" stroke="{accent}" stroke-width="2.4"/>
    <rect x="{x:.1f}" y="{y + h * 0.20:.1f}" width="{w:.1f}" height="{h * 0.17:.1f}" fill="{accent}" fill-opacity="0.55"/>
    <rect x="{x + w * 0.10:.1f}" y="{y + h * 0.58:.1f}" width="{w * 0.22:.1f}" height="{h * 0.20:.1f}" rx="4"
          fill="{accent}" fill-opacity="0.85"/>
    {ticks}
  </g>'''


def em_solitaire(cx, cy, r, accent):
    """Platinum solitaire ring with a pave band."""
    band = r * 0.72
    pave = "".join(
        f'<circle cx="{cx + band * math.cos(math.radians(a)):.1f}" '
        f'cy="{cy + r * 0.28 + band * math.sin(math.radians(a)):.1f}" r="3.4" fill="{accent}"/>'
        for a in range(20, 170, 15))
    gx, gy = cx, cy - r * 0.52
    g = r * 0.26
    return f'''<g>
    <circle cx="{cx}" cy="{cy + r * 0.28:.1f}" r="{band:.1f}" fill="none" stroke="{accent}" stroke-width="7" stroke-opacity="0.35"/>
    <circle cx="{cx}" cy="{cy + r * 0.28:.1f}" r="{band:.1f}" fill="none" stroke="{accent}" stroke-width="2.4"/>
    {pave}
    <polygon points="{gx - g:.1f},{gy:.1f} {gx:.1f},{gy - g * 0.95:.1f} {gx + g:.1f},{gy:.1f} {gx:.1f},{gy + g * 1.25:.1f}"
             fill="url(#accent)" fill-opacity="0.30" stroke="{accent}" stroke-width="2.4"/>
    <line x1="{gx - g:.1f}" y1="{gy:.1f}" x2="{gx + g:.1f}" y2="{gy:.1f}" stroke="{accent}" stroke-width="1.6"/>
  </g>'''


def em_filigree(cx, cy, r, accent):
    """Antique filigree frame with scrollwork."""
    scroll = "".join(
        f'<path d="M {cx + dx * r * 0.62:.1f} {cy + dy * r * 0.62:.1f} '
        f'q {dx * r * 0.22:.1f} {-dy * r * 0.10:.1f} {dx * r * 0.20:.1f} {dy * r * 0.22:.1f}" '
        f'fill="none" stroke="{accent}" stroke-width="2" stroke-opacity="0.75"/>'
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)])
    return f'''<g>
    <rect x="{cx - r * 0.86:.1f}" y="{cy - r * 0.86:.1f}" width="{r * 1.72:.1f}" height="{r * 1.72:.1f}"
          rx="10" fill="none" stroke="{accent}" stroke-width="2.6" transform="rotate(45 {cx} {cy})"/>
    <circle cx="{cx}" cy="{cy}" r="{r * 0.56:.1f}" fill="url(#accent)" fill-opacity="0.16" stroke="{accent}" stroke-width="2"/>
    <circle cx="{cx}" cy="{cy}" r="{r * 0.28:.1f}" fill="{accent}" fill-opacity="0.55"/>
    {scroll}
  </g>'''


def em_cad(cx, cy, r, accent):
    """CAD wireframe ring resolving into a cast band."""
    rings = "".join(
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 0.80:.1f}" ry="{r * 0.80 * (0.20 + i * 0.16):.1f}" '
        f'fill="none" stroke="{accent}" stroke-width="1.5" stroke-opacity="{0.30 + i * 0.12:.2f}"/>'
        for i in range(5))
    verts = "".join(
        f'<line x1="{cx + r * 0.80 * math.cos(math.radians(a)):.1f}" y1="{cy - r * 0.62:.1f}" '
        f'x2="{cx + r * 0.80 * math.cos(math.radians(a)):.1f}" y2="{cy + r * 0.62:.1f}" '
        f'stroke="{accent}" stroke-width="1" stroke-opacity="0.35"/>' for a in range(0, 180, 30))
    return f'''<g>
    {rings}{verts}
    <circle cx="{cx}" cy="{cy}" r="{r * 0.80:.1f}" fill="none" stroke="{accent}" stroke-width="2.6"/>
    <circle cx="{cx}" cy="{cy - r * 0.80:.1f}" r="9" fill="{accent}"/>
  </g>'''


def em_stopwatch(cx, cy, r, accent):
    """High-velocity stopwatch."""
    ticks = "".join(
        f'<line x1="{cx + r * 0.80 * math.cos(math.radians(a)):.1f}" y1="{cy + r * 0.80 * math.sin(math.radians(a)):.1f}" '
        f'x2="{cx + r * 0.94 * math.cos(math.radians(a)):.1f}" y2="{cy + r * 0.94 * math.sin(math.radians(a)):.1f}" '
        f'stroke="{accent}" stroke-width="2.4" stroke-opacity="0.8"/>' for a in range(0, 360, 30))
    return f'''<g>
    <circle cx="{cx}" cy="{cy}" r="{r * 0.94:.1f}" fill="url(#accent)" fill-opacity="0.12" stroke="{accent}" stroke-width="2.8"/>
    {ticks}
    <rect x="{cx - 13}" y="{cy - r * 1.18:.1f}" width="26" height="16" rx="5" fill="{accent}"/>
    <path d="M {cx} {cy} L {cx + r * 0.52:.1f} {cy - r * 0.42:.1f}" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M {cx} {cy} L {cx:.1f} {cy - r * 0.66:.1f}" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="{cx}" cy="{cy}" r="7" fill="{WHITE}"/>
    <path d="M {cx - r * 0.30:.1f} {cy + r * 0.52:.1f} l {r * 0.24:.1f} 0 l -{r * 0.10:.1f} {r * 0.20:.1f}"
          fill="none" stroke="{accent}" stroke-width="2"/>
  </g>'''


def em_crown(cx, cy, r, accent):
    """High-net-worth status crown over an anchoring scale."""
    w = r * 0.92
    pts = (f"{cx - w:.1f},{cy + r * 0.34:.1f} {cx - w:.1f},{cy - r * 0.34:.1f} "
           f"{cx - w * 0.42:.1f},{cy + r * 0.02:.1f} {cx:.1f},{cy - r * 0.60:.1f} "
           f"{cx + w * 0.42:.1f},{cy + r * 0.02:.1f} {cx + w:.1f},{cy - r * 0.34:.1f} "
           f"{cx + w:.1f},{cy + r * 0.34:.1f}")
    gems = "".join(f'<circle cx="{cx + dx:.1f}" cy="{cy - r * 0.10:.1f}" r="5" fill="{accent}"/>'
                   for dx in (-w * 0.55, 0, w * 0.55))
    return f'''<g>
    <polygon points="{pts}" fill="url(#accent)" fill-opacity="0.20" stroke="{accent}" stroke-width="2.6" stroke-linejoin="round"/>
    <rect x="{cx - w:.1f}" y="{cy + r * 0.40:.1f}" width="{w * 2:.1f}" height="12" rx="5" fill="{accent}" fill-opacity="0.75"/>
    {gems}
  </g>'''


def em_checklist(cx, cy, r, accent):
    """Daily operating-rhythm checklist board."""
    rows = "".join(f'''
    <rect x="{cx - r * 0.66:.1f}" y="{cy - r * 0.58 + i * (r * 0.34):.1f}" width="{r * 0.22:.1f}" height="{r * 0.22:.1f}"
          rx="5" fill="{accent}" fill-opacity="{0.85 if i < 2 else 0.18:.2f}" stroke="{accent}" stroke-width="1.8"/>
    <rect x="{cx - r * 0.32:.1f}" y="{cy - r * 0.50 + i * (r * 0.34):.1f}" width="{r * (0.98 - i * 0.14):.1f}" height="7"
          rx="3.5" fill="{accent}" fill-opacity="{0.55 - i * 0.10:.2f}"/>''' for i in range(4))
    return f'''<g>
    <rect x="{cx - r * 0.86:.1f}" y="{cy - r * 0.86:.1f}" width="{r * 1.72:.1f}" height="{r * 1.72:.1f}"
          rx="12" fill="url(#accent)" fill-opacity="0.10" stroke="{accent}" stroke-width="2.4"/>
    {rows}
  </g>'''


def em_chart(cx, cy, r, accent):
    """KPI bar chart with a trend line."""
    vals = [0.38, 0.58, 0.46, 0.74, 0.92]
    bw = r * 0.24
    bars, pts = [], []
    for i, v in enumerate(vals):
        x = cx - r * 0.78 + i * (r * 0.38)
        h = r * 1.20 * v
        bars.append(f'<rect x="{x:.1f}" y="{cy + r * 0.62 - h:.1f}" width="{bw:.1f}" height="{h:.1f}" '
                    f'rx="4" fill="{accent}" fill-opacity="{0.35 + i * 0.13:.2f}"/>')
        pts.append(f"{x + bw / 2:.1f},{cy + r * 0.62 - h - 12:.1f}")
    return f'''<g>
    <line x1="{cx - r * 0.90:.1f}" y1="{cy + r * 0.62:.1f}" x2="{cx + r * 0.90:.1f}" y2="{cy + r * 0.62:.1f}"
          stroke="{accent}" stroke-width="2.4" stroke-opacity="0.7"/>
    {''.join(bars)}
    <polyline points="{' '.join(pts)}" fill="none" stroke="{WHITE}" stroke-width="2.4" stroke-opacity="0.9"
              stroke-dasharray="6 4"/>
  </g>'''


def em_mentor(cx, cy, r, accent):
    """Leadership mentoring: a lead figure coaching two others."""
    def fig(x, y, s, op):
        return (f'<circle cx="{x:.1f}" cy="{y - s * 1.10:.1f}" r="{s * 0.46:.1f}" fill="{accent}" fill-opacity="{op}"/>'
                f'<path d="M {x - s * 0.66:.1f} {y + s * 0.80:.1f} q 0 -{s * 1.10:.1f} {s * 0.66:.1f} -{s * 1.10:.1f} '
                f'q {s * 0.66:.1f} 0 {s * 0.66:.1f} {s * 1.10:.1f} Z" fill="{accent}" fill-opacity="{op}"/>')
    arcs = "".join(
        f'<path d="M {cx - r * 0.20:.1f} {cy - r * 0.34:.1f} Q {cx + dx * 0.5:.1f} {cy - r * 0.86:.1f} {cx + dx:.1f} {cy - r * 0.16:.1f}" '
        f'fill="none" stroke="{accent}" stroke-width="2" stroke-opacity="0.5" stroke-dasharray="5 4"/>'
        for dx in (-r * 0.66, r * 0.66))
    return (f'<g>{arcs}{fig(cx, cy + r * 0.10, r * 0.40, 0.95)}'
            f'{fig(cx - r * 0.72, cy + r * 0.30, r * 0.28, 0.55)}'
            f'{fig(cx + r * 0.72, cy + r * 0.30, r * 0.28, 0.55)}</g>')


def em_region(cx, cy, r, accent):
    """Multi-unit regional network: HQ hub over four store pins."""
    stores = [(-0.78, 0.18), (-0.26, 0.62), (0.26, 0.62), (0.78, 0.18)]
    out = []
    for dx, dy in stores:
        x, y = cx + r * dx, cy + r * dy
        out.append(f'<line x1="{cx}" y1="{cy - r * 0.52:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
                   f'stroke="{accent}" stroke-width="1.6" stroke-opacity="0.5" stroke-dasharray="5 4"/>')
        out.append(f'<rect x="{x - 17:.1f}" y="{y - 15:.1f}" width="34" height="30" rx="6" '
                   f'fill="{accent}" fill-opacity="0.22" stroke="{accent}" stroke-width="2"/>')
        out.append(f'<path d="M {x - 20:.1f} {y - 15:.1f} l 20 -13 l 20 13 Z" fill="{accent}" fill-opacity="0.8"/>')
    out.append(f'<circle cx="{cx}" cy="{cy - r * 0.52:.1f}" r="{r * 0.26:.1f}" fill="url(#accent)" '
               f'fill-opacity="0.40" stroke="{accent}" stroke-width="2.6"/>')
    out.append(text_el(cx, cy - r * 0.52 + 6, "HQ", WHITE, 15, "800", "middle"))
    return "<g>" + "".join(out) + "</g>"


def em_trigems(cx, cy, r, accent):
    """Tri-gem cluster: ruby cushion, sapphire oval, emerald step-cut."""
    ruby, sapph, emer, jade = "#FB7185", "#60A5FA", "#34D399", "#A3E635"
    rx, ry = cx - r * 0.62, cy + r * 0.20
    sx, sy = cx + r * 0.62, cy + r * 0.20
    ex, ey = cx, cy - r * 0.46
    return f'''<g>
    <rect x="{ex - r * 0.34:.1f}" y="{ey - r * 0.28:.1f}" width="{r * 0.68:.1f}" height="{r * 0.56:.1f}" rx="8"
          fill="{emer}" fill-opacity="0.26" stroke="{emer}" stroke-width="2.4"/>
    <rect x="{ex - r * 0.22:.1f}" y="{ey - r * 0.17:.1f}" width="{r * 0.44:.1f}" height="{r * 0.34:.1f}" rx="5"
          fill="none" stroke="{emer}" stroke-width="1.5" stroke-opacity="0.8"/>
    <path d="M {rx - r * 0.32:.1f} {ry} L {rx:.1f} {ry - r * 0.30:.1f} L {rx + r * 0.32:.1f} {ry}
             L {rx:.1f} {ry + r * 0.34:.1f} Z" fill="{ruby}" fill-opacity="0.28" stroke="{ruby}" stroke-width="2.4"/>
    <line x1="{rx - r * 0.32:.1f}" y1="{ry}" x2="{rx + r * 0.32:.1f}" y2="{ry}" stroke="{ruby}" stroke-width="1.4"/>
    <ellipse cx="{sx:.1f}" cy="{ry:.1f}" rx="{r * 0.30:.1f}" ry="{r * 0.34:.1f}"
             fill="{sapph}" fill-opacity="0.28" stroke="{sapph}" stroke-width="2.4"/>
    <ellipse cx="{sx:.1f}" cy="{ry:.1f}" rx="{r * 0.15:.1f}" ry="{r * 0.17:.1f}"
             fill="none" stroke="{sapph}" stroke-width="1.5" stroke-opacity="0.8"/>
    <circle cx="{cx:.1f}" cy="{cy + r * 0.62:.1f}" r="{r * 0.17:.1f}" fill="{jade}" fill-opacity="0.30"
            stroke="{jade}" stroke-width="2.2"/>
    <circle cx="{cx:.1f}" cy="{cy + r * 0.62:.1f}" r="{r * 0.07:.1f}" fill="none" stroke="{jade}" stroke-width="1.6"/>
  </g>'''


def em_conversation(cx, cy, r, accent):
    """Sales conversation: two speech bubbles and a discovery arc."""
    return f'''<g>
    <path d="M {cx - r * 0.92:.1f} {cy - r * 0.62:.1f} h {r * 1.05:.1f} a 12 12 0 0 1 12 12
             v {r * 0.56:.1f} a 12 12 0 0 1 -12 12 h -{r * 0.70:.1f} l -{r * 0.22:.1f} {r * 0.26:.1f}
             v -{r * 0.26:.1f} h -{r * 0.13:.1f} a 12 12 0 0 1 -12 -12 v -{r * 0.56:.1f}
             a 12 12 0 0 1 12 -12 Z" fill="url(#accent)" fill-opacity="0.20" stroke="{accent}" stroke-width="2.4"/>
    <path d="M {cx + r * 0.92:.1f} {cy + r * 0.72:.1f} h -{r * 1.05:.1f} a 12 12 0 0 1 -12 -12
             v -{r * 0.44:.1f} a 12 12 0 0 1 12 -12 h {r * 1.05:.1f} a 12 12 0 0 1 12 12
             v {r * 0.44:.1f} a 12 12 0 0 1 -12 12 Z" fill="{accent}" fill-opacity="0.10"
          stroke="{accent}" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="{cx - r * 0.50:.1f}" cy="{cy - r * 0.28:.1f}" r="5" fill="{accent}"/>
    <circle cx="{cx - r * 0.24:.1f}" cy="{cy - r * 0.28:.1f}" r="5" fill="{accent}" fill-opacity="0.7"/>
    <circle cx="{cx + r * 0.02:.1f}" cy="{cy - r * 0.28:.1f}" r="5" fill="{accent}" fill-opacity="0.45"/>
  </g>'''


# ------------------------------------------------------------- course data
COURSES = [
    dict(code="C1", slug="c1-cover-diamond-gemstone-fluency",
         eyebrow="MASTERCLASS C1 — PRODUCT FLUENCY",
         title="Diamond & Gemstone Fluency",
         tag="Speak the 4Cs with authority and read a GIA report in front of the client.",
         badges=["4Cs FLUENCY", "GIA REPORT READING", "10 MODULES"],
         chips=["Cut · Color · Clarity · Carat", "Plot & inclusion symbols",
                "Fluorescence & treatments", "Colored-stone top 10"],
         emblem=em_diamond),
    dict(code="C2", slug="c2-cover-fine-jewelry-sales-conversation",
         eyebrow="MASTERCLASS C2 — SELLING SKILL",
         title="The Fine Jewelry Sales Conversation",
         tag="Sales psychology from the first 90 seconds on the floor to the close.",
         badges=["90-SECOND OPEN", "3 CLOSING PROTOCOLS", "10 MODULES"],
         chips=["Discovery questioning tree", "Buying signals & silence",
                "Price objections without discounting", "Three ways to ask"],
         emblem=em_conversation),
    dict(code="C3", slug="c3-cover-clienteling-and-crm",
         eyebrow="MASTERCLASS C3 — RELATIONSHIP REVENUE",
         title="Clienteling & CRM",
         tag="Build a client book that produces revenue without waiting for walk-in traffic.",
         badges=["2-2-2 CADENCE", "VIC TIERING", "8 MODULES"],
         chips=["Client profile architecture", "Segmenting the book",
                "Life-event triggers", "Referral engine"],
         emblem=em_nodes),
    dict(code="C4", slug="c4-cover-store-security-loss-prevention",
         eyebrow="MASTERCLASS C4 — RISK & CONTROL",
         title="Store Security & Loss Prevention",
         tag="Dual custody, showcase discipline, and the cash rules that keep you compliant.",
         badges=["DUAL CUSTODY", "SHOWCASE RULES", "AML / FORM 8300"],
         chips=["Opening & closing procedure", "Safes, vaults, put-away",
                "Distraction theft patterns", "Cycle counts & shrink"],
         emblem=em_shield),
    dict(code="C5", slug="c5-cover-financing-credit-compliance",
         eyebrow="MASTERCLASS C5 — CREDIT & COMPLIANCE",
         title="Financing, Credit & Compliance",
         tag="Present retail credit accurately — promotional terms, disclosures and all.",
         badges=["0% PROMO TERMS", "TILA DISCLOSURE", "6 MODULES"],
         chips=["Consumer financing basics", "Running an application",
                "Layaway vs. BNPL", "Memo, consignment, UCC-1"],
         emblem=em_card),
    dict(code="C6", slug="c6-cover-bridal-engagement-mastery",
         eyebrow="MASTERCLASS C6 — BRIDAL",
         title="Bridal & Engagement Mastery",
         tag="The couple's journey from first ring conversation to anniversary aftercare.",
         badges=["SOLITAIRE & PAVE", "COUPLE JOURNEY", "14 MODULES"],
         chips=["Shape vs. cut quality", "Natural, lab-grown, simulant",
                "Sizing, fit & comfort", "Proposal logistics"],
         emblem=em_solitaire),
    dict(code="C7", slug="c7-cover-estate-antique-trade-in",
         eyebrow="MASTERCLASS C7 — ESTATE & APPRAISAL",
         title="Estate, Antique & Trade-In",
         tag="Date a piece, authenticate the period, and price a trade-in with confidence.",
         badges=["VICTORIAN / ART DECO", "AUTHENTICATION", "APPRAISAL FORMULAS"],
         chips=["Reading a piece", "Dating & attribution",
                "Consignment & auction", "Legal and compliance"],
         emblem=em_filigree),
    dict(code="C8", slug="c8-cover-custom-design-repair-workflow",
         eyebrow="MASTERCLASS C8 — BENCH & CUSTOM",
         title="Custom Design & Repair Workflow",
         tag="CAD wireframe to cast gold — and the turnaround promises you can actually keep.",
         badges=["CAD TO CASTING", "REPAIR SLAs", "REVEAL CEREMONY"],
         chips=["Intake that prevents disputes", "Common bench repairs",
                "Pricing custom work", "Quality control & handoff"],
         emblem=em_cad),
    dict(code="C9", slug="c9-cover-selling-high-ticket-compressed-time",
         eyebrow="MASTERCLASS C9 — COMPRESSED TIME",
         title="Selling High-Ticket in Compressed Time",
         tag="Trunk shows, cruise ports and pop-ups: one window, no second visit.",
         badges=["3-HOUR TRUNK SHOW", "CRUISE-PORT CLOSING", "8 MODULES"],
         chips=["Compressed discovery", "Fast trust, no history",
                "The decision moment", "Fast, honest follow-up"],
         emblem=em_stopwatch),
    dict(code="C10", slug="c10-cover-luxury-consumer-psychology-negotiation",
         eyebrow="MASTERCLASS C10 — PSYCHOLOGY",
         title="Luxury Consumer Psychology & Negotiation",
         tag="Anchoring, scarcity and discretion for the high-net-worth buyer.",
         badges=["PRICE ANCHORING", "HNW DISCRETION", "CAPSTONE"],
         chips=["Reading the buyer", "Scarcity & social proof",
                "Anchoring & the decoy effect", "Cross-cultural buying"],
         emblem=em_crown),
    dict(code="C11", slug="c11-cover-running-the-store-operations",
         eyebrow="MASTERCLASS C11 — OPERATIONS",
         title="Running the Store",
         tag="The daily, weekly and monthly rhythm that keeps a jewelry floor on plan.",
         badges=["DAILY RHYTHM", "TRAFFIC-TO-SCHEDULE", "SHOWCASE ZONING"],
         chips=["Weekly counts & coaching", "Visual merchandising zones",
                "Peak-coverage scheduling", "Writing SOPs"],
         emblem=em_checklist),
    dict(code="C12", slug="c12-cover-retail-kpis-reporting",
         eyebrow="MASTERCLASS C12 — ANALYTICS",
         title="Retail KPIs & Reporting",
         tag="From KPI vocabulary to GMROI and a one-page store performance review.",
         badges=["GMROI", "CONVERSION FUNNEL", "DASHBOARDS"],
         chips=["ATV, UPT & product mix", "Inventory productivity",
                "Client-book health", "Diagnosing a miss"],
         emblem=em_chart),
    dict(code="C13", slug="c13-cover-hiring-coaching-performance",
         eyebrow="MASTERCLASS C13 — PEOPLE",
         title="Hiring, Coaching & Performance Management",
         tag="Audition-based hiring, 30-day onboarding, and coaching that sticks.",
         badges=["AUDITION HIRING", "30-DAY ONBOARDING", "10 MODULES"],
         chips=["Role profiles & sourcing", "Structured interviews",
                "Weekly one-on-ones", "Managing underperformance"],
         emblem=em_mentor),
    dict(code="C14", slug="c14-cover-multi-store-leadership",
         eyebrow="MASTERCLASS C14 — MULTI-UNIT",
         title="Multi-Store Leadership",
         tag="Running managers instead of stores — visits, comparatives and bench strength.",
         badges=["STORE-VISIT AUDITS", "COMPARATIVE KPIs", "TALENT SCALING"],
         chips=["From store to managers", "Coaching managers to coach",
                "Compliance oversight at scale", "Succession pipeline"],
         emblem=em_region),
    dict(code="C16", slug="c16-cover-gia-diamonds-deep-dive",
         eyebrow="MASTERCLASS C16 — GIA DEEP DIVE",
         title="The GIA Diamonds Deep Dive",
         tag="Mantle genesis to ray-traced light return, plus lab-grown diagnostics.",
         badges=["CARBON LATTICE", "3D RAY TRACING", "LAB-GROWN ID"],
         chips=["Mantle science & genesis", "Exploration & mining",
                "Cut-grade science", "Treatments & marketplace"],
         emblem=em_octahedron),
    dict(code="C17", slug="c17-cover-gia-colored-stones-deep-dive",
         eyebrow="MASTERCLASS C17 — GIA DEEP DIVE",
         title="The GIA Colored Stones Deep Dive",
         tag="Ruby, sapphire, emerald and jade — inclusion forensics and treatment tiers.",
         badges=["INCLUSION FORENSICS", "TREATMENT TIERS", "16 MODULES"],
         chips=["Formation & field gemology", "Color & light science",
                "Synthetics & separation", "Market hubs & auctions"],
         emblem=em_trigems),
]


# ------------------------------------------------------------------- cover
def build_cover(c):
    accent = COURSE_ACCENT[c["code"]]
    b = []

    # atmospheric glow behind the emblem
    b.append(f'  <circle cx="1210" cy="450" r="330" fill="url(#glow)"/>')
    # faint facet rays
    for a in range(0, 360, 18):
        x2 = 1210 + 520 * math.cos(math.radians(a))
        y2 = 450 + 520 * math.sin(math.radians(a))
        b.append(f'  <line x1="1210" y1="450" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{accent}" stroke-width="1" stroke-opacity="0.05"/>')

    # left rule + eyebrow
    b.append(f'  <rect x="96" y="120" width="64" height="4" rx="2" fill="url(#gold)"/>')
    b.append("  " + text_el(96, 168, c["eyebrow"], GOLD_LT_ := "#E5C378", 17, "700", spacing="2.6"))

    # title
    y = 246
    for line in wrap(c["title"], 22):
        b.append("  " + text_el(96, y, line, WHITE, 60, "800"))
        y += 68
    y += 4

    # tagline
    for line in wrap(c["tag"], 46):
        b.append("  " + text_el(96, y, line, MUTED, 22, "400"))
        y += 32

    # badge pills
    y += 22
    x = 96
    for badge in c["badges"]:
        w = 20 + len(badge) * 10.2
        b.append(f'  <rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="38" rx="19" '
                 f'fill="{accent}" fill-opacity="0.14" stroke="{accent}" stroke-width="1.6"/>')
        b.append("  " + text_el(x + w / 2, y + 25, badge, accent, 14, "700", "middle", spacing="0.8"))
        x += w + 14
    y += 74

    # curriculum chips (2 x 2)
    for i, chip in enumerate(c["chips"]):
        cx_ = 96 + (i % 2) * 300
        cy_ = y + (i // 2) * 42
        b.append(f'  <circle cx="{cx_ + 7}" cy="{cy_ - 5}" r="4.5" fill="{accent}"/>')
        b.append("  " + text_el(cx_ + 24, cy_, chip, TEXT, 17, "500"))
    y += 42 * 2 + 30

    # brand lockup
    b.append(f'  <rect x="96" y="{y}" width="3" height="40" rx="1.5" fill="url(#gold)"/>')
    b.append("  " + text_el(116, y + 18, "JEWELSWELL MASTER ACADEMY", "#E5C378", 14, "700", spacing="1.8"))
    b.append("  " + text_el(116, y + 38, "Fine Jewelry Retail Curriculum", DIM, 13, "400"))

    # emblem
    b.append("  " + c["emblem"](1210, 450, 250, accent))

    # course code chip, top right
    b.append(f'  <rect x="1396" y="96" width="108" height="46" rx="10" '
             f'fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-width="1.8"/>')
    b.append("  " + text_el(1450, 127, c["code"], accent, 24, "800", "middle", spacing="1.2"))

    return svg_doc(W, H, accent, "\n".join(b))


# -------------------------------------------------------------------- hero
def build_hero(stats):
    accent = "#38BDF8"
    b = []
    b.append('  <circle cx="1180" cy="450" r="380" fill="url(#glow)"/>')

    # 3D diamond wireframe (pavilion + crown, perspective)
    cx, cy, r = 1180, 430, 260
    girdle = [(cx + r * math.cos(math.radians(a)), cy + r * 0.34 * math.sin(math.radians(a)))
              for a in range(0, 360, 30)]
    culet = (cx, cy + r * 0.92)
    tbl_r = r * 0.52
    table = [(cx + tbl_r * math.cos(math.radians(a)), cy - r * 0.38 + tbl_r * 0.34 * math.sin(math.radians(a)))
             for a in range(0, 360, 30)]

    b.append('  <polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in girdle) +
             f'" fill="url(#accent)" fill-opacity="0.10" stroke="{accent}" stroke-width="2.6"/>')
    b.append('  <polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in table) +
             f'" fill="{accent}" fill-opacity="0.18" stroke="{accent}" stroke-width="2.2"/>')
    for i, (x, y) in enumerate(girdle):
        b.append(f'  <line x1="{x:.1f}" y1="{y:.1f}" x2="{culet[0]:.1f}" y2="{culet[1]:.1f}" '
                 f'stroke="{accent}" stroke-width="1.4" stroke-opacity="{0.22 if y < cy else 0.68:.2f}"/>')
        tx, ty = table[i]
        b.append(f'  <line x1="{x:.1f}" y1="{y:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
                 f'stroke="{accent}" stroke-width="1.4" stroke-opacity="{0.28 if y < cy else 0.7:.2f}"/>')
        b.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{accent}" fill-opacity="0.9"/>')
    b.append(f'  <circle cx="{culet[0]:.1f}" cy="{culet[1]:.1f}" r="6" fill="{accent}"/>')
    for a in (-38, -12, 16):
        b.append(f'  <line x1="{cx - 40}" y1="{cy - 120}" '
                 f'x2="{cx - 40 + 300 * math.cos(math.radians(a)):.1f}" '
                 f'y2="{cy - 120 + 300 * math.sin(math.radians(a)):.1f}" '
                 f'stroke="{WHITE}" stroke-width="1.6" stroke-opacity="0.16"/>')

    # brand + headline
    b.append('  <rect x="96" y="118" width="64" height="4" rx="2" fill="url(#gold)"/>')
    b.append("  " + text_el(96, 166, "JEWELSWELL MASTER ACADEMY", "#E5C378", 19, "700", spacing="3.2"))
    b.append("  " + text_el(96, 264, "Fine Jewelry Retail,", WHITE, 68, "800"))
    b.append("  " + text_el(96, 340, "Mastered End to End.", WHITE, 68, "800"))
    for i, line in enumerate(wrap(
            "A complete, source-verified curriculum for the selling floor, the "
            "client book, the bench and the P&L.", 52)):
        b.append("  " + text_el(96, 398 + i * 34, line, MUTED, 23, "400"))

    # statistics counters
    y = 520
    for i, (num, label) in enumerate(stats):
        x = 96 + i * 210
        b.append(f'  <rect x="{x}" y="{y}" width="184" height="118" rx="14" fill="#1E293B" '
                 f'fill-opacity="0.75" stroke="{accent}" stroke-width="1.6" stroke-opacity="0.55"/>')
        b.append("  " + text_el(x + 92, y + 62, num, WHITE, 46, "800", "middle"))
        b.append("  " + text_el(x + 92, y + 92, label, accent, 15, "700", "middle", spacing="1.6"))
    b.append(f'  <rect x="96" y="{y + 150}" width="614" height="1" fill="{"#334155"}"/>')
    b.append("  " + text_el(96, y + 184,
                            "Every figure below is generated from the curriculum itself.",
                            DIM, 15, "400"))
    return svg_doc(W, H, accent, "\n".join(b))


# -------------------------------------------------------------------- main
def curriculum_stats():
    courses_dir = os.path.join(ROOT, "courses")
    n_courses = n_articles = n_svgs = 0
    for name in sorted(os.listdir(courses_dir)):
        cdir = os.path.join(courses_dir, name)
        if not os.path.isdir(cdir):
            continue
        n_courses += 1
        adir = os.path.join(cdir, "articles")
        sdir = os.path.join(cdir, "assets")
        if os.path.isdir(adir):
            n_articles += len([f for f in os.listdir(adir) if f.endswith(".md")])
        if os.path.isdir(sdir):
            n_svgs += len([f for f in os.listdir(sdir) if f.endswith(".svg")])
    return n_courses, n_articles, n_svgs


def main():
    n_courses, n_articles, n_svgs = curriculum_stats()
    stats = [(str(n_courses), "COURSES"), (str(n_articles), "MODULES"),
             (str(n_svgs), "DIAGRAMS")]
    print(f"Curriculum: {n_courses} courses / {n_articles} modules / {n_svgs} diagrams")

    save(os.path.join(OUT, "hero-master-jewelswell-lms.svg"), build_hero(stats))
    print("Saved: assets/frontpage/hero-master-jewelswell-lms.svg")
    for c in COURSES:
        save(os.path.join(OUT, c["slug"] + ".svg"), build_cover(c))
        print(f"Saved: assets/frontpage/{c['slug']}.svg")
    print(f"\n{1 + len(COURSES)} frontpage assets written.")


if __name__ == "__main__":
    main()
