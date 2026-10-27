---
title: "Radianer og ωt"
weight: 10
pdf: "pdfs/radianer-omega-t.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A/B** · **Emne: Matematik – radianer, vinkelhastighed og φ = ωt**

I cirkelbevægelse og svingninger skriver vi vinklen som $\varphi = \omega \cdot t$.
Det ser mærkeligt ud, men det er **den samme regning som med sukker**:
"2 kg sukker koster 6,28 kr. Hvad koster 0,5 kg?". Den regning hedder
**reguladetri** (på tysk *Dreisatz*, på engelsk *the rule of three*).

Sukker er valgt med vilje: Ligesom tiden kan sukker deles i lige så små stykker,
du vil – du kan købe 0,72 kg. Og prisen 6,28 kr er netop $2\pi$ kr, så tallene
bliver de samme på begge sider. Kun enhederne er forskellige.

## Prøv selv

{{< sim omega-t.html 1050 >}}

Farverne betyder det samme i begge halvdele:

- <span style="color:#2563eb">**Blå**</span>: det, du har (kg sukker $m$ / tiden $t$).
- <span style="color:#16a34a">**Grøn**</span>: "prisen pr. enhed" (kr pr. kg / radianer pr. sekund $= \omega$).
- <span style="color:#ea580c">**Orange**</span>: det, du vil finde (prisen i kr / vinklen $\varphi$).

Med knappen *Samme tal begge sider* følges siderne ad. Slå den fra for at give
sukkeret en anden pris end cirklen.

## 1. Reguladetri med sukker

$Q = 2$ kg sukker koster $2\pi$ kr $\approx 6{,}28$ kr. Hvad koster $m = 0{,}5$ kg?
Det gør du i to trin: **først én, så mange**.

| | Sukker | Kroner |
|---|---|---|
| Det, du ved | $2$ kg | $2\pi$ kr $= 6{,}28$ kr |
| (1) Del med 2 | $1$ kg | $\dfrac{2\pi}{2} = \pi$ kr $= 3{,}14$ kr |
| (2) Gang med 0,5 | $0{,}5$ kg | $0{,}5 \cdot \pi = \dfrac{\pi}{2}$ kr $= 1{,}57$ kr |

Trin (1) giver **kilopris** (kr pr. kg). Så er

$$\text{pris} = \text{kr pr. kg} \cdot m = \frac{2\pi}{Q} \cdot m$$

Prisen er **proportional** med mængden. Grafen er en ret linje gennem $(0,0)$, og
hældningen er kiloprisen.

## 2. Radianer

En vinkel i **radianer** er buelængden $b$ divideret med radius $r$:

$$\varphi = \frac{b}{r}$$

- $1$ rad er den vinkel, hvor buen er **lige så lang som radius**. Slå *Radian-mærker* til i simuleringen: Mærkerne sidder med én radius' afstand langs cirklen.
- En hel omgang er hele omkredsen: $\varphi = \dfrac{2\pi r}{r} = 2\pi$. Så **$360° = 2\pi$ rad**.

Omregning mellem grader og radianer er også reguladetri:

| | Grader | Radianer |
|---|---|---|
| Det, du ved | $360°$ | $2\pi$ |
| (1) Del med 360 | $1°$ | $\dfrac{2\pi}{360} = \dfrac{\pi}{180}$ |
| (2) Gang med fx 90 | $90°$ | $90 \cdot \dfrac{\pi}{180} = \dfrac{\pi}{2}$ |

| Grader | $0°$ | $45°$ | $90°$ | $180°$ | $270°$ | $360°$ | $57{,}3°$ |
|---|---|---|---|---|---|---|---|
| Radianer | $0$ | $\pi/4$ | $\pi/2$ | $\pi$ | $3\pi/2$ | $2\pi$ | $1$ |

> **Husk lommeregneren:** Står den i grader (DEG), giver $\cos(\omega t)$ forkerte tal.
> I fysik skal den stå i **radianer** (RAD).

## 3. Vinklen $\varphi = \omega \cdot t$

Et punkt kører rundt i en cirkel med omløbstiden $T$. Du kender altså, at
**$T$ sekunder "koster" $2\pi$ radianer**. Hvor stor er vinklen efter tiden $t$?

| | Tid | Vinkel |
|---|---|---|
| Det, du ved | $T$ | $2\pi$ rad |
| (1) Del med $T$ | $1$ s | $\dfrac{2\pi}{T} = \omega$ |
| (2) Gang med $t$ | $t$ | $\omega \cdot t = \varphi$ |

Trin (1) giver **vinkelhastigheden** $\omega$ – vinklen pr. sekund. Den svarer til
kiloprisen. Enheden er rad/s. Så er

$$\varphi = \omega \cdot t \qquad \text{med} \qquad \omega = \frac{2\pi}{T} = 2\pi \cdot f$$

**Sammenligning**

