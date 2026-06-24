---
title: "Afstandskvadratloven"
weight: 80
---
**Niveau:** Fysik C · **Emne:** Radioaktivitet (γ-stråling)

---

## Introduktion

Når stråling spreder sig fra en lille kilde, fordeles den ud over en stadig større
kugleflade, jo længere væk man kommer. Derfor falder intensiteten ikke bare med
afstanden — den falder med **kvadratet** på afstanden. Det kaldes
**afstandskvadratloven**, og den gælder for al stråling fra en punktkilde: lys,
lyd og her $\gamma$-stråling.

### Teori

Forestil dig en punktkilde, der udsender stråling i alle retninger. I afstanden
$r$ er strålingen fordelt jævnt ud over overfladen af en kugle med radius $r$.
Kuglens overflade er

$$O = 4\pi \cdot r^2$$

Da den samlede udsendte energi er den samme uanset afstand, men fordeles over et
areal, der vokser med $r^2$, bliver intensiteten $I$ (her det korrigerede
tælletal):

$$I = \frac{k}{r^2}$$

hvor

- $I$ er intensiteten (korrigeret tælletal) i afstanden $r$
- $r$ er afstanden mellem kilde og GM-rør i $\text{m}$ (eller cm)
- $k$ er en konstant, der afhænger af kildens styrke

Det betyder, at hvis du **fordobler** afstanden, falder intensiteten til en
**fjerdedel**; tredobler du afstanden, falder den til en niendedel.

> **For de skarpe:** Ganger man begge sider med $r^2$, får man $I \cdot r^2 = k$,
> altså en konstant. En måde at teste loven på er derfor at tjekke, om produktet
> $I \cdot r^2$ er nogenlunde det samme for alle dine målinger.

---

## Variabelkontrol

- **Uafhængig variabel:** afstanden $r$ mellem kilde og GM-rør.
- **Afhængig variabel:** det korrigerede tælletal pr. måleinterval.
- **Kontrollerede variabler:** måletiden, samme kilde og samme GM-rør,
  samme måleopstilling.

---

## Materialer

- $\gamma$-kilde
- GM-rør med tæller
- lineal / målebånd
- stopur / timer

---

## Gennemførelse

1. Bestem baggrundsstrålingen $B$ for det måleinterval, du vil bruge.
2. Placér kilden i en kendt afstand $r$ fra GM-røret, og mål tælletallet.
3. Gentag for en række forskellige afstande — gerne fra helt tæt på til så langt
   væk, at tælletallet nærmer sig baggrunden.
4. Beregn det korrigerede tælletal ved at trække $B$ fra.

### Måletabel

| Afstand $r$ | $r^2$ | Tælletal | B | Korrigeret tælletal $I$ | $I \cdot r^2$ |
|------|------|------|------|------|------|
| | | | | | |
| | | | | | |
| | | | | | |

---

## Databehandling i Excel

Du kan teste afstandskvadratloven på to måder:

**1) Plot** $I$ **mod** $r$ — korrigeret tælletal ($y$) mod afstand ($x$). Du
skulle gerne se en kurve, der falder stejlt og så fladere ud (formen $1/r^2$).

**2) Plot** $I$ **mod** $1/r^2$ — hvis loven holder, ligger punkterne på en **ret
linje** gennem origo. Det er den klareste test.

Sådan gør du i Excel:

1. Lav kolonner med $r$, $r^2$, $1/r^2$ og korrigeret tælletal.
2. Markér de to kolonner, du vil plotte, og indsæt et diagram af typen
   **Punkt (XY)** — *ikke* søjle eller linje, ellers skaleres $x$-aksen forkert.
3. Læg en lineær tendenslinje ind på $I$-mod-$1/r^2$-plottet, og se, hvor godt
   punkterne følger en ret linje (aflæs $R^2$).

---

## Afrapportering

- Udfyldt måletabel inkl. kolonnen $I \cdot r^2$.
- Grafen, der bedst viser sammenhængen ($I$ mod $1/r^2$).
- En vurdering af, om afstandskvadratloven holder: Er produktet $I \cdot r^2$
  nogenlunde konstant? Hvor godt følger punkterne den rette linje?
- Diskutér mulige fejlkilder (fx at kilden ikke er en perfekt punktkilde, eller
  at GM-røret har en udstrækning).
