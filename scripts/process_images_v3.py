import os
import subprocess

SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
DEST_DIR = "/Users/ryotaasai/frenda-ranking/public/images"
os.makedirs(DEST_DIR, exist_ok=True)

# User's mapping:
# IMG_5180 -> 2-4 001 (Zygarde, ID: 112)
# IMG_5181 -> 2-4 002 (Giratina, ID: 113)
# IMG_5182 -> 2-4 003 (Regigigas, ID: 114)
# Sequential mapping follows.

# Master data IDs:
# 2-4: 112-121 (10 images starting at IMG_5180)
# 2-3: 102-111 (10 images starting at IMG_5190)
# 2-2: 086-095 (10 images starting at IMG_5200)
# 2-1: 070-079 (10 images starting at IMG_5210?)
# 1-5: 054-063 ... and so on.

mapping = {}
# BT4 (2-4)
for i in range(10):
    mapping[f"IMG_{5180+i}.PNG"] = f"{112+i:03d}"
# BT3 (2-3)
for i in range(10):
    mapping[f"IMG_{5190+i}.PNG"] = f"{102+i:03d}"
# BT2 (2-2)
for i in range(10):
    mapping[f"IMG_{5200+i}.PNG"] = f"{086+i:03d}"
# BT1 (2-1)
for i in range(10):
    mapping[f"IMG_{5210+i}.PNG"] = f"{070+i:03d}"

def process_one(src_name, target_id):
    src_path = os.path.join(SRC_DIR, src_name)
    if not os.path.exists(src_path):
        return
        
    final_path = os.path.join(DEST_DIR, f"{target_id}.png")
    
    # Crop artwork section using sips
    # The pick is in the upper part of the iPhone screenshot (1170x2532)
    # Target: 900x600 centered slightly above the middle
    # Center crop 1200x1200 first
    temp_path = os.path.join(DEST_DIR, f"tmp_{target_id}.png")
    subprocess.run(["sips", "--cropToHeightWidth", "1300", "1100", src_path, "--out", temp_path], capture_output=True)
    
    # Crop the top part of the center-cropped image where the pick is
    subprocess.run(["sips", "--cropToHeightWidth", "650", "950", temp_path, "--out", final_path], capture_output=True)
    
    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"Processed {src_name} -> {target_id}.png")

print("Processing images...")
for src, tid in mapping.items():
    process_one(src, tid)
print("Done.")
