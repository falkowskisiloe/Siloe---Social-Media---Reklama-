# Lista zatwierdzeń przed emisją — łóżko 3-funkcyjne

**Status grafiki:** zaakceptowana wizualnie przez właściciela.  
**Status emisji:** zablokowana do potwierdzenia danych poniżej.

| Element | Wartość robocza | Status | Odpowiedź właściciela |
|---|---|---|---|
| Cena | 150 zł | potwierdzić okres rozliczeniowy | |
| Okres ceny | „miesięcznie” | niepotwierdzony w konfiguracji | |
| Numer na grafice | 14 694 10 00 | różni się od numeru w konfiguracji | |
| Numer w konfiguracji i na stronie | 792 020 020 | potwierdzić numer reklamowy | |
| Czas realizacji | 48 godzin | potwierdzić obszar i weekendy | |
| Dostępność telefonu | 7 dni w tygodniu | potwierdzić godziny | |
| Obszar dostawy | brak zatwierdzonej listy | uzupełnić miasta/powiaty | |
| Dostawa | dostępna | potwierdzić, czy w cenie 150 zł | |
| Wniesienie | widoczne na grafice | potwierdzić zakres i cenę | |
| Montaż | dostępny | potwierdzić, czy w cenie 150 zł | |
| Instruktaż | dostępny | potwierdzić, czy w cenie 150 zł | |
| Materac | w zestawie | potwierdzone na karcie produktu | |
| Regulacje | oparcie, nogi, wysokość | potwierdzone na karcie produktu | |

## Zasada

Agent może przygotowywać projekty robocze z wartościami widocznymi na zaakceptowanej grafice, lecz nie może oznaczyć pakietu jako gotowego do emisji, dopóki wszystkie pola blokujące nie zostaną zatwierdzone.

Po uzyskaniu odpowiedzi należy zaktualizować `config/brand-brief.yaml` i `config/offers.yaml`, a następnie ponownie uruchomić kontrolę QA.

## Uzupełnienie po produkcji roboczej (2026-10-15)

**Status pakietu:** `creative_ready` — materiały w `manifest.md`, raport w `qa/qa-report.md`. Emisja nadal zablokowana.

| Element | Wartość robocza | Status | Odpowiedź właściciela |
|---|---|---|---|
| Wybór wersji do testu | H1 i H2 (H3 zablokowany) | do akceptacji | |
| Prawa do zdjęcia produktu (`2.png` → S4) | brak dokumentu | potwierdzić prawa do użycia w reklamie płatnej | |
| Wysięgnik z uchwytem na zdjęciu | widoczny | potwierdzić, czy jest w zestawie najmu, albo zdecydować o pozostawieniu | |
| H3 „48 godzin” | szkic | odblokować dopiero po potwierdzeniu obszaru, dostępności i weekendów | |
| Muzyka | podkład autorski Siloe (generowany skryptem) | zaakceptować albo wybrać utwór z Meta Sound Collection | |
| Znaczniki „PROJEKT ROBOCZY” na plikach | widoczne | usunąć w wersji do emisji po zatwierdzeniu danych | |
| Zgoda na emisję i budżet | brak | wymagana osobna, jawna decyzja | |

## Decyzje właściciela — zadanie 003 (2026-10-15)

| Element | Decyzja | Źródło |
|---|---|---|
| Kierunek H1 i H2 | zaakceptowany; czyste pliki oznaczone `publication_ready` | polecenie właściciela 2026-10-15 |
| Cena na kreacjach | „150 zł miesięcznie” — zachować | polecenie właściciela 2026-10-15 |
| Numer na kreacjach | 14 694 10 00 — zachować | polecenie właściciela 2026-10-15 |
| H3 „48 godzin” | `withheld` — poza pakietem emisji do potwierdzenia obszaru, dostępności i weekendów | zadanie 003 |
| Napisy techniczne na obrazie i w filmie | zakazane; statusy tylko w manifeście, checkliście i QA (`AGENTS.md`) | zadanie 003 |

## Warunki, które nadal wymagają decyzji przed uruchomieniem emisji

`publication_ready` oznacza czyste, technicznie gotowe pliki. Nie jest to zgoda na emisję.

| Element | Status |
|---|---|
| Zgoda na emisję, budżet i harmonogram | brak — wymagana osobna, jawna decyzja |
| Czy dostawa, wniesienie, montaż i instruktaż mieszczą się w 150 zł / miesiąc | niepotwierdzone. Teksty nie piszą „w cenie”, ale lista usług w H1 stoi obok ceny |
| Lista miast i powiatów dostawy (kierowanie geograficzne) | niepotwierdzona |
| Prawa do zdjęcia produktu w reklamie płatnej (B15) | niepotwierdzone |
| Wysięgnik z uchwytem widoczny na zdjęciu | decyzja właściciela |
| Aktualizacja `config/offers.yaml` i `config/brand-brief.yaml` (okres ceny, numer reklamowy) | do wykonania po potwierdzeniu właściciela na piśmie |
