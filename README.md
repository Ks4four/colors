# colors

一个关于普通人（非程序员、非设计师）如何将动漫角色转换为工具颜色主题的项目。

## 使用

如果你喜欢如下角色，可以查看对应角色的文档。

需要注意的是，对于有 LLM 参与的工作，结果一般是无法复现的，理论上有 seed，但实际上没什么意义。

- [nozomi (blue archive)](characters/nozomi_(blue_archive)/README.md)
- [mon3tr (arknights)](characters/mon3tr_(arknights)/README.md)

## 方法

### 构成

简单来说，一个 color palette 需要有基础色和语义色。以 Catppuccin 和 Dracula 为例：

- **Dracula**:
    - 主色：background, current line, foreground, comment
    - 语义色：cyan, green, orange, pink, purple, red, yellow
- **Catppuccin**:
    - 主色：Text, Subtext1, Subtext0, Overlay2, Overlay1, Overlay0, Surface2, Surface1, Surface0, Base, Mantle, Crust
    - 语义色：Rosewater, Flamingo, Pink, Mauve, Red, Maroon, Peach, Yellow, Green, Teal, Sky, Sapphire, Blue, Lavender

可以注意到，部分颜色（主色）接近于单色 (mono)，非常相近。

### 语义

动漫角色为了创造记忆点，通常不会使用过多的色彩。基础色的提取相对简单，使用视觉模型或经过特定程序处理即可。现在许多 LLM 也能提取颜色，综合来看，我最推荐能执行代码的 LLM。

但语义色是个难题，因为一个动漫角色的立绘不太可能包含至少六种可直接使用的语义色。

可以通过以下工具辅助生成语义色，但我目前只找到了：

-   <https://color.adobe.com>：只能通过锁定单个 base 色来生成。
-   <https://coolors.co>：可以锁定多个颜色，但需要付费，且价格昂贵。

### 指令

从性价比来看，我选择尝试使用 LLM（这里的 LLM **必须能执行程序**）来生成。这就需要用到 Prompt Engineering。

我参考了谷歌的 [Prompting guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)。其中指出，一个好的 prompt 可以由以下元素构成：

-   Persona (角色)
-   Task (任务)
-   Context (背景)
-   Format (格式)

发送的 prompt 类似如下：

