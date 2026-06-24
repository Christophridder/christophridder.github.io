---
Title: Lambda-funktioner i Python
weight: 20
---

# Lambda-funktioner

En **lambda** er bare en lille funktion på én linje, som du kan skrive uden navn. Den er smart, når du hurtigt skal sende en funktion videre — fx ind i `integrate.quad`.

## Syntaks

```python
lambda argumenter: udtryk
```

- alt før kolon er **input** (argumenterne)
- alt efter kolon er **det den returnerer** (ét udtryk, ingen `return`)

```python
f = lambda x: 0.25 * x**3
f(4)        # -> 16.0
```

## Kan den erstattes med def?

**Ja — altid.** En lambda er kun en kortere skrivemåde. De to her gør præcis det samme:

```python
# Med lambda
f = lambda x: 0.25 * x**3

# Med def — fuldstændig ækvivalent
def f(x):
    return 0.25 * x**3
```

Begge giver `16.0` i `integrate.quad(f, 0, 4)`.

## Hvornår bruger man hvad?

| | `lambda` | `def` |
| --- | --- | --- |
| Længde | Én linje | Flere linjer |
| Navn | Anonym (kan tildeles en variabel) | Har altid et navn |
| Flere beregningstrin | Nej | Ja |
| `return` | Underforstået | Skal skrives |
| Dokumentation (docstring) | Nej | Ja |
| God til | Hurtige engangsfunktioner | Genbrug og mere kompleks logik |

**Tommelfingerregel:** Skal funktionen bruges ét sted og fylder den én linje → `lambda`. Skal den genbruges, dokumenteres eller indeholde flere trin → `def`.

## Flere argumenter

En lambda kan godt tage flere input — adskil dem med komma:

```python
areal = lambda b, h: 0.5 * b * h
areal(4, 3)        # -> 6.0
```

## I integration-kontekst

Når du integrerer en kendt funktion, er lambda tit den hurtigste vej:

```python
from scipy import integrate

I = integrate.quad(lambda x: 0.25*x**3, 0, 4)[0]
print(I)        # 16.0
```

Bliver funktionen længere — eller skal du have parametre med `args` — så er `def` mere overskuelig:

```python
import numpy as np
from scipy import integrate

def integrand(x, a, b):
    return a*np.exp(-x**2) + b

I = integrate.quad(integrand, -10, 10, args=(4, 2))[0]
```
