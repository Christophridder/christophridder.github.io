---
title: "Farvestof i rød sodavand"
weight: 60
pdf: "pdfs/farvestof-sodavand.pdf"
pdf_ny_fane: true
---

**Niveau: Kemi B (2.g)** · **Emne: Farvede forbindelser og spektrofotometri**

# Der er lus i din sodavand!

Teorien bag – absorbans, Beer-Lamberts lov og standardkurver – står på siden [Spektrofotometri]({{< relref "/docs/kemi/Metoder/spektrofotometri" >}}). Læs den først.

Mange røde sodavand er farvet med **E120**, der også hedder *karmin* eller *cochenille*. Farvestoffet laves af små skjoldlus, der lever på kaktusser i Mexico og Sydamerika. Det farvede molekyle er **karminsyre**. Spørgsmålet er: **Hvor mange mg lus / farvestof – er der i en liter sodavand?**

I bestemmer koncentrationen af E120 i en rød sodavand med en standardkurve, præcis som i Excel-opgaven på [Spektrofotometri]({{< relref "/docs/kemi/Metoder/spektrofotometri" >}}). Forskellen er, at nu laver I selv standardopløsningerne og måler selv.

## Det skal I bruge

- Spektrofotometer, kuvetter og computer med LoggerPro
- Rød sodavand med E120 (tjek varedeklarationen). Den skal være **uden CO₂** – lad den stå åben, eller ryst den godt eller varm det op så alt $\ce{CO_2}$ fordamper
- Stamopløsning af E120: **250 mg/L**
- 0,01 M HCl
- 25 mL målekolber med prop
- 1 mL mikropipette med spidser, bægerglas og indikatorpapir

## Opgave 1 – Stamopløsningen i mol/L

Det farvede stof i E120 er karminsyre, $\ce{C22H20O13}$.

a) Beregn den molare masse $M$ af karminsyre. Brug $M(\ce{C}) = 12{,}01$ g/mol, $M(\ce{H}) = 1{,}008$ g/mol og $M(\ce{O}) = 16{,}00$ g/mol.

b) Stamopløsningen indeholder $250$ mg/L. Omregn til mol/L og µmol/L.

## Fortyndingsrækken

Karminsyre skifter farve med pH: den er orange-rød i sur opløsning og bliver mere violet, jo mindre sur opløsningen er. Derfor skal standarderne og sodavanden have **omtrent samme pH**. Sodavand er sur (pH ca. 2,5–3,5), så I fortynder med **0,01 M HCl** i stedet for vand.

1. Mål pH i sodavanden med indikatorpapir, og skriv den ned.
2. Afpipettér stamopløsning over i en 25,00 mL målekolbe. Mikropipetten tager 1 mL ad gangen, så gentag, til I har det volumen, der står i tabellen.
3. Fyld op til stregen med 0,01 M HCl, sæt prop i, og vend kolben et par gange.
4. Beregn koncentrationen med $c_1 \cdot V_1 = c_2 \cdot V_2$, og tjek pH i én af standarderne med indikatorpapir.

| Standard | Stamopløsning $V_1$ (mL) | Samlet volumen $V_2$ (mL) | $c_2$ (mg/L) | Absorbans $A$ |
|---|---|---|---|---|
| 0 (blind) | 0 | 25,00 | 0 | 0 |
| 1 | 1,00 | 25,00 | | |
| 2 | 2,00 | 25,00 | | |
| 3 | 3,00 | 25,00 | | |
| 4 | 4,00 | 25,00 | | |
| 5 | 5,00 | 25,00 | | |

## Måling

1. Nulstil spektrofotometeret med en kuvette med **0,01 M HCl** (blindprøve).
2. Scan hele det synlige spektrum (380–750 nm) for standard 5 **og** for sodavanden. Ligner de to spektre hinanden? Aflæs $\lambda_{max}$, og brug den bølgelængde til resten af målingerne.
3. Mål absorbansen af standard 1–5 ved $\lambda_{max}$. Start med den mest fortyndede.
4. Mål absorbansen af sodavanden. **Hold absorbansen under 1.** Er den over 1, så fortynd sodavanden med 0,01 M HCl (fx 10,00 mL sodavand fyldt op til 25,00 mL), og husk at gange med fortyndingsfaktoren bagefter.
5. Lav standardkurven i Excel: $c$ (mg/L) på x-aksen, $A$ på y-aksen, lineær tendenslinje, ligning og $R^2$.

