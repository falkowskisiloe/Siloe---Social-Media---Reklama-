"""Spokojny podkład syntetyczny (autorski, generowany w całości tym skryptem — brak praw osób trzecich).
Użycie: python3 music.py <sekundy> <plik.wav>"""
import sys, wave
import numpy as np

SR = 44100
dur = float(sys.argv[1]); out = sys.argv[2]
n = int(SR * dur)
t = np.arange(n) / SR
mix = np.zeros(n)


def note(f, start, length, amp, partials=(1, 0.45, 0.2, 0.08), attack=0.02, decay=1.6):
    s = int(start * SR); e = min(n, int((start + length) * SR))
    if s >= n:
        return
    tt = np.arange(e - s) / SR
    env = np.minimum(1, tt / attack) * np.exp(-tt / decay)
    sig = sum(a * np.sin(2 * np.pi * f * k * tt) for k, a in enumerate(partials, 1))
    mix[s:e] += amp * env * sig


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


# progresja: C – Am – F – G, 2 s na akord (tempo ok. 60 BPM)
chords = [(48, [60, 64, 67]), (45, [57, 60, 64]), (41, [57, 60, 65]), (43, [59, 62, 67])]
beat = 0.5
i = 0; start = 0.0
while start < dur:
    bass, tri = chords[i % 4]
    note(hz(bass), start, 2.4, 0.16, partials=(1, 0.3, 0.1), attack=0.05, decay=2.5)
    for j, m in enumerate(tri):  # miękki akord-pad
        note(hz(m), start, 2.4, 0.05, partials=(1, 0.2), attack=0.4, decay=3.0)
    arp = [tri[0] + 12, tri[1] + 12, tri[2] + 12, tri[1] + 12]
    for k, m in enumerate(arp):  # delikatne arpeggio „pianino”
        note(hz(m), start + k * beat, 0.9, 0.07, decay=0.7)
    start += 2.0; i += 1

# pogłos (proste echa) i wyciszenia
rev = mix.copy()
for dly, g in ((0.11, 0.25), (0.23, 0.15), (0.37, 0.08)):
    d = int(dly * SR); rev[d:] += g * mix[:-d]
fade_in = np.minimum(1, t / 0.4); fade_out = np.minimum(1, (dur - t) / 1.2)
rev *= fade_in * np.clip(fade_out, 0, 1)
rev = rev / (np.max(np.abs(rev)) + 1e-9) * 0.5  # ok. -6 dBFS szczytowo
pcm = (rev * 32767).astype(np.int16)
stereo = np.stack([pcm, np.roll(pcm, 120)], axis=1)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(stereo.tobytes())
print(out, dur)
