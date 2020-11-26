import os

from utils.controller import actions


def main_menu() -> str:
    print("O que você gostaria de fazer?")
    for key, action in actions.items():
        print(f"\t{key} - {action.get('name', '...')}")
    action = input(">> ").strip()
    if action not in actions.keys():
        raise ValueError(action)
    return action


def authentication_menu() -> str:
    print("Bem-vindo ao sistema de rastreamento de Covid.\n\n")
    print("O que você gostaria de fazer?\n")
    print("\tl - Login")
    print("\tc - Cadastro")
    print("\tx - Sair")
    escolha = input(" >> ").strip()
    os.system("clear")
    if escolha not in ["x", "l", "c"]:
        raise ValueError(escolha)
    return escolha
