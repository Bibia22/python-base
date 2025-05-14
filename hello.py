#!/usr/bin/env  python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt-BR

Ou informe através do CLI argument `--lang`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Gabrielle Santos"
__license__ = "Unlicense"

import os
import sys

# Argumentos padrão
arguments = {"lang": None, "count": 1}

# Lê argumentos da linha de comando
for arg in sys.argv[1:]:
    try:
       key, value = arg.split("=")
       key = key.lstrip("-").strip()
       value = value.strip()
       if key not in arguments:
         print(f"Invalid Option `{key}`")
         sys.exit()
       arguments[key] = value
    except ValueError:
        print(f"Invalid Argument: {arg}. Use the format --lang=xx_XX or --count=N")
        sys.exit()

# Converte count para inteiro com tratamento de erro
try:
    count = int(arguments["count"])
except ValueError:
    print("O valor de --count deve ser um número inteiro.")
    sys.exit()

# Mensagens traduzidas
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "OlÔö£├¡, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# Define idioma atual
current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")

# Normaliza o valor da linguagem
if current_language is not None:
    current_language = current_language.split(".")[0]

# Pergunta ao usuário até escolher um idioma válido
while current_language not in msg:
    print(f"unrecognized language: {current_language}")
    print("Idiomas disponiveis:" ",".join(msg.keys()))
    current_language = input("Choose language: ").strip()

print((msg[current_language] + "\n") * count)
