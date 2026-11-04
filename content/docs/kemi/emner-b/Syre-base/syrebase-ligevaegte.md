---
title: "Syrebase-ligevægte"
weight: 1
pdf: "pdfs/syrebase-ligevaegte.pdf"
pdf_ny_fane: true
---

**Niveau: Kemi B** · **Emne: Syrebase-ligevægte**

Du kender allerede ligevægtsloven fra [Ligevægt]({{< relref "ligevaegt" >}}) og [Gasligevægte]({{< relref "gasligevaegte" >}}). Nu bruger vi den på syrer og baser. Det er den samme lov: Kun navnet på konstanten er nyt.

## En syre afgiver en hydron

En **syre** er et stof, der kan afgive en hydron, $\ce{H+}$. En **base** er et stof, der kan optage en hydron. Det kaldes Brønsteds definition.

Når eddikesyre kommer i vand, afgiver molekylerne $\ce{H+}$ til vandet. Men reaktionen går også den anden vej: $\ce{H3O+}$ kan give hydronen tilbage til acetationen. Det er en ligevægt.

![Eddikesyre afgiver en hydron til vand. Der dannes acetat og oxonium, og reaktionen kan gå begge veje.](/img/syrebase/syre-ligevaegt.svg)

- Syren og den base, den bliver til, er et **korresponderende syre-basepar**. De to stoffer er ens, bortset fra én $\ce{H+}$.
- I hver syre-base-reaktion er der to par. Det ene stof afgiver hydronen, og det andet optager den.
- $\ce{H3O+}$ hedder **oxonium**. Nogle gange skriver vi bare $\ce{H+}$, sådan som på siden om ligevægt. Det dækker over det samme.

## Stærk og svag syre

Hvor langt reaktionen når, afhænger af syren.

![To bægre. I bægeret med saltsyre er alle molekyler blevet til ioner. I bægeret med eddikesyre er de fleste molekyler hele.](/img/syrebase/staerk-svag.svg)

- En **stærk syre** afgiver næsten alle sine hydroner. Vi skriver en almindelig pil: $\ce{HCl + H2O -> Cl- + H3O+}$.
- En **svag syre** afgiver kun få hydroner. Ligevægten ligger til venstre, og vi skriver ligevægtspile: $\ce{CH3COOH + H2O <=> CH3COO- + H3O+}$.

Figuren er ikke målfast: I $0{,}10\ \text{M}$ eddikesyre er kun ca. $1\ \%$ af molekylerne på ionform.

## Syrestyrkekonstanten $K_s$

Vi bruger ligevægtsloven på eddikesyre. Produkterne står i tælleren og udgangsstofferne i nævneren:

$$\ce{CH3COOH(aq) + H2O(l) <=> CH3COO-(aq) + H3O+(aq)}$$

Vand er opløsningsmiddel og står derfor ikke i brøken. Der er så meget vand, at dets koncentration næsten ikke ændrer sig. Tilbage står

$$K_s = \frac{[\ce{CH3COO-}] \cdot [\ce{H3O+}]}{[\ce{CH3COOH}]} = 1{,}75 \cdot 10^{-5}\ \text{M} \quad (25\ ^\circ\text{C})$$

For en vilkårlig syre $\ce{HA}$ i vand:

$$\ce{HA + H2O <=> A- + H3O+} \qquad K_s = \frac{[\ce{A-}] \cdot [\ce{H3O+}]}{[\ce{HA}]}$$

$K_s$ er **syrestyrkekonstanten**. Den er bare ligevægtskonstanten for syrens reaktion med vand.

- **Stor $K_s$:** Tælleren er stor, og ligevægten ligger mod højre. Syren er stærk.
- **Lille $K_s$:** Nævneren er stor, og ligevægten ligger mod venstre. Syren er svag.

Tallene er ofte meget små, så vi bruger **styrkeeksponenten**:

$$\text{p}K_s = -\log(K_s)$$

**Eksempel:** For eddikesyre er $\text{p}K_s = -\log(1{,}75 \cdot 10^{-5}) = 4{,}76$. Husk, at lille $\text{p}K_s$ betyder stærk syre.

## Basestyrkekonstanten $K_b$

En base i vand optager en hydron fra vandet. Her er vand altså syren, og der dannes hydroxid, $\ce{OH-}$.

![Ammoniak optager en hydron fra vand. Der dannes ammonium og hydroxid, og reaktionen kan gå begge veje.](/img/syrebase/base-ligevaegt.svg)

