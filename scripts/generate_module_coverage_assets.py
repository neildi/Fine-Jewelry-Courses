"""Generate a pedagogical SVG diagram for every course module that does not
already have one, bringing the curriculum to 100% visual coverage.

Each diagram is built from the article's own structure: its title, its
substantive H2 sections (with the opening sentence of each as the caption)
and its Key Takeaways bullets. Nothing is invented - if the article does not
say it, it does not appear in the figure.

Existing Wave 1 / Wave 2 assets are never overwritten.

Run from the repository root:
    python3 scripts/generate_module_coverage_assets.py [--force] [--only C9]
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jw_svg_kit import (  # noqa: E402
    COURSE_ACCENT, DIM, FRAME, MUTED, TEXT, WHITE,
    first_sentence, parse_article, save, strip_md, svg_doc, text_el, wrap,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES_DIR = os.path.join(ROOT, "courses")

W = 1100
STOPWORDS = {"the", "a", "an", "of", "and", "or", "to", "in", "for", "on",
             "with", "your", "you", "that", "this", "is", "it", "at", "as",
             "what", "why", "how", "when", "from", "not", "but"}


# ------------------------------------------------------------------ naming
def course_code(dirname):
    return dirname.split("-")[0]


def module_number(filename):
    m = re.match(r"M(\d+)", filename)
    return int(m.group(1)) if m else 0


def slugify(text, max_words=6):
    words = [w for w in re.sub(r"[^a-z0-9\s-]", "", strip_md(text).lower()).split()
             if w not in STOPWORDS]
    return "-".join(words[:max_words]) or "overview"


def asset_name(code, mnum, title):
    return f"{code.lower()}-m{mnum:02d}-{slugify(title)}.svg"


def figure_kicker(title):
    """A short, plain descriptor used in the figure eyebrow."""
    t = title.lower()
    pairs = [
        (("capstone",), "CAPSTONE WALKTHROUGH"),
        (("checklist", "procedure", "sop", "protocol"), "OPERATING PROCEDURE"),
        (("kpi", "metric", "report", "dashboard", "math", "formula"), "MEASUREMENT FRAMEWORK"),
        (("compliance", "legal", "law", "disclosure", "regulation"), "COMPLIANCE FRAMEWORK"),
        (("script", "conversation", "objection", "ask", "close", "pitch"), "CONVERSATION MAP"),
        (("workflow", "process", "pipeline", "intake", "turnaround"), "WORKFLOW MAP"),
        (("coaching", "hiring", "interview", "onboarding", "review"), "PEOPLE PRACTICE"),
        (("security", "theft", "fraud", "risk", "loss"), "RISK CONTROL"),
    ]
    for keys, label in pairs:
        if any(k in t for k in keys):
            return label
    return "MODULE FRAMEWORK"


# ----------------------------------------------------------------- drawing
def header(code, mnum, title, kicker, accent):
    out = [f'  <g transform="translate(46, 34)">']
    kw = 22 + len(kicker) * 7.4
    out.append(f'    <rect x="0" y="0" width="{kw:.0f}" height="24" rx="12" '
               f'fill="{accent}" fill-opacity="0.18"/>')
    out.append("    " + text_el(kw / 2, 16, kicker, accent, 11, "700", "middle", spacing="1"))
    out.append("    " + text_el(W - 92, 16, f"{code} · MODULE {mnum:02d}", DIM, 11, "700",
                                "end", spacing="1.2"))
    y = 52
    for line in wrap(title, 62):
        out.append("    " + text_el(0, y, line, WHITE, 22, "700"))
        y += 28
    out.append("  </g>")
    return "\n".join(out), 34 + y + 2


def card(x, y, w, h, n, head, lead, accent, compact=False):
    """A numbered section card."""
    hs = 13 if not compact else 12
    out = [f'  <g transform="translate({x}, {y})">']
    out.append(f'    <rect width="{w}" height="{h}" rx="10" fill="#1E293B" '
               f'stroke="{accent}" stroke-width="1.4" stroke-opacity="0.85"/>')
    out.append(f'    <rect width="4" height="{h}" rx="2" fill="{accent}"/>')
    out.append(f'    <circle cx="32" cy="30" r="14" fill="{accent}" fill-opacity="0.22"/>')
    out.append("    " + text_el(32, 35, str(n), accent, 13, "800", "middle"))

    tx, tw = 56, int((w - 72) / (hs * 0.50))
    hy = 27
    for line in wrap(head, tw)[:2]:
        out.append("    " + text_el(tx, hy, line, WHITE, hs, "700"))
        hy += 17
    if lead:
        ly = hy + 8
        body_w = int((w - 44) / 5.9)
        avail = int((h - ly - 12) / 15)
        lines = wrap(lead, body_w)
        if len(lines) > avail and avail > 0:
            lines = lines[:avail]
            lines[-1] = lines[-1].rstrip(" .,;") + "..."
        for line in lines:
            out.append("    " + text_el(22, ly, line, MUTED, 11, "400"))
            ly += 15
    out.append("  </g>")
    return "\n".join(out)


def takeaway_band(x, y, w, items, accent):
    h = 34 + len(items) * 19
    out = [f'  <g transform="translate({x}, {y})">']
    out.append(f'    <rect width="{w}" height="{h}" rx="10" fill="#0F172A" '
               f'stroke="{FRAME}" stroke-width="1.4"/>')
    out.append("    " + text_el(20, 24, "KEY TAKEAWAYS", accent, 11, "700", spacing="1.4"))
    ty = 46
    for it in items:
        out.append(f'    <circle cx="26" cy="{ty - 4}" r="3.2" fill="{accent}"/>')
        out.append("    " + text_el(40, ty, it, TEXT, 11.5, "400"))
        ty += 19
    out.append("  </g>")
    return "\n".join(out), h


def build_diagram(code, mnum, art):
    accent = COURSE_ACCENT[code]
    title = art["title"]
    sections = art["sections"][:8]
    kicker = figure_kicker(title)

    hdr, y = header(code, mnum, title, kicker, accent)
    body = [hdr]
    y += 14

    n = len(sections)
    cols = 2 if n <= 8 else 2
    gap, pad = 18, 46
    cw = int((W - pad * 2 - gap) / cols)
    rows = (n + cols - 1) // cols
    compact = rows >= 4
    ch = 132 if rows <= 2 else (118 if rows == 3 else 104)

    lead_chars = 150 if not compact else 110
    for i, s in enumerate(sections):
        cx_ = pad + (i % cols) * (cw + gap)
        cy_ = y + (i // cols) * (ch + gap)
        lead = first_sentence(" ".join(s["body"]), lead_chars)
        body.append(card(cx_, cy_, cw, ch, i + 1, strip_md(s["head"]), lead, accent, compact))

    y += rows * (ch + gap)

    takeaways = [first_sentence(t, 120) for t in art["takeaways"][:4]]
    band_h = 0
    if takeaways:
        band, band_h = takeaway_band(pad, y, W - pad * 2, takeaways, accent)
        body.append(band)
        y += band_h

    y += 34
    body.append("  " + text_el(pad, y - 12, "JEWELSWELL MASTER ACADEMY", "#C5A059", 10,
                               "700", spacing="1.6"))
    body.append("  " + text_el(W - pad, y - 12,
                               "Generated from the module article — headings and takeaways verbatim.",
                               DIM, 10, "400", "end"))
    H = int(y + 8)
    return svg_doc(W, H, accent, "\n".join(body))


# -------------------------------------------------------------------- main
def iter_modules():
    for cdir in sorted(os.listdir(COURSES_DIR)):
        full = os.path.join(COURSES_DIR, cdir)
        adir = os.path.join(full, "articles")
        if not os.path.isdir(adir):
            continue
        code = course_code(cdir)
        for fn in sorted(os.listdir(adir)):
            if fn.endswith(".md"):
                yield code, cdir, fn, os.path.join(adir, fn)


def existing_assets(cdir):
    sdir = os.path.join(COURSES_DIR, cdir, "assets")
    if not os.path.isdir(sdir):
        return {}
    out = {}
    for f in os.listdir(sdir):
        m = re.match(r"c(\d+)-m(\d+)-", f)
        if m and f.endswith(".svg"):
            out.setdefault(int(m.group(2)), []).append(f)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="regenerate even if a diagram exists")
    ap.add_argument("--only", help="limit to one course code, e.g. C9")
    args = ap.parse_args()

    created, skipped = 0, 0
    for code, cdir, fn, path in iter_modules():
        if args.only and code.upper() != args.only.upper():
            continue
        have = existing_assets(cdir)
        mnum = module_number(fn)
        if mnum in have and not args.force:
            skipped += 1
            continue
        art = parse_article(path)
        if not art["title"] or not art["sections"]:
            print(f"  !! unparseable: {path}")
            continue
        out = os.path.join(COURSES_DIR, cdir, "assets",
                           asset_name(code, mnum, art["title"]))
        save(out, build_diagram(code, mnum, art))
        created += 1
        print(f"Saved: {os.path.relpath(out, ROOT)}")

    print(f"\nCreated {created} new diagrams; left {skipped} existing assets untouched.")


if __name__ == "__main__":
    main()
