import os
from PIL import Image

src_path = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真/IMG_5206.PNG"
dest_path = "images/IMG_5206_fixed.png"

# Pattern 2: 1.25x crop (the one that makes Gachiguma look like Snorlax 1.5x)
box_oversized = (97, 525, 1072, 1175)

if os.path.exists(src_path):
    with Image.open(src_path) as img:
        cropped = img.crop(box_oversized)
        cropped.save(dest_path, "PNG")
        print(f"Generated {dest_path}")
else:
    print(f"Could not find {src_path}")
