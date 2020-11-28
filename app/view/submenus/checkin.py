from os import system
from utils.entity.usuario import Usuario
from utils.controller.checkin import view_checkins, create_checkin
from utils.colors import bcolors

def checkin_menu(user: Usuario):
    while True:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"O que você gostaria de fazer?"
              f"{bcolors.ENDC}\n")
        print("\tl - Listar checkins")
        print("\tc - Cadastrar um novo checkin")
        print("\tx - Voltar ao menu principal")
        option = input(" >> ")
        if option == 'l':
            pagina = 0
            while pagina != 'x':
                system("clear")
                pagina = view_checkins(pagina, user)
        elif option == 'c':
            create_checkin(user)
        elif option == 'x':
            system("clear")
            return user
        else:
            system("clear")
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")