---
title: Arbejdsdag — cirkelbevægelse
author: Mayunga
theme: light
bookHidden: true
build:
  render: never
  list: never
  publishResources: false
---

<!-- layout: section -->

# Modul 0

Opgaver fra opgavesættet

---

<!-- layout: section -->

# Udspring fra vippe

Opgave 5 · maj 2025 (sæt 2)

---

## Opgave 5 — Udspring fra vippe

![](arbejdsdag-slide/udspring.jpg)

- Udspringeren forlader vippen med $v_y = 7{,}24\ \text{m/s}$ opad. Massen er $m = 62{,}0\ \text{kg}$.
- **a)** Bestem bevægelsesmængden i lodret retning, idet udspringeren forlader vippen.
- **b)** Hun forlader vippen $4{,}08\ \text{m}$ over vandet. Bestem den maksimale højde over vandoverfladen.
- **c)** Brug bilaget ($v_y$ mod $t$) til at bestemme accelerationen ved $t = 0{,}245\ \text{s}$, hvor vippen er nedbøjet $92{,}5\ \text{cm}$. Bestem fjederkonstanten.

---

<!-- layout: title-content -->

## Udspring a) Løsning

Bevægelsesmængde: $p = m \cdot v$

$$
p_y = m \cdot v_y = 62{,}0\ \text{kg} \cdot 7{,}24\ \text{m/s} = 449\ \text{kg·m/s}
$$
<!-- step -->

**BC: 3** — styret af $7{,}24$ m/s og $62{,}0$ kg <!-- step -->

---

<!-- layout: title-content -->

## Udspring b) Løsning

Energibevarelse — kinetisk energi bliver til potentiel energi:

$$
\tfrac{1}{2} m v_y^2 = m g \Delta h \quad\Rightarrow\quad \Delta h = \frac{v_y^2}{2g}
$$
<!-- step -->

$$
\Delta h = \frac{(7{,}24\ \text{m/s})^2}{2 \cdot 9{,}82\ \text{m/s}^2} = 2{,}67\ \text{m}
$$
<!-- step -->

$$
h_{\max} = 4{,}08\ \text{m} + 2{,}67\ \text{m} = 6{,}75\ \text{m}
$$
<!-- step -->

**BC: 3** · Model: luftmodstand ses bort fra, kun den lodrette fart bidrager <!-- step -->

---

<!-- layout: title-content -->

## Udspring c) Accelerationen

Udspringer og vippe følges ad → accelerationen er **hældningen** af $(t, v_y)$-grafen

![](arbejdsdag-slide/udspring-fit.png)

Tangent (regression på 0,20–0,29 s): $a_y \approx 44\ \text{m/s}^2$ opad <!-- step -->

???
Aflæsningen er følsom for intervalvalget: 43–44 m/s².

---

<!-- layout: title-content -->

## Udspring c) Fjederkonstanten

Kræfter: elastisk kraft $k x$ op, tyngdekraft $mg$ ned. Newtons 2. lov:

$$
k x - m g = m a_y \quad\Rightarrow\quad k = \frac{m (a_y + g)}{x}
$$
<!-- step -->

$$
k = \frac{62{,}0\ \text{kg} \cdot (44 + 9{,}82)\ \text{m/s}^2}{0{,}925\ \text{m}} = 3{,}6 \cdot 10^3\ \text{N/m}
$$
<!-- step -->

**BC: 2** (tangentens hældning) · Model: Hookes lov, vippens egen masse ignoreres <!-- step -->

---

<!-- layout: section -->

# Løbesko

Opgave 6 

---

## Opgave 6 — Løbesko

![](arbejdsdag-slide/loebesko.png)

---

<!-- layout: title-content -->

## a) Formlerne:

Sålen som en **fjeder** → Hookes lov:

$$
F = k \cdot x
$$

Isolér sammentrykningen $x$:

$$
x = \frac{F}{k}
$$
<!-- step -->

Husk enheder: $1\ \text{kN/m} = 10^3\ \text{N/m}$ <!-- step -->

---

<!-- layout: title-content -->

## a) Løsning

Givet: $F = 419\ \text{N}$ og $k = 140\ \text{kN/m} = 140 \cdot 10^3\ \text{N/m}$

