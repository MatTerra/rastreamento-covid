from os import system

from getch import getch

from utils.colors import bcolors
from utils.database.localDAO import LocalDAO
from utils.entity.local import Local
from utils.input import read_simple_string

itens_per_page = 5


def create_local():
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos cadastrar um novo local!"
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Por favor preencha os dados abaixo:"
          f"{bcolors.ENDC}\n")
    name = read_simple_string("Nome do local")
    latitude = read_simple_string("Latitude")
    longitude = read_simple_string("Longitude")

    dao = None
    try:
        dao = LocalDAO()
        local = Local(nome=name, latitude=latitude, longitude=longitude)
        dao.create(local)
        system("clear")
        print(f"{bcolors.OKGREEN}Local cadastrado com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível guardar este local... "
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def view_locais(page: int = 0):
    dao = None
    try:
        dao = LocalDAO()
        system("clear")
        total, locais = dao.get_all(length=itens_per_page,
                                    offset=page*itens_per_page)
        pages = (total-1)//itens_per_page
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Locais:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Nome':^30}|{'Latitude':^20}|{'Longitude':^20}|"
              f"{bcolors.ENDC}")
        for local in locais:
            print(f"|{local.nome:^30}|{local.latitude:^20}"
                  f"|{local.longitude:^20}|")
        for i in range(itens_per_page - len(locais)):
            print(f"|{'-':^30}|{'-':^20}"
                  f"|{'-':^20}|")
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
        print(f"{bcolors.FAIL}Não foi possível listar os locais... "
              f"Tente novamente. {bcolors.ENDC}")
    finally:
        if dao:
            dao.close()
