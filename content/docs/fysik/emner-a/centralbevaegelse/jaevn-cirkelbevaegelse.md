---
title: "Jævn cirkelbevægelse"
weight: 4
---

**Niveau: Fysik A** · **Emne: Mekanik – jævn cirkelbevægelse** · **Eksperiment: centripetalkraft**

Forløbet behandler bevægelse rundt i en cirkel med konstant fart, indfører
centripetalacceleration og -kraft og rydder op i den klassiske misforståelse om
"centrifugalkraften". Til sidst en satellit-opgave, der bygger bro til
gravitationsblokken.

## Del 1 – Jævn cirkelbevægelse (teori)

Ved jævn cirkelbevægelse er **farten konstant**, men retningen ændrer sig hele
tiden. Hastigheden er en vektor, så selvom *farten* er konstant, ændres
*hastigheden* – og en ændring i hastighed er en **acceleration**. Det er den
centrale (og kontraintuitive) pointe.

Tre størrelser beskriver omløbet:

- **Omløbstid** $T$: tiden for én hel runde.
- **Frekvens** $f = 1/T$: antal runder pr. sekund.
- **Vinkelfrekvens** $\omega = \dfrac{2\pi}{T} = 2\pi \cdot f$: vinkel pr. sekund.

Farten langs cirklen med radius $r$ er omkredsen pr. omløbstid:

$$v = \frac{2\pi \cdot r}{T} = \omega \cdot r$$

## Del 2 – Centripetalkraften

Accelerationen peger altid **ind mod centrum** og kaldes
centripetalaccelerationen:

$$a = \frac{v^2}{r} = \omega^2 \cdot r$$

Efter Newtons 2. lov kræver det en resulterende kraft ind mod centrum –
**centripetalkraften**:

$$F = m \cdot \frac{v^2}{r} = m \cdot \omega^2 \cdot r$$

> **Vigtigt – centripetalkraften er ikke en ny kraft.** Den er navnet på den
> *resulterende* kraft ind mod centrum, og den leveres af noget konkret: snorens
> spænding, gnidningen mellem dæk og asfalt, tyngdekraften på en satellit, eller
> normalkraften i et loop.

> **Centrifugalkraften er en skinkraft.** I et inertialsystem findes der **kun**
> centripetalkraften, der trækker indad. Følelsen af at blive "slynget udad" i en
> sving er ikke en kraft – det er **inertien** (Newtons 1. lov): kroppen vil
> fortsætte ligeud, og det er bilen/sædet, der tvinger den ind i cirklen.
> Centrifugalkraften optræder kun som en **fiktiv kraft**, hvis man regner i et
> roterende referencesystem. 

> **Regneeksempel:** En bil på $1200$ kg kører gennem en kurve med radius $50$ m
> ved farten $15$ m/s. Den nødvendige centripetalkraft er
> $$F = m \cdot \frac{v^2}{r} = 1200 \cdot \frac{15^2}{50} = 5400 \text{ N}$$
> Den kraft skal gnidningen mellem dæk og vej kunne levere – ellers skrider bilen.

## Del 3 – Eksperiment: centripetalkraft

**Formål:** Eftervise sammenhængen $F = m \cdot v^2 / r$.

### Klassisk opstilling
Et lod med massen $m$ svinges rundt i en vandret cirkel i en snor, der løber
gennem et rør. I den anden ende hænger nogle lodder med samlet masse $M$, som
leverer en kendt, konstant centripetalkraft $F = M \cdot g$.

### Gennemførelse
1. Svingt loddet med fast radius $r$, så det hænger stabilt rundt.
2. Tag tid for fx 10 omløb og find omløbstiden $T$, og dermed
   $v = 2\pi r / T$.
3. Gentag med forskellige hængende masser $M$ (altså forskellig kraft $F$).

### Databehandling (Excel)
- Plot $F$ mod $v^2$. Sammenhængen er lineær gennem $(0,0)$, fordi
  $F = \dfrac{m}{r} \cdot v^2$. Hældningen er $\dfrac{m}{r}$ → sammenlign med den
  målte $m/r$.
- Diskutér usikkerheden: at holde radius konstant under svingningen er den
  største fejlkilde.

> **Prøverelevant:** Hold analysen i Excel. Et alternativ med moderne udstyr er
> en kraftsensor + rotationssensor på en roterende arm, som giver $F$ og $\omega$
> direkte.

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
4. **Diskussion:** En passager mærker sig "presset udad" i en skarp sving. Forklar
   med Newtons love, hvorfor der i virkeligheden ingen udadrettet kraft er.

> **Facit til opgave 3:** $r = 6{,}72 \cdot 10^{6}$ m giver
> $v = \sqrt{G \cdot M / r} \approx 7{,}7 \cdot 10^{3}$ m/s ($7{,}7$ km/s), og
> $T = 2\pi r / v \approx 5{,}5 \cdot 10^{3}$ s ($\approx 91$ min) – typisk for en
> satellit i lav kredsløbsbane.

## Det skal I kunne efter forløbet

- Forklare, at jævn cirkelbevægelse er accelereret, selv om farten er konstant.
- Bruge $v = 2\pi r / T = \omega \cdot r$ og $a = v^2/r$.
- Opstille centripetalkraften $F = m v^2 / r$ og identificere, hvilken konkret
  kraft der leverer den.
- Forklare, hvorfor centrifugalkraften er en skinkraft.
- Anvende centripetalkraften på en satellit, hvor tyngdekraften leverer kraften.
