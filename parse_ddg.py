with open('ddg.html', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, re.DOTALL)
print(f"Total links: {len(matches)}")
for href, title in matches:
    clean_title = re.sub(r'<[^>]+>', '', title).strip()
    if any(k in href.lower() or k in clean_title.lower() for k in ['etsy', 'wrap', 'bloom']):
        print(f"URL: {href}")
        print(f"TITLE: {clean_title}")
        print("-" * 40)
