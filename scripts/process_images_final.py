import os
from PIL import Image

SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
DEST_DIR = "/Users/ryotaasai/frenda-ranking/public/images"
os.makedirs(DEST_DIR, exist_ok=True)

# Mapping rules from user
mapping = {}
for i in range(10):
    mapping[f"IMG_{5180+i}.PNG"] = f"{112+i:03d}"
for i in range(10):
    mapping[f"IMG_{5190+i}.PNG"] = f"{102+i:03d}"
for i in range(10):
    mapping[f"IMG_{5200+i}.PNG"] = f"{86+i:03d}"
for i in range(10):
    mapping[f"IMG_{5210+i}.PNG"] = f"{70+i:03d}"

def process_image(src_file, target_id):
    src_path = os.path.join(SRC_DIR, src_file)
    if not os.path.exists(src_path):
        return
    
    dest_path = os.path.join(DEST_DIR, f"{target_id}.png")
    
    try:
        with Image.open(src_path) as img:
            # iPhone Screenshot size is 1170x2532
            # Crop box: (left, upper, right, lower)
            # The top shiny effect now starts perfectly around y=310.
            # The bottom card ends around y=1920.
            box = (0, 310, 1170, 1920)
            cropped_img = img.crop(box)
            cropped_img.save(dest_path, "PNG")
            print(f"Processed {src_file} -> {target_id}.png")
    except Exception as e:
        print(f"Error processing {src_file}: {e}")

print("Processing images with Pillow...")
for src, tid in mapping.items():
    process_image(src, tid)
print("Done.")
