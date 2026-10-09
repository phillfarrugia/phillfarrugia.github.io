#!/usr/bin/env python3
"""Fill in the EXIF data attributes for every photo in photography.html.

Reads each grid image's full-size file (data-full) with exiftool and writes
data-camera, data-lens, data-exposure, data-aperture and data-iso onto its
<img> tag, replacing any existing values. Safe to run repeatedly.

Usage: python3 scripts/update-photo-exif.py   (requires: brew install exiftool)
"""

import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "photography.html"
FIELDS = ["camera", "lens", "exposure", "aperture", "iso"]

# Friendlier names for camera models whose EXIF names are awkward
CAMERA_NAMES = {
    "NIKON Z 7_2": "Nikon Z7 II",
}


def camera(e):
    model = e.get("Model", "")
    return CAMERA_NAMES.get(model, model)


def lens(e):
    name = e.get("LensModel", "")
    # iPhone lenses read like "iPhone 13 Pro back triple camera 5.7mm f/1.5"
    if name.startswith("iPhone") and "FocalLengthIn35mmFormat" in e:
        return f"Main Camera {e['FocalLengthIn35mmFormat']}mm f/{e['FNumber']:g}"
    return name


def exposure(e):
    t = e.get("ExposureTime")
    if t is None:
        return ""
    return f"1/{round(1 / t)}s" if t < 1 else f"{t:g}s"


def aperture(e):
    return f"ƒ/{e['FNumber']:g}" if "FNumber" in e else ""


def iso(e):
    return f"ISO {e['ISO']}" if "ISO" in e else ""


def read_exif(paths):
    result = subprocess.run(
        ["exiftool", "-j", "-n", "-Model", "-LensModel", "-ExposureTime",
         "-FNumber", "-ISO", "-FocalLengthIn35mmFormat", *map(str, paths)],
        capture_output=True, text=True, cwd=ROOT,
    )
    if not result.stdout:
        sys.exit(result.stderr)
    return {Path(e["SourceFile"]).as_posix(): e for e in json.loads(result.stdout)}


def main():
    if not shutil.which("exiftool"):
        sys.exit("exiftool not found. Install it with: brew install exiftool")

    page = PAGE.read_text()
    tags = re.findall(r'<img [^>]*data-full="([^"]+)"[^>]*>', page)
    missing = [p for p in tags if not (ROOT / p).exists()]
    if missing:
        sys.exit("Missing photo files:\n  " + "\n  ".join(missing))

    exif = read_exif(tags)

    def update(match):
        tag, full = match.group(0), match.group(1)
        e = exif[full]
        values = {"camera": camera(e), "lens": lens(e), "exposure": exposure(e),
                  "aperture": aperture(e), "iso": iso(e)}
        tag = re.sub(r' data-(?:%s)="[^"]*"' % "|".join(FIELDS), "", tag)
        attrs = " ".join(f'data-{k}="{html.escape(v)}"' for k, v in values.items())
        print(f"{Path(full).name}: {' · '.join(v for v in values.values() if v)}")
        return tag.replace(f'data-full="{full}"', f'data-full="{full}" {attrs}', 1)

    PAGE.write_text(re.sub(r'<img [^>]*data-full="([^"]+)"[^>]*>', update, page))
    print(f"Updated {len(tags)} photos in {PAGE.name}")


if __name__ == "__main__":
    main()
