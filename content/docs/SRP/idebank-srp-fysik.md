---
title: Idébank SRP med fysik og kemi
weight: 2
---

# Inspiration til SRP-projekter med fysik og kemi

Lidt ideer til jer som overvejer at skrive SRP i fysik sammen med andre fag. Husk at det er bare ideer med nogle emner. 
Hvis I kan og det gælder især fysik og kemi på A-niveau så prøv at kik på de her sider fra universiteterne. De har ofte nogle færdige forløb i forskellige fagkombinationer: 

En del af emnerne – især dem med henfald eller bevægelse med modstand – kan udvides med en numerisk simulering, fx i Python, som en ekstra dimension i opgaven. Det er markeret enkelte steder nedenfor, men gælder som en generel mulighed flere steder.

Hvis jeg var jer så vil jeg starte med at browse de her uni-sider (lige nedenunder her eller helt i bunden af filen under [kilder](#kilder)) og finde et forsøg som passer. Så har man eksperiment, data og fag på plads inden man går i gang. Som regel hængder de projekter godt sammen. 


## Projekter på Universiteter i danmark
**Vær i god tid her!!!!!** Universiteterne har få pladser så det er først til mølle. 

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

**Andre**
- [DTU: Lav din SRP- eller SOP-øvelse](https://www.dtu.dk/uddannelse/tilbud-til-gymnasier-og-skoler/srp-sop)
- [RUC: SRP/SOP-øvelser på Roskilde Universitet](https://ruc.dk/srp-sop-oevelser-paa-roskilde-universitet) – bl.a. komplekse tal/harmonisk svingning i fysik

# Lidt inspiration til mulige projekter:
## Fysik + Kemi

**FysA · KeB**

- Kvantefysik og spektroskopi (NMR, IR, UV-Vis) – energiniveauer/orbitaler forklarer spektrallinjer
  *Forsøg: mål UV-Vis-absorptionsspektret for en farvet opløsning (fx KMnO4 eller en fødevarefarve) med spektrofotometer, og relatér den absorberede bølgelængde til en elektronovergangs energi.*
- Termodynamik og reaktionskinetik – Arrhenius-ligningen og aktiveringsenergi
  *Forsøg: klokkeforsøg (fx jod-klokkereaktionen) ved forskellige temperaturer – tag tiden og plot ln(k) mod 1/T for at bestemme aktiveringsenergien (Arrhenius-plot).*
- Elektrokemi og batteriteknologi – spændingsrækken, Nernst-ligningen, energitæthed
  *Forsøg: byg et Daniell-element (eller andre galvaniske celler) og mål EMK for forskellige elektrodepar – sammenlign med spændingsrækken.*
- Radioaktivt henfald som kinetisk model – halveringstid vs. kemisk reaktionsorden *(kan simuleres numerisk, fx i Python)*
- Solceller og halvledere – båndgab, fotoeffekt (kan kobles til iNANO's Grätzel-solcelle, se nedenfor)
  *Forsøg: mål I-U-karakteristikken for en solcelle ved forskellige lysintensiteter/vinkler og bestem virkningsgraden.*

**FysB · KeA**

- Syre-base-ligevægte og termodynamik – hvorfor ligger ligevægten, hvor den gør
  *Forsøg: titrer en svag syre og bestem pKa fra halvvejspunktet på titrerkurven.*
- Galvaniske celler og korrosion – strømlære som støttefag til elektrokemien
  *Forsøg: sammenlign korrosionshastighed for forskellige metaller i saltvand, eller byg en simpel galvanisk korrosionscelle.*
- Farvestoffers kemi og lys – absorptionsspektre og komplementærfarver (kræver kun optik på B-niveau)
  *Forsøg: mål absorptionsspektret for en farvet opløsning, og sammenhold den absorberede bølgelængde med den observerede (komplementære) farve.*
- Polymerers opbygning og mekaniske egenskaber
  *Forsøg: mål brudstyrke/elasticitet for forskellige plastfolier med en kraftmåler (spænding-tøjning-kurve).*
- Reaktionskinetik og temperaturafhængighed – kollisionsteori sat på simpel matematisk form

**Projekter fra universiteterne:**

| Niveau | Emne | Link | Kort beskrivelse |
|---|---|---|---|
| FysA · KeB | Hvad gør et molekyle til en effektiv drivhusgas? | [AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb/hvad-goer-et-molekyle-til-en-effektiv-drivhusgas) | IR-spektroskopi og molekylers evne til at absorbere infrarødt lys |
| FysA · KeB | Grøn energi: byg din egen Grätzel-solcelle | [AU](https://chem.au.dk/stx-og-htx/besoegsservice/eksperimentielle-oevelser-i-fysik/groen-energi-byg-din-egen-graetzel-solcelle-baseret-paa-fotosyntese-1) | Solcelle bygget efter fotosyntese-princippet, holdøvelse |
| FysA · KeB | Halvlederes optiske egenskaber: lysdioder og lasere | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/kvantefysik-og-halvlederes-optiske-egenskaber) | Båndgab, lysdioder og lasere |
| FysB · KeA | Superledere til fremtiden | [AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb/superledere-til-fremtiden) | Forskningspraktik om superledende materialer |
| FysB · KeA | Magneter – en tiltrækkende verden | [AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb/magneter-en-tiltraekkende-verden-fra-uparrede-elektroner-til-groen-omstilling) | Fra uparrede elektroner til grøn omstilling |
| FysB · KeA | Fremtidens genopladelige batterier | [AU](https://chem.au.dk/stx-og-htx/besoegsservice/oevelser/fremtidens-genopladelige-batterier-1) | Elektrokemi og batteriteknologi, holdøvelse |

## Fysik + Matematik

**FysA · MatA**

- Differentialligninger og harmonisk svingning (fjeder, pendul, RLC-kredsløb)
- Opdrift, flyvinger simulering og eksperiment (måske også med historie)
- Skråt kast med luftmodstand – ingen lukket analytisk løsning; oplagt til numerisk simulering, fx i Python (Euler/Runge-Kutta)
- Keplers love og numerisk baneberegning
- Kaos og den dobbelte pendul – følsomhed over for begyndelsesbetingelser (her kan man lave forsøg med dobbeltpendul og *simulere det med python*)
- Komplekse tal og vekselstrøm/impedans (svingkredse og beregning af disse)
- Statistik og radioaktivt henfald – Poisson-fordelingen som model for tælledata *(kan simuleres numerisk, fx i Python)*
- Fourier-analyse af lydsignaler – FFT af en optaget tone, dekomponering i overtoner *(uni-eksperiment: AAU's [Fourier-optik](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/fourier-optik))*
- Relativitetsteori og GPS – tidsdilatation udledt matematisk fra Lorentz-transformationen, efterprøvet på virkelige satellit-korrektionsdata
- Bølgeligningen og vandbølger – partiel differentialligning løst numerisk *(uni-eksperiment: AAU's [Vandbølger: interferens, refraktion, dispersion og spredning](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/vandbolger-interferens-refraktion-dispersion-og-spredning))*
- Ladede partikler i magnetfelt (Hall-effekt) – Lorentzkraften som differentialligning for cirkulær bevægelse *(uni-eksperiment: AAU's [Semiconductors: Hall Effect](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/halvledere-og-hall-effekt-1))*
- Aerodynamik omkring vingeprofiler – Bernoullis ligning og numerisk strømningssimulering *(uni-eksperiment: AAU's [vindtunnelforsøg](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-energi/maling-af-trykfordeling-pa-et-vingeprofil))*
- Fraktaler og dimension i naturen – box-counting-metoden på billeder af kystlinjer/brudflader; matematisk dimension mellem 1 og 2
- Statistisk mekanik og Boltzmann-fordelingen – temperatur som statistisk begreb, kobler eksponentialfunktioner til gaspartiklers energifordeling

**FysA · MatB**

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

**Projekter fra universiteterne:**

| Niveau | Emne | Link | Kort beskrivelse |
|---|---|---|---|
| FysA · MatA | Tunneleffekt og kvantemekanik | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/tunneleffekt-og-kvantemekanik) | STM-forsøg, kombineres direkte med Schrödingerligningen |
| FysA · MatA | Radiopulsarer og rotationsudvikling af neutronstjerner | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/radiopulsarer-og-rotationsudviklingen-af-neutronstjerner) | Observationsdata og teorigennemgang på gymnasieniveau |
| FysA · MatA | Fourier-optik | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/fourier-optik) | Fourier-transformation anvendt i moderne mikroskopi |
| FysA · MatA | Vandbølger: interferens, refraktion, dispersion og spredning | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/vandbolger-interferens-refraktion-dispersion-og-spredning) | Bølgeligningen efterprøvet i bølgetank |
| FysA · MatA | Semiconductors: Hall Effect | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-materialer-og-produktion/halvledere-og-hall-effekt-1) | Ledningsevnemåling i magnetfelt |
| FysA · MatA | Måling af trykfordeling på et vingeprofil | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-energi/maling-af-trykfordeling-pa-et-vingeprofil) | Vindtunnelforsøg, Bernoulli og opdrift |
| FysA · MatA | Statik og styrkelære – differentialligninger (Esbjerg) | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-energi/statik-og-styrkelaere-bojning-af-vinger-computer-baseret-multifysik-simulering-differentialligninger-esbjerg) | Bøjning af vinger, multifysik-simulering |
| FysA · MatA | Bølge-partikel-dualitet med enkle fotoner | [AU](https://phys.au.dk/vidensudveksling/for-fysiklaereren/sop-og-srp/boelge-partikel-dualitet-med-enkle-fotoner) | Enkeltfoton-eksperiment, vejledning direkte hos AU |

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

## Fysik/Kemi + Tysk

Bogen *Die Reise zum Mars* af Hans Dominik (1908), en tysk "Zukunftsroman". Handling: i år 2108 opdages vand og liv på Mars, og Doktor Müller opfinder en væske, der ophæver tyngdekraften – ikke raketteknologi, men en opdigtet "anti-tyngde-væske". Bogen er gratis og lovligt tilgængelig i fuld tekst,  man kan holde bogens fysik op mod den ægte (ækvivalensprincippet/generel relativitetsteori).
Kilde: [Die Reise zum Mars – Project Gutenberg](https://www.gutenberg.org/ebooks/40737)

**FysA · TyskB**

 *Die Reise zum Mars* (Hans Dominik, 1908) – den opfundne tyngdekraft-neutraliserende væske vurderet mod ægte fysik, samtidig med sproglig/genremæssig analyse af datidens tyske "Zukunftsroman"
- Einsteins originalartikel *"Zur Elektrodynamik bewegter Körper"* (1905) – speciel relativitetsteori læst i original tysk kildetekst, både sprogligt og fysisk
  Kilde: [Originalartikel (scan), Annalen der Physik 17, 1905 – Zenodo](https://zenodo.org/records/7113360)
- Röntgens opdagelse af røntgenstråler – originaltekst *"Ueber eine neue Art von Strahlen"* (1895/96) som kildegrundlag for både fysikken og datidens videnskabssprog
  Kilde: [Deutsches Textarchiv – fuld tekst](https://www.deutschestextarchiv.de/book/show/roentgen_strahlen_1896)
- Wernher von Braun og det tyske raketprogram (Peenemünde, V2) – raketfysik kombineret med tyske originalkilder og krigshistorisk kontekst
  Kilde: [„Held oder Verbrecher?" – Wernher von Braun, Historisch-Technisches Museum Peenemünde](https://museum-peenemuende.de/zeitreise/wernher-von-braun/)

**KeA · TyskB**

- Otto Hahn & Fritz Strassmanns opdagelse af kernefission (1939) – originalartiklen udkom på tysk i *Die Naturwissenschaften*; kernekemi + kildeanalyse af en af det 20. århundredes vigtigste tekster
  Kilde: [Originalartikel (scan), Internet Archive](https://archive.org/details/hahn-u-strassmann-uber-den-nachweis-und-das-verhalten-der-erdalkimetalle-1939)
- Fritz Haber og Haber-Bosch-processen – tysk kemisk industrihistorie med et stærkt etisk tveægget perspektiv (kunstgødning vs. kemiske våben)
  Kilde: [Habers Nobelvortrag (1920), original tysk tekst – NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/1918/haber/25890-nobelvortrag/)
- *Die Reise zum Mars* – de kemiske "opfindelser" i romanen (fx tyngdekraft-væsken) vurderet mod virkelig kemi

## Fysik + Filosofi

**FysA/B · FiC**

Det er lidt svært med eksperimenter her som passer til Fysik A niveau så jeg har tiføjet lidt muligheder.

- Heisenbergs usikkerhedsrelation og determinisme – hvad betyder det filosofisk, at naturen grundlæggende er indeterministisk?
  *Forsøg: enkeltspalte-diffraktion med laser – jo smallere spalte (mere præcis position), jo bredere diffraktionsmønster (mere usikker impuls). Viser Δx·Δp kvalitativt med udstyr I sandsynligvis allerede har. Vi har dobbeltspalt-glas på skolen, men ikke med forskellig **d** så her kan man kun variere $\lambda$*
- Kuhns paradigmeskift 1 – Det første er **oldtiden --> oplysningstiden** fra Aristoteles til Newton
- Kuhns paradigmeskift 2 - Det moderne gennembrud **klassisk fysik --> moderne tid** kvantemekanikkens og relativitetsteoriens fremkomst som case for et videnskabeligt paradigmeskift (fra klassisk til kvantefysik)
  *Forsøg: den fotoelektriske effekt (fotocelle + lys ved forskellige bølgelængder, mål stopspænding vs. frekvens) – selve eksperimentet, der ikke kunne forklares klassisk og tvang paradigmeskiftet igennem.*
- Poppers falsifikationisme vs. Kuhns paradigmebegreb – hvornår er en fysisk teori "god videnskab"?
  *Forsøg: brug egne måledata (fx en henfaldskurve eller pendulforsøg) som case – lav en statistisk test af, om data kan falsificere den forventede model. Metoden bliver selve det filosofiske eksempel.* Den her er nok lidt svært at få op på A-niveau i fysik. Men måske kan du finde et godt forsøg. 
- Kausalitet og Laplaces dæmon – fra klassisk determinisme til kvantemekanisk indeterminisme
  *Forsøg: dobbeltpendul filmet og analyseret (fx med Tracker) – systemet er 100% deterministisk, men praktisk uforudsigeligt pga. følsomhed over for begyndelsesbetingelser. Rejser spørgsmålet om determinisme ≠ forudsigelighed.*
- Kvantemekanikkens fortolkninger – Københavnerfortolkningen vs. mange-verdener-fortolkningen, og spørgsmålet om hvad "virkelighed" er
  *Forsøg: dobbeltspalteeksperimentet med laser (interferensmønster) – selve eksperimentet, der driver fortolkningsdiskussionen. AU tilbyder faktisk en udvidet version med enkeltfotoner (se universitetstilbud ovenfor), hvis du vil et niveau dybere.*
- Måleproblemet og bevidsthedens rolle – Schrödingers kat og Wigners ven som tankeeksperimenter
  *Her er det svært med et godt gymnasieforsøg, der direkte viser måleproblemet – det er grundlæggende et tankeeksperiment. Nærmeste I kommer eksperimentelt er AU/AAU's kvantesammenfiltrings- og Bell-uligheds-forsøg (se universitetstilbud)*
- Reduktionisme vs. holisme – kan alt i sidste ende forklares med fysikkens love?
  *Forsøg: en faseovergang (fx smeltepunkt eller en superleders overgangstemperatur, jf. AAU's superleder-forsøg ovenfor) – kollektiv/emergent opførsel, der ikke oplagt følger af enkeltpartiklers egenskaber alene, er et klassisk holisme-argument.*

## Fysik + Idræt

**FysA · IdrætB**

- Biomekanik af spring – impuls, kraftplatform og Newtons 3. lov (fx lodret spring, længdespring)
- Kastets fysik i sport – skråt kast og Magnus-effekt (spydkast, fodboldens "banana kick")
- Energiomsætning og virkningsgrad under løb/cykling – effekt, arbejde og muskulær virkningsgrad
- Aerodynamik og marginal gains i cykling – luftmodstand og drag coefficient
- Svømningens fysik – vandmodstand, viskositet og propulsion
- Pulsrespons og restitution som eksponentiel model – kobler måledata fra idræt til fysikkens henfaldsmodeller

**Projekter fra universiteterne:**

| Niveau | Emne | Link | Kort beskrivelse |
|---|---|---|---|
| FysA · IdrætB | Energiomsætningen i den menneskelige krop under cykelarbejde | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-medicin-og-sundhedsteknologi/energiomsaetningen-i-den-menneskelige-krop-under-cykelarbejde) | Direkte match til energiomsætnings-idéen ovenfor |
| FysA · IdrætB | Magnus-effekten på roterende tennisbold | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-energi/magnus-effekten-pa-roterende-tennisbold) | Samme fænomen som spydkast/"banana kick" ovenfor |
| FysA · IdrætB | Målinger og beregninger af kroppens signaler | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-medicin-og-sundhedsteknologi/malinger-og-beregninger-af-kroppens-signaler) | Biosignaler – kan kobles til pulsrespons-idéen ovenfor |

## Kemi + Biologi

**KeA · BiB**

- Enzymkinetik – Michaelis-Menten-modellen og temperaturens indflydelse på reaktionshastighed (her er der mulighed for forsøg på uni)
- Antioxidanters kemi – spektrofotometrisk/titrimetrisk bestemmelse af C-vitamin og biologisk relevans
- Gæringsprocessens kemi – ATP, enzymer og alkoholproduktion
- pH's indflydelse på enzymaktivitet – proteindenaturering forklaret kemisk

**KeB · BiA**

- Osmose og cellemembraner – diffusion og koncentrationsgradienter set gennem kemisk ligevægt
- Fotosyntese og $\textrm{CO}_2$-optag – kemisk reaktionsligning kombineret med biologisk regulering
- Næringsstoffers energiindhold – kalorimetri (kemi) sammenholdt med stofskifte (biologi)
- Antibiotika og bakteriers resistens – kemisk struktur af antibiotika og biologisk resistensudvikling

**Projekter fra universiteterne:**

| Niveau | Emne | Link | Kort beskrivelse |
|---|---|---|---|
| KeA · BiB | Karakterisering af enzymet xanthinoxidase | [AU (MBG, samlet oversigt)](https://mbg.au.dk/samarbejde/gymnasierskoler/studieretningsprojekt-for-3gere) | Enzymkinetik i praksis |
| KeA · BiB | Forøget opløselighed af ibuprofen ved brug af cyclodextriner | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-kemi-og-biovidenskab/foroget-oploselighed-af-ibuprofen-ved-brug-af-cyclodextriner) | Farmaceutisk kemi og opløselighed |
| KeA · BiB | Dyrkning af mælkesyrebakterier (Esbjerg) | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-kemi-og-biovidenskab/dyrkning-af-maelkesyrebakterier-esbjerg) | Fermentering, mikrobiologi og kemi |
| KeB · BiA | Biofuels fra alger (Esbjerg) | [AAU](https://www.aau.dk/samarbejde/tilbud-til-gymnasier/gymnasieopgaver/institut-for-kemi-og-biovidenskab/biofuels-fra-alger-esbjerg) | Bæredygtig energi fra biomasse |
| KeB · BiA | Stil skarpt på livets byggesten | [AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb/stil-skarpt-paa-livets-byggesten) | Forskningspraktik om biomolekylers struktur |
| KeB · BiA | Minimalistiske kunstige celler | [AU](https://chem.au.dk/stx-og-htx/srp-og-sop/forskningspraktik-srp-/sop-forloeb/minimalistiske-kunstige-celler) | Syntetisk biologi som forskningspraktik |

## Andre kombinationer

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
