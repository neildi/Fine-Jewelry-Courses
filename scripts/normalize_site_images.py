"""Normalize the generated jewelswell.com course imagery.

Generated art arrives at 1672x941; the site needs a predictable 1600x900 (16:9).
This resizes losslessly-proportionally (no crop needed, the source is already
16:9), writes an optimized PNG in place, and emits a JPEG sibling for pages
where a 2-3 MB PNG hero would hurt Largest Contentful Paint.

Run from the repository root:  python3 scripts/normalize_site_images.py
"""

import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "site-images")
JPG = os.path.join(SRC, "jpg")

TARGET = (1600, 900)
JPEG_QUALITY = 86


def main():
    if not os.path.isdir(SRC):
        sys.exit(f"missing {SRC}")
    os.makedirs(JPG, exist_ok=True)

    rows = []
    for fn in sorted(f for f in os.listdir(SRC) if f.endswith(".png")):
        path = os.path.join(SRC, fn)
        im = Image.open(path).convert("RGB")
        before = os.path.getsize(path)

        if im.size != TARGET:
            im = im.resize(TARGET, Image.LANCZOS)
        im.save(path, "PNG", optimize=True)

        jpath = os.path.join(JPG, fn[:-4] + ".jpg")
        im.save(jpath, "JPEG", quality=JPEG_QUALITY, optimize=True,
                progressive=True, subsampling=0)

        rows.append((fn, before, os.path.getsize(path), os.path.getsize(jpath)))

    print(f"{'file':52} {'was':>8} {'png':>8} {'jpg':>8}")
    for fn, b, p, j in rows:
        print(f"{fn:52} {b // 1024:7}K {p // 1024:7}K {j // 1024:7}K")
    print(f"\n{len(rows)} images at {TARGET[0]}x{TARGET[1]}; "
          f"PNG total {sum(r[2] for r in rows) // 1024 // 1024} MB, "
          f"JPEG total {sum(r[3] for r in rows) // 1024 // 1024} MB")


if __name__ == "__main__":
    main()
