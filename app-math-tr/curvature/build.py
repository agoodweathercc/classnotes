import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex curvature.tex")
    os.system("evince curvature.pdf")
    exit()
        
