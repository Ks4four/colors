#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
strip.py — create a colour‑strip PNG from a palette JSON.

Examples
--------
python src/strip.py themes/arknights_kaltsit/kaltsit.json --out kaltsit_strip.png
python src/strip.py palette.json --vertical -w 40 -h 40 --dark
"""

from __future__ import annotations
from pathlib import Path
import argparse, json, sys, yaml
from typing import List, Dict
from PIL import Image
from rich.console import Console

console = Console(width=100)


# ------------------------------------------------------------------- #
# Helpers
# ------------------------------------------------------------------- #
def load_palette(path: Path) -> Dict[str, List[Dict[str, str]]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        console.print_exception()
        sys.exit(1)


def yaml_order(path: Path, theme: str | None) -> List[str]:
    data = yaml.safe_load(path.read_text()) if path.is_file() else {}
    if theme and theme in data:
        return data[theme]
    return data.get("default", [])


def heuristic_order(pal: dict, dark: bool) -> List[str]:
    sem = [c["Name"] for c in pal["Semantic"]]
    ui  = [c["Name"] for c in pal["UI"]]
    txt = [c["Name"] for c in pal["Text"]]
    ui_txt = ui + txt if dark else list(reversed(txt + ui))
    return sem + ui_txt


def build_strip(pal: dict, order: List[str], w: int, h: int, vertical: bool, out_png: Path) -> None:
    colours = {c["Name"]: c["Hex"] for grp in pal.values() for c in grp}
    total   = len(order)
    width, height = (w, h * total) if vertical else (w * total, h)

    strip = Image.new("RGB", (width, height), color="#000000")

    for idx, name in enumerate(order):
        if name not in colours:
            console.print(f"[yellow]warning:[/yellow] {name!r} not found in palette — skipped")
            continue
        block = Image.new("RGB", (w, h), colour := colours[name])
        pos   = (0, idx * h) if vertical else (idx * w, 0)
        strip.paste(block, pos)
        console.print(f"  • {name:<12} {colour}")

    strip.save(out_png)
    console.print(f"[green]Strip saved → {out_png}[/green]")


# ------------------------------------------------------------------- #
# CLI
# ------------------------------------------------------------------- #
def parse_args():
    ap = argparse.ArgumentParser(description="Generate a colour‑strip PNG.")
    ap.add_argument("palette", type=Path, help="Palette JSON.")
    ap.add_argument("-o", "--order-file", type=Path, default=Path("strip.yaml"),
                    help="YAML with one or more colour orders.")
    ap.add_argument("-T", "--theme", help="Which key inside the YAML to use.")
    ap.add_argument("-W", "--width",  type=int, default=20, help="Block width  (px).")
    ap.add_argument("-H", "--height", type=int, default=50, help="Block height (px).")
    ap.add_argument("--vertical", action="store_true", help="Vertical layout (default horizontal).")
    ap.add_argument("--dark", action="store_true", help="Treat theme as dark when auto‑ordering.")
    ap.add_argument("--out", type=Path, default=Path("strip.png"), help="Destination PNG.")
    return ap.parse_args()


def main() -> None:
    a  = parse_args()
    pal = load_palette(a.palette)

    order = yaml_order(a.order_file, a.theme)
    if not order:
        console.print("[cyan]Using heuristic order.[/cyan]")
        order = heuristic_order(pal, a.dark)

    build_strip(pal, order, a.width, a.height, a.vertical, a.out)


if __name__ == "__main__":
    main()
