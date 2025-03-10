#!/usr/bin/env python3

import os
import logging

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)

# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s '
    'l:%(lineno)d - f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

# exemplos de log
log.debug("Mensagem pro dev, qa, sysadmin")
log.info("Mensgem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral, exemplo: banco de dados sumiu")

print("------")

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e)) 