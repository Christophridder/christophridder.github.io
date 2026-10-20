---
title: "Plot"
weight: 3
---

# Plot med matplotlib – opslagsside

Find det, du skal bruge, og kopiér linjen ind i dit eget plot. Alle linjer skal stå **før** `plt.show()`.

**Indhold:** [Skabelon](#skabelon) · [Farver og linjer](#farver-linjer-og-markører) · [Akser](#aksetitler-og-aksegrænser) · [Ticks](#ticks-tal-på-akserne) · [Gitter](#gitter) · [Vandrette og lodrette linjer](#vandrette-og-lodrette-linjer) · [Tekst og formler](#tekst-og-formler) · [Forklaring](#forklaring-legend) · [Subplots](#subplots--flere-grafer-ved-siden-af-hinanden) · [Akser gennem (0,0)](#akser-gennem-0-0) · [Fejlstænger](#fejlstænger) · [Log-akse](#logaritmisk-akse) · [Søjlediagram](#søjlediagram) · [Gem](#gem-figuren)

## Skabelon

Start altid her:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)       # 200 x-værdier fra 0 til 10
y = np.sin(x)

plt.figure(figsize=(8, 5))        # bredde, højde i tommer
plt.plot(x, y, label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Min første graf")
plt.grid()
plt.legend()
plt.show()
```

**Målepunkter i stedet for en linje:**

```python
plt.scatter(x_data, y_data, label="Målinger")          # prikker
plt.plot(x_data, y_data, "o", label="Målinger")        # samme med plot
```

## Farver, linjer og markører

Den hurtige måde: en kort tekst som tredje argument, fx `"r--"` = rød stiplet linje.

```python
plt.plot(x, y, "r-")       # rød fuld linje
plt.plot(x, y, "b--")      # blå stiplet
plt.plot(x, y, "k:")       # sort prikket
plt.plot(x, y, "go")       # grønne cirkler (ingen linje)
plt.plot(x, y, "ms-")      # magenta firkanter forbundet med linje
```

| Farve | | Linje | | Markør | |
|---|---|---|---|---|---|
| `r` | rød | `-` | fuld | `o` | cirkel |
| `b` | blå | `--` | stiplet | `s` | firkant |
| `g` | grøn | `:` | prikket | `^` | trekant |
| `k` | sort | `-.` | streg-prik | `x` | kryds |
| `m` | magenta | | | `*` | stjerne |
| `c` | cyan | | | `.` | lille prik |

**Den lange måde** – flere muligheder:

```python
plt.plot(x, y, color="darkorange", linestyle="--", linewidth=2.5,
         marker="o", markersize=4, alpha=0.7)          # alpha = gennemsigtighed
plt.scatter(x, y, s=10, color="teal")                    # s = punktstørrelse
```

Farver kan også skrives som navne (`"navy"`, `"crimson"`, `"teal"`) eller hex-koder (`"#1f5fa8"`).

## Aksetitler og aksegrænser

```python
plt.xlabel("t / s", fontsize=14)            # aksetitel med enhed
plt.ylabel("v / (m/s)", fontsize=14)
plt.title("Hastighed som funktion af tid", fontsize=16)

plt.xlim(0, 10)                             # x-aksen fra 0 til 10
plt.ylim(-2, 2)                             # y-aksen fra -2 til 2
plt.axis([0, 10, -2, 2])                    # begge på én gang
```

> **Enheder:** Skriv aksetitlen som *størrelse / enhed*, fx `t / s` eller `F / N`.

## Ticks (tal på akserne)

```python
plt.xticks(np.arange(0, 11, 1))                 # et tal for hver 1 fra 0 til 10
plt.yticks([-1, -0.5, 0, 0.5, 1])               # præcis disse tal
plt.xticks([0, np.pi, 2*np.pi], ["0", "π", "2π"])  # egne tekster på ticks
plt.xticks(rotation=45)                          # drej teksten
plt.tick_params(labelsize=12)                    # størrelse på tallene
plt.xticks([])                                   # ingen tal på x-aksen
plt.minorticks_on()                              # små mellem-ticks
```

**Komma som decimaltegn** på akserne:

```python
from matplotlib.ticker import FuncFormatter

komma = FuncFormatter(lambda v, pos: f"{v:g}".replace(".", ","))
plt.gca().xaxis.set_major_formatter(komma)
plt.gca().yaxis.set_major_formatter(komma)
```

## Gitter

```python
plt.grid()                                           # standardgitter
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)   # diskret gitter
plt.minorticks_on()
plt.grid(which="minor", linestyle=":", alpha=0.3)    # fint gitter (millimeterpapir)
```

## Vandrette og lodrette linjer

```python
plt.axhline(y=0, color="k", linewidth=1)                   # vandret linje hele vejen
plt.axvline(x=2.5, color="r", linestyle="--")              # lodret linje hele vejen
plt.hlines(y=0.5, xmin=0, xmax=4, colors="b")              # vandret linje fra x=0 til 4
plt.vlines(x=[1, 2, 3], ymin=0, ymax=1, colors="g")        # flere lodrette linjer
plt.axhspan(-0.2, 0.2, color="yellow", alpha=0.3)          # farvet vandret bånd
plt.axvspan(4, 6, color="gray", alpha=0.2)                 # farvet lodret bånd
```

## Tekst og formler

Tekst mellem `$ … $` skrives som en matematisk formel (LaTeX). Sæt `r` foran teksten:

```python
plt.text(2, 0.5, "Her er toppen", fontsize=12)                     # tekst i punktet (2; 0,5)
plt.text(6, -0.8, r"$E_{kin} = \frac{1}{2} m v^2$", fontsize=14)    # formel
plt.xlabel(r"$\Delta t$ / s")                                      # græsk bogstav i aksetitel
plt.title(r"$y = A \cdot \sin(\omega t)$")

