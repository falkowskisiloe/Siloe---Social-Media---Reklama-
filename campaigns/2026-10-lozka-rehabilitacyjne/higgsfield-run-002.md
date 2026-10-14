# Higgsfield — zlecenie 002: trzy warianty reklamy 3F na zdjęciu referencyjnym

- Data: 2026-10-14. Status: `creative_ready`, czeka na ocenę właściciela. Nic nie opublikowano i nie uruchomiono budżetu reklamowego.
- Kredyty: **6 / 50** (saldo 1200 → 1194; 3 podglądy po 2 kredyty).
- Poprzednia blokada sieci z [higgsfield-run-001.md](higgsfield-run-001.md) jest usunięta.

## 1. Przepływ plików

| Etap | Wynik |
| --- | --- |
| Test wysyłki (syntetyczny PNG, bez produktu) | PUT `upload.higgsfield.ai` → HTTP 200, `media_id 45f3061c-…`. **Nie używany jako referencja.** |
| Pobranie wysłanego pliku (`d2ol7oe51mr4n9.cloudfront.net`) | HTTP 200, plik identyczny z wysłanym |
| Pobranie wyniku (`d8j0ntlcm91z4.cloudfront.net`) | HTTP 200 po dodaniu domeny przez właściciela |
| Referencja produktu | `02.ANTAR-Model PSL013-Siloe24.jpg` z Google Drive (1500×1500) → `media_id 60e120d4-4b3d-4cbd-91bd-aa64d99e6778`. Ten sam plik co w zleceniu 001; B14 i B15 nadal otwarte |

## 2. Generacja

- Wywołany model: `nano_banana_pro`, 4:5, 2K, referencja jako `image_references`. **Uwaga:** status zadań zwrócił model `nano_banana_2`. Higgsfield mógł wykonać zadania tańszym modelem niż zamówiony. Koszt był zgodny z wyceną: 2 kredyty za podgląd.
- Wynik: 1856×2304 px. Prompty zachowują produkt bez zmian i nie dodają osób, tekstu, logo ani wysięgnika.

| Wariant | Hipoteza | Job ID |
| --- | --- | --- |
| V1 — dom | Odbiorca reaguje na obraz gotowego, spokojnego miejsca opieki w mieszkaniu | `c4894754-1504-4e80-95ea-36301f5799a7` |
| V2 — studio | Czytelna oferta i kontrast w feedzie wygrywają z kontekstem | `207e209c-d32a-4dd6-ae91-cfec934c70c3` |
| V3 — przez drzwi | Akcent na usługę i przestrzeń w pokoju | `1d5bacb9-c081-48d5-b6a2-405d2ee7b481` |

## 3. Kontrola konstrukcji (wynik vs referencja, pełna rozdzielczość)

| Element referencji | V1 | V2 | V3 |
| --- | --- | --- | --- |
| Dwa bukowe szczyty, szczyt nóg na szarej ramie stalowej | zgodne | zgodne | zgodne (szczyt nóg częściowo zasłonięty ościeżnicą) |
| 2 barierki na bok, brązowe zaślepki | zgodne | zgodne | zgodne |
| Rama jasnoszara, poprzeczki | zgodne | zgodne | zgodne |
| Siłownik pionowy + czarny silnik przy szczycie nóg | zgodne | zgodne | widoczny tylko fragment silnika |
| Pilot na spiralnym kablu, na barierce | zgodne | zgodne | zgodne |
| 4 koła z hamulcami | zgodne | zgodne | zgodne (widoczne 3) |
| Materac biały, płasko | zgodne | zgodne | zgodne |
| Dodane elementy | brak (szafka nocna to otoczenie) | brak | brak |

Kontrola wizualna; nie wykonano pomiaru proporcji. Drobne różnice wynikają z generatora, np. rysunek przycisków pilota i usłojenie drewna. Nie zmieniają one konstrukcji ani funkcji.

## 4. Wybór

- **Najlepszy: V1 — dom.** To najwierniejsze odwzorowanie przy najczytelniejszym, dużym produkcie. Wariant odpowiada założeniu „prawdziwe mieszkanie, naturalne światło” z zadania 001 i nie powtarza odrzuconego motywu gradientu.
- V2 — wierny i najbardziej kontrastowy. Ryzyko: estetyka studyjna jest bliska wcześniej odrzuconym makietom na granacie. Warto go pokazać jako drugą komórkę testu tylko wtedy, gdy właściciel zaakceptuje ten kierunek.
- V3 — zgodny konstrukcyjnie, ale produkt jest mały i ucięty ościeżnicą. Nie nadaje się jako główna kreacja; może posłużyć jako tło Stories lub karuzeli.

## 5. Projekty reklam (Facebook 4:5, wariant Śląsk)

Tekst złożono poza generatorem. Wszystkie elementy pochodzą z potwierdzeń właściciela (facts F01, F09, F10, F11):

- nadtytuł: „Wynajem łóżek rehabilitacyjnych · Śląsk”;
- V1: „Przygotuj dom do opieki” / „Elektryczne łóżko rehabilitacyjne z materacem w zestawie”;
- V2: „Wynajmij łóżko rehabilitacyjne” / „Elektryczna regulacja oparcia, nóg i wysokości”;
- V3: „Pomożemy zorganizować opiekę w domu” / „Dobierzemy łóżko i pokażemy jego obsługę”. Bez wzmianki o dostawie, bo cena transportu jest niepotwierdzona (B16);
- przycisk „Zadzwoń: 14 694 10 00” oraz „150 zł / miesiąc”.

Logo i kolory marki są nadal robocze (BRAND-01).

## 6. Przechowywanie plików

Zgodnie z B17 (publiczne repozytorium, niepotwierdzone prawa do packshotu ANTAR) wyniki i projekty **nie zostały dodane do repozytorium**. Znajdują się w Higgsfield pod powyższymi Job ID, a kopie robocze w sesji. Skrypt składu tekstu można dodać po decyzji B17.

## 7. Otwarte przed emisją

B14 (czy wynajmowany 3F to ANTAR PSL013), B15 (prawa do zdjęcia), B16 (transport), BRAND-01, wersja Kraków, akceptacja B11 dla wybranego pliku, zgoda na budżet.
