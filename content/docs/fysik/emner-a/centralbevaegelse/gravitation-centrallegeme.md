---
title: "Gravitation og bevægelse om et centrallegeme"
weight: 5
---

**Niveau: Fysik A** · **Emne: Mekanik – gravitation** · **Simulering: planetbane**

Forløbet udvider satellit-opgaven fra cirkelbevægelsen til den fulde
gravitationslov, Keplers tre love og energiforholdene i gravitationsfeltet.
Keplers love er omdrejningspunktet – inklusive en udledning af 3. lov for den
cirkulære bane.

## Del 1 – Newtons gravitationslov

To masser tiltrækker hinanden med kraften

$$F = G \cdot \frac{m_1 \cdot m_2}{r^2}$$

med gravitationskonstanten $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg². Loven er
universel – den samme kraft holder på Månen, Jorden om Solen og et æble på vej
mod jorden.

Et centrallegeme med masse $M$ sætter et **tyngdefelt** op. Feltstyrken i
afstanden $r$ er

$$g = \frac{G \cdot M}{r^2}$$

Ved Jordens overflade ($r = R$) giver det netop $g = 9{,}82$ m/s² – samme $g$ som
i tyngdefeltet nær jorden.

## Del 2 – Bevægelse om et centrallegeme

For en cirkulær bane leverer tyngdekraften centripetalkraften (jf.
cirkelbevægelsen):

$$\frac{G \cdot M \cdot m}{r^2} = \frac{m \cdot v^2}{r} \quad\Longrightarrow\quad v = \sqrt{\frac{G \cdot M}{r}}$$

Farten afhænger altså kun af centrallegemets masse og baneradius – ikke af det
kredsende legemes egen masse.

## Del 3 – Keplers love

Johannes Kepler fandt i begyndelsen af 1600-tallet tre love for planeternes
bevægelse – baseret på **Tycho Brahes** usædvanligt nøjagtige observationer af
især Mars, indsamlet på Hven. Lovene kom altså før Newtons gravitationslov, men
følger smukt af den.

### 1. lov – ellipseloven
Planeterne bevæger sig i **ellipsebaner** med Solen i det ene brændpunkt. En
cirkel er specialtilfældet, hvor de to brændpunkter falder sammen.

### 2. lov – fladeloven
En linje fra Solen til planeten **overstryger lige store arealer i lige store
tidsrum**.

Konsekvensen: planeten bevæger sig **hurtigst tæt på Solen** (perihel) og
**langsomst langt væk** (aphel). Det er i virkeligheden bevarelse af
bevægelsesmængdemoment.

### 3. lov – periodeloven
Kvadratet på omløbstiden er proportional med tredje potens af den store halvakse
$a$:

$$\frac{T^2}{a^3} = \text{konstant}$$

Konstanten er den samme for alle legemer om samme centrallegeme.

> **Udledning for den cirkulære bane (A-niveau):** Sæt $v = \dfrac{2\pi r}{T}$ ind
> i $v = \sqrt{G M / r}$:
> $$\frac{G \cdot M}{r^2} = \frac{v^2}{r} = \frac{4\pi^2 r}{T^2} \quad\Longrightarrow\quad T^2 = \frac{4\pi^2}{G \cdot M} \cdot r^3$$
> Altså $T^2 \propto r^3$ – netop Keplers 3. lov, nu udledt fra Newton.

> **Regneeksempel:** For Jorden er $T = 1$ år og $a = 1$ AE, så $T^2/a^3 = 1$
> (i disse enheder). Mars har $a = 1{,}52$ AE, så
> $T = \sqrt{1{,}52^3} = 1{,}87$ år – tæt på den målte værdi på $1{,}88$ år.

## Del 4 – Energi i gravitationsfeltet

Den potentielle energi i et centrallegemes felt regnes med **nul i det
uendelige**, så for et bundet legeme er den negativ:

$$E_{\text{pot}} = -\frac{G \cdot M \cdot m}{r}$$

