---
title: "Bestemmelse af halveringstykkelse"
weight: 60
---
**Niveau:** Fysik C · **Emne:** Radioaktivitet

---

## Introduktion

Når $\gamma$-stråling sendes gennem et materiale, bliver den dæmpet: jo tykkere
materiale, jo færre fotoner slipper igennem. Formålet med denne øvelse er at vise,
at $\gamma$-strålingens intensitet aftager **eksponentielt** med tykkelsen af det
absorberende stof, og at bestemme **halveringstykkelsen** $x_{1/2}$ for bly.

### Teori

Intensiteten $I$ (her det korrigerede tælletal) aftager eksponentielt med
materialets tykkelse $x$:

$$I = I_0 \cdot e^{-\mu \cdot x}$$

hvor

- $I$ er intensiteten efter materialet (korrigeret tælletal)
- $I_0$ er intensiteten uden absorbator
- $x$ er materialets tykkelse i $\text{mm}$
- $\mu$ er **dæmpningskonstanten** (halveringstykkelseskonstanten) i $[\text{mm}^{-1}]$

**Halveringstykkelsen** $x_{1/2}$ er den tykkelse, der skal til for at halvere
intensiteten. Sætter vi $I = \tfrac{1}{2} I_0$ ind og isolerer, fås sammenhængen
mellem $x_{1/2}$ og $\mu$:

$$\tfrac{1}{2} I_0 = I_0 \cdot e^{-\mu \cdot x_{1/2}}$$

$$\tfrac{1}{2} = e^{-\mu \cdot x_{1/2}}$$

Tag den naturlige logaritme på begge sider:

$$\ln\left(\tfrac{1}{2}\right) = -\mu \cdot x_{1/2} \quad\Rightarrow\quad -\ln(2) = -\mu \cdot x_{1/2}$$

$$\boxed{ x_{1/2} = \frac{\ln(2)}{\mu} }$$

Det er præcis samme matematik som ved radioaktivt henfald — bare med tykkelse $x$
i stedet for tid $t$ og dæmpningskonstant $\mu$ i stedet for henfaldskonstant $k$.

---

## Variabelkontrol

- **Uafhængig variabel:** den samlede blytykkelse $x$ i $\text{mm}$.
- **Afhængig variabel:** det korrigerede tælletal i $60\text{ s}$.
- **Kontrollerede variabler:** afstand mellem kilde og GM-rør, måletiden
  ($60\text{ s}$), samme kilde og samme GM-rør.

---

## Materialer

- $\gamma$-kilde
- GM-rør med tæller
- 10 blyplader
- mikrometerskrue (millimeterskrue)
- stopur / timer

---

## Gennemførelse

1. Mål tykkelsen af hver blyplade med mikrometerskruen, og noter den.
2. Bestem baggrundsstrålingen $B$ for $60\text{ s}$. Bruger du samme tid, sted og
   GM-rør som i [gennemtrængeligheds-øvelsen]({{< relref "gennemtraengelighed" >}}),
   kan du genbruge resultatet derfra.
3. Læg pladerne på én efter én, og mål tælletallet i $60\text{ s}$ for hver ny
   plade.
4. Beregn det korrigerede tælletal ved at trække $B$ fra.

### Tabel 2

| Pb-plader | Pb-tykkelse (mm) | Tælletal i 60 s | B i 60 s | Korrigeret tælletal |
|------|------|------|------|------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

> **Pas på:** På $x$-aksen skal stå den **samlede tykkelse** — altså de målte
> skivetykkelser lagt sammen — **ikke** antallet af skiver.

## Problemet med den første blyplade

Når gammastrålingen rammer blyet, slipper den ikke bare igennem — nogle af
fotonerne **vekselvirker** med blyet og river elektroner løs (bl.a. ved
fotoelektrisk effekt og Compton-spredning). Disse løsrevne elektroner kan nå frem
til GM-røret og give ekstra tællinger oven i selve gammastrålingen.

**Derfor** skal I **ikke** bruge det første punkt på jeres graf: efter kun én
blyplade når mange af disse elektroner frem til røret og giver en fejlmåling. Når
I har to eller flere plader på, bliver elektronerne absorberet inde i blyet, før
de når røret, og forstyrrer ikke længere.

## Databehandling i Excel

Du skal lave **to grafer** ud fra de samme data:

**1) Lineær graf** — korrigeret tælletal ($y$) mod samlet blytykkelse ($x$).
Den viser den eksponentielt aftagende kurve.

**2) Enkeltlogaritmisk graf** — samme data, men med logaritmisk $y$-akse. Her
bliver eksponentialfunktionen til en **ret linje**, og det er den, vi bruger til
at finde $x_{1/2}$.

Sådan gør du i Excel:

1. Skriv to kolonner: samlet tykkelse $x$ (mm) og korrigeret tælletal.
2. Markér data, og indsæt et diagram af typen **Punkt (XY)** — *ikke* et
   søjle- eller linjediagram, ellers bliver $x$-aksen ikke korrekt skaleret.
3. Det er den lineære graf. Kopiér diagrammet.
4. På kopien: dobbeltklik på $y$-aksen → sæt hak i **logaritmisk skala**. Nu har
   du det enkeltlogaritmiske plot, hvor punkterne ligger på en ret linje.
5. Læg evt. en tendenslinje (eksponentiel) ind for at se sammenhængen tydeligt.

**Find** $x_{1/2}$ **grafisk:** Aflæs på den lineære graf den tykkelse, hvor
tælletallet er faldet til **halvdelen** af startværdien $I_0$. Det er
halveringstykkelsen.

---

## Afrapportering

- Udfyldt tabel 2.
- De to grafer (lineær og enkeltlogaritmisk) vedhæftet som bilag.
- Den grafisk bestemte halveringstykkelse $x_{1/2}$ i $\text{mm}$.

> **Sammenlign med databogen:** Halveringstykkelsen afhænger ikke kun af
> materialet, men også af $\gamma$-fotonens energi. Antag, at skolekildens
> $\gamma$-stråling har en energi på ca. $0{,}555\text{ MeV}$. Find databogens
> værdi for halveringstykkelsen i bly ved denne energi, og sammenlign med din
> egen.
