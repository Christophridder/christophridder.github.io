---
title: "Titrering"
weight: 2
---

**Niveau: Kemi C–B** · **Emne: Kvantitativ analyse – hvor meget stof er der?**

[Tilbage til Metoder]({{< relref "/docs/kemi/Metoder" >}})

## Video: hvad er en titrering?

{{< yt id="w7WdHX8cbFg" >}}

*Kilde: Jesper Melchjorsen — "Hvad er en titrering?".*

## Kort forklaret

- En **titrering** er en metode til at finde ud af, **hvor meget** af et bestemt stof der er i en prøve.
- Man tilsætter langsomt en opløsning med **kendt koncentration** fra en **burette**, indtil præcis alt stoffet i prøven har reageret.
- Så aflæser man, **hvor mange mL** der blev brugt. Da man kender koncentrationen, kan man regne ud, hvor mange mol der er tilsat – og dermed hvor mange mol der var i prøven.
- For at se, hvornår man skal stoppe, bruger man en **indikator**, der skifter farve, når reaktionen er færdig (eller et pH-meter).

| Ord | Betydning |
|---|---|
| **Titrator** (titrant) | Opløsningen i buretten – med **kendt** koncentration, fx 0,100 M AgNO₃ |
| **Titrand** | Prøven i bægerglasset – med **ukendt** indhold, fx opløst småkage |
| **Burette** | Et langt, inddelt glasrør med hane, så man kan aflæse forbruget præcist (0,05 mL) |
| **Ækvivalenspunkt** | Det punkt, hvor der er tilsat *præcis* den mængde titrator, der skal til ifølge reaktionsskemaet |
| **Endepunkt** | Det punkt, hvor indikatoren skifter farve – og hvor du stopper. Ideelt er endepunkt = ækvivalenspunkt |
| **Indikator** | Et stof, der skifter farve ved endepunktet |

**De to formler, du skal bruge – hver eneste gang:**

$$n = c \cdot V \qquad\qquad m = M \cdot n$$

> **Husk enheden!** $V$ skal være i **liter**, når $c$ er i mol/L. 6,85 mL = 0,00685 L.

## Hvad sker der i kolben undervejs?

Vi følger **kontrolforsøget** fra [Salt i ting]({{< relref "/docs/kemi/C-Eksp/salt-i-ting" >}}): 10,00 mL af en NaCl-opløsning, som vi selv har lavet, så vi **ved**, at der er præcis $1{,}00 \cdot 10^{-3}$ mol Cl⁻ i kolben. Vi titrerer med 0,100 M AgNO₃ og bruger DCF som indikator.

Hver mL sølvnitrat indeholder $n = c \cdot V = 0{,}100\ \tfrac{\text{mol}}{\text{L}} \cdot 0{,}00100\ \text{L} = 1{,}00 \cdot 10^{-4}$ mol Ag⁺. Hver sølvion fælder præcis én chloridion:

$$\text{Ag}^+\text{(aq)} + \text{Cl}^-\text{(aq)} \rightarrow \text{AgCl(s)}$$

| Tilsat AgNO₃ | $n(\text{Ag}^+)$ tilsat | $n(\text{Cl}^-)$ tilbage i opløsningen | $n(\text{Ag}^+)$ i overskud | Hvad ser du? |
|---|---|---|---|---|
| 0 mL | 0 | $1{,}00 \cdot 10^{-3}$ mol | 0 | klar, gullig-grøn opløsning |
| 2,00 mL | $2{,}0 \cdot 10^{-4}$ mol | $8{,}0 \cdot 10^{-4}$ mol | 0 | hvidt bundfald af AgCl dannes |
| 5,00 mL | $5{,}0 \cdot 10^{-4}$ mol | $5{,}0 \cdot 10^{-4}$ mol | 0 | mere bundfald – halvdelen af Cl⁻ er fældet |
| 9,90 mL | $9{,}9 \cdot 10^{-4}$ mol | $1{,}0 \cdot 10^{-5}$ mol | 0 | stadig gullig-grøn – **næsten** færdig |
| **10,00 mL** | $1{,}00 \cdot 10^{-3}$ mol | ≈ 0 | ≈ 0 | **ækvivalenspunktet** |
| 10,05 mL (én dråbe mere) | $1{,}005 \cdot 10^{-3}$ mol | ≈ 0 | $5 \cdot 10^{-6}$ mol | bundfaldet bliver **lyserødt** → stop! |

**Pointen:** Så længe der er Cl⁻ tilbage, "forsvinder" hver sølvion ned i bundfaldet. Først når det sidste Cl⁻ er fældet, er der sølvioner i overskud – og **det** er det, indikatoren reagerer på. Ved endepunktet gælder derfor:

$$n(\text{Ag}^+)_{\text{tilsat}} = n(\text{Cl}^-)_{\text{i prøven}}$$

