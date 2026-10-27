"""Gør en PDF printsikker: al tekst laves om til vektorkurver med Ghostscript.
Så kan printeren/PDF-viseren ikke tabe tegn som ( ) + − og ligevægtspile.
Bruges af md2pdf.py og quizkort/build_pdf.py – kan også køres alene:
    python3 scripts/pdf/printsikker.py static/pdfs/fil.pdf"""
import os, shutil, subprocess, sys

def printsikker(pdf):
    gs = shutil.which("gs")
    if not gs:
        print("ADVARSEL: Ghostscript (gs) mangler -> PDF'en er ikke gjort printsikker.\n"
              "          Installér med:  brew install ghostscript", file=sys.stderr)
        return False
    tmp = pdf + ".tmp.pdf"
    r = subprocess.run([gs, "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER", "-sDEVICE=pdfwrite",
                        "-dNoOutputFonts", "-dCompatibilityLevel=1.6", "-o", tmp, pdf],
                       capture_output=True, text=True)
    if r.returncode or not os.path.exists(tmp):
        print("ADVARSEL: Ghostscript fejlede – original PDF beholdes.\n" + r.stderr[-1000:], file=sys.stderr)
        return False
    os.replace(tmp, pdf)
    return True

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(("Printsikker: " if printsikker(p) else "Uændret: ") + p)
