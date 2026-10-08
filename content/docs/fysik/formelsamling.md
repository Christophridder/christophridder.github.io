---
title: "Formelsamling – Fysik"
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

# Formelsamling – Fysik

**Niveau: Fysik C–A**: Jeg har bygget det op sådan at den første del er til ALLE niveauer. Så kan man springe ned til FysikB og FysikA.  

> **Brug formlerne med omtanke.** En formel er en *model* med et gyldighedsområde.
> Når der står en bemærkning om **gyldighed**(fx "uden luftmodstand" eller "for små
> udsving"), er det en del af formlen – og noget du skal kunne diskutere til eksamen.

---

## Fælles for alle niveauer

### Præfikser (pico til tera)

| Navn | Symbol | Faktor | Eksempel |
|---|---|---|---|
| pico | p | $10^{-12}$ | $1\ \text{pm} = 10^{-12}\ \text{m}$ |
| nano | n | $10^{-9}$ | $1\ \text{nm} = 10^{-9}\ \text{m}$ (synligt lys: 380–750 nm) |
| mikro | µ | $10^{-6}$ | $1\ \text{µm} = 10^{-6}\ \text{m}$ |
| milli | m | $10^{-3}$ | $1\ \text{mm} = 10^{-3}\ \text{m}$ |
| centi | c | $10^{-2}$ | $1\ \text{cm} = 10^{-2}\ \text{m}$ |
| kilo | k | $10^{3}$ | $1\ \text{km} = 10^{3}\ \text{m}$ |
| mega | M | $10^{6}$ | $1\ \text{MJ} = 10^{6}\ \text{J}$ |
| giga | G | $10^{9}$ | $1\ \text{GW} = 10^{9}\ \text{W}$ |
| tera | T | $10^{12}$ | $1\ \text{TWh} = 10^{12}\ \text{Wh}$ |

> **Pas på:** $\text{m}$ betyder både *milli* (foran en enhed) og *meter* (som enhed):
> $1\ \text{mm}$ = 1 millimeter. Og kg er den eneste SI-grundenhed, der allerede har et præfiks.

### Konstanter 

Værdier med ● er **eksakte** (fastlagt ved SI-definitionen fra 2019). De øvrige er målte
værdier, afrundet.

| Navn | Symbol | Værdi | Niveau|
|---|---|---|---|
| Tyngdeacceleration (Danmark) | $g$ | $9{,}82\ \text{m/s}^2 = 9{,}82\ \text{N/kg}$ | C |
| Lysets fart i vakuum ● | $c$ | $2{,}99792458 \cdot 10^{8}\ \text{m/s} \approx 3{,}00 \cdot 10^8\ \text{m/s}$ | C |
| Lydens fart i luft (20 °C) | $v_{\text{lyd}}$ | $343\ \text{m/s}$ | C |
| Plancks konstant ● | $h$ | $6{,}62607015 \cdot 10^{-34}\ \text{J·s} = 4{,}136 \cdot 10^{-15}\ \text{eV·s}$ | C |
| Nyttig kombination | $h \cdot c$ | $1{,}986 \cdot 10^{-25}\ \text{J·m} = 1240\ \text{eV·nm}$ | C |
| Elementarladning ● | $e$ | $1{,}602176634 \cdot 10^{-19}\ \text{C}$ | B |
| Elektronvolt | eV | $1\ \text{eV} = 1{,}602 \cdot 10^{-19}\ \text{J}$ | C |
| Atomar masseenhed | u | $1{,}66054 \cdot 10^{-27}\ \text{kg} \;\hat{=}\; 931{,}494\ \text{MeV}/c^2$ | B |
| Elektronens masse | $m_e$ | $9{,}10938 \cdot 10^{-31}\ \text{kg} = 5{,}486 \cdot 10^{-4}\ \text{u}$ | B |
| Protonens masse | $m_p$ | $1{,}67262 \cdot 10^{-27}\ \text{kg} = 1{,}007276\ \text{u}$ | B |
| Neutronens masse | $m_n$ | $1{,}67493 \cdot 10^{-27}\ \text{kg} = 1{,}008665\ \text{u}$ | B |
| Avogadros tal ● | $N_A$ | $6{,}02214076 \cdot 10^{23}\ \text{mol}^{-1}$ | B |
| Gaskonstanten | $R$ | $8{,}314\ \text{J/(mol·K)} = 8{,}314\ \text{m}^3\text{·Pa/(mol·K)}$ – flere enheder nedenfor | B |
| Boltzmanns konstant ● | $k_B$ | $1{,}380649 \cdot 10^{-23}\ \text{J/K}$ | B |
| Stefan–Boltzmanns konstant | $\sigma$ | $5{,}670 \cdot 10^{-8}\ \text{W/(m}^2\text{·K}^4)$ | B |
| Wiens konstant | $b$ | $2{,}898 \cdot 10^{-3}\ \text{m·K}$ | B |
| Gravitationskonstanten | $G$ | $6{,}674 \cdot 10^{-11}\ \text{N·m}^2/\text{kg}^2$ | A |
| Coulombs konstant | $k_e = \dfrac{1}{4\pi\varepsilon_0}$ | $8{,}988 \cdot 10^{9}\ \text{N·m}^2/\text{C}^2$ | A |
| Vakuumpermittivitet | $\varepsilon_0$ | $8{,}854 \cdot 10^{-12}\ \text{C}^2/(\text{N·m}^2)$ | A |
| Vakuumpermeabilitet | $\mu_0$ | $1{,}2566 \cdot 10^{-6}\ \text{T·m/A} \approx 4\pi \cdot 10^{-7}\ \text{T·m/A}$ | A |

**Gaskonstanten $R$ i forskellige enheder** – vælg den, der passer til enhederne for $p$ og $V$ i $p \cdot V = n \cdot R \cdot T$:

| Værdi af $R$ | Enheder for $p$ og $V$ | Bemærkning |
|---|---|---|
| $8{,}314\ \text{J/(mol·K)} = 8{,}314\ \text{m}^3\text{·Pa/(mol·K)}$ | Pa og m³ | SI; eksakt $8{,}314462618\ldots$ (fordi $R = N_A \cdot k_B$) |
| $8{,}314\ \text{L·kPa/(mol·K)}$ | kPa og L | |
| $0{,}08314\ \text{L·bar/(mol·K)}$ | bar og L | |
| $0{,}08206\ \text{L·atm/(mol·K)}$ | atm og L | |
| $62{,}36\ \text{L·mmHg/(mol·K)}$ | mmHg (torr) og L | 1 mmHg = 133,3 Pa |
| $1{,}987\ \text{cal/(mol·K)}$ | – | energi i kalorier |

**Stof- og astronomiske data**

| Størrelse | Værdi | Niveau|
|---|---|---|
| Absolut nulpunkt | $0\ \text{K} = -273{,}15\ \text{°C}$ | C |
| Normalt lufttryk | $1\ \text{atm} = 101\,325\ \text{Pa} \approx 1{,}013\ \text{bar}$ | B |
| Vands densitet (20 °C) | $998\ \text{kg/m}^3 \approx 1{,}00\ \text{g/mL}$ | C |
| Vands specifikke varmekapacitet | $c_{\text{vand}} = 4180\ \text{J/(kg·K)}$ | C |
| Is' specifikke varmekapacitet | $c_{\text{is}} \approx 2100\ \text{J/(kg·K)}$ | C |
| Vands specifikke smeltevarme | $L_s = 334\ \text{kJ/kg}$ | C |
| Vands specifikke fordampningsvarme (100 °C) | $L_f = 2257\ \text{kJ/kg} \approx 2{,}26\ \text{MJ/kg}$ | C |
| Jordens masse / middelradius | $5{,}972 \cdot 10^{24}\ \text{kg}$ / $6{,}371 \cdot 10^{6}\ \text{m}$ | A |
| Solens masse / radius | $1{,}989 \cdot 10^{30}\ \text{kg}$ / $6{,}957 \cdot 10^{8}\ \text{m}$ | A |
| Solens overfladetemperatur | $\approx 5772\ \text{K}$ | B |
| Solarkonstanten (ved Jorden) | $\approx 1361\ \text{W/m}^2$ | C |
| Astronomisk enhed ● | $1\ \text{AU} = 1{,}495978707 \cdot 10^{11}\ \text{m}$ | C |
| Lysår | $1\ \text{ly} = 9{,}461 \cdot 10^{15}\ \text{m}$ | C |
| Parsec | $1\ \text{pc} = 3{,}086 \cdot 10^{16}\ \text{m} = 3{,}26\ \text{ly}$ | B |
| Hubblekonstanten | $H_0 \approx 70\ \text{km/s/Mpc}$ – se note under B-niveau | B |

### SI-grundenheder

Alle andre enheder kan skrives som produkter af de syv grundenheder.

| Størrelse | Symbol | SI-enhed | Navn |
|---|---|---|---|
| Længde | $l,\ s,\ x,\ h,\ r$ | m | meter |
| Masse | $m$ | kg | kilogram |
| Tid | $t$ | s | sekund |
| Elektrisk strømstyrke | $I$ | A | ampere |
| Temperatur | $T$ | K | kelvin |
| Stofmængde | $n$ | mol | mol |
| Lysstyrke | $I_v$ | cd | candela |

### Afledte størrelser og enheder – skrevet i SI-grundenheder

| Størrelse | Symbol | Enhed | I SI-grundenheder | Niveau |
|---|---|---|---|---|
| Areal / rumfang | $A$ / $V$ | m² / m³ | $\text{m}^2$ / $\text{m}^3$ | C |
| Densitet | $\rho$ | kg/m³ | $\text{kg·m}^{-3}$ | C |
| Hastighed / fart | $v$ | m/s | $\text{m·s}^{-1}$ | C |
| Frekvens | $f$ | Hz (hertz) | $\text{s}^{-1}$ | C |
| Energi, arbejde | $E,\ A$ | J (joule) = N·m | $\text{kg·m}^2\text{·s}^{-2}$ | C |
| Effekt | $P$ | W (watt) = J/s | $\text{kg·m}^2\text{·s}^{-3}$ | C |
| Specifik varmekapacitet | $c$ | J/(kg·K) | $\text{m}^2\text{·s}^{-2}\text{·K}^{-1}$ | C |
| Varmekapacitet | $C$ | J/K | $\text{kg·m}^2\text{·s}^{-2}\text{·K}^{-1}$ | C |
| Brændværdi | $B$ | J/kg | $\text{m}^2\text{·s}^{-2}$ | C |
| Acceleration | $a$ | $\text{m/s}^2$ | $\text{m·s}^{-2}$ | B |
| Kraft | $F$ | N (newton) | $\text{kg·m·s}^{-2}$ | B |
| Tryk | $p$ | Pa (pascal) = $\text{N/m}^2$ | $\text{kg·m}^{-1}\text{·s}^{-2}$ | B |
| Ladning | $Q,\ q$ | C (coulomb) = A·s | $\text{A·s}$ | B |
| Spænding | $U$ | V (volt) = J/C | $\text{kg·m}^2\text{·s}^{-3}\text{·A}^{-1}$ | B |
| Resistans | $R$ | Ω (ohm) = V/A | $\text{kg·m}^2\text{·s}^{-3}\text{·A}^{-2}$ | B |
| Resistivitet | $\rho$ | Ω·m | $\text{kg·m}^3\text{·s}^{-3}\text{·A}^{-2}$ | B |
| Aktivitet | $A$ | Bq (becquerel) = henfald/s | $\text{s}^{-1}$ | B |
| Absorberet dosis | $D$ | Gy (gray) = J/kg | $\text{m}^2\text{·s}^{-2}$ | B |
| Ækvivalent dosis | $H$ | Sv (sievert) = J/kg | $\text{m}^2\text{·s}^{-2}$ | B |
| Bevægelsesmængde, kraftens impuls | $p$, $\Delta p$ | kg·m/s = N·s | $\text{kg·m·s}^{-1}$ | A |
| Vinkelfrekvens | $\omega$ | rad/s | $\text{s}^{-1}$ | A |
| Elektrisk feltstyrke | $E$ | N/C = V/m | $\text{kg·m·s}^{-3}\text{·A}^{-1}$ | A |
| Magnetisk flux­tæthed | $B$ | T (tesla) = N/(A·m) | $\text{kg·s}^{-2}\text{·A}^{-1}$ | A |
| Magnetisk flux | $\Phi$ | Wb (weber) = T·m² | $\text{kg·m}^2\text{·s}^{-2}\text{·A}^{-1}$ | A |
| Kapacitans | $C$ | F (farad) = C/V | $\text{s}^4\text{·A}^2\text{·kg}^{-1}\text{·m}^{-2}$ | A |

> **Samme bogstav – forskellige størrelser.** $A$ er både areal, arbejde, aktivitet og
> amplitude; $C$ er både varmekapacitet, coulomb og kapacitans; $\rho$ er både densitet og
> resistivitet. Skriv altid, hvad dine symboler betyder.

### Andre enheder, du møder – og hvordan de omregnes

| Enhed | Størrelse | Omregning til SI |
|---|---|---|
| kWh (kilowatttime) | energi | $1\ \text{kWh} = 3{,}6 \cdot 10^{6}\ \text{J} = 3{,}6\ \text{MJ}$ |
| eV (elektronvolt) | energi | $1\ \text{eV} = 1{,}602 \cdot 10^{-19}\ \text{J}$ |
| cal (kalorie) | energi | $1\ \text{cal} = 4{,}184\ \text{J}$ (1 kcal på fødevarer = 4,184 kJ) |
| u (atomar masseenhed) | masse | $1\ \text{u} = 1{,}66054 \cdot 10^{-27}\ \text{kg}$ |
| t (ton) | masse | $1\ \text{t} = 1000\ \text{kg}$ |
| km/h | fart | $1\ \text{m/s} = 3{,}6\ \text{km/h}$ – divider km/h med 3,6 |
| min, h, døgn, år | tid | 60 s; 3600 s; 86 400 s; $1\ \text{år} \approx 3{,}156 \cdot 10^{7}\ \text{s}$ |
| °C | temperatur | $T/\text{K} = t/\text{°C} + 273{,}15$. En *forskel* på 1 °C = 1 K |
| L, mL | rumfang | $1\ \text{L} = 1\ \text{dm}^3 = 10^{-3}\ \text{m}^3$; $1\ \text{mL} = 1\ \text{cm}^3$ |
| bar, atm, mmHg | tryk | $1\ \text{bar} = 10^5\ \text{Pa}$; $1\ \text{atm} = 101\,325\ \text{Pa}$; $1\ \text{mmHg} = 133{,}3\ \text{Pa}$ |
| g/mL | densitet | $1\ \text{g/mL} = 1\ \text{g/cm}^3 = 1000\ \text{kg/m}^3$ |
| mAh | ladning | $1\ \text{mAh} = 3{,}6\ \text{C}$ |
| AU, ly, pc | længde | se tabellen over astronomiske data |

### Amerikanske og britiske enheder

Siden 1959 er de fleste defineret **eksakt** ud fra SI-enheder (markeret med ●).

| Enhed | Størrelse | Omregning til SI | Bemærkning |
|---|---|---|---|
| inch (in, ″) ● | længde | $1\ \text{in} = 2{,}54\ \text{cm}$ | skærme, fælge, rør |
| foot (ft, ′) ● | længde | $1\ \text{ft} = 12\ \text{in} = 0{,}3048\ \text{m}$ | flyvehøjde |
| yard (yd) ● | længde | $1\ \text{yd} = 3\ \text{ft} = 0{,}9144\ \text{m}$ | |
| mile (mi) ● | længde | $1\ \text{mi} = 1760\ \text{yd} = 1609{,}344\ \text{m}$ | |
| sømil (nautical mile, NM) ● | længde | $1\ \text{NM} = 1852\ \text{m}$ | international; ≈ 1 bueminut på en længdegrad |
| knob (kn) | fart | $1\ \text{kn} = 1\ \text{NM/h} = 0{,}5144\ \text{m/s}$ | skibe og fly |
| mph ● | fart | $1\ \text{mph} = 0{,}44704\ \text{m/s} = 1{,}609\ \text{km/h}$ | |
| acre | areal | $1\ \text{acre} = 4047\ \text{m}^2$ | |
| US gallon (gal) ● | rumfang | $1\ \text{gal} = 3{,}785\ \text{L}$ | **UK-gallon er større:** $4{,}546\ \text{L}$ |
| US fluid ounce (fl oz) | rumfang | $1\ \text{fl oz} = 29{,}57\ \text{mL}$ | UK fl oz = 28,41 mL |
| cup (US) | rumfang | $\approx 237\ \text{mL}$ | på næringsdeklarationer bruges 240 mL |
| barrel (olie, bbl) ● | rumfang | $1\ \text{bbl} = 42\ \text{gal} = 159{,}0\ \text{L}$ | oliepriser |
| pound (lb) ● | masse | $1\ \text{lb} = 0{,}45359237\ \text{kg}$ | |
| ounce (oz) ● | masse | $1\ \text{oz} = \tfrac{1}{16}\ \text{lb} = 28{,}35\ \text{g}$ | |
| short ton (US) ● | masse | $1\ \text{ton} = 2000\ \text{lb} = 907{,}2\ \text{kg}$ | UK long ton = 1016 kg; metrisk ton = 1000 kg |
| stone (UK) ● | masse | $1\ \text{st} = 14\ \text{lb} = 6{,}350\ \text{kg}$ | kropsvægt i Storbritannien |
| pound-force (lbf) | kraft | $1\ \text{lbf} = 4{,}448\ \text{N}$ | |
| psi (lbf/in²) | tryk | $1\ \text{psi} = 6895\ \text{Pa} \approx 0{,}0690\ \text{bar}$ | dæktryk |
| grader Fahrenheit (°F) | temperatur | $t_F = 1{,}8 \cdot t_C + 32$, $\ t_C = \dfrac{t_F - 32}{1{,}8}$ | $0\ \text{°C} = 32\ \text{°F}$, $100\ \text{°C} = 212\ \text{°F}$; $-40\ \text{°C} = -40\ \text{°F}$ |
| BTU | energi | $1\ \text{BTU} \approx 1055\ \text{J}$ | varmepumper, aircondition; definitionen varierer (1054–1060 J) |
| foot-pound (ft·lbf) | energi, arbejde | $1\ \text{ft·lbf} = 1{,}356\ \text{J}$ | |
| horsepower (hp) | effekt | $1\ \text{hp} = 745{,}7\ \text{W}$ | **metrisk hestekraft (hk, PS) er 735,5 W** |
| mpg (miles per US gallon) | brændstofforbrug | $1\ \text{mpg} = 0{,}4251\ \text{km/L}$ | $\text{L/100 km} = \dfrac{235{,}2}{\text{mpg}}$ |

Eksempel: En amerikansk bil kører 30 mpg: $30 \cdot 0{,}4251 = 12{,}8\ \text{km/L}$, dvs. $\dfrac{235{,}2}{30} = 7{,}8\ \text{L/100 km}$.

---

## C-niveau

### Grundstørrelser i energiregning

| Størrelse | Symbol | Enhed | Formel / eksempel |
|---|---|---|---|
| Masse | $m$ | kg | $m = 10\ \text{kg}$ |
| Tid | $t$ | s | $t = 15\ \text{s}$ |
| Temperatur | $T$ (K), $t$ (°C) | K, °C | $8\ \text{°C} = 281\ \text{K}$ |
| Energi | $E$ | J | $E = P \cdot t$, fx $E = 2{,}7 \cdot 10^{6}\ \text{J} = 2{,}7\ \text{MJ}$ |
| Effekt | $P$ | W = J/s | $P = \dfrac{E}{t}$, fx $P = 40\ \text{W}$ |
| Nyttevirkning | $\eta$ | ingen (angives ofte i %) | $\eta = \dfrac{E_{\text{nyttig}}}{E_{\text{tilført}}} = \dfrac{P_{\text{nyttig}}}{P_{\text{tilført}}}$ |
| Densitet | $\rho$ | kg/m³ eller g/mL | $\rho = \dfrac{m}{V}$, fx $\rho = \dfrac{50{,}0\ \text{g}}{18{,}5\ \text{mL}} = 2{,}70\ \text{g/mL}$ (aluminium) |

### Energiformler

| Størrelse | Enhed | Formel | Eksempel |
|---|---|---|---|
| Potentiel energi $E_{\text{pot}}$ | J | $E_{\text{pot}} = m \cdot g \cdot h$ | $1{,}0\ \text{kg} \cdot 9{,}82\ \tfrac{\text{m}}{\text{s}^2} \cdot 3{,}5\ \text{m} = 34\ \text{J}$ |
| Kinetisk energi $E_{\text{kin}}$ | J | $E_{\text{kin}} = \tfrac{1}{2} \cdot m \cdot v^2$ | $\tfrac{1}{2} \cdot 2{,}0\ \text{kg} \cdot (3{,}0\ \tfrac{\text{m}}{\text{s}})^2 = 9{,}0\ \text{J}$ |
| Mekanisk energi $E_{\text{mek}}$ | J | $E_{\text{mek}} = E_{\text{kin}} + E_{\text{pot}}$ | $2000\ \text{J} + 1000\ \text{J} = 3{,}0\ \text{kJ}$ |
| Tyngdekraftens arbejde $A_{\text{tyngde}}$ | J | $A_{\text{tyngde}} = m \cdot g \cdot h$ (når legemet falder højden $h$) | $0{,}50\ \text{kg} \cdot 9{,}82\ \tfrac{\text{m}}{\text{s}^2} \cdot 10\ \text{m} = 49\ \text{J}$ |
| Effekt $P$ | W | $P = \dfrac{E}{t}$ | $\dfrac{2000\ \text{J}}{60\ \text{s}} = 33\ \text{W}$ |
| Termisk energi $E_{\text{term}}$ | J | $E_{\text{term}} = m \cdot c \cdot \Delta T$ | $1{,}000\ \text{kg} \cdot 4180\ \tfrac{\text{J}}{\text{kg·K}} \cdot 80{,}00\ \text{K} = 334{,}4\ \text{kJ}$ |
| Varmekapacitet $C$ | J/K | $C = m \cdot c$, og $E = C \cdot \Delta T$ | kalorimeter: $C = 200\ \tfrac{\text{J}}{\text{K}}$ |
| Specifik varmekapacitet $c$ | J/(kg·K) | $c = \dfrac{E}{m \cdot \Delta T}$ | $c_{\text{vand}} = 4180\ \tfrac{\text{J}}{\text{kg·K}}$ |
| Smeltning / størkning | J | $E = m \cdot L_s$ | $0{,}50\ \text{kg} \cdot 334\ \tfrac{\text{kJ}}{\text{kg}} = 167\ \text{kJ}$ |
| Fordampning / fortætning | J | $E = m \cdot L_f$ | $0{,}10\ \text{kg} \cdot 2257\ \tfrac{\text{kJ}}{\text{kg}} = 226\ \text{kJ}$ |
| Kemisk energi (brændværdi $B$) | J | $E_{\text{kem}} = B \cdot m$ | $43\ \tfrac{\text{MJ}}{\text{kg}} \cdot 2{,}0\ \text{kg} = 86\ \text{MJ}$ (benzin) |
| Elektrisk energi $E_{\text{el}}$ | J | $E_{\text{el}} = U \cdot I \cdot t$, $P = U \cdot I$ | $230\ \text{V} \cdot 2{,}0\ \text{A} \cdot 60\ \text{s} = 27{,}6\ \text{kJ}$ |
| Nyttevirkning $\eta$ | – | $\eta = \dfrac{E_{\text{nyttig}}}{E_{\text{tilført}}}$ | $\dfrac{334{,}4\ \text{kJ}}{2000\ \text{W} \cdot 200\ \text{s}} = 0{,}84 = 84\ \%$ |

> **Gyldighed og faldgruber**
> - $E_{\text{pot}} = m \cdot g \cdot h$ gælder **nær jordoverfladen**, hvor $g$ er konstant. $h$ måles fra et nulpunkt, du selv vælger.
> - $E_{\text{term}} = m \cdot c \cdot \Delta T$ gælder kun, **så længe stoffet ikke skifter tilstandsform** (og $c$ er ca. konstant). Ved smeltning/fordampning bruges $E = m \cdot L$.
> - Brændværdier varierer mellem kilder (nedre/øvre brændværdi, blandingens sammensætning). For benzin angives typisk 42–44 MJ/kg.
> - $\eta$ kan aldrig blive over 1 (100 %). Får du det, er der en fejl i målingen eller regningen.

![Energistrøm og nyttevirkning](/images/formelsamling/nyttevirkning.svg)

### Energiformer

| Energiform | Formel | Forklaring |
|---|---|---|
| Potentiel energi | $E_{\text{pot}} = m \cdot g \cdot h$ | Energi pga. placering i tyngdefeltet. $m$ er massen i kg, $g = 9{,}82\ \text{m/s}^2$, $h$ er højden over nulpunktet i m. |
| Kinetisk energi | $E_{\text{kin}} = \tfrac{1}{2} \cdot m \cdot v^2$ | Bevægelsesenergi. $m$ i kg, $v$ er farten i m/s. |
| Mekanisk energi | $E_{\text{mek}} = \tfrac{1}{2} m v^2 + m g h$ | Summen af kinetisk og potentiel energi. Fx et barn på en gynge: I vendepunkterne er energien potentiel, i bunden kinetisk. Uden gnidning og luftmodstand er $E_{\text{mek}}$ **bevaret**. |
| Termisk energi | $E_{\text{term}} = m \cdot c \cdot \Delta T$ | Den indre energi i et stof, der hænger sammen med molekylernes uordnede bevægelse (temperaturen). Næsten alle energiomsætninger ender – helt eller delvist – som termisk energi. |
| Kemisk energi | $E_{\text{kem}} = B \cdot m$ | Energi bundet i kemiske bindinger, som frigives fx ved forbrænding af mad, træ eller benzin. |
| Elektrisk energi | $E_{\text{el}} = U \cdot I \cdot t$ | Energi, der transporteres af en elektrisk strøm. |
| Strålingsenergi | $E_{\text{foton}} = h \cdot f$ | Energi, der transporteres af elektromagnetisk stråling (fotoner), fx sollys, som planterne bruger til fotosyntese. (α- og β-stråling er *partikelstråling* – her er energien partiklernes kinetiske energi.) |
| Kerneenergi | $E = \Delta m \cdot c^2$  | Energi frigivet ved **kernereaktioner**: fission (spaltning af fx U-235 i et kernekraftværk), fusion (i Solen) og radioaktive henfald. Energien bliver til kinetisk energi af partiklerne → termisk energi → fx damp, der driver en turbine. |

> **Energibevarelse:** Energi kan hverken skabes eller forsvinde – kun omdannes fra én
> form til en anden: $E_{\text{før}} = E_{\text{efter}}$.

### Bølger

![Bølge med bølgelængde og amplitude](/images/formelsamling/boelge.svg)

| Størrelse | Symbol | Enhed | Formel |
|---|---|---|---|
| Bølgelængde | $\lambda$ | m | afstand mellem to toppe (eller to dale) |
| Periode (svingningstid) | $T$ | s | $T = \dfrac{1}{f}$ |
| Frekvens | $f$ | Hz = 1/s | $f = \dfrac{1}{T}$ |
| Udbredelsesfart | $v$ | m/s | $v = \lambda \cdot f = \dfrac{\lambda}{T}$ |
| Amplitude | $A$ | m (eller Pa for lyd) | største udsving fra ligevægt |
| Lysets fart | $c$ | m/s | $c = \lambda \cdot f$, $\ c = 3{,}00 \cdot 10^8\ \text{m/s}$ |
| Fotonens energi | $E_{\text{foton}}$ | J eller eV | $E = h \cdot f = \dfrac{h \cdot c}{\lambda}$ |
| – i praksis | $E_{\text{foton}}$ | eV | $E \approx \dfrac{1240\ \text{eV·nm}}{\lambda}$ |
| Emission/absorption | $E_{\text{foton}}$ | eV | $E_{\text{foton}} = E_{\text{høj}} - E_{\text{lav}}$ (forskel mellem to energiniveauer) |
| Intensitet | $I$ | W/m² | $I = \dfrac{P}{4\pi r^2}$ (punktkilde → afstandskvadratloven) |
| Lydintensitetsniveau | $L$ | dB | $L = 10 \cdot \log\!\left(\dfrac{I}{I_0}\right)$, $\ I_0 = 10^{-12}\ \text{W/m}^2$ |

**Regneeksempler**

- Tonen A (440 Hz) i luft: $\lambda = \dfrac{v}{f} = \dfrac{343\ \text{m/s}}{440\ \text{Hz}} = 0{,}780\ \text{m}$
- Rødt lys, 650 nm: $f = \dfrac{c}{\lambda} = \dfrac{3{,}00 \cdot 10^8\ \text{m/s}}{650 \cdot 10^{-9}\ \text{m}} = 4{,}62 \cdot 10^{14}\ \text{Hz}$ og $E = \dfrac{1240}{650}\ \text{eV} = 1{,}91\ \text{eV}$
- +10 dB svarer til 10 gange så stor intensitet; +3 dB til ca. dobbelt så stor.

**Stående bølger (streng og rør)** – $n = 1$ er grundtonen, $n = 2, 3, \ldots$ er overtonerne.

| System | Betingelse | Frekvenser |
|---|---|---|
| Streng, fast i begge ender | $L = n \cdot \dfrac{\lambda}{2}$ | $f_n = n \cdot \dfrac{v}{2L}$, $\ n = 1, 2, 3, \ldots$ |
| Rør, åbent i begge ender | $L = n \cdot \dfrac{\lambda}{2}$ | $f_n = n \cdot \dfrac{v}{2L}$, $\ n = 1, 2, 3, \ldots$ |
| Rør, lukket i den ene ende | $L = n \cdot \dfrac{\lambda}{4}$ | $f_n = n \cdot \dfrac{v}{4L}$, $\ n = 1, 3, 5, \ldots$ (kun ulige) |

![Stående bølger på en streng](/images/formelsamling/staaende_boelger.svg)

> **Gyldighed:** For rør ligger "bugen" ved en åben ende lidt *uden for* røret
> (endekorrektion ≈ 0,6 · rørets radius pr. åben ende), så de målte frekvenser er lidt
> lavere end modellen forudsiger.

**Gitterligningen**

$$d \cdot \sin\theta_n = n \cdot \lambda \qquad d = \frac{1}{\text{antal spalter pr. meter}} \qquad \tan\theta_n = \frac{x_n}{L}$$

Eksempel: gitter med 600 streger/mm → $d = 1{,}67 \cdot 10^{-6}\ \text{m}$. Med $\lambda = 650\ \text{nm}$:
$\sin\theta_1 = \dfrac{650 \cdot 10^{-9}}{1{,}67 \cdot 10^{-6}} = 0{,}390$, så $\theta_1 = 23{,}0°$.
Brug **ikke** tilnærmelsen $\sin\theta \approx \tan\theta$, når vinklen er stor.

![Gitter](/images/formelsamling/gitter.svg)

**Det elektromagnetiske spektrum**

![Det elektromagnetiske spektrum](/images/formelsamling/em_spektrum.svg)

| Område | Bølgelængde (ca.) | Eksempel |
|---|---|---|
| γ-stråling | < 10 pm | radioaktive henfald |
| Røntgen | 10 pm – 10 nm | røntgenbilleder |
| UV | 10 nm – 380 nm | solbrænding |
| Synligt lys | 380 nm (violet) – 750 nm (rød) | øjet |
| Infrarød (IR) | 750 nm – 1 mm | varmestråling, fjernbetjening |
| Mikrobølger | 1 mm – 1 m | mikroovn (12 cm), wifi |
| Radiobølger | > 1 m | FM-radio (ca. 3 m) |

> Grænserne mellem områderne er **konventioner**, ikke skarpe fysiske grænser – kilder
> angiver fx synligt lys som 380–750 nm, 380–780 nm eller 400–700 nm.

### Store navne i fysikkens historie – fra Aristoteles til Einstein

| Navn | Levede | Største bedrift |
|---|---|---|
| Aristoteles | 384–322 f.Kr. | Geocentrisk verdensbillede med Jorden i centrum; fire elementer; "tunge ting falder hurtigere" (forkert – men ikke rettet før Galilei). |
| Aristarchos fra Samos | ca. 310–230 f.Kr. | Første kendte forslag om et **heliocentrisk** verdensbillede. |
| Archimedes | ca. 287–212 f.Kr. | **Archimedes' lov** (opdrift) og vægtstangsloven. |
| Eratosthenes | ca. 276–194 f.Kr. | Målte **Jordens omkreds** ud fra skyggevinkler i Syene og Alexandria. |
| Ptolemæus | ca. 100–170 e.Kr. | *Almagest*: geocentrisk model med **epicykler**, der kunne forudsige planeternes baner. Brugt i ca. 1400 år. |
| Nikolaus Kopernikus | 1473–1543 | **Heliocentrisk** verdensbillede (*De revolutionibus*, 1543). |
| Tycho Brahe | 1546–1601 | De mest præcise **observationer uden kikkert** (Uraniborg på Hven); supernovaen 1572 viste, at himlen ikke er uforanderlig. |
| Galileo Galilei | 1564–1642 | **Kikkerten** mod himlen (1609–10: Jupiters måner, Venus' faser) og **eksperimentet** som metode (faldbevægelse på skråplan, inerti). |
| Johannes Kepler | 1571–1630 | **Keplers tre love** (1609 og 1619): planeterne bevæger sig i ellipser – bygget på Tychos data. |
| Christiaan Huygens | 1629–1695 | **Bølgeteori for lys**; pendulur. |
| Isaac Newton | 1643–1727 ¹ | *Principia* (1687): **Newtons tre love** og **gravitationsloven** – samme fysik på Jorden og i himlen. |
| Ole Rømer | 1644–1710 | Viste i 1676, at **lysets fart er endelig** (ud fra Jupitermånen Io). |
| H.C. Ørsted | 1777–1851 | Opdagede **elektromagnetismen** i 1820: en strøm påvirker en kompasnål. |
| Michael Faraday | 1791–1867 | **Induktion** (1831) – grundlaget for generatoren og transformeren. |
| James Clerk Maxwell | 1831–1879 | **Maxwells ligninger** (1865): lys er en elektromagnetisk bølge. |
| Max Planck | 1858–1947 | **Kvantehypotesen** (1900): $E = h \cdot f$. |
| Marie Curie | 1867–1934 | Forskning i **radioaktivitet**; opdagede polonium og radium (1898). Nobelpris i både fysik (1903) og kemi (1911). |
| Ernest Rutherford | 1871–1937 | Opdagede **atomkernen** (1911, guldfolieforsøget). |
| Albert Einstein | 1879–1955 | 1905: **speciel relativitetsteori**, $E = mc^2$ og **fotoelektrisk effekt** (fotoner). 1915: **generel relativitetsteori**. |
| Niels Bohr | 1885–1962 | **Bohrs atommodel** (1913): elektroner i bestemte energiniveauer → linjespektre. |

¹ **Newtons fødsels- og dødsår afhænger af kalenderen.** England brugte stadig den
julianske kalender: født 25. december **1642** (juliansk) = 4. januar **1643** (gregoriansk);
død 20. marts 1726 (juliansk, med årsskifte 25. marts) = 31. marts **1727** (gregoriansk).
Begge angivelser er korrekte – de refererer bare til hver sin kalender.

![Tidslinje over fysikkens store navne](/images/formelsamling/tidslinje.svg)

---

## B-niveau

### Kinematik i 1D

| Størrelse | Formel | Bemærkning |
|---|---|---|
| (Gennemsnits)hastighed | $v = \dfrac{\Delta s}{\Delta t}$ | hældningen på en $(t, s)$-graf |
| (Gennemsnits)acceleration | $a = \dfrac{\Delta v}{\Delta t}$ | hældningen på en $(t, v)$-graf |
| Tilbagelagt strækning | $\Delta s$ = arealet under $(t, v)$-grafen | |
| Konstant hastighed | $s = s_0 + v \cdot t$ | |
| Konstant acceleration | $v = v_0 + a \cdot t$ | |
| | $s = s_0 + v_0 \cdot t + \tfrac{1}{2} \cdot a \cdot t^2$ | |
| | $v^2 - v_0^2 = 2 \cdot a \cdot (s - s_0)$ | tiden er elimineret |
| Frit fald | $a = g = 9{,}82\ \text{m/s}^2$ (nedad) | **uden luftmodstand** |

Eksempel: En bil accelererer fra 0 til 100 km/h $= 27{,}8\ \text{m/s}$ på 10 s:
$a = \dfrac{27{,}8\ \text{m/s}}{10\ \text{s}} = 2{,}8\ \text{m/s}^2$.

### Kræfter og Newtons love

| Lov / kraft | Formel | Bemærkning |
|---|---|---|
| Newtons 1. lov | $F_{\text{res}} = 0 \Leftrightarrow v$ konstant | inertiens lov |
| Newtons 2. lov | $F_{\text{res}} = m \cdot a$ | fx $10\ \text{kg} \cdot 5{,}0\ \tfrac{\text{m}}{\text{s}^2} = 50\ \text{N}$ |
| Newtons 3. lov | $F_{A \to B} = -F_{B \to A}$ | kraft og reaktion virker på **hver sit** legeme |
| Tyngdekraft | $F_{\text{tyngde}} = m \cdot g$ | $10\ \text{kg} \cdot 9{,}82\ \tfrac{\text{N}}{\text{kg}} = 98{,}2\ \text{N}$ |
| Normalkraft, vandret underlag | $F_N = m \cdot g$ | kun når ingen andre kræfter virker lodret |
| Normalkraft, skråplan | $F_N = m \cdot g \cdot \cos\theta$ | |
| Tyngdekraftens komposant langs skråplan | $F_{\parallel} = m \cdot g \cdot \sin\theta$ | |
| Gnidning, glidende (dynamisk) | $F_k = \mu_k \cdot F_N$ | $\mu_k$: dynamisk gnidningskoefficient |
| Gnidning, hvilende (statisk) | $F_s \le \mu_s \cdot F_N$ | legemet begynder at glide ved $\tan\theta_c = \mu_s$ |
| Arbejde | $A = F \cdot s \cdot \cos v$ | $v$ = vinkel mellem kraft og flytning; $A = F \cdot s$ når de er parallelle |
| Arbejdssætningen | $A_{\text{res}} = \Delta E_{\text{kin}}$ | |
| Effekt ved konstant fart | $P = F \cdot v$ | |

Eksempel (skråplan, $m = 2{,}0\ \text{kg}$, $\theta = 30°$):
$F_{\parallel} = 2{,}0 \cdot 9{,}82 \cdot \sin 30° = 9{,}8\ \text{N}$ og
$F_N = 2{,}0 \cdot 9{,}82 \cdot \cos 30° = 17\ \text{N}$.

![Kræfter på et skråplan](/images/formelsamling/skraaplan.svg)

> Gnidningsloven $F = \mu \cdot F_N$ er en **empirisk model**: $\mu$ afhænger af begge
> overflader og er kun tilnærmelsesvis uafhængig af fart og kontaktareal.

### Energi i tyngdefeltet

$$E_{\text{mek}} = \tfrac{1}{2} m v_1^2 + m g h_1 = \tfrac{1}{2} m v_2^2 + m g h_2 \qquad \text{(uden gnidning og luftmodstand)}$$

Frit fald fra højden $h$ fra hvile: $v = \sqrt{2 \cdot g \cdot h}$, fx $h = 5{,}0\ \text{m} \Rightarrow v = 9{,}9\ \text{m/s}$.
Med gnidning: $\Delta E_{\text{mek}} = -F_{\text{gnid}} \cdot s$ (energien bliver til termisk energi).

### Tryk, opdrift og gasser

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Tryk | $p = \dfrac{F}{A}$ | $1\ \text{Pa} = 1\ \text{N/m}^2$ |
| Tryk i en væske | $p = p_0 + \rho \cdot g \cdot h$ | $h$ = dybde; 10 m vand giver ca. +1 atm |
| Archimedes' lov | $F_{\text{op}} = \rho_{\text{væske}} \cdot V_{\text{fortrængt}} \cdot g$ | opdrift = tyngden af den fortrængte væske |
| Absolut temperatur | $T = t + 273{,}15$ | gaslovene kræver **kelvin** |
| Idealgasligningen | $p \cdot V = n \cdot R \cdot T$ | også $p \cdot V = N \cdot k_B \cdot T$ |
| Boyle–Mariottes lov ($T$, $n$ konst.) | $p_1 \cdot V_1 = p_2 \cdot V_2$ | |
| $p$, $n$ konstant ² | $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$ | |
| $V$, $n$ konstant ² | $\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}$ | |
| Gasmolekylers kinetiske energi | $\overline{E}_{\text{kin}} = \tfrac{3}{2} \cdot k_B \cdot T$ | én-atomig idealgas |

² **Navnene varierer mellem lærebøger:** $V/T$ = konstant kaldes både *Charles' lov* og
*Gay-Lussacs (1.) lov*; $p/T$ = konstant kaldes både *Gay-Lussacs (2.) lov* og
*Amontons' lov*. Skriv derfor altid, hvilken størrelse der holdes konstant.

Eksempler:
- En sten med $V = 0{,}50\ \text{L}$ helt under vand: $F_{\text{op}} = 1{,}00 \cdot 10^3 \cdot 5{,}0 \cdot 10^{-4} \cdot 9{,}82 = 4{,}9\ \text{N}$.
- 1,00 mol gas ved 20 °C og 1 atm: $V = \dfrac{nRT}{p} = \dfrac{1{,}00 \cdot 8{,}314 \cdot 293{,}15}{101\,325}\ \text{m}^3 = 24{,}1\ \text{L}$.

![Archimedes' lov](/images/formelsamling/archimedes.svg)

![Gaslovene](/images/formelsamling/gaslove.svg)

> **Idealgasmodellen** gælder godt ved lave tryk og høje temperaturer (langt fra
> kondensation). Ekstrapoleres $V$–$T$- eller $p$–$T$-linjen, rammer den 0 ved
> $-273{,}15\ \text{°C}$ – det absolutte nulpunkt. En rigtig gas bliver flydende længe før.

### Elektriske kredsløb

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Strømstyrke | $I = \dfrac{Q}{t}$ | $1\ \text{A} = 1\ \text{C/s}$ |
| Spændingsfald | $U = \dfrac{E}{Q}$ | $1\ \text{V} = 1\ \text{J/C}$ |
| Resistans (Ohms lov) | $U = R \cdot I$ | $R$ konstant kun for en **ohmsk** komponent (ikke fx glødepære eller diode) |
| Resistivitet | $R = \rho \cdot \dfrac{L}{A}$ | $\rho_{\text{kobber}} = 1{,}7 \cdot 10^{-8}\ \Omega\text{·m}$ (20 °C) |
| Effekt | $P = U \cdot I = R \cdot I^2 = \dfrac{U^2}{R}$ | |
| Energi | $E = P \cdot t = U \cdot I \cdot t$ | |
| Serieforbindelse | $R = R_1 + R_2 + \ldots$ | samme $I$; spændingerne lægges sammen |
| Parallelforbindelse | $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \ldots$ | samme $U$; strømmene lægges sammen |
| Kirchhoffs 1. lov (knudepunkt) | $\sum I_{\text{ind}} = \sum I_{\text{ud}}$ | ladning er bevaret |
| Kirchhoffs 2. lov (maske) | $\sum U = 0$ rundt i en lukket sløjfe | energi er bevaret |
| Polspænding | $U_{\text{pol}} = U_0 - R_i \cdot I$ | $U_0$: elektromotorisk kraft, $R_i$: indre resistans |
| Ohms 2. lov | $I = \dfrac{U_0}{R_y + R_i}$ | $R_y$: ydre resistans |
| Spændingsdeler (sensor) | $U_2 = U \cdot \dfrac{R_2}{R_1 + R_2}$ | fx med NTC-termistor eller LDR som $R_2$ |

Eksempler: $100\ \Omega$ og $220\ \Omega$ i serie giver $320\ \Omega$; parallelt giver de
$\left(\tfrac{1}{100} + \tfrac{1}{220}\right)^{-1}\ \Omega = 69\ \Omega$ – altid **mindre** end den mindste.
Et batteri med $U_0 = 9{,}0\ \text{V}$ og $R_i = 0{,}50\ \Omega$ leverer $I = 2{,}0\ \text{A}$: $U_{\text{pol}} = 9{,}0 - 0{,}50 \cdot 2{,}0 = 8{,}0\ \text{V}$.

![Serie- og parallelforbindelse](/images/formelsamling/kredsloeb.svg)

### Atomfysik og spektre

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Kernens opbygning | $^{A}_{Z}\text{X}$, $\ A = Z + N$ | $A$: nukleontal, $Z$: protontal (atomnummer), $N$: neutrontal |
| Fotonenergi | $E = h \cdot f = \dfrac{h \cdot c}{\lambda}$ | |
| Emission / absorption | $E_{\text{foton}} = E_m - E_n$ | fotonen har præcis forskellen mellem to niveauer |
| Hydrogens energiniveauer | $E_n = -\dfrac{13{,}6\ \text{eV}}{n^2}$ | Bohr-modellen – gælder kun for hydrogen(lignende) atomer |
| Wiens forskydningslov | $\lambda_{\max} \cdot T = 2{,}898 \cdot 10^{-3}\ \text{m·K}$ | sort legeme; Solen: $\lambda_{\max} \approx 502\ \text{nm}$ |
| Stefan–Boltzmanns lov | $P = \sigma \cdot A \cdot T^4$ | stjerne: $L = 4\pi R^2 \cdot \sigma \cdot T^4$ |

![Hydrogens energiniveauer](/images/formelsamling/energiniveauer.svg)

### Radioaktivitet og kernefysik

| Størrelse | Formel | Bemærkning |
|---|---|---|
| α-henfald | $^{A}_{Z}\text{X} \rightarrow {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}$ | |
| β⁻-henfald | $^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}$ | en neutron bliver til en proton |
| β⁺-henfald | $^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z-1}\text{Y} + {}^{0}_{+1}\text{e} + \nu$ | en proton bliver til en neutron |
| γ-henfald | $^{A}_{Z}\text{X}^{*} \rightarrow {}^{A}_{Z}\text{X} + \gamma$ | exciteret kerne udsender en foton |
| Aktivitet | $A = k \cdot N$ | $k$: henfaldskonstant (s⁻¹), $N$: antal kerner |
| Henfaldsloven | $N(t) = N_0 \cdot e^{-k \cdot t} = N_0 \cdot \left(\tfrac{1}{2}\right)^{t/T_{½}}$ | tilsvarende $A(t) = A_0 \cdot \left(\tfrac{1}{2}\right)^{t/T_{½}}$ |
| Halveringstid | $T_{½} = \dfrac{\ln 2}{k}$ | |
| Halveringstykkelse | $I(x) = I_0 \cdot \left(\tfrac{1}{2}\right)^{x/x_{½}}$ | γ-stråling gennem et materiale |
| Afstandskvadratloven | $I_1 \cdot r_1^2 = I_2 \cdot r_2^2$ | punktkilde, uden absorption |
| Absorberet dosis | $D = \dfrac{E}{m}$ | Gy |
| Ækvivalent dosis | $H = w_R \cdot D$ | Sv; $w_R = 1$ for β og γ, $w_R = 20$ for α |
| Masse-energi-ækvivalens | $E = m \cdot c^2$ | $1\ \text{u} \cdot c^2 = 931{,}494\ \text{MeV}$ |
| Q-værdi | $Q = (m_{\text{før}} - m_{\text{efter}}) \cdot c^2$ | $Q > 0$: energi frigives |
| Bindingsenergi | $E_B = (Z \cdot m_{\text{H}} + N \cdot m_n - m_{\text{atom}}) \cdot c^2$ | med atommasser; $m_{\text{H}} = 1{,}007825\ \text{u}$ |

