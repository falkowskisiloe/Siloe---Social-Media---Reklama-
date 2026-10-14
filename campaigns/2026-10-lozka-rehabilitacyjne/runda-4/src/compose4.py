import sys
from PIL import Image, ImageDraw, ImageFont
R, OUT, FONTS = sys.argv[1:4]
W, H = 1080, 1350; M = 64
NAVY = (20, 40, 75); BLUE = (0, 157, 228); WHITE = (255, 255, 255)
def F(w, s): return ImageFont.truetype(f'{FONTS}/Manrope-{w}.ttf', s)

def photo(name, zoom=1.0, dy=0):
    im = Image.open(f'{R}/{name}.png').convert('RGBA')
    s = max(W*zoom / im.width, H / im.height); im = im.resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    x0 = (im.width-W)//2; y0 = min(max(0, (im.height-H)//2 + dy), im.height-H)
    return im.crop((x0, y0, x0+W, y0+H))

def logo(h):
    lg = Image.open(f'{R}/logo-siloe.png').convert('RGBA'); lg = lg.crop(lg.getbbox())
    return lg.resize((round(lg.width*h/lg.height), h), Image.LANCZOS)

def fade(im, top, h, col, amax, down=True):
    lay = Image.new('RGBA', (W, h), (0,0,0,0)); d = ImageDraw.Draw(lay)
    for y in range(h):
        t = y/h; a = amax*((1-t) if down else t)**1.2
        d.line([(0,y),(W,y)], fill=col+(int(a),))
    im.alpha_composite(lay, (0, top))

def badge(im, x, y, small, big, suffix):
    d = ImageDraw.Draw(im); fb = F(800, 66); fs = F(600, 26)
    w = max(d.textlength(big, font=fb), d.textlength(small, font=fs), d.textlength(suffix, font=fs)) + 60
    d.rounded_rectangle([x, y, x+w, y+176], radius=30, fill=BLUE)
    d.text((x+30, y+24), small, font=fs, fill=WHITE)
    d.text((x+28, y+122), big, font=fb, fill=WHITE, anchor='ls')
    d.text((x+30, y+136), suffix, font=fs, fill=WHITE)
    return w

def ad(name, region, lines, sub, zoom, dy, badge_xy):
    im = photo(name, zoom, dy)
    fade(im, 0, 420, (250, 245, 238), 225, down=True)
    fade(im, H-240, 240, (250, 245, 238), 235, down=False)
    d = ImageDraw.Draw(im)
    d.text((M, 60), f'WYNAJEM ŁÓŻEK REHABILITACYJNYCH · {region.upper()}', font=F(700, 24), fill=BLUE)
    y = 100
    for ln in lines:
        d.text((M, y), ln, font=F(800, 64), fill=NAVY); y += 74
    d.text((M, y+6), sub, font=F(500, 29), fill=NAVY)
    badge(im, *badge_xy, 'Wynajem', '150 zł', 'za miesiąc')
    d.text((M, H-158), 'Zapytaj o wynajem', font=F(700, 28), fill=BLUE)
    d.text((M, H-58), '14 694 10 00', font=F(800, 60), fill=NAVY, anchor='ls')
    lg = logo(66); im.alpha_composite(lg, (W-M-lg.width, H-58-lg.height+4))
    return im.convert('RGB')

V = {
 'V1-wieczor': ('s4', ['Komfort i spokój', 'we własnym domu'], 'Łóżko rehabilitacyjne z materacem w zestawie', 1.0, 0),
 'V2-sniadanie': ('s5', ['Oparcie w górę', 'jednym przyciskiem'], 'Elektryczne łóżko rehabilitacyjne do domu', 1.08, 30),
 'V3-oferta': ('s3', ['Łóżko rehabilitacyjne', 'na wynajem'], 'Elektryczna regulacja. Materac w zestawie.', 1.0, 0),
}
import json
for key, (src, lines, sub, zoom, dy) in V.items():
    for region, slug in (('Śląsk','slask'), ('Kraków','krakow')):
        bx = W-M-240
        im = ad(src, region, lines, sub, zoom, dy, (bx, 360))
        im.save(f'{OUT}/{key}-{slug}.jpg', quality=93)
        im.resize((360,450), Image.LANCZOS).save(f'{OUT}/{key}-{slug}-phone.jpg', quality=90)
