# Porting

Since all palettes are based on a flavor of Catppuccin, the most comprehensive and beautiful method is to use Catppuccin's official porting tool, [Whiskers](https://github.com/catppuccin/whiskers).

## Usage

A basic example is to use whiskers to port to neovim:

```console
whiskers -f <FLAVOR> --color-overrides <COLOR_OVERRIDES> [TEMPLATE]
```

-   `<FLAVOR>`: The name of the Catppuccin flavor you want to port (`latte`, `frappe`, `macchiato`, `mocha`). For this project, you can only choose one, not generate all of them.
-   `<COLOR_OVERRIDES>`: The `palette-whiskers.json` corresponding to the character. Only accepts a JSON string.

### Neovim Example

For the [Kal'tsit](../themes/arknights_kaltsit/README.md) theme, if you need to port it to Neovim, use the following command line.

```console
whiskers -f latte --color-overrides ..\themes\arknights_kaltsit\palette-whiskers.json nvim.tera
```


Then, it will generate `.\lua\catppuccin\palettes\latte.lua` with the following content:

```lua
return {
	rosewater = "#b58f8f",
	flamingo = "#c28483",
	pink = "#c180a9",
	mauve = "#aa84da",
	red = "#d35b5b",
	maroon = "#b24444",
	peach = "#c38e66",
	yellow = "#9c9e2f",
	green = "#77a05e",
	teal = "#4aa99e",
	sky = "#5d9db8",
	sapphire = "#359fbd",
	blue = "#4f83e3",
	lavender = "#8d91e5",
	text = "#4c4b50",
	subtext1 = "#5c5b5e",
	subtext0 = "#6c6b6c",
	overlay2 = "#828283",
	overlay1 = "#929291",
	overlay0 = "#a2a3a0",
	surface2 = "#b2b3ae",
	surface1 = "#c2c3bc",
	surface0 = "#d2d3ca",
	base = "#f5f4e5",
	mantle = "#ececdf",
	crust = "#e2e3d8",
}
```