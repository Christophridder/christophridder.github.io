---
title: "Prompts og cmd"
weight: 5
aliases: ["/docs/it/cr-ting/prompts/"]
---

Mine faste prompts til Claude, så nye sider på crsite bliver lavet på samme måde. Kopiér en prompt, udfyld felterne i `[KANTEDE PARENTESER]`, og slet de linjer, du ikke skal bruge.

**Et forløb består typisk af tre sider, der linker til hinanden:**

| Side | Filnavn | Indhold |
|---|---|---|
| Teori | `emne.md` | Teori + gennemregnede eksempler |
| Opgaver | `emne-opgaver.md` | Opgave 1, 2, 3 … → Hint 1, 2, 3 … → Løsning 1, 2, 3 … |
| Quiz og byt | `quiz-og-byt-emne.md` + `data/quiz/emne.yaml` | 24–32 kort til CL-øvelsen + print-PDF |

## Kommandoer (cmd)

Kør dem i terminalen fra crsite-roden (`cd ~/Nextcloud/crsite`).

### PDF'er

| Hvad | Kommando |
|---|---|
| **PDF med blå bjælke** fra en side | `python3 scripts/pdf/md2pdf.py content/docs/.../side.md` |
| Quizkort som PDF (2×4 pr. A4) | `python3 scripts/quizkort/build_pdf.py <navn>` |

- PDF'en lander i `static/` efter `pdf:` i front matter, ellers i `static/pdfs/<filnavn>.pdf`.
- Undertitlen i bjælken tages fra linjen `**Niveau: …** · **Emne: …**`.
- Kemiformler med `\ce{}` kræver mhchem i TeX. Installér én gang: `sudo tlmgr install mhchem`

### Åbn filer

| Hvad | Kommando |
|---|---|
| PDF i Skim (genindlæser selv) | `open -a Skim fil.pdf` |
| Tekstdokument i LibreOffice | `open -a LibreOffice fil.odt` |
| Præsentation i LibreOffice | `open -a LibreOffice fil.odp` |
| Start præsentation direkte som diasshow | `/Applications/LibreOffice.app/Contents/MacOS/soffice --show fil.odp` |
| Åbn med standardprogrammet | `open fil.pdf` |
| Filnavn med mellemrum | `open -a Skim "min fil.pdf"` |

### Hugo

| Hvad | Kommando |
|---|---|
| Lokal forhåndsvisning med kladder (localhost:1313) | `./hugoserver` |
| Udgiv til GitHub Pages (git add/commit/push) | `./hugopush` |

---

## Husregler (står i alle prompts)

De gælder for alle sider på crsite og står derfor også inde i hver prompt nedenfor.

- Dansk. Eleven tiltales med **du**. Korte sætninger.
- Første linje efter front matter: `**Niveau: [FAG NIVEAU]** · **Emne: [EMNE]**`
- Matematik i `$...$`, decimalkomma som `{,}`, enheder efter tallet, gange med `\cdot`. Kemi med `\ce{}`.
- Fagtraditioner: arbejde hedder $A$, henfaldskonstant $k$, $p$ er *bevægelsesmængde*, $\Delta p$ er *kraftens impuls*. Centrifugalkraft er en *skinkraft*.
- Fysik A: nævn altid modellens gyldighed (en `> **Model:**`-boks).
- Grafer: matplotlib → SVG i `static/img/`, tern-gitter og decimalkomma. Python: `np.trapezoid` (ikke `np.trapz`), SymPy kun i et appendiks.
- Links mellem sider med `{{</* relref "filnavn" */>}}`.
- Regn alle tal efter, før siden er færdig.

---

## Quiz og byt

Laver kort til CL-strukturen *Quiz og byt* (eksempel: [Quiz og byt – Integration]({{< relref "quiz-og-byt-integration" >}})).