Eksempler:
- I-131 ($T_{½} = 8{,}02$ døgn): efter 24 døgn er der $\left(\tfrac{1}{2}\right)^{24/8{,}02} = 0{,}126 = 12{,}6\ \%$ tilbage.
- α-henfald af Ra-226: $Q = (226{,}025410 - 222{,}017578 - 4{,}002603)\ \text{u} \cdot 931{,}494\ \tfrac{\text{MeV}}{\text{u}} = 4{,}87\ \text{MeV}$.
- He-4: $E_B = (2 \cdot 1{,}007825 + 2 \cdot 1{,}008665 - 4{,}002603)\ \text{u} \cdot c^2 = 28{,}3\ \text{MeV}$, dvs. 7,07 MeV pr. nukleon.

> **Pas på med Q-værdier og atommasser:** Ved α- og β⁻-henfald går elektronerne "lige op",
> når man bruger atommasser. Ved β⁺-henfald skal man trække $2 \cdot m_e$ fra ekstra.

![Henfaldsloven](/images/formelsamling/henfald.svg)

### Bølger: interferens

| Forstærkning (konstruktiv) | Udslukning (destruktiv) |
|---|---|
| vejlængdeforskel $\Delta s = n \cdot \lambda$ | vejlængdeforskel $\Delta s = \left(n + \tfrac{1}{2}\right) \cdot \lambda$ |

