# src/compute_lib.py
from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# ---------- Contrast ---------- #
def hex_to_rgb_float(h: str) -> Tuple[float, float, float]:
    h = h.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    return r, g, b

def srgb_luminance(rgb: Tuple[float, float, float]) -> float:
    def f(c: float):  # sRGB → Linear
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(f, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(hex1: str, hex2: str) -> float:
    l1, l2 = srgb_luminance(hex_to_rgb_float(hex1)), srgb_luminance(hex_to_rgb_float(hex2))
    return (max(l1, l2) + .05) / (min(l1, l2) + .05)

# ---------- ΔE (optional) ---------- #
def delta_e(hex1: str, hex2: str) -> float:
    rgb1 = sRGBColor(*hex_to_rgb_float(hex1))
    rgb2 = sRGBColor(*hex_to_rgb_float(hex2))
    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)
    return lab1.delta_e(lab2, mode='cie2000')  # needs colormath

# ---------- Public API ---------- #
def analyze_palette(
    palette_json: Path,
    text_th: float,
    semantic_th: float,
    compute_de: bool = False,
) -> Dict[str, Dict]:
    import json
    data = json.loads(palette_json.read_text('utf-8'))
    semantic, text, ui = data['Semantic'], data['Text'], data['UI']

    def matrix(rows, cols, th):
        return {
            r['Name']: {
                c['Name']: contrast_ratio(r['Hex'], c['Hex']) >= th
                for c in cols
            }
            for r in rows
        }

    result = {
        'text_vs_ui':  matrix(text, ui, text_th),
        'semantic_vs_ui': matrix(semantic, ui, semantic_th),
    }
    if compute_de:
        result['semantic_delta_e'] = {
            a['Name']: {
                b['Name']: delta_e(a['Hex'], b['Hex'])
                for b in semantic
            } for a in semantic
        }
    return result
