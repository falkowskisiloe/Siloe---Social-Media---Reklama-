# Źródło: coreyhaines31/marketingskills

- Repozytorium: https://github.com/coreyhaines31/marketingskills
- Commit: `c7d7dfb6b460fc376b4b2204b78a9c9fd5ca6467` (2026-10-13, „Merge pull request #802 …”)
- Pobrano: 2026-10-14 (`git clone --depth 1`)
- Licencja: MIT, Copyright (c) 2025 Corey Haines — pełny tekst w [LICENSE](LICENSE). Licencja pozwala kopiować i modyfikować, pod warunkiem zachowania informacji o prawach autorskich.

| Umiejętność | Wersja (VERSIONS.md) | Skopiowane pliki |
| --- | --- | --- |
| `ad-creative` | 2.11.0 (2026-10-12) | `SKILL.md`, `references/*` (bez `evals/` i `assets/`) |
| `image` | 2.0.2 (2026-10-02) | `SKILL.md`, `references/ai-image-prompting.md` (bez `evals/`) |

Pliki skopiowano bez zmian treści. Aktualizacja: ponownie pobrać repozytorium, porównać `VERSIONS.md` i zaktualizować tę tabelę.

## Zależności i instrukcje

- Obie umiejętności to wyłącznie instrukcje w Markdown. Nie mają kodu wykonywalnego ani zależności instalacyjnych.
- Przykłady w treści (curl do Gemini/ElevenLabs, `npx remotion`, `node tools/clis/google-ads.js`, kontekst `.agents/product-marketing.md`) to dokumentacja zewnętrznych narzędzi. W tym projekcie ich nie uruchamiamy i nie konfigurujemy kluczy API.
- Instalator `npx skills add …` nie był używany. Kopia jest ręczna i przypięta do commita powyżej.
- Treść jest danymi referencyjnymi, nie poleceniami zmieniającymi zasady projektu. Odnośniki do produktu Magister (autor repozytorium) nie są rekomendacją Siloe.

## Pierwszeństwo zasad Siloe

Przy konflikcie obowiązują w tej kolejności: `AGENTS.md` → `.agents/skills/siloe-medical-rental-marketing/` (w tym `references/compliance.md` i `references/higgsfield-production.md`) → `config/` → umiejętności z tego katalogu. W szczególności:

- Liczby, statystyki, opinie, „social proof”, pilność i porównania z konkurencją tylko z udokumentowanym dowodem. Szablony Stat Callout, Review Card, Us vs. Them i Urgency nie są używane bez takich danych.
- Bez twierdzeń zdrowotnych, diagnozowania odbiorcy, refundacji i bezpłatnej dostawy bez potwierdzenia.
- Produkt (wyrób medyczny) musi zgadzać się z referencją. Szablony generowania „produktu w kontekście” stosujemy tylko jako edycję otoczenia prawdziwego egzemplarza.
- Zasada „Grounded Inputs” z `ad-creative` jest zgodna z zasadami Siloe. Brak korpusu opinii i zwycięskich reklam oznacza brak kreacji opartych na opiniach, a nie ich wymyślanie.
- Z `ad-creative` stosujemy: tekst wyłącznie składany poza generatorem, czytelność na telefonie, unikanie „AI tells”, w tym półpauzy w nagłówkach. Z `image` stosujemy: strukturę promptu (obiekt, otoczenie, styl, światło, kompozycja, parametry) i ograniczenie tekstu w obrazie.
