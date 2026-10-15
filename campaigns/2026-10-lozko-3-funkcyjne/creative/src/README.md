# Odtworzenie czystych eksportów

Wymagania: Python 3, Pillow, numpy, ffmpeg/ffprobe. Uruchom z katalogu skryptów:

```bash
python3 prepare_inputs.py /tmp/siloe-input /tmp/siloe-fonts
python3 build_static.py /tmp/siloe-input /tmp/siloe-fonts /tmp/siloe-output
python3 build_video.py /tmp/siloe-input /tmp/siloe-fonts /tmp/siloe-output cover
python3 build_video.py /tmp/siloe-input /tmp/siloe-fonts /tmp/siloe-output 15
python3 build_video.py /tmp/siloe-input /tmp/siloe-fonts /tmp/siloe-output 6
python3 music.py 15 /tmp/siloe-15.wav
python3 music.py 6 /tmp/siloe-6.wav
ffmpeg -i /tmp/siloe-output/3f-meta-reel-15s-v2-silent.mp4 -i /tmp/siloe-15.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -t 15 -movflags +faststart /tmp/siloe-output/3f-meta-reel-15s-v2-music.mp4
ffmpeg -i /tmp/siloe-output/3f-meta-reel-6s-v2-silent.mp4 -i /tmp/siloe-6.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -t 6 -movflags +faststart /tmp/siloe-output/3f-meta-reel-6s-v2-music.mp4
```

Skrypt statyk eksportuje domyślnie tylko H1/H2. Definicji H3 nie wykonuje. Nie używa API generacji. Poppins: SIL OFL, zachować OFL.txt. Wersje Pillow/ffmpeg mogą zmieniać bajty wyjściowe; sumy w manifeście identyfikują dostarczone eksporty.
