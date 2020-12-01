from os import system
from getch import getch
from utils.colors import bcolors
from datetime import datetime, date

from utils.database.sintomaDAO import SintomaDAO
from utils.database.caso_sintomaDAO import CasoSintomaDAO

from utils.entity.usuario import Usuario
from utils.entity.caso_sintoma import CasoSintoma
from utils.input import read_simple_string


itens_per_page = 5
datetime_format = "%d/%m/%y"

def select_sintoma():
    dao = None
    try:
        page = 0
        selected_sintoma = 0
        while True:
            dao = SintomaDAO()
            system("clear")
            # Get +1 to make it possible to change to the next page
            total, sintomas = dao.get_all(length=itens_per_page,
                                              offset=page*itens_per_page)

            if total==0:
                print(f"{bcolors.WARNING}Não há sintomas disponíveis para registro\n"
                    f"Pressione qualquer tecla para continuar.{bcolors.ENDC}")
                getch()
                system("clear")
                return -1

            pages = (total-1) // itens_per_page
            if pages < 0:
                pages = 0

            if page > pages:
                system("clear")
                print(f"{bcolors.WARNING}A página {page} não está disponível,"
                    f" mostrando a última página disponível.{bcolors.ENDC}")
            print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
                f"Selecione um sintoma:"
                f"{bcolors.ENDC}\n")
            print(f"{bcolors.OKCYAN}"
                f"|{'Descrição':^30}|{'Risco':^10}|"
                f"{bcolors.ENDC}")
            for idx, sintoma in enumerate(sintomas):
                if idx == selected_sintoma:
                    print(f"|>{sintoma.descricao[:30]:^30}"
                        f"|{sintoma.risco:^10}|"
                        )
                else:
                    print(f"| {sintoma.descricao[:30]:^30}"
                        f"|{sintoma.risco:^10}|"
                        )
            for i in range(itens_per_page - len(sintomas)):
                print(f"|{'-':^30}|{'-':^10}")
            print("\n\t  ", end="")
            for i in range(pages+1):
                print(i, end=' ')
            print("\n", "\t", " "*page*2, '^')
            print("Pressione <- ou -> para navegar entre os sintomas")
            print("Pressione s para confirmar a seleção de um sintoma")
            print("Pressione x para cancelar e sair da listagem")
            option=''
            while option != 'x' and option != 's':
                option = getch()
                if option == '[':
                    option = getch()
                    if option == "C":
                        system("clear")
                        if page == pages and selected_sintoma == total%itens_per_page-1:
                            break
                        if selected_sintoma == itens_per_page-1:
                            page = (page + 1) % (pages+1) if pages > 0 else 0
                        selected_sintoma = (selected_sintoma + 1) % itens_per_page
                        break
                    if option == "D":
                        system("clear")
                        if page == 0 and selected_sintoma == 0:
                            break
                        if selected_sintoma == 0:
                            page = (page - 1) % (pages+1) if pages > 0 else 0
                        selected_sintoma = (selected_sintoma - 1) % itens_per_page
                        break
            if option == 's':
                system("clear")
                return sintomas[selected_sintoma].id_
            elif option == 'x':
                system("clear")
                return -1
            if dao:
                dao.close()
    except Exception as e:
        system("clear")
        raise e
    finally:
        if dao:
            dao.close()


def create_caso_sintoma(user: Usuario):
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos cadastrar um novo sintoma"
          f"{bcolors.ENDC}\n")
    
    try:
        selected_sintoma = select_sintoma()
        if selected_sintoma == -1:
            return
    except Exception as e:
        print(f"{bcolors.FAIL}Não foi possível listar os sintomas... "
              f"Tente novamente. {str(e)}{bcolors.ENDC}")
        return

    print("Por favor, responda às perguntas: (caso queira, aperte CTRL + C para cancelar)")
    inicio_sintoma: date
    while True:
        print(f"{bcolors.BOLD}"
            f"Quando você começou a sentir esse sintoma?\n"
            f"(digite uma data no formato dd/mm/yy. Exemplo: 03/02/20)"
            f"{bcolors.ENDC}\n")
        try:
            inicio_sintoma = datetime.strptime( input(">> ").strip(), datetime_format)
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(f"{bcolors.WARNING}"
                f"Ops, a data que você digitou está no formato errado.\nPor favor, digite novamente conforme o formato dado."
                f"{bcolors.ENDC}\n")
        else:
            break

    final_sintoma: date
    while True:
        print("Você ainda sente esse sintoma?(s/n)")
        option = input(">> ")
        if option == 's':
            final_sintoma = None
            break
        elif option == "n":
            while True:
                print(f"{bcolors.BOLD}"
                    f"Quando você parou de sentir esse sintoma?\n"
                    f"(digite uma data no formato dd/mm/yy. Exemplo: 03/02/20)"
                    f"{bcolors.ENDC}\n")
                try:
                    final_sintoma = datetime.strptime(input(">> ").strip(), datetime_format)

                    if final_sintoma < inicio_sintoma:
                        print(f"{bcolors.WARNING}"
                        f"Ops, a data que você digitou é anterior à data de inicio.\nPor favor, digite novamente uma data válida."
                        f"{bcolors.ENDC}\n")
                except KeyboardInterrupt:
                    return
                except:
                    print(f"{bcolors.WARNING}"
                        f"Ops, a data que você digitou está no formato errado.\nPor favor, digite novamente conforme o formato dado."
                        f"{bcolors.ENDC}\n")
                else:
                    break
            break
        else:
            print("Ops, por favor, digite apenas 's' ou 'n'.")

    caso_sintoma_dao = None
    try:
        caso_sintoma_dao = CasoSintomaDAO()
        caso_sintoma = CasoSintoma(usuario_id_=user.id_, sintoma_id_=selected_sintoma, inicio=inicio_sintoma, final=final_sintoma)
        caso_sintoma_dao.create(caso_sintoma)
        system("clear")
        print(f"{bcolors.OKGREEN}Ocorrência de sintoma cadastrada.{bcolors.ENDC}")
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível guardar esta ocorrência..."
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if caso_sintoma_dao:
            caso_sintoma_dao.close()
    
# Lista ocorrencias de um sintoma
# para um determinado usuario
def view_caso_sintoma(page: int, user: Usuario):
    dao = None
    try:
        dao = CasoSintomaDAO()
        system("clear")
        total, casosintomas = dao.get_all(length=itens_per_page,
                                        offset=page*itens_per_page,
                                        filters={
                                                "usuario_id_": user.id_
                                            })
        pages = (total-1)//itens_per_page
        if pages < 0:
            pages = 0
        if page > pages:
            system("clear")
            print(f"{bcolors.WARNING}A página {page} não está disponível,"
                  f" mostrando a última página disponível.{bcolors.ENDC}")
            return pages
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
              f"Suas ocorrências de sintomas:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Sintoma':^30}|{'Inicio':^20}|{'Final':^20}|"
              f"{bcolors.ENDC}")
        sintoma_dao = SintomaDAO()
        for casosintoma in casosintomas:
            sintoma = sintoma_dao.get(casosintoma.sintoma_id_).descricao
            final = casosintoma.final.strftime(datetime_format) \
                        if casosintoma.final is not None else "ainda apresentado"
            print(f"|{sintoma[:30]:^30}|{casosintoma.inicio.strftime(datetime_format):^20}"
                  f"|{final:^20}|")
        sintoma_dao.close()
        for i in range(itens_per_page - len(casosintomas)):
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
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível listar as suas ocorrências de sintomas... "
              f"Tente novamente.{str(e)}{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


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