Gitterligningen $d \cdot \sin\theta_n = n \cdot \lambda$ (se C-niveau) er netop betingelsen for
forstærkning fra alle spalter.

### Universets udvidelse

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Rødforskydning | $z = \dfrac{\lambda_{\text{obs}} - \lambda_0}{\lambda_0}$ | |
| Fart (Doppler-tilnærmelse) | $v \approx z \cdot c$ | kun for $v \ll c$ ($z \lesssim 0{,}1$) |
| Hubbles lov | $v = H_0 \cdot d$ | |
| Universets alder (overslag) | $t \approx \dfrac{1}{H_0} \approx 14 \cdot 10^9\ \text{år}$ | ved $H_0 = 70\ \text{km/s/Mpc}$ |

Eksempel: En galakse med $z = 0{,}010$ har $v = 3000\ \text{km/s}$ og ligger i afstanden
$d = \dfrac{3000}{70}\ \text{Mpc} = 43\ \text{Mpc}$.

> **Hubblekonstanten er ikke kendt præcist.** To metoder giver forskellige værdier
> ("Hubble-spændingen"): kosmisk baggrundsstråling (Planck) giver $H_0 \approx 67{,}4$,
> mens afstandsstigen med supernovaer (SH0ES) giver $H_0 \approx 73\ \text{km/s/Mpc}$.
> $70$ er et rundt tal midt imellem. Estimatet $t \approx 1/H_0$ antager konstant udvidelseshastighed.

