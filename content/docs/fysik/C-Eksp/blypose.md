---
title: "Blypose"
weight: 8
---
**Niveau:** Fysik C · **Emne:** Energiformler og energikæder

---

## Introduktion

Når du løfter en blypose op i en højde $h$, giver du den **potentiel energi**. Når
du slipper den, omdannes den potentielle energi til **bevægelsesenergi** — og når
posen rammer din hånd (eller jorden), forsvinder bevægelsen igen. Men energi kan
ikke bare forsvinde, så hvor bliver den af?

I dette forsøg kaster I en blypose mange gange og undersøger, hvor stor en del af
energien der ender som **varme** i posen.

### Energikæden

$$E_{\text{pot}} \rightarrow E_{\text{bevægelse}} \rightarrow E_{\text{termisk (varme)}}$$

Den potentielle energi for ét løft er:

$$E_{\text{pot}} = m \cdot g \cdot h$$

hvor

- $m$ er blyposens masse i kilogram, $[\text{kg}]$
- $g$ er tyngdeaccelerationen, $g = 9{,}82\ \dfrac{\text{m}}{\text{s}^2}$
- $h$ er løftehøjden i meter, $[\text{m}]$

Kaster I posen $100$ gange, bliver den samlede tilførte energi:

$$E_{\text{pot,total}} = 100 \cdot m \cdot g \cdot h$$

Den varme, posen optager, beregnes med varmekapacitetsformlen:

$$E_{\text{term}} = m \cdot c_{\text{bly}} \cdot \Delta T$$

hvor $c_{\text{bly}} = 128\ \dfrac{\text{J}}{\text{kg} \cdot \text{K}}$ og
$\Delta T$ er posens temperaturstigning.

---

## Variabelkontrol

- **Uafhængig variabel:** antallet af kast (vi vælger 100).
- **Afhængig variabel:** blyposens temperaturstigning $\Delta T$.
- **Kontrollerede variabler:** løftehøjden $h$ (skal helst være ens hver gang),
  samme blypose, og at posen ikke når at køle af undervejs.

---

## Materialer

- en blypose med kendt masse
- et termometer (gerne et, der kan stikkes ind i posen)
- et målebånd til at fastlægge højden $h$

---

## Gennemførelse

Arbejd sammen tre og tre med klare roller:

1. Mål blyposens **starttemperatur**.
2. Mål løftehøjden $h$ — fx afstanden mellem to personer, der er **lige høje** og
   kaster posen frem og tilbage mellem sig. Højden skal være den samme hver gang.
3. Løft posen til højden $h$ og lade den falde ned **100 gange**:
   - **Person 1 og 2** skiftes til at kaste posen 20 gange per person .. i finder selv ud af det bare det går hurtigt og uden pause, vi vil ikke miste for meget energi til omgivelserne undervejs. 
   - **Person 3** tæller kastene.
4. Lige efter det 100. kast: mål blyposens **sluttemperatur**, og find
   $\Delta T = T_{\text{slut}} - T_{\text{start}}$.

---

## Databehandling

1. Beregn den samlede tilførte energi:
   $$E_{\text{pot,total}} = 100 \cdot m \cdot g \cdot h$$
2. Beregn den varme, posen har optaget:
   $$E_{\text{term}} = m \cdot c_{\text{bly}} \cdot \Delta T$$
3. Find, **hvor stor en del** af energien der endte som varme i posen:
   $$\eta = \frac{E_{\text{term}}}{E_{\text{pot,total}}}$$

---

## Fra brøkdel til procent — om at gange med 100 %

Resultatet $\eta$ er et **tal mellem 0 og 1**. Fx kunne I få $\eta = 0{,}42$. Det
betyder, at $42\%$ af den potentielle energi fra kastene er blevet til varme.

Men hvordan kommer man fra $0{,}42$ til $42\%$? Man "ganger med 100" — men det er
værd at forstå, hvad der **egentlig** sker:

