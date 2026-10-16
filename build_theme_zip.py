import zipfile
import os
import shutil

theme_dirs = ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']
output_zip = "WrapUpBlooms-Shopify-Theme.zip"

# Sync to WrapUpBlooms-Theme folder as well for backwards-compatibility
for d in theme_dirs:
    dest_dir = os.path.join("WrapUpBlooms-Theme", d)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(d, dest_dir)

if os.path.exists(output_zip):
    os.remove(output_zip)

with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for d in theme_dirs:
        for root, dirs, files in os.walk(d):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ".")
                zf.write(full_path, rel_path)
                print(f"Added to zip: {rel_path}")

print(f"\nSuccessfully generated {output_zip} ({os.path.getsize(output_zip)} bytes)!")

