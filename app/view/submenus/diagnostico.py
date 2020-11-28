from os import system

from utils.colors import bcolors
from utils.controller.diagnostico import atualizar_diagnostico, \
    create_diagnostico, \
    view_diagnosticos
from utils.entity.usuario import Usuario
from utils.controller.emissor import create_emissor, view_emissores


def diagnostico_submenu(user: Usuario) -> Usuario:
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tle - Listar emissores de diagnóstico")
        print("\tc - Cadastrar um novo emissor de diagnóstico")
        print("\td - Informar um diagnóstico")
        print("\tld - Listar diagnósticos")
        print("\ted - Editar diagnóstico")
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
        elif option == 'd':
            system("clear")
            create_diagnostico(user)
        elif option == 'ld':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_diagnosticos(pagina)
        elif option == 'ed':
            atualizar_diagnostico(user)
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")
    return user