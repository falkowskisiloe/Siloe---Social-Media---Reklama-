"""Skład reklam łóżka 3F na podstawie zaakceptowanej grafiki (Siloe, 2026-10).

Produkt pochodzi wyłącznie z pikseli zaakceptowanego zdjęcia (Higgsfield job 36c754cd).
Rozszerzenia kadru (outpaint) dostarczają tylko ścianę i podłogę; środek jest nadpisywany oryginałem.
Teksty, naklejka, etykiety, panel i logo są rysowane tutaj, nie przez generator.
"""
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

NAVY = (29, 43, 70)
BLUE = (0, 157, 228)
WHITE = (255, 255, 255)
CFG = {}


def setup(fonts_dir, logo_path, s4_path):
    CFG['fonts'] = fonts_dir
    lg = Image.open(logo_path).convert('RGBA')
    CFG['logo'] = lg.crop(lg.getbbox())
    CFG['s4'] = Image.open(s4_path).convert('RGB')


def F(w, s):
    return ImageFont.truetype(f"{CFG['fonts']}/Poppins-{w}.ttf", round(s))


# Punkty produktu we współrzędnych zdjęcia źródłowego S4 (1856 x 2304)
P = {
    'remote': (696, 1502),
    'mattress': (1126, 1314),
    'backrest': (520, 1120),
    'legs': (1290, 1340),
    'frame': (980, 1660),
}


def paste_source(canvas_rgb, op_img, op_scale, src_box_in_op, canvas_offset, feather=40):
    """Rozszerzone tło + oryginalne piksele S4 w miejscu źródła (miękkie krawędzie)."""
    return canvas_rgb


def base_from_outpaint(op_path, W, H, k, src_top_in_op, src_w_in_op, shift_y, shift_x=0, feather=36):
    """Buduje tło W x H: outpaint przeskalowany o k, przycięty; w miejsce źródła wkleja oryginał S4.
    Zwraca (obraz RGBA, funkcja mapująca punkt S4 -> kanwa)."""
    op = Image.open(op_path).convert('RGB')
    opk = op.resize((round(op.width * k), round(op.height * k)), Image.LANCZOS)
    x0 = (opk.width - W) // 2 + shift_x
    y0 = shift_y
    canvas = opk.crop((x0, y0, x0 + W, y0 + H)).convert('RGBA')
    s4 = CFG['s4']
    sw = round(src_w_in_op * k)
    sc = sw / s4.width
    sh = round(s4.height * sc)
    sx = round((op.width * k - sw) / 2) - x0 if src_w_in_op < op.width else -x0
    sy = round(src_top_in_op * k) - y0
    if src_w_in_op < op.width:
        sx = round(((op.width - src_w_in_op) / 2) * k) - x0
    src = s4.resize((sw, sh), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (sw, sh), 0)
    ImageDraw.Draw(mask).rectangle([feather, feather, sw - feather, sh - feather], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather / 2))
    # wnętrze maski = 100% oryginału (obszar produktu leży daleko od krawędzi)
    src.putalpha(mask)
    canvas.alpha_composite(src, (sx, sy))
    return canvas, (lambda p: (sx + p[0] * sc, sy + p[1] * sc)), sc


def base_crop(W, H, scale, off_x, off_y):
    s4 = CFG['s4']
    im = s4.resize((round(s4.width * scale), round(s4.height * scale)), Image.LANCZOS)
    canvas = im.crop((off_x, off_y, off_x + W, off_y + H)).convert('RGBA')
    return canvas, (lambda p: (p[0] * scale - off_x, p[1] * scale - off_y)), scale


def text_w(d, t, f):
    return d.textlength(t, font=f)


