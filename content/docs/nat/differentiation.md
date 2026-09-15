---
Title: Differentiation med Python
weight: 3
---

# Differentiation i Python — til Fysik A

Differentiation  finder hældningen af en graf eller funktion i et bestemt punkt eller som en funktion for hele udtrykket. Altså lidt i retning af "hvor stejl er grafen?". Har man fx en graf, eller nogle målinger der viser **position som funktion af tid** $s(t)$ så vil hældningen af denne graf $\frac{d(s(t))}{dt} = s'(t) = v(t)$  

| Din situation | Eksempel | Værktøj | Funktion |
| --- | --- | --- | --- |
| Du har **måledata** (en tabel af $x$ og $y$) | Fart fra position-tid | NumPy | `np.gradient` |
| Du har en **kendt funktion** $f(x)$ | $f'(x)$ i et punkt | SciPy | `differentiate.derivative` |
| Du vil have en **afledt funktion** (en formel) | $\frac{d}{dx}x^3 = 3x^2$ | SymPy | `diff` (nederst) |


## 1. Måledata: `np.gradient` 
Du har optaget data med loggerpro eller på en anden måde og du har dem som to talrækker i et regneark fx y(x) s(t) F(x) eller whatever. 
`np.gradient` finder hældningen i hvert punkt med centraldifferenser:

$$\frac{dy}{dx} \approx \frac{y_{i+1} - y_{i-1}}{x_{i+1} - x_{i-1}}$$

### Differentiér måledata

```python
import numpy as np

# Dine måledata 
t = np.array([0, 1, 2, 3, 4, 5])         # fx tid i s
s = np.array([0, 2, 8, 18, 32, 50])      # fx position i m

v = np.gradient(s, t)                    # differentier s med hensyn til t 
print(f'v = {v} i m/s ')  # hældning (fart) i hvert punkt
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

Acceleration er den anden afledede af positionen. Kør bare `np.gradient` to gange.
Data $s(t)$ er rigtige data optaget med loggerpro. Se her hvordan du nemt kan differentiere dem to gange med numpys gratients rutine *np.gradients* den virker klart bedst i midten fordi der har den flere data omkring punktet som dem kan arbejde med. Enderne vil altid drille !!

```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (6, 2) # laver plottet lidt smallere

t = np.array([0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
s = np.array([0.032,0.045,0.097,0.165,0.256,0.377,0.514,0.684,0.884,1.091,1.334])

v = np.gradient(s, t)
a = np.gradient(v, t)

plt.scatter(t, s);     plt.xlabel("t / s"); plt.ylabel("s / m");      plt.show()
plt.scatter(t, v);  plt.xlabel("t / s"); plt.ylabel("v / (m/s)");  plt.show()
plt.scatter(t, a);  plt.xlabel("t / s"); plt.ylabel("a / (m/s²)"); plt.show()
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
Jeg bruger aldrig det her !!! 
SymPy er pythons måde at lave symbolske beregninger som **Mapel** eller **Matcad**. Mere interessant for matematik end fysik eller kemi. 

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
