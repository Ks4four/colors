# nozomi

- **角色:** 橘ノゾミ (たちばなのぞみ)
- **出处:** ブルーアーカイブ (Blue Archive)
- **别名:** `Tachibana Nozomi` (EN), `橘望`、`橘希望` (CN)
- **参考:** [Donmai Wiki](<https://donmai.moe/wiki_pages/nozomi_(blue_archive)>), [ピクシブ百科事典](https://dic.pixiv.net/a/%E6%A9%98%E3%83%8E%E3%82%BE%E3%83%9F)
- **序号:** `#1`

---

> 她的特殊性仅限于她是第一个。\
> 不像 Neovim 对于 Catppuccin 的重要性，nozomi 单纯就是第一个。\
> 正因为如此，如果她没有存在过，那么也会有别的角色当作第一个。

## 配色

完整的色彩数据存储在 [JSON](nozomi.json) 文件中。

### 矩阵

对比度矩阵分析的原始数据为 [JSON 格式](contrast.json)（另提供一份 [仅与 base 对比的版本](base-contrast.json)），同时也提供了一份更易于阅读的 [Markdown 版本](contrast.md)。

### 来源

查看以下图片，这是不言自明的。

![nozomi-sample](./assets/sample.png)

## 移植

### Neovim

<details>
  <summary>作为 catppuccin 的 frappe flavor</summary>

```lua
frappe = {
  -- nozomi

    rosewater = "#F5E0DC",
    flamingo = "#F2CDCD",
    pink = "#F5C2E7",
    mauve = "#CBA6F7",
    red = "#F38BA8",
    maroon = "#EBA0AC",
    peach = "#FAB387",
    yellow = "#F9E2AF",
    green = "#A6E3A1",
    teal = "#94E2D5",
    sky = "#89DCEB",
    sapphire = "#74C7EC",
    blue = "#89B4FA",
    lavender = "#B4BEFE",

    text = "#F4F9E3",
    subtext0 = "#CCD2BD",
    subtext1 = "#E0E6D0",

    base = "#292A3C",
    mantle = "#303143",
    crust = "#38394C",
    surface0 = "#47495C",
    surface1 = "#58596D",
    surface2 = "#686A7F",
    overlay0 = "#7A7B91",
    overlay1 = "#8C8DA3",
    overlay2 = "#9EA0B6",
},
```

</details>
