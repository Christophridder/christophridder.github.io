---
title: "Lineær regression og aksetransformation"
weight: 5
pdf: "pdfs/lineaer-regression.pdf"
pdf_ny_fane: true
---

**Niveau: NV, Fysik og Kemi C–A** · **Emne: Databehandling – lineær regression og aksetransformation**

Lineær regression er den metode, du kommer til at bruge allermest i fysik og kemi. Du har nogle målinger, du har en teori – og regnearket finder den rette linje, der passer bedst. Det svære er ikke at få regnearket til at tegne linjen, men at forstå, **hvad tallene i ligningen betyder fysisk**.

Denne siden består af to dele:

1. **Lineær regression** – når sammenhængen i forvejen er lineær dvs at den fysiske model du vil bruge til at afbilde dine data følger en ret linje. $y = ax + b$. (Så kan du se om de gør eller ej)
2. **Aksetransformation** – når din fysiske model **ikke** forventer en lineær sammenhæng så har du to muligheder 1. du fitter dine data med den funktion som du forventer eller 2. (og det er det jeg viser her nedenunder) du laver **om på akserne** sådan at den graf du afbilder igen bliver lineær. Du transformerer akserne !!

Du skal kunne lave et punktdiagram i et regneark og tilføje en tendenslinje. Har du brug for en genopfriskning, så se [denne video](https://www.youtube.com/watch?v=krNyNWF6Ix0).

## Del 1 – Hvad er densiteten af vand?
Jeg illustrerer regression her vha et simpelt forsøg i fysikken: 

### Forsøget 

Du hælder vand i en målekolbe, der står på en vægt, og aflæser volumen og samlet masse flere gange. **Vægten er med vilje ikke nulstillet** med den tomme kolbe på – det kommer vi tilbage til.

| Volumen $V$ (mL) | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|
| Samlet masse $m$ (g) | 88,3 | 108,4 | 128,3 | 148,4 | 168,1 |

Punkterne ligger pænt på en ret linje:

![Samlet masse som funktion af volumen med tendenslinje](/img/linreg/linreg-densitet.svg)

### x og y løber – a og b står stille
Dvs at $x$ og $y$ er variabler som du har målt: $x-$værdier og $y-$værdier, eller som man vi skrive i matematikken $y(x)$ 

En ret linje har forskriften

$$y = a \cdot x + b$$

Det vigtige er, at de fire bogstaver ikke er af samme slags:

- $x$ og $y$ er  variabler, **rækker af målinger**. Hver søjle i tabellen er et sammenhørende par $(x, y)$.
- $a$ og $b$ er **konstanter** – ét tal hver, som gælder for hele måleserien.

Tabellen gemmer altså på fem ligninger med de samme to ubekendte:

$$88{,}3 = a \cdot 20 + b \qquad 108{,}4 = a \cdot 40 + b \qquad \dots \qquad 168{,}1 = a \cdot 100 + b$$

Målingerne er aldrig helt perfekte, så der findes ikke ét par $(a, b)$, der passer præcist i dem alle. **Lineær regression** finder det par, der passer *bedst*. Det er det, regnearket gør, når du vælger *Tilføj tendenslinje*. Husk at sætte flueben ved **Vis ligning** og **Vis R²**.

Her giver regnearket $a = 0{,}998$ og $b = 68{,}42$.

### Den dumme løsning

Teorien for densitet $\rho$ er

$$m = \rho \cdot V$$

Så kan man vel bare regne $\rho = \frac{m}{V}$ ud for hver måling?

> **Opgave 1.** Beregn $\frac{m}{V}$ for alle fem målinger. Hvad sker der? Hvorfor giver det ikke mening, når densiteten af vand er en konstant? Læs ikke videre, før du har et bud.

### b-værdien – det, vi glemte at nulstille

Problemet er, at vægten ikke er nulstillet. Den viser massen af vandet **plus kolben**. Derfor passer $m = \rho \cdot V$ ikke – når der ingen vand er ($V = 0$), viser vægten stadig kolbens masse.

Vi udvider teorien:

$$m = \rho \cdot V + m_{\text{kolbe}}$$

Nu har teorien præcis samme form som regnearkets ligning, og du kan sætte dem op over hinanden i et **tolkningsskema**:

![Tolkningsskema: m = ρ·V + m₁ over y = a·x + b, derfor a = ρ og b = m₁](/img/linreg/tolkning-densitet.svg)

| Regneark | Teori | Fysisk betydning | Værdi |
|---|---|---|---|
| $y$ | $m$ | samlet masse (målt) | række af tal |
| $x$ | $V$ | vandets volumen (målt) | række af tal |
| $a$ | $\rho$ | vandets densitet | $0{,}998$ g/mL |
| $b$ | $m_{\text{kolbe}}$ | kolbens masse | $68{,}42$ g |

Det smarte er, at du **ikke behøver at nulstille vægten**. Regressionen finder både densiteten og kolbens masse. I mange forsøg er det slet ikke muligt at "nulstille" – og så er $b$-værdien netop det, der redder dig.

> **Opgave 2.** Vis ud fra enhederne, at $b$ må være en masse, og at $a$ må have enheden g/mL.

### To ting skal være på plads

For at bruge lineær regression til noget naturvidenskabeligt skal du have:

1. **Et datasæt** – sammenhørende værdier af $x$ og $y$
2. **En teori eller hypotese**, der siger, hvordan $x$ og $y$ hænger sammen – og dermed hvad $a$ og $b$ betyder

Regnearket kan kun levere tallene. Tolkningen er dit arbejde.

### Brug ligningen til at forudsige

Når du kender $a$ og $b$, kan du beregne $y$ ud fra $x$ – eller omvendt:

| Find $y$ | Find $x$ |
|---|---|
| $y = a \cdot x + b$ | $x = \dfrac{y - b}{a}$ |

> **Opgave 3.**
>
> a) Skriv de to formler ovenfor med de fysiske størrelser $m$, $V$, $\rho$ og $m_{\text{kolbe}}$.
>
> b) Hvad viser vægten, hvis du fylder 10 L vand i den samme opstilling?
>
> c) Hvor meget vand er der i kolben, hvis vægten viser 14,5 kg?

