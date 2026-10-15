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
