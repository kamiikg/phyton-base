#!/usr/bin/env python3
"""
Exibe o relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
salas = {
    "1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "ingles": {
        "nome": "Inglês",
        "alunos": ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
    },
    "musica": {
        "nome": "Música",
        "alunos": ["Erik", "Carlos", "Maria"]
    },
    "danca": {
        "nome": "Dança",
        "alunos": ["Gustavo", "Sofia", "Joana", "Antonio"]
    }
}

for key, value in aulas.items():

    print(f"Alunos da atividade de {aulas[key]['nome']}\n")

    atividade_sala1 = set(aulas[key]['alunos']) & set(salas['1'])
    atividade_sala2 = set(aulas[key]['alunos']).intersection(set(salas['2']))

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print("-" * 40)