Sammen med $E_{\text{kin}} = \tfrac{1}{2} m v^2$ giver det den mekaniske energi.
For en cirkulær bane ($v^2 = GM/r$) bliver den

$$E_{\text{mek}} = E_{\text{kin}} + E_{\text{pot}} = \frac{G M m}{2r} - \frac{G M m}{r} = -\frac{G \cdot M \cdot m}{2r}$$

Den **samlede energi er negativ** – det er kendetegnet for en bunden bane. Skal
legemet rive sig løs (undvige), skal energien op på mindst nul, og det giver
**undvigelseshastigheden**:

$$v_{\text{undv}} = \sqrt{\frac{2 \cdot G \cdot M}{r}} = \sqrt{2} \cdot v_{\text{bane}}$$

Fra Jordens overflade er den ca. $11{,}2$ km/s.

> **Model og gyldighed:** Nær jordoverfladen bruger I det homogene felt med
> $E_{\text{pot}} = m \cdot g \cdot h$. Det er en god tilnærmelse, så længe højden
> $h$ er lille i forhold til Jordens radius. For satellitter og rumfart holder den
> ikke – der skal det fulde $-G M m / r$ bruges. Et godt eksempel på, hvornår en
> simpel model er gyldig.

## Simulering: planetbane (lærerdemo)

Simuleringen illustrerer Keplers 1. og 2. lov: en ellipse opstår, og planeten er
tydeligt hurtigere tæt på centrallegemet. Det er en demo til forståelse – ikke et
eksamensværktøj.

```python
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
M = 1.989e30        # Solens masse [kg]
dt = 60 * 60 * 6    # tidsskridt: 6 timer [s]

def acceleration(x, y):
    """Tyngdeacceleration mod centrallegemet i origo."""
    r = np.hypot(x, y)
    a = -G * M / r**2
    return a * x / r, a * y / r

# Start i aphel med fart under den cirkulære -> ellipse
x, y = 1.5e11, 0.0
vx, vy = 0.0, 24000.0     # m/s

xs, ys = [], []
for _ in range(2000):
    ax, ay = acceleration(x, y)
    vx, vy = vx + ax * dt, vy + ay * dt   # symplektisk Euler -> stabil bane
    x,  y  = x + vx * dt,  y + vy * dt
    xs.append(x); ys.append(y)

plt.plot(xs, ys)
plt.plot(0, 0, 'yo')      # centrallegemet
plt.axis('equal'); plt.show()
```

## Opgaver

1. En satellit i geostationær bane har omløbstid $T = 24$ timer
   ($8{,}64 \cdot 10^{4}$ s). Brug Keplers 3. lov ($T^2 = \tfrac{4\pi^2}{GM} r^3$)
   til at bestemme baneradius $r$, og dernæst farten $v$.
   *Givet:* $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg², $M = 5{,}97 \cdot 10^{24}$ kg.
2. Jupiter har en stor halvakse på $5{,}20$ AE. Bestem dens omløbstid om Solen i
   år ved hjælp af Keplers 3. lov.
3. Bestem den potentielle, kinetiske og samlede mekaniske energi pr. kg for en
   satellit i højden $350$ km. Kommentér fortegnet på den samlede energi.
4. **Diskussion:** Forklar med Keplers 2. lov, hvorfor en komet bevæger sig
   meget hurtigt, når den passerer tæt forbi Solen, og langsomt i den fjerne del
   af sin bane.

> **Facit til opgave 1:** $r \approx 4{,}2 \cdot 10^{7}$ m og
> $v \approx 3{,}1 \cdot 10^{3}$ m/s.

## Det skal I kunne efter forløbet

- Bruge gravitationsloven og tyngdefeltstyrken $g = GM/r^2$.
- Bestemme banefart og omløbstid for et legeme om et centrallegeme.
- Formulere Keplers tre love og udlede 3. lov for den cirkulære bane.
- Bruge $E_{\text{pot}} = -GMm/r$ og forklare, at en bunden bane har negativ
  samlet energi, samt bestemme undvigelseshastigheden.
- Vurdere hvornår det homogene felt ($mgh$) er en gyldig model.
