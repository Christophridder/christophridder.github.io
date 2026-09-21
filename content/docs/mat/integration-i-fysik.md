---
title: "Integration i fysik"
weight: 21
pdf: "pdfs/integration-i-fysik.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Matematik – integration i fysik**
 

Denne side viser, hvordan du integrerer i fysik. Du skal bruge to ting: at **gætte** en funktion og at **tegne et areal**.

## 1. Hvad er integration?

2 måder man kan integrere på:

- **Differentiation baglæns:** Du spørger: *Hvilken funktion skal jeg aflede for at få den her funktion?* Så har du "Integralfunktionen" og kan bruge den til at beregne integralet. 
- **Areal under grafen:** Integralet af en funktion er arealet mellem grafen og x-aksen. Her skal du aflæse arealet eller beregne det på et eller anden måde. Følg med her for mer :) 

For at finde **kraftens impuls** $\Delta p$  skal du finde arealet under funktionen $F(t)$ på $y-$aksen og $t$ på $x-$aksen. 
Det skrives på denne her måde med integraltegnet. 

$$\Delta p = \int_0^T F \, \mathrm{d}t$$

- $\mathrm{d}t$ er et meget lille tidsstykke.
- $F \cdot \mathrm{d}t$ er et smalt rektangel (højde $F$, bredde $\mathrm{d}t$).
- $\int$ betyder: læg alle de smalle rektangler sammen. Det giver **arealet** under $F$-$t$-grafen.

## 2. Gæt-metoden
Integralregning er det *omvendte* af differentialregning. Det er derfor denne her *gætte metode* er så god. 
Du har en funktion $f(x) = x + 3$ fx. For at finde integralet, lad os kalde det $F(x)$ skal du finde den funktion som afledt giver $f(x)$. 

1. Gæt en funktion.
2. **Afled** dit gæt.
3. Passer det ikke, så ret gættet, og afled igen.

**Eksempel: Hvad skal du aflede for at få $x + 3$?**

- Gæt: $f(x) = x^2$. 
- Afled: $(x^2)' = 2x$. Det er en faktor $2$ for meget og vi mangler $+3$. 
- Ret: vi prøver med $f(x)=\tfrac{1}{2}x^2+3x$. Så er $\left(\tfrac{1}{2} x^2 + 3x\right)' = x + 3$. ✓

Det er derfor, der står $\tfrac{1}{2}$ i så mange formler, fx i stedfunktionen $s(t) = \tfrac{1}{2} a t^2$ og energien i en fjeder $E(x) = \tfrac{1}{2} k x^2$.

| Du skal integrere | Første gæt | Afled gættet | Ret gættet til |
|---|---|---|---|
| $f(t) = 6$ | $6 \cdot t$ | $6$ ✓ | $6 \cdot t$ |
| $f(t) = t$ | $t^2$ | $2t$ (for meget: faktor 2) | $\tfrac{1}{2} t^2$ |
| $f(t)=t^2$ | $t^3$ | $3t^2$ (faktor 3 for meget) | $\tfrac{1}{3} t^3$ |
| $f(t)=t^3$ | $t^4$ | $4t^3$ (faktor 4 for meget) | $\tfrac{1}{4} t^4$ |
| $f(t) = a \cdot t$ | $t^2$ | $2t$ | $\tfrac{1}{2} a t^2$ |

Så vi kan lave én regel:

> **Regel:** Læg $1$ til eksponenten, og divider med den nye eksponent. $t^n$ bliver til $\dfrac{t^{n+1}}{n+1}$.

Tjek altid ved at aflede dit resultat. Får du det, du startede med, er du færdig.


## 3. Areal og enhed

Arealet under en graf har enheden **y-enhed gange x-enhed**. Det er sådan, du finder enheden på en integreret størrelse:

