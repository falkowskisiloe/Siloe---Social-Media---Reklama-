# Brief kampanii — łóżko rehabilitacyjne elektryczne 3-funkcyjne (Meta, 2026-10)

Aktualny wykaz eksportów i stan materiałów: [manifest.md](manifest.md). Emisji nie uruchomiono.
**Zadania:** 002 (produkcja bazowa) i 003 (czyste eksporty z zaakceptowanego kierunku).
**Data przygotowania:** 2026-10-15
**Poza zakresem tej rundy:** TWIST i karuzela produktowa.

## Jeden cel i pomiar

| Element | Ustalenie |
|---|---|
| Cel | Kwalifikowane połączenia telefoniczne w sprawie wynajmu łóżka 3-funkcyjnego |
| Główny wskaźnik | Koszt odebranego, wartościowego zapytania telefonicznego (koszt kwalifikowanego połączenia) |
| Wskaźniki pomocnicze | Kliknięcia „Zadzwoń”, CTR, odsetek odebranych połączeń |
| Kwalifikacja połączenia | Rozmowa odebrana i dotycząca wynajmu łóżka 3F w obsługiwanym obszarze. Definicję zatwierdza właściciel |
| Zamiennik pomiaru | Jeśli połączeń nie da się wiarygodnie mierzyć, właściciel wybiera **jeden** zamiennik: formularz albo Messenger |

## Jedna oferta

Wynajem łóżka rehabilitacyjnego elektrycznego 3-funkcyjnego (`config/offers.yaml` → `bed-electric-3-function-rental`). Elementy oferty: materac w zestawie, dostawa, montaż, instruktaż i wsparcie serwisowe w trakcie najmu.

## Obszar i odbiorcy

- **Obszar:** województwo śląskie oraz osobno Kraków (miasto). Tak wynika z potwierdzenia właściciela w kampanii 2026-10-lozka-rehabilitacyjne (facts F10, F13). Lista miast i powiatów oraz koszt dojazdu są **DO POTWIERDZENIA**. Kierowanie geograficzne ustawiamy dopiero na zatwierdzonej liście.
- **Odbiorcy:** dorośli organizujący opiekę domową bliskiej osoby, opiekunowie rodzinni oraz osoby przygotowujące dom na powrót bliskiego. Język neutralny, bez sugerowania diagnozy.

## Materiał bazowy

Zaakceptowana przez właściciela grafika „Jeden telefon. / Łóżko gotowe w 48 godzin” (1080 × 1350). Właściciel przekazał ją w rozmowie 2026-10-15 jako bazę do dalszej pracy. Grafiki **nie ma w repozytorium**: repozytorium jest publiczne, a prawa do zdjęcia produktu są niepotwierdzone (B17). Jej źródła w Higgsfield:

| Warstwa | Higgsfield ID |
|---|---|
| Zdjęcie łóżka i pokoju bez napisów (S4) | job `36c754cd-7267-4f6f-b71b-bc946d2d9ea8` |
| Zaakceptowany układ z napisami (bez logo) | job `b5431c60-fa3b-4764-8ff3-d1e9f41ef72c` |
| Produkt źródłowy (zdjęcie od właściciela) | media `748bc326-d1e2-4c9c-bfe9-eef1f98bff5a` |

We wszystkich formatach łóżko pochodzi z pikseli S4 (kontrola w `qa/qa-report.md`). Układ, kolory, naklejka, lista ✓, etykiety, panel i logo odtworzone są w programie składu (`creative/src/`). Teksty są wpisane czcionką, a nie generowane.

## Trzy hipotezy (ta sama oferta, obszar, cel i pomiar)

| ID | Hak | Dowód | CTA | Status |
|---|---|---|---|---|
| H1 | „Jeden telefon — my zajmiemy się resztą.” | dowozimy, wnosimy, montujemy, szkolimy; materac w zestawie | „Zadzwoń i sprawdź dostępność” | kierunek zaakceptowany przez właściciela |
| H2 | „Trzy regulacje, które pomagają dopasować łóżko do codziennej opieki.” | elektryczna regulacja oparcia, segmentu nóg i wysokości | „Zapytaj o wynajem łóżka 3-funkcyjnego” | kierunek zaakceptowany przez właściciela |
| H3 | „Łóżko gotowe w domu w 48 godzin.” | czas realizacji | „Zadzwoń i potwierdź termin” | **ZABLOKOWANY** — do czasu potwierdzenia 48 h, obszaru, dostępności i realizacji weekendowej |

