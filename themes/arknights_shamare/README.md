# Shamare

- **Character:** Shamare
- **Source:** Arknights
- **Alias:** `巫恋` (CN), `Shamare` (EN), `シャマレ` (JP)
- **Reference:** [Donmai Wiki](<https://donmai.moe/wiki_pages/shamare_(arknights)>), [PRTS](https://prts.wiki/w/%E5%B7%AB%E6%81%8B)
- **Index:** `#7`

---

> `Shamare` is the 7th character in this project.

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
	<summary>As catppuccin's frappe flavor</summary>

```lua
require("catppuccin").setup {
    color_overrides = {
        frappe = {
        rosewater= "#F2CED5",
        flamingo = "#EFB9C3",
        pink     = "#E8A2C0",
        mauve    = "#DDA6E3",
        red      = "#E591A2",
        maroon   = "#B97C88",
        peach    = "#E8B49A",
        yellow   = "#F0D591",
        green    = "#A9D8B8",
        teal     = "#9ACECF",
        sky      = "#B3CBF2",
        sapphire = "#8793C2",
        blue     = "#A6B3E3",
        lavender = "#B8A9C3",
        text     = "#E2DCEC",
        subtext0 = "#BCB3C9",
        subtext1 = "#CFC5DD",
        base     = "#3A314A",
        mantle   = "#322B41",
        crust    = "#2A2436",
        surface0 = "#4A435A",
        surface1 = "#5B536C",
        surface2 = "#6C647D",
        overlay0 = "#817896",
        overlay1 = "#9288A8",
        overlay2 = "#A89FBD",
        },
    }
}
```

</details>
