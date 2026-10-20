---
title: "Procentvis afvigelse"
weight: 7
---

**Niveau: NV, Fysik og Kemi C–A** · **Emne: Databehandling**

# Procentvis afvigelse

Ofte måler du i et forsøg en værdi $x_{\text{eksp}}$ og sammenligner den med en forventet – typisk teoretisk eller tabelopslået – værdi $x_{\text{teo}}$. Hvor godt de passer sammen, angiver du med den **procentvise afvigelse** (også kaldet den *relative afvigelse*):

$$\text{procentvis afvigelse} = \frac{x_{\text{eksp}} - x_{\text{teo}}}{x_{\text{teo}}} \cdot 100\,\%$$

Tre ting skal du huske:

- **Fortegnet skal med!** Et negativt resultat betyder, at din målte værdi er *mindre* end den teoretiske. Et positivt betyder, at den er *større*.
- **Du dividerer med den teoretiske værdi** – ikke med din egen måling. Den teoretiske værdi er referencen.
- **Enhederne går ud.** Den procentvise afvigelse har ingen enhed, så $x_{\text{eksp}}$ og $x_{\text{teo}}$ skal stå i samme enhed, før du regner.

Fortegnet er ikke pynt. Det er dit bedste fingerpeg om, **hvilken fejlkilde** der har trukket resultatet i en bestemt retning (se [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}})).

## Eksempel 1: Tyngdeaccelerationen $g$

Du bestemmer tyngdeaccelerationen ved at hænge lodder med kendt masse $m$ i en kraftmåler og aflæse kraften $F$. Når loddet hænger stille, er kraften lig med tyngdekraften:

$$F = g \cdot m$$

Plotter du $F$ som funktion af $m$, skal du altså få en ret linje gennem $(0,0)$ med hældningen $g$. I praksis laver du lineær regression $F = a \cdot m + b$, hvor $a$ er dit bud på $g$, og $b$ fanger en eventuel systematisk fejl, fx at kraftmåleren ikke var nulstillet (se [Lineær regression]({{< relref "/docs/nat/lineaer-regression" >}})).

![Graf af F som funktion af m med regressionslinje og den teoretiske linje F = 9,82 N/kg · m](/img/nat/procentvis-afvigelse-g.svg)

Regressionen giver:

$$F = 9{,}4317\,\tfrac{\text{N}}{\text{kg}} \cdot m + 0{,}0005\,\text{N}$$

- Hældning: $g_{\text{eksp}} = 9{,}4317\ \tfrac{\text{N}}{\text{kg}}$
- Skæring: $b = 0{,}0005\ \text{N}$ – så lille, at den i praksis er nul. Kraftmåleren var altså nulstillet.

Tabelværdien for tyngdeaccelerationen i Danmark er $g_{\text{teo}} = 9{,}82\ \tfrac{\text{N}}{\text{kg}}$ (= $9{,}82\ \tfrac{\text{m}}{\text{s}^2}$).

$$\text{procentvis afvigelse} = \frac{9{,}4317\,\tfrac{\text{N}}{\text{kg}} - 9{,}82\,\tfrac{\text{N}}{\text{kg}}}{9{,}82\,\tfrac{\text{N}}{\text{kg}}} \cdot 100\,\% = -3{,}95\,\% \approx -4{,}0\,\%$$

Resultatet er **negativt**, fordi den eksperimentelle værdi er mindre end den teoretiske. På grafen kan du se det direkte: den blå regressionslinje ligger under den grå, teoretiske linje, og afstanden vokser med $m$.

> **Hvor mange cifre?** Regnearket giver gerne $-3{,}954\,\%$, men $g_{\text{teo}}$ er kun angivet med 3 betydende cifre. Angiv derfor afvigelsen med 2–3 betydende cifre (se [Betydende cifre]({{< relref "/docs/nat/betydendecifre" >}})).

## Typiske fejl

