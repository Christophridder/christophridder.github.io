---
title: "Præcision og nøjagtighed"
weight: 8
---

**Niveau: NV, Fysik og Kemi C–A** · **Emne: Databehandling**

# Præcision og nøjagtighed

I daglig tale bruger man tit "præcis" og "nøjagtig" om det samme. I naturvidenskab betyder de to forskellige ting:

- **Præcision** beskriver, hvor tæt dine målinger ligger **på hinanden**. Gentager du målingen, får du så næsten det samme hver gang?
- **Nøjagtighed** beskriver, hvor tæt dine målinger (deres gennemsnit) ligger **på den sande værdi**.

Du kan godt have den ene uden den anden. Figuren viser de fire muligheder. Forestil dig, at hvert punkt er én måling, og at den sande værdi er krydset i midten, hvor de røde linjer mødes.

![Fire skiver: præcis og nøjagtig, præcis men ikke nøjagtig, nøjagtig men ikke præcis, hverken præcis eller nøjagtig](/img/nat/praecision-noejagtighed.svg)

| | **Nøjagtig** (gennemsnit tæt på sand værdi) | **Ikke nøjagtig** (gennemsnit forskudt) |
|---|---|---|
| **Præcis** (lille spredning) | Det, du går efter | Systematisk fejl – alle målinger skævvredet samme vej |
| **Ikke præcis** (stor spredning) | Store tilfældige fejl, men de udligner hinanden i gennemsnittet | Både systematiske og store tilfældige fejl |

## Sammenhængen med fejltyperne

Præcision og nøjagtighed hænger direkte sammen med fejltyperne fra [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}):

- **Tilfældige fejl ødelægger præcisionen.** De spreder målingerne ud, lige meget til begge sider. Du kan mindske deres betydning ved at lave **flere målinger** og tage gennemsnittet.
- **Systematiske fejl ødelægger nøjagtigheden.** De flytter alle målinger samme vej. Flere målinger hjælper **ikke** – gennemsnittet bliver bare forkert med stor sikkerhed. Du skal finde og fjerne selve fejlkilden.

Det er derfor, en meget præcis måleserie kan være farlig: den lille spredning får resultatet til at *se* troværdigt ud, selv om det er forkert.

## Sådan sætter du tal på

| Begreb | Mål | Formel |
|---|---|---|
| Nøjagtighed | Procentvis afvigelse af gennemsnittet | $\dfrac{\bar{x} - x_{\text{teo}}}{x_{\text{teo}}} \cdot 100\,\%$ |
| Præcision | Standardafvigelse (spredning) | $s = \sqrt{\dfrac{\sum (x_i - \bar{x})^2}{n-1}}$ |

Her er $\bar{x}$ gennemsnittet af dine $n$ målinger $x_i$. I regneark finder du $\bar{x}$ med `MIDDEL()` og $s$ med `STDAFV.S()`. Den procentvise afvigelse er gennemgået på siden [Procentvis afvigelse]({{< relref "/docs/nat/procentvis-afvigelse" >}}).

## Eksempel 1: Fire grupper måler $g$ med et pendul

Fire grupper bestemmer tyngdeaccelerationen ud fra pendulformlen $g = \dfrac{4\pi^2 \cdot L}{T^2}$. Hver gruppe laver 5 målinger. Den sande værdi er $g = 9{,}82\ \tfrac{\text{m}}{\text{s}^2}$.

| Gruppe | Målinger af $g$ / $\tfrac{\text{m}}{\text{s}^2}$ | $\bar{g}$ / $\tfrac{\text{m}}{\text{s}^2}$ | $s$ / $\tfrac{\text{m}}{\text{s}^2}$ | Afvigelse | Vurdering |
|---|---|---|---|---|---|
| A | 9,80 · 9,83 · 9,81 · 9,84 · 9,79 | 9,81 | 0,02 | −0,06 % | Præcis og nøjagtig |
| B | 9,52 · 9,55 · 9,53 · 9,56 · 9,51 | 9,53 | 0,02 | −2,9 % | Præcis, ikke nøjagtig |
| C | 9,45 · 10,21 · 9,68 · 10,05 · 9,66 | 9,81 | 0,31 | −0,10 % | Nøjagtig, ikke præcis |
| D | 9,12 · 9,71 · 9,38 · 9,95 · 9,24 | 9,48 | 0,34 | −3,5 % | Hverken eller |

**Hvad er der sket?**