---

## A-niveau

### Areal og enhed

Arealet under en graf har enheden **y-enhed gange x-enhed**. Det er sådan, du finder enheden på en integreret størrelse:

| y-akse | x-akse | Integral | Arealet er | Enhed |
|---|---|---|---|---|
| $F$ (N) | $t$ (s) | $\Delta p = \int F\,\mathrm{d}t$ | kraftens impuls $\Delta p$ | N·s (= kg·m/s) |
| $v$ (m/s) | $t$ (s) | $s = \int v\,\mathrm{d}t$ | strækning $s$ | m/s · s = m |
| $F$ (N) | $s$ eller $x$ (m) | $A = \int F\,\mathrm{d}s$ | arbejde $A$ | N·m = J |
| $P$ (W) | $t$ (s) | $E = \int P\,\mathrm{d}t$ | energi $E$ | W·s = J |
| $I$ (A) | $t$ (s) | $Q = \int I\,\mathrm{d}t$ | ladning $Q$ | A·s = C |

### Kinematik i 2D og skråt kast

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Hastighed og acceleration som afledte | $v(t) = s'(t)$, $\ a(t) = v'(t) = s''(t)$ | |
| Sted som integral | $s(t) = s_0 + \int_0^t v\,\mathrm{d}t$ | |
| Startkomposanter | $v_{0x} = v_0 \cdot \cos\alpha$, $\ v_{0y} = v_0 \cdot \sin\alpha$ | |
| Hastighed | $v_x = v_{0x}$, $\ v_y = v_{0y} - g \cdot t$ | |
| Sted | $x = v_{0x} \cdot t$, $\ y = v_{0y} \cdot t - \tfrac{1}{2} g t^2$ | |
| Banekurve | $y = x \cdot \tan\alpha - \dfrac{g \cdot x^2}{2 v_0^2 \cos^2\alpha}$ | en parabel |
| Maksimal højde | $h_{\max} = \dfrac{v_0^2 \sin^2\alpha}{2g}$ | |
| Kastelængde (samme højde) | $x = \dfrac{v_0^2 \cdot \sin(2\alpha)}{g}$ | størst ved $\alpha = 45°$ |
| Farten | $v = \sqrt{v_x^2 + v_y^2}$ | |
| Luftmodstand | $F_{\text{luft}} = \tfrac{1}{2} \cdot \rho \cdot C_d \cdot A \cdot v^2$ | $\rho$: luftens densitet (1,2 kg/m³), $C_d$: formfaktor |
| Grænsehastighed | $v_{\text{grænse}} = \sqrt{\dfrac{2 m g}{\rho \cdot C_d \cdot A}}$ | når $F_{\text{luft}} = F_{\text{tyngde}}$ |

