import os
import subprocess

SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
DEST_DIR = "/Users/ryotaasai/frenda-ranking/public/images"
os.makedirs(DEST_DIR, exist_ok=True)

# Mapping logic
# BT4: IMG_5180 -> ID 112
# BT3: IMG_5190 -> ID 102
# BT2: IMG_5200 -> ID 086
# BT1: IMG_5210 -> ID 070 (Estimated based on pattern)

def get_mapping():
    m = {}
    # BT4 (2-4)
    for i in range(10):
        m[f"IMG_{5180+i}.PNG"] = f"{112+i:03d}"
    # BT3 (2-3)
    for i in range(10):
        m[f"IMG_{5190+i}.PNG"] = f"{102+i:03d}"
    # BT2 (2-2)
    for i in range(10):
        m[f"IMG_{5200+i}.PNG"] = f"{086+i:03d}"
    # BT1 (2-1)
    for i in range(10):
        m[f"IMG_{5210+i}.PNG"] = f"{070+i:03d}"
    return m

def process(src, tid):
    src_path = os.path.join(SRC_DIR, src)
    if not os.path.exists(src_path):
        return False
        
    final_path = os.path.join(DEST_DIR, f"{tid}.png")
    temp_path = os.path.join(DEST_DIR, f"t_{tid}.png")
    
    # iPhone 1170x2532
    # The pick artwork is in the upper part.
    # We crop a 1300x1100 section slightly above center.
    subprocess.run(["sips", "--cropToHeightWidth", "1300", "1100", src_path, "--out", temp_path], capture_output=True)
    # Then crop the top half of that to get the card detail
    subprocess.run(["sips", "--cropToHeightWidth", "650", "950", temp_path, "--out", final_path], capture_output=True)
    
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return True

mapping = get_mapping()
print(f"Total mappings to process: {len(mapping)}")
success_count = 0
for src, tid in mapping.items():
    if process(src, tid):
        success_count += 1
        print(f"OK: {src} -> {tid}.png")
    else:
        print(f"FAIL: {src} not found")

print(f"Batch processing finished. Success: {success_count}/{len(mapping)}")
