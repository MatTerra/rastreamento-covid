from datetime import date
from os import system

from getch import getch

from utils.colors import bcolors
from utils.controller.emissor import select_emissor
from utils.database.diagnosticoDAO import DiagnosticoDAO
from utils.entity.diagnostico import Diagnostico
from utils.entity.emissor import Emissor
from utils.entity.usuario import Usuario
from utils.input import read_nullable_date, read_simple_date

itens_per_page = 2


def select_diagnostico(page: int, user: Usuario) -> Diagnostico:
    dao = None
    try:
        dao = DiagnosticoDAO()
        system("clear")
        total, diagnosticos = dao.get_all(length=itens_per_page,
                                          offset=page * itens_per_page,
                                          filters={"usuario": user.id_})
        pages = (total - 1) // itens_per_page
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Selecione o diagnóstico:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'ID Usuário':^32}|{'Emissor':^30}|{'Dia Exame':^9}"
              f"|{'In. Sint.':^9}|{'Fim Sint.':^9}|{'Fim Diag.':^9}|"
              f"{bcolors.ENDC}")
        for diagnostico in diagnosticos:
            print(f"|{diagnostico.usuario.id_:^32}|"
                  f"{diagnostico.emissor.nome:^30}"
                  f"|{diagnostico.data_exame.strftime('%d/%m/%y'):>9}|"
                  f"{diagnostico.data_inicio_sintomas.strftime('%d/%m/%y'):>9}|"
                  f"{diagnostico.data_fim_sintomas.strftime('%d/%m/%y') if diagnostico.data_fim_sintomas else '-':>9}|"
                  f"{diagnostico.data_recuperacao.strftime('%d/%m/%y') if diagnostico.data_recuperacao else '-':>9}|")
        for i in range(itens_per_page - len(diagnosticos)):
            print(f"|{'-':^32}|{'-':^30}|{'-':^9}"
                  f"|{'-':^9}|{'-':^9}|{'-':^9}|")
        print("\n\t  ", end="")
        for i in range(pages + 1):
            print(i, end=' ')
        print("\n", "\t", " " * page * 2, '^')
        print("Pressione -> para próxima página")
        print("Pressione <- para a página anterior")
        print("Pressione x para sair da listagem")
        print("Use o índice para selecionar")
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
            elif option in [str(i) for i in range(len(diagnosticos))]:
                return diagnosticos[int(option)]
        system("clear")
        return option
    except Exception as e:
        print(e)
        input()
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os diagnosticos... "
              f"Tente novamente. {bcolors.ENDC}")
    finally:
        if dao:
            dao.close()



def view_diagnosticos(page: int):
    dao = None
    try:
        dao = DiagnosticoDAO()
        system("clear")
        total, diagnosticos = dao.get_all(length=itens_per_page,
                                          offset=page * itens_per_page)
        pages = (total - 1) // itens_per_page
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Diagnósticos:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'ID Usuário':^32}|{'Emissor':^30}|{'Dia Exame':^9}"
              f"|{'In. Sint.':^9}|{'Fim Sint.':^9}|{'Fim Diag.':^9}|"
              f"{bcolors.ENDC}")
        for diagnostico in diagnosticos:
            print(f"|{diagnostico.usuario.id_:^32}|"
                  f"{diagnostico.emissor.nome:^30}"
                  f"|{diagnostico.data_exame.strftime('%d/%m/%y'):>9}|"
                  f"{diagnostico.data_inicio_sintomas.strftime('%d/%m/%y'):>9}|"
                  f"{diagnostico.data_fim_sintomas.strftime('%d/%m/%y') if diagnostico.data_fim_sintomas else '-':>9}|"
                  f"{diagnostico.data_recuperacao.strftime('%d/%m/%y') if diagnostico.data_recuperacao else '-':>9}|")
        for i in range(itens_per_page - len(diagnosticos)):
            print(f"|{'-':^32}|{'-':^30}|{'-':^9}"
                  f"|{'-':^9}|{'-':^9}|{'-':^9}|")
        print("\n\t  ", end="")
        for i in range(pages + 1):
            print(i, end=' ')
        print("\n", "\t", " " * page * 2, '^')
        print("Pressione -> para próxima página")
        print("Pressione <- para a página anterior")
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
        print(e)
        input()
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar os diagnosticos... "
              f"Tente novamente. {bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def atualizar_diagnostico(user: Usuario):
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos atualizar um diagnóstico!"
          f"{bcolors.ENDC}\n")
    diagnostico = 0
    while not isinstance(diagnostico, Diagnostico):
        diagnostico: Diagnostico = select_diagnostico(diagnostico, user)
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Por favor preencha os dados abaixo:"
          f"{bcolors.ENDC}\n")
    if not diagnostico.data_fim_sintomas:
        diagnostico.data_fim_sintomas = read_nullable_date(
            "Data de fim dos sintomas")
    if not diagnostico.data_recuperacao:
        diagnostico.data_recuperacao = read_nullable_date("Data final do caso")

    dao = None
    try:
        dao = DiagnosticoDAO()
        dao.update(diagnostico)
        system("clear")
        print(f"{bcolors.OKGREEN}Diagnóstico atualizado!"
              f"{bcolors.ENDC}")
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível atualizar o diagnóstico... "
              f"Tente novamente. {e}"
              f"{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()




def create_diagnostico(user: Usuario):
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos cadastrar um novo diagnóstico!"
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Por favor preencha os dados abaixo:"
          f"{bcolors.ENDC}\n")
    exam_date = read_simple_date("Data do exame")
    symptoms_date = read_simple_date("Data de início dos sintomas")
    end_symptoms_date = read_nullable_date("Data de fim dos sintomas")
    recovery_date = read_nullable_date("Data final do caso")

    emissor = 0
    while not isinstance(emissor, Emissor):
        emissor = select_emissor(emissor)

    dao = None
    try:
        dao = DiagnosticoDAO()
        diagnostico = Diagnostico(usuario=user, emissor=emissor,
                                  data_exame=exam_date,
                                  data_inicio_sintomas=symptoms_date,
                                  data_fim_sintomas=end_symptoms_date,
                                  data_recuperacao=recovery_date)
        dao.create(diagnostico)
        system("clear")
        print(
            f"{bcolors.OKGREEN}Diagnóstico cadastrado com sucesso!"
            f"{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível guardar este diagnóstico... "
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()
