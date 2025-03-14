#!/usr/bin/env python3
"""
Alarme de Temperatura

Faça um script que pergunta ao usuário qual a temperatura e o indice de umidade do ar
sendo que será exibida uma mensagem de alelrta dependendo das condições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA!!! Frio extremo
"""

import sys
import logging
log = logging.Logger("alerta")

try:
    temperatura = float(input("Informe a temperatura: ").strip())
    umidade = float(input("Informe a umidade: ").strip())
except ValueError:
    log.error("Informe apenas números inteiros ou decimais separados por ponto (ex: 24.5)")
    sys.exit(1)

if temperatura > 45:
    print("ALERTA!!! Perigo calor extremo")
elif (temperatura * 3) >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temperatura >= 10 and temperatura <= 30:
    print("Normal") 
elif temperatura >= 0 and temperatura <=10:
    print("Frio")
elif temperatura < 0:
    print("ALERTA!!! Frio extremo")
