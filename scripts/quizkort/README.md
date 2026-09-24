# Quiz og byt – kortgenerator

Én YAML-fil pr. quiz → webside (Hugo-shortcode `quizkort`) + print-PDF (2 × 4 kort pr. A4, svar på hovedet nederst).

| Fil | Rolle |
|---|---|
| `data/quiz/<navn>.yaml` | Kortene (kilde) |
| `static/img/quiz-<navn>/` | Grafer: `.svg` til web, `.pdf` til print |
| `layouts/shortcodes/quizkort.html` | Webvisning: filtre, Bland, hint/svar |
| `scripts/quizkort/build_pdf.py` | YAML → `static/pdfs/quiz-<navn>.pdf` (xelatex) |
| `scripts/quizkort/graphs_integration.py` | Eksempel på graf-script (matplotlib) |
| `scripts/quizkort/skabelon.yaml` | Start herfra |

## Ny quiz
1. `cp scripts/quizkort/skabelon.yaml data/quiz/<navn>.yaml` og skriv kortene.
2. Grafer (valgfrit): kopiér `graphs_integration.py`, ret funktionerne og `OUT`-mappen.
3. Side i `content/docs/...`:
   ```
   ---
   title: "Quiz og byt – <emne>"
   pdf: "pdfs/quiz-<navn>.pdf"
   pdf_ny_fane: true
   ---
   {{< quizkort "<navn>" >}}
   ```
4. `python3 scripts/quizkort/build_pdf.py <navn>` → `hugopush`.
