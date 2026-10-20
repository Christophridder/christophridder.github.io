---
title: "Python i VSCodium"
weight: 3
---

# Python og Jupyter i VSCodium

[VSCodium](https://vscodium.com/) er en gratis, open source-udgave af Visual Studio Code uden Microsofts sporing. Du kan skrive både almindelige `.py`-filer og Jupyter-notebooks (`.ipynb`) i den.

Der er to veje: Følg trinene herunder, eller få en AI til at guide dig skridt for skridt (se nederst).

## 1. Installér Python

| Styresystem | Sådan |
|---|---|
| Windows | Hent fra [python.org/downloads](https://www.python.org/downloads/). **Sæt flueben i *Add python.exe to PATH*** i første skærmbillede! |
| Mac | Hent fra [python.org/downloads](https://www.python.org/downloads/) og kør `.pkg`-filen. |
| Linux | Python er der allerede. Installér venv: `sudo apt install python3-venv` |

## 2. Installér VSCodium

| Styresystem | Sådan |
|---|---|
| Windows | Hent *User Installer* fra [vscodium.com](https://vscodium.com/#install) |
| Mac | Hent `.dmg` fra [vscodium.com](https://vscodium.com/#install) og træk VSCodium over i Programmer |
| Linux | Følg vejledningen på [vscodium.com](https://vscodium.com/#install) (apt, Flatpak eller Snap) |

> **Mac siger "VSCodium er beskadiget"?** Åbn Terminal og kør `xattr -cr /Applications/VSCodium.app`, og prøv igen.

## 3. Installér udvidelser

Klik på ikonet med de fire firkanter i venstre side (**Extensions**) og installér:

- **Python** (fra ms-python)
- **Jupyter** (fra ms-toolsai)

## 4. Lav en projektmappe med de rigtige pakker

1. Lav en mappe, fx `fysik-python`, og åbn den i VSCodium: **File → Open Folder**.
2. Åbn en terminal i VSCodium: **Terminal → New Terminal**.
3. Kør disse linjer én ad gangen:

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install numpy scipy matplotlib sympy ipykernel
```

**Mac og Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib sympy ipykernel
```

## 5. Test

1. Lav en ny fil `test.ipynb` (**File → New File**).
2. Klik på **Select Kernel** øverst til højre og vælg **.venv**.
3. Skriv i en celle og tryk **Shift + Enter**:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
plt.plot(x, np.sin(x))
plt.show()
```

Ser du en sinuskurve, virker det hele. 🎉

---

## Få en AI til at guide dig

Kopiér teksten herunder ind i Claude, ChatGPT eller en anden AI-chat. Så tager den dig igennem installationen ét trin ad gangen og hjælper, hvis noget går galt.

```text
Du er en tålmodig IT-hjælper for en gymnasieelev, der skal bruge Python i fysik og kemi.
Guid mig gennem installationen af Python og VSCodium, så jeg kan køre både .py-filer
og Jupyter-notebooks (.ipynb).

Regler:
- Spørg mig først, hvilket styresystem jeg har (Windows, Mac med Apple Silicon,
  Mac med Intel eller Linux), og om Python allerede er installeret.
- Giv mig ÉT trin ad gangen og vent på, at jeg skriver "ok" eller sender en
  fejlbesked, før du går videre.
- Forklar kort og på dansk, hvad hvert trin gør. Brug ikke fagudtryk uden at forklare dem.
- Når jeg skal skrive i terminalen, så skriv kommandoen i en kodeblok og forklar,
  hvordan jeg åbner terminalen.
- Hvis jeg sender en fejlbesked, så forklar, hvad den betyder, og hvordan jeg løser den.

Målet er:
1. Python 3 installeret (fra python.org på Windows/Mac; på Windows med "Add python.exe to PATH").
2. VSCodium installeret fra vscodium.com.
3. Udvidelserne "Python" (ms-python) og "Jupyter" (ms-toolsai) installeret i VSCodium.
4. En projektmappe med et virtuelt miljø (.venv), hvor pakkerne
   numpy, scipy, matplotlib, sympy og ipykernel er installeret med pip.
5. En test-notebook, hvor jeg vælger .venv som kernel og plotter en sinuskurve
   med numpy og matplotlib.

Afslut med at opsummere, hvordan jeg næste gang åbner mappen og starter en ny notebook.
```
