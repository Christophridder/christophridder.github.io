---
title: "Lineær regression"
weight: 4
---

**Niveau: Fysik C–A** · **Emne: Databehandling**

[Tilbage til Faglige metoder i fysik]({{< relref "/docs/fysik/Metoder" >}})

## Kort forklaret

- Du måler **sammenhørende værdier** af to størrelser, fx tilført energi og temperatur.
- Du har en **teori**, der siger, at sammenhængen er en ret linje: $y = a \cdot x + b$.
- Regnearket finder den linje, der passer **bedst** til alle punkterne på én gang. Det er lineær regression.
- Hældningen $a$ og skæringen $b$ er **fysiske størrelser**, når du har valgt akserne rigtigt.

Har du brug for det helt grundlæggende om $x$, $y$, $a$ og $b$, så start med [densitetsforsøget]({{< relref "/docs/fysik/C-Eksp/densitet" >}}). Her er hældningen densiteten, og $b$-værdien er måleglassets masse. Endnu flere eksempler finder du under [Lineær regression og aksetransformation]({{< relref "/docs/nat/lineaer-regression" >}}) i Nat.

## Eksempel: Varmekapacitet for vand i en elkedel

Du hælder vand i en elkedel og sætter kedlen til en **energimåler**. Undervejs tager du stikket ud, rører rundt og aflæser temperaturen $T$ og den samlede energi $E$, som energimåleren viser.

- Vandets masse: $m = 0{,}888\text{ kg}$
- Starttemperatur: $T_{\text{start}} = 22{,}0\,^\circ\text{C}$

Teorien er

$$E = m \cdot c \cdot \Delta T \qquad \text{hvor} \qquad \Delta T = T - T_{\text{start}}$$

og $c$ er vandets varmekapacitet. Se også [forsøget med varmekapacitet]({{< relref "/docs/fysik/C-Eksp/varmekapacitet" >}}).

### Målingerne

Du har kun målt de to første kolonner. De to sidste skal du selv regne ud:

| Målt $T$ (°C) | $E$ (J) | $\Delta T$ (K) | $m \cdot \Delta T$ (kg·K) – **x-akse** | $E$ (J) – **y-akse** |
|---|---|---|---|---|
| 22,0 | 0 | | | |
| 29,6 | 31 600 | | | |
| 35,1 | 53 800 | | | |
| 43,8 | 88 400 | | | |
| 51,9 | 120 500 | | | |
| 60,7 | 156 000 | | | |
| 72,3 | 202 100 | | | |
| 83,4 | 247 100 | | | |

### I regnearket – husk dollartegnet

Skriv $m$ og $T_{\text{start}}$ i hver sin celle **over** tabellen. Så kan du nøjes med at skrive dem én gang:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | $m$ (kg) | 0,888 | | | |
| 2 | $T_{\text{start}}$ (°C) | 22,0 | | | |
| 3 | | | |$x$ plot |$y$-plot |
| 4 | Målt $T$ (°C) | $E$ (J) | $\Delta T$ (K) | $m \cdot \Delta T$ (kg·K) | $E$ (J) |
| 5 | 22,0 | 0 | `=A5-$B$2` | `=$B$1*C5` | `=B5` |
| 6 | 29,6 | 31600 | `=A6-$B$2` | `=$B$1*C6` | `=B6` |

1. Skriv formlerne i C5, D5 og E5, og træk dem ned.
2. **Dollartegnet `$` låser cellen.** Når du trækker formlen ned, bliver `A5` til `A6`, `A7` … men `$B$2` bliver ved med at pege på $T_{\text{start}}$. Uden `$` ville Excel prøve at trække `B3`, `B4` … fra, og så bliver alt forkert. Du kan skrive `$` selv (dansk tastatur: **⌥ + 4** på Mac, **AltGr + 4** på Windows) eller trykke **⌘ + T** på Mac / **F4** på Windows, mens markøren står i cellereferencen.
3. Kolonne E er bare en kopi af B. Den står der kun, så $x$ og $y$ står ved siden af hinanden.
4. Markér kolonne D og E, lav et **punktdiagram (XY)**, og tilføj en lineær tendenslinje med ligning og $R^2$.

![Tilført energi som funktion af m·ΔT med tendenslinje](/img/linreg/linreg-varmekapacitet.svg)

### Tolkningsskema

Teorien har præcis samme form som regnearkets ligning, når $x = m \cdot \Delta T$:

![Tolkningsskema: E = c · (m·ΔT) + E₀ over y = a·x + b, derfor a = c og b = E₀](/img/linreg/tolkning-varmekapacitet.svg)

| Regneark | Teori | Fysisk betydning | Værdi |
|---|---|---|---|
| $y$ | $E$ | tilført energi (målt) | række af tal |
| $x$ | $m \cdot \Delta T$ | masse gange temperaturstigning (beregnet) | række af tal |
| $a$ | $c$ | vandets varmekapacitet | $4516\ \dfrac{\text{J}}{\text{kg} \cdot \text{K}}$ |
| $b$ | $E_0$ | energi, der er brugt, før vandet begynder at blive varmt | $748\text{ J}$ |

