import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

S, OUT = sys.argv[1], sys.argv[2]
W, H = 1080, 1350
NAVY = (18, 38, 74)
BLUE = (40, 112, 214)
F = '/usr/share/fonts/opentype/inter/'


def font(w, s):
    return ImageFont.truetype(F + {'b': 'Inter-Bold.otf', 'x': 'Inter-ExtraBold.otf', 'r': 'Inter-Regular.otf',
                                   's': 'Inter-SemiBold.otf', 'm': 'Inter-Medium.otf'}[w], s)


def vgrad(w, h, c1, c2):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(c1)[None, None, :] * (1 - t) + np.array(c2)[None, None, :] * t
    return Image.fromarray(np.repeat(a, w, axis=1).astype(np.uint8))


def radial(w, h, cx, cy, r, c_in, c_out):
    y, x = np.mgrid[0:h, 0:w]
    d = np.clip(np.sqrt((x - cx) ** 2 + (y - cy) ** 2) / r, 0, 1)[..., None]
    a = np.array(c_in) * (1 - d) + np.array(c_out) * d
    return Image.fromarray(a.astype(np.uint8))


def overlay(base, layer_fn, blur=0, opacity=255):
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0))
    layer_fn(ImageDraw.Draw(lay))
    if blur:
        lay = lay.filter(ImageFilter.GaussianBlur(blur))
    if opacity < 255:
        a = lay.split()[3].point(lambda v: v * opacity // 255)
        lay.putalpha(a)
    base.alpha_composite(lay)


def bed(width, which='02'):
    b = Image.open(f'{S}/cut-{which}.png')
    h = int(b.height * width / b.width)
    return b.resize((width, h), Image.LANCZOS)


def place_bed(base, b, x, y, shadow=(0, 0, 0), sh_op=110):
    # contact shadow under the frame/wheels, then the untouched product pixels
    overlay(base, lambda d: d.ellipse([x + b.width * 0.03, y + b.height * 0.80, x + b.width * 0.97, y + b.height * 1.03],
                                      fill=shadow + (sh_op,)), blur=22)
    overlay(base, lambda d: d.ellipse([x + b.width * 0.10, y + b.height * 0.90, x + b.width * 0.92, y + b.height * 1.01],
                                      fill=shadow + (sh_op,)), blur=8)
    base.alpha_composite(b, (x, y))


def badge(d):
    f = font('b', 20)
    t = 'SZKIC DO OCENY'
    w = d.textlength(t, font=f)
    d.rounded_rectangle([W - w - 56, 24, W - 24, 60], radius=18, fill=(200, 30, 30))
    d.text((W - 40 - w, 31), t, font=f, fill='white')


def pill(d, xy, text, f, bg, fg, padx=34, h=None):
    x, y = xy
    w = d.textlength(text, font=f) + 2 * padx
    h = h or f.size + 40
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=bg)
    d.text((x + padx, y + h / 2), text, font=f, fill=fg, anchor='lm')
    return x + w


def floor_planks(img, top, c1, c2, vx):
    fl = vgrad(W, H - top, c1, c2).convert('RGBA')
    d = ImageDraw.Draw(fl)
    for i in range(-10, 22):
        xb = vx + i * 150
        d.line([(vx + (xb - vx) * 0.18, 0), (xb, H - top)], fill=(60, 35, 10, 14), width=2)
    for j, yy in enumerate([40, 95, 170, 270, 400]):
        pass
    img.alpha_composite(fl, (0, top))


# ---------- 1. Przygotuj dom do opieki ----------
img = vgrad(W, H, (246, 241, 233), (233, 225, 213)).convert('RGBA')
FT = 690
floor_planks(img, FT, (205, 170, 128), (168, 128, 88), 540)
d = ImageDraw.Draw(img)
d.rectangle([0, FT - 22, W, FT], fill=(250, 248, 244))  # baseboard
# window on the right
overlay(img, lambda d: d.rectangle([700, 110, 1010, 600], fill=(214, 230, 242, 255)))
overlay(img, lambda d: [d.rectangle([700, 110, 1010, 600], outline=(252, 252, 250, 255), width=18),
                        d.line([(855, 110), (855, 600)], fill=(252, 252, 250, 255), width=12),
                        d.line([(700, 350), (1010, 350)], fill=(252, 252, 250, 255), width=12)])
overlay(img, lambda d: [d.rectangle([660, 80, 740, 680], fill=(255, 255, 255, 170)),
                        d.rectangle([980, 80, 1060, 680], fill=(255, 255, 255, 170))], blur=6)  # sheer curtains
# daylight falling on wall and floor
overlay(img, lambda d: d.polygon([(700, 690), (1010, 690), (900, 1350), (240, 1350)], fill=(255, 250, 238, 90)), blur=40)
overlay(img, lambda d: d.ellipse([560, 120, 1180, 760], fill=(255, 248, 230, 70)), blur=80)
# plant behind bed (left)
overlay(img, lambda d: [d.rectangle([905, 600, 1060, 700], fill=(196, 160, 118, 255)),
                        d.rectangle([915, 700, 930, 760], fill=(150, 116, 80, 255)), d.rectangle([1035, 700, 1050, 760], fill=(150, 116, 80, 255)),
                        d.rectangle([950, 520, 1010, 600], fill=(240, 236, 228, 255))])