| Sukker | Cirkelbevægelse |
|---|---|
| mængde $m$ (kg) | tid $t$ (s) |
| $Q$ kg koster $2\pi$ kr | $T$ sekunder svarer til $2\pi$ rad |
| kr pr. kg $= 2\pi/Q$ | $\omega = 2\pi/T$ |
| pris $= \dfrac{2\pi}{Q} \cdot m$ | $\varphi = \dfrac{2\pi}{T} \cdot t$ |
| graf: ret linje, hældning = kr pr. kg | graf: ret linje, hældning = $\omega$ |

### Vinklen bliver ved med at vokse

I simuleringen har sukkeret også en cirkel – en "pengemåler", hvor én hel omgang
er $2\pi$ kr, og hvert radian-mærke er 1 kr. Køber du mere sukker, kører viseren
rundt igen, men **prisen bliver ved med at vokse**: $2\pi$ kr, $4\pi$ kr, $6\pi$ kr, …

Sådan er det også med vinklen. Efter hver omgang er punktet tilbage, hvor det
startede, men $\varphi$ fortsætter: $2\pi$, $4\pi$, $6\pi$, …

Det er helt i orden, fordi $\cos$ og $\sin$ gentager sig med perioden $2\pi$:

$$\cos(\varphi + 2\pi) = \cos(\varphi)$$

Derfor kan vi skrive punktets position som
$\vec r(t) = \begin{pmatrix} r \cdot \cos(\omega t) \\ r \cdot \sin(\omega t) \end{pmatrix}$
uden at tænke på, hvor mange omgange der er gået. Se siden om
[jævn cirkelbevægelse]({{< relref "jaevn-cirkelbevaegelse" >}}).

> **Når $\omega$ ikke er konstant.** $\varphi = \omega \cdot t$ gælder kun, når
> vinkelhastigheden er konstant – præcis som "pris = enhedspris · antal" kun gælder,
> når kiloprisen er den samme for alt sukkeret. Ændrer $\omega$ sig, er vinklen arealet under
> $(t, \omega)$-grafen: $\varphi = \displaystyle\int_0^t \omega\, \mathrm{d}t$. Se
> [Integration i fysik]({{< relref "integration-i-fysik" >}}).

## Opgaver

1. **Sukker.**
   a) $2{,}5$ kg sukker koster $30$ kr. Hvad koster $4$ kg? Skriv begge trin.
   b) $1{,}5$ kg sukker koster $2\pi$ kr. Hvad koster $4{,}5$ kg? Giv svaret både med $\pi$ og i kr.
2. **Omregning.** Omregn $90°$ og $45°$ til radianer, og $1$ rad og $2{,}5$ rad til grader.
3. **Karrusel.** En karrusel kører én gang rundt på $12$ s.
   a) Bestem vinkelhastigheden $\omega$.
   b) Bestem vinklen efter $4{,}0$ s i radianer og grader.
   c) Bestem vinklen efter $30$ s. Hvor mange omgange er det, og hvor er stolen i forhold til start?
4. **Jorden.** Jorden drejer én gang om sig selv på et stjernedøgn, $T = 86\,164$ s.
   Bestem $\omega$ og den vinkel, Jorden drejer på $6$ timer.
5. **Cykelhjul.** Et hjul med radius $0{,}30$ m drejer $10$ omgange pr. sekund.
   Bestem $\omega$ og farten $v = \omega \cdot r$ af et punkt på hjulets kant.

## Facit

| Opgave | Facit |
|---|---|
| 1a | (1) $30/2{,}5 = 12$ kr pr. kg. (2) $4 \cdot 12 = 48$ kr |
| 1b | (1) $2\pi/1{,}5 = 4{,}19$ kr pr. kg. (2) $4{,}5 \cdot 2\pi/1{,}5 = 6\pi$ kr $= 18{,}85$ kr (tre "omgange") |
| 2 | $90° = \pi/2 = 1{,}57$ rad, $45° = \pi/4 = 0{,}785$ rad. $1$ rad $= 57{,}3°$, $2{,}5$ rad $= 143°$ |
| 3a | $\omega = 2\pi/12 = 0{,}524$ rad/s |
| 3b | $\varphi = 2{,}09$ rad $= 2\pi/3 = 120°$ |
| 3c | $\varphi = 15{,}7$ rad $= 5\pi$, dvs. $2{,}5$ omgange. Stolen er lige over for startpunktet |
| 4 | $\omega = 7{,}29 \cdot 10^{-5}$ rad/s. $\varphi = 1{,}58$ rad $\approx 90°$ |
| 5 | $\omega = 2\pi \cdot 10 = 62{,}8$ rad/s, $v = 18{,}8$ m/s |

## Det skal du kunne

- Løse et reguladetri-problem i to trin: først én, så mange.
- Forklare, hvad $1$ radian er, og omregne mellem grader og radianer.
- Forklare $\omega = 2\pi/T$ som "vinkel pr. sekund" og bruge $\varphi = \omega \cdot t$.
- Forklare, hvorfor $\varphi$ må blive større end $2\pi$.
