import os
import glob
from PIL import Image

# 1. Inject missing objects into index.html
with open('new_pokemon.js', 'r', encoding='utf-8') as f:
    new_objs = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '      { id: "120", season: "2-4", name: "カビゴン", type: "ノーマル", attack: 137, hasGimmick: true, gimmick: "テラスタル", category: "物理" },\n    ];'
# some formatting adjustments
replacement = '      { id: "120", season: "2-4", name: "カビゴン", type: "ノーマル", attack: 137, hasGimmick: true, gimmick: "テラスタル", category: "物理" },\n' + new_objs + '    ];'

if target in html:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html.replace(target, replacement))
    print("Injected new objects into index.html")
else:
    print("Error: Target JS end array not found in index.html")


# 2. Crop the newly copied NEW_*.png images
# Original images are full iPhone screenshots 1170x2532.
# We want the equivalent of cropped (0, 310, 1170, 1920) and then (195, 280, 975, 800)
# This results in an absolute original box of (195, 590, 975, 1110)
images = glob.glob("images/NEW_*.png")
box = (195, 590, 975, 1110)

count = 0
for img_path in images:
    try:
        with Image.open(img_path) as img:
            # Full crop in one go
            cropped = img.crop(box)
            cropped.save(img_path, "PNG")
            count += 1
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

print(f"Cropped {count} new images.")
