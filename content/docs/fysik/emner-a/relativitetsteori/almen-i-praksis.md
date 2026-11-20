---
title: "Almen relativitet i praksis"
weight: 9
---

**Niveau: Fysik A (supplerende stof)** · **Emne: Almen relativitet og GPS** · **1 modul**

På siden [Findes tyngdekraften?]({{< relref "tyngdekraft-referenceramme" >}}) så du Einsteins idé: Tyngde er ikke en kraft, men noget, rummet og tiden gør. En af følgerne er, at **ure højt oppe går hurtigere** end ure nede ved jorden. Det er den **almene relativitetsteori**. Uden den ville din telefons GPS være ubrugelig efter få minutter.

## To effekter – to simple formler

Et ur i kredsløb om Jorden påvirkes af to ting på én gang:

| Effekt | Teori | Hvad sker der? | Uret ændrer sig med ca. |
|---|---|---|---|
| **Farten** | Speciel relativitet | Uret går **langsommere** | $\Delta t \cdot \dfrac{\tfrac{1}{2} v^2}{c^2}$ |
| **Højden** | Almen relativitet | Uret går **hurtigere** | $\Delta t \cdot \dfrac{\dfrac{G \cdot M}{R} - \dfrac{G \cdot M}{r}}{c^2}$ |

- $R$ er Jordens radius (hvor vi står), $r$ er afstanden fra Jordens centrum til uret.
- Tæt ved jordoverfladen kan tyngdeformlen forenkles til $\Delta t \cdot \dfrac{g \cdot h}{c^2}$.

**Læg mærke til:** $\tfrac{1}{2} v^2$ er den kinetiske energi pr. kg, og $\dfrac{G M}{R} - \dfrac{G M}{r}$ er den potentielle energi pr. kg, der skal til for at løfte noget fra jordoverfladen op i afstanden $r$ (se [Energi i centralbevægelse]({{< relref "energi-centralbevaegelse" >}})). Begge effekter er altså *energi pr. kg divideret med $c^2$*.

Konstanter: $c = 3{,}00 \cdot 10^{8}$ m/s, $G = 6{,}674 \cdot 10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_\text{Jord} = 5{,}972 \cdot 10^{24}$ kg, $R_\text{Jord} = 6371$ km, $1$ døgn $= 86\,400$ s.

## Hvor er GPS-satellitterne?

<figure>
<svg viewBox="0 0 640 400" width="100%" style="max-width:640px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<circle cx="230" cy="200" r="167" fill="none" stroke="#e08a1e" stroke-width="2" stroke-dasharray="7 5"/>
<circle cx="230" cy="200" r="43" fill="none" stroke="#c0392b" stroke-width="1.5"/>
<circle cx="230" cy="200" r="40" fill="#3d7cc9"/>
<path d="M214,180 q10,-8 20,0 t14,10 q-5,12 -17,7 t-17,-17 z M222,212 q12,-5 20,4 q2,10 -10,10 q-9,-3 -10,-14 z" fill="#5fa55a"/>
<g fill="#e08a1e" stroke="#7a4a0e" stroke-width="1">
<rect x="390" y="193" width="14" height="14" rx="2"/>
<rect x="306" y="49" width="14" height="14" rx="2"/>
<rect x="140" y="49" width="14" height="14" rx="2"/>
<rect x="56" y="193" width="14" height="14" rx="2"/>
<rect x="140" y="337" width="14" height="14" rx="2"/>
<rect x="306" y="337" width="14" height="14" rx="2"/>
</g>
<circle cx="260" cy="170" r="4" fill="#c0392b"/>
<text x="268" y="160" fill="#c0392b">ISS · 408 km</text>
<text x="230" y="204" text-anchor="middle" fill="white" font-size="11" font-weight="bold">Jorden</text>
<text x="330" y="40" fill="#b5650d" font-weight="bold">GPS-satellitter</text>
<text x="330" y="22" fill="#b5650d">20 200 km over jorden</text>
<line x1="230" y1="200" x2="397" y2="200" stroke="#555" stroke-width="1"/>
<text x="300" y="217" fill="#333">r = 26 560 km</text>
<rect x="430" y="105" width="196" height="150" rx="8" fill="#f4f1ea" stroke="#999"/>
<text x="442" y="128" font-weight="bold" fill="#333">Et GPS-ur pr. døgn</text>
<text x="442" y="152" fill="#333">Farten (3,87 km/s):</text>
<text x="612" y="152" text-anchor="end" fill="#1f4fd1" font-weight="bold">−7 μs</text>
<text x="442" y="176" fill="#333">Højden:</text>
<text x="612" y="176" text-anchor="end" fill="#c0392b" font-weight="bold">+46 μs</text>
<line x1="442" y1="188" x2="612" y2="188" stroke="#999"/>
<text x="442" y="210" fill="#333" font-weight="bold">I alt:</text>
<text x="612" y="210" text-anchor="end" fill="#333" font-weight="bold">+38 μs</text>
<text x="442" y="238" fill="#555" font-size="12">≈ 11 km fejl pr. døgn</text>
</svg>
<figcaption>Tegnet i målestok: GPS-satellitterne er langt længere ude end ISS. Der er ca. 30 GPS-satellitter i 6 baneplaner – her ses kun nogle få. 1 μs = 10⁻⁶ s.</figcaption>
</figure>

