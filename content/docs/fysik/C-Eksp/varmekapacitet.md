---
title: "Varmekapacitet"
weight: 10
---
**Niveau:** Fysik C · **Emne:** Energi

---

## Introduktion

Temperatur er bevægelse på molekylært plan: jo varmere et stof er, jo mere bevæger
dets molekyler sig. I en krystal kan atomerne kun svinge frem og tilbage om deres
faste plads, mens atomerne i et molekyle også kan bevæge sig indbyrdes og dermed
optage endnu mere energi.

**Varmekapaciteten** $c$ er den størrelse, der beskriver, hvor meget energi ét
kilogram af et stof skal tilføres for at blive varmet $1\text{ K}$ (én grad) op.
Den termiske energi, der skal til, er givet ved:

$$E = m \cdot c \cdot \Delta T$$

hvor

- $E$ er den tilførte energi i joule, $[\text{J}]$
- $m$ er stoffets masse i kilogram, $[\text{kg}]$
- $c$ er varmekapaciteten i $\left[\dfrac{\text{J}}{\text{kg} \cdot \text{K}}\right]$
- $\Delta T$ er temperaturforskellen, $\Delta T = T_{\text{slut}} - T_{\text{start}}$

> En temperaturforskel er den samme målt i $^\circ\text{C}$ og i $\text{K}$, så
> $\Delta T$ kan regnes i begge enheder. Det er kun selve temperaturen, der skal
> over i kelvin, hvis en formel kræver det.

### Hældningskoefficient som fysisk størrelse

Når man plotter en lineær sammenhæng, har både hældningen $a$ og skæringen med
$y$-aksen $b$ ofte en fysisk betydning. Det udnytter vi i forsøget: hvis vi vælger
akserne rigtigt, kommer hældningen til at være **lige præcis** varmekapaciteten
$c$.

Skriver vi energiformlen om, ses det:

$$E = (m \cdot c) \cdot \Delta T$$

Plotter vi den tilførte energi $E$ op ad $y$-aksen og temperaturforskellen
$\Delta T$ ud ad $x$-aksen, bliver hældningen $m \cdot c$. Kender vi massen $m$,
kan vi finde $c$.

## Variabelkontrol

- **Uafhængig variabel:** den tilførte energi $E$ (i trin af ca. $5000\text{ J}$).
- **Afhængig variabel:** vandets temperatur (og dermed temperaturforskellen $\Delta T$).
- **Kontrollerede variabler:** vandets masse $m$ (samme ca. $200\text{ g}$ hele vejen), samme termobæger, samme dypkoger, og at der røres rundt før hver aflæsning.

## Materialer

- energimåler, som stilles på $\text{Ws}$
- termobæger
- ca. $200\text{ g}$ vand
- termometer
- dypkoger på ca. $300\text{ W}$

---

## Gennemførelse

1. Afmål meget nøjagtigt ca. $200\text{ g}$ vand og hæld det i termobægeret.
2. Tilslut energimåleren med de to strømstik og stil den på $\text{Ws}$.

> **PAS PÅ — FARLIGT!** Du må under ingen omstændigheder tænde for dypkogeren
> uden for vandet — den går i stykker. Put altid dypkogeren i vandet først.

3. Sæt dypkogeren ned i vandet og mål **starttemperaturen**.
4. Optag en måleserie med klar rollefordeling:
   - **Person 1** styrer dypkogeren og rører rundt.
   - **Person 2** styrer dypkogerens strømstik.
   - **Person 3** skriver tal ned.
5. Nulstil energimåleren. Person 2 sætter stikket i, og Person 1 rører rundt.
   Når der er tilført ca. $5000\text{ J}$, trækker Person 2 stikket ud, der røres
   rundt, og temperaturen aflæses.
6. Gentag mindst **15 gange**, eller indtil temperaturen er ca. $70\,^\circ\text{C}$.
   Pas på, I ikke brænder jer.

---

## Databehandling

- Plot jeres ca. 15 punkter i et regneark.
- Design regnearket, så **hældningskoefficienten bliver lige præcis
  varmekapaciteten** $c$ (lidt svært, men muligt — tænk på, hvad der skal stå på
  hver akse).
- Slå vandets varmekapacitet op (se tabellen nedenfor), og sammenlign med jeres
  resultat.
- Beregn den procentvise afvigelse, hvis I kan.

### Varmekapaciteter

| Stof | | $c$ i $\left[\dfrac{\text{J}}{\text{kg} \cdot \text{K}}\right]$ |
|------|------|------|
| Vand | (l) | 4182 |
| Kobber | (s) | 385 |
| Jern | (s) | 449 |
| Bly | (s) | 128 |
| Luft | (g) | 1010 |
| Zink | (s) | 387 |
| Aluminium | (s) | 897 |
| N₂ | (g) | 1040 |
| O₂ | (g) | 918 |
| Ethanol | (l) | 2440 |
| Olie | (l) | 1670 |

---

## Afrapportering

- Den udfyldte måletabel.
- Grafen med energi mod temperaturforskel og en forklaring af, hvorfor hældningen
  giver varmekapaciteten.
- Jeres bestemte værdi for $c$, sammenligning med tabelværdien og den procentvise
  afvigelse.
