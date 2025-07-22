# kal'tsit

- **角色:** 凯尔希 (Kal'tsit)
- **出处:** 《明日方舟》 (Arknights)
- **别名:** `kal'tsit` (EN), `ケルシー` (JP)
- **参考:** [Donmai Wiki](<https://donmai.moe/wiki_pages/kal'tsit_(arknights)>), [PRTS](https://prts.wiki/w/%E5%87%AF%E5%B0%94%E5%B8%8C)
- **序号:** `#4`

---

> `凯尔希` 是这个项目的第 4 个角色。在做这个角色的时候，引入了 JSON 和自动化脚本。对比前三个来看，这几乎是最成功的。
> 
> JSON 结构设计、对比度结果、语义色微调……做到这个角色上才算是形成一个 workflow。
>
> 有趣的是，这肯定比 [Mon3tr](..\mon3tr_(arknights)\README.md) 还要成功，不过在语义上，Mon3tr 应该是 Kal'tsit 的 dark mode。

## 配色

完整的色彩数据存储在 [JSON](kal'tsit.json) 文件中。

### 矩阵

对比度矩阵分析的原始数据为 [JSON 格式](kal'tsit-contrast.json)（另提供一份 [仅与 base 对比的版本](kal'tsit-base-contrast.json)），同时也提供了一份更易于阅读的 [Markdown 版本](kal'tsit-contrast.md)。

## 移植

### Neovim

<details>
	<summary>作为 catppuccin 的 latte flavor</summary>

```lua
latte = {
-- kal'tsit

    rosewater = "#B58F8F",
    flamingo = "#C28483",
    pink = "#C180A9",
    mauve = "#AA84DA",
    red = "#D35B5B",
    maroon = "#B24444",
    peach = "#C38E66",
    yellow = "#9C9E2F",
    green = "#77A05E",
    teal = "#4AA99E",
    sky = "#5D9DB8",
    sapphire = "#359FBD",
    blue = "#4F83E3",
    lavender = "#8D91E5",

    text = "#4C4B50",
    subtext0 = "#6C6B6C",
    subtext1 = "#5C5B5E",

    base = "#F5F4E5",
    mantle = "#ECECDF",
    crust = "#E2E3D8",
    surface0 = "#D2D3CA",
    surface1 = "#C2C3BC",
    surface2 = "#B2B3AE",
    overlay0 = "#A2A3A0",
    overlay1 = "#929291",
    overlay2 = "#828283",
},
```

</details>
