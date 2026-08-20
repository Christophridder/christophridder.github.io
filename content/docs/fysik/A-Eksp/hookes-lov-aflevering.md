---
title: "Hookes aflevering" 
date: 2026-06-11
weight: 9
draft: false
---

## Aflevering til Hookes lov
### Individuel aflevering i word
Vi bruger filerne 
- [Hookes-lov-0]({{< relref "hookes-lov-0" >}}) som omhandler intro
- [Hookes-lov-1]({{< relref "hookes-lov-1" >}}) omhandler sinus funktionen og dens afledte
- [Hookes-lov-2]({{< relref "hookes-lov-2" >}}) omhandler den udæmpede svingning
- [Hookes-lov-3]({{< relref "hookes-lov-3" >}}) omhandler den dæmpede svingning

Jeg er interesseret i at I forstår betydningen af de fire parametre i sinusfunktionen $A,\omega, \varphi,  C$ at I forstår ideen bag differentialligningen uden at forstår hvordan man løser sådanne generelt, det er alt for kompliceret. 


### Intro

1. sæt et billede af opstillingen ind, lav en tegning med forklaringer
1. lav en tabel med to kolonner hvor du til venstre sætter et screenshot fra din loggerpro ind som viser den dæmpede svingning og til højre dit passende python plot
1. kommenter alle figurer
1. vis nu dine data fra det allerførste forsøg med Hookes lov hvor du fandt $k$ ved at hænge nogle lodder på fjederen. Klip excel grafen ind her og kommenter $k$-værdien og dens enhed. Hvor nøjagtigt, med hvor mange decimaler, kan du egentlig angive $k$ her? Det er **denne** $k$-værdi du skal genfinde i svingningsforsøget senere.  
### Forarbejde
Lav et forsøg hvor du bestemmer $k$ værdien for din fjeder vha Hookes lov som linerær regression. 
$$m\cdot g = -k \cdot x$$

Brug 4-5 masser og mål x find så $k$
### Teori
Vis følgende ting: 
1. forklar **Hookes lov** helt overordnet her kan du bruge fysikbogen. Brug en tegning med en fjeder.  
1. hvordan man løser ligningen $\ddot{y} = -\omega^2\cdot y$ med funktionen $y = A\cdot \sin(\omega t + \varphi) + C $
1. hvordan man via kraftligningen for hookes lov fra fysikbogen kan vise at $\omega^2 = \frac{k}{m}$

Nu springer vi helt til resultater og konklusion. Journalen skal være kort og kun indeholde de vigtigste ting. 

### Resultater 1 uden dæmpning
Her skal du bruge din excel fil hvor du har optaget en svingning. Brug kkun de første 30 svingninger. 

1. brug filen [Hookes-lov-2]({{< relref "hookes-lov-2" >}}) og find de 4 parametre som du skriver op i en tabel med de rigtige enheder. Brug hertil de første 30 svingninger i din excel fil. Det kan du gøre ved at *gem-som* $\rightarrow$ *hookes-lov-uden-d.xlsx*  
1. I **forarbejde** har I bestemt fjederkonstanten $k$, så brug nu sammenhængen mellem $\omega, k, m$ til at finde $k$.  
1. regn afvigelsesprocenten ud hvor den førstmålte er din teoretiske værdi. Kommentér kort på resultatet. 

### Resultater 2 med dæmpning
Her skal I bruge [Hookes-lov-3]({{< relref "hookes-lov-3" >}}). I skal **ikke** løse differentialligningen her. Bare vis billedet af den dæmpede svingning og vis alle konstanter fra formlen:  

$$y(t) = A \cdot e^{-\beta t} \cdot \sin(\omega t + \varphi) + C$$

I en lille tabel hvor du kort diskuterer især $\beta$- værdien som dæmpningsfaktor. 

Find halveringstiden $T_{\frac{1}{2}} = \frac{log(2)}{\beta}$ 

(i python programmet hedder den: **t_halv** = np.log(2) / beta)

For meget dæmpede svingninger forandrer $\omega$ sig en lille smule. Kan du måle det? 

### Konklusion
Rems kort op hvad du har fundet ud af. Kan du med svingningseksperimentet at du kan genfinde $k$? 

**That's it**