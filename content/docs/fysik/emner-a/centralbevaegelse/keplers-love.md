---
title: "Keplers love"
weight: 3
pdf: "pdfs/keplers-love.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Centralbevægelse – Keplers love og satellitbaner**

Johannes Kepler fandt i begyndelsen af 1600-tallet tre love for planeternes
bevægelse. Han byggede dem på **Tycho Brahes** usædvanligt nøjagtige
observationer af især Mars, indsamlet på Hven. Keplers love kom altså **før**
[Newtons gravitationslov]({{< relref "gravitationsloven" >}}) – men de følger af den.

## Simulering: kredsløb om Jorden

{{< sim kredsloeb.html 700 >}}

Simuleringen regner med de rigtige tal for Jorden. Den røde prik er et fast
punkt på ækvator, så du kan se Jorden dreje.

**Undersøg selv**

1. **Masse eller afstand?** Vælg *ISS*. Skru på massen fra $1$ kg til Månens
   masse. Ændrer omløbstiden sig? Skru derefter på afstanden. Hvad bestemmer
   omløbstiden?
2. **Geostationær bane.** Skru langsomt afstanden op, indtil satellitten følger
   den røde prik. Aflæs afstanden og omløbstiden. Hvorfor er det ikke præcis
   $24$ timer?
3. **Ellipse.** Vælg *Geostationær*, og skru ellipsefaktoren op til $0{,}5$. Hvad
   sker der med omløbstiden? Hvor i banen er farten størst, og hvor er kraften størst?
4. **Keplers 2. lov.** Slå *Keplers 2. lov* til. Hvert farvet felt fejes ud på
   samme tid. Beskriv felternes form tæt på og langt fra Jorden.
5. **Når massen alligevel betyder noget.** Vælg *Månen* og massen *= Jorden*. Slå
   *Jorden bevæger sig* og *Sammenlign: 1 kg* til. Hvad sker der? Hvornår holder
   modellen "massen er ligegyldig"?

## Keplers 1. lov – ellipseloven

> Planeterne bevæger sig i **ellipsebaner** med Solen i det ene brændpunkt.

- En ellipse har en **store halvakse** $a$ (halvdelen af den længste diameter) og en **ellipsefaktor** (excentricitet) $e$ mellem $0$ og $1$.
- Mindste afstand: $r_{\min} = a \cdot (1 - e)$. Største afstand: $r_{\max} = a \cdot (1 + e)$.
- Om Solen hedder punkterne **perihel** og **aphel**. Om Jorden hedder de **perigæum** og **apogæum**.
- En **cirkel** er specialtilfældet $e = 0$, hvor $r_{\min} = r_{\max} = a$.

Newton viste, at en kraft, der aftager med $1/r^2$, altid giver en ellipse (eller
en parabel eller hyperbel, hvis legemet har nok energi til at undslippe – se
[Energi i centralbevægelse]({{< relref "energi-centralbevaegelse" >}})). Beviset
kræver mere matematik, end du har på A-niveau.

## Keplers 2. lov – fladeloven

> En linje fra Solen til planeten **overstryger lige store arealer i lige store tidsrum**.

![Keplers 2. lov: to lige store arealer på samme tid](/img/centralbevaegelse/kepler2.svg)

**Hvorfor?** På et kort tidsrum $\Delta t$ flytter planeten sig $v \cdot \Delta t$.
Linjen fra Solen fejer en smal trekant ud med arealet

$$\Delta A = \tfrac{1}{2} \cdot r \cdot v_\perp \cdot \Delta t$$

hvor $v_\perp$ er den del af farten, der står vinkelret på $\vec r$.

- Tyngdekraften peger **præcis mod Solen**. Den kan derfor ikke få planeten til at "dreje hurtigere eller langsommere rundt" om Solen. Fysikeren siger, at kraftmomentet om Solen er nul.
- Så er $r \cdot v_\perp$ konstant. Det kaldes, at **bevægelsesmængdemomentet** (impulsmomentet) $L = m \cdot r \cdot v_\perp$ er bevaret – som når en skøjteløber trækker armene ind og snurrer hurtigere.
- Dermed er $\Delta A / \Delta t = \tfrac{1}{2} r v_\perp$ konstant. Det er fladeloven.

**Konsekvens:** I perigæum og apogæum står farten vinkelret på $\vec r$, så

$$r_{\min} \cdot v_{\max} = r_{\max} \cdot v_{\min}$$

Planeten bevæger sig **hurtigst tæt på** og **langsomst langt væk**.

## Keplers 3. lov – periodeloven

> Kvadratet på omløbstiden er proportional med tredje potens af den store halvakse:
> $$\frac{T^2}{a^3} = \text{konstant}$$
> Konstanten er den samme for alle legemer om samme centrallegeme.

**Udledning for den cirkulære bane.** Tyngdekraften leverer centripetalkraften,
og farten er $v = 2\pi r/T$:

$$G \cdot \frac{M \cdot m}{r^2} = m \cdot \frac{v^2}{r} = m \cdot \frac{4\pi^2 \cdot r}{T^2} \quad\Longrightarrow\quad T^2 = \frac{4\pi^2}{G \cdot M} \cdot r^3$$

Altså $T^2 \propto r^3$ – Keplers 3. lov, nu udledt fra Newton. Konstanten er
$\dfrac{4\pi^2}{G \cdot M}$, og den afhænger **kun af centrallegemet**. For en
ellipse gælder samme formel med den store halvakse $a$ i stedet for $r$.