| Fejl | Hvad sker der? |
|---|---|
| Fortegnet droppes | Du mister informationen om, *hvilken vej* resultatet er skævt – og dermed om fejlkilden. |
| Dividerer med $x_{\text{eksp}}$ | Tallet bliver forkert, og jo større afvigelsen er, jo mere forkert. |
| Byttede tal i tælleren ($x_{\text{teo}} - x_{\text{eksp}}$) | Fortegnet bliver modsat – og din fejlkildediskussion peger den forkerte vej. |
| Forskellige enheder (fx g/mol og kg/mol) | Afvigelsen bliver fuldstændig meningsløs. |
| Teoriværdi, der ikke passer til forholdene | Se eksempel 3: lydens fart afhænger af temperaturen. |

## Flere eksempler

### Eksempel 2: Vands specifikke varmekapacitet (Fysik C)

Du opvarmer vand med en elkoger og finder $c_{\text{eksp}} = 4520\ \tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. Tabelværdien er $c_{\text{teo}} = 4180\ \tfrac{\text{J}}{\text{kg}\cdot\text{K}}$.

$$\text{procentvis afvigelse} = \frac{4520 - 4180}{4180} \cdot 100\,\% = +8{,}1\,\%$$

**Fortolkning:** Du har beregnet $c = \dfrac{E}{m \cdot \Delta T}$ ud fra den energi $E$, elkogeren har leveret. En del af energien går dog til at opvarme selve kogeren og omgivelserne. Vandet får altså mindre energi, end du regner med, så $\Delta T$ bliver mindre, og $c$ bliver for **stor**. Fortegnet passer med fejlkilden **varmetab**.

### Eksempel 3: Lydens fart (Fysik C/B)

Du måler lydens fart i luft til $v_{\text{eksp}} = 336\ \tfrac{\text{m}}{\text{s}}$ og sammenligner med tabelværdien ved 20 °C, $v_{\text{teo}} = 343\ \tfrac{\text{m}}{\text{s}}$.

$$\text{procentvis afvigelse} = \frac{336 - 343}{343} \cdot 100\,\% = -2{,}0\,\%$$

**Fortolkning:** Lydens fart i luft afhænger af temperaturen; tilnærmet gælder $v \approx 331{,}3\ \tfrac{\text{m}}{\text{s}} + 0{,}606\ \tfrac{\text{m}}{\text{s}\cdot{}^\circ\text{C}} \cdot t$. Blev forsøget lavet udenfor ved ca. 8 °C, er den rigtige teoretiske værdi $v_{\text{teo}} \approx 336\ \tfrac{\text{m}}{\text{s}}$ – og så er afvigelsen næsten **0 %**. Pointen: Den teoretiske værdi skal passe til de forhold, du har målt under.

### Eksempel 4: Molar masse af gassen i en lighter (Kemi C)

Du opsamler gassen fra en lighter over vand og bestemmer den molare masse til $M_{\text{eksp}} = 55{,}1\ \tfrac{\text{g}}{\text{mol}}$. Gassen er (overvejende) butan, $\ce{C4H10}$, med $M_{\text{teo}} = 58{,}12\ \tfrac{\text{g}}{\text{mol}}$.

$$\text{procentvis afvigelse} = \frac{55{,}1 - 58{,}12}{58{,}12} \cdot 100\,\% = -5{,}2\,\%$$

**Fortolkning:** Gas, der er opsamlet over vand, indeholder også **vanddamp**. Hvis du bruger hele trykket i idealgasligningen $n = \dfrac{p \cdot V}{R \cdot T}$, bliver stofmængden $n$ af butan for stor, og $M = \dfrac{m}{n}$ bliver for **lille**. Det passer med det negative fortegn. Desuden indeholder lightergas ofte lidt propan ($M = 44{,}10\ \tfrac{\text{g}}{\text{mol}}$), som trækker samme vej.

## Læs videre

- [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}) – grove fejl, systematiske fejl og usikkerheder
- [Præcision og nøjagtighed]({{< relref "/docs/nat/praecision-noejagtighed" >}})
- [Betydende cifre]({{< relref "/docs/nat/betydendecifre" >}})
- [Lineær regression og aksetransformation]({{< relref "/docs/nat/lineaer-regression" >}})

---

*Siderne er lavet af Christoph Ridder med hjælp af flere fysik-A-B-C-hold på Egaa Gymnasium 2020 2025. Feedback gerne til cr@egaa-gym.dk*
