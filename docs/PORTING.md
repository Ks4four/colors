# 移植

由于所有调色板都是基于 Catppuccin 的某个 Flavor，最大而美的方法就是使用 Catppuccin 官方的移植工具 [Whiskers](https://github.com/catppuccin/whiskers)。

## 用法

基础的例子是使用 whiskers 来移植 neovim：

```console
whiskers -f <FLAVOR> --color-overrides <COLOR_OVERRIDES> [TEMPLATE]
```

- `<FLAVOR>`：你想要移植的 Catppuccin Flavor 名称（`latte`、`frappe`、`macchiato`、`mocha`）。对于本项目，只能选择一种，而非都生成。
- `<COLOR_OVERRIDES>`：角色对应的 `palette-whiskers.json`。只接受 JSON 字符串。

### Neovim 例

对于 [kal'tsit](themes/arknights_kaltsit/README.md) 主题，如果需要移植到 Neovim，使用如下命令行。

```console
whiskers -f latte --color-overrides .\themes\arknights_kaltsit\palette-whiskers.json nvim.tera
```

然后，它会生成 `.\lua\catppuccin\palettes\latte.lua`，内容如下：

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
