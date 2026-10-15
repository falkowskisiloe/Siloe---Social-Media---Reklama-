# Raport QA — łóżko 3F, Meta, 2026-10

**Ostatnia kontrola:** 2026-10-15, zadanie 003 (pakiet czysty `v2`)
**Wynik:** H1 i H2 — `publication_ready`, brak błędów blokujących w plikach. H3 — `withheld`, pliki czyste, poza pakietem emisji.
**Publikacja:** nic nie opublikowano, nie wysłano wiadomości, nie utworzono kampanii ani wydatków.
**Kredyty Higgsfield w zadaniu 003:** 0. Bez nowych generacji: użyto istniejących skryptów i materiałów, saldo bez zmian (1151,25; pula 48,75 / 50).

## 1. Brak napisów technicznych

| Kontrola | Metoda | Wynik |
|---|---|---|
| „PROJEKT ROBOCZY”, „WERSJA TESTOWA”, „ZABLOKOWANE”, „cena robocza”, „do zatwierdzenia”, „numer do weryfikacji”, statusy QA | (1) usunięcie z kodu: `build_static.py` nie wywołuje `draft_tag`; `build_video.py` nie ma znacznika, dopisku pod ceną ani dopisku pod numerem. `grep` po skryptach nie znajduje tych fraz w tekstach rysowanych. (2) Przegląd wizualny wszystkich 9 statyk v2, okładki i 11 klatek kontrolnych filmów (15 s: 0,3 / 1,5 / 3,5 / 6,6 / 7,8 / 9,8 / 12,2 / 14,5 s; 6 s: 1,0 / 3,2 / 5,5 s) | ✓ brak we wszystkich plikach v2 |
| Status w nazwach plików | `-withheld` tylko w H3; H1 i H2 bez dopisków statusu | ✓ |

Teksty rysowane na plikach v2 to wyłącznie treści reklamowe: nagłówek, podtytuł, lista, etykiety „Materac w zestawie” / „Elektryczna regulacja”, naklejka „wynajem łóżka · 150 zł · miesięcznie”, panel z CTA i numerem, logo.

## 2. Kontrola każdego pliku (`publication_ready`)

| Plik | Wymiary / format | Polskie znaki | Numer 14 694 10 00 | Cena 150 zł miesięcznie | Logo | Produkt | Telefon (czytelność) | Strefy bezpieczne |
|---|---|---|---|---|---|---|---|---|
| `3f-meta-feed-4x5-h1-v2` .png/.jpg | 1080 × 1350 ✓ | ✓ | ✓ | ✓ naklejka | ✓ | ✓ | ✓ | n/d (Feed) |
| `3f-meta-feed-1x1-h1-v2` .png/.jpg | 1080 × 1080 ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ po powiększeniu | n/d |
| `3f-meta-story-9x16-h1-v2` .png/.jpg | 1080 × 1920 ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `3f-meta-feed-4x5-h2-v2` .png/.jpg | 1080 × 1350 ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | n/d |
| `3f-meta-feed-1x1-h2-v2` .png/.jpg | 1080 × 1080 ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ po powiększeniu | n/d |
| `3f-meta-story-9x16-h2-v2` .png/.jpg | 1080 × 1920 ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `3f-meta-reel-15s-v2-music.mp4` | 1080 × 1920, 15,0 s, H.264 High 30 kl./s, AAC 192 kb/s ✓ | ✓ | ✓ (13–15 s) | ✓ (11–13 s) | ✓ (13–15 s) | ✓ | ✓ | ✓ |
| `3f-meta-reel-15s-v2-silent.mp4` | jw., bez ścieżki audio ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `3f-meta-reel-6s-v2-music.mp4` | 1080 × 1920, 6,0 s, AAC ✓ | ✓ | ✓ (3,9–6 s) | n/d (bez ceny wg storyboardu) | ✓ | ✓ | ✓ | ✓ |
| `3f-meta-reel-6s-v2-silent.mp4` | jw., bez audio ✓ | ✓ | ✓ | n/d | ✓ | ✓ | ✓ | ✓ |
| `3f-meta-reel-cover-v2` .png/.jpg | 1080 × 1920 ✓ | ✓ „Łóżko 3-funkcyjne do domu” | n/d (okładka bez numeru) | n/d | ✓ | ✓ | ✓ duży tekst w centrum | ✓ |