Eksempel: $v_0 = 10\ \text{m/s}$, $\alpha = 50°$: $h_{\max} = 3{,}0\ \text{m}$ og kastelængde $10{,}0\ \text{m}$.

![Skråt kast](/images/formelsamling/skraat_kast.svg)

> Kasteparablen gælder **uden luftmodstand**. For en bold eller et spyd med stor fart
> bliver banen kortere og asymmetrisk (stejlere på vej ned).

### Bevægelsesmængde og stød

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Bevægelsesmængde | $p = m \cdot v$ | vektor; kg·m/s |
| Kraftens impuls | $\Delta p = F \cdot \Delta t$ | konstant kraft |
| | $\Delta p = \int F\,\mathrm{d}t$ | arealet under $(t, F)$-grafen |
| Newtons 2. lov (generel) | $F_{\text{res}} = \dfrac{\mathrm{d}p}{\mathrm{d}t}$ | |
| Bevarelse (isoleret system) | $m_1 v_1 + m_2 v_2 = m_1 u_1 + m_2 u_2$ | $v$: før, $u$: efter |
| Fuldstændig uelastisk stød | $u = \dfrac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$ | legemerne hænger sammen; $E_{\text{kin}}$ går tabt |
| Elastisk stød ($m_2$ i hvile) | $u_1 = \dfrac{m_1 - m_2}{m_1 + m_2} v_1$, $\ u_2 = \dfrac{2 m_1}{m_1 + m_2} v_1$ | både $p$ og $E_{\text{kin}}$ bevaret |

