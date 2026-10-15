# Końcowy raport QA — H1/H2, eksport v2

Data: 2026-10-15. Wynik: **PASS — publication_ready** dla H1 i H2. H3: **withheld**, poza eksportem. Zgoda na emisję i budżet: nieudzielona.

## Zakres i dowody

18 plików mediów: 12 statyk (H1/H2 × 3 proporcje × PNG/JPG), 2 okładki, 4 filmy (15 s/6 s × silent/music), dodatkowo 2 czyste SRT. Obejrzano po eksporcie wszystkie siedem kompozycji statycznych, 10 klatek filmu 15 s (0,6; 3,4; 5,8; 6,8; 7,7; 9; 11,9; 12,7; 13,6; 14,8 s) i 5 klatek filmu 6 s (0,6; 2,9; 3,5; 4,5; 5,8 s). Wersje z muzyką mają kopiowany identyczny strumień obrazu.

| Kontrola | Wynik |
|---|---|
| Polskie znaki | Poppins: poprawne „Łóżko”, „Zadzwoń”, „dostępność”, „miesięcznie”, „Wysokość”, „się” |
| Cena | 150 zł miesięcznie na statykach i w scenie ceny filmu 15 s; film 6 s zachowuje pierwotny skrót z funkcjami i telefonem |
| Telefon | 14 694 10 00 na statykach i końcowych planszach filmów; okładka bez numeru jak w bazie |
| Logo | istniejący znak odczytany z zatwierdzonego PNG; bez generowania i przerysowania, proporcje zachowane |
| Produkt | te same źródła S4, funkcje kadrowania i wklejania pikseli; brak generowanych klatek lub zmiany segmentów |
| Napisy techniczne | usunięto draft_tag, TAG, komentarz ceny i numeru; brak na obejrzanych obrazach i klatkach; SRT czyste |
| 1:1 | lista 23→30 px; etykiety 21→30 px; materac przy y=525, bez kolizji z listą |
| Stories | panel z y=1392–1560 do y=1272–1440; cyfry kończą się około y=1415; etykieta regulacji podniesiona do y=1130 |
| Okładka | logo podniesione o 120 px do y=1385–1481 |
| Filmy / CTA | numer w centralnej planszy około y=1100, z dużym zapasem od dołu |
| Czytelność | podglądy szerokości 360–540 px; brak uciętych liter lub kolizji |
| PNG / JPG | RGB, poprawne proporcje; 7/7 par: średnia różnica kodowania <3/255 na kanał |
| Wideo | 4/4 pliki dekodowane w całości bez błędów; H.264, 1080×1920, 30 fps, yuv420p, faststart; 15,0 i 6,0 s |
| Audio | istniejący music.py, AAC 192 kb/s; silent bez audio; brak subiektywnego odsłuchu, struktura i dekodowanie poprawne |
| Transfer | 18 uploadów HTTP 200; potwierdzone w bibliotece; ponowne pobranie zgodne z pełnym SHA-256 |
| H3 | nie wyeksportowano; nie ma go w katalogu aktualnego pakietu |

## Granice kontroli

Strefy są marginesami projektowymi, nie gwarancją wszystkich wariantów interfejsu Meta. Podglądy placementów należy sprawdzić przed faktycznym uruchomieniem. Nie wykonywano oceny fizycznego urządzenia ani oceny medycznej. Otwarte kwestie praw i warunków usług pozostają wyłącznie w dokumentacji. Nie dodano obietnic dostawy w 48 h, darmowego transportu lub właściwości leczniczych.

## Poprawki wychwycone w tej rundzie

1. Podniesiony panel Stories kolidował z etykietą regulacji — podniesiono etykietę przed finalnym eksportem.
2. Przy odzyskiwaniu logo z PNG usunięto z kadru fragment tła narożnika; użyto dokładnego obszaru znaku bez przerysowania.
3. Transfer urllib zwracał 403; upload curl z wymaganymi nagłówkami zakończył się HTTP 200.
4. Pierwszy upload okładki zastąpiono po podniesieniu logo. Nie używać ID 4913122d… i 4826660b…; aktualne ID są w manifeście.

Koszt tej rundy: **0 kredytów**. Nie opublikowano materiałów, nie wysłano ich klientom i nie uruchomiono wydatków.
