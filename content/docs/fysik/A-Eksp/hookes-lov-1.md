---
title: "Hookes lov 1"
date: 2026-06-11
draft: false
---

# Harmonisk oscillator

I dette forløb undersøger vi en svingning — fx en lod, der hænger i en fjeder og
hopper op og ned. Vi opstiller en model med fire parametre, leger med dem i
Python, og fitter til sidst modellen til jeres egne måledata fra
bevægelsessensoren.

---

## Del 1 — Fra position til svingningsligning

### Position, hastighed og acceleration

Vi lader $y(t)$ være **positionen** af loddet til tiden $t$. Enheden er meter, $[\text{m}]$.

Differentierer vi positionen med hensyn til tiden, får vi **hastigheden**:

$$v(t) = y'(t) \qquad [\text{m/s}]$$

Differentierer vi én gang til, får vi **accelerationen**:

$$a(t) = v'(t) = y''(t) \qquad [\text{m/s}^2]$$

Fysikere er dovne og skriver de *tidsafledte* med en **prik** over symbolet i stedet
for en mærke-streg (det er Newtons prik-notation):

$$\dot{y} = y' = v \qquad\qquad \ddot{y} = y'' = a$$

**Derfor** kan accelerationen kort skrives som $\ddot{y}$. Den notation bruger vi
fra nu af.

### Kraften fra fjederen (Hookes lov)

En fjeder trækker altid loddet tilbage mod sin **ligevægtsposition** $C$. Jo
længere væk fra ligevægten loddet er, jo større er kraften — og den peger
*modsat* udsvinget:

$$F = -k\cdot(y - C)$$

- $k$ er **fjederkonstanten** $[\text{N/m}]$ — fjederens stivhed.
- $C$ er **ligevægtspositionen** $[\text{m}]$.
- Minustegnet betyder "tilbage mod ligevægt".

Newtons 2. lov siger $F = m\cdota = m\cdot\ddot{y}$, hvor $m$ er loddets masse $[\text{kg}]$.
Sætter vi de to udtryk for kraften lig hinanden:

$$m\cdot\ddot{y} = -k\cdot(y - C)$$

$$\ddot{y} = -\frac{k}{m}\cdot(y - C)$$

Vi giver konstanten $k/m$ et navn, $\omega^2$, fordi den (som vi straks ser) sætter
svingningens hastighed:

$$\boxed{\ddot{y} = -\omega^2\cdot(y - C)}\qquad \text{med}\quad \omega^2 = \frac{k}{m}$$

Det er en **differentialligning**: en ligning, hvor det ukendte er en *funktion*
$y(t)$, og hvor funktionen og dens 2. afledte indgår.

### Vi gætter en løsning (ansatz)

Vi udleder ikke løsningen — vi **gætter** den og tjekker bagefter, at den passer.
Et kvalificeret gæt er:

$$y(t) = A\cdot\sin(\omega t + \varphi) + C$$

For at se om gættet løser ligningen, differentierer vi to gange:

$$\dot{y}(t) = A\cdot\omega\cdot\cos(\omega t + \varphi)$$

$$\ddot{y}(t) = -A\cdot\omega^2\cdot\sin(\omega t + \varphi)$$

Læg mærke til, at $A\cdot\sin(\omega t + \varphi) = y - C$. Derfor er

$$\ddot{y} = -\omega^2\cdot\big(y - C\big)$$

— og det er **præcis** differentialligningen. Gættet passer! 

Samtidig kan vi nu læse en vigtig fysisk sammenhæng af:

$$\omega = \sqrt{\frac{k}{m}}, \qquad T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$$

Svingningstiden afhænger altså kun af **massen og fjederen** — ikke af, hvor langt
du trækker loddet ud. Det er en pointe, eleverne kan tjekke eksperimentelt senere.

### Hvad betyder de fire parametre?