$$
x = \frac{F}{k} = \frac{419\ \text{N}}{140 \cdot 10^3\ \text{N/m}} = 2{,}99 \cdot 10^{-3}\ \text{m} = 2{,}99\ \text{mm}
$$
<!-- step -->

---

<!-- layout: title-content -->

## b) Hvad ved vi?

| Størrelse | Værdi | SI |
|---|---|---|
| Fjederkonstant *k* | 140 kN/m | 140·10³ N/m |
| Sammentrykning *x* | 4,6 mm | 4,6·10⁻³ m |
| Fart *v* | 14 km/h | 14 / 3,6 = 3,89 m/s |
| Skridtlængde *L* | 1,36 m | 1,36 m |
| Andel tabt til varme | 35 % | 0,35 |

???
F = 419 N fra a) bruges IKKE i b) — x er givet direkte.

---

<!-- layout: title-content -->

## b) Hvilke formler skal vi bruge?

- Elastisk energi: $E_{\text{el}} = \frac{1}{2} k x^2$ <!-- step -->
- Tab pr. skridt: $E_{\text{tab}} = 0{,}35 \cdot E_{\text{el}}$ <!-- step -->
- Skridt pr. sekund: $n = \dfrac{v}{L}$ <!-- step -->
- Effekt = energi pr. tid: $P = E_{\text{tab}} \cdot n$ <!-- step -->

---

<!-- layout: title-content -->

## b) Løsning

$$
E_{\text{el}} = \tfrac{1}{2} \cdot 140 \cdot 10^3\ \text{N/m} \cdot (4{,}6 \cdot 10^{-3}\ \text{m})^2 = 1{,}48\ \text{J}
$$

$$
E_{\text{tab}} = 0{,}35 \cdot 1{,}48\ \text{J} = 0{,}518\ \text{J}
$$
<!-- step -->

$$
n = \frac{3{,}89\ \text{m/s}}{1{,}36\ \text{m}} = 2{,}86\ \text{s}^{-1}
$$
<!-- step -->

$$
P = 0{,}518\ \text{J} \cdot 2{,}86\ \text{s}^{-1} = 1{,}5\ \text{W}
$$
<!-- step -->

**BC: 2** — styret af $4{,}6$ mm, $35\ \%$ og $14$ km/h <!-- step -->

???
Ét skridt = én sko i jorden, så resultatet gælder for begge sko samlet.
Model: sålen som ideel fjeder (Hookes lov), alle skridt ens, x er den maksimale sammentrykning.

---

<!-- layout: section -->

# Græshoppe

Opgave 5 · august 2025

---

## Opgave 5 — Græshoppe

![](arbejdsdag-slide/graeshoppe.png)

---

<!-- layout: title-content -->

## a) Hvilke formler skal vi bruge?

Bølgeformlen:

$$
v = \lambda \cdot f \quad\Rightarrow\quad \lambda = \frac{v}{f}
$$

Lydens fart i luft: $v \approx 343\ \text{m/s}$ (ved $20\ ^\circ\text{C}$) <!-- step -->

---

<!-- layout: title-content -->

## a) Løsning

Givet: $f = 11\ \text{kHz} = 11 \cdot 10^3\ \text{Hz}$

$$
\lambda = \frac{v}{f} = \frac{343\ \text{m/s}}{11 \cdot 10^3\ \text{Hz}} = 3{,}1 \cdot 10^{-2}\ \text{m} = 3{,}1\ \text{cm}
$$
<!-- step -->

???
Lydens fart afhænger af temperaturen — antagelse: 20 °C.

---

<!-- layout: title-content -->

## b) Hvad ved vi?

| Størrelse | Værdi |
|---|---|
| Billeder pr. sekund | 3200 → Δ*t* = 1/3200 s mellem billeder |
| Målestok | platformen 55 mm = 1260 pixel → 0,0437 mm/pixel |
| *g* | 9,82 m/s² |

Pas på: brug **3200** billeder/s — ikke videofilens 30 billeder/s!

---

<!-- layout: title-content -->

## b) Hvilke formler skal vi bruge?

- Lodret fart ved afsæt: $v_y = \dfrac{\Delta y}{\Delta t}$ (hældningen af $y(t)$) <!-- step -->
- Energibevarelse: $\tfrac{1}{2} m v_y^2 = m g \Delta h \;\Rightarrow\; \Delta h = \dfrac{v_y^2}{2g}$ <!-- step -->
- Maksimal højde: $h_{\max} = h_{\text{afsæt}} + \Delta h$ <!-- step -->

