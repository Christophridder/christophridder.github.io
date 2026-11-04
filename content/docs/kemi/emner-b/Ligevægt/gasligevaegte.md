---
title: "Gasligevægte"
weight: 2
pdf: "pdfs/gasligevaegte.pdf"
pdf_ny_fane: true
---

**Niveau: Kemi B** · **Emne: Gasligevægte og partialtryk**

Denne side hører til [Ligevægt]({{< relref "ligevaegt" >}}) og [Opgaver til ligevægt]({{< relref "opgaver-ligevaegt" >}}). Den forklarer det, der er særligt ved gasser, og gennemgår gaskortene i [Flashcards-ligevægt]({{< relref "flashcards-ligevaegt" >}}).

## Partialtryk

Molekylerne i en gas rammer hele tiden beholderens vægge. Det giver et tryk. I en gasblanding bidrager hver gas med sit eget tryk, **partialtrykket** $p$. Det samlede tryk er summen:

$$p_{\text{total}} = p(\ce{A}) + p(\ce{B}) + p(\ce{C})$$

Partialtrykket er proportionalt med koncentrationen, $p(\ce{A}) = [\ce{A}] \cdot R \cdot T$. Du kan derfor tænke på partialtrykket som gassens koncentration, og derfor skriver vi reaktionsbrøken med partialtryk i stedet for koncentrationer. For $\ce{2NO(g) + Br2(g) <=> 2NOBr(g)}$ er

$$Y = \frac{p(\ce{NOBr})^2}{p(\ce{NO})^2 \cdot p(\ce{Br2})}$$

Reglerne er de samme som hidtil: Ved ligevægt er $Y = K$. Lige efter et indgreb sammenligner du $Y$ med $K$.

## Hvad betyder "trykket øges"?

Det er her, de fleste fejl sker. Trykket kan stige på tre måder, og de gør ikke det samme ved ligevægten.

| Indgreb | Partialtryk | Sker der en forskydning? |
|---|---|---|
| Volumen mindskes | **Alle** partialtryk stiger med samme faktor | Kun hvis der er forskelligt antal gasmolekyler på de to sider |
| Der tilsættes mere af ét stof i reaktionen | Kun det stofs partialtryk stiger | Ja, væk fra stoffet |
| Der tilsættes en inaktiv gas ved fast volumen | Partialtrykkene i $Y$ ændres **ikke** | Nej, selvom det samlede tryk stiger |

Når en opgave bare siger, at "trykket øges", menes der normalt, at volumen mindskes.

## Tryk flytter ligevægten: NOBr

$$\underset{\text{3 gasmolekyler}}{\ce{2NO(g) + Br2(g)}} \ce{<=>} \underset{\text{2 gasmolekyler}}{\ce{2NOBr(g)}}$$

$$Y = \frac{p(\ce{NOBr})^2}{p(\ce{NO})^2 \cdot p(\ce{Br2})}$$

{{< gaskammer "nobr" >}}

Stemplet halverer volumen, så alle partialtryk fordobles. Der er 3 faktorer i nævneren og kun 2 i tælleren:

$$Y = \frac{2^2}{2^2 \cdot 2} \cdot K = \tfrac{1}{2} K$$

$K > Y$, så ligevægten forskydes mod **højre**. Der bliver færre molekyler, og trykket falder lidt. Det er Le Chateliers princip: Forskydningen formindsker virkningen af indgrebet, men fjerner den ikke. $K$ er uændret, fordi temperaturen er den samme. Tallene i figuren er valgt til eksemplet.

## Tryk flytter ikke ligevægten: HI

$$\underset{\text{2 gasmolekyler}}{\ce{H2(g) + I2(g)}} \ce{<=>} \underset{\text{2 gasmolekyler}}{\ce{2HI(g)}}$$

$$Y = \frac{p(\ce{HI})^2}{p(\ce{H2}) \cdot p(\ce{I2})}$$

{{< gaskammer "hi" >}}

Der er 2 faktorer i både tæller og nævner, så de går ud med hinanden:

$$Y = \frac{2^2}{2 \cdot 2} \cdot K = K$$

Der sker **ingen forskydning**. En reaktion, der ikke ændrer antallet af molekyler, kan ikke modvirke en trykændring.

Gassen bliver alligevel mørkere, når du presser den sammen, fordi den violette $\ce{I2}$ står tættere. Det er ikke en forskydning: Farven springer med det samme og ændrer sig ikke bagefter.

## Sådan afgør du det hurtigt

1. Tæl **gasmolekyler** på hver side. Stoffer på formen (s) og (l) tæller ikke.
2. Mindre volumen (højere tryk) forskyder mod siden med **færrest** gasmolekyler.
3. Større volumen (lavere tryk) forskyder mod siden med **flest** gasmolekyler.
4. Lige mange på begge sider: ingen forskydning.
5. Kun temperaturen ændrer $K$. Tryk ændrer $Y$.

