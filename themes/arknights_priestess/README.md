# Priestess

- **Character:** Priestess
- **Source:** Arknights
- **Alias:** `普瑞赛斯` (CN), `Priestess` (EN), `プリースティス` (JP)
- **Reference:** [Donmai Wiki](<https://donmai.moe/wiki_pages/arknights_priestess>), [Moegirlpedia](https://zh.moegirl.org.cn/zh-hans/%E6%99%AE%E7%91%9E%E8%B5%9B%E6%96%AF)
- **Index:** `#5`

---

> `Priestess` is the 5th character in this project.
>
> The first version looked very similar to [Helix](https://helix-editor.com/), so I lowered the brightness.
> Unfortunately, this doesn't stop it from still looking like a lower-brightness Helix.
>
> This character was made to test a purple-based theme. In terms of plagiarism suspicion, this seems to be a relative failure.

## Palette

The complete color data is stored in the [JSON](./palette.json) file.

The JSON format suitable for Whiskers is stored in [palette-whiskers.json](./palette-whiskers.json).

### Matrix

The raw data for the contrast matrix analysis is in [JSON format](./contrast-matrix.json) (another version with [only base comparison](./contrast-base.json) is also provided), and a more readable [Markdown version](./contrast-report.md) is also available.

### Source

Look at the following image, it's self-explanatory.

![sample](./assets/sample.png)

## Porting

### Neovim

<details>
	<summary>As catppuccin's macchiato flavor</summary>

```lua
require("catppuccin").setup {
    color_overrides = {
        macchiato = {
        rosewater= "#EFDDDA",
        flamingo = "#E9CCCC",
        pink     = "#AF9FCE",
        mauve    = "#D5B3F8",
        red      = "#DD96A0",
        maroon   = "#E1A5AA",
        peach    = "#E3AE90",
        yellow   = "#E2CFAA",
        green    = "#ABCF9F",
        teal     = "#96C9C2",
        sky      = "#9DCED6",
        sapphire = "#8CBED4",
        blue     = "#99B2E4",
        lavender = "#C0C4EE",
        text     = "#DAD7D9",
        subtext0 = "#B2ACB0",
        subtext1 = "#C6C1C4",
        base     = "#140F15",
        mantle   = "#0B080C",
        crust    = "#030203",
        surface0 = "#2A1F2D",
        surface1 = "#413045",
        surface2 = "#553F5A",
        overlay0 = "#6C5072",
        overlay1 = "#82608A",
        overlay2 = "#97749E",
        },
    }
}
```

</details>
