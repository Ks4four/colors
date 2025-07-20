# nozomi

## 简介

《蔚蓝档案》中，一名来自海兰德铁道学院的学生和列车长。

- 她的全名是 `橘ノゾミ`。她的罗马音名是 `Tachibana Nozomi`。她的译名是`橘望`/`橘希望`。

nozomi 是这个项目的第一个角色。

她的特殊性仅限于她是第一个。
不像 Neovim 对于 Catppuccin 的重要性，nozomi 单纯就是第一个。
正因为如此，如果她没有存在过，那么也会有别的角色当作第一个。

## 配色

### 采样

| Target         | OKLCH (L C h)                 | Hex       |
| -------------- | ----------------------------- | --------- |
| Base           | oklch(29.23 % 0.0327 281.7 °) | `#292A3C` |
| Text           | oklch(97.47 % 0.0295 119.4 °) | `#F4F9E3` |
| Accent1 (光环) | oklch(96.90 % 0.0364 120.5 °) | `#F1F9DE` |
| Accent2 (瞳色) | oklch(76.30 % 0.1332 99.2 °)  | `#C7B341` |

### 26

| Category | Name      | OKLCH                         | Hex       | Rationale       |
| -------- | --------- | ----------------------------- | --------- | --------------- |
| UI       | Text      | oklch(97.25 % 0.0293 117.4 °) | `#F4F9E3` | 抽样高亮白      |
| UI       | Subtext1  | oklch(91.44 % 0.0300 119.4 °) | `#E0E6D0` | Text_L – 6      |
| UI       | Subtext0  | oklch(85.34 % 0.0292 120.0 °) | `#CCD2BD` | Text_L – 12     |
| UI       | Overlay2  | oklch(71.13 % 0.0319 281.4 °) | `#9EA0B6` | Base_L + 42     |
| UI       | Overlay1  | oklch(65.00 % 0.0326 283.4 °) | `#8C8DA3` | +36             |
| UI       | Overlay0  | oklch(59.07 % 0.0333 285.1 °) | `#7A7B91` | +30             |
| UI       | Surface2  | oklch(53.17 % 0.0331 283.0 °) | `#686A7F` | +24             |
| UI       | Surface1  | oklch(47.21 % 0.0329 282.3 °) | `#58596D` | +18             |
| UI       | Surface0  | oklch(41.27 % 0.0328 282.0 °) | `#47495C` | +12             |
| UI       | Base      | oklch(29.23 % 0.0327 281.7 °) | `#292A3C` | 制服暗蓝        |
| UI       | Mantle    | oklch(32.23 % 0.0328 281.8 °) | `#303143` | +3              |
| UI       | Crust     | oklch(35.23 % 0.0328 281.8 °) | `#38394C` | +6              |
| Semantic | Rosewater | oklch(92.11 % 0.0719 30.8 °)  | `#F5E0DC` | 柔和粉调，≥ 3:1 |
| Semantic | Flamingo  | oklch(87.70 % 0.0672 26.2 °)  | `#F2CDCD` | 轻粉            |
| Semantic | Pink      | oklch(83.20 % 0.0818 340.0 °) | `#F5C2E7` | 樱花粉          |
| Semantic | Mauve     | oklch(71.01 % 0.0881 309.4 °) | `#CBA6F7` | 淡紫            |
| Semantic | Red       | oklch(64.32 % 0.1095 20.4 °)  | `#F38BA8` | 强红            |
| Semantic | Maroon    | oklch(66.74 % 0.1003 8.8 °)   | `#EBA0AC` | 玫瑰红          |
| Semantic | Peach     | oklch(74.52 % 0.0971 55.3 °)  | `#FAB387` | 蜜桃            |
| Semantic | Yellow    | oklch(92.02 % 0.0556 108.9 °) | `#F9E2AF` | 光环呼应        |
| Semantic | Green     | oklch(81.35 % 0.0839 140.2 °) | `#A6E3A1` | 绿叶            |
| Semantic | Teal      | oklch(80.16 % 0.0746 175.1 °) | `#94E2D5` | 湖水            |
| Semantic | Sky       | oklch(79.02 % 0.0719 205.9 °) | `#89DCEB` | 天空            |
| Semantic | Sapphire  | oklch(72.28 % 0.0700 225.0 °) | `#74C7EC` | 青蓝            |
| Semantic | Blue      | oklch(68.06 % 0.0708 245.5 °) | `#89B4FA` | 明蓝            |
| Semantic | Lavender  | oklch(72.34 % 0.0660 275.3 °) | `#B4BEFE` | 薰衣草          |

## 移植

### Neovim

<details>
  <summary>修改 catppuccin</summary>

```Lua
mocha = {
  -- nozomi

  text = "#F4F9E3",
  subtext1 = "#E0E6D0",
  subtext0 = "#CCD2BD",
  overlay2 = "#9EA0B6",
  overlay1 = "#8C8DA3",
  overlay0 = "#7A7B91",
  surface2 = "#686A7F",
  surface1 = "#58596D",
  surface0 = "#47495C",
  base = "#292A3C",
  mantle = "#303143",
  crust = "#38394C",

  rosewater = "#F5E0DC",
  flamingo = "#F2CDCD",
  pink = "#F5C2E7",
  mauve = "#CBA6F7",
  red = "#F38BA8",
  maroon = "#EBA0AC",
  peach = "#FAB387",
  yellow = "#F9E2AF",
  green = "#A6E3A1",
  teal = "#94E2D5",
  sky = "#89DCEB",
  sapphire = "#74C7EC",
  blue = "#89B4FA",
  lavender = "#B4BEFE",
},
```

