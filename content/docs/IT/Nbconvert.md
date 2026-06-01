---
Title: " Nbconvert"
Weight: 2
---

### Jupyter filer til HTML 
Programmet nbconvert konverterer jupyterfiler til html. 
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