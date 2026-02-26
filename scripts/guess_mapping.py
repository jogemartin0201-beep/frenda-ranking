import os

SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真"
files = sorted([f for f in os.listdir(SRC_DIR) if f.startswith("IMG_") and f.endswith(".PNG")])

# 現在判明しているマッピングの基準点
# IMG_5180 -> 112 (BT4弾開始)
# IMG_5190 -> 102 (BT3弾開始)
# IMG_5200 -> 086 (BT2弾開始)
# IMG_5210 -> 070 (BT1弾開始)

print(f"Total files: {len(files)}")
print(f"First file: {files[0]}, Last file: {files[-1]}")

# 逆算してみる
# リストの後ろ (IMG_5219 以降) が 1弾や5弾などにどう対応するか
# 1-5弾 (054-063), W弾など
# 5219 までが BT1弾。
# 5220 以降に 76ファイルある。
# IDの残り (001-069 + W/Legacy) はどうなるか？

# Let's print the latter files to inspect
print("Files after 5219:")
print(files[files.index("IMG_5220.PNG"):files.index("IMG_5220.PNG")+10])

# とりあえず名前順に表示してIDを割り当てるベースとなるマップを作る