---

<!-- layout: title-content -->

## b) Videoanalysen

![](arbejdsdag-slide/graeshoppe-video.png)

De sidste ≈ 4 ms før afsæt: $v_y = 1{,}6\ \text{m/s}$, og tyngdepunktet er hævet $23\ \text{mm}$ <!-- step -->

---

<!-- layout: title-content -->

## b) Løsning

$$
\Delta h = \frac{v_y^2}{2g} = \frac{(1{,}6\ \text{m/s})^2}{2 \cdot 9{,}82\ \text{m/s}^2} = 0{,}13\ \text{m}
$$

$$
h_{\max} \approx 0{,}02\ \text{m} + 0{,}13\ \text{m} \approx 0{,}15\ \text{m}
$$
<!-- step -->

**Vurdering: ca. 15–20 cm** · BC: 1–2 (videoanalysen) <!-- step -->

- Farten stiger stadig ved videoens slutning → snarere undervurderet <!-- step -->
- Luftmodstand er ikke ubetydelig for et let insekt med vinger → trækker ned <!-- step -->

???
OBS: Løsningsforslaget i FY-skriftlig skriver 0,14 m og 0,16 m, men 1,6²/(2·9,82) = 0,130 m.

---


<!-- layout: title-content -->
## Sladeopgaven
![](arbejdsdag-slide/slade-1.png)

![](arbejdsdag-slide/slade-2.png)

---
<!-- layout: title-content -->

## Løsning
![](arbejdsdag-slide/slade-l1.png)

![](arbejdsdag-slide/slade-l2.png)

---


# Arbejdsdag
Mandag 2.1

**Fysik A · 3 moduler**

Opgaveregning · Jævn cirkelbevægelse · Forsøg

---

## Dagens program

| | Hvad | Form |
|---|---|---|
| **Modul 1** | Opgaver fra opgavesættet | to og to |
| **Modul 2** | Jævn cirkelbevægelse — intro + cirkelopgaver | Tavle undervisning + par |
| **Modul 3** | Forsøg: rørforsøget og keglependulet | Grupper |


???
Tidsfordeling er et forslag — justér efter klassen.
Pause mellem modulerne.

---

<!-- layout: section -->

# Modul 1

Opgaver fra opgavesættet

---

## Sådan arbejder vi

- Arbejd i par — én skriver, én regner, byt for hver opgave <!-- step -->
- Skriv altid: **formel → indsæt tal med enheder → resultat** <!-- step -->
- Sidder I fast i mere end 5 min? → næste opgave, og skriv spørgsmålet op <!-- step -->
- Vi samler op på tavlen ca. 10 min før modulets slutning <!-- step -->

---

## Opgave 1

![](arbejdsdag-slide/opg-1.png)

???
Facit / pointe:

---

## Opgave 2

![](arbejdsdag-slide/opg-2.png)

???
Facit / pointe:

---

## Opgave 3

![](arbejdsdag-slide/opg-3.png)

???
Facit / pointe:

---

## Opsamling — modul 1

- Hvilken opgave var sværest? Hvorfor?
- Hvilken formel brugte I mest?
- Typiske fejl: enheder, omregning, betydende cifre

---

<!-- layout: section -->

# Modul 2

Jævn cirkelbevægelse

---

## Konstant fart — men accelereret?

- Farten er konstant ... <!-- step -->
- ... men **retningen** ændrer sig hele tiden <!-- step -->
- Hastighed er en **vektor** → ændret hastighed = **acceleration** <!-- step -->
- Og acceleration kræver en resulterende kraft (Newtons 2. lov) <!-- step -->

???
Start med spørgsmålet til klassen: "Accelererer en bil, der kører rundt i en rundkørsel med konstant 30 km/t?"
Lad dem stemme først.

---

## Tre størrelser beskriver omløbet

- **Omløbstid** $T$: tid for én runde
- **Frekvens** $f = \dfrac{1}{T}$
- **Vinkelhastighed** $\omega = \dfrac{2\pi}{T} = 2\pi f$  (rad/s)

