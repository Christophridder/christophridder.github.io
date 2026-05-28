# Logaritmer — Opgaveark

**Fysik A — Træning i logaritmeregler**

---

## Regler du skal kende

### Definitioner

$$\\log\_{10}(x) = a \\iff 10^a = x$$
$$\\ln(x) = a \\iff e^a = x \\qquad (e \\approx 2{,}718)$$

### Regneregler (gælder for både $\\log$ og $\\ln$)

| Regel         | Formel                                               | Eksempel                                                    |
|---------------|------------------------------------------------------|-------------------------------------------------------------|
| **Produktregel**  | $\\log(a \\cdot b) = \\log(a) + \\log(b)$                | $\\log(100 \\cdot 1000) = \\log(100) + \\log(1000) = 2 + 3 = 5$ |
| **Kvotientregel** | $\\log!\\left(\\dfrac{a}{b}\\right) = \\log(a) - \\log(b)$ | $\\log!\\left(\\dfrac{1000}{10}\\right) = 3 - 1 = 2$            |
| **Potensregel**   | $\\log(a^n) = n \\cdot \\log(a)$                        | $\\log(10^5) = 5 \\cdot \\log(10) = 5$                         |
| **Log af 1**      | $\\log(1) = 0$                                        | $\\ln(1) = 0$                                                |
| **Log af basen**  | $\\log(10) = 1$                                       | $\\ln(e) = 1$                                                |
| **Invers**        | $10^{\\log(x)} = x$                                   | $e^{\\ln(x)} = x$                                            |
| **Baseskift**     | $\\log_b(x) = \\dfrac{\\ln(x)}{\\ln(b)}$                 | $\\log_2(8) = \\dfrac{\\ln 8}{\\ln 2} = 3$                      |

### Isolering af eksponent — bruges meget i fysik!

$$A = A_0 \\cdot e^{-\\lambda t} \\implies t = \\frac{\\ln!\\left(\\dfrac{A_0}{A}\\right)}{\\lambda}$$

$$N = N_0 \\cdot 10^{k t} \\implies t = \\frac{\\log!\\left(\\dfrac{N}{N_0}\\right)}{k}$$

---

---

## Del 1 — Rene regneregler (uden lommeregner)

*Løs opgaverne ved at anvende reglerne ovenfor. Skriv hvert mellemtrin.*

---

### Opgave 1

Beregn uden lommeregner:
$$\\log(10^7)$$

**Svar:** \_____\_

---

### Opgave 2

Beregn uden lommeregner:
$$\\log(100 \\cdot 10^5)$$

**Svar:** \_____\_

---

### Opgave 3

Beregn uden lommeregner:
$$\\log!\\left(\\frac{10^8}{10^3}\\right)$$

**Svar:** \_____\_

---

### Opgave 4

Beregn uden lommeregner:
$$\\ln(e^{4})$$

**Svar:** \_____\_

---

### Opgave 5

Beregn uden lommeregner:
$$\\ln!\\left(\\frac{1}{e^3}\\right)$$

**Svar:** \_____\_

---

### Opgave 6

Omskriv til ét logaritmeudtryk:
$$\\log(3) + \\log(4) - \\log(6)$$

**Svar:** \_____\_

---

### Opgave 7

Omskriv til ét logaritmeudtryk og beregn:
$$2\\cdot\\log(5) + \\log(4)$$

*Hint: Brug potensreglen på det første led, og saml til sidst med produktreglen.*

**Svar:** \_____\_

---

### Opgave 8

Løs ligningen for $x$:
$$10^x = 500$$

**Svar:** \_____\_

---

### Opgave 9

Løs ligningen for $x$:
$$e^{2x} = 20$$

**Svar:** \_____\_

---

### Opgave 10

Løs ligningen for $t$:
$$3 = 12 \\cdot e^{-0{,}5 \\cdot t}$$

*Dette er formen du møder ved radioaktivt henfald og eksponentiel dæmpning.*

**Svar:** \_____\_

---

---

## Del 2 — Fysikopgaver med logaritmer

*Her bruges logaritmer til at isolere en ubekendt — præcis som i fysik A.*

---

### Opgave 11 — Radioaktivt henfald

Aktiviteten af et radioaktivt stof falder som:
$$A(t) = A_0 \\cdot e^{-\\lambda t}$$

Et stof har $A_0 = 800$ Bq og $\\lambda = 0{,}035 \\ \\text{s}^{-1}$.

**a)** Hvornår er aktiviteten faldet til $100$ Bq?

**b)** Hvad er halveringstiden $T\_{1/2}$?

*Hint til b: Sæt $A = \\frac{A_0}{2}$ og isoler $t$.*

**Svar a:** \_____\_  
**Svar b:** \_____\_

---

### Opgave 12 — Lydstyrke i decibel

Lydstyrken i decibel er defineret som:
$$L = 10 \\cdot \\log!\\left(\\frac{I}{I_0}\\right) \\quad \\text{dB}$$

hvor $I_0 = 10^{-12} \\ \\text{W/m}^2$ er høregrænsen.

**a)** En koncert har lydintensiteten $I = 0{,}1 \\ \\text{W/m}^2$. Beregn lydstyrken i dB.

**b)** En lyd måles til $85$ dB. Hvad er intensiteten i W/m²?

**Svar a:** \_____\_  
**Svar b:** \_____\_

---

### Opgave 13 — Befolkningsvækst

En bakteriekultur vokser eksponentielt:
$$N(t) = N_0 \\cdot e^{k t}$$

Ved $t = 0$ er der $N_0 = 500$ bakterier. Efter $3$ timer er der $4000$ bakterier.

**a)** Bestem vækstraten $k$.

**b)** Hvornår er der $10^6$ bakterier?

**Svar a:** \_____\_  
**Svar b:** \_____\_

---

### Opgave 14 — pH-værdi

pH er defineret som:
$$\\text{pH} = -\\log[\\text{H}^+]$$

hvor $[\\text{H}^+]$ er koncentrationen af H⁺-ioner i mol/L.

**a)** Rent vand har $[\\text{H}^+] = 10^{-7}$ mol/L. Hvad er pH?

**b)** En syre har pH = 3,5. Hvad er $[\\text{H}^+]$?

**c)** Hvis $[\\text{H}^+]$ fordobles — hvor meget ændrer pH sig så?

*Hint til c: Brug logaritmereglerne til at finde $\\Delta\\text{pH}$.*

**Svar a:** \_____\_  
**Svar b:** \_____\_  
**Svar c:** \_____\_

---

### Opgave 15 — Jordskælv og Richterskalaen

Richterskalaen er logaritmisk:
$$M = \\log!\\left(\\frac{A}{A_0}\\right)$$

Et jordskælv måles til $M = 6{,}0$. Et andet måles til $M = 8{,}0$.

**a)** Hvor mange gange større er amplituden $A$ ved det stærkeste jordskælv?

**b)** Energien frigivet er proportional med $10^{1{,}5M}$. Hvor mange gange mere energi frigives ved $M = 8{,}0$ end ved $M = 6{,}0$?

**Svar a:** \_____\_  
**Svar b:** \_____\_

---

---

## Del 3 — Grafer og logaritmisk skala

*Kør Python-kodecellerne nedenfor og besvar spørgsmålene.*