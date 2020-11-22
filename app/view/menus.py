import os
from time import sleep

from view.actions import actions


def main_menu() -> str:
    print("O que você gostaria de fazer?")
    for key, action in actions.items():
        print(f"\t{key} - {action.get('name', '...')}")
    action = input(">> ").strip()
    if action not in actions.keys():
        raise ValueError(action)
    return action


def authentication_menu() -> str:
    print("Bem-vindo ao sistema de rastreamento de Covid.")
    print("O que você gostaria de fazer?")
    print("\t0 - Sair")
    print("\t1 - Login")
    print("\t2 - Cadastro")
    escolha = input(">> ").strip()
    os.system("clear")
    if escolha not in ["0", "1", "2"]:
        raise ValueError(escolha)
    return escolha