| y-akse | x-akse |Integral| Arealet er | Enhed |
|---|---|---|---|---|
| $F$ (N) | $t$ (s) |$\Delta p = \int Fdt$| kraftens impuls $\Delta p$ | N·s (= kg·m/s) |
| $v$ (m/s) | $t$ (s) |$s=\int v dt$| strækning $s$ | m/s · s = m |
| $F$ (N) | $s$ eller $x$ (m) |$A=\int F ds$| arbejde $A$ | N·m = J |
| $P$ (W) | $t$ (s) |$E=\int P dt$| energi $E$ | W·s = J |
| $I$ (A) | $t$ (s) |$Q=\int I dt$| ladning $Q$ | A·s = C |

## 4. Startværdien, den konstant som forsvinder når du differentierer

Et integral giver kun **ændringen**. Vil du have hele funktionen, skal du lægge startværdien til. Det er fordi en konstant giver $0$, når du afleder:

$$s(t) = \tfrac{1}{2} a t^2 + v_0 \cdot t + s_0$$

- $\tfrac{1}{2} a t^2$ kommer fra integration af $a \cdot t$.
- $v_0 \cdot t$ kommer fra integration af den konstante startfart $v_0$.
- $s_0$ er startstedet.

$$v(t) = at + v_0$$
Integrerer du denne funktion for at finde s skal du huske at lægge $s_0$ til **efter** integrationen
$$s = \int v(t) dt = \int at + v_0 dt =  \tfrac{1}{2}at^2 + v_0 t + s_0$$

---

## Eksempel 1 – Kraftens impuls (konstant kraft)

Vi har en bevægelse hvor der udøves en konstant kraft $F = 6{,}0$ N i tiden $4{,}0$ s. Hvad er kraftens impuls $\Delta p$?
Vi ved at kraftens impuls er integralet over kraften som funktion af t. 
$$\Delta p = \int F dt$$
Kraften er konstant $F = 6N$

$$\Delta p = \int 6 dt$$

- **Gæt:** Hvilken funktion giver $6{,}0$, når du afleder? Svaret er $6{,}0 \cdot t$.
- **Areal:** Grafen er en vandret linje, så arealet er et **rektangel**: højde gange bredde.

$$\Delta p = F \cdot \Delta t = 6{,}0 \text{ N} \cdot 4{,}0 \text{ s} = 24 \text{ N·s}$$

![Kraften er konstant 6,0 N i 4,0 s. Arealet under grafen er kraftens impuls 24 N·s.](/img/integration-1-impuls.svg)

**Enhed:** N · s. Det er det samme som kg·m/s, fordi $1 \text{ N} = 1 \text{ kg·m/s}^2$.

## Eksempel 2 – Strækning fra hastighed

En bil starter i hvile og accelererer med $a = 2{,}0$ m/s². Hastigheden er $v = a \cdot t$. Hvor langt er den kørt efter $5{,}0$ s?

- **Gæt:** Hvilken funktion skal du aflede for at få $a \cdot t$? Gæt $t^2$, og afled: $2t$. Så skal du gange med $\tfrac{1}{2}$.
- **Resultat:** $s = \tfrac{1}{2} a t^2$.

$$s = \tfrac{1}{2} \cdot 2{,}0 \text{ m/s}^2 \cdot (5{,}0 \text{ s})^2 = 25 \text{ m}$$

- **Areal:** Grafen er en skrå linje, så arealet er en **trekant**: $\tfrac{1}{2} \cdot \text{grundlinje} \cdot \text{højde}$. Det er her, $\tfrac{1}{2}$ kommer fra.
- **strækningen** bilen har kørt er dermed lig med **arealet** under en $v(t)$ graf over den tid som bilen har kørt. 

![v som funktion af t. Arealet under den skrå linje er strækningen 25 m.](/img/integration-2-straekning.svg)

**Enhed:** for arealet, altså den blå del af ovenstående figur er: $\text{m/s} \cdot \text{s} = \text{m}$.

## Eksempel 3 – Fjederenergi

En fjeder har fjederkonstanten $k = 50$ N/m. Kraften er $F = k \cdot x$. Hvor meget energi er der i fjederen, når den er trukket $x = 0{,}20$ m?

