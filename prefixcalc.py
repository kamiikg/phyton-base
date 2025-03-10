"""
Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operacao: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.1"

import os
import sys
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
fh = handlers.RotatingFileHandler(
    "prefixcalc-exe.log",
    maxBytes=10**6,
    backupCount=10
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s '
    'l:%(lineno)d - f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
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
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(f"[ERROR] {str(e)}")
    sys.exit(1)

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymos')

try:
    with open (filepath, "w") as arquivo:
        arquivo.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    log.error("You dont have permission to create filepath: %s", str(e))
    sys.exit(1)

print(f"O resultado é {result}")
