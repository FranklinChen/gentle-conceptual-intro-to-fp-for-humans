# Use Beamer for slides, Minted for code highlighting.
# Minted requires Pygments: http://pygments.org/
# Use own copy of Minted for reproducibility.
PDFLATEX = latexmk -pdf

all:	presentation.pdf \
	#handout.pdf \
	feedback.pdf

handout.pdf:	slides.tex

presentation.pdf:	slides.tex

%.pdf:	%.tex minted.sty
	$(PDFLATEX) -shell-escape $*.tex

feedback.pdf:  feedback.txt
	enscript -B -o - $^ | ps2pdf - $@

clean:
	rm -rf *.pdf *.iml *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pyg *.fls *_latexmk _minted*

.PHONY:	all clean