Vi bruger ligevægtsloven på samme måde, og vand står igen ikke i brøken:

$$\ce{NH3(aq) + H2O(l) <=> NH4+(aq) + OH-(aq)}$$

$$K_b = \frac{[\ce{NH4+}] \cdot [\ce{OH-}]}{[\ce{NH3}]} = 1{,}8 \cdot 10^{-5}\ \text{M} \quad (25\ ^\circ\text{C})$$

For en vilkårlig base $\ce{B}$ i vand:

$$\ce{B + H2O <=> HB+ + OH-} \qquad K_b = \frac{[\ce{HB+}] \cdot [\ce{OH-}]}{[\ce{B}]} \qquad \text{p}K_b = -\log(K_b)$$

## Sammenhængen mellem $K_s$ og $K_b$

Vand kan både afgive og optage en hydron. Det reagerer derfor med sig selv:

$$\ce{H2O + H2O <=> H3O+ + OH-} \qquad K_v = [\ce{H3O+}] \cdot [\ce{OH-}] = 1{,}0 \cdot 10^{-14}\ \text{M}^2 \quad (25\ ^\circ\text{C})$$

Tag nu syren $\ce{HA}$ og dens korresponderende base $\ce{A-}$. Basen reagerer med vand: $\ce{A- + H2O <=> HA + OH-}$. Ganger vi de to brøker, går $[\ce{A-}]$ og $[\ce{HA}]$ ud:

$$K_s \cdot K_b = \frac{[\ce{A-}] \cdot [\ce{H3O+}]}{[\ce{HA}]} \cdot \frac{[\ce{HA}] \cdot [\ce{OH-}]}{[\ce{A-}]} = [\ce{H3O+}] \cdot [\ce{OH-}] = K_v$$

For et korresponderende syre-basepar ved $25\ ^\circ\text{C}$ gælder altså

$$K_s \cdot K_b = 1{,}0 \cdot 10^{-14}\ \text{M}^2 \qquad \text{p}K_s + \text{p}K_b = 14{,}00$$

Jo stærkere syren er, jo svagere er dens korresponderende base.

| Syre | Korresponderende base | $\text{p}K_s$ | $\text{p}K_b$ |
|---|---|---|---|
| $\ce{HF}$ | $\ce{F-}$ | 3,17 | 10,83 |
| $\ce{CH3COOH}$ | $\ce{CH3COO-}$ | 4,76 | 9,24 |
| $\ce{NH4+}$ | $\ce{NH3}$ | 9,25 | 4,75 |

## Indgreb i en syrebase-ligevægt

Reglerne er de samme som for alle andre ligevægte. Du sætter tallene ind i $Y$ lige efter indgrebet og sammenligner med $K_s$. Husk, at temperaturen er den eneste, der ændrer $K_s$.

**Eksempel:** Du tilsætter natriumacetat til eddikesyre. $[\ce{CH3COO-}]$ stiger, så tælleren bliver større. $K_s < Y$, og ligevægten forskydes mod **venstre**.

Fortynding virker som større volumen for en gas: Ligevægten forskydes mod siden med **flest** opløste partikler.

## Opgaver

**Opgave 1.** Flussyre reagerer med vand: $\ce{HF + H2O <=> F- + H3O+}$.

a) Hvilket stof er syre, og hvilket er base i reaktionen mod højre?

b) Angiv de to korresponderende syre-basepar.

**Opgave 2.** Opskriv udtrykket for:

a) $K_s$ for methansyre: $\ce{HCOOH + H2O <=> HCOO- + H3O+}$

b) $K_b$ for methylamin: $\ce{CH3NH2 + H2O <=> CH3NH3+ + OH-}$

**Opgave 3.** Methansyre har $K_s = 1{,}8 \cdot 10^{-4}\ \text{M}$, og flussyre har $\text{p}K_s = 3{,}17$.

a) Beregn $\text{p}K_s$ for methansyre.

b) Beregn $K_s$ for flussyre.

c) Hvilken af de to syrer er stærkest?

**Opgave 4.** Brug $K_s$ for flussyre fra opgave 3. Beregn $K_b$ og $\text{p}K_b$ for fluoridionen, $\ce{F-}$.

**Opgave 5.** I en methansyreopløsning måler du ved ligevægt $[\ce{HCOOH}] = 0{,}0958\ \text{M}$ og $[\ce{HCOO-}] = [\ce{H3O+}] = 4{,}2 \cdot 10^{-3}\ \text{M}$. Beregn $K_s$. Passer det med opgave 3?