## Opgave 1: GPS-urene

En GPS-satellit kredser om Jorden i afstanden $r = 26\,560$ km fra Jordens centrum. Den har et atomur om bord, og din telefon finder din position ved at måle, hvor lang tid signalerne er om at nå frem.

**a)** Bestem satellittens fart med $v = \sqrt{\dfrac{G \cdot M_\text{Jord}}{r}}$.

**b)** *Farten:* Hvor meget går satellittens ur **langsommere** pr. døgn?

**c)** *Højden:* Hvor meget går satellittens ur **hurtigere** pr. døgn?

**d)** Hvad bliver det samlet? Går satellittens ur for hurtigt eller for langsomt?

**e)** Lyset bevæger sig $300$ m på $1\ \mu$s. Hvor stor en fejl i din position giver det efter ét døgn, hvis man ikke retter for relativitet?

**f)** GPS skal kunne finde dig inden for ca. $5$ m. Hvor mange sekunder går der, før fejlen er $5$ m?

> **Sådan gør man i virkeligheden:** Før satellitterne sendes op, indstilles atomurene til at gå en lille smule *langsommere* end på jorden – frekvensen sættes til $10{,}229\,999\,995\,43$ MHz i stedet for $10{,}23$ MHz. Når de så er oppe i banen, går de præcis rigtigt.

## Opgave 2: ISS – hvem vinder?

ISS kredser i afstanden $r = 6779$ km fra Jordens centrum med farten $7{,}67$ km/s.

**a)** Hvor meget langsommere går et ur på ISS pr. døgn på grund af farten?

**b)** Hvor meget hurtigere går det pr. døgn på grund af højden?

**c)** Går uret på ISS samlet for hurtigt eller for langsomt?

**d)** For GPS vinder højden, men for ISS vinder farten. Forklar hvorfor.

**e)** *(Udfordring)* I hvilken højde ophæver de to effekter hinanden? Brug, at $v^2 = \dfrac{G \cdot M}{r}$ i en cirkelbane.

## Opgave 3: Uret på hylden (2010)

I 2010 målte forskere ved NIST i USA med ekstremt præcise optiske atomure, at et ur går hurtigere, når det løftes blot ca. $33$ cm. Tæt ved jorden bruger vi $\Delta t \cdot \dfrac{g \cdot h}{c^2}$ med $g = 9{,}82$ m/s².

**a)** Bestem $\dfrac{g \cdot h}{c^2}$ for $h = 33$ cm.

**b)** Du bor på 1. sal, $3$ m over din nabo i stuen. Hvor meget mere tid er der gået for dig efter $80$ år?

