---
Title: " Nbconvert"
Weight: 2
geometry: margin=1cm
fontsize: 11pt
---


### Jupyter filer til HTML, pdf, latex, markdown
Programmet nbconvert konverterer jupyterfiler til html og alt muligt andet. 
billederne ligger så i en undermappe . Kik evtl "nat/Integralregning.md" 
Den danner en index.md fil 
programmet kaldes med 

** jupyter nbconvert --to marktown mitnavn.ipynb**

Med VS Code: 
content/
  integralregning/
    index.md
    Integralregning_files/
      billede1.png
      billede2.png
  massedefekt/
    index.md
    massedefekt_files/
      ...
Fordele:

Billeder ligger ved siden af siden de hører til — let at overskue i VS Code's filstifinder
Billedlinks i .md virker uden at du retter noget
Hver notebook bliver sin egen selvstændige mappe

## Dit workflow bliver så bare:

- jupyter nbconvert --to markdown minnotebook.ipynb
- Opret mappe i content/
- Kopier .md → omdøb til index.md
- Kopier _files/ mappen med ind
## lave pdffer fra md 
pandoc fil.md -o fil.pdf
pandoc fil.md -o fil.docx
Pandoc kan **IKKE** lave gode pdffer fra docx filer! det kører via Latex 
## åbne pdffer med Skim
open -a Skim fil.pdf