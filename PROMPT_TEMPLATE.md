## 指令

从性价比来看，我选择尝试使用 LLM（这里的 LLM **必须能执行程序**）来生成。这就需要用到 Prompt Engineering。

我参考了谷歌的 [Prompting guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)。其中指出，一个好的 prompt 可以由以下元素构成：

- Persona (角色)
- Task (任务)
- Context (背景)
- Format (格式)

需要注意的是，对于有 LLM 参与的工作，结果一般是无法复现的，理论上有 seed，但实际上没什么意义。

---

```md

你是一个专业UI设计师，尤其擅长为开发者工具创造富有情感联系和视觉一致性的主题。

我希望你根据一个动漫角色的核心色系，为我创作一个专门用于代码编辑器的 Light Mode 调色板。这个调色板必须严格遵循下方指定的命名结构。

### 1. 角色与风格分析

- 角色名: 凯尔希 (本名 Kal'tsit)
- 出处: Arknights
- 核心性格与气质: 凯尔希，罗德岛高层管理人员之一，罗德岛医疗项目领头人。在冶金工业、社会学、源石技艺、考古学、历史系谱学、经济学、植物学、地质学等领域皆拥有渊博学识。于罗德岛部分行动中作为医务人员提供医学理论协助与应急医疗器械，同时也作为罗德岛战略指挥系统的重要组成人员活跃在各项目中。 

- 期望的调色板感觉: 应该是一个偏绿色的白色背景，配上她的服装语义色的主题。角色总体上是冷静的。
- 文件结构： kaltsit.png 是她的立绘。

### 2. 核心颜色基准
 
- 主要基调色 (用于背景): 观察 kaltsit.png 她的毛发，显然她的毛发都是包含绿色感觉的白色，提取这种白色来当作 base。
- 核心文本色 (用于文字): 对于文字色，应该是她身上装备的黑色综合起来的一种颜色作为 text。
- 第一强调色 (最标志性的颜色): 她身上的衣服是绿色的。
- 第二强调色 (次要特色): 她的耳朵是黄色的。

### 3. 设计任务与色彩学要求

请根据上述**核心颜色基准**，填充以下的调色板结构。
- 推断原则：你需要基于核心颜色，运用专业的色彩学知识（如调整饱和度、亮度，寻找邻近色、互补色）来生成剩余的颜色。所有颜色组合在一起时，必须感觉它们源自同一个角色。
- 风格指令：
    - UI系 (Base, Mantle, Crust, Surface 0, Surface 1, Surface 2, Overlay 0, Overlay 1, Overlay 2): 以**主要基调色 (base)**为基础进行微调，确保长时间阅读的舒适性。对于 Surface 和 Overlay，数字越大则越暗。具体梯度需要参看 # 4. Catppuccin 梯度示例。
    - Text系 (Text, Subtext 0, Subtext 1): 以**核心文本色 (text)**为基础创建不同亮度的版本，确保清晰易读。对于 Subtext，数字越大则越暗。具体梯度需要参看 # 4. Catppuccin 梯度示例。
    - Semantic系: 必须体现用户描述的**核心性格与气质**。它们需要比基础色更鲜明，但又不能过于刺眼。
        - 绿色系包含：Green。她的衣服显然是绿色的。你可以从 kaltsit.png 中提取和统计出来，为了长时间阅读性可以变化。
        - 黄色系包含：Yellow、Peach。你需要查看立绘，找出她耳朵上的 Yellow。为了长时间阅读可以压暗这种yellow。Peach 可以选择用专业的色彩学知识生成。
        - 蓝色系包含：Blue、Sapphire、Sky、Teal、Lavender。这些需要通过专业色彩学知识变化并生成。可以参照Catppuccin - Latte，但不能抄袭。
        - 红色系包含：Red、Maroon、Flamingo、Rosewater。这些需要通过专业色彩学知识变化并生成。可以参照Catppuccin - Latte，但不能抄袭。
        - 剩下 Mauve、Lavender、Pink 需要使用专业的色彩学知识变化后生成。可以参照Catppuccin - Latte，但不能抄袭。

### 4. 提取颜色

你必须首先使用图像分析工具从提供的图片中**提取核心色值**。你不得仅凭印象或描述生成颜色。你必须使用 Python 工具或其他方式从指定部位提取颜色。

你需要利用以下图像文件：
- `kaltsit.png`

### 5. Catppuccin 梯度示例

下表展示 Latte 口味中 *Base ⇢ Surface/Overlay/Mantle/Crust* 与 *Text ⇢ Subtext* 的精确梯度。  
请在生成新调色板时「复用同样的相对增量」，但以本角色的 Base / Text 作为起点。  

| Labels     | Hex       | RGB                | HSL                |
|------------|-----------|--------------------|--------------------|
| Text       | `#4c4f69` | `rgb(76, 79, 105)`   | `hsl(234, 16%, 35%)`|
| Subtext1   | `#5c5f77` | `rgb(92, 95, 119)`   | `hsl(233, 13%, 41%)`|
| Subtext0   | `#6c6f85` | `rgb(108, 111, 133)` | `hsl(233, 10%, 47%)`|
| Overlay2   | `#7c7f93` | `rgb(124, 127, 147)` | `hsl(232, 10%, 53%)`|
| Overlay1   | `#8c8fa1` | `rgb(140, 143, 161)` | `hsl(231, 10%, 59%)`|
| Overlay0   | `#9ca0b0` | `rgb(156, 160, 176)` | `hsl(228, 11%, 65%)`|
| Surface2   | `#acb0be` | `rgb(172, 176, 190)` | `hsl(227, 12%, 71%)`|
| Surface1   | `#bcc0cc` | `rgb(188, 192, 204)` | `hsl(225, 14%, 77%)`|
| Surface0   | `#ccd0da` | `rgb(204, 208, 218)` | `hsl(223, 16%, 83%)`|
| Base       | `#eff1f5` | `rgb(239, 241, 245)` | `hsl(220, 23%, 95%)`|
| Mantle     | `#e6e9ef` | `rgb(230, 233, 239)` | `hsl(220, 22%, 92%)`|
| Crust      | `#dce0e8` | `rgb(220, 224, 232)` | `hsl(220, 21%, 89%)`|

