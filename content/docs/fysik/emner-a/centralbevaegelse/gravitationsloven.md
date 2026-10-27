---
title: "Newtons gravitationslov"
weight: 2
pdf: "pdfs/gravitationsloven.pdf"
pdf_ny_fane: true
aliases: ["/docs/fysik/emner-a/centralbevaegelse/gravitation-centrallegeme/"]
---

**Niveau: Fysik A** · **Emne: Centralbevægelse – Newtons gravitationslov og tyngdefeltet**

På siden om [jævn cirkelbevægelse]({{< relref "jaevn-cirkelbevaegelse" >}}) så
du, at en cirkelbevægelse kræver en kraft ind mod centrum. For Månen og
satellitterne er det **tyngdekraften**. Her finder du ud af, hvor stor den er.
Bagefter bruger du loven til at forklare [Keplers love]({{< relref "keplers-love" >}}).

## Del 1 – Gravitationsloven

To masser $M$ og $m$ i afstanden $r$ (mellem centrene) tiltrækker hinanden med kraften

$$F = G \cdot \frac{M \cdot m}{r^2}$$

med gravitationskonstanten $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg².

- Kraften er **proportional med begge masser**: dobbelt masse giver dobbelt kraft.
- Kraften er **omvendt proportional med afstanden i anden**: dobbelt afstand giver en fjerdedel af kraften.
- Loven er **universel**. Den samme kraft får et æble til at falde, holder Månen om Jorden og Jorden om Solen.
- $G$ er meget lille. Derfor mærker du ikke tiltrækningen mellem to mennesker. Henry Cavendish målte den første gang i 1798 med en torsionsvægt.

### Kraften som vektor

Lad $\vec r$ være stedvektoren fra $M$ til $m$. Kraften på $m$ peger **mod** $M$, altså modsat $\vec r$:

$$\vec F = -G \cdot \frac{M \cdot m}{r^2} \cdot \frac{\vec r}{r}$$

Brøken $\vec r/r$ er en enhedsvektor (længde 1) i retning af $\vec r$. Sammenlign
med cirkelbevægelsen, hvor $\vec F_{\text{res}} = -m\omega^2 \cdot \vec r$. Begge
peger ind mod centrum – derfor kan tyngdekraften levere centripetalkraften.

**Newtons 3. lov:** Kraften fra $m$ på $M$ er lige så stor og modsat rettet. Månen
trækker i Jorden med præcis samme kraft, som Jorden trækker i Månen.

## Del 2 – Tyngdefeltet

Et centrallegeme med masse $M$ laver et **tyngdefelt** omkring sig.
Feltstyrken er kraften pr. kg:

$$g = \frac{F}{m} = \frac{G \cdot M}{r^2}$$

Ved Jordens overflade ($r = R$) giver det $g \approx 9{,}82$ m/s² – den $g$, du kender.
Længere ude bliver feltet svagere:

| Sted | Afstand fra Jordens centrum $r$ | $g$ (m/s²) |
|---|---|---|
| Jordens overflade | $6{,}37 \cdot 10^{6}$ m | $9{,}8$ |
| ISS (408 km over overfladen) | $6{,}78 \cdot 10^{6}$ m | $8{,}7$ |
| GPS-satellitter | $2{,}66 \cdot 10^{7}$ m | $0{,}56$ |
| Geostationær bane | $4{,}22 \cdot 10^{7}$ m | $0{,}22$ |
| Månens bane | $3{,}84 \cdot 10^{8}$ m | $0{,}0027$ |

> **Astronauterne på ISS er ikke vægtløse, fordi $g = 0$.** Tyngdekraften er
> stadig $88$ % af den ved jordoverfladen. De *føles* vægtløse, fordi både
> astronauten og rumstationen falder frit rundt om Jorden med samme acceleration.

## Del 3 – Newtons månetest

Newton spurgte: Er det den samme kraft, der får æblet til at falde og holder Månen i sin bane?

- Månen er ca. $60$ gange længere fra Jordens centrum end æblet ($r_{\text{Måne}}/R \approx 60$).
- Hvis kraften aftager med $1/r^2$, skal Månens acceleration være $60^2 \approx 3600$ gange mindre:
  $$a_{\text{forudsagt}} = 9{,}82\ \text{m/s}^2 \cdot \left(\frac{R}{r_{\text{Måne}}}\right)^2 = 2{,}70 \cdot 10^{-3}\ \text{m/s}^2$$
