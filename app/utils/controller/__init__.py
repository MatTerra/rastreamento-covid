from os import system

from utils.colors import bcolors
from utils.controller.authentication import logout
import utils.controller.profile
import view.submenus.profile
import view.submenus.location
import view.submenus.diagnostico

__all__ = ["authentication", "profile", "location", "actions"]


def sair():
    system("clear")
    print(bcolors.OKGREEN + "Obrigado por utilizar o sistema de rastreamento "
                            "do COVID" + bcolors.ENDC)
    exit(0)


actions = {"p": {"name": "Perfil",
                 "function": view.submenus.profile.profile_menu},
           "l": {"name": "Locais",
                 "function": view.submenus.location.local_submenu},
           "d": {"name": "Diagnóstico",
                 "function": view.submenus.diagnostico.diagnostico_submenu},
           "x": {"name": "Sair",
                 "function": logout}}
