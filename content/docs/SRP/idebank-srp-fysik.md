---
title: Idébank SRP med fysik og kemi
weight: 2
---

# Inspiration til SRP-projekter med fysik og kemi

Lidt ideer til jer som overvejer at skrive SRP i fysik sammen med andre fag. Husk at det er bare ideer med nogle emner. 
Hvis I kan og det gælder især fysik og kemi på A-niveau så prøv at kik på de her sider fra universiteterne. De har ofte nogle færdige forløb i forskellige fagkombinationer: 

En del af emnerne – især dem med henfald eller bevægelse med modstand – kan udvides med en numerisk simulering, fx i Python, som en ekstra dimension i opgaven. Det er markeret enkelte steder nedenfor, men gælder som en generel mulighed flere steder.


## Projekter på Universiteter i danmark

**Aarhus Universitet (AU)**
- [Liste over alle SRP-/SOP-forløb – Faculty of Natural Sciences](https://nat.au.dk/samarbejde/skoler-og-gymnasier/tilbud-til-gymnasieelever/lav-dit-srp-forloeb-hos-os/liste-over-alle-srp-forloeb)
- [SOP og SRP – Institut for Fysik og Astronomi](https://phys.au.dk/vidensudveksling/for-fysiklaereren/sop-og-srp)
- [SRP og SOP – Institut for Kemi](https://chem.au.dk/stx-og-htx/srp-og-sop)

**Aalborg Universitet (AAU)**
- [Hjælp til gymnasieopgaver (SRP/SOP) – samlet oversigt](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver)

**Syddansk Universitet (SDU, Odense)**
- [Find SDU's tilbud til gymnasier og grundskoler](https://www.sdu.dk/da/samarbejde/undervisningstilbud/findtilbud)
- [SRP, SOP og SSO med naturvidenskab som kernefag](https://www.sdu.dk/da/samarbejde/undervisningstilbud/findtilbud/tilbud/srp-sop-sso-naturvidenskab)
- [SRP og SOP i Fysik](https://www.sdu.dk/da/om-sdu/institutter-centre/fysik_kemi_og_farmaci/gymnasier/outreachifysik/srpfysik)

**Københavns Universitet (KU)**
- [Studieretningsprojekt og Studieområdeprojekt – SCIENCE-fakultetet](https://science.ku.dk/oplev-science/gymnasiet/studieretningsprojekt/)
- [Oversigt over konkrete SRP/SOP-forsøg – fokus.ku.dk](https://fokus.ku.dk/studieretningsprojek/)
- [SOP og SRP på Niels Bohr Institutet](https://nbi.ku.dk/moed-os/studieretningsprojekter-for-gymnasiet/)

**Bonus – to andre der dukkede op i søgningen**
- [DTU: Lav din SRP- eller SOP-øvelse](https://www.dtu.dk/uddannelse/tilbud-til-gymnasier-og-skoler/srp-sop)
- [RUC: SRP/SOP-øvelser på Roskilde Universitet](https://ruc.dk/srp-sop-oevelser-paa-roskilde-universitet) – bl.a. komplekse tal/harmonisk svingning i fysik

# Lidt inspiration til mulige projekter:
## Fysik + Kemi

**FysA · KeB**

- Kvantefysik og spektroskopi (NMR, IR, UV-Vis) – energiniveauer/orbitaler forklarer spektrallinjer
- Termodynamik og reaktionskinetik – Arrhenius-ligningen og aktiveringsenergi
- Elektrokemi og batteriteknologi – spændingsrækken, Nernst-ligningen, energitæthed
- Radioaktivt henfald som kinetisk model – halveringstid vs. kemisk reaktionsorden *(kan simuleres numerisk, fx i Python)*
- Solceller og halvledere – båndgab, fotoeffekt (kan kobles til iNANO's Grätzel-solcelle, se nedenfor)

**FysB · KeA**

- Syre-base-ligevægte og termodynamik – hvorfor ligger ligevægten, hvor den gør
- Galvaniske celler og korrosion – strømlære som støttefag til elektrokemien
- Farvestoffers kemi og lys – absorptionsspektre og komplementærfarver (kræver kun optik på B-niveau)
- Polymerers opbygning og mekaniske egenskaber
- Reaktionskinetik og temperaturafhængighed – kollisionsteori sat på simpel matematisk form

## Fysik + Matematik

**FysA · MatA**

- Differentialligninger og harmonisk svingning (fjeder, pendul, RLC-kredsløb)
- Skråt kast med luftmodstand – ingen lukket analytisk løsning; oplagt til numerisk simulering, fx i Python (Euler/Runge-Kutta)
- Keplers love og numerisk baneberegning
- Kaos og den dobbelte pendul – følsomhed over for begyndelsesbetingelser
- Komplekse tal og vekselstrøm/impedans
- Statistik og radioaktivt henfald – Poisson-fordelingen som model for tælledata *(kan simuleres numerisk, fx i Python)*

**FysB · MatB**

- Vektorer og kastebevægelse (fx sport – kuglestød, langspring)
- Eksponentiel vækst/henfald – Newtons afkølingslov, radioaktivitet *(kan simuleres numerisk, fx i Python)*
- Trigonometri og bølgefænomener – interferens, stående bølger
- Lineær regression på egne måleserier – usikkerhedsvurdering som matematisk håndværk

**FysA · MatA – kvantefysik**

- Brintatomets energiniveauer – Bohrs kvantiserede model ($E_n = -13{,}6 \textrm{ eV}/n^2$) udledt fra Coulombkraft og centripetalkraft, sammenholdt med spektrallinjer
- Partikel i en kasse – løsning af den tidsuafhængige Schrödingerligning for en uendelig potentialbrønd, kvantiserede energiniveauer og bølgefunktioner
- Kvantetunnellering gennem en potentialbarriere – hvordan bølgefunktionen "lækker" gennem en klassisk forbudt barriere; kan kobles til eksperimentelle STM-data (se AAU-tilbuddet nedenfor)
- Den kvanteharmoniske oscillator – sammenligning af kvante- og klassiske energiniveauer for fjederkraft
- Elektrondiffraktion og bølge-partikel-dualitet – de Broglie-bølgelængde og eksperimentel bekræftelse
- Numerisk løsning af Schrödingerligningen (fx shooting-metoden i Python) – for stærke elever, der vil regne det ud selv frem for kun at anvende færdige løsninger

## Fysik + Billedkunst

**FysA/B · Billedkunst C**

- Lys, farve og optik i maleriet – Newtons farvelære vs. kunstnerens farveblanding (additiv/subtraktiv)
- Perspektivgeometri og øjets optik
- Fotografiets fysik – blænde, eksponeringstid, linsers afbildning
- Kinetisk kunst – kræfter, moment og ligevægt (fx Calder-mobiler)
- Akustik og klangfarve i lydinstallation eller skulptur

## Fysik + Historie

**FysA/B · HiA/B**

- Langbuen: mekanik – spændkraft, projektilbane, energioverførsel
- Kanoners fysik i belejringskrig – ballistik og kastebevægelse
- Atombombens fysik og Manhattan-projektet – kernefysik mødt af videnskabshistorie
- Dampmaskinens termodynamik og den industrielle revolution
- Radioaktivitetens opdagelse (Curie/Becquerel) – videnskabshistorisk metode vs. moderne kernefysik
- Navigation gennem historien – fra sekstant til GPS (bølgefysik, relativitetsteori som perspektivering)

## Fysik + Dansk (formidlingsopgave)

**FysA/B · DaA**

- Formidling af kvantefysik til lægfolk – sprog, metaforer og deres begrænsninger
- Klimafysikkens retorik – hvordan drivhuseffekten formidles i medierne vs. fagligt korrekt
- Naturvidenskabelig formidling gennem tiden – fra H.C. Ørsted til nutidens YouTube-formidlere
- Science fiction og fysikkens grænser – hvor går grænsen mellem fakta og fiktion (fx rejser hurtigere end lyset)

## Fysik + Idræt

**FysA · IdrætB**

- Biomekanik af spring – impuls, kraftplatform og Newtons 3. lov (fx lodret spring, længdespring)
- Kastets fysik i sport – skråt kast og Magnus-effekt (spydkast, fodboldens "banana kick")
- Energiomsætning og virkningsgrad under løb/cykling – effekt, arbejde og muskulær virkningsgrad
- Aerodynamik og marginal gains i cykling – luftmodstand og drag coefficient
- Svømningens fysik – vandmodstand, viskositet og propulsion
- Pulsrespons og restitution som eksponentiel model – kobler måledata fra idræt til fysikkens henfaldsmodeller

## Kemi + Biologi

**KeA · BiB**

- Enzymkinetik – Michaelis-Menten-modellen og temperaturens indflydelse på reaktionshastighed
- Antioxidanters kemi – spektrofotometrisk/titrimetrisk bestemmelse af C-vitamin og biologisk relevans
- Gæringsprocessens kemi – ATP, enzymer og alkoholproduktion
- pH's indflydelse på enzymaktivitet – proteindenaturering forklaret kemisk

**KeB · BiA**

- Osmose og cellemembraner – diffusion og koncentrationsgradienter set gennem kemisk ligevægt
- Fotosyntese og $\textrm{CO}_2$-optag – kemisk reaktionsligning kombineret med biologisk regulering
- Næringsstoffers energiindhold – kalorimetri (kemi) sammenholdt med stofskifte (biologi)
- Antibiotika og bakteriers resistens – kemisk struktur af antibiotika og biologisk resistensudvikling

## Bonus: andre kombinationer

- **Fysik + Biologi**: biofysik, nanobiosensorer, energiomsætning i kroppen under cykling (AAU-tilbud, se nedenfor)
- **Fysik + Samfundsfag**: grøn energiomstilling, vindmøllers effektivitet og økonomi

## Konkrete eksperimentelle muligheder – Aarhus Universitet (AU)

**Institut for Fysik og Astronomi** – vejledning på udvalgte projekter, kontakt vejleder direkte (fx Thomas Tram), begrænset kapacitet, "first come, first served":

- Bølge-partikel-dualitet med enkle fotoner
- Enkelt-fotonkilde på mikrochip
- Kvantesammenfiltring og Bell-ulighedstest

**Institut for Kemi** – to spor:

- *Holdøvelser* (uden lærer, sammen med elever fra andre gymnasier): fx koffein i drikkevarer, nedbrydning af plastik, knæklys, syntese af paracetamol
- *Forskningspraktik* (1-2 dage, individuelt/små grupper): fx CO2-omdannelse, drivhusgassers egenskaber, superledere, batterimaterialer til fremtiden, kemisk modifikation af antistof
- *Spektraservice* (NMR/IR): I syntetiserer selv på skolen og indsender en ren prøve til AU, får spektre retur ca. en uge efter. Vær opmærksom på, at februar–april er en travl periode med længere ventetid.

**iNANO** (tværfagligt fysik/kemi, 5-8 timer): Grätzel-solcelle (byg din egen solcelle ud fra fotosyntese-princippet), AFM (atomart kraftmikroskop, ned til enkelte atomer), nanobiosensorer (guld-nanopartikler, ligner en antigentest)

## Konkrete eksperimentelle muligheder – Aalborg Universitet (AAU)

**Institut for Materialer og Produktion** (fysiktunge forsøg):

- Halvlederes optiske egenskaber – spektroskopi på krystaller/nanopartikler
- Halvledere og Halleffekt – ledningsevnemåling i stærkt magnetfelt
- Superledere – modstandsmåling ved flydende kvælstof, Meissner-effekt, magnetisk levitation
- Kvantetunnelering – STM-forsøg, kan kombineres med matematik (Schrödingerligningen)
- Fourieroptik – moderne optisk mikroskopi og rumlig filtrering

**Institut for Energi**:

- Brændselsceller og elektrolyse
- Vindtunnelforsøg – trykfordeling og vingekræfter (Esbjerg)

**Institut for Kemi og Biovidenskab**:

- Nikotinanalyse i tobak/vape (GC-MS)
- Parabener i kosmetik (HPLC)
- Guld-nanopartikel-syntese og karakterisering
- Ibuprofens opløselighed med cyclodextriner

## Praktiske bemærkninger

- Booking foregår typisk ved direkte kontakt til den enkelte vejleder/institut – ikke en central portal. Regn med, at I skal ud i god tid, især i den travle februar–april-periode.
- AU's institutter gør det klart, at de ikke leverer opgaveformulering eller metodebaggrund – det er stadig jeres og elevens arbejde. Universitetet leverer adgang til udstyr/data.
- Flere af de mest "fede" kemitilbud kræver ikke besøg – spektraservicen kan I bruge, uden at eleverne behøver rejse til Aarhus.

## Kilder

- [SOP og SRP – Institut for Fysik og Astronomi, AU](https://phys.au.dk/vidensudveksling/for-fysiklaereren/sop-og-srp)
- [SRP og SOP – Institut for Kemi, AU](https://chem.au.dk/stx-og-htx/srp-og-sop)
- [Forskningspraktik i din SRP eller SOP – Institut for Kemi, AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb)
- [NMR- og IR-spektreservice – Institut for Kemi, AU](https://chem.au.dk/stx-og-htx/spektre-og-roentgenservice/nmr-og-ir-spektreservice)
- [Liste over alle SRP-forløb – Faculty of Natural Sciences, AU](https://nat.au.dk/samarbejde/skoler-og-gymnasier/tilbud-til-gymnasieelever/lav-dit-srp-forloeb-hos-os/liste-over-alle-srp-forloeb)
- [SRP/SOP – iNANO, AU](https://inano.au.dk/schools/er-du-elev-paa-ungdomsuddannelse/srpsop)
- [SRP i Fysik på AAU (nano-hjemmeside)](https://homes.nano.aau.dk/srp/emner.html)
- [Hjælp til gymnasieopgaver (SRP/SOP) – AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver)
- [Institut for Kemi og Biovidenskab – AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-kemi-og-biovidenskab)
- [Introduktion til kvantemekanik og partikel i en boks – AU](https://phys.au.dk/fileadmin/site_files/forskning/ltc/klaus/introduktion_og_partikel_i_en_box.pdf)
- [Atommodel – Fysikleksikon, Niels Bohr Institutet](https://fysikleksikon.nbi.ku.dk/a/atommodel)

*Siden er lavet af Christoph Ridder til brug i vejledning af SRP-elever på Egaa Gymnasium.*