Ifølge teorien skal $b = 0$, for når $\Delta T = 0$, er der ikke tilført energi. Her er $b = 748\text{ J}$. Det er kun ca. $0{,}3\,\%$ af den største energi, så det er småt. Et bud er, at varmelegemet selv skal varmes op, før vandet mærker noget. Sammenlign med densitetsforsøget, hvor $b$ var **måleglassets masse** – her har $b$ en lignende rolle: noget andet end vandet, der også er med i målingen.

### Hvorfor er $c$ for stor?

Tabelværdien for vand er ca. $4180\ \frac{\text{J}}{\text{kg} \cdot \text{K}}$, men vi fik $4516\ \frac{\text{J}}{\text{kg} \cdot \text{K}}$. Det er ca. $8\,\%$ for meget.

> **Opgave 1.** Energimåleren måler al den energi, der går ind i kedlen. Hvad bliver varmet op udover vandet? Hvor bliver resten af energien af? Giv et bud, før du læser videre.

<details>
<summary>Løsning til opgave 1</summary>

**Kedlen selv** bliver også varm: varmelegemet, metalbunden og plastikken. Kedlen har sin egen varmekapacitet $C_{\text{kedel}}$ (i J/K – energi pr. grad for **hele** kedlen). Den rigtige teori er derfor

$$E = m \cdot c \cdot \Delta T + C_{\text{kedel}} \cdot \Delta T = \left(c + \frac{C_{\text{kedel}}}{m}\right) \cdot m \cdot \Delta T$$

Hældningen er altså **ikke** $c$, men $c + \dfrac{C_{\text{kedel}}}{m}$. Den er større end $c$. Bruger vi tabelværdien for vand, kan vi finde kedlens varmekapacitet:

$$C_{\text{kedel}} = (4516 - 4180)\ \tfrac{\text{J}}{\text{kg} \cdot \text{K}} \cdot 0{,}888\text{ kg} \approx 300\ \tfrac{\text{J}}{\text{K}}$$

Derudover går der lidt energi tabt som **varmetab** til luften omkring kedlen – mest når vandet er varmt. Det trækker også hældningen op.

</details>

## Hvorfor ikke bare dividere?

Man kunne jo isolere $c$ i teorien og regne den ud for hver måling for sig:

$$c = \frac{E}{m \cdot \Delta T}$$

Det giver syv forskellige værdier:

| $\Delta T$ (K) | 7,6 | 13,1 | 21,8 | 29,9 | 38,7 | 50,3 | 61,4 |
|---|---|---|---|---|---|---|---|
| $\dfrac{E}{m \cdot \Delta T}$ $\left(\frac{\text{J}}{\text{kg} \cdot \text{K}}\right)$ | 4682 | 4625 | 4566 | 4538 | 4539 | 4525 | 4532 |

![E/(m·ΔT) for hver måling sammenlignet med regressionens hældning og tabelværdien](/img/linreg/linreg-varmekapacitet-division.svg)

Værdierne falder **systematisk**, og de første er meget for store. Det er ikke tilfældigt. Divisionen antager, at linjen går gennem $(0,0)$, altså at $b = 0$. Den lille $b$-værdi på $748\text{ J}$ fylder meget, når $m \cdot \Delta T$ er lille, og næsten intet, når den er stor.

| | Dividere hver måling | Lineær regression |
|---|---|---|
| Resultat | Syv forskellige tal – hvilket er det rigtige? | **Ét** tal for $c$ |
| $b$-værdi (offset) | Giver en systematisk fejl, især for små $x$ | Bliver fanget af $b$ og påvirker ikke hældningen |
| Tilfældige fejl | Hver værdi har sin egen fejl | Udjævnes, fordi alle punkter bruges på én gang |
| Holder modellen? | Svært at se | Ligger punkterne på en ret linje? Se grafen og $R^2$ |
| Fejlmålinger | Gemmer sig i tabellen | Springer i øjnene på grafen |

Regression er altså ikke bare en anden måde at regne det samme ud på. Den **tester teorien** og giver dig samtidig det bedste bud på konstanterne.

## Variabeltransformation

Teorien $E = m \cdot c \cdot \Delta T$ kan afbildes på flere måder. Det er **dig**, der bestemmer, hvad du sætter ud ad $x$-aksen – og dermed hvad hældningen bliver.

| $x$-akse | Hældning $a$ | Skæring $b$ | Kommentar |
|---|---|---|---|
| $T$ | $m \cdot c$ | $-m \cdot c \cdot T_{\text{start}}$ | Lineær, men $b$ er besværlig at tolke |
| $\Delta T$ | $m \cdot c$ | $0$ | Du skal bagefter dividere hældningen med $m$ |
| $m \cdot \Delta T$ | $c$ | $0$ | **Hældningen er direkte $c$** |

Med $x = \Delta T$ ser tolkningsskemaet sådan ud:

![Tolkningsskema: E = (m·c) · ΔT + E₀, derfor a = m·c](/img/linreg/tolkning-varmekapacitet-dT.svg)

