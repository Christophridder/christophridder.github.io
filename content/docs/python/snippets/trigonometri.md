---
title: "Trigonometri"
weight: 4
---

# Trigonometri: sin, cos, tan – radianer og grader

## Den vigtigste regel

> **Python regner altid i radianer.** `np.sin(30)` er *ikke* sin(30°)!

```python
import numpy as np

print(np.sin(30))               # -0.988   ← sin(30 radianer) – forkert!
print(np.sin(np.radians(30)))   #  0.49999999999999994 ≈ 0.5  ← sin(30°) – rigtigt
```

## Omregning mellem grader og radianer

$$v_{\text{rad}} = v_{\text{grader}} \cdot \frac{\pi}{180^\circ} \qquad v_{\text{grader}} = v_{\text{rad}} \cdot \frac{180^\circ}{\pi}$$

```python
import numpy as np

v_rad = np.radians(45)      # grader → radianer   (0.785)
v_grad = np.degrees(np.pi)  # radianer → grader   (180.0)
```

| Grader | 0° | 30° | 45° | 60° | 90° | 180° | 360° |
|---|---|---|---|---|---|---|---|
| Radianer | 0 | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $2\pi$ |

## Funktionerne

| Funktion | Python | Input | Output |
|---|---|---|---|
| sin, cos, tan | `np.sin(v)`, `np.cos(v)`, `np.tan(v)` | vinkel i **rad** | tal |
| sin⁻¹, cos⁻¹, tan⁻¹ | `np.arcsin(x)`, `np.arccos(x)`, `np.arctan(x)` | tal | vinkel i **rad** |
| Vinkel ud fra to kateter | `np.arctan2(y, x)` | to tal | vinkel i **rad** (−π til π) |

Husk at omregne til grader til sidst med `np.degrees(...)`.

## Retvinklet trekant: vinkel ud fra to sider

En rampe er 3,0 m lang vandret og 0,80 m høj. Hvad er hældningsvinklen?

$$\tan(v) = \frac{\text{modstående}}{\text{hosliggende}}$$

```python
import numpy as np

modst = 0.80     # m
hosl = 3.0       # m

v = np.arctan(modst / hosl)
print(f"v = {v:.3f} rad = {np.degrees(v):.1f}°")      # 0.261 rad = 14.9°

hyp = np.hypot(modst, hosl)                            # Pythagoras: √(a² + b²)
print(f"Hypotenusen er {hyp:.2f} m")
```

## Opløs en vektor i komposanter

En kraft på 50 N trækker 30° over vandret:

```python
import numpy as np

F = 50              # N
vinkel = 30         # grader

Fx = F * np.cos(np.radians(vinkel))
Fy = F * np.sin(np.radians(vinkel))
print(f"Fx = {Fx:.1f} N,  Fy = {Fy:.1f} N")             # 43.3 N og 25.0 N
```

Og den anden vej – fra komposanter til størrelse og retning:

```python
import numpy as np

vx, vy = 4.0, -3.0          # m/s

v = np.hypot(vx, vy)                         # størrelse
retning = np.degrees(np.arctan2(vy, vx))     # vinkel i forhold til x-aksen
print(f"v = {v:.1f} m/s i retningen {retning:.1f}°")   # 5.0 m/s, -36.9°
```

> **Brug `arctan2(y, x)` frem for `arctan(y/x)`** til vektorer. `arctan` kan ikke se forskel på fx (3, 4) og (−3, −4), fordi brøken er den samme. `arctan2` kender kvadranten.

## Brydningsloven

$n_1 \cdot \sin(i) = n_2 \cdot \sin(b)$. Lys går fra luft ($n_1 = 1{,}00$) ind i vand ($n_2 = 1{,}33$) med indfaldsvinklen 40°:

```python
import numpy as np

n1, n2 = 1.00, 1.33
i = 40                                       # grader

b = np.degrees(np.arcsin(n1 * np.sin(np.radians(i)) / n2))
print(f"Brydningsvinkel: {b:.1f}°")          # 28.9°
```

## Plot med grader på x-aksen

```python
import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(0, 360, 361)                 # grader
plt.plot(v, np.sin(np.radians(v)), label="sin(v)")
plt.plot(v, np.cos(np.radians(v)), label="cos(v)")
plt.xticks(np.arange(0, 361, 45))
plt.xlabel("v / grader")
plt.axhline(0, color="k", lw=0.8)
plt.grid()
plt.legend()
plt.show()
```

## Plot med π på x-aksen

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 300)             # radianer
plt.plot(x, np.sin(x))
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ["0", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
plt.xlabel("x / rad")
plt.grid()
plt.show()
```

## `math` eller `numpy`?

Begge har `sin`, `cos`, `radians` osv. Brug **`numpy`** (`np.sin`), for den virker både på ét tal og på en hel liste – og det skal du bruge, når du plotter.
