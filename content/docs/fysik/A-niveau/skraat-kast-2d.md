---
title: "Skråt kast – bevægelse i to dimensioner"
weight: 2
---

**Niveau: Fysik A** · **Emne: Mekanik – kinematik i 2D** · **Eksperiment: videoanalyse**

Forløbet bygger den todimensionale bevægelse op fra det helt centrale princip –
at vandret og lodret bevægelse er uafhængige – og fører over i et
videoanalyse-eksperiment, som ligger tæt op ad den eksperimentelle delprøve.
Til sidst udvides med luftmodstand, hvor en simulering bruges, fordi der ikke
findes en simpel formel.

## Del 1 – Bevægelse i to dimensioner (teori)

### Det bærende princip: uafhængighed

Et skråt kast er to bevægelser på én gang:

- **Vandret (x):** ingen kraft (ser vi bort fra luftmodstand) → konstant fart.
- **Lodret (y):** tyngdekraften virker → konstant acceleration $g$.

De to retninger påvirker ikke hinanden. Tyngdekraften ændrer kun den lodrette
fart, aldrig den vandrette. Det var Galileis gennembrud, og det er nøglen til
hele kapitlet.

### Opløsning af starthastigheden

Kastes med farten $v_0$ under vinklen $\alpha$ over vandret:

$$v_{0x} = v_0 \cdot \cos\alpha \qquad v_{0y} = v_0 \cdot \sin\alpha$$

### Bevægelsesligningerne

Med startpunkt i origo og $g = 9{,}82$ m/s² (Danmark):

$$x(t) = v_{0x} \cdot t \qquad y(t) = v_{0y} \cdot t - \tfrac{1}{2} \cdot g \cdot t^2$$

$$v_x(t) = v_{0x} \qquad v_y(t) = v_{0y} - g \cdot t$$

### Afledte størrelser

| Størrelse | Formel | Hvornår |
|---|---|---|
| Tid til toppunkt | $t_{\text{top}} = \dfrac{v_{0y}}{g}$ | når $v_y = 0$ |
| Største højde | $y_{\text{max}} = \dfrac{v_{0y}^2}{2 \cdot g}$ | i toppunktet |
| Flyvetid (samme højde) | $T = \dfrac{2 \cdot v_{0y}}{g}$ | tilbage til udgangshøjde |
| Kastelængde (vandret) | $R = \dfrac{v_0^2 \cdot \sin(2\alpha)}{g}$ | størst ved $\alpha = 45^\circ$ |

Banen er en **parabel**. Sætter man $t$ fra $x$-ligningen ind i $y$-ligningen:

$$y = x \cdot \tan\alpha - \frac{g \cdot x^2}{2 \cdot v_0^2 \cdot \cos^2\alpha}$$

> **Regneeksempel:** $v_0 = 12$ m/s, $\alpha = 40^\circ$ giver
> $v_{0x} = 9{,}19$ m/s og $v_{0y} = 7{,}71$ m/s. Heraf
> $t_{\text{top}} = 0{,}79$ s, $y_{\text{max}} = 3{,}0$ m, $T = 1{,}6$ s og
> $R = 14{,}4$ m. Tjek selv: $R = v_{0x} \cdot T$ giver det samme.

## Del 2 – Eksperiment: videoanalyse af skråt kast

**Formål:** Bestemme banen for et skråt kast og sammenligne med den forventede
parabel for fri bevægelse i tyngdefeltet – herunder at bestemme $g$ ud fra data.

### Udstyr
- Kamera eller tablet på stativ, vinkelret på kasteplanet.
- En **målestok i billedet** (fx en meterstok) til kalibrering af afstande.
- Bold med tydelig kontrast til baggrunden.
- LoggerPro (eller Tracker) til videoanalyse, derefter Excel til databehandling.

### Gennemførelse
1. Film kastet, så hele banen er i billedet, og målestokken er synlig.
2. Kalibrér længdeskalaen i LoggerPro ud fra målestokken.
3. Sæt punkter på bolden frame for frame, og udtræk $x$ og $y$ som funktion af $t$.

> **Vigtig faldgrube (censor-erfaring):** LoggerPro bruger videoens
> **afspilnings-framerate**, ikke optage-frameraten. Med almindelig optagelse
> (fx 25 eller 30 fps) passer tiden. Men optager I i **slowmotion/high-speed**
> (fx 240 fps), skal den rigtige tid skaleres:
> $$t_{\text{rigtig}} = t_{\text{logget}} \cdot \frac{\text{afspilnings-fps}}{\text{optage-fps}}$$
> Fejlen forplanter sig: farten bliver forkert med skaleringsfaktoren, og en
> eventuel $g$-bestemmelse endnu mere. Tjek frameraten, før I regner.