```text
Jeg skal bruge kort til CL-øvelsen "Quiz og byt" på min Hugo-side crsite
(~/Nextcloud/crsite). Brug den eksisterende kortgenerator i scripts/quizkort/
(README.md og skabelon.yaml) – eller skill'en quiz-og-byt, hvis du har den.

Klasse og fag: [fx 3g Fysik A / 2w Kemi B]
Emne: [fx integration i fysik]
Byg på denne side: [fx content/docs/mat/integration-i-fysik.md]
Antal kort: [fx 30 – der er 8 kort pr. A4]
Kategorier (navn + ca. antal):
  - [fx Aflæs grafen – 10 kort med en graf, hvor et areal/integral skal aflæses]
  - [fx Begreber og enheder – 10 kort om grundbegreberne fra siden]
  - [fx Regn/integrér – 10 lette opgaver, fx 1/x, sin, cos, men ikke tan]
Særligt fokus: [fx gerne mange kort, hvor enheden skal findes – mærk dem "enhed"]

Sådan fungerer øvelsen: A stiller spørgsmålet, B svarer, A hjælper med hintet,
de bytter kort og finder en ny makker. Svaret står derfor på hovedet nederst på
forsiden – A må gerne se det og dækker det med tommelfingeren, når B skal se en graf.

Arbejdsgang:
1. Læs siden, og foreslå først spørgsmålene i en tabel pr. kategori. Vent på mit OK.
2. Skriv kortene i data/quiz/[navn].yaml: kort svar (højst 2-3 linjer), et hint der
   hjælper uden at give svaret, et par "fælder" (fortegn, enheder, negativt areal),
   og hellere "vis at …" end et for svært "find …".
3. Lav graferne med matplotlib (kopiér graphs_integration.py): tern-gitter,
   decimalkomma, gem både .svg (web) og .pdf (print) i static/img/quiz-[navn]/.
4. Lav print-PDF'en: python3 scripts/quizkort/build_pdf.py [navn]
5. Lav siden content/docs/[mappe]/quiz-og-byt-[navn].md med
   pdf: "pdfs/quiz-[navn].pdf", pdf_ny_fane: true, en kort intro (du-form),
   de 4 trin i quiz og byt, link til teorisiden og {{</* quizkort "[navn]" */>}}.
6. Regn alle svar efter (sympy/numpy), og se PDF-siderne igennem, før du melder færdig.

Husregler: dansk, du-form, $...$ til matematik, {,} som decimalkomma,
arbejde = A, kraftens impuls = Δp, bevægelsesmængde = p, centrifugalkraft er en skinkraft.
```

---

## Opgaveside (opgaver → hints → løsninger)

Laver en opgaveside ud fra en teoriside eller andet materiale (eksempel: [Integration-opgaver]({{< relref "integration-opgaver" >}})).

```text
Lav en opgaveside til min Hugo-side crsite (~/Nextcloud/crsite) i samme stil som
content/docs/mat/integration-opgaver.md – læs den først.

Klasse og fag: [fx 3g Fysik A]
Emne: [fx radioaktivt henfald]
Byg på: [sti til teoriside på crsite, en PDF, et link eller indsat tekst]
Filen skal hedde: content/docs/[mappe]/[emne]-opgaver.md
Antal opgaver: [fx 10] – [fx 6 lette, 3 middel, 1 svær (skriv "(lidt sværere)" i titlen)]
Gerne med: [fx 2 opgaver med graf hvor man tæller tern / 1 Python-opgave / hverdagseksempler]

Opbygning (præcis denne rækkefølge):
- Front matter: title, weight, pdf: "pdfs/[emne]-opgaver.pdf", pdf_ny_fane: true
- **Niveau: …** · **Emne: …**
- 2-3 linjer: hvilken teoriside opgaverne hører til (relref-link), "Forsøg først selv.
  Sidder du fast, så scroll ned til Hints, og til sidst til Løsninger." + evt. 2-3
  huskeregler i punktform.
- ## Opgaver  → ### Opgave 1 – [kort titel], ### Opgave 2 – …  (delspørgsmål a), b), c))
- ## Hints    → ### Hint 1, ### Hint 2, … (et hint pr. opgave, samme nummer; hintet
  peger på metoden eller første skridt – det giver ikke facit)
- ## Løsninger → ### Løsning 1, ### Løsning 2, … (fuld udregning med enheder hele vejen,
  facit med passende betydende cifre, og et tjek, fx med en trekant, en enhed eller en
  anden metode)

Krav:
- Opgaverne bygger på det, der står i materialet – brug samme metoder og notation.
- Tallene har enheder, så alt går op (fx 20 N/m · x).
- Fysik A: mindst én opgave spørger til modellens antagelser/gyldighed.
- Grafer: matplotlib → static/img/[emne]-opg[nr].svg, tern-gitter og decimalkomma.
- Regn ALLE facit efter med Python, før du melder færdig.
- Lav PDF'en til sidst: python3 scripts/pdf/md2pdf.py content/docs/[mappe]/[emne]-opgaver.md
- Tilføj et link til opgavesiden fra teorisiden (og omvendt).

Husregler: dansk, du-form, $...$ til matematik, {,} som decimalkomma, enhed efter tallet,
arbejde = A, henfaldskonstant = k, kraftens impuls = Δp, bevægelsesmængde = p,
centrifugalkraft er en skinkraft, np.trapezoid (ikke np.trapz).
```

