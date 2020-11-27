import os

from utils.colors import bcolors
from utils.controller import actions


def main_menu() -> str:
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"O que você gostaria de fazer?"
          f"{bcolors.ENDC}\n")
    for key, action in actions.items():
        print(f"\t{key} - {action.get('name', '...')}")
    action = input(">> ").strip()
    if action not in actions.keys():
        raise ValueError(action)
    return action


def authentication_menu() -> str:
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}"
          f"Bem-vindo ao sistema de rastreamento de Covid."
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"O que você gostaria de fazer?"
          f"{bcolors.ENDC}\n")
    print("\tl - Login")
    print("\tc - Cadastro")
    print("\tx - Sair")
    escolha = input(" >> ").strip()
    os.system("clear")
    if escolha not in ["x", "l", "c"]:
        raise ValueError(escolha)
    return escolha
