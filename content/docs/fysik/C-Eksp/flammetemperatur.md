---
title: "Flammetemperatur"
weight: 20
---
**Niveau:** Fysik C · **Emne:** Energi

---

## Introduktion

I dette forsøg bestemmer vi temperaturen af en flamme — uden at stikke et
termometer ind i den. I stedet varmer vi en metalbolt op i flammen og lader den
derefter afgive sin energi til en kendt mængde vand. Ved at måle, hvor meget
vandet varmes op, kan vi regne baglæns til boltens (og dermed flammens)
temperatur.

Vi antager, at boltens starttemperatur er den samme som flammens:

$$T_{\text{flamme}} \approx T_{\text{bolt-start}}$$

Idéen er **energibevarelse**: den energi, bolten afgiver, optages af vandet. Vi
regner boltens energi som negativ, fordi den *afgiver* energi:

$$\Delta E_{\text{vand}} = -\Delta E_{\text{bolt}} \qquad (1)$$

Venstre side er energien, vandet optager; højre side er energien, bolten afgiver.

Energien for de to størrelser regnes med varmekapacitetsformlen (se evt.
øvelsen om [varmekapacitet]({{< relref "varmekapacitet" >}})):

$$\Delta E_{\text{bolt}} = m_{\text{bolt}} \cdot c_{\text{jern}} \cdot \Delta T_{\text{bolt}} \qquad (2)$$

$$\Delta E_{\text{vand}} = m_{\text{vand}} \cdot c_{\text{vand}} \cdot \Delta T_{\text{vand}} \qquad (3)$$

hvor temperaturændringerne er

$$\Delta T_{\text{bolt}} = T_{\text{bolt-slut}} - T_{\text{bolt-start}} \qquad (a)$$

$$\Delta T_{\text{vand}} = T_{\text{vand-slut}} - T_{\text{vand-start}} \qquad (b)$$

$\Delta T_{\text{bolt}}$ bliver **negativ** (bolten køles ned), mens
$\Delta T_{\text{vand}}$ bliver **positiv** (vandet varmes op).

Alle størrelser har enheder:

- masserne $m$ i kilogram, $[\text{kg}]$
- varmekapaciteterne $c$ i $\left[\dfrac{\text{J}}{\text{kg} \cdot \text{K}}\right]$
- temperaturer og temperaturforskelle i $\text{K}$ eller $^\circ\text{C}$

![Forsøgsopstilling med alle størrelser](/images/flammetemperatur.png)

## Variabelkontrol

- **Uafhængig variabel:** boltens starttemperatur (flammetemperaturen) — den størrelse, vi i sidste ende vil bestemme.
- **Afhængig variabel:** vandets temperaturstigning $\Delta T_{\text{vand}}$.
- **Kontrollerede variabler:** vandets masse $m_{\text{vand}}$, boltens masse $m_{\text{bolt}}$, samme bolt (samme $c_{\text{jern}}$), og hurtig overførsel fra flamme til vand, så mindst muligt varme tabes undervejs.

## Materialer

- gasbrænder eller anden flamme
- metalbolt (jern) med kendt masse
- termobæger med vand
- energimåler / termometer
- vægt

---

## Gennemførelse

1. Vej bolten, og noter dens masse $m_{\text{bolt}}$.
2. Afmål en kendt mængde vand, og mål vandets starttemperatur $T_{\text{vand-start}}$.
3. Varm bolten op i flammen, til den har flammens temperatur.
4. Overfør hurtigt bolten til vandet, rør rundt, og aflæs den **fælles**
   sluttemperatur. Det er både $T_{\text{vand-slut}}$ og $T_{\text{bolt-slut}}$.
5. Sørg for at have målt **alle** størrelser, før I går videre til beregningen —
   den eneste ukendte skal være $T_{\text{bolt-start}}$ (= flammetemperaturen).

---

## Databehandling

Sæt formel **(2)** og **(3)** ind i **(1)**, erstat $\Delta T$ med udtrykkene
$(a)$ og $(b)$, og isolér $T_{\text{bolt-start}}$. Resultatet bliver:

$$T_{\text{bolt-start}} = \frac{m_{\text{vand}} \cdot c_{\text{vand}} \cdot \Delta T_{\text{vand}}}{m_{\text{bolt}} \cdot c_{\text{bolt}}} + T_{\text{bolt-slut}}$$

Indsæt jeres målte værdier, og beregn flammetemperaturen. **Husk, at alle værdier
skal være i SI-enheder.**

---

## Afrapportering

- Udledningen af formlen for $T_{\text{flamme}}$.
- En figur med alle de størrelser, der indgår i forsøget.
- Den udfyldte måletabel og den beregnede flammetemperatur.