Wszystkie 21 pliki (18 `publication_ready` + 3 `withheld`) pobrano z biblioteki mediów i porównano SHA-256 z plikami lokalnymi: zgodne 21/21 (`manifest.md`).

## 3. Produkt (brak deformacji)

| Format | Średnia różnica pikseli w obszarze łóżka względem zaakceptowanego zdjęcia S4 (0–255) |
|---|---|
| 4:5 | 1,22 |
| 1:1 | 2,26 |
| 9:16 (nowe położenie) | 2,90 |
| Film (tło 2x) | 0,55 |

Różnice wynikają wyłącznie z przeskalowania (surowy outpaint dawał ok. 10–11,6). Rama, szczyty, barierki, pilot z kablem, koła, materac i wysięgnik bez zmian. W filmie segmenty łóżka się nie poruszają; jedyny ruch to najazd i zbliżenie kamery oraz animacja etykiet.

## 4. Poprawki formatów z zadania 003

| Format | Zmiana | Pomiar |
|---|---|---|
| Stories 9:16 | zdjęcie przesunięte wyżej (S4 od y=150 zamiast 220, skala 0,705); panel z numerem przeniesiony z 1392–1560 na **1318–1468** | linia bazowa numeru y≈1447; zapas **≈89 px** od granicy dolnych 20% (y=1536) i **≈470 px** od dolnej krawędzi; nagłówek od y≈284 (górne 14% = 269). Dolny pas poniżej y≈1790 uzupełniono odbiciem podłogi (strefa interfejsu, poza produktem) |
| Feed 1:1 | lista 42 → 56 px wysokości, tekst 23 → 31 px; etykiety 21 → 29 px; panel 22/68 → 26/74 px; nagłówek 56 → 58 px | na ekranie telefonu (~375 px szerokości) tekst listy ≈ 11 px, etykiety ≈ 10 px, numer ≈ 26 px — czytelne. Etykieta „Elektryczna regulacja” stoi po prawej stronie pilota i częściowo zachodzi na dolną poprzeczkę boku łóżka (tak jak w zaakceptowanym 4:5); nie zasłania pilota, kół ani wysięgnika |
| Filmy 15 s i 6 s | usunięte: znacznik roboczy, dopisek pod ceną, dopisek pod numerem | ruch kamery, animacje etykiet i muzyka bez zmian |

## 5. Strefy bezpieczne (Stories / Reels)

| Kontrola | Wynik |
|---|---|
| Stories statyczne — górne 14% i dolne 20% bez kluczowych treści | ✓ (sekcja 4) |
| Reels — kluczowe treści powyżej y≈1250 (dolne ok. 35% zasłania interfejs) | ✓ nagłówki y≈266–480; etykiety y≈680–1240; plansza końcowa y 650–1240 |
| Prawa krawędź Reels (przyciski) | ✓ brak tekstu przy prawej krawędzi w dolnej połowie kadru |

## 6. Treść i zgodność

| Kontrola | Wynik |
|---|---|
| Obietnice medyczne, diagnozowanie odbiorcy, osoby lub pacjent na obrazie | brak |
| „W cenie” / „bezpłatnie” | nie użyto. **Ryzyko odbioru (nieblokujące dla plików):** w H1 lista usług stoi obok ceny. Potwierdzenie zakresu ceny w `approval-checklist.md` |
| Hipotezy | H1 — pełna obsługa; H2 — trzy regulacje; H3 (`withheld`) — 48 h |
| Muzyka | autorska (`creative/src/music.py`), bez praw osób trzecich |

## 7. Do decyzji przed uruchomieniem emisji (poza zakresem plików)

Zgoda na emisję i budżet, zakres usług w cenie, lista miast dostawy, prawa do zdjęcia produktu, wysięgnik. Szczegóły w `approval-checklist.md`.

## Historia

- 2026-10-15, zadanie 002: pakiet v1 `creative_ready` ze znacznikami roboczymi. Wycofany (`superseded` w manifeście).
