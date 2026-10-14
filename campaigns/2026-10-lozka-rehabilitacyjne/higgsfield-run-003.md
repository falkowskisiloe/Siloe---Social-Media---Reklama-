# Higgsfield — runda 3: łóżko 3F z materiałów właściciela, nowa typografia

- Data: 2026-10-14. Status: `creative_ready` — **propozycje do oceny, nie materiał finalny**. Nic nie opublikowano i nie uruchomiono emisji.
- Ocena właściciela po rundzie 2: 2/10. Fotografia jest lepsza, ale żadna reklama nie została zaakceptowana. Zakres rundy 3: spójność produktu, marki, typografii i oferty. TWIST jest pominięty.
- Kredyty: **12 / 50** (runda 2: 6; runda 3: 6). Saldo 1200 → 1188.

## 1. Referencja

| Plik (załącznik właściciela) | Decyzja |
| --- | --- |
| `2.png` — łóżko 3-funkcyjne, PNG z przezroczystym tłem (w podglądzie czarnym), 500×500 px | **Przyjęta referencja produktu.** W Higgsfield jako `media_id 748bc326-d1e2-4c9c-bfe9-eef1f98bff5a`, piksele bez zmian, podłożone jasnoszare tło zamiast przezroczystości |
| `1.png` — logo Siloe, PNG z przezroczystością, 500×500 px | Logo wstawione do składu jako plik; nie było przerysowywane przez generator. Kolor z logo: niebieski `#009DE4` |
| `3.webp` — przykład fotografii wnętrza | Tylko kierunek nastroju (jasne, naturalne wnętrze). Nie jest referencją produktu: pokazuje inne łóżko z materacem i pościelą |
| Drive: `Łózko rehabilitacyjne 3F.svg` | Sprawdzony pod kątem wyższej rozdzielczości. Zawiera inną, wygenerowaną grafikę łóżka (z materacem i poduszkami), więc go odrzucono |
| Drive: ANTAR PSL013 | Nieużyty, zgodnie z poleceniem |

Cechy referencji, które obowiązują: bukowe szczyty z ciemniejszymi słupkami, dwie barierki na każdy bok, bukowe nogi i rama, **goły stelaż listwowy bez materaca** z czarnymi uchwytami listew, uniesione oparcie i sekcja kolan, chromowane ograniczniki materaca, **szary wysięgnik z trójkątnym uchwytem**, pilot na spiralnym kablu na bliższej barierce, 4 koła z hamulcami.

Ograniczenie: referencja ma tylko 500 px, więc detale w wynikach 2K (np. przyciski pilota, słoje drewna) dorysował generator. Lepsza jakość wymaga oryginału w wyższej rozdzielczości albo sesji zdjęciowej.

## 2. Generacja — trzy zaplanowane kompozycje

Model: `nano_banana_pro`, 4:5, 2K. Status zadań ponownie zwrócił model `nano_banana_2`. Kąt 3/4 taki sam jak w referencji, bez osób, tekstu, logo, materaca i dodatkowego wyposażenia, z zarezerwowanymi strefami na tekst.

| ID | Plan kompozycji | Job ID | Wynik kontroli |
| --- | --- | --- | --- |
| K1 | Łóżko na środku, pusta ściana w górnych 35% | `25675f8f-1cd1-47bd-84f8-2cd21fd545ca` | Konstrukcja zgodna, dobre światło. **Odrzucona:** szczyt nóg ciemniejszy i bardziej czerwony niż w referencji |
| **K2** | Łóżko w środkowym pasie, ściana u góry (logo i nagłówek), podłoga u dołu (cena i telefon) | `1f9a41eb-c552-4ac0-a8e3-8d9df6eafe69` | **Wybrana.** Najwierniejsza: kolory, listwy i uchwyty, ograniczniki, pilot, wysięgnik, silnik pod oparciem, 4 koła. Całe łóżko widoczne i duże, bez przesłonięć |
| K3 | Łóżko przy prawej krawędzi, okno po lewej | `ed3d96f3-1e4c-4391-b369-c70cb0c60e6c` | **Odrzucona:** łóżko odbite lustrzanie (szczyt głowy po prawej, pilot po drugiej stronie), mniejsze w kadrze |

Korekta K2 poza generatorem: delikatne cienie kontaktowe pod czterema kołami, wyłącznie na podłodze; produktu nie zmieniano. Bez tej poprawki koła sprawiały wrażenie lekko unoszących się.

## 3. Skład reklamy (Facebook / Instagram feed 4:5, 1080×1350)

- Font: Manrope (OFL, z paczki fontsource scalono podzbiory latin i latin-ext), grubości 500/600/700/800. Polskie znaki sprawdzone.
- Kolory: granat `#14284B` dla tekstu, niebieski z logo `#009DE4` jako akcent, biel. Margines 64 px.
- Treść: „Łóżko rehabilitacyjne”, „Wynajem 150 zł / miesiąc”, „Elektryczna regulacja. Materac w zestawie.”, „Zapytaj o wynajem”, „14 694 10 00”, region, logo Siloe.
- Uwaga: na zdjęciu nie ma materaca, a tekst mówi „Materac w zestawie”. To prawda według oferty (F11), ale materaca nie dodano do obrazu bez potwierdzenia, jak to pokazać.
- Kontrola w pomniejszeniu 360×450 px (szerokość ekranu telefonu w feedzie): nagłówek, cena i telefon czytelne, logo rozpoznawalne.

| Wariant | Układ |
| --- | --- |
| **B — rekomendowany** | Region jako mały nadtytuł, dwuwierszowy nagłówek po lewej, cena w niebieskim bloku w kolorze logo po prawej (oferta i cena w jednej linii wzroku). U dołu, bez paska: dopisek, CTA i duży telefon po lewej oraz logo po prawej, na wspólnej linii bazowej |
| A | Logo i oznaczenie regionu w górnym rzędzie, jednowierszowy nagłówek z dopiskiem, a u dołu biała karta z ceną i telefonem w dwóch kolumnach |

Rekomendacja B: kolejność czytania odpowiada zadanej hierarchii (co → ile → kontakt → kto). Cena jest najmocniejszym akcentem, a układ nie powtarza dolnego paska z poprzednich rund. Wersja A jest spokojniejsza i stawia markę na pierwszym miejscu, ale jej karta cenowa przypomina pasek.

Wersje regionalne: `3f-B-slask`, `3f-B-krakow`, `3f-A-slask`, `3f-A-krakow`. Region jest jedyną różnicą.

## 4. Pliki

Zgodnie z B17 obrazy (wyniki i projekty) **nie są w repozytorium**. Są w Higgsfield pod powyższymi Job ID i w kopiach roboczych sesji. W repozytorium jest skrypt składu `runda-3/src/compose3.py` (argumenty: katalog z `k2.png` i `logo-siloe.png`, katalog wyjściowy, katalog z TTF Manrope).

## 5. Otwarte

Wybór wariantu i ocena właściciela (B11); prawa do zdjęcia `2.png` i identyfikacja modelu (B14/B15 dla nowego pliku); czy pokazywać materac na zdjęciu; zdjęcie w wyższej rozdzielczości; zgoda na emisję i budżet.
