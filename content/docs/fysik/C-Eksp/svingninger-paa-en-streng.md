---
title: "Svingninger på en streng"
weight: 100
---
**Niveau:** Fysik C · **Emne:** Lyd og bølger

---

## Introduktion

Når en streng spændes ud mellem to faste punkter og sættes i svingning, kan den
kun svinge i bestemte mønstre, kaldet **stående bølger**. Det dybeste mønster
kaldes **grundtonen** (kun en bug, knuder i hver ende). Skruer man frekvensen op,
rammer man **overtonerne**, hvor der kommer flere buer på snoren.

For en streng fastgjort i begge ender passer der et helt antal halve bølgelængder
ind på længden $L$. Det giver bølgelængderne:

$$\lambda_n = \frac{2 \cdot L}{n} \qquad (n = 1, 2, 3, \dots)$$

- $n = 1$: grundtonen, $\lambda_1 = 2 \cdot L$ (én bug)
- $n = 2$: første overtone, $\lambda_2 = L$ (to buer)
- $n = 3$: anden overtone, $\lambda_3 = \tfrac{2}{3} \cdot L$ (tre buer)
- … og så videre

### Sammenhængen vi vil eftervise

Bølgehastigheden, bølgelængden og perioden hænger sammen via den almindelige
bølgeformel:

$$v = \frac{\lambda}{T} \quad\Leftrightarrow\quad \lambda = v \cdot T$$

hvor

- $\lambda$ er bølgelængden i $[\text{m}]$
- $v$ er bølgens hastighed på snoren i $[\text{m/s}]$
- $T$ er svingningstiden (perioden) i sekunder, $T = \dfrac{1}{f}$

Det betyder, at hvis vi måler en række $(\lambda, T)$-værdier og **plotter
$\lambda$ op ad $y$-aksen mod $T$ ud ad $x$-aksen**, så bliver det en ret linje med
hældningen $v$:

$$\lambda = v \cdot T + \lambda_{\text{fejl}}$$

Her er $v$ hældningen (det, vi er ude efter), og $\lambda_{\text{fejl}}$ er
skæringen med $y$-aksen — en lille **b-værdi**, der ideelt skulle være $0$. At den
sjældent rammer præcis $0$, skyldes en lille systematisk fejl i, hvordan vi aflæser
bølgelængden (det er svært at se knudernes helt præcise placering). Den fortæller
altså noget om jeres måleusikkerhed.

> Det er samme idé som i [densitetsforsøget]({{< relref "densitet" >}}): hældningen
> er den fysiske størrelse, vi jagter, og b-værdien afslører en systematisk fejl.

### Den teoretiske hastighed

Hastigheden $v$ kan også beregnes ud fra, hvor hårdt snoren er spændt, og hvor tung
den er:

$$v = \sqrt{\frac{S}{\mu}}$$

- $S$ er snorens spænding (kraften, den er spændt med) i newton, $[\text{N}]$.
  Hænger der et lod med massen $m$, er $S = m \cdot g$.
- $\mu$ er snorens masse pr. længde i $\left[\dfrac{\text{kg}}{\text{m}}\right]$.

Til sidst sammenligner I den **målte** $v$ (hældningen på grafen) med den
**teoretiske** $v = \sqrt{S/\mu}$.

---

## Variabelkontrol

- **Uafhængig variabel:** svingningstiden $T$ (som vi får ved at ændre frekvensen
  og ramme de forskellige overtoner).
- **Afhængig variabel:** bølgelængden $\lambda$.
- **Kontrollerede variabler:** snorens spænding $S$ (samme lod hele vejen), snorens
  masse pr. længde $\mu$ (samme snor), og den faste længde $L$ mellem vibrator og
  trisse.

---

## Materialer

- en fiskesnor (eller tynd murersnor)
- en **vibrator**, spændt godt fast, koblet direkte til en **frekvensgenerator**
- en **trisse** (rulle) ved bordkanten, så snoren kan løbe ud over kanten
- lodder til at spænde snoren med (fx $200\text{ g}$)
- lineal / målebånd
- en vægt til at bestemme snorens masse pr. længde $\mu$

---

## Gennemførelse

1. Spænd fiskesnoren op mellem vibratoren og trissen, så den løber hen over
   trissen og ned over bordkanten, hvor loddet hænger og holder snoren stram.
   Vælg et lod (fx $200\text{ g}$), og hold det **samme** hele forsøget igennem.
2. Mål den frie længde $L$ mellem vibrator og trisse.
3. Skru langsomt op på frekvensgeneratoren, til snoren går i sin **første
   resonans** (grundtonen): kun knuder i enderne, én bug i midten. Noter
   frekvensen $f_1$.
4. Skru videre op, til I rammer **næste overtone** (to buer), og noter frekvensen.
   Fortsæt, til I har **grundtonen + 5–8 overtoner**.
5. For hver resonans noterer I ordenen $n$ og frekvensen $f$. Bølgelængden findes
   af mønsteret: $\lambda_n = \dfrac{2L}{n}$.

> **Bestem også** snorens masse pr. længde $\mu$: vej et kendt stykke snor, og
> divider massen med længden.

---

## Måletabel

| Orden $n$ | Frekvens $f$ / Hz | Bølgelængde $\lambda = \dfrac{2L}{n}$ / m |
|------|------|------|
| 1 | | |
| 2 | | |
| 3 | | |
| … | | |

---

## Databehandling i Excel

1. Lav kolonner med $n$, $f$, $\lambda$ og en ny kolonne med perioden
   $T = \dfrac{1}{f}$.
2. Plot $\lambda$ ($y$-aksen) mod $T$ ($x$-aksen) i et **Punkt (XY)**-diagram —
   *ikke* søjle eller linje, ellers skaleres $x$-aksen forkert.
3. Læg en **lineær tendenslinje** ind, og få vist ligningen ($y = a \cdot x + b$)
   og $R^2$.
4. Aflæs:
   - **hældningen** $a$ → det er den målte bølgehastighed $v$
   - **skæringen** $b$ → det er $\lambda_{\text{fejl}}$, jeres systematiske
     måleusikkerhed (ideelt $\approx 0$)
5. Beregn til sidst den **teoretiske** hastighed $v = \sqrt{\dfrac{S}{\mu}}$ med
   $S = m \cdot g$, og sammenlign med den målte hældning.

---

## Afrapportering

- Udfyldt måletabel med $n$, $f$, $\lambda$ og $T$.
- Grafen $\lambda(T)$ med tendenslinje, hældning og skæring.
- Den **målte** hastighed (hældningen) sammenlignet med den **teoretiske**
  $v = \sqrt{S/\mu}$, gerne med en procentvis afvigelse.
- En kommentar til $\lambda_{\text{fejl}}$ (b-værdien): hvor stor er den, og hvad
  fortæller den om jeres måling?
