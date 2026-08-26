"""Bundle index.html + img/ into a single self-contained HTML file.

Useful for emailing the page or opening it offline — every image becomes a
base64 data URI, so the result has no local dependencies at all.

    python tools/inline.py                  -> pocket-home-standalone.html
    python tools/inline.py out.html         -> custom output name

Only Google Fonts is still fetched from the network; the page falls back to
system fonts without it.
"""

import base64
import mimetypes
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
DST = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else "pocket-home-standalone.html")


def main():
    html = open(SRC, encoding="utf8").read()
    cache = {}

    def swap(m):
        rel = m.group(1)
        if rel not in cache:
            path = os.path.join(ROOT, rel.replace("/", os.sep))
            mime = mimetypes.guess_type(path)[0] or "image/jpeg"
            data = base64.b64encode(open(path, "rb").read()).decode("ascii")
            cache[rel] = f"data:{mime};base64,{data}"
        return cache[rel]

    html, n = re.subn(r'(img/[\w.-]+\.jpg)', swap, html)
    open(DST, "w", encoding="utf8").write(html)
    print(f"inlined {n} references ({len(cache)} unique files)")
    print(f"wrote {DST} ({len(html.encode('utf8')) / 1048576:.2f} MB)")


if __name__ == "__main__":
    main()
