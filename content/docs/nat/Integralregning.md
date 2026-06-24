---
Title: Integralregning
weight: 1
---
---
Title: Integralregning med Python
weight: 1
---

# Integraler i Python — til Fysik A

Når du skal integrere i en fysikopgave, er der reelt **to situationer**. Find din situation i tabellen, og hop direkte til den rigtige snippet.

| Din situation | Eksempel | Værktøj | Funktion |
| --- | --- | --- | --- |
| Du har **måledata** (en tabel af $x$ og $y$) | Areal under en kraft-vej-graf | NumPy | `np.trapezoid` |
| Måledata, men du vil have den **kumulerede** kurve | Position fra fart-tid | SciPy | `cumulative_trapezoid` |
| Du har en **kendt funktion** $f(x)$ | $\int_0^4 \tfrac14 x^3\,dx$ | SciPy | `integrate.quad` |
| Du vil have en **stamfunktion** (en formel) | $\int x^3\,dx = \tfrac14 x^4$ | SymPy | `integrate` (nederst) |

> **Bemærk (opdatering 2024–):** I gamle vejledninger ser du ofte `np.trapz`, `scipy.integrate.trapz` og `simps`. De er **fjernet** i NumPy 2.0 og SciPy 1.14. Brug i stedet `np.trapezoid`, `trapezoid` og `simpson`. Tilsvarende findes `scipy.pi` ikke mere — brug `np.pi`.

---

## 1. Måledata: trapez-metoden, når du skal finde integralet for måledata

I praksis har du sjældent en pæn funktion — du har en **måletabel**. Så er trapez-metoden dit standardværktøj. Den lægger små trapezer under datapunkterne og summer dem:

$$\int_a^b y\,dx \approx \sum \frac{(y_i + y_{i+1})}{2}\cdot \Delta x$$

### Klip-og-klar: areal under måledata

```python
import numpy as np

# Dine måledata (skift tallene ud)
x = np.array([0, 0.5, 1.0, 1.5, 2.0])    # fx position i m
y = np.array([0, 2.0, 3.5, 4.0, 4.2])    # fx kraft i N

areal = np.trapezoid(y, x)               # bemærk: y FØR x
print(f"Integralet (arealet) = {areal:.3g}")
```

`np.trapezoid(y, x)` kræver **ikke** lige store skridt mellem dine $x$-værdier — perfekt til rigtige målinger.

### De klassiske fysik-integraler — samme snippet, ny tolkning

Alle disse er "areal under en graf" og løses med præcis samme kode:

| Fysisk størrelse | Integral | `x` | `y` |
| --- | --- | --- | --- |
| Arbejde | $W = \int F dx$ | position | kraft |
| Strækning | $s = \int v dt$ | tid | fart |
| Impuls | $J = \int F dt$ | tid | kraft |
| Ladning | $Q = \int I dt$ | tid | strøm |
| Energi | $E = \int P dt$ | tid | effekt |

**Eksempel — arbejde fra en kraft-vej-måling:**

```python
import numpy as np

x = np.array([0, 0.5, 1.0, 1.5, 2.0])    # vej i m
F = np.array([0, 2.0, 3.5, 4.0, 4.2])    # kraft i N

W = np.trapezoid(F, x)
print(f"Arbejde W = {W:.3g} J")          # -> 5,8 J
```

---

## 2. Kumuleret integral: fx position undervejs

Nogle gange vil du ikke kun have det **samlede** integral, men kurven undervejs — fx hvor langt bilen er kørt til hvert tidspunkt. Brug `cumulative_trapezoid`:

```python
import numpy as np
from scipy import integrate

t = np.array([0, 1, 2, 3, 4, 5])         # tid i s
v = np.array([0, 2, 5, 9, 12, 14])       # fart i m/s

s = integrate.cumulative_trapezoid(v, t, initial=0)
print(s)                                  # strækning ved hvert t
print(f"Samlet strækning = {s[-1]:.3g} m")
```

- `initial=0` sørger for at kurven starter i 0 og har samme længde som dine data.
- `s[-1]` er den samlede strækning (samme tal som `np.trapezoid`).

---

## 3. Mere præcist på pæne data: Simpson

Hvis dine data er glatte og du har et **lige antal intervaller**, giver Simpsons metode ofte et bedre bud end trapez:

