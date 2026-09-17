---
title: "Kasteparabel"
weight: 10
pdf: "pdfs/kasteparabel.pdf"
---

**Niveau: Fysik A** · **Emne: Mekanik – skråt kast** · **Eksperiment: videoanalyse**

[Tilbage til Eksperimenter A](/docs/fysik/a-eksp/)

## 1) Kasteparabel

Du skal optage et skråt kast i to dimensioner med dit kamera og analysere det i LoggerPro.

### Udstyr

- Kamera/tablet på stativ, opstillet vinkelret på kasteplanet
- En målestok i billedet til kalibrering af afstande
- En bold (eller lignende) med god kontrast til baggrunden

### Fremgangsmåde

1. Film kastet, så hele banen er med i billedet, og målestokken er synlig gennem hele forløbet.
2. Importér videoen i LoggerPro, og kalibrér længdeskalaen ud fra målestokken.
3. Placér origo, og markér bolden frame for frame gennem hele kastet.
4. LoggerPro opbygger nu automatisk $x(t)$ og $y(t)$ ud fra dine punkter.

> **Tjek framerate:** LoggerPro bruger videoens afspilnings-fps, ikke optage-fps. Optager du i slowmotion, så tjek at de to passer sammen, inden du regner videre. Det her er ret vigtigt, prøv at forstå fps (frame per second) det var med i en opgave på A-niveau sidste år hvor man skulle regne fps om !!!!! 

### Grafer

Plot følgende grafer direkte i LoggerPro:

- $x(t)$ og $y(t)$ (stedfunktionerne)
- $y(x)$ (banekurven)
- $v_{x}(t)$ (hastighedsfunktionen for x)
- $v_{y}(t)$ (hastighedsfunktionen for y)

Sæt alle grafer op i en tabel. Billedet til venstre og forklaringen til højre.

- Beskriv formen (ret linje? parabel? noget andet?).
- Forklar formen ud fra selve bevægelsen – hvorfor ser grafen præcis sådan ud?
- Hvilekn funktion i LoggerPro, der kan fittes til grafen? Hvilken, og hvad fortæller fit-parametrene dig? 
- kik nu på de to hastighedsgrafer. Prøv at begrund hvorfor det oftest er bedre at finde hastigheden som lineær fit til stedfunktionen i stedet for at lade loggerpro finde hastighedsfunktionen og så bestemme gennemsnit
- så kommer banekurven $y(x)$. Det er lidt tricky og derfor lagt i bonusopgave 1 :-) 

## Bonusopgave 1 – Banekurven
Stedfunktionerne for $x$ og $y$ er 
$$x(t) = v_{0x}\cdot t$$
$$y(t) = -\frac{1}{2}\cdot g \cdot t^2 + v_{0y}\cdot t$$

Vis at at du kan omskrive de to funktioner til nedenstående funktion for banekurven. 

Brug nu de værdier for $v_{0x}$ og $v_{0y}$, som I finder ud fra jeres fits i LoggerPro, og sæt dem ind i banekurvens ligning:

$$y = -\frac{g}{2\cdot v_{0x}^2}\cdot x^2 + \frac{v_{0y}}{v_{0x}}\cdot x$$

- Plot denne funktion (fx i Excel eller GeoGebra) sammen med jeres målte $y(x)$-graf.
- Passer den beregnede banekurve med jeres data? Kommentér på eventuelle afvigelser.
- Sammenlign med Loggerpro grafen

## Bonusopgave 2 – Kastehøjden og længden
Vi antager her at vi kaster en bold fra jorden af altså $y_{0} = 0m$
Vis ud fra ovenstående stedfunktioner at den maksimale højde og længde kan skrives som 
$$ h_{max} = \frac{v_{0y}^2}{2g} \qquad \textrm{og} \qquad l_{max} = \frac{2v_{0x}\cdot v_{0y}}{g}$$

Med $v_{0x} = v_0 \cos(\phi)$ og $v_{0y} = v_0 \sin(\phi)$ kan du skrive kastelængden som  


$$l = \frac{v_0^2 \cdot \sin(2\phi)}{g}$$

Brug jeres startbetingelser ($v_0$ og $\phi$) til at bestemme kastelængden $l$. 
Sammenlign den beregnede kastelængde med den kastelængde, I faktisk målte i videoen.
