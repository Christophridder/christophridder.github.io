---
title: "Formelsamling – Kemi"
weight: -10
bookToc: true
---

<style>
.formelsamling table { font-size: 0.92em; }
.formelsamling table tr th, .formelsamling table tr td { padding: 0.4rem 0.6rem; }
.formelsamling img { max-width: 100%; }
.formelsamling .strukturformel { height: 80px; max-width: none; }
</style>
<div class="formelsamling">

# Formelsamling – Kemi

**Niveau: Kemi C–B** · Opbygning: først det, der gælder **alle niveauer**, derefter
**C-niveau** og **B-niveau**. På B-niveau skal du også kunne alt fra C.

> **Formler er modeller.** Mange af pH-formlerne gælder kun under bestemte
> forudsætninger (fx "svag syre", "ikke for fortyndet", "25 °C"). Forudsætningerne står
> i bemærkningskolonnen – de er en del af formlen.

---

## Fælles for alle niveauer

### Præfikser

Samme præfikser som i fysik – se [Formelsamling – Fysik]({{< relref "/docs/fysik/formelsamling" >}}).
I kemi bruges især **milli** (mL, mmol, mM = mmol/L), **mikro** (µg, µmol) og **nano** (nm for bølgelængder).

### Konstanter

| Navn | Symbol | Værdi | Bemærkning |
|---|---|---|---|
| Avogadros tal | $N_A$ | $6{,}022 \cdot 10^{23}\ \text{mol}^{-1}$ | eksakt: $6{,}02214076 \cdot 10^{23}$ |
| Gaskonstanten | $R$ | $8{,}314\ \text{J/(mol·K)} = 0{,}08314\ \text{L·bar/(mol·K)}$ | |
| Molvolumen af idealgas | $V_m$ | $22{,}41\ \text{L/mol}$ ved 0 °C og 1 atm | |
| | | $24{,}47\ \text{L/mol}$ ved 25 °C og 1 atm | |
| | | $24{,}79\ \text{L/mol}$ ved 25 °C og 1 bar | tjek altid, hvilke betingelser opgaven bruger |
| Vands ionprodukt | $K_w$ | $1{,}0 \cdot 10^{-14}\ \text{M}^2$ ved 25 °C | temperaturafhængig: ca. $1{,}1 \cdot 10^{-15}$ ved 0 °C og $5{,}5 \cdot 10^{-14}$ ved 50 °C |
| Faradays konstant | $F$ | $96\,485\ \text{C/mol}$ | ladning af 1 mol elektroner |
| Atomar masseenhed | u | $1{,}661 \cdot 10^{-27}\ \text{kg}$ | 1 u pr. atom ↔ 1 g/mol |
| Absolut nulpunkt | | $0\ \text{K} = -273{,}15\ \text{°C}$ | $T/\text{K} = t/\text{°C} + 273{,}15$ |
| Vands specifikke varmekapacitet | $c_{\text{vand}}$ | $4{,}18\ \text{J/(g·K)}$ | |
| Vands densitet (20 °C) | $\rho_{\text{vand}}$ | $0{,}998\ \text{g/mL} \approx 1{,}00\ \text{g/mL}$ | |

### Størrelser og enheder

