import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape logreg2.tex")
    os.system("evince logreg2.pdf")
    exit()