def headline(im, lines, cy_top, size, sub=None, sub_size=None, gap=1.12, align='center', x=None, max_w=None):
    d = ImageDraw.Draw(im)
    W = im.width
    y = cy_top
    for t, col in lines:
        f = F(700, size)
        while max_w and text_w(d, t, f) > max_w:
            size -= 2; f = F(700, size)
        tw = text_w(d, t, f)
        xx = (W - tw) / 2 if align == 'center' else x
        d.text((xx, y + size), t, font=f, fill=col, anchor='ls')
        y += size * gap
    if sub:
        f = F(400, sub_size)
        tw = text_w(d, sub, f)
        xx = (W - tw) / 2 if align == 'center' else x
        d.text((xx, y + sub_size * 1.55), sub, font=f, fill=NAVY, anchor='ls')
        y += sub_size * 1.9
    return y


def shadowed(im, shape_fn, blur=10, offset=(0, 6), alpha=60):
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    shape_fn(ImageDraw.Draw(sh), (0, 0, 0, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(sh, offset)


def sticker(im, cx, cy, r0, top=None, big='150 zł', small='miesięcznie', rot=-10):
    r = r0 * 2  # rysowanie w 2x, potem zmniejszenie (gładkie krawędzie)
    S = int(r * 3)
    c = S / 2
    lay = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    sh = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([c - r + 3, c - r + 9, c + r + 3, c + r + 9], fill=(0, 0, 0, 70))
    lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(r * 0.08)))
    d = ImageDraw.Draw(lay)
    d.ellipse([c - r, c - r, c + r, c + r], fill=BLUE)
    # zawinięty róg: mały jasny trójkąt na krawędzi, poza strefą tekstu
    a = math.radians(38)
    ex, ey = c + r * math.cos(a), c + r * math.sin(a)
    t = r * 0.30
    p1 = (ex - t * math.sin(a) * 1.0, ey - 0 + t * math.cos(a) * 0.0)
    p1 = (c + r * math.cos(a + 0.33), c + r * math.sin(a + 0.33))
    p2 = (c + r * math.cos(a - 0.33), c + r * math.sin(a - 0.33))
    p3 = (c + r * 0.72 * math.cos(a), c + r * 0.72 * math.sin(a))
    d.polygon([p1, p2, (ex + r * 0.04, ey + r * 0.04)], fill=(0, 0, 0, 0))
    d.polygon([p1, p2, p3], fill=(226, 242, 252))
    d.line([p1, p2], fill=(150, 200, 230), width=max(2, int(r * 0.02)))
    big_s = r * 0.50
    fb = F(700, big_s)
    while d.textlength(big, font=fb) > r * 1.45:
        big_s -= 1; fb = F(700, big_s)
    fs = F(400, r * 0.19)
    if top:
        d.text((c, c - r * 0.36), top, font=F(500, r * 0.16), fill=WHITE, anchor='mm')
    d.text((c, c + r * 0.16), big, font=fb, fill=WHITE, anchor='ms')
    d.text((c - r * 0.04, c + r * 0.42), small, font=fs, fill=WHITE, anchor='ms')
    lay = lay.rotate(rot, resample=Image.BICUBIC, center=(c, c))
    lay = lay.resize((S // 2, S // 2), Image.LANCZOS)
    im.alpha_composite(lay, (int(cx - S / 4), int(cy - S / 4)))


def tags(im, items, x, y0, h, gap, size, check=True):
    d = ImageDraw.Draw(im)
    f = F(400, size)
    for i, t in enumerate(items):
        y = y0 + i * (h + gap)
        tw = text_w(d, t, f)
        w = h * 1.12 + tw + h * 0.55
        shadowed(im, lambda dd, col: dd.rounded_rectangle([x, y, x + w, y + h], radius=h / 2, fill=col), blur=8, offset=(0, 3), alpha=35)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([x, y, x + w, y + h], radius=h / 2, fill=WHITE)
        cr = h * 0.36; cx = x + h * 0.52; cy = y + h / 2
        d.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=BLUE)
        d.line([(cx - cr * 0.45, cy + cr * 0.02), (cx - cr * 0.1, cy + cr * 0.38), (cx + cr * 0.5, cy - cr * 0.35)], fill=WHITE, width=max(3, int(h * 0.08)), joint='curve')
        d.text((x + h * 1.12, cy), t, font=f, fill=NAVY, anchor='lm')


def callout(im, lines, box_xy, size, dot, side='left'):
    d = ImageDraw.Draw(im)
    f = F(400, size)
    tw = max(text_w(d, t, f) for t in lines)
    pad_x, pad_y = size * 0.9, size * 0.55
    lh = size * 1.18
    w = tw + 2 * pad_x; h = lh * len(lines) + 2 * pad_y - (lh - size)
    x, y = box_xy
    ax = x if side == 'left' else x + w
    ay = y + h * 0.75
    if side == 'top':
        ax, ay = x + w * 0.5, y + h
    d.line([(ax, ay), dot], fill=WHITE, width=3)
    r = size * 0.2
    d.ellipse([dot[0] - r, dot[1] - r, dot[0] + r, dot[1] + r], fill=WHITE)
    shadowed(im, lambda dd, col: dd.rounded_rectangle([x, y, x + w, y + h], radius=min(h / 2, size * 1.6), fill=col), blur=8, offset=(0, 3), alpha=40)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x, y, x + w, y + h], radius=min(h / 2, size * 1.6), fill=WHITE)
    for i, t in enumerate(lines):
        d.text((x + w / 2, y + pad_y + i * lh + size * 0.82), t, font=f, fill=NAVY, anchor='ms')
    return (x, y, w, h)


