---
title: "Jævn cirkelbevægelse"
weight: 1
pdf: "pdfs/jaevn-cirkelbevaegelse.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Centralbevægelse – jævn cirkelbevægelse og kraft som vektor**

Her ser du på bevægelse rundt i en cirkel med konstant fart. Du indfører
stedvektoren, finder centripetalaccelerationen og -kraften og rydder op i
misforståelsen om "centrifugalkraften". Til sidst bygger opgaverne bro til
[Newtons gravitationslov]({{< relref "gravitationsloven" >}}).

## Del 1 – Jævn cirkelbevægelse

Ved jævn cirkelbevægelse er **farten konstant**, men retningen ændrer sig hele
tiden. Hastigheden er en vektor. Selvom *farten* er konstant, ændres
*hastigheden* – og en ændring i hastighed er en **acceleration**. Det er den
centrale (og kontraintuitive) pointe.

Tre størrelser beskriver omløbet:

- **Omløbstid** $T$: tiden for én hel runde.
- **Frekvens** $f = 1/T$: antal runder pr. sekund.
- **Vinkelhastighed** (også kaldet vinkelfrekvens) $\omega = \dfrac{2\pi}{T} = 2\pi \cdot f$: vinkel pr. sekund (i rad/s).

## Del 2 – Stedvektoren: fra $\vec r$ til $\vec v$ og $\vec a$

![Stedvektor, hastighed og acceleration ved jævn cirkelbevægelse](/img/centralbevaegelse/cirkel-vektorer.svg)

Læg et koordinatsystem med origo i cirklens centrum. Genstanden starter på
$x$-aksen og drejer vinklen $\omega t$ på tiden $t$. Så er **stedvektoren**

$$\vec r(t) = \begin{pmatrix} r \cdot \cos(\omega t) \\ r \cdot \sin(\omega t) \end{pmatrix}$$

**Hastigheden** er stedvektoren differentieret (kædereglen giver en ekstra faktor $\omega$):

$$\vec v(t) = \vec r\,'(t) = \begin{pmatrix} -r\omega \cdot \sin(\omega t) \\ r\omega \cdot \cos(\omega t) \end{pmatrix}$$

Længden er farten. Brug $\sin^2 + \cos^2 = 1$:

$$v = |\vec v| = \sqrt{(r\omega)^2 \cdot \left(\sin^2(\omega t) + \cos^2(\omega t)\right)} = \omega \cdot r$$

Prikproduktet $\vec r \cdot \vec v = -r^2\omega\cos\sin + r^2\omega\sin\cos = 0$.
Hastigheden står altså **vinkelret på radius** – den peger langs cirklen.

**Accelerationen** er hastigheden differentieret:

$$\vec a(t) = \vec v\,'(t) = \begin{pmatrix} -r\omega^2 \cdot \cos(\omega t) \\ -r\omega^2 \cdot \sin(\omega t) \end{pmatrix} = -\omega^2 \cdot \vec r(t)$$

Minustegnet fortæller, at $\vec a$ peger **modsat $\vec r$ – ind mod centrum**.
Længden er

$$a = \omega^2 \cdot r = \frac{v^2}{r} \qquad \left(\text{fordi } \omega = \tfrac{v}{r}\right)$$

> **Sammenfatning:** $v = \omega \cdot r = \dfrac{2\pi r}{T}$ og $a = \dfrac{v^2}{r} = \omega^2 \cdot r$, rettet ind mod centrum.

## Del 3 – Kraft som vektor: centripetalkraften

Newtons 2. lov er en **vektorligning**: $\vec F_{\text{res}} = m \cdot \vec a$.
Kraften peger samme vej som accelerationen. Her giver det

$$\vec F_{\text{res}} = m \cdot \vec a = -m\omega^2 \cdot \vec r$$

Den resulterende kraft peger altså **ind mod centrum**. Den kaldes
**centripetalkraften**, og størrelsen er

$$F = m \cdot \frac{v^2}{r} = m \cdot \omega^2 \cdot r$$

> **Vigtigt – centripetalkraften er ikke en ny kraft.** Den er navnet på den
> *resulterende* kraft ind mod centrum. Den leveres af noget konkret: snorens
> spænding, gnidningen mellem dæk og asfalt, tyngdekraften på en satellit eller
> normalkraften i et loop.