- **Gæt:** Hvilken funktion skal du aflede for at få $k \cdot x$? Det er samme problem som i Eksempel 2: $\tfrac{1}{2} k x^2$.
- **Resultat:** $E = \tfrac{1}{2} k x^2$.

$$E = \tfrac{1}{2} \cdot 50 \text{ N/m} \cdot (0{,}20 \text{ m})^2 = 1{,}0 \text{ J}$$

- **Areal:** Kraften vokser lineært fra $0$ til $k \cdot x = 10$ N, så arealet er en trekant.

![F som funktion af x for en fjeder. Arealet under grafen er fjederenergien 1,0 J.](/img/integration-3-fjeder.svg)

**Enhed:** $\text{N} \cdot \text{m} = \text{J}$.

> **Model:** Det forudsætter en ideel fjeder, hvor $F = k \cdot x$ gælder hele vejen (Hookes lov). Trækkes fjederen for langt, er kraften ikke længere lineær.

## Eksempel 4 – Kinetisk energi
(dette eksempel er lidt svært spring over hvis ikke du kan lide algebra)

Hvor kommer $E_{\text{kin}} = \tfrac{1}{2} m v^2$ fra?

- Arbejdet er $A = \int F \, \mathrm{d}s$, og Newtons 2. lov giver $F = m \cdot \dfrac{\mathrm{d}v}{\mathrm{d}t}$.
- I et lille stykke $\mathrm{d}s$ er $\mathrm{d}s = v \cdot \mathrm{d}t$. Det giver:

$$F \cdot \mathrm{d}s = m \cdot \frac{\mathrm{d}v}{\mathrm{d}t} \cdot v \cdot \mathrm{d}t = m \cdot v \cdot \mathrm{d}v$$

- Vi skal altså integrere $m \cdot v$ over $v$: $E_{\text{kin}} = \int m \cdot v \, \mathrm{d}v$.
- **Gæt:** Hvilken funktion skal du aflede for at få $m \cdot v$? Gæt $m \cdot v^2$, og afled: $2 m v$. Gang med $\tfrac{1}{2}$: $\tfrac{1}{2} m v^2$. ✓

**Regneeksempel:** En bil på $m = 1200$ kg kører $v = 20$ m/s.

$$E_{\text{kin}} = \tfrac{1}{2} \cdot 1200 \text{ kg} \cdot (20 \text{ m/s})^2 = 2{,}4 \cdot 10^5 \text{ J} = 240 \text{ kJ}$$

- **Areal:** Tegn $m \cdot v$ (bevægelsesmængden $p$) op ad y-aksen og $v$ ad x-aksen. Grafen er en ret linje gennem $(0,0)$, og arealet er en trekant.

![Bevægelsesmængden m·v som funktion af v for en bil på 1200 kg. Arealet under grafen er den kinetiske energi 240 kJ.](/img/integration-4-ekin.svg)

**Enhed:** $\dfrac{\text{kg·m}}{\text{s}} \cdot \dfrac{\text{m}}{\text{s}} = \dfrac{\text{kg·m}^2}{\text{s}^2} = \text{J}$.

> **Model:** Det forudsætter konstant masse og hastigheder, der er meget mindre end lysets fart. Ved farter tæt på $c$ virker formlen ikke.

## Eksempel 5 – Potentiel energi og effekt

### 5a) Potentiel energi

En bold på $m = 2{,}0$ kg løftes $h = 3{,}0$ m. Kraften, der skal løfte den, er tyngdekraften $m \cdot g$ (konstant).

- **Gæt:** Hvilken funktion giver konstanten $m \cdot g$, når du afleder? Det er $m \cdot g \cdot h$.
- **Areal:** Rektangel med højde $m \cdot g$ og bredde $h$.

$$E_{\text{pot}} = m \cdot g \cdot h = 2{,}0 \text{ kg} \cdot 9{,}8 \text{ m/s}^2 \cdot 3{,}0 \text{ m} = 58{,}8 \text{ J}$$

