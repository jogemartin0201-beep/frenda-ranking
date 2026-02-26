import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
imgs = ["IMG_5188.PNG", "IMG_5206.PNG", "IMG_5198.PNG"]

for i in imgs:
    path = os.path.join(src_dir, i)
    if os.path.exists(path):
        with Image.open(path) as img:
            print(f"{i}: size={img.size}")
    else:
        print(f"Not found: {i}")

