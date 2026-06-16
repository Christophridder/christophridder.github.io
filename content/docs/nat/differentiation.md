---
Title: Differentiation med Python
weight: 3
---

# Differentiation i Python — til Fysik A

Differentiation er "hvor stejl er grafen?" — altså hældningen. I fysik er det fx **fart fra en position-tid-graf** eller **acceleration fra en fart-tid-graf**. Find din situation og hop til den rigtige snippet.

| Din situation | Eksempel | Værktøj | Funktion |
| --- | --- | --- | --- |
| Du har **måledata** (en tabel af $x$ og $y$) | Fart fra position-tid | NumPy | `np.gradient` |
| Du har en **kendt funktion** $f(x)$ | $f'(x)$ i et punkt | SciPy | `differentiate.derivative` |
| Du vil have en **afledt funktion** (en formel) | $\frac{d}{dx}\,x^3 = 3x^2$ | SymPy | `diff` (nederst) |

> **Bemærk (opdatering 2024–):** I gamle vejledninger ser du `scipy.misc.derivative`. Den er **fjernet** (hele `scipy.misc` er på vej ud). Brug i stedet `scipy.differentiate.derivative` til kendte funktioner, og `np.gradient` til måledata.

---

## 1. Måledata: `np.gradient` (integral over eksperimentelle data)

Du har sjældent en formel — du har en **måletabel**. `np.gradient` finder hældningen i hvert punkt med centraldifferenser:

$$\frac{dy}{dx} \approx \frac{y_{i+1} - y_{i-1}}{x_{i+1} - x_{i-1}}$$

### Klip-og-klar: differentiér måledata

```python
import numpy as np

# Dine måledata (skift tallene ud)
t = np.array([0, 1, 2, 3, 4, 5])         # fx tid i s
x = np.array([0, 2, 8, 18, 32, 50])      # fx position i m

v = np.gradient(x, t)                      # bemærk: y FØR x
print(v)                                   # hældning (fart) i hvert punkt
```

`np.gradient(y, x)` kræver **ikke** lige store skridt — perfekt til rigtige målinger.

### De klassiske fysik-afledede — samme snippet, ny tolkning

Alt herunder er "hældning af en graf" og løses med præcis samme kode:

| Fysisk størrelse | Afledt | `x` | `y` |
| --- | --- | --- | --- |
| Fart | $v = \dfrac{dx}{dt}$ | tid | position |
| Acceleration | $a = \dfrac{dv}{dt}$ | tid | fart |
| Kraft | $F = \dfrac{dA}{ds}$ | vej | arbejde |
| Strøm | $I = \dfrac{dQ}{dt}$ | tid | ladning |
| Effekt | $P = \dfrac{dE}{dt}$ | tid | energi |
| Henfaldsrate (aktivitet) | $\dfrac{dN}{dt} = -k\cdot N$ | tid | antal kerner |

> **Pas på enderne:** `np.gradient` er mest præcis i midten af dine data. Det første og sidste punkt regnes med en simplere ensidet difference og er lidt mere unøjagtige.

---

## 2. Acceleration: differentiér to gange

Acceleration er den anden afledede af positionen. Kør bare `np.gradient` to gange:

```python
import numpy as np

t = np.linspace(0, 5, 11)
x = 3 + 2*t + 0.5*9.82*t**2               # målt position

v = np.gradient(x, t)                      # fart
a = np.gradient(v, t)                      # acceleration

print(f"Acceleration (midten) ≈ {a[5]:.3g} m/s²")   # ≈ 9,82
```

---

## 3. Kendt funktion: `scipy.differentiate.derivative`

Har du en formel for $f(x)$, så kan du få den afledede i et punkt numerisk. Resultatet ligger i `.df`:

```python
import numpy as np
from scipy.differentiate import derivative

f = lambda x: 0.25 * x**3

res = derivative(f, 4.0)                    # f'(x) i x = 4
print(f"f'(4) = {res.df:.4g}")              # -> 12
```

Et fysik-eksempel — Gauss-funktionens hældning:

```python
import numpy as np
from scipy.differentiate import derivative

f = lambda x: np.exp(-x**2)
res = derivative(f, 1.0)
print(f"f'(1) = {res.df:.4g}")              # -> -0,7358
```

> `scipy.differentiate` er ny i SciPy 1.15. Har du en ældre version, kan du i stedet selv lave en simpel difference: `(f(x+h) - f(x-h)) / (2*h)` med fx `h = 1e-5`.

---

## 4. Find et maksimum eller minimum

I fysik er toppunktet tit interessant — fx hvor et kast er højest (der hvor farten skifter fortegn, $v = 0$). Du kan finde det fra måledata ved at lede efter, hvor den afledede skifter fortegn:

```python
import numpy as np

t = np.linspace(0, 4, 41)
h = 20*t - 0.5*9.82*t**2                   # højde af et lodret kast

v = np.gradient(h, t)                       # fart
top = np.argmax(h)                          # indeks for største højde
print(f"Toppen nås ved t ≈ {t[top]:.2g} s, h ≈ {h[top]:.3g} m")
print(f"Farten dér ≈ {v[top]:.2g} m/s (tæt på 0)")
```

---

## 5. Plot funktion og dens afledede

```python
import numpy as np
import matplotlib.pyplot as plt

x  = np.linspace(-3, 3, 400)
y  = np.exp(-x**2)
dy = np.gradient(y, x)

plt.plot(x, y,  label="f(x)")
plt.plot(x, dy, label="f'(x)")
plt.legend(); plt.grid(True)
plt.show()
```

---

## Appendiks: SymPy — symbolsk differentiation

> Bruger du i praksis sjældent. Tag det med her, hvis du har brug for en **formel** for den afledede frem for et tal.

```python
from sympy import symbols, diff

x = symbols('x')
diff(x**3 - 4*x**2 + 10*x - 3, x)         # -> 3*x**2 - 8*x + 10
```

**Anden afledede** (skriv tallet til sidst):

```python
from sympy import symbols, diff

x = symbols('x')
diff(x**3 - 4*x**2 + 10*x - 3, x, 2)      # -> 6*x - 8
```

**Værdi i et punkt** (indsæt med `subs`):

```python
from sympy import symbols, diff

x = symbols('x')
fmark = diff(0.25*x**3, x)                 # 0.75*x**2
fmark.subs(x, 4)                           # -> 12
```

**Fysik-eksempel — henfaldsrate** (bemærk: henfaldskonstanten er $k$):

```python
from sympy import symbols, diff, exp

t, k, N0 = symbols('t k N0')
N = N0*exp(-k*t)
diff(N, t)                                 # -> -N0*k*exp(-k*t) = -k*N
```

> **Tommelfingerregel:** Hold SymPy adskilt fra `numpy`/`scipy`. Brug SymPy når du vil have en formel, og `np.gradient`/`differentiate.derivative` når du vil have tal.
