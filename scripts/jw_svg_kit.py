"""Shared SVG helpers for Jewelswell course media generation.

House style (matching the Wave 1 / Wave 2 assets already in the repo):
  - Slate navy gradient background (#0F172A -> #1E293B), rounded 16px frame
  - Gold accent gradient (#C5A059 -> #E5C378) for eyebrow/brand type
  - system-ui sans typography, white titles, #94A3B8 subtitles
"""

import os
import re

# ---------------------------------------------------------------- palette
BG_DARK = "#0F172A"
BG_MID = "#1E293B"
FRAME = "#334155"
WHITE = "#FFFFFF"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"
DIM = "#64748B"
GOLD = "#C5A059"
GOLD_LT = "#E5C378"

# Per-course accent colour, used for cover art and module diagrams.
COURSE_ACCENT = {
    "C1": "#38BDF8", "C2": "#F472B6", "C3": "#A78BFA", "C4": "#F87171",
    "C5": "#34D399", "C6": "#E5C378", "C7": "#FB923C", "C8": "#22D3EE",
    "C9": "#FBBF24", "C10": "#C084FC", "C11": "#60A5FA", "C12": "#4ADE80",
    "C13": "#2DD4BF", "C14": "#818CF8", "C16": "#7DD3FC", "C17": "#FB7185",
}


def esc(text):
    """Escape text for inclusion in SVG character data."""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def wrap(text, max_chars):
    """Greedy word wrap returning a list of lines."""
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if len(trial) <= max_chars:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_el(x, y, content, fill=TEXT, size=12, weight="400", anchor="start",
            spacing=None, opacity=None):
    attrs = [
        f'x="{x}"', f'y="{y}"', f'fill="{fill}"',
        'font-family="system-ui, sans-serif"', f'font-size="{size}"',
        f'font-weight="{weight}"',
    ]
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if opacity:
        attrs.append(f'fill-opacity="{opacity}"')
    return f'<text {" ".join(attrs)}>{esc(content)}</text>'


def wrapped_text(x, y, content, max_chars, line_height, **kw):
    """Emit several <text> elements for wrapped copy."""
    out = []
    for i, line in enumerate(wrap(content, max_chars)):
        out.append(text_el(x, y + i * line_height, line, **kw))
    return "\n".join(out)


def defs(accent, extra=""):
    return f'''  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_MID}"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{GOLD}"/>
      <stop offset="100%" stop-color="{GOLD_LT}"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
{extra}  </defs>'''


def frame(w, h):
    return (f'  <rect width="{w}" height="{h}" rx="16" fill="url(#bg)"/>\n'
            f'  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="14" '
            f'fill="none" stroke="{FRAME}" stroke-width="2"/>')


def svg_doc(w, h, accent, body, extra_defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="100%" height="100%" role="img">\n'
            f'{defs(accent, extra_defs)}\n\n{frame(w, h)}\n\n{body}\n</svg>\n')


def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


# ------------------------------------------------------- article parsing
BOILERPLATE = re.compile(
    r"^(why this module matters|key takeaways|practice exercise|"
    r"what you.ll (learn|be able)|summary|further reading|sources|"
    r"module (summary|objectives)|exercises?)\b", re.I)


def parse_article(path):
    """Pull the title, substantive H2 sections and key takeaways from an article."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    title, sections, takeaways = "", [], []
    current, collecting = None, False
    for line in lines:
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("## "):
            head = line[3:].strip()
            collecting = bool(re.match(r"^key takeaways", head, re.I))
            if not BOILERPLATE.match(head):
                current = {"head": head, "body": []}
                sections.append(current)
            else:
                current = None
        elif line.strip():
            if collecting and re.match(r"^\s*[-*]\s+", line):
                takeaways.append(re.sub(r"^\s*[-*]\s+", "", line).strip())
            elif current is not None and not line.startswith(("<", "|", "!")):
                current["body"].append(line.strip())

    for s in sections:
        s["lead"] = first_sentence(" ".join(s["body"]))
    return {"title": title, "sections": sections, "takeaways": takeaways}


def strip_md(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def first_sentence(text, limit=180):
    text = strip_md(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    out = parts[0] if parts else text
    if len(out) > limit:
        out = out[:limit].rsplit(" ", 1)[0] + "..."
    return out