Et **procent** = *per cent* = per hundrede

1 % er derfor lige med $1\cdot \frac{1}{100}$ altså:


Når I ganger med $100$%, ganger I altså i virkeligheden med $100 \cdot \frac{1}{100}$ som er 1. Og man må altid gerne gange ting med 1 :-) 

Tallet bliver derfor det samme, men nu skrevet i en ny "enhed" (procent i stedet for ren
brøkdel):

$0{,}42 = 0{,}42 \cdot 1 = 0{,}42 \cdot 100$% $= 42$%

> **Pointen:** Man "ganger ikke med 100" — man ganger med $100$% = $1$. Værdien er
> den samme; det er bare en anden måde at skrive det samme tal på. Det er præcis
> den slags omregning, I skal bruge igen i øvelsen om
> [nyttevirkning]({{< relref "nyttevirkning" >}}).

---

## Hvad bliver der af resten af energien?

I finder sikkert, at langtfra al energien endte som varme **i posen**. Hvor blev
resten af? Diskutér i gruppen — fx:

- Varme i jeres **hænder** og i luften omkring posen.
- **Lyd**, hver gang posen rammer gulvet.
- prøv mærk efter på gulvet der hvor posen ramte er det blevet varmere der?

Energien er altså ikke forsvundet — den er bare fordelt ud på flere steder, end I
kan måle. Det er en vigtig pointe: **energi bevares altid**, men den ender ofte som
spredt varme, vi ikke får gavn af. Varmetabet sker faktisk stort set altid når energi omdannes. 
Biler som skal køre, men hvor motoren bliver varm. Elpærer der skal lyse men som også producerer varme. Kraftværker som skal lave strøm men hvor turbinen og generatoren taber energi i form af varme **alle disse processer** har et $\eta$ altså en virkningsgrad. 
- Man kan sige at *bilen bruger 30% af energien fra brændstoffet til at bevæge sig* resten er spilt $\eta_{bil} = 0,3$. 
- Ved Studstrupværket *30% af energien til produktion af strøm* $\eta_{el} = 0,3$% 60% af energien går til fjernvarme, dvs at værket har en samlet $\eta_{Studstrupkrafvaerket} = 0,3 + 0,6 = 0,9$ 90% energiudnyttelse. 
---

## Fejlkilder

- **Højden er ikke ens for hvert kast.** Hvis personerne ikke er helt lige høje,
  eller kaster forskelligt, varierer $h$ — og dermed er $E_{\text{pot,total}}$
  kun et skøn. Overvej, om jeres $h$ er for høj eller for lav i gennemsnit, og i
  hvilken retning det trækker resultatet.

---

## Afrapportering

- Jeres målte masse, højde, start- og sluttemperatur.
- Beregningerne af $E_{\text{pot,total}}$, $E_{\text{term}}$ og $\eta$.
- $\eta$ omskrevet til procent (med forklaring af "gange med $100\% = 1$").
- En diskussion af, hvor resten af energien blev af, og af højde-fejlkilden.

## Bonusopgave som er lidt svær
Prøv at beregne med hvilken fart blyposen rammer jorden fra jeres højde. Her til skal du bruge formlen for kinetisk energi. Det er nemlig sådan at lige inden posen rammer jorden er alt den potentielle energi omdannet til kinetisk energi og formelen for den indeholder blyposens fart. 
$$E_{pot} = m \cdot g \cdot h$$
$$E_{kin} = \frac{1}{2}\cdot m \cdot v^2$$

Kik på et enkelt kast. Højden er $h$ og massen af posen er $m_{pose}$ sæt nu $E_{pot} = E_{kin}$ for et enkelt kast og isolér $v$ lidt tricky det er noget med en kvadratrod. Tyngdeaccelerationen $g$  står øverst i vejledningen. 
Gallileo gallilei lod forskellige ting falde ned fra Pisa tårnet, hvad var det han opdagede? kan du se det samme på formlen? 

HINT: hvad sker det lige med massen?
