---
title: "Hookes lov 3" 
date: 2026-06-11
draft: false
---

# Del 3 — Dæmpede svingninger

Hvis I kigger på *hele* jeres måling fra Del 2 — ikke kun de første perioder —
opdager I, at svingningen langsomt bliver mindre. Loddet svinger ikke for evigt.
I denne sidste del bygger vi det ind i modellen.

---

## 1. Hvorfor dør svingningen ud?

Den udæmpede model $y = A \cdot \sin(\omega t + \varphi) + C$ svinger med **konstant**
amplitude $A$ — den stopper aldrig. Men i virkeligheden taber loddet energi til
luftmodstand og gnidning, og udsvinget skrumper for hver tur. Amplituden er altså
ikke længere en konstant — den **aftager med tiden**.

---

## 2. Vi postulerer en løsning

Vi udleder ikke modellen denne gang — vi **postulerer** den. Idéen er enkel: tag den
gamle løsning, og lad amplituden $A$ blive ganget med en faktor, der langsomt
skrumper mod nul, nemlig $e^{-\beta t}$:

$$y(t) = A \cdot e^{-\beta t} \cdot \sin(\omega t + \varphi) + C$$

- $A \cdot \sin(\omega t + \varphi) + C$ er den velkendte svingning fra Del 1.
- $e^{-\beta t}$ er en **aftagende faktor**: ved $t=0$ er den $1$, og derefter falder
  den mod $0$. Den klemmer langsomt svingningen sammen.

Den nye størrelse er $\beta$.

---

## 3. Dæmpningskonstanten β

$\beta$ kaldes **dæmpningskonstanten**. Den har enheden $[\text{s}^{-1}]$ (så
produktet $\beta t$ bliver et rent tal).

### Indhyllingskurven

Selve svingningen vipper op og ned mellem to "vægge", der langsomt nærmer sig
hinanden:

$$\text{indhyllingskurve:}\qquad \pm A \cdot e^{-\beta t}$$

Det er den kasse, svingningen bliver klemt sammen i. Jo større $\beta$, jo
hurtigere lukker kassen sig.

### To måder at beskrive, hvor hurtigt det dør ud

- **Tidskonstanten** $\tau = \dfrac{1}{\beta}$: tiden, det tager, før amplituden er
  faldet til $1/e \approx 37\\%$ af starten.
- **Halveringstiden** $t_{1/2} = \dfrac{\ln 2}{\beta}$: tiden, det tager, før
  amplituden er **halveret**. For hver $t_{1/2}$ halveres udsvinget igen.

### Den fine analogi: radioaktivt henfald

Genkender I matematikken? Det er **præcis** samme form som henfaldsloven fra
kernefysik:

$$N(t) = N_0 \cdot e^{-\lambda t}, \qquad T_{1/2} = \frac{\ln 2}{\lambda}$$

Indhyllingskurven for svingningen henfalder altså ligesom antallet af radioaktive
kerner — dæmpningskonstanten $\beta$ spiller nøjagtig samme rolle som
henfaldskonstanten $\lambda$. Det er samme differentialligning, der gemmer sig bag
begge.

> **For de skarpe (kan springes over):**
>
> - **Energien** dør ud dobbelt så hurtigt som amplituden, fordi energi går som
>   amplitude i anden: $E \propto e^{-2\beta t}$. Energiens halveringstid er derfor
>   $\dfrac{\ln 2}{2\beta}$ — halvdelen af amplitudens.
> - Den frekvens, I måler på en dæmpet svingning, er en lille smule **lavere** end
>   den udæmpede: $\omega_d = \sqrt{\omega_0^2 - \beta^2}$, hvor $\omega_0 = \sqrt{k/m}$.
>   Ved svag dæmpning ($\beta \ll \omega_0$) er forskellen forsvindende lille, så vi
>   kalder den bare $\omega$ i modellen.

---

## 4. Leg med dæmpningen i Python

Som i Del 1 skruer I på parametrene og ser, hvad der sker — nu med $\beta$ som ny
knap. Vi tegner også **indhyllingskurven** med, så I tydeligt ser kassen, der lukker
sig:

