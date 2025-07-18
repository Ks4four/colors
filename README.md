# colors

一个关于普通人（非程序员、非设计师）如何将动漫角色转换为工具颜色主题的项目。

## 使用

如果你喜欢如下角色，可以测试对应的 ports。

- [nozomi (blue archive)](./characters/nozomi_(blue_archive)/README.md)
- mon3tr (arknights)

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

我最终发送的 prompt 如下：

```md
你是一个专业UI设计师，尤其擅长为开发者工具创造富有情感联系和视觉一致性的主题。

我希望你根据一个动漫角色的核心色系，为我创作一个专门用于代码编辑器的“暗黑模式” (Dark Mode) 调色板。这个调色板必须严格遵循下方指定的命名结构。

### 1. 角色与风格分析

橘ノゾミ、ハイランダー鉄道学園所属、CCC（中央管制センター）の幹部。陽気かつハツラツとした性格で、細かいことは気にしない。そのせいか、双子の姉であるヒカリと一緒にトラブルを引き起こすこともしばしば。面白そうなものにはとりあえず飛び込む性格だが、列車運行に関しては責任を持って臨んでいる。

这要求调色板在整体沉稳专业的基调上，必须拥有明亮、充满活力的强调色。

### 2. 核心颜色基准

在 Blue Archive 中，光环相当于学生的生命。如果光环破碎，学生就会死亡。她的光环颜色是 #eafac8。
除此之外，还有如下几点：
- 背景色 (base)：她的制服颜色，可以选择比立绘更深一点的蓝色。
- 文本色 (text)：可以从她的裤袜得到灵感。
- 黄色系：她的眼睛是黄色的，以及她身上的某些物品是金色的。

### 3. 设计任务与色彩学要求

请根据上述**核心颜色基准**，填充以下的调色板结构。
- 推断原则：你需要基于核心颜色，运用专业的色彩学知识（如调整饱和度、亮度，寻找邻近色、互补色）来生成剩余的颜色。所有颜色组合在一起时，必须感觉它们源自同一个角色。
- 风格指令：
    - 基础色 (Base, Mantle, Crust, Surface 0, Surface 1, Surface 2, Overlay 0, Overlay 1, Overlay 2): 必须沉稳、专业，以制服颜色为基础进行微调，确保长时间阅读的舒适性。对于 Surface 和 Overlay，数字越大则越亮。
    - 文本色 (Text, Subtext 0, Subtext 1): 必须清晰易读，以她的裤袜为基础，可以创建不同亮度的版本。对于 Subtext，数字越大则越亮。
    - 语义色: 必须体现角色“陽気かつハツラツ”的性格。它们需要比基础色更鲜明，但又不能过于刺眼。
        - `Green`, `Teal` 应从光环色 `#eafac8` 演变而来。
        - `Blue`, `Sapphire`, `Sky`, `Lavender` 需要你根据现有颜色进行和谐的创造，以补全整个色谱。
        - `Yellow`、`Peach` 应从她的眼睛颜色或配饰演变而来。
        - `Red`, `Maroon`, `Mauve`, `Pink`, `Flamingo`, `Rosewater` 应该使用色彩学知识来生成。

### 4. 输出格式
 
请以Markdown表格的形式返回最终的调色板，包含以下列：
- 分类 (Category): 语义 (Semantic) 或 基础 (Base)
- 名称 (Name): 如 Rosewater, Base 等
- 设计思路 (Rationale): 简要说明这个颜色的灵感来源或推导逻辑（例如：“源自金色纽扣颜色，增加了亮度以体现活泼感”）。
```

在命名方案上，我选择使用 Catppuccin，单纯因为它颜色多。此外，追求极简的用户也可以使用 Dracula。对于主题机制爱好者，还可以使用 Base16 的命名方案。

至于“设计思路”这一列，AI 输出的内容多为套话，对人类来说，用处仅在于判断 AI 是否按要求进行了思考。

## 移植

生成调色板后，便可以将其移植到各种软件中。这里涉及“CoT (Chain-of-Thought)”这个 prompt 技巧。简单来说，就是紧接着发送一个新 prompt。

### Neovim

你当然可以选择直接重写一个新的主题，但是在实践中，修改 tokyonight.nvim 更为实际，因为它支持许多插件。有趣的是，其中蓝色系（blue）的颜色值变化并非循序渐进。因此，在实际使用时，也应当相应地修改这个 prompt。

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

###
