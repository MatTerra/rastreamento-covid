from os import system

from utils.colors import bcolors
from utils.controller.location import create_local, view_locais
from utils.entity.usuario import Usuario


def local_submenu(user: Usuario) -> Usuario:
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tl - Listar locais")
        print("\tc - Cadastrar um novo local")
        print("\tx - Voltar ao menu principal")
        option = input(" >> ")
        if option == 'l':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_locais(pagina)
        elif option == 'c':
            create_local()
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")
