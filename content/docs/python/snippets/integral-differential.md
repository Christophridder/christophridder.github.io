---
title: "Integral og differential"
weight: 5
---

# Integral- og differentialregning – kort

Her er de korteste opskrifter. Der er grundige gennemgange med fysikeksempler her:

- 👉 [Integration i fysik]({{< relref "/docs/mat/integration-i-fysik" >}}) og [Integralregning med Python]({{< relref "/docs/nat/Integralregning-med-python" >}})
- 👉 [Differentiation med Python]({{< relref "/docs/nat/differentiation" >}})

## Hvilket værktøj?

| Jeg har … | Differentiation | Integration |
|---|---|---|
| **Måledata** (tabel med x og y) | `np.gradient(y, x)` | `np.trapezoid(y, x)` |
| **En funktion** og vil have et **tal** | – | `quad(f, a, b)` fra `scipy` |
| **En forskrift** og vil have en **forskrift** | `sp.diff(f, x)` fra `sympy` | `sp.integrate(f, x)` fra `sympy` |

## Måledata: fart ud fra position

```python
import numpy as np

t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])        # s
s = np.array([0.0, 1.2, 4.9, 11.0, 19.6, 30.7])     # m

v = np.gradient(s, t)                                # v = ds/dt
print(np.round(v, 2))
```

## Måledata: arbejde ud fra en kraft-vej-graf

$A = \int F \, ds$ = arealet under grafen:

```python
import numpy as np

s = np.array([0.00, 0.02, 0.04, 0.06, 0.08, 0.10])   # m
F = np.array([0.0, 1.1, 2.0, 3.1, 3.9, 5.0])         # N

A = np.trapezoid(F, s)
print(f"A = {A:.3g} J")
```

## Funktion: bestemt integral som et tal

```python
import numpy as np
from scipy.integrate import quad

def P(t):
    return 200 * np.sin(np.pi * t / 10)**2     # effekt i W

E, fejl = quad(P, 0, 10)                       # energi fra t = 0 til 10 s
print(f"E = {E:.4g} J")
```

## Forskrift: differentier og integrer med sympy

```python
import sympy as sp

t = sp.symbols("t")
s = 3*t**2 + 2*t + 5

v = sp.diff(s, t)             # differentier
a = sp.diff(v, t)
print("v(t) =", v)            # 6*t + 2
print("a(t) =", a)            # 6

F = sp.integrate(v, t)        # stamfunktion (uden konstant)
print("∫v dt =", F)           # 3*t**2 + 2*t

print("∫ fra 0 til 2:", sp.integrate(v, (t, 0, 2)))   # 16
```

## Nulpunkter, maksimum og skæringspunkter

**Med sympy** (eksakte løsninger):

```python
import sympy as sp

x = sp.symbols("x")
f = -x**2 + 4*x + 5

print("Nulpunkter:", sp.solve(f, x))                 # [-1, 5]

x_top = sp.solve(sp.diff(f, x), x)[0]                # f'(x) = 0
print("Toppunkt:", (x_top, f.subs(x, x_top)))        # (2, 9)

g = x + 1
print("Skæring med g:", sp.solve(f - g, x))          # [-1, 4]
```

**Med numpy** (når du har en kurve med mange punkter):

```python
import numpy as np

x = np.linspace(-2, 6, 10001)
y = -x**2 + 4*x + 5

i = np.argmax(y)                                    # nummeret på det største y
print(f"Maksimum: ({x[i]:.3f}; {y[i]:.3f})")
```

## Areal mellem to grafer

```python
import sympy as sp

x = sp.symbols("x")
f = -x**2 + 4*x + 5
g = x + 1

a, b = sp.solve(f - g, x)                           # skæringspunkterne er grænserne
areal = sp.integrate(f - g, (x, a, b))
print(f"Arealet mellem graferne er {areal} = {float(areal):.4g}")
```