<details>
<summary>Facit til opgave 3</summary>

b) $m = 0{,}998 \text{ g/mL} \cdot 10\,000 \text{ mL} + 68{,}42 \text{ g} \approx 10\,048 \text{ g} \approx 10{,}0 \text{ kg}$

c) $V = \dfrac{14\,500 \text{ g} - 68{,}42 \text{ g}}{0{,}998 \text{ g/mL}} \approx 14\,460 \text{ mL} \approx 14{,}5 \text{ L}$

</details>

### Forskellige eksempler

> **Opgave 4.** Opstil en teori på formen $y = a \cdot x + b$ for hvert eksempel. Hvad er $x$ og $y$, og hvad betyder $a$ og $b$? Er en ret linje overhovedet en god model?
>
> 1. Højden af et træ målt den 1. maj hvert år i 10 år
> 2. Vægten af en lillebror målt hver dag fra fødslen til han er 6 år
> 3. Bland-selv-slik, der vejes af i supermarkedet
> 4. En taxatur fra midtbyen i Aarhus til Trøjborg, Lystrup, Hjortshøj og Hornslet

## Del 2 – Aksetransformation

### Terningeopgaven

Byg en stor terning af små terninger – som en Rubiks terning. En terning med kantlængden 2 består af 8 små terninger. Kald kantlængden $a_{\text{akse}}$ og det samlede antal $a_{\text{tot}}$.

> **Opgave 5.** Byg (eller tegn) terninger med kantlængde 1 til 5, notér antallet, og lav et punktdiagram.

![Antal terninger som funktion af kantlængden – punkterne ligger på en krum kurve](/img/linreg/linreg-terninger.svg)

Punkterne ligger **ikke** på en ret linje. Fordobler du kantlængden, bliver antallet otte gange så stort. Så hvad nu?

### Teorien

Normalt er det svært at gætte den rigtige teori – men det er let at *afprøve* et gæt. Her kender vi svaret: antallet er kantlængden i tredje:

$$a_{\text{tot}} = a_{\text{akse}}^3$$

> **Opgave 6.** Skriv teorien på formen $y = a \cdot x + b$, og udfyld tolkningsskemaet. Hvad er $x$? Og hvad er $a$ og $b$?

![Tomt tolkningsskema](/img/linreg/tolkning-tom.svg)

<details>
<summary>Facit til opgave 6</summary>

![Tolkningsskema for terningerne: a_tot = 1·a_akse³ + 0](/img/linreg/tolkning-terninger.svg)

$y = a_{\text{tot}}$, $x = a_{\text{akse}}^3$, $a = 1$ og $b = 0$.

</details>

### Tving grafen til at blive lineær

Tricket er, at $x$ **ikke** er kantlængden, men kantlængden i tredje. Så laver du en ny kolonne med $a_{\text{akse}}^3$ og plotter antallet op ad den i stedet:

|   | A | B | C | D |
|---|---|---|---|---|
| 1 | $a_{\text{akse}}$ | $a_{\text{tot}}$ | $a_{\text{akse}}^3$ | $a_{\text{tot}}$ |
| 2 | 1 | 1 | `=A2^3` | `=B2` |
| 3 | 2 | 8 | `=A3^3` | `=B3` |

