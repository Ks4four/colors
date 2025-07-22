#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI
----
python compute.py palette.json
python compute.py palette.json --text-th 4.5 7 --semantic-th 3 --md
python compute.py palette.json -t 4.5 -s 3.0 4.5 --no-color

功能
----
1. 读取包含 Semantic / Text / UI 三组颜色的 JSON（忽略 Rationale）。
2. 根据 WCAG 2.1 相对亮度公式计算对比度。
3. 生成：
   - 终端肉眼检查矩阵（ANSI 颜色：红<普通阈值，绿≥严格阈值）。
   - <stem>-contrast.json          # 完整矩阵 JSON
   - <stem>-base-contrast.json     # 仅所有颜色 vs Base 的 JSON
   - (可选) <stem>-contrast.md     # Markdown 表格（--md 开启）

阈值
----
- Text vs UI：--text-th <normal> [strict]
- Semantic vs UI：--semantic-th <normal> [strict]
  （只给一个数字时表示只有普通阈值；不给则该矩阵无阈值）
- JSON 里每个 cell 的结构固定：{"ratio": 5.1, "pass_normal": true|null, "pass_strict": false|null}

其它
----
--no-color 关闭终端 ANSI 颜色。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# ---------------- Color math (WCAG 2.1) ----------------
def hex_to_rgb(hex_code: str) -> Tuple[float, float, float]:
    h = hex_code.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"非法 HEX: {hex_code}")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore


def srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: Tuple[float, float, float]) -> float:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex1: str, hex2: str) -> float:
    l1 = relative_luminance(hex_to_rgb(hex1))
    l2 = relative_luminance(hex_to_rgb(hex2))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


# ---------------- ANSI helpers ----------------
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def style_ratio(ratio: float,
                normal: Optional[float],
                strict: Optional[float],
                use_color: bool) -> str:
    s = f"{ratio:>10.2f}"
    if not use_color or normal is None:
        return s
    if ratio < normal:
        return f"{RED}{s}{RESET}"
    if strict is not None and ratio >= strict:
        return f"{GREEN}{s}{RESET}"
    return s


def add_cell_json(ratio: float,
                  normal: Optional[float],
                  strict: Optional[float]) -> Dict[str, object]:
    return {
        "ratio": round(ratio, 2),
        "pass_normal": (ratio >= normal) if normal is not None else None,
        "pass_strict": (ratio >= strict) if strict is not None else None,
    }


# ---------------- Markdown helpers ----------------
def md_table(title: str,
             rows: List[Dict[str, str]],
             cols: List[Dict[str, str]],
             normal: Optional[float],
             strict: Optional[float]) -> str:
    """生成一个矩阵的 Markdown 表格字符串"""
    header = [""] + [c["Name"] for c in cols]
    lines = []
    lines.append(f"### {title}")
    if normal is None:
        lines.append("阈值：未设置")
    elif strict is None:
        lines.append(f"阈值：普通 ≥ **{normal}** : 1")
    else:
        lines.append(f"阈值：普通 ≥ **{normal}** : 1；严格 ≥ **{strict}** : 1")

    # 表头
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")

    for r in rows:
        row_vals = [r["Name"]]
        for c in cols:
            ratio = contrast_ratio(r["Hex"], c["Hex"])
            cell = f"{ratio:.2f}"
            # 在 MD 中无法用 ANSI，使用符号标记
            mark = ""
            if normal is not None and ratio < normal:
                mark = " ❌"
            elif strict is not None and ratio >= strict:
                mark = " ✅"
            row_vals.append(cell + mark)
        lines.append("| " + " | ".join(row_vals) + " |")
    lines.append("")  # 结尾空行
    return "\n".join(lines)


# ---------------- Core printing & json build ----------------
def print_matrix(label: str,
                 rows: List[Dict[str, str]],
                 cols: List[Dict[str, str]],
                 normal: Optional[float],
                 strict: Optional[float],
                 use_color: bool) -> Dict[str, Dict[str, Dict[str, object]]]:
    print(f"\n{label}")
    if normal is None:
        print("阈值：未设置")
    else:
        if strict is None:
            print(f"阈值：普通 ≥ {normal}:1（无严格阈值）")
        else:
            print(f"阈值：普通 ≥ {normal}:1；严格 ≥ {strict}:1")

    col_names = [c["Name"] for c in cols]
    print(" " * 12 + "  ".join(f"{n:>10}" for n in col_names))

    matrix_json: Dict[str, Dict[str, Dict[str, object]]] = {}
    for r in rows:
        r_name = r["Name"]
        styled = []
        row_json: Dict[str, Dict[str, object]] = {}
        for c in cols:
            ratio = contrast_ratio(r["Hex"], c["Hex"])
            styled.append(style_ratio(ratio, normal, strict, use_color))
            row_json[c["Name"]] = add_cell_json(ratio, normal, strict)
        print(f"{r_name:<10}  " + "  ".join(styled))
        matrix_json[r_name] = row_json
    return matrix_json


