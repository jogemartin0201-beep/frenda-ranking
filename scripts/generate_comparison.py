import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "/Users/ryotaasai/.gemini/antigravity/brain/6093d02a-3de6-4865-b17d-a4fb69e4a681/"

imgs = {
    "Ursaluna_Original": "IMG_5206.PNG",
    "Snorlax_Original": "IMG_5188.PNG"
}

for name, filename in imgs.items():
    path = os.path.join(src_dir, filename)
    if os.path.exists(path):
        with Image.open(path) as img:
            # Resize a bit to fit in markdown reasonably
            img.thumbnail((400, 800))
            img.save(os.path.join(dest_dir, f"{name}.png"), "PNG")
    else:
        print(f"Not found: {path}")

# Also generate the exact crop again just to be double sure
box = (195, 590, 975, 1110)
for name, filename in imgs.items():
    path = os.path.join(src_dir, filename)
    if os.path.exists(path):
        with Image.open(path) as img:
            cropped = img.crop(box)
            cropped.thumbnail((400, 400)) # to match sizing
            cropped.save(os.path.join(dest_dir, f"{name}_cropped.png"), "PNG")

print("Created thumbnails for comparison.")
