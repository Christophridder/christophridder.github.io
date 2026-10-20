---
title: "Regression"
weight: 1
---

# Regression i Python

Alle snippets følger samme opskrift:

1. Skriv dine måledata ind i to lister `x` og `y`.
2. Definér modellen som en funktion.
3. Lad `curve_fit` finde de bedste parametre.
4. Udskriv resultatet (og evt. $R^2$) og tegn grafen.

| Model | Forskrift | Typisk eksempel |
|---|---|---|
| [Lineær](#lineær-regression-uden-plot) | $y = a \cdot x + b$ | Hookes lov, Ohms lov |
| [Eksponentiel](#eksponentiel-regression) | $y = b \cdot a^x$ eller $y = N_0 \cdot e^{-k \cdot t}$ | Radioaktivt henfald, afkøling |
| [Potens](#potensregression) | $y = b \cdot x^a$ | Pendul: $T$ som funktion af $L$ |
| [Polynomium](#polynomiumregression-2-grad) | $y = a \cdot x^2 + b \cdot x + c$ | Lodret kast: $s(t)$ |
| [Sinus](#sinusregression) | $y = A \cdot \sin(\omega \cdot x + \varphi) + d$ | Svingninger, vekselstrøm |

> **Decimaltegn:** Python bruger **punktum**, ikke komma: skriv `9.82`, ikke `9,82`.

## Lineær regression uden plot

Den hurtigste måde at få $a$ og $b$:

```python
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])     # fx masse i kg
y = np.array([0.1, 2.1, 3.9, 6.2, 7.9, 10.1])    # fx kraft i N

a, b = np.polyfit(x, y, 1)                       # 1 = første grad = ret linje
print(f"y = {a:.4g} · x + {b:.4g}")
```

## Lineær regression med plot og prognose

Her tegnes linjen længere ud end dataene, så du kan aflæse en prognose. Du får også $R^2$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.1, 2.1, 3.9, 6.2, 7.9, 10.1])

def model(x, a, b):
    return a * x + b

(a, b), _ = curve_fit(model, x, y)

# R^2
y_fit = model(x, a, b)
R2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - np.mean(y))**2)
print(f"y = {a:.4g} · x + {b:.4g}   R² = {R2:.4f}")

# Prognose: hvad er y, når x = 8?
x_ny = 8
print(f"Prognose: y({x_ny}) = {model(x_ny, a, b):.3g}")

x_plot = np.linspace(0, 9, 200)                  # længere ud end dataene
plt.scatter(x, y, label="Målinger")
plt.plot(x_plot, model(x_plot, a, b), "r-", label=f"y = {a:.3g}·x + {b:.3g}")
plt.plot(x_ny, model(x_ny, a, b), "k*", markersize=12, label="Prognose")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
```

## Eksponentiel regression

To versioner af samme model – brug den, dit fag bruger:

- **Matematikform:** $y = b \cdot a^x$
- **Fysikform (henfald):** $N = N_0 \cdot e^{-k \cdot t}$ med halveringstid $T_{1/2} = \dfrac{\ln 2}{k}$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = np.array([0, 10, 20, 30, 40, 50, 60])          # tid i s
N = np.array([1000, 742, 553, 405, 302, 226, 166]) # tælletal

def model(t, N0, k):
    return N0 * np.exp(-k * t)

(N0, k), _ = curve_fit(model, t, N, p0=[N[0], 0.01])   # p0 = gæt på startværdier
T_halv = np.log(2) / k

print(f"N = {N0:.4g} · e^(-{k:.4g} · t)")
print(f"Halveringstid: T½ = {T_halv:.3g} s")
print(f"Matematikform: y = {N0:.4g} · {np.exp(-k):.4g}^x")

t_plot = np.linspace(0, 70, 200)
plt.scatter(t, N, label="Målinger")
plt.plot(t_plot, model(t_plot, N0, k), "r-", label=rf"$N = {N0:.0f}\cdot e^{{-{k:.4f}\cdot t}}$")
plt.axhline(N0 / 2, color="k", ls="--", lw=1)      # halvdelen af N0
plt.axvline(T_halv, color="k", ls="--", lw=1)      # halveringstiden
plt.xlabel("t / s")
plt.ylabel("N")
plt.grid()
plt.legend()
plt.show()
```

![Eksponentiel regression med halveringstid markeret](/img/python/eksponentiel-regression.svg)

> **Hvorfor `p0`?** Ved ikke-lineære modeller skal `curve_fit` have et fornuftigt gæt at starte fra. Uden det kan den ende et forkert sted eller give en fejl. Et godt gæt for $N_0$ er den første måling.

## Potensregression

$y = b \cdot x^a$. Eksempel: svingningstiden $T$ for et pendul som funktion af snorlængden $L$ (teorien siger $a = 0{,}5$).

```python
import numpy as np
from scipy.optimize import curve_fit

L = np.array([0.20, 0.40, 0.60, 0.80, 1.00])   # snorlængde i m
T = np.array([0.90, 1.27, 1.55, 1.80, 2.01])   # svingningstid i s

def model(x, b, a):
    return b * x**a

(b, a), _ = curve_fit(model, L, T, p0=[2, 0.5])
print(f"T = {b:.4g} · L^{a:.4g}")
```

## Polynomiumregression (2. grad)

Eksempel: højden af en bold i et lodret kast. Koefficienten foran $t^2$ er $-\tfrac{1}{2}g$.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])     # s
h = np.array([1.00, 1.45, 1.80, 2.05, 2.21, 2.27, 2.23]) # m

