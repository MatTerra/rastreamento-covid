from time import sleep

from view.actions import actions
from utils.colors import bcolors


def main_menu() -> str:
    print("O que você gostaria de fazer?")
    for key, action in actions.items():
        print(f"\t {key} - {action.get('name', '...')}")
    action = input(">> ").strip()
    if action not in actions.keys():
        raise ValueError(action)
    return action