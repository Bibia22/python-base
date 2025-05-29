]#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mult 10 5 
50

$ prefixcal.py 
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.0"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("log", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:(lineno)d f:%(filename)s: %(message)s'
)
ch.setFomatter(fmt)
log.addHandler(ch)

from datetime import datetime

while True:

    arguments = sys.argv[1:]

    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        # TODO: Repetição while + exceptions
        if not num.replace(".", "").isdigit():
            print(f"Numero inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    # TODO: Usar dict de funcoes
    if operation == "sum":
        result = n1 + n2
    if operation == "sub":
        result = n1 - n2
    if operation == "mul":
        result = n1 * n2
    if operation == "div":
        result = n1 / n2

    print(f"O resultado é {result}")

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')


    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1}, {n2} = {result}\n")
    except PermissionError as e:
        # TODO: logging
        logging.error("Deu erro %s, str(e)")
        sys.exit(1)

    if input("Pressione enter para continuar ou qualquer tecla para sair")
        break
