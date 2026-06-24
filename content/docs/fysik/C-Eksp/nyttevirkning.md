---
title: "Nyttevirkning"
weight: 40
---
**Niveau:** Fysik C · **Emne:** Energi

---

## Introduktion

Apparater til opvarmning af vand — elkedel, gryde på kogeplade, mikrobølgeovn osv.
— er ikke lige gode til at udnytte den energi, de optager fra elnettet. I denne
undersøgelse skal I finde ud af, **hvilke apparater der er bedst** til at udnytte
energien (har høj nyttevirkning), og **hvorfor** nyttevirkningen er så forskellig.

### Teori

Når man opvarmer vand med et apparat, tilføres apparatet noget energi — den
**tilførte energi** $E_{\text{tilført}}$. Vandet optager kun en del af den, nemlig
den **nyttige energi** $E_{\text{nytte}}$.

**Nyttevirkningen** $\eta$ (det græske bogstav *eta*) er den brøkdel af energien,
der ender i vandet:

$$\eta = \frac{E_{\text{nytte}}}{E_{\text{tilført}}}$$

$\eta$ er et tal mellem 0 og 1 (eller en procent) og har ingen enhed.

**Den tilførte energi** måles direkte med en energimåler, der sættes mellem
stikkontakten og apparatet. Den måler simpelthen, hvor meget energi der omsættes
i apparatet.

**Den nyttige energi** er den, vandet faktisk optager. For at varme et stof op
skal man tilføre energi, som øger molekylernes bevægelse og dermed temperaturen
$T$. Hvor meget energi der skal til for at hæve temperaturen $1\text{ K}$, styres
af stoffets **specifikke varmekapacitet** $c$. Den nyttige energi beregnes derfor
med varmekapacitetsformlen (se evt. øvelsen om
[varmekapacitet]({{< relref "varmekapacitet" >}})):

$$E_{\text{nytte}} = m \cdot c \cdot \Delta T$$

hvor

- $m$ er vandets masse i kilogram, $[\text{kg}]$
- $c$ er vandets specifikke varmekapacitet, $c = 4182 \left[\dfrac{\text{J}}{\text{kg} \cdot \text{K}}\right]$
- $\Delta T = T_{\text{slut}} - T_{\text{start}}$ er temperaturstigningen

> $C$ (stort) er den samlede varmekapacitet, mens $c$ (lille) er den **specifikke**
> varmekapacitet — altså $C$ divideret med massen. Vi bruger her kun det lille $c$.

## Variabelkontrol

- **Uafhængig variabel:** apparatet, der bruges til opvarmningen (elkedel, mikrobølgeovn, gryde, dypkoger, gasblus …).
- **Afhængig variabel:** nyttevirkningen $\eta$.
- **Kontrollerede variabler:** vandets masse (ca. $0{,}5\text{ kg}$ hver gang), samme starttemperatur, samme energimåler, og samme måde at måle slut­temperaturen på.

## Materialer

- forskellige opvarmningsapparater: elkedel, mikrobølgeovn, kaffemaskine, gryde
  med og uden låg, bunsenbrænder …
- energimåler
- termometer
- vægt
- ca. $0{,}5\text{ kg}$ vand pr. forsøg

---

## Forskrivning

- Find en opstilling (fx en elkedel), og find ud af, hvilke størrelser I skal måle
  for at bestemme $\eta$.
- Diskutér **afhængig**, **uafhængig** og **kontrollerede** variabler.
- Design hver især et regneark, hvor I for hvert apparat kan taste de målte
  værdier ind og få beregnet nyttevirkningen $\eta$ i sidste kolonne.
- **Gæt** til sidst en forventet værdi for $\eta$ for hvert apparat, og skriv den
  i en ny kolonne lige efter jeres beregnede $\eta$.

---

## Gennemførelse

1. Afvej en passende mængde vand — gerne ca. $0{,}5\text{ kg}$ (afhænger lidt af
   apparatet).
2. Mål vandets starttemperatur, tilslut energimåleren, og start opvarmningen.

