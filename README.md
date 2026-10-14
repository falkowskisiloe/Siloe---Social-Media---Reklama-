# Siloe Marketing OS

Repozytorium sterujące tworzeniem, zatwierdzaniem i oceną treści marketingowych dla wypożyczalni medycznej. Codex Cloud korzysta z danych marki i ofert zapisanych w tym repozytorium, przygotowuje warianty kampanii dla Facebooka, Instagrama i TikToka oraz zleca produkcję materiałów w Higgsfield.

## Jak zacząć

1. Przeczytaj `AGENTS.md`.
2. Użyj umiejętności `.agents/skills/siloe-medical-rental-marketing/`.
3. Otwórz aktywne zadanie `tasks/001-lozka-rehabilitacyjne-start.md`.
4. Korzystaj z potwierdzonych faktów w `config/offers.yaml`.
5. Przygotuj pakiet kampanii zgodnie z `tools/campaign-package-contract.md`.
6. Zatrzymaj się na etapie `creative_ready` i przedstaw materiały do zatwierdzenia.

## Pierwsza kampania

Dwa produkty:

- elektryczne łóżko rehabilitacyjne 3-funkcyjne;
- łóżko obrotowe TWIST z funkcją fotela.

Celem jest stworzenie shortów, zdjęć, karuzel, Stories, tekstów organicznych i wariantów płatnych reklam na Facebook, Instagram i TikTok.

## Architektura

- **Codex Cloud** — research, briefy, warianty, kontrola faktów i raporty.
- **Higgsfield** — obrazy i pionowe filmy na podstawie prawdziwych referencji produktu.
- **n8n** — przyszła automatyzacja przepływu danych i cyklicznych zadań.
- **Postiz** — przyszły kalendarz i publikacja organiczna po zatwierdzeniu.
- **Plausible lub Matomo** — pomiar ruchu i kampanii.
- **Remotion** — opcjonalny skład napisów, formatów i plansz końcowych.

Publikacja, wysyłka wiadomości i uruchomienie budżetu reklamowego wymagają zgody człowieka.

## Ważne blokery

Przed publikacją trzeba potwierdzić:

- okres, którego dotyczą ceny 150 zł i 500 zł;
- bieżącą dostępność;
- obszar oraz koszt dostawy;
- czy wynajmowany TWIST jest wariantem z pionizacją;
- prawa do zdjęć oraz nagrania pełnego ruchu TWIST.

Nie zapisuj w repozytorium danych osobowych leadów ani danych o ich zdrowiu.
