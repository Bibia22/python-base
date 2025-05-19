#!/usr/bin/env python3

import os
import logging  

#TODO: usar função
#TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("log", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:(lineno)d f:%(filename)s: %(message)s'
)
ch.setFomatter(fmt)
log.addHandler(ch)


"""
log.debug("Mensagem para o dev, qe, sysadmin")
log.info("Mensagem geral para usuario")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral")
"""


try:
    1/0
except ZeroDivisionError as e:
    logging.error("Deu erro %s, str(e)")