| Parameter | Navn | Enhed | Hvad styrer den? | Bestemt af |
|-----------|------|-------|------------------|------------|
| $A$ | amplitude | $[\text{m}]$ | hvor stort udsvinget er | *dig* — hvor langt du trækker loddet ud |
| $\omega$ | vinkelfrekvens | $[\text{rad/s}]$ | hvor hurtigt det svinger ($T = 2\pi/\omega$) | *systemet* — $\sqrt{k/m}$ |
| $\varphi$ | fase | $[\text{rad}]$ | hvor i svingningen vi er ved $t=0$ | *dit ur* — hvornår du trykker start |
| $C$ | ligevægt | $[\text{m}]$ | hvor svingningen ligger og "balancerer" | *systemet/opstillingen* |

Bemærk forskellen: $\omega$ og $C$ er egenskaber ved **systemet**, mens $A$ og $\varphi$
afhænger af, hvordan og hvornår du **starter** forsøget. Især $\varphi$ er ikke en
egenskab ved svingeren overhovedet — den skifter bare, hvis du starter uret på et
andet tidspunkt.

---

## Del 2 — Leg med modellen i Python

Nu skal I selv mærke, hvad de fire parametre gør. Programmet tegner **to** kurver
oven i hinanden:

- en **referencekurve** (grå, stiplet) med $A=1$, $\omega=1$, $\varphi=0$, $C=0$ —
  den ændrer sig aldrig.
- **jeres egen kurve** (blå), som I skruer på.

Ved at sammenligne med referencen kan I se *præcis* hvad hver parameter gør.

```python
import numpy as np
import matplotlib.pyplot as plt

# Svingningsfunktionen (modellen)
def svingning(t, A, omega, phi, C):
    return A * np.sin(omega * t + phi) + C

# --- Referencekurve: skru ALDRIG på disse ---
A_ref     = 1.0      # amplitude        [m]
omega_ref = 1.0      # vinkelfrekvens   [rad/s]
phi_ref   = 0.0      # fase             [rad]
C_ref     = 0.0      # ligevægt         [m]

# --- Din kurve: skru på ÉN parameter ad gangen ---
A     = 1.0          # prøv fx 2.0
omega = 1.0          # prøv fx 2.0
phi   = 0.0          # prøv fx np.pi/2
C     = 0.0          # prøv fx 3.0

# Tidsakse: 0 til 20 sekunder, 1000 punkter
t = np.linspace(0, 20, 1000)

# Beregn de to kurver
y_ref = svingning(t, A_ref, omega_ref, phi_ref, C_ref)
y     = svingning(t, A, omega, phi, C)

# Afledte størrelser for DIN kurve
T = 2 * np.pi / omega        # svingningstid [s]
f = 1 / T                    # frekvens      [Hz]

# Plot
plt.figure(figsize=(9, 5))
plt.plot(t, y_ref, "--", color="grey",
         label="Reference (A=1, ω=1, φ=0, C=0)")
plt.plot(t, y, color="C0",
         label=f"Din kurve (T = {T:.2f} s,  f = {f:.3f} Hz)")
plt.axhline(C, color="C1", linestyle=":", linewidth=1)   # ligevægtslinje
plt.xlabel("tid  t  [s]")
plt.ylabel("udsving  y  [m]")
plt.title("Harmonisk svingning")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Prøv selv

Ændr **kun én** parameter ad gangen (sæt de andre tilbage til reference-værdien
bagefter), og skriv ned, hvad der sker:

1. **Amplitude:** sæt `A = 2.0`. Hvad sker der med udsvingets størrelse? Med
   svingningstiden $T$?
2. **Vinkelfrekvens:** sæt `omega = 2.0`. Hvad sker der med $T$? Aflæs den nye
   $T$-værdi i forklaringsboksen (legend) — passer den med $T = 2\pi/\omega$?
3. **Fase:** sæt `phi = np.pi/2` (altså $\pi/2 \approx 1{,}57$). Kurven flyttes
   vandret — hvilken kendt funktion ligner $\sin(\omega t + \pi/2)$ nu?
4. **Ligevægt:** sæt `C = 3.0`. Hvad sker der med hele kurven? Bemærk, at den
   stiplede ligevægtslinje følger med.

> **Spørgsmål til sidst:** Hvilke af de fire parametre ændrer på *formen* af
> svingningen, og hvilke flytter den bare rundt uden at ændre formen?

---

*Næste del: dæmpede svingninger + fit af jeres egne data fra bevægelsessensoren.*
