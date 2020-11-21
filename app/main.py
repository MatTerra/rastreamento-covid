import os

from view.authentication import login
from view.menus import main_menu, actions
from view.actions import sair
from utils.colors import bcolors


if __name__ == "__main__":
    os.system("clear")
    try:
        user_id = login()
        os.system("clear")
        print(bcolors.OKGREEN+"Logado!"+bcolors.ENDC)
        action = ''
        while True:
            try:
                action = main_menu()
                os.system("clear")
                if action not in actions.keys():
                    raise ValueError(action)
                actions[action].get("function", sair)()
            except ValueError as e:
                os.system("clear")
                print(bcolors.WARNING
                      + f"A opção deve ser uma das disponíveis!"
                        f" Opção {e} inválida!" + bcolors.ENDC)
    except KeyboardInterrupt:
        sair()