Prøv selv: [simulering af ω og t](https://christophridder.github.io/sim/omega-t.html)

---

## Stedvektoren

![](arbejdsdag-slide/cirkel-vektorer.svg)

$$\vec r(t) = \begin{pmatrix} r\cos(\omega t) \\ r\sin(\omega t) \end{pmatrix}$$

$$\vec v(t) = \vec r\,'(t) = \begin{pmatrix} -r\omega\sin(\omega t) \\ r\omega\cos(\omega t) \end{pmatrix}$$

???
Pointer: kædereglen giver faktoren ω.
r · v = 0 → hastigheden står vinkelret på radius.

---

## Accelerationen peger ind mod centrum

$$\vec a(t) = \vec v\,'(t) = -\omega^2 \cdot \vec r(t)$$

- Minustegnet: $\vec a$ peger **modsat** $\vec r$ → ind mod centrum <!-- step -->
- $v = \omega r = \dfrac{2\pi r}{T}$ <!-- step -->
- $a = \omega^2 r = \dfrac{v^2}{r}$ <!-- step -->

---

## Centripetalkraften

$$F_{\text{res}} = m \cdot \frac{v^2}{r} = m \cdot \omega^2 \cdot r$$

- **Ikke en ny kraft** — det er navnet på den *resulterende* kraft ind mod centrum <!-- step -->
- Leveres af noget konkret: snorkraft, gnidning, tyngdekraft, normalkraft <!-- step -->

???
Spørg: "Hvilken kraft er centripetalkraften for ... en satellit? en bil i et sving? en spand vand der svinges?"

---

## Centrifugalkraften er en skinkraft

- I et inertialsystem findes **kun** kraften ind mod centrum <!-- step -->
- "Slynget udad" i et sving = **inerti** (Newtons 1. lov) — kroppen vil fortsætte ligeud <!-- step -->
- Centrifugalkraften optræder kun som *fiktiv kraft*, hvis man regner i et roterende system <!-- step -->

???
Hvis der er en god YouTube-video (fx en bil i sving eller vandspand), sæt den ind på en ny slide:
!youtube[Titel](https://www.youtube.com/watch?v=...)

---

## Regneeksempel

En bil på $1200$ kg kører gennem et sving med radius $50$ m ved $15$ m/s.

$$F = m \cdot \frac{v^2}{r} = 1200\ \text{kg} \cdot \frac{(15\ \text{m/s})^2}{50\ \text{m}} = 5400\ \text{N}$$

Hvem leverer de 5400 N? <!-- step -->

???
Gnidningen mellem dæk og vej. Glat vej → for lille gnidning → bilen skrider ud (fortsætter ligeud, ikke "udad").

---

<!-- layout: section -->

# Cirkelopgaver

Brug formlerne fra før

---

## Formler til opgaverne

| Størrelse | Formel |
|---|---|
| Frekvens | *f* = 1/*T* |
| Vinkelhastighed | ω = 2π/*T* |
| Fart | *v* = ω·*r* = 2π*r*/*T* |
| Centripetalacceleration | *a* = *v*²/*r* = ω²·*r* |
| Centripetalkraft | *F* = *m*·*v*²/*r* = *m*·ω²·*r* |

---

## Cirkelopgave 1

![](arbejdsdag-slide/cirkel-opg-1.png)

???
Facit:

---

## Cirkelopgave 2

![](arbejdsdag-slide/cirkel-opg-2.png)

???
Facit:

---

## Ekstra opgaver (hvis I er hurtige)

1. En karruselstol kører rundt med omløbstid $4{,}0$ s i radius $3{,}0$ m. Bestem farten og centripetalaccelerationen.
2. Et lod på $0{,}20$ kg svinges i en snor i radius $0{,}60$ m med farten $2{,}5$ m/s. Bestem snorkraften.
3. Månen: $r = 3{,}84\cdot10^8$ m, $T = 27{,}3$ døgn. Bestem farten og centripetalaccelerationen.

???
Facit:
1. v = 4,7 m/s, a = 7,4 m/s²
2. F = 2,1 N
3. v = 1,02·10³ m/s, a = 2,72·10⁻³ m/s²

---

<!-- layout: section -->

# Modul 3

Forsøg — centripetalkraft

---

## To forsøg — vælg ét (eller begge)

| | Rørforsøget | Keglependulet |
|---|---|---|
| Kraften kendes fra | loddet: *F* = *M*·*g* | geometrien: tan θ = *r*/*h* |
| Du måler | *M*, *m*, *L*, *T* | *h*, *T* |
| Teori | *M*·*g* = *m*·ω²·*L* | *T* = 2π·√(*h*/*g*) |

Alle grupper: data i Excel og en graf, inden I går.

---

## Forsøg A — rørforsøget: opstilling

![](arbejdsdag-slide/roer-forsoeg.svg)

- Kugle (masse $m$) i snor
- Snoren går **ned gennem et glasrør**, som du holder
- Lodder (masse $M$) hænger i den anden ende
- Papirclips under røret markerer længden $L$

---

## Rørforsøget: hvordan kender vi kraften?

- Når loddet hænger **stille**, er snorkraften $M \cdot g$ <!-- step -->
- Samme snor hele vejen → den trækker i kuglen med $M \cdot g$ <!-- step -->
- Det er netop den kraft, der holder kuglen i cirklen <!-- step -->

$$M \cdot g = m \cdot \omega^2 \cdot L$$
<!-- step -->

Intet newtonmeter — du skifter kraften ved at skifte lodder. <!-- step -->

---

## Rørforsøget: sådan gør I

1. Mål $m$ (kugle) og $M$ (lodder). Sæt clipsen, så $L \approx 0{,}60$ m.
2. Sving kuglen over hovedet. Justér farten, så clipsen lige netop ligger under røret.
3. Tag tid for **10 omløb** → $T$ → $\omega = 2\pi/T$
4. Gentag med 4–5 forskellige $M$

**Sikkerhed:** Briller på · god afstand til andre grupper · hold røret, ikke snoren

???
Talforventning: m = 12 g, L = 0,60 m, M = 50 g → T ≈ 0,76 s (10 omløb ≈ 7,6 s).

---

## Rørforsøget: databehandling

- Plot $F = M g$ (y) mod $\omega^2$ (x) i Excel
- Teori: ret linje gennem $(0,0)$ med hældning $m \cdot L$
- Sammenlign hældningen med jeres målte $m \cdot L$ — afvigelse i %

**Modelovervejelser**
- Snoren er ikke vandret — men $\sin\varphi$ går ud, når vi bruger $L$ i stedet for $r$ <!-- step -->
- Gnidning mellem snor og rør er den største fejlkilde <!-- step -->
- Loddet skal hænge stille — ellers er snorkraften ikke $Mg$ <!-- step -->

---

## Forsøg B — keglependulet

![](arbejdsdag-slide/keglependul.svg)

- Et lod i en snor svinger i en **vandret cirkel**
- Snorkraftens lodrette del ophæver tyngdekraften
- Den vandrette del er den resulterende kraft ind mod centrum

---

## Keglependulet: teorien

$$m g \tan\theta = m \omega^2 r \quad\text{og}\quad \tan\theta = \frac{r}{h}$$

$$\Rightarrow\quad \omega^2 = \frac{g}{h} \quad\Rightarrow\quad T = 2\pi\sqrt{\frac{h}{g}}$$

Både $m$ og $r$ går ud — du skal kun måle **højden $h$** og **tiden**. <!-- step -->

???
h = højden fra ophængningspunktet ned til cirklens plan.
h = 0,50 m → T ≈ 1,42 s.

---

## Keglependulet: sådan gør I

1. Hæng loddet op. Tegn en kridtcirkel på gulvet / brug et mærke under cirklen.
2. Mål $h$: fra ophænget lodret ned til cirklens plan.
3. Sæt loddet i gang i en jævn, vandret cirkel. Tag tid for **10 omløb**.
4. Gentag for 4–5 forskellige $h$.

**Databehandling:** Plot $T^2$ mod $h$. Teori: ret linje gennem $(0,0)$ med hældning $\dfrac{4\pi^2}{g}$ → bestem $g$.

---

## Inden I går

- [ ] Data i Excel med enheder
- [ ] Graf med aksetitler og tendenslinje
- [ ] Sammenligning med teorien (afvigelse i %)
- [ ] Én sætning om den største fejlkilde

**Til næste gang:** Læs [Jævn cirkelbevægelse](https://christophridder.github.io/docs/fysik/emner-a/centralbevaegelse/jaevn-cirkelbevaegelse/)