Eksempel: $0{,}20\ \text{kg}$ med $0{,}50\ \text{m/s}$ støder uelastisk ind i $0{,}30\ \text{kg}$ i hvile:
$u = \dfrac{0{,}20 \cdot 0{,}50}{0{,}50}\ \text{m/s} = 0{,}20\ \text{m/s}$.

### Jævn cirkelbevægelse

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Frekvens | $f = \dfrac{1}{T}$ | $T$: omløbstid |
| Vinkelfrekvens | $\omega = \dfrac{2\pi}{T} = 2\pi f$ | rad/s |
| Fart | $v = \dfrac{2\pi r}{T} = \omega \cdot r$ | |
| Centripetalacceleration | $a_c = \dfrac{v^2}{r} = \omega^2 \cdot r$ | rettet **ind mod centrum** |
| Centripetalkraft | $F_c = m \cdot \dfrac{v^2}{r} = m \cdot \omega^2 \cdot r$ | den *resulterende* kraft – ikke en ny kraft |

![Jævn cirkelbevægelse](/images/formelsamling/cirkelbevaegelse.svg)

> **Centrifugalkraften er en skinkraft.** I et inertialsystem virker der kun
> centripetalkraften (indad). Følelsen af at blive "slynget udad" er inerti.
> Centrifugalkraften optræder kun, hvis man regner i et roterende (accelereret) referencesystem.