```md
你是一个专业UI设计师，尤其擅长为开发者工具创造富有情感联系和视觉一致性的主题。

我希望你根据一个动漫角色的核心色系，为我创作一个专门用于代码编辑器的“暗黑模式” (Dark Mode) 调色板。这个调色板必须严格遵循下方指定的命名结构。

### 1. 角色与风格分析

- 角色名: [例如：莱莎·斯托特]
- 出处: [例如：莱莎的炼金工房]
- 核心性格与气质: [例如：开朗、好奇心旺盛、充满活力、有行动力。]
- 期望的调色板感觉: [例如：整体需要一个稳定、自然的基调（对应其采集和炼金的背景），但必须有明亮、充满冒险感的强调色来体现她的性格。]

### 2. 核心颜色基准【用户填写区】
 
💡 **提示**: 请观察角色立绘，描述关键颜色来自哪里。
 
- 主要基调色 (用于背景): [描述来源，通常是**服装**。例如：来自她深棕色的短裤和皮质装备，需要设计成一个更深的、适合做背景的颜色。]
- 核心文本色 (用于文字): [描述来源，通常是**浅色衣物或肤色**。例如：来自她白色的衬衫，可以是一个略带暖调的米白色，以保证可读性。]
- 第一强调色 (最标志性的颜色): [描述来源，通常是**眼睛、发色或关键配饰**。例如：来自她标志性的蓝色头巾和翠绿色的炼金瓶，选择更明亮的翠绿色。]
- 第二强调色 (次要特色): [描述来源，例如：她金色的头发和一些金属配饰。]

### 3. 设计任务与色彩学要求

请根据上述**核心颜色基准**，填充以下的调色板结构。
- 推断原则：你需要基于核心颜色，运用专业的色彩学知识（如调整饱和度、亮度，寻找邻近色、互补色）来生成剩余的颜色。所有颜色组合在一起时，必须感觉它们源自同一个角色。
- 风格指令：
    - 基础色 (Base, Mantle, Crust, Surface 0, Surface 1, Surface 2, Overlay 0, Overlay 1, Overlay 2): 以**主要基调色 (base)**为基础进行微调，确保长时间阅读的舒适性。对于 Surface 和 Overlay，数字越大则越亮。
    - 文本色 (Text, Subtext 0, Subtext 1): 以**核心文本色 (text)**为基础创建不同亮度的版本，确保清晰易读。对于 Subtext，数字越大则越亮。
    - 语义色: 必须体现用户描述的**核心性格与气质**。它们需要比基础色更鲜明，但又不能过于刺眼。
        - 例子：从用户提供的**第一和第二强调色**中汲取灵感，生成与之协调的 `Green`, `Teal`, `Yellow`, `Peach`。
        - 例子：基于已有的核心色系，通过色彩学原理和谐地创造出 `Blue`, `Sapphire`, `Sky`, `Lavender`，以补全冷色调光谱。
        - 例子：同样，运用色彩学知识生成功能性的 `Red`, `Maroon`, `Mauve`, `Pink` 等暖色点缀色，确保整体色盘的和谐与完整。

### 4. Catppuccin 梯度示例

下表展示 Frappe 口味中 *Base ⇢ Surface/Overlay* 与 *Text ⇢ Subtext* 的精确梯度。  
请在生成新调色板时「复用同样的相对增量」，但以本角色的 Base / Text 作为起点。  

| Label | Hex | HSL |
|-------|-----|-----|
| Crust | #232634 | 229°, 20%, 17% |
| Mantle | #292c3c | 231°, 19%, 20% |
| Base | #303446 | 229°, 19%, 23% |
| Surface 0 | #414559 | 230°, 16%, 30% |
| Surface 1 | #51576d | 227°, 15%, 37% |
| Surface 2 | #626880 | 228°, 13%, 44% |
| Overlay 0 | #737994 | 229°, 13%, 52% |
| Overlay 1 | #838ba7 | 227°, 17%, 58% |
| Overlay 2 | #949cbb | 228°, 22%, 66% |
| Text | #c6d0f5 | 227°, 70%, 87% |
| Subtext 1 | #b5bfe2 | 227°, 44%, 80% |
| Subtext 0 | #a5adce | 228°, 29%, 73% |

如果不遵循梯度的话，部分 UI 会看不清字。

### 5. 输出格式
 
请以Markdown表格的形式返回最终的调色板，包含以下列：
- 分类 (Category): 语义 (Semantic) 或 基础 (Base)
- 名称 (Name): 如 Rosewater, Base 等
- Hex
- 设计思路 (Rationale): 简要说明这个颜色的灵感来源或推导逻辑（例如：“源自金色纽扣颜色，增加了亮度以体现活泼感”）。
```

在命名方案上，我选择使用 Catppuccin，单纯因为它颜色多。此外，追求极简的用户也可以使用 Dracula。对于主题机制爱好者，还可以使用 Base16 的命名方案。

至于“设计思路”这一列，AI 输出的内容多为套话，对人类来说，用处仅在于判断 AI 是否按要求进行了思考。

[nozomi (blue archive)](./characters/nozomi_(blue_archive)/README.md) 是第一个使用例。
所以，参照它可能更易于理解。
不过，由于使用上总会发现各种各样的问题，所以主文档会是最新的。

## 移植

生成调色板后，便可以将其移植到各种软件中。这里涉及“CoT (Chain-of-Thought)”这个 prompt 技巧。简单来说，就是紧接着发送一个新 prompt。

