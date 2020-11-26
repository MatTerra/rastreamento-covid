from os import system

from utils.colors import bcolors
from utils.controller.authentication import logout
import utils.controller.profile
import view.submenus.profile

__all__ = ["authentication", "profile", "location", "actions"]


def sair():
    system("clear")
    print(bcolors.OKGREEN + "Obrigado por utilizar o sistema de rastreamento "
                            "do COVID" + bcolors.ENDC)
    exit(0)


actions = {"p": {"name": "Visualizar perfil",
                 "function": view.submenus.profile.view_profile},
           "e": {"name": "Editar perfil",
                 "function": view.submenus.profile.edit_profile},
           "x": {"name": "Sair",
                 "function": logout}}
