---
title: "Centripetalkraft på roterende bane"
weight: 14
pdf: "pdfs/centripetalkraft-roterende-bane.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Mekanik – jævn cirkelbevægelse og centripetalkraft** · **Eksperiment: roterende bane med kraftsensor (LoggerPro)**

[Tilbage til Eksperimenter A](/docs/fysik/a-eksp/) · Teori og opgaver:
[Jævn cirkelbevægelse]({{< relref "jaevn-cirkelbevaegelse" >}})

## Formål

En vogn kører rundt i en cirkel, og en snor holder den inde. Du skal undersøge, om snorkraften passer med modellen for **jævn cirkelbevægelse**

$$F = m \cdot \omega^2 \cdot r$$

Det gør du ved at ændre én ting ad gangen: omdrejningshastigheden $\omega$, massen $m$ og radius $r$.

## Udstyr

![Den roterende bane med kraftsensor over aksen](/img/centralbevaegelse/roterende-bane-opstilling.jpg)

- Roterende bane med motor under midten og en vogn (200 g)
- Lodder, der kan skrues fast på vognen
- **Modvægt** (den sorte klods i den anden ende af banen)
- **Vernier Dual-Range Force Sensor** hængt op over aksen, tilsluttet computer med **LoggerPro** (husk den skal i analog indgangen)
- Snor fra vognen ind til aksen, gennem ringen og op til kraftsensoren
- Strømforsyning til motoren
- Målebånd på banen, vægt og evt. mobil med slowmotion

## Sådan virker opstillingen

- Motoren drejer banen rundt. Vognen vil gerne fortsætte ligeud, men snoren trækker den ind mod aksen.
- Snoren går op til kraftsensoren, så sensoren måler **snorkraften** hele tiden.
- Snorkraften er den kraft, der holder vognen i cirkelbanen.
- Modvægten skal afbalancere banen, ellers ryster hele stativet. Der står mærker på banen: **vogn alene, +50 g, +100 g … +250 g**. Sæt modvægten ved det mærke, der passer til det, du har lagt på vognen.

![Mærkerne for modvægten](/img/centralbevaegelse/roterende-bane-modvaegt.jpg)

> **Sikkerhed:** Banen drejer hurtigt rundt, og den kan nå at ramme dig, pas på. 
>
> - Skru lodderne **fast** på vognen. Et løst lod bliver til et projektil.
> - Tjek, at modvægten står ved det rigtige mærke, **før** du tænder. Justér afstanden på den sorte modvægt sådan at opstillingen ikke bevæger sig frem og tilbage når du tænde den. 
> - Start med lav spænding, og skru langsomt op.
> - Hold hænder, hår, ledninger og tasker væk fra banens cirkel.

## Hvad skal måles?

| Størrelse | Symbol | Hvordan | Enhed |
|---|---|---|---|
| Snorkraft | $F$ | Kraftsensoren (middelværdi over et stykke, hvor farten er stabil) | N |
| Masse | $m$ | Vej vognen **med** lodder | kg |
| Radius | $r$ | Fra aksens midte til vognens massemidtpunkt | m |
| Omløbstid | $T$ | Se nedenfor | s |
| Vinkelhastighed | $\omega$ | Beregnes ud fra $T$ | rad/s |

### Radius – pas på her

Vognen har en spids, der peger ned på målebåndet. Men tjek selv:

- Ligger målebåndets 0 præcis ved aksens midte?
- Er spidsen der, hvor vognens masse er samlet? Hvad med loddet oven på vognen?
- Står vognen samme sted, når banen drejer, som når den står stille? Snoren kan strække sig lidt.

Skriv ned, hvordan du har gjort, og vurdér usikkerheden på $r$.

### Omløbstiden – tre muligheder

1. **Stopur:** Tag tid på 10 omgange, og del med 10. (den er bedst så vi slipper for fotogate)
1. **Fotogate** Sæt et fotogate op som ved luftpudebanen og mål omløbstiden
2. **Slowmotion-video:** Film banen ovenfra, og tæl billeder pr. omgang.
3. **Fra kraftdataene:** Kraftkurven er ikke helt flad. Den har små bølger. Find ud af, om bølgerne har noget med omløbstiden at gøre. Hvis de har, kan du tælle fx 10 toppe i LoggerPro og aflæse tiden mellem første og sidste top.

