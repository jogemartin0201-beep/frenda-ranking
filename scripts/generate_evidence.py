import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "/Users/ryotaasai/.gemini/antigravity/brain/6093d02a-3de6-4865-b17d-a4fb69e4a681"

snorlax_src = os.path.join(src_dir, "IMG_5188.PNG")
gachi_src = os.path.join(src_dir, "IMG_5206.PNG")

# The exact 1.5x crop box we use for Pattern 1
box_1_5 = (195, 590, 975, 1110)

def process(src_path, prefix):
    if not os.path.exists(src_path):
        print(f"Not found: {src_path}")
        return
    with Image.open(src_path) as img:
        # Scale down original just so it's not a massive 5MB file in markdown, but keep ratio
        orig_thumb = img.copy()
        orig_thumb.thumbnail((600, 1200))
        orig_thumb.save(os.path.join(dest_dir, f"{prefix}_orig.png"))
        
        # Exact mathematical crop
        cr_1_5 = img.crop(box_1_5)
        cr_1_5.save(os.path.join(dest_dir, f"{prefix}_crop.png"))

process(snorlax_src, "snorlax")
process(gachi_src, "gachi")

print("Generated evidence images.")
