from os import system

from utils.entity.usuario import Usuario
from utils.controller.hospitais import view_hospitais

def hospitais_menu(user: Usuario):
    pagina = 0
    while pagina != 'x':
        system("clear")
        pagina = view_hospitais(pagina)
    return user