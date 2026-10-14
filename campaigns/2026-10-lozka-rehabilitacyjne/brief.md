# Zadanie 001 — pakiet do oceny właściciela

- Status: `creative_ready` — gotowe koncepcje, teksty i instrukcje produkcji; nie oznacza gotowych plików zdjęć/wideo ani zgody na emisję.
- Wersja: 1.2, 2026-10-14 (szkice 3F i potwierdzenia właściciela — [ad-proposal-3f.md](ad-proposal-3f.md)). Autor opracowania: Codex. Baza repozytorium: `52e24eddff1b0f3917c4855885f1bca48c4c7a24`.
- Zadanie: [001](../../tasks/001-lozka-rehabilitacyjne-start.md); kontrakt: [campaign-package-contract](../../tools/campaign-package-contract.md).
- Decyzja właściciela: OCZEKUJE. Publikacja: NIEZATWIERDZONA. Budżet: NIEZATWIERDZONY. Harmonogram: nie utworzono.

## Dwie osobne kampanie ofertowe

| Pole | 3F | TWIST |
| --- | --- | --- |
| ID | 2026-10_beds_3f_lead | 2026-10_beds_twist_lead |
| Jedna oferta | Wynajem elektrycznego łóżka 3F | Zapytanie o wynajem łóżka obrotowego z funkcją fotela |
| Sytuacja | Organizacja codziennej opieki w domu | Dobór łóżka z obrotem leża do siedzenia bokiem |
| Główna myśl | Trzy regulacje i pomoc w uruchomieniu sprzętu | Rzeczywisty obrót do fotela i dobór strony do pokoju |
| Dowód | Prawdziwe ujęcia regulacji oraz montażu/instruktażu | Prawdziwy ciągły ruch konkretnego egzemplarza |
| Główny CTA | Zadzwoń: 14 694 10 00 | Zadzwoń: 14 694 10 00 |

Statusy w config/offers.yaml bez zmian: 3F `ready_after_price_period_confirmation`, TWIST `blocked_until_variant_and_price_confirmation`.

Jeden wspólny mierzalny cel biznesowy: kwalifikowane kontakty telefoniczne o wynajem właściwego produktu. Miernik główny: liczba takich kontaktów; w płatnym teście koszt kwalifikowanego kontaktu (CPQL). Kwalifikacja oznacza zapytanie o 3F/TWIST, termin i miejscowość w zatwierdzonym obszarze oraz chęć poznania oferty. Bez diagnozy i bez danych zdrowotnych w raporcie. Rezerwacje i przychód to wynik dalszej obsługi; kliknięcie telefonu nie jest kontaktem.

Odbiorca podstawowy: dorośli organizujący opiekę domową, bliscy i opiekunowie rodzinni. Osobny język B2B dla placówek i profesjonalnych opiekunów w copy.md; nie mieszać go w pierwszym teście rodzinnym.

Aktualizacja 2026-10-14 (bezpośrednie potwierdzenie właściciela): priorytet to wynajem 3F, obszar kampanii — **województwo śląskie**, telefon kampanii 14 694 10 00, cena 3F „Wynajem 150 zł / miesiąc” (nie dotyczy TWIST). Cena transportu niepotwierdzona. Miasta i koszt dojazdu w Śląskiem nadal otwarte.

Obszar (stan wcześniejszy): Polska jako rynek i język; faktyczne miasta/powiaty dostawy obu modeli NIEPOTWIERDZONE. Nie uruchamiać targetowania ogólnopolskiego ani nie przyjmować historycznej listy miast jako potwierdzenia. Właściciel podaje obszar dla każdego modelu, koszty i ograniczenia dojazdu; dopiero wtedy powstają osobne wersje regionalne. Gotowy szablon lokalizacji: „Wynajem łóżka [MODEL] — [POTWIERDZONY OBSZAR]”; żadnego placeholdera nie eksportować do emisji.

## Rekomendowany kierunek do zatwierdzenia

3F: H1 — trzy regulacje pokazane osobno. TWIST: H1 — rzeczywisty obrót do fotela, pod warunkiem dostarczenia pełnego nagrania. To hipoteza sprzedażowa oparta na czytelności funkcji, a nie udowodniony zwycięzca. H2 wyjaśnia proces, H3 odpowiada na obawę; plan porównania w paid-ads.md.

Kreacje głównie 9:16; feed i karuzele 4:5, dodatkowo 1:1. Biel, granat i naturalne światło jako propozycja stylistyczna; brak zatwierdzonych kodów kolorów, fontów i logo. Realny pracownik w zwykłym stroju, bez sugerowania uprawnień medycznych. Zosia nie jest wymagana w Zadaniu 001 i brak jej referencji — nie generować postaci na podstawie pamięci.

## Granice faktów i produkcji

Źródłem treści handlowych są rekordy config/offers.yaml. Strony produktu sprawdzono pomocniczo przez przeglądarkę wyszukiwarki 2026-10-14; odczyt może być indeksowany, nie potwierdza stanu magazynu. Nie obiecywać czasu dostawy, ceny, darmowego transportu, refundacji, wyniku medycznego ani samodzielnego transferu. 3F: dostawa, montaż, instruktaż, wsparcie oraz materac są opisanym zakresem usługi, nie obietnicą ceny „wszystko gratis”. Nie przenosić automatycznie tego pakietu na TWIST.

Brak realnych plików w assets/products/. Całość to pakiet przedprodukcyjny zgodnie z warunkiem zatrzymania zadania. Produkcja finalnych wizualizacji oraz publikacja pozostają zablokowane; dopuszczona jest ocena koncepcji i tekstów. Lista decyzji w review.md. Nie zmieniono config ani nie oznaczono ofert jako zatwierdzonych.

## Nawigacja

[propozycja reklamy 3F + szkice](ad-proposal-3f.md) · [facts](facts.md) · [asset-manifest](asset-manifest.md) · [creative-concepts](creative-concepts.md) · [shorts](shorts.md) · [images](images.md) · [copy](copy.md) · [paid-ads](paid-ads.md) · [review](review.md) · [results](results.md) · [rejestr UTM](utm-register.csv)
