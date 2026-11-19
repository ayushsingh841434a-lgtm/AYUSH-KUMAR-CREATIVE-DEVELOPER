#!/usr/bin/env python3
"""Convert Ayush's photograph to the site's dark monochrome treatment.

Usage (from ayush-portfolio/):
    python tools/make-portrait.py /path/to/your-photo.jpg
    python tools/make-portrait.py /path/to/your-photo.jpg --out images/ayush-portrait.jpg
    python tools/make-portrait.py --placeholder

What it does — and only this:
  * converts to black and white (grayscale)
  * darkens the tone, raises contrast, adds a soft dark vignette
  * crops/resizes to a 4:5 portrait and saves as JPEG
What it does NOT do:
  * no face change, no reshaping, no beautifying, no replacement person
  * no identity alteration of any kind
A placeholder is created only when --placeholder is explicitly supplied.
Running without a source photo does not alter the existing portrait.
"""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def placeholder(out: Path):
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", (800, 1000), (18, 18, 16))
    d = ImageDraw.Draw(img)
    d.rectangle([40, 40, 760, 960], outline=(120, 115, 100), width=3)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 200)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 34)
    except Exception:
        font = ImageFont.load_default(); small = font
    d.text((400, 430), "AK", fill=(230, 225, 210), font=font, anchor="mm")
    d.text((400, 580), "YOUR PHOTOGRAPH HERE", fill=(160, 155, 140), font=small, anchor="mm")
    img.save(out, "JPEG", quality=88)
    print(f"Placeholder written to {out} — replace it with your real photograph.")

def convert(src: Path, out: Path):
    from PIL import Image, ImageDraw, ImageEnhance

    img = Image.open(src).convert("RGB")
    w, h = img.size
    target = 4 / 5
    if w / h > target:
        nw = int(h * target); x = (w - nw) // 2; img = img.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target); y = (h - nh) // 2; img = img.crop((0, y, w, y + nh))
    img = img.resize((800, 1000), Image.LANCZOS)
    img = img.convert("L").convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(1.18)
    img = ImageEnhance.Brightness(img).enhance(0.86)
    # Soft dark vignette
    vig = Image.new("L", img.size, 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-200, -150, 1000, 1150], fill=255)
    vig = vig.point(lambda p: int(255 - (255 - p) * 0.35))
    dark = Image.new("RGB", img.size, (0, 0, 0))
    img = Image.composite(img, dark, vig)
    img.save(out, "JPEG", quality=90)
    print(f"Dark monochrome portrait written to {out} from {src} (face untouched).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the portfolio's monochrome portrait asset.")
    parser.add_argument("source", nargs="?", type=Path, help="source photo to convert")
    parser.add_argument("--out", type=Path, default=ROOT / "images" / "ayush-portrait.jpg", help="output JPEG path")
    parser.add_argument("--placeholder", action="store_true", help="explicitly write the labelled placeholder")
    args = parser.parse_args()
    if args.placeholder and args.source:
        parser.error("--placeholder cannot be combined with a source photo")
    if args.placeholder:
        placeholder(args.out)
    elif args.source is None:
        parser.error("provide a source photo or use --placeholder; the existing portrait was not changed")
    else:
        convert(args.source, args.out)
