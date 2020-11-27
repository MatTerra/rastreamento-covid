from datetime import date, datetime
from os import system

from utils.colors import bcolors
from utils.input import read_simple_string
from utils.database.emailDAO import EmailDAO
from utils.database.usuarioDAO import UsuarioDAO
from utils.database.telefoneDAO import TelefoneDAO
from utils.entity.email import Email
from utils.entity.usuario import Usuario
from utils.entity.telefone import Telefone


def add_email(user: Usuario):
    new_email_addr = read_simple_string("Novo email")
    new_email = Email(email=new_email_addr,
                      usuario_id_=user.id_, primario=False)

    dao = None
    try:
        dao = EmailDAO()
        dao.create(new_email)
        system("clear")
        print(
            f"{bcolors.OKGREEN}Novo email inserido com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao inserir o novo email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()

    user.emails.append(new_email)


def remove_email(user: Usuario):
    print(f"{bcolors.HEADER}{bcolors.BOLD}"
          f"Qual email você gostaria de remover?"
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.BOLD}Emails:{bcolors.ENDC}")
    for index, email in enumerate(user.emails):
        print(f"\t{index} - {email.email}{'*' if email.primario else ''}")

    choice = -1
    while choice not in range(len(user.emails)):
        try:
            choice = int(input(">> "))
        except:
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")

    email = user.emails.pop(choice)

    dao = None
    try:
        dao = EmailDAO()
        dao.remove(email)
        if email.primario:
            user.emails[0].primario = True
            dao.update(user.emails[0])
        system("clear")
        print(
            f"{bcolors.OKGREEN}Email removido com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao remover o email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()

def add_telefone(user: Usuario):
    new_telefone_number = read_simple_string("Novo telefone")
    new_telefone = Telefone(telefone=new_telefone_number, usuario_id_=user.id_)

    dao = None
    try:
        dao = TelefoneDAO()
        dao.create(new_telefone)
        system("clear")
        print(
            f"{bcolors.OKGREEN}Novo telefone inserido com sucesso!{bcolors.ENDC}")
    except Exception as e:
        system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao inserir o novo telefone... "
              f"Por favor tente novamente.{bcolors.ENDC}")
        print(str(e))
    finally:
        if dao:
            dao.close()

    user.telefones.append(new_telefone)

def change_birthday(user: Usuario):
    birthday = ""
    while not isinstance(birthday, date):
        date_input = read_simple_string(
            "Data de nascimento (dd/mm/AAAA)")
        try:
            birthday = datetime.strptime(date_input, "%d/%m/%Y")
            if birthday.timestamp() > datetime.now().timestamp():
                birthday = ""
                raise ValueError
        except ValueError:
            print(f"{bcolors.FAIL}Data inválida!{bcolors.ENDC}")

    dao = None
    try:
        user.data_nascimento = birthday
        dao = UsuarioDAO()
        dao.update(user)
        system("clear")
        print(f"{bcolors.OKGREEN}Data de nascimento atualizada"
              f" com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível atualizar a data de"
              f" nascimento... Tente novamente mais tarde.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def view_profile(user: Usuario) -> Usuario:
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}"
          f"Perfil do usuário:"
          f"{bcolors.ENDC}\n")
    print(f"{bcolors.BOLD}\tNome:{bcolors.ENDC}"
          f"\t\t\t{user.primeiro_nome} {user.ultimo_nome}")
    print(
        f"\t{bcolors.BOLD}Data de nascimento:{bcolors.ENDC}"
        f"\t{user.data_nascimento.strftime('%d/%m/%Y')}")
    print(f"\t{bcolors.BOLD}Emails:{bcolors.ENDC}")
    for email in user.emails:
        print(f"\t\t{f'{bcolors.BOLD}*' if email.primario else '-'} "
              f"{email.email}{bcolors.ENDC}")
    print("")
    print("\t(*) Email primário")
    print("")
    print("Pressione qualquer tecla para sair...")
    input()
    system("clear")
    return user