![Kraften m·g som funktion af højden h. Arealet under grafen er den potentielle energi 58,8 J.](/img/integration-5a-epot.svg)

**Enhed:** $\text{N} \cdot \text{m} = \text{J}$.

### 5b) Energi fra effekt

En elbil øger sin effekt jævnt fra $0$ til $60$ kW på $10$ s. Hvor meget energi bruger den?

- **Energi er integralet af effekt:** $E = \int P \, \mathrm{d}t$.
- **Areal:** Trekant, $\tfrac{1}{2} \cdot 10 \text{ s} \cdot 60 \text{ kW} = 300 \text{ kW·s}$.

![Effekten P som funktion af tiden t. Arealet under grafen er energien 300 kJ, det vil sige 0,083 kWh.](/img/integration-5b-effekt.svg)

**Enhed:** $\text{kW} \cdot \text{s} = \text{kJ}$. Så er energien $300$ kJ.

Elregningen bruger kWh, og $1 \text{ kWh} = 3600 \text{ kJ} = 3{,}6 \text{ MJ}$:

$$\frac{300 \text{ kJ}}{3600 \text{ kJ/kWh}} = 0{,}083 \text{ kWh}$$

> **Model:** Det er en forenklet model, hvor effekten vokser lineært. En rigtig elbil har en mere kompliceret effektkurve, men princippet med areal under $P$-$t$-grafen er det samme.

## Eksempel 6 – Ladning fra strøm

Et batteri oplades med en strøm, der falder jævnt fra $2{,}0$ A til $0$ på $4{,}0$ timer. Hvor meget ladning er kommet ind?

- **Ladning er integralet af strøm:** $Q = \int I \, \mathrm{d}t$.
- **Areal:** Trekant, $\tfrac{1}{2} \cdot 4{,}0 \text{ h} \cdot 2{,}0 \text{ A} = 4{,}0 \text{ A·h}$.

![Strømmen I som funktion af tiden t. Arealet under grafen er ladningen 4,0 A·h, det vil sige 14 400 C.](/img/integration-6-ladning.svg)

**Enhed:** $\text{A} \cdot \text{h}$ er en almindelig enhed for batteriers kapacitet. Omregnet til SI:

$$4{,}0 \text{ A·h} = 4{,}0 \cdot 3600 \text{ A·s} = 14\,400 \text{ C}$$

---

## Opsummering

| | Størrelse | Funktion | Areal | Enhed |
|---|---|---|---|---|
| 1 | Kraftens impuls | $F$ konstant | rektangel | N·s |
| 2 | Strækning | $v = a \cdot t$ | trekant | m |
| 3 | Fjederenergi | $F = k \cdot x$ | trekant | J |
| 4 | Kinetisk energi | $m \cdot v$ over $v$ | trekant | J |
| 5a | Potentiel energi | $F = m \cdot g$ konstant | rektangel | J |
| 5b | Energi fra effekt | $P(t)$ | trekant | J (eller kWh) |
| 6 | Ladning fra strøm | $I(t)$ | trekant | C (eller A·h) |

- **Konstant funktion:** Rektangel, så $\text{højde} \cdot \text{bredde}$.
- **Ret linje gennem $(0,0)$:** Trekant, så $\tfrac{1}{2} \cdot \text{højde} \cdot \text{bredde}$.
- **Enheden:** y-enhed gange x-enhed. Tjek altid, at den passer til størrelsen.

---

## Når integralet ikke starter i 0

Indtil nu har vi altid integreret fra $0$. Men spørgsmål i fysik handler ofte om et **stykke af forløbet**, fx: *hvor langt kører bilen mellem $3$ s og $6$ s?* Det er den slags, du møder i opgave 5 og 6 i [Integration-opgaver]({{< relref "integration-opgaver" >}}).

### Et helt konkret eksempel

Et trafiklys skifter til grøn, og en bil starter i hvile. Farten stiger jævnt:

$$v(t) = 2{,}0 \text{ m/s}^2 \cdot t$$