Teksty: `copy/meta-copy-h1.md`, `copy/meta-copy-h2.md`, `copy/meta-copy-h3.md`.

## Plan testu (propozycja, nic nie uruchomiono)

1. Jedna kampania, cel „Połączenia” (lub zatwierdzony zamiennik), jeden zestaw reklam na obszar.
2. W zestawie reklamy H1 i H2, każda z obrazem 4:5, 1:1 i 9:16 oraz filmem 15 s. H3 dołączamy dopiero po odblokowaniu.
3. Ten sam budżet, harmonogram i odbiorcy dla każdej hipotezy. Ocena po osiągnięciu progu połączeń zatwierdzonego przez właściciela.
4. UTM dla kliknięć w link (jeśli będą): `utm_source=facebook&utm_medium=paid_social&utm_campaign=3f_meta_2026_10&utm_content=<h1|h2|h3>_<format>`. Połączenia rejestrujemy w Meta oraz w rejestrze rozmów Siloe.

## Fakty i źródła (kontrola danych — agent 1)

| Fakt | Wartość | Źródło | Data sprawdzenia | Status |
|---|---|---|---|---|
| Produkt | łóżko rehabilitacyjne elektryczne 3-funkcyjne | `config/offers.yaml` | 2026-10-15 | potwierdzony |
| Regulacje | oparcie, segment nóg, wysokość | `config/offers.yaml` (karta produktu 2026-10-14) | 2026-10-15 | potwierdzony |
| Materac w zestawie | tak | `config/offers.yaml` | 2026-10-15 | potwierdzony |
| Dostawa, montaż, instruktaż, wsparcie | w zakresie usługi | `config/offers.yaml` | 2026-10-15 | potwierdzony zakres; **czy w cenie — DO POTWIERDZENIA** |
| Wniesienie | widoczne na zaakceptowanej grafice | potwierdzenie właściciela (facts F11, 2026-10-14); brak w `offers.yaml` | 2026-10-15 | DO POTWIERDZENIA w konfiguracji |
| Cena | 150 zł | `offers.yaml` (`displayed_amount_pln: 150`) | 2026-10-15 | kwota potwierdzona |
| Okres ceny | „miesięcznie” | potwierdzenie właściciela F09 (2026-10-14); w `offers.yaml`: „DO POTWIERDZENIA” | 2026-10-15 | potwierdzone przez właściciela w rozmowie 2026-10-14 i ponownie w Zadaniu 003 |
| Numer reklamowy | 14 694 10 00 (numer tej kampanii) | grafika i F01 kontra `config/brand-brief.yaml` | 2026-10-15 | potwierdzony przez właściciela; globalny numer firmy bez zmian |
| Realizacja w 48 h | robocze | tekst właściciela 2026-10-15 | 2026-10-15 | **DO POTWIERDZENIA** (blokuje H3) |
| Odbieramy 7 dni w tygodniu | robocze | tekst właściciela 2026-10-15 | 2026-10-15 | **DO POTWIERDZENIA** (godziny) |
| Obszar dostawy | Śląsk i Kraków (kampania) | F10, F13 | 2026-10-15 | **lista miast i koszt DO POTWIERDZENIA** |
| Prawa do zdjęcia produktu | — | brak | 2026-10-15 | **DO POTWIERDZENIA** (B15) |
| Wysięgnik z uchwytem | widoczny na zdjęciu | brak w liście wyposażenia oferty | 2026-10-15 | **DO DECYZJI** |

## Decyzja właściciela

- Akceptacja kierunku H1/H2: właściciel, polecenie Zadania 003, 2026-10-15.
- Numer kampanii: 14 694 10 00 — potwierdzony przez właściciela.
- Cena najmu: 150 zł miesięcznie — potwierdzona. Usługi dodatkowe nie są określone jako bezpłatne.
- Zgoda na emisję i budżet: ____ (wymagana osobna, jawna decyzja)
