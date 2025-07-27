#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compute.py — Contrast matrices (WCAG) with optional CIEDE2000, single-file CLI.

Usage
-----
python src/compute.py themes/arknights_kaltsit/kaltsit.json -t 4.5 -s 2.5
python src/compute.py palette.json -t 4.5 7 -s 3 --semantic-self-th 3 4 --delta-e
python src/compute.py palette.json --no-color

Matrices
--------
1) Text vs UI
2) Semantic vs UI
3) Semantic vs Semantic

Outputs (written next to the input palette)
-------------------------------------------
- contrast-result.json
- base-contrast-result.json
- contrast-result.md

Notes
-----
- CLI and logs are English only.
- CIEDE2000 is optional (enable with --delta-e; requires `colormath`).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------- Rich UI ----------
from rich.console import Console
from rich.table import Table

console = Console(width=120)


# ---------- Colour math: WCAG ----------
def hex_to_rgb(h: str) -> Tuple[float, float, float]:
    h = h.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"Illegal HEX: {h}")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore


def srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: Tuple[float, float, float]) -> float:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex1: str, hex2: str) -> float:
    l1 = relative_luminance(hex_to_rgb(hex1))
    l2 = relative_luminance(hex_to_rgb(hex2))
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


# ---------- Optional ΔE2000 ----------
def try_delta_e():
    try:
        from colormath.color_objects import LabColor, sRGBColor  # type: ignore
        from colormath.color_conversions import convert_color  # type: ignore
        from colormath.color_diff import delta_e_cie2000  # type: ignore
    except Exception as exc:  # pragma: no cover
        return None, exc

    def _delta(hex1: str, hex2: str) -> float:
        c1 = sRGBColor.new_from_rgb_hex(hex1)
        c2 = sRGBColor.new_from_rgb_hex(hex2)
        return float(delta_e_cie2000(convert_color(c1, LabColor), convert_color(c2, LabColor)))

    return _delta, None


# ---------- Data helpers ----------
@dataclass
class Threshold:
    normal: Optional[float] = None
    strict: Optional[float] = None


def to_threshold(nums: Optional[List[float]]) -> Threshold:
    if not nums:
        return Threshold()
    if len(nums) == 1:
        return Threshold(normal=nums[0])
    return Threshold(normal=nums[0], strict=nums[1])


def cell_json(val: float, th: Threshold) -> Dict[str, object]:
    return {
        "ratio": round(val, 2),
        "pass_normal": None if th.normal is None else (val >= th.normal),
        "pass_strict": None if th.strict is None else (val >= th.strict),
    }


def build_grid(rows: List[Dict[str, str]], cols: List[Dict[str, str]], th: Threshold):
    grid: Dict[str, Dict[str, Dict[str, object]]] = {}
    for r in rows:
        rrow: Dict[str, Dict[str, object]] = {}
        for c in cols:
            rrow[c["Name"]] = cell_json(contrast_ratio(r["Hex"], c["Hex"]), th)
        grid[r["Name"]] = rrow
    return grid


def pretty_table(title: str, rows: List[Dict[str, str]], cols: List[Dict[str, str]], th: Threshold):
    table = Table(title=title, header_style="bold magenta")
    table.add_column("")  # row header
    for c in cols:
        table.add_column(c["Name"], justify="right")

    for r in rows:
        vals = []
        for c in cols:
            v = contrast_ratio(r["Hex"], c["Hex"])
            if th.normal is not None and v < th.normal:
                vals.append(f"[red]{v:.2f}[/red]")
            elif th.strict is not None and v >= th.strict:
                vals.append(f"[green]{v:.2f}[/green]")
            else:
                vals.append(f"{v:.2f}")
        table.add_row(r["Name"], *vals)
    console.print(table)


def write_markdown(out_path: Path, palette: dict):
    try:
        from tabulate import tabulate  # type: ignore
    except Exception:
        console.print("[yellow]tabulate is not installed; skipping Markdown output.[/yellow]")
        return

    def block(title: str, rows, cols):
        data = [[r["Name"]] + [f"{contrast_ratio(r['Hex'], c['Hex']):.2f}" for c in cols] for r in rows]
        return f"## {title}\n" + tabulate(data, headers=[''] + [c["Name"] for c in cols], tablefmt="github") + "\n"

    md_lines = [
        "# Contrast report",
        "",
        block("Text vs UI", palette["Text"], palette["UI"]),
        block("Semantic vs UI", palette["Semantic"], palette["UI"]),
        block("Semantic vs Semantic", palette["Semantic"], palette["Semantic"]),
    ]
    out_path.write_text("\n".join(md_lines), encoding="utf-8")
    console.print(f"[green]Markdown written → {out_path}[/green]")


