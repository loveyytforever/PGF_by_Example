from pathlib import Path
import subprocess


for i in range(1, 525):
    tmp_tex = Path(f'example_{i}.tex')
    tmp_pdf = Path(f'example_{i}.pdf')
    # if i in [11, 53, 58, 59, 499]:
    #     continue
    if i == 11:
        continue
    if tmp_tex.is_file():
        if tmp_pdf.is_file():
            ...
        else:
            print(f"File {tmp_pdf} does not exist.")
            # subprocess.run(f'pdflatex -shell-escape -output-directory pics {tmp_tex}', shell=True)
            subprocess.run(f'pdflatex --shell-escape {tmp_tex}', shell=True)

subprocess.run('latexmk -c', shell=True)
''' log
line 0: Cannot load input from 'example_3.sin.gnuplot'

system returned with code 256

! Package pgfplots Error: Sorry, the gnuplot-result file 'example_3.sin.table' 
could not be found. Maybe you need to enable the shell-escape feature? For pdfl
atex, this is '>> pdflatex -shell-escape'. You can also invoke '>> gnuplot <fil
e>.gnuplot' manually on the respective gnuplot file..
'''