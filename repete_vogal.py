#!/usr/bin/env python3
"""
Repete Vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras
e imprime cada uma das palavras com suas vogais duplicadas.

ex.
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

lista_palavras = []
while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    if not palavra: # condição de parada
        break

    palavra_final = ""
    for letra in palavra:
        # TODO: Remover acentuação usando função
        if letra.lower() in "aeiouãáàêéàíõôóú":
            palavra_final += letra * 2
        else:
            palavra_final += letra
    
    # If Ternário alternativo
    # palavra_final += letra * 2 if letra.lower() in "aeiouãáàêéàíõôóú" else letra

    lista_palavras.append(palavra_final)

# for palavra in lista_palavras:
#    print(palavra)

print(*lista_palavras, sep="\n")
