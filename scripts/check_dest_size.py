import os
from PIL import Image

dest_dir = "images"
imgs = ["IMG_5188.png", "IMG_5206.png", "IMG_5198.png"]

for i in imgs:
    path = os.path.join(dest_dir, i)
    if os.path.exists(path):
        with Image.open(path) as img:
            print(f"{i}: size={img.size}")
    else:
        print(f"Not found: {i}")
