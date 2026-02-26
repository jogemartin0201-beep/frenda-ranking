import re
import os
from PIL import Image

html_file = "index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all IDs from DATA array
# Example: { id: "IMG_5180", ... }
matches = re.findall(r'{[^}]*id:\s*"([^"]+)"', html)

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"
os.makedirs(dest_dir, exist_ok=True)

# Target crop box (Pattern 1: Tight 1.5x zoom)
box = (195, 590, 975, 1110)

count = 0
not_found = set()

for img_id in set(matches):
    if img_id.startswith("NOIMG_"):
        continue
    
    # Check possible source file names
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

print(f"Recropped {count} images with Tight (1.5x) crop pattern.")
if not_found:
    print(f"Could not find source on desktop for {len(not_found)} images: {sorted(list(not_found))}")