- Månens centripetalacceleration ud fra banen ($r = 3{,}84 \cdot 10^8$ m, $T = 27{,}3$ døgn) er
  $$a = \frac{4\pi^2 \cdot r}{T^2} = 2{,}72 \cdot 10^{-3}\ \text{m/s}^2$$

De to tal passer inden for 1 %. Det var et stærkt argument for, at tyngdekraften er universel og aftager med $1/r^2$.

## Del 4 – Cirkulær bane om et centrallegeme

For en cirkulær bane leverer tyngdekraften centripetalkraften:

$$G \cdot \frac{M \cdot m}{r^2} = \frac{m \cdot v^2}{r} \quad\Longrightarrow\quad v = \sqrt{\frac{G \cdot M}{r}}$$

Massen $m$ går ud. **Farten (og dermed omløbstiden) afhænger kun af centrallegemets masse $M$ og af afstanden $r$** – ikke af satellittens egen masse. En skruetrækker, som en astronaut taber, følger samme bane som rumstationen.

> **Model:**
> - **Centrallegemet regnes som en punktmasse.** Det gælder præcist for en kugle med kuglesymmetrisk massefordeling (Newton viste det). Jorden er lidt fladtrykt, så satellitbaner tæt på Jorden drejer langsomt.
> - **Centrallegemet står stille** ($m \ll M$). I virkeligheden kredser begge om det fælles tyngdepunkt. For Jorden og Månen ligger det $4{,}7 \cdot 10^{3}$ km fra Jordens centrum – stadig inde i Jorden. For en satellit er effekten helt forsvindende.
> - **Kun to legemer.** Solens tiltrækning forstyrrer Månens bane lidt.

## Opgaver

*Brug* $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg², $M_{\text{Jord}} = 5{,}97 \cdot 10^{24}$ kg,
$R_{\text{Jord}} = 6{,}37 \cdot 10^{6}$ m, $M_{\text{Måne}} = 7{,}35 \cdot 10^{22}$ kg,
$M_{\text{Sol}} = 1{,}99 \cdot 10^{30}$ kg og $1\ \text{AE} = 1{,}496 \cdot 10^{11}$ m.

1. **Solen og Jorden.** Bestem tyngdekraften mellem Solen og Jorden. Afstanden er $1$ AE.
2. **Din vægt på ISS.** En astronaut på $70$ kg er på ISS, $408$ km over jordoverfladen.
   a) Bestem tyngdekraften på astronauten på jordoverfladen og på ISS.
   b) Forklar, hvorfor astronauten alligevel svæver.
3. **Vej Jorden.** Brug $g = 9{,}82$ m/s² og Jordens radius til at bestemme Jordens masse.
4. **Mellem Jorden og Månen.** Afstanden mellem Jorden og Månen er $3{,}84 \cdot 10^{8}$ m.
   Hvor på linjen mellem dem er tyngdekraften fra Jorden og fra Månen lige store?
   *Hjælp:* sæt $G \cdot \dfrac{M \cdot m}{x^2} = G \cdot \dfrac{M_{\text{Måne}} \cdot m}{(r - x)^2}$, og tag kvadratroden.
5. **Modellens gyldighed.** I mekanik bruger du tit $g = 9{,}82$ m/s² som en konstant.
   I hvilken højde er $g$ faldet 1 %? Kommentér, hvornår modellen med konstant $g$ er god nok.

## Facit

| Opgave | Facit |
|---|---|
| 1 | $F = 3{,}54 \cdot 10^{22}$ N |
| 2a | Overfladen: $687$ N. ISS: $607$ N ($88$ %) |
| 2b | Astronaut og station falder frit med samme acceleration. Der er ingen normalkraft fra gulvet |
| 3 | $M = g R^2 / G = 5{,}97 \cdot 10^{24}$ kg |
| 4 | $x = 3{,}46 \cdot 10^{8}$ m fra Jordens centrum (90 % af vejen) |
| 5 | $h \approx 32$ km. Konstant $g$ er fin for alt, der foregår i atmosfærens nederste del – ikke for satellitter |

## Det skal du kunne efter forløbet

- Bruge gravitationsloven $F = G \cdot Mm/r^2$ og forklare, hvad der sker, når masser eller afstand ændres.
- Skrive tyngdekraften som en vektor rettet mod centrallegemet.
- Bruge tyngdefeltstyrken $g = GM/r^2$ og forklare Newtons månetest.
- Udlede $v = \sqrt{GM/r}$ for en cirkulær bane og forklare, hvorfor $m$ går ud.
- Diskutere modellens antagelser: punktmasse, $m \ll M$, kun to legemer.