| Størrelse | Symbol | Typisk enhed | I SI-enheder |
|---|---|---|---|
| Masse | $m$ | g | $1\ \text{g} = 10^{-3}\ \text{kg}$ |
| Molar masse | $M$ | g/mol | $1\ \text{g/mol} = 10^{-3}\ \text{kg/mol}$ |
| Stofmængde | $n$ | mol | mol (SI-grundenhed) |
| Antal partikler | $N$ | – | $N = n \cdot N_A$ |
| Rumfang | $V$ | L, mL | $1\ \text{L} = 10^{-3}\ \text{m}^3$, $\ 1\ \text{mL} = 1\ \text{cm}^3$ |
| Formel (stof)koncentration | $c(\text{X})$ | M = mol/L | $1\ \text{M} = 1000\ \text{mol/m}^3$ |
| Aktuel koncentration | $[\text{X}]$ | M = mol/L | koncentrationen af det, der *faktisk* findes i opløsningen |
| Densitet | $\rho$ | g/mL | $1\ \text{g/mL} = 1000\ \text{kg/m}^3$ |
| Tryk | $p$ | bar, atm, Pa | $1\ \text{bar} = 10^5\ \text{Pa}$, $\ 1\ \text{atm} = 1{,}01325\ \text{bar}$ |
| Temperatur | $T$ | K (og °C) | K |
| Energi / entalpi | $E$, $\Delta H$ | kJ, kJ/mol | $1\ \text{kJ} = 10^3\ \text{J}$ |
| Masseprocent | $w$ | % | $w = \dfrac{m_{\text{stof}}}{m_{\text{total}}} \cdot 100\ \%$ |
| Milliontedele | ppm | mg/kg | $1\ \text{ppm} = 10^{-6}$; i fortyndet vandig opløsning ≈ 1 mg/L |

---

## C-niveau

### Mængdeberegninger

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Stofmængde | $n = \dfrac{m}{M}$ | |
| Molar masse | $M$ = summen af atommasserne | $M(\ce{H2O}) = 2 \cdot 1{,}008 + 16{,}00 = 18{,}02\ \text{g/mol}$ |
| Antal partikler | $N = n \cdot N_A$ | |
| Koncentration | $c = \dfrac{n}{V}$ | $V$ i **liter** |
| Fortynding | $c_1 \cdot V_1 = c_2 \cdot V_2$ | stofmængden er den samme før og efter |
| Reaktionsskema | $\dfrac{n_A}{a} = \dfrac{n_B}{b}$ | for $a\,\text{A} + b\,\text{B} \rightarrow \ldots$: koefficienterne er **stofmængdeforhold** |
| Begrænsende reaktant | den reaktant med mindst $n/\text{koefficient}$ | den bestemmer, hvor meget produkt der kan dannes |
| Udbytte | $\text{udbytte} = \dfrac{m_{\text{faktisk}}}{m_{\text{teoretisk}}} \cdot 100\ \%$ | |
| Idealgas | $p \cdot V = n \cdot R \cdot T$ | eller $n = \dfrac{V}{V_m}$ |
| Masseprocent | $w = \dfrac{m_{\text{stof}}}{m_{\text{total}}} \cdot 100\ \%$ | |

**Formel og aktuel koncentration:** Opløses 0,10 mol $\ce{CaCl2}$ i 1,0 L vand, er
$c(\ce{CaCl2}) = 0{,}10\ \text{M}$, men $[\ce{Ca^2+}] = 0{,}10\ \text{M}$ og $[\ce{Cl-}] = 0{,}20\ \text{M}$ – og $[\ce{CaCl2}] = 0$.

Eksempel: 5,85 g NaCl ($M = 58{,}44\ \text{g/mol}$) opløses til 250 mL:
$n = \dfrac{5{,}85\ \text{g}}{58{,}44\ \text{g/mol}} = 0{,}100\ \text{mol}$ og $c = \dfrac{0{,}100\ \text{mol}}{0{,}250\ \text{L}} = 0{,}400\ \text{M}$.

### Titrering

Ved **ækvivalenspunktet** er der tilsat præcis så meget titrator, som reaktionsskemaet kræver.
For en monoprot syre og en monohydroxid base ($\ce{H3O+ + OH- -> 2H2O}$):

$$n_{\text{syre}} = n_{\text{base}} \quad\Longrightarrow\quad c_s \cdot V_s = c_b \cdot V_b$$

Eksempel: 10,00 mL HCl kræver 12,50 mL 0,100 M NaOH: $c_s = \dfrac{0{,}100 \cdot 12{,}50}{10{,}00}\ \text{M} = 0{,}125\ \text{M}$.

> Er forholdet ikke 1 : 1 (fx $\ce{H2SO4}$ eller $\ce{H3PO4}$), skal du bruge koefficienterne i reaktionsskemaet.

