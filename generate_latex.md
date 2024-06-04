Crea un file LaTeX con Python!

Ecco una possibile soluzione utilizzando la libreria `mako` per generare il codice LaTeX e `subprocess` per eseguire la compilazione:

1. Installa la libreria `mako`:
```bash
pip install mako
```
2. Crea un file Python chiamato ad esempio `generate_latex.py` con il seguente codice:
```python
import mako

template = """
\\documentclass{article}
\\title{%s}
\\begin{document}
%s
\\end{document}
"""

def generate_latex(title, content):
    return template % (title, content)

# Esempio di utilizzo
title = "My LaTeX File"
content = "Questo è il contenuto del mio file LaTeX"

latex_code = generate_latex(title, content)
print(latex_code)
```
3. Modifica il codice Python per adattarlo alle tue esigenze (ad esempio, puoi aggiungere più variabili o strutture dati).
4. Esegui il file Python:
```bash
python generate_latex.py
```
Questo dovrebbe stampare il codice LaTeX nel console.

5. Crea un file chiamato ad esempio `compile_latex.sh` con il seguente codice:
```bash
#!/bin/bash

latex_code=$1
pdflatex ${latex_code}
```
6. Modifica il percorso del file di output (ad esempio, se desideri che il file PDF venga salvato in una cartella specifica).
7. Fai partire lo script:
```bash
./compile_latex.sh generate_latex.py > my_latex_file.pdf
```
Questa volta, il codice LaTeX verrà compilato e il file PDF sarà creato!

Nota: Assicurati di avere installato `pdflatex` sulla tua macchina e che sia disponibile nel tuo percorso degli eseguibili. Inoltre, se desideri eseguire la compilazione in modo automatico all'avvio del sistema, potrai utilizzare un file `crontab` o una task scheduler come `cron`.
