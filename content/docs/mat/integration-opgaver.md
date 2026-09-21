---
title: "Integration-opgaver"
weight: 22
---

**Niveau: Fysik A** · **Emne: Matematik – integration**

Opgaverne hører til siden [Integration i fysik]({{< relref "integration-i-fysik" >}}). Forsøg først selv. Sidder du fast, kan du scrolle ned til **Hints**, og til sidst til **Løsninger**.

Husk de to metoder:

- **Gæt:** Hvilken funktion skal du aflede for at få funktionen i opgaven?
- **Areal:** Integralet er arealet under grafen. Enheden er y-enhed gange x-enhed.
- **Enheder på tallene:** Tallene i funktionerne har enheder, så det hele går op. I $F(x) = 20 \text{ N/m} \cdot x$ er $20$ en fjederkonstant med enheden N/m. Tjek: $\text{N/m} \cdot \text{m} = \text{N}$. ✓

## Opgaver

### Opgave 1 – Cykeltur

Du cykler med den konstante fart $v = 6{,}0$ m/s i $90$ s. Brug integration til at finde, hvor langt du kommer.

### Opgave 2 – Elkedel

En elkedel bruger den konstante effekt $P = 2{,}0$ kW i $3{,}0$ minutter. Energien er integralet af effekten. Find energien i både kJ og kWh.

### Opgave 3 – Bil der speeder op

En bil starter i hvile. Farten stiger, så $v(t) = 1{,}5 \text{ m/s}^2 \cdot t$, hvor $t$ er tiden.

a) Hvor langt kører bilen på de første $8{,}0$ s?

b) Hvad er farten efter $8{,}0$ s? Brug den til at tjekke dit svar fra a) med en trekant.

### Opgave 4 – Elastik

Du strækker en tyk elastik. Kraften er $F(x) = 20 \text{ N/m} \cdot x$, hvor $x$ er strækningen. Hvor meget arbejde udfører du, når du strækker den fra $x = 0$ til $x = 0{,}30$ m?

### Opgave 5 – Løberen (fra et sted til et andet)

En løber accelererer, så farten er $v(t) = 0{,}50 \text{ m/s}^2 \cdot t$, hvor $t$ er tiden. Hvor langt løber hun **mellem $t = 4{,}0$ s og $t = 10{,}0$ s**?

### Opgave 6 – Rulleskøjteløber (fra et sted til et andet)

En ven skubber dig på rulleskøjter. Skubbet aftager, så kraften er $F(t) = 30 \text{ N} - 5{,}0 \text{ N/s} \cdot t$, hvor $t$ er tiden. Vi kigger på tiden **fra $t = 1{,}0$ s til $t = 4{,}0$ s**.

a) Hvor stor er kraftens impuls i det tidsrum?

b) Du og rulleskøjterne vejer $50$ kg. Hvor meget ændres din fart?

### Opgave 7 – Kælk på is (lidt sværere)

Et barn på en kælk står stille på blank is. En ven skubber med en kraft, der vokser hurtigt: $F(t) = 0{,}40 \text{ N/s}^3 \cdot t^3$, hvor $t$ er tiden, fra $t = 0$ til $t = 3{,}0$ s. Barn og kælk vejer $25$ kg.

a) Find kraftens impuls.

b) Find kælkens fart efter $3{,}0$ s.

c) Hvilke antagelser har du lavet her? Nævn mindst én ting, som der ikke er taget højde for i opgaven. 

### Opgave 8 – Gynge (lidt sværere)

Du skubber en gynge. Kraften er $F(t) = 12 \text{ N} \cdot \sin(2{,}0 \text{ s}^{-1} \cdot t)$, hvor $t$ er tiden, fra $t = 0$ til $t = 1{,}57$ s (det er $\pi/2$). Regn med, at skubbet er vandret, og at barn og gynge vejer $30$ kg og starter i hvile.

a) Find kraftens impuls.

b) Find farten lige efter skubbet.

*Tip: Sæt regnemaskinen til radianer.*

### Opgave 9 – Cyklisten i lyskrydset (tæl tern)

Grafen viser en cyklists fart som funktion af tiden. **Hver tern svarer til $1$ s på x-aksen og $1$ m/s på y-aksen.**

