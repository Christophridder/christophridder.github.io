---
title: "Densitet"
weight: 5
---
**Niveau:** Fysik C · **Emne:** Grundlæggende fysik


## Introduktion

**Densiteten** $\rho$ (det græske bogstav *rho*) fortæller, hvor meget masse der
er pakket sammen i et bestemt rumfang. Den er givet ved:

$$\rho = \frac{m}{V}$$

hvor

- $\rho$ er densiteten i $\left[\dfrac{\text{kg}}{\text{m}^3}\right]$ (eller
  $\left[\dfrac{\text{g}}{\text{mL}}\right]$ i laboratoriet)
- $m$ er massen i kilogram, $[\text{kg}]$ (eller gram)
- $V$ er rumfanget i $[\text{m}^3]$ (eller mL)

## Omregning fra kg/m³ til g/mL

Vand har densiteten $1000\ \dfrac{\text{kg}}{\text{m}^3}$, hvilket er det samme som
$1\ \dfrac{\text{g}}{\text{mL}}$. Omregningen bygger på, at $1\text{ kg} = 1000\text{ g}$
og $1\text{ m}^3 = 10^6\text{ mL}$:

$$1000\ \frac{\text{kg}}{\text{m}^3} = \frac{1000 \cdot 1000\ \text{g}}{10^6\ \text{mL}} = \frac{10^6\ \text{g}}{10^6\ \text{mL}} = 1\ \frac{\text{g}}{\text{mL}}$$

I dette forsøg bestemmer vi densiteten af tre væsker — **vand**, **ethanol** og
**olie** — på en simpel måde: vi hælder væsken op i et måleglas, der står på en
vægt, og aflæser massen for forskellige rumfang.

Skriver vi formlen om, ses det, at masse og rumfang hænger lineært sammen:

$$m = \rho \cdot V$$

Plotter vi massen $m$ op ad $y$-aksen og rumfanget $V$ ud ad $x$-aksen, bliver
**hældningen lige præcis densiteten** $\rho$.

> **Lille tvist i dette forsøg:** I skal **ikke** nulstille (tarere) vægten,
> før I begynder! Måleglasset selv vejer jo noget, og det betyder, at jeres graf
> ikke går gennem $(0,0)$ — den skærer $y$-aksen et stykke oppe. Den skæring er
> selve **b-værdien** i en ret linje $y = a \cdot x + b$, og her svarer den til
> **måleglassets masse**. Det er en god anledning til at forstå, hvad et $b$-led
> egentlig betyder fysisk.

En ret linje har formen:

$$m = \rho \cdot V + m_{\text{glas}}$$

hvor hældningen $a = \rho$ er det, vi er ude efter, og skæringen
$b = m_{\text{glas}}$ er måleglassets masse.

---

## Variabelkontrol

- **Uafhængig variabel:** rumfanget $V$, vi hælder op.
- **Afhængig variabel:** den samlede masse $m$, vægten viser.
- **Kontrollerede variabler:** samme måleglas, samme vægt, samme væske gennem én
  måleserie, og vægten må **ikke** nulstilles undervejs.

---

## Materialer

- vægt (gerne med to decimaler)
- måleglas
- vand, ethanol og olie

---

## Gennemførelse

1. Stil det **tomme** måleglas på vægten, men **nulstil ikke** vægten. Aflæs
   massen ved rumfang $V = 0$ — det er måleglassets egen masse.
2. Hæld væske op til en kendt mængde (fx $20\text{ mL}$), og aflæs massen.
3. Hæld mere i til næste kendte rumfang (fx $40\text{ mL}$, $60\text{ mL}$ …), og
   aflæs massen hver gang.
4. Lav mindst 5–6 punkter for hver væske.
5. Gentag for alle tre væsker — husk at tømme og tørre måleglasset mellem
   væskerne.

### Måletabel (én pr. væske)

| Rumfang $V$ / mL | Masse $m$ / g |
|------|------|
| 0 | (måleglassets masse) |
| 20 | |
| 40 | |
| 60 | |
| 80 | |
| 100 | |

---

## Databehandling i Excel

1. Lav to kolonner: rumfang $V$ og masse $m$.
2. Markér data, og indsæt et diagram af typen **Punkt (XY)** — *ikke* søjle eller
   linje, ellers skaleres $x$-aksen forkert.
3. Læg en **lineær tendenslinje** ind, og få vist ligningen ($y = a \cdot x + b$)
   og $R^2$.
4. Aflæs:
   - **hældningen** $a$ → det er densiteten $\rho$ for væsken
   - **skæringen** $b$ → det er måleglassets masse $m_{\text{glas}}$

Lav alle tre væsker i samme diagram, så I kan sammenligne hældningerne direkte.

---

## Afrapportering

- En udfyldt måletabel for hver af de tre væsker.
- Grafen med alle tre væsker og deres tendenslinjer.
- De tre bestemte densiteter (hældninger), sammenlignet med tabelværdier
  (vand $\approx 1{,}00\text{ g/mL}$, ethanol $\approx 0{,}79\text{ g/mL}$, olie
  $\approx 0{,}92\text{ g/mL}$).
- En forklaring af, hvad **b-værdien** betyder i jeres graf, og hvorfor den er
  cirka den samme for alle tre væsker (fordi det er det samme måleglas).
