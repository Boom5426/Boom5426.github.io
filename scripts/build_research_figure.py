#!/usr/bin/env python3
"""Build the homepage research-loop figure: panels (a)-(d) from the v1 artwork plus strand (e).

Inputs, kept in docs/figure-src/ (excluded from the Jekyll build):
  research_loop_v1.webp           2400 px wide four-panel artwork, panels side by side
  research_loop_vertical_v1.webp   940 px wide four-panel artwork, panels stacked (phones)

Outputs, written to images/:
  research_loop.webp (2400 px), research_loop_1200.webp, research_loop_vertical.webp

Panels (a)-(d) and the Experiment pill are reused pixel for pixel. The loop band is
redrawn: (d) -> Experiment -> (e) Self-improving Models -> back into (b). Pillow crops
the v1 art, Chrome (driven by Playwright) draws the new band in HTML/SVG with rough.js
strokes and the Kalam / Noto Sans fonts, and Pillow writes the WebP files. Chrome
fetches the fonts and rough.js from public CDNs, so the build needs network access.

usage: python3 scripts/build_research_figure.py [--chrome /usr/bin/google-chrome]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "figure-src"
OUT = ROOT / "images"

# Geometry of the v1 artwork, measured from the files above (pixels).
H_PANEL_BOTTOM = 596             # panels (a)-(d) end at y~592; the old loop band starts below
H_PILL_BOX = (803, 632, 1600, 760)  # Experiment pill incl. the pipette, in the v1 band
H_B_CENTER_X = 894               # horizontal centre of panel (b)
H_D_LINE_X = 2114                # where the old red line leaves panel (d)
V_MARGIN = 128                   # vertical art: everything left of x=128 is the old loop line
V_B_CENTER_Y = 1360              # vertical centre of panel (b) in the stacked art
V_PILL_BOTTOM = 3905             # bottom of the Experiment pill in the stacked art

ROUGH_JS = "https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"
FONTS_CSS = ("https://fonts.googleapis.com/css2?family=Kalam:wght@400;700"
             "&family=Noto+Sans:wght@400;600;700&display=block")

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="__FONTS__"><script src="__ROUGH__"></script>
<style>
  html, body { margin: 0; background: #fff; }
  body { position: relative; width: __W__px; height: __H__px; overflow: hidden; }
  body > img, #ink, .t { position: absolute; }
  .hand { font-family: Kalam, cursive; }
  .sans { font-family: 'Noto Sans', sans-serif; }
  .ebox { position: absolute; display: flex; flex-direction: column; align-items: center;
          justify-content: space-evenly; box-sizing: border-box; }
  .etitle { position: absolute; display: flex; align-items: center; justify-content: center; color: #1a2433; }
  .elabel { position: absolute; color: #6c4fa3; }
  .works { color: #6c4fa3; font-weight: 700; }
  .q { color: #5f6876; }
  .row { display: flex; align-items: flex-start; }
  .cell { display: flex; flex-direction: column; align-items: center; color: #3a4250; }
  .loop { color: #c23829; white-space: nowrap; }
</style></head><body>
__IMGS__
<svg id="ink" width="__W__" height="__H__" style="left:0;top:0"></svg>
__TEXT__
<script>
const C = __CFG__;
const svg = document.getElementById('ink');
const rc = rough.svg(svg);
const INK = '#2f3642', RED = '#c23829';
const add = el => svg.appendChild(el);
function node(tag, attrs) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const k in attrs) el.setAttribute(k, attrs[k]);
  return el;
}
function rr(x, y, w, h, r) {
  return `M${x + r},${y} H${x + w - r} Q${x + w},${y} ${x + w},${y + r} V${y + h - r} Q${x + w},${y + h} ${x + w - r},${y + h}`
       + ` H${x + r} Q${x},${y + h} ${x},${y + h - r} V${y + r} Q${x},${y} ${x + r},${y} Z`;
}
function topRR(x, y, w, h, r) {
  return `M${x},${y + h} V${y + r} Q${x},${y} ${x + r},${y} H${x + w - r} Q${x + w},${y} ${x + w},${y + r} V${y + h} Z`;
}
const opt = (o) => Object.assign({roughness: 0.55, bowing: 0.6, seed: 7}, o);
function line(pts, color, width) {
  for (let i = 0; i + 1 < pts.length; i++)
    add(rc.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], opt({stroke: color, strokeWidth: width})));
}
function head(x, y, dir, s) {          // filled arrowhead with its tip at (x, y)
  const p = {up: [[x, y], [x - s * .62, y + s], [x + s * .62, y + s]],
             down: [[x, y], [x - s * .62, y - s], [x + s * .62, y - s]],
             left: [[x, y], [x + s, y - s * .62], [x + s, y + s * .62]],
             right: [[x, y], [x - s, y - s * .62], [x - s, y + s * .62]]}[dir];
  add(node('polygon', {points: p.map(q => q.join(',')).join(' '), fill: INK, stroke: INK,
                       'stroke-width': 2, 'stroke-linejoin': 'round'}));
}
function ebox(b) {                     // panel (e): fills, header, rough outline
  add(node('path', {d: rr(b.x, b.y, b.w, b.h, b.r), fill: '#f6f2fc'}));
  add(node('path', {d: topRR(b.x, b.y, b.w, b.hh, b.r), fill: '#ddd3f0'}));
  add(rc.path(rr(b.x, b.y, b.w, b.h, b.r), opt({stroke: INK, strokeWidth: b.sw})));
  add(rc.line(b.x, b.y + b.hh, b.x + b.w, b.y + b.hh, opt({stroke: INK, strokeWidth: b.sw * .8})));
}
ebox(C.box);
for (const seg of C.lines) line(seg.pts, seg.color === 'ink' ? INK : RED, seg.width);
for (const h of C.heads) head(h.x, h.y, h.dir, h.s);
document.body.dataset.ready = '1';
</script></body></html>
"""

