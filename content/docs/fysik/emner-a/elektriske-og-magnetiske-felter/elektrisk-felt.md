---
title: "Elektrisk felt"
weight: 9
---

**Niveau: Fysik A** · **Emne: Elektriske felter** · **Demonstration: pladekondensator**

Forløbet indfører det elektriske felt, kraften på en ladning, feltet om en
kuglesymmetrisk ladning og det homogene felt. Undervejs udledes
spændingsforskellen som arbejde pr. ladning – og dermed den centrale sammenhæng
E = U/d, der binder feltet sammen med den U, I kender fra kredsløb.

## Del 1 – Det elektriske felt

Et elektrisk felt er det område omkring en ladning, hvor en anden ladning mærker
en kraft. Feltstyrken defineres som **kraften pr. ladning**:

$$E = \frac{F}{q} \quad\Longleftrightarrow\quad F = q \cdot E$$

Enheden er N/C (som også kan skrives V/m). Feltet er en vektor; **feltlinjer**
peger den vej, en positiv prøveladning ville blive skubbet.

### Coulombs lov og det kuglesymmetriske felt

To punktladninger påvirker hinanden med Coulombkraften:

$$F = k \cdot \frac{q_1 \cdot q_2}{r^2}$$

med Coulombkonstanten $k = 8{,}99 \cdot 10^{9}$ N·m²/C². Feltet **omkring en enkelt
kuglesymmetrisk ladning** $Q$ (eller punktladning) er derfor

$$E = k \cdot \frac{Q}{r^2}$$

Det aftager med kvadratet på afstanden – ligesom tyngdefeltet.

> **Regneeksempel:** To ladninger på hver $1{,}0 \cdot 10^{-9}$ C i afstanden
> $0{,}10$ m frastøder hinanden med
> $F = 8{,}99 \cdot 10^{9} \cdot \dfrac{(1{,}0 \cdot 10^{-9})^2}{0{,}10^2} \approx 9{,}0 \cdot 10^{-7}$ N.

## Del 2 – Det homogene felt og spændingsforskellen

Mellem to parallelle, modsat ladede plader er feltet **homogent** – lige stort og
ensrettet overalt (på nær lige ved kanterne).

### Udledning: spændingsforskel som arbejde pr. ladning

En ladning $q$ i feltet mærker kraften $F = q \cdot E$. Flyttes ladningen
stykket $d$ langs feltet, udfører feltet arbejdet:

$$W = F \cdot d = q \cdot E \cdot d$$

**Spændingsforskellen** $U$ mellem de to punkter er netop arbejdet pr. ladning –
det er selve definitionen:

$$U = \frac{W}{q}$$

Indsætter vi $W = q \cdot E \cdot d$, går ladningen ud:

$$U = \frac{q \cdot E \cdot d}{q} = E \cdot d \quad\Longrightarrow\quad E = \frac{U}{d}$$

Det er den **samme $U$**, I kender fra elektriske kredsløb – nu set fra feltet.
For en **elektron** (ladning $e$), der accelereres gennem spændingsforskellen $U$,
bliver det tilførte arbejde til kinetisk energi:

$$e \cdot U = \tfrac{1}{2} \cdot m \cdot v^2 \quad\Longrightarrow\quad v = \sqrt{\frac{2 \cdot e \cdot U}{m}}$$

Det er også her enheden **elektronvolt** kommer fra: 1 eV er netop den energi, en
elektron får ved at gennemløbe 1 V.

> **Regneeksempel:** Plader med $U = 100$ V og afstand $d = 5{,}0$ cm giver
> $E = U/d = 100 / 0{,}050 = 2000$ V/m. En elektron, der accelereres gennem de
> $100$ V, opnår farten
> $v = \sqrt{2 \cdot 1{,}602 \cdot 10^{-19} \cdot 100 / 9{,}11 \cdot 10^{-31}} \approx 5{,}9 \cdot 10^{6}$ m/s.
> (Den fart bruger vi igen, når ladede partikler bevæger sig i felter.)

> **Kobling til strømstyrken (for de skarpe):** Feltet i en leder er det, der
> driver elektronerne. I en leder med tværsnitsareal $A$ er der $n$
> ladningsbærere pr. volumen, hver med ladning $e$, der driver med farten $v$. På
> tiden $t$ passerer alle bærere inden for afstanden $v \cdot t$ et tværsnit –
> altså $n \cdot A \cdot v \cdot t$ bærere med samlet ladning
> $Q = n \cdot e \cdot A \cdot v \cdot t$. Strømstyrken bliver:
> $$I = \frac{Q}{t} = n \cdot e \cdot A \cdot v$$
> Den basale $I = Q/t$ kender I fra kredsløb; det nye her er, at det er **feltet**,
> der sætter driften $v$ – og dermed strømmen – i gang.

## Del 3 – Demonstration: pladekondensator og feltlinjer

Det elektriske felt egner sig især til demonstration.

- **Feltlinjer synliggjort:** Drys små korn (fx semuljegryn) i olie mellem to
  elektroder. Kornene retter sig ind langs feltlinjerne og tegner mønsteret –
  både for to punktladninger og for parallelle plader.
- **Det homogene felt:** Tilslut to parallelle plader en højspændingskilde og vis,
  at feltet er ensrettet i midten.
- **Kraft på en ladning (kvantitativt):** Hæng en let, ladet kugle i en tråd nær
  en ladet plade. Kuglen trækkes til siden, og af kraftbalancen
  $F_e = m \cdot g \cdot \tan\theta$ kan den vandrette elektriske kraft bestemmes
  ud fra udsvingsvinklen $\theta$ og kuglens vægt. (Samme opstilling som i
  eksamensbilaget om elektriske felter.)

## Opgaver

1. To punktladninger på $+2{,}0 \cdot 10^{-9}$ C og $+3{,}0 \cdot 10^{-9}$ C er
   $0{,}20$ m fra hinanden. Bestem kraften mellem dem.
2. Bestem feltstyrken $0{,}10$ m fra en kuglesymmetrisk ladning på
   $5{,}0 \cdot 10^{-9}$ C.
3. To plader har spændingsforskellen $300$ V og afstanden $2{,}0$ cm. Bestem
   feltstyrken, og bestem kraften på en ladning på $4{,}0 \cdot 10^{-9}$ C i feltet.
4. En elektron accelereres fra hvile gennem en spændingsforskel på $250$ V.
   Bestem dens kinetiske energi (i J og eV) og dens slutfart.

## Det skal I kunne efter forløbet

- Bruge feltdefinitionen $E = F/q$ og tegne/tolke feltlinjer.
- Anvende Coulombs lov og feltet $E = kQ/r^2$ om en kuglesymmetrisk ladning.
- Udlede $U = E \cdot d$ ud fra arbejde pr. ladning og bruge det på det homogene felt.
- Bestemme den fart, en elektron opnår ved acceleration gennem en spændingsforskel.
- Forklare, hvordan feltet i en leder driver strømmen ($I = n e A v$).
