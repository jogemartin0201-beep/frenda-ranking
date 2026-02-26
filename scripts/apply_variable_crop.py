import re
import os
from PIL import Image

html_file = "index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Default crop box (Pattern 1: Tight 1.5x zoom)
box_default = (195, 590, 975, 1110)
# Custom crop box for Oversized pokemon (Pattern 2: Medium 1.25x zoom)
box_oversized = (97, 525, 1072, 1175)

# List of SearchNames for Pokémon that appear too large and need pattern 2
oversized_names = [
    "ガチグマ", "Ursaluna", 
    "ブリジュラス", "Archaludon",
    "ホウオウ", "Ho-Oh", 
    "レジギガス", "Regigigas",
    "ギラティナ", "Giratina",
    "バンギラス", "Tyranitar",
    "ギャラドス", "Gyarados"
]

matches = re.findall(r'{[^}]*id:\s*"([^"]+)"[^}]*searchName:\s*"([^"]+)"', html)
# This gives a list of tuples: (id, searchName)

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"
os.makedirs(dest_dir, exist_ok=True)

count_default = 0
count_oversized = 0

for img_id, search_name in matches:
    if img_id.startswith("NOIMG_"):
        continue
        
    src_path_PNG = os.path.join(src_dir, f"{img_id}.PNG")
    src_path_png = os.path.join(src_dir, f"{img_id}.png")
    src_path = src_path_PNG if os.path.exists(src_path_PNG) else src_path_png
    
    if os.path.exists(src_path):
        is_oversized = any(o_name in search_name for o_name in oversized_names)
        current_box = box_oversized if is_oversized else box_default
        
        dest_path = os.path.join(dest_dir, f"{img_id}.png")
        try:
            with Image.open(src_path) as img:
                cropped = img.crop(current_box)
                cropped.save(dest_path, "PNG")
                if is_oversized:
                    count_oversized += 1
                else:
                    count_default += 1
        except Exception as e:
            print(f"Error processing {src_path}: {e}")

print(f"Applied 1.5x tight crop to {count_default} standard images.")
print(f"Applied 1.25x medium crop to {count_oversized} oversized images.")
