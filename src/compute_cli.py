#!/usr/bin/env python3
# src/compute_cli.py
import argparse, sys, json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from compute_lib import analyze_palette

def main() -> None:
    p = argparse.ArgumentParser(
        description="Contrast checker for a single palette JSON")
    p.add_argument("palette", type=Path, help="Path to palette JSON")
    p.add_argument("-t", "--text-th", type=float, default=4.5,
                   help="Text vs UI threshold (default 4.5)")
    p.add_argument("-s", "--semantic-th", type=float, default=3.0,
                   help="Semantic vs UI threshold (default 3.0)")
    p.add_argument("--delta-e", action="store_true",
                   help="Also compute CIEDE2000 matrix")
    args = p.parse_args()

    res = analyze_palette(args.palette, args.text_th,
                          args.semantic_th, args.delta_e)
    console = Console()
    ok = True
    for name, mat in res.items():
        console.rule(f"[bold cyan]{name}")
        table = Table(show_lines=True)
        cols = list(next(iter(mat.values())).keys())
        table.add_column("Row\\Col", style="bold")
        for c in cols: table.add_column(c, justify="center")
        for row, cells in mat.items():
            table.add_row(row, *[
                "[green]✔[/]" if v else "[red]✖[/]"
                for v in cells.values()
            ])
            if not all(cells.values()): ok = False
        console.print(table)

    if not ok:
        console.print("[red bold]Contrast check failed[/]")
        sys.exit(1)

if __name__ == "__main__":
    main()
