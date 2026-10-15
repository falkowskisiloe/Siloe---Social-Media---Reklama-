# Higgsfield — runda 6: dwa warianty tekstowe projektu B

- Data: 2026-10-15. Status: propozycje do oceny, nic nie opublikowano.
- Polecenie właściciela: zostaje projekt B (`214de439-…`); zmienić tylko krój pisma i teksty, bez nazwy miasta. Teksty od właściciela: „Wszystko załatwisz jednym telefonem”, „48 godzin — od telefonu do Twoich drzwi”, „DOWOZIMY • WNOSIMY • MONTUJEMY • SZKOLIMY”, „Zadzwoń teraz — odbieramy 7 dni w tygodniu!”.
- Kredyty: ok. **36,75 / 50** (runda 6: 4 × 2).

| Wariant | Job ID | Krój | Teksty |
| --- | --- | --- | --- |
| **1 — „Wygodne łóżko w domu w 48 godzin”** | `c40a0296-9cd6-48e2-bc7f-0af88e48ba09` | w stylu Montserrat | nagłówek wyśrodkowany; „Wszystko załatwisz jednym telefonem”; wstęga z czterema usługami; etykiety „Materac w zestawie” i „Elektryczna regulacja”; panel „Zadzwoń teraz — odbieramy 7 dni w tygodniu!” + 14 694 10 00 |
| **2 — „Jeden telefon. Łóżko gotowe w 48 godzin”** | `b5431c60-fa3b-4764-8ff3-d1e9f41ef72c` | w stylu Poppins | „Od telefonu do Twoich drzwi”; lista ✓ Dowozimy / Wnosimy / Montujemy / Szkolimy; etykieta „Materac w zestawie”; panel „Wszystko załatwisz jednym telefonem” + 14 694 10 00 + „Odbieramy 7 dni w tygodniu” |
| Odrzucony duplikat wariantu 2 | `faf0a67f-5fbb-4c5f-b3f9-6e1ba272dc09` | — | gorszy podział nagłówka |
| Duplikat wariantu 1 | `e3983374-6adc-4706-8294-f13e136a5bfd` | — | niewykorzystany |

Polskie znaki są poprawne w obu wybranych wariantach. Logo Siloe jest oryginalnym plikiem wstawionym w biały narożnik.

## Nowe twierdzenia do zapisania jako fakty

„48 godzin”, „odbieramy 7 dni w tygodniu” oraz „dowozimy, wnosimy, montujemy, szkolimy” pochodzą od właściciela (2026-10-15). Nie ma ich w `config/offers.yaml`. Przed emisją trzeba potwierdzić:

- czy 48 godzin dotyczy całego obszaru (Śląsk i Kraków) i dni wolnych;
- godziny odbierania telefonu;
- czy transport, wniesienie i montaż mieszczą się w 150 zł / miesiąc (B16). Zestawienie usług z ceną będzie odczytane jako „w cenie”.