许多软件的主题和插件是绑定的，例如 Neovim、Obsidian、`Code.exe` 等。对于这些软件，可以在支持多插件的主题上修改颜色。

### Neovim

自然，在 Catppuccin/nvim 自定义颜色是最简单的。
当然，也可以选择修改别的主题。

修改 tokyonight.nvim 更为实际。有趣的是，其中蓝色系（blue）的颜色值变化并非循序渐进。因此，在实际使用时，也应当相应地修改这个 prompt。

我发送的新 prompt 如下：

```md
现在，请你继续，将我们刚刚创建的这个调色板“移植”到一个 Neovim 主题的 Lua 模板中。

这是我需要你填充的目标模板：

---@class Palette
local ret = {
  bg = "#",
  bg_dark = "#",
  bg_dark1 = "#",
  bg_highlight = "#",
  blue = "#",
  blue0 = "#",
  blue1 = "#",
  blue2 = "#",
  blue5 = "#",
  blue6 = "#",
  blue7 = "#",
  comment = "#",
  cyan = "#",
  dark3 = "#",
  dark5 = "#",
  fg = "#",
  fg_dark = "#",
  fg_gutter = "#",
  green = "#",
  green1 = "#",
  green2 = "#",
  magenta = "#",
  magenta2 = "#",
  orange = "#",
  purple = "#",
  red = "#",
  red1 = "#",
  teal = "#",
  terminal_black = "#",
  yellow = "#",
  git = {
    add = "#",
    change = "#",
    delete = "#",
  },
}
return ret


为了完成这个任务，请严格遵循以下的映射逻辑和推导规则：

### 1. 基础颜色映射 (Base & Foreground)
- `bg`: 使用我们调色板中的 `Base`。
- `bg_dark`: 使用我们调色板中的 `Mantle` 或 `Crust`（选择更深的一个）。
- `fg`: 使用我们调色板中的 `Text`。
- `fg_dark`: 使用我们调色板中的 `Subtext0`。
- `comment`, `fg_gutter`: 使用我们调色板中的 `Overlay0`，因为它足够柔和，不会干扰视线。
- `bg_highlight`: 使用 `Surface2`，用于突出显示区域。

### 2. 语义颜色映射 (Semantic Colors)
- `red`: 使用 `Red`。
- `green`: 使用 `Green`。
- `yellow`: 使用 `Yellow`。
- `blue`: 使用 `Blue`。
- `purple`: 使用 `Mauve`。
- `magenta`: 使用 `Pink` 或 `Flamingo`。
- `cyan`, `teal`: 都使用 `Teal` 或 `Sky`（选择一个你认为更合适的作为主色）。
- `orange`: 使用 `Peach`。
- `terminal_black`: 使用 `Crust`。

### 3. 颜色推导规则 (非常重要)
当目标模板需要源调色板中没有的颜色变体时（例如 `red1`, `blue0`, `blue1`, `blue2` 等），请不要凭空捏造。你需要：
- 以主色为基准：例如，要生成 `red1`，就以我们已有的 `Red` 颜色为基础。
- 通过调整亮度和饱和度来创建变体：
  - 对于带数字的亮色（如 `blue0`, `blue1`），可以适当增加亮度或饱和度，使其更醒目。
  - 对于带数字的暗色（如 `dark3`, `dark5`），以 `Mantle` 为基础，进一步降低亮度。
- 保持色相一致：推导出的颜色必须与主色属于同一个色系，以确保整体和谐。

### 4. 特殊模块映射 (`git`)
根据通用设计规范：
- `git.add`: 必须使用 `Green`。
- `git.delete`: 必须使用 `Red`。
- `git.change`: 使用 `Blue` 或 `Yellow`。

请在分析完所有规则后，直接输出完整的、已填充所有颜色代码的 Lua 代码块。不需要额外的解释，我只需要最终的代码成品。
```
