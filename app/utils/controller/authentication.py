from getpass import getpass
from os import system

from utils import authentication
from utils.colors import bcolors
from utils.input import read_simple_string
from utils.entity.usuario import Usuario


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
    print(f"{bcolors.WARNING}"
          f"Por favor se autentique:"
          f"{bcolors.ENDC}\n")
    email = read_simple_string("Email")
    password = getpass(f"{bcolors.BOLD} Password: {bcolors.ENDC}")
    user = authentication.login(email=email, password=password)
    if not user:
        system("clear")
        print(
            bcolors.FAIL + "As credenciais fornecidas não são conhecidas "
                           "pelo sistema, tente novamente!" + bcolors.ENDC)
    return user


def signup() -> Usuario:
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}"
          f"Vamos criar sua conta! Pressione CTRL + C para cancelar."
          f"{bcolors.ENDC}\n")
    try:
        print(f"{bcolors.HEADER}{bcolors.BOLD}"
              f"Por favor preencha os dados abaixo:"
              f"{bcolors.ENDC}\n")
        name = read_simple_string("Primeiro nome")
        last_name = read_simple_string("Último nome")
        consent = get_consent()
        if not consent:
            system("clear")
            print(
                bcolors.FAIL + "Você deve concordar com os termos para criar "
                               "uma conta!" + bcolors.ENDC)
            return None
        password = get_passwd()
        email = read_simple_string("Email")
        return authentication.signup(name, last_name, password, consent,
                                     [email])
    except KeyboardInterrupt:
        system("clear")
        print(
            bcolors.WARNING + "Cancelada criação de conta!" + bcolors.ENDC)
        return None