## Opgave 2 – Hvor meget farve er der i?

a) Bestem koncentrationen af E120 i sodavanden i mg/L ud fra standardkurven. Husk fortyndingsfaktoren.

b) Omregn hældningen på standardkurven fra L/mg til L/mol, og bestem den molare absorptionskoefficient $\varepsilon$ for karminsyre ved jeres $\lambda_{max}$ i L/(mol·cm). Kuvetten er $b = 1{,}00$ cm.

c) Find den højst tilladte mængde E120 i sodavand i EU's forordning om fødevaretilsætningsstoffer (nr. 1333/2008, bilag II, kategori 14.1.4 "Aromatiserede drikkevarer"). Overholder jeres sodavand grænsen?

> **Model:** Beer-Lamberts lov gælder kun for fortyndede opløsninger (typisk $A$ under ca. 1), og kun hvis det farvede stof er det samme i alle prøver. Hvis pH er forskellig i standarder og sodavand, har karminsyren forskellig farve – så passer standardkurven ikke til sodavanden. Og hvis sodavanden indeholder flere farvestoffer, måler I dem alle på én gang.

## Det skal jeres rapport indeholde

- **Forsøgsbeskrivelse** med billeder af jeres opstilling og jeres fortyndingsrække.
- **Spektre** af standard og sodavand, der viser, at sodavanden faktisk indeholder E120.
- **Farve og spektrum:** Forklar, hvorfor væsken ser rød ud, når I ser på absorptionsspektret. Forklar også, hvad i karminsyrens opbygning der gør den farvet (tip: konjugerede dobbeltbindinger).
- **En flot standardkurve** – med akser, enheder, tendenslinje, ligning og $R^2$.
- **$\varepsilon$** for karminsyre ved jeres bølgelængde.
- **Resultatet:** indholdet af E120 i sodavanden i mg/L, en vurdering af, om det virker rimeligt, og om grænseværdien er overholdt.
- **Fejlkilder:** Hvad kunne gøre resultatet for højt eller for lavt?


## Sikkerhed

- 0,01 M HCl er meget fortyndet, men brug alligevel briller.
- E120 og sodavand er fødevarer, men **drik ikke noget i laboratoriet**.
- Alle opløsninger kan hældes i vasken med rigeligt vand.


## Praktiske noter til læreren

- **Stamopløsning:** 250 mg/L E120 (karminsyre) i vand. Standarderne 10–50 mg/L fortyndes med 0,01 M HCl.
- **Forventet:** $M = 492{,}4$ g/mol, så stamopløsningen er ca. 508 µmol/L. Standarderne er 10 – 20 – 30 – 40 – 50 mg/L.
- **$\lambda_{max}$** ligger omkring 490–500 nm i sur opløsning, men flytter sig mod højere bølgelængde, når pH stiger. Lad eleverne selv finde den.
- **$\varepsilon$:** Med den ofte brugte værdi $E^{1\%}_{1\,\text{cm}} \approx 139$ ved 494 nm i stærk syre bliver $\varepsilon \approx 7 \cdot 10^3$ L/(mol·cm), så 50 mg/L giver $A \approx 0{,}7$. Værdien afhænger af pH – tjek den selv.
- **Grænseværdi:** E120 hører til gruppe III (farvestoffer med fælles maksimumsgrænse). For aromatiserede drikkevarer er grænsen efter min viden 100 mg/L for gruppen samlet – tjek den gældende forordning.
- **E120 er ikke vegansk,** og nogle få mennesker er allergiske over for det – en god snak om, hvorfor man vælger et naturligt farvestof frem for et syntetisk.
- **Vernier:** SpectroVis Plus (LoggerPro) har en indbygget "Concentration"-funktion. Lad eleverne regne manuelt i Excel først og bruge LoggerPro til at tjekke.