# Icons inside (e): a trained network, the weight program that edits it, the network with a new skill.
NET = """<svg width="{s}" height="{s}" viewBox="0 0 100 100">
  <g stroke="#2f3642" stroke-width="3.2" fill="none" stroke-linecap="round">
    <path d="M20 30 L50 18 M20 30 L50 52 M20 72 L50 52 M20 72 L50 84 M50 18 L80 50 M50 52 L80 50 M50 84 L80 50 M20 30 L20 72"/>
  </g>
  <g stroke="#2f3642" stroke-width="3">
    <circle cx="20" cy="30" r="9" fill="#c9bce6"/><circle cx="20" cy="72" r="9" fill="#c9bce6"/>
    <circle cx="50" cy="18" r="9" fill="#9b84c9"/><circle cx="50" cy="52" r="9" fill="#9b84c9"/>
    <circle cx="50" cy="84" r="9" fill="#9b84c9"/><circle cx="80" cy="50" r="10" fill="{out}"/>
  </g>{extra}
</svg>"""
STAR = ('<polygon points="86,6 90,17 102,17 92.5,24 96,35 86,28 76,35 79.5,24 70,17 82,17" '
        'fill="#f2c14e" stroke="#2f3642" stroke-width="2.6" stroke-linejoin="round" transform="translate(-6,0)"/>')
PROGRAM = """<svg width="{w}" height="{h}" viewBox="0 0 120 100">
  <rect x="6" y="6" width="108" height="88" rx="12" fill="#fff" stroke="#2f3642" stroke-width="3.4"/>
  <text x="60" y="44" text-anchor="middle" font-family="Noto Sans" font-weight="700" font-size="30" fill="#6c4fa3">&lt;/&gt;</text>
  <g stroke-linecap="round" stroke-width="6"><path d="M24 62 H96" stroke="#9b84c9"/><path d="M24 78 H70" stroke="#c9bce6"/></g>
</svg>"""
STEP = """<svg width="{w}" height="{h}" viewBox="0 0 60 40"><path d="M4 20 H46" stroke="#2f3642" stroke-width="4"
  stroke-linecap="round"/><polygon points="56,20 42,11 42,29" fill="#2f3642"/></svg>"""


