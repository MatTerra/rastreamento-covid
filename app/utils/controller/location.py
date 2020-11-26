from os import system

from utils.entity.local import Local
from utils.input import read_simple_string


def create_local():
    system("clear")
    print("Vamos cadastrar um novo local!")
    name = read_simple_string("Nome do local:")

def search_local():
    pass