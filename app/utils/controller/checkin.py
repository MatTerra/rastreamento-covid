from os import system
from datetime import datetime

from getch import getch

from utils.colors import bcolors
from utils.database.checkinDAO import CheckinDAO
from utils.database.localDAO import LocalDAO
from utils.entity.checkin import Checkin
from utils.entity.usuario import Usuario
from utils.input import read_simple_string

itens_per_page = 5
datetime_format = "%d/%m/%y-%H:%M"

def select_local_checkin():
    dao = None
    try:
        page = 0
        selected_local = 0
        while True:
            dao = LocalDAO()
            system("clear")
            # Get +1 to make it possible to change to the next page
            total, locais = dao.get_all(length=itens_per_page,
                                              offset=page*itens_per_page)

            if total==0:
                print(f"{bcolors.WARNING}Não há locais disponíveis para checkin\n"
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
                f"Selecione um local:"
                f"{bcolors.ENDC}\n")
            print(f"{bcolors.OKCYAN}"
                f"|{'Nome':^30}|{'Latitude':^20}|{'Longitude':^20}|"
                f"{bcolors.ENDC}")
            for idx, local in enumerate(locais):
                if idx == selected_local:
                    print(f"|{bcolors.UNDERLINE}{local.nome:^30}{bcolors.ENDC}"
                        f"|{local.latitude:^20}"
                        f"|{local.longitude:^20}|"
                        )
                else:
                    print(f"|{local.nome:^30}|{local.latitude:^20}"
                        f"|{local.longitude:^20}|")
            for i in range(itens_per_page - len(locais)):
                print(f"|{'-':^30}|{'-':^20}"
                    f"|{'-':^20}|")
            print("\n\t  ", end="")
            for i in range(pages+1):
                print(i, end=' ')
            print("\n", "\t", " "*page*2, '^')
            print("Pressione <- ou -> para navegar entre os locais")
            print("Pressione s para confirmar a seleção de um local")
            print("Pressione x para cancelar e sair da listagem")
            option=''
            while option != 'x' and option != 's':
                option = getch()
                if option == '[':
                    option = getch()
                    if option == "C":
                        system("clear")
                        if page == pages and selected_local == total%itens_per_page-1:
                            break
                        if selected_local == itens_per_page-1:
                            page = (page + 1) % (pages+1) if pages > 0 else 0
                        selected_local = (selected_local + 1) % itens_per_page
                        break
                    if option == "D":
                        system("clear")
                        if page == 0 and selected_local == 0:
                            break
                        if selected_local == 0:
                            page = (page - 1) % (pages+1) if pages > 0 else 0
                        selected_local = (selected_local - 1) % itens_per_page
                        break
            if option == 's':
                system("clear")
                return locais[selected_local].id_
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


def create_checkin(user: Usuario):
    system("clear")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos cadastrar um novo checkin!"
          f"{bcolors.ENDC}\n")
    
    try:
        selected_local = select_local_checkin()
        if selected_local == -1:
            return
    except Exception as e:
        print(f"{bcolors.FAIL}Não foi possível listar os locais... "
              f"Tente novamente. {str(e)}{bcolors.ENDC}")
        return

    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Por favor preencha os dados abaixo:"
          f"{bcolors.ENDC}\n")

    inicio_checkin: datetime
    while True:
        print(f"{bcolors.BOLD}"
            f"Quando você entrou nesse lugar?\n"
            f"(digite uma data no formato dd/mm/yy HH:MM. Exemplo: 03/02/20-16:05)"
            f"{bcolors.ENDC}\n")
        try:
            inicio_checkin = datetime.strptime( input(">> ").strip(), datetime_format)
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(f"{bcolors.WARNING}"
                f"Ops, a data que você digitou está no formato errado.\nPor favor, digite novamente conforme o formato dado."
                f"{bcolors.ENDC}\n")
        else:
            break

    final_checkin: datetime
    while True:
        print(f"{bcolors.BOLD}"
            f"Quando você saiu desse lugar?\n"
            f"(digite uma data no formato dd/mm/yy HH:MM. Exemplo: 03/02/20-16:05)"
            f"{bcolors.ENDC}\n")
        try:
            final_checkin = datetime.strptime(input(">> ").strip(), datetime_format)

            if final_checkin < inicio_checkin:
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

    dao = None
    try:
        dao = CheckinDAO()
        checkin = Checkin(inicio=inicio_checkin, final=final_checkin, id_usuario=user.id_, local_id_=selected_local)
        dao.create(checkin)
        system("clear")
        print(f"{bcolors.OKGREEN}Checkin cadastrado com sucesso!{bcolors.ENDC}")
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível guardar este checkin... {str(e)}"
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def view_checkins(page: int, user: Usuario):
    dao = None
    try:
        dao = CheckinDAO()
        system("clear")
        total, checkins = dao.get_all(length=itens_per_page,
                                        offset=page*itens_per_page,
                                        filters={
                                                "id_usuario": user.id_
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
              f"Seus checkins:"
              f"{bcolors.ENDC}\n")
        print(f"{bcolors.OKCYAN}"
              f"|{'Local':^30}|{'Inicio':^20}|{'Final':^20}|"
              f"{bcolors.ENDC}")
        local_dao = LocalDAO()
        for checkin in checkins:
            nome_local = local_dao.get(checkin.local_id_).nome
            print(f"|{nome_local:^30}|{checkin.inicio.strftime(datetime_format):^20}"
                  f"|{checkin.final.strftime(datetime_format):^20}|")
        local_dao.close()
        for i in range(itens_per_page - len(checkins)):
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
        print(f"{bcolors.FAIL}Não foi possível listar os checkins... "
              f"Tente novamente. {str(e)}{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()
