import os
from PIL import Image

src_path = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真/IMG_5206.PNG"
dest_path = "images/IMG_5206_fixed.png"

# Pattern 1: 1.5x tight crop
box_oversized = (195, 590, 975, 1110)

if os.path.exists(src_path):
    with Image.open(src_path) as img:
        cropped = img.crop(box_oversized)
        cropped.save(dest_path, "PNG")
        print(f"Generated {dest_path}")
else:
    print(f"Could not find {src_path}")
