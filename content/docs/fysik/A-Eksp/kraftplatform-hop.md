---
title: "Hop på kraftplatform: find v₀ ved afsæt"
weight: 12
pdf: "pdfs/kraftplatform-hop.pdf"
pdf_ny_fane: true
---

*Udtænkt af Torben Aagaard*

**Niveau: Fysik A** · **Emne: Mekanik – bevægelsesmængde og kraftens impuls** · **Eksperiment: kraftplatform (LoggerPro)**

[Tilbage til Eksperimenter A](/docs/fysik/a-eksp/) · Teori og opgaver:
[Stød og bevægelsesmængde]({{< relref "stoed-bevaegelsesmaengde" >}}) og
[Integration i fysik]({{< relref "/docs/mat/integration-i-fysik" >}})

## Formål

Bestemme din **afsætshastighed** $v_0$, dvs. farten i det øjeblik du forlader pladen, ved et lodret hop ud fra **kraftens impuls**, dvs. arealet under kraft–tid-grafen, og sammenligne med en uafhængig måling fx videoanalyse.

## Teori i korte træk

Newtons 2. lov med **bevægelsesmængde** $p = m \cdot v$:

$$F_{\text{res}} = \frac{dp}{dt}$$

Integreres fra $t_1$ til $t_2$, får vi **kraftens impuls**:

$$\Delta p = \int_{t_1}^{t_2} F_{\text{res}} \, dt = m \cdot v_2 - m \cdot v_1$$

Under hoppet virker kun to kræfter lodret: normalkraften $F_n$ fra pladen (opad) og tyngdekraften $F_t$ (nedad). Hvis opad er positiv:

$$F_{\text{res}} = F_n - F_t \qquad\text{hvor}\qquad F_t = m \cdot g$$

Personen står stille i $t_1$ ($v_1 = 0$), og $t_2$ er det øjeblik, hvor du forlader pladen. Så er $v_2 = v_0$:

$$m \cdot v_0 = \int_{t_1}^{t_2} F_n \, dt \;-\; F_t \cdot (t_2 - t_1)$$

- Første led er **arealet under kurven** $F_n(t)$. Det aflæses med **Integral**-værktøjet i LoggerPro.
- Andet led er arealet af en **rektangulær boks** med højden $F_t$ og bredden $t_2 - t_1$. Tyngdekraften er konstant, så vi kan bare gange.
- Enhed: $\text{N} \cdot \text{s} = \text{kg} \cdot \text{m/s}$.

## Udstyr

- Kraftplatform (Vernier, 3500 N) tilsluttet computer med **LoggerPro**
- God plads omkring pladen til landing

> **Sikkerhed:** Stå stabilt, og **land ved siden af pladen** , aldrig på pladens kant. Der skal være en person klar til at gribe, hvis nogen mister balancen. Ryd området omkring pladen.

## Hvad skal måles?

| Størrelse | Symbol | Hvordan | Enhed |
|---|---|---|---|
| Kraft fra pladen | $F_n$ | Måles af kraftplatformen som funktion af tiden | N |
| Tid | $t$ | Logges automatisk | s |
| Din vægt (tyngdekraft) | $F_t$ | Middelværdi af $F_n$, mens du står helt stille | N |
| Afsætsøjeblik | $t_2$ | Første måling, hvor $F_n$ er tæt på 0 | s |
| Flyvetid (kontrol) | $t_{\text{flyv}}$ | Fra videoen: tid fra du forlader jorden til du lander | s |

## Fremgangsmåde

### 1. Indstilling af LoggerPro

- Vælg **Indstillinger for dataindsamling** og sæt varigheden til ca. 5 s.
- Sæt **samplingsfrekvensen** så højt som muligt (fx 100 prøver/s eller mere). En højere frekvens giver en mere præcis bestemmelse af afsætsøjeblikket $t_2$.
- **Nulstil** pladen (Zero), **mens ingen står på den**.

### 2. Hoppet