![Cyklistens fart v (m/s) som funktion af tiden t (s), tegnet på tern.](/img/integration-opg9.svg)

a) Hvor mange meter svarer én tern til? Vis, at enheden passer.

b) Tæl tern under kurven, og find, hvor langt cyklisten kom på de $10$ s.

### Opgave 10 – Tennisserv (tæl tern)

Grafen viser kraften fra ketsjeren på en tennisbold. **Hver tern svarer til $1$ ms på x-aksen og $100$ N på y-aksen.** Kraften er meget lille efter $12$ ms, så du kan regne med det, der er tegnet.

![Kraften F (N) på tennisbolden som funktion af tiden t (ms), tegnet på tern.](/img/integration-opg10.svg)

a) Hvor stor er kraftens impuls, som én tern svarer til? Husk at omregne ms til s.

b) Tæl tern under kurven, og find kraftens impuls på bolden.

c) Bolden vejer $0{,}057$ kg og var i ro, lige før den blev ramt. Hvor stor er dens fart, når den forlader ketsjeren?

## Hints

### Hint 1
- Hvilken funktion skal du aflede for at få tallet $6{,}0$? Det er $6{,}0 \cdot t$.
- Arealet er et rektangel: højde $6{,}0$ m/s og bredde $90$ s.

### Hint 2
- Energi er integralet af effekt: $E = \int P \, \mathrm{d}t$. Effekten er konstant, så du får $P \cdot t$.
- kJ: Omregn kW til W og minutter til sekunder ($1$ min $= 60$ s).
- kWh: Omregn kun minutter til timer ($1$ time $= 60$ min), og behold kW.
- Tjek: $1 \text{ kWh} = 3600 \text{ kJ}$.

### Hint 3
- a) Gæt en funktion, der giver $1{,}5 \cdot t$ når du afleder. Prøv $t^2$, og se, hvilken faktor du mangler.
- b) Sæt $t = 8{,}0$ ind i $v(t)$. Trekanten har grundlinje $8{,}0$ s og højde lig farten.

### Hint 4
- Arbejde er integralet af kraft over vejen: $A = \int F \, \mathrm{d}x$.
- Gæt en funktion, der giver $20 \cdot x$, når du afleder. Prøv $x^2$, og ret faktoren.
- Tjek: Kraften vokser fra $0$ til $F(0{,}30)$, så arealet er en trekant.

### Hint 5
- Find først en funktion $S(t)$, som giver $0{,}50 \cdot t$, når du afleder.
- Arealet fra $4{,}0$ til $10{,}0$ er $S(10{,}0) - S(4{,}0)$. Det er arealet fra $0$ til $10$ minus arealet fra $0$ til $4$.
- Tjek: Området er en trapez med de to lodrette sider $v(4{,}0)$ og $v(10{,}0)$.

### Hint 6
- a) Find en funktion $S(t)$, som giver $30 - 5{,}0 \cdot t$, når du afleder. Led for led: $30$ giver $30 \cdot t$, og $5{,}0 \cdot t$ giver $2{,}5 \cdot t^2$. Så er kraftens impuls $S(4{,}0) - S(1{,}0)$.
- b) Kraftens impuls er ændringen i bevægelsesmængde: $\Delta p = m \cdot \Delta v$.

### Hint 7
- a) Gæt en funktion, der giver $0{,}40 \text{ N/s}^3 \cdot t^3$, når du afleder. Reglen: læg $1$ til eksponenten ($t^4$), og divider med $4$. Tjek ved at aflede.
- b) Kraftens impuls er $\Delta p = m \cdot \Delta v$. Kælken startede i hvile.
- c) Tænk på gnidning, og om skubbet er vandret.

### Hint 8
- a) Afled $\cos(2{,}0 \cdot t)$: du får $-2{,}0 \cdot \sin(2{,}0 \cdot t)$ (indre funktion $2{,}0 \cdot t$ giver faktoren $2{,}0$). Så skal du gange med $-\dfrac{12}{2{,}0} = -6{,}0$ for at få $12 \cdot \sin(2{,}0 \cdot t)$.
- Stamfunktionen er derfor $-6{,}0 \cdot \cos(2{,}0 \cdot t)$. Sæt grænserne $0$ og $1{,}57$ ind, og træk fra hinanden.
- b) $\Delta p = m \cdot \Delta v$.

