import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex dynp.tex")
    os.system("evince dynp.pdf")
    exit()
        
