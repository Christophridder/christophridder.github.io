---
title: Gnidning
weight: 1
---

# Gnidning

Prøv at skubbe en tung kasse hen ad gulvet. Du mærker straks en modstand — en kraft der trækker i den modsatte retning af din bevægelse. Det er **gnidning**, og det er én af de mest hverdagsagtige kræfter vi kender.

Gnidning opstår fordi ingen overflade er perfekt glat. Selv poleret metal har uregelmæssigheder på mikroskala, og det er disse "bakker og dale" der hænger fast i hinanden og modvirker bevægelse.

## Normalkraften

Inden vi kan tale om gnidning, skal vi have styr på **normalkraften** $F_N$. Normalkraften er den kraft en overflade udøver *vinkelret* (normalt) på et legeme der hviler på den — den er med andre ord overflades modsvar til tyngdekraften.

![Normalkraften på vandret overflade og skråplan](/img/normalkraft-illustration.svg)

På en **vandret overflade**:

$$F_N = mg$$

På et **skråplan** med vinkel $\theta$ er normalkraften mindre, fordi tyngdekraften ikke peger direkte ned mod overfladen:

$$F_N = mg\cos(\theta)$$

| Størrelse | Symbol | Enhed | Beskrivelse |
|---|---|---|---|
| Gnidningskraft | $F$ | N | Modvirker bevægelse eller tilbøjelighed til bevægelse |
| Normalkraft | $F_N$ | N | Kraft vinkelret på overfladen |
| Gnidningskoefficient | $\mu$ | — (dimensionsløs) | Afhænger kun af materialerne |
| Masse | $m$ | kg | Klodsens masse |
| Tyngdeacceleration | $g$ | m/s² | $g = 9{,}82\ \text{m/s}^2$ |
| Vinkel | $\theta$ | ° eller rad | Hældningsvinkel |

## To slags gnidning

Der er to former for gnidning som kaldes **statisk** og **dynamisk** gnidning, de har hver sin **gnidningskoefficient** $\mu$ (det græske bogstav *my*). $\mu$ er et tal uden enhed der beskriver, hvor meget to overflader "klistrer" til hinanden:

$$F_s \leq \mu_s \cdot F_N \qquad \text{(statisk gnidning)}$$

$$F_k = \mu_k \cdot F_N \qquad \text{(kinetisk/dynamisk gnidning)}$$

Det gælder altid at $\mu_k < \mu_s$ — det er sværere at sætte noget i gang end at holde det kørende, når det først glider.

---

## Statisk gnidning

Forestil dig du står på ski øverst på en piste. Skiene hviler på sneen, men du bevæger dig ikke endnu — selvom du er på et skråplan. Det skyldes **statisk gnidning**: overfladen holder fast og modvirker begyndende bevægelse.

Den statiske gnidningskraft er *ikke* konstant. Den tilpasser sig præcis til hvad der skal til for at holde legemet stillet — men den har et maksimum:

$$F_s \leq \mu_s \cdot N$$

Ulighedstegnet er afgørende. Så snart den ydre kraft overstiger $\mu_s \cdot N$, begynder legemet at glide, og vi skifter til dynamisk gnidning.

<div style="text-align:center">
  <img src="/img/gnidning-mikroskala.svg" alt="Kemiske bindinger mellem overfladeatomer på atomskala" width="70%">
</div>


Som man kan se i ovenstående figur skal årsagen til statisk gnidning findes på atomskala: de to overfladers uregelmæssigheder griber ind i hinanden og danner kortvarige kemiske bindinger. Jo "klistredere" materialerne er overfor hinanden, jo større er $\mu_s$.


### Tabelværdier for statisk gnidning


| Materialer | $\mu_s$ (ca.) |
|---|---|
| Træ på træ | 0,35–0,45 |
| Stål på stål (tørt) | 0,15–0,20 |
| Gummi på asfalt | 0,80–1,0 |
| Is på is (0 °C) | 0,07–0,12 |
| Beton på beton | 0,50–0,70 |


Bemærk: $\mu_s$ afhænger *ikke* af kontaktfladens størrelse eller klodsens masse — kun af materialekombinationen. Det er lidt sjovt.  

### $\mu_s$ fra hældningsforsøget

En elegant metode til at bestemme $\mu_s$ er at placere en klods på en plade og løfte den ene ende gradvist, indtil klodsen begynder at glide. I det øjeblik klodsen *netop* begynder at glide, er systemet i grænseligevægt.

Betragt kræfterne på skråplanet med vinkel $\theta$:

$F_N = mg\cos(\theta) \qquad \text{(normalkraft)}$

$F_\parallel = mg\sin(\theta) \qquad \text{(tyngdekraftens komponent lodret ned)}$

$F_s = \mu_s \cdot F_N = \mu_s \cdot mg\cos(\theta) \qquad \text{(statisk gnidningskraft)}$

Ved den **kritiske vinkel** $\theta_c$ er gnidningskraften netop stor nok til at holde klodsen:

$$
F_s = F_\parallel 
$$

$$
\mu_s \cdot \cancel{mg}\cos(\theta_c) = \cancel{mg}\sin(\theta_c) 
$$

$$\boxed{\mu_s = \frac{\sin(\theta_c)}{\cos(\theta_c)} = \tan(\theta_c)}$$

Massen $m$ falder ud af ligningen — det er netop derfor $\mu_s$ ikke afhænger af massen.

