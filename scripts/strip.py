from PIL import Image
import os
from collections import OrderedDict

ALL_COLORS = {
        "Text": "#F4F9E3",
        "Subtext1": "#E0E6D0",
        "Subtext0": "#CCD2BD",
        "Overlay2": "#9EA0B6",
        "Overlay1": "#8C8DA3",
        "Overlay0": "#7A7B91",
        "Surface2": "#686A7F",
        "Surface1": "#58596D",
        "Surface0": "#47495C",
        "Base": "#292A3C",
        "Mantle": "#303143",
        "Crust": "#38394C",
        "Rosewater": "#F5E0DC",
        "Flamingo": "#F2CDCD",
        "Pink": "#F5C2E7",
        "Mauve": "#CBA6F7",
        "Red": "#F38BA8",
        "Maroon": "#EBA0AC",
        "Peach": "#FAB387",
        "Yellow": "#F9E2AF",
        "Green": "#A6E3A1",
        "Teal": "#94E2D5",
        "Sky": "#89DCEB",
        "Sapphire": "#74C7EC",
        "Blue": "#89B4FA",
        "Lavender": "#B4BEFE"
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

IMAGE_SIZE = (20, 50)
OUTPUT_FILENAME = "color_strip.png"


def generate_color_strip():

    print("\nStarting color strip generation...")

    total_width = IMAGE_SIZE[0] * len(COLOR_ORDER)
    height = IMAGE_SIZE[1]

    strip_image = Image.new("RGB", (total_width, height))

    current_x = 0

    for color_name in COLOR_ORDER:
        hex_color = ALL_COLORS.get(color_name)

        if not hex_color:
            print(f"Warning: Color '{color_name}' not found in definitions. Skipping.")
            continue

        try:

            color_block = Image.new("RGB", IMAGE_SIZE, color=hex_color)


            strip_image.paste(color_block, (current_x, 0))


            current_x += IMAGE_SIZE[0]

            print(f"Pasted: {color_name}")

        except ValueError as e:
            print(f"Error creating image for {color_name} with hex {hex_color}: {e}")
            continue


    strip_image.save(OUTPUT_FILENAME)
    print(f"\nSuccessfully generated: {OUTPUT_FILENAME}")
    print("\nAll tasks completed. Your color strip is ready!")


if __name__ == "__main__":
    generate_color_strip()
