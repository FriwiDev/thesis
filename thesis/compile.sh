#!/bin/bash

cd "$(dirname "$0")" || exit 1
echo ">>> First render"
latexmk -auxdir=tmp -outdir=tmp -pdflatex='texfot lualatex -interaction nonstopmode' -pdf main.tex
echo ">>> Make glossaries"
makeglossaries -d tmp main
echo ">>> Second render"
latexmk -auxdir=tmp -outdir=tmp -pdflatex='texfot lualatex -interaction nonstopmode' -pdf main.tex
mv tmp/main.pdf .