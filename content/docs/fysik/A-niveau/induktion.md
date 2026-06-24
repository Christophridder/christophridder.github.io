---
title: "Induktion"
weight: 12
---

**Niveau: Fysik A** · **Emne: Elektromagnetisk induktion** · **Eksperiment: magnet gennem spole**

Forløbet binder elektromagnetismen sammen: hvor magnetfeltet gav en kraft på en
strøm (motoren), giver et **ændret** magnetfelt nu en strøm (generatoren).
Nøglen er Faradays induktionslov og Lenz' lov. Emnet er abstrakt, så formlerne
holdes centrale, og fortegnet forklares omhyggeligt.

## De centrale formler

> **Magnetisk flux** gennem et areal $A$ i et felt $B$ (vinkelret):
> $$\Phi = B \cdot A$$
> Enheden er weber (Wb), hvor $1$ Wb $= 1$ T·m².
>
> **Faradays induktionslov** – en *ændring* i flux inducerer en spænding:
> $$\varepsilon = -N \cdot \frac{\Delta \Phi}{\Delta t}$$
> hvor $N$ er antallet af vindinger i spolen.
>
> **Lenz' lov** (fortegnet): den inducerede strøm løber altid, så den **modvirker**
> den ændring, der skabte den.

## Del 1 – Magnetisk flux

Fluxen er et mål for, hvor meget magnetfelt der går gennem en sløjfe eller spole:

$$\Phi = B \cdot A$$

Den centrale pointe: der induceres **kun** en spænding, når fluxen **ændrer sig**.
Et konstant felt gennem en spole giver ingenting. Fluxen kan ændres på tre måder:

- ved at ændre **feltstyrken** $B$ (fx en magnet, der nærmer sig),
- ved at ændre **arealet** $A$ (fx en sløjfe, der trækkes ud af feltet),
- ved at ændre **vinklen** mellem felt og areal (fx en spole, der drejer – en generator).

> **Regneeksempel:** En spole med arealet $A = 0{,}020$ m² i et felt
> $B = 0{,}50$ T (vinkelret) har fluxen $\Phi = 0{,}50 \cdot 0{,}020 = 0{,}010$ Wb.

## Del 2 – Faradays induktionslov

Den inducerede spænding er lig med, hvor hurtigt fluxen ændrer sig, ganget med
antallet af vindinger:

$$\varepsilon = -N \cdot \frac{\Delta \Phi}{\Delta t}$$

Jo hurtigere ændringen sker, og jo flere vindinger spolen har, jo større spænding.

> **Regneeksempel:** En spole med $N = 200$ vindinger har en flux, der ændres fra
> $0{,}010$ Wb til $0$ på $0{,}050$ s. Da er
> $$\varepsilon = -200 \cdot \frac{0 - 0{,}010}{0{,}050} = 40 \text{ V}$$
> Størrelsen af den inducerede spænding er altså $40$ V.

## Del 3 – Lenz' lov og fortegnet

Minustegnet i Faradays lov er **Lenz' lov**: den inducerede strøm løber altid den
vej, der **modarbejder** den ændring, som skabte den.

Skub en magnets nordpol mod en spole: fluxen vokser, og den inducerede strøm
løber, så spolens nære side selv bliver en nordpol, der **frastøder** magneten.
Du skal altså udføre et **arbejde** for at presse magneten ind – og netop det
arbejde bliver til den elektriske energi. Lenz' lov er energibevarelse i
praksis; uden minustegnet kunne man få energi af ingenting.

## Del 4 – Generatoren og broen til elbilen

Drejer man en spole i et magnetfelt, ændres vinklen hele tiden, og der induceres
en **vekslende spænding** – det er en **generator**. Og her kommer den smukke
sammenhæng: en **elektromotor og en generator er den samme maskine** brugt hver
sin vej.

I en elbil betyder det, at motoren ved opbremsning kan køre "baglæns" som
generator: bilens bevægelsesenergi inducerer en spænding, der **lader batteriet
op igen**. Det kaldes regenerativ bremsning og er præcis et af elbil-forløbets
spørgsmål.

> **For de skarpe – generatorens spænding:** En spole med $N$ vindinger og areal
> $A$, der drejer med vinkelfrekvensen $\omega$ i et felt $B$, giver
> $$\varepsilon = N \cdot B \cdot A \cdot \omega \cdot \sin(\omega t)$$
> – en sinusformet vekselspænding med amplituden $N B A \omega$.

## Del 5 – Eksperiment: magnet gennem spole

**Formål:** Eftervise Faradays lov og Lenz' lov.

### Gennemførelse
- Lad en stangmagnet falde gennem en spole, der er tilsluttet et
  spændings-datalogningsudstyr (fx LoggerPro).
- Optag den inducerede spænding $\varepsilon$ som funktion af tiden.
- Gentag med større faldhøjde (større fart) og med flere vindinger.

### Iagttagelser og databehandling
- Der kommer **to pulser med modsat fortegn**: én når magneten kører **ind** i
  spolen, og én modsat, når den kører **ud**. Det er Lenz' lov direkte for øjnene.
- Større fart → større spændingstop (men kortere puls).
- Flere vindinger → større spænding.

> **For de skarpe:** Arealet under $\varepsilon$-$t$-grafen er $N \cdot \Delta\Phi$
> og er det samme uanset farten – fordi den samlede fluxændring er den samme.

> **Prøverelevant:** Den kvalitative tolkning (de to modsatte pulser) er stærk
> til den mundtlige del; dataloggingen passer til delprøven.

## Opgaver

1. En spole med arealet $0{,}015$ m² står vinkelret på et felt, der ændres fra
   $0{,}40$ T til $0{,}10$ T på $0{,}20$ s. Spolen har $150$ vindinger. Bestem
   den inducerede spænding.
2. En magnet falder gennem en spole. Forklar med Lenz' lov, hvorfor den
   inducerede strøm skifter retning, idet magneten går fra at køre ind til at
   køre ud af spolen.
3. En spole har $80$ vindinger og areal $0{,}010$ m². Hvor hurtigt skal et felt
   på $0{,}60$ T fjernes (helt til $0$), for at den inducerede spænding bliver
   $12$ V?
4. **Diskussion (bro til elbilen):** Forklar, hvorfor en elmotor kan virke som
   generator, og hvordan det bruges til at lade batteriet op under opbremsning.
   Hvilken energiform omdannes til hvilken?

> **Facit:** Opg. 1: $\Delta\Phi = (0{,}10 - 0{,}40) \cdot 0{,}015 = -4{,}5 \cdot 10^{-3}$ Wb,
> så $\varepsilon = -150 \cdot \dfrac{-4{,}5 \cdot 10^{-3}}{0{,}20} \approx 3{,}4$ V.
> Opg. 3: $\Delta\Phi = 0{,}60 \cdot 0{,}010 = 6{,}0 \cdot 10^{-3}$ Wb;
> $\Delta t = \dfrac{N \cdot \Delta\Phi}{\varepsilon} = \dfrac{80 \cdot 6{,}0 \cdot 10^{-3}}{12} = 0{,}040$ s.

## Det skal I kunne efter forløbet

- Bestemme magnetisk flux $\Phi = B \cdot A$ og kende enheden weber.
- Bruge Faradays induktionslov $\varepsilon = -N \cdot \Delta\Phi / \Delta t$.
- Forklare Lenz' lov og koble fortegnet til energibevarelse.
- Forklare generatorprincippet og sammenhængen mellem motor og generator.
- Tolke et induktionsforsøg med magnet og spole.