- **Gruppe A** har målt tiden for 10 svingninger ad gangen og målt snorlængden helt ned til loddets midte.
- **Gruppe B** har målt $L$ fra ophænget til **toppen** af loddet i stedet for til loddets midte (tyngdepunkt). $L$ bliver for lille hver gang, og dermed bliver $g$ for lille hver gang: en **systematisk fejl**. Spredningen er lige så lille som hos A, så gruppen kan ikke selv se fejlen ud fra spredningen – kun ved at sammenligne med tabelværdien.
- **Gruppe C** har taget tid på **én** svingning med stopur. Reaktionstiden giver store **tilfældige fejl**, men de går begge veje og udligner sig i gennemsnittet. Resultatet er nøjagtigt, men en enkelt måling for sig er ikke til at stole på.
- **Gruppe D** har begge fejl på én gang.

> **Bemærk:** Gruppe C kan forbedre sig ved at måle flere gange (eller tage tid på 10 svingninger). Gruppe B kan måle 100 gange uden at komme tættere på 9,82 – den skal ændre selve måden at måle $L$ på.

## Eksempel 2: Hverdagssituationer

| Situation | Præcis? | Nøjagtig? | Hvorfor |
|---|---|---|---|
| Vægt, der ikke er nulstillet (tareret), viser altid 2,0 g for meget | Ja | Nej | Systematisk fejl – samme forskydning hver gang |
| Burette aflæst fra skiftende vinkler (parallaksefejl) | Nej | Ja, i gennemsnit | Aflæsningen svinger tilfældigt op og ned |
| Burette aflæst nedefra hver gang | Ja | Nej | Samme vinkel → samme skævhed hver gang |
| Termometer, der er kalibreret og aflæst omhyggeligt | Ja | Ja | Hverken systematiske eller store tilfældige fejl |
| Digitalt multimeter med mange decimaler, men forkert kalibreret | Ja | Nej | Mange cifre giver **præcision**, ikke nøjagtighed |

Det sidste punkt er værd at huske: **mange decimaler på et display betyder ikke, at tallet er rigtigt.**

## Eksempel 3: Dartskiven

Fire spillere kaster hver 5 pile efter midten:

1. Alle fem pile sidder samlet i bullseye → **præcis og nøjagtig**.
2. Alle fem pile sidder samlet, men oppe i venstre hjørne → **præcis, ikke nøjagtig**. Spilleren sigter skævt på samme måde hver gang – ret sigtet, så rammer hun.
3. Pilene er spredt ud over hele skiven, men "i midten i gennemsnit" → **nøjagtig, ikke præcis**. Spilleren skal træne et mere stabilt kast.
4. Pilene er spredt, og alle i den nederste halvdel → **hverken eller**.

## Prøv selv i Python

Koden laver en skive som dem i figuren. Prøv at ændre centrum og spredning, så du får hver af de fire situationer.

<details>
<summary><strong>Vis Python-kode</strong></summary>

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)   # fast seed: samme punkter hver gang

def sky(cx, cy, spredning, n=20):
    """n målinger omkring (cx, cy) med en given spredning."""
    x = cx + rng.uniform(-spredning, spredning, n)
    y = cy + rng.uniform(-spredning, spredning, n)
    return x, y

grupper = {
    "Præcis og nøjagtig":       sky(5, 5, 0.4),
    "Præcis, ikke nøjagtig":    sky(8, 8, 0.4),
    "Nøjagtig, ikke præcis":    sky(5, 5, 2.0),
    "Hverken eller":            sky(8, 2, 1.5),
}

plt.figure(figsize=(7, 7))
for navn, (x, y) in grupper.items():
    plt.scatter(x, y, label=navn)

plt.axhline(5, color="r", lw=2)   # sand værdi
plt.axvline(5, color="r", lw=2)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 11, 1))
plt.xlabel("x-værdier")
plt.ylabel("y-værdier")
plt.title("Præcision vs. nøjagtighed")
plt.gca().set_aspect("equal")
plt.grid()
plt.legend()
plt.show()
```

</details>

## Læs videre

- [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}) – grove fejl, systematiske fejl og tilfældige fejl
- [Procentvis afvigelse]({{< relref "/docs/nat/procentvis-afvigelse" >}}) – sådan måler du nøjagtighed
- [Betydende cifre]({{< relref "/docs/nat/betydendecifre" >}})

---

*Siderne er lavet af Christoph Ridder med hjælp af flere fysik-A-B-C-hold på Egaa Gymnasium 2020 2025. Feedback gerne til cr@egaa-gym.dk*
