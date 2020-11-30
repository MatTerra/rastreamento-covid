from os import system
from utils.entity.usuario import Usuario
from utils.controller.sintoma import view_sintomas, create_sintoma
from utils.colors import bcolors

def sintoma_menu(user: Usuario):
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tl - Listar meus sintomas")
        print("\tc - Cadastrar um novo sintoma que apresentei")
        print("\ts - Listar os tipos de sintomas")
        print("\tx - Voltar ao menu principal")
        option = input(" >> ")
        if option == 'l':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_sintomas(pagina, user)
        elif option == 'c':
            create_sintoma(user)
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")