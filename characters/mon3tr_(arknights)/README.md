# mon3tr

## 简介

《明日方舟》中，最初以一个陪伴凯尔希的怪异实体形象登场的角色，后来拟人化成了人。

- 她的名字是 Mon3tr。她的名字读作 “Monster”。

mon3tr 是这个项目的第 2 个角色。

我对绿色角色没有特别的喜好，只是她碰巧是绿色，并且有一个和 nozomi 的 base 不一样的颜色。
我需要了解在绿色情况下这个 prompt 的鲁棒性。

## 配色

### 采样

| 目标           | 选定 Hex | OKLCH（约）          | 说明                           |
| -------------- | -------- | -------------------- | ------------------------------ |
| Base           | #0E1412  | L≈0.23 C≈0.02 h≈170° | 比纯黑略抬 L，微绿             |
| Text           | #CCB497  | L≈0.78 C≈0.05 h≈72°  | 皮肤亮色                       |
| Accent1 (Neon) | #7AF271  | L≈0.83 C≈0.15 h≈140° | 荧光绿（用于 Green/Teal 衍生） |
| Accent2 (Red)  | #C1453E  | L≈0.55 C≈0.16 h≈25°  | 晦暗红（Red/Maroon 基）        |

### 27

| Category | Name        | OKLCH           | Hex     |
| -------- | ----------- | --------------- | ------- |
| Semantic | Rosewater   | 0.74,0.06,20°   | #E3CFC7 |
| Semantic | Flamingo    | 0.64,0.12,25°   | #D97558 |
| Semantic | Pink        | 0.62,0.16,330°  | #D957B5 |
| Semantic | Mauve       | 0.60,0.13,300°  | #B870E8 |
| Semantic | Red         | 0.55,0.16,25°   | #C1453E |
| Semantic | Maroon      | 0.45,0.10,20°   | #8E332C |
| Semantic | Peach       | 0.66,0.12,60°   | #E09A52 |
| Semantic | Yellow      | 0.70,0.12,98°   | #D5D65A |
| Semantic | Green       | 0.83,0.15,140°  | #7AF271 |
| Semantic | Teal        | 0.65,0.14,170°  | #3ABF9C |
| Semantic | Sky         | 0.68,0.12,200°  | #56B4E9 |
| Semantic | Sapphire    | 0.55,0.10,225°  | #2F72C4 |
| Semantic | Blue        | 0.60,0.13,215°  | #3E8BDF |
| Semantic | Lavender    | 0.67,0.08,275°  | #A29CF5 |
| Text/UI  | Text        | 0.78,0.05,72°   | #CCB497 |
| Text/UI  | Subtext1    | 0.72,0.04,72°   | #B8A488 |
| Text/UI  | Subtext0    | 0.66,0.035,72°  | #A39077 |
| UI       | Overlay2    | 0.65,0.030,170° | #6F7D75 |
| UI       | Overlay1    | 0.59,0.028,170° | #5A665F |
| UI       | Overlay0    | 0.53,0.025,170° | #47514C |
| UI       | Surface2    | 0.47,0.022,170° | #3B4541 |
| UI       | Surface1    | 0.41,0.020,170° | #313B38 |
| UI       | Surface0    | 0.35,0.018,170° | #27312F |
| UI       | Crust       | 0.29,0.016,170° | #1D2624 |
| UI       | Mantle      | 0.26,0.014,170° | #16201E |
| UI       | Base        | 0.23,0.020,170° | #0E1412 |
| UI       | Accent Edge | 0.53,0.060,140° | #4FA85A |

## 移植

### Neovim

<details>
  <summary>修改 catppuccin</summary>

```lua
					frappe = {
						-- mon3tr

						crust = "#1D2624",
						mantle = "#16201E",
						base = "#0E1412",
						surface0 = "#27312F",
						surface1 = "#313B38",
						surface2 = "#3B4541",
						overlay0 = "#47514C",
						overlay1 = "#5A665F",
						overlay2 = "#6F7D75",
						text = "#CCB497",
						subtext1 = "#B8A488",
						subtext0 = "#A39077",

						rosewater = "#E3CFC7",
						flamingo = "#D97558",
						pink = "#D957B5",
						mauve = "#B870E8",
						red = "#C1453E",
						maroon = "#8E332C",
						peach = "#E09A52",
						yellow = "#D5D65A",
						green = "#7AF271",
						teal = "#3ABF9C",
						sky = "#56B4E9",
						sapphire = "#2F72C4",
						blue = "#3E8BDF",
						lavender = "#A29CF5",
					},
```

![mon3tr-screenshot](./img/mon3tr.png)

</details>

## 生成

要生成，需要和此角色的立绘（精英零）一起发送至 ChatGPT-o3 中。

由于初版已经设计好了，所以只需要按照对比度修正一下就行了。

<details>
  <summary>查看 prompt</summary>

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

## ◤ Dark Palette — Mon3tr ◢

遵循 **0. 共通约束**，并执行以下专属指令：

### 1-a. 角色 & 图片

- 角色：**Mon3tr**（Arknights）
- 图片：**mon3tr.png**（透明底立绘）

### 1-b. 采样目标

| 目标    | 说明                                                                                           |
| ------- | ---------------------------------------------------------------------------------------------- |
| Base    | 取自她袖子的近黑墨绿，作为总体背景基调，降低亮度以护眼                                         |
| Text    | 采自她偏冷白肤色，调高亮度保证可读性                                                           |
| Accent1 | 直接提取晶体的荧光绿，Mon3tr 的标志色，`Green`, `Teal` 应该从 Accent1 的来源提取出来。         |
| Accent2 | mon3tr.png 有不显眼的红色，找到并提取这种红色。`Red`、`Maroon` 应该从 Accent2 的来源提取出来。 |

### 2. 氛围指引

以下是我较为满意的配色，只是说可能不合规。你先尝试生成一个新的 mon3tr palette，再指出下面这个配色有什么问题，再去修改。

    				frappe = {
    					-- mon3tr

    					crust = "#010101",
    					mantle = "#0D0F0E",
    					base = "#141615",
    					surface0 = "#252927",
    					surface1 = "#353D39",
    					surface2 = "#45504B",
    					overlay0 = "#55695F",
    					overlay1 = "#5E7F6E",
    					overlay2 = "#6B9A83",
    					text = "#C4B69D",
    					subtext0 = "#AEA390",
    					subtext1 = "#989081",

    					rosewater = "#F2D6D8",
    					flamingo = "#F5989D",
    					pink = "#F5A2E5",
    					mauve = "#C592FF",
    					red = "#9C5B5B",
    					maroon = "#7A3F3F",
    					peach = "#FFBC8C",
    					yellow = "#E1DD8A",
    					green = "#8CEA92",
    					teal = "#6EE1CA",
    					sky = "#9CD4FF",
    					sapphire = "#3578E5",
    					blue = "#5AA9F9",
    					lavender = "#C8B6FF",
    				},

</details>