1. Stå helt stille midt på pladen med hænderne i siden (så armene ikke svinger med).
2. Start målingen, og **bliv stående helt stille i mindst 2 sekunder**. Det er her, du senere finder din vægt $F_t$.
3. Gå ned i benene, og sæt så kraftigt af lodret op (modbevægelseshop).
4. **Land ved siden af pladen** på måtten. Så registreres kun afsætsfasen.
5. Stop målingen. Gentag mindst **3 gange**, og gem alle målinger.

Læs graferne igennem, så du kan genkende de tre faser:

- **Stille stående:** $F_n = F_t$ (grafen er flad).
- **Ned:** Først falder $F_n$ under $F_t$ (du accelererer nedad), så stiger den over $F_t$, når du bremser nedgangen.
- **Op og afsæt:** $F_n$ er langt større end $F_t$, og til sidst falder den brat til 0, når du forlader pladen.

### 3. Kontrol med video

Optag hoppet fra siden med mobilen i slow-motion, uden at flytte kameraet. Aflæs (billede for billede) tiden $t_{\text{flyv}}$ fra afsæt til landing.

Er tyngdepunktet i samme højde ved afsæt og landing, er opstigningstiden $t_{\text{flyv}}/2$, og så gælder

$$v_0 = g \cdot \frac{t_{\text{flyv}}}{2}$$

## Databehandling i LoggerPro

Alt kan aflæses direkte i LoggerPro. Du skal bruge **fem tal**, og så er resten regning på lommeregneren.

### Det, du skal aflæse

| Nr. | Hvad | Sådan gør du | Enhed |
|---|---|---|---|
| 1 | $F_t$ (din vægt) | Marker det stille stykke i starten af grafen, og tryk **Statistik** (Analysér → Statistik). Aflæs **middelværdien**. | N |
| 2 | $t_1$ | Venstre kant af det område, du integrerer over. Vælg et sted **lige før du begynder at gå ned i benene**, mens kraften stadig er flad. | s |
| 3 | $t_2$ | Højre kant af området. Vælg **det første punkt, hvor kraften er tæt på 0**, dvs. det øjeblik du forlader pladen. | s |
| 4 | $\int F_n \, dt$ | Marker området fra $t_1$ til $t_2$ på grafen, og tryk **Integral** (Analysér → Integral). Aflæs tallet i boksen. | N·s |

> **Aflæsning af $t_1$ og $t_2$:** Brug **Undersøg** eller **Analyze** $\rightarrow$ **Integral**, og flyt musen hen til områdets venstre og højre kant. Eller aflæs tiderne i datatabellen ud for de to punkter **HUSK** at skrive $t_1$ og $t_2$ ned eksakt, du kan se det i tabellen hvor tallene passende til området bliver markeret. $t_1$ og $t_2$ skal være eksakt det samme som integralet. 

### Sådan ser det ud

Integralet i LoggerPro er hele det **lyserøde areal** mellem kraftkurven og 0-aksen, fra $t_1$ til $t_2$. Boksen $F_t \cdot (t_2 - t_1)$ er arealet under den vandrette linje i højden $F_t$. Forskellen mellem de to er den **nettokraft**, der ændrer din bevægelsesmængde: det, der ligger over linjen, tæller positivt, og det, der ligger under, tæller negativt.

### Beregn

1. **Massen:** $m = \dfrac{F_t}{g}$ med $g = 9{,}82$ N/kg
2. **Boksen:** $F_t \cdot (t_2 - t_1)$ (N·s)
3. **Kraftens impuls:**
$$\Delta p = \int_{t_1}^{t_2} F_n \, dt \;-\; F_t \cdot (t_2 - t_1)$$
4. **Afsætshastigheden:** Fordi du står stille i $t_1$, er $\Delta p = m \cdot v_0$, og dermed
$$v_0 = \frac{\Delta p}{m}$$
5. **Hævning af tyngdepunktet:**
$$h = \frac{v_0^2}{2 \cdot g}$$

