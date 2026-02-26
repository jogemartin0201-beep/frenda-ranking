import os
from PIL import Image

SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
DEST_DIR = "/Users/ryotaasai/frenda-ranking/public/images"
os.makedirs(DEST_DIR, exist_ok=True)

# ユーザー指定の3コンポーネントのみを抽出してテスト
# レジギガス (BT4): IMG_5182 -> 114
# エルレイド (BT3): IMG_5196 -> 108
# ルカリオ(BT1) : IMG_5217 -> 077
test_mapping = {
    "IMG_5182.PNG": "114",
    "IMG_5196.PNG": "108",
    "IMG_5217.PNG": "077"
}

def process_test_image(src_file, target_id):
    src_path = os.path.join(SRC_DIR, src_file)
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return
    
    dest_path = os.path.join(DEST_DIR, f"{target_id}.png")
    
    try:
        with Image.open(src_path) as img:
            # 前回: (0, 150, 1170, 1850)
            # 修正: 左右のはみ出しを防ぎ、少し縮小させるために、あえて余白を含めるか
            # あるいはもっと広い範囲を指定してCSSでフィットさせる。（ただしCSS側はobject-fit:coverの可能性が高い）
            # ユーザー指示により、Y座標を 280 -> 310 に設定して更に上部をクリッピング
            box = (0, 310, 1170, 1920)
            cropped_img = img.crop(box)
            cropped_img.save(dest_path, "PNG")
            print(f"Processed TEST {src_file} -> {target_id}.png")
    except Exception as e:
        print(f"Error processing {src_file}: {e}")

print("Processing 3 TEST images with expanded crop area...")
for src, tid in test_mapping.items():
    process_test_image(src, tid)
print("TEST Done.")