### Hint 9
- a) Areal af én tern er $1$ s $\cdot$ $1$ m/s. Hvilken enhed er det?
- b) Tæl først de tern, der er helt under kurven. Tæl derefter de tern, kurven skærer igennem, og regn dem for cirka halve. Læg det sammen.
- Din tælling må gerne afvige lidt fra andres. Til eksamen accepteres et interval.

### Hint 10
- a) Én tern er $1$ ms $\cdot$ $100$ N. Omregn $1$ ms til sekunder, og gang.
- b) Tæl tern som i opgave 9, og gang med det, én tern svarer til.
- c) Bolden startede i ro: $\Delta p = m \cdot v$, så $v = \Delta p / m$.

## Løsninger

### Løsning 1
Gæt: $6{,}0 \cdot t$ (afleder du den, får du $6{,}0$).

$$s = 6{,}0 \text{ m/s} \cdot 90 \text{ s} = 540 \text{ m}$$

Det passer med rektanglet: $6{,}0 \cdot 90 = 540$ m.

### Løsning 2
Effekt konstant, så $E = P \cdot t$.

- I kJ: $P = 2000$ W og $t = 180$ s.

$$E = 2000 \text{ W} \cdot 180 \text{ s} = 360\,000 \text{ J} = 360 \text{ kJ}$$

- I kWh: $t = 3{,}0 \text{ min} = 0{,}050$ h.

$$E = 2{,}0 \text{ kW} \cdot 0{,}050 \text{ h} = 0{,}10 \text{ kWh}$$

Tjek: $360 \text{ kJ} / 3600 \text{ kJ/kWh} = 0{,}10$ kWh. ✓

### Løsning 3
a) Gæt: $\tfrac{1}{2} \cdot 1{,}5 \text{ m/s}^2 \cdot t^2 = 0{,}75 \text{ m/s}^2 \cdot t^2$ (afleder du den, får du $1{,}5 \text{ m/s}^2 \cdot t$).

$$s = 0{,}75 \text{ m/s}^2 \cdot (8{,}0 \text{ s})^2 = 48 \text{ m}$$

Enhed: $\text{m/s}^2 \cdot \text{s}^2 = \text{m}$. ✓

b) $v(8{,}0) = 1{,}5 \cdot 8{,}0 = 12$ m/s. Trekant: $\tfrac{1}{2} \cdot 8{,}0 \text{ s} \cdot 12 \text{ m/s} = 48$ m. ✓

### Løsning 4
Gæt: $\tfrac{1}{2} \cdot 20 \text{ N/m} \cdot x^2 = 10 \text{ N/m} \cdot x^2$.

$$A = 10 \text{ N/m} \cdot (0{,}30 \text{ m})^2 = 0{,}90 \text{ N·m} = 0{,}90 \text{ J}$$

Enhed: $\text{N/m} \cdot \text{m}^2 = \text{N·m} = \text{J}$. ✓

Tjek: $F(0{,}30) = 6{,}0$ N, og trekanten giver $\tfrac{1}{2} \cdot 0{,}30 \text{ m} \cdot 6{,}0 \text{ N} = 0{,}90$ N·m $= 0{,}90$ J. ✓

### Løsning 5
Stamfunktion: $S(t) = 0{,}25 \text{ m/s}^2 \cdot t^2$ (afled: $0{,}50 \text{ m/s}^2 \cdot t$ ✓).

$$s = S(10 \text{ s}) - S(4{,}0 \text{ s}) = 0{,}25 \cdot 100 \text{ m} - 0{,}25 \cdot 16 \text{ m} = 25 \text{ m} - 4{,}0 \text{ m} = 21 \text{ m}$$

Tjek med trapezen: $v(4{,}0) = 2{,}0$ m/s og $v(10{,}0) = 5{,}0$ m/s.

$$\tfrac{1}{2} \cdot (2{,}0 + 5{,}0) \cdot 6{,}0 = 21 \text{ m} \quad ✓$$

### Løsning 6
a) Stamfunktion: $S(t) = 30 \text{ N} \cdot t - 2{,}5 \text{ N/s} \cdot t^2$.

$$\Delta p = S(4{,}0) - S(1{,}0) = (120 - 40) - (30 - 2{,}5) = 80 - 27{,}5 = 52{,}5 \text{ N·s}$$