**c)** Tilbage til flyet fra [Speciel relativitet i praksis]({{< relref "speciel-i-praksis" >}}): Flyet var $40$ timer i ca. $10$ km's højde. Hvor meget hurtigere gik uret på grund af højden? Sammenlign med de $50$ ns, det tabte på grund af farten.

## Modelgyldighed

- **Formlerne er tilnærmelser** for *svage* tyngdefelter og farter, der er langt mindre end $c$. Det er opfyldt rigtig godt ved Jorden – fejlen er langt under $1$ %. Ved et sort hul duer de ikke.
- **Jordens rotation** er udeladt. Ure ved ækvator bevæger sig også (ca. $465$ m/s), og det har GPS-systemet også med i sine beregninger.
- **Banerne** er regnet som perfekte cirkler. GPS-banerne er næsten cirkulære, men en lille afvigelse giver en lille ekstra korrektion, som modtageren selv regner ud.
- **Newton er ikke forkert** her – han er bare ikke præcis nok. Satellittens bane passer fint med Newton. Det er *urene*, der kræver Einstein.

## Hints og løsninger

<details>
<summary><strong>Hints</strong></summary>

**1a)** $r = 26\,560 \cdot 10^{3}$ m. Svaret bliver i m/s.

**1b)** Brug $\Delta t \cdot \dfrac{\tfrac{1}{2} v^2}{c^2}$ med $\Delta t = 86\,400$ s. Regn svaret om til mikrosekunder: $1\ \mu\mathrm{s} = 10^{-6}$ s.

**1c)** Udregn først $\dfrac{G M}{R}$ og $\dfrac{G M}{r}$ hver for sig. Husk meter.

**1d)** Gevinst minus tab.

**1e)** Fejl i afstand = antal μs gange $300$ m.

**1f)** Hvor mange mikrosekunder svarer $5$ m til? Og hvor meget går uret forkert pr. sekund?

**2e)** Sæt $\tfrac{1}{2} v^2 = \dfrac{G M}{R} - \dfrac{G M}{r}$ og indsæt $v^2 = \dfrac{G M}{r}$. Så forsvinder $G M$, og du kan isolere $r$.

**3b)** $80$ år $= 80 \cdot 365{,}25 \cdot 86\,400$ s.

</details>

<details>
<summary><strong>Løsninger</strong></summary>

$G \cdot M_\text{Jord} = 6{,}674 \cdot 10^{-11} \cdot 5{,}972 \cdot 10^{24} = 3{,}986 \cdot 10^{14}\ \mathrm{m^3/s^2}$

**1a)**

$$v = \sqrt{\frac{3{,}986 \cdot 10^{14}}{2{,}656 \cdot 10^{7}}}\ \mathrm{m/s} = 3874\ \mathrm{m/s} \approx 3{,}87\ \mathrm{km/s}$$

**1b)**

$$86\,400\ \mathrm{s} \cdot \frac{\tfrac{1}{2} \cdot 3874^2}{(3{,}00 \cdot 10^{8})^2} = 86\,400\ \mathrm{s} \cdot 8{,}34 \cdot 10^{-11} = 7{,}2 \cdot 10^{-6}\ \mathrm{s} = 7{,}2\ \mu\mathrm{s}$$

**1c)** $\dfrac{G M}{R} = 6{,}256 \cdot 10^{7}\ \mathrm{J/kg}$ og $\dfrac{G M}{r} = 1{,}501 \cdot 10^{7}\ \mathrm{J/kg}$. Forskellen er $4{,}755 \cdot 10^{7}$ J/kg.

$$86\,400\ \mathrm{s} \cdot \frac{4{,}755 \cdot 10^{7}}{(3{,}00 \cdot 10^{8})^2} = 86\,400\ \mathrm{s} \cdot 5{,}28 \cdot 10^{-10} = 45{,}7\ \mu\mathrm{s}$$

**1d)** $45{,}7\ \mu\mathrm{s} - 7{,}2\ \mu\mathrm{s} = 38{,}4\ \mu\mathrm{s}$ pr. døgn. Satellittens ur går **for hurtigt** – højden vinder over farten.

