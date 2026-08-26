---
title: Hugo
weight: 3
---
### Restart Hugo
- vise local host:  
	- gå til ~html/ og skriv: 
	- hugo server --buildDrafts   eller hugo server -D
- genstart server eller skriv ./hugoserver text
	- git add .
	- git commit -m "text til log"
	- git push
- vent 3 min
### Billeder 
Skal ligge i static/images. så inkluderes med 
![]nix(billedet.png)
De vises IKKE i obsidian .. trist men kommer med når man starter serveren. 
### YAML TOML JSON
Er metadata filer. YAML er det vi bruger her med tre streger --- hvis man bruger TOML er det +++
Tjek AI for syntax forskelle. 
FormatAfgrænsningSyntax
- YAML ---   key: value
- TOML +++   key = value
- JSON { / }  "key": "value"
### Youtube
- gå ind på din fil og skriv en shortcode
- man skal skrive {{ /* < yt> */ }}
- og husk at den er helt hys med mellemrum der må ikke være nogen mellem mellem id="  osv .. 
### 100%
{{< yt id="2xkNJL4gJ9E">}}
### 20%
{{< yt id="2xkNJL4gJ9E" width="200px" >}}

{{</* yt id="2xkNJL4gJ9E" width="200px" */>}}
### taxonomies
- tags er 
- categories 
### HTML kode
kik på filet "biler" 