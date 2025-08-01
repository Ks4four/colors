# Rosmontis

- **Character:** Rosmontis
- **Source:** Arknights
- **Alias:** `纳西莎` (CN), `Rosmontis`, `Narcissa` (EN), `ロスモンティス`, `ナルシッサ` (JP)
- **Reference:** [Donmai Wiki](<https://donmai.moe/wiki_pages/rosmontis_(arknights)>), [PRTS](https://prts.wiki/w/%E8%BF%B7%E8%BF%AD%E9%A6%99)
- **Index:** `#10`

---

> `Rosmontis` is the 10th character in this project.

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
			rosewater = "#d76787",
			flamingo = "#dd608d",
			pink = "#d96489",
			mauve = "#6c699f",
			red = "#d65b91",
			maroon = "#b84681",
			peach = "#d1732f",
			yellow = "#b3821f",
			green = "#469b60",
			teal = "#5a9591",
			sky = "#7d8da2",
			sapphire = "#4c6c94",
			blue = "#5e81ac",
			lavender = "#7c79a9",
			text = "#3b4251",
			subtext1 = "#4a5161",
			subtext0 = "#5a616f",
			overlay2 = "#636986",
			overlay1 = "#727896",
			overlay0 = "#838aa4",
			surface2 = "#939bb2",
			surface1 = "#a4abc1",
			surface0 = "#b5bcce",
			base = "#d8dee8",
			mantle = "#ced5e3",
			crust = "#c5cddd",
		},
	}
}
```

</details>
