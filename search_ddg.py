import urllib.request
import json
import urllib.parse
import re

query = 'WrapUpBlooms etsy'
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print("DDG results length:", len(html))
        links = re.findall(r'<a[^>]+class="[^"]*result__a[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html)
        for l, t in links[:10]:
            print("TITLE:", re.sub('<[^<]+?>', '', t).strip(), "URL:", l)
        snippets = re.findall(r'<a[^>]+class="[^"]*result__snippet[^"]*"[^>]*>(.*?)</a>', html)
        for s in snippets[:10]:
            print("SNIPPET:", re.sub('<[^<]+?>', '', s).strip())

except Exception as e:
    print("Error:", e)
