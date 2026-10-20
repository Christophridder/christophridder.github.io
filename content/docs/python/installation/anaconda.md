---
title: "Jupyter med Anaconda"
weight: 2
---

# Jupyter med Anaconda

Anaconda installerer Python, Jupyter og alle de pakker, du skal bruge i fysik og kemi (`numpy`, `scipy`, `matplotlib`, `sympy`, `pandas`) på én gang.

## 1. Download

👉 **[anaconda.com/download](https://www.anaconda.com/download)**

Du bliver bedt om en e-mail – klik på **Skip registration** (eller *Skip to download*) for at springe over.

| Styresystem | Vælg |
|---|---|
| Windows | *64-Bit Graphical Installer* |
| Mac med M1/M2/M3/M4 | *64-Bit (Apple silicon) Graphical Installer* |
| Mac med Intel | *64-Bit (Intel chip) Graphical Installer* |
| Linux | *64-Bit (x86) Installer* (`.sh`-fil) |

> Usikker på din Mac? Klik på æblet øverst til venstre → **Om denne Mac**. Står der *Chip: Apple M…*, er det Apple Silicon.

## 2. Installér

### Windows

1. Dobbeltklik på `.exe`-filen.
2. Vælg **Just Me** og behold standardindstillingerne.
3. Klik **Install** og vent (5–10 min).

### Mac

1. Dobbeltklik på `.pkg`-filen.
2. Klik dig igennem med **Fortsæt** og **Installér**.

### Linux

Åbn en terminal i mappen, hvor filen ligger, og kør:

```bash
bash Anaconda3-*.sh
```

Tryk **Enter**/**Mellemrum** gennem licensen, skriv `yes`, og svar `yes` til spørgsmålet om at initialisere conda. Luk terminalen og åbn en ny.

## 3. Start Jupyter

| Styresystem | Sådan |
|---|---|
| Windows | Start-menuen → **Anaconda Navigator** → **Launch** under *JupyterLab* |
| Mac | Programmer → **Anaconda-Navigator** → **Launch** under *JupyterLab* |
| Linux | Skriv `jupyter lab` i terminalen |

JupyterLab åbner i din browser. Klik på **Python 3** under *Notebook* for at lave en ny notebook.

## 4. Test, at det virker

Kopiér ind i en celle og tryk **Shift + Enter**:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
plt.plot(x, np.sin(x))
plt.show()
```

Ser du en sinuskurve, er alt i orden. 🎉

---

> **Om licens:** Anaconda er gratis til undervisning på en uddannelsesinstitution efter Anacondas vilkår. Vil du være helt fri af licensspørgsmålet, kan du i stedet bruge [Miniforge](https://conda-forge.org/download/), som er en lille, helt fri udgave. Så skal du selv installere pakkerne med `conda install jupyterlab numpy scipy matplotlib sympy`.