Du sætter et stopur i gang, når bilen starter. **Spørgsmål: Hvor langt kører bilen fra du har talt $3$ s, til du har talt $6$ s?**

### Trin 1: Tegn grafen og find det, du leder efter

Strækningen er arealet under $v$-$t$-grafen. Vi tegner grafen og farver to områder:

- **Blå** er arealet fra $0$ til $3$ s. 
- **Rød** er arealet fra $3$ til $6$ s. **Det er det, spørgsmålet handler om.**

![v som funktion af t. Blå er arealet fra 0 til 3 s (9,0 m). Rød er arealet fra 3 til 6 s (27 m). Blå og rød tilsammen er arealet fra 0 til 6 s (36 m).](/img/integration-a-til-b.svg)

Prøv lige at tælle tern her så kan du se hvad det røde areal giver. Husk at en streg på $y-$aksen er $3\frac{m}{s}$

### Trin 2: Tricket, du allerede kan

Vi ved, hvordan man finder et areal, der starter i $0$. Det kan vi bruge to gange:

- Blå + rød er arealet fra $0$ til $6$ s. Det kan vi finde.
- Blå er arealet fra $0$ til $3$ s. Det kan vi også finde.
- Så er rød det store areal **minus** det lille:

$$\text{rød} = (\text{blå} + \text{rød}) - \text{blå}$$

### Trin 3: Regn det ud

Først finder vi en stamfunktion med gæt-metoden. Hvilken funktion skal du aflede for at få $2{,}0 \text{ m/s}^2 \cdot t$? Det er

$$S(t) = 1{,}0 \text{ m/s}^2 \cdot t^2$$

Afled den, og tjek: $S'(t) = 2{,}0 \text{ m/s}^2 \cdot t$ ✓.

| Areal | Hvad er det? | Udregning |
|---|---|---|
| Blå + rød | Fra $0$ til $6$ s | $S(6 \text{ s}) = 1{,}0 \cdot 6^2 = 36$ m |
| Blå | Fra $0$ til $3$ s | $S(3 \text{ s}) = 1{,}0 \cdot 3^2 = 9{,}0$ m |
| **Rød** | **Fra $3$ til $6$ s** | $36 \text{ m} - 9{,}0 \text{ m} = \mathbf{27 \text{ m}}$ |

Bilen kører altså $27$ m mellem $3$ s og $6$ s.

### Trin 4: Skriv det kort

Det store minus det lille kan skrives med grænser. Tallet nederst ($3$) er starten, og tallet øverst ($6$) er slutningen:

$$\int_{3}^{6} v \, \mathrm{d}t = S(6) - S(3)$$

Rækkefølgen er altid: **sæt den øverste grænse ind, sæt den nederste grænse ind, og træk fra hinanden.** Det er præcis det, vi gjorde i tabellen.

### Trin 5: Tjek dit svar

Det røde område er en trapez. Farten er $v(3) = 6{,}0$ m/s og $v(6) = 12$ m/s, og bredden er $3{,}0$ s:

$$\tfrac{1}{2} \cdot (6{,}0 + 12) \text{ m/s} \cdot 3{,}0 \text{ s} = 27 \text{ m} \quad ✓$$

### Hvad med startværdien?

I afsnit 4 så vi, at en stamfunktion har en ekstra konstant $C$. Den er helt ligegyldig her, for den er med i begge led og forsvinder, når du trækker fra:

$$\left(S(6) + C\right) - \left(S(3) + C\right) = S(6) - S(3)$$

> **Huskeregel for grænser:**
> 1. Find en stamfunktion $S(t)$ med gæt-metoden.
> 2. Sæt den øverste grænse ind: $S(\text{slut})$.
> 3. Sæt den nederste grænse ind: $S(\text{start})$.
> 4. Træk fra: $S(\text{slut}) - S(\text{start})$.
> 5. Tjek enheden, og tjek med en trekant eller trapez, hvis du kan.

Prøv nu **opgave 5 og 6** i [Integration-opgaver]({{< relref "integration-opgaver" >}}).

---

## Integration i Python med måledata