**1e)** $38{,}4 \cdot 300\ \mathrm{m} \approx 11\,500\ \mathrm{m} \approx 11{,}5$ km pr. døgn. Efter en uge ville GPS'en tage $80$ km fejl.

**1f)** $5$ m svarer til $\dfrac{5}{300}\ \mu\mathrm{s} = 0{,}0167\ \mu\mathrm{s}$. Uret går $\dfrac{38{,}4\ \mu\mathrm{s}}{86\,400\ \mathrm{s}} = 4{,}45 \cdot 10^{-4}\ \mu\mathrm{s}$ forkert pr. sekund.

$$t = \frac{0{,}0167}{4{,}45 \cdot 10^{-4}}\ \mathrm{s} \approx 37\ \mathrm{s}$$

Uden almen relativitet ville GPS være ubrugelig efter **under et minut**.

**2a)** $86\,400\ \mathrm{s} \cdot \dfrac{\tfrac{1}{2} \cdot 7670^2}{(3{,}00 \cdot 10^{8})^2} = 28{,}2\ \mu\mathrm{s}$ langsommere

**2b)** $\dfrac{G M}{R} - \dfrac{G M}{r} = 6{,}256 \cdot 10^{7} - 5{,}880 \cdot 10^{7} = 3{,}77 \cdot 10^{6}$ J/kg, så

$$86\,400\ \mathrm{s} \cdot \frac{3{,}77 \cdot 10^{6}}{(3{,}00 \cdot 10^{8})^2} = 3{,}6\ \mu\mathrm{s}\ \text{hurtigere}$$

**2c)** $3{,}6 - 28{,}2 = -24{,}6\ \mu\mathrm{s}$ pr. døgn. Uret på ISS går **for langsomt**.

**2d)** ISS er tæt på Jorden, så højdeforskellen (og dermed tyngdeeffekten) er lille, mens farten er stor. GPS er langt ude: Højdeforskellen er stor, og farten er lavere.

**2e)** $\tfrac{1}{2} \cdot \dfrac{G M}{r} = \dfrac{G M}{R} - \dfrac{G M}{r}$. Divider med $G M$: $\dfrac{1}{2r} + \dfrac{1}{r} = \dfrac{1}{R}$, altså $\dfrac{3}{2r} = \dfrac{1}{R}$ og

$$r = \tfrac{3}{2} R = 9557\ \text{km}$$

Det er ca. $3200$ km over jordoverfladen. Længere nede vinder farten, længere ude vinder højden.

*Tilbage til Scott Kelly:* Fart $-9{,}6$ ms og højde $+3{,}6\ \mu\mathrm{s} \cdot 340 = +1{,}2$ ms. Samlet blev Scott ca. $8{,}4$ ms yngre end Mark.

**3a)** $\dfrac{9{,}82 \cdot 0{,}33}{(3{,}00 \cdot 10^{8})^2} = 3{,}6 \cdot 10^{-17}$. Uret vinder $3{,}6 \cdot 10^{-17}$ s pr. sekund – og det kunne de måle!

**3b)** $80 \cdot 365{,}25 \cdot 86\,400\ \mathrm{s} = 2{,}52 \cdot 10^{9}$ s og $\dfrac{9{,}82 \cdot 3}{(3{,}00 \cdot 10^{8})^2} = 3{,}27 \cdot 10^{-16}$:

$$2{,}52 \cdot 10^{9}\ \mathrm{s} \cdot 3{,}27 \cdot 10^{-16} = 8{,}3 \cdot 10^{-7}\ \mathrm{s} \approx 0{,}8\ \mu\mathrm{s}$$

Du bliver altså $0{,}8$ milliontedele af et sekund ældre end naboen.

**3c)** $144\,000\ \mathrm{s} \cdot \dfrac{9{,}82 \cdot 10\,000}{(3{,}00 \cdot 10^{8})^2} = 157$ ns hurtigere. Højden *vinder* over farten ($50$ ns), så samlet går flyets ur ca. $107$ ns hurtigere. Derfor var tyngden nødvendig for at forklare Hafele og Keatings resultater.

</details>