Eksempel: En bil på 1200 kg i et sving med $r = 50\ \text{m}$ ved $15\ \text{m/s}$ kræver
$F_c = 1200 \cdot \dfrac{15^2}{50}\ \text{N} = 5400\ \text{N}$ fra gnidningen.

### Gravitation og bevægelse om et centrallegeme

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Newtons gravitationslov | $F = G \cdot \dfrac{m_1 \cdot m_2}{r^2}$ | $r$: afstand mellem **centrene** |
| Tyngdeacceleration | $g = \dfrac{G \cdot M}{r^2}$ | Jordens overflade: 9,82 m/s² |
| Banefart (cirkelbane) | $v = \sqrt{\dfrac{G \cdot M}{r}}$ | fra $\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}$ |
| Keplers 3. lov | $\dfrac{T^2}{r^3} = \dfrac{4\pi^2}{G \cdot M}$ | for ellipser: $r \to a$ (halve storakse) |
| Potentiel energi | $E_{\text{pot}} = -\dfrac{G \cdot M \cdot m}{r}$ | nulpunkt i uendelig afstand |
| Mekanisk energi i cirkelbane | $E_{\text{mek}} = -\dfrac{G \cdot M \cdot m}{2r}$ | |
| Undvigelseshastighed | $v_{\text{undv}} = \sqrt{\dfrac{2 G M}{r}} = \sqrt{2} \cdot v_{\text{bane}}$ | Jorden: 11,2 km/s |

**Keplers love:** 1) Planetbanerne er ellipser med Solen i det ene brændpunkt.
2) Linjen Sol–planet overstryger lige store arealer på lige lange tider.
3) $T^2 / a^3$ er den samme for alle planeter om samme centrallegeme.

Eksempel (ISS, 408 km over jorden, $r = 6{,}779 \cdot 10^6\ \text{m}$):
$v = \sqrt{\dfrac{6{,}674 \cdot 10^{-11} \cdot 5{,}972 \cdot 10^{24}}{6{,}779 \cdot 10^{6}}}\ \text{m/s} = 7{,}67\ \text{km/s}$ og $T = \dfrac{2\pi r}{v} = 93\ \text{min}$.

> $E_{\text{pot}} = m \cdot g \cdot h$ fra C-niveau er en **tilnærmelse** til $-GMm/r$, som kun
> gælder, når $h \ll R_{\text{Jord}}$.

