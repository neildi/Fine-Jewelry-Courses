"""Rewrite the Tier 0 inventory inside courses/media-sources.md so it reflects
the current, complete state of the generated SVG library.

The section is regenerated from the filesystem, so the ledger can never drift
from what is actually committed. Everything outside the Tier 0 inventory
(licensing research, excluded sources) is preserved byte for byte.

Run from the repository root:  python3 scripts/update_media_ledger.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jw_svg_kit import parse_article, strip_md  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES_DIR = os.path.join(ROOT, "courses")
LEDGER = os.path.join(COURSES_DIR, "media-sources.md")

START = "### Inventory of"
END_RE = re.compile(r"^---\s*$", re.M)

FRONTPAGE_PURPOSE = {
    "hero-master-jewelswell-lms":
        ("Master homepage hero: 3D brilliant-cut diamond wireframe, Jewelswell Master "
         "Academy lockup, live curriculum counters", "Homepage hero banner"),
    "c1-cover-diamond-gemstone-fluency":
        ("Brilliant-cut diamond silhouette, 4Cs fluency badges, GIA report-reading tags",
         "C1 masterclass card"),
    "c2-cover-fine-jewelry-sales-conversation":
        ("Sales-conversation emblem, 90-second floor open, three closing protocols",
         "C2 masterclass card"),
    "c3-cover-clienteling-and-crm":
        ("VIP relationship node network, 2-2-2 outreach cadence, client-book tiering",
         "C3 masterclass card"),
    "c4-cover-store-security-loss-prevention":
        ("Vault dual-custody shield, showcase security rules, AML cash compliance",
         "C4 masterclass card"),
    "c5-cover-financing-credit-compliance":
        ("Retail credit installment emblem, 0% promotional terms, TILA disclosure",
         "C5 masterclass card"),
    "c6-cover-bridal-engagement-mastery":
        ("Platinum solitaire with matching pave band, couple journey, diamond origin",
         "C6 masterclass card"),
    "c7-cover-estate-antique-trade-in":
        ("Antique filigree frame, Victorian/Art Deco authentication, appraisal formulas",
         "C7 masterclass card"),
    "c8-cover-custom-design-repair-workflow":
        ("CAD wireframe resolving to a cast ring, bench repair SLAs, reveal ceremony",
         "C8 masterclass card"),
    "c9-cover-selling-high-ticket-compressed-time":
        ("High-velocity stopwatch, 3-hour trunk show and cruise-port closing dynamics",
         "C9 masterclass card"),
    "c10-cover-luxury-consumer-psychology-negotiation":
        ("High-net-worth status emblem, price anchoring, luxury negotiation capstone",
         "C10 masterclass card"),
    "c11-cover-running-the-store-operations":
        ("Daily operating-rhythm checklist, traffic-to-schedule staffing, showcase zoning",
         "C11 masterclass card"),
    "c12-cover-retail-kpis-reporting":
        ("Financial bar-chart analytics, GMROI calculation, store performance dashboards",
         "C12 masterclass card"),
    "c13-cover-hiring-coaching-performance":
        ("Leadership mentoring emblem, audition-based hiring, 30-day floor onboarding",
         "C13 masterclass card"),
    "c14-cover-multi-store-leadership":
        ("Regional multi-unit node network, unannounced store-visit audits, talent scaling",
         "C14 masterclass card"),
    "c16-cover-gia-diamonds-deep-dive":
        ("Carbon crystal-lattice octahedron, mantle genesis, ray tracing, lab-grown diagnostics",
         "C16 masterclass card"),
    "c17-cover-gia-colored-stones-deep-dive":
        ("Tri-gem cluster (ruby, sapphire, emerald, jade), inclusion forensics, treatment tiers",
         "C17 masterclass card"),
}


def module_number(name):
    m = re.search(r"-m(\d+)-", name) or re.match(r"M(\d+)", name)
    return int(m.group(1)) if m else 0


def collect():
    rows, per_course = [], []
    for cdir in sorted(os.listdir(COURSES_DIR),
                       key=lambda d: int(re.sub(r"\D", "", d.split("-")[0]) or 0)):
        full = os.path.join(COURSES_DIR, cdir)
        adir, sdir = os.path.join(full, "articles"), os.path.join(full, "assets")
        if not os.path.isdir(adir):
            continue
        code = cdir.split("-")[0]
        arts = {module_number(f): f for f in sorted(os.listdir(adir)) if f.endswith(".md")}
        svgs = sorted([f for f in os.listdir(sdir) if f.endswith(".svg")],
                      key=module_number) if os.path.isdir(sdir) else []

        covered = set()
        for svg in svgs:
            mnum = module_number(svg)
            art = arts.get(mnum)
            if not art:
                continue
            covered.add(mnum)
            parsed = parse_article(os.path.join(adir, art))
            title = strip_md(parsed["title"]) or art
            rows.append((code, f"courses/{cdir}/assets/{svg}", title, f"{code}/{art}"))
        per_course.append((code, cdir, len(arts), len(svgs), len(covered)))
    return rows, per_course


def build_section(rows, per_course):
    total_svgs = len(rows)
    total_arts = sum(p[2] for p in per_course)
    total_cov = sum(p[4] for p in per_course)
    pct = 100.0 * total_cov / total_arts if total_arts else 0

    out = [f"### Inventory of course-created SVG diagrams — {total_svgs} assets, "
           f"{total_cov}/{total_arts} modules covered ({pct:.0f}%)", "",
           "Regenerated from the filesystem by `scripts/update_media_ledger.py`; "
           "do not hand-edit this section.", "",
           "#### Coverage by course", "",
           "| Course | Modules | Diagrams | Modules with a diagram | Coverage |",
           "|---|---|---|---|---|"]
    for code, cdir, n_art, n_svg, n_cov in per_course:
        c = 100.0 * n_cov / n_art if n_art else 0
        out.append(f"| **{code}** | {n_art} | {n_svg} | {n_cov} | {c:.0f}% |")
    out.append(f"| **Total** | **{total_arts}** | **{total_svgs}** | **{total_cov}** | "
               f"**{pct:.0f}%** |")

    out += ["", "#### Frontpage assets (16:9, 1600x900)", "",
            "| Asset File | Placement | Focal imagery |", "|---|---|---|"]
    fdir = os.path.join(ROOT, "assets", "frontpage")
    if os.path.isdir(fdir):
        order = list(FRONTPAGE_PURPOSE)
        for name in sorted([f[:-4] for f in os.listdir(fdir) if f.endswith(".svg")],
                           key=lambda n: order.index(n) if n in order else 99):
            purpose, placement = FRONTPAGE_PURPOSE.get(name, ("—", "—"))
            out.append(f"| `assets/frontpage/{name}.svg` | {placement} | {purpose} |")

    out += ["", "#### Module diagrams", "",
            "| Course | Asset File | Module | Embedded target article |", "|---|---|---|---|"]
    for code, path, title, art in rows:
        out.append(f"| **{code}** | `{path}` | {title} | `{art}` |")
    out.append("")
    return "\n".join(out)


def main():
    with open(LEDGER, encoding="utf-8") as f:
        text = f.read()

    start = text.index(START)
    m = END_RE.search(text, start)
    end = m.start() if m else len(text)

    rows, per_course = collect()
    new = build_section(rows, per_course)
    out = text[:start] + new + "\n" + text[end:]

    # keep the standing-record preamble honest about scale
    out = out.replace("130-article catalog", f"{sum(p[2] for p in per_course)}-article catalog")

    with open(LEDGER, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Ledger updated: {len(rows)} module diagrams, "
          f"{sum(p[4] for p in per_course)}/{sum(p[2] for p in per_course)} modules covered.")


if __name__ == "__main__":
    main()
