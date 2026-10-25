import os, sys
os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
from playwright.sync_api import sync_playwright

src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file://" + os.path.abspath(src))
    pg.wait_for_timeout(500)
    pg.pdf(path=out, prefer_css_page_size=True, print_background=True)
    b.close()
print("ok", out)
