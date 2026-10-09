---
title: "Spektrofotometri"
weight: 1
---

**Niveau: Kemi B (2.g)** · **Emne: Farvede forbindelser og analysemetoder**

[Tilbage til Metoder]({{< relref "/docs/kemi/Metoder" >}})

## Video: hvad er spektrofotometri?

{{< yt id="Bi3N-gbYpCo" >}}

*Kilde: Biotech Academy — "Metoder: Spektrofotometri".*

## Kort forklaret

- Et spektrofotometer sender lys med én bestemt bølgelængde (monokromatisk lys) gennem en opløsning i en lille glas- eller plastbeholder, en **kuvette**.
- Molekylerne i opløsningen absorberer noget af lyset. Den farve, vi *ser*, er det lys, der **ikke** bliver absorberet.
- Jo mere stof der er opløst, jo mere lys bliver absorberet. Apparatet måler dette som **absorbans**, $A$ (ingen enhed).
- Absorbansen beregnes ud fra, hvor meget lys der sendes ind ($I_0$), og hvor meget der kommer igennem ($I$):

$$A = \log\left(\frac{I_0}{I}\right)$$

- Måler man på en kuvette med rent opløsningsmiddel (blindprøven, som apparatet nulstilles med), kommer alt lyset igennem, så $I = I_0$:

$$A = \log\left(\frac{I_0}{I_0}\right) = \log(1) = 0$$

- Slipper kun 10 % af lyset igennem, er absorbansen 1:

$$A = \log\left(\frac{100\ \%}{10\ \%}\right) = \log(10) = 1$$

  $A = 1$ er den **maksimalt tilladte absorbans** i vores forsøg. Ved højere absorbans kommer der så lidt lys igennem, at målingen bliver upræcis, og sammenhængen med koncentrationen er ikke længere lineær – så skal prøven fortyndes.

- Sammenhængen mellem absorbans og koncentration er givet ved **Lambert-Beers lov**:

$$A_\lambda = \varepsilon_\lambda \cdot l \cdot [\text{stof}]$$

  hvor $\varepsilon_\lambda$ er stoffets molare absorptionskoefficient ved bølgelængden $\lambda$, $l$ er kuvettens længde, dvs. den vej lyset går gennem opløsningen (typisk 1 cm), og $[\text{stof}]$ er stoffets **aktuelle** koncentration. Der bruges den aktuelle og ikke den formelle koncentration, fordi det kun er de partikler, der faktisk findes i opløsningen, som absorberer lyset.

- Ved en fast bølgelængde og en fast kuvette er $\varepsilon_\lambda \cdot l$ en konstant — så $A$ er **proportional** med $[\text{stof}]$. Det er derfor, metoden er så nyttig: mål absorbansen, og du kan regne koncentrationen ud.
- I praksis vælger man den bølgelængde, hvor stoffet absorberer *mest* ($\lambda_{max}$), fordi metoden så er mest følsom over for små ændringer i koncentration.

## Et meget simpelt eksempel

Forestil jer en kop vand, som I hælder mere og mere saftevand i:

- Jo mere saftevand, jo mørkere/mere farvet bliver vandet — og jo mindre lys kan I se igennem den, hvis I holder den op mod en lampe.
- Et spektrofotometer gør præcis det samme, bare med et tal i stedet for et øje: det måler, hvor meget lys der kommer igennem, og omregner det til absorbans.

Vi bruger samme idé med et konkret eksempel: **rødt farvestof i sodavand**. Rød sodavand og saftevand er farvet med et farvestof som E120 (karmin), E124 (Ponceau 4R) eller E129 (Allura Red AC) — tjek varedeklarationen på jeres flaske. Jo mere farvestof, jo højere absorbans.

## Opgave: byg en standardkurve i Excel
I har lavet det her før i NV hvor vi undersøgte C-vitaminindhold i appelsinjuice. 
I kan måske huske at vi havde 4 standardopløsninger i NV med $25mg/L$, $50mg/L$, $75mg/L$ og $100mg/L$

Til en standardkurve bruger man en række opløsninger med *kendt* koncentration, i det her forsøg er det det røde farvestof (en fortyndingsrække), og I har målt følgende absorbanser ved farvestoffets $\lambda_{max}$:

| Koncentration (mg/L) | Absorbans $A$ |
|---|---|
| 0 | 0,010 |
| 2 | 0,176 |
| 4 | 0,352 |
| 6 | 0,505 |
| 8 | 0,687 |
| 10 | 0,839 |

**Sådan gør I:**

1. Indtast tallene i Excel i to kolonner (koncentration og absorbans).
2. Indsæt et punktdiagram (scatter plot) med koncentration på x-aksen og absorbans på y-aksen.
3. Tilføj en lineær tendenslinje, og få Excel til at vise ligningen ($y = a\,x+b$) og $R^2$.
4. $R^2$ bør ligge tæt på 1 — det fortæller jer, hvor godt Lambert-Beers lov (en ret linje) passer på jeres data.

**Nu har I "rigtige" målinger** — tre ukendte prøver af rød sodavand, som I har fortyndet og målt absorbansen af:

| Prøve | Absorbans $A$ |
|---|---|
| A | 0,410 |
| B | 0,622 |
| C | 0,235 |

Brug tendenslinjens ligning til at regne koncentrationen $c$ ud for hver prøve (isolér $c$ i $y=ax+b$). Diskutér bagefter: hvis prøve A var 50 gange fortyndet, før I målte den — hvad var koncentrationen så i den *ufortyndede* sodavand?

## Eksperiment

Nu skal I selv prøve metoden: [Farvestof i rød sodavand]({{< relref "/docs/kemi/B-Eksp/farvestof-sodavand" >}}).

---

Flere opgaver: [Spektroskopi – tillægsopgaver]({{< relref "spektroskopiopgaver" >}})