a, b, c = np.polyfit(t, h, 2)                  # 2 = andengradspolynomium
print(f"h = {a:.4g}·t² + {b:.4g}·t + {c:.4g}")
print(f"g ≈ {-2*a:.3g} m/s²")

t_plot = np.linspace(0, 0.7, 200)
plt.scatter(t, h, label="Målinger")
plt.plot(t_plot, np.polyval([a, b, c], t_plot), "r-", label="2.-gradsfit")
plt.xlabel("t / s")
plt.ylabel("h / m")
plt.grid()
plt.legend()
plt.show()
```

Vil du have 3. grad, skriver du bare `np.polyfit(t, h, 3)` og får fire koefficienter.

## Sinusregression

$y = A \cdot \sin(\omega \cdot x + \varphi) + d$. Her er gode startgæt **helt afgørende**:

| Parameter | Betydning | Godt gæt |
|---|---|---|
| `A` | Amplitude | (største y − mindste y) / 2 |
| `omega` | Vinkelfrekvens $\omega = \dfrac{2\pi}{T}$ | $2\pi$ / (periode aflæst på grafen) |
| `phi` | Faseforskydning | 0 |
| `d` | Ligevægtsværdi | gennemsnittet af y |

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = np.linspace(0, 4, 25)                                  # s
y = np.array([0.23, 0.83, 1.41, 1.35, 0.86, 0.06, -0.84, -1.33, -1.46,
              -0.90, -0.28, 0.55, 1.21, 1.42, 1.13, 0.48, -0.34, -1.10,
              -1.40, -1.30, -0.69, 0.21, 0.95, 1.38, 1.37])  # m

def model(t, A, omega, phi, d):
    return A * np.sin(omega * t + phi) + d

T_gaet = 1.7                                               # periode aflæst på grafen
p0 = [(y.max() - y.min()) / 2, 2*np.pi / T_gaet, 0, y.mean()]
(A, omega, phi, d), _ = curve_fit(model, t, y, p0=p0)

print(f"y = {A:.3g} · sin({omega:.3g}·t + {phi:.3g}) + {d:.3g}")
print(f"Periode T = {2*np.pi/omega:.3g} s,  frekvens f = {omega/(2*np.pi):.3g} Hz")

t_plot = np.linspace(0, 4, 400)
plt.scatter(t, y, label="Målinger")
plt.plot(t_plot, model(t_plot, A, omega, phi, d), "r-", label="Sinusfit")
plt.xlabel("t / s")
plt.ylabel("y / m")
plt.grid()
plt.legend()
plt.show()
```

## Usikkerhed på parametrene

`curve_fit` giver også en kovariansmatrix. Kvadratroden af diagonalen er standardusikkerheden på hver parameter:

```python
import numpy as np
from scipy.optimize import curve_fit

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.1, 2.1, 3.9, 6.2, 7.9, 10.1])

def model(x, a, b):
    return a * x + b

(a, b), cov = curve_fit(model, x, y)
da, db = np.sqrt(np.diag(cov))
print(f"a = {a:.3f} ± {da:.3f}")
print(f"b = {b:.3f} ± {db:.3f}")
```

## Læs videre

- [Lineær regression og aksetransformation]({{< relref "/docs/nat/lineaer-regression" >}})
- [Plot]({{< relref "/docs/python/snippets/plot" >}}) – gør grafen pænere
