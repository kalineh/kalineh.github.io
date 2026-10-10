#!/usr/bin/env python3
"""Generate short-link redirect pages from links.json.
Each key becomes /<key>/index.html that forwards to its URL.
Edit links.json, run `python3 build_links.py`, commit and push."""
import json, os, html, shutil
links = json.load(open("links.json"))
for d in json.load(open(".generated.json")) if os.path.exists(".generated.json") else []:
    if d not in links and os.path.isdir(d): shutil.rmtree(d)
for key, url in links.items():
    os.makedirs(key, exist_ok=True)
    u = html.escape(url, quote=True)
    with open(os.path.join(key, "index.html"), "w") as f:
        f.write(f'''<!doctype html><html><head><meta charset="utf-8">
<title>kalin.games/{key}</title>
<link rel="canonical" href="{u}"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={u}">
<script>location.replace({json.dumps(url)})</script></head>
<body><p>Redirecting to <a href="{u}">{u}</a></p></body></html>
''')
json.dump(sorted(links), open(".generated.json", "w"))
print("built", len(links), "links")
