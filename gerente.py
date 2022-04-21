import Views.ModuloLogin.login as vl
import Views.dashboard as p
import sys


def carrega_sistema():
    logou = vl.executa()
    if logou:
        p.executa()


carrega_sistema()
sys.exit(0)
