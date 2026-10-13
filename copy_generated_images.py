import shutil
import os

generated_files = {
    r"C:\Users\user\.gemini\antigravity\brain\7912b088-e69f-4897-b47d-071046082756\hero_banner_1791916660959.jpg": "hero-bespoke-banner.jpg",
    r"C:\Users\user\.gemini\antigravity\brain\7912b088-e69f-4897-b47d-071046082756\product_lipstick_keychain_1791916738457.jpg": "bespoke-lipstick-keychain.jpg",
    r"C:\Users\user\.gemini\antigravity\brain\7912b088-e69f-4897-b47d-071046082756\product_compact_mirror_1791916787697.jpg": "bespoke-compact-mirror.jpg"
}

target_dirs = [
    "WrapUpBlooms-Theme/assets",
    "images",
    "preview/images"
]

for src, target_name in generated_files.items():
    if os.path.exists(src):
        for tdir in target_dirs:
            dst = os.path.join(tdir, target_name)
            shutil.copy2(src, dst)
            print(f"Copied {src} -> {dst}")
    else:
        print(f"Source not found: {src}")

print("Copied all generated assets successfully.")
