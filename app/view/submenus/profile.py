from os import system

from utils.colors import bcolors
from utils.controller.profile import add_email, change_birthday, \
    remove_email, view_profile
from utils.entity.usuario import Usuario


def edit_profile_submenu(user: Usuario) -> Usuario:
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de editar?"
              f"{bcolors.ENDC}\n")
        print("\ta - Adicionar email secundário")
        print("\tr - Remover email")
        print("\td - Data de nascimento")
        print("\tx - Voltar")
        choice = input(">> ")
        if choice == 'a':
            add_email(user)
        elif choice == 'r':
            system("clear")
            remove_email(user)
        elif choice == 'd':
            change_birthday(user)
        elif choice == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")


def profile_menu(user: Usuario)-> Usuario:
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tv - Visualizar perfil")
        print("\te - Editar perfil")
        print("\tx - Voltar")
        option = input(" >> ")
        if option == 'v':
            system("clear")
            user = view_profile(user)
        elif option == 'e':
            system("clear")
            user = edit_profile_submenu(user)
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")
