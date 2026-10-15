# Prompty Higgsfield — łóżko 3F, Meta, 2026-10

Projekt roboczy: **`Siloe | Łóżko 3F | Meta | 2026-10`** (project_id `405c9e29-298e-4226-a0b4-5d8c84e5527d`, workspace `30970aa5-4f16-4cac-97aa-4baa4a0cd2fd`).

## A. Wywołania w tej rundzie (2026-10-15)

| # | Narzędzie / model | Wejście | Parametry | Prompt | Wynik | Koszt |
|---|---|---|---|---|---|---|
| 1 | `outpaint_image` (model `outpaint`) | job `36c754cd-…` (zaakceptowane zdjęcie S4) | `aspect_ratio: "9:16"` | brak (narzędzie nie przyjmuje promptu) | job `04f94f57-2a17-4886-b777-f8156ec3659b`, 1536 × 2752 | 2 kr. |
| 2 | `outpaint_image` (model `outpaint`) | job `36c754cd-…` | `aspect_ratio: "1:1"` | brak | job `5a25dc6a-97fb-4227-bcca-0116363f9f75`, 2048 × 2048 | 2 kr. |
| — | `generate_video` `kling3_0` | job `36c754cd-…` jako `start_image` | `duration: 5`, `aspect_ratio: "9:16"`, `get_cost: true` | „slow camera push-in” (tylko wycena) | **nie uruchomiono** — 10 kr. przekracza pulę | 0 |
| — | `outpaint_image` | job `36c754cd-…` | `get_cost: true` | — | wycena 2 kr. | 0 |

Rozszerzenia kadru dostarczają **tylko ścianę i podłogę**. Środek kadru jest nadpisywany oryginalnymi pikselami S4 (`creative/src/layout.py`, funkcja `base_from_outpaint`). Uzasadnienie: surowy outpaint przerysował łóżko (średnia różnica ok. 10/255).

Filmy, okładka i grafiki statyczne nie są generowane przez model. To motion graphic złożony programowo z zaakceptowanego zdjęcia. Ruch tworzą wyłącznie najazd kamery i zbliżenie na pilot. Etykiety, lista usług, cena i CTA są animowane, a segmenty łóżka się nie poruszają. Gotowe pliki wgrano do magazynu mediów Higgsfield (`manifest.md`).

## B. Prompty, z których powstał zaakceptowany materiał (2026-10-14/15, zapis dla ciągłości)

### B1. Zdjęcie S3 — `nano_banana_pro`, 4:5, 2K, referencja `748bc326-…` (`image_references`) → job `83dbb6e9-8d92-4f07-bcd6-4123ba3f1c8b`

> Clean, bright and cosy product-in-home photograph for a home-care bed advert, minimal styling so the bed is the clear hero. HERO PRODUCT: the electric care bed from the reference image with its exact construction: beech-wood head and foot boards with darker beech edge posts, two beech-wood side rails on each side, beech-coloured legs and frame, grey hand remote on a coiled cable hanging on the near side rail, light grey lifting pole with a white triangle handle at the head end, four castor wheels with brakes. Now the bed has a thick white foam mattress with smooth white bedding, one white pillow and a light-blue cushion, a light-grey knitted throw at the foot. The backrest is slightly raised (about 25 degrees), the leg section is flat. A slim wooden over-bed table on a grey metal base stands beside the bed with a glass of water and a small plant. SCENE: soft warm-beige studio-like room corner with a smooth plaster wall, light oak floor, gentle diffused window light from the right, a soft shadow pattern of window frames on the wall. COMPOSITION 4:5: same 3/4 camera angle as the reference, the whole bed fully visible and large, about 88% of the width, centred in the lower 60% of the frame; upper 32% is calm empty wall for text; bottom 8% clean floor. Correct perspective, realistic contact shadows, no people, no text, no logos, no medical devices.

### B2. Zdjęcie S4 (zaakceptowane tło) — `nano_banana_pro`, 4:5, 2K, referencje: job `83dbb6e9-…` + media `748bc326-…` → job `36c754cd-7267-4f6f-b71b-bc946d2d9ea8`

> Edit the first image. Keep the care bed EXACTLY as it is in the first image: same position, size, camera angle, mattress, raised backrest, lifting pole at the head end, side rails, remote, wheels; its wooden frame construction matches the second image. Keep the over-bed table where it is, but put a cup of tea on a saucer and an open book on it. Change only the room and styling into a warm, cosy family home: warm cream walls with soft golden late-afternoon sunlight from a window on the right casting gentle window-shaped light on the wall, a small beech bedside table with a ceramic lamp (switched on, warm glow) and a green plant behind the head end of the bed, a soft beige wool rug under the bed, a pair of navy slippers on the rug by the bed, the bedding stays white with a navy-blue cushion instead of the light-blue one and a mustard-yellow knitted throw at the foot instead of the grey one. Keep the upper third of the image a calm plain wall for text. Single bed only. No people, no text, no logos, no photos on the wall, no medical devices.

### B3. Zaakceptowany układ z napisami — `nano_banana_pro`, 4:5, 2K, referencja: job `214de439-…` → job `b5431c60-fa3b-4764-8ff3-d1e9f41ef72c`

> Edit this advert. Keep the photo, the room, the care bed, the blue round '150 zł miesięcznie' sticker, the white callout label 'Materac w zestawie', the navy bottom-left panel and the empty white rounded box in the bottom-right corner exactly in place. Remove the 'Elektryczna regulacja' callout. Change the typography to a friendly, rounded, modern sans-serif like Poppins (Bold for headlines, Medium for small text), very legible for older readers, with perfect Polish diacritics. Replace the top headline with exactly two lines, left-aligned: navy (#14284B) "Jeden telefon." and below in bright blue (#009DE4) "Łóżko gotowe w 48 godzin". Under it, left-aligned, a smaller navy line exactly: "Od telefonu do Twoich drzwi". On the left side, at the height of the bed headboard, a neat vertical list of four small white rounded tags with a small blue check-mark icon each, exactly: "Dowozimy", "Wnosimy", "Montujemy", "Szkolimy". In the navy bottom-left panel replace the texts with: small white line exactly "Wszystko załatwisz jednym telefonem" and below it very large white "14 694 10 00", and under the number a small bright blue line exactly "Odbieramy 7 dni w tygodniu". Do not write any city name. Do not draw any logo; keep the bottom-right white box empty. No other text.

Logo Siloe na grafice bazowej to oryginalny plik właściciela nałożony programowo, a nie wynik generatora.
