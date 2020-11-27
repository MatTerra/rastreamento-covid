from os import system

from getch import getch

from utils.colors import bcolors
from utils.database.localDAO import LocalDAO
from utils.entity.local import Local
from utils.input import read_simple_string

itens_per_page = 2


def create_local():
    system("clear")
    print("Vamos cadastrar um novo local!")
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
            return 0
        print("Locais:\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Nome':^30}|{'Latitude':^20}|{'Longitude':^20}|"
              f"{bcolors.ENDC}")
        for local in locais:
            print(f"|{local.nome:^30}|{local.latitude:^20}"
                  f"|{local.longitude:^20}|")
        print("\n\t  ", end="")
        for i in range(pages+1):
            print(i, end=' ')
        print("\n", "\t", " "*page*2, '^')
        print("Pressione -> para próxima página")
        print("Pressione <- para a página anterior")
        print("Pressione x para sair da listagem")
        a=''
        while a != 'x':
            a = getch()
            if a == '[':
                a = getch()
                if a == "C":
                    system("clear")
                    return page+1 if page+1 <= pages else page
                if a == "D":
                    system("clear")
                    return page-1 if page > 0 else page
        system("clear")
        return a

    finally:
        if dao:
            dao.close()
