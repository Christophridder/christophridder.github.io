---
title: "Hookes lov 2"
date: 2026-06-11
draft: false
weight: 4
---

# Del 2 — Fit jeres egne data

I Del 1 legede I med modellen og fandt ud af, hvad de fire parametre gør. Nu
vender vi det om: I har optaget en rigtig svingning med bevægelsessensoren, og så
lader vi computeren finde de fire parametre, der passer bedst til **jeres** data.

Den svingning I har optaget er en dæmpet svingning, måske med et lille lod eller et stykke pap for at få dæmpning på. Vi kan godt bruge de første svingninger af den dæmpede som udæmpet. 

Vi bliver på den **udæmpede** model og bruger kun de første få perioder, hvor
svingningen næsten ikke er aftaget endnu:

$$y(t) = A \cdot \sin(\omega t + \varphi) + C$$

(Dæmpningen — at amplituden langsomt dør ud — tager vi i Del 3.)

---

## 1. Lav din datafil `hookes.xlsx`

I LoggerPro har I to kolonner: **tid** og **udsving**. Dem skal vi have over i en
Excel-fil:

1. Marker de to kolonner i LoggerPro og kopier dem.
2. Indsæt dem i et tomt Excel-ark, så **tid** står i kolonne **A** og **udsving**
   i kolonne **B**.
3. Skriv en overskrift i **række 1** (fx `tid` og `udsving`), så jeres tal starter
   i **A2** og **B2**.
4. Vælg **Gem som** → filtype **Excel-projektmappe (.xlsx)** → navngiv den
   `hookes.xlsx`, og gem den i **samme mappe** som jeres Python-fil.

Hav lige øje på om det kommer over med komma eller punktum. Hvis loggerpro kommer med punktum skal I lige omkring word for at erstatte . med ,

## 2. Hent data ind og tjek, at det lykkedes
(det sværeste her er at finde den mappe som jeres python fil ligger i. I prøvede det da vi lavede FFT med trompetlydfilen, det er desværre meget forskelligt fra computer til computer)

Først importerer I jeres data og tegner det **rå** — før vi fitter noget. På den måde
ser man med det samme, om importen gik godt. 

```python
import numpy as np
import pandas as pd #pandas får python til at læse excel filer
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Modellen (samme som i Del 1 vi vruger sin- funktionen)
def svingning(t, A, omega, phi, C):
    return A * np.sin(omega * t + phi) + C

# Hent data fra regnearket i samme mappe
data = pd.read_excel("hookes.xlsx") # ejg  har kaldt min fin hookes.xlsx 
t = data.iloc[:, 0].to_numpy()    # kolonne A: tid     [s]
y = data.iloc[:, 1].to_numpy()    # kolonne B: udsving [m]

# Tjek-graf: bare rådata
plt.figure(figsize=(9, 5))
plt.plot(t, y, ".", markersize=4, label="måledata")
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title("Rådata fra loggerpro")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
Læg mærke til de her to linjer 
```pyton
t = data.iloc[:, 0].to_numpy()    # kolonne A: tid     [s]
y = data.iloc[:, 1].to_numpy()    # kolonne B: udsving [m]

```
[:, 0] betyder at python tager den første kolonne i din excelfil. [:. 1] tager den anden så tjek lige din excel fil om alle data ligger som de skal. 

Så hvisgrafen ser ud som en pæn svingning så er importen i orden. (Ser den
mærkelig ud, så tjek at tid er i kolonne A, udsving i kolonne B, og at filen
hedder præcis `hookes.xlsx` og ligger i samme mappe som din python fil.)

---
## Fit af data 
Nu skal vi prøve at fitte disse data. Det er ikke helt simpelt da det ikke bare er en ret linje. Vi skal 
- bestemme hvilket fitteprogram vi vil bruge (curve fit fra scipy.optimize)
- definere fittefunktionen (y = Asin(omega t + phi) + C)
- sætte nogle startgæt (næste afsnit)
- lade programmet finde den bedste funktion
- aflæse og tolke på de data der kom ud af de. 

## 3. Gæt parametrene i hånden først

Computeren skal bruge nogle **startgæt** for at finde det rigtige svar — især på
$\omega$. Får den et dårligt gæt, kan den lande helt forkert.

Brug lidt tid på det her nu: Find gode startværdier og tast dem ind under *dine startgæt* i python koden. 

- **Amplitude:** $A \approx \dfrac{y_{\text{max}} - y_{\text{min}}}{2}$ — halvdelen
  af afstanden mellem top og bund.
- **Ligevægt:** $C \approx \dfrac{y_{\text{max}} + y_{\text{min}}}{2}$ — midterlinjen.
- **Vinkelfrekvens:** aflæs svingningstiden $T$ mellem to toppe, og brug
  $\omega \approx \dfrac{2\pi}{T}$.
- **Fase:** start med $\varphi = 0$ og juster, til kurven ligger rigtigt vandret.

Skriv jeres gæt ind, og se modellen lagt oven på data:

```python
# Dine startgæt - ret tallene, til den orange kurve følger punkterne
A_gaet     = 0.05     # [m]
omega_gaet = 6.0      # [rad/s]   ( = 2*pi/T )
phi_gaet   = 0.0      # [rad]
C_gaet     = 0.30     # [m]

