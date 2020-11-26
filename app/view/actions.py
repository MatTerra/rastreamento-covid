import os
import sys
from getpass import getpass

from utils.colors import bcolors
from utils.database.emailDAO import EmailDAO
from utils.database.usuarioDAO import UsuarioDAO
from utils.entity.email import Email
from utils.entity.usuario import Usuario
from utils import authentication


# -------------- BEGIN Utilities for input ---------------------------------- #
def read_simple_string(prop_name: str):
    result = ""
    while result == "":
        result = input(f" {prop_name}: ")
        if result == "":
            print(bcolors.WARNING + f"Você deve informar o(a) "
                                    f"{prop_name.lower()}!"
                  + bcolors.ENDC)
    return result


def get_consent():
    print("Seus dados serão utilizados para fazer o rastreamento do contato "
          "de infectados pelo COVID. O seu anonimato será preservado dentro "
          "do possível e não há nenhuma garantia de preservação do anonimato.")
    consent = ""
    while consent.lower() not in ['s', 'n']:
        consent = input("Você concorda com os termos acima? (s/n)")
    return consent.lower() == 's'


def get_passwd():
    passwd = ""
    while len(passwd) < 6:
        passwd = getpass(" Senha:")
        if len(passwd) >= 6:
            break
        print(bcolors.FAIL + "Sua senha deve ter ao menos 6 caracteres."
                  + bcolors.ENDC)
    confirm_passwd = ""
    while confirm_passwd != passwd:
        confirm_passwd = getpass(" Confirme sua senha:")
        if confirm_passwd == passwd:
            break
        print(bcolors.FAIL + "As senhas não são iguais!" + bcolors.ENDC)
    return passwd


# -------------- END Utilities for input ------------------------------------ #


# -------------- LEAVE ------------------------------------------------------ #
def sair():
    os.system("clear")
    print(bcolors.OKGREEN+"Obrigado por utilizar o sistema de rastreamento "
                          "do COVID"+bcolors.ENDC)
    sys.exit(0)

# -------------- END LEAVE -------------------------------------------------- #


# -------------- BEGIN Authentication --------------------------------------- #
def logout(user) -> Usuario:
    print(bcolors.OKGREEN + "Você foi deslogado!" + bcolors.ENDC)
    del user
    return None


def login() -> Usuario:
    """ Authenticate a user

    :param email: email of the user to authenticate
    :param password: hash of the password from the user to authenticate
    :return: The user id
    """
    print("Por favor se autentique:")
    email = input("Email: ")
    password = getpass("Password: ")
    user = authentication.login(email=email, password=password)
    if not user:
        os.system("clear")
        print(
            bcolors.FAIL + "As credenciais fornecidas não são conhecidas "
                           "pelo sistema, tente novamente!" + bcolors.ENDC)
    return user


def signup() -> Usuario:
    print("Vamos criar sua conta! Pressione CTRL + C para cancelar.")
    try:
        print("Por favor preencha os dados abaixo:")
        name = read_simple_string("Primeiro nome")
        last_name = read_simple_string("Último nome")
        consent = get_consent()
        if not consent:
            os.system("clear")
            print(bcolors.FAIL+"Você deve concordar com os termos para criar "
                               "uma conta!"+bcolors.ENDC)
            return None
        password = get_passwd()
        email = read_simple_string("Email")
        return authentication.signup(name, last_name, password, consent,
                                     [email])
    except KeyboardInterrupt:
        os.system("clear")
        print(
            bcolors.WARNING + "Cancelando criação de conta!" + bcolors.ENDC)
        return None

# -------------- END Authentication ----------------------------------------- #


# -------------- BEGIN Profile ---------------------------------------------- #
def add_email(user: Usuario):
    new_email_addr = read_simple_string("Insira o novo email: ")
    new_email = Email(email=new_email_addr,
                      usuario_id_=user.id_, primario=False)

    dao = None
    try:
        dao = EmailDAO()
        dao.create(new_email)
        os.system("clear")
        print(f"{bcolors.OKGREEN}Novo email inserido com sucesso!{bcolors.ENDC}")
    except:
        os.system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao inserir o novo email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()

    user.emails.append(new_email)


def remove_email(user: Usuario):
    print("Qual email você gostaria de remover?")
    print("\nEmails:")
    for index, email in enumerate(user.emails):
        print(f"\t{index} - {email.email}{'*' if email.primario else ''}")

    choice = -1
    while choice not in range(len(user.emails)):
        try:
            choice = int(input(">> "))
        except:
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")
            pass

    email = user.emails.pop(choice)

    dao = None
    try:
        dao = EmailDAO()
        dao.remove(email)
        if email.primario:
            user.emails[0].primario = True
            dao.update(user.emails[0])
        os.system("clear")
        print(
            f"{bcolors.OKGREEN}Email removido com sucesso!{bcolors.ENDC}")
    except:
        os.system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao remover o email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()




def change_birthday(user: Usuario):
    pass


def change_name(user: Usuario):
    pass


def edit_profile(user: Usuario) -> Usuario:
    print("O que você gostaria de editar?")
    print("\t0 - Adicionar email secundário")
    print("\t1 - Remover email")
    print("\t2 - Data de nascimento")
    print("\t3 - Nome\n")
    choice = ""
    while choice.lower() not in ["0", "1", "2", "3"]:
        choice = input(">> ")
    if choice == '0':
        os.system("clear")
        add_email(user)
    elif choice == '1':
        os.system("clear")
        remove_email(user)
    elif choice == '2':
        change_birthday(user)
    elif choice == '3':
        change_name(user)
    return user


def view_profile(user: Usuario) -> Usuario:
    print("Perfil do Usuário\n")
    print(f"\tNome:\t\t\t{user.primeiro_nome} {user.ultimo_nome}")
    print(f"\tData de nascimento:\t{user.data_nascimento}")
    print(f"\tEmails:")
    for email in user.emails:
        print(f"\t\t{'*' if email.primario else '-'} {email.email}")
    print("")
    print("\t(*) Email primário")
    print("")
    choice = ""
    while choice.lower() not in ["s", "n"]:
        choice = input("Gostaria de alterar algum dado? [s/N]\n>> ")
    if choice == 's':
        os.system("clear")
        return edit_profile(user)
    os.system("clear")
    return edit_profile(user)

# -------------- END Profile ------------------------------------------------ #


actions = {"p": {"name": "Meu perfil", "function": view_profile},
           "x": {"name": "Sair", "function": logout}}
