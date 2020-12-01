from os import system

from utils.controller.notificacao import view_notificacao
from utils.entity.usuario import Usuario


def notificacao_menu(user: Usuario) -> Usuario:
    pagina = 0
    while pagina != 'x':
        system("clear")
        pagina = view_notificacao(pagina, user)
    return user