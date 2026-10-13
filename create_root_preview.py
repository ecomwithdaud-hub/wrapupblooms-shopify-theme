import re

with open("preview/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace paths for root execution
content_root = content.replace("../WrapUpBlooms-Theme/assets/", "WrapUpBlooms-Theme/assets/")

with open("live-preview.html", "w", encoding="utf-8") as f:
    f.write(content_root)

print("Created live-preview.html at workspace root!")
