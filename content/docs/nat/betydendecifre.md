---
title: "Betydendecifre"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
# bookIcon: ''
---

# Betydende cifre

Når man måler en størrelse i fysik eller kemi — eller angiver et resultat — fortæller **antal betydende cifre** noget om, hvor nøjagtig talværdien er.

Skriver man fx en længde som

$$s = 1{,}23 \text{ m},$$

betyder det, at man har målt $s$ med en nøjagtighed på $0{,}01 \text{ m}$. Man ved derfor, at **"den sande værdi"** ligger mellem

$$s_{\min} = 1{,}225 \text{ m} \qquad \text{og} \qquad s_{\max} = 1{,}235 \text{ m}.$$

## Hvordan tæller man betydende cifre?

| Tal | Betydende cifre | Decimaler |
| :--- | :---: | :---: |
| $23{,}77$ | 4 | 2 |
| $0{,}002377$ | 4 | 6 |

**Nuller FØR den første "rigtige" ciffer tæller IKKE med.** $0{,}002377$ er jo det samme som $2{,}377 \cdot 10^{-3}$ og har altså 4 betydende cifre.

Trailing-nuller (nuller til sidst) tæller derimod **med**, fordi de fortæller om nøjagtigheden. Vil man angive, at man har målt en masse på 20 g med en nøjagtighed på mg, skal man skrive

$$m = 20{,}000 \text{ g}.$$

Her viser de tre decimaler, at man kender massen helt ned til milligram (5 betydende cifre).

### Hvorfor 10-tals-potenser er nyttige

Uden 10-tals-potenser kan det være **uklart**, hvor mange betydende cifre et stort tal har. Tabellen nedenfor viser samme tal, $9\,876\,000$, skrevet på forskellige måder:

| Tal | Betydende cifre | Decimaler |
| :--- | :---: | :---: |
| $9\,876\,000{,}00$ | 9 | 2 |
| $9\,876\,000$ | uklart: 4 til 7 | 0 |
| $98\,760 \cdot 10^{2}$ | uklart: 4 eller 5 | 0 |
| $987{,}6 \cdot 10^{4}$ | 4 | 1 |
| $9{,}876 \cdot 10^{6}$ | 4 | 3 |

Skriver man tallet i **videnskabelig notation** ($9{,}876 \cdot 10^{6}$), er der ingen tvivl: præcis 4 betydende cifre.

## Regneregler med målte størrelser

Når man bruger målinger i en formel, gælder der to regler — og de er **forskellige** for $+\,/\,-$ og for $\cdot\,/\,/$:

### Regel 1 — addition og subtraktion: tæl **decimaler**

Resultatet får lige så mange **decimaler** som det tal, der har **færrest decimaler**.

**Eksempel:**

$$20{,}567 + 0{,}0007 = 20{,}568$$

$20{,}567$ kender vi kun til 3 decimaler, mens $0{,}0007$ har 4. Vi kan altså højst beholde **3 decimaler** i svaret — derfor forsvinder $0{,}0007$ næsten helt.

$$12{,}00 + 1{,}234 = 13{,}23$$

$12{,}00$ har kun **2 decimaler**, så selvom $1{,}234$ har 3, kan vi kun beholde 2 decimaler i resultatet.

### Regel 2 — multiplikation og division: tæl **betydende cifre**

Resultatet får lige så mange **betydende cifre** som det tal, der har **færrest betydende cifre**.

**Eksempler:**

$$2{,}2 \cdot 0{,}0442 = 0{,}097 \qquad (2{,}2 \text{ har 2 bet. cifre})$$

$$1{,}234 \cdot 3{,}33 = 4{,}11 \qquad (3{,}33 \text{ har 3 bet. cifre})$$

$$24 \cdot \pi = 75 \qquad (24 \text{ har 2 bet. cifre; } \pi \text{ har uendelig mange})$$

## Gylden regel: rund kun til allersidst

> Regn altid videre med **alle** de cifre, lommeregneren viser, og rund først **det endelige resultat**, så det passer med de målte startværdier.
>
> Runder man undervejs, kan der opstå alvorlige afrundingsfejl.

**Eksempel:** Find kraften $F = m \cdot a$, hvor massen er målt nøjagtigt til $m = 2{,}455 \text{ kg}$, men accelerationen kun til $a = 2 \text{ m/s}^2$ (1 betydende ciffer).

* **Forkert** (rundet for tidligt): $m \approx 2 \text{ kg}$, så $F = 2 \cdot 2 = 4 \text{ N}$.
* **Rigtigt** (rund til sidst): $F = 2{,}455 \cdot 2 = 4{,}91 \text{ N} \approx 5 \text{ N}$ (1 betydende ciffer, fordi $a$ kun har ét).

De to fremgangsmåder giver forskellige svar — derfor: **rund altid først til allersidst.**

---

# Opgaver

## Opgave 1
Bestem volumen af en bog så nøjagtigt som muligt. Angiv, hvilke størrelser du måler, og hvor mange betydende cifre hver størrelse har.

## Opgave 2
Forklar, hvorfor det giver god mening, når din kemilærer siger:

> *"Afmål nøjagtigt ca. 2 g stof."*

## Opgave 3
Skriv følgende tal **uden** 10-tals-potenser:

a) $3{,}4 \cdot 10^{4}$
b) $6{,}2 \cdot 10^{-3}$
c) $4{,}7 \cdot 10^{-6}$

## Opgave 4
Angiv antallet af betydende cifre i følgende værdier:

a) $l = 34{,}502 \text{ m}$

b) $l = 0{,}34502 \text{ m}$

c) $m = 35 \text{ kg}$

d) $m = 7{,}1 \text{ mg}$

e) $t = 0{,}49 \cdot 10^{-3} \text{ s}$

f) $t = 293{,}30 \text{ s}$

## Opgave 5
Angiv arealet af en bordplade med det rette antal betydende cifre, når længden $l$ og bredden $b$ er målt som angivet:

a) $l = 2{,}43 \text{ m}, \quad b = 2{,}56 \text{ m}$

b) $l = 1{,}3 \text{ m}, \quad b = 0{,}5 \text{ m}$

c) $l = 0{,}310 \text{ m}, \quad b = 0{,}743 \text{ m}$
