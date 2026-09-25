"""Render the README's original diagrams. Requires Pillow, no network access.

Usage: python scripts/render_home_visuals.py
The GIFs play once in less than five seconds and end on the complete diagram.
"""
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/images/home"
BG = "#0a1422"
PANEL = "#101f32"
LINE = "#28405b"
WHITE = "#eef5ff"
MUTED = "#a4b8d1"
BLUE = "#3288ff"
CYAN = "#64e3df"


def font(size, bold=False):
    candidates = (
        ["C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
        if bold else
        ["C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    raise RuntimeError("Install Segoe UI or DejaVu Sans before rendering.")


def label(draw, xy, text, size=24, color=WHITE, bold=False):
    f = font(size, bold)
    bounds = draw.textbbox(xy, text, font=f)
    w, h = draw._image.size
    if bounds[0] < 0 or bounds[1] < 0 or bounds[2] > w or bounds[3] > h:
        raise ValueError(f"Text outside canvas: {text}")
    draw.text(xy, text, font=f, fill=color)


def canvas(size):
    im = Image.new("RGB", size, BG)
    return im, ImageDraw.Draw(im)


def node(draw, xy, active=False, radius=9):
    x, y = xy
    if active:
        draw.ellipse((x-19, y-19, x+19, y+19), fill="#153e5d")
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=CYAN if active else BLUE)


def banner(progress):
    im, d = canvas((1600, 520))
    # Diagram background, deliberately quiet behind the learning path.
    for x in range(915, 1600, 44):
        d.line((x, 34, x, 474), fill="#142338")
    for y in range(34, 475, 44):
        d.line((915, y, 1556, y), fill="#142338")
    d.rounded_rectangle((58, 51, 65, 109), radius=3, fill=BLUE)
    label(d, (87, 50), "ESTUDO ABERTO  /  BLUE TEAM", 22, CYAN, True)
    label(d, (80, 112), "CAMINHO", 78, WHITE, True)
    label(d, (80, 196), "DAS PEDRAS", 78, WHITE, True)
    label(d, (84, 296), "CYBERSECURITY", 31, MUTED)
    label(d, (84, 362), "Entenda a base. Investigue com método.", 28)
    label(d, (84, 405), "Aprenda • Pratique • Documente • Evolua", 22, MUTED)

    points = [(990, 379), (1114, 287), (1240, 195), (1372, 103)]
    d.line(points, fill=LINE, width=4)
    distance = progress * 3
    for i in range(3):
        t = min(1, max(0, distance-i))
        a, b = points[i], points[i+1]
        end = (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
        if t > 0:
            d.line((a, end), fill=CYAN, width=4)
    for i, (x, y) in enumerate(points):
        node(d, (x, y), progress >= i/3)
        label(d, (x+26, y-19), ["BASE", "DADOS", "INVESTIGAÇÃO", "CRITÉRIO"][i], 20, WHITE, True)
    label(d, (974, 452), "O caminho é feito de perguntas.", 23, MUTED)
    d.line((80, 487, 1520, 487), fill=LINE, width=1)
    return im


def investigation(progress):
    im, d = canvas((1200, 580))
    label(d, (48, 30), "DA PERGUNTA À EVIDÊNCIA", 35, WHITE, True)
    label(d, (48, 85), "O raciocínio permanece. A sintaxe muda.", 24, MUTED)
    items = [
        ("01", "PERGUNTA", "O que aconteceu?", "Defina o escopo."),
        ("02", "DADOS", "Qual fonte e campo?", "Confira a cobertura."),
        ("03", "CONSULTA", "Como relacionar?", "Filtre. Compare."),
        ("04", "EVIDÊNCIA", "O que sustenta?", "Declare os limites."),
    ]
    for i, (num, title, first, second) in enumerate(items):
        x = 40+i*288
        active = progress >= i/3
        d.rounded_rectangle((x, 159, x+256, 355), radius=16, fill=PANEL, outline=CYAN if active else LINE, width=2)
        label(d, (x+20, 177), num, 24, CYAN if active else MUTED, True)
        label(d, (x+20, 222), title, 26, WHITE, True)
        label(d, (x+20, 279), first, 19, MUTED)
        label(d, (x+20, 308), second, 19, MUTED)
        if i < 3:
            start, end = x+259, x+283
            color = CYAN if progress > i/3 else LINE
            d.line((start, 254, end, 254), fill=color, width=2)
            d.polygon([(end, 254), (end-6, 250), (end-6, 258)], fill=color)
    # Returning to data is part of investigation, not a claim of causality.
    d.line([(1032, 379), (1032, 411), (456, 411), (456, 379)], fill=BLUE, width=3)
    d.polygon([(456, 374), (450, 385), (462, 385)], fill=BLUE)
    label(d, (504, 428), "Faltou contexto? Volte aos dados.", 23, MUTED)
    d.line((48, 487, 1152, 487), fill=LINE)
    label(d, (48, 510), "KQL  /  SPL  /  AQL  /  WAZUH + OPENSEARCH", 24, CYAN, True)
    return im


def export(name, render):
    frames = []
    # 36 * 100 ms + 1000 ms final hold = 4.6 s, no infinite-loop extension.
    for i in range(37):
        t = i/36
        eased = (1-math.cos(math.pi*t))/2
        frames.append(render(eased))
    frames[-1].save(OUT / f"{name}.png", optimize=True)
    palette = frames[-1].quantize(colors=128)
    indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
    indexed[0].save(
        OUT / f"{name}.gif", save_all=True, append_images=indexed[1:],
        duration=[100]*36+[1000], optimize=True, disposal=1,
    )
    with Image.open(OUT / f"{name}.gif") as check:
        assert check.n_frames > 1 and "loop" not in check.info
        elapsed = 0
        for frame in range(check.n_frames):
            check.seek(frame)
            elapsed += check.info.get("duration", 0)
        assert elapsed < 5000
        print(f"{name}: {check.size}, {check.n_frames} frames, {elapsed} ms, {(OUT / (name+'.gif')).stat().st_size} bytes")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    export("banner-caminho", banner)
    export("fluxo-investigacao", investigation)
