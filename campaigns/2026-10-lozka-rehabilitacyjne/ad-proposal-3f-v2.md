# Kreacja 3F na Facebooka — nowe kierunki wizualne (v2)

- Data: 2026-10-14. Status: `creative_ready`. Podglądy kompozycji do oceny, nie materiał do emisji.
- Zakres: Facebook, 3F, cel — telefony o wynajem. Warianty regionalne: **Śląsk** i **Kraków**, każdy osobno. Kraków oznacza wyłącznie miasto, nie Małopolskę.
- Stałe: telefon kampanii „Zadzwoń: 14 694 10 00”, cena 3F „150 zł / miesiąc” (nie dotyczy TWIST). Bez bezpłatnej dostawy, terminu 24 h i deklaracji dostępności.
- Szkice v1 (`sketches/`, `ad-proposal-3f.md`) zostały **odrzucone przez właściciela 2026-10-14** i nie są punktem wyjścia.
- Akceptacja kierunku wizualnego nie jest zgodą na emisję ani na budżet.

## Źródło zdjęć

- Wskazany folder `C:\ai dysk\Social Media - Siloe\zdjęcia` to ścieżka na komputerze właściciela. **To środowisko nie ma do niej dostępu** (kontener Linux w chmurze, bez dysku C:). Na Google Drive nie ma folderu o tej nazwie: wyszukano „Social Media - Siloe”, „ai dysk” i foldery „zdjęcia”. Sprawdziłem też folder „1. Social - Media” — zawiera tylko arkusze.
- Podglądy v2 używają zdjęcia z Drive: `Łóżko Rehabilitacyjne 3F - Model PSL013 - ANTAR - Zdjęcia/02.ANTAR-Model PSL013-Siloe24.jpg`. **Nie wiem, czy to ten sam plik co w folderze wskazanym przez właściciela.** To kandydat do porównania, nie potwierdzone źródło.
- Identyfikacja modelu jest **NIEPOTWIERDZONA**: zdjęcie przedstawia ANTAR PSL013, a we flocie są też inne łóżka (B14). Prawa do zdjęcia są **NIEPOTWIERDZONE** (B15).
- Obróbka produktu: wyłącznie wycięcie tła i skalowanie. Piksele łóżka — rama, barierki, materac, koła, pilot, siłownik — są bez zmian; nie użyto AI. Prześwity między barierkami są przezroczyste, materac nienaruszony. Sprawdzone wizualnie na kontrastowym tle.
- Otoczenie (pokój, studio, drzwi) to **makieta kompozycji złożona programowo**, a nie fotografia. Pokazuje kadr, światło, proporcje i typografię. Warstwa fotograficzna ma powstać w Higgsfield lub na sesji (sekcja niżej). Skrypt składu: `sketches-v2/src/compose.py`.

## Trzy kierunki

Podglądy 1080×1350 (4:5) w wariancie Śląsk: [v2-1-dom.jpg](sketches-v2/v2-1-dom.jpg) · [v2-2-produkt.jpg](sketches-v2/v2-2-produkt.jpg) · [v2-3-usluga.jpg](sketches-v2/v2-3-usluga.jpg) · [zestawienie](sketches-v2/v2-zestawienie.jpg).

### 1. „Przygotuj dom do opieki”

- Kadr: jasny, ciepły pokój — okno z firanką po prawej, dzienne światło padające na podłogę, drewniana podłoga, jasny dywan, szafka nocna. Łóżko zajmuje ok. 70% szerokości i dolne 55% kadru. Horyzont ustawiony wysoko, zgodnie z kątem zdjęcia produktu.
- Tekst: nagłówek „Przygotuj dom do opieki”; pomocniczo „Elektryczne łóżko rehabilitacyjne z materacem w zestawie”. Granatowy przycisk „Zadzwoń: 14 694 10 00”, obok „150 zł / miesiąc”.
- Uzasadnienie: emocja spokoju i gotowości. Odbiorca widzi efekt — miejsce opieki gotowe w domu. Najsilniejszy przekaz, ale najbardziej zależny od jakości warstwy fotograficznej pokoju.

### 2. „Wynajmij łóżko rehabilitacyjne” — REKOMENDOWANY

- Kadr: studyjna prezentacja produktu na głębokim granacie z niebieskim światłem i plamą światła na podłodze. Łóżko na całą szerokość kadru, ok. 50% wysokości, wyraźny cień kontaktowy.
- Tekst: biały nagłówek „Wynajmij łóżko rehabilitacyjne”; pomocniczo „Elektryczna regulacja oparcia, nóg i wysokości”. Niebieski blok ceny „150 zł — za miesiąc wynajmu” i biały przycisk „Zadzwoń: 14 694 10 00”.
- Uzasadnienie: najwyższa czytelność na telefonie i najmocniejszy kontrast w feedzie. Oferta jest zrozumiała w sekundę, bez dodatkowych obietnic.

### 3. „Pomożemy zorganizować sprzęt do domu”