**Hvorfor skifter DCF farve?** Bundfaldskornene af AgCl binder de ioner på overfladen, der er i overskud i opløsningen:
- **Før ækvivalenspunktet** er der overskud af Cl⁻, så kornene bliver **negativt** ladede. Indikatoren er selv en negativ ion og frastødes – opløsningen er gullig-grøn.
- **Efter ækvivalenspunktet** er der overskud af Ag⁺, så kornene bliver **positivt** ladede. Nu bindes indikatorens negative ioner til overfladen, og bundfaldet farves **lyserødt**.

> Det er derfor, farveskiftet sidder på *bundfaldet* og ikke i selve opløsningen – og derfor skal der røres godt hele tiden.

**Tjek af metoden:** Brugte du 10,00 mL, rammer metoden præcist. Brugte du fx 10,40 mL, er afvigelsen $\dfrac{10{,}00 - 10{,}40}{10{,}00} \cdot 100\ \% = -4{,}0\ \%$ – typisk fordi farveskiftet først ses lidt efter ækvivalenspunktet. Den viden bruger du, når du bagefter titrerer prøver med **ukendt** indhold.

## Eksempel: salt i en småkage – trin for trin

Vi bruger forsøget [Salt i ting]({{< relref "/docs/kemi/C-Eksp/salt-i-ting" >}}). Salt er natriumchlorid, NaCl. Natriumionerne er svære at få til at reagere, men **chloridionerne** reagerer med sølvioner og danner et hvidt bundfald:

$$\text{Ag}^+\text{(aq)} + \text{Cl}^-\text{(aq)} \rightarrow \text{AgCl(s)}$$

**Målingerne** (opdigtede, men realistiske tal):

| Hvad | Værdi |
|---|---|
| Masse af knust småkage | $m_{\text{kage}} = 5{,}012\ \text{g}$ |
| Koncentration af sølvnitrat i buretten | $c(\text{AgNO}_3) = 0{,}100\ \text{M}$ |
| Burettens start-aflæsning | $0{,}40\ \text{mL}$ |
| Burettens slut-aflæsning (ved farveskift) | $7{,}25\ \text{mL}$ |
| Varedeklaration | salt: 0,85 g pr. 100 g |

### Trin 1 – Hvor meget sølvnitrat brugte vi?

Forbruget er forskellen mellem slut og start:

$$V = 7{,}25\ \text{mL} - 0{,}40\ \text{mL} = 6{,}85\ \text{mL} = 0{,}00685\ \text{L}$$

> 💡 Buretten behøver ikke starte på 0 – det er **forskellen**, der tæller.

### Trin 2 – Hvor mange mol sølvioner er det?

$$n(\text{Ag}^+) = c \cdot V = 0{,}100\ \tfrac{\text{mol}}{\text{L}} \cdot 0{,}00685\ \text{L} = 6{,}85 \cdot 10^{-4}\ \text{mol}$$

### Trin 3 – Hvor mange mol chloridioner var der så?

Reaktionsskemaet siger **1 Ag⁺ reagerer med 1 Cl⁻**. Ved ækvivalenspunktet er der altså tilsat lige så mange sølvioner, som der var chloridioner:

$$n(\text{Cl}^-) = n(\text{Ag}^+) = 6{,}85 \cdot 10^{-4}\ \text{mol}$$

### Trin 4 – Hvor mange mol salt er det?

Vi antager, at **alt chlorid kommer fra NaCl**. Én NaCl giver én Cl⁻:

$$n(\text{NaCl}) = n(\text{Cl}^-) = 6{,}85 \cdot 10^{-4}\ \text{mol}$$

### Trin 5 – Hvor mange gram salt er det?

$M(\text{NaCl}) = 22{,}99 + 35{,}45 = 58{,}44\ \text{g/mol}$:

$$m(\text{NaCl}) = M \cdot n = 58{,}44\ \tfrac{\text{g}}{\text{mol}} \cdot 6{,}85 \cdot 10^{-4}\ \text{mol} = 0{,}0400\ \text{g} = 40{,}0\ \text{mg}$$

### Trin 6 – Hvor mange procent salt er der i småkagen?

$$w(\text{NaCl}) = \frac{m(\text{NaCl})}{m_{\text{kage}}} \cdot 100\ \% = \frac{0{,}0400\ \text{g}}{5{,}012\ \text{g}} \cdot 100\ \% = 0{,}80\ \%$$

Det svarer til **0,80 g salt pr. 100 g småkage**.

### Trin 7 – Passer det med varedeklarationen?

$$\text{Afvigelse} = \frac{0{,}85 - 0{,}80}{0{,}85} \cdot 100\ \% = 5{,}9\ \%$$

