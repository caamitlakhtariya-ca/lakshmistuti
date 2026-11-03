"""Render a verse's sketch note to assets/sketch/<file>.png (needs the local server on :8765 and Playwright)."""
import sys
from playwright.sync_api import sync_playwright
slug, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 900}, device_scale_factor=2, color_scheme="light")
    pg.goto(f"http://localhost:8765/{slug}/"); pg.wait_for_timeout(600)
    pg.evaluate("""()=>{const c=document.querySelector('.ov-sketch');
      c.querySelector('.ov-h').textContent=document.querySelector('h1').textContent;
      c.querySelector('.sk-cap').textContent='lakshmistuti.com  ·  Amit N. Lakhtariya';
      c.querySelectorAll('.sk-act').forEach(e=>e.remove());
      c.style.cssText='width:820px;padding:28px 34px;border:0;background:#fdf6e6;box-shadow:none;border-radius:0';}""")
    pg.locator(".ov-sketch").screenshot(path=out)
    b.close()