### Syrer, baser og pH

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Syre / base (Brønsted) | syre = protondonor, base = protonacceptor | $\ce{HA + H2O <=> A- + H3O+}$ |
| pH | $\text{pH} = -\log[\ce{H3O+}]$ | $[\ce{H3O+}] = 10^{-\text{pH}}$ |
| pOH | $\text{pOH} = -\log[\ce{OH-}]$ | $[\ce{OH-}] = 10^{-\text{pOH}}$ |
| Vands autoprotolyse | $[\ce{H3O+}] \cdot [\ce{OH-}] = K_w$ | |
| Sammenhæng | $\text{pH} + \text{pOH} = 14{,}00$ | **kun ved 25 °C** |
| Stærk syre | $\text{pH} = -\log c_s$ | fuldstændigt protolyseret |
| Stærk base | $\text{pOH} = -\log c_b$, $\ \text{pH} = 14{,}00 - \text{pOH}$ | |
| Neutral opløsning | $[\ce{H3O+}] = [\ce{OH-}]$ | pH = 7,00 ved 25 °C |

Eksempler: 0,010 M HCl har pH = 2,00. 0,050 M NaOH har pOH = 1,30 og pH = 12,70.

> **Gyldighed:** $\text{pH} = -\log c_s$ passer dårligt for meget fortyndede opløsninger
> ($c_s \lesssim 10^{-6}\ \text{M}$, hvor vands egen protolyse betyder noget) og for
> koncentrerede opløsninger ($c_s \gtrsim 1\ \text{M}$). pH kan godt være under 0 eller over 14.

**Stærke syrer:** HCl, HBr, HI, $\ce{HNO3}$, $\ce{HClO4}$, $\ce{H2SO4}$ (1. trin).
**Stærke baser:** NaOH, KOH (og opløst $\ce{Ca(OH)2}$).

![pH-skalaen](/images/formelsamling/ph_skala.svg)

### Ioner og salte

Se også [ionnavne]({{< relref "/docs/kemi/C-Ioner/ionnavne" >}}) og [opløselighedstabellen]({{< relref "/docs/kemi/C-Ioner/opløselighedstabel" >}}).

| Ion | Navn | Ion | Navn |
|---|---|---|---|
| $\ce{NH4+}$ | ammonium | $\ce{OH-}$ | hydroxid |
| $\ce{H3O+}$ | oxonium | $\ce{NO3-}$ | nitrat |
| $\ce{CO3^2-}$ | carbonat | $\ce{HCO3-}$ | hydrogencarbonat |
| $\ce{SO4^2-}$ | sulfat | $\ce{HSO4-}$ | hydrogensulfat |
| $\ce{PO4^3-}$ | phosphat | $\ce{CH3COO-}$ | acetat |
| $\ce{MnO4-}$ | permanganat | $\ce{Cr2O7^2-}$ | dichromat |

- En ionforbindelse er **neutral**: summen af ladningerne er 0, fx $\ce{Ca^2+}$ + 2 $\ce{Cl-}$ → $\ce{CaCl2}$.
- Navn: positiv ion først, negativ ion bagefter – fx *calciumchlorid*, *jern(III)oxid*.

### Kemiske bindinger

| Forskel i elektronegativitet $\Delta EN$ | Bindingstype |
|---|---|
| under ca. 0,5 | upolær kovalent binding |
| ca. 0,5 – 1,7 | polær kovalent binding |
| over ca. 1,7 | ionbinding |

> Grænserne er **tommelfingerregler** – nogle bøger bruger 2,0 som grænse for ionbinding, og
> overgangen er glidende.

**Kræfter mellem molekyler** (svagest → stærkest, for molekyler af samme størrelse):
London-kræfter (van der Waals, vokser med molekylets størrelse) → dipol-dipol-bindinger →
hydrogenbindinger (H bundet til N, O eller F). Stærkere kræfter giver højere kogepunkt.

### Organisk kemi: alkaner

