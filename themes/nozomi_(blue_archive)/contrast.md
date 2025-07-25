# 对比度结果
源文件：**nozomi.json**

### Text vs UI
阈值：普通 ≥ **4.5** :1
|  | Base | Mantle | Crust | Surface0 | Surface1 | Surface2 | Overlay0 | Overlay1 | Overlay2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Text | 13.09 | 11.85 | 10.50 | 8.21 | 6.36 | 4.93 | 3.85 ❌ | 3.02 ❌ | 2.39 ❌ |
| Subtext0 | 9.07 | 8.21 | 7.28 | 5.69 | 4.41 ❌ | 3.42 ❌ | 2.67 ❌ | 2.09 ❌ | 1.66 ❌ |
| Subtext1 | 11.00 | 9.96 | 8.83 | 6.90 | 5.35 | 4.14 ❌ | 3.23 ❌ | 2.54 ❌ | 2.01 ❌ |

### Semantic vs UI
阈值：普通 ≥ **2.5** :1
|  | Base | Mantle | Crust | Surface0 | Surface1 | Surface2 | Overlay0 | Overlay1 | Overlay2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rosewater | 11.12 | 10.07 | 8.92 | 6.98 | 5.41 | 4.19 | 3.27 | 2.57 | 2.03 ❌ |
| Flamingo | 9.65 | 8.74 | 7.75 | 6.06 | 4.70 | 3.64 | 2.84 | 2.23 ❌ | 1.76 ❌ |
| Pink | 9.23 | 8.36 | 7.40 | 5.79 | 4.49 | 3.48 | 2.71 | 2.13 ❌ | 1.69 ❌ |
| Mauve | 6.93 | 6.28 | 5.56 | 4.35 | 3.37 | 2.61 | 2.04 ❌ | 1.60 ❌ | 1.27 ❌ |
| Red | 6.08 | 5.51 | 4.88 | 3.82 | 2.96 | 2.29 ❌ | 1.79 ❌ | 1.41 ❌ | 1.11 ❌ |
| Maroon | 6.81 | 6.17 | 5.47 | 4.28 | 3.31 | 2.57 | 2.00 ❌ | 1.57 ❌ | 1.25 ❌ |
| Peach | 7.96 | 7.21 | 6.39 | 4.99 | 3.87 | 3.00 | 2.34 ❌ | 1.84 ❌ | 1.45 ❌ |
| Yellow | 11.09 | 10.04 | 8.90 | 6.96 | 5.39 | 4.18 | 3.26 | 2.56 | 2.03 ❌ |
| Green | 9.47 | 8.58 | 7.60 | 5.95 | 4.61 | 3.57 | 2.79 | 2.19 ❌ | 1.73 ❌ |
| Teal | 9.46 | 8.57 | 7.59 | 5.94 | 4.60 | 3.56 | 2.78 | 2.18 ❌ | 1.73 ❌ |
| Sky | 9.06 | 8.20 | 7.27 | 5.68 | 4.41 | 3.41 | 2.66 | 2.09 ❌ | 1.65 ❌ |
| Sapphire | 7.46 | 6.76 | 5.99 | 4.68 | 3.63 | 2.81 | 2.19 ❌ | 1.72 ❌ | 1.36 ❌ |
| Blue | 6.69 | 6.06 | 5.37 | 4.20 | 3.25 | 2.52 | 1.97 ❌ | 1.55 ❌ | 1.22 ❌ |
| Lavender | 7.87 | 7.13 | 6.32 | 4.94 | 3.83 | 2.97 | 2.32 ❌ | 1.82 ❌ | 1.44 ❌ |

### Semantic vs Semantic
阈值：未设置
|  | Rosewater | Flamingo | Pink | Mauve | Red | Maroon | Peach | Yellow | Green | Teal | Sky | Sapphire | Blue | Lavender |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rosewater | 1.00 | 1.15 | 1.21 | 1.60 | 1.83 | 1.63 | 1.40 | 1.00 | 1.17 | 1.18 | 1.23 | 1.49 | 1.66 | 1.41 |
| Flamingo | 1.15 | 1.00 | 1.05 | 1.39 | 1.59 | 1.42 | 1.21 | 1.15 | 1.02 | 1.02 | 1.07 | 1.29 | 1.44 | 1.23 |
| Pink | 1.21 | 1.05 | 1.00 | 1.33 | 1.52 | 1.35 | 1.16 | 1.20 | 1.03 | 1.03 | 1.02 | 1.24 | 1.38 | 1.17 |
| Mauve | 1.60 | 1.39 | 1.33 | 1.00 | 1.14 | 1.02 | 1.15 | 1.60 | 1.37 | 1.36 | 1.31 | 1.08 | 1.04 | 1.14 |
| Red | 1.83 | 1.59 | 1.52 | 1.14 | 1.00 | 1.12 | 1.31 | 1.82 | 1.56 | 1.55 | 1.49 | 1.23 | 1.10 | 1.29 |
| Maroon | 1.63 | 1.42 | 1.35 | 1.02 | 1.12 | 1.00 | 1.17 | 1.63 | 1.39 | 1.39 | 1.33 | 1.10 | 1.02 | 1.16 |
| Peach | 1.40 | 1.21 | 1.16 | 1.15 | 1.31 | 1.17 | 1.00 | 1.39 | 1.19 | 1.19 | 1.14 | 1.07 | 1.19 | 1.01 |
| Yellow | 1.00 | 1.15 | 1.20 | 1.60 | 1.82 | 1.63 | 1.39 | 1.00 | 1.17 | 1.17 | 1.22 | 1.49 | 1.66 | 1.41 |
| Green | 1.17 | 1.02 | 1.03 | 1.37 | 1.56 | 1.39 | 1.19 | 1.17 | 1.00 | 1.00 | 1.05 | 1.27 | 1.42 | 1.20 |
| Teal | 1.18 | 1.02 | 1.03 | 1.36 | 1.55 | 1.39 | 1.19 | 1.17 | 1.00 | 1.00 | 1.04 | 1.27 | 1.41 | 1.20 |
| Sky | 1.23 | 1.07 | 1.02 | 1.31 | 1.49 | 1.33 | 1.14 | 1.22 | 1.05 | 1.04 | 1.00 | 1.21 | 1.35 | 1.15 |
| Sapphire | 1.49 | 1.29 | 1.24 | 1.08 | 1.23 | 1.10 | 1.07 | 1.49 | 1.27 | 1.27 | 1.21 | 1.00 | 1.12 | 1.06 |
| Blue | 1.66 | 1.44 | 1.38 | 1.04 | 1.10 | 1.02 | 1.19 | 1.66 | 1.42 | 1.41 | 1.35 | 1.12 | 1.00 | 1.18 |
| Lavender | 1.41 | 1.23 | 1.17 | 1.14 | 1.29 | 1.16 | 1.01 | 1.41 | 1.20 | 1.20 | 1.15 | 1.06 | 1.18 | 1.00 |
