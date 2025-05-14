#!/user/bin/env python3
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.1"


email_tmpl = """
Olá %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f
"""
import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath)
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        %{
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem"
            "link": "http//canetaslegais.com"
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-"*50)

