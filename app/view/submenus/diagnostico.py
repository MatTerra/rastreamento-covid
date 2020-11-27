from os import system

from utils.colors import bcolors
from utils.entity.usuario import Usuario
from utils.controller.emissor import create_emissor, view_emissores


def diagnostico_submenu(user: Usuario) -> Usuario:
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tle - Listar emissores de diagnóstico")
        print("\tc - Cadastrar um novo emissor de diagnóstico")
        print("\tx - Voltar ao menu principal")
        option = input(" >> ")
        if option == 'le':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_emissores(pagina)
        elif option == 'c':
            system("clear")
            create_emissor()
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")
    return user