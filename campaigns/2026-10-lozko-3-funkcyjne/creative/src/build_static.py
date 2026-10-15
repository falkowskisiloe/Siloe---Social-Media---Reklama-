"""Buduje statyczne kreacje 4:5, 1:1, 9:16 dla H1/H2/H3.
Użycie: python3 build_static.py <katalog_roboczy> <katalog_fontów> <katalog_wyjściowy>
Katalog roboczy: s4.png (zaakceptowane zdjęcie), op11.png, op916.png (outpaint), logo-siloe.png."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import layout as L

WORK, FONTS, OUT = sys.argv[1:4]
VER = sys.argv[4] if len(sys.argv) > 4 else 'v2'
L.setup(FONTS, f'{WORK}/logo-siloe.png', f'{WORK}/s4.png')

COPY = {
    'h1': dict(head=[('Jeden telefon.', L.NAVY), ('My zajmiemy się resztą.', L.BLUE)],
               sub='Od telefonu do gotowego łóżka',
               tags=['Dowozimy', 'Wnosimy', 'Montujemy', 'Szkolimy'],
               panel=('Zadzwoń i sprawdź dostępność', '14 694 10 00', 'Wynajem łóżka rehabilitacyjnego'),),
    'h2': dict(head=[('3 regulacje elektryczne', L.NAVY), ('dla codziennej opieki', L.BLUE)],
               sub='Łóżko 3-funkcyjne na wynajem',
               tags=['Oparcie', 'Segment nóg', 'Wysokość łóżka'],
               panel=('Zapytaj o wynajem łóżka 3-funkcyjnego', '14 694 10 00', 'Materac w zestawie'),),
    'h3': dict(head=[('Jeden telefon.', L.NAVY), ('Łóżko gotowe w 48 godzin', L.BLUE)],
               sub='Od telefonu do Twoich drzwi',
               tags=['Dowozimy', 'Wnosimy', 'Montujemy', 'Szkolimy'],
               panel=('Zadzwoń i potwierdź termin', '14 694 10 00', 'Odbieramy 7 dni w tygodniu'),),
}


def labels(im, m, mat_box, el_box, size):
    L.callout(im, ['Materac', 'w zestawie'], mat_box, size, m(L.P['mattress']), side='left')
    L.callout(im, ['Elektryczna', 'regulacja'], el_box, size, m(L.P['remote']), side='right')


def feed45(c):
    im, m, sc = L.base_crop(1080, 1350, 1350 / 2304, 3, 0)
    L.headline(im, c['head'], 50, 76, sub=c['sub'], sub_size=34, gap=1.12, max_w=960)
    L.sticker(im, 935, 362, 104, top='wynajem łóżka')
    L.tags(im, c['tags'], 55, 356, 50, 10, 28)
    labels(im, m, (752, 612), (122, 985), 27)
    L.bottom_panel(im, (0, 1148, 640, 1350), 70, *c['panel'], sizes=(27, 92, 26))
    L.logo_box(im, (840, 1148, 1080, 1350), 80, 80)
    return im


def feed11(c):
    im, m, sc = L.base_from_outpaint(f'{WORK}/op11.png', 1080, 1080, 1080 / 2048, 0, 1648, 0)
    L.headline(im, c['head'], 52, 56, sub=c['sub'], sub_size=27, gap=1.12, max_w=880)
    L.sticker(im, 958, 352, 86, top='wynajem łóżka')
    L.tags(im, c['tags'], 30, 285, 50, 8, 30)
    labels(im, m, (700, 525), (150, 795), 30)
    L.bottom_panel(im, (0, 948, 600, 1080), 56, c['panel'][0], c['panel'][1], None, sizes=(22, 68, 20), pad=40)
    L.logo_box(im, (820, 948, 1080, 1080), 60, 62)
    return im


def story916(c):
    im, m, sc = L.base_from_outpaint(f'{WORK}/op916.png', 1080, 1920, 0.74, 425, 1536, 94)
    L.headline(im, c['head'], 275, 80, sub=c['sub'], sub_size=37, gap=1.12, max_w=960)
    L.sticker(im, 915, 650, 112, top='wynajem łóżka')
    L.tags(im, c['tags'], 55, 625, 56, 12, 31)
    labels(im, m, (760, 860), (110, 1130), 29)
    L.bottom_panel(im, (0, 1272, 650, 1440), 70, c['panel'][0], c['panel'][1], None, sizes=(28, 88, 26))
    L.logo_box(im, (850, 1272, 1080, 1440), 80, 78)
    return im


os.makedirs(OUT, exist_ok=True)
for h in ('h1', 'h2'):
    c = COPY[h]
    for name, fn in (('feed-4x5', feed45), ('feed-1x1', feed11), ('story-9x16', story916)):
        im = fn(c).convert('RGB')
        base = f'{OUT}/3f-meta-{name}-{h}-{VER}'
        im.save(base + '.png', optimize=True)
        im.save(base + '.jpg', quality=93)
        print(base, im.size)
