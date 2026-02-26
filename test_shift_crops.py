import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"
os.makedirs(dest_dir, exist_ok=True)

test_image = "IMG_5240.PNG"

# Base Pattern 1: Tight 1.5x zoom
# Original box: (195, 590, 975, 1110)
base_left = 195
base_right = 975

# We need to SHIFT THE CROP BOX DOWN (increase Y values)
# so the content shifts UP in the final extracted image.
shifts = {
    "shift_down_50": 50,
    "shift_down_100": 100,
    "shift_down_150": 150
}

src_path = os.path.join(src_dir, test_image)

if os.path.exists(src_path):
    try:
        with Image.open(src_path) as img:
            for name, offset in shifts.items():
                box = (
                    base_left, 
                    590 + offset, 
                    base_right, 
                    1110 + offset
                )
                cropped = img.crop(box)
                dest_path = os.path.join(dest_dir, f"test_{name}.png")
                cropped.save(dest_path, "PNG")
                print(f"Generated {dest_path}")
    except Exception as e:
        print(f"Error processing {test_image}: {e}")
else:
    print(f"Could not find {src_path}")