- Kadr: widok przez otwarte drzwi do jasnego, niebiesko-białego pokoju. Ciepła ściana korytarza i rama drzwi na pierwszym planie dają głębię, a łóżko dominuje w środku. Bez ludzi — osoba może się pojawić tylko na prawdziwym zdjęciu pracownika Siloe, ze zgodą na wizerunek (organic + paid), w zwykłym stroju, bez sugerowania kwalifikacji medycznych. Nie generować osoby.
- Tekst: nagłówek „Pomożemy zorganizować sprzęt do domu”; pomocniczo „Doradzimy, dowieziemy i zmontujemy łóżko.” U dołu przycisk telefonu i „150 zł / mies.”
- Uzasadnienie: akcent na usługę („wszystko w jednym miejscu”). Uwaga: przy cenie zdanie o dowiezieniu i montażu może być odczytane jako „w cenie”. Przed finalizacją potrzebny zatwierdzony zapis o koszcie transportu (B16).

## Rekomendacja

**Kierunek 2.** Daje najmocniejszy efekt przy obecnych materiałach. Studyjna scena jest naturalnym środowiskiem dla katalogowego zdjęcia produktu, więc nie udaje mieszkania, którego nie sfotografowano. Cena i telefon są najczytelniejsze na telefonie. Kierunek 1 warto przygotować jako drugą komórkę testu, gdy powstanie prawdziwa warstwa fotograficzna pokoju.

Wersje regionalne po wyborze kierunku: dwie osobne grafiki z nadtytułem „Wynajem łóżek rehabilitacyjnych — Śląsk” albo „Wynajem łóżek rehabilitacyjnych — Kraków”. Jeden region na grafice, bez listy miast.

## Higgsfield

- Połączenie: aktywne (plan „plus”, 1200 kredytów). Model rekomendowany przez Higgsfield do produktu z referencją: `marketing_studio_image`. Koszt sprawdzony zapytaniem `get_cost` 2026-10-14: **2 kredyty za podgląd 4:5**, zarówno w 1k, jak i w 2k.
- **Generacji nie uruchomiono.** Polityka sieci tej sesji blokuje `upload.higgsfield.ai` (wgranie referencji zwróciło 403) oraz `d2ol7oe51mr4n9.cloudfront.net` (pobranie wyniku). Bez wgrania referencji nie da się wygenerować wiernego tła wokół produktu. Bez pobrania wyniku nie mogę porównać podglądu ze źródłem przed pokazaniem go właścicielowi. Utworzony został tylko pusty slot uploadu (media_id `f95ff7f2-…`, niepotwierdzony, bez pliku).
- Do uruchomienia potrzebne są: (1) dodanie obu hostów do dozwolonych domen środowiska; (2) zgoda na **3 podglądy × 2 kredyty = 6 kredytów** (po jednym tle na kierunek), z rezerwą do 12 kredytów na ewentualne powtórki.
- Sposób pracy: Higgsfield generuje tylko otoczenie wokół referencji `02`. Każdy wynik jest porównywany ze źródłem w 100% (rama, 4 barierki, szczyty, siłownik, pilot, koła, materac). Przy jakiejkolwiek deformacji produktu wynik nie jest używany w całości — bierzemy z niego tylko tło, a na nie nakładamy oryginalny wycięty produkt, tak jak w tych podglądach. Napisy i logo zawsze składane osobno.
- Prompt otoczenia, kierunek 1: „Bright, real Polish apartment bedroom in natural daylight, window with sheer curtain on the right, light oak floor, pale blue-grey rug, small wooden bedside table, warm white walls with soft blue accents, calm and tidy, no people, no text, no logos, empty space in the upper left third for typography, camera height and angle matching the reference bed photo, keep the bed from the reference exactly unchanged.”
- Prompt otoczenia, kierunek 2: „Professional studio product photograph, deep navy seamless backdrop with soft blue rim light, subtle floor spotlight, realistic soft contact shadow, the reference bed exactly unchanged, no people, no text, empty upper third for typography.”
- Prompt otoczenia, kierunek 3: „View through an open white door into a bright blue-and-white bedroom, warm hallway wall in the foreground for depth, daylight, oak floor, the reference bed exactly unchanged in the room, no people, no text, empty upper area for typography.”

## Co jest potrzebne do finalizacji

1. Wskazane zdjęcia z folderu `C:\ai dysk\Social Media - Siloe\zdjęcia`: wgrane na Drive (link) albo do `assets/products/` w repozytorium. Najlepiej oryginały pełnej rozdzielczości łóżka 3F, które faktycznie wynajmujemy.
2. Potwierdzenie modelu 3F na zdjęciu (B14) i praw do jego reklamowego użycia (B15).
3. Odblokowanie `upload.higgsfield.ai` i `d2ol7oe51mr4n9.cloudfront.net` oraz zgoda na 6 kredytów podglądów. Alternatywa: prawdziwa sesja zdjęciowa łóżka w mieszkaniu.
4. Zapis o koszcie transportu, jeśli w kreacji pojawi się dowóz lub montaż (dotyczy głównie kierunku 3).
5. Logo i kolory marki do finalnej typografii (podglądy używają roboczej palety granat / niebieski / biel).
