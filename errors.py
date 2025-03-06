#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission
# (É mais fácil pedir pedrão do que permissão)

try:
    names = open("names.txt").readlines()
    # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucess")
finally:
    print("Execute that always")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
