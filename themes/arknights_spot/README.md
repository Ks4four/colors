# Spot

- **Character:** Spot
- **Source:** Arknights
- **Alias:** `斑点` (CN), `伯克依·博尔努` (Real Name), `Spot`, `Bukar Bornu` (EN), `スポット` (JP)
- **Reference:** [Donmai Wiki](<https://donmai.moe/wiki_pages/spot_(arknights)>), [PRTS](https://prts.wiki/w/%E6%96%91%E7%82%B9)
- **Index:** `#8`

---

> `Spot` is the 8th character in this project.

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
  <summary>As catppuccin's latte flavor</summary>

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
</details>