> Vandet behøver **ikke** at koge — bare I får en rimelig $\Delta T$.

3. Tag et billede af opstillingen, mens I venter.
4. Når vandet er ved at koge, stop forsøget, og mål sluttemperaturen.
5. Tast jeres data ind i regnearket.
6. Diskutér til sidst værdierne for $\eta$: Hvor store burde de være? Hvordan
   passer de med det, I forventede på forhånd?

> **Bunsenbrænder:** Her kan I **ikke** måle $E_{\text{tilført}}$ på den
> sædvanlige måde med energimåler. I stedet skal I bruge gassens **brændværdi**
> (energi pr. kg eller pr. liter brændstof) til at finde den tilførte energi.

---

## Databehandling

Eksempel på en resultattabel:

| Apparat | $m_{\text{vand}}$ / $\text{kg}$ | $T_{\text{start}}$ / $\text{°C}$ | $T_{\text{slut}}$ / °$\text{C}$ | $E_{\text{tilført}}$ / $\text{J}$ | $E_{\text{nytte}}$ / $\text{J}$ | $\eta$ |
|---------|------|------|------|------|------|------|
| Eksempel | 0,8 | 20 | 80 | 336000 | 200640 | 0,597 |
| Elkedel | | | | | | |
| Mikrobølge | | | | | | |
| Gryde | | | | | | |
| Dypkoger | | | | | | |
| Gasblus | | | | | | |

Lav **én** fuldstændig eksempelberegning med enheder for et udvalgt apparat (fx
mikrobølgeovn). De øvrige beregninger fremgår blot af regnearket. Lavede I forsøg
med gasblus, skal den beregning også med, fordi den er anderledes end de andre.

---

## Afrapportering

Journalen skal indeholde:

- **Overskrift** med navnet på øvelsen.
- **Indledning:** hvad I vil måle og hvorfor.
- **Hypotese:** hvilket apparat tror I er bedst, og hvilket er dårligst?
- **Teori:** formlerne for termisk energi og nyttevirkning.
- **Metode:** hvad I vil gøre (veje vand, finde den nyttige energi, sammenligne
  med den tilførte og beregne $\eta$).
- **Udstyr:** dypkoger, elkedel, termometer …
- **Risici:** pas på det kogende vand.
- **Fremgangsmåde og observationer:** kort punktopstilling + billede af
  opstillingen + den udfyldte tabel.
- **Efterbehandling:** én fuld beregning med enheder; resten fra regnearket.
- **Fejlkilder:** vurder for hver fejlkilde, i hvilken **retning** den påvirker
  resultatet:
  - målefejl på temperaturer og masser
  - fordampning af vandet, når det koger
  - lille temperaturforskel mellem $T_{\text{start}}$ og $T_{\text{slut}}$
    (fx i mikrobølgeovn)
- **Konklusion:** gennemgå alle resultater, sammenlign apparaterne indbyrdes, og
  diskutér, hvorfor det fx er smart at bruge dypkoger til ét og gasblus til noget
  andet. Hvor langt er I fra jeres gættede værdier?

---

## Opgaver til afleveringen

**Opgave 1** *(regnes i afleveringen)*

I mange køkkener sidder der 5–10 halogenpærer, der lyser ned på bordpladen. Antag,
at du har **8 pærer på hver $30\text{ W}$**, som lyser $6{,}5$ timer hver dag.

- Beregn pærernes energiforbrug, først i joule og så i $\text{kWh}$.
- En $\text{kWh}$ koster ca. $3{,}5\text{ kr}$ i Århus. Beregn omkostningerne.

**Opgave 2** *(regnes derhjemme)*

Kig bag på mindst **4** husholdningsapparater (fjernsyn, køleskab, emhætte,
støvsuger …). Tag et billede af etiketten, og find maksimaleffekten i watt. Vurdér
sammen med din familie, hvor meget apparatet bruges om dagen/året. Antag, at en
$\text{kWh}$ koster ca. $6\text{ kr}$, og beregn, hvad netop dette apparat koster
familien om året. Stil det op i en tabel, og diskutér resultaterne.