1. Skriv formlerne i C2 og D2, og træk dem ned.
2. Kolonne D er bare en kopi af B – $y$-værdierne skal ikke ændres.
3. Markér kolonne C og D, lav et nyt punktdiagram, og tilføj en tendenslinje.

![Antal terninger som funktion af kantlængden i tredje – en ret linje](/img/linreg/linreg-terninger-lineariseret.svg)

Nu ligger punkterne på en ret linje. Du har vist en sammenhæng, der **ikke** er lineær, på en lineær måde – ved at **transformere aksen**. Det kaldes også *linearisering*.

> **Opgave 7.** Hvad fortæller det dig, at du får en ret linje med $a = 1$ og $b = 0$? Hvad ville det betyde, hvis punkterne *ikke* lå på en ret linje efter transformationen?

## Opgave 8 – Gnidningskoefficienten

Du trækker en træklods hen over et bord med et newtonmeter og lægger forskellige lodder oven på klodsen. Newtonmeteret viser gnidningskraften $F_{\text{gnid}}$. Normalkraften $F_N$ er lige så stor som tyngden af klods og lodder.

![Træklods med lodder trækkes med et newtonmeter](/img/linreg/linreg-gnidning-opstilling.svg)

Teorien er:

$$F_{\text{gnid}} = \mu \cdot F_N + F_{\text{fejl}}$$

hvor $\mu$ er gnidningskoefficienten.

| $F_N$ (N) | 3,0 | 5,5 | 8,0 | 10,0 | 12,0 | 15,0 | 17,0 |
|---|---|---|---|---|---|---|---|
| $F_{\text{gnid}}$ (N) | 0,92 | 1,49 | 2,11 | 2,55 | 3,05 | 3,73 | 4,23 |

> a) Udfyld et tolkningsskema, og lav grafen i regnearket.
>
> b) Bestem gnidningskoefficienten $\mu$. Hvilken enhed har den?
>
> c) Bestem $b$-værdien, og giv et bud på en fysisk tolkning. Den er ikke helt så oplagt som kolbens masse.

<details>
<summary>Facit til opgave 8</summary>

![Tolkningsskema for gnidning](/img/linreg/tolkning-gnidning.svg)

![Gnidningskraft som funktion af normalkraft med tendenslinje](/img/linreg/linreg-gnidning.svg)

- $\mu = 0{,}236$. Den har **ingen enhed**, fordi den er et forhold mellem to kræfter (N/N).
- $b = 0{,}205$ N. Ifølge teorien burde gnidningskraften være 0, når $F_N = 0$. En $b$-værdi forskellig fra nul peger på en **systematisk fejl** – fx at newtonmeteret ikke viser nul, når det ikke er belastet. Læs mere under [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}).

</details>

## Lineær regression i Python

Du kan gøre det samme med `numpy.polyfit`:

```python
import numpy as np

V = np.array([20, 40, 60, 80, 100])             # mL
m = np.array([88.3, 108.4, 128.3, 148.4, 168.1]) # g

a, b = np.polyfit(V, m, 1)
print(f"rho     = {a:.3f} g/mL")
print(f"m_kolbe = {b:.2f} g")
```

Ved aksetransformation transformerer du bare $x$ først, fx `np.polyfit(k**3, n, 1)`.

## Læs videre

- [Naturvidenskabelig metode]({{< relref "/docs/nat/naturvidenskabelig-metode" >}}) – hvor passer regression ind?
- [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}) og [Betydende cifre]({{< relref "/docs/nat/betydendecifre" >}})
- [Faglige metoder i fysik]({{< relref "/docs/fysik/Metoder" >}}) · [Faglige metoder i kemi]({{< relref "/docs/kemi/Metoder" >}})

<details>
<summary>Til læreren</summary>

Forløbet tager 2–3 moduler og kan laves som gruppearbejde. Eleverne kender $y = a \cdot x + b$ fra matematik, men har svært ved at genkende den, når bogstaverne bliver til fysiske størrelser. Typiske snublesten:

- Bogstaverne er ikke længere $x$, $y$, $a$ og $b$.
- $x$ og $y$ er rækker af målinger – ikke faste tal.
- $a$ og $b$ "spyttes ud" af regnearket, men er alligevel konstanter.
- $a$ og $b$ skal tolkes ud fra en teori – inklusive enheder.
- Ligningen skal bruges "begge veje" til at forudsige $x$ og $y$.
- $R^2$ bruges her kun intuitivt: jo tættere på 1, jo bedre passer linjen.
- Regnearket i sig selv kan være en barriere for de svageste elever.

Tolkningsskemaet er lavet for at gøre mønsteret genkendeligt på tværs af fysik, kemi og biologi.

</details>
