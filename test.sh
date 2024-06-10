# Testeja tots els tests dintre de src
# python -m unittest discover src -v 

# Per testejar un sol test o classe, cal indicar a Python quin directori conté tots els mòduls a importar
# La forma més senzilla és utilitzant PYTHONPATH=src davant del comando
# Una altra manera és posant un punt al davant de tots els noms del mòduls importats, això li diu a Python
# que el mòdul importat es troba en el mateix directori que el mòdul des d'on s'importa
# e.g. from .textnode import ...
#PYTHONPATH=src python -m unittest src.test_inline_markdown.TestInlineMarkdown.test_text_to_textnodes
PYTHONPATH=src python -m unittest src.test_block_markdown.TestBlockMarkdown