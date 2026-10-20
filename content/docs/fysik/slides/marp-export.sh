#!/bin/bash
# Eksporter alle *-slide.md filer og kopier billedmapper til static/slides/

KOVA="/Users/christophridder/Nextcloud/crsite/content/docs/fysik/slides/kova"
OUT="/Users/christophridder/Nextcloud/crsite/static/slides"

for f in "$KOVA"/*-slide.md; do
  name=$(basename "$f" -slide.md)
  echo "Eksporterer $name..."
  marp "$f" --html -o "$OUT/$name.html"

  # Kopier billedmappe hvis den findes
  imgdir="$KOVA/${name}-slide"
  if [ -d "$imgdir" ]; then
    cp -r "$imgdir" "$OUT/${name}-slide"
    echo "  → kopierede billeder fra ${name}-slide/"
  fi
done

echo "Færdig!"
