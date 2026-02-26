import os
from PIL import Image

src_dir = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
dest_dir = "images"
os.makedirs(dest_dir, exist_ok=True)

test_images = [
    ("IMG_5206.PNG", "gachiguma"),
    ("IMG_5198.PNG", "archaludon")
]

# Center X = 585
# Center Y = 850
crops = {
    "tight": (195, 590, 975, 1110),   # 1.5x zoom (used originally) -> 780x520
    "medium": (97, 525, 1072, 1175),  # 1.25x zoom -> 975x650
    "wide": (0, 460, 1170, 1240)      # 1.0x wide (full width) -> 1170x780
}

for img_file, name in test_images:
    src_path = os.path.join(src_dir, img_file)
    if os.path.exists(src_path):
        try:
            with Image.open(src_path) as img:
                for crop_name, box in crops.items():
                    cropped = img.crop(box)
                    dest_path = os.path.join(dest_dir, f"test_{name}_{crop_name}.png")
                    cropped.save(dest_path, "PNG")
                    print(f"Generated {dest_path}")
        except Exception as e:
            print(f"Error processing {img_file}: {e}")
    else:
        print(f"Could not find {src_path}")
