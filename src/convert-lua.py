#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

def json_to_lua(data):
    """
    将特定的JSON结构转换为Lua table字符串，并在类别之间添加空行。

    Args:
        data (dict): 解析后的JSON数据。

    Returns:
        str: 一个格式化为Lua table的字符串，可直接用于Lua。
    """
    lua_parts = []
    
    # 获取JSON中所有顶级键的列表，以便判断何时到达最后一个
    categories = list(data.keys())
    
    # 使用 enumerate 来同时获取索引和键名
    for i, category_name in enumerate(categories):
        # 遍历每个类别中的颜色项目列表
        for item in data[category_name]:
            name = item.get("Name")
            hex_code = item.get("Hex")
            
            if name and hex_code:
                # 将名称转换为小写以匹配Lua变量风格
                lua_name = name.lower()
                # 格式化为Lua table的一行
                lua_parts.append(f'    {lua_name} = "{hex_code}",')

        # 如果当前类别不是最后一个，就在其后添加一个空行
        if i < len(categories) - 1:
            lua_parts.append('')

    # 将所有部分连接起来，并用Lua table的结构包装
    # 使用 return { ... } 的格式，使其在Lua中可以通过 require() 加载
    return "return {\n" + "\n".join(lua_parts) + "\n}"

def main():
    """
    主函数，处理文件输入/输出和转换逻辑。
    """
    # 检查是否提供了正确数量的命令行参数
    if len(sys.argv) != 2:
        print("用法: python convert-lua.py <json_file_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]

    try:
        # 打开并读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as f:
            # 注意：对于Python 3.7+，字典会保持插入顺序，这对于此逻辑至关重要。
            # 如果使用更早版本的Python，可能需要使用 collections.OrderedDict。
            json_data = json.load(f)
        
        # 将JSON数据转换为Lua table字符串
        lua_output = json_to_lua(json_data)
        
        # 打印最终结果
        print(lua_output)

    except FileNotFoundError:
        print(f"错误: 文件 '{json_file_path}' 未找到。", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"错误: 文件 '{json_file_path}' 中的JSON格式无效。", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"发生意外错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