> [!NOTE]
> **Måling uden vinkelmåler**
>
> I praksis er det lettere at måle **pladelængden** $L$ (hypotenusen) og **løftehøjden** $h$ (den modstående katete) end at måle vinklen direkte.
>
> Fra den retvinklede trekant: $\sin(\theta) = h/L$ og $\cos(\theta) = \sqrt{L^2 - h^2}/L$
>
> Indsættes i $\mu_s = \tan(\theta_c)$:
>
> $$\mu_s = \frac{h}{\sqrt{L^2 - h^2}}$$
>
> Ingen vinkelmåler nødvendig — kun en lineal.

### Opgave — statisk gnidning

Brug **simulationen i bunden af siden** (fanen *Hældningsforsøg*).

1. Vælg overfladen **Træ på træ** og sæt massen til 1,0 kg.
2. Øg langsomt vinklen med slideren. Notér den kritiske vinkel $\theta_c$ hvor klodsen begynder at glide.
3. Beregn $\mu_s = \tan(\theta_c)$ og sammenlign med tabelværdien $\mu_s \approx 0{,}40$.
4. Skift nu til **Is på is** og gentag. Hvad er den kritiske vinkel nu?
5. Prøv at ændre massen — hvad sker der med $\theta_c$? Er det hvad du forventede ud fra formlen?

---

Når klodsen — eller skiene — er kommet i gang med at glide, tager en anden slags gnidning over.

---

## Dynamisk gnidning

**Dynamisk gnidning** (også kaldet *kinetisk gnidning*) er den gnidningskraft der virker *mens* et legeme er i bevægelse. I modsætning til statisk gnidning er den konstant og afhænger kun af normalkraften og materialerne:

$$F_k = \mu_k \cdot N$$

På en vandret overflade er $N = mg$, og for at trække en klods med konstant hastighed skal man udøve en kraft der præcis opvejer gnidningskraften:

$$F = F_k = \mu_k \cdot m \cdot g$$

Trækker man hårdere end $F_k$ accelererer klodsen. Trækker man svagere bremser den op. Konstant hastighed kræver præcis ligevægt.

### Tabelværdier for dynamisk gnidning

| Materialer | $\mu_k$ (ca.) |
|---|---|
| Træ på træ | 0,25–0,35 |
| Stål på stål (tørt) | 0,09–0,12 |
| Gummi på asfalt | 0,60–0,80 |
| Is på is (0 °C) | 0,03–0,06 |
| Beton på beton | 0,40–0,55 |

### Bestemmelse af $\mu_k$ via lineær regression

Siden $F = \mu_k \cdot g \cdot m$ er en lineær funktion af massen $m$ der går igennem origo, kan man bestemme $\mu_k$ ved at måle $F$ for flere forskellige masser og lave en lineær regression:

$$F = a \cdot m \qquad \Rightarrow \qquad \mu_k = \frac{a}{g}$$

Jo flere datapunkter, jo mere præcist resultat.

### Opgave — dynamisk gnidning

Brug **simulationen i bunden af siden** (fanen *Trækforsøg*).

1. Vælg **Stål på stål**.
2. Sæt massen til 0,5 kg og klik *Træk klodsen* — hvad viser newtonmetret?
3. Klik *Registrér måling*.
4. Gentag for $m = 1{,}0,\ 1{,}5,\ 2{,}0$ og $2{,}5$ kg.
5. Aflæs $\mu_k$ fra regressionsgrafen og sammenlign med tabelværdien $\mu_k \approx 0{,}10$.
6. Hvad er $R^2$ for din regression? Hvad siger det om den lineære sammenhæng?

---

## Simulation

{{< sim gnidning.html 760 >}}

---

## Forsøg i klassen

Nu er det tid til at prøve det med rigtige klodser, en plade og et newtonmeter.

### Del 1 — Statisk gnidning med hældningsforsøget

**Udstyr:** Plade (fx et spækbræt), klods, lineal eller målebånd.

**Fremgangsmåde:**

1. Placer klodsen på pladen og hold pladen vandret på bordet.
2. Løft langsomt den ene ende af pladen.
3. I det **præcise øjeblik** klodsen begynder at glide, stopper du og måler:
   - $L$: pladens fulde længde fra kant til kant langs pladen (hypotenusen)
   - $h$: højden af den løftede ende over bordoverfladen (den modstående katete)
4. Beregn:

$$\mu_s = \frac{h}{\sqrt{L^2 - h^2}}$$

5. Gentag forsøget mindst 3 gange og beregn et gennemsnit.

**Spørgsmål til diskussion:**
- Stemmer dit $\mu_s$ med tabelværdien?
- Hvad sker der hvis du lægger et lod oven på klodsen — ændrer $\theta_c$ sig?
- Prøv med to forskellige overflader (fx glat og ru side af pladen). Hvad er forskellen i $\mu_s$?

---

### Del 2 — Dynamisk gnidning med newtonmeter

**Udstyr:** Plade (vandret), klods, lodder, newtonmeter.

**Fremgangsmåde:**

1. Læg pladen vandret og fastgør newtonmetret til klodsen.
2. Træk klodsen med **lav, konstant hastighed** mens du aflæser newtonmetret.
   *(Konstant hastighed er afgørende: accelererer klodsen måler du mere end gnidningskraften alene.)*
3. Notér $F$ når nålen er stabil.
4. Gentag med mindst 5 forskellige masser (fx 200 g, 500 g, 1,0 kg, 1,5 kg, 2,0 kg).
5. Indtast dine målinger i regnearket nedenfor.

Regnearket beregner $\mu_k$ for hver enkelt måling og laver automatisk en lineær regression med graf. Klik **Kopier til Excel** for at tage data med videre.

{{< sim gnidning-data.html 800 >}}
