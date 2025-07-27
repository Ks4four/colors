#!/usr/bin/env python3
# src/strip.py
import argparse, json, sys
from PIL import Image
from pathlib import Path

SEMANTIC_ORDER = [
    "Rosewater","Flamingo","Pink","Mauve","Red","Maroon",
    "Peach","Yellow","Green","Teal","Sky","Sapphire","Blue","Lavender"
]
TEXT_ORDER = ["Text","Subtext0","Subtext1"]
UI_ORDER_LIGHT = [
    "Base","Mantle","Crust",
    "Surface0","Surface1","Surface2",
    "Overlay0","Overlay1","Overlay2"
]
UI_ORDER_DARK = list(reversed(UI_ORDER_LIGHT))

def build_order(theme_type: str):
    ui_part = UI_ORDER_DARK if theme_type == "dark" else UI_ORDER_LIGHT
    return SEMANTIC_ORDER + TEXT_ORDER + ui_part

def load_colors(path: Path):
    data = json.loads(path.read_text('utf-8'))
    colors = {d['Name']: d['Hex'] for group in data.values() for d in group}
    return colors

def generate_strip(colors, order, w, h, dest):
    img = Image.new("RGB", (w * len(order), h))
    for i, name in enumerate(order):
        color = colors.get(name)
        if not color:
            print(f"[warn] {name} not found, skip")
            continue
        block = Image.new("RGB", (w, h), color)
        img.paste(block, (i * w, 0))
    img.save(dest)
    print(f"✓ saved {dest}")

def main():
    ap = argparse.ArgumentParser("Generate color strip")
    ap.add_argument("palette", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=Path("strip.png"))
    ap.add_argument("--width", type=int, default=20)
    ap.add_argument("--height", type=int, default=50)
    ap.add_argument("--theme-type", choices=["light","dark"], default="light",
                    help="decides UI order")
    args = ap.parse_args()

    generate_strip(
        load_colors(args.palette),
        build_order(args.theme_type),
        args.width, args.height, args.out
    )

if __name__ == "__main__":
    main()