### Harmonisk svingning

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Hookes lov | $F = -k \cdot x$ | $k$: fjederkonstant (N/m); gælder for små udtræk |
| Bevægelsesligning | $m \cdot a = -k \cdot x \ \Rightarrow\ x''(t) = -\dfrac{k}{m} x$ | |
| Løsning | $x(t) = A \cdot \cos(\omega t + \varphi)$ | $A$: amplitude, $\varphi$: fase |
| Fjederpendul | $\omega = \sqrt{\dfrac{k}{m}}$, $\ T = 2\pi\sqrt{\dfrac{m}{k}}$ | uafhængig af amplituden |
| Matematisk pendul | $T = 2\pi\sqrt{\dfrac{L}{g}}$ | kun for **små udsving** (under ca. 10°) |
| Fjederenergi | $E_{\text{fjeder}} = \tfrac{1}{2} k x^2$ | |
| Energibevarelse | $\tfrac{1}{2} k A^2 = \tfrac{1}{2} k x^2 + \tfrac{1}{2} m v^2$ | |
| Maksimal fart / acceleration | $v_{\max} = A \cdot \omega$, $\ a_{\max} = A \cdot \omega^2$ | |

Eksempler: $m = 0{,}50\ \text{kg}$ i en fjeder med $k = 20\ \text{N/m}$: $T = 2\pi\sqrt{0{,}025}\ \text{s} = 0{,}99\ \text{s}$.
Pendul med $L = 1{,}00\ \text{m}$: $T = 2{,}0\ \text{s}$.

![Harmonisk svingning](/images/formelsamling/harmonisk.svg)

### Elektrisk felt

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Coulombs lov | $F = k_e \cdot \dfrac{q_1 \cdot q_2}{r^2}$ | $k_e = 8{,}99 \cdot 10^9\ \text{N·m}^2/\text{C}^2$ |
| Elektrisk feltstyrke | $E = \dfrac{F}{q} \ \Leftrightarrow\ F = q \cdot E$ | N/C = V/m |
| Felt fra punktladning | $E = k_e \cdot \dfrac{Q}{r^2}$ | |
| Homogent felt (pladekondensator) | $E = \dfrac{U}{d}$ | $d$: pladeafstand |
| Spænding og arbejde | $U = \dfrac{A}{q}$, $\ A = q \cdot U$ | |
| Acceleration af ladning gennem $U$ | $q \cdot U = \tfrac{1}{2} m v^2 \ \Rightarrow\ v = \sqrt{\dfrac{2 q U}{m}}$ | ikke-relativistisk |
| Kapacitans | $C = \dfrac{Q}{U}$, $\ C = \varepsilon_0 \cdot \varepsilon_r \cdot \dfrac{A}{d}$ | $A$: pladeareal |
| Energi i kondensator | $E = \tfrac{1}{2} C U^2$ | |

Eksempel: En elektron accelereret gennem 100 V: $v = \sqrt{\dfrac{2 \cdot 1{,}602 \cdot 10^{-19} \cdot 100}{9{,}109 \cdot 10^{-31}}}\ \text{m/s} = 5{,}93 \cdot 10^6\ \text{m/s}$.

### Magnetisk felt

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Kraft på strømførende leder (Laplace) | $F = B \cdot I \cdot L \cdot \sin\theta$ | $F = BIL$ når leder $\perp$ felt |
| Lorentzkraften | $F = q \cdot v \cdot B \cdot \sin\theta$ | retning: højrehåndsregel (for positiv ladning) |
| Cirkelbane i B-felt | $r = \dfrac{m \cdot v}{q \cdot B}$ | fra $qvB = \dfrac{mv^2}{r}$ |
| Omløbstid (cyklotron) | $T = \dfrac{2\pi m}{q B}$ | uafhængig af farten |
| Felt om lang lige leder | $B = \dfrac{\mu_0 \cdot I}{2\pi \cdot r}$ | $\dfrac{\mu_0}{2\pi} = 2{,}0 \cdot 10^{-7}\ \text{T·m/A}$ |
| Felt i lang spole | $B = \mu_0 \cdot \dfrac{N}{L} \cdot I$ | $N/L$: vindinger pr. længde |

Eksempel: Elektronen fra før ($5{,}93 \cdot 10^6\ \text{m/s}$) i $B = 1{,}0\ \text{mT}$:
$r = \dfrac{9{,}109 \cdot 10^{-31} \cdot 5{,}93 \cdot 10^{6}}{1{,}602 \cdot 10^{-19} \cdot 1{,}0 \cdot 10^{-3}}\ \text{m} = 3{,}4\ \text{cm}$.

![Magnetfelter](/images/formelsamling/b_felt.svg)

### Induktion

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Magnetisk flux | $\Phi = B \cdot A \cdot \cos\theta$ | $\theta$: vinkel mellem felt og fladenormal; Wb |
| Faradays induktionslov | $\varepsilon = -N \cdot \dfrac{\mathrm{d}\Phi}{\mathrm{d}t}$ | $N$: antal vindinger |
| Lenz' lov | minusset | den inducerede strøm modvirker **ændringen**, der skabte den |
| Generator | $\varepsilon(t) = N \cdot B \cdot A \cdot \omega \cdot \sin(\omega t)$ | spole der roterer i homogent felt |
| Effektiv værdi (sinus) | $U_{\text{eff}} = \dfrac{U_0}{\sqrt{2}}$ | stikkontakt: 230 V eff. → $U_0 = 325\ \text{V}$ |
| Ideal transformer | $\dfrac{U_2}{U_1} = \dfrac{N_2}{N_1}$ | uden tab: $U_1 I_1 = U_2 I_2$ |

Eksempel: En spole med 200 vindinger, hvor fluxen falder fra 0,010 Wb til 0 på 0,050 s:
$\varepsilon = -200 \cdot \dfrac{0 - 0{,}010}{0{,}050}\ \text{V} = 40\ \text{V}$.

### Kvantefysik

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Fotonenergi | $E = h \cdot f$ | |
| Fotoelektrisk effekt | $h \cdot f = W + E_{\text{kin,max}}$ | $W$: løsrivelsesarbejde (fx Na ca. 2,3 eV – kilder varierer) |
| Fotonens impuls | $p = \dfrac{E}{c} = \dfrac{h}{\lambda}$ | |
| de Broglie-bølgelængde | $\lambda = \dfrac{h}{p} = \dfrac{h}{m \cdot v}$ | partikler har bølgeegenskaber |
| Compton-spredning | $\Delta\lambda = \dfrac{h}{m_e c}(1 - \cos\theta)$ | $\dfrac{h}{m_e c} = 2{,}43\ \text{pm}$ |
| Heisenbergs ubestemthedsrelation | $\Delta x \cdot \Delta p \ge \dfrac{h}{4\pi}$ | supplerende |

Eksempel: En elektron med $v = 1{,}0 \cdot 10^6\ \text{m/s}$ har
$\lambda = \dfrac{6{,}63 \cdot 10^{-34}}{9{,}11 \cdot 10^{-31} \cdot 1{,}0 \cdot 10^{6}}\ \text{m} = 0{,}73\ \text{nm}$ – samme størrelsesorden som atomafstande.

### Speciel relativitetsteori

| Størrelse | Formel | Bemærkning |
|---|---|---|
| Lorentzfaktor | $\gamma = \dfrac{1}{\sqrt{1 - \dfrac{v^2}{c^2}}}$ | $\gamma \ge 1$ |
| Tidsforlængelse | $\Delta t = \gamma \cdot \Delta t_0$ | $\Delta t_0$: egentid (målt i legemets hvilesystem) |
| Længdeforkortning | $L = \dfrac{L_0}{\gamma}$ | $L_0$: hvilelængde |
| Hvileenergi | $E_0 = m \cdot c^2$ | elektron: 0,511 MeV |
| Total energi | $E = \gamma \cdot m \cdot c^2$ | |
| Kinetisk energi | $E_{\text{kin}} = (\gamma - 1) \cdot m \cdot c^2$ | → $\tfrac{1}{2}mv^2$ for $v \ll c$ |
| Relativistisk bevægelsesmængde | $p = \gamma \cdot m \cdot v$ | |
| Hastighedsaddition | $u = \dfrac{u' + v}{1 + \dfrac{u' v}{c^2}}$ | resultatet bliver aldrig større end $c$ |

Eksempel: Ved $v = 0{,}80c$ er $\gamma = \dfrac{1}{\sqrt{1 - 0{,}64}} = 1{,}67$. En myon med
egen-levetid 2,2 µs lever $1{,}67 \cdot 2{,}2\ \text{µs} = 3{,}7\ \text{µs}$ set fra Jorden.

> **Gyldighed:** For $v \ll c$ er $\gamma \approx 1$, og Newtons mekanik er en fremragende
> tilnærmelse. Ved $v = 0{,}1c$ er $\gamma = 1{,}005$ (0,5 % afvigelse); ved $v = 0{,}5c$ er $\gamma = 1{,}15$.

</div>
