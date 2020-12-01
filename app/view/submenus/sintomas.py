from os import system
from utils.entity.usuario import Usuario
from utils.controller.caso_sintoma import view_caso_sintoma, \
                                          create_caso_sintoma, \
                                          view_sintoma
from utils.colors import bcolors

def sintoma_menu(user: Usuario):
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tl - Listar sintomas que apresentei")
        print("\tc - Cadastrar um novo sintoma que apresentei")
        print("\ts - Listar os tipos de sintomas")
        print("\tx - Voltar ao menu principal")
        option = input(" >> ")
        if option == 'l':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_caso_sintoma(pagina, user)
        elif option == 'c':
            create_caso_sintoma(user)
        elif option == 's':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_sintoma(pagina)
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")