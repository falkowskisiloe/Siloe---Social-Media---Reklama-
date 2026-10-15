# Raport QA — łóżko 3F, Meta, 2026-10

**Data:** 2026-10-15 · **Zakres:** 24 pliki z `manifest.md` oraz teksty H1–H3
**Wynik:** brak błędów blokujących w samych kreacjach. **Emisja pozostaje zablokowana** do potwierdzenia danych (sekcja 6). H3 jest zablokowany w całości.

## 1. Zgodność wyglądu produktu

| Kontrola | Metoda | Wynik |
|---|---|---|
| Łóżko pochodzi z zaakceptowanego zdjęcia S4 | porównanie pikseli obszaru łóżka z S4 przeskalowanym do danego formatu | 4:5: 1,22 · 1:1: 2,26 · 9:16: 1,42 · film (2x): 0,55 — średnia różnica na 255. To błąd przeskalowania. Surowy outpaint dawał ok. 10–11,6, więc w środek wklejono oryginał |
| Rama, szczyty, barierki, pilot, kabel, koła, wysięgnik, materac, oparcie | przegląd wizualny klatek i statyk | bez zmian; segmenty się nie poruszają, nic nie dodano |
| Ruch w filmie | przegląd 8 klatek kontrolnych (15 s) i 3 klatek (6 s) | tylko najazd i zbliżenie kamery oraz animacja napisów; brak mechanicznej animacji łóżka |
| Osoby, pacjent, dane zdrowotne | przegląd | brak |
| Logo | plik właściciela `1.png`, wstawiony programowo | bez przerysowania |

## 2. Teksty i polskie znaki

| Kontrola | Wynik |
|---|---|
| Polskie znaki (ą, ę, ł, ó, ś, ż, ź, ć, ń) | font Poppins z podzbiorem latin-ext; teksty wpisane czcionką, a nie generowane. Sprawdzone wizualnie: „Łóżko”, „wniesienie”, „Zadzwoń”, „sprawdź dostępność”, „miesięcznie”, „Wysokość”, „zajmiemy się resztą” |
| Numer telefonu | wszędzie „14 694 10 00” (statyki, filmy, okładka bez numeru). Spójny, ale **do wyboru** (14 694 10 00 albo 792 020 020) |
| Cena | wszędzie „wynajem łóżka · 150 zł · miesięcznie”; w filmie z dopiskiem „cena robocza – do zatwierdzenia” |
| Zgodność z hipotezą | H1: proces usługi; H2: trzy regulacje; H3: 48 h (zablokowane). Każdy plik ma tylko argumenty swojej hipotezy plus wspólne elementy oferty (materac, cena, telefon) |
| Obietnice medyczne / diagnozowanie odbiorcy | brak; język neutralny („gdy organizujesz opiekę bliskiej osoby”) |
| „W cenie” / „bezpłatnie” | nie użyto. Na naklejce cena dotyczy „wynajmu łóżka”. **Ryzyko odbioru:** lista usług obok ceny może sugerować, że usługi są w cenie, więc trzeba potwierdzić zakres (sekcja 6) |

## 3. Formaty

| Plik | Wymóg | Wynik |
|---|---|---|
| Feed 4:5 | 1080 × 1350, PNG + JPG | ✓ (H1, H2, H3) |
| Feed 1:1 | 1080 × 1080, bez przycięcia łóżka, ceny, numeru i logo | ✓; całe łóżko z wysięgnikiem widoczne (tło rozszerzone na boki) |
| Stories 9:16 | 1080 × 1920, PNG + JPG | ✓ |
| Reels 15 s | 1080 × 1920, MP4 H.264, 15,0 s | ✓ H.264 High, 30 kl./s, yuv420p, faststart |
| Reels 6 s | 1080 × 1920, 6,0 s | ✓ |
| Okładka | 1080 × 1920, tekst w centrum, bez małych napisów | ✓ „Łóżko 3-funkcyjne do domu” + logo |
| Wersja z muzyką | prawa do reklamy | ✓ podkład autorski (`music.py`), AAC 192 kb/s, szczyt ok. −6 dBFS |
| Wersja bez dźwięku | czytelne napisy | ✓ wszystkie komunikaty w obrazie; plik bez ścieżki audio + `.srt` |

## 4. Strefy bezpieczne i czytelność

| Kontrola | Wynik |
|---|---|
| Stories 9:16 — górne 14% (do y≈269) i dolne 20% (od y≈1536) bez kluczowych treści | nagłówek od y=275; numer telefonu na linii y≈1532; logo y≈1440–1520. Mieści się, ale numer jest przy samej granicy — **uwaga drobna** |
| Reels — dolne ok. 35% zasłania interfejs (od y≈1250) | treści kluczowe w y≈266–1240; plansza końcowa y 650–1240. Etykietę „Wysokość” przeniesiono z y≈1374 do y≈1100 (poprawka po kontroli) |
| Prawa krawędź Reels (przyciski) | brak tekstu przy prawej krawędzi w dolnej połowie kadru |
| Czytelność na telefonie | podglądy 360 px szerokości: nagłówki, cena i numer czytelne. **Uwaga drobna:** w 1:1 etykiety i lista mają 21–23 px (ok. 7–8 px na ekranie) — czytelne, ale małe. Do rozważenia skrócenie listy w 1:1 |
| Znacznik „PROJEKT ROBOCZY” / „ZABLOKOWANE” | lewy górny róg wszystkich statyk i filmów (oprócz okładki). **Usunąć w wersji do emisji** |

## 5. Uwagi niezablokowane

1. Wskaźnik „Wysokość” w filmie trafia w bok ramy na wysokości koca; kropka nie wskazuje mechanizmu podnoszenia, bo na zdjęciu go nie widać.
2. Wysięgnik z uchwytem jest widoczny na zdjęciu, ale nie ma go w liście wyposażenia oferty. Decyzja właściciela.
3. Okładka nie ma znacznika roboczego (wymóg „bez małych napisów”). Jest projektem roboczym zgodnie z manifestem.

## 6. Blokady emisji (dane — nie kreacja)

| Element | Wartość robocza | Status |
|---|---|---|
| Okres ceny 150 zł | „miesięcznie” | DO ZATWIERDZENIA |
| Numer reklamowy | 14 694 10 00 albo 792 020 020 | DO WYBORU |
| Realizacja w 48 godzin | H3 | DO POTWIERDZENIA (obszar, weekendy, dostępność) |
| Obszar dostawy | Śląsk i Kraków (kampania) | lista miast i koszt DO POTWIERDZENIA |
| Godziny odbierania telefonu | „7 dni w tygodniu” (H3) | DO POTWIERDZENIA |
| Usługi w cenie | dostawa, wniesienie, montaż, instruktaż | DO POTWIERDZENIA |
| Prawa do zdjęcia produktu | — | DO POTWIERDZENIA (B15) |

## 7. Publikacja

Nic nie opublikowano, nie wysłano wiadomości, nie utworzono kampanii ani wydatków.
