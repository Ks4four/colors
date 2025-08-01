#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert-whiskers.py — Converts a palette JSON to a simplified, flavored format.

This script transforms a detailed palette JSON into a simple key-value
map of colors. It reads the target flavor (e.g., "mocha", "latte") from a
top-level "flavor" key within the source JSON itself.

The output file is automatically generated in the same directory as the input,
with a "-whiskers" suffix (e.g., input `palette.json` produces `palette-whiskers.json`)
and will overwrite any existing file.

Usage
-----
# To process a single file:
python src/convert-whiskers.py themes/arknights_rosmontis/palette.json

# To process all themes in batch (PowerShell):
# Get-ChildItem -Path themes -Recurse -Filter palette.json | ForEach-Object {
#   python src/convert-whiskers.py $_.FullName
# }
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

from rich.console import Console

console = Console(width=120)


def transform_palette(
    palette_data: Dict[str, List[Dict[str, str]]], flavor: str
) -> Dict[str, Dict[str, str]]:
    """Transforms the input palette data to the target flavored format."""
    transformed = OrderedDict()

    # The 'flavor' key is metadata, not a color category,
    # so it must be skipped during the color transformation.
    for category_name, category_list in palette_data.items():
        if category_name == "flavor":
            continue

        if isinstance(category_list, list):
            for item in category_list:
                name_key = item.get("Name", "").lower()
                hex_value = item.get("Hex", "").lstrip("#")

                if name_key and hex_value:
                    transformed[name_key] = hex_value

    return {flavor: transformed}


def parse_args() -> argparse.Namespace:
    """Parses command-line arguments for the script."""
    parser = argparse.ArgumentParser(
        description="Converts a palette JSON to a simplified, flavored format.",
        epilog="Example: python src/convert-whiskers.py themes/arknights_rosmontis/palette.json",
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the source palette JSON file (must contain a 'flavor' key).",
    )

    # The --flavor argument is no longer needed because the flavor
    # is now read directly from the JSON file itself.
    return parser.parse_args()


def main() -> None:
    """Main execution flow of the script."""
    args = parse_args()
    input_path = args.input_file

    if not input_path.is_file():
        console.print(f"[red]File not found:[/red] {input_path}")
        sys.exit(1)

    # The output path is derived from the input path, ensuring
    # the generated file is placed alongside its source.
    output_path = input_path.with_name(f"{input_path.stem}-whiskers{input_path.suffix}")

    try:
        source_data = json.loads(input_path.read_text(encoding="utf-8"))

        # The core logic of this approach: extract the flavor from the
        # source data rather than a command-line argument.
        flavor = source_data.get("flavor")
        if not flavor or not isinstance(flavor, str):
            console.print(
                f"[red]Error:[/red] 'flavor' key not found or invalid in {input_path}"
            )
            sys.exit(1)

        transformed_data = transform_palette(source_data, flavor)

        # Output is a single-line JSON. `ensure_ascii=False` correctly
        # handles any non-ASCII characters in color names.
        output_json_string = json.dumps(transformed_data, ensure_ascii=False)

        # `write_text` will automatically overwrite the destination file if it exists.
        output_path.write_text(output_json_string, encoding="utf-8")

        console.print(f"[green]Whiskers file created →[/green] {output_path}")

    except json.JSONDecodeError:
        console.print(
            f"[red]Error:[/red] Input file is not a valid JSON → {input_path}"
        )
        sys.exit(1)
    except Exception:
        # Catch any other unexpected errors and print a rich traceback.
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
