# colors

一个关于普通人（非程序员、非设计师）如何将动漫角色转换为工具颜色主题的项目。

## 使用

如果你喜欢如下角色，可以查看对应角色的文档。

需要注意的是，对于有 LLM 参与的工作，结果一般是无法复现的，理论上有 seed，但实际上没什么意义。

[![nozomi-icon](<characters/nozomi_(blue_archive)/img/nozomi-icon.png>)![nozomi-strip.png](<characters/nozomi_(blue_archive)/img/nozomi-strip.png>)](<characters/nozomi_(blue_archive)/README.md>)

[![mon3tr-icon](<characters/mon3tr_(arknights)/img/mon3tr-icon.png>)![mon3tr-strip.png](<characters/mon3tr_(arknights)/img/mon3tr-strip.png>)](<characters/mon3tr_(arknights)/README.md>)

[![suzuran-icon](<characters/suzuran_(arknights)/img/suzuran-icon.png>)![suzuran-strip.png](<characters/suzuran_(arknights)/img/suzuran-strip.png>)](<characters/suzuran_(arknights)/README.md>)

## 原理

个人认为要形成一个配色，步骤如下：

1. 决定 **概念**：这个配色要尝试去做什么？尝试描述什么？在这个项目里，无一例外都是角色。
1. 决定 **采样色彩**：角色有什么色彩是特别明显的？
1. 决定 **Base**、**Text**：一个配色好歹要有背景和正文。
1. 决定 **梯度**：如果遇到有 UI 的东西，这些背景应该要有不同的层级，亮度的差距就是梯度。由于梯度是固定的，决定完梯度之后，就不怎么需要微调了。
1. 决定 **语义色**：除了正文，要强调的时候应该用什么色？
1. 微调 **语义色**：调整语义色的亮度，直到其满足可读性。
1. 编写 文档：“讲故事”，然后为语义色和梯度变化编写语义。

### 概念

在本项目中，每个核心概念均对应一个特定的动漫角色。

### 采样

概念形成之后，就可以采样了。
采样可以选择直接从原画中取点，也可以通过统计学采样。
统计学采样需要用到中位数 / K-means 聚类，避免挑到极端亮点或暗点。

采样的内容包括 Base、Text、语义色。语义色可以后文再取。

采样还要注意的是色空间。
最简单的就是使用 HSL。
不过，我用过的 LLM 都说 OKLCH 更好。

- 本项目用的是 chatGPT o3 主动使用的 K-means，但有时这种取样并不能令人满意。
- 本项目使用 OKLCH。

### 基本色

又称 base & text、背景和正文、`bg`和`fg`。

任何有效的颜色主题都必须包含基础的背景色 (Base) 与文本色 (Text)。
为确保在长时间使用下的可读性，二者之间必须满足特定的对比度标准。

- 本项目使用的标准是 [WCAG 2.1 | Level AA](https://www.w3.org/TR/WCAG21/#contrast-minimum)，要求背景色与文本色的对比度不低于 `4.5:1`。

### 梯度

对于不同的 UI 元素，比如面板、按钮、悬浮状态等，总不可能和背景颜色是一样的。
所以要适当在背景色上面变化。
简单实践是调整亮度即可。

- 本项目的梯度层级设计参考了 Catppuccin 主题在亮度（ΔL）上的处理方式。

### 语义色

语义色是指用于特定目的的强调色，例如代码语法高亮、链接、警告或成功状态等。成熟的颜色主题通常包含一套完整的语义色。

- **Dracula**:
  - 基本色：background, current line, foreground, comment
  - 语义色：cyan, green, orange, pink, purple, red, yellow
- **Catppuccin**:
  - 基本色：Text, Subtext1, Subtext0, Overlay2, Overlay1, Overlay0, Surface2, Surface1, Surface0, Base, Mantle, Crust
  - 语义色：Rosewater, Flamingo, Pink, Mauve, Red, Maroon, Peach, Yellow, Green, Teal, Sky, Sapphire, Blue, Lavender

可以注意到，部分颜色（主色）接近于单色 (mono)，非常相近。

当然这里的语义色并不是要采完七八种颜色，因为动漫角色为了创造记忆点，通常不会使用过多的色彩。
本项目流程如下：

1. 首先从采样色中确定一至两个核心强调色。
1. 采样完两三个，就可以使用工具来辅助生成别的语义色了。从原理上看，用到的原理包括但不限于同色系微调、补色、类比色等。
1. 使用 Catppuccin 框架来辅助生成颜色。

对于颜色框架，追求极简的用户也可以使用 Dracula。对于主题机制爱好者，还可以使用 Base16 的命名方案。

辅助生成的工具包括但不限于：

- 能**执行程序**的 LLM。
- <https://color.adobe.com>：只能通过锁定单个 base 色来生成。
- <https://coolors.co>：可以锁定多个颜色，但需要付费，且价格昂贵。

### a11y

做好语义色之后，就可以调整亮度，以确保其与背景色的组合符合可读性要求。

- 本项目要求语义色与基础背景色的对比度 (contrast) 不低于 3:1。

### 确定

现在你就获得了基本色和语义色。只需要用一些什么工具跑一次对比度矩阵 (contrast-matrix) 即可。

跑完了，就可以截图展示，然后编写文档了。
编写文档的时候要说明白哪个颜色是用来干什么的。

当然，如果基于框架（如 Dracula）设计的，那就让色彩不言自明了。

- 本项目使用 chatGPT o3 根据框架设计，不需要此步。

## 指令

从性价比来看，我选择尝试使用 LLM（这里的 LLM **必须能执行程序**）来生成。这就需要用到 Prompt Engineering。

我参考了谷歌的 [Prompting guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)。其中指出，一个好的 prompt 可以由以下元素构成：

- Persona (角色)
- Task (任务)
- Context (背景)
- Format (格式)

发送的 prompt 类似如下：

```md
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

## ◤ Light Palette — Suzuran ◢

遵循 **0. 共通约束**，并执行以下专属指令：

### 1-a. 角色 & 图片

- 角色：**Suzuran**（Arknights，铃兰）
- 图片：**suzuran_0.png**（透明底立绘）

### 1-b. 采样目标

| 目标    | 说明                       |
| ------- | -------------------------- |
| Base    | 毛发主体淡黄色（不能带红） |
| Text    | 装备主体深灰黑             |
| Accent1 | 头顶蓝色发带               |
| Accent2 | 绿色眼睛                   |

### 2. 氛围指引

- 她被称为“大家的光”——整体温暖、柔和、可长时间阅读
- Semantic-Blue 系来自发带；Semantic-Green 来自眼睛；Yellow / Peach 系由发色加深而来
```

## 移植

生成调色板后，便可以将其移植到各种软件中。

许多软件的主题和插件是绑定的，例如 Neovim、Obsidian、`Code.exe` 等。对于这些软件，可以在支持多插件的主题上修改颜色。

### Neovim

自然，在 Catppuccin/nvim 自定义颜色是最简单的。
当然，也可以选择修改别的主题。

### Obsidian

使用支持 Style Settings 插件的主题均可。

### `Code.exe`

需要通过 LLM 来生成对应的 `settings.json`
