from os import system

from getch import getch
from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.colors import bcolors

itens_per_page = 5
datetime_format = "%d/%m/%y"


def view_relatorio_diagnostico_internacoes(page: int):
    dao = None
    try:
        dao = GenericSQLDAO(database_type=PostgreSQLHelper)
        system("clear")
        dao.database.query("SELECT * "
                           "FROM internacoes_diagnostico "
                           "LIMIT %s OFFSET %s;",
                           (itens_per_page, (page * itens_per_page)))
        results = dao.database.get_results()
        dao.database.query("SELECT COUNT(usuario_id_) "
                           "FROM internacoes_diagnostico;")
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
              f"Internações:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Usuário':^34}|{'Dt. Sint.':^10}|{'Dt. Exame':^10}"
              f"|{'Internação':^10}|{'Hospital':^20}|{'UTI':^3}"
              f"|{'Data Alta':^10}|{'Dt. Recu.':^10}|"
              f"{bcolors.ENDC}")
        for result in results:
            print(f"|{result[0]:^34}"
                  f"|{result[1].strftime(datetime_format):^10}"
                  f"|{result[2].strftime(datetime_format):^10}"
                  f"|{result[3].strftime(datetime_format) if result[3] else '-':^10}"
                  f"|{result[4] if result[4] else '-':^20}"
                  f"|{'s' if result[5] is True else 'n':^3}"
                  f"|{result[6].strftime(datetime_format) if result[6] else '-':^10}"
                  f"|{result[7].strftime(datetime_format) if result[7] else '-':^10}|")
        for i in range(itens_per_page - len(results)):
            print(f"|{'-':^34}"
                  f"|{'-':^10}"
                  f"|{'-':^10}"
                  f"|{'-':^10}"
                  f"|{'-':^20}"
                  f"|{'-':^3}"
                  f"|{'-':^10}"
                  f"|{'-':^10}|")
        print("\n\t  ", end="")
        for i in range(pages + 1):
            print(i, end=' ')
        print("\n", "\t", " " * page * 2, '^')
        print("Pressione <- ou -> para navegar entre os locais")
        print("Pressione s para confirmar a seleção de um local")
        print("Pressione x para cancelar e sair da listagem")
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
        print(f"{bcolors.FAIL}Não foi possível listar as notificações... "
              f"Tente novamente. {e}{bcolors.ENDC}")
        input()
    finally:
        if dao:
            dao.close()
    return page