### Databehandling i Excel
- **Vandret:** Plot $x$ mod $t$. Punkterne ligger på en ret linje → hældningen er
  $v_{0x}$. Det bekræfter, at den vandrette fart er konstant.
- **Lodret:** Plot $v_y$ mod $t$ (eller $y$ mod $t$ som parabel). $v_y$ mod $t$
  giver en ret linje med hældning $-g$ → bestem $g$ og sammenlign med $9{,}82$ m/s².
- Bestem $v_0$ og $\alpha$ ud fra $v_{0x}$ og $v_{0y}$.

### Afrapportering
- Diagrammer for $x(t)$, $y(t)$ og $v_y(t)$ med tilhørende fits.
- Den bestemte værdi af $g$ med afvigelse fra tabelværdien.
- Diskussion: passer banen med en parabel? Hvor kommer afvigelserne fra?

> **Prøverelevant:** Dette eksperiment svarer til den eksperimentelle delprøve
> (jf. Egaa-spørgsmål A). Hold derfor analysen i LoggerPro + Excel – det er det,
> eleverne skal kunne stå på egne ben med til prøven.

## Del 3 – Luftmodstand (udvidelse)

For en let bold (skumbold, badebold) holder den ideelle parabel ikke. Luften
bremser bevægelsen med en kraft modrettet farten:

$$F_{\text{luft}} = \tfrac{1}{2} \cdot \rho \cdot C_d \cdot A \cdot v^2$$

hvor $\rho$ er luftens massefylde, $C_d$ formfaktoren og $A$ tværsnitsarealet.
Accelerationen fra luftmodstand er $a = F_{\text{luft}}/m$, så en **let** bold
med stort areal påvirkes meget mere end en tung. Resultatet:

- Banen bliver **asymmetrisk** – nedturen er stejlere end opturen.
- Kastelængden bliver kortere, og toppunktet rykker mod kastestedet.

Der findes ingen pæn løsningsformel, så vi **simulerer** banen i små tidsskridt.

> **Om Python her:** Simuleringen er til forståelse og lærerdemo – ikke et
> eksamensværktøj. Den viser, hvordan luftmodstand ændrer banen, men selve
> dataanalysen (Del 2) klares i LoggerPro/Excel.

```python
import numpy as np
import matplotlib.pyplot as plt

g = 9.82          # tyngdeacceleration [m/s^2]
dt = 0.001        # tidsskridt [s]

def kast(v0, vinkel_grader, k_over_m):
    """Simulerer et skråt kast med luftmodstand proportional med v^2.
    k_over_m er konstanten (0.5*rho*Cd*A)/m. Sæt 0 for intet luftmodstand."""
    a = np.radians(vinkel_grader)
    vx, vy = v0 * np.cos(a), v0 * np.sin(a)
    x, y = 0.0, 0.0
    xs, ys = [x], [y]
    while y >= 0:
        v = np.hypot(vx, vy)
        ax = -k_over_m * v * vx
        ay = -g - k_over_m * v * vy
        vx, vy = vx + ax * dt, vy + ay * dt
        x, y = x + vx * dt, y + vy * dt
        xs.append(x); ys.append(y)
    return xs, ys

# Sammenlign tung bold (lille k/m) med let skumbold (stor k/m)
for k, navn in [(0.0, "ingen luft"), (0.02, "tung bold"), (0.15, "skumbold")]:
    xs, ys = kast(12, 40, k)
    plt.plot(xs, ys, label=navn)

plt.xlabel("x [m]"); plt.ylabel("y [m]"); plt.legend(); plt.show()
```

## Opgaver

1. En bold kastes med $v_0 = 15$ m/s under $35^\circ$. Bestem flyvetid, største
   højde og kastelængde (uden luftmodstand).
2. Vis, at kastelængden er størst ved $\alpha = 45^\circ$, og argumentér ud fra
   formlen for $R$.
3. I et videoforsøg aflæses den vandrette fart til $9{,}0$ m/s og den lodrette
   starthastighed til $6{,}5$ m/s. Bestem $v_0$ og kastevinklen $\alpha$.
4. **Diskussion:** En skumbold og en petanquekugle kastes ens. Forklar ud fra
   $a = F_{\text{luft}}/m$, hvorfor skumboldens bane afviger mest fra parablen.

## Det skal I kunne efter forløbet

- Opløse en starthastighed i vandret og lodret komposant.
- Opstille og bruge bevægelsesligningerne for skråt kast i to dimensioner.
- Gennemføre en videoanalyse og bestemme $g$, $v_0$ og $\alpha$ ud fra data.
- Forklare, hvordan luftmodstand ændrer banen, og hvornår parabel-modellen er
  en god beskrivelse (modellens gyldighedsområde).