Med $x = m \cdot \Delta T$ står $c$ alene som hældning (se skemaet ovenfor). At lave en ny kolonne ud fra de målte tal og bruge den som akse kaldes **variabeltransformation** (eller aksetransformation).

**Opskriften:**

1. Skriv teorien op.
2. Find den konstant, du vil bestemme. Den skal stå **alene** som $a$.
3. Alt det, der ganges på den, og som varierer fra måling til måling, samles i $x$.
4. Lav en ny kolonne i regnearket med $x$ – brug `$` til konstanter som $m$, $g$ og $T_{\text{start}}$.

Samme trick bruges, når sammenhængen slet ikke er lineær, fx $y = k \cdot x^2$ eller $y = k \cdot \sqrt{x}$. Så sætter du $x^2$ eller $\sqrt{x}$ ud ad $x$-aksen. Se terningeeksemplet under [Lineær regression og aksetransformation]({{< relref "/docs/nat/lineaer-regression" >}}).

## Opgave 2 – Gnidningskoefficienten

Du trækker en træklods hen over et bord med et newtonmeter med **lav, konstant fart**. Du lægger lodder oven på klodsen og vejer klods og lodder samlet. Newtonmeteret viser gnidningskraften $F_{\text{gnid}}$. Læs om teorien under [Gnidning]({{< relref "/docs/fysik/emner-b/kraefter/gnidning" >}}).

![Træklods med lodder trækkes med et newtonmeter](/img/linreg/linreg-gnidning-opstilling.svg)

| $m$ (kg) | 0,30 | 0,55 | 0,80 | 1,05 | 1,30 | 1,55 | 1,80 |
|---|---|---|---|---|---|---|---|
| $F_{\text{gnid}}$ (N) | 0,92 | 1,37 | 2,05 | 2,61 | 3,20 | 3,80 | 4,33 |

Teorien for dynamisk gnidning på et vandret bord er

$$F_{\text{gnid}} = \mu \cdot F_N = \mu \cdot m \cdot g$$

> a) Hvad skal du sætte ud ad $x$-aksen, for at hældningen bliver $\mu$? Udfyld et tolkningsskema (husk et $b$-led).
>
> b) Lav kolonnen med $x$-værdierne i regnearket. Skriv $g = 9{,}82\text{ m/s}^2$ i én celle, og brug `$`.
>
> c) Lav grafen, og bestem gnidningskoefficienten $\mu$. Hvilken enhed har den?
>
> d) Hvad er $b$-værdien? Giv et bud på en fysisk tolkning – ifølge teorien burde den være 0.
>
> e) Beregn $\dfrac{F_{\text{gnid}}}{m \cdot g}$ for hver måling. Hvilken måling skiller sig ud, og hvorfor?

<details>
<summary>Hints</summary>

- **a)** Normalkraften er ikke målt direkte. Hvad er $F_N$ på et vandret bord?
- **b)** Formlen i første række kan fx være `=A2*$H$1`, hvis $g$ står i H1.
- **c)** Se på enhederne: hældningen er N divideret med N.
- **d)** Hvad viser newtonmeteret, når der ikke hænger noget i det?
- **e)** Sammenlign med figuren "Divider hver måling for sig" ovenfor.

</details>

<details>
<summary>Løsning til opgave 2</summary>

a) $x = m \cdot g$ (normalkraften $F_N$), og $y = F_{\text{gnid}}$:

![Tolkningsskema for gnidning: F_gnid = μ · (m·g) + F_fejl](/img/linreg/tolkning-gnidning-masse.svg)

b) $m \cdot g$ bliver 2,95 · 5,40 · 7,86 · 10,31 · 12,77 · 15,22 · 17,68 N.

c)

![Gnidningskraft som funktion af m·g med tendenslinje](/img/linreg/linreg-gnidning-masse.svg)

$\mu = 0{,}236$. Den har **ingen enhed**, fordi den er et forhold mellem to kræfter (N/N).

d) $b = 0{,}18\text{ N}$. Det kan være en **systematisk fejl**, fx at newtonmeteret ikke viser 0, når det ikke er belastet – eller at du trækker en lille smule skævt. Læs mere under [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}).

e) $\dfrac{F_{\text{gnid}}}{m \cdot g}$ = 0,312 · 0,254 · 0,261 · 0,253 · 0,251 · 0,250 · 0,245. Den første (letteste klods) er for stor. Det er $b$-værdien igen: $0{,}18\text{ N}$ fylder meget, når gnidningskraften selv er lille. Regressionen giver ét tal, som $b$-leddet ikke forstyrrer.

</details>

## Læs videre

- [Densitet]({{< relref "/docs/fysik/C-Eksp/densitet" >}}) – det første eksempel på $a$ og $b$ med fysisk betydning
- [Varmekapacitet]({{< relref "/docs/fysik/C-Eksp/varmekapacitet" >}}) – forsøget med dypkoger
- [Lineær regression og aksetransformation]({{< relref "/docs/nat/lineaer-regression" >}}) – flere eksempler og Python
- [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}})
