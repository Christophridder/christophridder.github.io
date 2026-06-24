---
title: "Bestemmelse af halveringstid"
weight: 70
---
**Niveau:** Fysik C · **Emne:** Radioaktivitet


## Introduktion

Et radioaktivt stof henfalder med tiden: antallet af endnu ikke henfaldne kerner
bliver mindre og mindre, og dermed falder aktiviteten (henfald pr. sekund) også.
Formålet med denne øvelse er at vise, at aktiviteten aftager **eksponentielt** med
tiden, og at bestemme stoffets **halveringstid** $T_{1/2}$.

### Teori

Aktiviteten $A$ (her det korrigerede tælletal) aftager eksponentielt med tiden
$t$:

$$A = A_0 \cdot e^{-k \cdot t}$$

hvor

- $A$ er aktiviteten til tiden $t$ (korrigeret tælletal)
- $A_0$ er aktiviteten ved start ($t = 0$)
- $t$ er tiden i sekunder eller minutter
- $k$ er **henfaldskonstanten** i $[\text{s}^{-1}]$ (eller $[\text{min}^{-1}]$)

**Halveringstiden** $T_{1/2}$ er den tid, der skal til for at halvere aktiviteten.
Sætter vi $A = \tfrac{1}{2} A_0$ ind og isolerer, fås sammenhængen mellem
$T_{1/2}$ og $k$:

$$\tfrac{1}{2} A_0 = A_0 \cdot e^{-k \cdot T_{1/2}}$$

$$\tfrac{1}{2} = e^{-k \cdot T_{1/2}}$$

Tag den naturlige logaritme på begge sider:

$$\ln\left(\tfrac{1}{2}\right) = -k \cdot T_{1/2} \quad\Rightarrow\quad -\ln(2) = -k \cdot T_{1/2}$$

$$\boxed{\; T_{1/2} = \frac{\ln(2)}{k} \;}$$

Det er præcis samme matematik som ved halveringstykkelse — bare med tid $t$ i
stedet for tykkelse $x$ og henfaldskonstant $k$ i stedet for dæmpningskonstant
$\mu$.

---

## Variabelkontrol

- **Uafhængig variabel:** tiden $t$.
- **Afhængig variabel:** det korrigerede tælletal pr. måleinterval.
- **Kontrollerede variabler:** afstand mellem kilde og GM-rør, længden af hvert
  måleinterval, samme kilde og samme GM-rør.

> Vi bruger en kortlivet kilde (fx en med en halveringstid på minutter), så hele
> henfaldet kan følges i løbet af en lektion.

---

## Materialer

- kortlivet radioaktiv kilde
- GM-rør med tæller
- stopur / timer

---

## Gennemførelse

1. Bestem baggrundsstrålingen $B$ for det måleinterval, du vil bruge.
2. Mål tælletallet i faste, lige lange tidsintervaller (fx hvert $\,30\text{ s}$
   eller hvert minut) over så lang tid som muligt.
3. Beregn det korrigerede tælletal ved at trække $B$ fra hvert måltal.

### Måletabel

| Tid $t$ | Tælletal | B | Korrigeret tælletal |
|------|------|------|------|
| | | | |
| | | | |
| | | | |

---

## Databehandling i Excel

Som ved halveringstykkelse laver du **to grafer**:

**1) Lineær graf** — korrigeret tælletal ($y$) mod tid ($x$). Viser den
eksponentielt aftagende kurve.

**2) Enkeltlogaritmisk graf** — samme data med logaritmisk $y$-akse, hvor
punkterne kommer til at ligge på en ret linje.

Sådan gør du i Excel:

1. Skriv to kolonner: tid $t$ og korrigeret tælletal.
2. Markér data, og indsæt et diagram af typen **Punkt (XY)** — *ikke* søjle eller
   linje, ellers skaleres $x$-aksen forkert.
3. Det er den lineære graf. Kopiér diagrammet.
4. På kopien: dobbeltklik på $y$-aksen → sæt hak i **logaritmisk skala**. Nu er
   det det enkeltlogaritmiske plot.
5. Læg evt. en eksponentiel tendenslinje ind, så du kan aflæse henfaldskonstanten
   $k$ fra eksponenten.

**Find** $T_{1/2}$ **grafisk:** Aflæs på den lineære graf den tid, hvor
tælletallet er faldet til **halvdelen** af startværdien $A_0$. Det er
halveringstiden. Tjek gerne, at du får samme værdi ved at gå fra $A_0/2$ til
$A_0/4$ — det skal tage lige så lang tid igen.

---

## Afrapportering

- Udfyldt måletabel.
- De to grafer (lineær og enkeltlogaritmisk) vedhæftet som bilag.
- Den grafisk bestemte halveringstid $T_{1/2}$, gerne sammenlignet med
  tabelværdien for stoffet.
- Beregn henfaldskonstanten $k = \dfrac{\ln(2)}{T_{1/2}}$.
