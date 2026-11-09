---
title: "Fysikaflevering"
weight: -9
---

**Skriv din fysikaflevering med formler – og aflever den som PDF i Lectio.**

<p><a href="/fysikaflevering.html" target="_blank" style="display:inline-block;background:#1f5fa8;color:#fff;padding:.6rem 1.2rem;border-radius:6px;text-decoration:none;font-weight:600">✎ Åbn Fysikaflevering</a></p>

Editoren kører helt i din browser. Der bliver ikke sendt noget nogen steder hen, og der er ingen kunstig intelligens i den.

## Sådan afleverer du

1. Skriv dit navn, din klasse og afleveringens titel øverst.
2. Skriv afleveringen.
3. Tryk på **Aflever som PDF**, og vælg *Gem som PDF* i printvinduet.
4. Upload PDF'en under opgaven i Lectio.

Vil du hellere arbejde videre i Word, LibreOffice eller Google Docs, så tryk på **Gem som Word**. Formlerne bliver til Word-ligninger, som du kan rette i.

## Formler

| Det vil du | Sådan gør du |
|---|---|
| Indsætte en formel fra formelsamlingen | Tryk på **Fysikformler**, og klik på formlen |
| Indsætte en konstant | Tryk på **Konstanter**, og klik på værdien |
| Sætte formlen på sin egen linje | Hold **Shift** nede, når du klikker |
| Skrive din egen formel | Tryk på **Skriv egen formel**, eller skriv `$v = s/t$` direkte i teksten |
| Rette en formel | Klik på den |

Formler skrives i LaTeX. De vigtigste:

| Skriv | Bliver til |
|---|---|
| `\frac{a}{b}` | $\frac{a}{b}$ |
| `v^2` og `v_0` | $v^2$ og $v_0$ |
| `\sqrt{x}` | $\sqrt{x}$ |
| `\Delta t` | $\Delta t$ |
| `2{,}5 \cdot 10^{3}` | $2{,}5 \cdot 10^{3}$ |
| `\lambda`, `\rho`, `\omega` | $\lambda$, $\rho$, $\omega$ |
| `\ \mathrm{m/s}` | $\ \mathrm{m/s}$ |

Skriv komma som `{,}`. Ellers sætter LaTeX et mellemrum efter kommaet.

## Lommeregner

Tryk på **Lommeregner**. Skriv eller klik regnestykket ind, fx `6,674·10^-11·5,972·10^24/(6,371·10^6)^2`. Du ser det som en formel med resultatet.

- **Indsæt udregning** (eller Enter) sætter hele udregningen med resultat ind i teksten, der hvor markøren stod.
- **Indsæt kun resultat** sætter kun tallet ind.
- **Konstant** henter en naturkonstant ind i regnestykket, og **Enhed** sætter en enhed på resultatet.
- **Ans** er det sidste resultat, du har indsat.
- Vælg antal **betydende cifre**, og om vinkler er i grader eller radianer.
- Du kan flytte lommeregneren ved at trække i den mørke bjælke.

## Genveje med Markdown

| Skriv | Bliver til |
|---|---|
| `# ` , `## ` , `### ` i starten af en linje | Overskrift 1, 2 og 3 |
| `- ` eller `* ` i starten af en linje | Punktliste |
| `1. ` i starten af en linje | Nummereret liste |
| `**fed**` | **fed** |
| `*kursiv*` | *kursiv* |
| `$v = s/t$` | En formel |

Knappen **Markdown** viser hele afleveringen som Markdown-tekst, som du kan kopiere eller hente som fil. Du retter stadig i editoren.

## Billeder og tabeller

- **Billeder:** Tryk på billedknappen, eller træk et billede ind i teksten. Billedet bliver sat ind i halv bredde. Klik på det, og træk i den blå prik nederst til højre, eller vælg 25, 50, 75 eller 100 %.
- **Tabeller:** Tryk på **Tabel**. Sæt markøren i tabellen, og brug **+ række** og **+ søjle**. Hop mellem cellerne med Tab. En celle kan kun have én linje, så Enter hopper til cellen nedenunder. Fra nederste række kommer du ned under tabellen.

## Din kladde

- Kladden gemmes automatisk i **den browser, du skriver i**. Den er der stadig, når du kommer tilbage på samme computer.
- Den forsvinder, hvis du sletter browserdata, bruger privat vindue eller skifter computer. Tryk derfor på **Gem kladde** en gang imellem. Så får du en fil, som du kan åbne igen med **Åbn kladde**.
- Kladdefilen skal ikke afleveres. Det er PDF'en, du afleverer.