y_gaet = svingning(t, A_gaet, omega_gaet, phi_gaet, C_gaet)

plt.figure(figsize=(9, 5))
plt.plot(t, y, ".", markersize=4, label="måledata")
plt.plot(t, y_gaet, color="C1", label="min model (gæt)")
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title("Mit gæt oven på data")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

Det skal **ikke** ramme perfekt — det er nok, at den orange kurve svinger
nogenlunde i takt med punkterne. Computeren finpudser resten i næste skridt.

---

## 4. Lad computeren finde det bedste fit

Nu bruger vi `curve_fit`. Bemærk, at jeres håndgæt fra før genbruges som
startpunkt (`start`):

```python
# Jeres håndgæt bliver computerens startpunkt
start = [A_gaet, omega_gaet, phi_gaet, C_gaet]

params, kovarians = curve_fit(svingning, t, y, p0=start)
A_fit, omega_fit, phi_fit, C_fit = params

# Usikkerheder (standardafvigelser) fra fittet
usikkerhed = np.sqrt(np.diag(kovarians))
dA, domega, dphi, dC = usikkerhed

# Afledte størrelser med usikkerhed
T_fit = 2 * np.pi / omega_fit
f_fit = 1 / T_fit
dT = T_fit * (domega / omega_fit)     # samme relative usikkerhed som omega

print(f"A     = {A_fit:.4f} ± {dA:.4f} m")
print(f"omega = {omega_fit:.4f} ± {domega:.4f} rad/s")
print(f"phi   = {phi_fit:.4f} ± {dphi:.4f} rad")
print(f"C     = {C_fit:.4f} ± {dC:.4f} m")
print(f"T     = {T_fit:.4f} ± {dT:.4f} s")
print(f"f     = {f_fit:.4f} Hz")

# Tegn fittet oven på data
y_fit = svingning(t, A_fit, omega_fit, phi_fit, C_fit)
plt.figure(figsize=(9, 5))
plt.plot(t, y, ".", markersize=4, label="måledata")
plt.plot(t, y_fit, color="C3", label="bedste fit")
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title("Fit af den harmoniske svingning")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## 5. Tjek fit og teori 

Det fede er nu, at I kan tjekke jeres fit mod teorien fra Del 1. Der fandt vi

$$\omega = \sqrt{\frac{k}{m}}$$

Hvis I har målt fjederkonstanten $k$ (med Hookes lov) og loddets masse $m$
uafhængigt, kan I *forudsige* $\omega$ og sammenligne med fittet:

```python
# Indsæt JERES målte værdier
k = 12.0     # fjederkonstant [N/m]  (fra Hookes lov)
m = 0.250    # masse          [kg]

omega_teori = np.sqrt(k / m)

print(f"omega (teori) = {omega_teori:.4f} rad/s")
print(f"omega (fit)   = {omega_fit:.4f} ± {domega:.4f} rad/s")
```

Stemmer de to tal inden for usikkerheden, så er det jo helt fantastisk :-) 
fra **kraftloven** ($F = -k \cdot (y-C)$), gennem **differentialligningen**, til
**jeres egne målinger**. FEDT!

---

*Næste del: hvorfor dør svingningen langsomt ud? Vi indfører dæmpningen
$A \cdot e^{-\beta t}$, indhyllingskurven, halveringstiden — og den fine analogi
til radioaktivt henfald.*