> **Centrifugalkraften er en skinkraft.** I et inertialsystem findes der **kun**
> centripetalkraften, der trækker indad. Følelsen af at blive "slynget udad" i et
> sving er ikke en kraft – det er **inertien** (Newtons 1. lov). Kroppen vil
> fortsætte ligeud, og det er bilen/sædet, der tvinger den ind i cirklen.
> Centrifugalkraften optræder kun som en **fiktiv kraft**, hvis man regner i et
> roterende referencesystem.

> **Regneeksempel:** En bil på $1200$ kg kører gennem en kurve med radius $50$ m
> ved farten $15$ m/s. Den nødvendige centripetalkraft er
> $$F = m \cdot \frac{v^2}{r} = 1200\ \text{kg} \cdot \frac{(15\ \text{m/s})^2}{50\ \text{m}} = 5400\ \text{N}$$
> Den kraft skal gnidningen mellem dæk og vej kunne levere – ellers skrider bilen.

## Del 4 – Eksperiment: centripetalkraft

**Formål:** Eftervise sammenhængen $F = m \cdot \omega^2 \cdot L$ (svarer til $F = m v^2/r$).

### Opstilling

![Opstilling med glasrør, prop og lodder](/img/centralbevaegelse/roer-forsoeg.svg)

- En lille prop med massen $m$ sidder i den ene ende af en snor.
- Snoren løber ned **gennem et lodret glasrør**, som du holder i hånden.
- I den nederste ende hænger lodder med samlet masse $M$.
- En papirclips på snoren lige under røret viser, om længden $L$ fra røret til proppen er konstant.

### Hvordan kender man kraften?

Du skal **ikke** måle kraften med et newtonmeter.

- Når loddet $M$ hænger stille, er snorspændingen $M \cdot g$.
- Snoren er den samme hele vejen, så den trækker også i proppen med $M \cdot g$.
- Det er netop den kraft, der holder proppen i cirkelbanen. **Kraften er altså givet af loddet:** $F = M \cdot g$.

Du skifter kraften ved at skifte lodder.

### Gennemførelse

1. Sæt clipsen, så $L$ er fx $0{,}60$ m. Mål $m$ og $M$.
2. Sving proppen rundt over hovedet. Justér farten, så clipsen bliver lige under røret.
3. Tag tid for $10$ omløb, og find $T$ og $\omega = 2\pi/T$.
4. Gentag med 4–5 forskellige $M$.

### Databehandling (Excel)

- Plot $F = M \cdot g$ mod $\omega^2$. Teorien giver en ret linje gennem $(0,0)$ med hældningen $m \cdot L$.
- Sammenlign hældningen med den målte $m \cdot L$.

> **Model:** Snoren er ikke helt vandret – proppen hænger lidt ned. Brug derfor
> snorlængden $L$ og ikke radius $r$. Snorens vandrette del af kraften er
> $F_{\text{snor}} \cdot \sin\varphi$ og radius er $r = L \cdot \sin\varphi$, så
> $\sin\varphi$ går ud: $M \cdot g = m \cdot \omega^2 \cdot L$ gælder **præcist**.
> Modellen antager desuden, at der ingen gnidning er mellem snor og rør, og at
> loddet hænger stille. Gnidningen er den største fejlkilde. Den gør, at loddet
> kan hænge stille ved lidt forskellig fart.

> **Talforventning:** Med $m = 12$ g, $L = 0{,}60$ m og $M = 50$ g giver teorien
> $T \approx 0{,}76$ s, dvs. $10$ omløb på ca. $7{,}6$ s.

### Alternativ: keglependul

![Keglependul med kræfter](/img/centralbevaegelse/keglependul.svg)

Et lod i en snor svinger rundt i en vandret cirkel, så snoren beskriver en kegle.
Her måler du kraften **geometrisk** i stedet:

- Kræfterne på loddet er snorkraften $\vec T$ og tyngdekraften $m\cdot\vec g$.
- Den lodrette del af $\vec T$ ophæver tyngdekraften. Den vandrette del er den resulterende kraft ind mod centrum.
- Trekanten giver $F_{\text{res}} = m \cdot g \cdot \tan\theta = m \cdot g \cdot \dfrac{r}{h}$.
- Sæt lig $m \cdot \omega^2 \cdot r$. Så går både $m$ og $r$ ud:
  $$\omega^2 = \frac{g}{h} \quad\Longrightarrow\quad T = 2\pi\sqrt{\frac{h}{g}}$$