```python
import numpy as np
from scipy import integrate

x = np.linspace(0, 4, 5)
y = 0.25 * x**3

print(f"trapez   = {np.trapezoid(y, x):.4g}")
print(f"simpson  = {integrate.simpson(y, x=x):.4g}")
```

På få punkter ser man tydeligt forskellen: trapez giver her 17, mens Simpson rammer det eksakte 16.

---

## 4. Kendt funktion: scipy `quad`

Har du en formel for $f(x)$, så regn integralet numerisk med `quad`. Den returnerer **to tal**: værdien og en usikkerhed.

### Et bestemt integral hvor du kender den matematiske formel

```python
from scipy import integrate

f = lambda x: 0.25 * x**3              # din funktion f(x) = 0.25 * x^3
vaerdi, usik = integrate.quad(f, 0, 4)  # grænser 0 til 4
print(f"Integral = {vaerdi:.4g}")      # -> 16
```

Vil du regne videre med tallet, så tag bare det første element:

```python
I = integrate.quad(lambda x: 0.25*x**3, 0, 4)[0]
```

### Uendelige grænser

`quad` kan håndtere $\pm\infty$ via `np.inf`:

```python
import numpy as np
from scipy import integrate

f = lambda x: np.exp(-x**2)
I = integrate.quad(f, -np.inf, np.inf)[0]
print(f"{I:.6g}")                       # = sqrt(pi)
```

### Funktion med parametre (`args`)

Skal funktionen indeholde konstanter, så definér dem som ekstra argumenter og send dem med via `args`:

```python
import numpy as np
from scipy import integrate

def f(x, a, b):
    return a*np.exp(-x**2) + b

I = integrate.quad(f, -10, 10, args=(4, 2))[0] #a = 4 og b = 2
print(f"{I:.6g}")
```

### Areal mellem to kurver

Træk de to integraler fra hinanden:

```python
from scipy import integrate

oeverst  = lambda x: -x**2 + 4
nederst  = lambda x:  x**2 - 4

A = integrate.quad(oeverst, -2, 2)[0] - integrate.quad(nederst, -2, 2)[0]
print(f"Areal = {A:.4g}")
```

### Rotationslegeme (omdrejningslegeme)

Volumenet af det legeme $f(x)$ danner ved omdrejning om $x$-aksen:

$$V = \pi \int_a^b \big(f(x)\big)^2\,dx$$

```python
import numpy as np
from scipy import integrate

f = lambda x: 0.5 * x                   # fx en kegle
a, b = 0, 10

V = integrate.quad(lambda x: np.pi*f(x)**2, a, b)[0]
print(f"Volumen = {V:.4g}")
```

---

## 5. Hurtigt plot af integranden

Et plot giver tit indsigt i forløbet, før du regner:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.exp(-x**2)

plt.plot(x, y)
plt.xlabel("x"); plt.ylabel("f(x)")
plt.grid(True)
plt.show()
```

---

## Appendiks: SymPy — symbolsk integration

> Bruger du i praksis sjældent. Tag det med her, hvis du har brug for en **formel** (stamfunktion) frem for et tal — altså noget i stil med Maple, Maxima eller WolframAlpha.

```python
from sympy import symbols, integrate, exp, sin, ln, pi, oo

x = symbols('x')

integrate(x**3 - 4*x**2 + 10*x - 3, x)        # stamfunktion (formel)
```

**Bestemt integral** (sæt grænser som en tuple):

```python
from sympy import symbols, integrate

x = symbols('x')
integrate(x**3 - 4*x**2 + 10*x - 3, (x, 0, 4))        # -> 140/3 (eksakt brøk)
```

Tilføj `.evalf()` for et decimaltal:

```python
integrate(x**3 - 4*x**2 + 10*x - 3, (x, 0, 4)).evalf()  # -> 46,667
```

**Uendelige grænser** klares med `oo`:

```python
from sympy import symbols, integrate, exp, oo, sqrt, pi

x = symbols('x')
integrate(exp(-x**2), (x, -oo, oo))           # -> sqrt(pi), eksakt
```

Et par flere eksempler:

```python
from sympy import symbols, integrate, sin, ln

x = symbols('x')
integrate(ln(x))        # x*log(x) - x
integrate(4*x**3)       # x**4
integrate(sin(x))       # -cos(x)
```

> **Tommelfingerregel:** SymPy passer dårligt sammen med `numpy`/`scipy` i samme udregning. Hold dem adskilt — brug SymPy når du vil have en formel, og `quad`/`trapezoid` når du vil have et tal.
