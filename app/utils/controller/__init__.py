from os import system

from utils.colors import bcolors
from utils.controller.authentication import logout
import utils.controller.profile
import view.submenus.profile
import view.submenus.location
import view.submenus.diagnostico
import view.submenus.checkin
import view.submenus.notificacao
import view.submenus.internacao
import view.submenus.sintomas


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
           "s": {"name": "Apresentei sintomas",
                 "function": view.submenus.sintomas.sintoma_menu},
           "c": {"name": "Quero registrar/ver registros de entrada em locais (checkin)",
                 "function": view.submenus.checkin.checkin_menu},
           "n": {"name": "Notificações",
                 "function": view.submenus.notificacao.notificacao_menu},
           "i": {"name": "Relatório de internações",
                 "function": view.submenus.internacao
                     .relatorio_diagnostico_internacoes},
           "x": {"name": "Sair",
                 "function": logout}
           }
