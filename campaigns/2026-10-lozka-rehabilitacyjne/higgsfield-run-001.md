# Higgsfield — zlecenie 001: fotografia łóżka 3F w mieszkaniu

- Data: 2026-10-14. Status: **ZABLOKOWANE na etapie przepływu plików** — generacja nieuruchomiona, kredyty nienaruszone (saldo 1200, plan „plus”).
- Wszystkie wcześniejsze projekty (szkice v1 i podglądy v2) zostały odrzucone przez właściciela. Nie powstają kolejne makiety z łóżkiem na gradiencie ani wnętrza rysowane z figur.
- Warsztat: `ad-creative` 2.11.0 i `image` 2.0.2 z marketingskills (źródło: `.agents/skills/vendor/marketingskills/SOURCE.md`). Zasady Siloe mają pierwszeństwo.

## 1. Test przepływu: referencja → Higgsfield → wynik

| Etap | Wynik | Dokładny komunikat |
| --- | --- | --- |
| Referencja dostępna lokalnie | OK | `02.ANTAR-Model PSL013-Siloe24.jpg`, 1500×1500 px, pobrana z Google Drive (folder ANTAR PSL013). To nie jest potwierdzony plik z `C:\ai dysk\Social Media - Siloe\zdjęcia`. |
| Połączenie z Higgsfield (MCP) | OK | `balance` zwraca 1200 kredytów; `models_explore` i `get_cost` działają |
| Utworzenie slotu uploadu | OK | `media_upload` → `media_id f95ff7f2-08e1-40be-bfdb-b01bcc23f6bc` (niepotwierdzony, bez pliku) |
| **Wysłanie pliku (PUT)** | **BŁĄD** | `curl -X PUT … https://upload.higgsfield.ai/…` → `curl: (56) CONNECT tunnel failed, response 403`. Proxy wyjściowe sesji odpowiada `HTTP/1.1 403 Forbidden` na CONNECT do `upload.higgsfield.ai:443`. Ponowny test 2026-10-14 bez zmian. |
| **Odbiór wyniku do kontroli** | **BŁĄD** | `https://d2ol7oe51mr4n9.cloudfront.net/` (host plików wynikowych i mediów Higgsfield) → `CONNECT tunnel failed, response 403`. Bez pobrania nie da się porównać wyniku ze źródłem przed pokazaniem. |

Dlaczego nie inną drogą:

- Przesłanie bajtów obrazu jako tekstu lub base64 przez inne narzędzie jest wykluczone przez instrukcję Higgsfield i nie omija kontroli wyniku.
- `media_import_url` wymaga publicznego adresu obrazu. Jedyny dostępny to publiczne repozytorium GitHub. Dodanie tam oryginalnego zdjęcia produktu przy niepotwierdzonych prawach (B15) byłoby jego dalszą publikacją — nie zrobiono tego bez decyzji właściciela.
- Nawet z importem przez URL nie da się pobrać wyniku do kontroli konstrukcji, więc warunek „porównaj przed pokazaniem” nie byłby spełniony.

Środowisko: ta sesja działa w **Claude Code w chmurze (claude.ai/code)**, nie w Codex Cloud. Dozwolone domeny ustawia się w ustawieniach środowiska tej sesji. Nie podaję instrukcji dla Codex Cloud, bo nie mam jego dokumentacji. Do odblokowania potrzebne są hosty: `upload.higgsfield.ai` i `d2ol7oe51mr4n9.cloudfront.net`.

## 2. Wybór modelu

Koszty sprawdzone 2026-10-14 przez `get_cost`, format 4:5:

