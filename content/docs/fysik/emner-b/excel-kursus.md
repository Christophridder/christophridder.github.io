---
title: "Excel-kursus"
weight: -2
---

**Niveau: Fysik B** · **Emne: Databehandling i Excel**

I fysik bruger du regneark hele tiden. Her lærer du det vigtigste i to trin: først en graf ud fra dine målinger i densitetsforsøget og derefter et regneark til en skolefest.

## Det skal du kunne

| Hvad | Sådan gør du | Eksempel |
|---|---|---|
| Skrive en formel | Start altid med `=` | `=A2*2` |
| Bruge en celle | Skriv cellens adresse i stedet for tallet | `=B2*C2` |
| Trække en formel ned | Træk i den lille firkant nederst til højre i cellen | Formlen følger med ned |
| Lægge sammen | Brug `SUM` | `=SUM(B2:B29)` |
| Låse en celle | Sæt `$` foran kolonne og række | `$H$1` |

## Del 1: Graf over dine densitetsmålinger

Brug dine målinger fra [Densitet]({{< relref "/docs/fysik/C-Eksp/densitet" >}}).

1. Skriv rumfang i kolonne A og masse i kolonne B. Skriv overskrifter med enhed i første række, fx `V / mL` og `m / g`.
2. Markér de to kolonner, og indsæt et **Punkt (XY)**-diagram.
3. Tilføj akseoverskrifter med enhed.
4. Tilføj en **lineær tendenslinje**, og vis ligningen og $R^2$ i diagrammet.
5. Find densiteten: Hældningen i ligningen er $\rho$ i g/mL.

## Del 2: Regneark til en skolefest

28 elever holder fest i et fælleshus. Fem elever har lagt ud for indkøbene, og nogle af dem har købt ind syd for grænsen i euro. Festen skal gå i nul, så alle betaler lige meget. Regnearket skal vise, hvad hver elev skal betale, eller hvad hver elev skal have tilbage.

| Indkøber | Euro (syd for grænsen) | Kroner | Købt |
|---|---|---|---|
| Anton Bech | 142,80 € | 215,00 kr | øl, is til kølekasser |
| Freja Winther | 96,40 € | 2000,00 kr | sodavand, husleje til fælleshuset |
| Jonas Kristoffersen | 118,65 € | 180,50 kr | chips og slik, engangsservice |
| Maja Rask | 74,25 € | 342,75 kr | pølser og brød, salat |
| Nour Haddad | 53,90 € | 420,00 kr | saft og vand, pizza til vegetarerne |

### Byg regnearket

Regnearket skal se sådan ud:

| Kolonne | Indhold |
|---|---|
| A | Navn |
| B | Indkøb i euro |
| C | Indkøb i kroner |
| D | Samlet indkøb i kroner |
| E | Får tilbage (+) / skal betale (−) |

1. Skriv overskrifterne i række 1.
2. Skriv 28 navne i `A2:A29`: de fem indkøbere og 23 andre. Du må gerne bruge klassens navne.
3. Skriv indkøbene i kolonne B og C. De andre elever får `0`.
4. Skriv teksten `Eurokurs` i `G1` og kursen `7,46` i `H1`.
5. Skriv en formel i `D2`, der regner euro om til kroner og lægger kronerne til:

   `=B2*$H$1+C2`

6. Træk formlen ned til `D29`.
7. Skriv `I alt` i `A30`, og læg kolonne D sammen i `D30` med `=SUM(D2:D29)`.
8. Find prisen pr. elev: Skriv `=D30/28` i `H5`, og skriv `Pris pr. elev` i `G5`.
9. Skriv i `E2`, hvad den første elev får tilbage:

   `=D2-$H$5`

10. Træk formlen ned til `E29`, og læg kolonne E sammen i `E30`.

**Tjek:** Hvis festen går i nul, skal `E30` være $0$.

### Hvad gør `$`?

Når du trækker en formel ned, flytter Excel alle cellereferencer med. Det er smart for `B2` og `C2`, som skal blive til `B3` og `C3`. Men eurokursen står kun ét sted, så den reference må ikke flytte sig.

| Formel i D2 | I D3 bliver den til | Resultat |
|---|---|---|
| `=B2*H1+C2` | `=B3*H2+C3` | Forkert: `H2` er tom, så euroerne forsvinder |
| `=B2*$H$1+C2` | `=B3*$H$1+C3` | Rigtigt: Kursen bliver stående i `H1` |

Når markøren står i referencen, kan du trykke **F4** på en pc eller **⌘T** på en Mac. Så sætter Excel selv `$`-tegnene ind.

### Prøv selv

1. Fjern `$`-tegnene i `D2`, og træk formlen ned. Hvad sker der i kolonne D og i `E30`?
2. Sæt dem på igen. Ændr kursen i `H1` til `7,50`. Hvilke celler ændrer sig?
3. Fem elever bliver syge. Hvad skal du ændre, for at festen stadig går i nul?