Prøv gerne mindst to metoder ved den første måling, og se om de giver det samme.

## Fremgangsmåde

### 1. Indstil LoggerPro

- Sæt varigheden til ca. 10–20 s, og sæt samplingsfrekvensen op, fx 100 målinger/s.
- Vælg måleområdet **±10 N** på sensoren (kontakten på siden). Skift til ±50 N, hvis kraften bliver for stor.
- **Nulstil** sensoren (Experiment → Zero), mens banen står stille og snoren er slap.
- Viser LoggerPro negative værdier, når snoren trækker, så kan du vende fortegnet under sensorindstillingerne, eller bare regne med talværdien.

### 2. En måling

1. Tænd motoren, og vent til farten er **stabil**. Den skal ikke stige eller falde i løbet af målingen.
2. Start målingen.
3. Marker et stykke af grafen, hvor farten er stabil, og brug **Statistik** (Analyze → Statistics) til at finde middelkraften $F$.
4. Find omløbstiden $T$.

### 3. Tre måleserier

**Serie A – kraft og vinkelhastighed**
Behold samme $m$ og $r$. Mål ved 5–6 forskellige spændinger på motoren.

**Serie B – kraft og masse**
Behold samme $r$ og nogenlunde samme spænding. Mål med vognen alene og med +50 g, +100 g … op til +250 g. **Flyt modvægten hver gang.**

**Serie C – kraft og radius**
Behold samme $m$. Mål ved 4–5 forskellige radier.

I serie B og C kan du ikke garantere, at $\omega$ er præcis den samme hver gang. Det er helt i orden. Mål $\omega$ hver gang, og tænk over, hvilken størrelse du så skal plotte, så $\omega$ ikke ødelægger sammenligningen.

## Databehandling (Excel)

Lav en tabel med én række pr. måling:

|Serie|$m$ (kg)|$r$ (m)|$T$ (s)|$\omega$ (rad/s)|$\omega^2$ (rad²/s²)|$F$ (N)|$\dfrac{F}{\omega^2}$|...|
|---|---|---|---|---|---|---|---|---|
|A1|||||||||
|A2|||||||||
|...|||||||||

Til hver serie:

- **Hypotese først:** Skriv ned, hvilken graf du forventer at se, før du laver den. Ret linje? Gennem (0,0)? Hvad skal hældningen være?
- Lav grafen, og lav en lineær regression.
- Sammenlign hældningen med det, du har målt direkte (fx $m \cdot r$ i serie A). Beregn afvigelsen i procent.

## Spørgsmål til journalen

1. **Hvilken kraft er centripetalkraften her?** Tegn kræfterne på vognen set fra siden og set oppefra. Hvilken kraft peger ind mod centrum?
2. **Hypoteserne:** Passer dine tre grafer med $F = m \cdot \omega^2 \cdot r$? Går linjerne gennem (0,0)? Hvis ikke, hvad kan forklare det?
3. **Bølgerne på kraftkurven:** Hvorfor er kraften ikke helt konstant? Kom med mindst to forklaringer, og vurdér, hvilken du tror mest på.
4. **Omløbstiden:** Gav dine metoder til at finde $T$ det samme? Hvilken metode stoler du mest på, og hvorfor?
5. **Usikkerhed:** Hvilken målt størrelse giver den største usikkerhed på $F/\omega^2$? Husk at $\omega$ indgår i anden potens.
6. **Modelgyldighed:** Diskutér, hvor godt modellen holder:
   - Er bevægelsen **jævn**? Hvad viser grafen?
   - Er $r$ målt til vognens massemidtpunkt?
   - Snoren går gennem en ring ved aksen. Er snorkraften ved sensoren den samme som ved vognen? Hvad gør gnidning i ringen?
   - Vognen kører på hjul i en skinne. Kan skinnen også give en kraft ind mod centrum?
   - Snorens masse og strækning.
7. **Centrifugalkraft?** En klassekammerat siger: *"Vognen bliver slynget udad af centrifugalkraften, og snoren holder igen."* Forklar, hvorfor det er forkert i et inertialsystem, og hvornår man alligevel kan tale om en centrifugalkraft (som en **skinkraft**).
8. **Ekstra:** Hvad sker der med snorkraften, hvis du fordobler omløbstiden? Forudsig først, og mål så.