Tjek med trapezen: $F(1{,}0) = 25$ N og $F(4{,}0) = 10$ N, så $\tfrac{1}{2} \cdot (25 + 10) \cdot 3{,}0 = 52{,}5$ N·s. ✓

b) $\Delta v = \dfrac{\Delta p}{m} = \dfrac{52{,}5 \text{ N·s}}{50 \text{ kg}} = 1{,}05 \text{ m/s} \approx 1{,}1 \text{ m/s}$

### Løsning 7
a) Stamfunktion: $S(t) = 0{,}10 \text{ N/s}^3 \cdot t^4$ (afled: $0{,}40 \text{ N/s}^3 \cdot t^3$ ✓).

$$\Delta p = 0{,}10 \text{ N/s}^3 \cdot (3{,}0 \text{ s})^4 = 0{,}10 \cdot 81 \text{ N·s} = 8{,}1 \text{ N·s}$$

b) $\Delta v = \dfrac{8{,}1 \text{ N·s}}{25 \text{ kg}} = 0{,}32 \text{ m/s}$

c) Der er regnet som om:
- Der er ingen gnidning mellem kælken og isen (blank is er en god tilnærmelse, men ikke perfekt).
- Skubbet er vandret, så hele kraften går til at flytte kælken fremad.
- Kraften følger formlen $0{,}40 \cdot t^3$ hele vejen, selv om et rigtigt skub ikke er så regelmæssigt.

### Løsning 8
a) Stamfunktion: $S(t) = -6{,}0 \text{ N·s} \cdot \cos(2{,}0 \text{ s}^{-1} \cdot t)$ (afled: $-6{,}0 \text{ N·s} \cdot (-\sin(2{,}0 \text{ s}^{-1} t)) \cdot 2{,}0 \text{ s}^{-1} = 12 \text{ N} \cdot \sin(2{,}0 \text{ s}^{-1} t)$ ✓).

$$\Delta p = S(1{,}57) - S(0) = -6{,}0 \cdot \cos(3{,}14) - \left(-6{,}0 \cdot \cos 0\right) = 6{,}0 + 6{,}0 = 12 \text{ N·s}$$

b) $\Delta v = \dfrac{12 \text{ N·s}}{30 \text{ kg}} = 0{,}40 \text{ m/s}$

Tjek: Rektanglet med højde $12$ N og bredde $1{,}57$ s har arealet $18{,}8$ N·s. Arealet under sinuskurven er cirka $64\,\%$ af det ($2/\pi$), altså cirka $12$ N·s. ✓

### Løsning 9
a) $1 \text{ tern} = 1 \text{ s} \cdot 1 \text{ m/s} = 1 \text{ m}$. Enheden er $\text{s} \cdot \text{m/s} = \text{m}$. ✓

b) Cirka $12$ hele tern og cirka $18$ tern, som kurven går igennem. De $18$ regnes for cirka halve:

$$12 + \tfrac{1}{2} \cdot 18 = 21 \text{ tern} \approx 21 \text{ m}$$

Den nøjagtige værdi (beregnet med en computer) er $19{,}5$ m. Svar mellem cirka $18$ m og $22$ m er gode. Cyklisten kom altså cirka $20$ m.

### Løsning 10
a) $1 \text{ tern} = 1 \text{ ms} \cdot 100 \text{ N} = 0{,}001 \text{ s} \cdot 100 \text{ N} = 0{,}10 \text{ N·s}$.

b) Cirka $17$ hele tern og cirka $22$ tern, som kurven går igennem:

$$17 + \tfrac{1}{2} \cdot 22 = 28 \text{ tern} \Rightarrow \Delta p = 28 \cdot 0{,}10 \text{ N·s} = 2{,}8 \text{ N·s}$$

Den nøjagtige værdi (beregnet) er $2{,}80$ N·s. Svar mellem $2{,}6$ og $3{,}0$ N·s er gode.

c) $v = \dfrac{\Delta p}{m} = \dfrac{2{,}8 \text{ N·s}}{0{,}057 \text{ kg}} = 49 \text{ m/s} \approx 180 \text{ km/h}$

Svar mellem cirka $46$ og $53$ m/s er gode.
