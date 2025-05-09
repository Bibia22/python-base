#!/usr/bin/env python3
"""Exibe o relatório de ciranças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"

#Dados
salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]    
}

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca)
]

#Listar alunos em cada atividade por sala

for nome_atividade, alunos_atividade in atividades:

    print(f"Alunos da atividade de {nome_atividade}\n")
    print("-" * 40)

    for nome_sala, alunos_sala in salas.items():
        alunos_na_atividade = set(alunos_sala) & set(alunos_atividade)
        print(f"{nome_sala}: {sorted(alunos_na_atividade)}")

    print()
    print("_" * 40)