```python
import numpy as np
import matplotlib.pyplot as plt

# Den dæmpede svingningsfunktion
def daempet_svingning(t, A, beta, omega, phi, C):
    return A * np.exp(-beta * t) * np.sin(omega * t + phi) + C

# --- Skru især på beta ---
A     = 1.0          # start-amplitude   [m]
beta  = 0.15         # dæmpningskonstant  [1/s]   (prøv 0.0, 0.15, 0.5)
omega = 2.0          # vinkelfrekvens     [rad/s]
phi   = 0.0          # fase               [rad]
C     = 0.0          # ligevægt           [m]

t = np.linspace(0, 30, 2000)

y = daempet_svingning(t, A, beta, omega, phi, C)

# Indhyllingskurven: +/- A*e^(-beta*t) (lagt om ligevægten C)
oevre = C + A * np.exp(-beta * t)
nedre = C - A * np.exp(-beta * t)

# Halveringstid for amplituden
t_halv = np.log(2) / beta

plt.figure(figsize=(9, 5))
plt.plot(t, y, color="C0", label=f"dæmpet svingning (β = {beta})")
plt.plot(t, oevre, "--", color="grey", label="indhyllingskurve  ± A·e^(−βt)")
plt.plot(t, nedre, "--", color="grey")
plt.axhline(C, color="C1", linestyle=":", linewidth=1)
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title(f"Dæmpet svingning   (amplitudens halveringstid = {t_halv:.1f} s)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Prøv selv:**

1. Sæt `beta = 0.0`. Hvad sker der? (Den udæmpede svingning fra Del 1 — kassen er
   helt vandret.)
2. Sæt `beta = 0.5`. Hvor hurtigt dør den ud nu? Aflæs halveringstiden i titlen.
3. Bemærk, at $\omega$, $\varphi$ og $C$ stadig gør præcis det samme som i Del 1 —
   $\beta$ rører kun ved, hvor hurtigt amplituden skrumper.

---

## 5. Fit den dæmpede model til jeres data

Nu kan I bruge **hele** jeres måling fra `hookes.xlsx` — også de sene perioder, hvor
svingningen er dødet ud. Den udæmpede model fra Del 2 kunne kun klare de første få
perioder; den dæmpede model passer hele vejen.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def daempet_svingning(t, A, beta, omega, phi, C):
    return A * np.exp(-beta * t) * np.sin(omega * t + phi) + C

# Hent hele datasættet
data = pd.read_excel("hookes.xlsx")
t = data.iloc[:, 0].to_numpy()
y = data.iloc[:, 1].to_numpy()

# Startgæt - genbrug A, omega, phi, C fra Del 2-fittet, og gæt beta:
# Find tiden hvor toppene er ca. halveret -> beta = ln(2)/t_halv
A_gaet     = 0.05
beta_gaet  = 0.1      # [1/s]
omega_gaet = 6.0
phi_gaet   = 0.0
C_gaet     = 0.30

start = [A_gaet, beta_gaet, omega_gaet, phi_gaet, C_gaet]

# maxfev sat højt, fordi 5 parametre er sværere at fitte
params, kovarians = curve_fit(daempet_svingning, t, y, p0=start, maxfev=10000)
A_fit, beta_fit, omega_fit, phi_fit, C_fit = params

usikkerhed = np.sqrt(np.diag(kovarians))
dA, dbeta, domega, dphi, dC = usikkerhed

# Afledte størrelser
T_fit     = 2 * np.pi / omega_fit
t_halv    = np.log(2) / beta_fit       # amplitudens halveringstid
tau       = 1 / beta_fit               # tidskonstant

print(f"A     = {A_fit:.4f} ± {dA:.4f} m")
print(f"beta  = {beta_fit:.4f} ± {dbeta:.4f} 1/s")
print(f"omega = {omega_fit:.4f} ± {domega:.4f} rad/s")
print(f"phi   = {phi_fit:.4f} ± {dphi:.4f} rad")
print(f"C     = {C_fit:.4f} ± {dC:.4f} m")
print(f"T          = {T_fit:.4f} s")
print(f"halveringstid = {t_halv:.2f} s")
print(f"tidskonstant  = {tau:.2f} s")

# Plot fit + indhyllingskurve oven på data
y_fit = daempet_svingning(t, A_fit, beta_fit, omega_fit, phi_fit, C_fit)
oevre = C_fit + A_fit * np.exp(-beta_fit * t)
nedre = C_fit - A_fit * np.exp(-beta_fit * t)

plt.figure(figsize=(9, 5))
plt.plot(t, y, ".", markersize=3, label="måledata")
plt.plot(t, y_fit, color="C3", label="dæmpet fit")
plt.plot(t, oevre, "--", color="grey", label="indhyllingskurve")
plt.plot(t, nedre, "--", color="grey")
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title("Fit af den dæmpede svingning")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 6. Til refleksion

- **Sammenlign** $\omega$ fra det dæmpede fit med $\omega$ fra Del 2. De ligger
  meget tæt — dæmpningen ændrer næsten ikke frekvensen, kun amplituden.
- **Halveringstiden** I lige har fittet: passer den med, hvad I ser på grafen?
  Find et sted, hvor toppene er halveret, og tjek tiden.
- **Den store sammenhæng:** I har nu beskrevet en helt almindelig fjedersvingning
  med fem tal — og opdaget, at amplituden dør ud efter *samme* lov som radioaktive
  kerner. Samme matematik, to vidt forskellige fænomener. Det er dér, fysikken
  bliver smuk.