overlay(img, lambda d: d.ellipse([920, 470, 1040, 560], fill=(255, 226, 170, 120)), blur=30)
# rug
overlay(img, lambda d: d.polygon([(140, 900), (980, 900), (1080, 1300), (10, 1300)], fill=(206, 218, 230, 255)), blur=2)
b = bed(960)
place_bed(img, b, 60, 1310 - b.height, shadow=(60, 40, 20))
# warm vignette
overlay(img, lambda d: d.rectangle([0, 0, W, H], outline=(90, 60, 30, 60), width=120), blur=90)
d = ImageDraw.Draw(img)
d.text((64, 96), 'Wynajem łóżek rehabilitacyjnych — Śląsk', font=font('s', 28), fill=BLUE)
d.text((64, 140), 'Przygotuj dom', font=font('x', 84), fill=NAVY)
d.text((64, 232), 'do opieki', font=font('x', 84), fill=NAVY)
d.text((64, 346), 'Elektryczne łóżko rehabilitacyjne', font=font('m', 34), fill=(60, 66, 80))
d.text((64, 390), 'z materacem w zestawie', font=font('m', 34), fill=(60, 66, 80))
x = pill(d, (64, 466), 'Zadzwoń: 14 694 10 00', font('x', 38), NAVY, 'white', padx=30, h=80)
d.text((x + 24, 506), '150 zł / miesiąc', font=font('b', 34), fill=NAVY, anchor='lm')
badge(d)
img.convert('RGB').save(f'{OUT}/v2-1-dom.jpg', quality=88)

# ---------- 2. Wynajmij łóżko rehabilitacyjne ----------
img = radial(W, H, 540, 760, 900, (44, 86, 150), (10, 24, 52)).convert('RGBA')
overlay(img, lambda d: d.ellipse([60, 1020, 1020, 1300], fill=(120, 170, 235, 70)), blur=60)  # floor spot
overlay(img, lambda d: d.polygon([(380, 0), (700, 0), (1000, 1300), (80, 1300)], fill=(255, 255, 255, 18)), blur=50)
b = bed(980)
place_bed(img, b, 50, 1300 - b.height, shadow=(0, 0, 0), sh_op=150)
d = ImageDraw.Draw(img)
d.text((64, 92), 'Wynajem łóżek rehabilitacyjnych — Śląsk', font=font('s', 28), fill=(150, 190, 245))
d.text((64, 136), 'Wynajmij łóżko', font=font('x', 86), fill='white')
d.text((64, 230), 'rehabilitacyjne', font=font('x', 86), fill='white')
d.text((64, 344), 'Elektryczna regulacja oparcia, nóg i wysokości', font=font('m', 32), fill=(205, 222, 245))
# price block
d.rounded_rectangle([64, 420, 470, 600], radius=28, fill=BLUE)
d.text((96, 438), '150 zł', font=font('x', 96), fill='white')
d.text((100, 548), 'za miesiąc wynajmu', font=font('s', 30), fill=(225, 238, 255))
pill(d, (520, 486), 'Zadzwoń: 14 694 10 00', font('x', 38), 'white', NAVY, padx=30)
badge(d)
img.convert('RGB').save(f'{OUT}/v2-2-produkt.jpg', quality=88)

# ---------- 3. Pomożemy zorganizować sprzęt do domu ----------
img = vgrad(W, H, (226, 236, 246), (212, 226, 240)).convert('RGBA')  # room wall (light blue)
FT = 720
floor_planks(img, FT, (214, 182, 140), (182, 144, 102), 600)
d = ImageDraw.Draw(img)
d.rectangle([0, FT - 20, W, FT], fill=(250, 250, 248))
overlay(img, lambda d: d.ellipse([300, 200, 1200, 900], fill=(255, 250, 235, 90)), blur=90)
# framed picture on wall + side table with lamp

b = bed(860)
place_bed(img, b, 200, 1240 - b.height, shadow=(40, 50, 70))
# foreground doorway (hallway wall + white door frame) for depth
overlay(img, lambda d: [d.rectangle([0, 0, 150, H], fill=(236, 226, 212, 255)),
                        d.rectangle([0, 0, W, 70], fill=(236, 226, 212, 255)),
                        d.rectangle([150, 70, 190, H], fill=(250, 250, 248, 255)),
                        d.rectangle([150, 70, W, 104], fill=(250, 250, 248, 255))])
overlay(img, lambda d: d.polygon([(190, 104), (330, 170), (330, 1180), (190, H)], fill=(246, 244, 240, 255)))  # open door leaf
overlay(img, lambda d: d.line([(318, 640), (318, 700)], fill=(150, 150, 150, 255), width=8))
overlay(img, lambda d: d.rectangle([186, 100, 230, H], fill=(0, 0, 0, 40)), blur=14)  # jamb shadow
overlay(img, lambda d: d.rectangle([0, 0, 150, H], fill=(70, 45, 20, 40)))
d = ImageDraw.Draw(img)
d.text((370, 150), 'Wynajem łóżek rehabilitacyjnych — Śląsk', font=font('s', 24), fill=BLUE)
d.text((370, 188), 'Pomożemy', font=font('x', 66), fill=NAVY)
d.text((370, 262), 'zorganizować', font=font('x', 66), fill=NAVY)
d.text((370, 336), 'sprzęt do domu', font=font('x', 66), fill=NAVY)
d.text((370, 432), 'Doradzimy, dowieziemy i zmontujemy łóżko.', font=font('m', 28), fill=(55, 64, 84))
pill(d, (236, 1262 - 0), 'Zadzwoń: 14 694 10 00', font('x', 38), NAVY, 'white', padx=30, h=72)
d.text((W - 60, 1298), '150 zł / mies.', font=font('b', 32), fill=NAVY, anchor='rm')
badge(d)
img.convert('RGB').save(f'{OUT}/v2-3-usluga.jpg', quality=88)
print('ok')
