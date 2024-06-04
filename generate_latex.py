# pip install mako

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