# ---------- CLI ----------
def parse_args():
    p = argparse.ArgumentParser(description="Compute WCAG contrast matrices for a palette JSON.")
    p.add_argument("json_file", type=Path, help="Palette JSON file (must contain Semantic/Text/UI).")
    p.add_argument("-t", "--text-th", nargs="+", type=float, metavar=("NORMAL", "STRICT"),
                   help="Thresholds for Text vs UI.")
    p.add_argument("-s", "--semantic-th", nargs="+", type=float, metavar=("NORMAL", "STRICT"),
                   help="Thresholds for Semantic vs UI.")
    p.add_argument("-ss", "--semantic-self-th", nargs="+", type=float, metavar=("NORMAL", "STRICT"),
                   help="Thresholds for Semantic vs Semantic.")
    p.add_argument("--delta-e", action="store_true",
                   help="Also compute CIEDE2000 ΔE for Semantic pairs (requires `colormath`).")
    p.add_argument("--no-color", action="store_true", help="Disable coloured terminal output.")
    return p.parse_args()


def main():
    args = parse_args()
    console_no_color = Console(width=120, no_color=args.no_color)

    if not args.json_file.is_file():
        console_no_color.print(f"[red]File not found:[/red] {args.json_file}")
        sys.exit(1)

    palette = json.loads(args.json_file.read_text(encoding="utf-8"))
    semantic = palette.get("Semantic", [])
    text = palette.get("Text", [])
    ui = palette.get("UI", [])

    if not (semantic and text and ui):
        console_no_color.print("[red]Palette JSON must include Semantic/Text/UI arrays.[/red]")
        sys.exit(1)

    t_th = to_threshold(args.text_th)
    s_th = to_threshold(args.semantic_th)
    ss_th = to_threshold(args.semantic_self_th)

    # pretty preview in terminal (Rich)
    pretty_table("Text vs UI", text, ui, t_th)
    pretty_table("Semantic vs UI", semantic, ui, s_th)
    pretty_table("Semantic vs Semantic", semantic, semantic, ss_th)

    # Build JSON results
    results = {
        "meta": {"source": args.json_file.name},
        "matrices": {
            "Text_vs_UI": {"thresholds": t_th.__dict__, "rows": build_grid(text, ui, t_th)},
            "Semantic_vs_UI": {"thresholds": s_th.__dict__, "rows": build_grid(semantic, ui, s_th)},
            "Semantic_vs_Semantic": {
                "thresholds": ss_th.__dict__,
                "rows": build_grid(semantic, semantic, ss_th),
            },
        },
    }

    # Optional ΔE2000
    if args.delta_e:
        delta, err = try_delta_e()
        if err is not None or delta is None:
            console_no_color.print(
                "[red]colormath is not installed or failed to import; --delta-e is unavailable.[/red]"
            )
            sys.exit(1)
        # Build ΔE grid for Semantic pairs
        de_rows: Dict[str, Dict[str, float]] = {}
        names = [c["Name"] for c in semantic]
        hexes = {c["Name"]: c["Hex"] for c in semantic}
        for r in names:
            row = {}
            for c in names:
                row[c] = round(delta(hexes[r], hexes[c]), 2)
            de_rows[r] = row
        results["delta_e_ciede2000"] = {"rows": de_rows}

    # Write outputs (always, with fixed filenames) next to the palette file
    out_dir = args.json_file.parent
    out_full = out_dir / "contrast-matrix.json"
    out_full.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    console_no_color.print(f"[green]JSON written → {out_full}[/green]")

    # Base-only JSON
    base_entry = next((c for c in ui if c["Name"].lower() == "base"), None)
    if base_entry is None:
        console_no_color.print("[red]UI section must contain a 'Base' colour.[/red]")
        sys.exit(1)
    base_hex = base_entry["Hex"]

    def build_vs_base(group: List[Dict[str, str]], th: Threshold):
        return {g["Name"]: cell_json(contrast_ratio(g["Hex"], base_hex), th) for g in group}

    base_json = {
        "base": {"name": "Base", "hex": base_hex},
        "Text_vs_Base": {"thresholds": t_th.__dict__, "rows": build_vs_base(text, t_th)},
        "Semantic_vs_Base": {"thresholds": s_th.__dict__, "rows": build_vs_base(semantic, s_th)},
    }
    out_base = out_dir / "contrast-base.json"
    out_base.write_text(json.dumps(base_json, ensure_ascii=False, indent=2), encoding="utf-8")
    console_no_color.print(f"[green]JSON written → {out_base}[/green]")

    # Markdown
    out_md = out_dir / "contrast-report.md"
    write_markdown(out_md, palette)

    console_no_color.print("[bold green]All done.[/bold green]")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # pragma: no cover
        console.print_exception()
        sys.exit(1)
