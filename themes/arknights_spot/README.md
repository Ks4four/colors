# Spot

- **角色:** 斑点
- **出处:** 《明日方舟》 (Arknights)
- **别名:** `伯克依·博尔努` (本名), `Spot`、`Bukar Bornu` (EN), `スポット` (JP)
- **参考:** [Donmai Wiki](<https://donmai.moe/wiki_pages/spot_(arknights)>), [PRTS](https://prts.wiki/w/%E6%96%91%E7%82%B9)
- **序号:** `#8`

---

> `斑点` 是这个项目的第 8 个角色。

## 配色

完整的色彩数据存储在 [JSON](./palette.json) 文件中。

### 矩阵

对比度矩阵分析的原始数据为 [JSON 格式](./contrast-matrix.json)（另提供一份 [仅与 base 对比的版本](./contrast-base.json)），同时也提供了一份更易于阅读的 [Markdown 版本](./contrast-report.md)。

### 来源

查看以下图片，这是不言自明的。

![sample](./assets/sample.png)

## 移植

### Neovim

<details>
  <summary>作为 catppuccin 的 latte flavor</summary>

```lua
require("catppuccin").setup {
    color_overrides = {
        latte = {
        rosewater= "#DC2E85",
        flamingo = "#E72747",
        pink     = "#E12D69",
        mauve    = "#8C6AAF",
        red      = "#CC3333",
        maroon   = "#7A1F1F",
        peach    = "#B85E05",
        yellow   = "#947400",
        green    = "#528439",
        teal     = "#1937E1",
        sky      = "#0C74E4",
        sapphire = "#0A7EBD",
        blue     = "#007EC2",
        lavender = "#8F63BB",
        text     = "#222222",
        subtext0 = "#1A1A1A",
        subtext1 = "#121212",
        base     = "#C4C4C4",
        mantle   = "#BDBDBD",
        crust    = "#B5B5B5",
        surface0 = "#A6A6A6",
        surface1 = "#969696",
        surface2 = "#878787",
        overlay0 = "#787878",
        overlay1 = "#696969",
        overlay2 = "#595959",
        },
    }
}
```
