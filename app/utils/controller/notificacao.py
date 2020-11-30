from os import system

from getch import getch

from utils.colors import bcolors
from utils.database.notificacaoDAO import NotificacaoDAO
from utils.entity.notificacao import Notificacao
from utils.entity.usuario import Usuario

itens_per_page = 5
datetime_format = "%d/%m/%y-%H:%M"


def view_notificacao(page: int, user: Usuario) -> Usuario:
    dao = None
    try:
        dao = NotificacaoDAO()
        system("clear")
        dao.database.query("SELECT checkin_id_, notificacao_recebida, "
                           "local_nome, checkin_risco, checkin_inicio, "
                           "checkin_final "
                           "FROM notificacao_view "
                           "WHERE checkin_id_usuario=%s LIMIT %s OFFSET %s;",
                           (user.id_, itens_per_page, (page * itens_per_page)))
        results = dao.database.get_results()
        dao.database.query("SELECT COUNT(checkin_id_) "
                           "FROM notificacao_view "
                           "WHERE checkin_id_usuario=%s;",
                           (user.id_,))
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
              f"Suas notificações:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Local':^30}|{'Risco':^5}|{'Inicio':^20}|{'Final':^20}|"
              f"{bcolors.ENDC}")
        for result in results:
            notificacao = Notificacao(*result[:2])
            if not notificacao.recebida:
                notificacao.recebida = True
                dao.update(notificacao)
            print(f"|{result[2]:^30}|{result[3]:^5}|"
                  f"{result[4].strftime(datetime_format):^20}"
                  f"|{result[5].strftime(datetime_format):^20}|")
        for i in range(itens_per_page - len(results)):
            print(f"|{'-':^30}|{'-':^5}|{'-':^20}"
                  f"|{'-':^20}|")
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
