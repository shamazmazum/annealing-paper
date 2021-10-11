annealing.pdf: annealing.tex
	pdflatex annealing.tex
	bibtex annealing
	pdflatex annealing.tex
	pdflatex annealing.tex

all: annealing.pdf

clean: .PHONY
	rm -f *.aux *.log *.bbl *.blg annealingNotes.bib
