import os

theme_dirs = [
    "WrapUpBlooms-Theme/assets",
    "WrapUpBlooms-Theme/config",
    "WrapUpBlooms-Theme/layout",
    "WrapUpBlooms-Theme/locales",
    "WrapUpBlooms-Theme/sections",
    "WrapUpBlooms-Theme/snippets",
    "WrapUpBlooms-Theme/templates",
    "images",
    "preview"
]

for d in theme_dirs:
    os.makedirs(d, exist_ok=True)

print("Theme directories created successfully.")