def rounded_one_corner(d, box, r, corner, fill):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=fill)
    if corner == 'tr':
        d.rectangle([x1 - r, y0, x1, y0 + r], fill=(0, 0, 0, 0))
        d.pieslice([x1 - 2 * r, y0, x1, y0 + 2 * r], 270, 360, fill=fill)
    if corner == 'tl':
        d.rectangle([x0, y0, x0 + r, y0 + r], fill=(0, 0, 0, 0))
        d.pieslice([x0, y0, x0 + 2 * r, y0 + 2 * r], 180, 270, fill=fill)


def bottom_panel(im, box, r, top_line, number, bottom_line=None, sizes=(28, 92, 27), pad=57):
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
    rounded_one_corner(ImageDraw.Draw(lay), box, r, 'tr', NAVY + (255,))
    im.alpha_composite(lay)
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = box
    s1, s2, s3 = sizes
    fnum = F(700, s2)
    while text_w(d, number, fnum) > (x1 - x0) - pad - 30:
        s2 -= 2; fnum = F(700, s2)
    lines_h = s1 * 1.3 + s2 * 0.95 + (s3 * 1.45 if bottom_line else 0)
    y = y0 + ((y1 - y0) - lines_h) / 2 + s1
    d.text((x0 + pad, y), top_line, font=F(400, s1), fill=WHITE, anchor='ls')
    y += s2 * 1.0
    d.text((x0 + pad - 3, y), number, font=fnum, fill=WHITE, anchor='ls')
    if bottom_line:
        y += s3 * 1.45
        d.text((x0 + pad, y), bottom_line, font=F(400, s3), fill=BLUE, anchor='ls')


def logo_box(im, box, r, logo_h):
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
    rounded_one_corner(ImageDraw.Draw(lay), box, r, 'tl', WHITE + (255,))
    im.alpha_composite(lay)
    lg = CFG['logo']
    l = lg.resize((round(lg.width * logo_h / lg.height), logo_h), Image.LANCZOS)
    x0, y0, x1, y1 = box
    im.alpha_composite(l, (round((x0 + x1) / 2 - l.width / 2 + 8), round((y0 + y1) / 2 - l.height / 2 + 4)))


def draft_tag(im, text, blocked=False):
    d = ImageDraw.Draw(im)
    f = F(600, 19)
    tw = text_w(d, text, f)
    col = (196, 40, 40) if blocked else NAVY
    d.rounded_rectangle([14, 12, 14 + tw + 28, 44], radius=16, fill=col + (215,))
    d.text((28, 28), text, font=f, fill=WHITE, anchor='lm')
