import os

from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.colors import bcolors
from utils.controller import actions
from utils.entity.usuario import Usuario


def main_menu(user: Usuario) -> str:
    dao = None
    try:
        dao = GenericSQLDAO(database_type=PostgreSQLHelper)
        dao.database.query("SELECT COUNT(checkin_id_) FROM notificacao_view "
                           "WHERE checkin_id_usuario=%s "
                           "AND notificacao_recebida=FALSE;",
                           [user.id_])
        notificacoes = dao.database.get_results()[0][0]
    except:
        pass
    finally:
        if dao:
            dao.close()
    if notificacoes > 0:
        print(f"{bcolors.WARNING}{bcolors.BOLD} Você tem "
              f"{notificacoes} notificações!{bcolors.ENDC}")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"O que você gostaria de fazer?"
          f"{bcolors.ENDC}\n")
    for key, action in actions.items():
        print(f"\t{key} - {action.get('name', '...')}")
    action = input(">> ").strip()
    if action not in actions.keys():
        raise ValueError(action)
    return action


def authentication_menu() -> str:
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}"
          f"Bem-vindo ao sistema de rastreamento de Covid."
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"O que você gostaria de fazer?"
          f"{bcolors.ENDC}\n")
    print("\tl - Login")
    print("\tc - Cadastro")
    print("\tx - Sair")
    escolha = input(" >> ").strip()
    os.system("clear")
    if escolha not in ["x", "l", "c"]:
        raise ValueError(escolha)
    return escolha
