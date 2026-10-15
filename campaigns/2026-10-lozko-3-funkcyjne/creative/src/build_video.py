"""Motion graphic 9:16 z zaakceptowanego zdjęcia łóżka 3F: najazd kamery, zbliżenie na pilot,
animowane etykiety, lista usług, cena najmu i CTA. Łóżko nie jest generowane ani animowane mechanicznie.
Użycie: python3 build_video.py <work> <fonts> <out_dir> <15|6> [cover]"""
import sys, os, subprocess, math
sys.path.insert(0, os.path.dirname(__file__))
import layout as L
from PIL import Image, ImageDraw

WORK, FONTS, OUT, MODE = sys.argv[1:5]
VER = sys.argv[5] if len(sys.argv) > 5 else 'v2'
L.setup(FONTS, f'{WORK}/logo-siloe.png', f'{WORK}/s4.png')
W, H, FPS = 1080, 1920, 30
os.makedirs(OUT, exist_ok=True)

# tło w 2x (2160 x 3840), te same parametry co Stories, przeskalowane x2
BASE, m2, _ = L.base_from_outpaint(f'{WORK}/op916.png', 2 * W, 2 * H, 1.48, 425, 1536, 188)
BASE = BASE.convert('RGB')
def m(p):
    x, y = m2(p); return (x / 2, y / 2)

REMOTE = m(L.P['remote'])
CENTER = (W / 2, H / 2)


def ease(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)


def lerp(a, b, u):
    return a + (b - a) * u


def frame_bg(cam):
    cx, cy, z = cam
    vw, vh = W / z, H / z
    box = [2 * (cx - vw / 2), 2 * (cy - vh / 2), 2 * (cx + vw / 2), 2 * (cy + vh / 2)]
    return BASE.resize((W, H), Image.BICUBIC, box=box).convert('RGBA')


def to_screen(p, cam):
    cx, cy, z = cam
    return ((p[0] - (cx - W / 2 / z)) * z, (p[1] - (cy - H / 2 / z)) * z)


def layer(fn):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); fn(lay); return lay


def put(im, lay, a, dy=0):
    if a <= 0: return
    if a < 1:
        al = lay.getchannel('A').point(lambda v: int(v * a)); lay = lay.copy(); lay.putalpha(al)
    im.alpha_composite(lay, (0, int(dy)))


def env(t, t0, t1, fi=0.35, fo=0.3):
    if t < t0 or t > t1: return 0.0
    return min(ease((t - t0) / fi), ease((t1 - t) / fo) if fo else 1.0)


def heading(lines, top=300, size=76, sub=None):
    txt = layer(lambda im: L.headline(im, lines, top, size, sub=sub, sub_size=38, gap=1.14, max_w=900))
    x0, y0, x1, y1 = txt.getchannel('A').getbbox()
    card = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle([x0 - 44, y0 - 34, x1 + 44, y1 + 38], radius=40, fill=(255, 255, 255, 226))
    card.alpha_composite(txt)
    return card




def end_card():
    def fn(im):
        d = ImageDraw.Draw(im)
        x0, y0, x1, y1 = 70, 720, 1010, 1240
        L.shadowed(im, lambda dd, col: dd.rounded_rectangle([x0, y0, x1, y1], radius=48, fill=col), blur=16, offset=(0, 10), alpha=70)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([x0, y0, x1, y1], radius=48, fill=L.NAVY)
        d.rounded_rectangle([x0 + 300, y0 - 70, x1 - 300, y0 + 70], radius=40, fill=L.WHITE)
        lg = L.CFG['logo']; lh = 84
        l = lg.resize((round(lg.width * lh / lg.height), lh), Image.LANCZOS)
        im.alpha_composite(l, (int(W / 2 - l.width / 2 + 6), int(y0 - l.height / 2 + 2)))
        d.text((W / 2, y0 + 175), 'Zadzwoń i sprawdź', font=L.F(600, 58), fill=L.WHITE, anchor='ms')
        d.text((W / 2, y0 + 245), 'dostępność', font=L.F(600, 58), fill=L.WHITE, anchor='ms')
        d.text((W / 2, y0 + 380), '14 694 10 00', font=L.F(700, 112), fill=L.WHITE, anchor='ms')
    return layer(fn)


