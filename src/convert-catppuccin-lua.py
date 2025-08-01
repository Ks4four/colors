#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_catppuccin.py — JSON → Catppuccin Neovim snippet.

Example
-------
python src/convert_catppuccin.py themes/arknights_kaltsit/kaltsit.json --flavor frappe
"""

from __future__ import annotations
from pathlib import Path
import argparse, json, sys
from rich.console import Console

console = Console()


def build_snippet(flat: dict[str, str], flavor: str) -> str:
    body = "\n        ".join(f'{k.lower():<9}= "{v}",' for k, v in flat.items())
    return (
        'require("catppuccin").setup {\n'
        "    color_overrides = {\n"
        f"        {flavor} = {{\n"
        f"        {body}\n"
        "        },\n"
        "    }\n"
        "}"
    )


def flatten_palette(pal: dict) -> dict[str, str]:
    return {c["Name"]: c["Hex"] for group in pal.values() for c in group}


def parse_args():
    ap = argparse.ArgumentParser(description="Convert palette → Catppuccin override snippet.")
    ap.add_argument("palette", type=Path, help="Palette JSON.")
    ap.add_argument("-f", "--flavor", choices=("latte", "frappe", "macchiato", "mocha"),
                    default="latte", help="Catppuccin flavor to override.")
    ap.add_argument("--out", type=Path, help="Write snippet to file (stdout if omitted).")
    return ap.parse_args()


def main() -> None:
    a = parse_args()
    try:
        pal  = json.loads(a.palette.read_text(encoding="utf-8"))
        flat = flatten_palette(pal)
        lua  = build_snippet(flat, a.flavor)

        if a.out:
            a.out.write_text(lua, encoding="utf-8")
            console.print(f"[green]Snippet saved → {a.out}[/green]")
        else:
            print(lua)
    except Exception:
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