**Eksempel på udregning (tallene er ikke dine egne):** Hvis $F_t = 853$ N, $t_2 - t_1 = 1{,}21$ s og LoggerPro giver $\int F_n \, dt = 1249$ N·s, så er

$$m = \frac{853\ \text{N}}{9{,}82\ \text{N/kg}} = 86{,}9\ \text{kg} \qquad \Delta p = 1249\ \text{N·s} - 853\ \text{N} \cdot 1{,}21\ \text{s} = 217\ \text{N·s}$$

$$v_0 = \frac{217\ \text{N·s}}{86{,}9\ \text{kg}} = 2{,}5\ \text{m/s} \qquad h = \frac{(2{,}5\ \text{m/s})^2}{2 \cdot 9{,}82\ \text{m/s}^2} = 0{,}32\ \text{m}$$

### Genvej: integrér nettokraften direkte (valgfrit)

Opret en beregnet kolonne $F_{\text{res}} = F_n - F_t$ (Data → Ny beregnet kolonne, formel `"Force" - <F_t>` med dit eget tal indsat). Integrér så $F_{\text{res}}$ fra $t_1$ til $t_2$. Tallet i boksen er **$\Delta p$ direkte**, og du kan springe boksen over.

### Tjek dit resultat

- Forvent en afsætshastighed på nogle få m/s og en hævning på 10–40 cm. Ligger dit resultat langt uden for, så tjek enhederne og dit valg af $t_1$ og $t_2$.
- Hvis du flytter $t_2$ **ét punkt**, ændrer $v_0$ sig med op til ca. $0{,}2$ m/s. Det er den største usikkerhed i forsøget, så angiv kun 2 betydende cifre.

## Beregninger og resultater lav forsøget 3 gange 

Lav en tabel med en række pr. hop:

|Hop|$m$ (kg)|$F_t$ (N)|$t_2 - t_1$ (s)|$\int F_n\,dt$ (N·s)|$\Delta p$ (N·s)|$v_0$ (m/s)|$h$ (m)|$v_0$ fra video (m/s)|
|---|---|---|---|---|---|---|---|---|
|1|||||||||
|2|||||||||
|3|||||||||

## Spørgsmål til journalen

1. **Graflæsning:** Forklar med Newtons 2. lov, hvorfor $F_n$ først bliver mindre end $F_t$ og bagefter meget større. Hvornår er din hastighed 0 nedad? Hvor på grafen ligger det punkt?
2. **Boksen:** Hvorfor kan man trække tyngdekraftens bidrag fra som en simpel rektangelboks?
3. **Valg af $t_1$:** Hvad sker der med $v_0$, hvis du flytter $t_1$ tidligere eller senere i den stille periode? Hvorfor?
4. **Usikkerhed på $t_2$:** Beregn $v_0$ igen med $t_2$ ét datapunkt tidligere og ét senere. Hvor meget ændrer resultatet sig? Hvad siger det om, hvor mange betydende cifre du kan angive?
5. **Kontrol:** Passer $v_0$ fra kraftplatformen med $g \cdot t_{\text{flyv}}/2$ fra videoen? Beregn afvigelsen i procent.
6. **Modelgyldighed:** Diskutér, hvad modellen forudsætter:
   - Kraftplatformen måler kun den lodrette kraft, og vi behandler dig som ét punkt (tyngdepunktet). Dit legeme deformeres og bevæger sig i flere dele.
   - Luftmodstanden er ubetydelig i den korte afsætsfase.
   - Tyngdepunktet er ikke i samme højde ved afsæt og ved landing, fordi du strækker benene og tæerne ved afsæt, men lander med lidt bøjede ben.
   - Aflæsningen af $t_2$ afhænger af samplingsfrekvensen.
7. **Enheder:** Vis, at arealet under en kraft–tid-graf har enheden kg·m/s. Hvad er det for en fysisk størrelse?
8. **Ekstra:** Sammenlign to forskellige hop (fx med og uden armsving, eller et hop uden nedgang først). Hvad ændrer sig i grafen, i $\Delta p$ og i $v_0$?
