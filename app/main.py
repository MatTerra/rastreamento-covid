import os
from time import sleep

from utils.entity.usuario import Usuario
from view.menus import main_menu, authentication_menu
from view.actions import sair, actions, login, signup, logout
from utils.colors import bcolors


if __name__ == "__main__":
    os.system("clear")
    try:
        while True:
            user = None
            while not user:
                try:
                    option = authentication_menu()
                    os.system("clear")
                    if option == "0":
                        sair()
                    elif option == "1":
                        user = login()
                    elif option == "2":
                        user = signup()
                except ValueError as e:
                    os.system("clear")
                    print(bcolors.WARNING
                          + f"A opção deve ser 0, 1 ou 2!"
                            f" Opção {e} inválida!" + bcolors.ENDC)
            os.system("clear")
            print(bcolors.OKGREEN+"Autenticado!"+bcolors.ENDC)
            action = ''
            while user:
                try:
                    action = main_menu()
                    os.system("clear")
                    if action not in actions.keys():
                        raise ValueError(action)
                    user = actions[action].get("function", logout)()
                except ValueError as e:
                    os.system("clear")
                    print(bcolors.WARNING
                          + f"A opção deve ser uma das disponíveis!"
                            f" Opção {e} inválida!" + bcolors.ENDC)
                except KeyboardInterrupt as e:
                    os.system("clear")
                    user = logout()
    except KeyboardInterrupt:
        sair()
