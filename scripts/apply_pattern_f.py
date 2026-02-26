import os
import re
from PIL import Image

html_file = "index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern F: 150px down from base (195, 590, 975, 1110)
shift_down = 150
box_shifted = (195, 590 + shift_down, 975, 1110 + shift_down)

# The specific IDs to shift
def is_target(img_id):
    if not img_id.startswith("IMG_"): return False
    num_str = img_id.replace("IMG_", "")
    if not num_str.isdigit(): return False
    num = int(num_str)
    return (5240 <= num <= 5249) or (5260 <= num <= 5269)

matches = re.findall(r'{[^}]*id:\s*"([^"]+)"', html)

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"

count = 0
for img_id in set(matches):
    if is_target(img_id):
        src_path_PNG = os.path.join(src_dir, f"{img_id}.PNG")
        src_path_png = os.path.join(src_dir, f"{img_id}.png")
        src_path = src_path_PNG if os.path.exists(src_path_PNG) else src_path_png
        
        if os.path.exists(src_path):
            dest_path = os.path.join(dest_dir, f"{img_id}.png")
            try:
                with Image.open(src_path) as img:
                    cropped = img.crop(box_shifted)
                    cropped.save(dest_path, "PNG")
                    count += 1
            except Exception as e:
                print(f"Error processing {src_path}: {e}")

print(f"Applied 150px downward shift (Pattern F) to {count} misaligned images.")