def run15():
    T = 15.0
    CAM_FULL = (540, 960, 1.0)
    CAM_R = (REMOTE[0] + 20, REMOTE[1] + 80, 1.9)
    CAM_HOLD = (540, 960, 1.06)

    def cam(t):
        if t < 2.0: return (540, 960, lerp(1.0, 1.05, t / 2))
        if t < 3.0:
            u = ease((t - 2) / 1.0); a = (540, 960, 1.05)
            return tuple(lerp(a[i], CAM_R[i], u) for i in range(3))
        if t < 4.7: return (CAM_R[0], CAM_R[1], lerp(1.9, 1.96, (t - 3) / 1.7))
        if t < 5.5:
            u = ease((t - 4.7) / 0.8); a = (CAM_R[0], CAM_R[1], 1.96)
            return tuple(lerp(a[i], CAM_HOLD[i], u) for i in range(3))
        if t < 8.2: return CAM_HOLD
        if t < 11.0: return (540, 960, lerp(1.06, 1.10, (t - 8.2) / 2.8))
        return (540, 960, 1.10)

    H0 = heading([('Łóżko rehabilitacyjne', L.NAVY), ('do opieki w domu', L.BLUE)])
    camR = (CAM_R[0], CAM_R[1], 1.93)
    rs = to_screen(L.P and REMOTE, camR)
    REM = layer(lambda im: L.callout(im, ['3 funkcje', 'elektryczne'], (rs[0] + 90, rs[1] + 170), 46, (rs[0] + 2, rs[1] + 10), side='left'))
    H3F = heading([('3 funkcje elektryczne', L.NAVY)], top=300, size=72)
    pts = {k: to_screen(m(L.P[k]), CAM_HOLD) for k in ('backrest', 'legs', 'frame')}
    OP = layer(lambda im: L.callout(im, ['Oparcie'], (70, pts['backrest'][1] - 230), 44, pts['backrest'], side='left'))
    NO = layer(lambda im: L.callout(im, ['Nogi'], (790, pts['legs'][1] - 260), 44, pts['legs'], side='left'))
    WY = layer(lambda im: L.callout(im, ['Wysokość'], (630, pts['frame'][1] - 150), 44, pts['frame'], side='left'))
    SV = heading([('Dostawa • wniesienie', L.NAVY), ('montaż • instruktaż', L.BLUE)], size=70)
    mat = to_screen(m(L.P['mattress']), (540, 960, 1.10))
    MT = heading([('Materac w zestawie', L.NAVY)], size=74)
    MTC = layer(lambda im: L.callout(im, ['Materac', 'w zestawie'], (mat[0] + 120, mat[1] - 230), 40, mat, side='left'))
    def stk(im):
        L.sticker(im, 850, 600, 130, top='wynajem łóżka')
    STK = layer(stk)
    END = end_card()
    return T, cam, [
        (H0, 0.15, 2.05, 0.4, 0.3),
        (REM, 2.9, 4.75, 0.35, 0.25),
        (H3F, 5.4, 8.15, 0.35, 0.3),
        (OP, 5.6, 8.15, 0.3, 0.3), (NO, 6.3, 8.15, 0.3, 0.3), (WY, 7.0, 8.15, 0.3, 0.3),
        (SV, 8.3, 11.0, 0.4, 0.3),
        (MT, 11.15, 13.0, 0.35, 0.3), (MTC, 11.3, 13.0, 0.35, 0.3),
        (STK, 11.5, 13.1, 0.3, 0.3),
        (END, 13.0, 15.0, 0.4, 0),
    ]


def run6():
    T = 6.0
    CAM_R = (REMOTE[0] + 20, REMOTE[1] + 80, 1.85)
    def cam(t):
        if t < 1.8: return (540, 960, lerp(1.0, 1.04, t / 1.8))
        if t < 2.5:
            u = ease((t - 1.8) / 0.7); a = (540, 960, 1.04)
            return tuple(lerp(a[i], CAM_R[i], u) for i in range(3))
        if t < 3.8: return CAM_R
        if t < 4.4:
            u = ease((t - 3.8) / 0.6)
            return tuple(lerp(CAM_R[i], (540, 960, 1.06)[i], u) for i in range(3))
        return (540, 960, 1.06)
    H0 = heading([('Łóżko 3-funkcyjne', L.NAVY), ('do domu', L.BLUE)], size=84)
    rs = to_screen(REMOTE, CAM_R)
    REM = layer(lambda im: L.callout(im, ['3 funkcje', 'elektryczne'], (rs[0] + 90, rs[1] + 170), 46, (rs[0] + 2, rs[1] + 10), side='left'))
    FN = heading([('Oparcie • Nogi • Wysokość', L.NAVY)], size=60)
    END = end_card()
    return T, cam, [(H0, 0.1, 1.85, 0.3, 0.25), (REM, 2.45, 3.85, 0.25, 0.2), (FN, 2.55, 3.85, 0.25, 0.2), (END, 3.9, 6.0, 0.35, 0)]


def render(T, cam, items, path):
    n = int(T * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', os.environ.get('SILOE_X264_PRESET', 'medium'), '-crf', '18', '-pix_fmt', 'yuv420p', '-threads', '2', '-profile:v', 'high', '-movflags', '+faststart', path],
                         stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        im = frame_bg(cam(t))
        for lay, t0, t1, fi, fo in items:
            a = env(t, t0, t1, fi, fo)
            put(im, lay, a, dy=(1 - a) * 24 if a < 1 else 0)
        p.stdin.write(im.convert('RGB').tobytes())
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError("ffmpeg export failed")


if MODE == 'cover':
    im = frame_bg((540, 960, 1.04))
    lay = layer(lambda x: None)
    def fn(x):
        d = ImageDraw.Draw(x)
        d.rounded_rectangle([90, 300, 990, 700], radius=56, fill=(255, 255, 255, 228))
        d.text((W / 2, 430), 'Łóżko', font=L.F(700, 110), fill=L.NAVY, anchor='ms')
        d.text((W / 2, 545), '3-funkcyjne', font=L.F(700, 110), fill=L.BLUE, anchor='ms')
        d.text((W / 2, 650), 'do domu', font=L.F(700, 92), fill=L.NAVY, anchor='ms')
        lg = L.CFG['logo']; lh = 96
        l = lg.resize((round(lg.width * lh / lg.height), lh), Image.LANCZOS)
        d.rounded_rectangle([W / 2 - l.width / 2 - 40, 1360, W / 2 + l.width / 2 + 40, 1360 + lh + 50], radius=36, fill=(255, 255, 255, 240))
        x.alpha_composite(l, (int(W / 2 - l.width / 2 + 6), 1385))
    fn(lay); im.alpha_composite(lay)
    im = im.convert('RGB'); im.save(f'{OUT}/3f-meta-reel-cover-{VER}.png'); im.save(f'{OUT}/3f-meta-reel-cover-{VER}.jpg', quality=93)
    print('cover ok')
else:
    T, cam, items = run15() if MODE == '15' else run6()
    out = f'{OUT}/3f-meta-reel-{MODE}s-{VER}-silent.mp4'
    render(T, cam, items, out)
    print(out)
