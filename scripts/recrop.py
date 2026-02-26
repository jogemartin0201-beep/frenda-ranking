import re
import os
from PIL import Image

html_file = "index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all IDs from DATA array
# Example: { id: "IMG_5180", ... }
matches = re.findall(r'{[^}]*id:\s*"([^"]+)"', html)
# We might also have NOIMG_ ids, which we can ignore if there's no source image.
# We also want to recrop the existing 112.png etc if they are present in the desktop folder.
# Wait, actually the original images on desktop areIMG_XXXX.PNG. "112.png" might not correspond to "112.png" on desktop.
# Let's check what images are on the desktop.
src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"

# Target crop box (full width, 1.5 ratio)
box = (0, 310, 1170, 1090)

count = 0
not_found = set()

for img_id in set(matches):
    if img_id.startswith("NOIMG_"):
        continue
    
    # Check possible source file names
    # Usually IMG_XXXX.PNG
    src_path_PNG = os.path.join(src_dir, f"{img_id}.PNG")
    src_path_png = os.path.join(src_dir, f"{img_id}.png")
    
    src_path = src_path_PNG if os.path.exists(src_path_PNG) else src_path_png
    
    if os.path.exists(src_path):
        dest_path = os.path.join(dest_dir, f"{img_id}.png")
        try:
            with Image.open(src_path) as img:
                cropped = img.crop(box)
                cropped.save(dest_path, "PNG")
                count += 1
        except Exception as e:
            print(f"Error processing {src_path}: {e}")
    else:
        not_found.add(img_id)

print(f"Recropped {count} images with full-width horizontal crop.")
if not_found:
    print(f"Could not find source on desktop for {len(not_found)} images: {sorted(list(not_found))}")
