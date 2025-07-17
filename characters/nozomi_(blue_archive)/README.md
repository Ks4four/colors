# nozomi

## 简介

《蔚蓝档案》中，一名来自海兰德铁道学院的学生和列车长。

她的全名是 `橘ノゾミ`。
她的罗马音名是 `Tachibana Nozomi`。
她的译名是`橘望`/`橘希望`。

她和她姐姐的名字来源于[東海旅客鉄道](https://ja.wikipedia.org/wiki/%E6%9D%B1%E6%B5%B7%E6%97%85%E5%AE%A2%E9%89%84%E9%81%93)运营的现实生活中的新干线列车“[のぞみ](<https://ja.wikipedia.org/wiki/%E3%81%AE%E3%81%9E%E3%81%BF_(%E5%88%97%E8%BB%8A)>)”和“[ひかり](<https://ja.wikipedia.org/wiki/%E3%81%B2%E3%81%8B%E3%82%8A_(%E5%88%97%E8%BB%8A)>)”。

## 配色

设计思路**并不是**人类写的。

| 分类 | 名称 | Hex | 设计思路 |
|------|------|------|----------|
| 基础 | Crust | #141827 | 制服最深阴影再加深，作为最底层背景减少眩光。 |
| 基础 | Mantle | #1A1E32 | 在 Crust 之上稍亮一级，供大型面板或分栏使用。 |
| 基础 | Base | #1E2339 | 取自制服主色并略微提亮，作为主要代码区背景。 |
| 基础 | Surface | #262D45 | 比 Base 再亮一级，供浮层 / 悬停菜单。 |
| 基础 | Text | #F2F4F8 | 来自她的白色裤袜，保证暗背景下的高对比正文。 |
| 基础 | Subtext | #C3C6D1 | Text 降低亮度 25%，用于注释与次要信息。 |
| 语义 | Rosewater | #F4E0D7 | 以暖粉作柔和提示；取自肤色高光并减饱和。 |
| 语义 | Flamingo | #F9A8B4 | 粉中带橙，表现调皮语气；Rosewater 增饱和。 |
| 语义 | Pink | #FFB1D3 | 明艳粉，用于正向高亮；Flamingo 偏紫调。 |
| 语义 | Mauve | #D1A4E8 | 紫粉混合，适合函数名；与制服蓝形成类比色。 |
| 语义 | Red | #F66D7F | 高警示错误色；取粉色补色并提高饱和度。 |
| 语义 | Maroon | #C04554 | Red 加黑加蓝，供严重错误或删除状态。 |
| 语义 | Peach | #FBBD8D | 源自徽章金属光泽，添加橙调显活力。 |
| 语义 | Yellow | #F7D76A | 直接取眼睛金黄并提亮，用于警告或标记。 |
| 语义 | Green | #C0E89C | 从光环色 #eafac8 降低亮度，作成功状态。 |
| 语义 | Teal | #B7EFD3 | 以光环色向青色旋转 30°，用于信息提示。 |
| 语义 | Sky | #8FC8FF | 制服蓝提亮＋加青，表现轻盈悬浮元素。 |
| 语义 | Sapphire | #366DB6 | 制服蓝降低亮度，强调选中或活动标签。 |
| 语义 | Blue | #5082CC | 直接采样肩章条纹，用作主链接 / 关键词。 |
| 语义 | Lavender | #AAADFF | Blue 向紫移并提亮，作为次级链接或配色平衡。 |
| 基础 | Surface 2 | #3F588F | Hover / 次级卡片，数字越大越亮 |
| 基础 | Subtext 0 | #B3BAD0 | Text 降低亮度 25%，用作注释 |
| 基础 | Surface 0 | #2C406D | Base 再提亮 8%，代码块背板 |
| 基础 | Surface 1 | #354C7F | 用于选中行 / 输入框填充 |
| 基础 | Surface 2 | #3F588F | Hover / 次级卡片，数字越大越亮 |
| 基础 | Overlay 0 | #4964A0 | 悬浮面板／下拉菜单底色 |
| 基础 | Overlay 1 | #546FB0 | Modal 窗口，亮度再提升 |
| 基础 | Overlay 2 | #5F7CC1 | Tooltip／通知气泡，使其从背景中弹出 |

## 移植

### Neovim

由于 tokyonight 支持许多插件，所以只需要在上面修改颜色即可。

```Lua
{
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
    opts = function()
        local styles = require("tokyonight.colors").styles
        styles.nozomi = vim.tbl_extend("force", styles.night, {
            bg = "#1E2339", -- Base
            bg_dark = "#141827", -- Crust
            bg_dark1 = "#1A1E32", -- Mantle
            bg_highlight = "#2C406D", -- Surface 2
            blue = "#3C6AFF", -- Blue
            blue0 = "#5980FF",
            blue1 = "#7696FF",
            blue2 = "#93ADFF",
            blue5 = "#B1C3FF",
            blue6 = "#CED9FF",
            blue7 = "#E1E8FF",
            comment = "#4964A0", -- Overlay 0
            cyan = "#8FC8FF", -- Sky
            dark3 = "#141C32",
            dark5 = "#0C111F",
            fg = "#F2F4F8", -- Text
            fg_dark = "#B3BAD0", -- Subtext 0
            fg_gutter = "#4964A0", -- Overlay 0
            green = "#C0E89C", -- Green
            green1 = "#CFF2B4",
            green2 = "#C6D4AA",
            magenta = "#FFB1D3", -- Pink
            magenta2 = "#F9A8B4", -- Flamingo
            orange = "#FBBD8D", -- Peach
            purple = "#D1A4E8", -- Mauve
            red = "#F66D7F", -- Red
            red1 = "#FF8888",
            teal = "#B7EFD3", -- Teal
            terminal_black = "#141827", -- Crust
            yellow = "#F7D76A", -- Yellow
            git = {
                add = "#C0E89C", -- Green
                change = "#5082CC", -- Blue
                delete = "#FF6B6B", -- Red
            },
        })

        return {
            style = "nozomi",
            transparent = false,
            styles = {
                sidebars = "transparent",
                floats = "transparent",
            },
        }
    end,
}
```

![nozomi-screenshot](<./img/nozomi.png>)