> **Afstanden bestemmer omløbstiden – ikke massen.** Satellittens masse $m$ går
> ud. Simuleringen viser det: Ændrer du massen, er $T$ uændret. Ændrer du
> ellipsefaktoren og beholder $a$, er $T$ også uændret.

> **Model:** Formlen antager, at centrallegemet står stille ($m \ll M$). Den
> præcise formel er $T^2 = \dfrac{4\pi^2 \cdot a^3}{G \cdot (M + m)}$, fordi begge legemer
> kredser om det fælles tyngdepunkt. For Månen ($m/M \approx 1/81$) giver det
> $27{,}26$ døgn i stedet for $27{,}42$ døgn. Den målte værdi er $27{,}32$ døgn,
> så korrektionen bringer os tættere på. Resten skyldes bl.a. Solens tiltrækning.

**Kendte baner om Jorden** (beregnet med $T^2 = \tfrac{4\pi^2}{GM} \cdot a^3$):

| Bane | $a$ fra Jordens centrum | Højde over overfladen | Omløbstid $T$ |
|---|---|---|---|
| ISS | $6\,780$ km | $408$ km | $92{,}6$ min |
| GPS | $26\,600$ km | $20\,200$ km | $11$ t $58$ min |
| Geostationær | $42\,150$ km | $35\,780$ km | $23$ t $56$ min |
| Månen | $384\,000$ km | – | $27{,}4$ døgn |

### Den geostationære bane

En geostationær satellit står stille over samme sted på ækvator. Den skal derfor
gå rundt **én gang, mens Jorden drejer én gang** – og i samme retning.

- Jorden drejer én gang på et **stjernedøgn**: $23$ t $56$ min $= 86\,164$ s.
- Et almindeligt døgn ($24$ t) er lidt længere, fordi Jorden også flytter sig i
  sin bane om Solen. Jorden skal dreje lidt ekstra, før Solen igen står højest.
- TV-paraboler peger på geostationære satellitter, og derfor skal de aldrig flyttes.

## Opgaver

*Brug* $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg² og $M_{\text{Jord}} = 5{,}97 \cdot 10^{24}$ kg.

1. **Geostationær bane.** Omløbstiden er et stjernedøgn, $T = 86\,164$ s. Brug
   Keplers 3. lov til at bestemme baneradius $r$, højden over jordoverfladen og farten $v$.
2. **Jupiter.** Jupiter har en store halvakse på $5{,}20$ AE. Bestem omløbstiden om Solen i år.
   *Hjælp:* for Jorden er $T = 1$ år og $a = 1$ AE, så $T^2/a^3 = 1$ år²/AE³.
3. **GPS.** GPS-satellitterne går to gange rundt pr. stjernedøgn, $T = 11$ t $58$ min.
   Bestem den store halvakse $a$ og højden over jordoverfladen.
4. **Halleys komet** har store halvakse $a = 17{,}8$ AE og ellipsefaktor $e = 0{,}967$.
   a) Bestem omløbstiden.
   b) Bestem den mindste og største afstand til Solen.
   c) Hvor mange gange hurtigere bevæger kometen sig i perihel end i aphel?
5. **Diskussion.** Forklar med Keplers 2. lov, hvorfor en komet bevæger sig meget
   hurtigt, når den passerer tæt forbi Solen, og langsomt i den fjerne del af sin bane.
6. **Modellens gyldighed.** I simuleringen kan du vælge, at satellitten vejer lige
   så meget som Jorden. Hvorfor passer $T^2 = \tfrac{4\pi^2}{GM} \cdot a^3$ så ikke
   længere? Hvilken antagelse er brudt?

## Facit

| Opgave | Facit |
|---|---|
| 1 | $r = 4{,}22 \cdot 10^{7}$ m, højde $3{,}58 \cdot 10^{7}$ m, $v = 3{,}07 \cdot 10^{3}$ m/s |
| 2 | $T = 5{,}20^{1{,}5} = 11{,}9$ år |
| 3 | $a = 2{,}66 \cdot 10^{7}$ m, højde $2{,}02 \cdot 10^{7}$ m |
| 4a | $T = 75{,}1$ år |
| 4b | $r_{\min} = 0{,}59$ AE, $r_{\max} = 35{,}0$ AE |
| 4c | $v_{\max}/v_{\min} = r_{\max}/r_{\min} = 59{,}6$ gange |
| 5 | Linjen til Solen skal feje samme areal pr. tid. Tæt på er linjen kort, så kometen skal flytte sig langt |
| 6 | Antagelsen $m \ll M$ er brudt. Jorden bevæger sig også, og $T^2 = 4\pi^2 a^3 / (G(M+m))$ |

## Det skal du kunne efter forløbet

- Formulere Keplers tre love og bruge begreberne store halvakse, ellipsefaktor, perigæum og apogæum.
- Forklare fladeloven med bevarelse af bevægelsesmængdemomentet og bruge $r_{\min} \cdot v_{\max} = r_{\max} \cdot v_{\min}$.
- Udlede Keplers 3. lov for den cirkulære bane fra Newtons gravitationslov.
- Forklare, at omløbstiden bestemmes af afstanden og centrallegemets masse – ikke af satellittens masse – og hvornår det holder.
- Beregne geostationær bane og forklare forskellen på stjernedøgn og døgn.