Alkaner har den generelle formel $\mathrm{C}_n\mathrm{H}_{2n+2}$ og kun enkeltbindinger. Navnets stamme
fortæller antallet af C-atomer – den samme stamme bruges i alle andre stofklasser.

| $n$ | Navn | Molekylformel | Strukturformel | Kogepunkt (1 atm) |
|---|---|---|---|---|
| 1 | methan | $\ce{CH4}$ | <img class="strukturformel" src="/images/formelsamling/alkan_01_methan.svg" alt="methan"> | −161,5 °C |
| 2 | ethan | $\ce{C2H6}$ | <img class="strukturformel" src="/images/formelsamling/alkan_02_ethan.svg" alt="ethan"> | −88,6 °C |
| 3 | propan | $\ce{C3H8}$ | <img class="strukturformel" src="/images/formelsamling/alkan_03_propan.svg" alt="propan"> | −42,1 °C |
| 4 | butan | $\ce{C4H10}$ | <img class="strukturformel" src="/images/formelsamling/alkan_04_butan.svg" alt="butan"> | −0,5 °C |
| 5 | pentan | $\ce{C5H12}$ | <img class="strukturformel" src="/images/formelsamling/alkan_05_pentan.svg" alt="pentan"> | 36,1 °C |
| 6 | hexan | $\ce{C6H14}$ | <img class="strukturformel" src="/images/formelsamling/alkan_06_hexan.svg" alt="hexan"> | 68,7 °C |
| 7 | heptan | $\ce{C7H16}$ | <img class="strukturformel" src="/images/formelsamling/alkan_07_heptan.svg" alt="heptan"> | 98,4 °C |
| 8 | octan | $\ce{C8H18}$ | <img class="strukturformel" src="/images/formelsamling/alkan_08_octan.svg" alt="octan"> | 125,7 °C |
| 9 | nonan | $\ce{C9H20}$ | <img class="strukturformel" src="/images/formelsamling/alkan_09_nonan.svg" alt="nonan"> | 150,8 °C |
| 10 | decan | $\ce{C10H22}$ | <img class="strukturformel" src="/images/formelsamling/alkan_10_decan.svg" alt="decan"> | 174,1 °C |

Kogepunkterne gælder de uforgrenede (normal-)alkaner. Stavemåden *hexan/octan* følger den
officielle danske nomenklatur; *heksan/oktan* ses i ældre bøger.

![Kogepunkter for alkaner](/images/formelsamling/alkan_kogepunkter.svg)

| Stofklasse | Generel formel | Endelse | Eksempel |
|---|---|---|---|
| Alkan | $\mathrm{C}_n\mathrm{H}_{2n+2}$ | -an | propan |
| Alken (én C=C) | $\mathrm{C}_n\mathrm{H}_{2n}$ | -en | propen |
| Alkyn (én C≡C) | $\mathrm{C}_n\mathrm{H}_{2n-2}$ | -yn | ethyn |
| Alkohol (én OH) | $\mathrm{C}_n\mathrm{H}_{2n+1}\mathrm{OH}$ | -ol | ethanol |

---

## B-niveau

### Redox

| Begreb | Regel |
|---|---|
| Oxidation | afgivelse af elektroner – oxidationstallet **stiger** |
| Reduktion | optagelse af elektroner – oxidationstallet **falder** |
| Oxidationsmiddel | bliver selv reduceret |
| Reduktionsmiddel | bliver selv oxideret |

**Regler for oxidationstal (OT)**
1. Et frit grundstof har OT = 0 (fx Fe, $\ce{O2}$, $\ce{Cl2}$).
2. En monoatomig ion har OT = ionens ladning (fx $\ce{Fe^3+}$: +III).
3. H har normalt +I (undtagen i metalhydrider: −I).
4. O har normalt −II (undtagen i peroxider: −I).
5. Summen af OT er lig med partiklens ladning (0 for et molekyle).

