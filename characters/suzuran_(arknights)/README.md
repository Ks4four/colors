# suzuran

## 简介

《明日方舟》中，一名基于九尾狐设计的角色。

- 她的名字是`铃兰`。她的译名是 `Suzuran`，日文译名是`スズラン`。她的本名是`丽萨`，译名为 `Lisa`、`リサ`。

铃兰是这个项目的第 3 个角色。

尝试做一个 light theme，挑上铃兰（或所谓的“大家的光”）算是合适的。然而，可能是因为 o3 的模型更熟悉 dark theme 的用法，导致我多次尝试 prompt，都未能选出理想的语义化颜色。

一开始我是喂了她的 4 个时装进去的，但是这直接导致 o3 的 python 环境崩溃，导致它一直重启它的环境，最后思考时间超过 12 分钟之后直接卡死，过程非常有趣。

后来，我改为仅使用她的默认时装，这才基本成功。

## 配色

| 颜色名称  | 十六进制代码 |
| --------- | ------------ |
| Rosewater | `#8F4E4C`    |
| Flamingo  | `#874542`    |
| Pink      | `#8E4561`    |
| Mauve     | `#6B4A7F`    |
| Red       | `#b43842`    |
| Maroon    | `#a34246`    |
| Peach     | `#8F5524`    |
| Yellow    | `#6E5715`    |
| Green     | `#0C6B51`    |
| Teal      | `#18685A`    |
| Sky       | `#255B74`    |
| Sapphire  | `#066ca2`    |
| Blue      | `#386a8f`    |
| Lavender  | `#715894`    |
| Text      | `#111115`    |
| Subtext1  | `#1e1f24`    |
| Subtext0  | `#2b2e34`    |
| Overlay2  | `#6C5A0D`    |
| Overlay1  | `#806B12`    |
| Overlay0  | `#947C16`    |
| Surface2  | `#A48F3F`    |
| Surface1  | `#B5A25E`    |
| Surface0  | `#C5B57B`    |
| Base      | `#E7DCB4`    |
| Mantle    | `#DED2A6`    |
| Crust     | `#D6C897`    |

## 移植

### Neovim

<details>
  <summary>修改 catppuccin</summary>

```lua
latte = {
		-- suzuran

		base = "#E7DCB4",
		mantle = "#DED2A6",
		crust = "#D6C897",
		surface0 = "#C5B57B",
		surface1 = "#B5A25E",
		surface2 = "#A48F3F",
		overlay0 = "#947C16",
		overlay1 = "#806B12",
		overlay2 = "#6C5A0D",
		text = "#111115",
		subtext1 = "#1e1f24",
		subtext0 = "#2b2e34",

		rosewater = "#8F4E4C",
		flamingo = "#874542",
		pink = "#8E4561",
		mauve = "#6B4A7F",
		red = "#b43842",
		maroon = "#a34246",
		peach = "#8F5524",
		yellow = "#6E5715",
		green = "#0C6B51",
		teal = "#18685A",
		sky = "#255B74",
		sapphire = "#066ca2",
		blue = "#386a8f",
		lavender = "#715894",
},
```


<!-- <details>
  <summary>查看 prompt</summary>


</details> -->