#!/usr/bin/env python3
"""
Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print("you must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {argument[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower(): # TODO: Tratar exception
                print(f"title: {titulo}")
                print(f"text: {texto}")
                print("-" * 30)
                print()

if arguments[0] == "new":
    titulo = arguments[1] # TODO: Tratar exception
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip()
    ]
    # \t - tsv
    with open(filepath, "a") as arquivo:
        arquivo.write("\t".join(text) + "\n")
