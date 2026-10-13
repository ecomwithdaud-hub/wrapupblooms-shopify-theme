import os
import shutil

pages = [
    "index.html",
    "pocket-mirrors.html",
    "jewelry-boxes.html",
    "our-story.html",
    "reviews.html",
    "contact.html"
]

# Sync index.html to live-preview.html
shutil.copy2("index.html", "live-preview.html")
print("Synced live-preview.html")

# Sync all pages into preview/ directory with relative path ../WrapUpBlooms-Theme/assets/
os.makedirs("preview", exist_ok=True)
for page in pages:
    with open(page, "r", encoding="utf-8") as f:
        content = f.read()
    preview_content = content.replace("WrapUpBlooms-Theme/assets/", "../WrapUpBlooms-Theme/assets/")
    dst = os.path.join("preview", page)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(preview_content)
    print(f"Synced preview/{page}")

shutil.copy2("favicon.svg", "preview/favicon.svg")
shutil.copy2("favicon.png", "preview/favicon.png")
print("Synced preview favicons")

print("All standalone pages synced successfully!")
