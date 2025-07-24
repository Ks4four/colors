#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI
----
python compute.py palette.json
python compute.py palette.json -t 4.5 7 -s 3 --md
python compute.py palette.json -t 4.5 -s 3 -ss 3 4 --no-color

矩阵
-----
1. Text   vs UI
2. Semantic vs UI
3. Semantic vs Semantic （新增）

输出
-----
- <stem>-contrast.json
- <stem>-base-contrast.json
- (可选) <stem>-contrast.md

阈值
-----
各矩阵可独立设置：
  - Text vs UI        : -t  / --text-th      <normal> [strict]
  - Semantic vs UI    : -s  / --semantic-th  <normal> [strict]
  - Semantic vs Self  : -ss / --semantic-self-th <normal> [strict]
若省略则该矩阵无阈值。
"""

from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# ---------- WCAG contrast ----------
def hex_to_rgb(h: str) -> Tuple[float, float, float]:
    h = h.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"非法 HEX: {h}")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore

def srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def relative_luminance(rgb: Tuple[float, float, float]) -> float:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(hex1: str, hex2: str) -> float:
    l1, l2 = relative_luminance(hex_to_rgb(hex1)), relative_luminance(hex_to_rgb(hex2))
    return (max(l1, l2) + .05) / (min(l1, l2) + .05)

# ---------- ANSI ----------
RED, GREEN, RESET = "\033[31m", "\033[32m", "\033[0m"
def style(r: float, n: Optional[float], s: Optional[float], color: bool) -> str:
    txt = f"{r:>10.2f}"
    if not color or n is None:             return txt
    if r < n:                              return f"{RED}{txt}{RESET}"
    if s is not None and r >= s:           return f"{GREEN}{txt}{RESET}"
    return txt

def cell_json(r: float, n: Optional[float], s: Optional[float]) -> Dict[str, object]:
    return {
        "ratio": round(r, 2),
        "pass_normal": (r >= n) if n is not None else None,
        "pass_strict": (r >= s) if s is not None else None,
    }

# ---------- Markdown ----------
def md_matrix(title: str, rows: List[Dict[str, str]], cols: List[Dict[str, str]],
              n: Optional[float], s: Optional[float]) -> str:
    head = [""] + [c["Name"] for c in cols]
    md = [f"### {title}"]
    md.append("阈值：" + ("未设置" if n is None else
             (f"普通 ≥ **{n}** :1" if s is None else
              f"普通 ≥ **{n}** :1；严格 ≥ **{s}** :1")))
    md.append("| " + " | ".join(head) + " |")
    md.append("| " + " | ".join(["---"]*len(head)) + " |")
    for r in rows:
        row = [r["Name"]]
        for c in cols:
            ratio = contrast_ratio(r["Hex"], c["Hex"])
            mark = "" if n is None else (" ❌" if ratio < n else (" ✅" if s is not None and ratio >= s else ""))
            row.append(f"{ratio:.2f}{mark}")
        md.append("| " + " | ".join(row) + " |")
    md.append("")
    return "\n".join(md)

# ---------- 核心打印 ----------
def print_matrix(label: str, rows: List[Dict[str,str]], cols: List[Dict[str,str]],
                 n: Optional[float], s: Optional[float], color: bool) -> Dict[str, Dict[str, Dict[str, object]]]:
    print(f"\n{label}")
    if n is None: print("阈值：未设置")
    else: print(f"阈值：普通 ≥ {n}:1" +("" if s is None else f"；严格 ≥ {s}:1"))
    print(" "*12 + "  ".join(f"{c['Name']:>10}" for c in cols))
    m: Dict[str, Dict[str, Dict[str, object]]] = {}
    for r in rows:
        row_json, styled = {}, []
        for c in cols:
            ratio = contrast_ratio(r["Hex"], c["Hex"])
            row_json[c["Name"]] = cell_json(ratio, n, s)
            styled.append(style(ratio, n, s, color))
        m[r["Name"]] = row_json
        print(f"{r['Name']:<10}  " + "  ".join(styled))
    return m

# ---------- Base JSON helper ----------
def build_base(base_hex: str, grp: List[Dict[str,str]], n: Optional[float], s: Optional[float]):
    return {g["Name"]: cell_json(contrast_ratio(g["Hex"], base_hex), n, s) for g in grp}

# ---------- Argparse ----------
def parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute WCAG contrast matrices for a palette JSON.")
    p.add_argument("json_file", type=Path, help="颜色 JSON 文件")
    p.add_argument("-t","--text-th", metavar="N", type=float, nargs="+",
                   help="Text vs UI 阈值 <normal> [strict]")
    p.add_argument("-s","--semantic-th", metavar="N", type=float, nargs="+",
                   help="Semantic vs UI 阈值 <normal> [strict]")
    p.add_argument("-ss","--semantic-self-th", metavar="N", type=float, nargs="+",
                   help="Semantic vs Semantic 阈值 <normal> [strict]")
    p.add_argument("--md", action="store_true", help="生成 Markdown 文件")
    p.add_argument("--no-color", action="store_true", help="关闭终端彩色输出")
    return p.parse_args()

def to_th(nums: Optional[List[float]])->Tuple[Optional[float],Optional[float]]:
    if not nums: return None, None
    return (nums+[None,None])[:2]  # 保证长度2

# ---------- Main ----------
def main():
    args = parse()
    if not args.json_file.is_file():
        sys.exit(f"文件不存在: {args.json_file}")
    palette = json.loads(args.json_file.read_text(encoding="utf-8"))
    semantic, text, ui = palette.get("Semantic",[]), palette.get("Text",[]), palette.get("UI",[])
    if not (semantic and text and ui):
        sys.exit("JSON 中必须包含 Semantic/Text/UI 三组颜色")

    tn, ts = to_th(args.text_th)
    sn, ss = to_th(args.semantic_th)
    s2n, s2s = to_th(args.semantic_self_th)
    color = not args.no_color

    # 打印三张矩阵
    txt_json  = print_matrix("Text vs UI",      text,     ui,        tn,  ts,  color)
    sem_json  = print_matrix("Semantic vs UI",  semantic, ui,        sn,  ss,  color)
    sem2_json = print_matrix("Semantic vs Semantic", semantic, semantic, s2n, s2s, color)

    # 完整 JSON
    full_json = {"matrices":{
        "Text_vs_UI":        {"thresholds":{"normal":tn,"strict":ts},  "rows":txt_json},
        "Semantic_vs_UI":    {"thresholds":{"normal":sn,"strict":ss},  "rows":sem_json},
        "Semantic_vs_Sem":   {"thresholds":{"normal":s2n,"strict":s2s},"rows":sem2_json},
    }}
    out_full = args.json_file.with_name(args.json_file.stem+"-contrast.json")
    out_full.write_text(json.dumps(full_json,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"\n已生成结果文件: {out_full}")

    # Base JSON
    base = next((c for c in ui if c["Name"].lower()=="base"),None)
    if base is None: sys.exit("UI 组中未找到 Base 颜色")
    base_hex = base["Hex"]
    base_json = {
        "base":{"name":"Base","hex":base_hex},
        "Text_vs_Base":     {"thresholds":{"normal":tn,"strict":ts},  "rows": build_base(base_hex,text,tn,ts)},
        "Semantic_vs_Base": {"thresholds":{"normal":sn,"strict":ss},  "rows": build_base(base_hex,semantic,sn,ss)}
    }
    out_base=args.json_file.with_name(args.json_file.stem+"-base-contrast.json")
    out_base.write_text(json.dumps(base_json,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"已生成结果文件: {out_base}")

    # Markdown
    if args.md:
        md = ["# 对比度结果", f"源文件：**{args.json_file.name}**\n"]
        md.append(md_matrix("Text vs UI",      text,     ui,        tn,  ts))
        md.append(md_matrix("Semantic vs UI",  semantic, ui,        sn,  ss))
        md.append(md_matrix("Semantic vs Semantic", semantic, semantic, s2n, s2s))
        out_md=args.json_file.with_name(args.json_file.stem+"-contrast.md")
        out_md.write_text("\n".join(md),encoding="utf-8")
        print(f"已生成 Markdown 文件: {out_md}")

if __name__=="__main__":
    try: main()
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr); sys.exit(1)