def diagram(icon: int, label_px: int, gap: int) -> str:
    """Row 'trained model -> weight program -> new capability' as inline HTML."""
    def cell(svg: str, label: str) -> str:
        return f'<div class="cell sans" style="font-size:{label_px}px;gap:4px">{svg}<span>{label}</span></div>'
    step = STEP.format(w=int(icon * .6), h=int(icon * .4))
    arrow = f'<div style="padding-top:{int(icon * .3)}px">{step}</div>'
    return (f'<div class="row" style="gap:{gap}px">'
            + cell(NET.format(s=icon, out="#9b84c9", extra=""), "trained model") + arrow
            + cell(PROGRAM.format(w=int(icon * 1.2), h=icon), "weight program") + arrow
            + cell(NET.format(s=icon, out="#f2c14e", extra=STAR), "new capability")
            + "</div>")


def e_content(b: dict, title_px: int, works_px: int, q_px: int, icon: int, label_px: int) -> str:
    """Header text and body of panel (e), positioned over the box drawn in SVG."""
    x, y, w, h, hh = b["x"], b["y"], b["w"], b["h"], b["hh"]
    return (
        f'<div class="elabel hand" style="left:{x + 22}px;top:{y + 6}px;font-size:{int(title_px * .82)}px">(e)</div>'
        f'<div class="etitle hand" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;font-size:{title_px}px">'
        'Self-improving Models</div>'
        f'<div class="ebox" style="left:{x}px;top:{y + hh}px;width:{w}px;height:{h - hh}px;padding:6px 0 10px">'
        f'<div class="works sans" style="font-size:{works_px}px">WeightCode · WeightLoop · CellScientist</div>'
        + diagram(icon, label_px, int(icon * .18))
        + f'<div class="q hand" style="font-size:{q_px}px">Can each result become a lasting capability?</div>'
        '</div>')


def horizontal(tmp: Path) -> tuple[str, int, int]:
    v1 = Image.open(SRC / "research_loop_v1.webp").convert("RGB")
    w = v1.width
    v1.crop((0, 0, w, H_PANEL_BOTTOM)).save(tmp / "h_panels.png")
    v1.crop(H_PILL_BOX).save(tmp / "h_pill.png")
    pill_w, pill_h = H_PILL_BOX[2] - H_PILL_BOX[0], H_PILL_BOX[3] - H_PILL_BOX[1]
    box = {"x": H_B_CENTER_X - 450, "y": 700, "w": 900, "h": 330, "hh": 74, "r": 26, "sw": 4.6}
    mid_y = box["y"] + box["h"] // 2
    pill_x, pill_y = 1580, mid_y - (704 - H_PILL_BOX[1])     # align the pill's red line with (e)'s middle
    height = box["y"] + box["h"] + 18
    cfg = {"box": box,
           "lines": [{"pts": [[H_D_LINE_X, H_PANEL_BOTTOM - 4], [H_D_LINE_X, pill_y + 46]], "color": "red", "width": 5},
                     {"pts": [[pill_x + 4, mid_y], [box["x"] + box["w"] + 22, mid_y]], "color": "red", "width": 5},
                     {"pts": [[H_B_CENTER_X, box["y"]], [H_B_CENTER_X, H_PANEL_BOTTOM + 30]], "color": "red", "width": 5}],
           "heads": [{"x": H_D_LINE_X, "y": pill_y + 50, "dir": "down", "s": 30},
                     {"x": box["x"] + box["w"] + 2, "y": mid_y, "dir": "left", "s": 30},
                     {"x": H_B_CENTER_X, "y": H_PANEL_BOTTOM + 2, "dir": "up", "s": 34}]}
    imgs = (f'<img src="h_panels.png" style="left:0;top:0">'
            f'<img src="h_pill.png" style="left:{pill_x}px;top:{pill_y}px;width:{pill_w}px;height:{pill_h}px">')
    text = (e_content(box, 46, 31, 34, 74, 23)
            + f'<div class="t loop hand" style="left:{H_B_CENTER_X + 22}px;top:{H_PANEL_BOTTOM + 22}px;font-size:31px">'
              'closing the loop: lasting model updates</div>'
            + f'<div class="t loop hand" style="left:{box["x"] + box["w"] + 26}px;top:{mid_y + 8}px;font-size:25px">'
              'measured outcomes</div>')
    return page(w, height, imgs, text, cfg), w, height


