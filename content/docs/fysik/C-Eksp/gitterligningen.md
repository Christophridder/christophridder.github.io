---
title: "Gitterligningen"
weight: 130
---
**Niveau:** Fysik C · **Emne:** Lys og bølger

---

## Introduktion

Et **optisk gitter** er en plade med tusindvis af fine, parallelle ridser. Når
laserlys sendes gennem gitteret, bøjes lyset af og danner en række lyse prikker på
en skærm bagved — en i midten (0. orden) og symmetriske prikker på hver side
(1. orden, 2. orden osv.). Sammenhængen mellem prikkernes placering, lysets
bølgelængde og gitterets finhed beskrives af **gitterligningen**:

$$d \cdot \sin(\theta) = n \cdot \lambda$$

### De fire variabler

| Symbol | Betydning |
|--------|-----------|
| $d$ | afstanden mellem to gitterspalter (gitterkonstanten), målt i $\text{m}$ |
| $\theta$ | vinklen mellem 0. ordens strålen og den $n$'te stråle |
| $n$ | ordenen — den midterste plet er 0. orden, så 1., 2. osv. |
| $\lambda$ | bølgelængden af laserlyset, målt i $\text{m}$ |

![Opstilling med laser, gitter og skærm](/images/gitter-opstilling.png)

### Hvordan finder man vinklen θ?

$\theta$ er vinklen mellem 0. orden og 1. ordens stråle (for $n=1$), mellem 0. og
2. orden (for $n=2$) osv. Måler man afstanden $x$ fra 0. orden ud til den $n$'te
prik på skærmen, og afstanden $a$ fra gitteret til skærmen, kan vinklen findes med
tangens:

$$\tan(\theta) = \frac{x}{a} \quad\Rightarrow\quad \theta = \arctan\!\left(\frac{x}{a}\right)$$

### Hvordan finder man gitterkonstanten d?

Hvis et gitter har fx $600$ streger pr. $\text{mm}$, er afstanden mellem to streger:

$$d = \frac{1\text{ mm}}{600} = \frac{1 \cdot 10^{-3}\text{ m}}{600} \approx 1{,}6 \cdot 10^{-6}\text{ m}$$

---

## 1) Undersøg gitteret (kvalitativt)

Byg en opstilling, hvor laser, gitter og skærm er spændt fast. Diskutér
variabelkontrol, og identificér de fire variabler $d$, $\theta$, $n$ og $\lambda$.

Ved kun at kigge på 0. og 1. ordens prikken holder du $n$ konstant. Undersøg nu
følgende sammenhænge **kvalitativt**, og forklar resultaterne ud fra
gitterligningen:

| Hvis du ændrer … | … hvad sker der så med $\theta$? |
|------|------|
| $a$ bliver større (gitter længere fra skærm) | ? |
| $\lambda$ bliver større (skift laserfarve) | ? |
| $d$ bliver større (færre streger pr. mm) | ? |

Forklar for hver: bliver vinklen større, mindre eller forbliver den konstant — og
hvorfor følger det af $d \cdot \sin(\theta) = n \cdot \lambda$?

---

## 2) Opgave: Maksimalt antal prikker

Beregn det maksimale antal prikker (afbøjninger), det er muligt at se med skolens
røde laserpointer ($\lambda = 632\text{ nm}$) for gitre med hhv. $100$, $300$ og
$600$ streger pr. $\text{mm}$.

> *Hint: Lyset kan højst bøjes $90^\circ$, så sæt $\theta = 90^\circ$ (altså
> $\sin(\theta) = 1$) i gitterligningen, og find det største heltal $n$, der
> stadig kan lade sig gøre.*

| Gitter | Max prikker (teoretisk) |
|------|------|
| 100 streger pr. mm | |
| 300 streger pr. mm | |
| 600 streger pr. mm | |

---

## 3) Eftervisning af gitterligningen

For at eftervise ligningen bestemmer du afbøjningen for **5 ordener** (prikker).
Idéen er at skrive gitterligningen om, så den får form som en ret linje. Ganger vi
$d \cdot \sin(\theta) = n \cdot \lambda$ ud, ser vi:

$$d \cdot \sin(\theta) = \lambda \cdot n$$