Vi fandt lidt **mindre** salt end deklarationen. Mulige forklaringer:
- Ikke alt salt blev opløst fra krummerne (kagen skal knuses godt og røres længe).
- Endepunktet blev aflæst en anelse for tidligt (farveskiftet med DCF er svagt).
- Varedeklarationens "salt" er beregnet ud fra **natrium** ($\text{salt} = 2{,}5 \cdot \text{natrium}$). Natrium fra fx natron (NaHCO₃) tæller med i deklarationen, men giver ingen Cl⁻ – og chlorid fra andre kilder end NaCl tæller omvendt med i vores titrering.

**Hele udregningen i én linje** – når du har forstået trinene:

$$w = \frac{c \cdot V \cdot M}{m_{\text{kage}}} \cdot 100\ \% = \frac{0{,}100 \cdot 0{,}00685 \cdot 58{,}44}{5{,}012} \cdot 100\ \% = 0{,}80\ \%$$

## Opgave: prøv selv

**1) Chips.** 2,506 g knuste chips titreres med 0,100 M AgNO₃. Forbruget er 5,60 mL. Beregn saltindholdet i g pr. 100 g.

<details>
<summary>Facit</summary>

$n = 0{,}100 \cdot 0{,}00560 = 5{,}60 \cdot 10^{-4}\ \text{mol}$ → $m = 58{,}44 \cdot 5{,}60 \cdot 10^{-4} = 0{,}0327\ \text{g}$ → $w = \dfrac{0{,}0327}{2{,}506} \cdot 100\ \% = 1{,}31\ \%$, dvs. **1,3 g salt pr. 100 g**.

</details>

**2) Havvand (med fortynding).** 10,0 mL havvand fortyndes til 100,0 mL i en målekolbe. Du udtager 10,0 mL af den fortyndede opløsning og titrerer med 0,100 M AgNO₃. Forbruget er 5,50 mL. Hvor mange gram salt er der pr. liter havvand?

<details>
<summary>Facit</summary>

- $n(\text{Cl}^-) = 0{,}100 \cdot 0{,}00550 = 5{,}50 \cdot 10^{-4}\ \text{mol}$ i de 10,0 mL **fortyndede** opløsning.
- 10,0 mL fortyndet opløsning indeholder kun 1,00 mL havvand (fortyndingsfaktor 10).
- $c(\text{Cl}^-)_{\text{havvand}} = \dfrac{5{,}50 \cdot 10^{-4}\ \text{mol}}{0{,}00100\ \text{L}} = 0{,}550\ \text{M}$
- $0{,}550\ \tfrac{\text{mol}}{\text{L}} \cdot 58{,}44\ \tfrac{\text{g}}{\text{mol}} = $ **32 g salt pr. liter** (regnet som NaCl).

Det passer fint med åbent ocean. De danske farvande er mindre salte – især Østersøen og fjordene.

</details>

Flere opgaver af samme slags: [Titreringsopgaver]({{< relref "/docs/kemi/C-Mængdeberegninger/titreringsopgaver" >}}).

## Typer af titrering – og hvor du møder dem

| Type | Reaktion | Endepunkt ses med | Niveau | Øvelse |
|---|---|---|---|---|
| Fældningstitrering | $\text{Ag}^+ + \text{Cl}^- \rightarrow \text{AgCl(s)}$ | DCF-indikator (bliver lyserød) | C | [Salt i ting]({{< relref "/docs/kemi/C-Eksp/salt-i-ting" >}}) |
| Syre-base, farveindikator | $\text{H}_3\text{O}^+ + \text{OH}^- \rightarrow 2\,\text{H}_2\text{O}$ | fx phenolphthalein | C | [Syre i vingummibamser]({{< relref "/docs/kemi/C-Eksp/vingummi" >}}) |
| Redoxtitrering | $\text{MnO}_4^-$ oxiderer $\text{Fe}^{2+}$ | permanganatens egen lilla farve | C → B | [Jern i ståluld]({{< relref "/docs/kemi/B-Eksp/staaluld" >}}) |
| pH-titrering | syre + base, pH måles hele vejen | pH-meter → titrerkurve | B | [Phosphorsyre i cola]({{< relref "/docs/kemi/B-Eksp/phosphorsyre-cola" >}}) |

## Gode råd ved titrering

- **Skyl buretten** med lidt titrator først, så den ikke fortyndes af vandrester.
- Fjern **luftbobler** i spidsen af buretten, inden du aflæser startvolumen.
- Aflæs i **øjenhøjde** ved bunden af menisken – med to decimaler (fx 7,25 mL).
- Titrér **hurtigt** i starten og **dråbevis** tæt på endepunktet. Lav gerne en hurtig "prøvetitrering" først, så du ved, hvor endepunktet ligger.
- Lav mindst en **dobbeltbestemmelse**, og brug gennemsnittet.
- Brug en **hvid baggrund** under glasset, så farveskiftet er lettere at se.

## Eksperiment

Nu skal du selv prøve metoden: [Salt i ting]({{< relref "/docs/kemi/C-Eksp/salt-i-ting" >}}).
