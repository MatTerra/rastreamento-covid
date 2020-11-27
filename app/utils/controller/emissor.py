from os import system

from getch import getch

from utils.colors import bcolors
from utils.database.emissorDAO import EmissorDAO
from utils.entity.emissor import Emissor
from utils.input import read_simple_string

itens_per_page = 5


def create_emissor():
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos cadastrar um novo emissor!"
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Por favor preencha os dados abaixo:"
          f"{bcolors.ENDC}\n")
    name = read_simple_string("Nome do emissor")
    local = '.'*300
    while len(local) > 256:
        local = read_simple_string("Local")
    dao = None
    try:
        dao = EmissorDAO()
        emissor = Emissor(nome=name, local=local)
        dao.create(emissor)
        system("clear")
        print(f"{bcolors.OKGREEN}"
              f"Emissor cadastrado com sucesso!"
              f"{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível guardar este emissor... "
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def select_emissor(page: int = 0) -> Emissor:
    dao = None
    try:
        dao = EmissorDAO()
        system("clear")
        total, emissores = dao.get_all(length=itens_per_page,
                                    offset=page*itens_per_page)
        pages = (total-1)//itens_per_page if total > 0 else 0
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Selecione o emissor:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Índice':^6}|{'Nome':^30}|{'Local':^60}|"
              f"{bcolors.ENDC}")
        for index, emissor in enumerate(emissores):
            print(f"|{index:^6}|{emissor.nome:^30}|{emissor.local:^60}|")
        for i in range(itens_per_page - len(emissores)):
            print(f"|{'-':^30}|{'-':^60}|")
        print("\n\t  ", end="")
        for i in range(pages+1):
            print(i, end=' ')
        print("\n", "\t", " "*page*2, '^')
        print("Pressione -> para próxima página")
        print("Pressione <- para a página anterior")
        print("Pressione x para sair da listagem")
        print("Use o índice para selecionar")
        option=''
        while option != 'x':
            option = getch()
            if option == '[':
                option = getch()
                if option == "C":
                    system("clear")
                    return page+1 if page+1 <= pages else page
                if option == "D":
                    system("clear")
                    return page-1 if page > 0 else page
            elif option in [str(i) for i in range(itens_per_page)]:
                return emissores[int(option)]
        system("clear")
        return option
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os emissores... "
              f"Tente novamente. {bcolors.ENDC}")
        return 'x'
    finally:
        if dao:
            dao.close()


def view_emissores(page: int = 0):
    dao = None
    try:
        dao = EmissorDAO()
        system("clear")
        total, emissores = dao.get_all(length=itens_per_page,
                                    offset=page*itens_per_page)
        pages = (total-1)//itens_per_page
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Emissores:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Nome':^30}|{'Local':^60}|"
              f"{bcolors.ENDC}")
        for emissor in emissores:
            print(f"|{emissor.nome:^30}|{emissor.local:^60}|")
        for i in range(itens_per_page - len(emissores)):
            print(f"|{'-':^30}|{'-':^60}|")
        print("\n\t  ", end="")
        for i in range(pages+1):
            print(i, end=' ')
        print("\n", "\t", " "*page*2, '^')
        print("Pressione -> para próxima página")
        print("Pressione <- para a página anterior")
        print("Pressione x para sair da listagem")
        option=''
        while option != 'x':
            option = getch()
            if option == '[':
                option = getch()
                if option == "C":
                    system("clear")
                    return page+1 if page+1 <= pages else page
                if option == "D":
                    system("clear")
                    return page-1 if page > 0 else page
        system("clear")
        return option
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os emissores... "
              f"Tente novamente. {bcolors.ENDC}")
        return 'x'
    finally:
        if dao:
            dao.close()
