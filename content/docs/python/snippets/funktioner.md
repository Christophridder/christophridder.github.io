---
title: "Funktioner"
weight: 2
---

# Funktioner i Python

En funktion er en lille "maskine": Du giver den nogle tal (**argumenter**), og den giver et resultat tilbage (**returværdi**). Det svarer til en formel i fysik.

## Den simpleste funktion

Kinetisk energi $E_{\text{kin}} = \tfrac{1}{2} \cdot m \cdot v^2$:

```python
def E_kin(m, v):
    return 0.5 * m * v**2

print(E_kin(2, 3))        # 2 kg med farten 3 m/s  →  9.0
```

Læg mærke til:

| Del | Betydning |
|---|---|
| `def` | "Nu definerer jeg en funktion" |
| `E_kin` | Funktionens navn (ingen mellemrum, ingen æøå) |
| `(m, v)` | Argumenterne – de tal, funktionen skal bruge |
| `:` | Kolon i slutningen af linjen er **obligatorisk** |
| indrykning | Alt, der hører til funktionen, skal rykkes ind (4 mellemrum / Tab) |
| `return` | Det, funktionen giver tilbage |

## Typiske fejl

| Fejl | Rigtigt | Forklaring |
|---|---|---|
| `v^2` | `v**2` | `^` betyder noget helt andet i Python! Potens er `**` |
| `9,82` | `9.82` | Decimaltegn er punktum |
| Glemt `return` | `return 0.5*m*v**2` | Uden `return` giver funktionen `None` tilbage |
| `2m` | `2*m` | Gangetegnet skal altid skrives |
| Glemt kolon | `def f(x):` | Giver `SyntaxError` |

## Funktioner med numpy – regn på mange tal på én gang

Bruger du `numpy`-funktioner (`np.sin`, `np.exp`, `np.sqrt` …), virker din funktion også på en hel liste af tal. Det er smart til grafer:

```python
import numpy as np
import matplotlib.pyplot as plt

def N(t, N0, k):
    """Antal kerner tilbage efter tiden t (radioaktivt henfald)."""
    return N0 * np.exp(-k * t)

t = np.linspace(0, 100, 200)       # 200 tider mellem 0 og 100 s
plt.plot(t, N(t, 1000, 0.05))
plt.xlabel("t / s")
plt.ylabel("N")
plt.show()
```

> Brug `np.exp`, ikke `math.exp`. `math`-udgaven virker kun på ét tal ad gangen.

## Standardværdier for argumenter

Giv et argument en standardværdi med `=`. Så behøver du kun skrive det, hvis du vil ændre det:

```python
def tyngdekraft(m, g=9.82):
    return m * g

print(tyngdekraft(5))           # bruger g = 9.82   → 49.1
print(tyngdekraft(5, g=1.62))   # på Månen          → 8.100000000000001
print(f"{tyngdekraft(5, g=1.62):.3g}")   # pænere    → 8.1
```

## Flere returværdier

En funktion kan give flere ting tilbage på én gang:

```python
import numpy as np

def skraat_kast(v0, vinkel_grader, g=9.82):
    """Returnerer kastevidde og maksimal højde for et skråt kast fra jorden."""
    theta = np.radians(vinkel_grader)
    vidde = v0**2 * np.sin(2 * theta) / g
    hoejde = (v0 * np.sin(theta))**2 / (2 * g)
    return vidde, hoejde

vidde, hoejde = skraat_kast(15, 45)
print(f"Vidde: {vidde:.3g} m,  højde: {hoejde:.3g} m")
```

## Funktioner med fysikkonstanter

Læg konstanter øverst, så du kun skal skrive dem én gang:

```python
import numpy as np

G = 6.674e-11        # N·m²/kg²   (6.674e-11 betyder 6,674 · 10⁻¹¹)
M_jord = 5.972e24    # kg
R_jord = 6.371e6     # m

def g_i_hoejden(h):
    """Tyngdeaccelerationen i højden h over jordoverfladen."""
    return G * M_jord / (R_jord + h)**2

print(f"Ved overfladen: {g_i_hoejden(0):.3g} m/s²")
print(f"ISS (408 km):   {g_i_hoejden(408e3):.3g} m/s²")
```

## Pænt output med f-strings

Computeren regner med binære tal, så der kan komme små afrundingsrester som `8.100000000000001`. Brug f-strings til at vise et passende antal cifre:


| Kode | Resultat for `x = 1234.5678` | Betydning |
|---|---|---|
| `f"{x}"` | `1234.5678` | Som det er |
| `f"{x:.2f}"` | `1234.57` | 2 **decimaler** |
| `f"{x:.3g}"` | `1.23e+03` | 3 **betydende cifre** |
| `f"{x:.3e}"` | `1.235e+03` | Videnskabelig notation |

> `.2f` styrer antal decimaler, mens `.3g` styrer antal **betydende cifre** – det er som regel `g`, du vil have i fysik.

## Korte funktioner: lambda

Til helt små funktioner på én linje kan du bruge `lambda`. Se [Lambda-funktioner]({{< relref "/docs/nat/lambda-funktioner" >}}).

```python
f = lambda x: 3*x**2 + 2
print(f(2))     # 14
```