**Opgave 6.** Du har en methansyreopløsning, hvor $[\ce{HCOOH}] \approx 0{,}10\ \text{M}$ ved ligevægt.

a) Forklar, hvorfor $[\ce{HCOO-}] = [\ce{H3O+}]$.

b) Beregn $[\ce{H3O+}]$.

c) Hvor stor en procentdel af syren er på ionform?

**Opgave 7.** Eddikesyre er i ligevægt: $\ce{CH3COOH + H2O <=> CH3COO- + H3O+}$. Hvilken vej forskydes ligevægten, når du

a) fortynder opløsningen 10 gange? Vis det med $Y$.

b) tilsætter lidt natriumhydroxid, så $\ce{OH-}$ fjerner $\ce{H3O+}$?

c) tilsætter lidt saltsyre?

## Hints

**Hint 1.** Hvilket stof mister en $\ce{H+}$? Parrene er stoffer, der kun adskiller sig med én $\ce{H+}$.

**Hint 2.** Produkter i tælleren, udgangsstoffer i nævneren. Vand skal ikke med.

**Hint 3.** $\text{p}K_s = -\log(K_s)$ og $K_s = 10^{-\text{p}K_s}$.

**Hint 4.** $K_s \cdot K_b = 1{,}0 \cdot 10^{-14}\ \text{M}^2$.

**Hint 5.** Sæt de tre koncentrationer ind i udtrykket fra opgave 2a.

**Hint 6.** Kald $[\ce{H3O+}] = x$. Så er $K_s = \dfrac{x^2}{0{,}10\ \text{M}}$. Isolér $x$.

**Hint 7.** Alle tre koncentrationer bliver $\tfrac{1}{10}$ så store i a). I b) og c): Hvad sker der med $[\ce{H3O+}]$?

## Løsninger

**Løsning 1.** a) $\ce{HF}$ er syre, og $\ce{H2O}$ er base.

b) $\ce{HF}/\ce{F-}$ og $\ce{H3O+}/\ce{H2O}$.

**Løsning 2.** a) $K_s = \dfrac{[\ce{HCOO-}] \cdot [\ce{H3O+}]}{[\ce{HCOOH}]}$

b) $K_b = \dfrac{[\ce{CH3NH3+}] \cdot [\ce{OH-}]}{[\ce{CH3NH2}]}$

**Løsning 3.** a) $\text{p}K_s = -\log(1{,}8 \cdot 10^{-4}) = 3{,}74$

b) $K_s = 10^{-3{,}17}\ \text{M} = 6{,}8 \cdot 10^{-4}\ \text{M}$

c) Flussyre er stærkest, fordi den har størst $K_s$ og mindst $\text{p}K_s$.

**Løsning 4.**

$$K_b = \frac{1{,}0 \cdot 10^{-14}\ \text{M}^2}{6{,}8 \cdot 10^{-4}\ \text{M}} = 1{,}5 \cdot 10^{-11}\ \text{M} \qquad \text{p}K_b = 14{,}00 - 3{,}17 = 10{,}83$$

**Løsning 5.**

$$K_s = \frac{(4{,}2 \cdot 10^{-3}\ \text{M})^2}{0{,}0958\ \text{M}} = 1{,}8 \cdot 10^{-4}\ \text{M}$$

Det passer med opgave 3.

**Løsning 6.** a) Hvert molekyle, der afgiver en $\ce{H+}$, danner præcis én $\ce{HCOO-}$ og én $\ce{H3O+}$.

b)

$$x = \sqrt{1{,}8 \cdot 10^{-4}\ \text{M} \cdot 0{,}10\ \text{M}} = 4{,}2 \cdot 10^{-3}\ \text{M}$$

c) $\dfrac{4{,}2 \cdot 10^{-3}\ \text{M}}{0{,}10\ \text{M}} = 0{,}042 = 4{,}2\ \%$

**Løsning 7.** a) Alle koncentrationer bliver $\tfrac{1}{10}$ så store:

$$Y = \frac{\tfrac{1}{10} \cdot \tfrac{1}{10}}{\tfrac{1}{10}} \cdot K_s = \tfrac{1}{10} K_s$$

$K_s > Y$, så ligevægten forskydes mod **højre**.

b) $[\ce{H3O+}]$ falder, så $Y$ bliver mindre. $K_s > Y$, og ligevægten forskydes mod **højre**.

c) $[\ce{H3O+}]$ stiger, så $Y$ bliver større. $K_s < Y$, og ligevægten forskydes mod **venstre**.
