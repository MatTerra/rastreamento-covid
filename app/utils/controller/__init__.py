from os import system

from utils.colors import bcolors
from utils.controller.authentication import logout
import utils.controller.profile
import view.submenus.profile
import view.submenus.location
import view.submenus.diagnostico
import view.submenus.checkin
import view.submenus.sintomas

__all__ = ["authentication", "profile", "location", "actions"]


def sair():
    system("clear")
    print(bcolors.OKGREEN + "Obrigado por utilizar o sistema de rastreamento "
                            "do COVID" + bcolors.ENDC)
    exit(0)


actions = {"p": {"name": "Meu perfil",
                 "function": view.submenus.profile.profile_menu},
           "l": {"name": "Quero ver/adicionar um local",
                 "function": view.submenus.location.local_submenu},
           "d": {"name": "Fui diagnosticado com COVID",
                 "function": view.submenus.diagnostico.diagnostico_submenu},
           "c": {"name": "Quero registrar que estive em um local (checkin)",
                 "function": view.submenus.checkin.checkin_menu},
           "s": {"name": "Apresentei sintomas",
                 "function": view.submenus.sintomas.sintoma_menu},
           "x": {"name": "Sair",
                 "function": logout}
          }
