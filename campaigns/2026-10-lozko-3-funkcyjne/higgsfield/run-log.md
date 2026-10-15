# Dziennik produkcji — Higgsfield i skład (łóżko 3F, Meta, 2026-10)

**Status:** `creative_ready` — wszystkie materiały są projektami roboczymi. Higgsfield niczego nie publikował i nie uruchomił reklam.

## Kredyty

| Pozycja | Kredyty |
|---|---|
| Zatwierdzona pula produkcji 3F | 50 |
| Wydane przed tą rundą (rundy 2–7, kampania 2026-10-lozka-rehabilitacyjne) | 44,75 |
| Ta runda: outpaint 9:16 | 2 |
| Ta runda: outpaint 1:1 | 2 |
| **Razem wydane** | **48,75 / 50** (saldo konta 1200 → 1151,25) |
| Pozostało w puli | 1,25 |

Wyceny bez wydatku: wideo `kling3_0`, 5 s, 9:16, z obrazu = **10 kredytów**. Przekracza pulę, więc nie uruchomiono. Potrzebna byłaby nowa zgoda (patrz „Odrzucone / niewykonane”).

## Przebieg

| Krok | Narzędzie / ustawienia | Próby | Wynik |
|---|---|---|---|
| 1. Odszukanie grafiki bazowej | repozytorium, materiały zadania | — | W repozytorium jej nie ma. W materiałach zadania jest `8.webp` (1080 × 1350) przekazana przez właściciela 2026-10-15 jako baza. Źródła w Higgsfield: S4 `36c754cd-…`, układ `b5431c60-…` |
| 2. Projekt roboczy | `create_project` | 1 | `Siloe \| Łóżko 3F \| Meta \| 2026-10` (`405c9e29-…`) |
| 3. Tło 9:16 | `outpaint_image`, 9:16 | 1 | 1536 × 2752; łóżko przerysowane (różnica ok. 10/255), więc środek zastąpiono oryginałem S4 |
| 4. Tło 1:1 | `outpaint_image`, 1:1 | 1 | 2048 × 2048; łóżko przerysowane (ok. 11,6/255), więc środek zastąpiono oryginałem S4 |
| 5. Grafiki statyczne | `creative/src/build_static.py` (PIL, Poppins 400–700, logo z pliku właściciela) | 3 iteracje | 9 plików × PNG + JPG (H1–H3 × 4:5, 1:1, 9:16) |
| 6. Film 15 s / 6 s | `creative/src/build_video.py`; tło 2160 × 3840, wyjście 1080 × 1920, 30 kl./s, x264 High, CRF 18, yuv420p, faststart | 3 iteracje | wersje bez dźwięku |
| 7. Muzyka | `creative/src/music.py` — autorski podkład syntetyczny (C–Am–F–G, ok. 60 BPM, szczyt ok. −6 dBFS) | 1 | AAC 192 kb/s w wersjach `-music` |
| 8. Okładka Reels | `build_video.py cover` | 2 | 1080 × 1920 |
| 9. Magazyn mediów | `media_upload` + PUT + `media_confirm` | 24 pliki + 2 ponowne (film 15 s po poprawce); 1 PUT powtórzony po błędzie 520 | adresy w `manifest.md`; pobranie każdego pliku zgodne z SHA-256 |

## Odrzucone wersje i powody

| Wersja | Powód odrzucenia |
|---|---|
| Surowe tła outpaint jako pełne kadry | generator przerysował łóżko; użyto tylko ściany i podłogi |
| Statyki — iteracja 1 | „150 zł” ucięte na naklejce; zawinięty róg zasłaniał „miesięcznie”; podtytuł H1 4:5 wchodził pod naklejkę |
| Statyki — iteracja 2 | róg naklejki dotykał „miesięcznie”; podtytuł H2 pod naklejką (skrócony do „Łóżko 3-funkcyjne na wynajem”) |
| Film 6 s — iteracja 1 | napis „Oparcie • Nogi • Wysokość” nieczytelny na tle pościeli; dodano półprzezroczystą kartę pod nagłówki |
| Film 15 s — iteracja 1 | naklejka ceny zachodziła na planszę końcową; wygaszana przed 13 s zgodnie ze storyboardem |
| Okładka — iteracja 1 | logo zasłaniało podstawę stolika; przeniesione na dywan |
| Film 15 s — iteracja 2 | etykieta „Wysokość” w dolnej strefie interfejsu Reels (y≈1374); przeniesiona do y≈1100. Wcześniej wgrane pliki `f080d3e2-…` i `422fe7e4-…` zastąpiono przez `c3365e3e-…` i `24a180a0-…` |

## Niewykonane

- **Wideo generatywne (Kling 3.0, 5 s = 10 kr.)**: poza pulą 50 kr. Zadanie i tak zabrania animowania segmentów łóżka z jednego zdjęcia. Motion graphic z oryginalnych pikseli spełnia storyboard bez ryzyka deformacji produktu. Jeśli właściciel chce ujęcia z ruchem kamery z modelu, potrzebna jest nowa zgoda na kredyty, a wynik przejdzie kontrolę konstrukcji klatka po klatce.
- **Pozostawienie plików w folderze projektu Higgsfield**: `media_upload` nie przyjmuje folderu docelowego, a narzędzie `outpaint_image` nie przyjmuje `folder_id`. Pliki są w bibliotece mediów konta (stałe adresy w manifeście). Projekt `405c9e29-…` istnieje jako miejsce robocze.
- **Pliki graficzne w repozytorium**: celowo pominięte (B17 — publiczne repozytorium, niepotwierdzone prawa do zdjęcia).

## Fonty i licencje

- Poppins 400/500/600/700 (SIL Open Font License 1.1), pakiet npm `@fontsource/poppins@5.0.14`; podzbiory latin + latin-ext scalone (polskie znaki).
- Muzyka: wygenerowana w całości skryptem `music.py`, bez próbek i utworów osób trzecich. Brak praw osób trzecich do rozliczenia. Alternatywa przy emisji: Meta Sound Collection.