如果不遵循梯度的话，部分 UI 会看不清字。

### 6. 输出格式
 
请以JSON返回最终的调色板：
- 顶层是一个对象，键为颜色分类，顺序为 Semantic、Text、UI。
- 每个分类的值是一个包含颜色对象的数组。
- 每个颜色对象包含 Name, Hex, Rationale 三个字段。
  - 名称 (Name): 如 Rosewater, Base 等。
  - Hex
  - 设计思路 (Rationale): 简要说明这个颜色的灵感来源或推导逻辑（例如：“源自金色纽扣颜色，增加了亮度以体现活泼感”）。
- 顺序：Rosewater、Flamingo、Pink、Mauve、Red、Maroon、Peach、Yellow、Green、Teal、Sky、Sapphire、Blue、Lavender、Text、Subtext0、Subtext1、Base、Mantle、Crust、Surface0、Surface1、Surface2、Overlay0、Overlay1、Overlay2。

范例：

```json
{
  "Semantic": [
    {
      "Name": "Rosewater",
      "Hex": "#F9E2AF",
      "Rationale": "光环呼应"
    },
		{
      "Name": "Flamingo",
			// ...
		},
    // ... all other semantic colors here
  ],
  "Text": [
    {
      "Name": "Text",
      "Hex": "#F4F9E3",
      "Rationale": "抽样高亮白"
    },
		{
      "Name": "Subtext0",
			// ...
		},
		// ... all other text colors here
  ],
  "UI": [
    {
      "Name": "Base",
      "Hex": "#292A3C",
      "Rationale": "制服暗蓝"
    },
		{
      "Name": "Mantle",
			// ...
		},
  // ... all other UI colors here
  ]
}
```