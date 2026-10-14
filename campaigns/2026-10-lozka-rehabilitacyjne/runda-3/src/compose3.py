import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = sys.argv[1]; OUT = sys.argv[2]; FONTS = sys.argv[3]
W, H = 1080, 1350
NAVY = (20, 40, 75); BLUE = (0, 157, 228); WHITE = (255, 255, 255); MUTED = (20, 40, 75, 200)
def F(w, s): return ImageFont.truetype(f'{FONTS}/Manrope-{w}.ttf', s)

def photo():
    im = Image.open(f'{R}/k2.png').convert('RGBA')
    # soft contact shadows on the floor only, under the four castors (full-res coords)
    sh = Image.new('L', im.size, 0); d = ImageDraw.Draw(sh)
    for (x, y, rx, ry, a) in [(145, 1688, 60, 14, 120), (1500, 1945, 70, 16, 130), (1690, 1675, 62, 14, 115), (475, 1517, 44, 10, 90)]:
        d.ellipse([x-rx, y-ry, x+rx, y+ry], fill=a)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    dark = Image.new('RGBA', im.size, (60, 45, 30, 255)); dark.putalpha(sh)
    # keep the shadow below the wheels: mask out everything above each contact line
    im.alpha_composite(dark)
    s = H / im.height; im = im.resize((round(im.width*s), H), Image.LANCZOS)
    x0 = (im.width - W)//2
    return im.crop((x0, 0, x0+W, H))

def logo(h):
    lg = Image.open(f'{R}/logo-siloe.png').convert('RGBA'); lg = lg.crop(lg.getbbox())
    return lg.resize((round(lg.width*h/lg.height), h), Image.LANCZOS)

def tw(d, t, f): return d.textlength(t, font=f)

def region_tag(im, x_right, y, region):
    d = ImageDraw.Draw(im); f = F(700, 26); t = region.upper()
    w = tw(d, t, f) + 2*22
    d.rounded_rectangle([x_right-w, y, x_right, y+48], radius=24, outline=NAVY, width=2, fill=(255,255,255,170))
    d.text((x_right-w+22, y+9), t, font=f, fill=NAVY)

def variant_a(region):
    im = photo(); d = ImageDraw.Draw(im, 'RGBA'); M = 64
    # soft wall wash for legibility of the top zone
    wash = Image.new('RGBA', (W, 330), (0,0,0,0)); wd = ImageDraw.Draw(wash)
    for y in range(330): wd.line([(0,y),(W,y)], fill=(250,248,245, int(210*(1-y/330)**1.4)))
    im.alpha_composite(wash, (0,0))
    lg = logo(70); im.alpha_composite(lg, (M-6, 52))
    region_tag(im, W-M, 64, region)
    d = ImageDraw.Draw(im, 'RGBA')
    d.text((M, 156), 'Łóżko rehabilitacyjne', font=F(800, 70), fill=NAVY)
    d.text((M, 246), 'Elektryczna regulacja. Materac w zestawie.', font=F(500, 30), fill=(20,40,75,215))
    # offer card on the floor
    cy, ch = 1146, 156; d.rounded_rectangle([M-16, cy, W-M+16, cy+ch], radius=28, fill=(255,255,255,240))
    d.text((M+16, cy+26), 'WYNAJEM', font=F(700, 22), fill=BLUE)
    bl = cy+124; d.text((M+16, bl), '150 zł', font=F(800, 64), fill=NAVY, anchor='ls')
    x = M+16+tw(d, '150 zł', F(800,64))+12; d.text((x, bl), '/ miesiąc', font=F(600, 28), fill=NAVY, anchor='ls')
    xs = W//2 + 70; d.line([(xs-40, cy+30), (xs-40, cy+ch-30)], fill=(20,40,75,60), width=2)
    d.text((xs, cy+26), 'ZAPYTAJ O WYNAJEM', font=F(700, 22), fill=BLUE)
    d.text((xs, bl), '14 694 10 00', font=F(800, 50), fill=NAVY, anchor='ls')
    return im

def variant_b(region):
    im = photo(); M = 64
    wash = Image.new('RGBA', (W, 340), (0,0,0,0)); wd = ImageDraw.Draw(wash)
    for y in range(340): wd.line([(0,y),(W,y)], fill=(250,248,245, int(200*(1-y/340)**1.3)))
    im.alpha_composite(wash, (0,0))
    fl = Image.new('RGBA', (W, 260), (0,0,0,0)); fd = ImageDraw.Draw(fl)
    for y in range(260): fd.line([(0,y),(W,y)], fill=(250,248,245, int(225*(y/260)**0.9)))
    im.alpha_composite(fl, (0, H-260))
    d = ImageDraw.Draw(im, 'RGBA')
    d.text((M, 62), f'WYNAJEM · {region.upper()}', font=F(700, 24), fill=BLUE)
    d.text((M, 100), 'Łóżko', font=F(800, 76), fill=NAVY)
    d.text((M, 182), 'rehabilitacyjne', font=F(800, 76), fill=NAVY)
    # price badge, logo blue
    bx1, by0, bw, bh = W-M, 62, 300, 196; bx0 = bx1-bw
    d.rounded_rectangle([bx0, by0, bx1, by0+bh], radius=32, fill=BLUE+(255,))
    d.text((bx0+30, by0+26), 'Wynajem', font=F(600, 28), fill=WHITE)
    d.text((bx0+28, by0+60), '150 zł', font=F(800, 72), fill=WHITE)
    d.text((bx0+30, by0+144), 'za miesiąc', font=F(600, 28), fill=WHITE)
    # bottom: CTA + phone left, logo right, shared baseline
    d.text((M, H-188), 'Elektryczna regulacja. Materac w zestawie.', font=F(500, 28), fill=(20,40,75,210))
    d.text((M, H-140), 'Zapytaj o wynajem', font=F(700, 28), fill=BLUE)
    d.text((M, H-56), '14 694 10 00', font=F(800, 58), fill=NAVY, anchor='ls')
    lg = logo(64); im.alpha_composite(lg, (W-M-lg.width, H-56-lg.height+4))
    return im

for region in ('Śląsk', 'Kraków'):
    slug = 'slask' if region == 'Śląsk' else 'krakow'
    for name, fn in (('A', variant_a), ('B', variant_b)):
        im = fn(region).convert('RGB'); im.save(f'{OUT}/3f-{name}-{slug}.jpg', quality=93)
        im.resize((360, 450), Image.LANCZOS).save(f'{OUT}/3f-{name}-{slug}-phone.jpg', quality=90)