## Gaskortene i flashcards

Numrene er kortenes numre i [Flashcards-ligevægt]({{< relref "flashcards-ligevaegt" >}}).

### Volumen og tryk

**Kort 11** · $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$, trykket falder. Der er 4 gasmolekyler til venstre og 2 til højre. Lavere tryk forskyder mod flest molekyler, altså mod **venstre**. Med brøken: Halveres alle tryk, bliver $Y = \dfrac{(1/2)^2}{(1/2)^4}K = 4K$. $K < Y$, så brøken skal blive mindre.

**Kort 21** · $\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$, trykket øges. Reaktionsbrøken er bygget præcis som for NOBr: 3 molekyler mod 2. Ligevægten forskydes mod **højre**.

**Kort 20** · Flest gasmolekyler til venstre, volumen øges. Større volumen forskyder mod flest molekyler, altså mod **venstre**.

**Kort 24** · $\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}$, volumen øges. Ligevægten forskydes mod **højre**, hvor der er 2 molekyler. Stofmængden af $\ce{PCl3}$ stiger, men **koncentrationen** $[\ce{PCl3}]$ ender lavere end før, fordi alt er fordelt i et større volumen. Forskydningen opvejer kun en del af fortyndingen. Skeln mellem stofmængde og koncentration.

**Kort 34** · Grafen viser $\ce{N2O4(g) <=> 2NO2(g)}$. Begge kurver springer op til det dobbelte ved $t = 60\ \text{s}$, altså er volumen halveret. $Y = \dfrac{[\ce{NO2}]^2}{[\ce{N2O4}]}$ fordobles, så $K < Y$. Ligevægten forskydes mod venstre, og derfor falder $[\ce{NO2}]$ bagefter. Springet er indgrebet, og den langsomme ændring bagefter er forskydningen.

### Inaktiv gas

**Kort 5** · Fast volumen, inaktiv gas tilsættes. Det samlede tryk stiger, men de reagerende gasser har samme stofmængde i samme volumen, så deres partialtryk er uændrede. $Y = K$, og der sker **ingen forskydning**. Reaktionsbrøken er ligeglad med gasser, der ikke står i den. Får beholderen lov at udvide sig, er det noget andet: Så falder partialtrykkene, præcis som ved større volumen.

### Tilsæt eller fjern ét stof

**Kort 12** · $\ce{H2(g) + I2(g) <=> 2HI(g)}$, du fjerner $\ce{H2}$. Tryk flytter ikke denne ligevægt, men det gør et stof, der fjernes: Nævneren bliver mindre, $K < Y$, og ligevægten forskydes mod **venstre**, hen mod $\ce{H2}$. Det er den vigtigste pointe i HI-eksemplet: Lige mange molekyler betyder kun, at *volumenændringer* er uden virkning.

**Kort 10** · $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}$, mere $\ce{CO}$. Samme logik: $p(\ce{CO})$ står i nævneren, $K > Y$, og ligevægten forskydes mod **højre**.

**Kort 23** · $\ce{CH4(g) + H2O(g) <=> CO(g) + 3H2(g)}$, du fjerner $\ce{H2}$. Tælleren bliver mindre, $K > Y$, så ligevægten forskydes mod **højre**, hen mod $\ce{H2}$.

**Kort 7** · Reaktionsbrøken for $\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$:

$$Y = \frac{p(\ce{SO3})^2}{p(\ce{SO2})^2 \cdot p(\ce{O2})}$$

**Kort 26** · $\ce{CO3^2-(aq) + 2H+(aq) <=> H2O(l) + CO2(g)}$. Flere $\ce{H+}$ forskyder mod højre, og $\ce{CO2}$ bobler ud af det åbne glas. Gassen bliver ved med at forsvinde, så reaktionen fortsætter. I et åbent system er det ikke en ligevægt, og reaktionen kan løbe til ende.

### Temperatur

Temperatur er anderledes end tryk: Den ændrer selve $K$. Skriv derfor $Q$ i skemaet, og argumentér kun ud fra skemaet.

**Kort 9 og kort 4** · $\ce{N2(g) + 3H2(g) <=> 2NH3(g) + Q}$. Mere varme forskyder mod **venstre**, så der er mindre $\ce{NH3}$ ved ligevægt. Alligevel bruger man høj temperatur i Haber-processen, fordi ligevægten så indstiller sig hurtigere. *Hvor hurtigt* og *hvor langt* er to forskellige spørgsmål. Højt tryk hjælper til gengæld både hastigheden og ligevægten.

**Kort 22 og kort 41** · $\ce{N2O4(g) + Q <=> 2NO2(g)}$. Afkøling fjerner $Q$ og forskyder mod **venstre** mod farveløs $\ce{N2O4}$. Opvarmning forskyder mod højre mod brun $\ce{NO2}$, så den mørkeste kolbe står i det kogende vand.
