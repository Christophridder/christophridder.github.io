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

Tryk på **Lommeregner**. Lommeregneren har linjer ligesom et regneark: hver linje viser regnestykket som en formel med resultatet, og Enter giver en ny linje.

**Gem tal under et navn.** Skriv fx `m = 5,2` på én linje og `v = 12` på den næste. Så kan du skrive `E = 1/2 m v^2` nedenunder. Lommeregneren viser både formlen, formlen med tallene sat ind og resultatet:

$$E = \frac{1}{2} \cdot m \cdot v^{2} = \frac{1}{2} \cdot 5{,}2\ \mathrm{kg} \cdot \left(12\ \mathrm{m/s}\right)^{2} = 374\ \mathrm{J}$$

**Ret et enkelt tal.** Klik på linjen med tallet, og ret det. Alle linjer nedenunder bliver regnet om med det samme.

**Regn en formel fra teksten ud.** Klik på formlen i afleveringen, og tryk på **🖩 Regn ud**. Formlen bliver oversat til lommeregneren. Har du skrevet tallene ind i formlen, regnes de ud med det samme. Har du kun skrevet bogstaver, fx $v = \frac{s}{t}$, viser lommeregneren knapper som `s = …`, så du kan give dem en værdi på linjen ovenover. Du kan også markere noget tekst og trykke på **Lommeregner**.

| Det vil du | Sådan gør du |
|---|---|
| Sætte hele udregningen ind i teksten | **Indsæt udregning** (eller Ctrl+Enter) |
| Sætte kun resultatet ind | **Indsæt kun resultat**. Står der en formel lige før, kommer resultatet ind som $= \ldots$ efter den |
| Hente en naturkonstant | Vælg den under **Konstant**. På en tom linje bliver den gemt under sit navn, fx `g = 9,82` med enheden m/s² |
| Sætte en enhed på | Skriv den i **Enhed på linjen**. Enheden kommer også med, når tallet sættes ind i en formel længere nede |
| Bruge resultatet på linjen ovenover | Skriv `Ans` |
| Slette en linje | Tryk på ✕, eller tryk Backspace på en tom linje |

- Vælg antal **betydende cifre**, og om vinkler er i grader eller radianer.
- Du kan flytte lommeregneren ved at trække i den mørke bjælke. **Ryd** sletter alle linjer.
- Linjerne bliver gemt i din browser, så de er der stadig, når du åbner siden igen.

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
