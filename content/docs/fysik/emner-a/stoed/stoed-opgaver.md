---
title: "Opgaver: bevægelsesmængde og kraftens impuls"
weight: 4
---

**Niveau: Fysik A** · **Emne: Bevægelsesmængde $p$ og kraftens impuls $\Delta p$**

Opgaverne hører til siden [Stød og bevægelsesmængde]({{< relref "stoed-bevaegelsesmaengde" >}}).
Forsøg først selv. Scroll derefter ned til **Hints**, hvis du sidder fast, og til
sidst til **Løsninger**.

Husk: $p = m \cdot v$ (kg·m/s) og kraftens impuls $\Delta p = F \cdot \Delta t$ (N·s).
Ved en kraft, der ændrer sig med tiden, gælder $F(t) = \dfrac{\mathrm{d}p}{\mathrm{d}t}$
og $\Delta p = \displaystyle\int_{t_1}^{t_2} F(t)\,\mathrm{d}t$.

## Opgaver

### Opgave 1 – Bevægelsesmængde

En cyklist og cyklen vejer tilsammen $92$ kg. Cyklisten kører med $18$ km/h.
Bestem bevægelsesmængden $p$.

### Opgave 2 – Kraftens impuls

En modelraketmotor yder en konstant kraft på $12$ N i $1{,}8$ s.
Bestem kraftens impuls $\Delta p$.

### Opgave 3 – Kraften ud fra $p(t)$ (differentiér)

En bil på $1200$ kg accelererer fra hvile. De første sekunder er bilens
bevægelsesmængde givet ved

$$p(t) = 3000 \cdot t + 150 \cdot t^2$$

hvor $p$ er i kg·m/s og $t$ i sekunder.

a) Bestem en funktion for kraften $F(t)$ på bilen.

b) Bestem kraften efter $t = 4{,}0$ s.

### Opgave 4 – Bremsning på cykel (differentiér)

En cyklist og cykel på $92$ kg kører med $5{,}0$ m/s og bremser. Under
bremsningen er bevægelsesmængden givet ved

$$p(t) = 460 - 40 \cdot t - 2{,}0 \cdot t^2$$

hvor $p$ er i kg·m/s og $t$ i sekunder.

a) Bestem $F(t)$.

b) Bestem kraften efter $t = 2{,}0$ s.

c) Hvad fortæller fortegnet på kraften?

### Opgave 5 – Indkøbsvogn (integrér)

Du skubber en indkøbsvogn på $15$ kg, som starter i hvile. Du skubber
mindre og mindre hårdt, så kraften i de første $5{,}0$ s er

$$F(t) = 20 - 4{,}0 \cdot t$$

hvor $F$ er i N og $t$ i sekunder.

a) Bestem kraftens impuls $\Delta p$ i tidsrummet $0$ til $5{,}0$ s.

b) Bestem vognens fart efter $5{,}0$ s.

### Opgave 6 – Spark til en fodbold (integrér)

En fodbold på $0{,}43$ kg ligger stille. Under et spark vokser kraften jævnt fra
nul, og sparket varer $0{,}010$ s:

$$F(t) = 1{,}5 \cdot 10^5 \cdot t \qquad \text{for } 0 \le t \le 0{,}010 \text{ s}$$

hvor $F$ er i N og $t$ i sekunder.

a) Bestem kraftens impuls $\Delta p$.

b) Bestem boldens fart efter sparket.

c) Bestem den gennemsnitlige kraft, og sammenlign med den maksimale kraft.

## Hints

### Hint 1
- Farten skal være i m/s, før du bruger $p = m \cdot v$.
- Omregn: $1\ \text{m/s} = 3{,}6\ \text{km/h}$, så divider med $3{,}6$.

### Hint 2
- Kraften er konstant, så du kan bruge $\Delta p = F \cdot \Delta t$ direkte.
- Enheden bliver N·s.

### Hint 3
- Kraften er den afledede af bevægelsesmængden: $F(t) = \dfrac{\mathrm{d}p}{\mathrm{d}t}$.
- Differentiér led for led: leddet $a \cdot t^n$ bliver til $n \cdot a \cdot t^{n-1}$.
- I b) sætter du bare $t = 4{,}0$ ind i din funktion.