plt.annotate("Maksimum", xy=(np.pi/2, 1), xytext=(3, 1.3),        # tekst med pil
             arrowprops=dict(arrowstyle="->"))
```

| Skriv | Får | | Skriv | Får |
|---|---|---|---|---|
| `$x^2$` | $x^2$ | | `$\alpha, \beta, \lambda$` | $\alpha, \beta, \lambda$ |
| `$v_0$` | $v_0$ | | `$\Delta, \omega, \pi$` | $\Delta, \omega, \pi$ |
| `$E_{kin}$` | $E_{kin}$ | | `$\frac{a}{b}$` | $\frac{a}{b}$ |
| `$10^{-3}$` | $10^{-3}$ | | `$\sqrt{x}$` | $\sqrt{x}$ |
| `$\cdot$` | $\cdot$ | | `$^\circ$C` | $^\circ$C |

**Tal fra beregningen ind i teksten** – brug en f-string:

```python
a = 9.4317
plt.text(1, 0.8, f"a = {a:.3g} N/kg")
plt.plot(x, y, label=f"y = {a:.3g}·x")
```

## Forklaring (legend)

Giv hver graf en `label=` og kald `plt.legend()` til sidst:

```python
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()                              # Python finder selv en god plads
plt.legend(loc="upper right")             # eller vælg selv
plt.legend(fontsize=12, frameon=False)    # større tekst, uden ramme
```

`loc` kan være `"upper left"`, `"upper right"`, `"lower left"`, `"lower right"`, `"center"` eller `"best"`.

## Subplots – flere grafer ved siden af hinanden

Til flere grafer bruger du `fig, ax = plt.subplots(...)`. Bemærk, at kommandoerne så hedder `ax.set_xlabel` i stedet for `plt.xlabel`.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4, 200)
s = 5 * t**2
v = 10 * t

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)   # 2 rækker, 1 søjle

ax1.plot(t, s, "b")
ax1.set_ylabel("s / m")
ax1.set_title("Bevægelse med konstant acceleration")
ax1.grid()

ax2.plot(t, v, "r")
ax2.set_xlabel("t / s")
ax2.set_ylabel("v / (m/s)")
ax2.grid()

plt.tight_layout()           # sørger for, at tekst ikke overlapper
plt.show()
```

