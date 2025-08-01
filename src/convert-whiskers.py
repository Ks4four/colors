#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert-whiskers.py — Converts a palette JSON to a simplified, flavored format.

This script transforms a detailed palette JSON into a simple key-value
map of colors, nested under a specific flavor (e.g., mocha). The "Rationale"
field from the source is ignored.

The output file is automatically generated in the same directory as the input,
with a "-whiskers" suffix (e.g., input `palette.json` produces `palette-whiskers.json`).

Usage
-----
python src/convert-whiskers.py themes/arknights_rosmontis/palette.json -f latte
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

# Rich UI for styled console output, consistent with other project scripts
from rich.console import Console

console = Console(width=120)

# Centralized messages for easier maintenance and future i18n
MESSAGES = {
    "success": "[green]Transformation successful! File saved to:[/] {path}",
    "error_file_not_found": "[red]Error: Input file not found ->[/] {path}",
    "error_invalid_json": "[red]Error: Input file is not a valid JSON ->[/] {path}",
    "all_done": "[bold green]All done.[/bold green]",
}


def transform_palette(
    palette_data: Dict[str, List[Dict[str, str]]], flavor: str
) -> Dict[str, Dict[str, str]]:
    """
    Transforms the input palette data to the target flavored format.

    Args:
        palette_data: The original palette data, expected to have keys
                      like "Semantic", "Text", "UI".
        flavor: The flavor name (e.g., "mocha") to use as the root key
                in the output dictionary.

    Returns:
        The transformed palette dictionary.
    """
    # Using OrderedDict to maintain the key order from the original file
    transformed_palette = OrderedDict()

    for category_list in palette_data.values():
        for item in category_list:
            name_key = item.get("Name", "").lower()
            hex_value = item.get("Hex", "").lstrip("#")

            if name_key and hex_value:
                transformed_palette[name_key] = hex_value

    return {flavor: transformed_palette}


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(
        description="Converts a palette JSON to a simplified, flavored format.",
        epilog="Example: python src/convert-whiskers.py themes/arknights_rosmontis/palette.json -f mocha",
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the source palette JSON file.",
    )

    parser.add_argument(
        "--flavor",
        "-f",
        required=True,
        choices=["latte", "frappe", "macchiato", "mocha"],
        help="Required. The Catppuccin flavor to use for the output structure.",
    )

    return parser.parse_args()


def main() -> None:
    """
    Main execution flow of the script.
    """
    args = parse_args()
    input_path = args.input_file

    # Automatically determine the output path.
    # e.g., "palette.json" -> "palette-whiskers.json"
    output_path = input_path.with_name(
        f"{input_path.stem}-whiskers{input_path.suffix}"
    )

    try:
        # Load source palette from input file
        source_text = input_path.read_text(encoding="utf-8")
        # Use json.loads() to parse a string, not json.load()
        source_data = json.loads(source_text)

        # Perform the transformation
        transformed_data = transform_palette(source_data, args.flavor)

        # Write the result to the auto-generated output file
        # Ensure_ascii=False for i18n
        output_json_string = json.dumps(
            transformed_data, ensure_ascii=False
        )
        output_path.write_text(output_json_string, encoding="utf-8")

        console.print(MESSAGES["success"].format(path=output_path))
        console.print(MESSAGES["all_done"])

    except FileNotFoundError:
        console.print(MESSAGES["error_file_not_found"].format(path=input_path))
        sys.exit(1)
    except json.JSONDecodeError:
        console.print(MESSAGES["error_invalid_json"].format(path=input_path))
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Catch any unexpected errors and print a rich traceback
        console.print_exception()
        sys.exit(1)