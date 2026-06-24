---
title: "Lydens hastighed"
weight: 90
---
**Niveau:** Fysik C · **Emne:** Lyd og bølger


## Introduktion

Lyd er en longitudinal bølge, der bevæger sig gennem luften med en bestemt hastighed. Lydbølger er trykændringer i luften, dvs at trykket varierer over en bølgelængde i samme retning som lyden udbreder sig. Det er det der gør bølgen **longitudinal** 

Ved stuetemperatur er lydens hastighed i luft ca. $343\text{ m/s}$. I denne øvelse
bestemmer I selv lydens hastighed på **to forskellige måder** og sammenligner
resultaterne.

Grundformlen er den simple sammenhæng mellem strækning, tid og hastighed:

$$v = \frac{s}{t}$$

hvor

- $v$ er hastigheden i $[\text{m/s}]$
- $s$ er den tilbagelagte strækning i $[\text{m}]$
- $t$ er tiden i sekunder, $[\text{s}]$

---

## Metode 1: Ekko i idrætsgården

I denne metode bruger I et **ekko**: lyden sendes af sted, rammer en mur i den
anden ende af gården, og kommer tilbage. Tricket er at klappe i takt med sit eget
ekko, så man slipper for at måle en enkelt, meget kort tid.

### Variabelkontrol

- **Uafhængig variabel:** antal klap (vi tæller et fast antal).
- **Afhængig variabel:** den samlede tid for klappene.
- **Kontrollerede variabler:** afstanden $L$ til muren, samme person der klapper,
  samme sted. Vigtigt er at I står så tæt på muren som muligt når i klapper. 

### Gennemførelse

1. Mål afstanden $L$ fra jer hen til muren i den anden ende af gården (i meter).
2. Stå med et klaptræ, og klap, så hvert nyt klap falder **præcis sammen med
   ekkoet** af det forrige. Find en fast, jævn rytme. Læg mærke til at man skal klappe **ret hurtigt** !!
3. Når rytmen er stabil, måler I tiden for **20 klap**.

### Databehandling

For hvert klap når lyden **hen til muren og tilbage igen** — altså strækningen
$2L$ — før næste klap. Tiden mellem to klap er derfor tiden for lyden at rejse
$2L$.

- Tiden for ét klap-interval: $\quad t_1 = \dfrac{t_{20}}{20}$
- Strækningen pr. interval: $\quad s = 2 \cdot L$
- Lydens hastighed:

$$v = \frac{s}{t_1} = \frac{2 \cdot L}{t_1} = \frac{2 \cdot L \cdot 20}{t_{20}}$$

Indsæt jeres målte $L$ og $t_{20}$, og beregn $v$. Sammenlign med $343\text{ m/s}$.

---

## Metode 2: To mikrofoner i LoggerPro

Her måler I tiden direkte: en lyd når den **nærmeste** mikrofon lidt før den
**fjerneste**, fordi den skal rejse en ekstra strækning. Den lille tidsforskel kan
aflæses i LoggerPro.

### Variabelkontrol

- **Uafhængig variabel:** afstanden mellem de to mikrofoner.
- **Afhængig variabel:** tidsforskellen mellem de to optagne signaler.
- **Kontrollerede variabler:** samme lydkilde, samme opstilling, samme
  samplingsrate i LoggerPro.

### Gennemførelse

1. Stil de to mikrofoner op på en lige linje med præcis $1\text{ m}$ imellem dem.
2. Tilslut dem til LoggerPro, og lav en lyd (fx et klap) ud for den nærmeste
   mikrofon, så lyden bevæger sig hen langs linjen.
3. Optag, så I ser to kurver — én for hver mikrofon. Den fjerneste mikrofon
   registrerer lyden lidt senere end den nærmeste.

### Databehandling

- Aflæs i LoggerPro, hvornår signalet starter på hver af de to kurver, og find
  **tidsforskellen** $t$ mellem dem.
- Strækningen $s$ er afstanden mellem mikrofonerne ($1\text{ m}$).
- Beregn lydens hastighed:

$$v = \frac{s}{t}$$

Sammenlign med både $343\text{ m/s}$ og jeres resultat fra metode 1.

---

## Afrapportering

- Måledata og beregnet $v$ for **begge** metoder.
- En sammenligning af de to resultater og af tabelværdien $343\text{ m/s}$.
- En diskussion af, hvilken metode der gav det mest præcise resultat, og hvorfor.

---

## Opgave

Et lyn slår ned. Du ser lyset næsten med det samme, men det tager lyden
$6\text{ sekunder}$ at nå frem til dig bagefter. **Hvor langt væk er uvejret?**

> *Hint: Lyset rejser så hurtigt, at vi kan se bort fra dets rejsetid. Brug
> $v = \dfrac{s}{t}$ med lydens hastighed.*
