from PIL import Image
import os
from collections import OrderedDict

ALL_COLORS = {
    "Crust": "#E0D19D",
    "Mantle": "#E3D7A8",
    "Base": "#E7DCB4",
    "Text": "#292B36",
    "Rosewater": "#B87E7D",
    "Flamingo": "#B06D6C",
    "Pink": "#C08A9B",
    "Mauve": "#9B8CA8",
    "Red": "#A54F4C",
    "Maroon": "#7A3333",
    "Peach": "#C88B5D",
    "Yellow": "#9E8244",
    "Green": "#219876",
    "Teal": "#4F8F82",
    "Sky": "#608CA6",
    "Sapphire": "#324863",
    "Blue": "#4E5B77",
    "Lavender": "#7B6A90",
    "Surface0": "#D8C686",
    "Surface1": "#D1BC6E",
    "Surface2": "#C9B157",
    "Overlay0": "#C2A640",
    "Overlay1": "#AC9337",
    "Overlay2": "#957F30",
    "Subtext1": "#363947",
    "Subtext0": "#434759",
}

COLOR_ORDER = [
    "Rosewater",
    "Flamingo",
    "Pink",
    "Mauve",
    "Red",
    "Maroon",
    "Peach",
    "Yellow",
    "Green",
    "Teal",
    "Sky",
    "Sapphire",
    "Blue",
    "Lavender",
    "Text",
    "Subtext1",
    "Subtext0",
    "Overlay2",
    "Overlay1",
    "Overlay0",
    "Surface2",
    "Surface1",
    "Surface0",
    "Base",
    "Mantle",
    "Crust",
]

# 每个色块的尺寸
IMAGE_SIZE = (20, 50)
# 输出文件名
OUTPUT_FILENAME = "color_strip.png"


def generate_color_strip():
    """
    根据 COLOR_ORDER 将色块横向合并成一个条状图片。
    """
    print("\nStarting color strip generation...")

    # 计算合并后图像的总宽度和高度
    total_width = IMAGE_SIZE[0] * len(COLOR_ORDER)
    height = IMAGE_SIZE[1]

    # 创建一个新的空白图像（画布）
    strip_image = Image.new("RGB", (total_width, height))

    current_x = 0  # 当前粘贴位置的x坐标

    for color_name in COLOR_ORDER:
        hex_color = ALL_COLORS.get(color_name)

        if not hex_color:
            print(f"Warning: Color '{color_name}' not found in definitions. Skipping.")
            continue

        try:
            # 在内存中创建单个色块图像
            color_block = Image.new("RGB", IMAGE_SIZE, color=hex_color)

            # 将色块粘贴到画布的指定位置
            strip_image.paste(color_block, (current_x, 0))

            # 更新下一个色块的x坐标
            current_x += IMAGE_SIZE[0]

            print(f"Pasted: {color_name}")

        except ValueError as e:
            print(f"Error creating image for {color_name} with hex {hex_color}: {e}")
            continue

    # 保存最终合并的图像
    strip_image.save(OUTPUT_FILENAME)
    print(f"\nSuccessfully generated: {OUTPUT_FILENAME}")
    print("\nAll tasks completed. Your color strip is ready!")


if __name__ == "__main__":
    generate_color_strip()