---

## Teoriside

Laver en teoriside med gennemregnede eksempler (eksempel: [Integration i fysik]({{< relref "integration-i-fysik" >}})).

```text
Lav en teoriside til min Hugo-side crsite (~/Nextcloud/crsite) i samme stil som
content/docs/mat/integration-i-fysik.md – læs den først.

Klasse og fag: [fx 1g Fysik C / 3g Fysik A]
Emne: [fx bevægelsesmængde og stød]
Filen skal hedde: content/docs/[mappe]/[emne].md
Kilder / det, siden skal bygge på: [fx lærebogskapitel, noter, et link – eller "din viden"]
Eleverne kan i forvejen: [fx differentialregning, Newtons 2. lov]
Skal med: [fx 3 gennemregnede eksempler, et afsnit med Python og måledata, en opsummeringstabel]
Links til: opgavesiden [emne]-opgaver.md og quiz og byt-siden quiz-og-byt-[emne].md
(lav links nu, også selvom siderne ikke findes endnu – så siger du det bare til mig)

Opbygning:
- Front matter: title, weight, pdf: "pdfs/[emne].pdf", pdf_ny_fane: true
- **Niveau: …** · **Emne: …**
- 1-2 sætninger: hvad du lærer på siden.
- ## 1. [Grundidé] … ## 2. … – nummererede teoriafsnit. Hver ny formel forklares med ord
  (hvad betyder hvert symbol, og hvilken enhed har det).
- ## Eksempel 1 – [titel], ## Eksempel 2 – … : gennemregnede eksempler med
  opstilling → udregning med enheder → facit → tjek. Gerne en figur (SVG) pr. eksempel.
- > **Model:** … – en boks, hvor modellen har antagelser (Fysik A-krav).
- ## Opsummering – en tabel + 3-4 punkter med det vigtigste.
- Nederst en linje med links: Opgaver: [..](relref) · Quiz og byt: [..](relref)

Krav:
- Start konkret (et hverdagseksempel), og generalisér bagefter.
- Kort og præcist: korte sætninger, punktform frem for lange afsnit, tabeller hvor det
  giver overblik.
- Figurer: matplotlib → static/img/[emne]-[nr].svg (lys baggrund, tern-gitter, decimalkomma,
  alt-tekst der forklarer figuren).
- Regn alle tal efter med Python, før du melder færdig.
- Lav PDF'en til sidst: python3 scripts/pdf/md2pdf.py content/docs/[mappe]/[emne].md
- Foreslå til sidst 3-5 idéer til opgaver og quizkort, der passer til siden.

Husregler: dansk, du-form, $...$ til matematik, {,} som decimalkomma, enhed efter tallet,
arbejde = A, henfaldskonstant = k, kraftens impuls = Δp, bevægelsesmængde = p,
centrifugalkraft er en skinkraft, np.trapezoid (ikke np.trapz), SymPy kun i et appendiks.
```
