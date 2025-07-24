import argparse
import json
import sys
from PIL import Image

# 1. 定义最终色带中颜色的显示顺序
COLOR_ORDER = [
    "Rosewater", "Flamingo", "Pink", "Mauve", "Red", "Maroon", "Peach",
    "Yellow", "Green", "Teal", "Sky", "Sapphire", "Blue", "Lavender",
    "Text", "Subtext0", "Subtext1", "Base", "Mantle", "Crust", "Surface0",
    "Surface1", "Surface2", "Overlay0", "Overlay1", "Overlay2"
]

# 2. 输出图片的配置
IMAGE_SIZE = (20, 50)  # 每个色块的尺寸 (宽, 高)
OUTPUT_FILENAME = "color_strip.png"  # 输出文件名

def load_colors_from_json(file_path):
    """
    从指定的 JSON 文件中加载颜色定义。
    JSON 文件应包含 'Semantic', 'Text', 'UI' 等类别，
    每个类别下是包含 'Name' 和 'Hex' 的颜色对象列表。
    """
    print(f"正在从文件读取颜色: {file_path}")
    all_colors = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 遍历 JSON 中的每个类别 (例如 "Semantic", "Text", "UI")
            for category_colors in data.values():
                # 每个类别的值是一个颜色对象的列表
                for color_item in category_colors:
                    name = color_item.get("Name")
                    hex_val = color_item.get("Hex")
                    if name and hex_val:
                        all_colors[name] = hex_val
            print(f"成功加载 {len(all_colors)} 种颜色。")
            return all_colors
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"错误: 无法解析 '{file_path}' 中的 JSON。请检查文件格式。")
        sys.exit(1)
    except Exception as e:
        print(f"发生未知错误: {e}")
        sys.exit(1)

def generate_color_strip(colors, order):
    """
    根据颜色字典和指定的顺序生成一个色带图片。
    """
    print("\n开始生成色带图片...")

    # 计算最终图片的总尺寸
    total_width = IMAGE_SIZE[0] * len(order)
    height = IMAGE_SIZE[1]
    strip_image = Image.new("RGB", (total_width, height))

    current_x = 0
    # 按照指定的顺序遍历颜色
    for color_name in order:
        hex_color = colors.get(color_name)

        if not hex_color:
            print(f"警告: 在 JSON 中未找到颜色 '{color_name}'，将跳过。")
            continue

        try:
            # 创建一个纯色块
            color_block = Image.new("RGB", IMAGE_SIZE, color=hex_color)
            # 将色块粘贴到主图上
            strip_image.paste(color_block, (current_x, 0))
            current_x += IMAGE_SIZE[0]
            print(f"已粘贴: {color_name}")
        except ValueError as e:
            print(f"为 {color_name} (Hex: {hex_color}) 创建图片时出错: {e}")
            continue

    # 保存最终的图片
    strip_image.save(OUTPUT_FILENAME)
    print(f"\n成功生成图片: {OUTPUT_FILENAME}")
    print("\n所有任务已完成！")

def main():
    """
    主函数，用于解析命令行参数并运行生成器。
    """
    # 1. 设置命令行参数解析器
    parser = argparse.ArgumentParser(
        description="从 JSON 颜色定义文件生成一个色带 PNG 图片。"
    )
    # 添加一个必需的位置参数，用于接收 JSON 文件路径
    parser.add_argument(
        "json_file",
        type=str,
        help="包含颜色定义的输入 JSON 文件的路径。"
    )
    args = parser.parse_args()

    # 2. 从指定的 JSON 文件加载颜色
    all_colors = load_colors_from_json(args.json_file)

    # 3. 使用加载的颜色和预定义的顺序生成色带
    generate_color_strip(colors=all_colors, order=COLOR_ORDER)

if __name__ == "__main__":
    main()
