#!/bin/bash

cd "$(dirname "$0")" || exit 1
latexmk -auxdir=tmp -outdir=tmp -pdflatex='texfot lualatex -interaction nonstopmode' -pdf main.tex
makeglossaries main
latexmk -auxdir=tmp -outdir=tmp -pdflatex='texfot lualatex -interaction nonstopmode' -pdf main.tex
mv tmp/main.pdf .