- Ved siden af hinanden: `plt.subplots(1, 2)`
- 2 × 2 grafer: `fig, axs = plt.subplots(2, 2)` og brug `axs[0, 0]`, `axs[0, 1]` osv.

| `plt.`-kommando | Tilsvarende `ax.`-kommando |
|---|---|
| `plt.xlabel(...)` | `ax.set_xlabel(...)` |
| `plt.ylabel(...)` | `ax.set_ylabel(...)` |
| `plt.title(...)` | `ax.set_title(...)` |
| `plt.xlim(...)` | `ax.set_xlim(...)` |
| `plt.xticks(...)` | `ax.set_xticks(...)` |
| `plt.plot`, `plt.grid`, `plt.legend`, `plt.text`, `plt.axhline` | `ax.plot`, `ax.grid`, `ax.legend`, `ax.text`, `ax.axhline` |

## Akser gennem (0, 0)

Som i matematikbogen – akserne krydser i origo:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 300)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.spines["left"].set_position("zero")       # y-aksen gennem x = 0
ax.spines["bottom"].set_position("zero")     # x-aksen gennem y = 0
ax.spines["right"].set_color("none")         # fjern rammen til højre
ax.spines["top"].set_color("none")           # og foroven
plt.show()
```

## Fejlstænger

Vis usikkerheden på dine målepunkter:

```python
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
y_usik = np.array([0.2, 0.2, 0.3, 0.3, 0.4])

plt.errorbar(x_data, y_data, yerr=y_usik, fmt="o", capsize=4, label="Målinger")
```

`xerr=` giver vandrette fejlstænger.

## Logaritmisk akse

```python
plt.yscale("log")        # y-aksen logaritmisk (enkeltlogaritmisk papir)
plt.xscale("log")        # også x-aksen (dobbeltlogaritmisk papir)
```

Eksponentielle sammenhænge bliver rette linjer med log på y-aksen, potenssammenhænge med log på begge akser.

## Søjlediagram

```python
import matplotlib.pyplot as plt

grundstof = ["H", "He", "Li", "Be"]
masse = [1.008, 4.003, 6.94, 9.012]

plt.bar(grundstof, masse, color="steelblue")
plt.ylabel("Atommasse / u")
plt.show()
```

## Gem figuren

```python
plt.savefig("min_graf.png", dpi=300, bbox_inches="tight")   # høj opløsning, ingen tom kant
plt.savefig("min_graf.pdf")                                  # vektorgrafik til rapporten
plt.show()                                                   # savefig skal stå FØR show
```

## Større tekst over det hele

Står det hele for småt i din rapport? Sæt det én gang øverst:

```python
plt.rcParams.update({"font.size": 14})
```

## Alt samlet i ét eksempel

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 300)
y = 2 * np.exp(-0.2 * t) * np.cos(2 * t)
t_data = np.arange(0, 10.5, 1.0)
y_data = 2 * np.exp(-0.2 * t_data) * np.cos(2 * t_data) + np.array(
    [0.05, -0.08, 0.06, -0.03, 0.07, -0.05, 0.02, -0.06, 0.04, -0.02, 0.03])

plt.figure(figsize=(9, 5))
plt.plot(t, y, "b-", lw=2, label="Model")
plt.errorbar(t_data, y_data, yerr=0.1, fmt="o", color="darkorange", capsize=3, label="Målinger")
plt.plot(t, 2*np.exp(-0.2*t), "k--", lw=1, label=r"$\pm 2 e^{-0{,}2 t}$")
plt.plot(t, -2*np.exp(-0.2*t), "k--", lw=1)
plt.axhline(0, color="gray", lw=1)
plt.text(6, 1.4, r"$y = 2 e^{-0{,}2 t} \cdot \cos(2t)$", fontsize=14)
plt.xlabel("t / s", fontsize=13)
plt.ylabel("y / cm", fontsize=13)
plt.title("Dæmpet svingning", fontsize=15)
plt.xticks(np.arange(0, 11, 1))
plt.xlim(0, 10)
plt.grid(alpha=0.4)
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
```

![Dæmpet svingning med model, målinger med fejlstænger, indhyllingskurver og formel](/img/python/plot-samlet.svg)
