import os
import sys
from getpass import getpass

from utils.colors import bcolors
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


def signup():
    pass


actions = {"0": {"name": "Sair", "function": sair}}
