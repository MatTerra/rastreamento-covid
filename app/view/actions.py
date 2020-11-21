import os
import sys

from utils.colors import bcolors


def sair():
    os.system("clear")
    print(bcolors.OKGREEN+"Obrigado por utilizar o sistema de rastreamento "
                          "do COVID"+bcolors.ENDC)
    sys.exit(0)


actions = {"0": {"name": "Sair", "function": sair}}