def build_base_json(base_hex: str,
                    group: List[Dict[str, str]],
                    normal: Optional[float],
                    strict: Optional[float]) -> Dict[str, Dict[str, object]]:
    res: Dict[str, Dict[str, object]] = {}
    for item in group:
        ratio = contrast_ratio(item["Hex"], base_hex)
        res[item["Name"]] = add_cell_json(ratio, normal, strict)
    return res


# ---------------- Argparse ----------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute contrast matrices (WCAG 2.1) for a palette JSON."
    )
    parser.add_argument("json_file", type=Path, help="输入的颜色 JSON 文件")

    # 阈值：可给 0/1/2 个数字
    parser.add_argument(
        "-t", "--text-th", metavar="N", type=float, nargs="+",
        help="Text vs UI 阈值：<normal> [strict]"
    )
    parser.add_argument(
        "-s", "--semantic-th", metavar="N", type=float, nargs="+",
        help="Semantic vs UI 阈值：<normal> [strict]"
    )

    parser.add_argument("--md", action="store_true",
                        help="同时输出 Markdown 表格，并写入 <stem>-contrast.md")
    parser.add_argument("--no-color", action="store_true",
                        help="关闭终端彩色输出")
    return parser.parse_args()


def nums_to_threshold(nums: Optional[List[float]]) -> Tuple[Optional[float], Optional[float]]:
    if not nums:
        return None, None
    if len(nums) == 1:
        return nums[0], None
    # 取前两个，多余忽略
    return nums[0], nums[1]


# ---------------- Main ----------------
def main() -> None:
    args = parse_args()

    # 读取 JSON
    if not args.json_file.is_file():
        print(f"文件不存在: {args.json_file}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    semantic = data.get("Semantic", [])
    text = data.get("Text", [])
    ui = data.get("UI", [])
    if not (semantic and text and ui):
        print("JSON 中必须包含 Semantic / Text / UI 三组颜色", file=sys.stderr)
        sys.exit(1)

    text_norm, text_strict = nums_to_threshold(args.text_th)
    sem_norm, sem_strict = nums_to_threshold(args.semantic_th)

    use_color = not args.no_color

    # 打印矩阵
    text_vs_ui_json = print_matrix("Text vs UI", text, ui, text_norm, text_strict, use_color)
    semantic_vs_ui_json = print_matrix("Semantic vs UI", semantic, ui, sem_norm, sem_strict, use_color)

    # 写完整矩阵 JSON
    full_json = {
        "matrices": {
            "Text_vs_UI": {
                "thresholds": {"normal": text_norm, "strict": text_strict},
                "rows": text_vs_ui_json,
            },
            "Semantic_vs_UI": {
                "thresholds": {"normal": sem_norm, "strict": sem_strict},
                "rows": semantic_vs_ui_json,
            },
        }
    }
    out_full = args.json_file.with_name(args.json_file.stem + "-contrast.json")
    out_full.write_text(json.dumps(full_json, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n已生成结果文件: {out_full}")

    # Base-only JSON
    base = next((c for c in ui if c["Name"].lower() == "base"), None)
    if base is None:
        print("UI 组中未找到名为 Base 的颜色", file=sys.stderr)
        sys.exit(1)
    base_hex = base["Hex"]

    base_json = {
        "base": {"name": "Base", "hex": base_hex},
        "Text_vs_Base": {
            "thresholds": {"normal": text_norm, "strict": text_strict},
            "rows": build_base_json(base_hex, text, text_norm, text_strict),
        },
        "Semantic_vs_Base": {
            "thresholds": {"normal": sem_norm, "strict": sem_strict},
            "rows": build_base_json(base_hex, semantic, sem_norm, sem_strict),
        },
    }
    out_base = args.json_file.with_name(args.json_file.stem + "-base-contrast.json")
    out_base.write_text(json.dumps(base_json, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已生成结果文件: {out_base}")

    # Markdown
    if args.md:
        md_parts = []
        md_parts.append(f"# 对比度结果：{args.json_file.name}\n")
        # Text vs UI
        md_parts.append(md_table("Text vs UI", text, ui, text_norm, text_strict))
        # Semantic vs UI
        md_parts.append(md_table("Semantic vs UI", semantic, ui, sem_norm, sem_strict))

        md_content = "\n".join(md_parts)
        out_md = args.json_file.with_name(args.json_file.stem + "-contrast.md")
        out_md.write_text(md_content, encoding="utf-8")
        print(f"已生成 Markdown 文件: {out_md}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)