from os import system

from getch import getch

from utils.colors import bcolors
from utils.entity.hospital import Hospital
from utils.database.hospitalDAO import HospitalDAO
from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

itens_per_page = 5

def view_hospitais(page: int):
    dao = None
    try:
        dao = GenericSQLDAO(database_type=PostgreSQLHelper)
        dao.database.query("SELECT * "
                           "FROM hospitais_view LIMIT %s OFFSET %s",
                           (itens_per_page, page*itens_per_page)
                           )
        results = dao.database.get_results()
        dao.database.query("SELECT COUNT(*) "
                           "FROM hospitais_view"
                           )
        total = dao.database.get_results()[0][0]
        pages = (total - 1) // itens_per_page
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Hospital"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Nome':^30}|{'Internações':^20}|{'Médicos':^20}|{'Relação I/M':^20}|"
              f"{bcolors.ENDC}")
        for result in results:
            print(f"|{result[0]:^30}|"
                  f"{result[1]:^20}"
                  f"|{result[2]:^20}"
                  f"|{result[3]:^20.2f}|")
        for i in range(itens_per_page - len(results)):
            print(f"|{'-':^30}|{'-':^20}"
                  f"|{'-':^20}"
                  f"|{'-':^20}|")
        print("\n\t  ", end="")
        for i in range(pages + 1):
            print(i, end=' ')
        print("\n", "\t", " " * page * 2, '^')
        print("Pressione <- ou -> para navegar entre as páginas")
        print("Pressione x para sair da listagem")
        option = ''
        while option != 'x':
            option = getch()
            if option == '[':
                option = getch()
                if option == "C":
                    system("clear")
                    return page + 1 if page + 1 <= pages else page
                if option == "D":
                    system("clear")
                    return page - 1 if page > 0 else page
        system("clear")
        return option
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os hospitais... "
              f"Tente novamente. {e}{bcolors.ENDC}")
        input()
    finally:
        if dao:
            dao.close()
    return page
