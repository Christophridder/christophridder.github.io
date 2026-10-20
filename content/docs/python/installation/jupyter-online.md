---
title: "Jupyter online"
weight: 1
---

# Jupyter online – uden installation

Vil du bare hurtigt prøve noget kode eller se resultatet af en fil, kan du køre Jupyter direkte i browseren.

## JupyterLite (anbefalet)

👉 **[Åbn JupyterLite](https://jupyter.org/try-jupyter/lab/)**

- Kræver **ingen konto** og intet login.
- Python kører **i din egen browser** – din kode sendes ikke til en server.
- `numpy`, `matplotlib`, `scipy` og `sympy` virker direkte med `import`.

### Sådan gør du

1. Åbn linket og vent, til siden er indlæst.
2. Klik på **Python (Pyodide)** under *Notebook* for at lave en ny notebook.
3. Skriv kode i cellen og tryk **Shift + Enter** for at køre den.

### Åbn en fil, du har fået

- **`.ipynb`-fil:** Træk filen ind i fillisten til venstre (eller brug upload-knappen ⬆), og dobbeltklik på den.
- **`.py`-fil:** Upload filen, åbn den, og kopiér indholdet ind i en celle i en ny notebook. Kør cellen.

> ⚠️ **Gem dit arbejde!** Filerne ligger kun i din browsers lager. Rydder du browserdata eller skifter computer, er de væk. Højreklik på filen → **Download**, når du er færdig.

### Mangler en pakke?

Skriv i en celle:

```python
%pip install pakkenavn
```

## Google Colab (alternativ)

[Google Colab](https://colab.research.google.com/) kører også Jupyter online og gemmer filerne i Google Drive. Det kræver en **Google-konto**, og koden kører på Googles servere.

## Videre

Skal du bruge Python meget, er det rarere at have det på din egen computer: se [Anaconda]({{< relref "/docs/python/installation/anaconda" >}}) eller [VSCodium]({{< relref "/docs/python/installation/vscodium" >}}).
