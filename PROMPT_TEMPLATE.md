## 指令

从性价比来看，我选择尝试使用 LLM（这里的 LLM **必须能执行程序**）来生成。这就需要用到 Prompt Engineering。

我参考了谷歌的 [Prompting guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)。其中指出，一个好的 prompt 可以由以下元素构成：

- Persona (角色)
- Task (任务)
- Context (背景)
- Format (格式)

需要注意的是，对于有 LLM 参与的工作，结果一般是无法复现的，理论上有 seed，但实际上没什么意义。

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
