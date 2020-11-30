from os import system
from getch import getch
from utils.colors import bcolors

from utils.database.sintomaDAO import SintomaDAO
from utils.database.caso_sintomaDAO import CasoSintomaDAO

itens_per_page = 5

def create_caso_sintoma():
    pass

# Lista ocorrencias de um sintoma
# para um determinado usuario
def view_caso_sintoma():
    pass

# Lista os tipos de sintomas
def view_sintoma(page: int):
    dao = None
    try:
        dao = SintomaDAO()
        system("clear")
        total, sintomas = dao.get_all(length=itens_per_page,
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
              f"Sintomas:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Descricao':^30}|{'Risco':^20}|"
              f"{bcolors.ENDC}")
        for sintoma in sintomas:
            print(f"|{sintoma.descricao[:30]:^30}"
                  f"|{sintoma.risco:^20}|")
        for i in range(itens_per_page - len(sintomas)):
            print(f"|{'-':^30}"
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
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os tipos de sintomas... "
              f"Tente novamente.{str(e)}{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()