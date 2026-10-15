"""Poziome kreacje Meta 1,91:1 (1200 x 628) — osobny układ, nie kadr z innych formatów.
Lewa część: jednolity panel tekstowy w kolorze ściany. Prawa: zaakceptowane zdjęcie S4 (bez zmian, tylko przycięcie i skala).
Użycie: python3 build_landscape.py <katalog_roboczy> <katalog_fontów> <katalog_wyjściowy> [wersja]"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import layout as L
from PIL import Image, ImageDraw

WORK, FONTS, OUT = sys.argv[1:4]
VER = sys.argv[4] if len(sys.argv) > 4 else 'v1'
L.setup(FONTS, f'{WORK}/logo-siloe.png', f'{WORK}/s4.png')
W, H = 1200, 628
TEXT_W = 540                 # szerokość panelu tekstowego
CREAM = (244, 233, 220)      # jednolite tło panelu (ciepła ściana z kampanii)
M = 40                       # margines bezpieczny

COPY = {
    'h1': dict(head=[('Jeden telefon.', L.NAVY), ('My zajmiemy się resztą.', L.BLUE)],
               tags=['Dowozimy', 'Wnosimy', 'Montujemy', 'Szkolimy'],
               cta='Zadzwoń i sprawdź dostępność'),
    'h2': dict(head=[('3 regulacje elektryczne', L.NAVY), ('dla codziennej opieki', L.BLUE)],
               tags=['Oparcie', 'Segment nóg', 'Wysokość łóżka'],
               cta='Zapytaj o wynajem łóżka 3-funkcyjnego'),
}


def photo_panel():
    """Prawa część: S4 przeskalowane tak, by całe łóżko z wysięgnikiem mieściło się w wysokości kadru."""
    s4 = L.CFG['s4']
    pw = W - TEXT_W
    # łóżko w S4: x 95–1760, y 597 (szczyt wysięgnika) – 2000 (koła); margines ≥ 28 px z każdej strony
    sc = (pw - 2 * 28) / (1760 - 95)
    im = s4.resize((round(s4.width * sc), round(s4.height * sc)), Image.LANCZOS)
    cx = (95 + 1760) / 2 * sc
    cy = (597 + 2000) / 2 * sc
    x0 = round(cx - pw / 2); y0 = round(cy - H / 2 + 10)
    crop = im.crop((x0, y0, x0 + pw, y0 + H))
    return crop, (lambda p: (TEXT_W + p[0] * sc - x0, p[1] * sc - y0)), sc


def wrap_words(segments, font, max_w, d):
    """Łamanie po słowach z zachowaniem koloru segmentu; segment łamany na najmniejszą liczbę
    wierszy, a przy dwóch wierszach — w miejscu dającym najbardziej wyrównane długości."""
    lines = []
    for text, col in segments:
        words = text.split()
        if d.textlength(text, font=font) <= max_w:
            lines.append((text, col)); continue
        best = None
        for i in range(1, len(words)):
            a, b = ' '.join(words[:i]), ' '.join(words[i:])
            wa, wb = d.textlength(a, font=font), d.textlength(b, font=font)
            if max(wa, wb) <= max_w and (best is None or max(wa, wb) < best[0]):
                best = (max(wa, wb), a, b)
        if best:
            lines += [(best[1], col), (best[2], col)]; continue
        cur = ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=font) <= max_w: cur = t
            else: lines.append((cur, col)); cur = w
        lines.append((cur, col))
    return lines


def chips(im, items, x, y, h, gap, size, max_w):
    """Białe etykiety z ptaszkiem, układane w wiersze."""
    d = ImageDraw.Draw(im); f = L.F(400, size)
    cx, cy = x, y
    for t in items:
        w = h * 1.12 + d.textlength(t, font=f) + h * 0.55
        if cx + w > x + max_w:
            cx = x; cy += h + gap
        L.tags(im, [t], cx, cy, h, 0, size)
        cx += w + gap
    return cy + h


def build(c):
    im = Image.new('RGBA', (W, H), CREAM + (255,))
    ph, m, sc = photo_panel()
    im.paste(ph, (TEXT_W, 0))
    d = ImageDraw.Draw(im)
    tx = M + 8; tw = TEXT_W - tx - 34
    # logo (oryginalny plik)
    lg = L.CFG['logo']; lh = 44
    l = lg.resize((round(lg.width * lh / lg.height), lh), Image.LANCZOS)
    im.alpha_composite(l, (tx, M))
    # nagłówek
    py0 = H - M - 128
    def chips_h(sz):
        f = L.F(400, 26); rows, cx = 1, 0
        for t in c['tags']:
            w = 50 * 1.12 + d.textlength(t, font=f) + 50 * 0.55
            if cx and cx + w > tw + 8: rows += 1; cx = 0
            cx += w + 9
        return rows * 50 + (rows - 1) * 9
    size = 58
    while True:  # największy nagłówek, przy którym lista ma ≥ 24 px odstępu od panelu CTA
        fh = L.F(700, size); lines = wrap_words(c['head'], fh, tw, d)
        end = M + lh + 24 + len(lines) * size * 1.12 + 14 + chips_h(size)
        if end <= py0 - 24 or size <= 36: break
        size -= 2
    y = M + lh + 24
    for t, col in lines:
        d.text((tx, y + size), t, font=fh, fill=col, anchor='ls'); y += size * 1.12
    # lista
    y = chips(im, c['tags'], tx - 4, y + 14, 50, 9, 26, tw + 8)
    # panel CTA (granatowy, jak w zaakceptowanym projekcie)
    py1 = H - M
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([tx - 4, py0, TEXT_W - 30, py1], radius=26, fill=L.NAVY)
    fc = L.F(400, 25)
    while d.textlength(c['cta'], font=fc) > (TEXT_W - 30) - (tx - 4) - 52:
        fc = L.F(400, fc.size - 1)
    d.text((tx + 22, py0 + 46), c['cta'], font=fc, fill=L.WHITE, anchor='ls')
    d.text((tx + 19, py0 + 108), '14 694 10 00', font=L.F(700, 60), fill=L.WHITE, anchor='ls')
    # na zdjęciu: naklejka z ceną i etykieta materaca
    L.sticker(im, W - 44 - 94, 36 + 94, 94, top='wynajem łóżka', text_scale=1.15, curl_deg=62)
    mat = m(L.P['mattress'])
    L.callout(im, ['Materac', 'w zestawie'], (mat[0] + 52, mat[1] - 72), 24, mat, side='left')
    return im, y, py0


os.makedirs(OUT, exist_ok=True)
for h, c in COPY.items():
    im, y_list_end, py0 = build(c)
    base = f'{OUT}/3f-meta-feed-1.91x1-{h}-{VER}'
    im = im.convert('RGB'); im.save(base + '.png', optimize=True); im.save(base + '.jpg', quality=93)
    print(os.path.basename(base), im.size, 'koniec listy y=%d, panel od y=%d' % (y_list_end, py0))