Har du en måletabel i stedet for en formel, kan Python lægge trapezer sammen for dig. Der er flere muligheder i siden [Integralregning med Python]({{< relref "/docs/nat/Integralregning-med-python" >}}). Her kommer et eksempel, hvor du selv kan tælle tern og sammenligne.

### Eksempel: Elbilens energi de første 9 sekunder

En elbil accelererer fra stilstand. Bilens display viser effekten hvert sekund:

| $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| $P$ (kW) | 0 | 22 | 38 | 48 | 54 | 56 | 52 | 44 | 32 | 16 |

**Spørgsmål:** Hvor meget energi har motoren brugt fra $t = 0$ til $t = 9$ s? Energi er arealet under $P$-$t$-grafen: $E = \int P \, \mathrm{d}t$.

### Trin 1: Læg data ind som lister (arrays)

```python
import numpy as np

t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])            # tid i s
P = np.array([0, 22, 38, 48, 54, 56, 52, 44, 32, 16])   # effekt i kW
```

### Trin 2: Grafen på ternpapir

Punkterne forbindes med rette linjer. **Hver tern svarer til $1$ s og $10$ kW.**

![Effekten P (kW) som funktion af tiden t (s) for en elbil, med punkter for hver sekund og tern til at tælle.](/img/integration-python-tern.svg)

Hvad er én tern værd? Gang enhederne:

$$1 \text{ s} \cdot 10 \text{ kW} = 10 \text{ kW·s} = 10 \text{ kJ}$$

### Trin 3: Integrér med `np.trapezoid`

```python
E = np.trapezoid(P, t)                  # y FØR x. Enhed: kW·s = kJ
print(f"E = {E:.0f} kJ = {E/3600:.3f} kWh")
```

Python skriver: `E = 354 kJ = 0.098 kWh` (Python bruger punktum som decimaltegn).

- `np.trapezoid(P, t)` lægger et lille trapez under hver stump mellem to punkter: $\dfrac{P_i + P_{i+1}}{2} \cdot \Delta t$. Derefter lægger den alle trapezerne sammen.
- Enheden er $\text{kW} \cdot \text{s} = \text{kJ}$. For at få kWh dividerer vi med $3600$.
- I gamle vejledninger står `np.trapz`. Den findes ikke længere i nye versioner af NumPy, så brug `np.trapezoid`.

### Trin 4: Tjek ved at tælle tern

Nu kan du selv se, at Python har ret. Tæl tern under kurven:

- Cirka $27$ tern er helt under kurven.
- Cirka $18$ tern skæres af kurven. Regn dem for cirka halve: $18 / 2 = 9$.
- Sammen: $27 + 9 = 36$ tern.

$$36 \text{ tern} \cdot 10 \text{ kJ/tern} = 360 \text{ kJ}$$

Det passer rigtig godt med Pythons $354$ kJ. En lille forskel er normal, for man tæller delvise tern med et skøn, mens Python regner nøjagtigt.

### Bonus: Fra et sted til et andet i Python

Vil du kun have energien mellem $3$ s og $6$ s (som i bil-eksemplet ovenfor), vælger du kun de punkter:

```python
maske = (t >= 3) & (t <= 6)                     # kun tiderne fra 3 s til 6 s
E_3_6 = np.trapezoid(P[maske], t[maske])
print(E_3_6)                                    # 160.0 kJ
```

Det er den samme idé som med blå og rød: $E_{0 \to 6} - E_{0 \to 3} = 244 \text{ kJ} - 84 \text{ kJ} = 160 \text{ kJ}$. ✓

> **Model:** `np.trapezoid` regner, som om effekten går i rette linjer mellem punkterne. Det er en god tilnærmelse, når målingerne ligger tæt. Et tal for hvert sekund er en ret grov måling, så resultatet er et estimat.

---

Opgaver: [Integration-opgaver]({{< relref "integration-opgaver" >}}) · Python: [Integralregning med Python]({{< relref "/docs/nat/Integralregning-med-python" >}})