**Afstemning af redoxreaktioner:** 1) Find OT og hvem der oxideres/reduceres.
2) Afstem OT-ændringerne (op = ned). 3) Afstem ladning med $\ce{H3O+}$ (sur opløsning) eller
$\ce{OH-}$ (basisk). 4) Afstem H og O med $\ce{H2O}$.

**Spændingsrækken:** K, Ca, Na, Mg, Al, Zn, Fe, Ni, Sn, Pb, (H), Cu, Ag, Hg, Pt, Au.
Et metal kan reducere ionerne af de metaller, der står **til højre** for det.
Uædle metaller (venstre for H) opløses i ikke-oxiderende syre under udvikling af $\ce{H2}$.

### Spektrofotometri

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Absorbans | $A = \log\!\left(\dfrac{I_0}{I}\right) = -\log T$ | $T$: transmittans |
| Lambert–Beers lov | $A_\lambda = \varepsilon_\lambda \cdot l \cdot [\text{stof}]$ | $\varepsilon_\lambda$: molar absorptionskoefficient ved $\lambda$ (M⁻¹·cm⁻¹), $l$: kuvettens længde (cm), $[\text{stof}]$: **aktuel** koncentration |
| Standardkurve | $A = k \cdot c$ | en ret linje gennem (0, 0) → $c = A/k$ |

> **Gyldighed:** Lambert–Beer er kun lineær ved **lave koncentrationer** (typisk $A \lesssim 1$).
> Mål ved absorptionsmaksimum $\lambda_{\max}$ og fortynd prøven, hvis $A$ er for stor.
> Se [Spektrofotometri]({{< relref "/docs/kemi/Metoder/spektrofotometri" >}}).

### Kemisk ligevægt

For reaktionen $a\,\ce{A} + b\,\ce{B} \rightleftharpoons c\,\ce{C} + d\,\ce{D}$:

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Ligevægtsloven | $K = \dfrac{[\ce{C}]^c \cdot [\ce{D}]^d}{[\ce{A}]^a \cdot [\ce{B}]^b}$ | kun ligevægtskoncentrationer |
| Reaktionsbrøk | $Y = \dfrac{[\ce{C}]^c \cdot [\ce{D}]^d}{[\ce{A}]^a \cdot [\ce{B}]^b}$ | samme udtryk, men for *aktuelle* koncentrationer |
| Retning | $Y < K$: forløber mod **højre**; $\ Y > K$: mod **venstre**; $\ Y = K$: ligevægt | |
| Heterogen ligevægt | faste stoffer, rene væsker og vand (som opløsningsmiddel) udelades | |
| Gasligevægt | $K_p$ med partialtryk i bar | |
| Opløselighedsprodukt | $K_s = [\ce{M+}] \cdot [\ce{X-}]$ for $\ce{MX(s) <=> M+ + X-}$ | supplerende |

**Le Chateliers princip:** Et indgreb i en ligevægt får ligevægten til at forskyde sig, så
virkningen af indgrebet **formindskes**.

| Indgreb | Virkning |
|---|---|
| Tilsæt reaktant / fjern produkt | forskydning mod højre ($K$ uændret) |
| Øg trykket (mindsk rumfanget) | forskydning mod den side med **færrest gasmolekyler** |
| Hæv temperaturen | forskydning i den **endoterme** retning – nu ændres $K$ |
| Tilsæt katalysator | ingen forskydning – ligevægten indstiller sig blot hurtigere |

Eksempel: $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$ har $K = \dfrac{[\ce{NH3}]^2}{[\ce{N2}] \cdot [\ce{H2}]^3}$ med enheden $\text{M}^{-2}$.

