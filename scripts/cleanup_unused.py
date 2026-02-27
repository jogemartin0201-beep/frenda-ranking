import os
import re

html_file = "/Users/ryotaasai/frenda-ranking/index.html"
img_dir = "/Users/ryotaasai/frenda-ranking/images"

# 1. Get all valid IDs from index.html
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'{[^}]*id:\s*"([^"]+)"', html)
valid_images = {f"{m}.png" for m in set(matches) if not m.startswith("NOIMG_")}

# Also keep placeholders if any exist, but we only have placehold.co
# 2. Delete unreferenced files in images/
deleted_images = 0
for filename in os.listdir(img_dir):
    if filename.endswith(".png") and filename not in valid_images:
        os.remove(os.path.join(img_dir, filename))
        deleted_images += 1

print(f"Deleted {deleted_images} unused images.")

# 3. Clean up root and scripts directory
useless_files = [
    "/Users/ryotaasai/frenda-ranking/images.zip",
    "/Users/ryotaasai/frenda-ranking/test_shift_crops.py",
    "/Users/ryotaasai/frenda-ranking/scripts/debug_jimp.js",
    "/Users/ryotaasai/frenda-ranking/scripts/process_improved.js",
    "/Users/ryotaasai/frenda-ranking/scripts/test_crop_3images.py",
    "/Users/ryotaasai/frenda-ranking/scripts/guess_mapping.py",
    "/Users/ryotaasai/frenda-ranking/scripts/process_images_final.py",
    "/Users/ryotaasai/frenda-ranking/scripts/generate_gachiguma.py",
    "/Users/ryotaasai/frenda-ranking/scripts/prepare_upload.py",
    "/Users/ryotaasai/frenda-ranking/scripts/crop_gachi_standard.py",
    "/Users/ryotaasai/frenda-ranking/scripts/fix_oversized_only.py",
    "/Users/ryotaasai/frenda-ranking/scripts/apply_pattern_f.py",
    "/Users/ryotaasai/frenda-ranking/scripts/apply_variable_crop.py"
]

deleted_scripts = 0
for uf in useless_files:
    if os.path.exists(uf):
        os.remove(uf)
        deleted_scripts += 1

print(f"Deleted {deleted_scripts} obsolete test scripts and zip files.")
