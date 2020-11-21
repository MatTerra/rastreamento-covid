import os
from getpass import getpass

from utils.entity.usuario import Usuario
from utils.colors import bcolors


def authenticate(email: str, password: str) -> (bool, Usuario):
    return True, Usuario()


def login() -> Usuario:
    """ Authenticate a user

    :param email: email of the user to authenticate
    :param password: hash of the password from the user to authenticate
    :return: The user id
    """
    logged_in = False
    user = None
    while not logged_in:
        print("Bem-vindo ao sistema de rastreamento de Covid."
              " Por favor se autentique:")
        email = input("Email: ")
        password = getpass("Password: ")
        logged_in, user = authenticate(email=email, password=password)
        if not logged_in:
            os.system("clear")
            print(bcolors.FAIL+"As credenciais fornecidas não são conhecidas "
                               "pelo sistema, tente novamente!"+bcolors.ENDC)
    return user
