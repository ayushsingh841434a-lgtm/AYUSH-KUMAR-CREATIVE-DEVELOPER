#!/usr/bin/env python3
"""Convert Ayush's photograph to the site's dark monochrome treatment.

Usage (from ayush-portfolio/):
    python3 tools/make-portrait.py /path/to/your-photo.jpg
    python3 tools/make-portrait.py /path/to/your-photo.jpg --out images/ayush-portrait.jpg

What it does — and only this:
  * converts to black and white (grayscale)
  * darkens the tone, raises contrast, adds a soft dark vignette
  * crops/resizes to a 4:5 portrait and saves as JPEG
What it does NOT do:
  * no face change, no reshaping, no beautifying, no replacement person
  * no identity alteration of any kind
If no argument is given, it creates the labelled monogram placeholder
currently used in the hero, so the site never shows a fake person.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent

def placeholder(out: Path):
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
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else ROOT / "images" / "ayush-portrait.jpg"
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        placeholder(out)
    else:
        convert(Path(args[0]), out)
