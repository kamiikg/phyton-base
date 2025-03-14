#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python3 numeros_pares.py`
2
4
6
8
...
"""

# com while
n = 0
while n  < 201:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1

# com for
for num in range (1, 201):
    if num % 2 != 0:
        continue
    print(num)
