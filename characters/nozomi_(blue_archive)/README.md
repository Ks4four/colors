# nozomi

## 简介

《蔚蓝档案》中，一名来自海兰德铁道学院的学生和列车长。

她的全名是 `橘ノゾミ`。
她的罗马音名是 `Tachibana Nozomi`。
她的译名是`橘望`/`橘希望`。

她和她姐姐的名字来源于[東海旅客鉄道](https://ja.wikipedia.org/wiki/%E6%9D%B1%E6%B5%B7%E6%97%85%E5%AE%A2%E9%89%84%E9%81%93)运营的现实生活中的新干线列车“[のぞみ](<https://ja.wikipedia.org/wiki/%E3%81%AE%E3%81%9E%E3%81%BF_(%E5%88%97%E8%BB%8A)>)”和“[ひかり](<https://ja.wikipedia.org/wiki/%E3%81%B2%E3%81%8B%E3%82%8A_(%E5%88%97%E8%BB%8A)>)”。

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