Du skal altså kun måle **højden** $h$ fra ophænget ned til cirklens plan (fx med
kridtcirkel på gulvet) og tage tid. Med $h = 0{,}50$ m forventer du
$T \approx 1{,}42$ s.

> **Prøverelevant:** Hold analysen i Excel. Et alternativ med moderne udstyr er
> en kraftsensor og en rotationssensor på en roterende arm. De giver $F$ og
> $\omega$ direkte.

## Opgaver

1. En karruselstol kører rundt med omløbstid $4{,}0$ s i radius $3{,}0$ m. Bestem
   farten og centripetalaccelerationen.
2. Et lod på $0{,}20$ kg svinges i en snor i radius $0{,}60$ m med farten
   $2{,}5$ m/s. Bestem centripetalkraften, dvs. snorens spænding.
3. **Satellit – beregn farten.** En satellit bevæger sig i en cirkulær bane om
   Jorden i højden $h = 350$ km over overfladen. Her leverer **tyngdekraften**
   netop centripetalkraften, så
   $$\frac{G \cdot M \cdot m}{r^2} = \frac{m \cdot v^2}{r}$$
   Bestem satellittens fart $v$, og find derefter omløbstiden $T$.
   *Givet:* $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg², Jordens masse
   $M = 5{,}97 \cdot 10^{24}$ kg, Jordens radius $R = 6{,}37 \cdot 10^{6}$ m.
   *Hjælp:* banens radius er $r = R + h$, og $m$ går ud.
4. **Diskussion:** En passager mærker sig "presset udad" i et skarpt sving.
   Forklar med Newtons love, hvorfor der i virkeligheden ingen udadrettet kraft er.
5. **Månen om Jorden.** Månen bevæger sig i en (næsten) cirkulær bane om Jorden.
   Afstanden mellem centrene er $r = 3{,}84 \cdot 10^{8}$ m, og omløbstiden er
   $T = 27{,}3$ døgn. Månens masse er $m = 7{,}35 \cdot 10^{22}$ kg.
   a) Bestem Månens fart og centripetalacceleration.
   b) Bestem den centripetalkraft, der skal til for at holde Månen i banen.
   c) Bestem tyngdekraften fra Jorden på Månen med $F = G \cdot \dfrac{M \cdot m}{r^2}$ (tal fra opgave 3).
   d) Sammenlign b) og c). Hvad viser det? Hvor stor er kraften fra *Månen* på *Jorden*?

## Facit

| Opgave | Facit |
|---|---|
| 1 | $v = 4{,}7$ m/s, $a = 7{,}4$ m/s² |
| 2 | $F = 2{,}1$ N |
| 3 | $r = 6{,}72 \cdot 10^{6}$ m, $v = \sqrt{GM/r} \approx 7{,}7$ km/s, $T = 2\pi r/v \approx 5{,}5 \cdot 10^{3}$ s $\approx 91$ min |
| 4 | Ingen kraft udad. Kroppen vil fortsætte ligeud (1. lov), sædet/døren skubber den ind mod centrum (2. lov) |
| 5a | $T = 2{,}36 \cdot 10^{6}$ s, $v = 1{,}02 \cdot 10^{3}$ m/s, $a = 2{,}72 \cdot 10^{-3}$ m/s² |
| 5b | $F = m \cdot a = 2{,}00 \cdot 10^{20}$ N |
| 5c | $F = 1{,}98 \cdot 10^{20}$ N |
| 5d | Under 1 % forskel: tyngdekraften leverer netop centripetalkraften. Efter Newtons 3. lov trækker Månen i Jorden med samme kraft, $2{,}0 \cdot 10^{20}$ N |

## Det skal du kunne efter forløbet

- Forklare, at jævn cirkelbevægelse er accelereret, selv om farten er konstant.
- Opskrive stedvektoren $\vec r(t)$ og differentiere den til $\vec v$ og $\vec a$.
- Bruge $v = 2\pi r / T = \omega \cdot r$ og $a = v^2/r = \omega^2 \cdot r$.
- Opstille centripetalkraften $F = m v^2 / r$ og pege på, hvilken konkret kraft der leverer den.
- Forklare, hvorfor centrifugalkraften er en skinkraft.
- Forklare, hvordan kraften kendes i rørforsøget og i keglependulet.
