import zipfile
import os

theme_source_dir = "WrapUpBlooms-Theme"
output_zip = "WrapUpBlooms-Shopify-Theme.zip"

if os.path.exists(output_zip):
    os.remove(output_zip)

with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(theme_source_dir):
        for file in files:
            full_path = os.path.join(root, file)
            # Store relative path so assets/, config/, layout/, etc are at the zip root
            rel_path = os.path.relpath(full_path, theme_source_dir)
            zf.write(full_path, rel_path)
            print(f"Added to zip: {rel_path}")

print(f"\nSuccessfully generated {output_zip} ({os.path.getsize(output_zip)} bytes)!")