### Syre-base og pH-beregninger

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Syrestyrkekonstant | $K_a = \dfrac{[\ce{H3O+}] \cdot [\ce{A-}]}{[\ce{HA}]}$ | |
| Basestyrkekonstant | $K_b = \dfrac{[\ce{HB+}] \cdot [\ce{OH-}]}{[\ce{B}]}$ | |
| Styrkeeksponent | $\text{p}K_a = -\log K_a$ | lille $\text{p}K_a$ → stærk syre |
| Korresponderende syre-basepar | $K_a \cdot K_b = K_w$, $\ \text{p}K_a + \text{p}K_b = 14{,}00$ | 25 °C |
| Svag syre | $\text{pH} = \tfrac{1}{2}\left(\text{p}K_a - \log c_s\right)$ | kun når syren er **lidt** protolyseret (tjek: $[\ce{H3O+}] \ll c_s$) |
| Svag base | $\text{pOH} = \tfrac{1}{2}\left(\text{p}K_b - \log c_b\right)$ | tilsvarende forudsætning |
| Middelstærk syre | $K_a = \dfrac{x^2}{c_s - x}$, $\ x = [\ce{H3O+}]$ | løs andengradsligningen |
| Pufferligningen | $\text{pH} = \text{p}K_a + \log\!\left(\dfrac{c_b}{c_s}\right)$ | Henderson–Hasselbalch; god puffer for $\text{pH} = \text{p}K_a \pm 1$ |
| Halvækvivalenspunkt | $\text{pH} = \text{p}K_a$ | $c_s = c_b$ |

Eksempler: 0,10 M eddikesyre ($\text{p}K_a = 4{,}76$): $\text{pH} = \tfrac{1}{2}(4{,}76 + 1{,}00) = 2{,}88$.
En puffer med 0,10 M eddikesyre og 0,10 M natriumacetat har pH = 4,76.

| Syre | Korresponderende base | $\text{p}K_a$ (25 °C) |
|---|---|---|
| $\ce{H3PO4}$ | $\ce{H2PO4-}$ | 2,15 |
| HF | $\ce{F-}$ | 3,17 |
| $\ce{CH3COOH}$ (eddikesyre) | $\ce{CH3COO-}$ | 4,76 |
| $\ce{CO2(aq)}$ ("kulsyre") | $\ce{HCO3-}$ | 6,35 |
| $\ce{H2PO4-}$ | $\ce{HPO4^2-}$ | 7,20 |
| $\ce{NH4+}$ | $\ce{NH3}$ | 9,25 |
| $\ce{HCO3-}$ | $\ce{CO3^2-}$ | 10,33 |
| $\ce{HPO4^2-}$ | $\ce{PO4^3-}$ | 12,35 |

> $\text{p}K_a$-værdier afviger typisk med nogle få hundrededele mellem databøger
> (fx angives phosphorsyres 3. trin som 12,32–12,38). Brug din egen databogs værdier til eksamen.

![Titrerkurve for en svag syre](/images/formelsamling/titrerkurve.svg)

### Reaktionshastighed

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Reaktionshastighed | $v = -\dfrac{1}{a} \cdot \dfrac{\mathrm{d}[\ce{A}]}{\mathrm{d}t} = \dfrac{1}{c} \cdot \dfrac{\mathrm{d}[\ce{C}]}{\mathrm{d}t}$ | M/s |
| Hastighedsudtryk | $v = k \cdot [\ce{A}]^x \cdot [\ce{B}]^y$ | $x$, $y$: **ordener** – bestemmes eksperimentelt, ikke fra koefficienterne |
| Totalorden | $x + y$ | |

**Integrerede hastighedslove – og hvordan man lineariserer dem**

| Orden | Integreret lov | Ret linje ved at afbilde | Halveringstid |
|---|---|---|---|
| 0. orden | $[\ce{A}] = [\ce{A}]_0 - k \cdot t$ | $[\ce{A}]$ mod $t$ (hældning $-k$) | $T_{½} = \dfrac{[\ce{A}]_0}{2k}$ |
| 1. orden | $\ln[\ce{A}] = \ln[\ce{A}]_0 - k \cdot t$ | $\ln[\ce{A}]$ mod $t$ (hældning $-k$) | $T_{½} = \dfrac{\ln 2}{k}$ – uafhængig af $[\ce{A}]_0$ |
| 2. orden | $\dfrac{1}{[\ce{A}]} = \dfrac{1}{[\ce{A}]_0} + k \cdot t$ | $\dfrac{1}{[\ce{A}]}$ mod $t$ (hældning $k$) | $T_{½} = \dfrac{1}{k \cdot [\ce{A}]_0}$ |

