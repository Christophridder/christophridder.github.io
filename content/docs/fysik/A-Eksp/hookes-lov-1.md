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
### Fra stedfunktion til acceleration

Stedfunktionen:  

$$s(t) = at^2 + v_0t + s_0$$

Differentierer man stedfunktionen får man hastighedsfunktionen og differentierer man den får man acceleration: 

$$s'(t)= v(t) = at + v$$
$$s''(t) = v'(t) = a(t) = a$$

Læg mærke til at de tre ligninger har forskellige enheder.
- I $s(t)$ ligningen er alle led i $m$
- i $v(t)$ ligningen er alle led i $\frac{m}{s}$
- i $a(t)$ ligningen er alle led i $\frac{m}{s^2}$

### Position, hastighed og acceleration nu i forhold til Hookes lov:

Ved Hookes lov er det kotyme at man bruger $y(t)$ som stedvektor og ikke $s(t)$. 
Så: $y(t)$ er **positionen** af loddet til tiden $t$ fordi vi bevæger os op og ned i $y$ aksens retning. Enheden, of course, er stadig meter, $[\text{m}]$.

Differentierer man positionen med hensyn til tiden, får man, lige som før:  **hastigheden**:

$$v(t) = y'(t) \qquad [\text{m/s}]$$

Differentierer man én gang til, får man **accelerationen**:

$$a(t) = v'(t) = y''(t) \qquad [\text{m/s}^2]$$

I fysikken differentierer man ofte til tiden $t$ og for ikke at forveksle det med andre differentiationer har fysikere fundet på at skrive  den *tidsafledte* med en **prik** over symbolet i stedet
for en mærke-streg (det er Newtons prik-notation): (I wordmat skal i skrive **\dot{y}** eller **\ddot(y)**)

$$\dot{y} = y' = v \qquad\qquad \ddot{y} = y'' = a$$

**Derfor** kan accelerationen nu kort skrives som $\ddot{y}$. Den notation bruger vi
fra nu af.

### Kraften fra fjederen (Hookes lov)

En fjeder trækker altid loddet tilbage mod sin **ligevægtsposition** $C$. Jo
længere væk fra ligevægt loddet er, jo større er kraften — og den peger
*modsat* udsvinget:

$$F = -k\cdot(y - C)$$
Hvis $C = 0$ gælder der: 
$$F = -k\cdot y$$

- $k$ er **fjederkonstanten** $[\text{N/m}]$ — fjederens stivhed.
- $C$ er **ligevægtspositionen** $[\text{m}]$ — det punkt loddet hviler i uden at svinge, starter man målingen af svingningen i denne position er C = 0m
- $y - C$ er selve **udsvinget fra ligevægt** — ikke positionen fra gulvet eller nul. Tænk det som lodet svinger om positionen $C$ og ikke om positionen 0. I praksis vil vi ofte sætte startpositionen til $0m$ hvad betyder at $C = 0$ og dermed bortfalder. $F = - ky$ 
- Minustegnet betyder "tilbage mod ligevægt". Når loddet svinger ned ad ($-y$ retning) så trækker fjederen tilbage i $+y$ retningen og omvendt. 

Newtons 2. lov siger nu: $F = m\cdot a = m\cdot\ddot{y}$, hvor $m$ er loddets masse $[\text{kg}]$.
Sætter vi de to udtryk for kraften lig hinanden:

$$m\cdot\ddot{y} = -k\cdot y$$

### Vi måler fra ligevægten (kaldes ofte variabelskift men vi gør det her uden!)

$$m\cdot\ddot{y} = -k\cdot y$$

$$\ddot{y} = -\frac{k}{m}\cdot y$$

**$C$ er væk.** Vi giver konstanten $k/m$ et navn, $\omega^2$:

$$\boxed{\ddot{y} = -\omega^2\cdot y}\qquad \text{med}\quad \omega^2 = \frac{k}{m}$$

Det er en **differentialligning**: en ligning, hvor det ukendte er en *funktion*
$y(t)$, og hvor funktionen og dens 2. afledte indgår.

### Vi gætter en løsning (ansatz)

Vi udleder ikke løsningen — vi **gætter** den og tjekker bagefter, at den passer.
Den enkle ligning $\ddot{y} = -\omega^2 y$ indbyder til gættet:

$$y(t) = A\cdot\sin(\omega t + \varphi)$$

For at se om gættet løser ligningen, differentierer vi to gange:

1. gang: 
$$\dot{y}(t) = A\cdot\omega\cdot\cos(\omega t + \varphi)$$

2. gang:
$$\ddot{y}(t) = -A\cdot\omega^2\cdot\sin(\omega t + \varphi) = -\omega^2\cdot y(t)$$

$sin'(\omega t)$ bliver til $\omega cos(\omega t)$ og $\omega cos'(\omega t)$ til $-\omega^2 sin(\omega t)$. 

Afleder man $sin(\omega t)$ to gange får man dermed $-\omega^2 sin(\omega t)$. Præcis sådan en funktion opfylder differentialligningen.  

$$\boxed{\ddot{y} = -\omega^2\cdot y}\qquad \text{med}\quad \omega^2 = \frac{k}{m}$$

 For at være helt præcis sætter vi nu konstanten $C$ på igen og formlen bliver:

$$y(t) = A\cdot\sin(\omega t + \varphi) + C$$

Husk at $C$ bortfalder med det samme når man differentierer. $C$ er y-værdien af ligevægtspositionen.


Der gælder nu at: 

$$\omega = \sqrt{\frac{k}{m}}, \qquad T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$$

Svingningstiden afhænger altså kun af **massen og fjederen** — ikke af, hvor langt
man trækker loddet ud. 

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
A_ref     = 1.0           # amplitude        [m]
T_ref     = 1.0           # periode [s]
omega_ref = 2*np.pi/T_ref # vinkelfrekvens   [rad/s]
phi_ref   = 0.0           # fase             [rad]
C_ref     = 0.0           # ligevægt         [m]

# --- Din kurve: skru på ÉN parameter ad gangen ---
A     = 1.0          # prøv fx 2.0
T     = 2.0          # prøv fx 2.0
omega = 2*np.pi/T    # prøv fx 2.0
phi   = 0.0          # prøv fx np.pi/2
C     = 0.0          # prøv fx 3.0

# printe omega 
print(f'omega_ref = {omega_ref:.3f}  rad/s')
print(f'omega = {omega:.3f} rad/s')

# Tidsakse: 0 til 20 sekunder, 1000 punkter
t = np.linspace(0, 10, 1000)

# Beregn de to kurver
y_ref = svingning(t, A_ref, omega_ref, phi_ref, C_ref)
y     = svingning(t, A, omega, phi, C)

# Afledte størrelser for DIN kurve
T = 2 * np.pi / omega        # svingningstid [s] regnes tilbage
f = 1 / T                    # frekvens      [Hz]

# Plot
plt.figure(figsize=(9, 5))
plt.plot(t, y_ref, "--", color="grey",
        label=f"Reference (A=1, ω={omega:.2f}s^-1, φ=0, C=0)")
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
>**Lav en wordfil hvori du afrapporterer nedenstående**
Sæt screenshots ind af ændringen af de 4 variabler ind i en tabel, lidt som her nedenunder: 
$A, \omega, \varphi , C$
|variabel|reference screenshot 1 | variations screenshot 2| kommentar| 
|---|---|---|---|
|A||||
|$\omega$||||
|$\varphi$||||
|C|||C er en slags $y_0$-værdi som skubber hele funktionen op og ned af $y$-aksen|

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


### Opgave om $\omega$ og $T$
$\omega$ er vinkelfrekvensen: denne opgave er til for at forstå sammenhæng mellem $\omega$ og $T$

Prøv at sætte $T = 0.5s$, $T = 2.0s$ og $T = 4.0s$ 

For hver værdi: aflæs den omega, Python beregner, og udfyld tabellen.

|T [s]	|ω [rad/s]|	$T\cdot \omega$ |
|---|---|---|
|0.5|	||	
|1.0|	6.283||	
|2.0|		||
|4.0|		||

Spørgsmål: Hvad bemærker du ved produktet 
𝑇
⋅
𝜔
T⋅ω i alle fire rækker? Kan du forklare hvorfor det altid bliver den samme værdi — og hvad den værdi egentlig er (tip: hvor mange radianer er der i én hel omgang af enhedscirklen)?
---

*Næste del: dæmpede svingninger + fit af jeres egne data fra bevægelsessensoren.*