def vertical(tmp: Path) -> tuple[str, int, int]:
    v1 = Image.open(SRC / "research_loop_vertical_v1.webp").convert("RGB")
    w = v1.width
    base = v1.crop((0, 0, w, V_PILL_BOTTOM + 4))
    base.paste((255, 255, 255), (0, 0, V_MARGIN, base.height))   # remove the old loop line and its label
    base.save(tmp / "v_base.png")
    box = {"x": 130, "y": V_PILL_BOTTOM + 70, "w": 776, "h": 420, "hh": 82, "r": 26, "sw": 4.4}
    mid_y = box["y"] + box["h"] // 2
    height = box["y"] + box["h"] + 18
    pill_cx = 518
    cfg = {"box": box,
           "lines": [{"pts": [[pill_cx, V_PILL_BOTTOM - 2], [pill_cx, box["y"] - 24]], "color": "red", "width": 5},
                     {"pts": [[box["x"], mid_y], [47, mid_y], [47, V_B_CENTER_Y], [box["x"] - 30, V_B_CENTER_Y]],
                      "color": "red", "width": 5}],
           "heads": [{"x": pill_cx, "y": box["y"] - 2, "dir": "down", "s": 28},
                     {"x": box["x"] - 2, "y": V_B_CENTER_Y, "dir": "right", "s": 30}]}
    imgs = '<img src="v_base.png" style="left:0;top:0">'
    text = (e_content(box, 44, 27, 31, 82, 22)
            + f'<div class="t loop hand" style="left:-118px;top:{(V_B_CENTER_Y + mid_y) // 2 - 20}px;font-size:31px;'
              'width:330px;text-align:center;transform:rotate(-90deg)">closing the loop</div>'
            + f'<div class="t loop hand" style="left:{pill_cx + 18}px;top:{V_PILL_BOTTOM + 8}px;font-size:26px">'
              'measured outcomes</div>')
    return page(w, height, imgs, text, cfg), w, height


def page(w: int, h: int, imgs: str, text: str, cfg: dict) -> str:
    return (PAGE.replace("__FONTS__", FONTS_CSS).replace("__ROUGH__", ROUGH_JS)
            .replace("__W__", str(w)).replace("__H__", str(h)).replace("__IMGS__", imgs)
            .replace("__TEXT__", text).replace("__CFG__", json.dumps(cfg)))


async def render(jobs: list[tuple[Path, Path, int, int]], chrome: str | None) -> None:
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=chrome, args=["--no-sandbox"]) if chrome \
            else await p.chromium.launch()
        for html, png, w, h in jobs:
            pg = await browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            await pg.goto(html.as_uri(), wait_until="networkidle")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_selector("body[data-ready='1']")
            if not await pg.evaluate("document.fonts.check('40px Kalam') && document.fonts.check('30px \"Noto Sans\"')"):
                raise SystemExit("Kalam / Noto Sans did not load; refusing to render with fallback fonts.")
            await pg.screenshot(path=str(png))
            await pg.close()
        await browser.close()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--chrome", help="Chrome/Chromium executable (default: Playwright's bundled browser)")
    ap.add_argument("--keep", type=Path, help="also copy the intermediate HTML and PNG files here")
    args = ap.parse_args()
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        jobs = []
        for name, build in (("h", horizontal), ("v", vertical)):
            html, w, h = build(tmp)
            (tmp / f"{name}.html").write_text(html)
            jobs.append((tmp / f"{name}.html", tmp / f"{name}.png", w, h))
        asyncio.run(render(jobs, args.chrome))
        h_img = Image.open(tmp / "h.png").convert("RGB")
        v_img = Image.open(tmp / "v.png").convert("RGB")
        h_img.save(OUT / "research_loop.webp", "WEBP", quality=88, method=6)
        h_img.resize((1200, round(h_img.height * 1200 / h_img.width)), Image.LANCZOS) \
             .save(OUT / "research_loop_1200.webp", "WEBP", quality=90, method=6)
        v_img.save(OUT / "research_loop_vertical.webp", "WEBP", quality=88, method=6)
        if args.keep:
            args.keep.mkdir(parents=True, exist_ok=True)
            for f in tmp.iterdir():
                (args.keep / f.name).write_bytes(f.read_bytes())
        print(f"research_loop.webp {h_img.size}, research_loop_1200.webp (1200, "
              f"{round(h_img.height * 1200 / h_img.width)}), research_loop_vertical.webp {v_img.size}")


if __name__ == "__main__":
    main()
