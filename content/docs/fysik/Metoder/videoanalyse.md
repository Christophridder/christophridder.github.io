---
title: "Videoanalyse"
weight: 1
---

**Niveau: Fysik C–A** · **Emne: Bevægelse og databehandling**

[Tilbage til Faglige metoder i fysik]({{< relref "/docs/fysik/Metoder" >}})

## Kort forklaret

- Du filmer en bevægelse og markerer genstandens position i **hvert billede (frame)** af videoen.
- Programmet kender tiden mellem to frames og – når du har sat en **målestok** – afstanden i meter. Resultatet er en tabel med $t$, $x$ og $y$.
- Ud fra tabellen laver du grafer og **fits**: Hældninger og konstanter i fittene er fysiske størrelser som hastighed og tyngdeacceleration.

Metoden er god til bevægelser, der er for hurtige til at måle med stopur, men for langsomme og store til sensorer: kast, fald, stød, pendul, cykler og biler.

## Det skal du bruge

- Telefon, tablet eller kamera på **stativ** – kameraet må ikke flytte sig
- En **målestok** (fx en meterstok) i samme plan som bevægelsen
- God belysning og en genstand med god kontrast til baggrunden
- Et analyseprogram: **LoggerPro** (skolens program) eller **Tracker** (gratis)

## Sådan gør du

1. **Stil kameraet vinkelret** på det plan, bevægelsen sker i, og så langt væk, at hele bevægelsen er med. Zoom hellere lidt ind bagefter end at filme tæt på.
2. **Film bevægelsen.** Brug gerne slowmotion eller høj framerate ved hurtige bevægelser.
3. **Indlæs videoen** i programmet.
4. **Sæt skalaen:** Træk en linje hen over målestokken, og skriv dens længde.
5. **Placér koordinatsystemet:** Origo et fornuftigt sted, fx i startpunktet, med $y$-aksen opad.
6. **Markér genstanden** i hvert frame – samme punkt på genstanden hver gang (fx midten af bolden).
7. **Lav grafer og fits** af $x(t)$ og $y(t)$, og aflæs de fysiske størrelser.

> **Pas på framerate i slowmotion!** Programmet regner tiden ud fra videoens *afspilnings*-framerate, ikke den framerate, der blev *optaget* med. Filmer du i 240 fps, og afspilles videoen i 30 fps, går tiden i programmet 8 gange for langsomt. Så skal alle tider divideres med 8 – ellers bliver hastigheder 8 gange og accelerationer 64 gange for små. Tjek altid, at tiden i programmet passer med virkeligheden.

## Fra graf til fysik

| Graf | Forventet form | Det giver dig |
|---|---|---|
| $x(t)$ ved konstant hastighed | Ret linje: $x = v \cdot t + x_0$ | Hastigheden $v$ = hældningen |
| $y(t)$ ved frit fald eller kast | Parabel: $y = a_2 t^2 + a_1 t + a_0$ | Tyngdeaccelerationen $g = -2 \cdot a_2$ og starthastigheden $v_{0y} = a_1$ |
| $v(t)$ | Ret linje ved konstant acceleration | Accelerationen = hældningen |

Fit hellere en funktion til **stedgrafen** end at bruge programmets udregnede hastigheder. Hastighederne regnes ud fra små forskelle mellem to naboframes, og derfor bliver de meget støjfyldte.

## Eksempel: En bold falder

Du filmer en bold, der falder fra hvile, og fitter en parabel til $y(t)$. Programmet giver (eksempeldata):

$$y = -4{,}87 \cdot t^2 + 0{,}02 \cdot t + 1{,}49$$

Sammenlignet med $y = -\frac{1}{2} g \cdot t^2 + v_0 \cdot t + y_0$ får du:

$$g = -2 \cdot (-4{,}87 \text{ m/s}^2) = 9{,}74 \text{ m/s}^2$$

Tabelværdien i Danmark er $9{,}82$ m/s², så afvigelsen er $\frac{9{,}82 - 9{,}74}{9{,}82} \approx 0{,}8\,\%$. Leddet $0{,}02 \cdot t$ er næsten nul, som det skal være, når bolden slippes fra hvile.

**Model:** Parablen bygger på, at luftmodstanden er uden betydning. Det er rimeligt for en tung, lille bold over et fald på et par meter – men ikke for en ballon eller en kageform.

## Typiske fejlkilder

| Fejlkilde | Hvad sker der? | Hvad gør du ved det? |
|---|---|---|
| Målestok og bevægelse i forskellige afstande fra kameraet | Skalaen passer ikke – alle længder bliver for store eller for små | Hold målestokken i samme plan som bevægelsen |
| Kameraet står skævt | Afstande i billedets kant bliver forvrænget | Stil kameraet vinkelret og langt væk |
| Slørede billeder (motion blur) | Svært at markere det rigtige punkt | Mere lys, kortere lukkertid, højere framerate |
| For få frames | Grov tidsopløsning, få punkter at fitte til | Højere framerate eller slowmotion – men tjek tiden! |
| Unøjagtig markering | Punkterne "hopper" omkring den rigtige bane | Markér samme punkt hver gang, zoom ind |

## Databehandling i Python

Eksportér tabellen fra LoggerPro eller Tracker som en csv-fil med kolonnerne `t`, `x` og `y`:

```python
import numpy as np

t, x, y = np.loadtxt("kast.csv", delimiter=";", skiprows=1, unpack=True)

a2, a1, a0 = np.polyfit(t, y, 2)   # parabel til y(t)
b1, b0 = np.polyfit(t, x, 1)       # ret linje til x(t)

print(f"g    = {-2*a2:.2f} m/s^2")
print(f"v0y  = {a1:.2f} m/s")
print(f"v0x  = {b1:.2f} m/s")
```

Har filen **decimalkomma** (dansk opsætning), så læs den med pandas i stedet:

```python
import pandas as pd
df = pd.read_csv("kast.csv", sep=";", decimal=",")
t, x, y = df["t"], df["x"], df["y"]
```

## Forsøg, der bruger videoanalyse

- [Kasteparabel]({{< relref "/docs/fysik/A-Eksp/kasteparabel" >}}) – skråt kast i to dimensioner (Fysik A)
- Idé: Faldende kageforme – hvornår kan luftmodstanden ikke længere ignoreres?
- Idé: Pendul – svingningstid og dæmpning
