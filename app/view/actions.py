import os
import sys
from getpass import getpass

from utils.colors import bcolors
from utils.database.usuarioDAO import UsuarioDAO
from utils.entity.email import Email
from utils.entity.usuario import Usuario
from utils import authentication


def sair():
    os.system("clear")
    print(bcolors.OKGREEN+"Obrigado por utilizar o sistema de rastreamento "
                          "do COVID"+bcolors.ENDC)
    sys.exit(0)


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
        return authentication.signup(name, last_name, password, consent, [email])
    except KeyboardInterrupt:
        os.system("clear")
        print(
            bcolors.WARNING + "Cancelando criação de conta!" + bcolors.ENDC)
        return None


actions = {"0": {"name": "Sair", "function": sair}}
