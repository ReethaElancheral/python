# 3. Image Pixel Color Analyzer

# Goal: Work with image pixel RGB color values.
# Requirements:
# Store RGB values as (R, G, B) tuples.
# Use a list of tuples to represent image pixels.
# Count how many pixels match a specific color using .count().
# Slice the pixel list to analyze a subregion.
# Return dominant colors using tuple frequency.


pixels = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 0, 0), (255, 0, 0), (0, 255, 0),
    (128, 128, 128), (0, 0, 0), (255, 255, 255)
]


target_color = (255, 0, 0)
red_count = pixels.count(target_color)
print(f"Red pixels: {red_count}")


subregion = pixels[2:7]
print("Subregion pixels:", subregion)


def dominant_color(pixel_list):
    unique = set(pixel_list)
    return max(unique, key=pixel_list.count)

dom = dominant_color(pixels)
print("Dominant color:", dom)

print("Dominant in subregion:", dominant_color(subregion))