### Hint 4
- Samme metode som i opgave 3: konstanten $460$ forsvinder, når du differentierer.
- I c) skal du tænke på, hvilken retning "fremad" er, og om bevægelsesmængden vokser eller aftager.

### Hint 5
- Kraftens impuls er arealet under $F$-$t$-grafen: $\Delta p = \displaystyle\int_0^{5{,}0} F(t)\,\mathrm{d}t$.
- Find en stamfunktion led for led: stamfunktionen til en konstant $a$ er $a \cdot t$, og til $b \cdot t$ er den $\tfrac{1}{2} b \cdot t^2$.
- Vognen starter i hvile, så $\Delta p = m \cdot v$ og dermed $v = \Delta p / m$.

### Hint 6
- Integrér fra $0$ til $0{,}010$ s. Stamfunktionen til $k \cdot t$ er $\tfrac{1}{2} k \cdot t^2$.
- Bolden starter i hvile, så $v = \Delta p / m$.
- Gennemsnitskraften er $F_{\text{gns}} = \Delta p / \Delta t$. Den maksimale kraft finder du ved at sætte $t = 0{,}010$ s ind i $F(t)$.

## Løsninger

### Løsning 1
$v = 18 / 3{,}6 = 5{,}0$ m/s

$$p = m \cdot v = 92 \text{ kg} \cdot 5{,}0 \text{ m/s} = 4{,}6 \cdot 10^2 \text{ kg·m/s}$$

### Løsning 2
$$\Delta p = F \cdot \Delta t = 12 \text{ N} \cdot 1{,}8 \text{ s} = 22 \text{ N·s}$$

(21,6 N·s, afrundet til to betydende cifre.)

### Løsning 3
a) $$F(t) = \frac{\mathrm{d}p}{\mathrm{d}t} = 3000 + 300 \cdot t$$
med $F$ i N.

b) $$F(4{,}0) = 3000 + 300 \cdot 4{,}0 = 4200 \text{ N}$$

### Løsning 4
a) $$F(t) = \frac{\mathrm{d}p}{\mathrm{d}t} = -40 - 4{,}0 \cdot t$$
med $F$ i N.

b) $$F(2{,}0) = -40 - 4{,}0 \cdot 2{,}0 = -48 \text{ N}$$

c) Kraften er negativ, altså rettet mod kørselsretningen. Bevægelsesmængden
aftager, og cyklisten bremser. Kraften bliver kraftigere, jo længere
bremsningen varer.

### Løsning 5
a) $$\Delta p = \int_0^{5{,}0} (20 - 4{,}0 \cdot t)\,\mathrm{d}t = \Big[\,20 \cdot t - 2{,}0 \cdot t^2\,\Big]_0^{5{,}0} = 100 - 50 = 50 \text{ N·s}$$

b) $$v = \frac{\Delta p}{m} = \frac{50 \text{ N·s}}{15 \text{ kg}} = 3{,}3 \text{ m/s}$$

Kontrol: $F(5{,}0) = 0$, så kraften er positiv i hele tidsrummet, og vognen
accelererer hele tiden.

### Løsning 6
a) $$\Delta p = \int_0^{0{,}010} 1{,}5 \cdot 10^5 \cdot t\,\mathrm{d}t = \Big[\,7{,}5 \cdot 10^4 \cdot t^2\,\Big]_0^{0{,}010} = 7{,}5 \text{ N·s}$$

b) $$v = \frac{\Delta p}{m} = \frac{7{,}5 \text{ N·s}}{0{,}43 \text{ kg}} = 17 \text{ m/s} \approx 63 \text{ km/h}$$

c) $$F_{\text{gns}} = \frac{\Delta p}{\Delta t} = \frac{7{,}5 \text{ N·s}}{0{,}010 \text{ s}} = 750 \text{ N}$$

Den maksimale kraft er $F(0{,}010) = 1{,}5 \cdot 10^5 \cdot 0{,}010 = 1500$ N, altså
det dobbelte. Det passer med, at kraften vokser lineært fra nul, så gennemsnittet
er halvdelen af maksimum.
