# Architektura systemu

## Warstwa sterująca

Codex Cloud czyta repozytorium, przygotowuje research, brief i pakiet kampanii. Reguły stałe są w `AGENTS.md`, a procedura kampanii w `.agents/skills/siloe-medical-rental-marketing/`.

## Warstwa danych

Źródłem prawdy są wersjonowane pliki w `config/`: fakty o marce, ceny, dostępność, dowody i ograniczenia. Wyniki reklam powinny wracać do repozytorium wyłącznie w formie zbiorczej, bez danych pozwalających rozpoznać stan zdrowia konkretnej osoby.

## Warstwa produkcji

Higgsfield tworzy obrazy i filmy na podstawie zatwierdzonego briefu oraz prawdziwych referencji. Remotion może później dodawać powtarzalne elementy: napisy, logo, ceny, zastrzeżenia, plansze końcowe oraz eksport 9:16, 4:5 i 1:1.

## Warstwa automatyzacji

n8n może obsługiwać statusy kampanii, zadania produkcyjne, wyniki i przekazywanie zaakceptowanych treści do Postiz lub oficjalnych narzędzi platform. Publikacja oraz wydatki mają bramkę zatwierdzenia.

## Pomiar

Każdy wariant dostaje identyfikator i UTM. Raport łączy koszt, kwalifikowane kontakty, rezerwacje i przychód. Polubienia i czas oglądania służą do diagnozy kreacji.

## Stany kampanii

`idea -> researched -> drafted -> compliance_review -> creative_ready -> approved -> scheduled -> live -> measured -> learned`
