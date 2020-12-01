from os import system

from utils.colors import bcolors
from utils.controller.authentication import logout
import utils.controller.profile
import view.submenus.profile
import view.submenus.location
import view.submenus.diagnostico
import view.submenus.checkin
import view.submenus.notificacao
import view.submenus.hospitais

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
           "c": {"name": "Checkin",
                 "function": view.submenus.checkin.checkin_menu},
           "n": {"name": "Notificações",
                 "function": view.submenus.notificacao.notificacao_menu},
           "h": {"name": "Hospitais", 
                 "function": view.submenus.hospitais.hospitais_menu},
           "x": {"name": "Sair",
                 "function": logout}
          }
