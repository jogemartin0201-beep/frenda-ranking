import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"

# We will check based on the IDs
# Gachiguma is IMG_5206
# Snorlax is IMG_5xxx (need to find out)

def check_image(img_name):
    path = os.path.join(src_dir, img_name)
    if os.path.exists(path):
        with Image.open(path) as img:
            print(f"{img_name}: {img.size}, format: {img.format}, mode: {img.mode}")
    else:
        print(f"Not found: {path}")

check_image("IMG_5206.PNG") # Gachiguma
# Snorlax checking logic will be added via bash once we know the ID
