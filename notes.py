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
    print(f"Invalid command {arguments[0]}")

while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag? ").strip().lower()

        # leitura das notas    
        for line in open(filepath):
            titulo, tag, texto = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {titulo}")
                print(f"text: {texto}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        try:
            titulo = arguments[1]
        except IndexError:
            titulo = input("Qual o título? ").strip().title()

        text = [
            f"{titulo}",
            input("tag: ").strip(),
            input("text:\n").strip()
        ]
        # \t - tsv
        with open(filepath, "a") as arquivo:
            arquivo.write("\t".join(text) + "\n")

    continuar =  input(f"Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if continuar != "y":
        break
