from colorsys import rgb_to_hsv
from colorsys import hsv_to_rgb

print(rgb_to_hsv(1, 0, 0))
print(*(round(f * 255) for f in hsv_to_rgb(0.4, 1, 1)))