Plotter du altså $d \cdot \sin(\theta)$ op ad $y$-aksen og ordenen $n$ ud ad
$x$-aksen, bliver det en ret linje gennem origo, og **hældningen er lige præcis
bølgelængden** $\lambda$.

**Sådan bygger du regnearket:**

1. Mål afstanden $a$ fra gitter til skærm og skriv den i cellen **C9** 
2. Skriv også gitterkonstanten $d$ fx i cellen C8, fx for et gitter med 300 streger
   pr. mm: $d = \dfrac{1}{300000}\text{ m}$
3. Lav en kolonne med ordenen $n$ (1, 2, 3, 4, 5) start i **E3**
4. Mål afstanden $x$ fra 0. orden ud til den $n$'te prik, både til højre $x_{xr}$ og til venstre $x_{xl}$
   brug gennemsnittet (`=MIDDEL(...)`) som du beregner i kolonne **C**
5. Beregn nu vinkln i kolonne **D**: $\theta = \arctan\left(\dfrac{x}{a}\right)$,
   i Excel `=ARCTAN(x/a)` eller `=ATAN(x/a)` hvis du har en engelsk version.
6. Beregn $y_{plot}$-værdien $d \cdot \sin(\theta)$ i en sidste kolonne, i Excel
   `=d*SIN(theta)`.
7. Plot $x_{plot}$ som x-akse og $y_{plot}$ som y-akse. $d \cdot \sin(\theta)$ mod $n$ i et **Punkt (XY)**-diagram — *ikke* søjle
   eller linje. Læg en lineær tendenslinje ind gennem origo, og aflæs hældningen:
   det er bølgelængden $\lambda$.

||A|B|C|D|E|F|
|---|---|---|---|---|---|---|
|1|||||x-plot|y-plot|
|2|$x_{1r}$|$x_{1l}$|$x_{middel}$|$\theta$|n|$d\cdot sin(\theta)$|
|3|||||1||
|4|||||2||
|5|||||3||
|6|||||4||
|7|||||5||
|8|$d=$|...|||||
|9|$a=$|...|||||
> **Excel-hint:** Bølgelængden er et meget lille tal (omkring $6 \cdot 10^{-7}$ m),
> så tendenslinjens mærkat viser ofte bare $0$. Højreklik på mærkatet →
> **Formatér mærkat** → **Tal** → kategori **Tal** → sæt antal decimaler til
> **12**. Så kan du aflæse hældningen og dermed $\lambda$.

---

## 4) En CD som optisk gitter

Sporene på en CD ligger så tæt, at den kan virke som et gitter. Er der mørkt i
lokalet, kan I se linjerne, når I lyser igennem den.

- Prøv at sende laserlys gennem CD'en  hvis det er mørkt i lokalet, eller brug den som spejl: lys næsten
  vinkelret ind, så lyset kastes tilbage og danner et mønster. 
- Mål afstanden fra CD til skærm og afstandene fra 0. orden til de øvrige ordener.
- Bestem gitterkonstanten $d$ — altså hvor tæt sporene ligger.

> Der er forskel på **CD** og **DVD** — prøv gerne begge, og find $d$ for hver.

---

## 5) Find laserens eksakte bølgelængde

Tag en blå, en rød og en grøn laser, og bestem den **eksakte** bølgelængde for
hver. Det er præcis samme metode som i del 3 — hældningen på
$d \cdot \sin(\theta)$-mod-$n$-grafen *er* bølgelængden. Lav bare et plot for hver
laserfarve, og aflæs de tre hældninger (husk 12 decimaler på mærkatet).

$$\lambda_{\text{blå}} = \underline{\hspace{2cm}}\text{ nm} \qquad \lambda_{\text{rød}} = \underline{\hspace{2cm}}\text{ nm} \qquad \lambda_{\text{grøn}} = \underline{\hspace{2cm}}\text{ nm}$$

---

## Afrapportering

- Den udfyldte kvalitative tabel fra del 1 med forklaringer.
- Beregningerne af max antal prikker (del 2).
- Eftervisningen af gitterligningen med graf og bestemt bølgelængde (del 3).
- Resultater fra CD-gitteret (del 4) og de eksakte bølgelængder (del 5), hvis I når
  dem.
