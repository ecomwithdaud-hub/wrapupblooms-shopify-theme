import urllib.request
import os

images_map = {
    # Hero & Banners
    "hero-banner.jpg": "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?auto=format&fit=crop&w=1920&q=80",
    "hero-mobile.jpg": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=800&q=80",
    "floral-texture.jpg": "https://images.unsplash.com/photo-1508615039623-a25605d2b022?auto=format&fit=crop&w=1920&q=80",
    
    # Products
    "product-lipstick-case.jpg": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80",
    "product-compact-mirror.jpg": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
    "product-jewelry-box.jpg": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=800&q=80",
    "product-bear-puzzle.jpg": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=800&q=80",
    "product-floral-keychain.jpg": "https://images.unsplash.com/photo-1611591475152-477d8c5ff770?auto=format&fit=crop&w=800&q=80",
    "product-bridesmaid-box.jpg": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=800&q=80",
    "product-acrylic-plaque.jpg": "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=800&q=80",
    "product-cosmetic-pouch.jpg": "https://images.unsplash.com/photo-1590439471364-192aa70c0b53?auto=format&fit=crop&w=800&q=80",
    
    # Story & Lookbook
    "story-artisan-craft.jpg": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1000&q=80",
    "lookbook-1.jpg": "https://images.unsplash.com/photo-1513094735237-8f2714d57c13?auto=format&fit=crop&w=600&q=80",
    "lookbook-2.jpg": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=600&q=80",
    "lookbook-3.jpg": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80",
    "lookbook-4.jpg": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=600&q=80"
}

dest_dirs = [
    "WrapUpBlooms-Theme/assets",
    "images",
    "preview/images"
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in images_map.items():
    print(f"Downloading {fname}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            for d in dest_dirs:
                target_path = os.path.join(d, fname)
                with open(target_path, "wb") as f:
                    f.write(data)
        print(f"Saved {fname} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {fname}: {e}")

print("All curated photographic assets downloaded successfully!")