| Model | Edycja z referencją | Maks. rozdzielczość, 4:5 | Koszt 4K | Ocena |
| --- | --- | --- | --- | --- |
| `nano_banana_pro` (Google) | tak, `image_references` | 4K, 4:5 | **4 kredyty** (2K: 2) | **Wybrany.** Najwyższa jakość edycji referencyjnej i fotorealizm; natywne 4:5 i 4K |
| `nano_banana_2` | tak, plus maska inpaint | 4K, 4:5 | 3 kredyty | Rezerwa: maska pozwala ograniczyć zmiany do otoczenia, gdyby Pro zmieniał produkt |
| `marketing_studio_image` | tak | 4K, 4:5 | 4 kredyty | Szablon „one-click ad” — mniej kontroli nad wiernością produktu |
| `gpt_image_2` | tak | 4K, bez 4:5 | — | Odrzucony: brak 4:5 |

Zlecenie: **1 podgląd `nano_banana_pro`, 4:5, 4K = 4 kredyty.** Ewentualne powtórki po 4 kredyty, każda po osobnej decyzji. Wymagana zgoda: na 4 kredyty, a przed odblokowaniem hostów — także na wgranie zdjęcia ANTAR do Higgsfield mimo niepotwierdzonych praw (B15).

## 3. Prompt (zgodnie z `image`: obiekt, otoczenie, styl, światło, kompozycja, parametry)

Referencja: `02.ANTAR-Model PSL013-Siloe24.jpg` (rola `image_references`).

> Place the exact electric care bed from the reference image, completely unchanged, in a bright, warm, real Polish apartment bedroom. Soft natural daylight from a window on the left, light oak floor, warm white walls, muted blue linen curtain, small wooden bedside table. Camera angle and height match the reference 3/4 view. The whole bed visible and large in frame, realistic contact shadows under all four wheels. Calm empty wall area in the upper third. Photorealistic interior photography, no people, no text, no logos.

Elementy, które muszą zostać bez zmian: dwa drewniane szczyty, cztery drewniane barierki (po dwie na bok), jasnoszara rama, siłownik przy szczycie nóg, pilot na spiralnym kablu, cztery koła z hamulcami, biały materac płasko. Bez wysięgnika — nie ma go na tym zdjęciu.

## 4. Kontrola wyniku (przed pokazaniem właścicielowi)

Porównanie ze źródłem w 100%, element po elemencie: kształt i proporcje szczytów, liczba i układ barierek, rama i poprzeczki, siłownik i silnik, pilot i kabel, liczba kół i hamulce, materac. Dodatkowo: spójna perspektywa podłogi i ścian z kątem łóżka, cienie pod wszystkimi kołami, brak wygenerowanych liter, logotypów i osób.

- Odrzucenie przy jakiejkolwiek zmianie konstrukcji.
- Jeśli tylko produkt jest zniekształcony, a otoczenie dobre: wykorzystać otoczenie i nałożyć oryginalny wycięty produkt. Taki obraz jest oznaczany jako składany, a cienie kontaktowe sprawdzane osobno.
- Najpierw pokazujemy samą fotografię, bez tekstu.

## 5. Rozdzielczość

- Źródło: 1500×1500 px, łóżko w kadrze ok. 1334×978 px.
- Docelowo 2160×2700 px. Jeżeli finalny obraz zawiera oryginalne piksele produktu, łóżko może zająć najwyżej ok. 1330 px szerokości (ok. 62% kadru) bez powiększania. Większe łóżko wymagałoby powiększenia źródła, czego nie robimy i czego nie nazwiemy poprawą jakości.
- Jeśli generacja odtworzy produkt wiernie w 4K, ograniczenie dotyczy tylko jakości kontroli porównawczej, nie skali.
- Lepsze źródło: oryginał zdjęcia w wyższej rozdzielczości albo zdjęcie faktycznie wynajmowanego egzemplarza.

## 6. Reklama — dopiero po akceptacji fotografii

Tekst składany poza generatorem, osobno dla każdego regionu:

1. „Wynajem łóżek rehabilitacyjnych”, w drugiej linii region („Śląsk” albo „Kraków”). Bez półpauzy w nagłówku (zasada `ad-creative`).
2. „150 zł / miesiąc” (dotyczy 3F).
3. „Zadzwoń: 14 694 10 00”.

Bez obietnic dotyczących klikalności, wyników, dostępności, terminu i bezpłatnej dostawy. Bez publikacji i budżetu.