| Faktor | Virkning på hastigheden |
|---|---|
| Koncentration / tryk | flere sammenstød pr. sekund |
| Temperatur | flere sammenstød har energi nok til at overvinde aktiveringsenergien |
| Overfladeareal | flere partikler kan reagere samtidig (fast stof) |
| Katalysator | sænker aktiveringsenergien ved at åbne en anden reaktionsvej |

**Arrhenius' ligning** (supplerende): $k = A \cdot e^{-E_a/(R \cdot T)}$, lineariseret
$\ln k = \ln A - \dfrac{E_a}{R} \cdot \dfrac{1}{T}$ – afbild $\ln k$ mod $1/T$ og find $E_a$ af hældningen.

> Tommelfingerreglen "10 °C højere temperatur fordobler hastigheden" passer kun for
> reaktioner med $E_a \approx 50\ \text{kJ/mol}$ nær stuetemperatur.

### Reaktionsenergi

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Entalpiændring | $\Delta H = \sum \Delta_f H°(\text{produkter}) - \sum \Delta_f H°(\text{reaktanter})$ | husk koefficienterne |
| Kalorimetri | $q = m \cdot c \cdot \Delta T$, $\ \Delta H = -\dfrac{q}{n}$ | $q$: varme optaget af opløsningen |
| Fortegn | $\Delta H < 0$: exoterm; $\ \Delta H > 0$: endoterm | |

### Organisk kemi: stofklasser og reaktioner

| Stofklasse | Funktionel gruppe | Navneendelse | Eksempel |
|---|---|---|---|
| Alken | $\ce{C=C}$ | -en | but-2-en |
| Halogenalkan | $\ce{C-X}$ (X = F, Cl, Br, I) | forstavelse chlor-, brom- … | 2-chlorpropan |
| Alkohol | $\ce{-OH}$ | -ol | propan-2-ol |
| Ether | $\ce{R-O-R'}$ | -ether | diethylether |
| Aldehyd | $\ce{-CHO}$ | -al | ethanal |
| Keton | $\ce{R-CO-R'}$ | -on | propanon (acetone) |
| Carboxylsyre | $\ce{-COOH}$ | -syre | ethansyre (eddikesyre) |
| Ester | $\ce{-COO-}$ | -oat | ethylethanoat |
| Amin | $\ce{-NH2}$ | -amin | methylamin |
| Amid | $\ce{-CONH2}$ | -amid | ethanamid |
| Aminosyre | $\ce{-NH2}$ og $\ce{-COOH}$ | | glycin |

**Oxidation af alkoholer:** primær alkohol → aldehyd → carboxylsyre;
sekundær alkohol → keton; tertiær alkohol oxideres ikke (uden at C–C-bindinger brydes).

**Esterdannelse (kondensation):** carboxylsyre + alkohol $\rightleftharpoons$ ester + $\ce{H2O}$ – den modsatte reaktion er **hydrolyse** (fx forsæbning af fedt med NaOH).

| Reaktionstype | Kendetegn |
|---|---|
| Substitution | et atom/en gruppe udskiftes (fx alkan + $\ce{Br2}$ i lys) |
| Addition | et molekyle lægges til en dobbelt- eller tripelbinding |
| Elimination | et lille molekyle (fx $\ce{H2O}$) fraspaltes → dobbeltbinding |
| Kondensation | to molekyler kobles under fraspaltning af $\ce{H2O}$ |
| Hydrolyse | et molekyle spaltes ved reaktion med $\ce{H2O}$ |

**Isomeri:** *Strukturisomere* har samme molekylformel, men forskellig struktur (fx butan og
2-methylpropan). *Cis-trans-isomeri* ved C=C, når begge C-atomer har to forskellige grupper.
*Spejlbilledisomeri* ved et C-atom med fire forskellige grupper (chiralt C-atom).

</div>
