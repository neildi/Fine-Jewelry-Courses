"""Embed a <figure> block into every course article that has a diagram but no
figure yet, matching the markup convention used by the Wave 1 / Wave 2 embeds.

The figure is inserted after the opening section of the article, so the reader
meets the diagram once the module's purpose has been stated.

Idempotent: an article that already references its SVG is left alone.

Run from the repository root:
    python3 scripts/embed_coverage_figures.py [--dry-run]
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jw_svg_kit import esc, parse_article, strip_md  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES_DIR = os.path.join(ROOT, "courses")


def module_number(filename):
    m = re.match(r"M(\d+)", filename)
    return int(m.group(1)) if m else 0


def find_asset(cdir, mnum):
    sdir = os.path.join(COURSES_DIR, cdir, "assets")
    if not os.path.isdir(sdir):
        return None
    for f in sorted(os.listdir(sdir)):
        m = re.match(r"c\d+-m(\d+)-", f)
        if m and int(m.group(1)) == mnum and f.endswith(".svg"):
            return f
    return None


def caption(art, mnum):
    """Caption naming the frameworks the diagram actually lays out."""
    heads = [strip_md(s["head"]) for s in art["sections"]
             if not META_H2.match("## " + s["head"])][:3]
    tail = " · ".join(heads)
    if len(tail) > 150:
        tail = " · ".join(heads[:2])
    return (f"<strong>Figure {mnum}.1:</strong> {esc(strip_md(art['title']))} — "
            f"module framework at a glance: {esc(tail)}.")


def figure_block(svg, art, mnum):
    alt = esc(strip_md(art["title"]))
    return (f'<figure>\n'
            f'  <img src="../assets/{svg}" alt="{alt}" width="100%" />\n'
            f'  <figcaption>{caption(art, mnum)}</figcaption>\n'
            f'</figure>')


# Production-meta sections that must never host the figure: these are
# author-facing records (rubrics, change logs, fact-check tables), not content
# the learner reads.
META_H2 = re.compile(
    r"^##\s*(self-critique|critique|change ?log|rubric|fact.?check|"
    r"evidence table|media manifest|production|revision|source list|"
    r"verification|editorial)", re.I)


def insertion_index(lines):
    """Index just after the opening paragraph of the first learner-facing H2."""
    first_h2 = next((i for i, l in enumerate(lines)
                     if l.startswith("## ") and not META_H2.match(l)), None)
    if first_h2 is None:
        # no H2 at all: fall back to just after the title
        h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), -1)
        return h1 + 1
    i = first_h2 + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    # advance through the opening prose paragraph only - never into a table,
    # list, blockquote or existing HTML block
    while (i < len(lines) and lines[i].strip()
           and not lines[i].startswith(("#", "|", ">", "<", "- ", "* ", "!["))
           and not re.match(r"^\d+\.\s", lines[i])):
        i += 1
    return i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    embedded = skipped = missing = 0
    for cdir in sorted(os.listdir(COURSES_DIR)):
        adir = os.path.join(COURSES_DIR, cdir, "articles")
        if not os.path.isdir(adir):
            continue
        for fn in sorted(os.listdir(adir)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(adir, fn)
            with open(path, encoding="utf-8") as f:
                text = f.read()

            mnum = module_number(fn)
            svg = find_asset(cdir, mnum)
            if not svg:
                print(f"  !! no diagram for {cdir}/{fn}")
                missing += 1
                continue
            if "<figure" in text and svg in text:
                skipped += 1
                continue
            if "<figure" in text:
                skipped += 1
                continue

            art = parse_article(path)
            lines = text.split("\n")
            idx = insertion_index(lines)
            block = figure_block(svg, art, mnum)
            lines[idx:idx] = ["", block]
            out = "\n".join(lines)

            if args.dry_run:
                print(f"[dry-run] would embed {svg} -> {cdir}/{fn}")
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(out)
                print(f"Embedded {svg} -> {cdir}/{fn}")
            embedded += 1

    print(f"\nEmbedded {embedded}; already-figured {skipped}; missing diagrams {missing}.")


if __name__ == "__main__":
    main()