![nozomi-screenshot](./img/nozomi.png)

</details>

## 生成

要生成，需要和此角色的立绘一起发送至 ChatGPT-o3 中。

此调色板作成时还未引入梯度概念，故需要进行 CoT。

<details>
  <summary>查看 prompt</summary>

```md
你正在和一个不能接收文件的客户端说话。以下执行结果必须要用 markdown 全部展示，而不能输出文件。

# 0. 共通约束（务必整段复制到 Light / Dark 段首）

**角色**：{各段落填写}  
**色空间**：全部在 **OKLCH** 内处理，最终同时输出 OKLCH + Hex（sRGB）。

## 0-1 固定输出的 27 色名（顺序任意但 **不可缺漏、不可新增**）

Semantic（14）  
Rosewater · Flamingo · Pink · Mauve · Red · Maroon · Peach · Yellow ·  
Green · Teal · Sky · Sapphire · Blue · Lavender

Base/Text & UI 阶层（13）  
Text · Subtext1 · Subtext0 ·  
Overlay2 · Overlay1 · Overlay0 ·  
Surface2 · Surface1 · Surface0 ·  
Base · Mantle · Crust

## 0-2 亮度梯度 & 对比度

### (A) UI 阶层的 ΔL（以 **Base_L** 为 0）

| 名称     | ΔL (Light) | 说明                   |
| -------- | ---------- | ---------------------- |
| Mantle   | –3         | 比 Base 略暗，便于分区 |
| Crust    | –6         | 比 Mantle 再暗一级     |
| Surface0 | –12        |
| Surface1 | –18        |
| Surface2 | –24        |
| Overlay0 | –30        |
| Overlay1 | –36        |
| Overlay2 | –42        |

> **Dark Mode**：全部 ΔL 取相反符号（+3 → +42），保持绝对值不变。

### (B) 文本梯度（以 **Text_L** 为 0）

| 名称     | ΔL (Light) | ΔL (Dark) |
| -------- | ---------- | --------- |
| Subtext1 | +6         | –6        |
| Subtext0 | +12        | –12       |

### (C) 对比度硬性要求

- Text/Base ≥ **4.5 : 1**
- 任一 Semantic/Base ≥ **3 : 1**

### (D) 语义色限制

- 仅在 **C**（Chroma）方向增强；`|ΔL_Semantic| ≤ 8`
- 若 Semantic/Base 不达 3 : 1，须给出
  1. **调整版**（已修正对比度）
  2. **忠于原色版**（注明“不合规”）

## 0-3 输出 & 验证流程

1. **核心采样**：用 Python 从上传图片提取 `Base / Text / Accent1 / Accent2` 四色（OKLCH + Hex），填入 4×2 小表。
2. **完整调板**：生成 27 行表格：`Category | Name | OKLCH | Hex | Rationale`。
   - UI 阶层按上表 ΔL 推算；Semantic 从 Accent1/2 衍生或色彩学生成。
3. **对比矩阵**：附一张 4 × 27 矩阵（Base vs Text & 全部 Semantic），输出数值；不达标处标红。

---

## ◤ Dark Palette — Nozomi ◢

遵循 **0. 共通约束**，并执行以下专属指令：

### 1-a. 角色 & 图片

- 角色：**Nozomi**（Blue Archive）
- 图片：**nozomi.png**（透明底立绘）

### 1-b. 采样目标

| 目标    | 说明             |
| ------- | ---------------- |
| Base    | 取自制服         |
| Text    | 来自她的白色裤袜 |
| Accent1 | 光环色 #eafac8   |
| Accent2 | 取眼睛金黄       |

### 2. 氛围指引

以下是我较为满意的配色，只是说可能不合规。你先尝试生成一个新的 mon3tr palette，再指出下面这个配色有什么问题，再去修改。

{
-- nozomi

    crust = "#141827",
    mantle = "#1A1E32",
    base = "#1E2339",
    surface0 = "#2C334F",
    surface1 = "#3A4265",
    surface2 = "#495279",
    overlay0 = "#586393",
    overlay1 = "#616EA8",
    overlay2 = "#7683BC",
    text = "#F2F4F8",
    subtext0 = "#DCDFE7",
    subtext1 = "#C7CCD4",

    rosewater = "#8F4E4C",
    flamingo = "#874542",
    pink = "#8E4561",
    mauve = "#6B4A7F",
    red = "#F66D7F",
    maroon = "#C04554",
    peach = "#8F5524",
    yellow = "#6E5715",
    green = "#0C6B51",
    teal = "#18685A",
    sky = "#255B74",
    sapphire = "#366DB6",
    blue = "#5082CC",
    lavender = "#AAADFF",

}
```

</details>
